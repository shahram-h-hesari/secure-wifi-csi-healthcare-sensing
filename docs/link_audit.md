# Link Audit — Secure WiFi CSI Healthcare Sensing Repository

This document tracks the status of all external URLs referenced across the repository (docs, literature, paper_cards, related_projects). It serves as a running audit log for link verification, broken-link detection, and placeholder URL resolution.

> **Last Updated:** 2025-05-25

---

## Purpose

- Identify and replace GitHub topic-page placeholders (`github.com/topics/...`) with canonical repository URLs.
- Flag entries where no confirmed public repository was found (label: **Pending verification**).
- Ensure no link falsely implies code was tested or results reproduced locally.
- Document URL corrections across phases of the literature cleanup.

---

## Remaining Literature Cleanup Pass

The following items were identified during Phase 11 (2025-05-25) as requiring URL correction or verification. Items marked **FIXED** have been updated in the relevant file.

| File | Entry | Old URL | Corrected URL | Status |
|------|-------|---------|---------------|--------|
| docs/related_projects.md | Awesome-RIS-Security | https://github.com/topics/ris-security | https://github.com/awesome-ris-security/awesome-ris-security.github.io | FIXED |
| docs/related_projects.md | WiFi-CSI-Human-Pose-Detection | https://github.com/topics/wifi-csi-pose | https://github.com/euaziel/WiFi-CSI-Human-Pose-Detection | FIXED |
| docs/related_projects.md | RuView | https://github.com/topics/ruview | https://github.com/ruvnet/RuView | FIXED |
| docs/related_projects.md | CSI-Bench | https://github.com/topics/csi-benchmark | https://github.com/Jenny-Zhu/CSI-Bench-Real-WiFi-Sensing-Benchmark | FIXED |
| docs/related_projects.md | unilateral-csi-entropy | https://github.com/topics/csi-entropy | No confirmed canonical repo found. Topic page retained with explicit **URL pending verification** notice. | PENDING |

---

## URL Verification Policy

1. **No `github.com/topics/...` URLs** may be used as the primary link for a project entry. Topic pages aggregate many projects and do not represent a single codebase.
2. **No `github.com/example/...` URLs** or any invented/placeholder URLs.
3. For entries where no canonical repository is found after web search: use the best available URL (e.g., a project website or arXiv page) and note `URL pending verification — no confirmed public repository found.`
4. Entries in `papers.csv`, `reproducibility_matrix.md`, `code_release_watchlist.md`, `references.bib`, and `prisma_tracking.csv` must be consistent with any URL corrections made here.

---

## Literature Files Cross-Reference

| Central File | Last Audit Pass | Notes |
|---|---|---|
| `literature/papers.csv` | 2025-05-24 | 11 papers; all URLs verified or marked Pending verification |
| `literature/reproducibility_matrix.md` | 2025-05-24 | Rebuilt; 11 entries; aligned with papers.csv |
| `literature/code_release_watchlist.md` | 2025-05-24 | Rebuilt; public code section separated from no-code section |
| `literature/references.bib` | 2025-05-24 | Cleaned; fake entries removed; TODO blocks for unverified items |
| `literature/prisma_tracking.csv` | 2025-05-24 | Rebuilt; 14-column schema; 11 rows |
| `literature/paper_cards/README.md` | 2025-05-24 | Created; indexes all paper cards by category |
| `docs/related_projects.md` | 2025-05-25 | Topic-page placeholder URLs replaced with canonical URLs |
| `THIRD_PARTY_NOTICES.md` | 2025-05-24 | Updated; NoiSec URL corrected; date corrected |

---

## Outstanding Items (Pending Verification)

| Entry | Location | Issue | Action Required |
|-------|----------|-------|----------------|
| unilateral-csi-entropy | docs/related_projects.md, third_party/wifi_sensing_security/unilateral_csi_entropy/ | No confirmed public GitHub repository found for this project name. | Manual search or removal if no canonical source is identified. |
| goop-veil dataset | docs/related_projects.md | Dataset existence not confirmed. | Verify at https://github.com/kobepaw/goop-veil and update status if dataset is absent. |
| CsiGAN license | literature/papers.csv, reproducibility_matrix.md | License for ChunjingXiao/CsiGAN not confirmed. | Check repo license tab; update from "Pending verification" if MIT or other confirmed. |
| NoiSec license | literature/papers.csv, reproducibility_matrix.md | License not confirmed. | Check repo license tab; update from "Pending verification". |

---

*This audit document is maintained as part of the Secure WiFi CSI Healthcare Sensing research prototype at Portland State University.*
