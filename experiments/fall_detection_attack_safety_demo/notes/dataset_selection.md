# Dataset and Baseline Selection

This document records the first dataset and baseline selection decision for the WiFi CSI fall detection attack-safety demo.

The goal is to select one reproducible WiFi CSI fall-detection or fall-related activity-recognition baseline that can support:

```text
clean WiFi CSI fall detection
→ saved clean predictions
→ adversarial perturbation
→ saved attacked predictions
→ clean-to-attacked clinical-safety metric comparison
```

---

## 1. Selection Goal

The first baseline should allow us to run a clean WiFi CSI model and export:

```text
y_true
y_pred_clean
prediction scores
binary fall vs non-fall labels
```

After that, the same baseline should allow FGSM and PGD adversarial perturbations so we can compare:

```text
clean missed fall rate vs attacked missed fall rate
clean false alarms vs attacked false alarms
clean precision vs attacked precision
clean recall vs attacked recall
clean F1-score vs attacked F1-score
```

---

## 2. Candidate Baselines

| Candidate | Type | Why It Matters | Initial Priority |
|---|---|---|---|
| SenseFi / WiFi-CSI-Sensing-Benchmark | WiFi CSI benchmark | General reusable WiFi CSI deep-learning benchmark with multiple models and datasets | High |
| FallDeFi | WiFi CSI fall detection | Directly focused on commodity WiFi fall detection | High |
| CSI-Bench | WiFi CSI benchmark | Newer large-scale in-the-wild benchmark; useful for later extension | Medium |
| Other WiFi CSI fall/HAR repository | Backup | Can be used if the main candidates are not practical | Medium |

---

## 3. Selection Criteria

| Criterion | Requirement | Why It Matters |
|---|---|---|
| Public code | Required | Needed for reproducible implementation |
| Dataset access or clear download path | Required | Needed to run experiments |
| Fall or fall-related class | Required | Needed for fall vs non-fall evaluation |
| Clean inference can run | Required | Needed before adversarial attack |
| Can save `y_true` | Required | Needed for all metrics |
| Can save `y_pred_clean` | Required | Needed for clean baseline |
| Prediction scores/probabilities | Preferred | Useful for thresholding and AUC-PR |
| PyTorch or modifiable ML framework | Preferred | Easier to add FGSM/PGD |
| Clear preprocessing steps | Preferred | Needed for reproducibility |
| Timestamps or event IDs | Preferred | Needed for event-level metrics and latency |
| License/reuse terms available | Preferred | Needed for responsible public repo documentation |
| Compatible with adversarial perturbation | Preferred | Needed for attack-safety demo |

---

## 4. Review Table

Fill this table during review.

| Candidate | Code Available? | Dataset Available? | Fall Label? | Non-Fall Labels? | PyTorch? | Clean Inference? | Can Save Predictions? | Timestamps/Event IDs? | License Clear? | Attack Feasible? | Decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SenseFi | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| FallDeFi | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| CSI-Bench | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Other | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

---

## 5. Candidate 1: SenseFi Review

| Review Item | Finding |
|---|---|
| Repository URL | TBD |
| Paper / benchmark reference | TBD |
| Dataset candidate inside SenseFi | TBD |
| Fall label exists? | TBD |
| Fall-related label exists? | TBD |
| Binary fall vs non-fall mapping possible? | TBD |
| PyTorch code available? | TBD |
| Clean training script available? | TBD |
| Clean inference script available? | TBD |
| Prediction scores available? | TBD |
| Can save `y_true`? | TBD |
| Can save `y_pred_clean`? | TBD |
| Timestamps available? | TBD |
| Event IDs available? | TBD |
| License clear? | TBD |
| FGSM/PGD attack feasible? | TBD |
| Main limitation | TBD |
| Decision | Use / Defer / Reject |

---

## 6. Candidate 2: FallDeFi Review

| Review Item | Finding |
|---|---|
| Paper URL | TBD |
| Code repository URL | TBD |
| Dataset URL | TBD |
| Dataset available? | TBD |
| Fall label exists? | TBD |
| Non-fall labels exist? | TBD |
| Binary fall vs non-fall mapping possible? | TBD |
| Implementation language | TBD |
| PyTorch available? | TBD |
| TensorFlow available? | TBD |
| MATLAB or other framework? | TBD |
| Clean training script available? | TBD |
| Clean inference script available? | TBD |
| Prediction scores available? | TBD |
| Can save `y_true`? | TBD |
| Can save `y_pred_clean`? | TBD |
| Timestamps available? | TBD |
| Event IDs or trial IDs available? | TBD |
| License clear? | TBD |
| FGSM/PGD attack feasible? | TBD |
| Main limitation | TBD |
| Decision | Use / Defer / Reject |

---

## 7. Candidate 3: CSI-Bench Review

| Review Item | Finding |
|---|---|
| Project page | TBD |
| Paper URL | TBD |
| Code repository URL | TBD |
| Dataset URL | TBD |
| Dataset available? | TBD |
| Fall detection task available? | TBD |
| Breathing/respiration task available? | TBD |
| Binary fall vs non-fall mapping possible? | TBD |
| PyTorch code available? | TBD |
| Clean inference script available? | TBD |
| Prediction scores available? | TBD |
| Timestamps available? | TBD |
| Event IDs available? | TBD |
| License clear? | TBD |
| FGSM/PGD attack feasible? | TBD |
| Main limitation | TBD |
| Decision | Use later / Defer / Reject |

---

## 8. Binary Fall vs Non-Fall Mapping

Once a dataset is selected, define the label mapping here.

| Original Label | Binary Safety Label | Notes |
|---|---:|---|
| fall | 1 | True fall class |
| walking | 0 | Non-fall activity |
| sitting | 0 | Non-fall activity |
| standing | 0 | Non-fall activity |
| lying down | 0 | High-risk confusion class |
| bending / pickup | 0 | May cause false alarms |
| running | 0 | Non-fall activity |
| other | 0 | Confirm dataset-specific meaning |

If the dataset does not clearly separate fall and non-fall labels, document the limitation.

---

## 9. Selection Decision

Final selected baseline:

```text
Selected baseline: TBD
Dataset name: TBD
Source repository: TBD
Paper reference: TBD
Reason for selection: TBD
```

Candidates deferred:

| Candidate | Reason Deferred |
|---|---|
| SenseFi | TBD |
| FallDeFi | TBD |
| CSI-Bench | TBD |

---

## 10. Metric Feasibility

After choosing the dataset, mark which metrics are possible.

| Metric | Possible? | Required Data | Notes |
|---|---|---|---|
| Accuracy | TBD | `y_true`, `y_pred` | Window-level |
| Precision | TBD | TP, FP | Window or event-level |
| Recall / sensitivity | TBD | TP, FN | Window or event-level |
| F1-score | TBD | TP, FP, FN | Window or event-level |
| Specificity | TBD | TN, FP | Window-level |
| Missed fall rate | TBD | FN, TP | Window or event-level |
| False alarm count | TBD | FP | Basic safety proxy |
| False alarms per day | TBD | FP, monitoring duration | Requires time duration |
| Event-level recall | TBD | Event IDs | Requires event annotations |
| Detection latency | TBD | Fall impact time, alert time | Requires timestamps |
| Delayed detection rate | TBD | Latency threshold | Requires timestamps |
| Long-lie risk proxy | TBD | Missed events and severe delays | Requires event/timestamp data |

---

## 11. Decision Options

Use one of these decisions.

```text
Use as first baseline
```

Use this if the dataset/code is accessible, fall labels are clear, clean inference can run, and predictions can be saved.

```text
Use as second baseline
```

Use this if it is useful but another candidate is easier for the first demo.

```text
Defer
```

Use this if it is promising but requires too much setup for the first implementation.

```text
Reject for first demo
```

Use this if access, labels, licensing, or prediction export are not practical.

---

## 12. Completion Criteria

This selection step is complete when:

- [ ] At least SenseFi and FallDeFi have been reviewed
- [ ] CSI-Bench has been reviewed as a later extension option
- [ ] One baseline has been selected
- [ ] Dataset/code access has been confirmed
- [ ] Fall or fall-related label has been confirmed
- [ ] Binary `fall` vs `non-fall` mapping is possible
- [ ] Clean prediction export appears possible
- [ ] Metric feasibility is documented
- [ ] Limitations are documented

---

## 13. Next Step

After selecting the first baseline, move to:

```text
Run clean WiFi CSI fall-detection baseline
```

The next implementation goal is to produce:

```text
results/predictions_clean.csv
results/metrics_clean.csv
results/clean_baseline_summary.md
```

---

## 14. Claim Boundary

This document supports research implementation planning only.

It does not claim:

- clinical validation,
- medical-device readiness,
- diagnostic capability,
- real patient deployment,
- regulatory approval, or
- formal clinical standard compliance.
