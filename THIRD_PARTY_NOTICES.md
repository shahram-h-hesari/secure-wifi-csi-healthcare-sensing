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

*Last updated: May 2026*
