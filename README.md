# WiFi CSI Fall Detection — Research Prototype

> **Early-stage research prototype** | PhD research in Electrical & Computer Engineering | Portland State University

---

## Project Title

**WiFi CSI-Based Fall Detection: Signal Processing and ML Prototype**

---

## Research Motivation

Falls are a leading cause of injury among older adults. Contactless, privacy-preserving monitoring systems that do not require wearables or cameras offer a promising path toward eldercare safety. WiFi Channel State Information (CSI) provides rich multipath signal data that can be passively extracted from standard 802.11 hardware, making it an accessible substrate for ambient human activity sensing research.

---

## Research Context

This repository supports PhD research in the area of **secure WiFi-based vital sign and activity sensing**, with a focus on:
- Fall detection and eldercare monitoring
- Respiration-rate and heart-rate estimation
- Apnea-related monitoring
- Adversarial robustness and physical-layer security for CSI-based systems

This is an **early-stage, actively evolving prototype**. It is not a finished system. It is being developed as part of coursework and dissertation research while the author is concurrently learning Python and machine learning.

---

## Why WiFi CSI?

WiFi CSI is derived from OFDM preamble symbols, channel training sequences, and pilot subcarriers during the physical-layer channel estimation process — **before higher-layer security mechanisms protect the payload**. This means:

- CSI is inherently accessible at the radio level without encryption barriers
- It reflects fine-grained multipath channel conditions sensitive to body movement
- It does not require wearable sensors or cameras
- It enables passive, ambient monitoring using commodity WiFi infrastructure

This dual-use nature makes CSI-based sensing both powerful for healthcare applications and potentially vulnerable at the physical layer.

---

## Physical-Layer Security Motivation

Because CSI is extracted before cryptographic protections apply, CSI-based sensing systems face an underexplored attack surface:

- **RF channel manipulation** — an adversary could alter the wireless environment to distort CSI
- **Spoofed signal injection** — fabricated 802.11 frames may pollute CSI measurements
- **Synthetic CSI perturbation** — adversarial perturbations could suppress or trigger false detections

Understanding these threats is essential before deploying WiFi sensing in safety-critical healthcare settings. This repository begins to explore these concepts in a synthetic, controlled setting.

---

## Current Scope

This prototype currently:
- Generates **synthetic CSI-like time-series signals** simulating normal activity and fall-like events
- Applies basic signal preprocessing (smoothing, normalization)
- Extracts simple time-series features (mean, std, energy, peak-to-peak, max amplitude)
- Trains a **baseline scikit-learn classifier** (Logistic Regression / Random Forest)
- Evaluates with accuracy score and confusion matrix
- Documents an initial threat model for physical-layer security concepts

> All data used in this repository is **synthetic and simulated**. No real patient, clinical, or private data is used.

---

## Repository Structure

```
wifi-csi-fall-detection/
│
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── references.md                # Research references
├── LICENSE                      # MIT License
├── .gitignore                   # Python .gitignore
│
├── data/
│   └── README.md                # Data policy and notes
│
├── notebooks/
│   └── 01_csi_signal_exploration.ipynb  # Main exploration notebook
│
├── src/
│   ├── simulate_csi.py          # Synthetic CSI signal generation
│   ├── preprocessing.py         # Signal smoothing and normalization
│   ├── features.py              # Time-series feature extraction
│   └── baseline_model.py        # Baseline ML classifier and evaluation
│
├── results/
│   └── README.md                # Results notes
│
├── figures/
│   └── README.md                # Figures from notebooks
│
└── docs/
    └── threat_model.md          # Physical-layer threat model notes
```

---

## Tools Used

| Tool | Purpose |
|---|---|
| Python 3.x | Core programming language |
| NumPy | Numerical computation and signal arrays |
| Pandas | Data organization and feature tables |
| Matplotlib | Signal visualization and plots |
| SciPy | Signal filtering and processing |
| scikit-learn | Baseline ML classification and evaluation |
| Jupyter Notebook | Interactive exploration and documentation |

---

## Planned Next Steps

- [ ] Integrate a small real-world public CSI dataset (e.g., UT-HAR, Widar, or similar — subject to license review)
- [ ] Add CNN or LSTM-based deep learning classifier (PyTorch)
- [ ] Implement adversarial perturbation examples on synthetic CSI
- [ ] Expand threat model with concrete attack simulations
- [ ] Explore federated learning concepts for privacy-preserving multi-site sensing
- [ ] Add cross-validation and more robust evaluation metrics
- [ ] Improve signal simulation with more realistic OFDM-like multipath characteristics

---

## Important Disclaimer

> **This repository is a research prototype. It is not a clinically validated fall detection system and should not be used for medical decision-making.**
>
> All experiments use synthetic, simulated data. Results reported in notebooks are for demonstration and learning purposes only and do not represent real-world clinical performance. This project is part of an academic research and learning process.

---

## Author

PhD Candidate, Electrical & Computer Engineering
Portland State University

*Research areas: WiFi CSI sensing, healthcare AI, physical-layer security, adversarial ML, signal processing*

---

*Last updated: May 2026*
