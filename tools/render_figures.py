# -*- coding: utf-8 -*-
"""Rend toutes les figures enregistrées (FR + EN) dans images/figures/{fr,en}/<id>.png
et écrit images/figures/manifest.json (id, ancre, légende, dimensions).

Usage : python3 tools/render_figures.py [id-substring ...]
"""
import sys, os, json, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import figlib
from figlib import Fig, REGISTRY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'images', 'figures')

MODULES = ['figures_part1', 'figures_part2', 'figures_part3', 'figures_part4']
for m in MODULES:
    try:
        importlib.import_module(m)
    except ModuleNotFoundError as e:
        if m not in str(e):
            raise

filt = sys.argv[1:]
manifest = []
for spec in REGISTRY:
    if filt and not any(f in spec['id'] for f in filt):
        continue
    entry = dict(id=spec['id'], anchor=spec['anchor'], caption=spec['caption'], mode=spec['mode'], files={})
    for L in ('fr', 'en'):
        figlib.OVERFLOW.clear()
        F = Fig(1000, spec['h'])
        spec['draw'](F, L)
        for o in figlib.OVERFLOW:
            print('   !! déborde [%s] %s' % (L, o))
        path = os.path.join(OUT, L, spec['id'] + '.png')
        size = F.save(path)
        entry['files'][L] = dict(path=os.path.relpath(path, ROOT), w=size[0], h=size[1])
    manifest.append(entry)
    print('%-26s %4dx%-4d' % (spec['id'], entry['files']['fr']['w'], entry['files']['fr']['h']))

if not filt:
    json.dump(manifest, open(os.path.join(OUT, 'manifest.json'), 'w'), ensure_ascii=False, indent=1)
print(len(manifest), 'figures')
