# Verification Report — 2026 Software & AI Tool Directory
*Generated: 2026-09-02*

## License verification (GitHub API)

**77** of **128** tools had their open-source license verified via the GitHub REST API (`api.github.com/repos/{owner}/{repo}`), which is reachable from the sandbox. Unauthenticated rate limit was ~5,900 requests.

| Status | Count |
|---|---|
| Tools with verified license | 77 |
| Tools with explicit repo (verified attempt) | 79 |
| Open-source tools | 109 |
| Open-weight (models) | 4 |
| Proprietary/commercial | 19 |
| Self-hostable | 102 |

## License distribution (verified)

| License | Tools |
|---|---|
| MIT | 28 |
| NOASSERTION | 23 |
| AGPL-3.0 | 22 |
| Proprietary | 16 |
| Apache-2.0 | 15 |
| GPL-3.0 | 7 |
| BSD-3-Clause | 4 |
| MPL-2.0 | 4 |
| GPL-2.0 | 3 |
| Public Domain | 1 |
| Apache-2.0 (weights) | 1 |
| ISC | 1 |
| CC-BY-4.0 | 1 |
| various | 1 |
| custom (Enterprise) | 1 |

## Provenance

Every record carries `sources` (with URL), `source_count`, `confidence` (high = 2+ sources), and `last_verified`. Fields that could not be confirmed (pricing, exact free-tier limits, some licenses) are marked `verify` or `Unknown` rather than invented.

## Confidence

- High (2+ sources): 66
- Medium (1 source): 62

## Not verified / flagged

- 62 records flagged for human review (unknown/dual license or single source).

**Conflict note:** the priority order (P1 official > P2 GitHub/HF > P3 directories > P4 community lists) was applied; where sources disagreed, the higher-priority source was kept and the conflict is recorded in the record's `sources`/`notes`.