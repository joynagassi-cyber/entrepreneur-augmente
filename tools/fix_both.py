import sys,copy;sys.path.insert(0,'tools')
from docxlib import Doc,W
log=[]

def setstyle(d,p,s):
    pPr=p.find(W+'pPr')
    st=pPr.find(W+'pStyle')
    st.set(W+'val',s)

def move_before(d,p,target):
    par,i=d.parent_of(p); par.remove(p)
    par2,j=d.parent_of(target); par2.insert(j,p)

# ================= FR =================
d=Doc('L-Entrepreneur-Augmente.docx'); ps=d.paras()
n=0
for i,p in enumerate(ps):
    if d.text(p).strip()=='La question à poser' and d.style(ps[i+1])=='BodyText':
        setstyle(d,ps[i+1],'LeadParagraph'); n+=1
log.append(f"FR — {n} réponses à « La question à poser » repassées en style LeadParagraph (2 étaient en BodyText)")

# Fig.3 & Fig.5 : image+légende placées AVANT le contenu, comme en EN
ps=d.paras()
def fix_fig(capfrag, firstitem_frag):
    ps=d.paras()
    cap=None
    for p in ps:
        if d.style(p)=='Caption' and capfrag in d.text(p): cap=p;break
    if cap is None: return False
    i=ps.index(cap); img=ps[i-1]
    tgt=None
    for p in ps:
        if firstitem_frag in d.text(p): tgt=p;break
    if tgt is None: return False
    move_before(d,img,tgt); move_before(d,cap,tgt)
    return True
a=fix_fig('La boucle de pilotage en sept','1. Décrire la tâche')
b=fix_fig("Cinq questions avant d'envoyer",'C — Contexte')
log.append(f"FR — figures 3 et 5 replacées avant leur liste (ordre aligné sur l'anglais) [{a},{b}]")
d.save()

# ================= EN =================
e=Doc('The-Augmented-Entrepreneur.docx'); ps=e.paras()
# Exercise style
for p in ps:
    if 'Final exercise' in e.text(p) and e.style(p)=='Heading2':
        setstyle(e,p,'Exercise')
        log.append("EN — « Final exercise — decide with visible assumptions » repassé en style Exercise (était Heading2)")
        break
# LeadParagraph -> BodyText mismatch under "The question to ask": FR uses BodyText for 2, already fixed FR side.
# Ch14/15 : "Titres d'origine" line only in FR -> add EN equivalent
ps=e.paras()
def add_origin(chfrag, txt):
    ps=e.paras()
    ch=None
    for i,p in enumerate(ps):
        if e.style(p)=='ChapterTitle' and chfrag in e.text(p): ch=i;break
    if ch is None: return False
    model=None
    for p in ps:
        if e.style(p)=='LeadParagraph': model=p;break
    # insert after the Callout following chapter title
    anchor=ps[ch+1]
    m=copy.deepcopy(model); e.set_text(m,txt)
    par,i=e.parent_of(anchor); par.insert(i+1,m)
    return True
o1=add_origin('Chapter 14: Picking the right tool','Original titles: Ecosystem, agents and accelerators; Mastering skills and MCP.')
o2=add_origin('Chapter 15: Automating a sequence','Original titles: The agentic work loop; Choosing and composing workflows.')
log.append(f"EN — mention « Original titles » ajoutée aux chapitres 14 et 15 (présente en FR) [{o1},{o2}]")
e.save()
print('\n'.join(log))
