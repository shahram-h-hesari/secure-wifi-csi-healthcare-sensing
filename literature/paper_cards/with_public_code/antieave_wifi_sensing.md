# Paper Card: AntiEave — Scheduled Spatial Sensing against Adversarial WiFi Sensing

## Status Summary

| Field | Value |
|---|---|
| Work type | Conference paper with public code |
| Code status | Public GitHub available |
| Dataset status | Pending verification |
| License status | Pending verification (no LICENSE file observed in upstream repo) |
| Reproducibility status | Not tested |
| Repository status | External reference only; no code copied |
| Thesis relevance | Chapter 6 defense methods; anti-eavesdropping and privacy defense |

## Official Links

| Item | URL | Status |
|---|---|---|
| GitHub repository | https://github.com/MoWiNG-Lab/AntiEave-WiFi-Sensing | Verified live |
| Venue | IEEE PerCom 2023 | Verified from upstream README and BibTeX |

## Code and Dataset Availability

| Item | Status | Notes |
|---|---|---|
| Public code | Available | https://github.com/MoWiNG-Lab/AntiEave-WiFi-Sensing |
| Code tested locally | No | Not tested in this repository |
| Dataset | dataset/ folder in upstream repo | Actual dataset files stored via git-lfs; pending verification of accessibility |
| Dataset license | Pending verification | Not confirmed from upstream repo |
| License | Pending verification | No explicit LICENSE file observed in upstream repo |

## Paper / Project Summary

AntiEave proposes a scheduled spatial sensing defense against adversarial WiFi sensing attacks.
The approach uses spatially distributed transmitter antennas connected to a single source device
to schedule sensing in a way that resists eavesdropping by an adversary.

> **Note:** This is not a healthcare-specific work.
> External reference only. No code, PDFs, or datasets are copied into this repository.

## Task and Modality

| Field | Value |
|---|---|
| Primary task | Anti-eavesdropping defense for WiFi sensing |
| Modality | WiFi CSI (Channel State Information) |
| Venue | IEEE PerCom 2023 |
| Authors | S. M. Hernandez and Eyuphan Bulut (verified from upstream BibTeX) |

## Attack / Defense / Benchmark Role

This is a **defense paper**.
It proposes scheduled spatial sensing as a countermeasure against adversarial WiFi sensing.
Relevant to anti-eavesdropping, privacy preservation, and physical-layer defense strategies.

## Relevance to Thesis Chapters

| Chapter | Role |
|---|---|
| Chapter 5: Clinical Safety and Privacy | Anti-eavesdropping defense reference |
| Chapter 6: Software-Based Hardening | Scheduled spatial sensing as a defense method |

## Reproducibility Status

| Item | Status |
|---|---|
| Code available | Yes — https://github.com/MoWiNG-Lab/AntiEave-WiFi-Sensing |
| Tested locally | No |
| Reproduction score | Not assessed |
| Reproducibility note | Not tested in this repository |

## How This Supports the Repository

Provides a reference implementation for scheduled spatial sensing as a physical-layer privacy defense.
Useful for evaluating anti-eavesdropping strategies in WiFi sensing threat models.

## Limitations and Open Questions

- No explicit LICENSE file in upstream repository; license status is pending verification.
- Dataset uses git-lfs; actual data file availability should be verified.
- Not evaluated in a healthcare or vital-sign sensing context.

## Citation Status

```bibtex
@INPROCEEDINGS{AntiEave,
  AUTHOR={S. M. Hernandez and Eyuphan Bulut},
  TITLE={{Scheduled Spatial Sensing against Adversarial WiFi Sensing}},
  BOOKTITLE="Proceedings of the International Conference on Pervasive Computing and Communications (PerCom 2023)",
  ADDRESS="Atlanta, USA"
}
```

> Citation verified from upstream README BibTeX block.

## Last Verified

2026-05-24 — GitHub URL confirmed live; title, authors, and venue verified from upstream README.

---

*Third-party folder reference: `third_party/wifi_sensing_security/antieave_wifi_sensing/`*
*See also: `literature/papers.csv`, `literature/reproducibility_matrix.md`*
