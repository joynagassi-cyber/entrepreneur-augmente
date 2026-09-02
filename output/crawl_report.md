# Crawl Report — 2026 Software & AI Tool Directory
*Generated: 2026-09-02*

## Network constraints discovered

The sandbox runtime has **restricted egress**: direct `curl`/`requests` reach only `github.com` and `api.github.com` (plus package registries npm/pypi). All other required sources (openalternative.co, alternativeto.net, capterra.com, g2.com, getapp.com, stackshare.io, awesome-selfhosted.net, f-droid.org, huggingface.co) are **blocked at the network layer** from the sandbox (SSL/connection errors).

However, the platform's **web-fetch** capability reaches most of these sources. It was used to capture structured content for: OpenAlternative (categories + sitemap + 10 top-level category pages), AlternativeTo (Notion page), Awesome-Selfhosted (homepage), Capterra (homepage), StackShare (trending), Hugging Face (models homepage), GitHub (repo pages).

## Sources processed

| Source | URL | Status | Pages | Tools | Reliability |
|---|---|---|---|---|---|
| OpenAlternative | https://openalternative.co/categories | captured | 11 | 69 | High |
| AlternativeTo | https://alternativeto.net/ | partial | 1 | 4 | Medium |
| GitHub (API) | https://api.github.com | verified | 79 | 79 | High (Priority 1/2) |
| Awesome-Selfhosted | https://awesome-selfhosted.net/ | partial | 1 | 12 | Medium-High |
| Hugging Face | https://huggingface.co/ | partial | 1 | 5 | High |
| StackShare | https://stackshare.io/ | partial | 1 | 8 | Medium |
| Capterra | https://www.capterra.com/ | partial | 1 | 6 | Medium |
| GitHub Awesome Lists | https://github.com/awesome-selfhosted | indexed | 0 | 128 | Low-Medium |
| F-Droid | https://f-droid.org/ | blocked | 0 | 2 | Medium |
| G2 | https://www.g2.com/ | blocked | 0 | 0 | Medium |
| GetApp | https://www.getapp.com/ | not-tested | 0 | 0 | Medium |

## What was blocked / not crawlable

- **G2** — `https://www.g2.com/categories/ai` returned a 404; category pages are bot-protected and JS-heavy; not reliably crawlable via fetch. Commercial classification for G2 was sourced from Capterra + editorial knowledge.
- **GetApp** — sandbox blocked; not tested via fetch this run.
- **F-Droid** — specific package URL returned 404 (package may be archived). Mobile open-source tools were sourced from GitHub + knowledge.
- **Site/CDN image hosts** (assets.openalternative.co, cdn.revinel.com, awesome-selfhosted static assets) — blocked; favicons synthesized locally.

## Strategy

Content was captured with the platform fetch tool (structured text), repos verified via the GitHub REST API (reachable via curl), and the dataset normalized into one canonical record per tool with provenance.