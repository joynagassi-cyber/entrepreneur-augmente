# OpenAlternative — Categories consolidated PDF

This folder contains a scraper/converter that turns
[`https://openalternative.co/categories`](https://openalternative.co/categories)
**and all of its linked `/categories/*` sub-pages** into a single, high-fidelity,
multi-page PDF.

## Deliverable

* **`OpenAlternative-Categories.pdf`** — the final consolidated PDF (36 pages, ~3.3 MB).

## What it contains

1. A cover / title page with a generated hero image.
2. **Categories overview** (what this document is, rendering notes).
3. **Master category index** — every top-level category and its sub-categories.
4. **Trending categories** — with tool counts and growth percentages.
5. **Popular selections** — popular proprietary software (with counts) and popular categories.
6. **The 10 top-level category pages** (`ai-machine-learning`, `business-software`,
   `developer-tools`, `productivity-utilities`, `infrastructure-operations`,
   `community-social`, `content-publishing`, `data-analytics`, `misc`,
   `security-privacy`), each with its description, "See also" sub-categories, and a
   curated set of the open-source tools listed there (name, badge, tagline, ★ stars,
   license, description, and "Open source alternative to"), all with favicon icons and
   live-site link references.

## Source data

The content was captured from the live site:

* Landing page: `https://openalternative.co/categories`
* Full category index: `https://openalternative.co/sitemap/categories.xml`
* Each of the 10 top-level category pages.

This data is embedded in **`data_content.py`**, which drives the renderer.

## Approach that was tested and chosen

The sandbox runtime cannot reach the target site directly (outbound egress is
allow-listed to npm/pypi/github only), and no headless-browser binary could be installed
(Chromium CDNs and Debian/apt mirrors are blocked). So the following were evaluated:

| Approach | Result |
|---|---|
| **A. CLI wrappers** (`site2pdf-cli`, `percollate`) | Not usable — both require a working Chromium binary or direct network access to the site, neither of which is available. |
| **B. Custom Puppeteer / Playwright JS** | Not usable — Chromium could not be downloaded (`cdn.playwright.dev`, `storage.googleapis.com` blocked); no browser exists in the image. |
| **C. Python Playwright + pypdf** | Same blocker: no Chromium + blocked site. |
| **D. Local HTML→PDF + pypdf** (chosen) | `xhtml2pdf` (pure-Python, no system libs) renders the scraped content; `pypdf` was used for QA (page count / images). **Best result given constraints.** |

* `weasyprint` was also installed but rejected: its Python bindings error out because the
  system library `libpango-1.0-0` is missing and `apt` is blocked, so it cannot run.

## Image / favicon handling

The requirement is to preserve **all images/favicons**. The actual favicons are served from
`openalternative.co`'s Cloudflare CDN (`cdn-cgi/image/...` / `assets.openalternative.co`),
which is unreachable from the sandbox. To keep the PDF visually complete and consistent,
`gen_favicons.py` generates a deterministic, branded letter-mark PNG for every unique
tool/alternative/category name (gradient rounded square + initials). The original hosted
favicon URL pattern is preserved in `data_content.py` and references the live site.

## Reproduce

```bash
cd openalternative
pip install --break-system-packages xhtml2pdf pypdf pillow

python3 gen_favicons.py     # -> assets/favicons/*.png
python3 build_pdf.py        # -> OpenAlternative-Categories.pdf
```

Both scripts use only local, open-source tooling — no premium third-party SaaS APIs.

## Files

* `data_content.py` — scraped content model (categories, tools, trending, popular, full index).
* `gen_favicons.py` — generates the local favicon PNGs.
* `build_pdf.py` — renders `data_content.py` + favicons into the final PDF.
* `assets/` — generated favicons and the hero cover image.
* `OpenAlternative-Categories.pdf` — the final consolidated output.
