# References

This file collects references related to the research areas and software tools used in this repository.

At this stage, this repository is an early synthetic-data research prototype. The code is not a reproduction or implementation of any specific WiFi CSI sensing paper. Research references for WiFi CSI sensing, fall detection, physical-layer security, and adversarial robustness will be added later as the literature review develops.

> References will be expanded as the repository develops.

---

## WiFi CSI Sensing

To be added — foundational and recent papers on WiFi CSI sensing will be included after review.

---

## Fall Detection and Healthcare Sensing

To be added — papers on contactless fall detection, healthcare sensing, and vital-sign monitoring will be included after review.

---

## Physical-Layer Security and Adversarial Robustness

> **Note:** The papers listed below motivate future work in this repository. They are not implemented in the current codebase. The current pipeline uses synthetic CSI-like data only. These references are included for literature context and to guide planned adversarial robustness evaluation.

- **[1]** Yin, G., et al. "Practical Adversarial Attacks on WiFi Sensing Through Unnoticeable Communication Packet Perturbation." *ACM MobiCom 2024*.
  - Highly relevant to physical-domain attacks on WiFi sensing and CSI/preamble perturbation. Related to: `docs/adversarial_robustness.md`, planned robustness evaluation.

- **[2]** (Author TBD). "Adversarial Attack and Defense for WiFi-Based Apnea Detection Systems." *IEEE INFOCOM 2023*.
  - Highly relevant to healthcare WiFi sensing, apnea monitoring, adversarial ML, and clinical-safety motivation. Related to: `docs/clinical_safety_metrics.md`, `docs/security_motivation.md`.

Additional papers on physical-layer security, adversarial robustness, spoofing, and secure WiFi sensing will be added after full literature review.

---

## Signal Processing and Machine Learning Tools Used in This Repository

- **1. Scikit-learn:** Pedregosa, F., et al. (2011). *Machine learning in Python.* Journal of Machine Learning Research, 12, 2825–2830. https://jmlr.org/papers/v12/pedregosa11a.html
- **2. SciPy:** Virtanen, P., et al. (2020). *Fundamental algorithms for scientific computing in Python.* Nature Methods, 17, 261–272. https://doi.org/10.1038/s41592-019-0686-2
- **3. NumPy:** Harris, C. R., et al. (2020). *Array programming with NumPy.* Nature, 585, 357–362. https://doi.org/10.1038/s41586-020-2649-2

---

## Author

**Shahram H. Hesari**
PhD Candidate, Electrical and Computer Engineering
Portland State University
