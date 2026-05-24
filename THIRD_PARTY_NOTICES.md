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

## RuView (Placeholder — Pending License Review)

**Project:** RuView — WiFi-based human sensing reference

**Status:** Referenced for literature review only. No code has been copied or adapted yet.

**Action required before inclusion:** Review the project's license to confirm compatibility with this repository's usage. If compatible, any included or adapted code will be placed under `third_party/wifi_sensing/` with full attribution and original license notice preserved.

> Note: This placeholder section will be updated once license review is complete.

---

*Last updated: May 2026*


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
- **Attribution Note:** Any code copied or included from RuView remains subject to its original MIT License terms. Original license text must be preserved if code is copied.
