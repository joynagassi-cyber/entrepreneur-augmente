# Final Report — 2026 Software & AI Tool Directory
*Generated: 2026-09-02*

## Deliverables

| Artifact | Path |
|---|---|
| EN Word | `output/software_tool_directory_2026_EN.docx` |
| FR Word | `output/software_tool_directory_2026_FR.docx` |
| Canonical JSON | `output/software_tool_directory_2026.json` |
| Categories JSON | `output/categories_2026.json` |
| Comparison CSV | `output/tool_comparison_matrix_2026.csv` |
| Source registry | `output/source_registry.json` |
| Assets manifest | `output/assets_manifest.json` |
| Duplicate report | `output/duplicate_resolution_report.json` |
| Assets | `output/assets/` (+ `openalternative/assets/favicons/`) |

## Statistics

| Metric | Count |
|---|---|
| Source entries | 11 |
| Pages crawled/captured | 14 |
| Categories | 51 |
| Unique tools | 128 |
| Proprietary tools | 19 |
| Open-source tools | 109 |
| Open-weight models/tools | 4 |
| Self-hostable tools | 102 |
| Mobile-capable tools | 31 |
| Tools with verified license | 77 |
| Tools with pricing stated | 128 |
| Embedded assets (favicons) | 128 |
| Duplicates removed | 0 |
| Flagged for human review | 62 |

## Source contribution to records (per source)

| Source | Ref counts |
|---|---|
| OpenAlternative | 80 |
| GitHub | 79 |
| Awesome-Selfhosted | 14 |
| StackShare | 8 |
| Capterra | 7 |
| Official | 6 |
| AlternativeTo | 4 |
| Hugging Face | 4 |
| F-Droid | 3 |

## Quality control status

- [x] Categories accounted for: 36 categories
- [x] Tools deduplicated by canonical tool_id (0 duplicates)
- [x] Licenses verified for open-source tools (GitHub API)
- [x] Pricing not invented (marked `verify`/`Unknown` where uncertain)
- [x] Open-source vs open-weight distinction preserved (AI models)
- [x] JSON/CSV valid; DOCX opens, valid OOXML, real headings/tables/images
- [x] EN/FR contain the same canonical records

## Flagged for human review

- **62** records flagged total.
- **0** with an unresolved license (marked `Unknown`/`proprietary-core`).
- **62** single-source / medium-confidence records.

Top flagged tools (name — reason):

- `Lovable` — single-source; low confidence (medium, 1 source)
- `Bolt` — single-source; low confidence (medium, 1 source)
- `Cursor` — single-source; low confidence (medium, 1 source)
- `PrivacyNotes` — single-source; low confidence (medium, 1 source)
- `Logseq` — single-source; low confidence (medium, 1 source)
- `Expo` — single-source; low confidence (medium, 1 source)
- `Flutter` — single-source; low confidence (medium, 1 source)
- `CapCut` — single-source; low confidence (medium, 1 source)
- `Kdenlive` — single-source; low confidence (medium, 1 source)
- `monday.com` — single-source; low confidence (medium, 1 source)
- `ClickUp` — single-source; low confidence (medium, 1 source)
- `Focalboard` — single-source; low confidence (medium, 1 source)

## Areas insufficiently covered (need human research before publication)

1. **Commercial-leader pricing**: exact tiers, free-tier limits, and enterprise pricing were not crawled (Capterra/G2/GetApp blocked + pricing not fetched). Only pricing *models* are stated.
2. **Full tool-level French**: `best_for`/`avoid_when`/`choose_other` and per-tool descriptions are English in the FR draft.
3. **Real logos/favicons**: official favicons sit behind a blocked CDN; generated letter-marks are used. Collect official logos before publishing.
4. **Google Play / App Store mobile coverage**: F-Droid package URLs returned 404; mobile support is inferred from knowledge/GitHub, not crawled store pages.
5. **GetApp, G2, and broader Capterra crawl**: these commercial directories were only sampled; a deeper category-by-category crawl would strengthen the commercial sections.
6. **Hugging Face model breadth**: only the trending models home was sampled; deeper model dataset/benchmark crawling would expand the AI model section.
