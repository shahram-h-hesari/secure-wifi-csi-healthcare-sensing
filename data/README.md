# Data Folder

## Data Policy

**No real clinical, private, or patient data is included in this repository.**

This folder is reserved for datasets used in experiments. All current examples use **synthetic, simulated CSI-like data** generated programmatically in the notebook and source files.

---

## Current Data

- All data used in the current version of this repository is **synthetically generated** using NumPy.
- Synthetic data simulates basic CSI-like time-series patterns for two classes:
  - Normal activity
  - Fall-like event
- This data is created on-the-fly in `notebooks/01_csi_signal_exploration.ipynb` and `src/simulate_csi.py`.
- It does **not** represent real-world WiFi channel measurements, patient data, or clinical recordings.

---

## Future Data

Real CSI datasets may be incorporated in future versions of this repository **only if**:

1. The dataset is publicly available and properly licensed for research use.
2. The dataset does not contain personally identifiable information (PII) or protected health information (PHI).
3. The dataset is ethically appropriate for use and consistent with IRB/ethical research guidelines.
4. Clear attribution and licensing documentation is included.

Potential future public datasets under consideration (subject to license review):
- UT-HAR (University of Toronto Human Activity Recognition)
- Widar 3.0 (Tsinghua University CSI gesture dataset)
- Other publicly available WiFi sensing benchmarks

---

## Important Disclaimer

> This repository does not contain, process, or store real patient data. It is not a clinical system. All current experiments are based on synthetic, simulated data for research and learning purposes only.
