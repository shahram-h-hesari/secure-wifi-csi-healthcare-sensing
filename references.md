# References

This file collects references related to the research areas and software tools used in this repository.

At this stage, this repository is an early synthetic-data research prototype. The code is not a reproduction or implementation of any specific WiFi CSI sensing paper. Research references for WiFi CSI sensing, fall detection, physical-layer security, and adversarial robustness will be expanded as the literature review develops.

> **Note:** References below motivate research directions and future work. The current pipeline uses **synthetic CSI-like data only**. Cited papers are included for literature context and do not imply implementation or validation in this repository.

> **Last Updated:** 2025-05-24

---

## WiFi CSI Sensing

*To be expanded* — foundational and recent papers on WiFi CSI sensing will be included after review.

**Key related repositories (external references only):**
- MM-Fi Dataset: Multi-modal CSI HAR benchmark
- Widar 3.0: Large-scale WiFi CSI dataset
- UT-HAR: Human activity recognition benchmark
- SignFi: Gesture recognition dataset

---

## Fall Detection and Healthcare Sensing

*To be expanded* — papers on contactless fall detection, healthcare sensing, and vital-sign monitoring will be included after review.

**Key related areas:**
- WiFi CSI-based fall detection (FallDeFi and related)
- Vital sign monitoring via CSI (respiration, HR/RR)
- Apnea detection using WiFi signals

---

## Physical-Layer Security and Adversarial Robustness

> **Note:** The papers listed below motivate future work in this repository. They are not implemented in the current codebase. The current pipeline uses synthetic CSI-like data only. These references are included for literature context and to guide planned adversarial robustness evaluation.

- **[1]** Yin, G., et al. "Practical Adversarial Attacks on WiFi Sensing Through Unnoticeable Communication Packet Perturbation." *ACM MobiCom 2023*.
  - Related repository: https://github.com/Guolin-Yin/Attack_WiFi_Sensing

- **[2]** (Author TBD). "Curated Resources for Wireless Sensing Security."
  - Related repository: https://github.com/Intelligent-Perception-Lab/Awesome-WS-Security

- **[3]** (Author TBD). "Scheduled Spatial Sensing against Adversarial WiFi Sensing." *IEEE PerCom 2023*.
  - Related repository: https://github.com/MoWiNG-Lab/AntiEave-WiFi-Sensing

- **[4]** Zhou, S., et al. "Adversarial WiFi Sensing for Privacy Preservation of Human Behaviors." *IEEE Communications Letters*, 2019.
  - Related repository: https://github.com/siwangzhou/WiFi-ADG

- **[5]** (Author TBD). "Noise-Based Adversarial Defense for WiFi Sensing." *(Pending citation verification)*
  - Related repository: NoiSec (https://github.com/noise-lab/noisec)
  - Note: Identified via open-source landscape analysis (Gemini report 2025). Citation and URL require independent verification.

- **[6]** (Author TBD). "Physical-Layer Attacks and Defenses for Reconfigurable Intelligent Surfaces (RIS)." *(Pending citation verification)*
  - Related resource: Awesome-RIS-Security (literature tracker)
  - Note: Identified via open-source landscape analysis (Gemini report 2025). Citation and URL require independent verification.

- **[7]** (Author TBD). "CSI-Based Entropy Analysis for Edge Security and Cryptographic Key Generation." *(Pending citation verification)*
  - Related repository: unilateral-csi-entropy
  - Note: Identified via open-source landscape analysis (Gemini report 2025). Citation and URL require independent verification.

---

## Data Augmentation and Generative Models

- **[8]** Xiao, C., et al. "CsiGAN: Robust Channel State Information-Based Activity Recognition with GANs." *IEEE Internet of Things Journal*, 2019.
  - Related repository: https://github.com/ChunjingXiao/CsiGAN
  - Note: License pending verification.

---

## Benchmarks and Datasets

> **Note:** Datasets listed below are future candidates only. None are currently downloaded, integrated, or validated in this repository.

- **CSI-Bench:** Real WiFi sensing benchmark with standardized evaluation protocols.
  - Status: Pending verification (URL, license, access method)
  - Note: Identified via open-source landscape analysis (Gemini report 2025). High-priority future dataset candidate.
  - See: `datasets/future_datasets/README.md`

- **MM-Fi Dataset:** Multi-modal CSI HAR benchmark (WiFi + radar + vision). Academic release.
  - Status: Future dataset candidate

- **Widar 3.0:** Large-scale WiFi CSI gesture and activity recognition dataset.
  - Status: Future dataset candidate

---

## Open-Source Landscape Analysis

A comprehensive review of the open-source landscape was conducted to identify related repositories and characterize the research gap. Key findings:

- No existing public repository fully combines WiFi CSI healthcare sensing with adversarial robustness and clinical-safety evaluation.
- Adjacent resources (CSI-Bench, NoiSec, Awesome-RIS-Security, unilateral-csi-entropy) are identified as candidate references but are not yet fully verified.
- The gap analysis is documented in [`docs/open_source_gap.md`](docs/open_source_gap.md).

---

## Software and Tools

- Python 3.10+
- NumPy, SciPy, scikit-learn, pandas
- Matplotlib, Seaborn
- Streamlit (interactive dashboard)
- Jupyter Notebooks

---

*References will be expanded as the literature review and implementation develop. All external references are documented in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).*
