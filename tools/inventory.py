import sys,zipfile,re,json
sys.path.insert(0,'tools')
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

def load(f):
    z=zipfile.ZipFile(f)
    rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('word/_rels/document.xml.rels'))}
    x=ET.fromstring(z.read('word/document.xml'))
    out=[];part=None;chap=None
    for p in x.iter(W+'p'):
        st=p.find(W+'pPr/'+W+'pStyle'); s=st.get(W+'val') if st is not None else 'Normal'
        t=''.join(n.text or '' for n in p.iter(W+'t'))
        if s=='PartTitle': part=t.strip()
        if s=='ChapterTitle': chap=t.strip()
        urls=[rels.get(h.get(R+'id'),'') for h in p.iter(W+'hyperlink')]
        urls=[u for u in urls if u.startswith('http')]
        # urls en texte brut
        urls+= re.findall(r'https?://[^\s,;)\]»"]+', t)
        if urls or t.strip():
            out.append({'part':part,'chap':chap,'style':s,'text':t,'urls':urls})
    return out

def domain(u):
    m=re.match(r'https?://([^/]+)',u)
    d=m.group(1).lower().replace('www.','') if m else u
    return d

# nom lisible d'outil depuis le domaine
NAMES={
 'github.com':'GitHub','docs.github.com':'GitHub Docs','raw.githubusercontent.com':'GitHub',
 'anthropic.com':'Anthropic','code.claude.com':'Claude Code','platform.claude.com':'Claude Platform',
 'anthropic.skilljar.com':'Anthropic Skills','claude.ai':'Claude',
 'openai.com':'OpenAI','developers.openai.com':'OpenAI Developers','openai.github.io':'OpenAI Agents SDK',
 'platform.openai.com':'OpenAI Platform',
 'modelcontextprotocol.io':'Model Context Protocol','docs.bmad-method.org':'BMAD Method',
 'kiro.dev':'Kiro','diataxis.fr':'Diátaxis','docs.arc42.org':'arc42',
 'martinfowler.com':'Martin Fowler','ycombinator.com':'Y Combinator','paulgraham.com':'Paul Graham',
 'stripe.com':'Stripe','docs.stripe.com':'Stripe Docs','gumroad.com':'Gumroad','payhip.com':'Payhip',
 'paddle.com':'Paddle','docs.lemonsqueezy.com':'Lemon Squeezy','lemonsqueezy.com':'Lemon Squeezy',
 'docs.docker.com':'Docker','vercel.com':'Vercel','netlify.com':'Netlify','supabase.com':'Supabase',
 'prompt-guide.com':'Prompt Guide','atlassian.com':'Jira','super-productivity.com':'Super Productivity',
 'developers.google.com':'Google Developers','stitch.withgoogle.com':'Google Stitch',
 'microsoft.com':'Microsoft Research','nist.gov':'NIST','owasp.org':'OWASP',
 'stackoverflow.co':'Stack Overflow','survey.stackoverflow.co':'Stack Overflow Survey',
 'graphify.net':'Graphify','strategyzer.com':'Strategyzer','nngroup.com':'Nielsen Norman Group',
}
def toolname(d):
    if d in NAMES: return NAMES[d]
    base=d.split('.')
    return base[-2].capitalize() if len(base)>=2 else d

for f,lang in [('L-Entrepreneur-Augmente.docx','FR')]:
    data=load(f)
    # sections avant "Sources" = corps du livre
    body=[]
    for d in data:
        if d['chap']=='Sources': break
        body.append(d)
    # regrouper par chapitre
    chaps=[]
    seen={}
    for d in body:
        if not d['urls']: continue
        key=d['chap'] or d['part'] or '(début)'
        seen.setdefault(key,{'part':d['part'],'tools':{}})
        for u in d['urls']:
            dom=domain(u)
            seen[key]['tools'].setdefault(dom,set()).add(u)
    json.dump({k:{'part':v['part'],'tools':{d:sorted(us) for d,us in v['tools'].items()}} for k,v in seen.items()},
              open('tools/inventory.json','w'),ensure_ascii=False,indent=1)
    tot_ch=len(seen); tot_tools=len({d for v in seen.values() for d in v['tools']})
    tot_urls=sum(len(us) for v in seen.values() for us in v['tools'].values())
    print(f'== {lang} : {tot_ch} chapitres avec liens | {tot_tools} outils distincts | {tot_urls} URL')
