# Attack_WiFi_Sensing

> **Third-Party Notice:** Attack_WiFi_Sensing is an external open-source project. It is not part of the original work in this repository. All code, claims, and results remain attributed to the original authors at https://github.com/Guolin-Yin/Attack_WiFi_Sensing.

---

## Source

- **Original Repository:** https://github.com/Guolin-Yin/Attack_WiFi_Sensing
- **Original Authors:** Guolin Yin and contributors
- **License:** To be verified before any code use

---

## Category

WiFi sensing security — adversarial evasion attacks, universal perturbation testing, adversarial training, and robustness evaluation for WiFi sensing models.

---

## Why This Project Is Included

Attack_WiFi_Sensing is included in this repository as a **third-party open-source external reference** for the following research purposes:

1. Literature review of adversarial attack methodologies applied to WiFi sensing
2. Understanding adversarial evasion and universal perturbation approaches for CSI-based models
3. Planning future adversarial robustness evaluation experiments for WiFi CSI fall-detection models
4. Identifying attack strategies relevant to the physical-layer security threat model
5. Reference for future adversarial training and defense design

This project is **not** presented as original work and is **not** independently validated within this repository.

---

## Relationship to This Repository

This repository (`wifi-csi-fall-detection`) is a WiFi CSI fall-detection research prototype that uses **synthetic CSI-like data only**. Attack_WiFi_Sensing focuses on adversarial attacks against real WiFi sensing models.

| This Repository | Attack_WiFi_Sensing (Third-Party) |
|---|---|
| `src/` — original pipeline code | `third_party/wifi_sensing_security/attack_wifi_sensing/` — documentation only |
| Synthetic CSI-like data | Adversarial perturbations for real WiFi sensing |
| Offline research prototype | Adversarial attack framework |
| My original research work | Third-party adversarial attack reference |

---

## Current Use

- **Documentation and reference review only** at this time
- No Attack_WiFi_Sensing code has been copied, adapted, or mixed with the original `src/`, `notebooks/`, or `app.py` code in this repository
- Any future code reuse requires **license review and proper attribution**
- No Git submodule has been added; this folder serves as a placeholder and reference note only

---

## Validation Status

> **Important:** Attack_WiFi_Sensing's results and attack claims are **not independently validated** in this repository. All performance, accuracy, or attack-success claims in its documentation represent the original authors' claims and have not been reproduced or verified here. Inclusion of this reference does **not** imply that the attacks described have been tested against this repository's pipeline.

---

## License and Attribution

- The license of this repository must be verified independently before any code reuse.
- **No source code has been copied or adapted from Attack_WiFi_Sensing into this project.**
- Any future code reuse requires: (1) verifying the original license, (2) preserving the original license text, and (3) adding proper attribution in the relevant source files and `THIRD_PARTY_NOTICES.md`.
- See the repository root `THIRD_PARTY_NOTICES.md` for the full attribution and license policy.

---

*This file was created as part of the wifi-csi-fall-detection research prototype repository to track external WiFi sensing security references.*
