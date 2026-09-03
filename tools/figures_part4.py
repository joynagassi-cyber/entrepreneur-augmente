# -*- coding: utf-8 -*-
"""Figures explicatives — Partie VI (chapitres 36 à 42) et annexes."""
from figlib import *

RED = '#D0665A'
GREEN = '#4E9C64'


# ------------------------------------------------------------------ ch. 36

@fig('ch36-modes',
     {'fr': ('BodyText', 'Le mode n’est pas un statut social. Il change par tâche'),
      'en': ('BodyText', 'The mode is not a social status. It changes by task')},
     {'fr': 'Quatre modes de travail, choisis par tâche : la part de l’IA grandit seulement là où le périmètre est prouvé',
      'en': 'Four working modes, chosen per task: the AI’s share grows only where the perimeter is proven'},
     h=280)
def ch36_modes(F, L):
    T = {'fr': dict(items=[('Humain seul', 'l’IA n’entre pas', 'entretien de vente, prix, excuse, KILL'),
                           ('IA sous revue', 'elle produit, un humain envoie', 'brouillon de confirmation'),
                           ('IA bornée', 'elle agit dans un périmètre prouvé (banc ch. 23)', 'classer des notes anonymisées'),
                           ('Interdit à l’IA', 'même le brouillon est trop risqué ou trop formateur', 'décision GO, premier message d’incident')],
                    ax='part de l’IA dans la tâche →', down='redescend après un incident (ch. 40)', per='par tâche, pas par personne'),
         'en': dict(items=[('Human only', 'the AI does not enter', 'sales interview, price, apology, KILL'),
                           ('AI under review', 'it produces, a human sends', 'confirmation draft'),
                           ('Bounded AI', 'it acts within a proven perimeter (bench ch. 23)', 'sort anonymised notes'),
                           ('Forbidden to AI', 'even the draft is too risky or too formative', 'GO decision, first incident message')],
                    ax='AI share in the task →', down='goes down after an incident (ch. 40)', per='per task, not per person')}[L]
    w, gap = 220, 22
    kinds = ['human', 'box', 'box', 'risk']
    shares = [0.0, 0.5, 0.85, None]
    for i, (t, d, ex) in enumerate(T['items']):
        x = 20 + i * (w + gap)
        F.box(x, 16, w, 104, t, kind=kinds[i], sub=d + '\n— ' + ex, pt=7.2, sub_pt=5.7)
        # jauge
        F.rect(x, 132, w, 12, kind='ghost', radius=3, width=1)
        if shares[i] is None:
            F.cross(x + w / 2, 138, r=5)
        else:
            F.rect(x, 132, w * shares[i], 12, kind='box', radius=3, width=1)
    F.axis(20, 160, 20 + 3 * (w + gap) + w - 242, 160, T['ax'], side='below')
    F.text(500, 210, T['per'], pt=6.2, color='muted')
    F.arrow(740, 236, 260, 236, head_size=7, color=RED)
    F.text(500, 252, T['down'], pt=6, color=RED)


# ------------------------------------------------------------------ ch. 37

@fig('ch37-modeles',
     {'fr': ('CodeBlock', 'subgraph A[A — Coordinateur et workers]'),
      'en': ('CodeBlock', 'subgraph A[A — Coordinator and workers]')},
     {'fr': 'Quatre formes de collaboration entre agents : le modèle se choisit pour la forme des dépendances et la preuve disponible',
      'en': 'Four shapes of collaboration between agents: the model is chosen for the shape of the dependencies and the available evidence'},
     h=330, mode='replace_code')
def ch37_modeles(F, L):
    T = {'fr': dict(a='A — Coordinateur et workers', b='B — Handoffs spécialisés', c='C — Parallèle puis agrégation', d='D — Séquence gouvernée',
                    coord='Coordinateur', worker='Worker', ag1='Agent 1', ag2='Agent 2', an='Analyse', agg='Agrégateur',
                    seq=['Spec', 'Implémentation', 'Vérification', 'Documentation'],
                    when=['dépendances fortes, traçabilité prioritaire', 'chaque étape a une preuve différente', 'tâches vraiment indépendantes', 'un artefact utile par étape']),
         'en': dict(a='A — Coordinator and workers', b='B — Specialised handoffs', c='C — Parallel then aggregation', d='D — Governed sequence',
                    coord='Coordinator', worker='Worker', ag1='Agent 1', ag2='Agent 2', an='Analysis', agg='Aggregator',
                    seq=['Spec', 'Implementation', 'Verification', 'Documentation'],
                    when=['strong dependencies, traceability first', 'each step has a different proof', 'truly independent tasks', 'one useful artefact per step'])}[L]
    pw, ph, gx, gy = 470, 140, 20, 18
    panels = [(20, 14), (20 + pw + gx, 14), (20, 14 + ph + gy), (20 + pw + gx, 14 + ph + gy)]
    titles = [T['a'], T['b'], T['c'], T['d']]
    for (x, y), t, w_ in zip(panels, titles, T['when']):
        F.rect(x, y, pw, ph, kind='ghost', radius=8, width=1.1)
        F.text(x + 10, y + 14, t, pt=6.6, weight='SemiBold', anchor='lm')
        F.text(x + pw - 10, y + ph - 12, w_, pt=5.4, color='muted', anchor='rm')
    # A
    x, y = panels[0]
    F.box(x + 30, y + 52, 130, 36, T['coord'], kind='box', pt=6.4)
    F.box(x + 260, y + 34, 110, 30, T['worker'], kind='box', pt=6.2)
    F.box(x + 260, y + 78, 110, 30, T['worker'], kind='box', pt=6.2)
    F.arrow(x + 162, y + 66, x + 256, y + 49, head_size=6)
    F.arrow(x + 162, y + 74, x + 256, y + 93, head_size=6)
    # B
    x, y = panels[1]
    F.box(x + 60, y + 54, 130, 36, T['ag1'], kind='box', pt=6.4)
    F.box(x + 280, y + 54, 130, 36, T['ag2'], kind='box', pt=6.4)
    F.arrow(x + 192, y + 72, x + 276, y + 72, label='handoff', head_size=6, pt=5.4, label_offset=(0, -9))
    # C
    x, y = panels[2]
    F.box(x + 40, y + 34, 130, 30, T['an'] + ' 1', kind='box', pt=6.2)
    F.box(x + 40, y + 78, 130, 30, T['an'] + ' 2', kind='box', pt=6.2)
    F.box(x + 290, y + 52, 130, 36, T['agg'], kind='human', pt=6.4)
    F.arrow(x + 172, y + 49, x + 286, y + 66, head_size=6)
    F.arrow(x + 172, y + 93, x + 286, y + 74, head_size=6)
    # D
    x, y = panels[3]
    kk = ['human', 'box', 'ok', 'ghost']
    bw2, bh2 = 180, 30
    pos = [(x + 40, y + 34), (x + 250, y + 34), (x + 250, y + 84), (x + 40, y + 84)]
    for i, (lab, (bx, by)) in enumerate(zip(T['seq'], pos)):
        F.box(bx, by, bw2, bh2, lab, kind=kk[i], pt=6.2)
    F.arrow(x + 40 + bw2 + 2, y + 49, x + 250 - 2, y + 49, head_size=6)
    F.arrow(x + 250 + bw2 / 2, y + 66, x + 250 + bw2 / 2, y + 82, head_size=6)
    F.arrow(x + 250 - 2, y + 99, x + 40 + bw2 + 2, y + 99, head_size=6)


# ------------------------------------------------------------------ ch. 38

@fig('ch38-roles',
     {'fr': ('BodyText', 'L’agent peut exécuter un brouillon. Il n’autorise pas. Il ne répond pas.'),
      'en': ('BodyText', 'The agent can execute a draft. It does not authorise. It does not answer.')},
     {'fr': 'Quatre rôles sur une même action : l’agent peut exécuter un brouillon, il n’autorise pas et ne répond pas',
      'en': 'Four roles on the same action: the agent can execute a draft, it does not authorise and does not answer'},
     h=250)
def ch38_roles(F, L):
    T = {'fr': dict(roles=[('Autorise', 'a-t-on le droit de le faire maintenant ?', 'Nina, note datée'),
                           ('Exécute', 'qui produit le geste ?', 'agent (brouillon) ou Nina'),
                           ('Revue', 'qui voit avant que ce soit irréversible ?', 'Nina ou freelance (ch. 36)'),
                           ('Répond', 'qui assume si ça casse ?', 'toujours un humain nommé')],
                    act='message tarifaire à une cliente', agent='agent : possible', human='humain seulement'),
         'en': dict(roles=[('Authorises', 'are we allowed to do it now?', 'Nina, dated note'),
                           ('Executes', 'who produces the gesture?', 'agent (draft) or Nina'),
                           ('Reviews', 'who sees before it becomes irreversible?', 'Nina or freelancer (ch. 36)'),
                           ('Answers', 'who takes it if it breaks?', 'always a named human')],
                    act='pricing message to a client', agent='agent: possible', human='human only')}[L]
    F.box(330, 12, 340, 30, T['act'], kind='dark', pt=6.6, color='white')
    w, gap = 220, 22
    kinds = ['human', 'box', 'human', 'human']
    for i, (r, q, who) in enumerate(T['roles']):
        x = 20 + i * (w + gap)
        F.arrow(500, 44, x + w / 2, 66, head_size=6, color='rule')
        F.box(x, 68, w, 92, r, kind=kinds[i], sub=q + '\n' + who, pt=7.4, sub_pt=5.7)
        tag = T['agent'] if i == 1 else T['human']
        pill(F, x + w / 2, 180, tag, kind='box' if i == 1 else 'human', pt=5.6, h=17)
    note_t = {'fr': 'fusionner les quatre dans « Nina + l’agent » = autonomie déguisée', 'en': 'merging the four into “Nina + the agent” = disguised autonomy'}[L]
    F.text(500, 222, note_t, pt=6.2, color=RED)


# ------------------------------------------------------------------ ch. 39

@fig('ch39-environnement',
     {'fr': ('BodyText', 'Ces composants ne sont pas tous des produits séparés'),
      'en': ('BodyText', 'These components are not all separate products')},
     {'fr': 'L’environnement d’un run : ce qui entoure l’agent pour qu’il agisse dans un périmètre, avec un état et une escalade',
      'en': 'The environment of a run: what surrounds the agent so it acts within a perimeter, with a state and an escalation'},
     h=330)
def ch39_environnement(F, L):
    T = {'fr': dict(agent='Agent', run='un run',
                    inputs=[('Déclencheur', 'demande, événement, horaire, pipeline'), ('Identité', 'agent, utilisateur ou service'), ('Mémoire et contexte', 'documents et règles nécessaires')],
                    inside=[('État', 'étape, décisions, prochaine action'), ('Workspace', 'fichiers, branche, données isolés'), ('Outils', 'opérations disponibles'), ('Permissions', 'capacités attachées à la tâche')],
                    outputs=[('Vérification', 'tests, contrats, conditions de passage'), ('Observabilité', 'événements, coûts, durées, appels'), ('Arrêt et reprise', 'pause, checkpoint, rollback'), ('Escalade', 'condition et destinataire')]),
         'en': dict(agent='Agent', run='one run',
                    inputs=[('Trigger', 'request, event, schedule, pipeline'), ('Identity', 'agent, user or service'), ('Memory and context', 'necessary documents and rules')],
                    inside=[('State', 'step, decisions, next action'), ('Workspace', 'isolated files, branch, data'), ('Tools', 'available operations'), ('Permissions', 'capabilities attached to the task')],
                    outputs=[('Verification', 'tests, contracts, pass conditions'), ('Observability', 'events, costs, durations, calls'), ('Stop and resume', 'pause, checkpoint, rollback'), ('Escalation', 'condition and recipient')])}[L]
    # colonne gauche : entrées
    for i, (t, d) in enumerate(T['inputs']):
        y = 30 + i * 92
        F.box(20, y, 210, 70, t, kind='human' if i == 0 else 'ghost', sub=d, pt=6.6, sub_pt=5.5)
        F.arrow(232, y + 35, 268, y + 35, head_size=6)
    # cadre du run
    F.rect(270, 14, 440, 300, kind='ghost', radius=10, width=1.2, dash=True)
    F.text(282, 26, T['run'], pt=6.2, weight='SemiBold', color='muted', anchor='lm')
    F.box(410, 44, 160, 44, T['agent'], kind='box', pt=8.2, weight='SemiBold')
    for i, (t, d) in enumerate(T['inside']):
        col, row = i % 2, i // 2
        x = 286 + col * 210
        y = 112 + row * 94
        F.box(x, y, 196, 76, t, kind='box', sub=d, pt=6.4, sub_pt=5.4)
    F.line(490, 90, 490, 108, color='rule')
    F.line(384, 108, 596, 108, color='rule')
    F.arrow(384, 108, 384, 110, head_size=5, color='rule')
    F.arrow(596, 108, 596, 110, head_size=5, color='rule')
    # colonne droite : sorties / contrôles
    for i, (t, d) in enumerate(T['outputs']):
        y = 20 + i * 76
        F.box(760, y, 220, 68, t, kind='ok' if i < 2 else 'human', sub=d, pt=6.4, sub_pt=5.4)
        F.arrow(712, y + 34, 756, y + 34, head_size=6)


@fig('ch39-autonomie-risque',
     {'fr': ('BodyText', 'La règle n’est pas « toujours demander une confirmation »'),
      'en': ('BodyText', 'The rule is not “always ask for a confirmation”')},
     {'fr': 'L’autonomie suit le risque : plus l’action est irréversible ou externe, plus le degré de liberté baisse et le contrôle monte',
      'en': 'Autonomy follows risk: the more irreversible or external the action, the lower the freedom and the higher the control'},
     h=300)
def ch39_autonomie_risque(F, L):
    T = {'fr': dict(rows=[('Résumer des notes anonymisées', 'élevée', 'sources et format'),
                          ('Modifier une branche de code', 'moyenne', 'périmètre, tests et revue'),
                          ('Envoyer un message à un client', 'faible à moyenne', 'brouillon, destinataire et approbation'),
                          ('Modifier une réservation réelle', 'faible', 'autorisation, confirmation et audit'),
                          ('Migrer une base', 'très faible', 'dry-run, sauvegarde, gate et rollback')],
                    h1='action', h2='autonomie raisonnable', h3='contrôle attendu', ax='risque : irréversible, coûteux, sensible, externe, difficile à vérifier',
                    rule='relier le degré de liberté à la possibilité de prouver, d’annuler et d’attribuer l’action'),
         'en': dict(rows=[('Summarise anonymised notes', 'high', 'sources and format'),
                          ('Modify a code branch', 'medium', 'scope, tests and review'),
                          ('Send a message to a customer', 'low to medium', 'draft, recipient and approval'),
                          ('Modify a real booking', 'low', 'authorisation, confirmation and audit'),
                          ('Migrate a database', 'very low', 'dry-run, backup, gate and rollback')],
                    h1='action', h2='reasonable autonomy', h3='expected control', ax='risk: irreversible, costly, sensitive, external, hard to verify',
                    rule='tie the degree of freedom to the ability to prove, undo and attribute the action')}[L]
    levels = [1.0, 0.65, 0.42, 0.25, 0.1]
    top, rh, gap = 34, 34, 8
    F.text(30, 16, T['h1'], pt=6, weight='SemiBold', color='muted', anchor='lm')
    F.text(420, 16, T['h2'], pt=6, weight='SemiBold', color='muted', anchor='lm')
    F.text(660, 16, T['h3'], pt=6, weight='SemiBold', color='muted', anchor='lm')
    for i, (act, aut, ctl) in enumerate(T['rows']):
        y = top + i * (rh + gap)
        kind = 'ok' if i == 0 else ('box' if i < 3 else 'risk')
        F.box(20, y, 380, rh, act, kind=kind, pt=6.4, weight='Medium', align='left', pad=10)
        F.rect(420, y + rh / 2 - 8, 200, 16, kind='ghost', radius=4, width=1)
        F.rect(420, y + rh / 2 - 8, 200 * levels[i], 16, kind='ok' if levels[i] > 0.5 else ('human' if levels[i] > 0.2 else 'risk'), radius=4, width=1)
        F.text(628, y + rh / 2, aut, pt=5.4, color='muted', anchor='lm') if False else None
        F.text_fit(660, y + rh / 2, ctl, 320, pt=5.9, color='text')
    yb = top + 5 * (rh + gap)
    F.axis(10, top, 10, yb - gap, T['ax'], side='right') if False else None
    F.axis(408, top, 408, yb - gap, '', side='right')
    F.text(500, yb + 4, T['ax'], pt=5.8, color=RED, anchor='mt')
    F.text(500, yb + 24, T['rule'], pt=6, color='muted', anchor='mt')


# ------------------------------------------------------------------ ch. 40

@fig('ch40-rollbacks',
     {'fr': ('BodyText', 'Les deux sont nécessaires. Ni l’un ni l’autre n’est « plus noble »'),
      'en': ('BodyText', 'Both are necessary. Neither is “nobler”')},
     {'fr': 'Deux rollbacks, deux objets : le revert du système ne prévient pas la cliente ; le message de correction passe avant',
      'en': 'Two rollbacks, two objects: reverting the system does not warn the client; the correction message comes first'},
     h=340)
def ch40_rollbacks(F, L):
    T = {'fr': dict(inc='Incident : rappel parti avec 10 h 30 au lieu de 10 h, à trois clientes',
                    a='Rollback métier — d’abord', b='Rollback technique — ensuite',
                    ai=['objet : ce que la cliente a vu, payé, cru', 'geste : message correctif, appel, remboursement', 'succès : plus personne n’agit sur l’heure fausse'],
                    bi=['objet : code, config, prompt, donnée système', 'geste : revenir à une version, un checkpoint', 'succès : le système est dans un état connu'],
                    trap_a='piège : un « désolé » n’annule pas un paiement', trap_b='piège : croire que le revert prévient la cliente', minute='chaque minute, le mensonge vieillit'),
         'en': dict(inc='Incident: reminder sent with 10:30 instead of 10:00, to three clients',
                    a='Business rollback — first', b='Technical rollback — then',
                    ai=['object: what the client saw, paid, believed', 'gesture: corrective message, call, refund', 'success: nobody acts on a false time anymore'],
                    bi=['object: code, config, prompt, system data', 'gesture: return to a version, a checkpoint', 'success: the system is in a known state'],
                    trap_a='trap: a “sorry” does not cancel a badly taken payment', trap_b='trap: believing the revert warns the client', minute='every minute, the lie gets older')}[L]
    F.rect(20, 12, 960, 30, kind='risk', radius=6)
    F.text(500, 27, T['inc'], pt=6.6, weight='Medium')
    (lx, ly, lw, lh), (rx, ry, rw, rh) = compare(F, T['a'], T['b'], y=56, h=250, kinds=('human', 'box'))
    for x, y, w, h, items, trap in ((lx, ly, lw, lh, T['ai'], T['trap_a']), (rx, ry, rw, rh, T['bi'], T['trap_b'])):
        yy = y + 12
        for i, it in enumerate(items):
            bw_, bh_ = F.text(x + 14, yy, it, pt=6, anchor='lt', max_w=w - 28, align='left')
            yy += bh_ + 8
        F.text(x + 14, y + h - 12, trap, pt=5.8, color=RED, anchor='lb', max_w=w - 28, align='left')
    F.badge(lx + lw - 16, ly - 34 + 17, '1', r=9, pt=5.8, kind='dark')
    F.badge(rx + rw - 16, ry - 34 + 17, '2', r=9, pt=5.8, kind='dark')
    F.text(500, 324, T['minute'], pt=6.2, color='muted')


# ------------------------------------------------------------------ ch. 41

@fig('ch41-un-objet',
     {'fr': ('BodyText', 'Un objet dans trois chats = pas d’objet'),
      'en': ('BodyText', 'An object in three chats = no object')},
     {'fr': 'Un objet, un lieu, une revue humaine : le système de l’entreprise est un assemblage de fichiers déjà écrits dans ce livre',
      'en': 'One object, one place, one human review: the company system is an assembly of files already written in this book'},
     h=330)
def ch41_un_objet(F, L):
    T = {'fr': dict(rows=[('Vision / offre', 'proposition-de-valeur.md', 'ch. 9, 29'), ('Objectifs de période', 'budget-evolution.md', 'ch. 11, 28, 35'),
                          ('Contexte', 'ancrage + context-map.md', 'ch. 3, 13'), ('Connaissances', 'registre-faits.md', 'ch. 24'),
                          ('Décisions', 'decisions.md', 'ch. 11, 28, 38'), ('Agents / délégation', 'delegation-map.md', 'ch. 36'),
                          ('Preuves', 'tests + golden-tasks.md', 'ch. 20, 23'), ('Métriques / finances', 'tableur + economie-unitaire.md', 'ch. 30–35'),
                          ('Incidents', 'incidents/ + jugement.md', 'ch. 40, 2')],
                    chats='trois chats, un tableur, un Notion : le même objet en cinq versions', one='docs/ — un fichier par objet', review='revue humaine, datée'),
         'en': dict(rows=[('Vision / offer', 'value-proposition.md', 'ch. 9, 29'), ('Period objectives', 'evolution-budget.md', 'ch. 11, 28, 35'),
                          ('Context', 'anchor + context-map.md', 'ch. 3, 13'), ('Knowledge', 'fact-register.md', 'ch. 24'),
                          ('Decisions', 'decisions.md', 'ch. 11, 28, 38'), ('Agents / delegation', 'delegation-map.md', 'ch. 36'),
                          ('Evidence', 'tests + golden-tasks.md', 'ch. 20, 23'), ('Metrics / finances', 'spreadsheet + unit-economics.md', 'ch. 30–35'),
                          ('Incidents', 'incidents/ + judgment.md', 'ch. 40, 2')],
                    chats='three chats, a spreadsheet, a Notion: the same object in five versions', one='docs/ — one file per object', review='human review, dated')}[L]
    # gauche : nuage barré
    F.rect(20, 40, 250, 200, kind='ghost', radius=8, width=1, dash=True)
    for i, lab in enumerate(['chat 1', 'chat 2', 'chat 3', 'tableur' if L == 'fr' else 'spreadsheet', 'Notion']):
        F.rect(40 + (i % 2) * 110, 56 + (i // 2) * 44, 90, 30, kind='ghost', radius=4, width=1)
        F.text(85 + (i % 2) * 110, 71 + (i // 2) * 44, lab, pt=5.8, color='muted')
    F.line(20, 40, 270, 240, color=RED, width=1.6)
    F.text(145, 254, T['chats'], pt=5.7, color=RED, anchor='mt', max_w=250)
    F.arrow(276, 140, 316, 140, head_size=8)
    # droite : dossier docs/
    F.rect(320, 14, 660, 300, kind='ok', radius=8, width=1.1)
    F.text(336, 30, T['one'], pt=6.8, weight='SemiBold', anchor='lm')
    F.text(964, 30, T['review'], pt=6, color='muted', anchor='rm')
    for i, (obj, f, ch) in enumerate(T['rows']):
        y = 48 + i * 28
        F.text_fit(336, y + 10, obj, 190, pt=6, weight='Medium')
        F.rect(536, y, 320, 20, kind='ghost', radius=4, width=1)
        F.text_fit(696, y + 10, f, 306, pt=5.8, color='text', anchor='mm')
        F.text(964, y + 10, ch, pt=5.4, color='muted', anchor='rm')


# ------------------------------------------------------------------ ch. 42

@fig('ch42-complexite',
     {'fr': ('BodyText', 'Ce scénario est fictif, mais fréquent : chaque ajout paraît raisonnable pris seul'),
      'en': ('BodyText', 'This scenario is fictional, but frequent: each addition seems reasonable taken alone')},
     {'fr': 'Le compteur qui monte sans améliorer le service : chaque ajout paraît raisonnable, le problème est dans la somme',
      'en': 'The counter that rises without improving the service: each addition seems reasonable, the problem is in the sum'},
     h=300)
def ch42_complexite(F, L):
    T = {'fr': dict(adds=['coordinateur', '4 workers', '3 serveurs MCP', '2 modèles', 'scheduler'], runs='runs affichés', value='valeur pour la cliente',
                    q='qu’est-ce que cette complexité donne que la solution simple ne donnait pas ?', base='baseline simple à battre — sinon retirer', ax='ajouts →'),
         'en': dict(adds=['coordinator', '4 workers', '3 MCP servers', '2 models', 'scheduler'], runs='runs displayed', value='value for the client',
                    q='what does this complexity give that the simple solution did not?', base='simple baseline to beat — otherwise remove', ax='additions →')}[L]
    x0, x1, yb, yt = 90, 700, 190, 30
    F.arrow(x0, yb, x1 + 20, yb, color='rule', width=1.2, head_size=8)
    F.text(x1 + 26, yb, T['ax'], pt=6, color='muted', anchor='lm')
    F.axis(x0, yb, x0, yt, '', side='left')
    n = len(T['adds'])
    step = (x1 - x0) / n
    pts_runs, pts_val = [], []
    for i, a in enumerate(T['adds']):
        x = x0 + step * (i + 0.5)
        F.text_fit(x, yb + 14, a, step - 8, pt=5.4, min_pt=4.6, color='muted', anchor='mm')
        pts_runs.append((x, yb - 20 - i * 28))
        pts_val.append((x, yb - 30 - (2 if i > 0 else 0)))
    for a, b in zip(pts_runs[:-1], pts_runs[1:]):
        F.line(a[0], a[1], b[0], b[1], color='#9A8CE0', width=2)
    for a, b in zip(pts_val[:-1], pts_val[1:]):
        F.line(a[0], a[1], b[0], b[1], color=GREEN, width=2)
    for p in pts_runs:
        F.circle(p[0], p[1], 4, kind='box')
    for p in pts_val:
        F.circle(p[0], p[1], 4, kind='ok')
    F.text(pts_runs[-1][0] + 14, pts_runs[-1][1], T['runs'], pt=6, color='#7A6BD0', anchor='lm')
    F.text(pts_val[-1][0] + 14, pts_val[-1][1] + 10, T['value'], pt=6, color=GREEN, anchor='lm')
    # question + baseline
    F.rect(20, 236, 960, 28, kind='human', radius=6)
    F.text(500, 250, T['q'], pt=6.4, weight='Medium')
    F.text(500, 282, T['base'], pt=6.2, color=RED)


# ------------------------------------------------------------------ annexes

@fig('annexeB-playbook',
     {'fr': ('CodeBlock', 'P[problème] --> C[capacité nécessaire]'),
      'en': ('CodeBlock', 'P[problem] --> C[necessary capability]')},
     {'fr': 'Choisir un outil ou une méthode : du problème à l’adoption limitée, en passant par une preuve d’adéquation',
      'en': 'Choosing a tool or a method: from the problem to limited adoption, via evidence of fitness'},
     h=150, mode='replace_code')
def annexeB_playbook(F, L):
    T = {'fr': ['problème', 'capacité nécessaire', 'outil ou méthode', 'preuve d’adéquation', 'adoption limitée'],
         'en': ['problem', 'necessary capability', 'tool or method', 'evidence of fitness', 'limited adoption']}[L]
    hint = {'fr': 'un système de contrôle proportionné, pas une obligation de remplir tous les fichiers',
            'en': 'a proportionate control system, not an obligation to fill every file'}[L]
    hflow(F, T, y=24, h=56, x0=20, x1=980, gap=26, kinds=['human', 'ghost', 'box', 'ok', 'ok'], pt=6.6)
    F.text(500, 110, hint, pt=6, color='muted')


@fig('annexeC-arbre',
     {'fr': ('CodeBlock', 'R[Entrepreneur augmenté]'),
      'en': ('CodeBlock', 'R[Augmented entrepreneur]')},
     {'fr': 'L’arbre du livre : cinq verbes, six parties',
      'en': 'The book’s tree: five verbs, six parts'},
     h=280, mode='replace_code')
def annexeC_arbre(F, L):
    T = {'fr': dict(root='Entrepreneur augmenté', verbs=['Voir', 'Borner', 'Prouver', 'Vendre', 'Ranger'],
                    parts=['I Rôle, jugement, contexte, contrôle', 'II Problème et offre', 'III Brief, skill, surfaces', 'IV Expérience, qualité, sécurité', 'V Position, prix, canal, économie', 'VI Orga, gouvernance, système'],
                    links=[(0, 1), (1, 0), (1, 2), (2, 2), (2, 3), (3, 4), (4, 5)]),
         'en': dict(root='Augmented entrepreneur', verbs=['See', 'Bound', 'Prove', 'Sell', 'File'],
                    parts=['I Role, judgment, context, control', 'II Problem and offer', 'III Brief, skill, surfaces', 'IV Experience, quality, security', 'V Position, price, channel, economics', 'VI Org, governance, system'],
                    links=[(0, 1), (1, 0), (1, 2), (2, 2), (2, 3), (3, 4), (4, 5)])}[L]
    F.box(360, 12, 280, 40, T['root'], kind='dark', pt=7.6, weight='SemiBold', color='white')
    nv = len(T['verbs'])
    vw, vgap = 150, 40
    vx0 = (1000 - (nv * vw + (nv - 1) * vgap)) / 2
    vy = 96
    vcenters = []
    for i, v in enumerate(T['verbs']):
        x = vx0 + i * (vw + vgap)
        F.box(x, vy, vw, 40, v, kind='human', pt=7.2, weight='SemiBold')
        vcenters.append(x + vw / 2)
        F.polyline_arrow([(500, 54), (500, 74), (x + vw / 2, 74), (x + vw / 2, vy - 2)], color='rule')
    np_ = len(T['parts'])
    pw, pgap = 150, 12
    px0 = (1000 - (np_ * pw + (np_ - 1) * pgap)) / 2
    py = 196
    pcenters = []
    for i, p in enumerate(T['parts']):
        x = px0 + i * (pw + pgap)
        F.box(x, py, pw, 70, p, kind='box', pt=5.8, weight='Regular')
        pcenters.append(x + pw / 2)
    for v, p in T['links']:
        F.polyline_arrow([(vcenters[v], vy + 42), (vcenters[v], 170), (pcenters[p], 170), (pcenters[p], py - 2)], color='rule')
