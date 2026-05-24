# Paper Card: CsiGAN

## Status Summary

| Field | Value |
|---|---|
| Work type | Peer-reviewed journal article with public code |
| Code status | Public GitHub available |
| Dataset status | Pending verification |
| License status | Pending verification (no explicit LICENSE file in upstream repo) |
| Reproducibility status | Not tested |
| Repository status | External reference only; no code copied |
| Thesis relevance | Chapter 6 augmentation; Chapter 7 generalization baseline |

## Official Links

| Item | URL | Status |
|---|---|---|
| GitHub repository | https://github.com/ChunjingXiao/CsiGAN | Verified live |
| DOI | https://doi.org/10.1109/JIOT.2019.2936580 | Verified from upstream BibTeX |

## Code and Dataset Availability

| Item | Status | Notes |
|---|---|---|
| Public code | Available | https://github.com/ChunjingXiao/CsiGAN |
| Code tested locally | No | Not tested in this repository |
| Dataset | SignFi (external) | Available at https://github.com/yongsen/SignFi; processed data via Baidu/Google Drive links in upstream README |
| Dataset license | Pending verification | Not confirmed from upstream repo |
| License | Pending verification | No explicit LICENSE file found in upstream repo |

## Paper / Project Summary

CsiGAN proposes a semi-supervised Generative Adversarial Network (GAN) for CSI-based human activity recognition.
It addresses the performance degradation problem of leave-one-subject-out validation.
The model introduces a complement generator, extended discriminator outputs, and manifold regularization for stable training.

> **Note:** This is not a healthcare-specific work and is not an adversarial attack or defense repository.
> External reference only. No code, PDFs, or datasets are copied into this repository.

## Task and Modality

| Field | Value |
|---|---|
| Primary task | CSI-based human activity recognition |
| Modality | WiFi Channel State Information (CSI) |
| Dataset used | SignFi |
| DL approach | Semi-supervised GAN (CsiGAN) |

## Attack / Defense / Benchmark Role

This work is neither an attack nor a defense paper.
It is relevant as a **CSI data augmentation and robust recognition** reference.
Potential relevance to synthetic-to-real transfer and augmentation pipelines.

## Relevance to Thesis Chapters

| Chapter | Role |
|---|---|
| Chapter 6: Software-Based Hardening | GAN-based augmentation as a data-level defense mechanism |
| Chapter 7: Generalization | Baseline recognition performance under domain shift |

## Reproducibility Status

| Item | Status |
|---|---|
| Code available | Yes — https://github.com/ChunjingXiao/CsiGAN |
| Tested locally | No |
| Reproduction score | Not assessed |
| Reproducibility note | Not tested in this repository |

## How This Supports the Repository

Provides a reference implementation for GAN-based CSI augmentation.
Useful for understanding semi-supervised learning approaches that could improve model robustness under limited labeled data scenarios.

## Limitations and Open Questions

- No explicit license in upstream repository; license status is pending verification.
- Dataset (SignFi) external links (Baidu/Google Drive) should be verified for accessibility.
- Not evaluated on healthcare or vital-sign sensing tasks.

## Citation Status

```bibtex
@ARTICLE{CsiGAN2019,
  author={Xiao, Chunjing and Han, Daojun and Ma, Yongsen and Qin, Zhiguang},
  journal={IEEE Internet of Things Journal},
  title={CsiGAN: Robust Channel State Information-Based Activity Recognition With GANs},
  year={2019},
  volume={6},
  number={6},
  pages={10191-10204},
  doi={10.1109/JIOT.2019.2936580}
}
```

> Citation verified from upstream README BibTeX block.

## Last Verified

2026-05-24 — GitHub URL confirmed live; BibTeX and DOI verified from upstream README.

---

*Third-party folder reference: `third_party/wifi_sensing/csigan/`*
*See also: `literature/papers.csv`, `literature/reproducibility_matrix.md`*
