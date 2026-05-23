# WiFi CSI Fall Detection Research Prototype

> **Disclaimer:** This repository currently uses synthetic CSI-like time-series data for demonstration purposes. It does not use real patient data, real clinical data, or validated WiFi CSI measurements. Results are intended only to demonstrate the research workflow and should not be interpreted as clinical or real-world fall detection performance.

---

## Overview

This is an early-stage research prototype exploring WiFi Channel State Information (CSI)-inspired fall detection using synthetic CSI-like signals, signal processing, and machine learning workflows. The goal is to demonstrate a clean, beginner-friendly pipeline from signal generation through preprocessing, feature extraction, and baseline ML classification.

This repository is intended to support PhD research in Electrical and Computer Engineering at Portland State University. It is not a clinical product, not a production system, and not a validated fall detection tool.

---

## Research Motivation

Contactless sensing using WiFi CSI is being explored for eldercare and healthcare monitoring applications. Potential use cases include:

- fall detection for elderly individuals
- respiration-rate and heart-rate monitoring
- sleep apnea-related monitoring
- continuous vital-sign sensing without wearable devices

WiFi-based sensing is attractive because it is non-invasive, does not require the user to wear any device, and may operate using existing WiFi infrastructure in homes and care facilities.

---

## Why WiFi CSI?

WiFi Channel State Information describes how a wireless signal propagates from a transmitter to a receiver through the environment. Key points:

- CSI captures amplitude and phase information across multiple OFDM subcarriers.
- Human motion, posture changes, breathing, and environmental movement can affect the multipath propagation of WiFi signals.
- These changes in CSI can be analyzed to study human activity and vital-sign-related patterns.
- CSI-based sensing is contactless and can be studied without camera-based monitoring.

---

## Physical-Layer Security Motivation

WiFi CSI is derived from OFDM preamble, training symbols, and pilot subcarriers before higher-layer security mechanisms protect the payload. This creates an underexplored attack surface for WiFi-based sensing systems. If an adversary manipulates the RF channel, injects spoofed signals, or perturbs CSI measurements, the sensing pipeline could be corrupted or degraded even without directly attacking application-layer security controls.

This repository includes a conceptual threat model in `docs/threat_model.md` documenting these risks at a research level.

---

## Current Scope

Version 1 of this repository focuses on:

- generating synthetic CSI-like time-series signals
- simulating two classes: normal activity, class 0, and fall-like events, class 1
- preprocessing time-series signals using smoothing and normalization
- extracting simple statistical features such as mean, standard deviation, energy, peak-to-peak range, maximum value, minimum value, and variance
- training a baseline scikit-learn classifier
- evaluating the workflow using accuracy score and confusion matrix
- documenting limitations and a conceptual physical-layer threat model

**All data used in this version is synthetic and simulated. No real WiFi CSI measurements are used.**

---

## What This Repository Is NOT

This repository is:

- **not** a clinical fall detection system
- **not** trained on real patient data
- **not** clinically validated
- **not** a production ML system
- **not** a medical device or clinical decision support tool
- **not** a deployment-ready application
- **not** a benchmark against real-world WiFi CSI datasets

---

## Repository Structure

```text
wifi-csi-fall-detection/
│
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── references.md              # Research references
├── LICENSE                    # MIT License
├── .gitignore                 # Git ignore rules
│
├── data/
│   └── README.md              # Data disclaimer and description
│
├── notebooks/
│   └── 01_csi_signal_exploration.ipynb  # Main exploration notebook
│
├── src/
│   ├── __init__.py            # Package init
│   ├── simulate_csi.py        # Synthetic signal generation
│   ├── preprocessing.py       # Signal preprocessing functions
│   ├── features.py            # Feature extraction functions
│   └── baseline_model.py      # Baseline ML classifier
│
├── results/
│   └── README.md              # Results disclaimer
│
├── figures/
│   └── README.md              # Figures description
│
└── docs/
    └── threat_model.md        # Conceptual physical-layer threat model
```

---

## Tools Used

- **Python** — primary programming language
- **NumPy** — numerical computing and signal generation
- **Pandas** — feature table creation and data handling
- **Matplotlib** — signal and result visualization
- **SciPy** — signal filtering and preprocessing
- **scikit-learn** — baseline ML classifier, train/test split, and evaluation
- **Jupyter Notebook** — interactive exploration and documentation

> PyTorch may be added later for deep learning-based time-series models after the baseline workflow is complete.

---

## Planned Next Steps

## Development Roadmap

This repository is an early-stage research prototype for exploring WiFi CSI-inspired signal processing, machine-learning workflows, and robustness evaluation for contactless healthcare and aging-in-place sensing. The current version uses synthetic CSI-like data only. It is not a medical device and has not been clinically validated.

### Phase 1 — Research Prototype Foundation

- [x] Create public GitHub repository for WiFi CSI-inspired fall-detection research
- [x] Add synthetic CSI-like signal exploration notebook
- [x] Include basic preprocessing and visualization examples
- [x] Add feature extraction and baseline ML workflow
- [x] Document research motivation, current scope, and limitations
- [x] Add conceptual physical-layer threat model

### Phase 2 — Machine Learning Baseline

- [ ] Improve feature extraction from CSI-like time-series data
- [ ] Compare multiple baseline ML models, such as logistic regression, random forest, SVM, and k-nearest neighbors
- [ ] Add evaluation metrics such as accuracy, precision, recall, F1-score, false alarm rate, and missed detection rate
- [ ] Add clearer visual summaries of model performance
- [ ] Improve notebook explanations for collaborators and non-specialist readers

### Phase 3 — Robustness and Adversarial Evaluation

- [ ] Add controlled noise and signal perturbation experiments
- [ ] Evaluate model performance under signal distortion and environmental variation
- [ ] Add simple adversarial perturbation experiments using simulated CSI-like signals
- [ ] Compare clean versus perturbed model performance
- [ ] Begin mapping ML errors to safety-relevant outcomes such as missed falls and false alerts

### Phase 4 — Clinical-Safety-Aware Metrics

- [ ] Add clinical-safety-oriented evaluation tables
- [ ] Translate model errors into practical safety endpoints, including missed falls per day, false alarms per hour, and time-to-alert delay
- [ ] Include visual summaries connecting ML performance to healthcare monitoring risk
- [ ] Document assumptions, limitations, and validation needs

### Phase 5 — Vital-Sign and Aging-in-Place Extension

- [ ] Extend the roadmap toward respiratory-rate and heart-rate sensing workflows
- [ ] Explore apnea-related monitoring scenarios using CSI-like signal patterns
- [ ] Connect the research direction to passive in-home sensing and aging-in-place applications
- [ ] Identify public datasets or collaboration opportunities for future validation

### Phase 6 — Reproducibility and Collaboration

- [ ] Improve repository structure for external collaborators
- [ ] Add environment setup instructions
- [ ] Add example outputs and figures
- [ ] Add a short technical blog or project page explaining the research in plain language
- [ ] Prepare the repository for future academic collaboration, pilot-study discussion, and publication support

## Current Status

The repository currently provides an early research foundation for WiFi CSI-inspired sensing and machine-learning exploration. The next priority is to strengthen the baseline ML workflow, improve feature extraction, and add robustness evaluation experiments.

---

## Author

**Shahram H. Hesari**  
PhD Candidate, Electrical and Computer Engineering  
Portland State University

---

## License

MIT License. See [LICENSE](LICENSE) for details.
