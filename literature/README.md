# Literature and Reproducibility Tracker
## Secure WiFi CSI Healthcare Sensing — Research Prototype

> **Last Updated:** 2026-05-24
> **Status:** Active — initial cleanup complete; 11 papers tracked; 7 with confirmed public code; 4 pending code verification

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

## Critical Clarifications

> **"Public GitHub available" does NOT mean code has been tested locally, reproduced, or integrated into this repository.**
> All public-code entries default to `Reproducibility Status: Not tested` and `Tested Locally: No` unless explicit evidence exists in this repository.

> **Duplicate paper cards across category folders are NOT allowed.**
> Each paper or repository must have exactly ONE paper card in exactly ONE category folder.
> If a card exists in `with_public_code/`, `datasets_and_benchmarks/`, or `defense_methods/`, it must NOT also appear in `no_confirmed_code/`.

> **Category folder assignment rules:**
> - `with_public_code/` — Papers or repositories with a confirmed, verified public GitHub URL
> - `no_confirmed_code/` — ONLY for papers where no public GitHub has been confirmed as of the last check
> - `datasets_and_benchmarks/` — For dataset/benchmark repositories such as CSI-Bench
> - `defense_methods/` — For defense-method repositories or defense-method reference papers such as NoiSec

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
| Systematic-review screening decisions | Duplicate paper cards across folders |

---

## File Organization

| File / Folder | Purpose |
|---|---|
| `README.md` (this file) | Overview of the literature tracking layer |
| `papers.csv` | Machine-readable index of all tracked papers and repositories |
| `references.bib` | BibTeX entries (verified or marked PENDING) |
| `reproducibility_matrix.md` | Human-readable reproducibility status table with sections |
| `code_release_watchlist.md` | Public-code and no-code watchlist for monitoring |
| `systematic_review_protocol.md` | Systematic review plan (not a completed review) |
| `inclusion_exclusion_criteria.md` | Criteria for including/excluding papers in the review |
| `search_queries.md` | Exact search queries for systematic review reproducibility |
| `prisma_tracking.csv` | PRISMA-compatible paper screening records |
| `thesis_chapter_mapping.md` | Maps thesis chapters to GitHub artifacts and literature evidence |
| `paper_cards/` | Structured summaries per paper or repository |
| `paper_cards/with_public_code/` | Papers/repos with confirmed public GitHub code (NOT necessarily tested) |
| `paper_cards/no_confirmed_code/` | Papers WITHOUT confirmed public GitHub code |
| `paper_cards/datasets_and_benchmarks/` | Dataset and benchmark repository cards (e.g., CSI-Bench) |
| `paper_cards/defense_methods/` | Defense-method repository or reference cards (e.g., NoiSec) |

---

## Status Legend

### Code Status

| Value | Meaning |
|---|---|
| Public GitHub available | Code confirmed at official repository URL; NOT necessarily tested locally |
| No confirmed public GitHub found | No public code found as of last check |
| Pending verification | Not yet checked |

### Reproducibility Status

| Value | Meaning |
|---|---|
| Not tested | Code or paper available but code has not been run locally |
| Not reproducible from public code yet | No confirmed public code; cannot reproduce |
| Pending verification | Not yet assessed |

### Reproducibility Score (A–E)

| Score | Meaning |
|---|---|
| A | Official code + dataset available; installation tested; baseline reproduced locally |
| B | Official code available; dataset available or documented; not yet reproduced locally |
| C | Code available but dataset missing, unclear, or license/access unresolved |
| D | Paper available but no confirmed public code |
| E | Unverified or weak relevance; watchlist/background only |

> **Note:** Scores should be conservative. Do not assign A unless the code actually runs locally and results are reproduced.

---

## Important Disclaimers

- **Inclusion does not imply endorsement or validation.** Papers and repositories are included for literature evidence, not as validated methods.
- **All uncertain citation/code/license details remain Pending verification** until independently confirmed.
- **This repository uses synthetic CSI-like data only.** No real WiFi CSI hardware, clinical data, or medical-grade validation is claimed.
- **No third-party code has been copied.** All third-party items are external references only.
- **Reproducibility scores reflect local testing status.** A score of B does not mean the code was run; it means the code appears available but has not been tested locally.
- **Public GitHub available ≠ Tested locally ≠ Results reproduced.**

---

## Quick Links

- [`literature/papers.csv`](papers.csv) — Machine-readable paper index
- [`literature/reproducibility_matrix.md`](reproducibility_matrix.md) — Full reproducibility status table
- [`literature/code_release_watchlist.md`](code_release_watchlist.md) — Watchlist for code monitoring
- [`literature/prisma_tracking.csv`](prisma_tracking.csv) — PRISMA screening records
- [`literature/systematic_review_protocol.md`](systematic_review_protocol.md) — Systematic review plan
- [`literature/thesis_chapter_mapping.md`](thesis_chapter_mapping.md) — Chapter-to-evidence map
- [`docs/open_source_gap.md`](../docs/open_source_gap.md) — Open-source gap analysis
- [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) — Attribution and license policy

---

*Maintained as part of the PhD research project: "Adversarial Attack and Software-Based Hardening of Deep Learning Wi-Fi Sensing for Vital Sign and Fall Detection in Elderly Homes with Worst-Case Clinical Safety Metrics" — Portland State University.*
