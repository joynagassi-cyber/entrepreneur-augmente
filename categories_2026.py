# -*- coding: utf-8 -*-
"""
Normalized category architecture for the 2026 Software & AI Tool Directory.

Reconciled from:
  * OpenAlternative primary taxonomy (10 top-level categories + sub-categories)
  * Commercial-directory style categories (Capterra / G2 / GetApp)
  * AI/ML ecosystem categories (Hugging Face distinction: open weights vs open source)
  * Self-hosting / privacy categories (Awesome-Selfhosted, F-Droid)

Each category: {id, name_en, name_fr, parent, type, description_en, description_fr,
                objectives: [ids], tools: [tool ids], commercial_leaders, open_source_alts}
"""
import os, json

OUT = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUT, exist_ok=True)


def cat(cid, name_en, name_fr, parent, ctype, desc_en, desc_fr, objectives=None, tools=None):
    return {
        "id": cid,
        "name_en": name_en,
        "name_fr": name_fr,
        "parent": parent,
        "type": ctype,
        "description_en": desc_en,
        "description_fr": desc_fr,
        "objectives": objectives or [],
        "tools": tools or [],
    }


CATEGORIES = [
    # ---- Top-level: AI & ML ----
    cat("ai", "AI & Machine Learning", "IA & Apprentissage automatique", None, "ai",
        "Models, platforms and tooling for building, running and using artificial intelligence and machine-learning systems.",
        "Modèles, plateformes et outils pour construire, exécuter et utiliser des systèmes d'intelligence artificielle et d'apprentissage automatique.",
        objectives=["build-ai", "run-llm", "agent-automation", "prototype-fast"]),
    cat("ai-agents", "AI Agents & Assistants", "Agents & assistants IA", "ai", "ai",
        "Autonomous agents and assistants that plan, act and complete tasks on a user's behalf.",
        "Agents et assistants autonomes qui planifient, agissent et accomplissent des tâches pour le compte de l'utilisateur.",
        objectives=["agent-automation", "run-llm"]),
    cat("ai-coding", "AI Coding & Development", "Codage & développement assistés par IA", "ai", "ai",
        "AI coding agents, assistants and app builders for software development.",
        "Agents de codage IA, assistants et constructeurs d'applications pour le développement logiciel.",
        objectives=["build-ai", "build-app", "prototype-fast", "developer-control"]),
    cat("ai-models", "AI Models & Open Weights", "Modèles IA & poids ouverts", "ai", "ai",
        "Foundation models, open-weight models, and the frameworks used to run them. Distinguishes open source, open weights, and proprietary.",
        "Modèles de fondation, modèles à poids ouverts et frameworks utilisés pour les exécuter. Distingue open source, poids ouverts et propriétaire.",
        objectives=["run-llm", "build-ai"]),
    cat("ai-ml-infra", "ML Infrastructure & Serving", "Infrastructure ML & service de modèles", "ai", "ai",
        "Serving, orchestration, vector search and evaluation infrastructure for ML systems.",
        "Infrastructure de service, d'orchestration, de recherche vectorielle et d'évaluation pour les systèmes de ML.",
        objectives=["build-ai", "deploy-quickly"]),

    # ---- Top-level: Software Development ----
    cat("dev", "Software Development", "Développement logiciel", None, "dev",
        "IDEs, editors, frameworks, version control, CI/CD, testing and API tooling.",
        "IDE, éditeurs, frameworks, contrôle de version, CI/CD, tests et outils d'API.",
        objectives=["build-app", "developer-control", "build-saas"]),
    cat("dev-ide", "IDEs & Code Editors", "IDE & éditeurs de code", "dev", "dev",
        "Integrated development environments and code editors.",
        "Environnements de développement intégrés et éditeurs de code.",
        objectives=["developer-control"]),
    cat("dev-frameworks", "Frameworks & Platforms", "Frameworks & plateformes", "dev", "dev",
        "Web and application frameworks, no-code/low-code platforms and PaaS.",
        "Frameworks web et d'application, plateformes no-code/low-code et PaaS.",
        objectives=["build-app", "build-saas", "prototype-fast"]),
    cat("dev-backend", "Backend & Databases", "Backend & bases de données", "dev", "dev",
        "Databases, ORMs, APIs, backend services and infrastructure for applications.",
        "Bases de données, ORM, API, services backend et infrastructure applicative.",
        objectives=["build-app", "build-saas", "developer-control"]),
    cat("dev-devops", "DevOps & Deployment", "DevOps & déploiement", "dev", "dev",
        "CI/CD, containers, hosting, deployment and infrastructure as code.",
        "CI/CD, conteneurs, hébergement, déploiement et infrastructure as code.",
        objectives=["deploy-quickly", "self-host", "build-saas"]),
    cat("dev-test", "Testing & QA", "Tests & assurance qualité", "dev", "dev",
        "Testing frameworks, test automation and quality assurance tooling.",
        "Frameworks de test, automatisation des tests et outils d'assurance qualité.",
        objectives=["developer-control", "build-app"]),
    cat("dev-mobile", "Mobile Development", "Développement mobile", "dev", "dev",
        "Cross-platform and native mobile build tooling and workflows.",
        "Outils et workflows de construction mobile cross-platform et natifs.",
        objectives=["build-mobile", "test-on-device", "build-app"]),

    # ---- Top-level: Design & Creative ----
    cat("design", "Design & Creative", "Design & création", None, "creative",
        "UI/UX design, prototyping, graphics, image, video and audio tools.",
        "Design UI/UX, prototypage, graphisme, outils image, vidéo et audio.",
        objectives=["create-content", "prototype-fast"]),
    cat("design-uiux", "UI/UX & Prototyping", "UI/UX & prototypage", "design", "creative",
        "Interface design and interactive prototyping tools.",
        "Outils de conception d'interface et de prototypage interactif.",
        objectives=["prototype-fast", "create-content"]),
    cat("design-video", "Video & Audio", "Vidéo & audio", "design", "creative",
        "Video editing, screen recording, audio and media tools.",
        "Outils de montage vidéo, d'enregistrement d'écran, d'audio et de médias.",
        objectives=["create-content"]),
    cat("design-image", "Image Generation & Editing", "Génération & édition d'images", "design", "creative",
        "Raster/vector graphics and generative image tools.",
        "Outils graphiques raster/vectoriels et outils d'images génératives.",
        objectives=["create-content"]),

    # ---- Top-level: Productivity & Business ----
    cat("productivity", "Productivity & Utilities", "Productivité & utilitaires", None, "business",
        "Notes, tasks, documents, automation, personal and team productivity.",
        "Notes, tâches, documents, automatisation, productivité personnelle et d'équipe.",
        objectives=["organize", "automate", "prototype-fast"]),
    cat("prod-notes", "Note-taking & Knowledge", "Prise de notes & connaissance", "productivity", "business",
        "Note-taking apps, knowledge bases, wikis and PKM tools.",
        "Applications de prise de notes, bases de connaissances, wikis et outils PKM.",
        objectives=["organize"]),
    cat("prod-automation", "Automation", "Automatisation", "productivity", "business",
        "Workflow automation and no-code integration platforms.",
        "Automatisation de workflows et plateformes d'intégration no-code.",
        objectives=["automate", "prototype-fast"]),
    cat("prod-docs", "Docs & Collaboration", "Documents & collaboration", "productivity", "business",
        "Document editing, collaboration, whiteboards and communication.",
        "Édition de documents, collaboration, tableaux blancs et communication.",
        objectives=["organize", "collaborate"]),
    cat("prod-email", "Email & Communication", "E-mail & communication", "productivity", "business",
        "Email clients, team chat and messaging platforms.",
        "Clients e-mail, messagerie d'équipe et plateformes de messagerie.",
        objectives=["collaborate"]),

    cat("business", "Business Software", "Logiciels d'entreprise", None, "business",
        "CRM, ERP, finance, HR, project management, marketing and enterprise software.",
        "CRM, ERP, finance, RH, gestion de projet, marketing et logiciels d'entreprise.",
        objectives=["run-business", "collaborate"]),
    cat("biz-crm", "CRM & Sales", "CRM & vente", "business", "business",
        "Customer relationship management and sales tooling.",
        "Gestion de la relation client et outils de vente.",
        objectives=["run-business", "collaborate"]),
    cat("biz-pm", "Project & Task Management", "Gestion de projet & tâches", "business", "business",
        "Project management, task tracking and team planning.",
        "Gestion de projet, suivi des tâches et planification d'équipe.",
        objectives=["run-business", "organize", "collaborate"]),
    cat("biz-finance", "Finance & Accounting", "Finance & comptabilité", "business", "business",
        "Accounting, invoicing, payroll and financial management.",
        "Comptabilité, facturation, paie et gestion financière.",
        objectives=["run-business"]),
    cat("biz-marketing", "Marketing & Engagement", "Marketing & engagement", "business", "business",
        "Marketing automation, email marketing, SEO and social management.",
        "Automatisation marketing, e-mailing, SEO et gestion des réseaux sociaux.",
        objectives=["run-business", "marketing"]),

    # ---- Top-level: Data & Analytics ----
    cat("data", "Data & Analytics", "Données & analytique", None, "dev",
        "Analytics, BI, data engineering, warehousing and web scraping.",
        "Analytique, BI, ingénierie des données, entreposage et scraping web.",
        objectives=["analyze-data", "build-app"]),
    cat("data-bi", "BI & Analytics", "BI & analytique", "data", "dev",
        "Business intelligence, dashboards and product analytics.",
        "Business intelligence, tableaux de bord et analytique produit.",
        objectives=["analyze-data"]),
    cat("data-etl", "Data Engineering & Warehousing", "Ingénierie & entreposage de données", "data", "dev",
        "ETL, ingestion, warehousing and streaming data platforms.",
        "ETL, ingestion, entreposage et plateformes de données en streaming.",
        objectives=["analyze-data", "build-app"]),
    cat("data-scraping", "Web Scraping & Crawlers", "Scraping web & robots d'indexation", "data", "dev",
        "Web scraping libraries, platforms and SDKs.",
        "Bibliothèques, plateformes et SDK de scraping web.",
        objectives=["analyze-data", "build-app"]),

    # ---- Top-level: Infrastructure & Ops ----
    cat("infra", "Infrastructure & Operations", "Infrastructure & opérations", None, "dev",
        "Databases, networking, orchestration, observability, storage and security.",
        "Bases de données, réseau, orchestration, observabilité, stockage et sécurité.",
        objectives=["self-host", "deploy-quickly", "run-business"]),
    cat("infra-monitoring", "Monitoring & Observability", "Supervision & observabilité", "infra", "dev",
        "Monitoring, logging, tracing and alerting.",
        "Supervision, journalisation, traçage et alertes.",
        objectives=["self-host", "run-business"]),
    cat("infra-storage", "Databases & Storage", "Bases de données & stockage", "infra", "dev",
        "Relational, NoSQL, vector and object-storage systems.",
        "Systèmes relationnels, NoSQL, vectoriels et stockage objet.",
        objectives=["self-host", "build-app", "build-saas"]),
    cat("infra-security", "Cybersecurity & Privacy", "Cybersécurité & confidentialité", "infra", "dev",
        "Identity, secrets, network security, privacy and encryption tools.",
        "Identité, secrets, sécurité réseau, confidentialité et chiffrement.",
        objectives=["self-host", "secure"]),

    # ---- Top-level: Privacy & Self-hosting ----
    cat("selfhost", "Open Source & Self-hosted", "Open source & auto-hébergement", None, "open",
        "Open-source, self-hosted and privacy-first software and platforms.",
        "Logiciels open source, auto-hébergés et axés sur la confidentialité.",
        objectives=["self-host", "open-source", "avoid-setup", "secure"]),
    cat("selfhost-mobile", "Open-source Mobile Apps", "Applications mobiles open source", "selfhost", "open",
        "Open-source Android/iOS applications, including the F-Droid ecosystem.",
        "Applications Android/iOS open source, y compris l'écosystème F-Droid.",
        objectives=["open-source", "build-mobile", "secure"]),

    # ---- Extra categories referenced by the canonical seed (added so every tool
    #      category has a defined, bilingual node for navigation) ----
    cat("ai-machine-learning", "AI/ML Foundations", "Fondamentaux IA/ML", "ai", "ai",
        "Core machine-learning libraries, training tooling and model runtimes that underpin AI applications.",
        "Bibliothèques d'apprentissage automatique, outils d'entraînement et runtimes de modèles qui sous-tendent les applications d'IA.",
        objectives=["build-ai", "run-llm"]),
    cat("business-software", "Business Application Software", "Logiciels d'application métier", "business", "business",
        "General-purpose business software for operations, managing teams and running a company.",
        "Logiciels d'entreprise à usage général pour les opérations, la gestion d'équipe et la direction d'une société.",
        objectives=["run-business", "collaborate"]),
    cat("community-social", "Community & Social", "Communauté & social", "business", "business",
        "Community platforms, forums, social media management and audience engagement.",
        "Plateformes communautaires, forums, gestion des réseaux sociaux et engagement de l'audience.",
        objectives=["collaborate", "marketing"]),
    cat("content-publishing", "Content & Publishing", "Contenu & publication", "productivity", "business",
        "Publishing tools for documents, blogs, newsletters, and public-facing content.",
        "Outils de publication pour documents, blogs, newsletters et contenus publics.",
        objectives=["organize", "create-content", "marketing"]),
    cat("data-analytics", "Analytics & Reporting", "Analytique & reporting", "data", "dev",
        "Analytics engines, reporting and insight tooling used to understand data.",
        "Moteurs d'analyse, reporting et outils de compréhension des données.",
        objectives=["analyze-data"]),
    cat("developer-tools", "Developer Tooling", "Outils développeur", "dev", "dev",
        "CLIs, SDKs, debugging, profiling and general developer utility tools.",
        "CLI, SDK, débogage, profilage et outils utilitaires pour développeurs.",
        objectives=["developer-control", "build-app"]),
    cat("identity", "Identity & Access", "Identité & accès", "infra", "dev",
        "Authentication, authorization, SSO, passwordless and identity management systems.",
        "Systèmes d'authentification, d'autorisation, de SSO, sans mot de passe et de gestion d'identité.",
        objectives=["self-host", "secure"]),
    cat("infrastructure-operations", "Infra Operations", "Opérations d'infrastructure", "infra", "dev",
        "Day-2 operations for infrastructure: orchestration, provisioning, secrets and services.",
        "Opérations de jour 2 pour l'infrastructure : orchestration, provisionnement, secrets et services.",
        objectives=["self-host", "deploy-quickly", "run-business"]),
    cat("misc", "Miscellaneous & Uncategorized", "Divers & non catégorisé", None, "misc",
        "Tools that have not yet been assigned to a primary category.",
        "Outils non encore rattachés à une catégorie principale.",
        objectives=[]),
    cat("open-source", "Open Source", "Open source", "selfhost", "open",
        "Cross-cutting open-source software, independent of application type.",
        "Logiciels open source transversaux, indépendamment du type d'application.",
        objectives=["open-source", "self-host"]),
    cat("privacy", "Privacy-First", "Confidentialité d'abord", "selfhost", "open",
        "Privacy-first tools that minimize data collection and are designed to protect personal data.",
        "Outils axés sur la confidentialité qui minimisent la collecte de données et protègent les données personnelles.",
        objectives=["secure", "self-host", "open-source"]),
    cat("productivity-utilities", "Productivity Utilities", "Utilitaires de productivité", "productivity", "business",
        "General-purpose utilities and companion software that boost personal productivity.",
        "Utilitaires à usage général et logiciels compagnons qui renforcent la productivité personnelle.",
        objectives=["organize", "automate"]),
    cat("security", "Security & Compliance", "Sécurité & conformité", "infra", "dev",
        "Security tooling, secrets management, vulnerability scanning and compliance.",
        "Outils de sécurité, gestion des secrets, analyse des vulnérabilités et conformité.",
        objectives=["secure", "self-host"]),
    cat("security-privacy", "Security & Privacy", "Sécurité & confidentialité", "infra", "dev",
        "Tools combining security hardening and privacy protection.",
        "Outils combinant durcissement de la sécurité et protection de la confidentialité.",
        objectives=["secure", "self-host"]),
    cat("session", "Session & Runtime", "Session & runtime", "infra", "dev",
        "Session management, runtime and middleware tooling for applications.",
        "Gestion de session, runtime et outils intermédiaires pour applications.",
        objectives=["build-app", "self-host"]),
]


def build():
    data = {"version": "2026.0", "generated": __import__("datetime").date.today().isoformat(),
            "categories": CATEGORIES}
    with open(os.path.join(OUT, "categories_2026.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("categories:", len(CATEGORIES))
    return CATEGORIES


if __name__ == "__main__":
    build()
