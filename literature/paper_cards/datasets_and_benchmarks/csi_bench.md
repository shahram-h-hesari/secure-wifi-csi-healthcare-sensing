# Paper Card: CSI-Bench — Real-World WiFi Sensing Benchmark

## Status Summary

| Field | Value |
|---|---|
| Work type | Benchmark dataset and code repository |
| Code status | Public GitHub available / benchmark repository available |
| Dataset status | Candidate dataset; pending verification |
| License status | MIT (verified: LICENSE file present in upstream repo) |
| Reproducibility status | Not tested |
| Repository status | External reference only; no code or data copied |
| Thesis relevance | Chapter 3 dataset selection; Chapter 7 cross-environment generalization |

## Official Links

| Item | URL | Status |
|---|---|---|
| GitHub repository | https://github.com/guozhen-jenn-zhu/CSI-Bench-Real-WiFi-Sensing-Benchmark | Verified live; MIT license confirmed |
| arXiv preprint | https://arxiv.org/abs/2505.21866 | Listed in upstream README |
| Dataset (Kaggle) | https://www.kaggle.com/datasets/guozhenjennzhu/csi-bench | Listed in upstream README |

## Code and Dataset Availability

| Item | Status | Notes |
|---|---|---|
| Public code | Available | https://github.com/guozhen-jenn-zhu/CSI-Bench-Real-WiFi-Sensing-Benchmark |
| Code tested locally | No | Not tested in this repository |
| Dataset | Candidate; pending verification | Available on Kaggle per upstream README; actual structure and size pending verification |
| Dataset license | Pending verification | Dataset license separate from code license; not explicitly stated |
| Library license | MIT | LICENSE file confirmed in upstream repo |

## Paper / Project Summary

CSI-Bench is a large-scale, in-the-wild dataset for multi-task WiFi sensing.
It covers multiple sensing tasks including human activity recognition, fall detection, breathing detection, localization, and more.
Data is organized by environment folders with recordings from specific environments, devices, and users.

> **Note:** This benchmark has not been downloaded, integrated, used for training, used for validation, or clinically validated in this repository.
> External reference only. No code, datasets, or PDFs are copied into this repository.

## Task and Modality

| Field | Value |
|---|---|
| Primary task | Multi-task WiFi sensing benchmark |
| Modality | WiFi CSI (Channel State Information) |
| Title | CSI-Bench: A large-scale in-the-wild dataset for multi-task WiFi sensing |
| Authors | Zhu, Guozhen; Hu, Yuqian; Gao, Weihang; Wang, Wei-Hsiang; Wang, Beibei; Liu, K. |
| Venue | Advances in Neural Information Processing Systems (NeurIPS 2025) |
| Year | 2026 |
| Tasks covered | HAR, Fall Detection, Breathing Detection, Localization, Proximity Recognition, Motion Source Recognition, Human Identification |

> Authors, venue, and title verified from upstream README BibTeX block.

## Attack / Defense / Benchmark Role

This is a **benchmark dataset** project.
Not an adversarial attack or defense work.
Provides real-world, multi-task WiFi sensing data for benchmarking across diverse environments.

## Relevance to Thesis Chapters

| Chapter | Role |
|---|---|
| Chapter 3: Background and Dataset Selection | High-priority future dataset candidate for real-world sensing evaluation |
| Chapter 7: Generalization and Evaluation | Cross-environment and multi-task generalization evaluation |

## Reproducibility Status

| Item | Status |
|---|---|
| Code available | Yes — https://github.com/guozhen-jenn-zhu/CSI-Bench-Real-WiFi-Sensing-Benchmark |
| Tested locally | No |
| Reproduction score | Not assessed |
| Reproducibility note | Not used for training, validation, or benchmarking in this repository |

## How This Supports the Repository

Provides a real-world, multi-environment WiFi sensing dataset candidate for potential future use in cross-environment evaluation.
Particularly relevant for fall detection and vital-sign sensing generalization studies.

## Limitations and Open Questions

- Dataset must be downloaded from Kaggle; access and structure pending verification.
- Dataset license (as distinct from code license) not explicitly stated in upstream repo.
- Clinical relevance and healthcare-specific validation not yet assessed.
- Paper under review/recently published; long-term availability of Kaggle dataset pending.

## Citation Status

```bibtex
@article{zhu2026csi,
  title={CSI-Bench: A large-scale in-the-wild dataset for multi-task WiFi sensing},
  author={Zhu, Guozhen and Hu, Yuqian and Gao, Weihang and Wang, Wei-Hsiang and Wang, Beibei and Liu, K},
  journal={Advances in Neural Information Processing Systems},
  volume={38},
  year={2026}
}
```

> Citation verified from upstream README BibTeX block.

## Last Verified

2026-05-24 — GitHub URL confirmed live; MIT LICENSE file confirmed; title, authors, and venue verified from upstream README.

---

*See also: `literature/papers.csv`, `literature/reproducibility_matrix.md`*
