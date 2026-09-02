import sys,zipfile,copy,re,shutil,uuid
sys.path.insert(0,'tools')
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
RN='http://schemas.openxmlformats.org/package/2006/relationships'
ET.register_namespace('w',W[1:-1]); ET.register_namespace('r',R[1:-1])

def norm(u):
    u=u.rstrip('/').replace('https://','').replace('http://','').replace('www.','').lower()
    return re.sub(r'/(fr|en)(/|$)','/',u)

def read(f):
    z=zipfile.ZipFile(f); return z, {n:z.read(n) for n in z.namelist()}

# ---- FR source list ----
zf,rawf=read('L-Entrepreneur-Augmente.docx')
relf={r.get('Id'):r.get('Target') for r in ET.fromstring(rawf['word/_rels/document.xml.rels'])}
xf=ET.fromstring(rawf['word/document.xml']); pf=list(xf.iter(W+'p'))
sf=[i for i,p in enumerate(pf) if (p.find(W+'pPr/'+W+'pStyle') is not None and p.find(W+'pPr/'+W+'pStyle').get(W+'val')=='ChapterTitle' and ''.join(n.text or '' for n in p.iter(W+'t')).strip()=='Sources')][-1]
FR=[]
for p in pf[sf:]:
    st=p.find(W+'pPr/'+W+'pStyle')
    if st is None or st.get(W+'val')!='ListBullet2': continue
    t=''.join(n.text or '' for n in p.iter(W+'t')).strip()
    us=[relf.get(h.get(R+'id'),'') for h in p.iter(W+'hyperlink')]
    FR.append((t,[u for u in us if u.startswith('http')]))

# ---- EN doc ----
ze,rawe=read('The-Augmented-Entrepreneur.docx')
relroot=ET.fromstring(rawe['word/_rels/document.xml.rels'])
rele={r.get('Id'):r.get('Target') for r in relroot}
xe=ET.fromstring(rawe['word/document.xml']); body=xe.find(W+'body')
pe=list(xe.iter(W+'p'))
se=[i for i,p in enumerate(pe) if (p.find(W+'pPr/'+W+'pStyle') is not None and p.find(W+'pPr/'+W+'pStyle').get(W+'val')=='ChapterTitle' and ''.join(n.text or '' for n in p.iter(W+'t')).strip()=='Sources')][-1]
ENp=[]
for p in pe[se:]:
    st=p.find(W+'pPr/'+W+'pStyle')
    if st is None or st.get(W+'val')!='ListBullet2': continue
    us=[rele.get(h.get(R+'id'),'') for h in p.iter(W+'hyperlink')]
    ENp.append((p,[norm(u) for u in us if u.startswith('http')]))
enset={u for _,us in ENp for u in us}

def parent(el):
    for par in body.iter():
        for i,ch in enumerate(par):
            if ch is el: return par,i
    return None,None

model=ENp[0][0]
added=0
for idx,(t,us) in enumerate(FR):
    if not us or any(norm(u) in enset for u in us): continue
    url=us[0]
    # anchor: nearest previous FR entry present in EN
    anchor=None
    for j in range(idx-1,-1,-1):
        pt,pu=FR[j]
        for u in pu:
            for p,eus in ENp:
                if norm(u) in eus: anchor=p;break
            if anchor:break
        if anchor:break
    if anchor is None: anchor=ENp[-1][0]
    rid='rIdAdd%s'%uuid.uuid4().hex[:12]
    r=ET.SubElement(relroot,'{%s}Relationship'%RN)
    r.set('Id',rid); r.set('Type','http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink')
    r.set('Target',url); r.set('TargetMode','External')
    new=copy.deepcopy(model)
    h=new.find(W+'hyperlink')
    h.set(R+'id',rid)
    ts=[x for x in h.iter(W+'t')]
    ts[0].text=url; ts[0].set('{http://www.w3.org/XML/1998/namespace}space','preserve')
    for x in ts[1:]: x.text=''
    par,i=parent(anchor); par.insert(i+1,new)
    ENp.insert(ENp.index((anchor,[norm(u) for u in [] ]) ) if False else len(ENp),(new,[norm(url)]))
    enset.add(norm(url)); added+=1

rawe['word/document.xml']=ET.tostring(xe,encoding='UTF-8',xml_declaration=True)
rawe['word/_rels/document.xml.rels']=ET.tostring(relroot,encoding='UTF-8',xml_declaration=True)
with zipfile.ZipFile('tmp.docx','w',zipfile.ZIP_DEFLATED) as z:
    for n in ze.namelist(): z.writestr(n,rawe[n])
shutil.move('tmp.docx','The-Augmented-Entrepreneur.docx')
print(f"EN — {added} URLs sources manquantes ajoutées (avec hyperliens cliquables)")
