# Fall Detection Attack-Safety Demo

This folder is the practical experiment workspace for evaluating WiFi CSI fall detection under clean and adversarial conditions.

The goal is to reproduce a clean WiFi CSI fall-detection baseline, apply adversarial perturbations, save clean and attacked predictions, and translate model degradation into clinical-safety metrics.

> Status: Planning and lab-manual setup only. No experiments have been executed yet.

---

## 1. Research Goal

Most WiFi CSI fall-detection and adversarial sensing papers report technical metrics such as accuracy, F1-score, or attack success rate.

This experiment asks a more safety-oriented question:

> If a WiFi CSI fall-detection model is degraded by adversarial perturbation, does it miss more real falls, create more false alarms, reduce alert trustworthiness, delay detection, or increase long-lie risk?

The central translation pathway is:

```text
WiFi CSI fall detection output
→ ML prediction error
→ clinical-safety metric
→ adversarial safety degradation
```

---

## 2. Repository Roles

This work uses two related repositories with different purposes.

| Repository | Role |
|---|---|
| `ai-ml-wifi-sensing-hub` | Evidence hub, literature mapping, clinical-safety metric framework, and research gap documentation |
| `secure-wifi-csi-healthcare-sensing` | Implementation repo for experiments, scripts, notebooks, prediction files, metrics, figures, and lab reports |

The evidence hub explains **why** clinical-safety metrics matter.

This implementation repo shows **how** to calculate them.

---

## 3. Experiment Scope

This first practical demo focuses on:

```text
fall vs non-fall classification
```

The initial clean-vs-attacked comparison will use:

```text
Clean baseline
FGSM attack
PGD attack
```

The first safety-oriented metrics will include:

```text
missed fall rate
false alarm count
precision / alert trustworthiness
recall / sensitivity
F1-score
confusion matrix
```

If timestamps or event IDs are available, the experiment can also calculate:

```text
event-level recall
event-level missed fall rate
false alarms per day or user-day
detection latency
delayed detection rate
long-lie risk proxy
```

If timestamps or event IDs are unavailable, this experiment will report **window-level clinical-safety proxies** and clearly state the limitation.

---

## 4. Candidate Starting Points

The first step is to select a reproducible WiFi CSI fall-detection or fall-related activity-recognition baseline.

Recommended candidates:

| Candidate | Why It Matters | Priority |
|---|---|---|
| SenseFi / WiFi-CSI-Sensing-Benchmark | General WiFi CSI benchmark with reusable deep-learning model structure | High |
| FallDeFi | Direct WiFi CSI fall-detection work | High |
| CSI-Bench | Newer and larger in-the-wild WiFi CSI benchmark; useful for later extension | Medium |
| Other WiFi CSI fall/HAR repository | Backup option if the above are not immediately reproducible | Medium |

Selection criteria:

| Criterion | Requirement |
|---|---|
| Public code | Required |
| Dataset access or clear download path | Required |
| Fall or fall-related class | Required |
| Ability to run clean inference | Required |
| Ability to save `y_true` and `y_pred_clean` | Required |
| Prediction scores or probabilities | Preferred |
| PyTorch or modifiable ML pipeline | Preferred |
| Clear preprocessing steps | Preferred |
| Timestamps or event IDs | Preferred |
| License/reuse terms available | Preferred |
| Compatible with adversarial input perturbation | Preferred |

---

## 5. Recommended Folder Structure

Use this structure as the experiment develops:

```text
experiments/fall_detection_attack_safety_demo/
├── README.md
├── notes/
│   ├── dataset_selection.md
│   ├── sensefi_review.md
│   ├── falldefi_review.md
│   ├── dataset_access_and_labels.md
│   ├── setup_notes.md
│   └── limitations.md
├── scripts/
│   ├── run_clean_baseline.py
│   ├── run_fgsm_attack.py
│   ├── run_pgd_attack.py
│   └── compute_safety_metrics.py
├── notebooks/
│   └── 01_clean_vs_attacked_safety_metrics.ipynb
├── results/
│   ├── predictions_clean.csv
│   ├── predictions_fgsm.csv
│   ├── predictions_pgd.csv
│   ├── metrics_clean.csv
│   ├── metrics_fgsm.csv
│   ├── metrics_pgd.csv
│   ├── clean_vs_fgsm_summary.csv
│   ├── safety_degradation_summary.csv
│   ├── clean_vs_attacked_safety_change.csv
│   └── safety_degradation_interpretation.md
└── figures/
    ├── clean_confusion_matrix.png
    ├── fgsm_confusion_matrix.png
    ├── pgd_confusion_matrix.png
    └── clinical_safety_degradation_bar_chart.png
```

---

## 6. Step-by-Step Workflow

## Phase 1 — Dataset and Baseline Selection

Select the first reproducible WiFi CSI fall-detection baseline.

Document the decision in:

```text
notes/dataset_selection.md
```

The selection note should include:

```text
selected baseline
source repository
dataset name
paper reference
available labels
fall vs non-fall mapping
whether timestamps exist
whether event IDs exist
license/reuse notes
reason for selection
reason other options were deferred
```

Minimum decision:

```text
Does this dataset allow fall vs non-fall evaluation?
```

---

## Phase 2 — Dataset Access and Label Review

Create:

```text
notes/dataset_access_and_labels.md
```

Document:

| Field | Finding |
|---|---|
| Dataset name | TBD |
| Dataset source URL | TBD |
| Code repository URL | TBD |
| Paper URL / DOI | TBD |
| Download method | TBD |
| Access status | TBD |
| License / terms of use | TBD |
| CSI format | TBD |
| Activity labels | TBD |
| Fall label exists? | TBD |
| Non-fall labels exist? | TBD |
| Binary fall/non-fall mapping possible? | TBD |
| Timestamps available? | TBD |
| Event IDs available? | TBD |
| Trial/session IDs available? | TBD |
| Subject/environment IDs available? | TBD |
| Prediction export feasible? | TBD |
| Main limitations | TBD |

Important rule:

```text
Do not upload restricted datasets to this repository unless the license clearly allows redistribution.
```

Preferred approach:

```text
Keep dataset links and download instructions in the repo.
Do not store large or restricted raw data in GitHub.
```

---

## Phase 3 — Binary Fall vs Non-Fall Mapping

For clinical-safety evaluation, convert the original dataset labels into a binary safety label.

```text
fall = 1
non-fall = 0
```

Example mapping:

| Original Label | Binary Safety Label | Notes |
|---|---:|---|
| fall | 1 | Positive safety class |
| walking | 0 | Non-fall activity |
| sitting | 0 | Non-fall activity |
| standing | 0 | Non-fall activity |
| lying down | 0 | Important high-risk confusion class |
| bending / pickup | 0 | May cause false alarms |
| running | 0 | Non-fall movement |
| other | 0 | Confirm dataset-specific meaning |

This mapping is required before calculating missed fall rate, false alarms, precision, recall, and F1-score.

---

## Phase 4 — Clean Baseline

Run the selected model on clean WiFi CSI input.

Expected clean workflow:

```text
load dataset
→ preprocess CSI
→ load or train clean model
→ run clean inference
→ save clean predictions
→ compute clean metrics
```

Create or update:

```text
scripts/run_clean_baseline.py
```

Example command placeholder:

```bash
python experiments/fall_detection_attack_safety_demo/scripts/run_clean_baseline.py
```

Save clean predictions to:

```text
results/predictions_clean.csv
```

Required columns:

```csv
sample_id,timestamp,event_id,subject_id,environment_id,true_label,binary_true_label,clean_prediction,clean_score
```

If timestamp, event ID, subject ID, or environment ID is unavailable, use:

```text
NA
```

Do not delete these columns. Keeping a consistent schema makes later datasets easier to compare.

---

## Phase 5 — Clean ML Metrics

Compute clean baseline ML metrics.

Confusion matrix definitions:

| Term | Meaning in Fall Detection |
|---|---|
| TP | Real fall predicted as fall |
| TN | Non-fall predicted as non-fall |
| FP | Non-fall predicted as fall |
| FN | Real fall predicted as non-fall |

For this project:

```text
FN = missed fall
FP = false fall alarm
```

Metric formulas:

```text
Accuracy = (TP + TN) / (TP + TN + FP + FN)

Precision = TP / (TP + FP)

Recall = Sensitivity = TP / (TP + FN)

Specificity = TN / (TN + FP)

F1 = 2 * (Precision * Recall) / (Precision + Recall)

Balanced Accuracy = (Sensitivity + Specificity) / 2

Missed Fall Rate = FN / (TP + FN)

False Positive Rate = FP / (FP + TN)
```

Save clean metrics to:

```text
results/metrics_clean.csv
```

Recommended columns:

```csv
condition,accuracy,precision,recall,specificity,f1,balanced_accuracy,missed_fall_rate,false_positive_rate,tp,tn,fp,fn
```

Use:

```text
condition = clean
```

---

## Phase 6 — Clean Clinical-Safety Proxy Metrics

At minimum, compute these clean clinical-safety proxy metrics:

| Metric | Formula | Safety Meaning |
|---|---|---|
| Missed fall rate | `FN / (TP + FN)` | Percentage of real falls missed |
| False alarm count | `FP` | Number of non-fall samples/windows incorrectly flagged as falls |
| Precision / PPV | `TP / (TP + FP)` | Trustworthiness of fall alerts |
| Recall / sensitivity | `TP / (TP + FN)` | Percentage of real falls detected |
| F1-score | `2TP / (2TP + FP + FN)` | Balance between missed falls and false alarms |

If monitoring duration is available:

```text
False alarms per day = FP / monitoring_days
False alarms per user-day = FP / user_days
```

If event IDs are available:

```text
Event-level recall = detected_fall_events / total_fall_events
Event-level missed fall rate = missed_fall_events / total_fall_events
```

If timestamps are available:

```text
Detection latency = alert_time - fall_impact_time
Delayed detection rate = delayed_detected_falls / detected_falls
```

If timestamps or event IDs are unavailable, state:

```text
This experiment reports window-level clinical-safety proxies. Event-level recall, detection latency, false alarms per day, and long-lie risk proxy require timestamped or event-level annotations.
```

---

## Phase 7 — FGSM Attack

FGSM stands for Fast Gradient Sign Method.

It perturbs the input in the direction that increases the model loss:

```text
x_adv = x + epsilon * sign(gradient_x(loss(model(x), y)))
```

Where:

| Symbol | Meaning |
|---|---|
| `x` | Clean WiFi CSI input |
| `y` | True label |
| `model(x)` | Model output on clean input |
| `loss(model(x), y)` | Classification loss |
| `gradient_x` | Gradient of loss with respect to input CSI |
| `sign(...)` | Direction of perturbation |
| `epsilon` | Attack strength |
| `x_adv` | Adversarially perturbed CSI input |

FGSM is used here as a **software-level adversarial robustness test**, not a physical-world wireless attack.

Create or update:

```text
scripts/run_fgsm_attack.py
```

Expected workflow:

```text
load trained clean model
load clean test data
enable gradient on input tensor
compute clean model output
compute loss
compute gradient with respect to input
create perturbed CSI input
run model on perturbed CSI input
save attacked predictions
```

Recommended starting epsilon values:

```text
epsilon = 0.001
epsilon = 0.005
epsilon = 0.01
epsilon = 0.05
```

The exact values may need adjustment depending on CSI normalization and input scale.

Save FGSM predictions to:

```text
results/predictions_fgsm.csv
```

Required columns:

```csv
sample_id,timestamp,event_id,subject_id,environment_id,true_label,binary_true_label,clean_prediction,clean_score,attacked_prediction,attacked_score,attack_type,epsilon
```

Use:

```text
attack_type = FGSM
```

---

## Phase 8 — PGD Attack

PGD stands for Projected Gradient Descent.

It is a stronger iterative adversarial attack. After FGSM works, PGD can be added to test whether stronger perturbations create larger safety degradation.

Create or update:

```text
scripts/run_pgd_attack.py
```

Save PGD predictions to:

```text
results/predictions_pgd.csv
```

Required columns:

```csv
sample_id,timestamp,event_id,subject_id,environment_id,true_label,binary_true_label,clean_prediction,clean_score,attacked_prediction,attacked_score,attack_type,epsilon,steps
```

Use:

```text
attack_type = PGD
```

---

## Phase 9 — Attacked Metrics

For each attack type and epsilon value, compute:

```text
accuracy
precision
recall / sensitivity
specificity
F1-score
balanced accuracy
missed fall rate
false positive rate
false alarm count
confusion matrix
```

Save FGSM metrics to:

```text
results/metrics_fgsm.csv
```

Save PGD metrics to:

```text
results/metrics_pgd.csv
```

Recommended columns:

```csv
condition,attack_type,epsilon,accuracy,precision,recall,specificity,f1,balanced_accuracy,missed_fall_rate,false_positive_rate,tp,tn,fp,fn
```

Use:

```text
condition = attacked
```

---

## Phase 10 — Clean vs Attacked Safety Comparison

The key output of this experiment is the clean-vs-attacked safety comparison.

Create:

```text
results/safety_degradation_summary.csv
```

Recommended columns:

```csv
condition,attack_type,epsilon,accuracy,f1,recall,precision,specificity,missed_fall_rate,false_positive_rate,false_alarm_count,event_recall,detection_latency,delayed_detection_rate,long_lie_proxy
```

Also create:

```text
results/clean_vs_attacked_safety_change.csv
```

Recommended columns:

```csv
metric,clean_value,attacked_value,absolute_change,relative_change,safety_degradation_ratio,safety_interpretation
```

For each safety metric, calculate:

```text
absolute change = attacked value - clean value

relative change = (attacked value - clean value) / clean value

safety degradation ratio = attacked value / clean value
```

Example:

```text
Clean missed fall rate = 6%
Attacked missed fall rate = 18%

Absolute increase = +12 percentage points
Relative increase = 200%
Safety degradation ratio = 3.0
```

Interpretation:

```text
The attack tripled the missed-fall rate.
```

---

## Phase 11 — Safety Interpretation

Create:

```text
results/safety_degradation_interpretation.md
```

A weak ML-only result would be:

```text
The adversarial attack reduced accuracy from 96% to 86%.
```

A stronger clinical-safety interpretation would be:

```text
The adversarial attack reduced accuracy from 96% to 86%, but the safety impact was more severe. Missed fall rate increased from 6% to 18%, false alarms increased from 2 to 9 per monitoring period, and alert precision dropped from 91% to 63%. This indicates that adversarial degradation creates both missed-fall risk and alarm-burden risk.
```

The interpretation should answer:

```text
What changed under attack?
Which safety metric worsened most?
Did the attack mainly increase missed falls, false alarms, or both?
Did alert trustworthiness decrease?
Are event-level metrics possible with this dataset?
What limitations must be stated?
```

---

## 7. Expected Output Files

This experiment should eventually produce:

```text
results/predictions_clean.csv
results/predictions_fgsm.csv
results/predictions_pgd.csv
results/metrics_clean.csv
results/metrics_fgsm.csv
results/metrics_pgd.csv
results/safety_degradation_summary.csv
results/clean_vs_attacked_safety_change.csv
results/safety_degradation_interpretation.md
```

Optional figures:

```text
figures/clean_confusion_matrix.png
figures/fgsm_confusion_matrix.png
figures/pgd_confusion_matrix.png
figures/missed_fall_rate_change.png
figures/false_alarm_change.png
figures/clinical_safety_degradation_bar_chart.png
```

---

## 8. Final Result Table Template

Use this table in the final report:

| Condition | Accuracy | F1 | Recall | Precision | Missed Fall Rate | False Alarms | Safety Meaning |
|---|---:|---:|---:|---:|---:|---:|---|
| Clean | TBD | TBD | TBD | TBD | TBD | TBD | Baseline |
| FGSM | TBD | TBD | TBD | TBD | TBD | TBD | Attack impact |
| PGD | TBD | TBD | TBD | TBD | TBD | TBD | Stronger attack impact |

If event-level metrics are possible:

| Condition | Event Recall | Event Missed Fall Rate | False Alarms/Day | Median Latency | Delayed Detection Rate | Long-Lie Proxy |
|---|---:|---:|---:|---:|---:|---:|
| Clean | TBD | TBD | TBD | TBD | TBD | TBD |
| FGSM | TBD | TBD | TBD | TBD | TBD | TBD |
| PGD | TBD | TBD | TBD | TBD | TBD | TBD |

---

## 9. Completion Criteria

This experiment is complete when the implementation repo contains:

- [ ] Selected WiFi CSI fall-detection dataset or baseline
- [ ] Dataset access and label review
- [ ] Binary `fall` vs `non-fall` mapping
- [ ] Clean predictions saved to CSV
- [ ] FGSM attacked predictions saved to CSV
- [ ] PGD attacked predictions saved to CSV
- [ ] Clean ML metrics
- [ ] Attacked ML metrics
- [ ] Clean clinical-safety proxy metrics
- [ ] Attacked clinical-safety proxy metrics
- [ ] Clean-to-attacked safety-degradation table
- [ ] Short interpretation of safety impact
- [ ] Limitation statement

---

## 10. Claim Boundary

This experiment is a research prototype.

It does not claim:

- clinical validation,
- medical-device readiness,
- diagnostic capability,
- real patient deployment,
- regulatory approval,
- physical-world attacker validation, or
- formal clinical standard compliance.

Use careful wording:

```text
clinically motivated
safety-oriented
healthcare-relevant
research evaluation
clinical-safety translation
adversarial safety degradation
```

---

## 11. Next Step

The next practical step is to select the first reproducible WiFi CSI fall-detection baseline and create:

```text
notes/dataset_selection.md
```

Candidate baselines:

```text
SenseFi / WiFi-CSI-Sensing-Benchmark
FallDeFi
CSI-Bench
```
