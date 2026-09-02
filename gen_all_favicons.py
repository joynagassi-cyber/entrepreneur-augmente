# -*- coding: utf-8 -*-
"""
Generate deterministic monogram favicons for EVERY canonical tool in the merged
directory (seed + OpenAlternative), writing them to output/assets/favicons/.

Reuses the same deterministic letter-mark design as openalternative/gen_favicons.py
so the Word documents (which embed favicons) and the assets manifest stay consistent.
Official favicons are behind a blocked CDN; these are placeholders until real logos
are collected before publication.
"""
import os, json, hashlib
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output", "assets", "favicons")
os.makedirs(OUT, exist_ok=True)

PALETTES = [
    ((34, 211, 238), (59, 130, 246)),
    ((168, 85, 247), (236, 72, 153)),
    ((52, 211, 153), (16, 185, 129)),
    ((251, 191, 36), (245, 158, 11)),
    ((239, 68, 68), (190, 24, 93)),
    ((96, 165, 250), (37, 99, 235)),
    ((244, 114, 182), (192, 38, 211)),
    ((45, 212, 191), (20, 184, 166)),
    ((163, 230, 53), (132, 204, 22)),
    ((129, 140, 248), (79, 70, 229)),
]


def hexid(name):
    return hashlib.md5(name.encode("utf-8")).hexdigest()


def colors_for(name):
    return PALETTES[int(hexid(name)[:4], 16) % len(PALETTES)]


def initials(name):
    parts = [p for p in name.replace("-", " ").split() if p]
    if not parts:
        return "?"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()


def slug(n):
    import re
    return re.sub(r"[^a-z0-9]+", "-", str(n).lower()).strip("-") or "x"


def make(name):
    size = 256
    (c1, c2) = colors_for(name)  # c1 = fg (top-left), c2 = bg (bottom-right)
    img = Image.new("RGB", (size, size), (24, 24, 27))
    draw = ImageDraw.Draw(img)
    # diagonal gradient background drawn as interpolated horizontal stripes (fast)
    for y in range(size):
        t = y / size
        r = int(c2[0] * (1 - t) + c1[0] * t)
        g = int(c2[1] * (1 - t) + c1[1] * t)
        b = int(c2[2] * (1 - t) + c1[2] * t)
        draw.line([(0, y), (size, y)], fill=(r, g, b))
    draw = ImageDraw.Draw(img)
    txt = initials(name)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)
    except Exception:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), txt, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size - w) / 2 - bbox[0], (size - h) / 2 - bbox[1]),
              txt, font=font, fill=(255, 255, 255))
    img.save(os.path.join(OUT, slug(name) + ".png"))


def main():
    d = json.load(open(os.path.join(HERE, "output", "software_tool_directory_2026.json")))
    names = {t["name"] for t in d["tools"]}
    count = 0
    for n in sorted(names):
        p = os.path.join(OUT, slug(n) + ".png")
        if not os.path.exists(p):
            make(n)
            count += 1
    # also ensure OpenAlternative favicons are present for backward-compatible references
    print(f"favicons generated (new): {count}; total tools: {len(names)}")


if __name__ == "__main__":
    main()
