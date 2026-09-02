import zipfile, shutil, copy, os
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
NS={'w':W[1:-1]}
ET.register_namespace('w',W[1:-1])

class Doc:
    def __init__(self,path):
        self.path=path
        self.z=zipfile.ZipFile(path)
        self.names=self.z.namelist()
        self.raw={n:self.z.read(n) for n in self.names}
        self.root=ET.fromstring(self.raw['word/document.xml'])
        self.body=self.root.find(W+'body')
    def paras(self):
        return [p for p in self.body.iter(W+'p')]
    def text(self,p):
        return ''.join(n.text or '' for n in p.iter(W+'t'))
    def style(self,p):
        s=p.find(W+'pPr/'+W+'pStyle')
        return s.get(W+'val') if s is not None else 'Normal'
    def parent_of(self,el):
        for par in self.body.iter():
            for i,ch in enumerate(par):
                if ch is el: return par,i
        return None,None
    def find_text(self,frag,style=None,nth=0):
        hits=[p for p in self.paras() if frag in self.text(p) and (style is None or self.style(p)==style)]
        return hits[nth] if len(hits)>nth else None
    def set_text(self,p,txt):
        runs=[r for r in p.findall(W+'r')]
        ts=[t for r in runs for t in r.findall(W+'t')]
        if not ts: return False
        ts[0].text=txt
        ts[0].set('{http://www.w3.org/XML/1998/namespace}space','preserve')
        for t in ts[1:]:
            t.text=''
        return True
    def clone_after(self,model,anchor,txt):
        new=copy.deepcopy(model)
        self.set_text(new,txt)
        par,i=self.parent_of(anchor)
        par.insert(i+1,new)
        return new
    def remove(self,p):
        par,i=self.parent_of(p)
        par.remove(p)
    def save(self,out=None):
        out=out or self.path
        self.raw['word/document.xml']=ET.tostring(self.root,encoding='UTF-8',xml_declaration=True)
        tmp=out+'.tmp'
        with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as z:
            for n in self.names: z.writestr(n,self.raw[n])
        shutil.move(tmp,out)
