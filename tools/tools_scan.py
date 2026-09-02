import sys,zipfile,re,json
sys.path.insert(0,'tools')
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

# outil -> (regex, url officielle, categorie)
TOOLS=[
 ('Claude Code',          r'\bClaude Code\b',            'https://code.claude.com','Agent CLI'),
 ('Claude',               r'\bClaude\b(?! Code)',        'https://claude.ai','Assistant'),
 ('ChatGPT',              r'\bChatGPT\b',                'https://chatgpt.com','Assistant'),
 ('OpenAI',               r'\bOpenAI\b',                 'https://openai.com','Plateforme'),
 ('Codex',                r'\bCodex\b',                  'https://openai.com/codex','Agent'),
 ('Gemini',               r'\bGemini\b',                 'https://gemini.google.com','Assistant'),
 ('Cursor',               r'\bCursor\b',                 'https://cursor.com','IDE'),
 ('GitHub Copilot',       r'\bCopilot\b',                'https://github.com/features/copilot','Assistant'),
 ('GitHub',               r'\bGitHub\b(?! Copilot)',     'https://github.com','Plateforme'),
 ('MCP',                  r'\bMCP\b',                    'https://modelcontextprotocol.io','Protocole'),
 ('BMAD Method',          r'\bBMAD\b',                   'https://docs.bmad-method.org','Méthode'),
 ('GitHub Spec Kit',      r'\bSpec Kit\b',               'https://github.com/github/spec-kit','Méthode'),
 ('OpenSpec',             r'\bOpenSpec\b',               'https://github.com/Fission-AI/OpenSpec','Méthode'),
 ('Kiro',                 r'\bKiro\b',                   'https://kiro.dev','IDE'),
 ('Google Stitch',        r'\bStitch\b',                 'https://stitch.withgoogle.com','Design IA'),
 ('Figma',                r'\bFigma\b',                  'https://figma.com','Design'),
 ('Docker',               r'\bDocker\b',                 'https://docker.com','Infra'),
 ('Supabase',             r'\bSupabase\b',               'https://supabase.com','BaaS'),
 ('Firebase',             r'\bFirebase\b',               'https://firebase.google.com','BaaS'),
 ('Vercel',               r'\bVercel\b',                 'https://vercel.com','Déploiement'),
 ('Netlify',              r'\bNetlify\b',                'https://netlify.com','Déploiement'),
 ('Stripe',               r'\bStripe\b',                 'https://stripe.com','Paiement'),
 ('Gumroad',              r'\bGumroad\b',                'https://gumroad.com','Paiement'),
 ('Lemon Squeezy',        r'\bLemon ?Squeezy\b',         'https://lemonsqueezy.com','Paiement'),
 ('Paddle',               r'\bPaddle\b',                 'https://paddle.com','Paiement'),
 ('Payhip',               r'\bPayhip\b',                 'https://payhip.com','Paiement'),
 ('Notion',               r'\bNotion\b',                 'https://notion.so','Productivité'),
 ('Jira',                 r'\bJira\b',                   'https://atlassian.com/software/jira','Suivi'),
 ('Linear',               r'\bLinear\b',                 'https://linear.app','Suivi'),
 ('Super Productivity',   r'\bSuper Productivity\b',     'https://super-productivity.com','Suivi'),
 ('n8n',                  r'\bn8n\b',                    'https://n8n.io','Automatisation'),
 ('Zapier',               r'\bZapier\b',                 'https://zapier.com','Automatisation'),
 ('Make',                 r'\bMake\.com\b',              'https://make.com','Automatisation'),
 ('Calendly',             r'\bCalendly\b',               'https://calendly.com','SaaS'),
 ('WhatsApp',             r'\bWhatsApp\b',               'https://whatsapp.com','Canal'),
 ('Prompt Guide',         r'\bPrompt Guide\b',           'https://prompt-guide.com','Ressource'),
 ('Y Combinator',         r'\bY Combinator\b|\bYC\b',    'https://ycombinator.com/library','Ressource'),
 ('Diátaxis',             r'\bDiátaxis\b|\bDiataxis\b',  'https://diataxis.fr','Méthode'),
 ('arc42',                r'\barc42\b',                  'https://docs.arc42.org','Méthode'),
 ('NIST',                 r'\bNIST\b',                   'https://nist.gov','Référentiel'),
 ('OWASP',                r'\bOWASP\b',                  'https://owasp.org','Référentiel'),
 ('Lighthouse',           r'\bLighthouse\b',             'https://developer.chrome.com/docs/lighthouse','Outil'),
 ('Playwright',           r'\bPlaywright\b',             'https://playwright.dev','Test'),
 ('Sentry',               r'\bSentry\b',                 'https://sentry.io','Monitoring'),
 ('Superpowers',          r'\bsuperpowers\b',            'https://github.com/obra/superpowers','Skills'),
]

def scan(f):
    z=zipfile.ZipFile(f)
    rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('word/_rels/document.xml.rels'))}
    x=ET.fromstring(z.read('word/document.xml'))
    rows=[];part=None;chap=None
    for p in x.iter(W+'p'):
        st=p.find(W+'pPr/'+W+'pStyle'); s=st.get(W+'val') if st is not None else 'Normal'
        t=''.join(n.text or '' for n in p.iter(W+'t'))
        if s=='PartTitle': part=t.strip()
        if s=='ChapterTitle':
            chap=t.strip()
            if chap=='Sources': break
        urls=[rels.get(h.get(R+'id'),'') for h in p.iter(W+'hyperlink')]
        urls+=re.findall(r'https?://[^\s,;)\]»"]+',t)
        rows.append({'part':part,'chap':chap,'text':t,'urls':[u for u in urls if u.startswith('http')]})
    return rows

rows=scan('L-Entrepreneur-Augmente.docx')
chaps={}
for r in rows:
    key=r['chap'] or '(liminaires)'
    c=chaps.setdefault(key,{'part':r['part'],'tools':{},'urls':set()})
    for u in r['urls']: c['urls'].add(u)
    for name,rx,url,cat in TOOLS:
        if re.search(rx,r['text']):
            c['tools'][name]=c['tools'].get(name,0)+len(re.findall(rx,r['text']))
res={k:{'part':v['part'],'tools':v['tools'],'cat':{n:(c,u) for n,rx,u,c in [(a,b,d,e) for a,b,d,e in TOOLS] if n in v['tools']},'urls':sorted(v['urls'])} for k,v in chaps.items() if v['tools'] or v['urls']}
json.dump(res,open('tools/inventory.json','w'),ensure_ascii=False,indent=1)
allt={}
for v in res.values():
    for n,c in v['tools'].items(): allt[n]=allt.get(n,0)+c
print('chapitres concernés :',len(res))
print('outils distincts    :',len(allt))
print('mentions totales    :',sum(allt.values()))
print('URL dans le corps   :',len({u for v in res.values() for u in v['urls']}))
