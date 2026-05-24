# Literature and Reproducibility Tracker
## Secure WiFi CSI Healthcare Sensing — Research Prototype

> **Last Updated:** 2026-05-24  
> **Status:** Active — scaffolding complete; paper cards and reproducibility scoring in progress.

---

## Purpose

This folder is the **literature and reproducibility tracking layer** for the Secure WiFi CSI Healthcare Sensing PhD research project. It provides:

- A curated index of papers and repositories relevant to the thesis
- Reproducibility status for each public-code reference
- A systematic review scaffold for a planned future review paper
- Thesis-chapter-to-evidence mapping
- PRISMA-compatible screening records

**This folder is NOT a PDF archive.** Copyrighted papers are not stored here. Third-party source code and datasets are not copied here. Only metadata, official links, original summaries written by the repository author, BibTeX entries after verification, and reproducibility notes are stored.

---

## What Is and Is Not Stored Here

| Allowed | Not Allowed |
|---------|-------------|
| Paper metadata (title, year, venue, authors) | Copyrighted PDFs |
| DOI links and official publisher URLs | Paywalled IEEE/ACM PDFs |
| arXiv / OpenReview / project-page links | Copied paper text |
| Official GitHub links | Third-party source code |
| Dataset source links (no downloads) | Downloaded datasets |
| BibTeX entries (after verification only) | Invented citation details |
| Short original summaries by repo author | Fake or unverified metadata |
| Reproducibility notes and code-status notes | Claims of tested/reproduced code unless verified |
| Thesis-chapter relevance notes | Medical or clinical validation claims |
| Systematic-review screening decisions |   |

---

## File Organization

| File / Folder | Purpose |
|---|---|
| `README.md` (this file) | Overview of the literature tracking layer |
| `papers.csv` | Machine-readable index of all tracked papers and repositories |
| `references.bib` | Verified BibTeX entries (or TODO placeholders for unverified) |
| `reproducibility_matrix.md` | Human-readable reproducibility status table |
| `systematic_review_protocol.md` | Systematic review plan (not a completed review) |
| `inclusion_exclusion_criteria.md` | Criteria for including/excluding papers in the review |
| `search_queries.md` | Exact search queries for systematic review reproducibility |
| `prisma_tracking.csv` | PRISMA-compatible paper screening records |
| `thesis_chapter_mapping.md` | Maps thesis chapters to GitHub artifacts and literature evidence |
| `paper_cards/` | Structured summaries per paper or repository |
| `paper_cards/with_public_code/` | Papers/repos with confirmed public GitHub code |
| `paper_cards/no_confirmed_code/` | High-priority papers without confirmed public code |
| `paper_cards/datasets_and_benchmarks/` | Dataset/benchmark paper cards |
| `paper_cards/defense_methods/` | Defense method reference cards |
| `paper_cards/healthcare_sensing/` | Healthcare sensing reference cards |

---

## Status Legend

### Code Status
| Value | Meaning |
|---|---|
| Public official code | Code confirmed at official repository URL |
| Public unofficial code | Third-party reproduction, not from original authors |
| No confirmed public GitHub found | No public code found as of last check |
| Pending release | Authors announced intent to release |
| Broken/unusable | Code found but cannot run / dependencies broken |
| Pending verification | Not yet checked |

### Dataset Status
| Value | Meaning |
|---|---|
| Public dataset | Dataset freely available without request |
| Request-only dataset | Requires formal data-access request |
| Dataset link broken | Link found but URL dead |
| Dataset missing | No public dataset link found |
| Candidate dataset | Identified as candidate but not yet verified |
| Pending verification | Not yet checked |

### Reproducibility Status
| Value | Meaning |
|---|---|
| Not tested | Code/data not yet run locally |
| Installed successfully | Dependencies installed without errors |
| Dataset unavailable | Code available but dataset cannot be accessed |
| Ran baseline | Ran inference/baseline script |
| Ran attack | Ran adversarial attack script |
| Partially reproduced | Some results match; not full reproduction |
| Fully reproduced | Main results match within reported margins |
| Failed to reproduce | Attempted but results do not match |
| Not reproducible from public artifacts | No public code or data available |

### Reproducibility Score (A–E)
| Score | Meaning |
|---|---|
| A | Official code + dataset available; installation tested; baseline reproduced |
| B | Official code available; dataset available or documented; not yet reproduced |
| C | Code available but dataset missing, unclear, or license/access unresolved |
| D | Paper available but no confirmed public code |
| E | Unverified or weak relevance; watchlist/background only |

> **Note:** Scores should be conservative. Do not assign A unless the code actually runs locally and results are reproduced. Most entries begin at B, C, D, or Pending verification.

---

## Important Disclaimers

- **Inclusion does not imply endorsement or validation.** Papers and repositories are included for literature evidence, not as validated methods.
- **All uncertain citation/code/license details remain Pending verification** until independently confirmed.
- **This repository uses synthetic CSI-like data only.** No real WiFi CSI hardware, clinical data, or medical-grade validation is claimed.
- **No third-party code has been copied.** All third-party items are external references only.
- **Reproducibility scores reflect local testing status.** A score of B does not mean the code was run; it means the code appears available but has not been tested locally.

---

## Related Documents

- [`literature/reproducibility_matrix.md`](reproducibility_matrix.md) — Full reproducibility status table
- [`literature/systematic_review_protocol.md`](systematic_review_protocol.md) — Systematic review plan
- [`literature/thesis_chapter_mapping.md`](thesis_chapter_mapping.md) — Chapter-to-evidence map
- [`literature/papers.csv`](papers.csv) — Machine-readable paper index
- [`docs/open_source_gap.md`](../docs/open_source_gap.md) — Open-source gap analysis
- [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) — Attribution and license policy

---

*Maintained as part of the PhD research project: "Adversarial Attack and Software-Based Hardening of Deep Learning Wi-Fi Sensing for Vital Sign and Fall Detection in Elderly Homes with Worst-Case Clinical Safety Metrics" — Portland State University.*
