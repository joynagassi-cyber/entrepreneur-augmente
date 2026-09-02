import json, difflib, os
fr=json.load(open('tools/fr.json')); en=json.load(open('tools/en.json'))

def chaps(d):
    out=[];cur=None
    for i,p in enumerate(d):
        if p['style'] in ('ChapterTitle','EABookTitle'):
            cur={'title':p['text'],'idx':i,'items':[]}; out.append(cur)
        elif cur is not None:
            if p['text'].strip() or p['img']: cur['items'].append(p)
    return out

cf,ce=chaps(fr),chaps(en)
data=[]
for i,(a,b) in enumerate(zip(cf,ce)):
    A,B=a['items'],b['items']
    sa=[p['style'] for p in A]; sb=[p['style'] for p in B]
    sm=difflib.SequenceMatcher(None,sa,sb,autojunk=False)
    rows=[]
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=='equal':
            for k in range(i2-i1): rows.append({'k':'=','l':A[i1+k],'r':B[j1+k]})
        elif tag=='replace':
            n=max(i2-i1,j2-j1)
            for k in range(n):
                rows.append({'k':'~','l':A[i1+k] if i1+k<i2 else None,'r':B[j1+k] if j1+k<j2 else None})
        elif tag=='delete':
            for k in range(i1,i2): rows.append({'k':'-','l':A[k],'r':None})
        elif tag=='insert':
            for k in range(j1,j2): rows.append({'k':'+','l':None,'r':B[k]})
    wa=sum(len(p['text'].split()) for p in A); wb=sum(len(p['text'].split()) for p in B)
    nd=sum(1 for r in rows if r['k']!='=')
    data.append({'i':i,'tfr':a['title'],'ten':b['title'],'wfr':wa,'wen':wb,
                 'ifr':sum(p['img'] for p in A),'ien':sum(p['img'] for p in B),
                 'diffs':nd,'rows':rows})
os.makedirs('review',exist_ok=True)
json.dump(data,open('review/data.json','w'),ensure_ascii=False)
print('chapitres',len(data),'ecarts',sum(d['diffs'] for d in data))
