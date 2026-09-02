# -*- coding: utf-8 -*-
import json,re,csv,unicodedata

d=json.load(open('tools/inventory.json'))

URL={
 'Claude Code':'https://code.claude.com','Claude':'https://claude.ai','ChatGPT':'https://chatgpt.com',
 'OpenAI':'https://openai.com','Codex':'https://openai.com/codex','Gemini':'https://gemini.google.com',
 'Cursor':'https://cursor.com','GitHub Copilot':'https://github.com/features/copilot','GitHub':'https://github.com',
 'MCP':'https://modelcontextprotocol.io','BMAD Method':'https://docs.bmad-method.org',
 'GitHub Spec Kit':'https://github.com/github/spec-kit','OpenSpec':'https://github.com/Fission-AI/OpenSpec',
 'Kiro':'https://kiro.dev','Google Stitch':'https://stitch.withgoogle.com','Figma':'https://figma.com',
 'Docker':'https://docker.com','Supabase':'https://supabase.com','Firebase':'https://firebase.google.com',
 'Vercel':'https://vercel.com','Netlify':'https://netlify.com','Stripe':'https://stripe.com',
 'Gumroad':'https://gumroad.com','Lemon Squeezy':'https://lemonsqueezy.com','Paddle':'https://paddle.com',
 'Payhip':'https://payhip.com','Notion':'https://notion.so','Jira':'https://atlassian.com/software/jira',
 'Linear':'https://linear.app','Super Productivity':'https://super-productivity.com','n8n':'https://n8n.io',
 'Zapier':'https://zapier.com','Calendly':'https://calendly.com','WhatsApp':'https://whatsapp.com',
 'Prompt Guide':'https://prompt-guide.com','Y Combinator':'https://ycombinator.com/library',
 'Diátaxis':'https://diataxis.fr','arc42':'https://docs.arc42.org','NIST':'https://nist.gov',
 'OWASP':'https://owasp.org','Lighthouse':'https://developer.chrome.com/docs/lighthouse',
 'Playwright':'https://playwright.dev','Sentry':'https://sentry.io',
 'Superpowers':'https://github.com/obra/superpowers',
}
# page secondaire utile (tarifs / doc) quand elle a du sens
URL2={
 'Stripe':'https://stripe.com/pricing','Gumroad':'https://gumroad.com/pricing',
 'Lemon Squeezy':'https://lemonsqueezy.com/pricing','Paddle':'https://paddle.com/pricing',
 'Payhip':'https://payhip.com/pricing','Supabase':'https://supabase.com/pricing',
 'Vercel':'https://vercel.com/pricing','Netlify':'https://netlify.com/pricing',
 'Notion':'https://notion.so/pricing','Linear':'https://linear.app/pricing',
 'n8n':'https://n8n.io/pricing','Zapier':'https://zapier.com/pricing',
 'Calendly':'https://calendly.com/pricing','Cursor':'https://cursor.com/pricing',
 'Kiro':'https://kiro.dev/pricing','Figma':'https://figma.com/pricing',
 'Jira':'https://atlassian.com/software/jira/pricing','Sentry':'https://sentry.io/pricing',
 'Firebase':'https://firebase.google.com/pricing','Docker':'https://docker.com/pricing',
 'Google Stitch':'https://stitch.withgoogle.com','Claude':'https://claude.ai/new',
 'ChatGPT':'https://chatgpt.com','Gemini':'https://gemini.google.com',
 'Super Productivity':'https://super-productivity.com','Prompt Guide':'https://prompt-guide.com',
}
CAP={'Google Stitch','Kiro','Figma','Cursor','Supabase','Vercel','Netlify','Stripe','Gumroad',
 'Lemon Squeezy','Paddle','Payhip','Notion','Jira','Linear','Super Productivity','n8n','Zapier',
 'Calendly','Claude','ChatGPT','Gemini','Sentry','Prompt Guide','Firebase','Docker'}

def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()
    s=re.sub(r'[^a-zA-Z0-9]+','-',s).strip('-').lower()
    return s

def is_card(k): return bool(re.match(r'Chapitre \d+ —',k))
def chnum(k):
    m=re.search(r'Chapitre (\d+)',k)
    return int(m.group(1)) if m else None

rows=[]
vu={}   # outil -> premier fichier capture (pour reutilisation)
for k,v in d.items():
    if is_card(k): continue          # fiches de l'annexe C : pas d'illustration
    n=chnum(k)
    if n is not None: cid=f'ch{n:02d}'
    elif k.startswith('Annexe A'): cid='annexeA'
    elif k.startswith('Annexe B'): cid='annexeB'
    elif k.startswith('Glossaire'): continue
    else: cid=slug(k)[:12]
    tools=[(t,c) for t,c in sorted(v['tools'].items(),key=lambda x:-x[1]) if t in CAP]
    for t,c in tools[:3]:            # 2-3 captures max par chapitre
        base=f'{cid}-{slug(t)}'
        u1=URL.get(t,'')
        u2=URL2.get(t,'')
        if u2==u1: u2=''             # pas de doublon d'URL
        rows.append({'chapitre':k,'partie':v['part'] or '','num':n if n else 99,
                     'outil':t,'mentions':c,
                     'url_1':u1,'fichier_1':base+'-01.png',
                     'url_2':u2,'fichier_2':(base+'-02.png') if u2 else '',
                     'slug':slug(t)})

rows.sort(key=lambda r:(r['num'],r['outil']))

# marquer les reutilisations : un outil deja capture ailleurs
for r in rows:
    if r['slug'] in vu:
        r['note']='Reutiliser '+vu[r['slug']]
        r['url_1']=''; r['fichier_1']=vu[r['slug']]
        r['url_2']=''; r['fichier_2']=''
    else:
        vu[r['slug']]=r['fichier_1']
        r['note']='A capturer'

with open('CAPTURES-A-FAIRE.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f,delimiter=';')
    w.writerow(['Chapitre','Partie','Outil','Mentions','Action','URL a capturer','Nom du fichier','URL secondaire','Nom du fichier 2','Fait'])
    for r in rows:
        w.writerow([r['chapitre'],r['partie'],r['outil'],r['mentions'],r['note'],
                    r['url_1'],r['fichier_1'],r['url_2'],r['fichier_2'],''])

neuf=[r for r in rows if r['note']=='A capturer']
print('lignes CSV            :',len(rows))
print('captures a realiser   :',len(neuf))
print('  + pages secondaires :',sum(1 for r in neuf if r['url_2']))
print('  = images totales    :',len(neuf)+sum(1 for r in neuf if r['url_2']))
print('reutilisations        :',len(rows)-len(neuf))
print('chapitres couverts    :',len({r['chapitre'] for r in rows}))

# --- fichier 2 : la liste de travail, une ligne par capture unique ---
work=[]
for r in rows:
    if r['note']!='A capturer': continue
    work.append([r['outil'],r['url_1'],r['fichier_1'],'Page d\'accueil',r['chapitre'],''])
    if r['url_2']:
        work.append([r['outil'],r['url_2'],r['fichier_2'],'Tarifs / secondaire',r['chapitre'],''])
with open('CAPTURES-LISTE-DE-TRAVAIL.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f,delimiter=';')
    w.writerow(['Outil','URL','Nom du fichier','Type de page','Chapitre d\'origine','Fait'])
    w.writerows(work)
print('liste de travail      :',len(work),'captures uniques')
