# Defense Methods — Secure WiFi CSI Healthcare Sensing Research Prototype

> **Important note:** This document describes simple synthetic prototype defenses applied to **synthetic CSI-like data only**. No real physical-layer defense has been implemented. No real WiFi hardware is used. No clinical validation or validated security protection is included. All results are prototype outputs intended for research-methodology demonstration only.

> **Project identity note:** This document is part of the **Secure WiFi CSI Healthcare Sensing** research prototype. The current implemented prototype task is **fall detection** using synthetic data. Broader healthcare sensing tasks (vital-sign monitoring, apnea detection, respiration, HR/RR) are part of the long-term thesis direction.

## Purpose

This document explains the motivation and methodology for defense and robustness-hardening methods in the **Secure WiFi CSI Healthcare Sensing** research prototype. The current focus is to evaluate whether basic preprocessing defenses can reduce the effect of synthetic perturbations on the baseline fall-detection classifier, and to measure improvement using both ML metrics and clinical-safety-aware metrics such as missed falls and false alarms.

This work supports the PhD research direction of developing secure and robust WiFi CSI sensing systems for healthcare-oriented applications.

The long-term thesis goal is **software-only hardening calibrated to clinical-safety endpoints** — ensuring that adversarial attacks on WiFi CSI sensing systems do not lead to clinically unsafe outcomes such as suppressed fall alarms or missed apnea events.

---

## Why Defenses Are Needed

WiFi CSI-based sensing systems are exposed to multiple sources of signal degradation:

- **Noise and interference**: Background RF noise, co-channel interference, and multipath effects can corrupt CSI amplitude and phase measurements.
- **Adversarial perturbations**: A motivated attacker may inject signals or manipulate the wireless channel to degrade sensing performance.
- **Hardware imperfections**: Calibration drift, phase offsets, and subcarrier-level noise can introduce systematic distortions.
- **Distribution shift**: A model trained in one environment may encounter signal statistics not seen during training.

Without any defense, even modest perturbations can increase missed falls and false alarms, degrading the safety profile of the system. Simple preprocessing defenses provide a first-line hardening layer that may reduce perturbation impact before signals reach the classifier.

> **Important:** Simple preprocessing defenses are not complete security solutions. They do not guarantee robustness against adaptive adversaries or real-world physical-layer attacks. They are evaluated here as baseline hardening methods only.

---

## Defense Taxonomy: Implemented, External References, and Future Work

This section organizes defense methods into three tiers based on current implementation status.

### Tier 1: Implemented in Current Prototype

These defenses are **implemented** in `src/defenses.py` and evaluated on synthetic CSI-like data. They are baseline hardening only and do not represent complete security solutions.

| Defense | Type | Implementation | Notes |
|---------|------|---------------|-------|
| Moving average smoothing | Time-domain filtering | `moving_average_defense()` | Reduces high-frequency noise perturbations |
| Median filtering | Robust filtering | `median_filter_defense()` | Reduces spike-like burst perturbations |
| Outlier clipping | Statistical thresholding | `clip_outliers()` | Limits extreme perturbation values |
| Robust normalization | Robust scaling | `robust_normalize()` | Reduces outlier effect on normalization |
| Perturbation-aware augmentation | Training data augmentation | `augment_with_perturbations()` | Prototype for adversarial training concept |

### Tier 2: External References Only

These defense families are referenced from related third-party repositories and academic literature. **No external code has been copied into this repository.** These are cited for literature context and future work planning only.

| Defense Family | Source / Reference | Relevance to Thesis |
|---------------|-------------------|---------------------|
| Adversarial training / evasion robustness | Attack_WiFi_Sensing | FGSM/PGD-trained models; robustness evaluation for WiFi sensing |
| Anti-eavesdropping / scheduled spatial sensing | AntiEave-WiFi-Sensing | Defense mechanism against adversarial WiFi sensing; privacy-preserving scheduled sensing |
| Adversarial data generation for privacy | WiFi-ADG | CSI data transformation; behavior obfuscation for privacy preservation |
| Router-side privacy mitigation | goop-veil | CSI surveillance detection; band steering; software-only router-side defense |
| GAN-based CSI augmentation | CsiGAN | GAN-based augmentation for class imbalance and synthetic-to-real CSI robustness |
| Domain/generalization robustness | WiFi-CSI-Human-Pose-Detection / SenseFi | Cross-room and cross-device generalization; relevant to robustness but not adversarial defense specifically |

### Tier 3: Planned Future Work

These defense methods are identified as future work in the thesis roadmap. They are **not yet implemented**.

| Defense | Status | Priority |
|---------|--------|----------|
| FGSM adversarial training | Future work | High |
| PGD adversarial training | Future work | High |
| C&W adversarial training | Future work | Medium |
| Universal perturbation robustness | Future work | Medium |
| Transfer-based black-box defense evaluation | Future work | Medium |
| Randomized smoothing / certified robustness | Future work | High (for certified safety bounds) |
| Raw CSI-level signal filtering | Future work | Medium |
| Clinical-safety-aware defense thresholds | Future work | High |
| Detection-delay-aware defense evaluation | Future work | Medium |
| Domain / generalization robustness across rooms and devices | Future work | Medium |
| Federated Byzantine-robust aggregation | Future work | Low (Phase 5+) |

---

## Defense Taxonomy Table

| Defense Family | Source / Reference | Current Status | Thesis Relevance |
|---------------|-------------------|---------------|------------------|
| Preprocessing defenses | This repository | Implemented on synthetic data | Baseline hardening; not a complete security solution |
| Perturbation-aware augmentation | This repository | Prototype implemented | Conceptual adversarial training precursor |
| Adversarial training (FGSM/PGD/C&W) | Attack_WiFi_Sensing + thesis plan | Future work | Core defense for adversarial robustness evaluation |
| Certified robustness (randomized smoothing) | Thesis plan + literature | Future work | Certified worst-case safety bounds; critical for healthcare sensing |
| Anti-eavesdropping / privacy scheduling | AntiEave-WiFi-Sensing | External reference only | Defense against adversarial WiFi sensing eavesdropping |
| Adversarial data generation / privacy | WiFi-ADG | External reference only | Behavior obfuscation; adversarial privacy preservation |
| Router-side privacy mitigation | goop-veil | External reference only | Not healthcare-specific; software-only surveillance defense |
| GAN-based CSI augmentation | CsiGAN | External reference only / future | Class imbalance; synthetic-to-real robustness support |
| Domain / generalization robustness | WiFi-CSI-Human-Pose-Detection + SenseFi | External reference / future | Cross-room and cross-device generalization |

---

## Defense Methods to Clinical-Safety Metric Mapping

All safety-metric connections are evaluated using **synthetic data only**. They do not represent clinical outcomes or validated healthcare performance.

| Defense | Missed Falls / Day Impact | False Alarms / Hour Impact | Suppressed Apnea Alarms / Hour | Time-to-Alarm Delay |
|---------|--------------------------|---------------------------|-------------------------------|--------------------|
| Moving average smoothing | May reduce (noise-induced FN) | May reduce (noise-induced FP) | Not evaluated (future work) | Not evaluated |
| Median filtering | May reduce (burst-induced FN) | May reduce (burst-induced FP) | Not evaluated (future work) | Not evaluated |
| Outlier clipping | May reduce (extreme-perturbation FN) | May reduce (extreme-perturbation FP) | Not evaluated (future work) | Not evaluated |
| Robust normalization | Minor effect | Minor effect | Not evaluated (future work) | Not evaluated |
| Perturbation-aware augmentation | Prototype only; not yet evaluated | Prototype only; not yet evaluated | Not evaluated (future work) | Not evaluated |
| Adversarial training (future) | Primary target: reduce | Primary target: reduce | Primary target: reduce | Must not increase |
| Randomized smoothing (future) | Certified bound; evaluate | Certified bound; evaluate | Certified bound; evaluate | Must not increase |
| Clinical-threshold defense (future) | Tune defense for safety margin | Tune defense for safety margin | Tune defense for safety margin | Must not increase |

> **Disclaimer:** All connections above are evaluated using synthetic data only. The safety-metric columns for future work methods are design targets, not measured results.

---

## Preprocessing-Based Defenses (Implemented)

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

---

## Perturbation-Aware Training (Implemented as Prototype)

Perturbation-aware training (also called adversarial training in the machine learning literature) involves augmenting the training dataset with perturbed examples so that the trained classifier learns to be robust to expected perturbations.

In this repository, `augment_with_perturbations()` provides a simple prototype of this concept by generating a combined dataset of clean and perturbed synthetic samples. Full adversarial training with FGSM, PGD, or C&W is **not yet implemented** and is identified as future work.

---

## Connection to Clinical-Safety Metrics

Defense quality is evaluated not only using standard ML metrics but also using clinical-safety-aware metrics:

| Defense Effect | Safety Metric Impact |
|---------------|---------------------|
| Reduced false negatives after defense | Lower missed fall rate |
| Reduced false positives after defense | Lower false alarm rate |
| No improvement | Defense insufficient for this perturbation type |
| Worse performance after defense | Over-smoothing or over-clipping effect |

> **Disclaimer:** These safety-metric connections are evaluated using synthetic data only. They do not represent clinical outcomes or validated healthcare performance.

---

## Current Repository Status

| Component | Status |
|-----------|--------|
| Preprocessing defense functions | Implemented (`src/defenses.py`) |
| Clean vs perturbed vs defended comparison | Implemented (notebook Section 17) |
| ML metrics for all three conditions | Implemented (notebook Section 17) |
| Safety metrics for all three conditions | Implemented (notebook Section 17) |
| Defense results summary | Saved to `results/defense_methods_summary.md` |
| Perturbation-aware augmentation prototype | Implemented (`src/defenses.py`) |
| Full adversarial training (FGSM/PGD/C&W) | Not implemented (future work) |
| Certified robustness (randomized smoothing) | Not implemented (future work) |
| Real physical-layer defense | Not implemented (future work) |
| Clinical defense validation | Not implemented (future work) |
| Detection-delay-aware evaluation | Not implemented (future work) |
| Cross-dataset / real-data defense evaluation | Not implemented (future work) |

---

## Limitations

- All defenses are synthetic. They operate on synthetic CSI-like features, not on real WiFi CSI measurements.
- Preprocessing defenses are not designed to resist adaptive adversaries. An attacker with knowledge of the defense strategy could likely circumvent these methods.
- The evaluation is performed using a simple Random Forest classifier on synthetic data. Results may not generalize to deep learning models or real hardware.
- No formal security guarantee (such as certified robustness) is provided.
- Results should not be interpreted as evidence of real-world defense effectiveness, clinical safety improvement, or hardware-validated performance.

---

## Future Extensions

- Implement adversarial training using FGSM, PGD, C&W, and MIM attacks on synthetic and real CSI data.
- Evaluate randomized smoothing as a certifiable defense; compute certified radius and worst-case safety bounds.
- Apply defenses to raw synthetic CSI-like time-series signals instead of extracted features.
- Evaluate defense effectiveness against adaptive perturbations.
- Collect real CSI measurements and evaluate hardware-level defense effectiveness.
- Connect defense evaluation to detection delay metrics and clinical-safety endpoints.
- Evaluate defenses under WiFi 7 multi-link operation scenarios.
- Extend to federated learning settings where Byzantine-robust aggregation serves as a defense.
- Map every defense to clinical-safety metrics: missed falls per day, false alarms per hour, suppressed apnea alarms per hour, and time-to-alarm delay.

---

*This document is part of the Secure WiFi CSI Healthcare Sensing Research Prototype. All content is intended for academic research and prototype demonstration purposes only. Last updated: 2026-05-24*
