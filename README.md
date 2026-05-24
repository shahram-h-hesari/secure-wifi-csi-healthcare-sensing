# Secure WiFi CSI Healthcare Sensing — Research Prototype

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Research%20Prototype-yellow)
![Data](https://img.shields.io/badge/Data-Synthetic%20Only-lightgrey)

> **Disclaimer:** This repository uses **synthetic CSI-like data only**. It does not use real patient data, real clinical data, or validated WiFi CSI hardware measurements. All results are prototype outputs intended to demonstrate a research workflow. This is not a clinical product, a validated fall-detection system, or a medical device.

---

## Project Summary

An end-to-end research prototype exploring **WiFi Channel State Information (CSI)-inspired fall detection and healthcare sensing security** using synthetic signals, signal processing, and machine learning. The project demonstrates a full pipeline from synthetic CSI generation through baseline classification, clinical-safety-aware evaluation, adversarial robustness stress testing, defense methods, and interactive visualization.

Built to support PhD research in **secure WiFi sensing for healthcare IoT** at Portland State University, with emphasis on:
- Adversarial robustness and attack resilience for CSI-based sensing
- Clinical-safety-aware evaluation metrics (missed falls, false alarms)
- Defense taxonomy for physical-layer and ML-layer threats
- Open-source gap analysis in combined healthcare + adversarial CSI research

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
| Defense taxonomy documentation | Implemented |
| Open-source landscape gap analysis | Documented |
| Real CSI hardware data | Future work |
| Clinical validation | Not claimed |
| Hardware deployment | Not claimed |

---

## Open-Source Landscape Gap

A thorough review of public GitHub repositories and academic resources (informed by open-source landscape analysis) reveals a **clear research gap**: no existing public repository fully combines:

1. WiFi CSI-based healthcare sensing (fall detection / vital signs)
2. Adversarial robustness and evasion-attack stress testing
3. Clinical-safety-aware evaluation metrics
4. Defense method taxonomy (preprocessing + model-level)

This repository is positioned to address that gap as a research prototype. See [`docs/open_source_gap.md`](docs/open_source_gap.md) for the full landscape analysis.

**Adjacent open-source projects referenced (external only — no code copied):**

| Project | Area | Notes |
|---|---|---|
| [Attack\_WiFi\_Sensing](https://github.com/Guolin-Yin/Attack_WiFi_Sensing) | Adversarial attacks on WiFi sensing | Core adversarial reference |
| [NoiSec](https://github.com/NoiSec) | Noise-based adversarial defense | Defense taxonomy reference |
| [Awesome-RIS-Security](https://github.com/topics/ris-security) | Physical-layer attack literature | Literature tracker reference |
| [CSI-Bench](https://github.com/topics/csi-benchmark) | Real WiFi sensing benchmark | Future dataset candidate (Pending verification) |
| [unilateral-csi-entropy](https://github.com/topics/csi-entropy) | Edge security / CSI entropy | Cryptographic entropy reference |

> All referenced projects are **external references only**. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/related_projects.md`](docs/related_projects.md) for full attribution.

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/shahram-h-hesari/secure-wifi-csi-healthcare-sensing.git
cd secure-wifi-csi-healthcare-sensing

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the Jupyter notebook
jupyter notebook notebooks/01_csi_signal_exploration.ipynb
```

## Demo Dashboard

An interactive Streamlit dashboard visualizes the full synthetic prototype pipeline.

```bash
streamlit run app.py
```

---

## Repository Structure

```
secure-wifi-csi-healthcare-sensing/
├── data/                        # Synthetic CSI-like data (generated, not real)
├── datasets/                    # Dataset catalog and future dataset roadmap
│   ├── README.md
│   ├── dataset_catalog.md
│   └── future_datasets/         # Candidate real datasets (Pending verification)
├── docs/                        # Research documentation
│   ├── adversarial_robustness.md
│   ├── clinical_safety_metrics.md
│   ├── defense_methods.md
│   ├── open_source_gap.md       # Open-source landscape analysis
│   ├── related_projects.md      # External project references
│   ├── roadmap.md
│   └── project_status.md
├── experiments/                 # Experiment scripts and results
├── notebooks/                   # Jupyter notebooks (pipeline walkthrough)
├── results/                     # Output figures and metrics
├── src/                         # Core source code
├── tests/                       # Unit tests
├── third_party/                 # External reference stubs (no copied code)
│   ├── README.md
│   ├── wifi_sensing/
│   └── wifi_sensing_security/
├── app.py                       # Streamlit dashboard
├── references.md                # Academic and open-source references
├── THIRD_PARTY_NOTICES.md       # Attribution and license notices
└── requirements.txt
```

---

## Research Context

This prototype supports a PhD dissertation focused on:

- **Threat modeling** for WiFi CSI-based healthcare sensing systems
- **Adversarial attack characterization** at the physical and ML layers
- **Clinical-safety impact assessment** of adversarial perturbations
- **Defense method evaluation** under synthetic stress conditions
- **Open-source gap identification** in healthcare-aware adversarial CSI research

See [`docs/research_context.md`](docs/research_context.md) and [`docs/roadmap.md`](docs/roadmap.md) for the full research agenda.

---

## Documentation Index

| Document | Description |
|---|---|
| [docs/adversarial\_robustness.md](docs/adversarial_robustness.md) | Adversarial attack methods and stress testing |
| [docs/clinical\_safety\_metrics.md](docs/clinical_safety_metrics.md) | Clinical-safety evaluation framework |
| [docs/defense\_methods.md](docs/defense_methods.md) | Defense taxonomy (preprocessing + model-level) |
| [docs/open\_source\_gap.md](docs/open_source_gap.md) | Open-source landscape gap analysis |
| [docs/related\_projects.md](docs/related_projects.md) | External project references by research area |
| [docs/roadmap.md](docs/roadmap.md) | Research and development roadmap |
| [docs/project\_status.md](docs/project_status.md) | Current implementation status |
| [docs/threat\_model.md](docs/threat_model.md) | Threat modeling documentation |
| [datasets/dataset\_catalog.md](datasets/dataset_catalog.md) | Dataset catalog and candidate future datasets |
| [references.md](references.md) | Academic and open-source references |
| [THIRD\_PARTY\_NOTICES.md](THIRD_PARTY_NOTICES.md) | Third-party attribution and licenses |

---

## Contributing

This is an active PhD research repository. Contributions, suggestions, and collaborations are welcome, particularly in:
- Real CSI dataset integration (pending IRB/data-access verification)
- Advanced defense method implementations
- Clinical-safety metric extensions
- Cross-layer threat modeling

Please open an issue or contact via GitHub before submitting pull requests.

---

## License

See [LICENSE](LICENSE) for repository license terms.

All third-party references are documented in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). No third-party code or datasets have been copied into this repository.

---

*Built at Portland State University — PhD Research in Secure WiFi Sensing for Healthcare IoT*
