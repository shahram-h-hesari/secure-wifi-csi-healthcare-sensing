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
