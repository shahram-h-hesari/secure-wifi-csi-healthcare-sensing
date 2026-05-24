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
  - 
- **[3]** (Author TBD). "Scheduled Spatial Sensing against Adversarial WiFi Sensing." *IEEE PerCom 2023*.
  - Paper page: https://www.computer.org/csdl/proceedings-article/percom/2023/10099079/1MrG8Bbqka4
  - Related repository: https://github.com/MoWiNG-Lab/AntiEave-WiFi-Sensing
  - Relevant to anti-eavesdropping countermeasures and adversarial WiFi sensing defenses. Related to: `third_party/wifi_sensing_security/antieave_wifi_sensing/`, `datasets/antieave-wifi-sensing/`.

- **[4]** Zhou, S., et al. "Adversarial WiFi Sensing for Privacy Preservation of Human Behaviors." *IEEE Communications Letters*, 2019. DOI: https://doi.org/10.1109/LCOMM.2019.2952844
  - Related repository: https://github.com/siwangzhou/WiFi-ADG
  - Relevant to adversarial CSI modification and privacy preservation of human behaviors. Related to: `third_party/wifi_sensing_security/wifi_adg/`, `datasets/wifi-adg/`.

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


---

## GitHub Repository References (Added 2026-05-24)

The following GitHub repositories have been added as external references to `third_party/`. These are tool and code repository references, not formal academic citations. They are listed here for completeness and future citation planning.

> **Note:** Formal paper citations for these repositories are pending verification. If an upstream publication is confirmed, references will be updated with the proper citation. Do not treat repository links as peer-reviewed citations.

---

### WiFi Sensing Security / Privacy Defense

- **goop-veil** — kobepaw. *goop-veil: Software-only WiFi privacy defense: detect, degrade, and document potential CSI surveillance.* GitHub repository. https://github.com/kobepaw/goop-veil. License: Apache-2.0. (Accessed 2026-05-24. External reference only. Formal paper citation: Pending verification.)
  - See `third_party/wifi_sensing_security/goop_veil/`.
  - Relevance: WiFi CSI privacy defense, CSI-based surveillance threat awareness, router-side mitigation, software-only adversarial sensing defense.

---

### WiFi CSI Sensing / Pose Sensing / Domain Generalization

- **WiFi-CSI-Human-Pose-Detection** — euaziel (Aziel S.). *WiFi-CSI-Human-Pose-Detection: Human pose estimation using WiFi Channel State Information (CSI) and deep learning — enabling camera-free sensing through walls.* GitHub repository. https://github.com/euaziel/WiFi-CSI-Human-Pose-Detection. License: GPL-3.0. (Accessed 2026-05-24. External reference only. Formal paper citation: Pending verification.)
  - See `third_party/wifi_sensing/wifi_csi_human_pose_detection/`.
  - Relevance: WiFi CSI human pose estimation, through-wall sensing, fall-detection context, domain generalization. Not classified as adversarial attack repo.

---

### WiFi CSI Fall Detection / Human Activity Recognition Baselines

- **mowa-wifi-sensing** — oss-inc (Jungik Jang, Pio). *mowa-wifi-sensing: Wi-Fi sensing model of MOWA — real-time WiFi CSI-based HAR using Nexmon CSI extractor.* GitHub repository. https://github.com/oss-inc/mowa-wifi-sensing. License: BSD-3-Clause. (Accessed 2026-05-24. External reference only. Formal paper citation: Pending verification.)
  - Related fork: https://github.com/cheeseBG/wifi-sensing
  - See `third_party/wifi_sensing/mowa_wifi_sensing/`.
  - Relevance: WiFi CSI HAR and fall-detection baseline, Nexmon CSI pipeline, meta-learning for WiFi sensing.

---

### WiFi CSI Vital-Sign / Breathing / Apnea Sensing Baselines

- **baby-monitor-wifi-csi (BabyGuard)** — mohosy. *baby-monitor-wifi-csi: Contactless baby breathing monitor using WiFi Channel State Information (CSI). Turns an ESP32 + any WiFi router into a real-time infant apnea detection system — no wearables or cameras needed.* GitHub repository. https://github.com/mohosy/baby-monitor-wifi-csi. License: MIT. (Accessed 2026-05-24. External reference only. Formal paper citation: Pending verification.)
  - See `third_party/wifi_sensing/baby_monitor_wifi_csi/`.
  - Relevance: WiFi CSI contactless breathing monitoring, apnea-style sensing, healthcare-relevant vital-sign baseline.

---

> **Important note on adversarial WiFi sensing papers without confirmed public GitHub:** Major adversarial WiFi sensing papers that do not have confirmed public GitHub repositories remain in the literature references sections above and should not be added as `third_party/` folders. Only repositories with confirmed GitHub URLs are tracked in `third_party/`.

---

*Last updated: 2026-05-24*
