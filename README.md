# WiFi CSI Fall Detection Research Prototype

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Research%20Prototype-yellow)
![Data](https://img.shields.io/badge/Data-Synthetic%20Only-lightgrey)

> **Disclaimer:** This repository uses **synthetic CSI-like data only**. It does not use real patient data, real clinical data, or validated WiFi CSI hardware measurements. All results are prototype outputs intended to demonstrate a research workflow. This is not a clinical product, a validated fall-detection system, or a medical device.

---

## Project Summary

An end-to-end research prototype exploring **WiFi Channel State Information (CSI)-inspired fall detection** using synthetic signals, signal processing, and machine learning. The project demonstrates a full pipeline from synthetic CSI generation through baseline classification, clinical-safety-aware evaluation, adversarial robustness stress testing, simple defense methods, and interactive visualization. Built to support PhD research in secure WiFi sensing at Portland State University.

---

## Repository Highlights

| Feature | Status |
|---|---|
| Synthetic CSI-like signal generation | Implemented |
| Amplitude and phase visualization | Implemented |
| Normal vs fall-like event simulation | Implemented |
| Preprocessing and feature extraction | Implemented |
| Baseline Random Forest classifier | Implemented |
| Clinical-safety-aware metrics (missed falls, false alarms) | Implemented |
| Adversarial robustness stress testing (synthetic) | Implemented |
| Simple preprocessing defense methods (synthetic) | Implemented |
| Streamlit interactive dashboard | Implemented |
| Real CSI hardware data | Future work |
| Clinical validation | Not claimed |
| Hardware deployment | Not claimed |

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/shahram-h-hesari/wifi-csi-fall-detection.git
cd wifi-csi-fall-detection

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the Jupyter notebook
jupyter notebook notebooks/01_csi_signal_exploration.ipynb
```

---

## Demo Dashboard

An interactive Streamlit dashboard visualizes the full synthetic prototype pipeline.

```bash
streamlit run app.py
```

The dashboard includes:
- Synthetic CSI amplitude and phase visualization
- Normal vs fall-like event comparison
- Baseline classifier prototype predictions
- Clinical-safety-aware metrics (missed falls, false alarms)
- Clean vs perturbed adversarial robustness comparison
- Perturbed vs defended comparison

See [`docs/demo_dashboard.md`](./docs/demo_dashboard.md) for full instructions.

> **Note:** The dashboard uses synthetic data only. It is for research visualization and education, not clinical use.

---

## Repository Structure

```
wifi-csi-fall-detection/
├── app.py                          # Streamlit demo dashboard
├── requirements.txt                # Python dependencies
├── notebooks/
│   └── 01_csi_signal_exploration.ipynb  # Full prototype pipeline notebook
├── src/
│   ├── simulate_csi.py             # Synthetic CSI signal generation
│   ├── preprocessing.py            # Signal preprocessing
│   ├── features.py                 # Feature extraction
│   ├── baseline_model.py           # Baseline ML classifier
│   ├── clinical_metrics.py         # Clinical-safety-aware metrics
│   ├── adversarial.py              # Synthetic perturbation functions
│   └── defenses.py                 # Preprocessing defense functions
├── docs/
│   ├── research_context.md         # Research background
│   ├── threat_model.md             # Physical-layer threat model
│   ├── clinical_safety_metrics.md  # Safety metrics explanation
│   ├── adversarial_robustness.md   # Adversarial robustness methodology
│   ├── defense_methods.md          # Defense methods explanation
│   ├── demo_dashboard.md           # Dashboard instructions
│   ├── project_status.md           # Project status checklist
│   ├── roadmap.md                  # Research roadmap
│   └── validation_status.md        # Validation transparency
├── results/
│   ├── baseline_results.md
│   ├── clinical_safety_summary.md
│   ├── adversarial_robustness_summary.md
│   └── defense_methods_summary.md
├── figures/                        # Saved plots
├── data/                           # Data directory (synthetic only)
├── datasets/               # External dataset catalog (metadata and source links only; no dataset files stored)
|   ├── mm-fi/              # MM-Fi multi-modal WiFi sensing dataset card
|   ├── wi-pose/            # Wi-Pose WiFi CSI pose estimation dataset card
|   ├── signfi/             # SignFi sign language WiFi CSI dataset card
|   ├── widar/              # Widar3 cross-domain WiFi gesture dataset card
|   ├── ut-har/             # UT-HAR WiFi HAR dataset card (SenseFi benchmark)
|   ├── ntu-fi-har/         # NTU-Fi HAR WiFi dataset card (SenseFi benchmark)
|   ├── ntu-fi-humanid/     # NTU-Fi HumanID WiFi dataset card (SenseFi benchmark)
|   ├── antieave-wifi-sensing/ # AntiEave anti-eavesdropping security dataset card
|   ├── wifi-adg/           # WiFi-ADG adversarial privacy dataset card
|   └── future_datasets/    # Placeholder for future dataset tracking
└── third_party/            # Third-party attributions (external reference READMEs; no code copied)
    ├── wifi_sensing/
    |   ├── ruview/         # RuView third-party reference
    |   ├── sensefi/        # SenseFi WiFi CSI Sensing Benchmark reference
    |   └── esp_csi/        # ESP-CSI WiFi CSI toolkit reference
    └── wifi_sensing_security/
        ├── attack_wifi_sensing/    # Attack_WiFi_Sensing adversarial attack reference
        ├── awesome_ws_security/    # Awesome-WS-Security literature reference
        ├── antieave_wifi_sensing/  # AntiEave anti-eavesdropping defense reference
        └── wifi_adg/               # WiFi-ADG adversarial privacy reference
```

---

## Project Status

See [`docs/project_status.md`](./docs/project_status.md) for the full component status table.

**Current phase:** Phase 9 - GitHub Polish and LinkedIn-Ready Presentation

All results are synthetic prototype outputs. Real CSI datasets, hardware deployment, and clinical validation are identified as future work.

---

## Research Motivation

WiFi Channel State Information (CSI) captures how wireless signals propagate through an environment. Human movement affects the multipath profile of WiFi signals, making CSI a candidate signal for contactless sensing applications such as:

- Fall detection for elderly individuals
- Respiration-rate and heart-rate monitoring
- Sleep monitoring
- Continuous vital-sign sensing without wearable devices

CSI-based sensing also operates at the **physical layer**, creating a potential attack surface that motivates the study of **adversarial robustness** and **physical-layer security** for healthcare-oriented WiFi sensing systems.

---

## Security and Robustness Evaluation

This repository includes synthetic adversarial robustness stress testing and simple preprocessing defense evaluation:

- Three synthetic perturbation types: random noise, burst perturbation, subcarrier-level perturbation
- Clean vs perturbed ML metrics and safety metrics
- Defense methods: moving average smoothing, median filtering, outlier clipping, robust normalization
- Results connect perturbation impact to missed falls and false alarms

See [`docs/adversarial_robustness.md`](./docs/adversarial_robustness.md) and [`docs/defense_methods.md`](./docs/defense_methods.md).

> **Note:** These are synthetic prototype evaluations only. No real physical-layer attack or validated defense is implemented.

---

## Clinical-Safety-Aware Metrics

The prototype evaluates models using safety-aware metrics appropriate for healthcare sensing contexts:

- **Missed falls** (false negatives): Fall events predicted as normal activity
- **False alarms** (false positives): Normal activity predicted as a fall
- **Missed fall rate** and **false alarm rate**
- **Alarm fatigue indicator**

See [`docs/clinical_safety_metrics.md`](./docs/clinical_safety_metrics.md).

> **Note:** All safety metrics are computed from synthetic labels and predictions only.

---

## Documentation

| Document | Description |
|---|---|
| [`docs/research_context.md`](./docs/research_context.md) | PhD research framing |
| [`docs/threat_model.md`](./docs/threat_model.md) | Physical-layer threat model |
| [`docs/clinical_safety_metrics.md`](./docs/clinical_safety_metrics.md) | Safety metrics explanation |
| [`docs/adversarial_robustness.md`](./docs/adversarial_robustness.md) | Robustness methodology |
| [`docs/defense_methods.md`](./docs/defense_methods.md) | Defense methods |
| [`docs/demo_dashboard.md`](./docs/demo_dashboard.md) | Dashboard instructions |
| [`docs/project_status.md`](./docs/project_status.md) | Project status checklist |
| [`docs/roadmap.md`](./docs/roadmap.md) | Research roadmap |
| [`docs/validation_status.md`](./docs/validation_status.md) | Validation transparency |
| [`references.md`](./references.md) | Academic references |
| [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md) | Third-party attributions |

---

## Results

| File | Description |
|---|---|
| [`results/baseline_results.md`](./results/baseline_results.md) | Baseline classifier results |
| [`results/clinical_safety_summary.md`](./results/clinical_safety_summary.md) | Clinical-safety metric results |
| [`results/adversarial_robustness_summary.md`](./results/adversarial_robustness_summary.md) | Robustness stress test results |
| [`results/defense_methods_summary.md`](./results/defense_methods_summary.md) | Defense comparison results |

All results are synthetic prototype outputs and should not be interpreted as real-world performance.

---

## Tools and Technologies

- **Python 3.10+**
- **NumPy, Pandas** - Data manipulation and signal processing
- **Matplotlib** - Signal and results visualization
- **SciPy** - Filtering and FFT
- **scikit-learn** - Machine learning pipeline
- **Streamlit** - Interactive demo dashboard
- **Jupyter Notebook** - Prototype exploration

---

## Limitations

- All data are synthetic CSI-like signals, not real WiFi CSI measurements
- No clinical data, patient data, or hospital data are used
- No hardware deployment is included
- The fall-like event model is simplified and not clinically validated
- Adversarial perturbations are synthetic stress tests, not real physical-layer attacks
- Defense methods are simple preprocessing prototypes, not certified security solutions
- All results should be interpreted as prototype outputs only

---

## LinkedIn and Portfolio Use

See [`docs/linkedin_summary.md`](./docs/linkedin_summary.md) for a LinkedIn-ready project summary, post draft, and skills overview.

---


## Testing & Verification

This repository includes a smoke test script and basic pytest unit tests. All tests operate on **synthetic data only** and verify prototype pipeline logic, not real-world CSI performance.

### Run Smoke Test

```bash
python scripts/smoke_test.py
```

Expected output: pipeline stages complete without errors on synthetic data.

### Run Unit Tests (pytest)

```bash
pip install pytest
pytest tests/
```

Expected output: all tests pass on synthetic pipeline checks.

> **Note:** Tests validate the synthetic prototype pipeline only. They do not validate real WiFi CSI hardware, clinical fall-detection accuracy, or real-world deployment readiness.

See [`docs/testing_and_verification.md`](./docs/testing_and_verification.md) for full testing documentation.

---
## Roadmap

See [`docs/roadmap.md`](./docs/roadmap.md) for the full multi-phase research roadmap.

| Phase | Description | Status |
|---|---|---|
| Phase 1 | Repository structure and synthetic pipeline | Completed |
| Phase 2 | README and documentation foundation | Completed |
| Phase 3 | Source code refactoring | Completed |
| Phase 4 | Synthetic CSI pipeline notebook | Completed |
| Phase 5 | Clinical-safety-aware metrics | Completed |
| Phase 6 | Adversarial robustness stress testing | Completed |
| Phase 7 | Defense methods and robustness hardening | Completed |
| Phase 8 | Streamlit demo dashboard | Completed |
| Phase 9 | GitHub polish and LinkedIn-ready presentation | Completed |
| Phase 10 | Testing & verification (synthetic pipeline) | Completed |
| Phase 11 | RuView third-party integration and adversarial evaluation workspace | Completed |
| Phase 10+ | Real CSI datasets, hardware, clinical evaluation | Future work |

---

## Third-Party Projects

This repository references third-party open-source WiFi sensing projects for academic study. Third-party code is kept **strictly separate** from this repository's original `src/`, `notebooks/`, and `app.py` pipeline.

### RuView (Third-Party Reference and Experimental Target)

- **Source:** https://github.com/ruvnet/RuView
- **License:** MIT (verified May 2026)
- **Documentation:** [`third_party/wifi_sensing/ruview/`](./third_party/wifi_sensing/ruview/README.md)
- **Experiment Workspace:** [`experiments/ruview_adversarial_evaluation/`](./experiments/ruview_adversarial_evaluation/README.md)
- **Use:** Repository-structure review, simulation workflow study, dashboard/interface design inspiration, and planned future offline adversarial robustness evaluation
- **Validation Status:** RuView's claims are **not independently validated** in this repository. No clinical, hardware, or real-world validation is claimed.

See [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md) for the full attribution and license policy.

---

## Dataset Catalog

The [`datasets/`](./datasets/README.md) folder contains a curated catalog of public and research WiFi CSI datasets relevant to this repository's research area.

- **Initial entries:** [MM-Fi](./datasets/mm-fi/README.md) and [Wi-Pose](./datasets/wi-pose/README.md) — related WiFi CSI sensing datasets referenced in third-party documentation
- **Full catalog:** [`datasets/dataset_catalog.md`](./datasets/dataset_catalog.md)
- **Future candidates:** Widar3.0, FallDeFi, SignFi, UT-HAR, and others (see [`datasets/future_datasets/README.md`](./datasets/future_datasets/README.md))

**Dataset policy:**
- Dataset files are **not stored directly** in this repository unless redistribution is explicitly permitted
- Current repository experiments still use **synthetic CSI-like data only**
- Real CSI dataset integration is **future work**
- MM-Fi and Wi-Pose are cataloged as related datasets; they are **not currently used for validation** in this repository

---

## Author

**Shahram H. Hesari**
PhD Candidate, Electrical Engineering and Computer Science
Portland State University

---

## License

This project is licensed under the MIT License. See [`LICENSE`](./LICENSE) for details.

Third-party project attributions are documented in [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md).


---

> **Update Note (2026-05-24):** Four new external repository references have been added to `third_party/`:
> - `third_party/wifi_sensing_security/goop_veil/` — goop-veil: software-only WiFi CSI privacy defense (Apache-2.0)
> - `third_party/wifi_sensing/wifi_csi_human_pose_detection/` — WiFi-CSI-Human-Pose-Detection: pose sensing, through-wall sensing, domain generalization (GPL-3.0)
> - `third_party/wifi_sensing/mowa_wifi_sensing/` — mowa-wifi-sensing: WiFi CSI HAR / fall baseline (BSD-3-Clause)
> - `third_party/wifi_sensing/baby_monitor_wifi_csi/` — baby-monitor-wifi-csi: WiFi CSI breathing / apnea baseline (MIT)
>
> All are external references only. No code, datasets, or files have been copied. The `datasets/future_datasets/` folder tracks candidate dataset notes for these repositories pending future verification. Current implementation continues to use **synthetic CSI-like data only**. Third-party projects and dataset candidates are cataloged for future work and are not currently used for model validation or benchmarking.
