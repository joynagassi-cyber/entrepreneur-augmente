import sys;sys.path.insert(0,'tools')
from docxlib import Doc,W
e=Doc('The-Augmented-Entrepreneur.docx'); log=[]

def move_after(p,target):
    par,i=e.parent_of(p); par.remove(p)
    par2,j=e.parent_of(target); par2.insert(j+1,p)

ps=e.paras()
# locate blocks
i_meth=next(i for i,p in enumerate(ps) if 'Method — one channel, thirty days' in e.text(p))
i_prof=next(i for i,p in enumerate(ps) if '2. Name the profile again' in e.text(p))
i_list=next(i for i,p in enumerate(ps) if '1. List where the customer is already looking' in e.text(p))
i_cannot=next(i for i,p in enumerate(ps) if 'If you cannot, do not open a channel' in e.text(p))

# ordre voulu: Method / 1.List + 6 codeblocks / 2.Name profile / If you cannot / 3.Choose channel...
block=ps[i_list:i_cannot]          # heading1 + body + 6 codeblocks
cur=ps[i_meth]
for b in block:
    move_after(b,cur); cur=b
# renumber "2. Choose one channel" -> 3, etc.
ps=e.paras()
ren=[('2. Choose one channel that already contains the complaint','3. Choose one channel that already contains the complaint'),
     ('3. Entry offer — not the complete offer','4. Entry offer — not the complete offer'),
     ('4. Tie each action to a conversation','5. Tie each action to a conversation'),
     ('5. Stop threshold — written before','6. Stop threshold — written before')]
for old,new in ren:
    for p in ps:
        if e.style(p)=='Heading3' and e.text(p).strip()==old:
            e.set_text(p,new); break
log.append("EN — ch.32 : étapes de la méthode remises dans l'ordre et renumérotées 1→6")

# orphan "Reference" heading
ps=e.paras()
for i,p in enumerate(ps):
    if e.style(p)=='Heading2' and e.text(p).strip() in ('Reference','References') and e.style(ps[i+1]) in ('ChapterTitle','PartTitle'):
        e.remove(p); log.append("EN — 1 titre « Reference » orphelin supprimé (ch.3)"); break
e.save()
print('\n'.join(log))
