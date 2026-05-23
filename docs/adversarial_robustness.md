# Adversarial Robustness

> **Important note:** This document describes synthetic perturbation stress testing applied to synthetic CSI-like data only. No real physical-layer attack has been implemented. No real WiFi hardware is used. No clinical validation is included. All results are prototype outputs intended for research-methodology demonstration.

## Purpose

This document explains the motivation and methodology for adversarial robustness stress testing in the WiFi CSI Fall Detection Research Prototype. The goal is to evaluate how a baseline fall-detection classifier responds to synthetic signal perturbations, and to connect robustness degradation to safety-aware metrics such as missed falls and false alarms.

This work supports the broader PhD research direction of evaluating secure WiFi CSI sensing systems under adversarial or physical-layer perturbations.

## Why Robustness Matters for WiFi CSI Sensing

WiFi Channel State Information (CSI)-based sensing systems operate at the physical layer of the wireless communication stack. This makes them potentially sensitive to a range of signal-level disturbances, including:

- **Environmental interference**: Multipath reflections, co-channel interference, and environmental changes can alter CSI amplitude and phase.
- **Adversarial perturbations**: A motivated attacker may inject RF signals or manipulate the wireless channel to degrade sensing performance.
- **Hardware imperfections**: Real CSI hardware introduces calibration noise, phase offsets, and subcarrier-level variability.

In a fall-detection context, robustness degradation can have serious consequences:

- **Missed falls**: A perturbed signal may cause a fall event to be misclassified as normal activity, delaying emergency response.
- **False alarms**: Perturbations may cause normal activity to be flagged as a fall, increasing alarm fatigue for caregivers.
- **Detection delay**: Repeated perturbations may increase the time before a genuine fall is detected.

Understanding robustness is therefore a necessary step toward designing reliable, secure WiFi CSI sensing systems.

## Synthetic Perturbation Model

This repository currently implements three classes of synthetic perturbations applied to synthetic CSI-like data:

### 1. Random Noise Perturbation

- **Description**: Adds Gaussian random noise to the CSI-like amplitude features.
- **Motivation**: Models low-level background interference or hardware noise.
- **Implementation**: Controlled by a noise standard deviation parameter (`noise_std`).

### 2. Burst Perturbation

- **Description**: Adds a short, time-localized disturbance to a subset of samples.
- **Motivation**: Simulates a sudden interference-like event, such as a co-channel transmitter activating briefly.
- **Implementation**: Controlled by burst magnitude and the fraction of samples affected (`burst_fraction`).

### 3. Subcarrier-Level Perturbation

- **Description**: Adds perturbation to selected feature dimensions (simulating subcarrier-sensitive effects).
- **Motivation**: CSI measurements are subcarrier-resolved; selective subcarrier degradation may affect sensing performance differently than broadband noise.
- **Implementation**: Controlled by a list of target feature indices and a perturbation scale.

> **Note:** These are simplified synthetic perturbation models. They are not equivalent to real physical-layer attacks, hardware jamming, or adversarial machine learning attacks. Real-world robustness evaluation would require hardware experiments with genuine CSI measurements.

## Clean vs Perturbed Evaluation

The robustness evaluation workflow is:

1. Train a baseline Random Forest classifier on clean synthetic CSI-like training data.
2. Apply each perturbation type to the synthetic test set.
3. Run the trained classifier on both the clean and perturbed test sets.
4. Compare performance using ML metrics (accuracy, precision, recall, F1-score).
5. Compute safety-aware metrics (missed falls, false alarms, missed fall rate, false alarm rate) for both clean and perturbed conditions.
6. Report the degradation in each metric caused by the perturbation.

This workflow demonstrates how a robustness evaluation framework can be structured, even when using synthetic data.

## Connection to Clinical-Safety Metrics

Robustness degradation is connected to safety-aware metrics in the following way:

| Robustness Effect | Safety Metric Impact |
|---|---|
| Increased false negatives (fall missed) | Higher missed fall rate |
| Increased false positives (normal flagged as fall) | Higher false alarm rate |
| Both increase together | Alarm fatigue, reduced system trust |

For a healthcare-oriented WiFi CSI sensing system, missed falls are typically the highest-priority safety concern, as they directly delay emergency response. Perturbations that selectively increase missed falls are therefore the most safety-critical.

> **Disclaimer:** These safety-metric connections are demonstrated using synthetic data only. They do not represent clinical outcomes or validated healthcare performance.

## Current Repository Status

| Component | Status |
|---|---|
| Synthetic perturbation functions | Implemented (`src/adversarial.py`) |
| Clean vs perturbed ML metrics | Implemented (notebook Section 16) |
| Clean vs perturbed safety metrics | Implemented (notebook Section 16) |
| Robustness results summary | Saved to `results/adversarial_robustness_summary.md` |
| Real physical-layer attack | Not implemented (future work) |
| Real CSI hardware validation | Not implemented (future work) |
| Clinical robustness validation | Not implemented (future work) |

## Limitations

- All perturbations are synthetic. They do not replicate real WiFi channel behavior.
- The baseline classifier is a simple Random Forest trained on synthetic features. Its robustness profile may differ substantially from deep learning models or models trained on real CSI data.
- No adversarial machine learning techniques (e.g., FGSM, PGD) are implemented. Current perturbations are non-adaptive.
- Results should not be interpreted as evidence of real-world attack impact or clinical system failure.
- Subcarrier-level perturbations are simulated at the feature level, not at the true RF subcarrier level.

## Future Extensions

- Implement adaptive adversarial perturbations (e.g., gradient-based attacks on a neural network classifier).
- Collect real CSI measurements to evaluate hardware-level robustness.
- Model specific physical-layer attack scenarios (e.g., pilot contamination, channel spoofing).
- Evaluate robustness of federated learning models under Byzantine or poisoning attacks.
- Develop robustness-hardening methods (e.g., adversarial training, anomaly detection, secure aggregation).
- Connect robustness evaluation to WiFi 7 multi-link operation security considerations.
- Expand safety-metric analysis to include detection delay under sustained perturbations.

---

*This document is part of the WiFi CSI Fall Detection Research Prototype. All content is intended for academic research and prototype demonstration purposes only.*
