# Related Projects — Secure WiFi CSI Healthcare Sensing Research Prototype

This document lists open-source projects and academic repositories that are relevant to the **Secure WiFi CSI Healthcare Sensing** research conducted in this repository. These are organized by research area for reference and literature context.

> **Note:** All GitHub repos listed here are **external references only**. They are not part of the current pipeline. Inclusion does not imply endorsement, validation of claims, or incorporation into this repository's implementation. The current implementation uses **synthetic CSI-like data only**. See [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) for the full attribution and license policy.

> **Last Updated:** 2025-05-24

---

## WiFi Sensing Security / Privacy / Adversarial Robustness

| Project | Link | Description | Relevance | Status |
|---------|------|-------------|-----------|--------|
| Attack\_WiFi\_Sensing | https://github.com/Guolin-Yin/Attack_WiFi_Sensing | Adversarial evasion attacks, universal perturbation testing, adversarial training, and robustness evaluation for WiFi sensing models. | Core adversarial attack reference for the thesis threat model. | External reference only; no code copied. See `third_party/wifi_sensing_security/attack_wifi_sensing/`. |
| Awesome-WS-Security | https://github.com/Intelligent-Perception-Lab/Awesome-WS-Security | Curated literature and resource list for wireless sensing security, attacks, privacy, and defenses. | Literature survey resource for adversarial WiFi sensing. | External reference only. See `third_party/wifi_sensing_security/awesome_ws_security/`. |
| AntiEave-WiFi-Sensing | https://github.com/MoWING-Lab/AntiEave-WiFi-Sensing | Anti-eavesdropping WiFi sensing defense; scheduled spatial sensing against adversarial WiFi sensing (IEEE PerCom 2023). | Defense mechanism reference for privacy-preserving WiFi sensing. | External reference only; no code copied. See `third_party/wifi_sensing_security/antieave_wifi_sensing/`. |
| WiFi-ADG | https://github.com/siwangzhou/WiFi-ADG | Adversarial WiFi sensing for privacy preservation; adversarial CSI data generation to prevent unauthorized behavior recognition (IEEE Communications Letters 2019). | Adversarial data generation reference for the thesis defense pipeline. | External reference only; no code copied. See `third_party/wifi_sensing_security/wifi_adg/`. |
| goop-veil | https://github.com/kobepaw/goop-veil | Software-only WiFi privacy defense: detect, degrade, and document potential CSI surveillance. Apache-2.0. | Relevant to WiFi CSI privacy defense, CSI-based surveillance mitigation, router-side mitigation, and Wi-Spoof-style adversarial sensing threat awareness. Not healthcare-specific. | External reference only; no code copied. Dataset: not confirmed. See `third_party/wifi_sensing_security/goop_veil/`. |
| NoiSec | https://github.com/noise-lab/noisec | Noise-based adversarial defense and signal obfuscation for wireless sensing. | Defense taxonomy reference: noise injection and signal-layer defense methods. | External reference only; no code copied. License: Pending verification. See `third_party/wifi_sensing_security/noisec/`. |
| Awesome-RIS-Security | https://github.com/topics/ris-security | Curated literature tracker for reconfigurable intelligent surface (RIS) physical-layer attacks and defenses. | Physical-layer attack literature reference for threat model expansion. | External reference only; literature aggregator. License: Pending verification. See `third_party/wifi_sensing_security/awesome_ris_security/`. |
| unilateral-csi-entropy | https://github.com/topics/csi-entropy | CSI-based entropy analysis for edge security and cryptographic key generation. | Cryptographic entropy reference for CSI-layer security discussion. | External reference only; no code copied. License: Pending verification. See `third_party/wifi_sensing_security/unilateral_csi_entropy/`. |

---

## WiFi CSI Sensing / Data Augmentation / Robustness Support

| Project | Link | Description | Relevance | Status |
|---------|------|-------------|-----------|--------|
| CsiGAN | https://github.com/ChunjingXiao/CsiGAN | Semi-supervised GAN for robust WiFi CSI-based activity recognition and data augmentation (IEEE IoT Journal, 2019). | Victim-model experiments and class-imbalance handling in adversarial robustness evaluation. | External reference only; no code copied. License: Pending verification. See `third_party/wifi_sensing/csigan/`. |

---

## WiFi CSI Sensing / Pose Sensing / Generalization

| Project | Link | Description | Relevance | Status |
|---------|------|-------------|-----------|--------|
| WiFi-CSI-Human-Pose-Detection | https://github.com/topics/wifi-csi-pose | Human pose estimation using WiFi CSI and deep learning (GPL-3.0). | Relevant for fall-detection and through-wall sensing contexts; sensing pipeline reference. | External reference only; no code copied. See `third_party/wifi_sensing/wifi_csi_human_pose_detection/`. |

---

## WiFi CSI Sensing and Benchmark Repositories

| Project | Link | Description | Relevance | Status |
|---------|------|-------------|-----------|--------|
| RuView | https://github.com/topics/ruview | WiFi-based spatial intelligence, vital sign monitoring, and presence detection. | Simulation workflow study and planned offline adversarial robustness evaluation. | External reference only. License: Pending verification. |
| CSI-Bench | https://github.com/topics/csi-benchmark | Real WiFi sensing benchmark with standardized evaluation protocols across multiple sensing tasks. | Future dataset candidate for real-data validation phase. | External reference only; no data copied. License: Pending verification. See `datasets/future_datasets/README.md`. |

---

## Open-Source Gap Summary

A review of the above repositories confirms a **clear gap**: no existing public repository fully combines WiFi CSI healthcare sensing with adversarial robustness evaluation, clinical-safety metrics, and a defense taxonomy. See [`docs/open_source_gap.md`](open_source_gap.md) for the full landscape analysis.

---

*This document is maintained as part of the Secure WiFi CSI Healthcare Sensing research prototype at Portland State University.*
