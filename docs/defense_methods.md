# Defense Methods — Secure WiFi CSI Healthcare Sensing Research Prototype

> **Important note:** This document describes simple synthetic prototype defenses applied to **synthetic CSI-like data only**. No real physical-layer defense has been implemented. No real WiFi hardware is used. No clinical validation or validated security protection is included. All results are prototype outputs intended for research-methodology demonstration only.

> **Project identity note:** This document is part of the **Secure WiFi CSI Healthcare Sensing** research prototype. The current implemented prototype task is **fall detection** using synthetic data. Broader healthcare sensing tasks (vital-sign monitoring, apnea detection, respiration, HR/RR) are part of the long-term thesis direction.

---

## Purpose

This document explains the motivation and methodology for defense and robustness-hardening methods in the **Secure WiFi CSI Healthcare Sensing** research prototype. The current focus is to evaluate whether basic preprocessing defenses can reduce the effect of synthetic perturbations on the baseline fall-detection classifier, and to measure improvement using both ML metrics and clinical-safety-aware metrics such as missed falls and false alarms.

This work supports the PhD research direction of developing secure and robust WiFi CSI sensing systems for healthcare-oriented applications.

The long-term thesis goal is **software-only hardening calibrated to clinical-safety endpoints** — ensuring that adversarial attacks on WiFi CSI sensing systems do not lead to clinically unsafe outcomes such as suppressed fall alarms or missed apnea events.

---

## Why Defenses Are Needed

WiFi CSI-based sensing systems are exposed to multiple sources of signal degradation:

- **Noise and interference:** Background RF noise, co-channel interference, and multipath effects can corrupt CSI amplitude and phase measurements.
- **Adversarial perturbations:** A motivated attacker may inject signals or manipulate the wireless channel to degrade sensing performance.
- **Hardware imperfections:** Calibration drift, phase offsets, and subcarrier-level noise can introduce systematic distortions.
- **Clinical-safety stakes:** In healthcare applications, missed fall alarms or false positives carry direct patient-safety consequences — not merely accuracy costs.

---

## Defense Taxonomy (Two-Layer)

Defenses are organized into two layers:

### Layer 1: Preprocessing / Signal-Level Defenses

These methods operate on the raw CSI signal before feature extraction and classification:

| Method | Type | Description | Status |
|--------|------|-------------|--------|
| Moving average smoothing | Signal filtering | Reduces high-frequency noise perturbations in time-domain CSI | Implemented |
| Median filtering | Robust filtering | Reduces spike-like burst perturbations | Implemented |
| Outlier clipping | Statistical thresholding | Limits extreme perturbation values | Implemented |
| Robust normalization | Robust scaling | Reduces outlier effect during normalization | Implemented |
| Wavelet denoising | Advanced filtering | Multi-resolution noise removal (reference method) | Future work |
| Noise injection defense (NoiSec-style) | Signal obfuscation | Adds calibrated noise to prevent CSI eavesdropping and adversarial sensing | External reference only |
| Physical-layer shaping | RIS / antenna control | Reconfigures physical-layer signal to degrade attacker CSI quality | External reference only |

### Layer 2: Model-Level / Adversarial Training Defenses

These methods operate at the ML model layer:

| Method | Type | Description | Status |
|--------|------|-------------|--------|
| Perturbation-aware augmentation | Adversarial training | Prototype adversarial training via training data augmentation | Implemented |
| Adversarial training (PGD-style) | Adversarial training | Full projected gradient descent adversarial training (reference method) | Future work |
| Certified robustness (randomized smoothing) | Certified defense | Probabilistic guarantee of robustness to bounded perturbations | Future work |
| Ensemble defenses | Model diversity | Multiple diverse models to reduce adversarial transfer | Future work |

---

## Tier 1: Implemented Baseline Defenses

The following methods are implemented in `src/defenses.py` to provide a first-line hardening layer:

- **Moving average smoothing:** Time-domain filtering used to reduce high-frequency noise perturbations.
- **Median filtering:** Robust filtering used to reduce spike-like burst perturbations.
- **Outlier clipping:** Statistical thresholding used to limit extreme perturbation values.
- **Robust normalization:** Robust scaling used to reduce the effect of outliers during data normalization.
- **Perturbation-aware augmentation:** A prototype for adversarial training concepts, applied via training data augmentation.

**All Tier 1 defenses are evaluated against synthetic perturbations only. No real-world attack validation has been performed.**

---

## Tier 2: External Reference Methods (Not Implemented)

The following methods are referenced from academic literature and third-party repositories for future planning. **No external code has been copied into this repository.**

### Noise-Based Signal Obfuscation

- **NoiSec** (external reference): Noise-injection and signal obfuscation techniques for preventing CSI eavesdropping and adversarial WiFi sensing.
  - Source: `third_party/wifi_sensing_security/noisec/`
  - Relevance: Defense taxonomy reference for noise-injection layer
  - License: Pending verification
  - Status: External reference only; no code copied

### Physical-Layer Attack Defenses (RIS Security)

- **Awesome-RIS-Security** (external reference): Literature tracker for reconfigurable intelligent surface (RIS) physical-layer attacks and defenses. Covers beam-forming manipulation, channel spoofing, and physical-layer shaping defenses.
  - Source: `third_party/wifi_sensing_security/awesome_ris_security/`
  - Relevance: Physical-layer attack literature for threat model expansion
  - License: Pending verification
  - Status: External reference only; literature aggregator

### CSI Entropy and Edge Security

- **unilateral-csi-entropy** (external reference): CSI-based entropy analysis for edge security and cryptographic key generation from channel variation.
  - Source: `third_party/wifi_sensing_security/unilateral_csi_entropy/`
  - Relevance: Cryptographic entropy reference for CSI-layer security discussion
  - License: Pending verification
  - Status: External reference only; no code copied

### Anti-Eavesdropping Defenses

- **AntiEave-WiFi-Sensing** (external reference): Scheduled spatial sensing against adversarial WiFi sensing and eavesdropping (IEEE PerCom 2023).
  - Source: `third_party/wifi_sensing_security/antieave_wifi_sensing/`
  - Relevance: Defense mechanism reference for privacy-preserving WiFi sensing
  - Status: External reference only; no code copied

### Adversarial Training References

- **Attack\_WiFi\_Sensing** (external reference): Adversarial training and universal perturbation techniques for WiFi sensing models.
  - Source: `third_party/wifi_sensing_security/attack_wifi_sensing/`
  - Relevance: Core adversarial reference for defense evaluation methodology
  - Status: External reference only; no code copied

---

## Clinical-Safety Defense Evaluation

In the context of healthcare sensing, defense effectiveness is evaluated not only on ML metrics (accuracy, F1) but also on **clinical-safety metrics**:

| Metric | Defense Goal | Why It Matters |
|--------|-------------|----------------|
| Missed fall rate (under attack) | Minimize increase | Missed falls = direct patient safety risk |
| False alarm rate (under attack) | Minimize increase | False alarms = alarm fatigue, care burden |
| Fall detection recovery (post-defense) | Maximize | Defenses should restore safety-critical performance |
| F1 score degradation | Minimize | General ML robustness indicator |

See [`docs/clinical_safety_metrics.md`](clinical_safety_metrics.md) for the full clinical-safety evaluation framework.

---

## Important Caveats

- **Prototype Limitations:** These defenses are evaluated as baseline hardening only; they are not complete security solutions and do not guarantee robustness against real-world physical-layer attacks or adaptive adversaries.
- **Data Scope:** Methods are currently only applied to synthetic CSI data; no real WiFi hardware or clinical validation has been utilized.
- **External References:** Tier 2 methods are external references only. No third-party code has been copied. All are documented in [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md).
- **Open-Source Gap:** No existing public repository fully combines WiFi CSI healthcare sensing with this defense taxonomy. See [`docs/open_source_gap.md`](open_source_gap.md) for the full landscape analysis.

---

*Maintained as part of the Secure WiFi CSI Healthcare Sensing research prototype at Portland State University.*
