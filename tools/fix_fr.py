import sys, copy
sys.path.insert(0,'tools')
from docxlib import Doc, W
import xml.etree.ElementTree as ET

d=Doc('L-Entrepreneur-Augmente.docx')
log=[]

# ---- FIX 1: schéma "La transformation" manquant en FR ----
DIAG=["Idée encore floue","  → Problème vu dans la vraie vie","  → Hypothèse que l’on peut réfuter",
"  → Preuve venue d’une personne réelle","  → Offre : ce que vous vendez, à qui",
"  → Plus petite version qui apprend (MVP)","  → Ce que l’IA a le droit de voir",
"  → Délégation avec une limite","  → Produit qui tient","  → Vente",
"  → Économie qui tient encore","  → Croissance sans casse",
"  → Organisation humain + IA","  → Autonomie sous contrôle"]

# modèle CodeBlock existant dans le doc FR
model=None
for p in d.paras():
    if d.style(p)=='CodeBlock': model=p; break
assert model is not None

anchor=d.find_text("Fig. 2 — La transformation", style='Caption')
assert anchor is not None, "ancre Fig.2 introuvable"
cur=anchor
first=True
for line in DIAG:
    m=copy.deepcopy(model)
    # bordure haute sur la 1re ligne, comme en EN
    pPr=m.find(W+'pPr')
    for b in pPr.findall(W+'pBdr'): pPr.remove(b)
    if first:
        bdr=ET.SubElement(pPr,W+'pBdr')
        top=ET.SubElement(bdr,W+'top')
        top.set(W+'val','single'); top.set(W+'color','D6D3D1'); top.set(W+'sz','4'); top.set(W+'space','4')
        pPr.remove(bdr); pPr.insert(1,bdr)
        first=False
    d.set_text(m,line)
    par,i=d.parent_of(cur); par.insert(i+1,m); cur=m
log.append(f"FIX 1 — schéma « La transformation » ajouté en FR ({len(DIAG)} lignes CodeBlock)")

# ---- FIX 2: titres « Références » orphelins (sans contenu) ----
removed=0
while True:
    ps=d.paras(); done=True
    for i,p in enumerate(ps):
        if d.style(p)=='Heading2' and d.text(p).strip() in ('Références','Référence'):
            if i+1<len(ps) and d.style(ps[i+1]) in ('ChapterTitle','PartTitle'):
                d.remove(p); removed+=1; done=False; break
    if done: break
log.append(f"FIX 2 — {removed} titres « Références » orphelins (sans aucune référence dessous) supprimés en FR")

# ---- FIX 3: doublon Annexe B ----
ps=d.paras()
seen=[p for p in ps if d.text(p).strip().startswith('La YC Startup Library') ]
if len(seen)>1:
    d.remove(seen[-1])
    log.append("FIX 3 — paragraphe « La YC Startup Library… » dupliqué supprimé (Annexe B)")

d.save()
print('\n'.join(log))
