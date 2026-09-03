# -*- coding: utf-8 -*-
"""
Petite bibliothèque de rendu pour les figures explicatives du livre.

Principe : chaque figure est décrite dans un repère logique de 1000 unités de
large (= 4,17 pouces imprimés, la largeur des figures existantes). Le rendu se
fait à 400 dpi avec suréchantillonnage ×2 puis réduction, pour des traits nets.

Palette volontairement proche des figures déjà présentes dans le manuscrit
(rendus Mermaid : boîtes lavande, bord violet, texte anthracite).
"""
import math, os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, 'fonts')

PRINT_WIDTH_IN = 4.17          # largeur d'impression des figures
DPI = 400
SS = 2                         # suréchantillonnage
UNITS = 1000.0                 # largeur logique
PX_PER_UNIT = PRINT_WIDTH_IN * DPI / UNITS      # 1.668 px / unité (avant SS)
UNITS_PER_PT = (DPI / 72.0) / PX_PER_UNIT       # 1 pt = 3.33 unités

C = {
    'text':   '#2A2A2E',
    'muted':  '#6E6E78',
    'arrow':  '#7A7A85',
    'rule':   '#C9C9D2',
    'box':    ('#ECEBFB', '#9A8CE0'),   # lavande — élément neutre / système
    'human':  ('#FFF0D4', '#E0AC55'),   # sable — geste ou décision humaine
    'risk':   ('#FDE3DF', '#E0857A'),   # rouge doux — risque, arrêt, interdit
    'ok':     ('#E2F2E6', '#6FB584'),   # vert doux — preuve, autorisé
    'ghost':  ('#F5F5F7', '#BDBDC7'),   # gris — contexte, secondaire
    'dark':   ('#4B4B57', '#4B4B57'),   # sombre — titre de bande
}


OVERFLOW = []


def _hex(c):
    c = c.lstrip('#')
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


class Fig:
    EXTRA = 160   # marge de sécurité (unités) ajoutée sous la hauteur de conception ; recadrée à la sortie

    def __init__(self, w=1000, h=400, bg='white'):
        self.W, self.H = float(w), float(h)
        self.k = PX_PER_UNIT * SS
        self.im = Image.new('RGB', (int(round(w * self.k)), int(round((h + self.EXTRA) * self.k))), bg)
        self.d = ImageDraw.Draw(self.im)
        self._fonts = {}

    # ---------- unités ----------
    def px(self, v):
        return v * self.k

    def font(self, pt=7.5, weight='Regular'):
        key = (round(pt, 2), weight)
        if key not in self._fonts:
            path = os.path.join(FONT_DIR, 'Inter-%s.ttf' % weight)
            self._fonts[key] = ImageFont.truetype(path, int(round(pt * UNITS_PER_PT * self.k)))
        return self._fonts[key]

    # ---------- texte ----------
    def wrap(self, text, font, max_w_units):
        max_px = self.px(max_w_units)
        out = []
        for para in str(text).split('\n'):
            words = para.split(' ')
            line = ''
            for w in words:
                cand = (line + ' ' + w).strip()
                if font.getlength(cand) <= max_px or not line:
                    line = cand
                else:
                    out.append(line)
                    line = w
            out.append(line)
        return out

    def line_height(self, font, leading=1.28):
        return font.size * leading

    def text_block_size(self, lines, font, leading=1.28):
        lh = self.line_height(font, leading)
        w = max((font.getlength(l) for l in lines), default=0)
        return w / self.k, (lh * len(lines)) / self.k, lh / self.k

    def text(self, x, y, s, pt=7.5, weight='Regular', color='text', anchor='mm',
             max_w=None, leading=1.28, align='center'):
        """Écrit un bloc (avec retour à la ligne) ancré en (x, y).
        anchor : 'mm' centre, 'lm' gauche-milieu, 'lt' gauche-haut, 'mt' centre-haut, 'rm' droite-milieu, 'mb' centre-bas"""
        font = self.font(pt, weight)
        lines = self.wrap(s, font, max_w) if max_w else str(s).split('\n')
        bw, bh, lh = self.text_block_size(lines, font, leading)
        ax, ay = anchor[0], anchor[1]
        top = y - (bh / 2 if ay == 'm' else (bh if ay == 'b' else 0))
        col = C.get(color, color)
        asc, desc = font.getmetrics()
        # décalage pour centrer le corps des glyphes dans la ligne
        dy = (self.px(lh) - (asc + desc)) / 2 / self.k
        for i, line in enumerate(lines):
            lw = font.getlength(line) / self.k
            if align == 'center':
                cx = x - (bw / 2 if ax == 'm' else (bw if ax == 'r' else 0)) + (bw - lw) / 2
            elif align == 'left':
                cx = x - (bw / 2 if ax == 'm' else (bw if ax == 'r' else 0))
            else:
                cx = x - (bw / 2 if ax == 'm' else (bw if ax == 'r' else 0)) + (bw - lw)
            self.d.text((self.px(cx), self.px(top + i * lh + dy)), line, font=font, fill=col)
        return bw, bh

    def text_fit(self, x, y, s, max_w, pt=6.4, min_pt=5.0, weight='Regular', color='text', anchor='lm'):
        """Texte sur une seule ligne, taille réduite jusqu'à tenir dans max_w."""
        cur = pt
        while cur > min_pt and self.font(cur, weight).getlength(s) / self.k > max_w:
            cur -= 0.2
        return self.text(x, y, s, pt=cur, weight=weight, color=color, anchor=anchor)

    def vtext(self, x, y, s, pt=6.3, weight='Regular', color='muted', up=True):
        """Texte vertical (lecture de bas en haut si up) centré en (x, y)."""
        font = self.font(pt, weight)
        w = int(font.getlength(s)) + 4
        asc, desc = font.getmetrics()
        h = asc + desc + 4
        tmp = Image.new('RGBA', (w, h), (255, 255, 255, 0))
        ImageDraw.Draw(tmp).text((2, 2), s, font=font, fill=C.get(color, color))
        tmp = tmp.rotate(90 if up else -90, expand=True)
        self.im.paste(tmp, (int(self.px(x) - tmp.size[0] / 2), int(self.px(y) - tmp.size[1] / 2)), tmp)

    # ---------- formes ----------
    def rect(self, x, y, w, h, kind='box', radius=7, width=1.4, fill=None, stroke=None, dash=False):
        f, s = C[kind] if isinstance(kind, str) else kind
        f = fill or f
        s = stroke or s
        box = [self.px(x), self.px(y), self.px(x + w), self.px(y + h)]
        if dash:
            self.d.rounded_rectangle(box, radius=self.px(radius), fill=f, outline=None)
            self._dashed_rect(x, y, w, h, s, width)
        else:
            self.d.rounded_rectangle(box, radius=self.px(radius), fill=f, outline=s, width=max(1, int(self.px(width))))

    def _dashed_rect(self, x, y, w, h, color, width):
        pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            self.line(x1, y1, x2, y2, color=color, width=width, dash=(7, 5))

    def box(self, x, y, w, h, label='', kind='box', sub=None, pt=7.5, weight='Medium',
            sub_pt=6.3, radius=7, color='text', sub_color='muted', pad=8, width=1.4, dash=False,
            align='center', min_pt=5.2):
        """Boîte arrondie avec texte centré (et sous-texte optionnel). Ajuste la taille si besoin."""
        self.rect(x, y, w, h, kind, radius=radius, width=width, dash=dash)
        if not label and not sub:
            return
        # ajustement automatique de la taille pour tenir dans la boîte
        cur_pt, cur_sub = pt, sub_pt
        while True:
            f1 = self.font(cur_pt, weight)
            l1 = self.wrap(label, f1, w - 2 * pad) if label else []
            w1, h1, _ = self.text_block_size(l1, f1) if l1 else (0, 0, 0)
            if sub:
                f2 = self.font(cur_sub, 'Regular')
                l2 = self.wrap(sub, f2, w - 2 * pad)
                w2, h2, _ = self.text_block_size(l2, f2)
            else:
                w2, h2 = 0, 0
            gap = 3 if (label and sub) else 0
            if (h1 + h2 + gap <= h - 8 and max(w1, w2) <= w - 2 * pad) or cur_pt <= min_pt:
                break
            cur_pt -= 0.4
            cur_sub -= 0.3
        total = h1 + h2 + gap
        if total > h - 4:
            OVERFLOW.append((label or sub or '')[:40] + ' (%.0f > %.0f)' % (total, h))
        top = y + (h - total) / 2
        cx = x + w / 2
        if label:
            self.text(cx if align == 'center' else x + pad, top, label, pt=cur_pt, weight=weight,
                      color=color, anchor='mt' if align == 'center' else 'lt', max_w=w - 2 * pad, align=align)
        if sub:
            self.text(cx if align == 'center' else x + pad, top + h1 + gap, sub, pt=cur_sub, weight='Regular',
                      color=sub_color, anchor='mt' if align == 'center' else 'lt', max_w=w - 2 * pad, align=align)

    def diamond(self, cx, cy, w, h, label='', kind='human', pt=7, weight='Medium'):
        f, s = C[kind]
        pts = [(cx, cy - h / 2), (cx + w / 2, cy), (cx, cy + h / 2), (cx - w / 2, cy)]
        self.d.polygon([(self.px(a), self.px(b)) for a, b in pts], fill=f, outline=s, width=max(1, int(self.px(1.4))))
        if label:
            self.text(cx, cy, label, pt=pt, weight=weight, max_w=w * 0.62)

    def circle(self, cx, cy, r, kind='box', width=1.4, fill=None, stroke=None):
        f, s = C[kind]
        self.d.ellipse([self.px(cx - r), self.px(cy - r), self.px(cx + r), self.px(cy + r)],
                       fill=fill or f, outline=stroke or s, width=max(1, int(self.px(width))))

    def line(self, x1, y1, x2, y2, color='arrow', width=1.4, dash=None):
        col = C.get(color, color)
        if dash:
            on, off = dash
            L = math.hypot(x2 - x1, y2 - y1)
            if L == 0:
                return
            ux, uy = (x2 - x1) / L, (y2 - y1) / L
            t = 0
            while t < L:
                t2 = min(L, t + on)
                self.d.line([(self.px(x1 + ux * t), self.px(y1 + uy * t)), (self.px(x1 + ux * t2), self.px(y1 + uy * t2))],
                            fill=col, width=max(1, int(self.px(width))))
                t += on + off
        else:
            self.d.line([(self.px(x1), self.px(y1)), (self.px(x2), self.px(y2))], fill=col, width=max(1, int(self.px(width))))

    def head(self, x, y, angle, size=9, color='arrow'):
        col = C.get(color, color)
        a = math.radians(angle)
        p1 = (x, y)
        p2 = (x - size * math.cos(a) + size * 0.5 * math.sin(a), y - size * math.sin(a) - size * 0.5 * math.cos(a))
        p3 = (x - size * math.cos(a) - size * 0.5 * math.sin(a), y - size * math.sin(a) + size * 0.5 * math.cos(a))
        self.d.polygon([(self.px(a_), self.px(b_)) for a_, b_ in (p1, p2, p3)], fill=col)

    def arrow(self, x1, y1, x2, y2, label=None, color='arrow', width=1.4, dash=None, head=True, pt=6.2,
              label_pos=0.5, label_offset=(0, -9), label_color='muted', head_size=9):
        ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
        if head:
            # raccourcir la ligne pour ne pas dépasser la pointe
            L = math.hypot(x2 - x1, y2 - y1)
            if L > 0:
                sx, sy = x2 - (x2 - x1) / L * head_size * 0.8, y2 - (y2 - y1) / L * head_size * 0.8
            else:
                sx, sy = x2, y2
            self.line(x1, y1, sx, sy, color=color, width=width, dash=dash)
            self.head(x2, y2, ang, size=head_size, color=color)
        else:
            self.line(x1, y1, x2, y2, color=color, width=width, dash=dash)
        if label:
            lx = x1 + (x2 - x1) * label_pos + label_offset[0]
            ly = y1 + (y2 - y1) * label_pos + label_offset[1]
            self.text(lx, ly, label, pt=pt, color=label_color, anchor='mm')

    def polyline_arrow(self, pts, color='arrow', width=1.4, dash=None, label=None, pt=6.2, label_at=None,
                       label_offset=(0, -9), head=True):
        for (x1, y1), (x2, y2) in zip(pts[:-1], pts[1:]):
            last = (x2, y2) == tuple(pts[-1])
            if last and head:
                self.arrow(x1, y1, x2, y2, color=color, width=width, dash=dash)
            else:
                self.line(x1, y1, x2, y2, color=color, width=width, dash=dash)
        if label:
            if label_at is None:
                (x1, y1), (x2, y2) = pts[len(pts) // 2 - 1], pts[len(pts) // 2]
                label_at = ((x1 + x2) / 2, (y1 + y2) / 2)
            self.text(label_at[0] + label_offset[0], label_at[1] + label_offset[1], label, pt=pt, color='muted')

    def brace_label(self, x1, x2, y, label, pt=6.3, color='muted', tick=6):
        """Trait horizontal avec petites bornes et libellé au-dessous (pour annoter une zone)."""
        self.line(x1, y, x2, y, color='rule', width=1.1)
        self.line(x1, y - tick, x1, y + tick, color='rule', width=1.1)
        self.line(x2, y - tick, x2, y + tick, color='rule', width=1.1)
        self.text((x1 + x2) / 2, y + tick + 4, label, pt=pt, color=color, anchor='mt', max_w=x2 - x1)

    def axis(self, x1, y1, x2, y2, label, pt=6.3, color='muted', side='below'):
        self.arrow(x1, y1, x2, y2, color='rule', width=1.2, head_size=8)
        ang = math.atan2(y2 - y1, x2 - x1)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        if abs(math.degrees(ang)) < 45:      # horizontal
            self.text(mx, my + (8 if side == 'below' else -8), label, pt=pt, color=color,
                      anchor='mt' if side == 'below' else 'mb')
        else:                                # vertical
            self.vtext(mx + (9 if side == 'right' else -9), my, label, pt=pt, color=color)

    def cross(self, cx, cy, r=6, color='#D0665A', width=1.8):
        self.line(cx - r, cy - r, cx + r, cy + r, color=color, width=width)
        self.line(cx - r, cy + r, cx + r, cy - r, color=color, width=width)

    def check(self, cx, cy, r=6, color='#4E9C64', width=1.8):
        self.line(cx - r, cy, cx - r * 0.25, cy + r * 0.8, color=color, width=width)
        self.line(cx - r * 0.25, cy + r * 0.8, cx + r * 1.1, cy - r * 0.9, color=color, width=width)

    def badge(self, cx, cy, s, r=11, kind='dark', pt=6.4, color='white'):
        self.circle(cx, cy, r, kind=kind)
        self.text(cx, cy + 0.5, s, pt=pt, weight='SemiBold', color=color)

    # ---------- sortie ----------
    def save(self, path, margin=10):
        from PIL import ImageChops
        bg = Image.new('RGB', self.im.size, 'white')
        bbox = ImageChops.difference(self.im, bg).getbbox()
        w, h = self.im.size
        if bbox:
            top = max(0, bbox[1] - int(self.px(margin)))
            bottom = min(h, bbox[3] + int(self.px(margin)))
            im = self.im.crop((0, top, w, bottom))
        else:
            im = self.im
        out = im.resize((im.size[0] // SS, im.size[1] // SS), Image.LANCZOS)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        out.save(path, optimize=True)
        return out.size


# ---------------------------------------------------------------- gabarits

def hflow(F, items, y, h, x0=20, x1=980, gap=26, kind='box', pt=7.3, sub_pt=6.2, kinds=None,
          edge_labels=None, arrow_len=None):
    """Boîtes alignées horizontalement reliées par des flèches. Retourne la liste des rectangles (x, y, w, h)."""
    n = len(items)
    w = (x1 - x0 - gap * (n - 1)) / n
    rects = []
    for i, it in enumerate(items):
        x = x0 + i * (w + gap)
        label, sub = (it if isinstance(it, tuple) else (it, None))
        k = kinds[i] if kinds else kind
        F.box(x, y, w, h, label, kind=k, sub=sub, pt=pt, sub_pt=sub_pt)
        rects.append((x, y, w, h))
        if i < n - 1:
            lab = edge_labels[i] if edge_labels else None
            F.arrow(x + w + 2, y + h / 2, x + w + gap - 2, y + h / 2, label=lab, head_size=8)
    return rects


def vflow(F, items, x, w, y0, h, gap=22, kind='box', kinds=None, pt=7.3, sub_pt=6.2, notes=None, note_x=None,
          note_w=None, note_pt=6.4, edge_labels=None):
    """Boîtes empilées verticalement avec flèches ; notes optionnelles à droite."""
    rects = []
    for i, it in enumerate(items):
        y = y0 + i * (h + gap)
        label, sub = (it if isinstance(it, tuple) else (it, None))
        k = kinds[i] if kinds else kind
        F.box(x, y, w, h, label, kind=k, sub=sub, pt=pt, sub_pt=sub_pt)
        rects.append((x, y, w, h))
        if notes and notes[i]:
            F.text(note_x, y + h / 2, notes[i], pt=note_pt, color='muted', anchor='lm', max_w=note_w, align='left')
        if i < len(items) - 1:
            lab = edge_labels[i] if edge_labels else None
            F.arrow(x + w / 2, y + h + 2, x + w / 2, y + h + gap - 2, head_size=8,
                    label=lab, label_offset=(w / 2 - 40, 0) if lab else (0, 0))
    return rects


def cycle(F, items, cx, cy, rx, ry, bw, bh, kind='box', kinds=None, pt=7.2, sub_pt=6.1, start_deg=-90,
          clockwise=True, center_label=None, center_pt=7.5, center_kind=None, center_w=None, center_h=None):
    """Boîtes disposées en anneau (ellipse), reliées par des flèches courbes approximées."""
    n = len(items)
    centers = []
    for i in range(n):
        a = math.radians(start_deg + (360.0 / n) * i * (1 if clockwise else -1))
        centers.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    # flèches d'abord (dessous)
    for i in range(n):
        a1 = math.radians(start_deg + (360.0 / n) * i * (1 if clockwise else -1))
        a2 = math.radians(start_deg + (360.0 / n) * (i + 1) * (1 if clockwise else -1))
        pts = []
        steps = 14
        for t in range(steps + 1):
            a = a1 + (a2 - a1) * t / steps
            pts.append((cx + rx * 1.0 * math.cos(a), cy + ry * 1.0 * math.sin(a)))
        # découper la portion à l'intérieur des boîtes
        def inside(p, c):
            return abs(p[0] - c[0]) <= bw / 2 + 4 and abs(p[1] - c[1]) <= bh / 2 + 4
        seg = [p for p in pts if not inside(p, centers[i]) and not inside(p, centers[(i + 1) % n])]
        if len(seg) >= 2:
            F.polyline_arrow(seg, head=True)
    for i, it in enumerate(items):
        x, y = centers[i]
        label, sub = (it if isinstance(it, tuple) else (it, None))
        k = kinds[i] if kinds else kind
        F.box(x - bw / 2, y - bh / 2, bw, bh, label, kind=k, sub=sub, pt=pt, sub_pt=sub_pt)
    if center_label:
        if center_kind:
            cw, ch = center_w or rx * 0.9, center_h or ry * 0.6
            F.box(cx - cw / 2, cy - ch / 2, cw, ch, center_label, kind=center_kind, pt=center_pt, weight='SemiBold')
        else:
            F.text(cx, cy, center_label, pt=center_pt, weight='SemiBold', color='muted', max_w=rx * 1.2)
    return centers


def ladder(F, items, x0=40, x1=960, y_top=30, y_bottom=None, rise=None, step_h=None, kind='box', kinds=None,
           pt=7.2, sub_pt=6.1, ascending=True, axis_label=None, axis_side='right', gap=10):
    """Escalier : chaque marche est une boîte (label, sous-texte), décalée vers le haut (ou le bas)."""
    n = len(items)
    w = (x1 - x0 - gap * (n - 1)) / n
    H = F.H
    step_h = step_h or 78
    bottom_room = 46 if axis_label else 10
    y_bottom = (H - bottom_room) if y_bottom is None else y_bottom
    if rise is None:
        rise = min(40, (y_bottom - step_h - y_top) / max(1, n - 1))
    base = y_bottom - step_h
    rects = []
    for i, it in enumerate(items):
        lvl = i if ascending else (n - 1 - i)
        x = x0 + i * (w + gap)
        y = base - lvl * rise
        label, sub = (it if isinstance(it, tuple) else (it, None))
        k = kinds[i] if kinds else kind
        F.box(x, y, w, step_h, label, kind=k, sub=sub, pt=pt, sub_pt=sub_pt)
        rects.append((x, y, w, step_h))
        # ligne de sol sous la marche (effet escalier)
        F.line(x, y + step_h, x + w, y + step_h, color='rule', width=1)
    if axis_label:
        yA0 = base + step_h + 10
        F.axis(x0, yA0, x1, yA0, axis_label, side='below')
    return rects


def compare(F, left, right, y=20, h=None, x0=20, x1=980, gap=30, title_h=34, kinds=('ghost', 'box')):
    """Deux panneaux côte à côte avec titre ; retourne (rect gauche, rect droit) intérieurs."""
    h = h or (F.H - y - 20)
    w = (x1 - x0 - gap) / 2
    out = []
    for i, (title, kind) in enumerate(((left, kinds[0]), (right, kinds[1]))):
        x = x0 + i * (w + gap)
        F.rect(x, y, w, h, kind=kind, radius=9, width=1.2)
        f, s = C[kind]
        F.d.rounded_rectangle([F.px(x), F.px(y), F.px(x + w), F.px(y + title_h)], radius=F.px(9), fill=s)
        F.d.rectangle([F.px(x), F.px(y + title_h - 9), F.px(x + w), F.px(y + title_h)], fill=s)
        F.text_fit(x + w / 2, y + title_h / 2, title, w - 16, pt=7.6, min_pt=5.6, weight='SemiBold', color='white', anchor='mm')
        out.append((x, y + title_h, w, h - title_h))
    return out


def pill(F, cx, cy, s, kind='ghost', pt=6.2, padx=9, h=18, weight='Medium', color='text'):
    font = F.font(pt, weight)
    w = font.getlength(s) / F.k + 2 * padx
    F.rect(cx - w / 2, cy - h / 2, w, h, kind=kind, radius=h / 2, width=1.1)
    F.text(cx, cy, s, pt=pt, weight=weight, color=color)
    return w


def note(F, x, y, w, s, kind='ghost', pt=6.4, h=None, weight='Regular', color='text', radius=6, align='center'):
    """Encadré de remarque (texte multi-lignes)."""
    font = F.font(pt, weight)
    lines = F.wrap(s, font, w - 20)
    bw, bh, lh = F.text_block_size(lines, font)
    h = h or bh + 14
    F.rect(x, y, w, h, kind=kind, radius=radius, width=1.1)
    F.text(x + w / 2 if align == 'center' else x + 10, y + h / 2, s, pt=pt, weight=weight, color=color,
           anchor='mm' if align == 'center' else 'lm', max_w=w - 20, align=align)
    return h


REGISTRY = []


def fig(fid, anchor, caption, h, mode='after'):
    """Décorateur d'enregistrement d'une figure.
    anchor : {'fr': (style, fragment), 'en': (style, fragment)}
    mode   : 'after' (insérer après le paragraphe) ou 'replace_code' (remplacer le bloc de code contigu)."""
    def deco(fn):
        REGISTRY.append(dict(id=fid, anchor=anchor, caption=caption, h=h, mode=mode, draw=fn))
        return fn
    return deco
