# Related Projects

This document lists open-source projects and academic repositories that are relevant to the research conducted in this repository. These are organized by research area for reference and literature context.

> **Note:** Listings here are for academic reference only. Inclusion does not imply endorsement, validation of claims, or incorporation into this repository's pipeline. The current implementation uses **synthetic CSI-like data only**. See [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) for the full attribution and license policy.

---

## WiFi Sensing Security / Privacy / Adversarial Robustness

| Project | Link | Description | Relevance | Status |
|---|---|---|---|---|
| Attack_WiFi_Sensing | https://github.com/Guolin-Yin/Attack_WiFi_Sensing | Adversarial evasion attacks, universal perturbation testing, adversarial training, and robustness evaluation for WiFi sensing models. | Core adversarial attack reference for the thesis threat model. | External reference only; no code copied. See `third_party/wifi_sensing_security/attack_wifi_sensing/`. |
| Awesome-WS-Security | https://github.com/Intelligent-Perception-Lab/Awesome-WS-Security | Curated literature and resource list for wireless sensing security, attacks, privacy, and defenses. | Literature survey resource for adversarial WiFi sensing. | External reference only. See `third_party/wifi_sensing_security/awesome_ws_security/`. |
| AntiEave-WiFi-Sensing | https://github.com/MoWiNG-Lab/AntiEave-WiFi-Sensing | Anti-eavesdropping WiFi sensing defense; scheduled spatial sensing against adversarial WiFi sensing (IEEE PerCom 2023). | Defense mechanism reference for privacy-preserving WiFi sensing. | External reference only; no code copied. See `third_party/wifi_sensing_security/antieave_wifi_sensing/`. |
| WiFi-ADG | https://github.com/siwangzhou/WiFi-ADG | Adversarial WiFi sensing for privacy preservation; adversarial CSI data generation to prevent unauthorized behavior recognition (IEEE Communications Letters 2019). | Adversarial data generation reference for the thesis defense pipeline. | External reference only; no code copied. See `third_party/wifi_sensing_security/wifi_adg/`. |
| goop-veil | https://github.com/kobepaw/goop-veil | Software-only WiFi privacy defense: detect, degrade, and document potential CSI surveillance. Apache-2.0. | Relevant to WiFi CSI privacy defense, CSI-based surveillance mitigation, router-side mitigation, and Wi-Spoof-style adversarial sensing threat awareness. Not healthcare-specific. | External reference only; no code copied. Dataset: not confirmed. See `third_party/wifi_sensing_security/goop_veil/`. |

---

## WiFi CSI Sensing / Pose Sensing / Generalization

| Project | Link | Description | Relevance | Status |
|---|---|---|---|---|
| WiFi-CSI-Human-Pose-Detection | https://github.com/euaziel/WiFi-CSI-Human-Pose-Detection | Human pose estimation using WiFi CSI and deep learning — enabling camera-free sensing through walls. GPL-3.0. | Relevant to fall-detection context, through-wall sensing, and robustness/domain-generalization ideas. Not an adversarial attack repo (no adversarial domain generalization confirmed). | External reference only; no code copied. Dataset: pending verification. See `third_party/wifi_sensing/wifi_csi_human_pose_detection/`. |

---

## WiFi CSI Sensing and Benchmark Repositories

| Project | Link | Description | Status |
|---|---|---|---|
| RuView | https://github.com/ruvnet/RuView | WiFi-based spatial intelligence, vital sign monitoring, and presence detection. | External reference and experimental target; included for repo-structure review, simulation workflow study, and planned offline adversarial robustness evaluation. See `third_party/wifi_sensing/ruview/`. |
| SenseFi / WiFi CSI Sensing Benchmark | https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark | Benchmark framework for deep-learning-based WiFi CSI human sensing. | External reference only; useful for future victim-model and robustness evaluation. See `third_party/wifi_sensing/sensefi/`. |
| Widar3.0 | — | Gesture recognition via WiFi CSI. | Published academic system; external reference only. |
| WiSe | — | WiFi sensing benchmark dataset. | External reference only; for reproducibility comparison. |

---

## WiFi CSI Sensing / Fall Detection / Human Activity Recognition Baselines

| Project | Link | Description | Relevance | Status |
|---|---|---|---|---|
| mowa-wifi-sensing | https://github.com/oss-inc/mowa-wifi-sensing | Real-time WiFi CSI-based human activity recognition using Nexmon CSI extractor on Raspberry Pi. Supports supervised learning and meta-learning. BSD-3-Clause. | Fall/HAR baseline reference for future healthcare sensing experiments. Uses Nexmon CSI pipeline relevant to understanding real vs. synthetic CSI gap. Not an adversarial/security repo. | External reference only; no code copied. Dataset: pending verification (real-time Nexmon CSI; possible domain-specific HAR folders). See `third_party/wifi_sensing/mowa_wifi_sensing/`. |

---

## WiFi CSI Sensing / Vital-Sign / Breathing / Apnea Baseline References

| Project | Link | Description | Relevance | Status |
|---|---|---|---|---|
| baby-monitor-wifi-csi (BabyGuard) | https://github.com/mohosy/baby-monitor-wifi-csi | Contactless baby breathing monitor using WiFi CSI and ESP32 — real-time infant apnea detection without wearables or cameras. MIT. | Relevant to WiFi CSI breathing monitoring, apnea-style sensing, contactless healthcare monitoring, and future vital-sign experiments. Not an adversarial/security repo. Not clinically validated by this project. | External reference only; no code copied. Dataset: pending verification. See `third_party/wifi_sensing/baby_monitor_wifi_csi/`. |

---

## WiFi CSI Collection and Hardware Repositories

| Project | Link | Description | Status |
|---|---|---|---|
| ESP-CSI | https://github.com/espressif/esp-csi | ESP32-based CSI collection and wireless sensing examples. | External reference only; useful for future real CSI collection and prototyping. See `third_party/wifi_sensing/esp_csi/`. |
| ESP32 CSI Toolkit | — | CSI extraction tools for ESP32 hardware. | Hardware-level CSI capture; external reference only. |
| nexmon_csi | — | Nexmon-based CSI extraction for Broadcom/Cypress chips. | Widely used in research; external reference only. |

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

*Last updated: 2026-05-24*


---

## WiFi CSI Sensing / Data Augmentation / Robustness Support

| Project | Link | Description | Relevance | Status |
|---|---|---|---|---|
| CsiGAN | https://github.com/ChunjingXiao/CsiGAN | Semi-supervised GAN for robust WiFi CSI-based activity recognition and data augmentation (IEEE IoT Journal, 2019). License: Pending verification (no LICENSE file detected). | Optional robustness/data-augmentation reference for future victim-model experiments; useful for synthetic-to-real CSI variation, class-imbalance experiments, and semi-supervised learning with limited labeled fall/vital-sign data. Not healthcare-specific. Not an adversarial attack/defense repo. | External reference only; no code copied. Dataset: pending verification. See `third_party/wifi_sensing/csigan/`. |

---

*Last updated: 2026-05-24*
