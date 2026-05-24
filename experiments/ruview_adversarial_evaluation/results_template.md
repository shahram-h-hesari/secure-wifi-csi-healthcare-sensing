# Results Template

> **Important:** This is a template only. No results have been fabricated or inserted. All tables are empty placeholders to be filled after actual experiments are run. Do not insert hypothetical, estimated, or fabricated data.

---

## Experiment Overview

| Field | Value |
|---|---|
| RuView version / commit | TBD |
| Experiment date | TBD |
| Software environment | TBD |
| Baseline simulation status | TBD |
| Hardware used | None (offline synthetic only) |

---

## Section 1: Baseline Simulation Results

> *Fill in after successfully running baseline simulation (see `run_ruview_baseline.md`).*

### 1.1 Simulation Environment

| Parameter | Value |
|---|---|
| Python version | TBD |
| Docker used | TBD |
| RuView entry point | TBD |
| Input data source | TBD |
| Model files loaded | TBD |

### 1.2 Baseline Output Summary

| Output Type | Description | Value |
|---|---|---|
| Simulation completes without error | Yes/No | TBD |
| Output format | JSON/CSV/Plot/Dashboard | TBD |
| Example output value | TBD | TBD |
| Hardware required for full run | Yes/No | TBD |

### 1.3 Baseline Reproducibility Notes

> *Notes on what was and was not reproducible without hardware.*

*[To be filled after running]*

---

## Section 2: Perturbed Simulation Results

> *Fill in after running each perturbation experiment (see `perturbation_plan.md`). Do not fill in with estimated or fabricated values.*

### 2.1 Random Noise Perturbation Results

| Noise Std | Output Class Changed | Confidence Delta | Missed Detection | False Alarm | Notes |
|---|---|---|---|---|---|
| 0.01 | TBD | TBD | TBD | TBD | Pending |
| 0.05 | TBD | TBD | TBD | TBD | Pending |
| 0.10 | TBD | TBD | TBD | TBD | Pending |
| 0.20 | TBD | TBD | TBD | TBD | Pending |
| 0.50 | TBD | TBD | TBD | TBD | Pending |

### 2.2 Burst Perturbation Results

| Burst Duration | Burst Magnitude | Position | Output Changed | Notes |
|---|---|---|---|---|
| 1 sample | 2x | Middle | TBD | Pending |
| 5 samples | 5x | Middle | TBD | Pending |
| 10 samples | 10x | Middle | TBD | Pending |
| 5 samples | Dropout | Middle | TBD | Pending |

### 2.3 Subcarrier Perturbation Results

| Subcarriers Perturbed | Type | Output Changed | Notes |
|---|---|---|---|
| 1 | Zeroed | TBD | Pending |
| 5 | Zeroed | TBD | Pending |
| 10 | Random | TBD | Pending |
| All | Amplified 2x | TBD | Pending |

### 2.4 Feature-Level Perturbation Results

| Features Perturbed | Magnitude | Output Changed | Notes |
|---|---|---|---|
| All features | +0.1 | TBD | Pending |
| All features | +0.5 | TBD | Pending |
| Single feature | +1.0 | TBD | Pending |

### 2.5 Phase Distortion Results

| Phase Noise (degrees) | Output Changed | Notes |
|---|---|---|
| 5 | TBD | Pending |
| 15 | TBD | Pending |
| 30 | TBD | Pending |
| 90 | TBD | Pending |

---

## Section 3: Comparison and Summary

> *Fill in after all perturbation experiments are run.*

| Perturbation Type | Most Impactful Parameter | Threshold | Key Finding |
|---|---|---|---|
| Random noise | TBD | TBD | Pending |
| Burst | TBD | TBD | Pending |
| Subcarrier | TBD | TBD | Pending |
| Feature-level | TBD | TBD | Pending |
| Phase distortion | TBD | TBD | Pending |

---

## Section 4: Limitations

- All results are based on offline perturbation of data files or model inputs only
- No real WiFi hardware is used
- No real CSI measurements are collected
- Results apply only to the specific RuView version studied
- Findings cannot be generalized to real-world deployment without further validation
- No clinical or safety validation is claimed
- This template must only be filled with actual experimental observations

---

## Section 5: Reproducibility Notes

> *Document any issues that would prevent another researcher from reproducing these results.*

*[To be filled after running]*

---

*Template created: May 2026. All result fields are empty and pending actual experiment execution.*
