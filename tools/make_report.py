import json,re
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
 'Playwright':'https://playwright.dev','Sentry':'https://sentry.io','Superpowers':'https://github.com/obra/superpowers',
}
CAPTURABLE={'Google Stitch','Kiro','Figma','Cursor','Supabase','Vercel','Netlify','Stripe','Gumroad',
 'Lemon Squeezy','Paddle','Payhip','Notion','Jira','Linear','Super Productivity','n8n','Zapier',
 'Calendly','Claude','ChatGPT','Gemini','Sentry','Prompt Guide','Firebase','Docker'}

tot={}
for v in d.values():
    for n,c in v['tools'].items(): tot[n]=tot.get(n,0)+c

def is_card(k):
    # fiches de l'annexe C : 'Chapitre N — Titre' (tiret cadratin), vs 'Chapitre N : Titre'
    return bool(re.match(r'Chapitre \d+ —',k))

def key(k):
    m=re.search(r'Chapitre (\d+)',k)
    if m and not is_card(k): return (2,int(m.group(1)),0)
    if is_card(k): return (4,int(m.group(1)),0)
    if k.startswith('Annexe'): return (3,0,k)
    return (1,0,k)

L=['# Inventaire des outils cités — L\'Entrepreneur Augmenté','',
   f'**{len(tot)} outils distincts · {sum(tot.values())} mentions · {len(d)} sections concernées**  ',
   'Périmètre : corps du livre uniquement (la section Sources est exclue).','',
   '> Colonne « Capture » : ✅ = site produit avec une interface montrable · — = organisme, protocole,',
   '> méthode ou réseau social, où une capture apporte peu.','',
   '---','','## Vue d\'ensemble — outils par fréquence','',
   '| Outil | Mentions | Chapitres | Capture | URL |','|---|---:|---:|:---:|---|']
for n,c in sorted(tot.items(),key=lambda x:-x[1]):
    nch=len([k for k,v in d.items() if n in v['tools']])
    L.append(f'| **{n}** | {c} | {nch} | {"✅" if n in CAPTURABLE else "—"} | `{URL.get(n,"")}` |')

L+=['','---','','## Détail chapitre par chapitre','']
cur=None
for k in sorted(d,key=key):
    v=d[k]
    if not v['tools'] and not v['urls']: continue
    sec = 'Annexe C — fiches de synthèse' if is_card(k) else (v['part'] or '(liminaires)')
    if sec!=cur:
        cur=sec; L+=[f'### {cur}','']
    L.append(f'**{k}**  ')
    if v['tools']:
        items=sorted(v['tools'].items(),key=lambda x:-x[1])
        L.append('Outils : '+', '.join(f'{n} ({c})' for n,c in items)+'  ')
        shots=[n for n,_ in items if n in CAPTURABLE]
        if shots: L.append(f'→ Captures pertinentes : **{", ".join(shots[:3])}**  ')
    if v['urls']:
        L.append('Liens dans le texte :')
        for u in v['urls']: L.append(f'  - `{u}`')
    L.append('')
open('INVENTAIRE-OUTILS.md','w').write('\n'.join(L))
print('ecrit, lignes:',len(L))
print('capturables:',len([n for n in tot if n in CAPTURABLE]),'/',len(tot))
