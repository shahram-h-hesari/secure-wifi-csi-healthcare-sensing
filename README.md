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
└── third_party/                    # Third-party attributions
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
| Phase 10+ | Real CSI datasets, hardware, clinical evaluation | Future work |

---

## Author

**Shahram H. Hesari**
PhD Candidate, Electrical Engineering and Computer Science
Portland State University

---

## License

This project is licensed under the MIT License. See [`LICENSE`](./LICENSE) for details.

Third-party project attributions are documented in [`THIRD_PARTY_NOTICES.md`](./THIRD_PARTY_NOTICES.md).
