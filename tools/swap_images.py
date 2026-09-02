import sys,zipfile,shutil,os
sys.path.insert(0,'tools')
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A='{http://schemas.openxmlformats.org/drawingml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
CT='{http://schemas.openxmlformats.org/package/2006/content-types}'
for k,v in [('w',W),('a',A),('r',R)]: ET.register_namespace(k,v[1:-1])

NEW={'partie-1.png':'partie-1.jpg','partie-2.png':'partie-2.jpg','partie-3.png':'partie-3.jpg',
     'partie-4.png':'partie-4.jpg','partie-5.png':'partie-5.jpg','partie-6.png':'partie-6.jpg',
     'annexes.png':'annexes.jpg'}

def process(path):
    z=zipfile.ZipFile(path); names=list(z.namelist()); raw={n:z.read(n) for n in names}
    ct=ET.fromstring(raw['[Content_Types].xml'])
    if not any(e.get('Extension')=='jpg' for e in ct if e.tag==CT+'Default'):
        d=ET.SubElement(ct,CT+'Default'); d.set('Extension','jpg'); d.set('ContentType','image/jpeg')
    relroot=ET.fromstring(raw['word/_rels/document.xml.rels'])
    n=0
    for rel in relroot:
        t=rel.get('Target') or ''
        base=t.split('/')[-1]
        if base in NEW:
            newbase=NEW[base]
            rel.set('Target','media/'+newbase)
            raw['word/media/'+newbase]=open('images/print/'+newbase,'rb').read()
            old='word/media/'+base
            if old in names: names.remove(old); raw.pop(old,None)
            if 'word/media/'+newbase not in names: names.append('word/media/'+newbase)
            n+=1
    raw['[Content_Types].xml']=ET.tostring(ct,encoding='UTF-8',xml_declaration=True)
    raw['word/_rels/document.xml.rels']=ET.tostring(relroot,encoding='UTF-8',xml_declaration=True)
    tmp=path+'.tmp'
    with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as zo:
        for nm in names: zo.writestr(nm,raw[nm])
    shutil.move(tmp,path)
    print(path,'-> ',n,'images remplacées')

process('L-Entrepreneur-Augmente.docx')
process('The-Augmented-Entrepreneur.docx')
