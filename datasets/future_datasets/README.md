# Future Dataset Entries

## Purpose

This folder is a placeholder for WiFi CSI-related datasets that may be added to the catalog in future phases. It lists candidate dataset types and specific datasets that are relevant to the research areas of this repository.

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
| WiFi CSI vital signs | Indirect: health sensing research context |
| Multi-modal CSI datasets | Indirect: broader sensing research context |

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

## Review Checklist

For each new dataset entry, complete the following before adding it to the catalog:

- [ ] Identify official dataset source (URL, paper, DOI)
- [ ] Verify license type and access requirements
- [ ] Confirm redistribution policy
- [ ] Confirm citation requirements
- [ ] Assess task relevance to this repository
- [ ] Create a folder under `datasets/<dataset-name>/`
- [ ] Add `README.md`, `DATASET_CARD.md`, `LICENSE_SUMMARY.md`, `DOWNLOAD_INSTRUCTIONS.md`
- [ ] Update `datasets/dataset_catalog.md` with a new row
- [ ] Update `docs/roadmap.md` with the cataloging task

---

*Last updated: May 2026*


---

## New Candidate Dataset Entries (Added 2026-05-24)

The following candidate entries were added based on newly tracked third-party repositories. All entries are candidates only. No data has been downloaded, integrated, validated, or benchmarked. These are tracking notes for future verification.

---

### goop-veil live/router CSI data

- **Candidate Name:** goop-veil live/router CSI data
- **Related Repo:** `third_party/wifi_sensing_security/goop_veil/`
- **GitHub:** https://github.com/kobepaw/goop-veil
- **Task Relevance:** Security/privacy tooling — WiFi CSI surveillance detection and defense. No fall-detection or vital-sign dataset confirmed.
- **Dataset Availability:** No public dataset confirmed. The repository appears to operate on live/router-side CSI or WiFi privacy-defense workflows.
- **License Status:** Pending verification for any associated data.
- **Action Needed:** Manually inspect upstream repository for any public dataset links or example CSI traces. Do not create dataset folder unless confirmed.
- **Status:** Candidate only — not downloaded, integrated, or benchmarked.

---

### WiFi-CSI-Human-Pose-Detection dataset

- **Candidate Name:** WiFi-CSI-Human-Pose-Detection dataset
- **Related Repo:** `third_party/wifi_sensing/wifi_csi_human_pose_detection/`
- **GitHub:** https://github.com/euaziel/WiFi-CSI-Human-Pose-Detection
- **Task Relevance:** Possible WiFi CSI pose/through-wall dataset. Fall-detection relevance: possible (pending verification).
- **Dataset Availability:** Pending verification — the upstream repository may contain or reference CSI pose/through-wall data. No confirmed public downloadable dataset identified.
- **License Status:** Repo license GPL-3.0 (confirmed). Dataset license: pending verification.
- **Action Needed:** Inspect upstream repository for dataset links, included data files, or external dataset references. Verify license terms before any download or use.
- **Status:** Candidate only — not downloaded, integrated, or benchmarked.

---

### mowa-fall-har

- **Candidate Name:** mowa-fall-har
- **Related Repo:** `third_party/wifi_sensing/mowa_wifi_sensing/`
- **GitHub:** https://github.com/oss-inc/mowa-wifi-sensing
- **Related Fork:** https://github.com/cheeseBG/wifi-sensing
- **Task Relevance:** WiFi CSI HAR and fall-detection baseline. Fall-detection relevance: possible (pending verification).
- **Dataset Availability:** Pending verification — the repository may expect or include real-time Nexmon CSI data with domain-specific HAR folders (e.g., `csi_dataset/domain_A`, `domain_B`). No confirmed public downloadable dataset identified.
- **License Status:** Repo license BSD-3-Clause (confirmed). Dataset license: pending verification.
- **Action Needed:** Inspect upstream repository for any included dataset folders, data download links, or collection scripts. Verify license and access terms before any use. Assess whether domain-specific HAR data includes fall-related activity classes relevant to this thesis.
- **Status:** Candidate only — not downloaded, integrated, or benchmarked.

---

### baby-monitor-wifi-csi

- **Candidate Name:** baby-monitor-wifi-csi breathing/apnea CSI data
- **Related Repo:** `third_party/wifi_sensing/baby_monitor_wifi_csi/`
- **GitHub:** https://github.com/mohosy/baby-monitor-wifi-csi
- **Task Relevance:** WiFi CSI breathing/apnea sensing baseline. Vital-sign relevance: possible (pending verification).
- **Dataset Availability:** Unknown — the upstream repository implements a real-time sensing system. No confirmed public downloadable CSI breathing/apnea dataset identified.
- **License Status:** Repo license MIT (confirmed). Dataset license: pending verification.
- **Action Needed:** Inspect upstream repository for any included recorded CSI traces, dataset folders, or data download links. Verify license and access terms before any use. Assess applicability to thesis vital-sign experiments.
- **Status:** Candidate only — not downloaded, integrated, or benchmarked.

---

*Last updated: 2026-05-24*
