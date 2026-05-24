# Paper Card: SenseFi — WiFi CSI Sensing Benchmark

## Status Summary

| Field | Value |
|---|---|
| Work type | Peer-reviewed paper with public benchmark library |
| Code status | Public GitHub available |
| Dataset status | Pending verification |
| License status | Pending verification |
| Reproducibility status | Not tested |
| Repository status | External reference only; no code copied |
| Thesis relevance | Chapter 3 baseline models; Chapter 7 generalization |

## Official Links

| Item | URL | Status |
|---|---|---|
| GitHub repository | https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark | Verified live |
| Paper (arXiv) | https://arxiv.org/abs/2207.07859 | Cited in upstream README |
| DOI | https://doi.org/10.1016/j.patter.2023.100764 | Cited in upstream README |

## Code and Dataset Availability

| Item | Status | Notes |
|---|---|---|
| Public code | Available | https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark |
| Code tested locally | No | Not tested in this repository |
| Datasets referenced | NTU-Fi-HAR, NTU-Fi-HumanID, UT-HAR, Widardata | Listed in upstream README; download via Google Drive links |
| Dataset license | Pending verification | Individual dataset licenses not confirmed |
| Library license | Pending verification | License badge in upstream README links to a different repository (Marsrocky/Awesome-WiFi-CSI-Sensing); xyanchen repo license pending direct verification |

## Paper / Project Summary

SenseFi is the first open-source benchmark and library for WiFi CSI human sensing, implemented in PyTorch.
It evaluates state-of-the-art networks (MLP, CNN, RNN, Transformers) on four public datasets across different WiFi CSI platforms.

> **Note:** External reference only. No code, PDFs, or datasets are copied into this repository.

## Task and Modality

| Field | Value |
|---|---|
| Primary task | WiFi CSI human sensing benchmark |
| Modality | WiFi Channel State Information (CSI) |
| Title | SenseFi: A Library and Benchmark on Deep-Learning-Empowered WiFi Human Sensing |
| Authors | Yang, Jianfei; Chen, Xinyan; Wang, Dazhuo; Zou, Han; Lu, Chris Xiaoxuan; Sun, Sumei; Xie, Lihua |
| Journal | Patterns (Cell Press), Volume 4, Number 3, 2023 |
| Datasets | NTU-Fi-HAR, NTU-Fi-HumanID, UT-HAR, Widardata |

> Authors and metadata verified from upstream README BibTeX block.

## Attack / Defense / Benchmark Role

This is a **benchmark and library** project.
Not an adversarial attack or defense work.
Provides standardized baselines for WiFi CSI human sensing across multiple datasets and architectures.

## Relevance to Thesis Chapters

| Chapter | Role |
|---|---|
| Chapter 3: Background and Dataset Selection | Key benchmark library; public multi-dataset reference |
| Chapter 7: Generalization and Evaluation | Generalization evaluation across multiple CSI platforms |

## Reproducibility Status

| Item | Status |
|---|---|
| Code available | Yes — https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark |
| Tested locally | No |
| Reproduction score | Not assessed |
| Reproducibility note | Not tested in this repository |

## How This Supports the Repository

Provides standardized benchmark baselines and public dataset references for WiFi CSI human sensing.
Useful for evaluating model generalization across different sensing environments and hardware configurations.

## Limitations and Open Questions

- License status pending direct verification (upstream license badge points to a different repository).
- Dataset download requires Google Drive access; availability should be verified.
- Not evaluated on adversarial or healthcare-specific tasks.

## Citation Status

```bibtex
@article{yang2023benchmark,
  title={SenseFi: A Library and Benchmark on Deep-Learning-Empowered WiFi Human Sensing},
  author={Yang, Jianfei and Chen, Xinyan and Wang, Dazhuo and Zou, Han and Lu, Chris Xiaoxuan and Sun, Sumei and Xie, Lihua},
  journal={Patterns},
  volume={4},
  number={3},
  publisher={Elsevier},
  year={2023}
}
```

> Citation verified from upstream README BibTeX block.

## Last Verified

2026-05-24 — GitHub URL confirmed live; title, authors, and venue verified from upstream README.

---

*Third-party folder reference: `third_party/wifi_sensing/sensefi/`*
*See also: `literature/papers.csv`, `literature/reproducibility_matrix.md`*
