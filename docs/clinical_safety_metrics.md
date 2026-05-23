# Clinical-Safety-Aware Metrics

> **Disclaimer:** All metrics documented here are computed from synthetic CSI-like prototype outputs only. This repository does not use real patient data, real clinical data, or validated WiFi CSI measurements. No clinical validation is claimed.

---

## Purpose

This document explains the clinical-safety-aware evaluation framework used in the WiFi CSI fall detection research prototype. The goal is to go beyond standard machine learning accuracy metrics and evaluate model outputs in terms of their potential impact on patient safety in healthcare and assisted-living scenarios.

This is a research framework, not a clinical tool. It is designed to build a foundation for safety-aware evaluation that can later be applied to real CSI data and validated in clinical studies.

---

## Why Accuracy Alone Is Not Enough

In standard machine learning evaluation, accuracy measures the fraction of correct predictions overall. For a balanced binary classification problem, accuracy is often a reasonable first metric.

However, in fall detection for healthcare settings, accuracy alone is insufficient because the two types of prediction errors have very different consequences:

| Error type | ML label | Healthcare consequence |
|---|---|---|
| False negative | Predicted: normal, True: fall | Missed fall — patient does not receive timely assistance |
| False positive | Predicted: fall, True: normal | False alarm — unnecessary alert or caregiver response |

A model with high accuracy can still be dangerous if it systematically misses real fall events, even at a low rate. In healthcare deployments, the cost asymmetry between missing a fall and triggering a false alarm must be explicitly modeled and reported.

---

## Mapping ML Errors to Safety Outcomes

In the context of WiFi CSI-based fall detection:

- **False negatives (missed falls):** The model predicts normal activity when a fall-like event occurred. In a real deployment, this would mean the patient is not detected as having fallen, delaying or preventing intervention.

- **False positives (false alarms):** The model predicts a fall-like event when normal activity is occurring. In a real deployment, this would trigger unnecessary caregiver responses or system alerts.

- **Alarm fatigue:** A high false-alarm rate may cause caregivers to ignore or deprioritize alerts over time, reducing the safety value of the system even when true falls occur.

- **Detection delay:** Even when a fall is eventually detected, the delay between event occurrence and detection may affect the quality of intervention. Shorter delays are generally safer.

These concepts are well established in clinical alarm management literature and are increasingly relevant as ML-based sensing systems are considered for healthcare settings.

---

## Fall-Detection Safety Metrics

The following metrics are used in this repository to extend conventional ML evaluation toward safety-aware assessment:

### Missed Fall Count

The total number of true fall-like events that the model failed to detect (false negatives).

```
missed_falls = number of samples where y_true == 1 and y_pred == 0
```

### False Alarm Count

The total number of normal activity samples that the model incorrectly classified as fall-like events (false positives).

```
false_alarms = number of samples where y_true == 0 and y_pred == 1
```

### Missed Fall Rate

The proportion of true fall-like events that were missed.

```
missed_fall_rate = missed_falls / total_true_fall_events
```

A lower missed fall rate is always preferable in safety-critical settings.

### False Alarm Rate

The proportion of true normal events that triggered a false alarm.

```
false_alarm_rate = false_alarms / total_true_normal_events
```

### Alarm Fatigue Indicator

A simple prototype indicator derived from the false alarm count and rate. High false alarm rates may contribute to alarm fatigue in caregivers, reducing system trustworthiness even when true fall detection is accurate.

In this prototype, the alarm fatigue indicator is a categorical label: `low`, `moderate`, or `high`, based on the false alarm rate threshold.

### Detection Delay

For correctly detected fall-like events, detection delay measures the time between the onset of the fall-like event and the moment it is predicted. In this prototype, detection delay is simulated from synthetic data since no hardware timestamps are available.

---

## Example Metrics Used in This Repository

All metrics below are computed on synthetic CSI-like prototype data and have no clinical validity.

| Metric | Description | Prototype status |
|---|---|---|
| Missed fall count | Number of undetected fall-like events | Computed on synthetic labels |
| False alarm count | Number of false fall detections | Computed on synthetic labels |
| Missed fall rate | Fraction of falls missed | Computed on synthetic labels |
| False alarm rate | Fraction of normal events misclassified | Computed on synthetic labels |
| Alarm fatigue indicator | Categorical risk level based on false alarm rate | Derived from synthetic metrics |
| Detection delay (mean) | Average simulated delay for detected falls | Simulated from synthetic data |

---

## Current Prototype Status

- All clinical-safety metrics are computed from synthetic CSI-like prototype outputs.
- No real patient data, real CSI hardware data, or real clinical outcomes are used.
- The metrics are intended to demonstrate the evaluation framework, not to claim clinical validity.
- Missed fall rate and false alarm rate reflect the behavior of the baseline Random Forest classifier on a synthetic balanced dataset.
- Detection delay values are simulated and do not represent real hardware timing.

See [`results/clinical_safety_summary.md`](../results/clinical_safety_summary.md) for the computed synthetic prototype metrics.

---

## Limitations

- Synthetic data does not capture the full complexity of real WiFi CSI signals, environmental variability, subject variability, or hardware noise.
- The clinical-safety framework is conceptual at this stage and has not been validated in any real healthcare environment.
- Class balance in synthetic data may make the metrics appear more optimistic than they would be on real-world imbalanced data.
- Detection delay is simulated and does not reflect real hardware latency or processing delay.
- Alarm fatigue thresholds used here are illustrative and not derived from clinical guidelines.

---

## Future Extensions

- Apply clinical-safety metrics to real CSI datasets when available.
- Investigate cost-sensitive learning to explicitly penalize missed falls more heavily than false alarms.
- Integrate clinical alarm management guidelines (e.g., IEC 60601-1-8) as evaluation references.
- Evaluate detection delay using hardware timestamps from real CSI capture systems.
- Connect clinical-safety evaluation to adversarial robustness: evaluate whether adversarial perturbations increase the missed fall rate.
- Explore federated learning scenarios where clinical-safety metrics are aggregated across distributed sites.

---

*Part of the wifi-csi-fall-detection research prototype.*
*Author: Shahram H. Hesari, PhD Student, Electrical and Computer Engineering, Portland State University*
*See also: [`validation_status.md`](validation_status.md), [`threat_model.md`](threat_model.md), [`roadmap.md`](roadmap.md)*
