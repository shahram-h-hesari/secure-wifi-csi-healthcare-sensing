# WiFi CSI Fall Detection Research Prototype

> **Disclaimer:** This repository currently uses synthetic CSI-like time-series data for demonstration purposes. It does not use real patient data, real clinical data, or validated WiFi CSI measurements. Results are intended only to demonstrate the research workflow and should not be interpreted as clinical or real-world fall detection performance.

---

## Overview

This is an early-stage research prototype exploring WiFi Channel State Information (CSI)-inspired fall detection using synthetic CSI-like signals, signal processing, and machine learning workflows. The goal is to demonstrate a clean, beginner-friendly pipeline from signal generation through baseline ML classification.

This repository is intended to support PhD research in Electrical and Computer Engineering at Portland State University. It is not a clinical product, not a production system, and not a validated fall detection tool.

---

## Research Motivation

Contactless sensing using WiFi CSI is being actively explored for eldercare and healthcare monitoring applications. Potential use cases include:

- Fall detection for elderly individuals
- Respiration-rate and heart-rate monitoring
- Sleep apnea-related monitoring
- Continuous vital-sign sensing without wearable devices

WiFi-based sensing is attractive because it is non-invasive, does not require the user to wear any device, and can operate using existing WiFi infrastructure in homes and care facilities.

---

## Why WiFi CSI?

WiFi Channel State Information (CSI) describes how a wireless signal propagates from a transmitter to a receiver through the environment. Key points:

- CSI captures amplitude and phase information across multiple OFDM subcarriers.
- Human motion — such as walking, falling, or breathing — changes the multipath propagation of WiFi signals.
- These changes in CSI can be analyzed to infer information about human activity and vital signs.
- CSI-based sensing is contactless and does not require dedicated hardware beyond a standard WiFi setup.

---

## Physical-Layer Security Motivation

WiFi CSI is derived from OFDM preamble, training symbols, and pilot subcarriers before higher-layer security mechanisms protect the payload. This creates an underexplored attack surface for WiFi-based sensing systems. If an adversary manipulates the RF channel, injects spoofed signals, or perturbs CSI measurements, the sensing pipeline could be corrupted or degraded even without directly attacking application-layer security controls.

This repository includes a conceptual threat model in `docs/threat_model.md` documenting these risks at a research level.

---

## Current Scope

Version 1 of this repository focuses on:

- Generating synthetic CSI-like time-series signals
- Simulating two classes: normal activity (class 0) and fall-like events (class 1)
- Preprocessing time-series signals (smoothing and normalization)
- Extracting simple statistical features (mean, std, energy, peak-to-peak range, max, min, variance)
- Training a baseline scikit-learn classifier (Logistic Regression or Random Forest)
- Evaluating with accuracy score and confusion matrix
- Documenting limitations and a conceptual threat-model

**All data used in this version is synthetic and simulated. No real WiFi CSI measurements are used.**

---

## What This Repository Is NOT

- **Not** a clinical fall detection system
- **Not** trained on real patient data
- **Not** clinically validated
- **Not** a production ML system
- **Not** a medical device or clinical decision support tool
- **Not** a deployment-ready application
- **Not** a benchmark against real-world WiFi CSI datasets

---

## Repository Structure

```
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
- **scikit-learn** — baseline ML classifier, train/test split, evaluation
- **Jupyter Notebook** — interactive exploration and documentation

> PyTorch may be added later for deep learning-based time-series models after the baseline workflow is complete.

---

## Planned Next Steps

- Add real public WiFi CSI dataset if available and properly licensed
- Improve preprocessing pipeline
- Add more feature extraction methods
- Compare multiple baseline classifiers
- Add synthetic perturbation experiments
- Add adversarial robustness analysis
- Add PyTorch time-series model as a future extension
- Document all limitations carefully

> Future versions may add real public WiFi CSI datasets if they are publicly available, properly licensed, and ethically appropriate.

---

## Author

**Shahram H. Hesari**  
PhD Candidate, Electrical and Computer Engineering  
Portland State University

---

## License

MIT License. See [LICENSE](LICENSE) for details.
