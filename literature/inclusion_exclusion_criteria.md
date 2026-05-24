# Inclusion and Exclusion Criteria

**Project:** Secure WiFi CSI Healthcare Sensing — Systematic Review
**Last Updated:** 2026-05-24
**Status:** Draft v0.1

---

## Inclusion Criteria

A paper is **included** if it meets ALL of the following:

| # | Criterion | Rationale |
|---|---|---|
| I1 | Published 2018 or later | Captures deep learning era for Wi-Fi sensing |
| I2 | Peer-reviewed venue (journal, conference, workshop) OR arXiv preprint with 6+ months of availability | Ensures baseline quality while allowing emerging work |
| I3 | Addresses deep learning models applied to Wi-Fi CSI sensing (human activity, vital signs, fall detection, or presence detection) | Core domain of thesis |
| I4 | Addresses adversarial attacks, robustness, privacy threats, OR software-based defenses for such models | Core research question |
| I5 | Full text accessible (open access, institutional access, or preprint) | Required for data extraction |

A paper is **also included** (additional track) if:

| # | Criterion | Rationale |
|---|---|---|
| I6 | Provides a public dataset or benchmark for Wi-Fi CSI sensing evaluation | Supports reproducibility and Chapter 7 |
| I7 | Provides open-source code implementing an attack or defense on Wi-Fi sensing models | Directly supports reproducibility matrix |

---

## Exclusion Criteria

A paper is **excluded** if it meets ANY of the following:

| # | Criterion | Rationale |
|---|---|---|
| E1 | Does not use Wi-Fi CSI or similar RF-based passive sensing (e.g., uses cameras, wearables, UWB, radar as primary modality without comparison) | Out of domain |
| E2 | Does not address deep learning or machine learning models | Out of scope for adversarial ML focus |
| E3 | Published before 2018 | Pre-dates deep learning dominance in this area |
| E4 | Not available in English | Language limitation of reviewer |
| E5 | No adversarial, robustness, privacy, or defense component | Does not address core research question |
| E6 | Hardware-only defense (no software component evaluated) | Out of scope for software-based hardening thesis |
| E7 | Duplicate of an already-included paper (same dataset, same results, prior version) | De-duplication |
| E8 | Grey literature without peer review AND less than 6 months old on arXiv | Insufficient quality signal |

---

## Edge Cases and Adjudication

- Papers on physical-layer security that include a machine learning component and compare against CSI sensing are included under I4
- Survey papers on Wi-Fi sensing or adversarial ML are included only if they synthesize results directly relevant to healthcare sensing adversarial robustness
- Papers where real-data vs. synthetic-data experiments are mixed: include but note data type in extraction
- Uncertain cases: default to include at title/abstract stage; resolve at full-text stage

---

## Application to `papers.csv`

Each paper in `papers.csv` has been pre-screened against these criteria. The `thesis_chapters` column serves as a proxy for relevance mapping. The `prisma_tracking.csv` file records screening decisions with rationale.

---

*These criteria are a living document. Update version and date with each significant revision.*
