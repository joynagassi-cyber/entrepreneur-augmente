# -*- coding: utf-8 -*-
"""Figures explicatives — Parties IV et V (chapitres 21 à 35)."""
from figlib import *

RED = '#D0665A'
GREEN = '#4E9C64'


# ------------------------------------------------------------------ ch. 21

@fig('ch21-deux-parcours',
     {'fr': ('BodyText', 'Si vous n’écrivez qu’un parcours « utilisateur »'),
      'en': ('BodyText', 'If you write only one “user” journey')},
     {'fr': 'Deux acteurs, deux parcours : le même état « jeudi 10 h — confirmé », vu des deux côtés',
      'en': 'Two actors, two journeys: the same state “Thursday 10:00 — confirmed”, seen from both sides'},
     h=240)
def ch21_deux_parcours(F, L):
    T = {'fr': dict(cli='Cliente', nina='Nina', state='jeudi 10 h — confirmé',
                    c=['reçoit le message', 'répond en un geste', 'lit l’état'],
                    n=['ne relance plus après 19 h', 'voit le même état', 'ne rouvre pas WhatsApp au hasard'],
                    fc='échec silencieux : elle ignore le message ou ne sait pas répondre',
                    fn='échec silencieux : l’agent a « réussi », elle vérifie quand même'),
         'en': dict(cli='Client', nina='Nina', state='Thursday 10:00 — confirmed',
                    c=['receives the message', 'answers in one gesture', 'reads the state'],
                    n=['no longer chases after 7 p.m.', 'sees the same state', 'does not reopen WhatsApp at random'],
                    fc='silent failure: she ignores the message or does not know how to answer',
                    fn='silent failure: the agent “succeeded”, she checks anyway')}[L]
    # état central
    F.box(360, 40, 280, 56, T['state'], kind='ok', pt=7.6, weight='SemiBold')
    F.box(20, 44, 120, 48, T['cli'], kind='human', pt=7.6)
    F.arrow(142, 68, 356, 68, head_size=8)
    F.box(860, 44, 120, 48, T['nina'], kind='human', pt=7.6)
    F.arrow(858, 68, 644, 68, head_size=8)
    for i, step in enumerate(T['c']):
        y = 116 + i * 22
        F.badge(30, y, str(i + 1), r=7, pt=5, kind='human', color='text')
        F.text(44, y, step, pt=6, color='muted', anchor='lm')
    for i, step in enumerate(T['n']):
        y = 116 + i * 22
        F.badge(560, y, str(i + 1), r=7, pt=5, kind='human', color='text')
        F.text(574, y, step, pt=6, color='muted', anchor='lm')
    # échecs silencieux
    F.cross(30, 208, r=5)
    F.text(46, 208, T['fc'], pt=5.9, color=RED, anchor='lm', max_w=440, align='left')
    F.cross(560, 208, r=5)
    F.text(576, 208, T['fn'], pt=5.9, color=RED, anchor='lm', max_w=400, align='left')


# ------------------------------------------------------------------ ch. 22

@fig('ch22-hier-maintenant',
     {'fr': ('CodeBlock', 'I1[Idée] --> M1[Main Figma ou Framer]'),
      'en': ('CodeBlock', 'I1[Idea] --> M1[Hand: Figma or Framer]')},
     {'fr': 'Hier, la main et le goût ; maintenant, le goût écrit : l’écran arrive, vous tranchez s’il sert le parcours',
      'en': 'Yesterday, the hand and the taste; today, written taste: the screen arrives, you decide whether it serves the journey'},
     h=250, mode='replace_code')
def ch22_hier_maintenant(F, L):
    T = {'fr': dict(a='Hier', b='Maintenant', ai=['Idée', 'Main : Figma ou Framer', 'Écran'],
                    bi=['Idée', 'Spec écrite', 'Stitch propose', 'Vous tranchez'],
                    an='il fallait la main et le goût', bn='il faut le goût écrit'),
         'en': dict(a='Yesterday', b='Today', ai=['Idea', 'Hand: Figma or Framer', 'Screen'],
                    bi=['Idea', 'Written spec', 'Stitch proposes', 'You decide'],
                    an='it took the hand and the taste', bn='it takes written taste')}[L]
    (lx, ly, lw, lh), (rx, ry, rw, rh) = compare(F, T['a'], T['b'], y=16, h=190, kinds=('ghost', 'box'))
    hflow(F, T['ai'], y=ly + 30, h=52, x0=lx + 14, x1=lx + lw - 14, gap=18, kinds=['ghost', 'ghost', 'ghost'], pt=6.4)
    F.text(lx + lw / 2, ly + 118, T['an'], pt=6.2, color='muted')
    hflow(F, T['bi'], y=ry + 30, h=52, x0=rx + 14, x1=rx + rw - 14, gap=14, kinds=['ghost', 'human', 'box', 'human'], pt=6.2)
    F.text(rx + rw / 2, ry + 118, T['bn'], pt=6.2, color='muted')


# ------------------------------------------------------------------ ch. 23

@fig('ch23-banc',
     {'fr': ('BodyText', 'Si le taux passe sous le seuil, vous baissez le niveau d’autonomie'),
      'en': ('BodyText', 'If the rate falls under the threshold, you lower the autonomy level')},
     {'fr': 'Le banc d’évaluation : cinq tâches figées, rejouées à chaque changement, un seuil écrit avant la mesure',
      'en': 'The evaluation bench: five frozen tasks, replayed on every change, a threshold written before measuring'},
     h=310)
def ch23_banc(F, L):
    T = {'fr': dict(tasks=['T1', 'T2', 'T3', 'T4', 'T5'], frozen='5 tâches figées, entrées + sortie acceptable',
                    change='changement : prompt, skill, modèle, contexte ou règle', replay='rejouer les 5',
                    metrics=['taux de succès', 'coût par succès', 'latence', 'taux d’escalade'],
                    above='≥ seuil : autonomie maintenue ou élargie', below='< seuil : autonomie baissée (ch. 39)',
                    thr='seuil écrit avant la mesure'),
         'en': dict(tasks=['T1', 'T2', 'T3', 'T4', 'T5'], frozen='5 frozen tasks, inputs + acceptable output',
                    change='change: prompt, skill, model, context or rule', replay='replay the 5',
                    metrics=['success rate', 'cost per success', 'latency', 'escalation rate'],
                    above='≥ threshold: autonomy kept or widened', below='< threshold: autonomy lowered (ch. 39)',
                    thr='threshold written before measuring')}[L]
    # tâches figées
    for i, t in enumerate(T['tasks']):
        F.box(20 + i * 54, 30, 46, 40, t, kind='ghost', pt=7, weight='SemiBold')
    F.text(155, 80, T['frozen'], pt=5.8, color='muted', anchor='mt', max_w=280)
    # changement -> rejouer
    F.box(330, 22, 240, 64, T['change'], kind='human', pt=6.0, weight='Regular')
    F.arrow(300, 50, 326, 50, head_size=7)
    F.arrow(572, 50, 606, 50, head_size=7)
    F.text(589, 98, T['replay'], pt=5.4, color='muted')
    # métriques
    F.box(610, 22, 176, 64, '\n'.join(T['metrics'][:2]), kind='box', pt=6)
    F.box(796, 22, 184, 64, '\n'.join(T['metrics'][2:]), kind='box', pt=6)
    # seuil et décision
    F.line(698, 88, 698, 116, color='arrow')
    F.line(888, 88, 888, 116, color='arrow')
    F.line(698, 116, 888, 116, color='arrow')
    F.arrow(793, 116, 793, 146, head_size=8)
    F.diamond(793, 190, 250, 82, T['thr'], kind='human', pt=6.2)
    F.arrow(668, 190, 616, 190, head_size=8)
    F.box(330, 166, 284, 48, T['above'], kind='ok', pt=6.2, weight='Regular')
    F.arrow(793, 231, 793, 258, head_size=8)
    F.box(620, 260, 346, 46, T['below'], kind='risk', pt=6.2, weight='Regular')
    # boucle : autonomie -> nouvelle campagne
    F.polyline_arrow([(330, 190), (140, 190), (140, 96)], color='rule')


# ------------------------------------------------------------------ ch. 24

@fig('ch24-autorite',
     {'fr': ('BodyText', 'Les couches du chapitre 16 restent : mémoire durable'),
      'en': ('BodyText', 'The layers of chapter 16 remain: durable memory')},
     {'fr': 'Une source d’autorité, pas une pile : l’agent lit le fichier daté au moment d’écrire, il ne « se souvient » pas',
      'en': 'One source of authority, not a pile: the agent reads the dated file when writing, it does not “remember”'},
     h=290)
def ch24_autorite(F, L):
    T = {'fr': dict(pile=['prompt d’avril', 'chat de mai', 'tableur', 'page Notion', 'mémoire du modèle'],
                    pile_t='la pile : cinq versions du délai', file='docs/regles.md',
                    lines=['Fait : délai d’annulation = 24 h', 'Date : 12 août 2026', 'Propriétaire : Nina'],
                    agent='Agent', read='lit à la demande', write='écrit à la cliente', out='« annulation possible jusqu’à 24 h avant »',
                    two='deux autorités = aucune', forbid='interdit : inventer 48 h, coller le délai dans le prompt'),
         'en': dict(pile=['April prompt', 'May chat', 'spreadsheet', 'Notion page', 'model memory'],
                    pile_t='the pile: five versions of the delay', file='docs/rules.md',
                    lines=['Fact: cancellation delay = 24 h', 'Date: 12 August 2026', 'Owner: Nina'],
                    agent='Agent', read='reads on demand', write='writes to the client', out='“cancellation possible up to 24 h before”',
                    two='two authorities = none', forbid='forbidden: inventing 48 h, pasting the delay into the prompt')}[L]
    # pile barrée
    for i, p in enumerate(T['pile']):
        y = 20 + i * 26
        F.rect(20, y, 200, 22, kind='ghost', radius=4, width=1)
        F.text(120, y + 11, p, pt=5.8, color='muted')
    F.line(20, 20, 220, 20 + 5 * 26 - 4, color=RED, width=1.6)
    F.text(120, 158, T['pile_t'], pt=5.8, color=RED, anchor='mt', max_w=200)
    F.text(120, 204, T['two'], pt=6.2, weight='Medium', color=RED)
    # fichier d'autorité
    F.rect(280, 30, 310, 110, kind='ok', radius=6)
    F.text(435, 46, T['file'], pt=7, weight='SemiBold')
    for i, l in enumerate(T['lines']):
        F.text(296, 70 + i * 20, l, pt=6, anchor='lm')
    # agent
    F.box(760, 55, 150, 60, T['agent'], kind='box', pt=8, weight='SemiBold')
    F.arrow(758, 85, 594, 85, head_size=8)
    F.text(676, 72, T['read'], pt=5.8, color='muted')
    F.arrow(835, 118, 835, 160, head_size=8)
    F.text(846, 138, T['write'], pt=5.8, color='muted', anchor='lm')
    F.box(620, 162, 360, 44, T['out'], kind='human', pt=6.2, weight='Regular')
    note(F, 280, 232, 700, T['forbid'], kind='risk', pt=6.1)


# ------------------------------------------------------------------ ch. 25

@fig('ch25-triade',
     {'fr': ('BodyText', 'Un code correct peut partir sous une identité non autorisée'),
      'en': ('BodyText', 'Correct code can leave under an unauthorised identity')},
     {'fr': 'Sécurité, qualité, gouvernance : trois questions distinctes, aucune ne remplace les deux autres',
      'en': 'Security, quality, governance: three distinct questions, none replaces the other two'},
     h=240)
def ch25_triade(F, L):
    T = {'fr': dict(items=[('Sécurité', 'qui peut faire quoi ?', 'identité, permissions, secrets, isolation'),
                           ('Qualité', 'le résultat est-il correct ?', 'critères, tests, contrats, non-régression'),
                           ('Gouvernance', 'qui décide et répond ?', 'propriétaires, approbations, journaux, audit')],
                    fails=['code correct, identité non autorisée', 'action autorisée, résultat faux', 'politique approuvée, jamais appliquée'],
                    act='une action agentique'),
         'en': dict(items=[('Security', 'who may do what?', 'identity, permissions, secrets, isolation'),
                           ('Quality', 'is the result correct?', 'criteria, tests, contracts, non-regression'),
                           ('Governance', 'who decides and answers?', 'owners, approvals, logs, audit')],
                    fails=['correct code, unauthorised identity', 'authorised action, false result', 'approved policy, never applied'],
                    act='one agentic action')}[L]
    w, gap = 296, 36
    kinds = ['risk', 'ok', 'human']
    F.box(330, 14, 340, 28, T['act'], kind='dark', pt=6.6, color='white')
    F.line(168, 58, 832, 58, color='rule')
    F.line(500, 42, 500, 58, color='rule')
    for i, (t, q, d) in enumerate(T['items']):
        x = 20 + i * (w + gap)
        F.arrow(x + w / 2, 58, x + w / 2, 76, head_size=7, color='rule')
        F.box(x, 78, w, 96, t, kind=kinds[i], sub=q + '\n' + d, pt=8.2, sub_pt=6)
        F.cross(x + 14, 200, r=4)
        F.text(x + 26, 200, T['fails'][i], pt=5.8, color='muted', anchor='lm', max_w=w - 30, align='left')


@fig('ch25-chaine',
     {'fr': ('CodeBlock', 'Identité : agent de release dans le dépôt du projet.'),
      'en': ('CodeBlock', 'Identity: release agent in the project repository.')},
     {'fr': 'La chaîne de contrôle d’une promotion en production : sept maillons, imposés par les permissions, les gates et les logs',
      'en': 'The control chain of a production promotion: seven links, enforced by permissions, gates and logs'},
     h=330, mode='replace_code')
def ch25_chaine(F, L):
    T = {'fr': [('Identité', 'agent de release dans le dépôt du projet'), ('Permission', 'lire la PR et déclencher staging, pas produire'),
                ('Outil', 'pipeline de déploiement limité'), ('Action', 'promouvoir une version déjà approuvée'),
                ('Preuve', 'gates CI, smoke test et checklist'), ('Approbation', 'responsable de la production'),
                ('Audit', 'run, version, heure, identité et décision')],
         'en': [('Identity', 'release agent in the project repository'), ('Permission', 'read the PR and trigger staging, not production'),
                ('Tool', 'limited deployment pipeline'), ('Action', 'promote an already approved version'),
                ('Evidence', 'CI gates, smoke test and checklist'), ('Approval', 'production owner'),
                ('Audit', 'run, version, time, identity and decision')]}[L]
    kinds = ['box', 'box', 'box', 'human', 'ok', 'human', 'ghost']
    n = len(T)
    rh, gap = 34, 8
    for i, (name, ex) in enumerate(T):
        y = 14 + i * (rh + gap)
        F.badge(30, y + rh / 2, str(i + 1), r=10, pt=6)
        F.box(52, y, 150, rh, name, kind=kinds[i], pt=6.8, weight='SemiBold')
        F.text(216, y + rh / 2, ex, pt=6.2, anchor='lm')
        if i < n - 1:
            F.arrow(127, y + rh + 1, 127, y + rh + gap - 1, head_size=5, color='rule')
    F.line(700, 14, 700, 14 + n * (rh + gap) - gap, color='rule') if False else None


# ------------------------------------------------------------------ ch. 26

@fig('ch26-maturite',
     {'fr': ('BodyText', 'Limite. Ce cadre ne dit pas « il faut scaler »'),
      'en': ('BodyText', 'Limit. This frame does not say “you must scale”')},
     {'fr': 'Le cadre de maturité : on monte seulement avec une preuve, on redescend après un incident',
      'en': 'The maturity frame: you move up only with evidence, you move down after an incident'},
     h=310)
def ch26_maturite(F, L):
    T = {'fr': dict(steps=[('0 — Prototype', 'chez vous, données fictives'), ('1 — MVP', 'un parcours réel, un apprentissage'),
                           ('2 — Production', 'vrais utilisateurs, chemin de retour'), ('3 — Maintenance', 'revues, dette, un non écrit')],
                    up='monter = une preuve', down='redescendre = un incident (ch. 40)', ax='ce que l’IA a le droit de faire s’élargit →',
                    thread='fil rouge : script local → une cliente confirmée → parcours en ligne avec rollback → budget et revue'),
         'en': dict(steps=[('0 — Prototype', 'on your machine, fake data'), ('1 — MVP', 'one real journey, one learning'),
                           ('2 — Production', 'real users, a way back'), ('3 — Maintenance', 'reviews, debt, a written no')],
                    up='moving up = evidence', down='moving down = an incident (ch. 40)', ax='what the AI may do widens →',
                    thread='thread: local script → one confirmed client → online journey with rollback → budget and review')}[L]
    rects = ladder(F, T['steps'], x0=30, x1=970, y_top=16, y_bottom=216, step_h=72, kinds=['ghost', 'box', 'box', 'ok'],
                   axis_label=T['ax'], pt=6.8, sub_pt=5.8)
    for i in range(3):
        x1, y1, w1, h1 = rects[i]
        x2, y2, w2, h2 = rects[i + 1]
        F.arrow(x1 + w1 + 2, y1 + 14, x2 - 2, y2 + 14, head_size=6, color=GREEN)
        F.arrow(x2 - 2, y2 + h2 - 14, x1 + w1 + 2, y1 + h1 - 14, head_size=6, color=RED)
    F.text(30, 276, T['up'], pt=6, color=GREEN, anchor='lm')
    F.text(970, 276, T['down'], pt=6, color=RED, anchor='rm')
    F.text(500, 298, T['thread'], pt=5.8, color='muted')


@fig('ch26-promotion',
     {'fr': ('CodeBlock', 'A[build] --> B[vérifications CI]'),
      'en': ('CodeBlock', 'A[build] --> B[CI checks]')},
     {'fr': 'La séquence de promotion : une suite de portes, la réussite d’une porte n’autorise pas à ignorer la suivante',
      'en': 'The promotion sequence: a series of gates, passing one gate does not authorise ignoring the next'},
     h=250, mode='replace_code')
def ch26_promotion(F, L):
    T = {'fr': ['build', 'vérifications CI', 'revue et approbation', 'déploiement staging', 'smoke tests', 'observation courte', 'promotion production', 'monitoring et décision'],
         'en': ['build', 'CI checks', 'review and approval', 'staging deployment', 'smoke tests', 'short observation', 'production promotion', 'monitoring and decision']}[L]
    gate = {'fr': 'porte', 'en': 'gate'}[L]
    rb = {'fr': 'rollback testé disponible à chaque porte', 'en': 'tested rollback available at every gate'}[L]
    kinds = ['ghost', 'box', 'human', 'box', 'ok', 'ok', 'risk', 'box']
    row1, row2 = T[:4], T[4:]
    k1, k2 = kinds[:4], kinds[4:]
    r1 = hflow(F, row1, y=24, h=52, x0=20, x1=980, gap=40, kinds=k1, pt=6.6)
    r2 = hflow(F, row2, y=124, h=52, x0=20, x1=980, gap=40, kinds=k2, pt=6.6)
    # liaison ligne 1 -> ligne 2
    x_end = r1[3][0] + r1[3][2] / 2
    x_start = r2[0][0] + r2[0][2] / 2
    F.polyline_arrow([(x_end, 78), (x_end, 100), (x_start, 100), (x_start, 122)])
    # marqueurs de porte
    for rects in (r1, r2):
        for i in range(3):
            x = rects[i][0] + rects[i][2] + 20
            F.line(x, 32, x, 72, color='#B0A8D8', width=1.2, dash=(3, 3)) if rects is r1 else F.line(x, 132, x, 172, color='#B0A8D8', width=1.2, dash=(3, 3))
    F.text(500, 200, gate + ' ×7 · ' + rb, pt=6, color='muted')


# ------------------------------------------------------------------ ch. 27

@fig('ch27-compatibilite',
     {'fr': ('CodeBlock', '5. supprimer l’ancien chemin après la période décidée.'),
      'en': ('CodeBlock', '5. remove the old path after the decided period.')},
     {'fr': 'La période de compatibilité : l’ancien et le nouveau format coexistent jusqu’à la date décidée',
      'en': 'The compatibility period: the old and the new format coexist until the decided date'},
     h=300)
def ch27_compatibilite(F, L):
    T = {'fr': dict(old='ancien format', new='nouveau format', steps=['1. ajouter le nouveau', '2. lecteurs comprennent les deux', '3. migrer les producteurs, observer', '4. annoncer la fin', '5. supprimer l’ancien'],
                    ax='temps →', period='période de compatibilité décidée'),
         'en': dict(old='old format', new='new format', steps=['1. add the new one', '2. readers understand both', '3. migrate producers, observe', '4. announce the end', '5. remove the old one'],
                    ax='time →', period='decided compatibility period')}[L]
    x0, x1 = 170, 960
    # bandes
    F.rect(x0, 30, 620, 26, kind='ghost', radius=4)
    F.text(x0 - 8, 43, T['old'], pt=6.2, color='muted', anchor='rm')
    F.rect(300, 70, x1 - 300, 26, kind='box', radius=4)
    F.text(x0 - 8, 83, T['new'], pt=6.2, color='muted', anchor='rm')
    # jalons
    xs = [300, 440, 580, 700, 800]
    for i, (x, st) in enumerate(zip(xs, T['steps'])):
        F.line(x, 24, x, 110, color='arrow', dash=(3, 3))
        F.badge(x, 122, str(i + 1), r=9, pt=5.8)
        F.text(x, 136, st[3:], pt=5.4, color='muted', anchor='mt', max_w=126)
    F.brace_label(300, 800, 216, T['period'], tick=4)
    F.axis(x0, 258, x1, 258, T['ax'], side='below')


# ------------------------------------------------------------------ ch. 28

@fig('ch28-tiroirs',
     {'fr': ('BodyText', 'Un ticket qui ne rentre dans aucun tiroir n’entre pas dans le sprint'),
      'en': ('BodyText', 'A ticket that fits in no drawer does not enter the sprint')},
     {'fr': 'Quatre tiroirs pour ranger une idée : chacun a sa question, sa preuve et sa suite',
      'en': 'Four drawers to file an idea: each has its question, its evidence and its next step'},
     h=270)
def ch28_tiroirs(F, L):
    T = {'fr': dict(idea='une idée, un ticket', items=[('Correction', 'l’offre actuelle est cassée', 'maintenant'),
                                                      ('Amélioration', 'même offre, moins de friction', 'une, puis re-marche'),
                                                      ('Nouvelle offre', 'autre travail à accomplir', 'retour ch. 8–11'),
                                                      ('Envie d’outil', 'un modèle, une mode', 'jamais, jusqu’à preuve')],
                    fog='aucun tiroir → pas de sprint : le brouillard'),
         'en': dict(idea='an idea, a ticket', items=[('Fix', 'the current offer is broken', 'now'),
                                                     ('Improvement', 'same offer, less friction', 'one, then re-walk'),
                                                     ('New offer', 'another job to be done', 'back to ch. 8–11'),
                                                     ('Tool craving', 'a model, a fashion', 'never, until proven')],
                    fog='no drawer → no sprint: the fog')}[L]
    F.box(380, 14, 240, 40, T['idea'], kind='human', pt=7)
    w, gap = 222, 24
    kinds = ['risk', 'box', 'ok', 'ghost']
    for i, (t, q, nxt) in enumerate(T['items']):
        x = 20 + i * (w + gap)
        F.arrow(500, 56, x + w / 2, 96, head_size=7, color='rule')
        F.box(x, 98, w, 78, t, kind=kinds[i], sub=q, pt=7.2, sub_pt=5.9)
        pill(F, x + w / 2, 196, nxt, kind='ghost', pt=5.6, h=17)
    F.text(500, 240, T['fog'], pt=6.2, color=RED)


# ------------------------------------------------------------------ ch. 29

@fig('ch29-trois-couches',
     {'fr': ('BodyText', 'La proposition de valeur décrit le travail. Le positionnement choisit le voisinage'),
      'en': ('BodyText', 'The value proposition describes the work. Positioning chooses the neighbourhood')},
     {'fr': 'Positionnement ≠ proposition de valeur ≠ offre : le voisinage choisi change la comparaison que fait le client',
      'en': 'Positioning ≠ value proposition ≠ offer: the chosen neighbourhood changes the comparison the customer makes'},
     h=260)
def ch29_trois_couches(F, L):
    T = {'fr': dict(items=[('Proposition de valeur', 'quel résultat, pour qui, à la place de quoi ?', 'ch. 9'),
                           ('Positionnement', 'dans quelle comparaison le client nous range-t-il ?', 'ici'),
                           ('Offre et prix', 'qu’achète-t-il, combien, comment on encaisse ?', 'ch. 30')],
                    a='« nous sommes une IA »', an='à côté de ChatGPT', b='« nous remplaçons la relance WhatsApp de la veille »', bn='à côté du soir volé'),
         'en': dict(items=[('Value proposition', 'what result, for whom, instead of what?', 'ch. 9'),
                           ('Positioning', 'in which comparison does the customer file us?', 'here'),
                           ('Offer and price', 'what do they buy, how much, how do we collect?', 'ch. 30')],
                    a='“we are an AI”', an='next to ChatGPT', b='“we replace the evening WhatsApp chase”', bn='next to the stolen evening')}[L]
    rects = vflow(F, [(t, q) for t, q, _ in T['items']], x=20, w=400, y0=16, h=60, gap=14, kinds=['human', 'box', 'ok'], pt=7, sub_pt=5.8)
    for (x, y, w, h), (_, _, ref) in zip(rects, T['items']):
        pill(F, x + w - 26, y + 2, ref, kind='ghost', pt=5.2, h=13, padx=5)
    # à droite : deux voisinages
    F.text(710, 24, '', pt=6)
    F.box(480, 40, 220, 44, T['a'], kind='ghost', pt=6.2, weight='Regular')
    F.arrow(702, 62, 740, 62, head_size=7)
    F.box(742, 40, 238, 44, T['an'], kind='risk', pt=6.4)
    F.box(480, 124, 220, 68, T['b'], kind='ghost', pt=6.2, weight='Regular')
    F.arrow(702, 158, 740, 158, head_size=7)
    F.box(742, 136, 238, 44, T['bn'], kind='ok', pt=6.4)
    F.line(440, 106, 476, 106, color='rule')
    F.line(476, 62, 476, 158, color='rule')
    F.line(476, 62, 478, 62, color='rule')


# ------------------------------------------------------------------ ch. 30

@fig('ch30-flux',
     {'fr': ('BodyText', 'Dans le fil rouge, l’outil de rendez-vous peut être techniquement prêt'),
      'en': ('BodyText', 'In the thread, the appointment tool can be technically ready')},
     {'fr': 'Du paiement au versement : ce que le client paie n’est pas ce qui arrive sur votre compte',
      'en': 'From payment to payout: what the customer pays is not what lands in your account'},
     h=250)
def ch30_flux(F, L):
    T = {'fr': dict(steps=['paiement client', 'frais plateforme et paiement', 'taxes de consommation éventuelles', 'remboursements, réserves, chargebacks', 'coûts directs de livraison', 'net avant impôt sur le revenu', 'versement'],
                    tail='puis : comptabilité et obligations du pays', who='qui est le vendeur légal ? dépend des conditions (processeur, plateforme, MoR)'),
         'en': dict(steps=['customer payment', 'platform and payment fees', 'possible consumption taxes', 'refunds, reserves, chargebacks', 'direct delivery costs', 'net before income tax', 'payout'],
                    tail='then: accounting and the country’s obligations', who='who is the legal seller? depends on the terms (processor, platform, MoR)')}[L]
    # cascade : barre qui diminue
    x0, w = 330, 560
    vals = [1.0, 0.9, 0.82, 0.74, 0.66, 0.66, 0.66]
    kinds = ['human', 'risk', 'risk', 'risk', 'risk', 'box', 'ok']
    for i, (st, v) in enumerate(zip(T['steps'], vals)):
        y = 14 + i * 27
        F.text_fit(x0 - 10, y + 10, st, x0 - 30, pt=6, anchor='rm', color='text' if i in (0, 5, 6) else 'muted')
        F.rect(x0, y, w * v, 20, kind=kinds[i], radius=3, width=1)
        if 0 < i < 5:
            F.text(x0 + w * v + 8, y + 10, '−', pt=7, color=RED, anchor='lm')
    F.text(500, 214, T['tail'], pt=6, color='muted')
    F.text(500, 234, T['who'], pt=6, color=RED)


@fig('ch30-encaisser',
     {'fr': ('BodyText', 'Un MoR peut simplifier une partie des ventes internationales'),
      'en': ('BodyText', 'A MoR can simplify part of international sales')},
     {'fr': 'Quatre rôles pour encaisser : qui porte quoi entre le client et vous',
      'en': 'Four roles to collect payment: who carries what between the customer and you'},
     h=270)
def ch30_encaisser(F, L):
    T = {'fr': dict(cli='Client', you='Vous', items=[('Processeur de paiement', 'transfère l’argent ; vous restez le vendeur'),
                                                  ('Plateforme de vente', 'page, checkout, livraison ; rôle légal selon ses conditions'),
                                                  ('Merchant of Record', 'vend la transaction, porte remboursements, litiges et taxes de consommation'),
                                                  ('Versement', 'calendrier, devise, seuil, frais — selon pays et compte')],
                    keep='reste chez vous : impôt sur le revenu, résidence fiscale, propriété intellectuelle, règles du produit'),
         'en': dict(cli='Customer', you='You', items=[('Payment processor', 'moves the money; you remain the seller'),
                                                   ('Sales platform', 'page, checkout, delivery; legal role per its terms'),
                                                   ('Merchant of Record', 'sells the transaction, carries refunds, disputes and consumption taxes'),
                                                   ('Payout', 'schedule, currency, threshold, fees — per country and account')],
                    keep='stays with you: income tax, tax residence, intellectual property, product rules')}[L]
    F.box(20, 75, 100, 60, T['cli'], kind='human', pt=7.4)
    F.box(880, 75, 100, 60, T['you'], kind='human', pt=7.4)
    xs = [150, 330, 510, 700]
    ws = [160, 160, 170, 160]
    kinds = ['ghost', 'ghost', 'box', 'ok']
    for i, (t, d) in enumerate(T['items']):
        F.box(xs[i], 30, ws[i], 150, t, kind=kinds[i], sub=d, pt=6.4, sub_pt=5.5)
    F.arrow(122, 105, 148, 105, head_size=6)
    F.arrow(xs[3] + ws[3] + 2, 105, 878, 105, head_size=6)
    for i in range(3):
        F.arrow(xs[i] + ws[i] + 2, 105, xs[i + 1] - 2, 105, head_size=6, color='rule')
    note(F, 20, 200, 960, T['keep'], kind='human', pt=6)


# ------------------------------------------------------------------ ch. 31

@fig('ch31-entretien',
     {'fr': ('BodyText', 'Préparez une page, pas un argumentaire.'),
      'en': ('BodyText', 'Prepare a page, not a brief.')},
     {'fr': 'L’entretien de vingt minutes : qualifier, démontrer, traiter une objection, demander la décision',
      'en': 'The twenty-minute interview: qualify, demonstrate, handle one objection, ask for the decision'},
     h=250)
def ch31_entretien(F, L):
    T = {'fr': dict(steps=[('Qualifier', '5 min · trois faits', 'dernier épisode, alternative, qui paie'), ('Démontrer', '5 min · le parcours du ch. 21', '« c’est mon jeudi » ou « c’est joli »'),
                           ('Objection', '5 min · un fait ou une peur', 'répondre à cela, pas « écraser »'), ('Décision', '5 min · une phrase', 'OUI / NON / date — pas de brouillard')],
                    stop='pas de problème récent ou aucun moyen de payer → arrêter, proposer le carnet du ch. 8', ax='0 → 20 min'),
         'en': dict(steps=[('Qualify', '5 min · three facts', 'last episode, alternative, who pays'), ('Demonstrate', '5 min · the journey of ch. 21', '“that’s my Thursday” or “that’s pretty”'),
                           ('Objection', '5 min · a fact or a fear', 'answer that, do not “crush” it'), ('Decision', '5 min · one sentence', 'YES / NO / date — no fog')],
                    stop='no recent problem or no way to pay → stop, offer the ch. 8 notebook', ax='0 → 20 min')}[L]
    items = [(t, s1 + '\n' + s2) for t, s1, s2 in T['steps']]
    rects = hflow(F, items, y=30, h=96, x0=20, x1=980, gap=18, kinds=['human', 'box', 'box', 'ok'], pt=7.2, sub_pt=5.7)
    F.axis(20, 146, 980, 146, T['ax'], side='below')
    x, y, w, h = rects[0]
    F.polyline_arrow([(x + w / 2, 128), (x + w / 2, 196), (x + w / 2 + 20, 196)], color=RED)
    F.text(x + w / 2 + 28, 196, T['stop'], pt=5.9, color=RED, anchor='lm', max_w=760, align='left')


# ------------------------------------------------------------------ ch. 32

@fig('ch32-canal',
     {'fr': ('BodyText', 'Ce n’est pas encore le CAC du chapitre 34'),
      'en': ('BodyText', 'This is not yet the CAC of chapter 34')},
     {'fr': 'Portée n’est pas pipeline : ce qui compte est le coût d’une conversation utile, pas le nombre de vues',
      'en': 'Reach is not pipeline: what counts is the cost of a useful conversation, not the number of views'},
     h=260)
def ch32_canal(F, L):
    T = {'fr': dict(levels=[('vues, likes, réactions', 'portée'), ('DM « c’est quoi le prix ? » sans profil', 'bruit'),
                            ('conversation utile', 'bon profil, épisode réel possible, joignable'), ('entretien (ch. 31)', 'le canal nourrit la vente')],
                    formula='coût d’une conversation utile = (temps + argent du canal) / conversations réellement qualifiables',
                    one='un canal, trente jours, puis décision'),
         'en': dict(levels=[('views, likes, reactions', 'reach'), ('DM “what’s the price?” without a profile', 'noise'),
                            ('useful conversation', 'right profile, real episode possible, reachable'), ('interview (ch. 31)', 'the channel feeds the sale')],
                    formula='cost of a useful conversation = (time + money of the channel) / conversations that can really be qualified',
                    one='one channel, thirty days, then a decision')}[L]
    # entonnoir : largeurs décroissantes
    ws = [760, 560, 380, 240]
    kinds = ['ghost', 'ghost', 'ok', 'ok']
    cx = 500
    for i, ((lab, sub), w) in enumerate(zip(T['levels'], ws)):
        y = 14 + i * 44
        F.box(cx - w / 2, y, w, 36, lab, kind=kinds[i], sub=None, pt=6.4, weight='Medium')
        F.text(cx + w / 2 + 12, y + 18, sub, pt=5.7, color='muted', anchor='lm', max_w=cx - w / 2 - 20, align='left')
    note(F, 20, 196, 960, T['formula'], kind='human', pt=6)
    F.text(500, 244, T['one'], pt=6, color='muted')


# ------------------------------------------------------------------ ch. 33

@fig('ch33-activation',
     {'fr': ('BodyText', 'Le temps jusqu’à l’activation compte autant que le taux'),
      'en': ('BodyText', 'Time to activation counts as much as the rate')},
     {'fr': 'Activation, rétention, churn : le moment de valeur doit arriver dans les premières 48 heures, pas au jour 12',
      'en': 'Activation, retention, churn: the moment of value must arrive in the first 48 hours, not on day 12'},
     h=300)
def ch33_activation(F, L):
    T = {'fr': dict(defs=[('Activation', 'première confirmation réellement obtenue — pas un login'),
                          ('Rétention', 'au moins une confirmation par semaine d’activité'),
                          ('Churn', '14 jours sans confirmation, ou « arrêtez »')],
                    ax='jours après le paiement →', h48='48 h', pay='paiement', act='activation', d12='jour 12 : beaucoup sont déjà parties',
                    conf='confirmations', churn='14 j sans confirmation'),
         'en': dict(defs=[('Activation', 'first confirmation actually obtained — not a login'),
                          ('Retention', 'at least one confirmation per active week'),
                          ('Churn', '14 days without confirmation, or “stop”')],
                    ax='days after payment →', h48='48 h', pay='payment', act='activation', d12='day 12: many have already left',
                    conf='confirmations', churn='14 d without confirmation')}[L]
    hflow(F, T['defs'], y=14, h=70, x0=20, x1=980, gap=24, kinds=['ok', 'box', 'risk'], pt=7.2, sub_pt=5.8)
    x0, x1 = 60, 960
    y = 236
    def X(d):
        return x0 + d * ((x1 - 40 - x0) / 30)
    F.arrow(x0, y, x1, y, color='rule', width=1.2, head_size=8)
    for d in range(0, 31, 5):
        F.line(X(d), y - 3, X(d), y + 3, color='rule')
        F.text(X(d), y + 6, str(d), pt=5, color='muted', anchor='mt')
    F.text(x1, y + 30, T['ax'], pt=6, color='muted', anchor='rm')
    # fenêtre 48 h
    F.rect(X(0), 150, X(2) - X(0), 82, kind='ok', radius=3, width=1)
    F.text(X(2) + 6, 160, T['h48'], pt=6.2, weight='SemiBold', color=GREEN, anchor='lm')
    F.text(X(2) + 6, 176, T['act'], pt=5.8, color=GREEN, anchor='lm')
    F.circle(X(0), y, 5, kind='human')
    F.text(X(0) - 8, 143, T['pay'], pt=5.6, color='muted', anchor='lb')
    F.circle(X(1.3), y, 6, kind='ok')
    # rétention : une confirmation par semaine
    for d in (6, 13, 20, 27):
        F.circle(X(d), y, 4, kind='box')
    F.line(X(6), 200, X(27), 200, color='rule')
    F.text(X(6), 194, T['conf'], pt=5.6, color='muted', anchor='lb')
    # churn : 14 jours sans confirmation
    F.line(X(16), 218, X(30), 218, color=RED, dash=(4, 3))
    F.text(X(30), 212, T['churn'], pt=5.6, color=RED, anchor='rb')
    # jour 12
    F.line(X(12), 126, X(12), y - 6, color=RED, dash=(3, 3))
    F.text(X(12) + 6, 126, T['d12'], pt=5.7, color=RED, anchor='lt', max_w=210, align='left')


# ------------------------------------------------------------------ ch. 34

@fig('ch34-marge',
     {'fr': ('BodyText', 'Les chiffres sont un exemple. Changez la devise, le tarif, le taux'),
      'en': ('BodyText', 'The figures are an example. Change the currency, the rate, the ratio')},
     {'fr': 'Une ligne sans temps n’est pas une ligne : la marge « tableau de bord » contre la marge de contribution',
      'en': 'A line without time is not a line: the “dashboard” margin versus the contribution margin'},
     h=260)
def ch34_marge(F, L):
    T = {'fr': dict(a='Sans le temps de Nina', b='Avec le temps de Nina',
                    rows_a=[('Prix', 29.0), ('Frais paiement / plateforme', -3.0), ('Envoi', -0.4), ('Jetons', -0.2)], tot_a=('Marge « tableau de bord »', 25.4),
                    rows_b=[('Support + envoi (20 min)', -8.0), ('Remboursement attendu (1/10)', -2.9)], tot_b=('Marge de contribution', 14.5), lie='mensonge fréquent : une ligne sans temps', dec='la ligne qui décide'),
         'en': dict(a='Without Nina’s time', b='With Nina’s time',
                    rows_a=[('Price', 29.0), ('Payment / platform fees', -3.0), ('Sending', -0.4), ('Tokens', -0.2)], tot_a=('“Dashboard” margin', 25.4),
                    rows_b=[('Support + sending (20 min)', -8.0), ('Expected refund (1/10)', -2.9)], tot_b=('Contribution margin', 14.5), lie='frequent lie: a line without time', dec='the line that decides')}[L]
    def fmt(v):
        s = ('%.2f' % abs(v)).replace('.', ',' if L == 'fr' else '.')
        return ('−' if v < 0 else '') + s
    (lx, ly, lw, lh), (rx, ry, rw, rh) = compare(F, T['a'], T['b'], y=14, h=220, kinds=('ghost', 'box'))
    # gauche
    yy = ly + 14
    for lab, v in T['rows_a']:
        F.text(lx + 14, yy, lab, pt=6, anchor='lm')
        F.text(lx + lw - 14, yy, fmt(v), pt=6, anchor='rm', color='text' if v > 0 else RED)
        yy += 22
    F.line(lx + 14, yy - 6, lx + lw - 14, yy - 6, color='rule')
    F.text(lx + 14, yy + 8, T['tot_a'][0], pt=6.2, weight='SemiBold', anchor='lm')
    F.text(lx + lw - 14, yy + 8, fmt(T['tot_a'][1]), pt=6.4, weight='SemiBold', anchor='rm')
    # barre
    F.rect(lx + 14, yy + 26, (lw - 28) * 25.4 / 29, 12, kind='human', radius=3)
    F.text(lx + lw / 2, yy + 54, T['lie'], pt=5.8, color=RED)
    # droite
    yy = ry + 14
    F.text(rx + 14, yy, T['tot_a'][0], pt=6, anchor='lm', color='muted')
    F.text(rx + rw - 14, yy, fmt(25.4), pt=6, anchor='rm', color='muted')
    yy += 22
    for lab, v in T['rows_b']:
        F.text(rx + 14, yy, lab, pt=6, anchor='lm')
        F.text(rx + rw - 14, yy, fmt(v), pt=6, anchor='rm', color=RED)
        yy += 22
    F.line(rx + 14, yy - 6, rx + rw - 14, yy - 6, color='rule')
    F.text(rx + 14, yy + 8, T['tot_b'][0], pt=6.2, weight='SemiBold', anchor='lm')
    F.text(rx + rw - 14, yy + 8, fmt(T['tot_b'][1]), pt=6.4, weight='SemiBold', anchor='rm')
    F.rect(rx + 14, yy + 26, (rw - 28) * 14.5 / 29, 12, kind='ok', radius=3)
    F.rect(rx + 14 + (rw - 28) * 14.5 / 29, yy + 26, (rw - 28) * (25.4 - 14.5) / 29, 12, kind='risk', radius=3)
    F.text(rx + rw / 2, yy + 54, T['dec'], pt=5.8, color=GREEN)


@fig('ch34-ltv-cac',
     {'fr': ('BodyText', 'Ces formules sont des ordres de grandeur'),
      'en': ('BodyText', 'These formulas are orders of magnitude')},
     {'fr': 'LTV / CAC sur le fil rouge : 58 contre 72 — une vente de plus, à ce canal, ne suffit pas',
      'en': 'LTV / CAC on the thread: 58 against 72 — one more sale, through this channel, is not enough'},
     h=260)
def ch34_ltv_cac(F, L):
    T = {'fr': dict(cac='CAC ≈ coût du canal / clients payants', cacv='6 h × 24 = 144, pour 2 oui → 72',
                    ltv='LTV ≈ marge de contribution × périodes avant départ', ltvv='14,50 × 4 mois → 58',
                    verdict='LTV / CAC ≈ 58 / 72 < 1', so='WAIT ou PIVOT : canal (32), prix (30), support (33) — pas « plus d’agents »',
                    date='hypothèses datées, recalculées — pas un 3:1 lu dans un article'),
         'en': dict(cac='CAC ≈ channel cost / paying customers', cacv='6 h × 24 = 144, for 2 yeses → 72',
                    ltv='LTV ≈ contribution margin × periods before leaving', ltvv='14.50 × 4 months → 58',
                    verdict='LTV / CAC ≈ 58 / 72 < 1', so='WAIT or PIVOT: channel (32), price (30), support (33) — not “more agents”',
                    date='dated assumptions, recalculated — not a 3:1 read in an article')}[L]
    # deux barres comparées
    F.box(20, 14, 440, 78, T['ltv'], kind='ok', sub=T['ltvv'], pt=6.4, sub_pt=6)
    F.box(540, 14, 440, 78, T['cac'], kind='risk', sub=T['cacv'], pt=6.4, sub_pt=6)
    scale = 800 / 72
    F.text(80, 118, 'LTV', pt=6.4, weight='SemiBold', anchor='rm')
    F.rect(100, 108, 58 * scale, 20, kind='ok', radius=3)
    F.text(100 + 58 * scale + 8, 118, '58', pt=6.4, anchor='lm')
    F.text(80, 148, 'CAC', pt=6.4, weight='SemiBold', anchor='rm')
    F.rect(100, 138, 72 * scale, 20, kind='risk', radius=3)
    F.text(100 + 72 * scale + 8, 148, '72', pt=6.4, anchor='lm')
    F.text(500, 186, T['verdict'], pt=7.4, weight='SemiBold', color=RED)
    F.text(500, 210, T['so'], pt=6, color='text')
    F.text(500, 236, T['date'], pt=5.8, color='muted')


# ------------------------------------------------------------------ ch. 35

@fig('ch35-boucle',
     {'fr': ('BodyText', 'Si chaque vente recommence à zéro (dix nouveaux messages froids)'),
      'en': ('BodyText', 'If each sale starts from zero (ten new cold messages)')},
     {'fr': 'Une boucle, pas un moulin : le résultat d’un tour alimente le tour suivant',
      'en': 'A loop, not a treadmill: the result of one turn feeds the next'},
     h=320)
def ch35_boucle(F, L):
    T = {'fr': dict(items=[('Client activé', ''), ('Résultat tenu', 'ch. 21, 33'), ('Preuve racontable ou introduction', ''), ('Nouvelle conversation utile', 'ch. 32'), ('Vente', 'ch. 31')],
                    mill='le moulin : dix messages froids à chaque vente — il tourne tant que vous pédalez', goulet='goulet : un seul point à traiter'),
         'en': dict(items=[('Activated customer', ''), ('Result held', 'ch. 21, 33'), ('Tellable proof or introduction', ''), ('New useful conversation', 'ch. 32'), ('Sale', 'ch. 31')],
                    mill='the treadmill: ten cold messages for each sale — it turns as long as you pedal', goulet='bottleneck: a single point to treat')}[L]
    items = [(t, s or None) for t, s in T['items']]
    cycle(F, items, cx=500, cy=140, rx=330, ry=98, bw=220, bh=68, kinds=['ok', 'ok', 'human', 'box', 'human'], pt=6.2, sub_pt=5.4,
          center_label=None)
    F.text(500, 140, '↻', pt=14, color='rule')
    F.text(500, 262, T['goulet'], pt=6, color='muted')
    note(F, 20, 282, 960, T['mill'], kind='risk', pt=6)
