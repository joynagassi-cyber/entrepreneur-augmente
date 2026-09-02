import zipfile, json, sys
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def paras(f):
    z=zipfile.ZipFile(f)
    x=ET.fromstring(z.read('word/document.xml'))
    body=x.find(W+'body')
    out=[]
    def walk(el, intable):
        for ch in el:
            if ch.tag==W+'p':
                t=''.join(n.text or '' for n in ch.iter(W+'t'))
                st=ch.find(W+'pPr/'+W+'pStyle')
                s=st.get(W+'val') if st is not None else 'Normal'
                nimg=len(list(ch.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}blip')))
                out.append({'style':s,'text':t,'img':nimg,'table':intable})
            elif ch.tag==W+'tbl':
                walk_tbl(ch)
            else:
                walk(ch,intable)
    def walk_tbl(tbl):
        for row in tbl.findall(W+'tr'):
            cells=[]
            for c in row.findall(W+'tc'):
                cells.append(' '.join(''.join(n.text or '' for n in p.iter(W+'t')) for p in c.iter(W+'p')).strip())
            out.append({'style':'__ROW__','text':' | '.join(cells),'img':0,'table':True,'cells':cells})
    walk(body,False)
    return out

if __name__=='__main__':
    for f,o in [('L-Entrepreneur-Augmente.docx','fr.json'),('The-Augmented-Entrepreneur.docx','en.json')]:
        p=paras(f)
        json.dump(p,open('tools/'+o,'w'),ensure_ascii=False)
        print(f,len(p))
