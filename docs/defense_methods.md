# Defense Methods

> **Important note:** This document describes simple synthetic prototype defenses applied to synthetic CSI-like data only. No real physical-layer defense has been implemented. No real WiFi hardware is used. No clinical validation or validated security protection is included. All results are prototype outputs intended for research-methodology demonstration only.

## Purpose

This document explains the motivation and methodology for simple defense and robustness-hardening methods in the WiFi CSI Fall Detection Research Prototype. The goal is to evaluate whether basic preprocessing defenses can reduce the effect of synthetic perturbations on the baseline fall-detection classifier, and to measure any improvement using both ML metrics and clinical-safety-aware metrics such as missed falls and false alarms.

This work supports the PhD research direction of developing secure and robust WiFi CSI sensing systems for healthcare-oriented applications.

## Why Defenses Are Needed

WiFi CSI-based sensing systems are exposed to multiple sources of signal degradation:

- **Noise and interference**: Background RF noise, co-channel interference, and multipath effects can corrupt CSI amplitude and phase measurements.
- **Adversarial perturbations**: A motivated attacker may inject signals or manipulate the wireless channel to degrade sensing performance.
- **Hardware imperfections**: Calibration drift, phase offsets, and subcarrier-level noise can introduce systematic distortions.
- **Distribution shift**: A model trained in one environment may encounter signal statistics not seen during training.

Without any defense, even modest perturbations can increase missed falls and false alarms, degrading the safety profile of the system. Simple preprocessing defenses provide a first-line hardening layer that may reduce perturbation impact before signals reach the classifier.

> **Important:** Simple preprocessing defenses are not complete security solutions. They do not guarantee robustness against adaptive adversaries or real-world physical-layer attacks. They are evaluated here as baseline hardening methods only.

## Current Defense Scope

This repository implements the following simple preprocessing defenses for synthetic CSI-like data:

| Defense | Type | Purpose |
|---|---|---|
| Moving average smoothing | Time-domain filtering | Reduces high-frequency noise |
| Median filtering | Robust filtering | Reduces spike-like burst perturbations |
| Outlier clipping | Statistical thresholding | Limits extreme values |
| Robust normalization | Robust scaling | Reduces the effect of outliers on normalization |
| Perturbation-aware augmentation | Training data augmentation | Prepares model for future robust training |

All defenses are applied to the synthetic feature-level representation of CSI-like signals. No signal-level or RF-level defense is implemented.

## Preprocessing-Based Defenses

### Moving Average Smoothing

- **Description**: Applies a sliding-window mean filter along each feature dimension across the sample axis.
- **Purpose**: Reduces the effect of high-frequency Gaussian noise perturbations on the feature distribution.
- **Limitation**: Cannot remove large burst perturbations or structured adversarial perturbations.
- **Implementation**: `src/defenses.py` → `moving_average_defense()`

### Median Filtering

- **Description**: Applies a median filter along each feature dimension across the sample axis.
- **Purpose**: Robust to spike-like outliers and burst perturbations; preserves edges better than mean filtering.
- **Limitation**: Computationally more expensive than mean filtering; may blur step-change signals.
- **Implementation**: `src/defenses.py` → `median_filter_defense()`

### Outlier Clipping

- **Description**: Clips feature values to a configurable range defined by percentile thresholds or standard-deviation bounds.
- **Purpose**: Prevents extreme perturbation values from dominating the feature space.
- **Limitation**: May discard genuine extreme values if thresholds are too tight.
- **Implementation**: `src/defenses.py` → `clip_outliers()`

### Robust Normalization

- **Description**: Normalizes features using median and interquartile range (IQR) instead of mean and standard deviation.
- **Purpose**: Standard normalization is sensitive to outliers; robust normalization reduces their effect.
- **Limitation**: Does not remove perturbations, only reduces their relative scale.
- **Implementation**: `src/defenses.py` → `robust_normalize()`

## Robust Feature Extraction

In a real WiFi CSI sensing system, robust feature extraction choices — such as using median amplitude instead of mean amplitude, or applying wavelet denoising — can reduce the sensitivity of downstream classifiers to perturbations. In the current synthetic prototype, feature-level defenses are applied to the already-extracted feature matrix, as a proxy for feature-level robustness.

Future extensions should evaluate defense effectiveness at the raw CSI signal level using real hardware.

## Perturbation-Aware Training

Perturbation-aware training (also called adversarial training in the machine learning literature) involves augmenting the training dataset with perturbed examples so that the trained classifier learns to be robust to expected perturbations.

In this repository, `augment_with_perturbations()` provides a simple prototype of this concept by generating a combined dataset of clean and perturbed synthetic samples. Full adversarial training is not yet implemented and is identified as future work.

## Connection to Clinical-Safety Metrics

Defense quality is evaluated not only using standard ML metrics but also using clinical-safety-aware metrics:

| Defense Effect | Safety Metric Impact |
|---|---|
| Reduced false negatives after defense | Lower missed fall rate |
| Reduced false positives after defense | Lower false alarm rate |
| No improvement | Defense insufficient for this perturbation type |
| Worse performance after defense | Over-smoothing or over-clipping effect |

> **Disclaimer:** These safety-metric connections are evaluated using synthetic data only. They do not represent clinical outcomes or validated healthcare performance.

## Current Repository Status

| Component | Status |
|---|---|
| Preprocessing defense functions | Implemented (`src/defenses.py`) |
| Clean vs perturbed vs defended comparison | Implemented (notebook Section 17) |
| ML metrics for all three conditions | Implemented (notebook Section 17) |
| Safety metrics for all three conditions | Implemented (notebook Section 17) |
| Defense results summary | Saved to `results/defense_methods_summary.md` |
| Perturbation-aware augmentation prototype | Implemented (`src/defenses.py`) |
| Full adversarial training | Not implemented (future work) |
| Certified robustness | Not implemented (future work) |
| Real physical-layer defense | Not implemented (future work) |
| Clinical defense validation | Not implemented (future work) |

## Limitations

- All defenses are synthetic. They operate on synthetic CSI-like features, not on real WiFi CSI measurements.
- Preprocessing defenses are not designed to resist adaptive adversaries. An attacker with knowledge of the defense strategy could likely circumvent these methods.
- The evaluation is performed using a simple Random Forest classifier on synthetic data. Results may not generalize to deep learning models or real hardware.
- No formal security guarantee (such as certified robustness) is provided.
- Results should not be interpreted as evidence of real-world defense effectiveness, clinical safety improvement, or hardware-validated performance.

## Future Extensions

- Implement adversarial training using perturbed synthetic samples.
- Evaluate randomized smoothing as a certifiable defense.
- Apply defenses to raw synthetic CSI-like time-series signals instead of extracted features.
- Evaluate defense effectiveness against adaptive perturbations.
- Collect real CSI measurements and evaluate hardware-level defense effectiveness.
- Connect defense evaluation to detection delay metrics.
- Extend to federated learning settings where Byzantine-robust aggregation serves as a defense.
- Evaluate defenses under WiFi 7 multi-link operation scenarios.

---

*This document is part of the WiFi CSI Fall Detection Research Prototype. All content is intended for academic research and prototype demonstration purposes only.*
