# Demo Dashboard

> **Important note:** The demo dashboard uses synthetic CSI-like data only. It is for research visualization and education. It is not clinical validation, real CSI validation, hardware deployment, or medical-grade fall-detection performance.

## Purpose

The demo dashboard provides an interactive visualization of the full synthetic WiFi CSI fall-detection prototype pipeline. It is designed to make the research workflow accessible to GitHub visitors, LinkedIn viewers, collaborators, recruiters, and PhD committee members without requiring them to run the Jupyter notebook.

The dashboard generates all data synthetically at runtime. No external data files are required.

## How to Run

### Prerequisites

```bash
# 1. Clone the repository
git clone https://github.com/shahram-h-hesari/wifi-csi-fall-detection.git
cd wifi-csi-fall-detection

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Launch the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.

## What the Dashboard Shows

The dashboard is organized into the following sections:

### 1. Title and Disclaimer
- Prominent synthetic-data-only disclaimer
- Overview of what the dashboard demonstrates

### 2. Sidebar Controls
Interactive sliders and toggles for:
- **Number of packets**: Length of the synthetic CSI-like time series
- **Number of subcarriers**: Width of the synthetic CSI matrix
- **Noise level**: Standard deviation of background noise on the signal
- **Fall event strength**: Magnitude of the synthetic fall-like event
- **Perturbation strength**: Magnitude of adversarial perturbation for robustness section
- **Defense toggle**: Enable/disable preprocessing defense in the comparison section

### 3. Synthetic CSI Signal Generation
- Generates a synthetic normal-activity CSI-like amplitude signal
- Generates a synthetic fall-like event CSI-like amplitude signal

### 4. Amplitude Visualization
- Line plot of synthetic CSI amplitude over packet index
- Multiple subcarrier traces shown together

### 5. Phase Visualization
- Line plot of synthetic CSI phase over packet index
- Illustrates phase behavior for normal vs fall-like conditions

### 6. Normal vs Fall-Like Event Comparison
- Side-by-side comparison of amplitude signals for both activity types
- Demonstrates visual separability in the synthetic data

### 7. Baseline Classifier Demo
- Extracts statistical features from synthetic signals
- Trains a prototype Random Forest classifier on synthetic training data
- Shows prototype predictions on synthetic test samples
- Displays accuracy, precision, recall, and F1-score

### 8. Clinical-Safety-Aware Metrics
- Computes missed falls, false alarms, missed fall rate, false alarm rate
- Displays alarm fatigue indicator
- All metrics are computed from synthetic labels and predictions only

### 9. Adversarial Robustness Stress Test
- Applies a synthetic perturbation to the test set
- Compares clean vs perturbed ML metrics
- Compares clean vs perturbed safety metrics
- Shows metric degradation caused by the perturbation

### 10. Defense and Hardening Comparison
- Applies a preprocessing defense to the perturbed test set
- Compares clean, perturbed, and defended ML metrics
- Compares clean, perturbed, and defended safety metrics
- Shows whether the defense reduces perturbation impact

### 11. Limitations and Next Steps
- Summary of current prototype limitations
- Pointer to future work items

## Synthetic Prototype Disclaimer

The following limitations apply to all dashboard outputs:

- All CSI-like signals are mathematically synthesized. They are not measured from real WiFi hardware.
- The fall-like event model is simplified and not derived from clinical observations.
- Classifier predictions are trained and evaluated on synthetic data only.
- Adversarial perturbations are synthetic stress tests, not real physical-layer attacks.
- Defense results are from simple preprocessing methods, not validated security solutions.
- Safety metrics (missed falls, false alarms) are computed from synthetic labels only.
- No patient data, clinical data, or healthcare outcomes are involved.

## Controls

| Control | Type | Effect |
|---|---|---|
| Number of packets | Integer slider | Changes time-series length |
| Number of subcarriers | Integer slider | Changes feature matrix width |
| Noise level | Float slider | Changes background noise magnitude |
| Fall event strength | Float slider | Changes fall-like event amplitude |
| Perturbation strength | Float slider | Changes adversarial perturbation magnitude |
| Defense toggle | Checkbox | Enables/disables defense in comparison section |

## Interpreting the Outputs

| Output | What it means |
|---|---|
| High accuracy (clean) | Synthetic signals are well-separated in feature space |
| Accuracy drops after perturbation | Perturbation shifts feature distribution |
| Defense improves accuracy | Preprocessing reduces perturbation impact |
| Missed fall rate increases after perturbation | Perturbation causes fall events to be missed |
| Alarm fatigue HIGH | False alarm rate exceeds 20% |

All interpretations apply to synthetic prototype results only.

## Limitations

- The dashboard does not use real WiFi CSI data.
- Performance metrics depend heavily on synthetic signal parameters.
- The baseline classifier is simple; deep learning models may behave differently.
- Defense effectiveness is specific to the perturbation type and magnitude.
- The dashboard is for education and research demonstration, not clinical use.

## Future Extensions

- Add support for loading real CSI data files (e.g., CSV, .mat)
- Add confusion matrix visualization
- Add ROC curve and precision-recall curve plots
- Add detection delay metric visualization
- Add real-time signal simulation with animated plots
- Add export of results to CSV or PDF
- Deploy as a public Streamlit Cloud application

---

*This document is part of the WiFi CSI Fall Detection Research Prototype. All content is intended for academic research and prototype demonstration purposes only.*
