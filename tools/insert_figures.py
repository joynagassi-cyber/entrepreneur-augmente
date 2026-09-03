"""Insère les figures explicatives (images/figures/manifest.json) dans les deux manuscrits.

Pour chaque figure du manifeste :
  - mode 'after'        : image + légende insérées juste après le paragraphe d'ancrage ;
  - mode 'replace_code' : le bloc CodeBlock contigu contenant l'ancrage (souvent un
                          diagramme Mermaid en texte) est retiré, image + légende
                          insérées à sa place.
Toutes les légendes « Fig. N — … » (existantes + nouvelles) sont ensuite renumérotées
dans l'ordre du document. Idempotent : les figures déjà présentes (repérées par le nom
de fichier media) ne sont pas insérées deux fois.

Usage : python3 tools/insert_figures.py [--dry-run]
"""
import copy
import json
import os
import re
import shutil
import sys
import zipfile
from xml.etree import ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
WP = '{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}'
PIC = '{http://schemas.openxmlformats.org/drawingml/2006/picture}'
RN = 'http://schemas.openxmlformats.org/package/2006/relationships'
CT = '{http://schemas.openxmlformats.org/package/2006/content-types}'
XML_SPACE = '{http://www.w3.org/XML/1998/namespace}space'
for k, v in [('w', W), ('a', A), ('r', R), ('wp', WP), ('pic', PIC)]:
    ET.register_namespace(k, v[1:-1])
ET.register_namespace('mc', 'http://schemas.openxmlformats.org/markup-compatibility/2006')

EMU = 914400
IMG_W_IN = 4.17                      # même largeur que les figures existantes (cx = 3 810 000 EMU)
IMG_W = int(IMG_W_IN * EMU)
DOCPR_BASE = 1000                    # ids docPr uniques pour les nouveaux dessins
CAPTION_RE = re.compile(r'^Fig\.\s*\d+\s*—\s*')

DOCS = [('L-Entrepreneur-Augmente.docx', 'fr'), ('The-Augmented-Entrepreneur.docx', 'en')]


def para_text(p):
    return ''.join(n.text or '' for n in p.iter(W + 't'))


def para_style(p):
    s = p.find(W + 'pPr/' + W + 'pStyle')
    return s.get(W + 'val') if s is not None else 'Normal'


def png_size(data):
    # IHDR : largeur/hauteur en big-endian aux octets 16..24
    return int.from_bytes(data[16:20], 'big'), int.from_bytes(data[20:24], 'big')


def image_paragraph(rid, docpr_id, cx, cy, name):
    xml = f'''<w:p xmlns:w="{W[1:-1]}" xmlns:r="{R[1:-1]}" xmlns:a="{A[1:-1]}"
 xmlns:wp="{WP[1:-1]}" xmlns:pic="{PIC[1:-1]}">
<w:pPr><w:keepNext/><w:spacing w:before="120" w:after="40"/><w:jc w:val="center"/></w:pPr>
<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">
<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent t="0" r="0" b="0" l="0"/>
<wp:docPr id="{docpr_id}" name="{name}" descr="" title=""/>
<wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>
<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
<pic:pic><pic:nvPicPr><pic:cNvPr id="0" name="{name}" descr=""/>
<pic:cNvPicPr><a:picLocks noChangeAspect="1" noChangeArrowheads="1"/></pic:cNvPicPr></pic:nvPicPr>
<pic:blipFill><a:blip r:embed="{rid}" cstate="none"/><a:srcRect/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
<pic:spPr bwMode="auto"><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>
<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>
</a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'''
    return ET.fromstring(xml)


def process(path, lang, manifest, dry_run=False):
    z = zipfile.ZipFile(path)
    names = z.namelist()
    raw = {n: z.read(n) for n in names}
    z.close()

    relroot = ET.fromstring(raw['word/_rels/document.xml.rels'])
    ctroot = ET.fromstring(raw['[Content_Types].xml'])
    defaults = {e.get('Extension') for e in ctroot if e.tag == CT + 'Default'}
    if 'png' not in defaults:
        d = ET.SubElement(ctroot, CT + 'Default')
        d.set('Extension', 'png')
        d.set('ContentType', 'image/png')
    # les 13 figures d'origine sont des PNG stockés avec l'extension « .undefined » sans type
    # de contenu déclaré : Word tolère, les lecteurs stricts (python-docx…) refusent le fichier.
    if 'undefined' not in defaults and any(n.startswith('word/media/') and n.endswith('.undefined') for n in names):
        d = ET.SubElement(ctroot, CT + 'Default')
        d.set('Extension', 'undefined')
        d.set('ContentType', 'image/png')
    existing_targets = {rel.get('Target') for rel in relroot}
    existing_rids = {rel.get('Id') for rel in relroot}

    doc = ET.fromstring(raw['word/document.xml'])
    body = doc.find(W + 'body')

    # index parent de chaque paragraphe (les paragraphes peuvent être dans des cellules de tableau)
    parent_of = {}
    for par in doc.iter():
        for ch in par:
            if ch.tag == W + 'p':
                parent_of[ch] = par

    # modèle de légende : la première légende numérotée existante
    capmodel = None
    for p in doc.iter(W + 'p'):
        if para_style(p) == 'Caption' and CAPTION_RE.match(para_text(p)):
            capmodel = p
            break
    if capmodel is None:
        raise SystemExit(f'{path}: aucune légende « Fig. N — » trouvée pour servir de modèle')

    inserted = skipped = 0
    for n, spec in enumerate(manifest):
        style, frag = spec['anchor'][lang]
        img_path = spec['files'][lang]['path']
        media_name = f"fig-{spec['id']}.png"
        target = 'media/' + media_name
        if target in existing_targets:
            skipped += 1
            continue

        hits = [p for p in doc.iter(W + 'p') if para_style(p) == style and frag in para_text(p)]
        if len(hits) != 1:
            print(f"  !! {spec['id']} [{lang}] : ancre trouvée {len(hits)} fois — ignorée ({frag[:50]!r})")
            continue
        anchor = hits[0]
        par = parent_of[anchor]
        kids = list(par)
        idx = kids.index(anchor)

        if spec['mode'] == 'replace_code':
            if style != 'CodeBlock':
                raise SystemExit(f"{spec['id']} : replace_code exige une ancre CodeBlock")
            a = idx
            while a - 1 >= 0 and kids[a - 1].tag == W + 'p' and para_style(kids[a - 1]) == 'CodeBlock':
                a -= 1
            b = idx
            while b + 1 < len(kids) and kids[b + 1].tag == W + 'p' and para_style(kids[b + 1]) == 'CodeBlock':
                b += 1
            removed = kids[a:b + 1]
            if not dry_run:
                for p in removed:
                    par.remove(p)
            insert_at = a
            note = f'remplace {len(removed)} lignes CodeBlock'
        else:
            insert_at = idx + 1
            note = 'après le paragraphe'

        data = open(img_path, 'rb').read()
        w_px, h_px = png_size(data)
        cx = IMG_W
        cy = int(IMG_W * h_px / w_px)

        rid = f"rIdFig{n:03d}"
        assert rid not in existing_rids
        rel = ET.SubElement(relroot, '{%s}Relationship' % RN)
        rel.set('Id', rid)
        rel.set('Type', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/image')
        rel.set('Target', target)
        raw['word/' + target] = data
        if 'word/' + target not in names:
            names.append('word/' + target)

        pimg = image_paragraph(rid, DOCPR_BASE + n, cx, cy, media_name)
        pcap = copy.deepcopy(capmodel)
        ts = list(pcap.iter(W + 't'))
        ts[0].text = 'Fig. 0 — ' + spec['caption'][lang]      # numéro provisoire, renuméroté ci-dessous
        ts[0].set(XML_SPACE, 'preserve')
        for t in ts[1:]:
            t.text = ''
        if not dry_run:
            par.insert(insert_at, pcap)
            par.insert(insert_at, pimg)
        inserted += 1
        print(f"  + {spec['id']:22} [{lang}] {note} — {IMG_W_IN:.2f} in × {cy / EMU:.2f} in")

    # renumérotation de toutes les légendes « Fig. N — » dans l'ordre du document
    k = 0
    for p in doc.iter(W + 'p'):
        if para_style(p) != 'Caption':
            continue
        txt = para_text(p)
        if not CAPTION_RE.match(txt):
            continue
        k += 1
        new = CAPTION_RE.sub(f'Fig. {k} — ', txt, count=1)
        ts = list(p.iter(W + 't'))
        ts[0].text = new
        ts[0].set(XML_SPACE, 'preserve')
        for t in ts[1:]:
            t.text = ''

    if dry_run:
        print(f'{path}: {inserted} figures à insérer, {skipped} déjà présentes, {k} légendes numérotées (dry-run)')
        return

    raw['word/document.xml'] = ET.tostring(doc, encoding='UTF-8', xml_declaration=True)
    raw['word/_rels/document.xml.rels'] = ET.tostring(relroot, encoding='UTF-8', xml_declaration=True)
    raw['[Content_Types].xml'] = ET.tostring(ctroot, encoding='UTF-8', xml_declaration=True)
    tmp = path + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zo:
        # [Content_Types].xml en tête, comme l'exige la plupart des lecteurs
        order = ['[Content_Types].xml'] + [nm for nm in names if nm != '[Content_Types].xml']
        for nm in order:
            zo.writestr(nm, raw[nm])
    shutil.move(tmp, path)
    print(f'{path}: {inserted} figures insérées, {skipped} déjà présentes, {k} légendes numérotées')


if __name__ == '__main__':
    dry = '--dry-run' in sys.argv
    manifest = json.load(open('images/figures/manifest.json'))
    for path, lang in DOCS:
        process(path, lang, manifest, dry_run=dry)
