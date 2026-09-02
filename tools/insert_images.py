import sys,zipfile,copy,shutil,uuid,os
sys.path.insert(0,'tools')
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
RN='http://schemas.openxmlformats.org/package/2006/relationships'
CT='{http://schemas.openxmlformats.org/package/2006/content-types}'
for k,v in [('w',W),('a',A),('r',R)]: ET.register_namespace(k,v[1:-1])

EMU=914400
IMG_W=int(5.9*EMU)                 # 15 cm de large
IMG_H=int(IMG_W*650/1600)

MAP=[  # (fragment PartTitle FR, EN, image, légende FR, légende EN)
 ('Partie I','Part I','partie-1.png',
  'De l’exécution au pilotage : vous cessez de produire, vous décidez.',
  'From doing to piloting: you stop producing, you decide.'),
 ('Partie II','Part II','partie-2.png',
  'Beaucoup d’idées, une seule mérite d’être construite — celle qui est prouvée.',
  'Many ideas, only one worth building — the one that is proven.'),
 ('Partie III','Part III','partie-3.png',
  'Un brief clair en entrée, un résultat vérifiable en sortie.',
  'A clear brief in, a verifiable result out.'),
 ('Partie IV','Part IV','partie-4.png',
  'Un système qui tourne n’est pas un produit : quelqu’un doit pouvoir s’en servir.',
  'A running system is not a product: someone must be able to use it.'),
 ('Partie V','Part V','partie-5.png',
  'Un produit devient une activité quand la valeur circule dans les deux sens.',
  'A product becomes a business when value flows both ways.'),
 ('Partie VI','Part VI','partie-6.png',
  'Déléguer sans disparaître : l’humain reste au centre de la décision.',
  'Delegate without disappearing: the human stays at the centre of the decision.'),
 ('Annexes lecteur','Reader annexes','annexes.png',
  'La boîte à outils : à consulter au besoin, pas à lire d’un trait.',
  'The toolbox: consult it as needed, not a straight read.'),
]

def process(path, lang):
    z=zipfile.ZipFile(path); names=z.namelist(); raw={n:z.read(n) for n in names}
    relroot=ET.fromstring(raw['word/_rels/document.xml.rels'])
    ctroot=ET.fromstring(raw['[Content_Types].xml'])
    if not any(e.get('Extension')=='png' for e in ctroot if e.tag.endswith('Default')):
        d=ET.SubElement(ctroot,CT+'Default'); d.set('Extension','png'); d.set('ContentType','image/png')
    x=ET.fromstring(raw['word/document.xml']); body=x.find(W+'body')

    def parent(el):
        for par in body.iter():
            for i,ch in enumerate(par):
                if ch is el: return par,i
        return None,None
    def paras(): return list(x.iter(W+'p'))
    def text(p): return ''.join(n.text or '' for n in p.iter(W+'t'))
    def style(p):
        s=p.find(W+'pPr/'+W+'pStyle'); return s.get(W+'val') if s is not None else 'Normal'

    capmodel=next(p for p in paras() if style(p)=='Caption')
    n=0
    for frag_fr,frag_en,img,cap_fr,cap_en in MAP:
        frag = frag_fr if lang=='fr' else frag_en
        cap  = cap_fr  if lang=='fr' else cap_en
        part=None
        for p in paras():
            if style(p)=='PartTitle' and text(p).strip().startswith(frag): part=p;break
        if part is None: print('  !! introuvable:',frag); continue
        # ancrer après le sous-titre + le paragraphe d'intro de la partie
        ps=paras(); i=ps.index(part); anchor=part
        for q in ps[i+1:i+4]:
            if style(q) in ('ChapterTitle','PartTitle'): break
            anchor=q
        # media
        data=open('images/print/'+img,'rb').read()
        target='media/'+img
        raw['word/'+target]=data
        if 'word/'+target not in names: names.append('word/'+target)
        rid='rIdImg'+uuid.uuid4().hex[:10]
        rel=ET.SubElement(relroot,'{%s}Relationship'%RN)
        rel.set('Id',rid); rel.set('Type','http://schemas.openxmlformats.org/officeDocument/2006/relationships/image')
        rel.set('Target',target)
        # paragraphe image
        xml=f'''<w:p xmlns:w="{W[1:-1]}" xmlns:r="{R[1:-1]}" xmlns:a="{A[1:-1]}"
 xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
 xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
<w:pPr><w:spacing w:before="240" w:after="60"/><w:jc w:val="center"/></w:pPr>
<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">
<wp:extent cx="{IMG_W}" cy="{IMG_H}"/><wp:effectExtent t="0" r="0" b="0" l="0"/>
<wp:docPr id="{900+n}" name="" descr="" title=""/>
<wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>
<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
<pic:pic><pic:nvPicPr><pic:cNvPr id="0" name="" descr=""/>
<pic:cNvPicPr><a:picLocks noChangeAspect="1" noChangeArrowheads="1"/></pic:cNvPicPr></pic:nvPicPr>
<pic:blipFill><a:blip r:embed="{rid}" cstate="none"/><a:srcRect/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
<pic:spPr bwMode="auto"><a:xfrm><a:off x="0" y="0"/><a:ext cx="{IMG_W}" cy="{IMG_H}"/></a:xfrm>
<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>
</a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'''
        pimg=ET.fromstring(xml)
        pcap=copy.deepcopy(capmodel)
        ts=[t for t in pcap.iter(W+'t')]
        ts[0].text=cap; ts[0].set('{http://www.w3.org/XML/1998/namespace}space','preserve')
        for t in ts[1:]: t.text=''
        par,idx=parent(anchor)
        par.insert(idx+1,pcap); par.insert(idx+1,pimg)
        n+=1
    raw['word/document.xml']=ET.tostring(x,encoding='UTF-8',xml_declaration=True)
    raw['word/_rels/document.xml.rels']=ET.tostring(relroot,encoding='UTF-8',xml_declaration=True)
    raw['[Content_Types].xml']=ET.tostring(ctroot,encoding='UTF-8',xml_declaration=True)
    tmp=path+'.tmp'
    with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as zo:
        for nm in names: zo.writestr(nm,raw[nm])
    shutil.move(tmp,path)
    print(f'{path}: {n} images insérées')

process('L-Entrepreneur-Augmente.docx','fr')
process('The-Augmented-Entrepreneur.docx','en')
