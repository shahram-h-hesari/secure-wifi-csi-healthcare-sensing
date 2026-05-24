# Related Projects

This document lists open-source projects and academic repositories that are relevant to the research conducted in this repository. These are organized by research area for reference and literature context.

> **Note:** Listings here are for academic reference only. Inclusion does not imply endorsement, validation of claims, or incorporation into this repository's pipeline. The current implementation uses **synthetic CSI-like data only**. See [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) for the full attribution and license policy.

---

## WiFi CSI Sensing and Benchmark Repositories

| Project | Link | Description | Status |
|---|---|---|---|
| RuView | https://github.com/ruvnet/RuView | WiFi-based spatial intelligence, vital sign monitoring, and presence detection. | External reference and experimental target; included for repo-structure review, simulation workflow study, and planned offline adversarial robustness evaluation. See `third_party/wifi_sensing/ruview/`. |
| SenseFi / WiFi CSI Sensing Benchmark | https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark | Benchmark framework for deep-learning-based WiFi CSI human sensing. | External reference only; useful for future victim-model and robustness evaluation. See `third_party/wifi_sensing/sensefi/`. |
| Widar3.0 | — | Gesture recognition via WiFi CSI. | Published academic system; external reference only. |
| WiSe | — | WiFi sensing benchmark dataset. | External reference only; for reproducibility comparison. |

---

## WiFi CSI Collection and Hardware Repositories

| Project | Link | Description | Status |
|---|---|---|---|
| ESP-CSI | https://github.com/espressif/esp-csi | ESP32-based CSI collection and wireless sensing examples. | External reference only; useful for future real CSI collection and prototyping. See `third_party/wifi_sensing/esp_csi/`. |
| ESP32 CSI Toolkit | — | CSI extraction tools for ESP32 hardware. | Hardware-level CSI capture; external reference only. |
| nexmon_csi | — | Nexmon-based CSI extraction for Broadcom/Cypress chips. | Widely used in research; external reference only. |

---

## WiFi Sensing Security and Adversarial Robustness

| Project | Link | Description | Status |
|---|---|---|---|
| Attack_WiFi_Sensing | https://github.com/Guolin-Yin/Attack_WiFi_Sensing | External repository focused on adversarial evasion attacks, universal perturbation testing, adversarial training, and robustness evaluation for WiFi sensing models. | External reference only; no code copied. See `third_party/wifi_sensing_security/attack_wifi_sensing/`. |
| Awesome-WS-Security | https://github.com/Intelligent-Perception-Lab/Awesome-WS-Security | Curated literature and resource list for wireless sensing security, attacks, privacy, and defenses. | External reference only. See `third_party/wifi_sensing_security/awesome_ws_security/`. |
| AntiEave-WiFi-Sensing | https://github.com/MoWiNG-Lab/AntiEave-WiFi-Sensing | Anti-eavesdropping WiFi sensing defense; scheduled spatial sensing against adversarial WiFi sensing (IEEE PerCom 2023). | External reference only; no code copied. See `third_party/wifi_sensing_security/antieave_wifi_sensing/`. |
| WiFi-ADG | https://github.com/siwangzhou/WiFi-ADG | Adversarial WiFi sensing for privacy preservation of human behaviors; adversarial CSI data generation to prevent unauthorized behavior recognition (IEEE Communications Letters 2019). | External reference only; no code copied. See `third_party/wifi_sensing_security/wifi_adg/`. |

*These repositories are referenced for literature review and future robustness evaluation only. No code has been copied or adapted. See `THIRD_PARTY_NOTICES.md` for details.*

---

## Federated Learning and Privacy-Preserving ML

| Project | Description | Status |
|---|---|---|
| PySyft | Privacy-preserving ML framework. | External reference; relevant to future federated learning phase. |
| Flower (flwr) | Federated learning framework. | External reference; under consideration for Phase 5. |
| OpenDP | Differential privacy library. | External reference; relevant to privacy-preserving sensing extensions. |

---

## Datasets

| Dataset | Description | Status |
|---|---|---|
| FallDefi | WiFi-based fall detection dataset. | Published research dataset; external reference. |
| UT-HAR | University of Toronto HAR WiFi dataset. | Activity recognition benchmark; external reference. |
| (TBD) | Additional CSI datasets. | To be identified during literature review. |

---

*Last updated: May 2026*
