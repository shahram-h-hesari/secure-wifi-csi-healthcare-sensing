# Project Status

> **Important note:** This document reflects the current status of the WiFi CSI Fall Detection Research Prototype. This repository uses synthetic CSI-like data only. No real WiFi CSI hardware, clinical data, or medical-grade validation is included.

## Purpose

This document provides a transparent, up-to-date record of what the repository contains, what has been implemented, what is planned, and what is explicitly not claimed. It is intended for PhD committee members, collaborators, recruiters, and GitHub visitors.

## Current Status Summary

**Current phase:** Phase 9 - GitHub Polish and LinkedIn-Ready Presentation

**Repository type:** Research prototype (synthetic data only)

**Research affiliation:** Portland State University, PhD research in Electrical Engineering and Computer Science

**Key research focus:** Secure WiFi CSI sensing, fall detection, clinical-safety-aware evaluation, adversarial robustness, and defense methods

## Component Status Table

| Component | Status | Evidence | Notes |
|---|---|---|---|
| Synthetic CSI-like data generation | Completed | `src/simulate_csi.py`, notebook | Synthetic signals only |
| Notebook prototype pipeline | Completed | `notebooks/01_csi_signal_exploration.ipynb` | 1200+ lines, runs top to bottom |
| CSI amplitude and phase visualization | Completed | Notebook, `app.py` | Matplotlib and Streamlit |
| Normal vs fall-like event simulation | Completed | Notebook, `app.py` | Synthetic event model |
| Signal preprocessing | Completed | `src/preprocessing.py` | Smoothing, normalization |
| Feature extraction | Completed | `src/features.py` | Statistical features |
| Baseline Random Forest classifier | Completed | `src/baseline_model.py`, notebook | Synthetic data only |
| Clinical-safety-aware metrics | Completed | `src/clinical_metrics.py`, `results/clinical_safety_summary.md` | Missed falls, false alarms, rates |
| Adversarial robustness stress testing | Completed | `src/adversarial.py`, `results/adversarial_robustness_summary.md` | Synthetic perturbations only |
| Defense and robustness hardening | Completed | `src/defenses.py`, `results/defense_methods_summary.md` | Preprocessing defenses only |
| Streamlit interactive dashboard | Completed | `app.py` | `streamlit run app.py` |
| Documentation suite | Completed | `docs/` directory | 9+ documentation files |
| Threat model | Completed | `docs/threat_model.md` | Conceptual, not hardware-validated |
| References and third-party notices | Completed | `references.md`, `THIRD_PARTY_NOTICES.md` | Academic and OSS attributions |
| Real CSI hardware dataset | Not yet implemented | N/A | Planned future work |
| Hardware deployment | Not implemented | N/A | Future work |
| Clinical validation | Not implemented | N/A | Not claimed |
| Medical-grade performance | Not implemented | N/A | Not claimed |
| Real physical-layer attack defense | Not implemented | N/A | Future work |
| Certified robustness | Not implemented | N/A | Future work |

## Completed Components

### Phase 1-4: Synthetic Pipeline Foundation
- Synthetic CSI-like signal generation with configurable parameters
- Normal activity and fall-like event simulation
- Signal preprocessing: moving average, standard normalization
- Feature extraction: mean, std, energy, peak-to-peak range, max, min, variance
- Baseline Random Forest classifier with standard ML metrics
- End-to-end Jupyter notebook prototype

### Phase 5: Clinical-Safety-Aware Evaluation
- Missed fall count and missed fall rate
- False alarm count and false alarm rate
- Alarm fatigue indicator
- Results saved to `results/clinical_safety_summary.md`

### Phase 6: Adversarial Robustness Stress Testing
- Random noise perturbation
- Burst perturbation
- Subcarrier-level perturbation
- Clean vs perturbed ML metrics and safety metrics
- Results saved to `results/adversarial_robustness_summary.md`

### Phase 7: Defense Methods and Robustness Hardening
- Moving average smoothing defense
- Median filter defense
- Outlier clipping
- Robust normalization (median/IQR)
- Perturbation-aware augmentation prototype
- Clean vs perturbed vs defended comparison
- Results saved to `results/defense_methods_summary.md`

### Phase 8: Streamlit Demo Dashboard
- Interactive Streamlit dashboard (`app.py`)
- Sidebar controls for signal parameters, noise, perturbation, defense
- Full pipeline visualization from synthetic CSI generation to defense comparison

### Phase 9: GitHub Polish and LinkedIn-Ready Presentation
- Polished README with badges, highlights table, quick start, roadmap
- Project status documentation (this file)
- LinkedIn summary documentation
- Dashboard documentation
- Screenshot placeholder for future local testing

## Future Work

- Collect real WiFi CSI measurements using hardware (e.g., Intel 5300, Nexmon, ESP32)
- Evaluate pipeline performance on real CSI datasets
- Implement adversarial training for improved robustness
- Evaluate certified robustness methods (e.g., randomized smoothing)
- Extend to deep learning models (CNN, LSTM, Transformer)
- Evaluate federated learning models under Byzantine robustness constraints
- Connect detection delay metrics to safety-aware evaluation
- Explore WiFi 7 multi-link operation security implications
- Pursue hardware deployment in a controlled research environment
- Seek IRB approval and conduct clinical feasibility studies (long-term)

## Not Claimed

This repository **does not** claim any of the following:

- Real WiFi CSI hardware validation
- Clinical validation of fall detection performance
- Medical-grade accuracy or sensitivity
- Validated security protection against real physical-layer attacks
- Hardware deployment readiness
- Regulatory compliance (e.g., FDA, CE)
- Patient safety guarantees

---

*This document is part of the WiFi CSI Fall Detection Research Prototype. Last updated: Phase 9.*


---

## Update Log — 2026-05-24

### New Third-Party Repository References Added

Four new external GitHub repositories have been added to `third_party/` as tracking placeholders and attribution notes:

| Folder | Repository | Category | License |
|---|---|---|---|
| `third_party/wifi_sensing_security/goop_veil/` | [goop-veil](https://github.com/kobepaw/goop-veil) | WiFi Sensing Security / Privacy Defense | Apache-2.0 |
| `third_party/wifi_sensing/wifi_csi_human_pose_detection/` | [WiFi-CSI-Human-Pose-Detection](https://github.com/euaziel/WiFi-CSI-Human-Pose-Detection) | WiFi CSI Sensing / Pose / Domain Generalization | GPL-3.0 |
| `third_party/wifi_sensing/mowa_wifi_sensing/` | [mowa-wifi-sensing](https://github.com/oss-inc/mowa-wifi-sensing) | WiFi CSI HAR / Fall Detection Baseline | BSD-3-Clause |
| `third_party/wifi_sensing/baby_monitor_wifi_csi/` | [baby-monitor-wifi-csi](https://github.com/mohosy/baby-monitor-wifi-csi) | WiFi CSI Breathing / Apnea Sensing Baseline | MIT |

### Status of New Additions

- **These newly added third-party repos are external references only.** No code, binaries, or dataset files have been copied.
- **No new external code has been used in the current project implementation.** The project continues to use synthetic CSI-like data only.
- **No new real-data validation has been performed.** The current implementation status is unchanged.
- **Healthcare-specific adversarial WiFi CSI GitHub code remains limited or not publicly confirmed** beyond the currently tracked repositories (`attack_wifi_sensing`, `awesome_ws_security`, `antieave_wifi_sensing`, `wifi_adg`, `goop_veil`).
- **Four new candidate dataset entries** have been added to `datasets/future_datasets/README.md` and `datasets/dataset_catalog.md` for future verification. No datasets have been downloaded or integrated.
- **Updated files:** `third_party/README.md`, `THIRD_PARTY_NOTICES.md`, `docs/related_projects.md`, `datasets/future_datasets/README.md`, `datasets/dataset_catalog.md`, `README.md`, `references.md`, `docs/project_status.md`, `docs/roadmap.md`.

---

*Last updated: 2026-05-24*


---

## Update Log — 2026-05-24 (Second-Pass Research Update)

### CsiGAN Added as External Reference

- `third_party/wifi_sensing/csigan/` added — CsiGAN (Chunjing Xiao et al., IEEE IoT Journal 2019): semi-supervised GAN for robust WiFi CSI activity recognition and data augmentation.
- **Status:** External reference only. No code copied. License pending verification (no LICENSE file in upstream repo).
- **Use:** Not used in current project implementation. Candidate for future robustness/augmentation experiments.

### No New External Code or Datasets Copied

- No source code from any external repository was copied into this project.
- No datasets were downloaded or integrated.
- No new real-data validation was performed.
- The project continues to use **synthetic CSI-like data only**.

### Open-Source Gap Confirmed

- A second-pass search confirmed: **no additional healthcare-specific adversarial WiFi CSI GitHub repository was found** beyond the currently tracked references.
- The most directly relevant paper-only work (INFOCOM 2023 apnea attack/defense) has no confirmed public GitHub implementation.
- Existing public repositories primarily cover general WiFi CSI sensing, activity recognition, privacy defense, or non-healthcare adversarial WiFi sensing — not the specific combination of healthcare sensing + adversarial evaluation + clinical safety metrics targeted by this thesis.
- The `device-classification-5g` repository identified in the second-pass search was **not added** — it is 5G RF fingerprinting, not WiFi CSI healthcare sensing.

### Updated Files

- `third_party/wifi_sensing/csigan/README.md` (new)
- `third_party/README.md`
- `THIRD_PARTY_NOTICES.md`
- `docs/related_projects.md`
- `datasets/future_datasets/README.md`
- `datasets/dataset_catalog.md`
- `README.md`
- `references.md`
- `docs/project_status.md`
- `docs/roadmap.md`

---

*Last updated: 2026-05-24*
