# Paper Card: NoiSec — Unified Defense Against Adversarial and Backdoor Attacks

## Status Summary

| Field | Value |
|---|---|
| Work type | Conference paper with public code (official implementation) |
| Code status | Public GitHub available |
| Dataset status | Pending verification |
| License status | MIT (verified: LICENSE file confirmed in upstream repo) |
| Reproducibility status | Not tested |
| Repository status | External reference only; no code copied |
| Thesis relevance | Chapter 6 defense methods; noise-based unified adversarial and backdoor defense |

## Official Links

| Item | URL | Status |
|---|---|---|
| GitHub repository | https://github.com/shahriar0651/NoiSec | Verified live; MIT license confirmed |
| arXiv preprint | https://arxiv.org/abs/2406.13073 | Listed in upstream README |
| Venue | ESORICS 2025 | Verified from upstream README and BibTeX |

## Code and Dataset Availability

| Item | Status | Notes |
|---|---|---|
| Public code | Available | https://github.com/shahriar0651/NoiSec |
| Code tested locally | No | Not tested in this repository |
| WiFi CSI dataset used | CSI Activity dataset | Included in upstream repo supporting datasets; source: github.com/ludlows/CSI-Activity-Recognition |
| Dataset license | Pending verification | CSI Activity dataset license not confirmed |
| Code license | MIT | LICENSE file confirmed in upstream repo |

## Paper / Project Summary

NoiSec is a unified, attack-agnostic defense system that uses reconstruction noise (residual noise from a denoising autoencoder) combined with an anomaly detector to identify adversarial and backdoor attacks.
The upstream repository explicitly includes a WiFi CSI dataset (CSI Activity) in its supported datasets, confirming direct WiFi CSI applicability.

> **Note:** External reference only. No code, PDFs, or datasets are copied into this repository.

## Task and Modality

| Field | Value |
|---|---|
| Primary task | Unified adversarial and backdoor attack detection |
| Modality | General ML; WiFi CSI experiments included (CSI Activity dataset) |
| Title | Let the Noise Speak: Harnessing Noise for a Unified Defense Against Adversarial and Backdoor Attacks |
| Authors | Shahriar, Md Hasan; Wang, Ning; Ramakrishnan, Naren; Hou, Y. Thomas; Lou, Wenjing |
| Venue | ESORICS 2025 (Proceedings of the 30th European Symposium on Research in Computer Security) |
| Year | 2025 |

> Authors, title, and venue verified from upstream README BibTeX block.

## Attack / Defense / Benchmark Role

This is a **defense paper** with a general ML defense that includes WiFi CSI experiments.
NoiSec uses a denoising autoencoder and anomaly detection on reconstruction noise to detect adversarial and backdoor inputs.
Directly applicable to adversarial robustness for WiFi sensing systems.

## Relevance to Thesis Chapters

| Chapter | Role |
|---|---|
| Chapter 5: Clinical Safety and Privacy | Backdoor detection as a clinical safety mechanism |
| Chapter 6: Software-Based Hardening | Noise-based unified defense; adversarial and backdoor detection reference |

## Reproducibility Status

| Item | Status |
|---|---|
| Code available | Yes — https://github.com/shahriar0651/NoiSec |
| Tested locally | No |
| Reproduction score | Not assessed |
| Reproducibility note | Not tested in this repository |

## How This Supports the Repository

Provides an official implementation of a noise-based, unified defense against adversarial and backdoor attacks with verified WiFi CSI applicability.
Useful as a defense method reference and potential future implementation target for Chapter 6.

## Limitations and Open Questions

- Not yet tested in this repository.
- WiFi CSI dataset (CSI Activity) license pending verification.
- Healthcare-specific validation not yet performed.

## Citation Status

```bibtex
@inproceedings{shahriar2025noisec,
  title={Let the Noise Speak: Harnessing Noise for a Unified Defense Against Adversarial and Backdoor Attacks},
  author={Shahriar, Md Hasan and Wang, Ning and Ramakrishnan, Naren and Hou, Y. Thomas and Lou, Wenjing},
  booktitle={Proceedings of the 30th European Symposium on Research in Computer Security (ESORICS)},
  year={2025}
}
```

> Citation verified from upstream README BibTeX block.

## Last Verified

2026-05-24 — GitHub URL confirmed live; MIT LICENSE confirmed; title, authors, venue, and WiFi CSI dataset inclusion verified from upstream README.

---

*Third-party folder reference: `third_party/wifi_sensing_security/noisec/` (if present)*
*See also: `literature/papers.csv`, `literature/reproducibility_matrix.md`*
