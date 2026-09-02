import sys,copy;sys.path.insert(0,'tools')
from docxlib import Doc,W
e=Doc('The-Augmented-Entrepreneur.docx'); log=[]

def model(style):
    for p in e.paras():
        if e.style(p)==style: return p
    return None

def insert_after(anchor,style,txt):
    m=copy.deepcopy(model(style)); e.set_text(m,txt)
    par,i=e.parent_of(anchor); par.insert(i+1,m); return m

# --- ch32: bloc "1. List where the customer already looks" manquant en EN
ps=e.paras(); h3=None
for p in ps:
    if e.style(p)=='Heading3' and 'Name the profile again' in e.text(p): h3=p;break
if h3:
    cur=h3
    cur=insert_after(cur,'Heading3','1. List where the customer is already looking for a solution')
    cur=insert_after(cur,'BodyText','Not where you like to post. Where she complains, asks, improvises:')
    for line in ["Word of mouth in the same trade","Local group of practitioners",
                 "Personal message after she told you about a no-show",
                 "Partner (accountant, coworking space, association)",
                 "Search “confirm appointment” — often too early",
                 "Advertising — almost always too early"]:
        cur=insert_after(cur,'CodeBlock',line)
    # renumber the following headings
    ps=e.paras(); i=ps.index(h3)
    e.set_text(h3,'2. Name the profile again (chapter 29)')
    log.append("EN — ch.32 : étape « 1. List where the customer is already looking » + ses 6 canaux ajoutés (absente en anglais)")

# --- ch2 : ligne CodeBlock tronquée manquante
ps=e.paras()
for i,p in enumerate(ps):
    if 'your own reminders that are missing' in e.text(p).lower() or 'are YOUR reminders' in e.text(p):
        nxt=e.text(ps[i+1])
        if 'discipline' not in nxt:
            insert_after(p,'CodeBlock',"of organisation? A tool does not solve a discipline problem.")
            log.append("EN — ch.2 : ligne de prompt manquante restaurée (« …a discipline problem. »)")
        break

# --- mentions légales : phrase "Titres d'origine" présente en FR
ps=e.paras()
for p in ps:
    if 'Check official documentation' in e.text(p) or 'Tools, prices, interfaces' in e.text(p):
        insert_after(p,'BodyText','The Original title notes under some chapters recall an older heading. They may disappear in a later edition.')
        log.append("EN — mentions légales : paragraphe « Original title notes… » ajouté (présent en FR)")
        break
e.save()
print('\n'.join(log))
