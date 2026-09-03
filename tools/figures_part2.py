# -*- coding: utf-8 -*-
"""Figures explicatives — Partie III (chapitres 12 à 20)."""
from figlib import *

RED = '#D0665A'
GREEN = '#4E9C64'


# ------------------------------------------------------------------ ch. 12

@fig('ch12-niveaux',
     {'fr': ('BodyText', 'Le lecteur doit donc choisir le bon niveau'),
      'en': ('BodyText', 'The reader must therefore choose the right level')},
     {'fr': 'Prompt, skill, workflow, méthode, connecteur : le niveau grandit avec la répétition et le nombre d’étapes',
      'en': 'Prompt, skill, workflow, method, connector: the level grows with repetition and the number of steps'},
     h=340)
def ch12_niveaux(F, L):
    T = {'fr': dict(steps=[('Prompt clair', 'question ponctuelle'), ('Skill versionnée', 'tâche répétitive'),
                           ('Workflow / Spec Kit', 'feature à plusieurs étapes'), ('Méthode complète', 'grand projet')],
                    mcp='MCP : connecteur vers une donnée ou un outil externe — permission limitée, à tout niveau',
                    ax='répétition × nombre d’étapes →', warn='choisir trop haut = cérémonie inutile'),
         'en': dict(steps=[('Clear prompt', 'one-off question'), ('Versioned skill', 'repetitive task'),
                           ('Workflow / Spec Kit', 'multi-step feature'), ('Full method', 'large project')],
                    mcp='MCP: connector to an external data source or tool — limited permission, at any level',
                    ax='repetition × number of steps →', warn='choosing too high = useless ceremony')}[L]
    ladder(F, T['steps'], x0=40, x1=960, y_top=20, y_bottom=230, step_h=80,
           kinds=['ghost', 'box', 'box', 'box'], axis_label=T['ax'], pt=7.4, sub_pt=6.1)
    F.text(500, 290, T['warn'], pt=6.2, color=RED)
    note(F, 40, 308, 920, T['mcp'], kind='human', pt=6.4)


# ------------------------------------------------------------------ ch. 13

@fig('ch13-couches',
     {'fr': ('BodyText', 'Le context engineering, c’est choisir la couche et la dose'),
      'en': ('BodyText', 'Context engineering is choosing the layer and the dose')},
     {'fr': 'Cinq couches de contexte : on choisit la couche et la dose, on ne recopie pas les cinq à chaque run',
      'en': 'Five layers of context: you choose the layer and the dose, you do not copy all five on every run'},
     h=290)
def ch13_couches(F, L):
    T = {'fr': dict(rows=[('Projet', 'mission, structure, commandes — fichier d’ancrage court', 'stable'),
                          ('Tâche', 'ce qui change MAINTENANT', 'par tâche'),
                          ('Documentaire', 'sources d’autorité datées', 'à la demande'),
                          ('Dynamique', 'erreur, test, diff — d’aujourd’hui', 'par run'),
                          ('État', 'fait / échoué / prochaine action autorisée', 'mis à jour')],
                    run='ce run', dose='dose choisie', ttl='durée de vie'),
         'en': dict(rows=[('Project', 'mission, structure, commands — short anchor file', 'stable'),
                          ('Task', 'what changes NOW', 'per task'),
                          ('Documentary', 'dated sources of authority', 'on demand'),
                          ('Dynamic', 'error, test, diff — from today', 'per run'),
                          ('State', 'done / failed / next authorised action', 'updated')],
                    run='this run', dose='chosen dose', ttl='lifetime')}[L]
    top, rh, gap = 30, 40, 8
    F.text(20 + 100, 14, '', pt=6)
    F.text(590, 14, T['ttl'], pt=6.2, color='muted')
    F.text(830, 14, T['dose'], pt=6.2, color='muted')
    doses = [0.25, 0.9, 0.45, 0.7, 0.35]
    for i, (name, what, ttl) in enumerate(T['rows']):
        y = top + i * (rh + gap)
        F.box(20, y, 150, rh, name, kind='box', pt=7.4, weight='SemiBold')
        F.text(184, y + rh / 2, what, pt=6.4, color='text', anchor='lm', max_w=330, align='left')
        pill(F, 590, y + rh / 2, ttl, kind='ghost', pt=5.8, h=17)
        # jauge de dose
        F.rect(700, y + rh / 2 - 8, 260, 16, kind='ghost', radius=4, width=1)
        F.rect(700, y + rh / 2 - 8, 260 * doses[i], 16, kind='human', radius=4, width=1)
    # accolade "ce run"
    yb = top + 5 * (rh + gap)
    F.brace_label(700, 960, yb + 2, T['run'], tick=5)


@fig('ch13-deux-contextes',
     {'fr': ('BodyText', 'Si A « a l’air plus complet » et produit plus d’erreurs'),
      'en': ('BodyText', 'If A “looks more complete” and produces more errors')},
     {'fr': 'Même tâche, deux paquets de contexte : le grenier produit des inventions, la carte produit la bonne sortie',
      'en': 'Same task, two context packages: the attic produces inventions, the map produces the right output'},
     h=300)
def ch13_deux_contextes(F, L):
    T = {'fr': dict(a='Contexte A — tout le grenier', b='Contexte B — la carte',
                    ain=['dépôt entier', 'historique des chats', 'anciens tarifs', 'notes non datées'],
                    bin=['3 fichiers', 'règle datée (docs/regles.md)', 'hors-périmètre écrit'],
                    aout='statut + tarif 19 + délai 48 h', bout='statut seulement',
                    an='inventions fréquentes · coût haut', bn='inventions rares · coût bas',
                    task='Tâche identique : « écris le message de confirmation »', more='plus ≠ mieux'),
         'en': dict(a='Context A — the whole attic', b='Context B — the map',
                    ain=['whole repository', 'chat history', 'old prices', 'undated notes'],
                    bin=['3 files', 'dated rule (docs/rules.md)', 'written out-of-scope'],
                    aout='status + price 19 + 48 h delay', bout='status only',
                    an='frequent inventions · high cost', bn='rare inventions · low cost',
                    task='Identical task: “write the confirmation message”', more='more ≠ better')}[L]
    F.rect(20, 14, 960, 30, kind='ghost', radius=6)
    F.text(500, 29, T['task'], pt=6.8, weight='Medium')
    (lx, ly, lw, lh), (rx, ry, rw, rh) = compare(F, T['a'], T['b'], y=58, h=200, kinds=('ghost', 'box'))
    for (x, y, w, h, items, out, note_, kind, ok) in [
            (lx, ly, lw, lh, T['ain'], T['aout'], T['an'], 'risk', False),
            (rx, ry, rw, rh, T['bin'], T['bout'], T['bn'], 'ok', True)]:
        # entrées empilées (pile)
        n = len(items)
        for i, it in enumerate(items):
            yy = y + 12 + i * 24
            F.rect(x + 14, yy, 236, 21, kind='ghost' if not ok else 'box', radius=4, width=1)
            F.text_fit(x + 132, yy + 10.5, it, 224, pt=5.9, anchor='mm')
        ym = y + 12 + (n * 24) / 2 - 1
        F.arrow(x + 254, ym, x + 284, ym, head_size=7)
        F.box(x + 288, ym - 26, w - 304, 52, out, kind=kind, pt=6.3, weight='Medium')
        (F.check if ok else F.cross)(x + w - 22, y + h - 20, r=5)
        F.text(x + w / 2, y + h - 18, note_, pt=6, color='muted')
    F.text(500, 280, T['more'], pt=7.4, weight='SemiBold', color=RED)


# ------------------------------------------------------------------ ch. 14

@fig('ch14-trois-objets',
     {'fr': ('BodyText', 'Un agent peut utiliser ces objets et décider d’une partie de son parcours'),
      'en': ('BodyText', 'An agent can use these objects and decide part of its journey')},
     {'fr': 'Spec, skill, MCP : le plan, la procédure et la porte contrôlée — aucun des trois n’est l’agent',
      'en': 'Spec, skill, MCP: the plan, the procedure and the controlled door — none of the three is the agent'},
     h=300)
def ch14_trois_objets(F, L):
    T = {'fr': dict(items=[('Spec', 'le plan du changement', 'borne l’intention : quoi, hors-périmètre, preuve'),
                           ('Skill', 'la fiche de procédure', 'capacité réutilisable qu’un stagiaire pourrait suivre'),
                           ('MCP', 'la porte contrôlée', 'connexion à des ressources et outils externes, scopes limités')],
                    agent='Agent', uses='utilise ces objets et décide d’une partie de son parcours',
                    not_='aucun objet ne devient automatiquement l’agent, la méthode ou le produit'),
         'en': dict(items=[('Spec', 'the plan of the change', 'bounds intent: what, out of scope, evidence'),
                           ('Skill', 'the procedure sheet', 'reusable capability an intern could follow'),
                           ('MCP', 'the controlled door', 'connection to external resources and tools, limited scopes')],
                    agent='Agent', uses='uses these objects and decides part of its journey',
                    not_='no object automatically becomes the agent, the method or the product')}[L]
    w, gap = 290, 45
    kinds = ['human', 'box', 'ghost']
    for i, (t, meta, desc) in enumerate(T['items']):
        x = 20 + i * (w + gap)
        F.box(x, 20, w, 92, t, kind=kinds[i], sub=meta + '\n' + desc, pt=8.4, sub_pt=6)
        F.arrow(x + w / 2, 116, x + w / 2, 150, head_size=8)
    F.box(300, 152, 400, 60, T['agent'], kind='dark', sub=None, pt=8.4, weight='SemiBold', color='white')
    F.text(500, 226, T['uses'], pt=6.4, color='muted')
    F.line(300, 152, 700, 152, color='rule')
    F.text(500, 262, T['not_'], pt=6.2, color=RED)


@fig('ch14-pipeline',
     {'fr': ('CodeBlock', 'A[Idée encore floue] --> B[Problème vu dans la vraie vie]'),
      'en': ('CodeBlock', 'A[Idea still fuzzy] --> B[Problem seen in real life]')},
     {'fr': 'Le pipeline du livre : chaque étape transforme une sortie en entrée de la suivante',
      'en': 'The book’s pipeline: each step turns an output into the input of the next'},
     h=390, mode='replace_code')
def ch14_pipeline(F, L):
    T = {'fr': ['Idée encore floue', 'Problème vu dans la vraie vie', 'Hypothèse qu’on peut infirmer', 'Preuve chez une vraie personne',
                'Offre : ce que vous vendez, à qui', 'Plus petite version qui apprend', 'Ce que l’IA a le droit de voir',
                'Délégation avec limite', 'Produit qui tient', 'Vente', 'Économie qui compte encore',
                'Croissance sans casser', 'Organisation humain + IA', 'Autonomie sous contrôle'],
         'en': ['Idea still fuzzy', 'Problem seen in real life', 'Hypothesis that can be falsified', 'Evidence with a real person',
                'Offer: what you sell, to whom', 'Smallest version that learns', 'What AI is allowed to see',
                'Delegation with a limit', 'Product that holds', 'Sale', 'Economics that still count',
                'Growth without breaking', 'Human + AI organisation', 'Autonomy under control']}[L]
    parts = {'fr': ['I–II', 'II', 'II', 'II', 'II', 'II', 'III', 'III', 'IV', 'V', 'V', 'V', 'VI', 'VI'],
             'en': ['I–II', 'II', 'II', 'II', 'II', 'II', 'III', 'III', 'IV', 'V', 'V', 'V', 'VI', 'VI']}[L]
    kinds = ['ghost', 'human', 'human', 'ok', 'human', 'box', 'box', 'box', 'box', 'human', 'human', 'human', 'box', 'box']
    # serpentin : 2 rangées de 7 ? -> 3 rangées (5,5,4) en boustrophédon
    rows = [T[0:5], T[5:10], T[10:14]]
    kr = [kinds[0:5], kinds[5:10], kinds[10:14]]
    pr = [parts[0:5], parts[5:10], parts[10:14]]
    bw, bh, gapx, rowgap = 176, 62, 24, 48
    x0 = 20
    centers = []
    for r, items in enumerate(rows):
        y = 16 + r * (bh + rowgap)
        for c, it in enumerate(items):
            col = c if r % 2 == 0 else (4 - c)
            x = x0 + col * (bw + gapx)
            F.box(x, y, bw, bh, it, kind=kr[r][c], pt=6.6, weight='Medium')
            pill(F, x + bw - 16, y, pr[r][c], kind='dark', pt=5.4, h=14, padx=5, color='white', weight='SemiBold')
            centers.append((x + bw / 2, y + bh / 2, x, y))
    # flèches
    for i in range(len(T) - 1):
        cx1, cy1, x1, y1 = centers[i]
        cx2, cy2, x2, y2 = centers[i + 1]
        if abs(cy1 - cy2) < 1:
            if cx2 > cx1:
                F.arrow(x1 + bw + 2, cy1, x2 - 2, cy1, head_size=7)
            else:
                F.arrow(x1 - 2, cy1, x2 + bw + 2, cy1, head_size=7)
        else:
            F.arrow(cx1, y1 + bh + 2, cx2, y2 - 2, head_size=7)


@fig('ch14-mcp',
     {'fr': ('BodyText', 'Avant une connexion, vérifiez : identité, scopes'),
      'en': ('BodyText', 'Before a connection, check: identity, scopes')},
     {'fr': 'MCP : le serveur expose des outils, la spec et l’application décident de ce qui est autorisé dans ce run',
      'en': 'MCP: the server exposes tools, the spec and the application decide what is authorised in this run'},
     h=300)
def ch14_mcp(F, L):
    T = {'fr': dict(agent='Agent', app='Application + spec\n(décident)', server='Serveur MCP', res='Ressources\net outils externes',
                    tools=['rechercher les réservations', 'lire un créneau', 'annuler une réservation'],
                    allowed=['autorisé (lecture)', 'autorisé (lecture)', 'interdit dans ce run'],
                    checks='Avant de connecter : identité · scopes · lecture/écriture séparées · validation des arguments · limites d’appel · taille des sorties · logs · expiration · arrêt',
                    data='une donnée externe peut ressembler à une instruction : elle reste une donnée'),
         'en': dict(agent='Agent', app='Application + spec\n(decide)', server='MCP server', res='External resources\nand tools',
                    tools=['search bookings', 'read a slot', 'cancel a booking'],
                    allowed=['allowed (read)', 'allowed (read)', 'forbidden in this run'],
                    checks='Before connecting: identity · scopes · read/write separated · argument validation · call limits · output size · logs · expiry · stop',
                    data='external data can look like an instruction: it stays data')}[L]
    F.box(20, 70, 150, 60, T['agent'], kind='box', pt=8, weight='SemiBold')
    F.box(230, 55, 200, 90, T['app'], kind='human', pt=7.2)
    F.box(500, 70, 170, 60, T['server'], kind='box', pt=7.6)
    F.box(760, 62, 220, 76, T['res'], kind='ghost', pt=7)
    F.arrow(172, 100, 226, 100, head_size=8)
    F.arrow(432, 100, 496, 100, head_size=8)
    F.arrow(672, 92, 756, 92, head_size=8)
    F.arrow(756, 110, 672, 110, head_size=8, color='rule')
    F.text(870, 150, T['data'], pt=5.6, color=RED, max_w=220, anchor='mt')
    # outils exposés
    y = 176
    F.text(585, 160, '', pt=6)
    for i, (tool, al) in enumerate(zip(T['tools'], T['allowed'])):
        yy = y + i * 28
        F.rect(500, yy, 170, 22, kind='ghost', radius=4, width=1)
        F.text(585, yy + 11, tool, pt=5.9)
        kind = 'ok' if i < 2 else 'risk'
        pill(F, 330, yy + 11, al, kind=kind, pt=5.8, h=18)
        F.line(432, yy + 11, 498, yy + 11, color='rule', dash=(4, 3))
    F.line(330, 147, 330, y - 4, color='rule', dash=(4, 3))
    F.line(585, 132, 585, y - 4, color='rule', dash=(4, 3))
    note(F, 20, 270, 960, T['checks'], kind='ok', pt=6.1)


# ------------------------------------------------------------------ ch. 15

@fig('ch15-boucle',
     {'fr': ('CodeBlock', 'Comprendre → Planifier → Agir → Vérifier → Intégrer'),
      'en': ('CodeBlock', 'Understand → Plan → Act → Check → Integrate')},
     {'fr': 'Une boucle, pas un bouton : cinq étapes, et un retour « corriger » quand la vérification échoue',
      'en': 'A loop, not a button: five steps, and a “correct” return when checking fails'},
     h=230, mode='replace_code')
def ch15_boucle(F, L):
    T = {'fr': dict(items=[('Comprendre', 'contexte, fichiers, contraintes, inconnues'), ('Planifier', 'étapes, périmètre, preuves attendues'),
                           ('Agir', 'modification bornée'), ('Vérifier', 'tests, lint, diff, métier'), ('Intégrer', 'résumé, preuves, approbation')],
                    back='corriger', skip='sauter une étape = hypothèses, zones touchées en trop, possibilité prise pour un fait'),
         'en': dict(items=[('Understand', 'context, files, constraints, unknowns'), ('Plan', 'steps, scope, expected evidence'),
                           ('Act', 'bounded change'), ('Check', 'tests, lint, diff, business'), ('Integrate', 'summary, evidence, approval')],
                    back='correct', skip='skipping a step = assumptions, too many zones touched, a possibility taken for a fact')}[L]
    rects = hflow(F, T['items'], y=30, h=84, x0=20, x1=980, gap=22, kinds=['box', 'box', 'human', 'ok', 'box'], pt=7.4, sub_pt=5.9)
    # retour Vérifier -> Planifier
    x_v = rects[3][0] + rects[3][2] / 2
    x_p = rects[1][0] + rects[1][2] / 2
    F.polyline_arrow([(x_v, 116), (x_v, 150), (x_p, 150), (x_p, 116)], color='arrow')
    F.text((x_v + x_p) / 2, 162, T['back'], pt=6.4, color='muted')
    F.text(500, 200, T['skip'], pt=6.1, color=RED, max_w=900)


@fig('ch15-etats',
     {'fr': ('BodyText', 'Un état doit être conservé dans un artefact ou un système de suivi'),
      'en': ('BodyText', 'A state must be kept in an artefact or a tracking system')},
     {'fr': 'Les états d’un run : le chemin nominal, les arrêts et les sorties — conservés dans un artefact, pas dans la dernière phrase de l’agent',
      'en': 'The states of a run: the nominal path, the stops and the exits — kept in an artefact, not in the agent’s last sentence'},
     h=290)
def ch15_etats(F, L):
    T = {'fr': dict(main=['READY', 'PLANNED', 'RUNNING', 'VERIFYING', 'READY_FOR_REVIEW', 'DONE'],
                    sub=['tâche reçue', 'plan accepté', 'action en cours', 'checks en cours', 'preuves disponibles', 'intégration acceptée'],
                    wait='WAITING_APPROVAL', waits='confirmation nécessaire', failed='FAILED', faileds='contrôle échoué',
                    esc='ESCALATED', escs='décision hors périmètre', canc='CANCELLED', cancs='reprise interdite',
                    human='décision humaine'),
         'en': dict(main=['READY', 'PLANNED', 'RUNNING', 'VERIFYING', 'READY_FOR_REVIEW', 'DONE'],
                    sub=['task received', 'plan accepted', 'action in progress', 'checks running', 'evidence available', 'integration accepted'],
                    wait='WAITING_APPROVAL', waits='confirmation needed', failed='FAILED', faileds='check failed',
                    esc='ESCALATED', escs='decision out of scope', canc='CANCELLED', cancs='resumption forbidden',
                    human='human decision')}[L]
    items = list(zip(T['main'], T['sub']))
    rects = hflow(F, items, y=96, h=74, x0=20, x1=980, gap=14, kinds=['ghost', 'box', 'box', 'box', 'ok', 'ok'], pt=5.6, sub_pt=5.0)
    xs = [r[0] + r[2] / 2 for r in rects]
    # WAITING_APPROVAL au-dessus de RUNNING
    F.box(xs[2] - 95, 6, 190, 66, T['wait'], kind='human', sub=T['waits'], pt=5.6, sub_pt=5.0)
    F.arrow(xs[2] - 22, 94, xs[2] - 22, 72, head_size=7)
    F.arrow(xs[2] + 22, 72, xs[2] + 22, 94, head_size=7)
    F.text(xs[2] + 102, 40, T['human'], pt=5.6, color='muted', anchor='lm')
    # FAILED sous VERIFYING, retour vers RUNNING
    F.box(xs[3] - 75, 214, 150, 66, T['failed'], kind='risk', sub=T['faileds'], pt=5.6, sub_pt=5.0)
    F.arrow(xs[3], 172, xs[3], 212, head_size=7, color=RED)
    F.polyline_arrow([(xs[3] - 75, 247), (xs[2], 247), (xs[2], 172)], color='arrow')
    # ESCALATED et CANCELLED : sorties possibles depuis les états actifs
    F.box(xs[4] - 70, 214, 150, 66, T['esc'], kind='human', sub=T['escs'], pt=5.6, sub_pt=5.0)
    F.box(xs[5] - 90, 214, 150, 66, T['canc'], kind='ghost', sub=T['cancs'], pt=5.6, sub_pt=5.0)
    F.line(xs[1], 172, xs[1], 194, color='rule', dash=(4, 3))
    F.line(xs[1], 194, xs[5] - 15, 194, color='rule', dash=(4, 3))
    F.arrow(xs[4] + 5, 194, xs[4] + 5, 212, head_size=7, color='rule')
    F.arrow(xs[5] - 15, 194, xs[5] - 15, 212, head_size=7, color='rule')


@fig('ch15-jonction',
     {'fr': ('CodeBlock', 'A[Agent ou étape A] -->|handoff| J[Jonction]'),
      'en': ('CodeBlock', 'A[Agent or step A] -->|handoff| J[Junction]')},
     {'fr': 'Le handoff est une interface : à la jonction, les preuves et les formats doivent s’aligner, sinon un humain décide',
      'en': 'The handoff is an interface: at the junction, evidence and formats must align, otherwise a human decides'},
     h=250, mode='replace_code')
def ch15_jonction(F, L):
    T = {'fr': dict(a='Agent ou étape A', b='Agent ou étape B', j='Jonction', q='Preuves et formats alignés ?',
                    yes='oui', no='non', d='Suite autorisée', e='Décision humaine', hand='handoff',
                    hint='handoff = passation écrite : ce que le suivant a le droit de savoir'),
         'en': dict(a='Agent or step A', b='Agent or step B', j='Junction', q='Evidence and formats aligned?',
                    yes='yes', no='no', d='Continuation authorised', e='Human decision', hand='handoff',
                    hint='handoff = written hand-over: what the next one is allowed to know')}[L]
    F.box(20, 30, 190, 54, T['a'], kind='box', pt=7)
    F.box(20, 140, 190, 54, T['b'], kind='box', pt=7)
    F.box(320, 85, 130, 54, T['j'], kind='ghost', pt=7.4, weight='SemiBold')
    F.polyline_arrow([(212, 57), (270, 57), (270, 100), (316, 100)], label=T['hand'], label_at=(262, 57), label_offset=(0, -10))
    F.polyline_arrow([(212, 167), (270, 167), (270, 124), (316, 124)], label=T['hand'], label_at=(262, 167), label_offset=(0, 11))
    F.arrow(452, 112, 500, 112, head_size=8)
    F.diamond(620, 112, 236, 96, T['q'], kind='human', pt=6.4)
    F.arrow(740, 112, 790, 112, label=T['yes'], head_size=8, label_offset=(0, -10))
    F.box(792, 86, 188, 52, T['d'], kind='ok', pt=6.8)
    F.polyline_arrow([(620, 162), (620, 200), (790, 200)], label=T['no'], label_at=(620, 181), label_offset=(-14, 0))
    F.box(792, 176, 188, 48, T['e'], kind='human', pt=6.8)
    F.text(160, 226, T['hint'], pt=6, color='muted', anchor='lm')


# ------------------------------------------------------------------ ch. 16

@fig('ch16-couches',
     {'fr': ('BodyText', 'Le journal d’audit n’entre pas entier dans le prompt'),
      'en': ('BodyText', 'The audit log does not enter the prompt in full')},
     {'fr': 'Les couches à séparer : plus la durée est longue, plus l’entrée exige provenance, date et revue',
      'en': 'The layers to separate: the longer the lifetime, the more an entry requires provenance, date and review'},
     h=330)
def ch16_couches(F, L):
    T = {'fr': dict(rows=[('Contexte actif', 'prompt, fichiers, sorties d’outils', 'tour ou session'),
                          ('Notes de session', 'hypothèses, décisions temporaires', 'session ou tâche'),
                          ('État de workflow', 'étape, statut, sorties attendues', 'jusqu’à la clôture'),
                          ('Mémoire de projet', 'conventions, ADR, invariants', 'longue, avec revue'),
                          ('Retrieval externe', 'documents, code, tickets, données', 'selon la source'),
                          ('Journal d’audit', 'actions, approbations, résultats', 'selon politique')],
                    ax='durée de vie →', prompt='entre dans le prompt', not_prompt='ne rentre pas entier dans le prompt : sert à reconstruire'),
         'en': dict(rows=[('Active context', 'prompt, files, tool outputs', 'turn or session'),
                          ('Session notes', 'hypotheses, temporary decisions', 'session or task'),
                          ('Workflow state', 'step, status, expected outputs', 'until closure'),
                          ('Project memory', 'conventions, ADRs, invariants', 'long, with review'),
                          ('External retrieval', 'documents, code, tickets, data', 'according to the source'),
                          ('Audit log', 'actions, approvals, results', 'according to policy')],
                    ax='lifetime →', prompt='enters the prompt', not_prompt='does not enter the prompt in full: used to reconstruct')}[L]
    top, rh, gap = 16, 36, 8
    lens = [0.12, 0.28, 0.42, 0.85, 0.65, 1.0]
    kinds = ['box', 'box', 'box', 'human', 'ghost', 'dark']
    bx, bwmax = 486, 474
    for i, (name, what, ttl) in enumerate(T['rows']):
        y = top + i * (rh + gap)
        F.box(20, y, 178, rh, name, kind=kinds[i], pt=6.4, weight='SemiBold', color='white' if kinds[i] == 'dark' else 'text')
        F.text_fit(208, y + rh / 2, what, 262, pt=6, color='text')
        bw_ = bwmax * lens[i]
        F.rect(bx, y + rh / 2 - 9, bw_, 18, kind=kinds[i] if kinds[i] != 'dark' else 'ghost', radius=4, width=1)
        if bw_ >= 150:
            F.text(bx + 8, y + rh / 2, ttl, pt=5.5, color='muted', anchor='lm')
        else:
            F.text(bx + bw_ + 8, y + rh / 2, ttl, pt=5.5, color='muted', anchor='lm')
    yb = top + 6 * (rh + gap)
    F.axis(bx, yb, bx + bwmax, yb, T['ax'], side='below')
    F.text(500, yb + 40, T['not_prompt'], pt=6, color=RED)


@fig('ch16-cycle',
     {'fr': ('CodeBlock', 'W[write] --> M[manage] --> R[read] --> W'),
      'en': ('CodeBlock', 'W[write] --> M[manage] --> R[read] --> W')},
     {'fr': 'Le cycle d’une mémoire : écrire avec provenance, gérer (corriger, désactiver, supprimer), lire à la demande',
      'en': 'The lifecycle of a memory: write with provenance, manage (correct, deactivate, delete), read on demand'},
     h=210, mode='replace_code')
def ch16_cycle(F, L):
    T = {'fr': [('write', 'ajouter : source, date, propriétaire, expiration'), ('manage', 'corriger, désactiver, supprimer, revoir'),
                ('read', 'retrouver à la demande, pas tout recharger')],
         'en': [('write', 'add: source, date, owner, expiry'), ('manage', 'correct, deactivate, delete, review'),
                ('read', 'retrieve on demand, do not reload everything')]}[L]
    label = {'fr': 'plus fiable que « tout sauvegarder »', 'en': 'more reliable than “save everything”'}[L]
    rects = hflow(F, T, y=30, h=84, x0=40, x1=960, gap=50, kinds=['human', 'box', 'ok'], pt=8, sub_pt=6)
    x_r = rects[2][0] + rects[2][2] / 2
    x_w = rects[0][0] + rects[0][2] / 2
    F.polyline_arrow([(x_r, 116), (x_r, 150), (x_w, 150), (x_w, 116)])
    F.text(500, 164, label, pt=6.3, color='muted')


# ------------------------------------------------------------------ ch. 17

@fig('ch17-surfaces',
     {'fr': ('BodyText', 'Vous n’avez pas à tout maîtriser avant le premier incrément'),
      'en': ('BodyText', 'You do not have to master all four before the first increment')},
     {'fr': 'Quatre surfaces, une phrase chacune : ce que le client voit, ce qui décide, ce qui est loué, ce qui est en ligne',
      'en': 'Four surfaces, one sentence each: what the customer sees, what decides, what is rented, what is online'},
     h=260)
def ch17_surfaces(F, L):
    T = {'fr': dict(cli='Cliente', items=[('Frontend', 'ce qu’on voit et clique', 'un parcours, pas cinq écrans'),
                                          ('Backend', 'ce qui décide, enregistre, refuse', 'qui a le droit, quelle preuve'),
                                          ('BaaS', 'auth, données, fichiers loués', 'ce que vous refusez d’opérer cette semaine'),
                                          ('Déploiement', 'une URL qui n’est plus votre ordinateur', 'qui promeut, comment reculer')],
                    bound='ce que vous bornez'),
         'en': dict(cli='Client', items=[('Frontend', 'what they see and click', 'one journey, not five screens'),
                                         ('Backend', 'what decides, records, refuses', 'who is allowed, what evidence'),
                                         ('BaaS', 'auth, data, files rented', 'what you refuse to operate this week'),
                                         ('Deploy', 'a URL that is no longer your laptop', 'who promotes, how to roll back')],
                    bound='what you bound')}[L]
    F.box(20, 55, 110, 60, T['cli'], kind='human', pt=7.6)
    F.arrow(132, 85, 176, 85, head_size=8)
    # frontend, backend, baas empilés horizontalement ; déploiement = cadre
    F.rect(178, 14, 802, 178, kind='ghost', radius=10, width=1.2, dash=True)
    x = 200
    ws = [230, 250, 250]
    kinds = ['box', 'box', 'ghost']
    for i in range(3):
        name, what, bound = T['items'][i]
        F.box(x, 50, ws[i], 70, name, kind=kinds[i], sub=what, pt=7.6, sub_pt=6)
        F.text(x + ws[i] / 2, 126, bound, pt=5.8, color='muted', max_w=ws[i] - 6, anchor='mt')
        if i < 2:
            F.arrow(x + ws[i] + 2, 85, x + ws[i] + 20, 85, head_size=7)
        x += ws[i] + 22
    name, what, bound = T['items'][3]
    F.text(190, 28, name + ' — ' + what, pt=6.6, weight='SemiBold', color='muted', anchor='lm')
    F.text(966, 176, bound, pt=5.8, color='muted', anchor='rm')
    F.brace_label(200, 960, 212, T['bound'], tick=4)


@fig('ch17-couches',
     {'fr': ('CodeBlock', 'UI[Frontend — ce qu’on voit]'),
      'en': ('CodeBlock', 'UI[Frontend — what they see]')},
     {'fr': 'Frontend, backend, domaine, infra : les responsabilités et les points de contrôle deviennent discutables',
      'en': 'Frontend, backend, domain, infra: responsibilities and control points become discussable'},
     h=300, mode='replace_code')
def ch17_couches(F, L):
    T = {'fr': dict(ui='Frontend — ce qu’on voit', app='Backend — cas d’usage', dom='Domaine — règles et invariants',
                    inf='Infra / BaaS — données et services', rules=['le domaine ne dépend pas de l’interface', 'les accès aux données passent par l’interface autorisée', 'les changements de contrat public sont versionnés']),
         'en': dict(ui='Frontend — what they see', app='Backend — use cases', dom='Domain — rules and invariants',
                    inf='Infra / BaaS — data and services', rules=['the domain does not depend on the interface', 'data access goes through the authorised interface', 'public contract changes are versioned'])}[L]
    cx = 300
    F.box(cx - 200, 16, 400, 48, T['ui'], kind='box', pt=7.4)
    F.arrow(cx, 66, cx, 96, head_size=8)
    F.box(cx - 200, 98, 400, 48, T['app'], kind='box', pt=7.4)
    F.arrow(cx - 100, 148, cx - 100, 178, head_size=8)
    F.arrow(cx + 100, 148, cx + 100, 178, head_size=8)
    F.box(cx - 240, 180, 230, 56, T['dom'], kind='human', pt=6.8)
    F.box(cx + 10, 180, 230, 56, T['inf'], kind='ghost', pt=6.8)
    # règles vérifiables
    F.text(600, 30, '', pt=6)
    for i, r in enumerate(T['rules']):
        yy = 40 + i * 62
        F.check(618, yy + 12, r=5)
        F.text(636, yy + 12, r, pt=6.2, anchor='lm', max_w=330, align='left')


# ------------------------------------------------------------------ ch. 18

@fig('ch18-tranche',
     {'fr': ('BodyText', 'Le premier incrément doit répondre à une question'),
      'en': ('BodyText', 'The first increment must answer a question')},
     {'fr': 'Une tranche verticale traverse toutes les couches pour produire une petite valeur observable — pas une couche entière',
      'en': 'A vertical slice cuts through all the layers to produce a small observable value — not a whole layer'},
     h=280)
def ch18_tranche(F, L):
    T = {'fr': dict(layers=['Interface', 'Cas d’usage', 'Règles', 'Données'], slice='I1 — créer un cabinet et afficher son nom',
                    bad='couche entière d’abord : aucune question tranchée', good='tranche : une question tranchée, une preuve',
                    q='« une secrétaire peut-elle publier puis retrouver un créneau sans aide ? »'),
         'en': dict(layers=['Interface', 'Use case', 'Rules', 'Data'], slice='I1 — create a practice and display its name',
                    bad='whole layer first: no question settled', good='slice: one question settled, one proof',
                    q='“can a secretary publish then find a slot without help?”')}[L]
    # gauche : couches horizontales, une seule couche remplie (mauvais)
    for panel, x0 in ((0, 20), (1, 520)):
        for i, lay in enumerate(T['layers']):
            y = 30 + i * 44
            kind = 'ghost'
            if panel == 0 and i == 3:
                kind = 'risk'
            F.rect(x0, y, 440, 38, kind=kind, radius=5, width=1.1)
            F.text(x0 + 10, y + 19, lay, pt=6.4, color='muted', anchor='lm')
        if panel == 1:
            F.rect(x0 + 160, 24, 120, 4 * 44 - 2, kind='ok', radius=6, width=1.4)
            F.text(x0 + 220, 24 + (4 * 44 - 2) / 2, T['slice'], pt=6.2, weight='Medium', max_w=104)
    F.cross(34, 226, r=5)
    F.text(50, 226, T['bad'], pt=6.2, color='muted', anchor='lm', max_w=400, align='left')
    F.check(534, 226, r=5)
    F.text(550, 226, T['good'], pt=6.2, color='muted', anchor='lm', max_w=400, align='left')
    F.text(500, 262, T['q'], pt=6.2, color='text')


# ------------------------------------------------------------------ ch. 19

@fig('ch19-escalier',
     {'fr': ('BodyText', 'Le bon incrément n’est pas le plus petit morceau de code'),
      'en': ('BodyText', 'The right increment is not the smallest piece of code')},
     {'fr': 'L’escalier des incréments : chaque marche produit une preuve que l’on peut relire ou annuler',
      'en': 'The staircase of increments: each step produces evidence you can reread or undo'},
     h=360)
def ch19_escalier(F, L):
    T = {'fr': dict(steps=[('1. Contrat de disponibilité', 'preuve : schéma relu'), ('2. Cas acceptés / refusés', 'preuve : tests écrits'),
                           ('3. Règle de non-chevauchement', 'preuve : tests verts'), ('4. Cas d’usage → interface', 'preuve : parcours cliquable'),
                           ('5. Parcours avec deux utilisateurs', 'preuve : observation notée')],
                    bad='« Construire toute la réservation » : une seule marche, trop haute, aucune preuve intermédiaire',
                    undo='chaque marche : relisible, annulable'),
         'en': dict(steps=[('1. Availability contract', 'evidence: schema reviewed'), ('2. Accepted / refused cases', 'evidence: tests written'),
                           ('3. Non-overlap rule', 'evidence: green tests'), ('4. Use case → interface', 'evidence: clickable journey'),
                           ('5. Journey with two users', 'evidence: noted observation')],
                    bad='“Build the whole booking feature”: one single step, too high, no intermediate evidence',
                    undo='each step: rereadable, undoable')}[L]
    ladder(F, T['steps'], x0=30, x1=970, y_top=16, y_bottom=276, step_h=96, kinds=['box', 'box', 'box', 'box', 'ok'], pt=6.0, sub_pt=5.4)
    F.text(500, 292, T['undo'], pt=6.2, color=GREEN)
    note(F, 30, 310, 940, T['bad'], kind='risk', pt=6.2)


# ------------------------------------------------------------------ ch. 20

@fig('ch20-pyramide',
     {'fr': ('CodeBlock', 'S[statique] --> U[unitaire]'),
      'en': ('CodeBlock', 'S[static] --> U[unit]')},
     {'fr': 'La chaîne de preuve : chaque niveau établit une propriété, aucun ne certifie le produit entier',
      'en': 'The evidence chain: each level establishes a property, none certifies the whole product'},
     h=300, mode='replace_code')
def ch20_pyramide(F, L):
    T = {'fr': dict(levels=[('statique', 'le code se charge-t-il ?'), ('unitaire', 'la règle est-elle vraie ?'),
                            ('intégration', 'les composants communiquent-ils ?'), ('contrat', 'la réponse reste-t-elle stable ?'),
                            ('parcours', 'le parcours fonctionne-t-il ?'), ('métier', 'le résultat convient-il au cabinet ?')],
                    ax_l='coût, causes d’échec →', ax_r='proximité de l’usage réel →', one='un test vert prouve sa propriété'),
         'en': dict(levels=[('static', 'does the code load?'), ('unit', 'is the rule true?'),
                            ('integration', 'do the components talk?'), ('contract', 'does the response stay stable?'),
                            ('journey', 'does the journey work?'), ('business', 'does the result suit the practice?')],
                    ax_l='cost, causes of failure →', ax_r='closeness to real use →', one='a green test proves its property')}[L]
    n = len(T['levels'])
    top, rh, gap = 16, 36, 6
    cx = 360
    kinds = ['ghost', 'box', 'box', 'box', 'human', 'ok']
    for i, (name, q) in enumerate(T['levels']):
        idx = n - 1 - i
        y = top + idx * (rh + gap)
        w = 200 + i * 56
        F.box(cx - w / 2, y, w, rh, name, kind=kinds[i], pt=7, weight='SemiBold')
        F.text_fit(660, y + rh / 2, q, 320, pt=6, color='muted')
    yb = top + n * (rh + gap)
    F.axis(40, yb - 4, 40, top, T['ax_l'], side='right')
    F.text(500, yb + 12, T['one'], pt=6.2, color='muted')


@fig('ch20-debug',
     {'fr': ('CodeBlock', 'A[Reproduire] --> B[Première divergence]'),
      'en': ('CodeBlock', 'A[Reproduce] --> B[First divergence]')},
     {'fr': 'Quand une preuve échoue : reproduire, trouver la première divergence, corriger la cause, rejouer, prévenir',
      'en': 'When evidence fails: reproduce, find the first divergence, correct the cause, replay, prevent'},
     h=200, mode='replace_code')
def ch20_debug(F, L):
    T = {'fr': [('Reproduire', 'même entrée, même échec'), ('Première divergence', 'où attendu ≠ observé'), ('Corriger la cause', 'pas le symptôme'),
                ('Rejouer', 'reproduction, non-régression, cas limite'), ('Prévention', 'test, règle, doc ou métrique')],
         'en': [('Reproduce', 'same input, same failure'), ('First divergence', 'where expected ≠ observed'), ('Correct the cause', 'not the symptom'),
                ('Replay', 'reproduction, non-regression, edge case'), ('Prevention', 'test, rule, doc or metric')]}[L]
    hint = {'fr': 'si le rejeu échoue : la cause n’était pas la bonne → retour à la divergence',
            'en': 'if the replay fails: the cause was not the right one → back to the divergence'}[L]
    rects = hflow(F, T, y=24, h=92, x0=20, x1=980, gap=20, kinds=['ghost', 'human', 'box', 'ok', 'ok'], pt=6.8, sub_pt=5.7)
    x_r = rects[3][0] + rects[3][2] / 2
    x_d = rects[1][0] + rects[1][2] / 2
    F.polyline_arrow([(x_r, 118), (x_r, 148), (x_d, 148), (x_d, 118)], color='arrow')
    F.text(500, 166, hint, pt=6, color='muted')
