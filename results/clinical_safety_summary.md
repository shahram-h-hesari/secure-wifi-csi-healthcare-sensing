# Clinical-Safety-Aware Summary

> **Important Note:** These metrics are computed from synthetic CSI-like prototype outputs only. They are intended to demonstrate the evaluation framework and should not be interpreted as clinical validation, medical-grade fall-detection performance, or real-world deployment evidence. No real patient data, real CSI hardware data, or real clinical outcomes are used.

---

## Metrics

All values below are derived from the baseline Random Forest classifier evaluated on a synthetic test set. Delay values are simulated from a uniform distribution as no hardware timestamps are available.

| Metric | Value | Notes |
|---|---|---|
| Total test samples | *computed at runtime* | Synthetic labels |
| True fall-like events | *computed at runtime* | Synthetic labels |
| True normal events | *computed at runtime* | Synthetic labels |
| Missed falls (count) | *computed at runtime* | False negatives on synthetic data |
| False alarms (count) | *computed at runtime* | False positives on synthetic data |
| Missed fall rate | *computed at runtime* | Missed falls / total true falls |
| False alarm rate | *computed at runtime* | False alarms / total true normal |
| Alarm fatigue indicator | *computed at runtime* | Low / Moderate / High (illustrative) |
| Mean simulated delay | *computed at runtime* | Simulated only, not hardware-based |

*Run the notebook `notebooks/01_csi_signal_exploration.ipynb` to populate these values with computed results.*

---

## Interpretation

In a real fall-detection deployment, missed falls (false negatives) represent the most safety-critical error type. A missed fall means the patient is not detected as having fallen, potentially delaying or preventing timely intervention.

False alarms (false positives) are less immediately dangerous but can reduce system usefulness over time. A high false alarm rate may contribute to alarm fatigue, causing caregivers to become desensitized to alerts and potentially miss future true detections.

The alarm fatigue indicator in this prototype is a simplified categorical label based on the false alarm rate. Thresholds are illustrative and are not derived from clinical alarm management standards.

Detection delay values are fully simulated in this prototype and do not represent any real hardware latency or processing pipeline timing.

**All interpretations above apply to the synthetic prototype only.** They do not represent real-world fall detection performance.

---

## Limitations

- All data is synthetic. No real subjects, environments, or hardware are involved.
- The synthetic signal model is a simplified one-dimensional representation. Real WiFi CSI data is significantly more complex.
- Class balance in synthetic data may produce optimistically low missed fall rates and false alarm rates compared to real-world imbalanced scenarios.
- Alarm fatigue thresholds are illustrative, not clinically validated.
- Detection delay is simulated from a uniform distribution, not measured from hardware.
- No adverse event outcomes, clinical endpoints, or patient outcomes are modeled.

---

## Next Steps

- Connect clinical-safety metrics to real CSI data experiments when hardware data becomes available.
- Apply cost-sensitive learning to penalize missed falls more heavily than false alarms in model training.
- Evaluate whether adversarial perturbations to the CSI-like signal increase the missed fall rate (Phase 6).
- Integrate clinical alarm management guidelines (e.g., IEC 60601-1-8) as evaluation references for future work.
- Report clinical-safety metrics per environment or deployment scenario when multi-environment data is available.

---

*Part of the wifi-csi-fall-detection research prototype.*
*See also: [`docs/clinical_safety_metrics.md`](../docs/clinical_safety_metrics.md), [`docs/validation_status.md`](../docs/validation_status.md)*
