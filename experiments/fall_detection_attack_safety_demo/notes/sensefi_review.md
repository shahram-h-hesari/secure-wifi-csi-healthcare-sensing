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
| Does SenseFi provide dataset download instructions? | Yes. The SenseFi GitHub README includes a **Download Processed Data** section and instructs users to download and organize the processed datasets into a `Benchmark/Data/` structure. The README also links to processed datasets and pretrained weights. |
| Are datasets included directly or linked externally? | The datasets are **linked externally**, not stored directly in the GitHub repository. The GitHub README links to processed datasets through Google Drive, and the paper/data record links to Mendeley Data. |
| Is access public? | Yes, the processed dataset record is publicly available through Mendeley Data: [SenseFi: A Library and Benchmark on Deep Learning Empowered WiFi Human Sensing](https://data.mendeley.com/datasets/dzvgyxkx2f/1). The Mendeley page provides a `Download All` option and lists the dataset DOI as [10.17632/dzvgyxkx2f.1](https://doi.org/10.17632/dzvgyxkx2f.1). |
| Is the dataset size manageable? | TBD after download. The GitHub README lists processed datasets and sample counts, including UT-HAR with 3,977 training samples and 996 test samples, NTU-Fi_HAR with 936 training samples and 264 test samples, NTU-Fi-HumanID with 546 training samples and 294 test samples, and Widar with 34,926 training samples and 8,726 test samples. This suggests UT-HAR and NTU-Fi_HAR are likely manageable first-start candidates, but actual file size should still be checked before implementation. |
| Is the data format documented? | Partially yes. The GitHub README documents expected folder structure and dataset shapes. UT-HAR is listed as CSI size `1 x 250 x 90`; NTU-Fi_HAR and NTU-Fi-HumanID are listed as CSI size `3 x 114 x 500`; Widar is listed as BVP size `22 x 20 x 20`. The README also notes that UT-HAR data files are CSV format but should be loaded through the provided code because they may not be readable in Excel due to encoding. |
| Are preprocessing steps documented? | Partially yes. The README provides dataset organization and run instructions, while `dataset.py` shows important loading/preprocessing steps. For UT-HAR, the loader reshapes data to `1 x 250 x 90` and applies min-max normalization. For NTU-Fi-style data, the loader loads `.mat` files, normalizes CSI amplitude, downsamples from 2000 to 500 by sampling every fourth point, and reshapes to `3 x 114 x 500`. For Widar, the loader reads CSV files, normalizes values, and reshapes to `22 x 20 x 20`. |
| Are labels documented? | Yes for the benchmark-level classes. The GitHub README documents UT-HAR classes as `lie down`, `fall`, `walk`, `pickup`, `run`, `sit down`, and `stand up`. It documents NTU-Fi_HAR classes as `box`, `circle`, `clean`, `fall`, `run`, and `walk`. NTU-Fi-HumanID is a 14-subject identification dataset, and Widar contains 22 gesture classes. For this project, UT-HAR and NTU-Fi_HAR are the most relevant SenseFi datasets because both include a `fall` class and non-fall activity classes. |

---

## 4. Fall Label Review

| Question | Finding |
|---|---|
| Does SenseFi include a fall label? | Yes. SenseFi includes at least two relevant human-activity-recognition datasets with a `fall` class: **UT-HAR** and **NTU-Fi_HAR**. The SenseFi README lists UT-HAR classes as `lie down`, `fall`, `walk`, `pickup`, `run`, `sit down`, and `stand up`. It lists NTU-Fi_HAR classes as `box`, `circle`, `clean`, `fall`, `run`, and `walk`. |
| Does it include a fall-related activity label? | Yes. UT-HAR includes several fall-related or fall-confusable activities, especially `lie down`, `sit down`, `stand up`, and `pickup`. NTU-Fi_HAR includes `fall` plus non-fall motion classes such as `box`, `circle`, `clean`, `run`, and `walk`. |
| Which dataset inside SenseFi is most relevant? | **UT-HAR is the best first candidate** because it has 7 activity classes and includes both `fall` and clinically important fall-confusion classes such as `lie down`, `sit down`, and `stand up`. **NTU-Fi_HAR is the second candidate** because it also includes `fall`, but its non-fall labels are less directly related to fall-safety confusion. |
| Are non-fall activity labels available? | Yes. UT-HAR has multiple non-fall labels: `lie down`, `walk`, `pickup`, `run`, `sit down`, and `stand up`. NTU-Fi_HAR has non-fall labels: `box`, `circle`, `clean`, `run`, and `walk`. |
| Can labels be converted to binary `fall` vs `non-fall`? | Yes. Both UT-HAR and NTU-Fi_HAR can be converted into binary labels by assigning `fall = 1` and all other activity labels as `non-fall = 0`. This supports window-level fall/non-fall classification and allows calculation of missed fall rate, false alarm count, precision, recall, F1-score, and confusion matrix. |

---

### Candidate Dataset Priority

| Dataset | Fall Label? | Non-Fall Labels | Priority | Reason |
|---|---|---|---|---|
| UT-HAR | Yes | `lie down`; `walk`; `pickup`; `run`; `sit down`; `stand up` | First choice | Best first candidate because it includes fall plus realistic confusion classes such as lying down, sitting down, standing up, and pickup. |
| NTU-Fi_HAR | Yes | `box`; `circle`; `clean`; `run`; `walk` | Second choice | Useful fallback because it includes fall, but the non-fall classes are less directly aligned with clinical fall-confusion scenarios. |
| NTU-Fi-HumanID | No fall class | Subject identity labels | Not suitable for first fall demo | Human identification dataset, not fall detection. |
| Widar | No fall class | Gesture classes | Not suitable for first fall demo | Gesture-recognition dataset, not fall detection. |

---

### Proposed Binary Mapping: UT-HAR

| Original Label | Binary Safety Label | Notes |
|---|---:|---|
| fall | 1 | True fall class |
| lie down | 0 | High-risk confusion class; may look similar to fall in CSI patterns |
| walk | 0 | Non-fall activity of daily living |
| pickup | 0 | Important confusion class; bending/pickup may trigger false alarms |
| run | 0 | Non-fall movement |
| sit down | 0 | Important transition activity; may be confused with fall |
| stand up | 0 | Non-fall transition activity |

---

### Proposed Binary Mapping: NTU-Fi_HAR

| Original Label | Binary Safety Label | Notes |
|---|---:|---|
| fall | 1 | True fall class |
| box | 0 | Non-fall activity |
| circle | 0 | Non-fall activity |
| clean | 0 | Non-fall activity |
| run | 0 | Non-fall movement |
| walk | 0 | Non-fall activity of daily living |

---

### Initial Decision

```text
SenseFi should remain a high-priority candidate for the first clean fall/non-fall baseline.
```

Recommended first dataset:

```text
UT-HAR
```

Reason:

```text
UT-HAR includes a fall class and multiple clinically relevant non-fall confusion classes. It is more suitable than NTU-Fi_HAR for the first fall safety translation demo because missed falls and false fall alarms can be interpreted against activities such as lie down, sit down, stand up, pickup, walk, and run.
```

Limitation:

```text
The SenseFi README documents class labels and sample counts, but event-level timestamps, continuous monitoring duration, and fall impact times still need to be checked. Therefore, the first SenseFi experiment may support window-level clinical-safety proxies rather than full event-level metrics such as detection latency or false alarms per day.
```

Key finding:

```text
SenseFi is usable for fall/non-fall mapping, and UT-HAR should be the first candidate inside SenseFi.
```

Reference:

- [SenseFi / WiFi-CSI-Sensing-Benchmark GitHub repository](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark)
- [SenseFi paper in Patterns / Cell Press](https://www.sciencedirect.com/science/article/pii/S2666389923000405)
- [SenseFi arXiv version](https://arxiv.org/abs/2207.07859)

---

## 5. Code Usability Review

| Question | Finding |
|---|---|
| Can the repo be cloned? | Yes. The repository is public and can be cloned from [xyanchen/WiFi-CSI-Sensing-Benchmark](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark). |
| Is installation documented? | Partially yes. The README provides a **Requirements** section and a **Run** section. It instructs users to install PyTorch/torchvision and then run `pip install -r requirements.txt`. It also notes that the code runs best on Linux/Ubuntu and may require path changes on Windows. |
| Are dependencies listed? | Yes. The repository includes `requirements.txt`, which lists `scipy==1.7.3`, `numpy==1.21.5`, and `einops==0.4.0`. The README separately states that PyTorch and torchvision are required, specifically `pytorch==1.12.0` and `torchvision==0.13.0`. |
| Is PyTorch used? | Yes. The README states that SenseFi is implemented in PyTorch. The code imports `torch`, `torch.nn`, `torch.utils.data`, and defines multiple PyTorch `nn.Module` models. |
| Is there a clean training script? | Yes. The main supervised training and testing script is `run.py`. It supports the command `python run.py --model [model name] --dataset [dataset name]`. The script loads data/model using `load_data_n_model()`, trains the model, and then runs testing. |
| Is there a clean inference script? | Partially. There is no separate standalone inference-only script. However, `run.py` includes a `test()` function that runs model evaluation on the test loader after training. This function can be modified to export clean predictions. |
| Can the model output prediction scores? | Yes, with modification. In `run.py`, the model produces `outputs = model(inputs)`, and predictions are currently generated with `torch.argmax(outputs, dim=1)`. These `outputs` can be converted to scores or probabilities using `torch.softmax(outputs, dim=1)` before saving. |
| Can `y_true` be saved? | Yes, with modification. The `test()` loop already receives `labels` from the test loader. These labels can be saved as `y_true` or converted into binary `fall` vs `non-fall` labels before export. |
| Can `y_pred_clean` be saved? | Yes, with modification. The `test()` function already computes `predict_y = torch.argmax(outputs, dim=1)`. This value can be saved as `y_pred_clean`. |
| Can the code be modified to save CSV outputs? | Yes. The current code prints validation accuracy and loss but does not save prediction CSVs by default. A practical next step is to modify `test()` or create a wrapper script that saves `sample_id`, `true_label`, `binary_true_label`, `clean_prediction`, and `clean_score` into `results/predictions_clean.csv`. |

---

### Code Usability Summary

SenseFi is usable as a first implementation candidate because it provides:

- public GitHub code,
- documented dataset organization,
- PyTorch-based model implementations,
- supervised training/testing through `run.py`,
- reusable dataset loaders,
- multiple model choices,
- UT-HAR support with a fall class,
- model outputs that can be converted into prediction scores.

However, SenseFi needs modification for this project because it does not currently export the prediction files required for clinical-safety translation.

The required modification is:

```text
Modify the test/evaluation loop to save:
sample_id
true_label
binary_true_label
clean_prediction
clean_score
```

---

### Recommended First Implementation Choice

Use this starting configuration first:

```bash
python run.py --model LeNet --dataset UT_HAR_data
```

Reason:

```text
UT_HAR_data includes a fall class and clinically relevant non-fall confusion classes. LeNet is a simpler CNN-style model than ResNet or ViT, making it easier to debug before adding FGSM and PGD attacks.
```

Alternative model choices:

```text
MLP      = simplest model, easiest to debug
LeNet    = simple CNN-style model, good first practical choice
ResNet18 = stronger CNN baseline, useful after LeNet works
CNN+GRU  = useful later for temporal modeling
ViT      = useful later, but more complex for first demo
```

---

### Required Code Modification

The current `test()` function should be extended from accuracy-only evaluation to prediction export.

Current behavior:

```text
model input
→ outputs
→ argmax prediction
→ validation accuracy/loss printed
```

Needed behavior:

```text
model input
→ outputs
→ clean prediction
→ clean score
→ save y_true
→ save y_pred_clean
→ save prediction score
→ export CSV
```

Target output file:

```text
experiments/fall_detection_attack_safety_demo/results/predictions_clean.csv
```

Required columns:

```csv
sample_id,timestamp,event_id,subject_id,environment_id,true_label,binary_true_label,clean_prediction,clean_score
```

For unavailable fields, use:

```text
NA
```

---

### Practical Code Feasibility Decision

```text
SenseFi code is usable for the first clean baseline, but it must be modified to save prediction outputs.
```

Reason:

```text
The repository already provides PyTorch models, dataset loaders, and supervised training/testing. The missing piece is prediction export. Because the test loop already has access to model outputs and labels, saving y_true, y_pred_clean, and clean_score should be straightforward.
```

Limitation:

```text
SenseFi appears to support window-level or sample-level prediction export. Event-level metrics such as detection latency, false alarms per day, and long-lie risk still require timestamps, event IDs, or monitoring-duration metadata, which must be checked separately.
```

---

### Reference Links

- [SenseFi / WiFi-CSI-Sensing-Benchmark GitHub repository](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark)
- [run.py](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark/blob/main/run.py)
- [util.py](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark/blob/main/util.py)
- [dataset.py](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark/blob/main/dataset.py)
- [requirements.txt](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark/blob/main/requirements.txt)
- [UT_HAR_model.py](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark/blob/main/UT_HAR_model.py)

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
