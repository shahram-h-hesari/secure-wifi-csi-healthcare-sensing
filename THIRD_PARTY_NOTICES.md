# Third-Party Notices

This repository may include or reference third-party open-source projects for the following purposes:

- Literature review and academic comparison
- Technical code review and reproducibility testing
- Research inspiration and methodology reference
- Evaluation of sensing pipelines and security approaches

Third-party projects are **not** part of the core fall-detection pipeline of this repository unless explicitly stated.

Third-party claims (e.g., accuracy figures, system performance) are **not** treated as validated unless independently supported by our own experiments.

The current implementation uses **synthetic CSI-like data only**.

---

## License and Attribution Policy

- All third-party code remains under its original license.
- Any code copied or adapted from a third-party project must retain the original attribution and license notices.
- Adapted code will be clearly marked with a comment referencing the original source.
- This repository's MIT License applies only to original work authored by the repository contributors.

---

## Third-Party Projects Referenced

### WiFi Sensing

Projects related to WiFi CSI sensing, activity recognition, fall detection, and related applications are organized under `third_party/wifi_sensing/`.

### WiFi Sensing Security

Projects related to adversarial attacks, CSI spoofing, privacy leakage, physical-layer security, and robustness evaluation are organized under `third_party/wifi_sensing_security/`.

---

### RuView

- **Original Repository:** https://github.com/ruvnet/RuView
- **Original Authors:** ruvnet and contributors
- **License:** MIT (verified May 2026)
- **Category:** WiFi sensing — real-time spatial intelligence, vital sign monitoring, and presence detection
- **Use in This Repository:** Third-party open-source reference and experimental target. Included for repository-structure review, simulation workflow study, dashboard/interface design inspiration, and planned future offline adversarial robustness evaluation.
- **Validation Status:** RuView's claims are **not independently validated** in this repository. No clinical, hardware, or real-world validation is claimed.
- **Code Status:** No RuView code has been copied into this repository. A Git submodule is the preferred method for including code (see `third_party/wifi_sensing/ruview/SUBMODULE_INSTRUCTIONS.md`).
- **Documentation:** `third_party/wifi_sensing/ruview/`
- **Experiment Workspace:** `experiments/ruview_adversarial_evaluation/`
- **Attribution Note:** Any code copied or included from RuView remains subject to its original MIT License terms. Original authors (ruvnet and contributors) must be credited in any derivative or adapted work. License text must be preserved in full.
- **Dataset and validation protocol:** Pending review. RuView's dataset, model provenance, and validation protocol have not yet been independently verified in this repository.
- **Independent validation status:** RuView is not treated as independent validation for this repository. Its inclusion does not imply endorsement of its sensing claims.
- **Future adversarial evaluation:** Any future adversarial evaluation will first document baseline data/model provenance before applying perturbation experiments. See `third_party/wifi_sensing/ruview/REVIEW_NOTES.md` for the full dataset review checklist.

---

### SenseFi / WiFi CSI Sensing Benchmark

- **Original Repository:** https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark
- **Original Authors:** xyanchen and contributors
- **License:** To be verified before any code use
- **Category:** WiFi CSI sensing benchmark — deep-learning-based WiFi CSI human sensing evaluation framework
- **Use in This Repository:** Linked as an external reference for WiFi CSI sensing benchmarks. Useful for future victim-model identification and robustness evaluation planning. Referenced for literature review and future baseline comparison only.
- **Validation Status:** SenseFi's benchmark results and claims are **not independently validated** in this repository.
- **Code Status:** No source code has been copied into this project. Any future code reuse requires verifying the original license and adding proper attribution.
- **Documentation:** `third_party/wifi_sensing/sensefi/README.md`

---

### ESP-CSI

- **Original Repository:** https://github.com/espressif/esp-csi
- **Original Authors:** Espressif Systems and contributors
- **License:** To be verified before any code use (likely Apache 2.0 or similar)
- **Category:** WiFi CSI collection and hardware — ESP32-based CSI extraction and wireless sensing examples
- **Use in This Repository:** Linked as an external reference for ESP32 CSI collection and hardware prototyping. Referenced for literature review and future real CSI collection planning only.
- **Validation Status:** ESP-CSI's examples and results are **not independently validated** in this repository.
- **Code Status:** No source code has been copied into this project. Any future code reuse requires verifying the original license and adding proper attribution.
- **Documentation:** `third_party/wifi_sensing/esp_csi/README.md`

---

### Attack_WiFi_Sensing

- **Original Repository:** https://github.com/Guolin-Yin/Attack_WiFi_Sensing
- **Original Authors:** Guolin Yin and contributors
- **License:** To be verified before any code use
- **Category:** WiFi sensing security — adversarial evasion attacks, universal perturbation testing, adversarial training, and robustness evaluation
- **Use in This Repository:** Linked as an external reference for adversarial attacks and robustness evaluation in WiFi sensing. Referenced for literature review and future adversarial robustness evaluation planning only. No code has been copied or adapted.
- **Validation Status:** Attack_WiFi_Sensing's results and attack claims are **not independently validated** in this repository. Inclusion does not imply that described attacks have been tested against this repository's pipeline.
- **Code Status:** No source code has been copied into this project. Any future code reuse requires verifying the original license and adding proper attribution.
- **Documentation:** `third_party/wifi_sensing_security/attack_wifi_sensing/README.md`

---

### Awesome-WS-Security

- **Original Repository:** https://github.com/Intelligent-Perception-Lab/Awesome-WS-Security
- **Original Authors:** Intelligent Perception Lab and contributors
- **License:** To be verified before any use
- **Category:** WiFi sensing security literature — curated list of papers, tools, and resources on wireless sensing security, attacks, privacy, and defenses
- **Use in This Repository:** Linked as an external reference for wireless sensing security literature and resources. Referenced for literature review and future robustness evaluation scoping only. No code or content has been copied.
- **Validation Status:** Listings and papers in this curated resource are **not independently validated** by this repository. Inclusion does not imply endorsement of any listed paper or tool.
- **Code Status:** No code or content has been copied into this project. Any future reuse requires verifying the original license and adding proper attribution.
- **Documentation:** `third_party/wifi_sensing_security/awesome_ws_security/README.md`

---

### AntiEave-WiFi-Sensing

- **Original Repository:** https://github.com/MoWiNG-Lab/AntiEave-WiFi-Sensing
- **Original Authors:** MoWiNG Lab and contributors
- **License:** To be verified before any code use
- **Category:** WiFi sensing security — anti-eavesdropping defense and scheduled spatial sensing against adversarial WiFi sensing
- **Associated Paper:** Scheduled Spatial Sensing against Adversarial WiFi Sensing (IEEE PerCom 2023)
- **Use in This Repository:** Linked as an external reference for WiFi sensing security, anti-eavesdropping, and adversarial robustness research context. Referenced for literature review and future adversarial robustness evaluation planning only. No code has been copied or adapted.
- **Validation Status:** AntiEave-WiFi-Sensing's results and claims are **not independently validated** in this repository. Inclusion does not imply that described defenses have been tested against this repository's pipeline.
- **Code Status:** No source code has been copied into this project. Any future code reuse requires verifying the original license and adding proper attribution.
- **Documentation:** `third_party/wifi_sensing_security/antieave_wifi_sensing/README.md`
- **Dataset:** Cataloged separately in `datasets/antieave-wifi-sensing/`; dataset files not downloaded or stored.

---

### WiFi-ADG

- **Original Repository:** https://github.com/siwangzhou/WiFi-ADG
- **Original Authors:** Siwang Zhou and contributors
- **License:** To be verified before any code use
- **Category:** WiFi sensing security — adversarial WiFi sensing for privacy preservation of human behaviors; adversarial CSI data generation
- **Associated Paper:** Adversarial WiFi Sensing for Privacy Preservation of Human Behaviors (IEEE Communications Letters, DOI: 10.1109/LCOMM.2019.2952844)
- **Use in This Repository:** Linked as an external reference for adversarial CSI data generation, WiFi sensing privacy preservation, and behavior obfuscation research context. Referenced for literature review and future adversarial robustness evaluation planning only. No code has been copied or adapted.
- **Validation Status:** WiFi-ADG's results and claims are **not independently validated** in this repository. Inclusion does not imply that described adversarial techniques have been tested against this repository's pipeline.
- **Code Status:** No source code has been copied into this project. Any future code reuse requires verifying the original license and adding proper attribution.
- **Documentation:** `third_party/wifi_sensing_security/wifi_adg/README.md`
- **Dataset:** Cataloged separately in `datasets/wifi-adg/`; dataset files not downloaded or stored. Baidu download link is recorded as an upstream-provided reference only.

---

*Last updated: May 2026*


---

### goop-veil

- **Repository Name:** goop-veil
- **GitHub URL:** https://github.com/kobepaw/goop-veil
- **Original Author(s):** kobepaw and contributors
- **License:** Apache-2.0 (verified from upstream `LICENSE` file)
- **Category:** WiFi Sensing Security / Privacy Defense — software-only WiFi CSI surveillance detection, degradation, and documentation tool
- **Status:** External reference only
- **Use in This Repository:** Linked as an external reference for WiFi CSI privacy defense, CSI-based surveillance mitigation, router-side mitigation, and Wi-Spoof-style adversarial sensing threat awareness. Referenced for literature review and future software-only defense framework planning. No code has been copied or adapted.
- **Important Notes:** This repository is not healthcare-specific. No dataset has been confirmed. Not used in current project implementation.
- **Code Status:** No source code has been copied into this project. Any future code reuse requires review of the Apache-2.0 license terms and adding proper attribution.
- **Documentation:** `third_party/wifi_sensing_security/goop_veil/README.md`
- **Dataset:** No public dataset confirmed. Candidate entry added to `datasets/future_datasets/README.md`.

---

### WiFi-CSI-Human-Pose-Detection

- **Repository Name:** WiFi-CSI-Human-Pose-Detection
- **GitHub URL:** https://github.com/euaziel/WiFi-CSI-Human-Pose-Detection
- **Original Author(s):** euaziel (Aziel S.) and contributors
- **License:** GPL-3.0 (verified from upstream repository)
- **Category:** WiFi CSI Sensing / Pose Sensing / Domain Generalization — human pose estimation through walls using WiFi CSI and deep learning
- **Status:** External reference only
- **Placement:** Placed under `third_party/wifi_sensing/` (general sensing) because the upstream repository does not explicitly confirm adversarial domain generalization or adversarial robustness.
- **Use in This Repository:** Linked as an external reference for WiFi CSI human pose estimation, through-wall sensing, fall-detection context, elderly monitoring, and robustness/domain-generalization ideas. No code has been copied or adapted.
- **Important Notes:** Not an adversarial attack repo. Not healthcare-specific or clinically validated. Not used in current project implementation.
- **Code Status:** No source code has been copied into this project. Any future code reuse requires review of the GPL-3.0 copyleft license terms and adding proper attribution.
- **Documentation:** `third_party/wifi_sensing/wifi_csi_human_pose_detection/README.md`
- **Dataset:** Dataset availability pending verification. Candidate entry added to `datasets/future_datasets/README.md`.

---

### mowa-wifi-sensing

- **Repository Name:** mowa-wifi-sensing
- **GitHub URL:** https://github.com/oss-inc/mowa-wifi-sensing
- **Related Fork:** https://github.com/cheeseBG/wifi-sensing
- **Original Author(s):** oss-inc (Jungik Jang, Pio) and contributors
- **License:** BSD-3-Clause (verified from upstream `LICENSE` file)
- **Category:** Healthcare-Relevant WiFi CSI / Fall Detection / Human Activity Recognition Baseline — real-time WiFi CSI HAR using Nexmon CSI extractor
- **Status:** External reference only
- **Use in This Repository:** Linked as an external reference for WiFi CSI HAR baseline research, fall-detection context, and future real-data benchmarking planning. No code has been copied or adapted.
- **Important Notes:** Not an adversarial/security repo. Not healthcare-specific or clinically validated. Not used in current project implementation. Current project uses synthetic CSI-like data only.
- **Code Status:** No source code has been copied into this project. Any future code reuse requires review of the BSD-3-Clause license terms and adding proper attribution.
- **Documentation:** `third_party/wifi_sensing/mowa_wifi_sensing/README.md`
- **Dataset:** Dataset availability pending verification (real-time Nexmon CSI; possible domain-specific HAR folders). Candidate entry added to `datasets/future_datasets/README.md` as `mowa-fall-har`.

---

### baby-monitor-wifi-csi

- **Repository Name:** baby-monitor-wifi-csi (BabyGuard)
- **GitHub URL:** https://github.com/mohosy/baby-monitor-wifi-csi
- **Original Author(s):** mohosy and contributors
- **License:** MIT (verified from upstream repository)
- **Category:** Healthcare-Relevant WiFi CSI / Breathing Monitoring / Apnea-Style Sensing Baseline — contactless infant breathing monitoring via WiFi CSI and ESP32
- **Status:** External reference only
- **Use in This Repository:** Linked as an external reference for WiFi CSI contactless breathing monitoring, apnea-style sensing, and future vital-sign experiment planning. No code has been copied or adapted.
- **Important Notes:** Not an adversarial/security repo. Not clinically validated. This project does not treat this repository as a medical device or clinical reference. Not used in current project implementation. Current project uses synthetic CSI-like data only.
- **Code Status:** No source code has been copied into this project. Any future code reuse requires review of the MIT license terms and adding proper attribution.
- **Documentation:** `third_party/wifi_sensing/baby_monitor_wifi_csi/README.md`
- **Dataset:** Dataset availability unknown. No confirmed public downloadable CSI breathing dataset identified. Candidate entry added to `datasets/future_datasets/README.md`.

---

*Last updated: 2026-05-24*


---

### CsiGAN

- **Repository Name:** CsiGAN
- **GitHub URL:** https://github.com/ChunjingXiao/CsiGAN
- **Original Author(s):** Chunjing Xiao and contributors
- **Associated Paper:** Chunjing Xiao et al. "CsiGAN: Robust Channel State Information-based Activity Recognition with GANs." *IEEE Internet of Things Journal*, 2019.
- **License:** No LICENSE file detected in upstream repository as of 2026-05-24. **License status: Pending verification — do not copy, adapt, or build upon this code until license is confirmed.**
- **Category:** WiFi CSI Sensing / Data Augmentation / Robustness Support
- **Status:** External reference only
- **Use in This Repository:** Linked as an external reference for GAN-based data augmentation in WiFi CSI activity recognition. Potentially relevant for future robustness, class-imbalance, and synthetic-to-real CSI variation experiments. No code has been copied or adapted.
- **Important Notes:** Not a healthcare-specific repository. Not an adversarial attack repository. Not an adversarial defense repository. Not used in the current project implementation. Current project uses synthetic CSI-like data only.
- **Code Status:** No source code has been copied into this project. Any future code reuse requires verifying the upstream license terms and citing the associated IEEE IoT Journal 2019 paper.
- **Documentation:** `third_party/wifi_sensing/csigan/README.md`
- **Dataset:** Dataset/source-data status pending verification. No dataset files are stored in this repository. Candidate entry added to `datasets/future_datasets/README.md`.

---

*Last updated: 2026-05-24*
