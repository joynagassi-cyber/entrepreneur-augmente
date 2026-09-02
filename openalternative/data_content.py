# -*- coding: utf-8 -*-
"""
Content extracted from https://openalternative.co/categories and its sub-pages
via the platform fetch tool (direct sandbox egress to the site is blocked).

This module holds a faithful, structured snapshot of:
  * the categories landing page (tree, trending, popular),
  * the complete category index (all /categories/* URLs from sitemap),
  * the 10 top-level category pages (description, sub-categories, notable tools).
"""

SITE = "https://openalternative.co"
CATEGORIES_URL = "https://openalternative.co/categories"
PAGE_TITLE = "Open Source Software Categories"
TAGLINE = "Browse top categories to find your best Open Source software options."
BASELINE_DESC = (
    "OpenAlternative is a curated directory of the best open-source alternatives to "
    "popular proprietary software. Below is the complete categories system, captured "
    "from the live site and rendered as a single consolidated PDF."
)

# ---------------------------------------------------------------------------
# 1. Top-level category pages + notable tools (curated from each page's listing)
# ---------------------------------------------------------------------------
CATEGORY_PAGES = [
    {
        "slug": "ai-machine-learning",
        "name": "AI & Machine Learning",
        "title": "Open Source AI & Machine Learning Tools",
        "description": (
            "A curated collection of the best open source software for building and "
            "running AI: model serving and training infrastructure, agent and app "
            "frameworks, chat interfaces, and AI security tooling."
        ),
        "subs": [
            ("AI Development Platforms", "ai-development-platforms"),
            ("Machine Learning Infrastructure", "machine-learning-infrastructure"),
            ("AI Interaction & Interfaces", "ai-interaction-interfaces"),
            ("AI Security & Privacy", "ai-security-privacy"),
        ],
        "tools": [
            ("Parlant", "", "Structured control layer for customer-facing AI agents", "18,273", "Apache-2.0",
             "A conversational AI server that manages agent behavior through context-aware guidelines, keeping responses consistent, auditable, and aligned at scale.", "Voiceflow"),
            ("OpenClaw", "AI", "An AI assistant that acts, not just answers", "388,648", "MIT",
             "A personal AI assistant that connects to your existing chat apps and handles real tasks like email, calendar, and flight check-ins on your behalf.", "Grok Bot"),
            ("Hermes Agent", "AI", "Desktop AI agent with persistent memory across platforms", "240,035", "MIT",
             "Cross-platform desktop agent from Nous Research that connects to Telegram, Discord, Slack, WhatsApp, and more, with persistent memory, scheduling, and isolated sandboxing.", "Grok Bot"),
            ("Ollama", "AI", "Run open-source LLMs locally on your own machine", "179,989", "MIT",
             "Runs open-source language models locally with a simple setup, plus optional cloud access for larger models when local hardware isn't enough.", "LM Studio"),
            ("Open WebUI", "AI", "One interface for every AI model you run or connect", "150,729", "BSD-3-Clause",
             "Self-hosted AI platform that connects local and cloud models, extends with Python, and keeps your data under your control.", "Claude"),
            ("Dify", "AI", "Build and deploy AI agents and RAG pipelines visually", "154,246", "Unknown",
             "Visual platform for building agentic workflows, RAG pipelines, and MCP servers with a drag-and-drop builder.", "Voiceflow"),
            ("Macro Mail", "", "Keyboard-first email client with AI, chat, and tasks", "4,175", "AGPL-3.0",
             "An AI-powered email client that combines inbox management, chat, tasks, and AI agents in one shared workspace, built for keyboard-driven workflows.", "Gmail"),
            ("Proton Lumo", "AI", "Private AI chat with zero-access encryption", "5,571", "GPL-3.0",
             "AI chat assistant from Proton that stores conversations with zero-access encryption, never logs chats, and never uses your data to train models.", "Claude"),
        ],
    },
    {
        "slug": "business-software",
        "name": "Business Software",
        "title": "Open Source Business Software",
        "description": (
            "A curated collection of the best open source software that runs a business "
            "day to day, covering CRM and sales, finance and accounting, HR, legal, "
            "project management, e-commerce, and customer support."
        ),
        "subs": [
            ("CRM & Sales", "crm-sales"), ("ERP & Operations", "erp-operations"),
            ("Finance & Accounting", "finance-accounting"), ("Human Resources (HR)", "human-resources-hr"),
            ("Marketing & Customer Engagement", "marketing-customer-engagement"),
            ("Customer Support & Success", "customer-support-success"),
            ("E-commerce Platforms", "e-commerce-platforms"),
            ("Project & Work Management", "project-work-management"),
            ("Collaboration & Communication", "collaboration-communication"),
            ("Scheduling & Event Management", "scheduling-event-management"),
            ("Document Management & E-Signatures", "document-management-e-signatures"),
            ("Forms & Surveys", "forms-surveys"),
            ("Compliance & Risk Management", "compliance-risk-management"),
            ("Legal", "legal"), ("Education", "education"),
        ],
        "tools": [
            ("Novu", "", "Multi-channel notification infrastructure for apps", "39,713", "Unknown",
             "Open-source platform for building in-app, email, push, SMS, and chat notifications with a unified API, workflow engine, and embeddable inbox component.", "Customer.io"),
            ("Postiz", "", "Schedule, analyze, and manage 30+ social media accounts", "35,394", "AGPL-3.0",
             "Self-hostable social media scheduler that lets you plan, generate, and publish content across 30+ networks with AI assistance, team collaboration, and automation integrations.", "Buffer"),
            ("Dub Partners", "", "Affiliate marketing platform built for SaaS companies", "24,655", "AGPL-3.0",
             "Run affiliate, influencer, and referral programs with flexible reward structures, real-time attribution, and automated global payouts.", "Affonso"),
            ("OpenSEO", "", "Self-hosted SEO platform for keyword, backlink, and rank tracking", "16,362", "MIT",
             "Manage keyword research, backlink analysis, competitor monitoring, and rank tracking without expensive SaaS subscriptions.", "Semrush"),
            ("CRM", "", "An agentic CRM that keeps records current automatically", "9,293", "MIT",
             "Open source CRM with AI agents that read your inbox, enrich contacts and companies, schedule follow-ups, and build new agents from plain-language descriptions.", "Attio"),
            ("Baserow", "", "No-code database and app builder you can self-host", "5,768", "MIT",
             "Open-source platform for building databases, internal apps, and automated workflows without writing code. Available on cloud or self-hosted.", "Airtable"),
        ],
    },
    {
        "slug": "developer-tools",
        "name": "Developer Tools",
        "title": "Open Source Developer Tools",
        "description": (
            "A curated collection of the best open source software for building software: "
            "IDEs and editors, frameworks, API tooling, testing, version control, build "
            "and deployment pipelines, and AI coding assistants."
        ),
        "subs": [
            ("Website Builders", "website-builders"), ("IDEs & Code Editors", "ides-code-editors"),
            ("Frameworks & Platforms", "frameworks-platforms"),
            ("API Development & Testing", "api-development-testing"),
            ("Testing & Quality Assurance", "testing-quality-assurance"),
            ("Version Control & Collaboration", "version-control-collaboration"),
            ("Code Analysis & Transformation", "code-analysis-transformation"),
            ("Build & Deployment", "build-deployment"),
            ("Integration Platforms", "integration-platforms"),
            ("AI Assisted Coding", "ai-assisted-coding"), ("Terminals", "terminals"),
        ],
        "tools": [
            ("OpenCode", "AI", "AI coding agent for terminal, IDE, and desktop", "203,253", "MIT",
             "Open source AI coding agent that works in your terminal, IDE, or desktop app, supporting 75+ LLM providers with no code storage.", "Claude Code"),
            ("n8n", "", "Visual workflow automation with code flexibility and AI agents", "203,159", "Unknown",
             "Build automated workflows connecting 500+ apps, write custom code, and deploy AI agents with full visibility into every decision. Self-hostable or cloud.", "Make"),
            ("Langflow", "AI", "Visual builder for AI agents and RAG pipelines", "154,113", "MIT",
             "Build, deploy, and iterate on AI agents, RAG applications, and MCP servers using a drag-and-drop visual interface backed by Python.", "Voiceflow"),
            ("Supabase", "", "Postgres-powered backend platform for production apps", "108,744", "Apache-2.0",
             "Provides a full backend stack built on Postgres: authentication, auto-generated APIs, edge functions, realtime subscriptions, file storage, and vector search.", "Firebase"),
            ("pi", "AI", "Minimal terminal coding agent you can fully customize", "100,964", "MIT",
             "Terminal-based coding agent with a minimal core, 15+ LLM providers, tree-structured session history, and a TypeScript extension system.", "Claude Code"),
            ("Paperclip", "AI", "Org chart, budgets, and governance for AI agent teams", "79,879", "MIT",
             "Manages teams of AI agents across business functions with org charts, goal alignment, cost tracking, ticket tracing, and board-level governance controls.", "Lindy"),
            ("Baserow", "", "No-code database and app builder you can self-host", "5,768", "MIT",
             "Open-source platform for building databases, internal apps, and automated workflows without writing code. Available on cloud or self-hosted.", "Airtable"),
        ],
    },
    {
        "slug": "productivity-utilities",
        "name": "Productivity & Utilities",
        "title": "Open Source Productivity & Utilities",
        "description": (
            "A curated collection of the best open source everyday desktop and mobile "
            "utilities for notes, tasks, files, email, passwords, automation, screen "
            "capture, and keeping a machine tidy and fast."
        ),
        "subs": [
            ("Office Suites", "office-suites"),
            ("Note Taking & Knowledge Management", "note-taking-knowledge-management"),
            ("Password & Secret Management", "password-secret-management"),
            ("Screen Capture & Recording", "screen-capture-recording"),
            ("File Management & Sync", "file-management-sync"),
            ("Email & Communication", "email-communication"),
            ("Browsers & Extensions", "browsers-extensions"),
            ("Automation", "automation"), ("Time & Task Management", "time-task-management"),
            ("Personal Finance Management", "personal-finance-management"),
            ("Design & Visualization", "design-visualization"),
            ("Bookmark & Content Management", "bookmark-content-management"),
            ("Remote Desktop & Access", "remote-desktop-access"),
            ("System Cleanup & Optimization", "system-cleanup"),
            ("Maps & Navigation", "maps-navigation"), ("Input & Dictation", "input-dictation"),
        ],
        "tools": [
            ("Cap", "", "Open source screen recorder with editing and instant sharing", "21,473", "AGPL-3.0",
             "Record your screen or webcam, edit with backgrounds and effects, then share via link. Built on Rust and Tauri for native performance on macOS and Windows.", "Screen Studio"),
            ("Parlant", "AI", "Structured control layer for customer-facing AI agents", "18,273", "Apache-2.0",
             "A conversational AI server that manages agent behavior through context-aware guidelines, keeping responses consistent, auditable, and aligned at scale.", "Voiceflow"),
            ("VoiceInk", "AI", "Local voice dictation with AI enhancement for macOS", "6,256", "GPL-3.0",
             "Privacy-first dictation app for Apple Silicon Macs that transcribes speech locally, cleans up output with AI, and auto-switches settings per app.", "Wispr Flow"),
            ("Macro Mail", "", "Keyboard-first email client with AI, chat, and tasks", "4,175", "AGPL-3.0",
             "An AI-powered email client that combines inbox management, chat, tasks, and AI agents in one shared workspace, built for keyboard-driven workflows.", "Gmail"),
            ("Macro Docs", "", "Markdown docs wired into tasks, email, and agents", "4,175", "AGPL-3.0",
             "Collaborative markdown documents with real-time CRDT editing, AI agent cursors, mention linking, and built-in properties tied to your tasks, channels, and email.", "Notion"),
            ("Novu", "", "Multi-channel notification infrastructure for apps", "39,713", "Unknown",
             "Open-source platform for building in-app, email, push, SMS, and chat notifications with a unified API, workflow engine, and embeddable inbox component.", "Customer.io"),
        ],
    },
    {
        "slug": "infrastructure-operations",
        "name": "Infrastructure & Operations",
        "title": "Open Source Infrastructure & Operations Tools",
        "description": (
            "A curated collection of the best open source software for running servers "
            "and services: databases, storage, networking, orchestration, messaging, "
            "monitoring, and backup and recovery."
        ),
        "subs": [
            ("Search Engines", "search-engines"),
            ("Cloud Infrastructure Management", "cloud-infrastructure-management"),
            ("Server & VM Management", "server-vm-management"),
            ("Monitoring & Observability", "monitoring-observability"),
            ("Databases", "databases"), ("Networking & Connectivity", "networking-connectivity"),
            ("Orchestration & Scheduling", "orchestration-scheduling"),
            ("Messaging & Event Streaming", "messaging-event-streaming"),
            ("Storage Solutions", "storage-solutions"), ("Backup & Recovery", "backup-recovery"),
        ],
        "tools": [
            ("Immich", "", "Self-hosted photo and video backup for your own server", "113,277", "AGPL-3.0",
             "Back up, organize, search, and browse your personal photo and video library on your own server, with no third-party cloud access.", "Google Photos"),
            ("Uptime Kuma", "", "Self-hosted uptime monitoring with a clean dashboard", "90,886", "MIT",
             "Monitors websites, APIs, and services with real-time alerts, a status page, and support for dozens of notification channels. Self-hosted and Docker-friendly.", "Opsgenie"),
            ("NetData", "", "Real-time monitoring for systems and applications", "80,407", "GPL-3.0",
             "Powerful, efficient, and user-friendly monitoring solution for servers, containers, and applications with instant insights and alerts.", "DataDog"),
            ("Elasticsearch", "", "The leading distributed search and analytics engine", "77,892", "Unknown",
             "Elasticsearch is an open-source, RESTful search engine designed for scalability, reliability, and easy management.", "Algolia"),
            ("Grafana", "", "Unified observability for metrics, logs, traces, and more", "76,565", "AGPL-3.0",
             "Grafana unifies metrics, logs, traces, profiles, and business data into one OpenTelemetry-native platform with AI-assisted root cause analysis and adaptive cost controls.", "Power BI"),
            ("Coolify", "", "Deploy apps, databases, and services to your own server", "61,315", "Apache-2.0",
             "Self-hostable deployment platform that lets you deploy apps, databases, and 280+ one-click services to any server via SSH, with Git integration and automatic SSL.", "Vercel"),
        ],
    },
    {
        "slug": "community-social",
        "name": "Community & Social",
        "title": "Open Source Community & Social Tools",
        "description": (
            "A curated collection of the best open source platforms and tools for "
            "building and managing online communities and social interactions."
        ),
        "subs": [
            ("Social Networking", "social-networking"),
            ("Community Building Platforms", "community-building-platforms"),
            ("Collaboration & Feedback", "collaboration-feedback"),
        ],
        "tools": [
            ("Mastodon", "", "Decentralized social networking in your control", "50,262", "AGPL-3.0",
             "A free, open-source social media platform that puts users in charge of their data and connections.", "X (Twitter)"),
            ("Discourse", "", "Cultivate vibrant online communities with ease", "47,781", "GPL-2.0",
             "A powerful, customizable platform for building and managing online forums, fostering engaging discussions and collaborative spaces.", "Skool"),
            ("Hey", "", "Decentralized social networking for the Web3 era", "29,379", "GPL-3.0",
             "A blockchain-powered social platform offering censorship-resistant content sharing, user-owned data, and innovative monetization options.", "X (Twitter)"),
            ("Bluesky", "", "Social media reimagined for community and connection", "18,261", "MIT",
             "A decentralized social network focused on fostering meaningful interactions and giving users control over their data and experience.", "X (Twitter)"),
            ("Flarum", "", "Modern forum software for vibrant online communities", "16,389", "MIT",
             "Lightweight, extensible forum platform with a sleek interface, powerful moderation tools, and seamless integration capabilities.", "Skool"),
            ("Apache Answer", "", "Open-source Q&A platform for knowledge sharing", "15,664", "Apache-2.0",
             "A versatile, community-driven Q&A platform that fosters collaboration and knowledge exchange within organizations and communities.", "Skool"),
            ("PeerTube", "", "Decentralized video platform for true digital freedom", "15,296", "AGPL-3.0",
             "Create your own video hosting platform - a free, open-source alternative to YouTube, without ads or tracking.", "YouTube"),
            ("Lemmy", "", "Build your own federated discussion community", "14,579", "AGPL-3.0",
             "Open-source forum and link aggregator that connects communities across the fediverse. Self-hosted, ad-free, with powerful moderation tools and federation.", "Reddit"),
        ],
    },
    {
        "slug": "content-publishing",
        "name": "Content & Publishing",
        "title": "Open Source Content & Publishing Tools",
        "description": (
            "A curated collection of the best open source software for writing and "
            "publishing: content management systems, blogs, documentation and knowledge "
            "bases, digital asset management, and course platforms."
        ),
        "subs": [
            ("Content Management Systems (CMS)", "content-management-systems-cms"),
            ("Blogging & Personal Sites", "blogging-personal-sites"),
            ("Community Platforms", "community-platforms"),
            ("Documentation & Knowledge Base", "documentation-knowledge-base"),
            ("Learning Management Systems (LMS)", "learning-management-systems-lms"),
            ("Digital Asset Management (DAM)", "digital-asset-management-dam"),
            ("Publishing", "publishing"),
        ],
        "tools": [
            ("Strapi", "", "Headless CMS with REST and GraphQL APIs out of the box", "73,061", "MIT",
             "TypeScript headless CMS that generates REST and GraphQL APIs from your content model, with a no-code builder, plugin system, and full self-hosting support.", "Sanity"),
            ("Ghost", "", "Publishing platform for blogs, newsletters, and paid memberships", "55,101", "MIT",
             "Publish content, send email newsletters, and sell paid subscriptions from one platform. Used by independent journalists, creators, and businesses like YCombinator and Kickstarter.", "WordPress"),
            ("Discourse", "", "Cultivate vibrant online communities with ease", "47,781", "GPL-2.0",
             "A powerful, customizable platform for building and managing online forums, fostering engaging discussions and collaborative spaces.", "Skool"),
            ("Payload", "", "Headless CMS for developers, built with Node.js", "44,547", "MIT",
             "A powerful, flexible, and developer-friendly content management system that prioritizes customization and scalability.", "WordPress"),
            ("Outline", "", "Fast, collaborative wiki for teams who need organized docs", "40,424", "BUSL-1.1",
             "Team knowledge base with real-time collaboration, AI-powered search, Slack integration, and self-hosting support for internal docs and wikis.", "Notion"),
            ("Immich", "", "Self-hosted photo and video backup for your own server", "113,277", "AGPL-3.0",
             "Back up, organize, search, and browse your personal photo and video library on your own server, with no third-party cloud access.", "Google Photos"),
            ("Tolgee", "", "Open-source localization platform for multilingual apps", "4,088", "Apache-2.0",
             "Manage app translations with in-context editing, AI translation, and collaborative tools. Self-hostable and free to start.", "Crowdin"),
        ],
    },
    {
        "slug": "data-analytics",
        "name": "Data & Analytics",
        "title": "Open Source Data & Analytics Tools",
        "description": (
            "A curated collection of the best open source software for collecting, moving, "
            "and making sense of data, from web scraping and pipelines to warehousing, "
            "business intelligence, and product analytics."
        ),
        "subs": [
            ("Web & Product Analytics", "analytics"),
            ("Business Intelligence & Reporting", "business-intelligence-reporting"),
            ("Data Engineering & Integration", "data-engineering-integration"),
            ("Data Warehousing & Processing", "data-warehousing-processing"),
            ("Data Extraction & Web Scraping", "data-extraction-web-scraping"),
        ],
        "tools": [
            ("Firecrawl", "AI", "Turn any website into clean, AI-ready data via API", "175,683", "AGPL-3.0",
             "API for AI agents to search, scrape, crawl, and interact with the live web, returning clean Markdown, structured JSON, or screenshots from any page.", "Jina AI"),
            ("Mermaid", "", "Text-based diagramming that renders in code and docs", "90,045", "MIT",
             "Create flowcharts, sequence diagrams, Gantt charts, and more using a simple Markdown-like syntax that renders anywhere.", "Microsoft Visio"),
            ("Crawl4AI", "AI", "LLM-ready web crawler built for AI data pipelines", "81,114", "Apache-2.0",
             "Open-source web crawler and scraper that produces clean, structured output optimized for LLMs, RAG pipelines, and AI agents.", "Jina AI"),
            ("Grafana", "", "Unified observability for metrics, logs, traces, and more", "76,565", "AGPL-3.0",
             "Grafana unifies metrics, logs, traces, profiles, and business data into one OpenTelemetry-native platform with AI-assisted root cause analysis.", "Power BI"),
            ("Apache Superset", "", "Self-serve data exploration and dashboard builder", "74,588", "Apache-2.0",
             "Connect any SQL database, build charts with drag-and-drop or raw SQL, and publish interactive dashboards without writing application code.", "Power BI"),
            ("OpenBB", "AI", "AI-powered analytics workspace built for investment teams", "72,617", "AGPL-3.0",
             "Connects proprietary, licensed, and public financial data with AI agents in a self-hostable workspace for asset managers, hedge funds, and banks.", "Power BI"),
            ("OpenPanel", "", "Cookie-free web and product analytics, self-hostable", "6,845", "AGPL-3.0",
             "Open-source analytics platform covering web traffic, custom events, funnels, retention, session replay, and revenue tracking.", "Google Analytics"),
        ],
    },
    {
        "slug": "misc",
        "name": "Miscellaneous",
        "title": "Open Source Miscellaneous Tools",
        "description": (
            "A curated collection of the best open source software that does not fit the "
            "other categories, including gaming, design, media and streaming, crypto, IoT, "
            "health, fintech, and logistics tools."
        ),
        "subs": [
            ("Cryptocurrency & Blockchain", "cryptocurrency-blockchain"),
            ("Gaming", "gaming"), ("Internet of Things (IoT)", "internet-of-things-iot"),
            ("Logistics & Supply Chain", "logistics-supply-chain"),
            ("Design & Prototyping", "design-prototyping"),
            ("Media & Streaming", "media-and-streaming"),
            ("Photo & Video Editors", "photo-video-editors"),
            ("Finance & Fintech", "finance-fintech"),
        ],
        "tools": [
            ("Godot", "", "Free 2D and 3D game engine for cross-platform projects", "116,537", "MIT",
             "Build 2D, 3D, and XR games with a full-featured engine that includes its own scripting language, scene editor, and export tools for multiple platforms.", "Unity"),
            ("Home Assistant", "", "Local control smart home automation with privacy first", "90,225", "Apache-2.0",
             "Open source home automation platform supporting 1000+ devices with local control, powerful automations, custom dashboards, and voice assistant. No cloud required.", "Google Assistant"),
            ("OpenCut", "", "Open source video editor that runs in your browser", "88,483", "MIT",
             "Browser-based, open source video editor built for privacy. No installs, no account required, works on any platform.", "CapCut"),
            ("OpenBB", "AI", "AI-powered analytics workspace built for investment teams", "72,617", "AGPL-3.0",
             "Connects proprietary, licensed, and public financial data with AI agents in a self-hostable workspace for asset managers, hedge funds, and banks.", "Power BI"),
            ("Penpot", "", "Open-source UI design and prototyping for product teams", "59,506", "MPL-2.0",
             "Design, prototype, and hand off to developers in one platform. Supports design systems, tokens, flexible layouts, and AI workflows with real CSS/HTML output.", "Canva"),
            ("Jellyfin", "", "Self-hosted media server for movies, music, and more", "56,471", "GPL-2.0",
             "Free, open source media server that lets you collect, manage, and stream your personal library to any device, with no fees, tracking, or vendor lock-in.", "Netflix"),
            ("Hyperswitch", "", "Open source payment orchestrator for global transactions", "43,568", "Apache-2.0",
             "A unified payment infrastructure that connects multiple payment processors through a single API integration, enabling global payment processing.", "Stripe Billing"),
        ],
    },
    {
        "slug": "security-privacy",
        "name": "Security & Privacy",
        "title": "Open Source Security & Privacy Tools",
        "description": (
            "A curated collection of the best open source software for protecting systems "
            "and data, spanning application and network security, identity and access "
            "management, secrets, and threat detection."
        ),
        "subs": [
            ("Identity & Access Management (IAM)", "identity-access-management-iam"),
            ("Secrets Management", "secrets-management"),
            ("Threat Detection & Response", "threat-detection-response"),
            ("Network Security", "network-security"),
            ("Data Security & Privacy", "data-security-privacy"),
            ("Application Security", "application-security"),
            ("Fraud Prevention", "fraud-prevention"),
        ],
        "tools": [
            ("Zen Browser", "", "Privacy-focused browser with powerful customization", "44,216", "MPL-2.0",
             "A Firefox-based browser offering enhanced privacy, split views, and extensive customization options for a personalized browsing experience.", "Firefox"),
            ("Puter", "", "A full desktop environment that runs in your browser", "43,335", "AGPL-3.0",
             "Puter is a cloud-based desktop OS you run in the browser, with built-in apps, file storage, and support for hosting web apps and sites.", "Google Drive"),
            ("Mattermost", "", "Secure collaboration platform for mission-critical work", "38,974", "Unknown",
             "Mattermost provides a flexible, open-source platform for secure team collaboration, designed for organizations with strict security and privacy requirements.", "Slack"),
            ("Keycloak", "", "Secure authentication and access control made simple", "36,563", "Apache-2.0",
             "Comprehensive open source identity management solution offering single sign-on, social login, and fine-grained authorization for applications and services.", "Auth0"),
            ("Tailscale", "", "Zero-config VPN with WireGuard for secure networking", "36,030", "BSD-3-Clause",
             "Deploy a modern WireGuard-based VPN with zero configuration. Connect devices securely across clouds, VPCs, and on-premises networks without firewall rules.", "Zerotier"),
            ("Better Auth", "", "Framework-agnostic authentication for TypeScript applications", "29,803", "MIT",
             "A comprehensive authentication framework offering email/password, social sign-on, two-factor auth, and multi-tenant support with full TypeScript integration.", "Auth0"),
            ("Hanko", "", "Passkeys, SSO, and MFA without vendor lock-in", "9,019", "Unknown",
             "Open source authentication platform supporting passkeys, 2FA, SSO, and social login. Self-host or use Hanko Cloud, with full control over your data.", "Auth0"),
        ],
    },
]

# ---------------------------------------------------------------------------
# 2. Trending categories (from the landing page)
# ---------------------------------------------------------------------------
TRENDING_CATEGORIES = [
    ("AI Coding Agent Orchestrators", "developer-tools/ai-assisted-coding/ai-coding-agent-orchestrators",
     "Tools that run and coordinate multiple AI coding agents in parallel across isolated git worktrees, also known as agent harnesses or agentic dev environments.", "8", "+9.8%"),
    ("Voice Dictation Tools", "productivity-utilities/input-dictation/voice-dictation",
     "Applications that convert spoken words into text for faster writing across any application.", "7", "+8.6%"),
    ("ERP Systems", "business-software/erp-operations/erp-systems",
     "Enterprise Resource Planning systems integrating various business functions.", "4", "+6.9%"),
    ("Scraping Platforms & SDKs", "data-analytics/data-extraction-web-scraping/scraping-platforms-sdks",
     "Platforms and SDKs for building web scraping solutions.", "5", "+6.8%"),
    ("CRM Systems", "business-software/crm-sales/crm-systems",
     "Customer relationship management systems for tracking contacts, deals, and pipelines, with activity history and sales reporting.", "13", "+5.5%"),
    ("Subscription & Billing Management Tools", "business-software/finance-accounting/subscription-billing-management",
     "Platforms for managing recurring subscriptions and complex billing models.", "8", "+5.3%"),
]

# ---------------------------------------------------------------------------
# 3. Popular lists from the landing page
# ---------------------------------------------------------------------------
POPULAR_PROPRIETARY = [
    ("Claude Code", "alternatives/claude-code", "14"),
    ("Spotify", "alternatives/spotify", "2"),
    ("Notion", "alternatives/notion", "20"),
    ("Lovable", "alternatives/lovable", "3"),
    ("Wispr Flow", "alternatives/wisprflow", "7"),
    ("CapCut", "alternatives/capcut", "5"),
    ("Discord", "alternatives/discord", "11"),
    ("n8n", "alternatives/n8n", "5"),
    ("Cursor", "alternatives/cursor", "9"),
    ("Codex", "alternatives/codex", "18"),
    ("Adobe Photoshop", "alternatives/photoshop", "3"),
    ("Microsoft Word", "alternatives/microsoft-word", "5"),
]

POPULAR_CATEGORIES = [
    ("Low-Code/No-Code Platforms", "categories/developer-tools/frameworks-platforms/low-code-no-code", "37"),
    ("AI Agent Platforms", "categories/ai-machine-learning/ai-development-platforms/ai-agent-platforms", "25"),
    ("Project Management Suites", "categories/business-software/project-work-management/project-management-suites", "21"),
    ("Infrastructure Monitoring Tools", "categories/infrastructure-operations/monitoring-observability/infrastructure-monitoring", "20"),
    ("Web Analytics", "categories/data-analytics/analytics/web-analytics", "16"),
    ("Team Chat & Messaging Tools", "categories/business-software/collaboration-communication/team-chat-messaging", "16"),
    ("PaaS & Deployment Tools", "categories/developer-tools/build-deployment/paas-deployment-tools", "17"),
    ("Note-Taking Tools", "categories/productivity-utilities/note-taking-knowledge-management/note-taking", "16"),
    ("Cloud File Sync & Share Tools", "categories/productivity-utilities/file-management-sync/cloud-file-sync-share", "14"),
    ("Personal Knowledge Management (PKM) Tools", "categories/productivity-utilities/note-taking-knowledge-management/personal-knowledge-management-pkm", "14"),
    ("Customer Communication Platforms", "categories/business-software/marketing-customer-engagement/customer-communication-platforms", "15"),
    ("Collaborative Workspaces", "categories/business-software/collaboration-communication/collaborative-workspaces", "15"),
]

# ---------------------------------------------------------------------------
# 4. Full category index tree (levels 1-2 from the landing page + deeper nodes)
# ---------------------------------------------------------------------------
CATEGORY_TREE = [
    ("AI & Machine Learning", "ai-machine-learning", [
        ("AI Development Platforms", "ai-development-platforms"),
        ("Machine Learning Infrastructure", "machine-learning-infrastructure"),
        ("AI Interaction & Interfaces", "ai-interaction-interfaces"),
        ("AI Security & Privacy", "ai-security-privacy"),
    ]),
    ("Business Software", "business-software", [
        ("CRM & Sales", "crm-sales"), ("ERP & Operations", "erp-operations"),
        ("Finance & Accounting", "finance-accounting"), ("Human Resources (HR)", "human-resources-hr"),
        ("Marketing & Customer Engagement", "marketing-customer-engagement"),
        ("Customer Support & Success", "customer-support-success"),
        ("E-commerce Platforms", "e-commerce-platforms"),
        ("Project & Work Management", "project-work-management"),
        ("Collaboration & Communication", "collaboration-communication"),
        ("Scheduling & Event Management", "scheduling-event-management"),
        ("Document Management & E-Signatures", "document-management-e-signatures"),
        ("Forms & Surveys", "forms-surveys"),
        ("Compliance & Risk Management", "compliance-risk-management"),
        ("Legal", "legal"), ("Education", "education"),
    ]),
    ("Community & Social", "community-social", [
        ("Social Networking", "social-networking"),
        ("Community Building Platforms", "community-building-platforms"),
        ("Collaboration & Feedback", "collaboration-feedback"),
    ]),
    ("Content & Publishing", "content-publishing", [
        ("Content Management Systems (CMS)", "content-management-systems-cms"),
        ("Blogging & Personal Sites", "blogging-personal-sites"),
        ("Community Platforms", "community-platforms"),
        ("Documentation & Knowledge Base", "documentation-knowledge-base"),
        ("Learning Management Systems (LMS)", "learning-management-systems-lms"),
        ("Digital Asset Management (DAM)", "digital-asset-management-dam"),
        ("Publishing", "publishing"),
    ]),
    ("Data & Analytics", "data-analytics", [
        ("Web & Product Analytics", "analytics"),
        ("Business Intelligence & Reporting", "business-intelligence-reporting"),
        ("Data Engineering & Integration", "data-engineering-integration"),
        ("Data Warehousing & Processing", "data-warehousing-processing"),
        ("Data Extraction & Web Scraping", "data-extraction-web-scraping"),
    ]),
    ("Developer Tools", "developer-tools", [
        ("Website Builders", "website-builders"), ("IDEs & Code Editors", "ides-code-editors"),
        ("Frameworks & Platforms", "frameworks-platforms"),
        ("API Development & Testing", "api-development-testing"),
        ("Testing & Quality Assurance", "testing-quality-assurance"),
        ("Version Control & Collaboration", "version-control-collaboration"),
        ("Code Analysis & Transformation", "code-analysis-transformation"),
        ("Build & Deployment", "build-deployment"),
        ("Integration Platforms", "integration-platforms"),
        ("AI Assisted Coding", "ai-assisted-coding"), ("Terminals", "terminals"),
    ]),
    ("Infrastructure & Operations", "infrastructure-operations", [
        ("Search Engines", "search-engines"),
        ("Cloud Infrastructure Management", "cloud-infrastructure-management"),
        ("Server & VM Management", "server-vm-management"),
        ("Monitoring & Observability", "monitoring-observability"),
        ("Databases", "databases"), ("Networking & Connectivity", "networking-connectivity"),
        ("Orchestration & Scheduling", "orchestration-scheduling"),
        ("Messaging & Event Streaming", "messaging-event-streaming"),
        ("Storage Solutions", "storage-solutions"), ("Backup & Recovery", "backup-recovery"),
    ]),
    ("Miscellaneous", "misc", [
        ("Cryptocurrency & Blockchain", "cryptocurrency-blockchain"),
        ("Gaming", "gaming"), ("Internet of Things (IoT)", "internet-of-things-iot"),
        ("Logistics & Supply Chain", "logistics-supply-chain"),
        ("Design & Prototyping", "design-prototyping"),
        ("Media & Streaming", "media-and-streaming"),
        ("Photo & Video Editors", "photo-video-editors"),
        ("Finance & Fintech", "finance-fintech"),
    ]),
    ("Productivity & Utilities", "productivity-utilities", [
        ("Office Suites", "office-suites"),
        ("Note Taking & Knowledge Management", "note-taking-knowledge-management"),
        ("Password & Secret Management", "password-secret-management"),
        ("Screen Capture & Recording", "screen-capture-recording"),
        ("File Management & Sync", "file-management-sync"),
        ("Email & Communication", "email-communication"),
        ("Browsers & Extensions", "browsers-extensions"),
        ("Automation", "automation"), ("Time & Task Management", "time-task-management"),
        ("Personal Finance Management", "personal-finance-management"),
        ("Design & Visualization", "design-visualization"),
        ("Bookmark & Content Management", "bookmark-content-management"),
        ("Remote Desktop & Access", "remote-desktop-access"),
        ("System Cleanup & Optimization", "system-cleanup"),
        ("Maps & Navigation", "maps-navigation"), ("Input & Dictation", "input-dictation"),
    ]),
    ("Security & Privacy", "security-privacy", [
        ("Identity & Access Management (IAM)", "identity-access-management-iam"),
        ("Secrets Management", "secrets-management"),
        ("Threat Detection & Response", "threat-detection-response"),
        ("Network Security", "network-security"),
        ("Data Security & Privacy", "data-security-privacy"),
        ("Application Security", "application-security"),
        ("Fraud Prevention", "fraud-prevention"),
    ]),
]

# Deeper (level-3) sub-categories observed in the sitemap, grouped by parent
DEEP_SUBCATEGORIES = {
    "developer-tools/ai-assisted-coding": ["ai-app-website-builders", "ai-code-reviewers",
        "ai-coding-agent-orchestrators", "ai-coding-agents", "ai-coding-assistants"],
    "developer-tools/ides-code-editors": ["ai-powered-editors", "general-purpose-editors"],
    "developer-tools/terminals": ["ai-terminals", "terminal-emulators", "terminal-multiplexers"],
    "developer-tools/frameworks-platforms": ["backend-as-a-service-baas", "frontend-developer",
        "low-code-no-code", "mobile-development", "web-frameworks"],
    "developer-tools/testing-quality-assurance": ["automated-testing", "visual-testing"],
    "developer-tools/code-analysis-transformation": ["static-analysis"],
    "developer-tools/version-control-collaboration": ["development-environments", "git-clients", "git-platforms"],
    "developer-tools/build-deployment": ["ci-cd-platforms", "paas-deployment-tools"],
    "developer-tools/integration-platforms": ["api-integration"],
    "developer-tools/api-development-testing": ["api-clients", "api-infrastructure"],
    "developer-tools/website-builders": ["website-builders"],
    "ai-machine-learning/ai-development-platforms": ["ai-agent-platforms", "ai-gateways",
        "ai-memory", "ai-sandboxes", "llm-application-frameworks"],
    "ai-machine-learning/machine-learning-infrastructure": ["ai-data-platforms", "gpu-compute-platforms",
        "llm-observability-evaluation", "local-model-runners"],
    "ai-machine-learning/ai-interaction-interfaces": ["ai-chat-interfaces", "ai-personal-assistants",
        "ai-search-tools", "browser-automation-for-ai", "enterprise-ai-search", "meeting-transcription"],
    "ai-machine-learning/ai-security-privacy": ["ai-api-key-protection", "ai-governance"],
    "business-software/crm-sales": ["crm-systems", "investor-relations-platforms", "sales-automation"],
    "business-software/erp-operations": ["asset-inventory-management", "erp-systems", "logistics-management"],
    "business-software/finance-accounting": ["accounting-software", "expense-management",
        "financial-planning-analysis-fp-a", "freelancer-tools", "invoicing-payments",
        "payment-infrastructure", "subscription-billing-management"],
    "business-software/project-work-management": ["agile-project-management", "project-management-suites", "task-management"],
    "business-software/marketing-customer-engagement": ["affiliate-referral-marketing",
        "customer-communication-platforms", "email-marketing-newsletters", "link-management-shorteners",
        "marketing-automation", "seo-tools", "social-media-management"],
    "business-software/customer-support-success": ["feedback-feature-request-management",
        "helpdesk-software", "live-chat-messaging", "product-tour-user-onboarding"],
    "business-software/collaboration-communication": ["collaborative-workspaces", "team-chat-messaging",
        "video-conferencing-virtual-office"],
    "business-software/scheduling-event-management": ["appointment-scheduling", "event-ticketing-management"],
    "business-software/document-management-e-signatures": ["document-management-systems",
        "e-signature-platforms", "secure-document-sharing"],
    "business-software/forms-surveys": ["form-builders", "survey-tools"],
    "business-software/compliance-risk-management": ["compliance-automation", "financial-risk-management"],
    "business-software/legal": ["legal-ai-platforms"],
    "business-software/human-resources-hr": ["hr-management-systems-hrms"],
    "business-software/e-commerce-platforms": ["frontend-e-commerce-solutions", "full-stack-e-commerce",
        "headless-commerce", "product-information-management-pim"],
    "community-social/social-networking": ["decentralized-social-networks", "news-aggregators"],
    "community-social/collaboration-feedback": ["community-feedback-platforms"],
    "content-publishing/content-management-systems-cms": ["headless-cms", "traditional-flat-file-cms"],
    "content-publishing/blogging-personal-sites": ["blogging-platforms"],
    "content-publishing/community-platforms": ["forum-software", "qa-platforms"],
    "content-publishing/documentation-knowledge-base": ["api-documentation-generators",
        "internal-knowledge-bases", "technical-writing-platforms", "wiki-software"],
    "content-publishing/learning-management-systems-lms": ["course-creation-platforms"],
    "content-publishing/digital-asset-management-dam": ["image-optimization-cdn", "photo-video-management"],
    "content-publishing/publishing": ["changelog-generators", "translation-management"],
    "data-analytics/analytics": ["product-analytics", "web-analytics"],
    "data-analytics/business-intelligence-reporting": ["bi-platforms", "data-visualization"],
    "data-analytics/data-engineering-integration": ["change-data-capture-cdc", "data-observability",
        "etl-data-integration", "semantic-layer-platforms"],
    "data-analytics/data-warehousing-processing": ["cloud-data-warehouses", "stream-processing"],
    "data-analytics/data-extraction-web-scraping": ["scraping-platforms-sdks", "web-crawlers"],
    "infrastructure-operations/cloud-infrastructure-management": ["cloud-computing",
        "cloud-cost-optimization", "infrastructure-as-code-iac"],
    "infrastructure-operations/server-vm-management": ["control-panels"],
    "infrastructure-operations/monitoring-observability": ["error-tracking", "infrastructure-monitoring",
        "log-management", "performance-monitoring-apm", "status-pages", "uptime-monitoring"],
    "infrastructure-operations/databases": ["database-tools-guis", "distributed-storage",
        "graph-databases", "in-memory-databases", "nosql-document-databases",
        "relational-databases-sql", "time-series-databases", "vector-databases"],
    "infrastructure-operations/networking-connectivity": ["vpn-secure-access", "websockets-servers"],
    "infrastructure-operations/orchestration-scheduling": ["container-orchestration", "distributed-compute",
        "durable-execution", "job-scheduling", "workflow-orchestration"],
    "infrastructure-operations/messaging-event-streaming": ["event-streaming-platforms",
        "message-queues", "webhook-platforms"],
    "infrastructure-operations/storage-solutions": ["cloud-storage", "file-management", "storage"],
    "infrastructure-operations/backup-recovery": ["server-backup"],
    "infrastructure-operations/search-engines": ["search-engines"],
    "productivity-utilities/office-suites": ["document-editors", "spreadsheets"],
    "productivity-utilities/note-taking-knowledge-management": ["collaborative-notes-wikis",
        "note-taking", "personal-knowledge-management-pkm", "secure-encrypted-notes"],
    "productivity-utilities/password-secret-management": ["password-managers"],
    "productivity-utilities/screen-capture-recording": ["screen-recording", "screenshot-utilities"],
    "productivity-utilities/file-management-sync": ["cloud-file-sync-share"],
    "productivity-utilities/email-communication": ["email-clients", "email-platforms",
        "push-notification", "secure-email-providers"],
    "productivity-utilities/browsers-extensions": ["browser-extensions", "web-browsers"],
    "productivity-utilities/automation": ["browser-automation", "chatbot-platforms", "workflow-automation"],
    "productivity-utilities/time-task-management": ["launchers-quick-access", "task-management-apps",
        "time-tracking", "workspace-organizers"],
    "productivity-utilities/personal-finance-management": ["budgeting-apps", "investment-tracking"],
    "productivity-utilities/design-visualization": ["code-snippet-stylers", "online-design", "whiteboarding"],
    "productivity-utilities/bookmark-content-management": ["bookmark-managers", "personal-tracking-apps",
        "read-it-later-knowledge-hubs"],
    "productivity-utilities/remote-desktop-access": ["remote-desktop-software"],
    "productivity-utilities/system-cleanup": ["system-cleanup"],
    "productivity-utilities/maps-navigation": ["maps-navigation"],
    "productivity-utilities/input-dictation": ["voice-dictation"],
    "security-privacy/identity-access-management-iam": ["authentication-sso", "authorization-permissions"],
    "security-privacy/secrets-management": ["secrets-platforms"],
    "security-privacy/threat-detection-response": ["security-automation-siem-soar",
        "threat-intelligence", "vulnerability-scanning"],
    "security-privacy/network-security": ["ssh-access-management", "vpn-secure-tunnels"],
    "security-privacy/data-security-privacy": ["encrypted-communication", "encrypted-storage"],
    "security-privacy/application-security": ["captcha-bot-protection", "feature-flags"],
    "security-privacy/fraud-prevention": ["financial-fraud-detection"],
    "misc/cryptocurrency-blockchain": ["trading-bots", "web3-platforms"],
    "misc/gaming": ["game-development-platforms"],
    "misc/internet-of-things-iot": ["iot-databases", "smart-home-automation"],
    "misc/design-prototyping": ["ui-ux-design", "vector-graphics-illustration"],
    "misc/media-and-streaming": ["digital-signage", "media-servers", "video-platforms"],
    "misc/photo-video-editors": ["audio-editors", "photo-editors", "video-editors"],
    "misc/finance-fintech": ["financial-data", "fintech-infrastructure"],
}


def slugify(name):
    import re
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s


def tool_url(slug):
    return f"{SITE}/{slugify(slug)}"


def alt_url(name):
    return f"{SITE}/alternatives/{slugify(name)}"
