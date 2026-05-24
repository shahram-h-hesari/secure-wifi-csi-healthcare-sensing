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
