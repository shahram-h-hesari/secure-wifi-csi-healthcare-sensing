# Future Dataset Entries — Secure WiFi CSI Healthcare Sensing Research Prototype

## Purpose

This folder is a placeholder for WiFi CSI-related datasets that may be added to the catalog in future phases. It lists candidate dataset types and specific datasets that are relevant to the broader **Secure WiFi CSI Healthcare Sensing** research direction, including fall detection, vital-sign monitoring, apnea detection, and adversarial robustness evaluation.

Future datasets should be added only after:

1. Identifying the official source and verifying the license
2. Confirming task relevance to the repository's research focus
3. Confirming citation requirements
4. Creating a proper dataset card, license summary, and download instructions

**Datasets should first be cataloged before any integration into the pipeline.**

---

## Candidate Dataset Types

| Category | Relevance |
|----------|-----------|
| WiFi CSI fall detection | Direct: supports fall-detection evaluation |
| WiFi CSI activity recognition | Indirect: activity context for safety sensing |
| WiFi CSI pose estimation | Indirect: body position for fall inference |
| WiFi CSI vital signs / breathing / apnea | Direct/Indirect: health sensing research context |
| Multi-modal CSI datasets | Indirect: broader sensing research context |
| Adversarial WiFi sensing / privacy defense data | Indirect: security and robustness context |

---

## Candidate Dataset List

> **Note:** The datasets listed below are candidates only. None are currently downloaded, integrated, or validated by this repository. All require license review, source verification, and citation confirmation before use.

### Fall Detection Datasets

| Dataset | Description | Task | Status |
|---------|-------------|------|--------|
| FallDeFi | WiFi CSI-based fall detection dataset; published research on CSI fingerprinting for fall events | Fall detection | Candidate — not yet cataloged |

### Activity Recognition Datasets

| Dataset | Description | Task | Status |
|---------|-------------|------|--------|
| Widar3.0 | Large-scale WiFi CSI gesture and activity recognition dataset | Activity/gesture recognition | Candidate — not yet cataloged |
| UT-HAR | University of Toronto WiFi CSI human activity recognition dataset | Activity recognition | Candidate — not yet cataloged |
| SignFi | WiFi CSI sign language recognition dataset | Sign/gesture recognition | Candidate — not yet cataloged |

### Other WiFi CSI Datasets

| Dataset | Description | Task | Status |
|---------|-------------|------|--------|
| WiFi vital sign datasets | Various published WiFi CSI datasets for respiration and heart rate monitoring | Vital sign sensing | Research ongoing — not yet cataloged |
| Other WiFi CSI pose datasets | Additional WiFi CSI datasets with pose or skeleton annotations | Pose estimation | Research ongoing — not yet cataloged |

---

## Candidate Dataset Notes from Third-Party Repository Tracking

The following candidate entries were added based on newly tracked third-party repositories. All entries are **candidates only**. No data has been downloaded, integrated, validated, or benchmarked. These are tracking notes for future verification.

> **Status for all entries below:** Candidate only — not downloaded; not integrated; not used for training, validation, or benchmarking.

---

### mowa-fall-har (mowa-wifi-sensing)

- **Candidate Name:** mowa-fall-har candidate CSI data
- **Related Repo:** `third_party/wifi_sensing/mowa_wifi_sensing/`
- **GitHub:** https://github.com/oss-inc/mowa-wifi-sensing
- **Related Fork:** https://github.com/cheeseBG/wifi-sensing
- **Why It Matters:** Real-time WiFi CSI-based HAR system using Nexmon CSI extractor on Raspberry Pi. Possible fall-detection baseline; relevant to understanding the synthetic-to-real CSI gap.
- **Task Relevance:** Fall detection / human activity recognition baseline (pending verification)
- **Fall-Detection Relevance:** Possible — pending verification (depends on whether fall class is included in HAR data)
- **Vital-Sign Relevance:** Not applicable
- **Dataset Availability:** Pending verification — may use real-time Nexmon CSI; possible domain-specific HAR folders (e.g., `csi_dataset/domain_A`, `domain_B`)
- **License:** Repo: BSD-3-Clause (confirmed). Dataset: pending verification.
- **What Must Be Verified:** Dataset download availability; fall-related activity classes; dataset license; format and loader compatibility
- **Action:** Inspect upstream repository for dataset folders or download links. Do not create full dataset card until data access, license, and fall class relevance are confirmed.
- **Status:** Candidate only — not downloaded; not integrated; not used for training, validation, or benchmarking.

---

### baby-monitor-wifi-csi (BabyGuard)

- **Candidate Name:** BabyGuard / baby-monitor-wifi-csi candidate breathing/apnea CSI data
- **Related Repo:** `third_party/wifi_sensing/baby_monitor_wifi_csi/`
- **GitHub:** https://github.com/mohosy/baby-monitor-wifi-csi
- **Why It Matters:** Contactless infant breathing monitoring using WiFi CSI and ESP32. Possible vital-sign / apnea-style healthcare sensing baseline. Most directly relevant to breathing/apnea clinical-safety experiments.
- **Task Relevance:** Breathing / apnea-style healthcare sensing baseline (pending verification)
- **Fall-Detection Relevance:** Not applicable
- **Vital-Sign / Apnea Relevance:** Possible — pending verification
- **Dataset Availability:** Unknown — implements real-time sensing; no confirmed public downloadable CSI breathing dataset
- **License:** Repo: MIT (confirmed). Dataset: pending verification.
- **What Must Be Verified:** Presence of recorded CSI breathing traces; dataset license; format and loader compatibility; applicability to thesis vital-sign experiments
- **Action:** Inspect upstream repository for recorded CSI traces or data links. Do not create full dataset card until data availability and license are confirmed.
- **Status:** Candidate only — not downloaded; not integrated; not used for training, validation, or benchmarking.

---

### WiFi-CSI-Human-Pose-Detection

- **Candidate Name:** WiFi-CSI-Human-Pose-Detection candidate pose CSI data
- **Related Repo:** `third_party/wifi_sensing/wifi_csi_human_pose_detection/`
- **GitHub:** https://github.com/euaziel/WiFi-CSI-Human-Pose-Detection
- **Why It Matters:** Human pose estimation through walls using WiFi CSI. Possible pose/through-wall sensing baseline relevant to fall-detection context and domain generalization.
- **Task Relevance:** Pose estimation, through-wall sensing, fall-context baseline (pending verification)
- **Fall-Detection Relevance:** Possible — pending verification
- **Vital-Sign Relevance:** Not applicable
- **Dataset Availability:** Pending verification — no confirmed public downloadable dataset identified
- **License:** Repo: GPL-3.0 (confirmed). Dataset: pending verification. Note: GPL-3.0 copyleft implications must be reviewed before any code adaptation.
- **What Must Be Verified:** Dataset access and download links; dataset license; GPL-3.0 copyleft implications; format and loader compatibility
- **Action:** Inspect upstream repository for dataset links. Verify license before any download or code adaptation.
- **Status:** Candidate only — not downloaded; not integrated; not used for training, validation, or benchmarking.

---

### CsiGAN-related CSI activity-recognition data

- **Candidate Name:** CsiGAN-related CSI activity-recognition data
- **Related Repo:** `third_party/wifi_sensing/csigan/`
- **GitHub:** https://github.com/ChunjingXiao/CsiGAN
- **Associated Paper:** Chunjing Xiao et al. "CsiGAN: Robust Channel State Information-based Activity Recognition with GANs." IEEE Internet of Things Journal, 2019.
- **Why It Matters:** GAN-based CSI augmentation and robustness support. Could assist class-imbalance, synthetic-to-real variation, and semi-supervised learning experiments in victim models.
- **Task Relevance:** GAN-based CSI augmentation / robustness support; not healthcare-specific
- **Healthcare Relevance:** None directly. Possible indirect support for future victim-model augmentation.
- **Fall-Detection Relevance:** Not directly applicable
- **Dataset Availability:** Pending verification — CsiGAN may use CSI activity-recognition datasets (possibly SignFi or similar); source data access unknown
- **License:** No LICENSE file detected in upstream repo (as of 2026-05-24). License pending verification — do not copy or build upon until confirmed.
- **What Must Be Verified:** Source dataset used for training/evaluation; dataset license; repository license; format and loader compatibility
- **Action:** Inspect upstream repository for dataset links. Verify license before any download or use.
- **Status:** Candidate only — not downloaded; not integrated; not used for training, validation, or benchmarking.

---

### goop-veil live/router CSI privacy-defense data

- **Candidate Name:** goop-veil live/router CSI privacy-defense data
- **Related Repo:** `third_party/wifi_sensing_security/goop_veil/`
- **GitHub:** https://github.com/kobepaw/goop-veil
- **Why It Matters:** Software-only WiFi CSI surveillance detection and privacy-defense tool. Relevant to router-side privacy mitigation and CSI-based defense workflows. No healthcare-specific content.
- **Task Relevance:** WiFi CSI privacy-defense and router-side mitigation workflow only
- **Fall-Detection Relevance:** Not applicable
- **Vital-Sign Relevance:** Not applicable
- **Dataset Availability:** No public dataset confirmed. Repository appears to operate on live/router-side CSI or WiFi privacy-defense workflows only.
- **License:** Apache-2.0 (confirmed for code). Dataset license: pending verification for any associated data.
- **What Must Be Verified:** Whether any public CSI dataset or example traces exist in the upstream repository
- **Action:** Track as candidate workflow only. Do not create dataset folder unless public dataset is confirmed.
- **Status:** Candidate only — not downloaded; not integrated; not used for training, validation, or benchmarking.

---

## Review Checklist

For each new dataset entry, complete the following before adding it to the catalog:

- [ ] Identify official dataset source (URL, paper, DOI)
- [ ] Verify license type and access requirements
- [ ] Confirm redistribution policy
- [ ] Confirm citation requirements
- [ ] Assess task relevance to this repository
- [ ] Assess victim-model baseline compatibility (fall, apnea, respiration, HR/RR, HAR)
- [ ] Assess attack compatibility (FGSM, PGD, C&W, MIM, universal perturbation)
- [ ] Assess defense compatibility (adversarial training, randomized smoothing, preprocessing)
- [ ] Assess clinical-safety metric mapping (missed falls/day, false alarms/hour, suppressed apnea alarms/hour)
- [ ] Create a folder under `datasets/<dataset-name>/`
- [ ] Add `README.md`, `DATASET_CARD.md`, `LICENSE_SUMMARY.md`, `DOWNLOAD_INSTRUCTIONS.md`
- [ ] Update `datasets/dataset_catalog.md` with a new row
- [ ] Update `docs/roadmap.md` with the cataloging task

---

*Last updated: 2026-05-24*
