# RuView

> **Third-Party Notice:** RuView is an external open-source project. It is not part of the original work in this repository. All RuView code, claims, and results remain attributed to the original authors at https://github.com/ruvnet/RuView.

---

## Source

- **Original Repository:** https://github.com/ruvnet/RuView
- **Original Authors:** ruvnet and contributors
- **License:** MIT (verified May 2026)
- **Stars at time of inclusion:** ~64.8k

---

## Category

WiFi sensing — real-time spatial intelligence, vital sign monitoring, and presence detection using commodity WiFi signals.

---

## Why This Project Is Included

RuView is included in this repository as a **third-party open-source reference and experimental target** for the following research purposes:

1. Studying WiFi sensing simulation workflows and architecture
2. Reviewing repository structure, data organization, and model file patterns
3. Examining dashboard/interface design approaches for WiFi-based sensing applications
4. Reviewing data and model file organization as a reference for my own PhD research
5. Planning future offline adversarial robustness evaluation experiments against WiFi sensing pipelines

RuView is **not** presented as my original work and is **not** independently validated within this repository.

---

## Relationship to This Repository

This repository (`wifi-csi-fall-detection`) is a WiFi CSI fall-detection research prototype that uses **synthetic CSI-like data only**. RuView is an external project that uses real WiFi hardware and commodity CSI collection methods.

RuView is studied here as an external reference. Its code and documentation are kept strictly separated from this repository's original pipeline:

| This Repository | RuView (Third-Party) |
|---|---|
| `src/` — original pipeline code | `third_party/wifi_sensing/ruview/` — documentation only |
| Synthetic CSI-like data | Real WiFi hardware (ESP32, etc.) |
| Offline research prototype | Active open-source project |
| My original research work | Third-party reference and experimental target |

---

## Current Use

- **Documentation and reference review only** at this time
- RuView code is **not** mixed with the original `src/`, `notebooks/`, or `app.py` code in this repository
- A Git submodule pointing to the original RuView repository is the **preferred** method for including code; see [`SUBMODULE_INSTRUCTIONS.md`](./SUBMODULE_INSTRUCTIONS.md)
- An experiment workspace has been created at `experiments/ruview_adversarial_evaluation/` for future offline evaluation planning

---

## Validation Status

> **Important:** RuView's claims (vital sign monitoring, presence detection, spatial intelligence) are **not independently validated** in this repository. All performance, accuracy, or capability claims in RuView's documentation represent the original authors' claims and have not been reproduced or verified here. No clinical, hardware, or real-world validation is claimed.

---

## Planned Review

See [`REVIEW_NOTES.md`](./REVIEW_NOTES.md) for a structured technical review template.

See [`EXPERIMENT_PLAN.md`](./EXPERIMENT_PLAN.md) for a planned offline adversarial robustness evaluation plan.

---

## Attribution and License

- RuView is licensed under the **MIT License**.
- Original license: https://github.com/ruvnet/RuView/blob/main/LICENSE
- Any code copied or included from RuView remains subject to its original MIT License terms.
- Original license text must be preserved if any code is copied.
- See [`LICENSE_SUMMARY.md`](./LICENSE_SUMMARY.md) for a practical attribution summary.

---

*This file was created as part of Phase 11 of the wifi-csi-fall-detection research prototype repository.*
