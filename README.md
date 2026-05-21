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

Future versions may:

- improve the preprocessing pipeline
- add more feature extraction methods
- compare multiple baseline scikit-learn classifiers
- add synthetic perturbation experiments
- add adversarial robustness analysis using simulated perturbations
- add real public WiFi CSI datasets if they are publicly available, properly licensed, and ethically appropriate
- document all limitations carefully as the repository develops

---

## Author

**Shahram H. Hesari**  
PhD Candidate, Electrical and Computer Engineering  
Portland State University

---

## License

MIT License. See [LICENSE](LICENSE) for details.
