# Thesis Chapter Mapping

**Thesis Title:** Adversarial Attack and Software-Based Hardening of Deep Learning Wi-Fi Sensing for Vital Sign and Fall Detection in Elderly Homes with Worst-Case Clinical Safety Metrics
**Author:** Shahram H. Hesari, Portland State University
**Last Updated:** 2026-05-24

> **Disclaimer:** This project uses **synthetic CSI data only**. No real patient data, clinical validation, or real hardware deployment is claimed. The chapter mapping below reflects planned thesis contributions, not validated experimental results.

---

## Thesis Chapter Structure

| Chapter | Title | Description |
|---|---|---|
| Ch. 1 | Introduction | Motivation, problem statement, scope, thesis contributions |
| Ch. 2 | Background and Related Work | Wi-Fi CSI sensing, deep learning models, adversarial ML, security landscape |
| Ch. 3 | System Model and Baseline Evaluation | Synthetic CSI pipeline, baseline DL models, performance benchmarks |
| Ch. 4 | Adversarial Attack Framework | Threat model, attack types (FGSM, PGD, etc.), attack evaluation on Wi-Fi sensing |
| Ch. 5 | Clinical Safety Impact Analysis | Worst-case clinical safety metrics (false negatives, fall miss rates, vital sign errors) |
| Ch. 6 | Software-Based Hardening Methods | Adversarial training, input transformation, noise injection, certified defenses |
| Ch. 7 | Generalization and Reproducibility | Cross-dataset evaluation, open-source gap analysis, reproducibility evidence |
| Ch. 8 | Conclusion and Future Work | Summary, limitations, future directions |

---

## Paper-to-Chapter Evidence Map

| Paper ID | Ch. 1 | Ch. 2 | Ch. 3 | Ch. 4 | Ch. 5 | Ch. 6 | Ch. 7 | Ch. 8 | Role |
|---|---|---|---|---|---|---|---|---|---|
| attack_wifi_sensing | | | | **Primary** | | Ref | | | Primary adversarial attack reference |
| sensefi | | | **Primary** | | | | **Primary** | | Key benchmark; baseline model and generalization |
| antieave_wifi_sensing | | Ref | | | | **Primary** | | | Anti-eavesdropping defense; hardening Chapter 6 |
| wifi_adg | | Ref | | | | **Primary** | | | Adversarial defense generation; hardening Chapter 6 |
| csigan | | Ref | | | | Ref | **Primary** | | GAN augmentation; generalization and robustness |
| csi_bench | | | Ref | | | | **Primary** | | Future dataset; generalization Chapter 7 |
| noisec | | Ref | | | | **Primary** | | | Noise-based defense; hardening Chapter 6 |
| infocom_2023_wifi_ap | Ref | Ref | | **Ref** | **Primary** | | | | Physical-layer privacy risk; clinical safety Chapter 5 |
| wicam_wicam2 | **Ref** | Ref | | **Ref** | | | | | Motivation; attack model Chapter 4 |
| wiintruder | | | | | **Ref** | **Primary** | | | Universal perturbation; hardening Chapter 6 |
| awesome_ris_security | | **Ref** | | | | | **Ref** | | Background survey reference |
| unilateral_csi_entropy | | **Ref** | **Ref** | | | | **Ref** | | Entropy estimation; evaluation context |

**Key:** **Primary** = primary evidence source for this chapter; **Ref** = background/supporting reference

---

## Per-Chapter Evidence Summary

### Chapter 1: Introduction
- Motivation: `wicam_wicam2` (attack scenario), `infocom_2023_wifi_ap` (privacy risk)
- Research gap: lack of systematic adversarial robustness work for healthcare Wi-Fi sensing

### Chapter 2: Background
- Wi-Fi CSI sensing: `sensefi`, `unilateral_csi_entropy`
- Adversarial ML landscape: `attack_wifi_sensing`, `noisec`, `awesome_ris_security`
- Defense taxonomy: `antieave_wifi_sensing`, `wifi_adg`

### Chapter 3: System Model and Baseline
- Baseline models: `sensefi` (benchmark)
- Evaluation context: `unilateral_csi_entropy`, `csi_bench`

### Chapter 4: Adversarial Attacks
- Primary attack reference: `attack_wifi_sensing`
- Physical-layer attack model: `wicam_wicam2`, `infocom_2023_wifi_ap`

### Chapter 5: Clinical Safety Impact
- Physical-layer privacy risk: `infocom_2023_wifi_ap`
- Universal perturbation risk: `wiintruder`

### Chapter 6: Software-Based Hardening
- Anti-eavesdropping: `antieave_wifi_sensing`
- Adversarial defense generation: `wifi_adg`
- Noise-based defense: `noisec`
- Intrusion hardening: `wiintruder`

### Chapter 7: Generalization and Reproducibility
- Multi-dataset benchmark: `sensefi`
- Future dataset: `csi_bench`
- GAN augmentation: `csigan`
- Open-source gap: documented in `docs/open_source_gap.md`

### Chapter 8: Conclusion
- All papers contribute to open problems and future work narrative

---

*This document is cross-referenced by `papers.csv` (thesis_chapters column). Update both files together.*
