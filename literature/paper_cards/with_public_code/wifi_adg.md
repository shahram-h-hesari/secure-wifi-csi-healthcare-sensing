# Paper Card: WiFi-ADG

## Status Summary

| Field | Value |
|---|---|
| Work type | Research project with public code |
| Code status | Public GitHub available |
| Dataset status | Pending verification |
| License status | Pending verification (no LICENSE file in upstream repo) |
| Reproducibility status | Not tested |
| Repository status | External reference only; no code copied |
| Thesis relevance | Chapter 6 defense methods; adversarial data generation for WiFi privacy |

## Official Links

| Item | URL | Status |
|---|---|---|
| GitHub repository | https://github.com/siwangzhou/WiFi-ADG | Verified live |
| Paper title | Pending verification (not provided in upstream README) | Pending |
| DOI | Pending verification | Not provided in upstream repo |

## Code and Dataset Availability

| Item | Status | Notes |
|---|---|---|
| Public code | Available | https://github.com/siwangzhou/WiFi-ADG |
| Code tested locally | No | Not tested in this repository |
| Dataset | Nine .mat files (data0.mat through data7.mat and resdata.mat) | Available via Baidu link listed in upstream README; direct access pending verification |
| Dataset license | Pending verification | No license information in upstream repo |
| License | Pending verification | No LICENSE file in upstream repo |

## Paper / Project Summary

WiFi-ADG provides Python scripts for adversarial data generation (ADG) targeting WiFi-based deep learning sensing systems.
The upstream repository contains WIFI_ADG_ae.py, WIFI_ADG_model.py, and WIFI_ADG_run.py.
The repository contact is swzhou@hnu.edu.cn; no formal citation block is provided upstream.

> **Note:** Paper title, authors, venue, and DOI are pending verification — not provided in upstream README.
> External reference only. No code, PDFs, or datasets are copied into this repository.

## Task and Modality

| Field | Value |
|---|---|
| Primary task | Adversarial data generation for WiFi sensing |
| Modality | WiFi CSI (Channel State Information) |
| Authors | Pending verification (contact: swzhou@hnu.edu.cn) |
| Year | Approximately 2017–2018 (based on commit history; not formally stated) |

## Attack / Defense / Benchmark Role

This is an **adversarial generation** project relevant to both attack and defense research.
Generates adversarial perturbations for WiFi sensing models.
Relevant to CSI privacy, behavior obfuscation, and adversarial data generation workflows.

## Relevance to Thesis Chapters

| Chapter | Role |
|---|---|
| Chapter 5: Clinical Safety and Privacy | Behavior obfuscation and privacy reference |
| Chapter 6: Software-Based Hardening | Adversarial data generation for defense testing |

## Reproducibility Status

| Item | Status |
|---|---|
| Code available | Yes — https://github.com/siwangzhou/WiFi-ADG |
| Tested locally | No |
| Reproduction score | Not assessed |
| Reproducibility note | Not tested in this repository |

## How This Supports the Repository

Provides a reference implementation for WiFi CSI adversarial data generation.
Useful for evaluating perturbation-based privacy preservation and defense pipeline design.

## Limitations and Open Questions

- Paper title, authors, venue, and DOI not confirmed from upstream README; all pending verification.
- No LICENSE file in upstream repository.
- Dataset access relies on external Baidu link; availability pending verification.
- Not validated in a healthcare or vital-sign sensing context.

## Citation Status

Citation pending verification — no formal BibTeX or paper reference found in upstream README.
Contact: swzhou@hnu.edu.cn

## Last Verified

2026-05-24 — GitHub URL confirmed live. Paper metadata (title, authors, DOI, venue) pending verification.

---

*Third-party folder reference: `third_party/wifi_sensing_security/wifi_adg/`*
*See also: `literature/papers.csv`, `literature/reproducibility_matrix.md`*
