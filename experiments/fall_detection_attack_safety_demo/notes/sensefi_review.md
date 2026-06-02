# SenseFi Review for Fall Detection Attack-Safety Demo

This note reviews SenseFi / WiFi-CSI-Sensing-Benchmark as a candidate starting point for the fall detection attack-safety demo.

The goal is to determine whether SenseFi can support:

```text
clean WiFi CSI fall detection
→ saved clean predictions
→ FGSM/PGD adversarial perturbation
→ attacked predictions
→ clean-to-attacked clinical-safety metric comparison
```

---

## 1. Review Goal

SenseFi is being reviewed as a possible first implementation baseline because it may provide reusable WiFi CSI datasets, deep-learning model code, and benchmark structure.

This review should answer:

```text
Can SenseFi be used to run a clean WiFi CSI fall or fall-related activity baseline and export predictions for later adversarial testing?
```

---

## 2. Repository and Reference

| Item | Finding |
|---|---|
| Repository URL | [xyanchen/WiFi-CSI-Sensing-Benchmark](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark) |
| Paper / benchmark reference | [SenseFi: A library and benchmark on deep-learning-empowered WiFi human sensing](https://www.sciencedirect.com/science/article/pii/S2666389923000405) |
| Journal / publisher | [Patterns, Cell Press / Elsevier, Volume 4, Issue 3, Article 100703, 2023](https://www.sciencedirect.com/science/article/pii/S2666389923000405) |
| Paper DOI | [10.1016/j.patter.2023.100703](https://doi.org/10.1016/j.patter.2023.100703) |
| arXiv version | [arXiv:2207.07859](https://arxiv.org/abs/2207.07859) |
| Authors | Jianfei Yang; Xinyan Chen; Dazhuo Wang; Han Zou; Chris Xiaoxuan Lu; Sumei Sun; Lihua Xie |
| Dataset / data source | [Mendeley Data: SenseFi: A Library and Benchmark on Deep Learning Empowered WiFi Human Sensing](https://data.mendeley.com/datasets/dzvgyxkx2f/1) |
| Dataset DOI | [10.17632/dzvgyxkx2f.1](https://doi.org/10.17632/dzvgyxkx2f.1) |
| Code archive / Zenodo DOI | [10.5281/zenodo.7501869](https://doi.org/10.5281/zenodo.7501869) |
| Main framework | WiFi CSI human-sensing benchmark and model-zoo library |
| Programming language | Python |
| Deep-learning library | PyTorch |
| Available models | MLP; LeNet/CNN; ResNet18; ResNet50; ResNet101; RNN; GRU; LSTM; BiLSTM; CNN+GRU; ViT |
| Available datasets | UT_HAR_data; NTU-Fi_HAR; NTU-Fi-HumanID; Widar |
| Code license | [MIT license](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark/blob/main/LICENSE) |
| Dataset license | [CC BY 4.0 on Mendeley Data](https://data.mendeley.com/datasets/dzvgyxkx2f/1) |
| Initial relevance to this project | High: SenseFi includes reusable WiFi CSI model code, processed datasets, and fall-containing or fall-related HAR datasets that may support clean fall vs non-fall baseline evaluation. |
| Initial limitation | SenseFi is a general WiFi CSI benchmark, not a clinical fall-safety benchmark; event-level timestamps, false alarms per day, and detection latency still need to be checked. |
---

## 3. Dataset Availability

| Question | Finding |
|---|---|
| Does SenseFi provide dataset download instructions? | TBD |
| Are datasets included directly or linked externally? | TBD |
| Is access public? | TBD |
| Is the dataset size manageable? | TBD |
| Is the data format documented? | TBD |
| Are preprocessing steps documented? | TBD |
| Are labels documented? | TBD |

---

## 4. Fall Label Review

| Question | Finding |
|---|---|
| Does SenseFi include a fall label? | TBD |
| Does it include a fall-related activity label? | TBD |
| Which dataset inside SenseFi is most relevant? | TBD |
| Are non-fall activity labels available? | TBD |
| Can labels be converted to binary `fall` vs `non-fall`? | TBD |

Potential binary mapping:

| Original Label | Binary Safety Label | Notes |
|---|---:|---|
| fall | 1 | True fall class |
| walking | 0 | Non-fall activity |
| sitting | 0 | Non-fall activity |
| standing | 0 | Non-fall activity |
| lying down | 0 | Important high-risk confusion class |
| bending / pickup | 0 | May cause false alarms |
| running | 0 | Non-fall activity |
| other | 0 | Confirm dataset-specific meaning |

---

## 5. Code Usability Review

| Question | Finding |
|---|---|
| Can the repo be cloned? | TBD |
| Is installation documented? | TBD |
| Are dependencies listed? | TBD |
| Is PyTorch used? | TBD |
| Is there a clean training script? | TBD |
| Is there a clean inference script? | TBD |
| Can the model output prediction scores? | TBD |
| Can `y_true` be saved? | TBD |
| Can `y_pred_clean` be saved? | TBD |
| Can the code be modified to save CSV outputs? | TBD |

---

## 6. Attack Feasibility

| Question | Finding |
|---|---|
| Can input tensors be accessed before model inference? | TBD |
| Is the model differentiable? | TBD |
| Can gradients be computed with respect to CSI input? | TBD |
| Can FGSM be added at input-tensor level? | TBD |
| Can PGD be added later? | TBD |
| Does preprocessing make attack integration difficult? | TBD |

---

## 7. Metric Feasibility

| Metric | Possible? | Notes |
|---|---|---|
| Accuracy | TBD | Window-level |
| Precision | TBD | Window-level or event-level |
| Recall / sensitivity | TBD | Window-level or event-level |
| F1-score | TBD | Window-level |
| Specificity | TBD | Window-level |
| Missed fall rate | TBD | Requires fall/non-fall labels |
| False alarm count | TBD | Requires non-fall labels |
| False alarms per day | TBD | Requires monitoring duration |
| Event-level recall | TBD | Requires event IDs |
| Detection latency | TBD | Requires timestamps |
| Long-lie risk proxy | TBD | Requires event/timestamp data |

---

## 8. Main Strengths

- TBD
- TBD
- TBD

---

## 9. Main Limitations

- TBD
- TBD
- TBD

---

## 10. Decision

Final decision:

```text
Use SenseFi as first baseline / Defer SenseFi / Reject SenseFi for first demo
```

Reason:

```text
TBD
```

---

## 11. Next Step

If SenseFi is selected, move to:

```text
Run clean WiFi CSI fall-detection baseline
```

If SenseFi is deferred or rejected, review:

```text
FallDeFi
```

as the next candidate.

---

## Claim Boundary

This review supports research implementation planning only.

It does not claim:

- clinical validation,
- medical-device readiness,
- diagnostic capability,
- real patient deployment,
- regulatory approval, or
- formal clinical standard compliance.
