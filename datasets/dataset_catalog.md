# Dataset Catalog — Secure WiFi CSI Healthcare Sensing Research Prototype

## Overview

This catalog lists public and research WiFi CSI datasets that are relevant to the `secure-wifi-csi-healthcare-sensing` repository. Entries are included for reference, citation planning, and future real-data integration.

**Important:** Inclusion in this catalog does **not** mean a dataset is currently used by this repository. Current experiments use **synthetic CSI-like data only**. Real-data integration is future work.

> Official dataset links are provided for convenience and reproducibility planning. Dataset files are not stored in this repository.

---

## Confirmed Cataloged Dataset Table

The following datasets have full dataset cards in this repository. All are **cataloged only** and are **not integrated** into the current pipeline.

| Dataset | Official Source | Modality | Primary Task | Format | Status in This Repo | Notes |
|---------|----------------|----------|-------------|--------|--------------------|---------|
| MM-Fi | [Project page](https://ntu-aiot-lab.github.io/mm-fi) \| [GitHub/tooling](https://github.com/ybhbingo/MMFi_dataset) \| [Paper](https://openreview.net/forum?id=1uAsASS1th) | WiFi CSI + multi-modal (pending verification) | Human sensing / pose / activity-related research | .npy (mentioned in RuView docs; verify officially) | Cataloged only; not integrated | Related to WiFi CSI sensing; not claimed as fall-detection validation here |
| Wi-Pose | [GitHub dataset repo](https://github.com/NjtechCVLab/Wi-PoseDataset) \| [CSI-Former paper](https://www.mdpi.com/1099-4300/25/1/20) | WiFi CSI with pose-related annotations (pending verification) | WiFi-based pose estimation | .mat (mentioned in RuView docs; verify officially) | Cataloged only; not integrated | Related to WiFi CSI sensing; not claimed as fall-detection validation here |
| SignFi | [GitHub dataset repo](https://github.com/yichenwang231/SignFi) \| [Paper](https://dl.acm.org/doi/10.1145/3161189) | WiFi CSI | Sign language gesture recognition | .mat (pending verification) | Cataloged only; not integrated | WiFi CSI sensing reference; not fall-detection; tracked for future robustness benchmarking |
| Widar | [GitHub dataset repo](https://github.com/Harlinn/widar3.0) \| [Official page](http://tns.thss.tsinghua.edu.cn/widar3.0/) \| [Paper](https://dl.acm.org/doi/10.1145/3307334.3326081) | WiFi CSI | Gesture recognition / cross-domain WiFi sensing | .mat (pending verification) | Cataloged only; not integrated | WiFi CSI sensing reference; cross-domain; tracked for future robustness benchmarking |
| UT-HAR | [SenseFi Benchmark](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark) \| [Paper](https://ieeexplore.ieee.org/document/8067693) | WiFi CSI | Human activity recognition (includes fall class) | Pending verification | Cataloged only; not integrated | Tracked via SenseFi; fall class may be relevant to benchmarking; license pending |
| NTU-Fi HAR | [SenseFi Benchmark](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark) | WiFi CSI | Human activity recognition | Pending verification | Cataloged only; not integrated | Tracked via SenseFi; may be relevant for future comparative benchmarking; license pending |
| NTU-Fi HumanID | [SenseFi Benchmark](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark) | WiFi CSI | Human identification via WiFi | Pending verification | Cataloged only; not integrated | Tracked via SenseFi; adversarial robustness relevance; license pending |
| AntiEave-WiFi-Sensing Dataset | [Official GitHub repository](https://github.com/MoWiNG-Lab/AntiEave-WiFi-Sensing) \| [Paper](https://www.computer.org/csdl/proceedings-article/percom/2023/10099079/1MrG8Bbqka4) | WiFi sensing / CSI-related | Adversarial WiFi sensing / anti-eavesdropping (IEEE PerCom 2023) | Pending verification | Cataloged only; not downloaded; not integrated | Not a fall-detection dataset; not healthcare-specific; WiFi sensing cybersecurity/privacy context; related repo: `third_party/wifi_sensing_security/antieave_wifi_sensing/` |
| WiFi-ADG Dataset | [Official GitHub repository](https://github.com/siwangzhou/WiFi-ADG) \| [Paper DOI](https://doi.org/10.1109/LCOMM.2019.2952844) | WiFi CSI | Adversarial WiFi sensing / privacy-preserving human behavior (IEEE Comm. Letters 2019) | .mat (pending verification) | Cataloged only; not downloaded; not integrated | Not a fall-detection dataset; not healthcare-specific; WiFi sensing cybersecurity/adversarial robustness context; related repo: `third_party/wifi_sensing_security/wifi_adg/` |

> **Note:** All dataset details must be verified from official dataset pages or papers before use. Do not treat unverified fields as authoritative. Links point to official or associated sources and do not mean data are stored in this repository.

---

## Current Integration Status

| Dataset | Official Links Added | Downloaded Locally | Integrated in Pipeline | Used for Validation | Used for Benchmarking |
|---------|---------------------|-------------------|----------------------|--------------------|-----------------------|
| MM-Fi | Yes | No | No | No | No |
| Wi-Pose | Yes | No | No | No | No |
| SignFi | Yes | No | No | No | No |
| Widar | Yes | No | No | No | No |
| UT-HAR | Pending | No | No | No | No |
| NTU-Fi HAR | Pending | No | No | No | No |
| NTU-Fi HumanID | Pending | No | No | No | No |
| AntiEave-WiFi-Sensing Dataset | Yes | No | No | No | No |
| WiFi-ADG Dataset | Yes | No | No | No | No |

All experiments currently use **synthetic CSI-like data**. This will be updated as real-data integration progresses.

---

## Notes on Dataset Validation

- Inclusion of a dataset in this catalog does **not** imply clinical validation.
- Inclusion does **not** imply fall-detection validation.
- Dataset claims (accuracy, performance, subject counts) are **not independently verified** by this repository.
- MM-Fi and Wi-Pose are categorized as **related datasets** — not as current validation sources.
- Any future integration will require: license review, data verification, baseline documentation, and citation compliance.

---

## Candidate / Future Dataset Sources

The following entries are **candidate dataset sources** associated with newly tracked third-party repositories. None of these are confirmed datasets with verified access. They are tracked here for future investigation only. All are marked **Pending verification**. No data has been downloaded or used.

> **Important:** These are not validated datasets. They are tracking placeholders for future work. The current implementation uses synthetic CSI-like data only. Do not treat these as training, validation, or benchmarking sources.

| Candidate Name | Related Repo | GitHub | Task Relevance | Fall-Detection Relevance | Vital-Sign / Apnea Relevance | Dataset Availability | License Status | Action Needed |
|---------------|-------------|--------|---------------|------------------------|------------------------------|--------------------|--------------|--------------|
| mowa-fall-har candidate CSI data | `third_party/wifi_sensing/mowa_wifi_sensing/` | [mowa-wifi-sensing](https://github.com/oss-inc/mowa-wifi-sensing) | Fall detection and human activity recognition baseline; Nexmon CSI pipeline | Possible — pending verification | Not applicable | Pending verification | Repo: BSD-3-Clause; Dataset: pending verification | Inspect upstream for dataset folders or download links; verify fall-related activity classes; do not create full dataset card until confirmed |
| BabyGuard / baby-monitor-wifi-csi candidate breathing data | `third_party/wifi_sensing/baby_monitor_wifi_csi/` | [baby-monitor-wifi-csi](https://github.com/mohosy/baby-monitor-wifi-csi) | Breathing / apnea-style healthcare sensing baseline (ESP32) | Not applicable | Possible — pending verification | Unknown | Repo: MIT; Dataset: pending verification | Inspect upstream for recorded CSI traces or data download links; assess applicability to vital-sign experiments; do not create full dataset card until confirmed |
| WiFi-CSI-Human-Pose-Detection candidate pose CSI data | `third_party/wifi_sensing/wifi_csi_human_pose_detection/` | [WiFi-CSI-Human-Pose-Detection](https://github.com/euaziel/WiFi-CSI-Human-Pose-Detection) | Pose estimation, through-wall sensing, fall-context baseline | Possible — pending verification | Not applicable | Pending verification | Repo: GPL-3.0; Dataset: pending verification | Inspect upstream for dataset source and links; verify GPL-3.0 copyleft implications; do not create full dataset card until confirmed |
| CsiGAN-related CSI activity-recognition data | `third_party/wifi_sensing/csigan/` | [CsiGAN](https://github.com/ChunjingXiao/CsiGAN) | GAN-based CSI augmentation / robustness support; not healthcare-specific | Not directly applicable | Not directly applicable | Pending verification | No LICENSE file detected in upstream repo (2026-05-24); Dataset: pending verification | Inspect upstream for dataset links or included data; verify license before any download or use; do not create full dataset card until confirmed |
| goop-veil live/router CSI privacy-defense data | `third_party/wifi_sensing_security/goop_veil/` | [goop-veil](https://github.com/kobepaw/goop-veil) | WiFi CSI privacy-defense and router-side mitigation workflow | Not applicable | Not applicable | No public dataset confirmed | Pending verification for any associated data | Track as candidate workflow only; do not create dataset folder unless confirmed |

---

## Future Additions

The following dataset categories are candidates for future catalog entries:

- **Fall detection datasets:** FallDeFi, and other WiFi CSI fall-detection corpora
- **Activity recognition datasets:** Widar3.0, additional HAR datasets
- **Vital sign / health sensing datasets:** WiFi-based respiration, heart rate, and apnea datasets
- **Pose estimation datasets:** Additional WiFi CSI pose datasets
- **Candidate sources from newer repos:** See Candidate / Future Dataset Sources section above

See `datasets/future_datasets/README.md` for the structured candidate list and review checklist.

---

*Last updated: 2026-05-24*
