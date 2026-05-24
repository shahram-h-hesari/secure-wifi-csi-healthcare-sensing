# Related Projects

This document lists open-source projects and academic repositories that are relevant to the research conducted in this repository. These are organized by research area for reference and literature context.

> **Note:** Listings here are for academic reference only. Inclusion does not imply endorsement, validation of claims, or incorporation into this repository's pipeline. See [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) for the full attribution and license policy.

---

## WiFi CSI Sensing and Fall Detection

| Project | Link | Description | Notes |
|---|---|---|---|
| ESP32 CSI Toolkit | — | CSI extraction tools for ESP32 hardware | Hardware-level CSI capture |
| nexmon_csi | — | Nexmon-based CSI extraction for Broadcom/Cypress chips | Widely used in research |
| Widar3.0 | — | Gesture recognition via WiFi CSI | Published academic system |
| WiSe | — | WiFi sensing benchmark dataset | For reproducibility comparison |
| RuView | — | WiFi-based spatial intelligence and vital sign sensing | Open-source reference project/experimental target; included for repo-structure review, simulation workflow study, and planned offline adversarial robustness evaluation. |
| SenseFi / WiFi CSI Sensing Benchmark | https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark | Benchmark framework for deep-learning-based WiFi CSI human sensing. | Useful future baseline framework for testing robustness and adversarial attacks. External reference only. |
| ESP-CSI | https://github.com/espressif/esp-csi | ESP32-based CSI collection and wireless sensing examples. | Useful for future real CSI collection and hardware prototyping. External reference only. |

*This table will be expanded as projects are reviewed and added to `third_party/wifi_sensing/`.*

---

## WiFi Sensing Security and Adversarial Robustness

| Project | Link | Description | Notes |
|---|---|---|---|
| Attack_WiFi_Sensing | https://github.com/Guolin-Yin/Attack_WiFi_Sensing | Adversarial evasion attacks, universal perturbation testing, adversarial training, and robustness evaluation for WiFi sensing models. | Directly relevant to future adversarial robustness evaluation for WiFi CSI-based sensing. External reference only; no code copied. |
| Awesome-WS-Security | https://github.com/Intelligent-Perception-Lab/Awesome-WS-Security | Curated literature and resources on wireless sensing security, attacks, privacy, and defenses. | Useful as a literature map for WiFi sensing security. External reference only. |

*These repositories are referenced for literature review and future robustness evaluation only. No code has been copied or adapted. See `THIRD_PARTY_NOTICES.md` for details.*

---

## Federated Learning and Privacy-Preserving ML

| Project | Description | Notes |
|---|---|---|
| PySyft | Privacy-preserving ML framework | Relevant to future federated learning phase |
| Flower (flwr) | Federated learning framework | Under consideration for Phase 5 |
| OpenDP | Differential privacy library | Relevant to privacy-preserving sensing extensions |

---

## Datasets

| Dataset | Description | Notes |
|---|---|---|
| FallDefi | WiFi-based fall detection dataset | Published research dataset |
| UT-HAR | University of Toronto HAR WiFi dataset | Activity recognition benchmark |
| (TBD) | Additional CSI datasets | To be identified during literature review |

---

*Last updated: May 2026*
