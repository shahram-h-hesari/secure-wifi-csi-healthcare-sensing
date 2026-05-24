# Third-Party Notices

This repository may include or reference third-party open-source projects for the following purposes:

- Literature review and academic comparison
- Technical code review and reproducibility testing
- Research inspiration and methodology reference
- Evaluation of sensing pipelines and security approaches

Third-party projects are **not** part of the core fall-detection pipeline of this repository unless explicitly stated.

Third-party claims (e.g., accuracy figures, system performance) are **not** treated as validated unless independently supported by our own experiments.

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

### Attack_WiFi_Sensing

- **Original Repository:** https://github.com/Guolin-Yin/Attack_WiFi_Sensing
- **Original Authors:** Guolin Yin and contributors
- **License:** To be verified before any code use
- **Category:** WiFi sensing security — adversarial evasion attacks, universal perturbation testing, adversarial training, and robustness evaluation
- **Use in This Repository:** Referenced for literature review and future adversarial robustness evaluation planning only. No code has been copied or adapted into this repository.
- **Validation Status:** Claims from this repository are **not independently validated** here. Its inclusion does not imply endorsement of its results.
- **Code Status:** No code copied. License review must be completed before any code is adapted or incorporated.
- **Documentation:** To be added under `third_party/wifi_sensing_security/` after license review.

---

### Awesome-WS-Security

- **Original Repository:** https://github.com/Intelligent-Perception-Lab/Awesome-WS-Security
- **Original Authors:** Intelligent Perception Lab and contributors
- **License:** To be verified before any use
- **Category:** WiFi sensing security — curated literature and resources on wireless sensing security, attacks, privacy, and defenses
- **Use in This Repository:** Referenced as a literature map for WiFi sensing security research. Used for literature review and future robustness evaluation scoping only. No code or content has been copied.
- **Validation Status:** Listings in this curated repository are **not independently validated** by this repository.
- **Code Status:** No code copied. This is a reference/literature-tracking resource only.
- **Documentation:** To be added under `third_party/wifi_sensing_security/` after review.

---

*Last updated: May 2026*
