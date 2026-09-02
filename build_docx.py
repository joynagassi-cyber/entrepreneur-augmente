# -*- coding: utf-8 -*-
"""
Generate the bilingual (EN/FR) Word documents for the 2026 Software & AI Tool Directory.

Native Word elements only: headings, paragraphs, tables, hyperlinks, bullets, images,
page breaks, document metadata. No PDF intermediate, no screenshots.
"""
import os, sys, json, re, datetime
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "output")
sys.path.insert(0, HERE)

d = json.load(open(os.path.join(OUT, "software_tool_directory_2026.json")))
CATS = json.load(open(os.path.join(OUT, "categories_2026.json")))
TOOLS = d["tools"]
TODAY = datetime.date.today().strftime("%B %d, %Y")


# ---------------- bilingual text ----------------
LANG = {
    "en": {
        "title": "2026 Software & AI Tool Directory",
        "subtitle": "A decision-oriented guide to open-source and commercial software",
        "intro_heading": "Introduction",
        "how_heading": "How to Use This Directory",
        "choose_heading": "How to Choose the Right Tool",
        "part_obj": "PART I — Find a Tool by Objective",
        "part_user": "PART II — Find a Tool by User Profile",
        "part_tech": "PART III — Find a Tool by Technical Level",
        "part_cat": "PART IV — Software Categories",
        "part_oss": "PART V — Open-Source & Self-Hosted Alternatives",
        "part_commercial": "PART VI — Commercial Leaders",
        "part_decisions": "PART VII — Decision Maps",
        "part_matrix": "PART VIII — Reference Matrices",
        "appendix": "Appendices",
        "sources": "Sources",
        "verified": "Last Verified Information",
        "obj_label": "Objective",
        "tools_label": "Recommended tools",
        "profile_label": "Profile",
        "tech_label": "Technical level",
        "cat_label": "Category",
        "subcat": "Sub-categories",
        "tool": "Tool",
        "category": "Category",
        "license": "License",
        "difficulty": "Difficulty",
        "setup": "Setup effort",
        "hosting": "Hosting",
        "price": "Pricing",
        "best_for": "Choose this when",
        "avoid_when": "Avoid this when",
        "choose_other": "Choose another when",
        "reco": "Recommended tools",
        "oss_alt": "Open-source alternatives",
        "commercial": "Commercial leaders",
        "what_obj": "What are you trying to accomplish?",
        "table_caption": "Comparison table",
        "intro_cat": "In this section",
        "generated": "Generated",
        "count": "tools documented",
        "nav_by_cat": "By category",
        "nav_by_obj": "By objective",
        "nav_by_user": "By user",
        "nav_by_tech": "By technical level",
        "nav_by_setup": "By setup",
    },
    "fr": {
        "title": "Annuaire des Logiciels et de l'IA 2026",
        "subtitle": "Un guide décisionnel des logiciels open source et commerciaux",
        "intro_heading": "Introduction",
        "how_heading": "Comment utiliser cet annuaire",
        "choose_heading": "Comment choisir le bon outil",
        "part_obj": "PARTIE I — Trouver un outil par objectif",
        "part_user": "PARTIE II — Trouver un outil par profil d'utilisateur",
        "part_tech": "PARTIE III — Trouver un outil par niveau technique",
        "part_cat": "PARTIE IV — Catégories de logiciels",
        "part_oss": "PARTIE V — Alternatives open source et auto-hébergées",
        "part_commercial": "PARTIE VI — Leaders commerciaux",
        "part_decisions": "PARTIE VII — Cartes de décision",
        "part_matrix": "PARTIE VIII — Matrices de référence",
        "appendix": "Annexes",
        "sources": "Sources",
        "verified": "Informations vérifiées en dernier",
        "obj_label": "Objectif",
        "tools_label": "Outils recommandés",
        "profile_label": "Profil",
        "tech_label": "Niveau technique",
        "cat_label": "Catégorie",
        "subcat": "Sous-catégories",
        "tool": "Outil",
        "category": "Catégorie",
        "license": "Licence",
        "difficulty": "Difficulté",
        "setup": "Effort d'installation",
        "hosting": "Hébergement",
        "price": "Tarification",
        "best_for": "Choisissez cet outil si",
        "avoid_when": "Évitez cet outil si",
        "choose_other": "Choisissez un autre outil si",
        "reco": "Outils recommandés",
        "oss_alt": "Alternatives open source",
        "commercial": "Leaders commerciaux",
        "what_obj": "Que cherchez-vous à accomplir ?",
        "table_caption": "Tableau comparatif",
        "intro_cat": "Dans cette section",
        "generated": "Généré le",
        "count": "outils documentés",
        "nav_by_cat": "Par catégorie",
        "nav_by_obj": "Par objectif",
        "nav_by_user": "Par utilisateur",
        "nav_by_tech": "Par niveau technique",
        "nav_by_setup": "Par installation",
    },
}


# ---------------- helpers ----------------
FAV_DIR = os.path.join(HERE, "output", "assets", "favicons")


def slugify(n):
    return re.sub(r"[^a-z0-9]+", "-", str(n).lower()).strip("-") or "x"


def favicon_path(name):
    p = os.path.join(FAV_DIR, slugify(name) + ".png")
    return p if os.path.exists(p) else None


def add_tool_cell(cell, name):
    """Add an optional favicon image + tool name into a table cell."""
    cell.text = ""
    p = cell.paragraphs[0]
    img = favicon_path(name)
    if img:
        try:
            run = p.add_run()
            run.add_picture(img, width=Inches(0.22), height=Inches(0.22))
        except Exception:
            pass
    r = p.add_run("  " + name)
    r.bold = True


def set_cell_bg(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color)
    tcPr.append(shd)


def add_hyperlink(paragraph, url, text, color="1155CC", underline=True):
    part = paragraph.part
    r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    if color:
        c = OxmlElement("w:color"); c.set(qn("w:val"), color); rPr.append(c)
    if underline:
        u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rPr.append(u)
    new_run.append(rPr)
    t = OxmlElement("w:t"); t.text = text; new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink


def add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style="List Bullet")
    if bold_prefix:
        r = p.add_run(bold_prefix); r.bold = True
    p.add_run(text)
    return p


def add_page_num_footer(doc):
    section = doc.sections[0]
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE")
    run._r.addnext(fld)


# ---------------- content builders ----------------
def build_report(doc, L):
    # Title
    h = doc.add_heading(L["title"], level=0)
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(L["subtitle"]); r.italic = True; r.font.color.rgb = RGBColor(0x64, 0x74, 0x8b)
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.add_run(f"{L['generated']}: {TODAY}  •  {len(TOOLS)} {L['count']}").font.color.rgb = RGBColor(0x94, 0xa3, 0xb8)


def build_user_profiles(doc, L):
    """PART II — navigate by user profile / persona."""
    doc.add_heading(L["part_user"], level=1)
    profiles = [
        ("beginner", ("Beginner / no-code user", "Débutant / utilisateur sans code"), "prod-notes"),
        ("solo", ("Solo creator & freelancer", "Créateur solo & indépendant"), "business"),
        ("startup", ("Startup team", "Équipe de startup"), "biz-pm"),
        ("developer", ("Developer / engineer", "Développeur / ingénieur"), "dev"),
        ("data-scientist", ("Data scientist / ML engineer", "Data scientist / ingénieur ML"), "ai-ml-infra"),
        ("self-hoster", ("Privacy advocate / self-hoster", "Défenseur de la vie privée / auto-hébergeur"), "selfhost"),
    ]
    for key, (en, fr), cat in profiles:
        matched = [t for t in TOOLS if cat in t["categories"]]
        doc.add_heading(en if L is LANG["en"] else fr, level=2)
        doc.add_paragraph(f"{L['tools_label']}: " + ", ".join(t["name"] for t in matched[:8]) or "—")


def build_tech_level(doc, L):
    """PART III — navigate by technical level / setup effort."""
    doc.add_heading(L["part_tech"], level=1)
    levels = ["Beginner", "Intermediate", "Advanced", "Expert"]
    for lvl in levels:
        matched = [t for t in TOOLS if t["difficulty"] == lvl or t["difficulty"].startswith(lvl)]
        doc.add_heading(lvl, level=2)
        doc.add_paragraph(f"{L['tools_label']}: " + ", ".join(t["name"] for t in matched[:8]) or "—")
    # Setup effort
    doc.add_heading(L["setup"], level=2)
    for setup in ["Minimal", "Moderate", "Complex"]:
        matched = [t for t in TOOLS if t["setup_effort"] == setup]
        doc.add_paragraph(f"{setup}: " + ", ".join(t["name"] for t in matched[:6]) or "—")


def build_objectives(doc, L):
    doc.add_heading(L["part_obj"], level=1)
    objectives = [
        ("build-app", "Build a web application", "Construire une application web"),
        ("build-saas", "Build a SaaS quickly", "Construire un SaaS rapidement"),
        ("build-mobile", "Build a mobile application", "Construire une application mobile"),
        ("test-on-device", "Test on a physical phone", "Tester sur un téléphone physique"),
        ("agent-automation", "Automate with AI agents", "Automatiser avec des agents IA"),
        ("run-llm", "Run/use huge language models", "Exécuter/utiliser de grands modèles de langage"),
        ("prototype-fast", "Fastest prototype", "Prototype le plus rapide"),
        ("developer-control", "Full control over code", "Contrôle total du code"),
        ("self-host", "Self-host my tools", "Auto-héberger mes outils"),
        ("open-source", "Use open source", "Utiliser de l'open source"),
    ]
    for oid, en, fr in objectives:
        matched = [t for t in TOOLS if oid in (t.get("objectives") or [])]
        if not matched:
            matched = [t for t in TOOLS if oid in " ".join(t["categories"])]
        doc.add_heading(en if L is LANG["en"] else fr, level=2)
        name = ",".join(t["name"] for t in matched[:6]) if matched else "—"
        doc.add_paragraph(f"{L['tools_label']}: {name}")


def build_decisions(doc, L):
    doc.add_heading(L["part_decisions"], level=1)
    decisions = [
        ("want_open_source", ("I want open source", "Je veux de l'open source")),
        ("want_selfhost", ("I want self-hosting", "Je veux de l'auto-hébergement")),
        ("want_avoid_setup", ("I want to avoid technical setup", "Je veux éviter la configuration technique")),
        ("want_mobile", ("I want mobile support", "Je veux un support mobile")),
        ("want_deploy_fast", ("I want to deploy quickly", "Je veux déployer rapidement")),
        ("want_control", ("I want complete control", "Je veux un contrôle total")),
    ]
    for key, (en, fr) in decisions:
        catmap = {"want_open_source": "selfhost", "want_selfhost": "selfhost",
                  "want_avoid_setup": "prod-notes", "want_mobile": "dev-mobile",
                  "want_deploy_fast": "dev-devops", "want_control": "dev"}
        catid = catmap.get(key)
        matched = [t for t in TOOLS if catid and catid in t["categories"]]
        doc.add_heading(en if L is LANG["en"] else fr, level=2)
        doc.add_paragraph(f"{L['tools_label']}: " + ", ".join(t["name"] for t in matched[:8]))


def build_categories(doc, L):
    doc.add_heading(L["part_cat"], level=1)
    for cat in CATS["categories"]:
        doc.add_heading(cat["name_en"] if L is LANG["en"] else cat["name_fr"], level=2)
        doc.add_paragraph((cat["description_en"] if L is LANG["en"] else cat["description_fr"]))
        # Recommended tools
        idline = cat["id"]
        matched = [t for t in TOOLS if idline in t["categories"]]
        # open-source vs commercial leaders
        oss = [t for t in matched if t["open_source"]]
        comm = [t for t in matched if not t["open_source"]]
        p = doc.add_paragraph()
        r = p.add_run(f"{L['reco']}: "); r.bold = True
        p.add_run(", ".join(t["name"] for t in matched[:8]) if matched else "—")
        if L is LANG["en"]:
            add_bullet(doc, ", ".join(t["name"] for t in oss[:6]) or "—", bold_prefix=L["oss_alt"] + ": ")
            add_bullet(doc, ", ".join(t["name"] for t in comm[:6]) or "—", bold_prefix=L["commercial"] + ": ")
            add_bullet(doc, ", ".join(t["name"] for t in matched[:6]) or "—", bold_prefix=L["what_obj"] + ": ")
        else:
            add_bullet(doc, ", ".join(t["name"] for t in oss[:6]) or "—", bold_prefix=L["oss_alt"] + " : ")
            add_bullet(doc, ", ".join(t["name"] for t in comm[:6]) or "—", bold_prefix=L["commercial"] + " : ")
            add_bullet(doc, ", ".join(t["name"] for t in matched[:6]) or "—", bold_prefix=L["what_obj"] + " : ")
        build_comparison_table(doc, matched[:6], L)
        doc.add_paragraph("")


def build_comparison_table(doc, tools, L):
    if not tools:
        return
    doc.add_paragraph(L["table_caption"]).runs[0].bold = True
    table = doc.add_table(rows=1, cols=6)
    table.style = "Light Grid Accent 1"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table.rows[0].cells
    headers = [L["tool"], L["category"], L["license"], L["difficulty"], L["setup"], L["hosting"]]
    for i, htxt in enumerate(headers):
        hdr[i].text = ""
        run = hdr[i].paragraphs[0].add_run(htxt); run.bold = True
        set_cell_bg(hdr[i], "D9E2F3")
    for t in tools:
        cells = table.add_row().cells
        vals = [
            t["name"],
            ",".join(t["categories"][:2]) if t["categories"] else "",
            t.get("verified_license") or t["license"],
            t["difficulty"],
            t["setup_effort"],
            ",".join(t["hosting"]) if t["hosting"] else "",
        ]
        for i, v in enumerate(vals):
            cells[i].text = ""
            cells[i].paragraphs[0].add_run(str(v))


def build_oss_part(doc, L):
    doc.add_heading(L["part_oss"], level=1)
    doc.add_paragraph(
        "Open-source and self-hosted tools give you control over your data and code. The table below "
        "lists the open-source & self-hosted tools in this directory with verified licenses." if L is LANG["en"] else
        "Les outils open source et auto-hébergés vous donnent le contrôle de vos données et de votre code. "
        "Le tableau ci-dessous recense les outils open source et auto-hébergés de cet annuaire avec leurs "
        "licences vérifiées."
    )
    oss = [t for t in TOOLS if t["open_source"] and t["self_hosted"]]
    table = doc.add_table(rows=1, cols=4)
    table.style = "Light Grid Accent 1"
    hdr = table.rows[0].cells
    for i, htxt in enumerate([L["tool"], L["license"], L["hosting"], "GitHub"]):
        hdr[i].text = ""
        run = hdr[i].paragraphs[0].add_run(htxt); run.bold = True
        set_cell_bg(hdr[i], "D9E2F3")
    for t in oss:
        cells = table.add_row().cells
        add_tool_cell(cells[0], t["name"])
        cells[1].text = t.get("verified_license") or t["license"]
        cells[2].text = ", ".join(t["hosting"])
        cells[3].text = ""
        if t.get("repository"):
            add_hyperlink(cells[3].paragraphs[0], t["repository"], "repo", color="1155CC")


def build_commercial_part(doc, L):
    doc.add_heading(L["part_commercial"], level=1)
    doc.add_paragraph(
        "Commercial leaders are often the most convenient choice. They are listed here for comparison "
        "against the open-source alternatives in the previous sections." if L is LANG["en"] else
        "Les leaders commerciaux sont souvent le choix le plus pratique. Ils sont listés ici pour "
        "comparaison avec les alternatives open source des sections précédentes."
    )
    comm = [t for t in TOOLS if not t["open_source"]]
    table = doc.add_table(rows=1, cols=4)
    table.style = "Light Grid Accent 1"
    hdr = table.rows[0].cells
    for i, htxt in enumerate([L["tool"], L["category"], L["price"], L["best_for"]]):
        hdr[i].text = ""
        run = hdr[i].paragraphs[0].add_run(htxt); run.bold = True
        set_cell_bg(hdr[i], "D9E2F3")
    for t in comm:
        cells = table.add_row().cells
        add_tool_cell(cells[0], t["name"])
        cells[1].text = ",".join(t["categories"][:2])
        cells[2].text = t["pricing_model"]
        cells[3].text = t["best_for"][:160]


def build_ref_matrix(doc, L):
    doc.add_heading(L["part_matrix"], level=1)
    doc.add_paragraph(
        "The full machine-readable comparison matrix is in tool_comparison_matrix_2026.csv. Below is a "
        "summary table of every documented tool with its key decision fields." if L is LANG["en"] else
        "La matrice de comparaison complète lisible par machine se trouve dans "
        "tool_comparison_matrix_2026.csv. Voici un tableau récapitulatif de chaque outil documenté avec "
        "ses champs de décision clés."
    )
    table = doc.add_table(rows=1, cols=6)
    table.style = "Light Grid Accent 1"
    hdr = table.rows[0].cells
    for i, htxt in enumerate([L["tool"], L["category"], L["license"], L["difficulty"], L["setup"], L["price"]]):
        hdr[i].text = ""
        run = hdr[i].paragraphs[0].add_run(htxt); run.bold = True
        set_cell_bg(hdr[i], "D9E2F3")
    for t in TOOLS:
        cells = table.add_row().cells
        add_tool_cell(cells[0], t["name"])
        cells[1].text = ",".join(t["categories"][:2])
        cells[2].text = t.get("verified_license") or t["license"]
        cells[3].text = t["difficulty"]
        cells[4].text = t["setup_effort"]
        cells[5].text = t["pricing_model"]


def build_appendix(doc, L):
    doc.add_heading(L["appendix"], level=1)
    doc.add_heading(L["sources"], level=2)
    reg = json.load(open(os.path.join(OUT, "source_registry.json")))
    for s in reg["sources"]:
        doc.add_paragraph(f"•  {s['source']} — {s['purpose']} ({s['crawl_status']})")
    doc.add_heading(L["verified"], level=2)
    doc.add_paragraph(f"{L['generated']}: {TODAY}")


def build_guide(OUT_PATH, lang):
    L = LANG[lang]
    doc = Document()
    # set metadata
    cp = doc.core_properties
    cp.title = L["title"]
    cp.subject = "Software & AI tool directory"
    cp.author = "Open-source directory builder"

    # Title page then page break
    build_report(doc, L)
    doc.add_page_break()

    # Front matter (Introduction / How to use / How to choose) as Heading 1
    doc.add_heading(L["intro_heading"], level=1)
    doc.add_paragraph(
        "This directory is a decision-oriented guide. For each software or AI tool it answers "
        "three questions: WHEN SHOULD I USE THIS TOOL? WHEN SHOULD I NOT USE THIS TOOL? AND WHEN "
        "SHOULD I CHOOSE ANOTHER TOOL INSTEAD? It pairs commercial leaders with their open-source "
        "and self-hosted alternatives." if L is LANG["en"] else
        "Cet annuaire est un guide décisionnel. Pour chaque logiciel ou outil d'IA, il répond à trois "
        "questions : QUAND DOIS-JE UTILISER CET OUTIL ? QUAND NE PAS L'UTILISER ? ET QUAND CHOISIR UN "
        "AUTRE OUTIL À LA PLACE ? Il met en regard les leaders commerciaux et leurs alternatives open "
        "source et auto-hébergées."
    )
    doc.add_heading(L["how_heading"], level=1)
    doc.add_paragraph(
        "Navigate by category, by objective, by user profile, by technical level, by setup effort, "
        "by hosting preference, by budget, or by openness. Every tool record carries a difficulty, "
        "setup effort, technical involvement, deployment effort, and maintenance rating, so two tools "
        "that do the same thing can still be the right or wrong choice for a given reader." if L is LANG["en"] else
        "Naviguez par catégorie, par objectif, par profil d'utilisateur, par niveau technique, par effort "
        "d'installation, par préférence d'hébergement, par budget ou par ouverture. Chaque fiche outil "
        "comporte une difficulté, un effort d'installation, une implication technique, un effort de "
        "déploiement et une maintenance, si bien que deux outils équivalents peuvent être le bon ou le "
        "mauvais choix selon le lecteur."
    )
    doc.add_heading(L["choose_heading"], level=1)
    doc.add_paragraph(
        "Do not ask 'which tool is better?'. Ask 'which tool is better for this user and this situation?' "
        "A powerful tool can be the wrong choice for a beginner, and a simple tool the wrong choice for a "
        "developer needing deep customization. The directory makes these trade-offs explicit." if L is LANG["en"] else
        "Ne demandez pas « quel outil est meilleur ? ». Demandez « quel outil est meilleur pour cet "
        "utilisateur et cette situation ? ». Un outil puissant peut être un mauvais choix pour un "
        "débutant, et un outil simple un mauvais choix pour un développeur exigeant une personnalisation "
        "poussée. L'annuaire rend ces arbitrages explicites."
    )
    doc.add_page_break()

    # Part I — objectives
    build_objectives(doc, L)
    doc.add_page_break()

    # Part II — user profiles
    build_user_profiles(doc, L)
    doc.add_page_break()

    # Part III — technical level & setup
    build_tech_level(doc, L)
    doc.add_page_break()

    # Part IV — categories
    build_categories(doc, L)
    doc.add_page_break()

    # Part V + VI — open-source/self-hosted alts + commercial leaders
    build_oss_part(doc, L)
    build_commercial_part(doc, L)
    doc.add_page_break()

    # Part VII — decision maps
    build_decisions(doc, L)
    doc.add_page_break()

    # Part VIII — reference matrices
    build_ref_matrix(doc, L)

    build_appendix(doc, L)

    doc.save(OUT_PATH)
    return OUT_PATH


def main():
    en = build_guide(os.path.join(OUT, "software_tool_directory_2026_EN.docx"), "en")
    fr = build_guide(os.path.join(OUT, "software_tool_directory_2026_FR.docx"), "fr")
    print("EN:", en, os.path.getsize(en), "bytes")
    print("FR:", fr, os.path.getsize(fr), "bytes")


if __name__ == "__main__":
    main()
