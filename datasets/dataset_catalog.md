# Dataset Catalog

## Overview

This catalog lists public and research WiFi CSI datasets that are relevant to the `wifi-csi-fall-detection` repository. Entries are included for reference, citation planning, and future real-data integration.

**Important:** Inclusion in this catalog does **not** mean a dataset is currently used by this repository. Current experiments use synthetic CSI-like data only. Real-data integration is future work.

---

## Dataset Table

| Dataset | Modality | Primary Task | Subjects / Setting | Format | Status in This Repo | Notes |
|---------|----------|-------------|-------------------|--------|---------------------|-------|
| MM-Fi | WiFi CSI + multi-modal (pending verification) | Human sensing / pose / activity-related research | Pending verification from official source | .npy (mentioned in RuView docs; verify officially) | Cataloged only; not integrated | Related to WiFi CSI sensing; not claimed as fall-detection validation here |
| Wi-Pose | WiFi CSI with pose-related annotations (pending verification) | WiFi-based pose estimation | Pending verification from official source | .mat (mentioned in RuView docs; verify officially) | Cataloged only; not integrated | Related to WiFi CSI sensing; not claimed as fall-detection validation here |

> **Note:** All dataset details must be verified from official dataset pages or papers before use. Do not treat unverified fields as authoritative.

---

## Current Integration Status

| Dataset | Downloaded Locally | Integrated in Pipeline | Used for Validation | Used for Benchmarking |
|---------|-------------------|----------------------|--------------------|-----------------------|
| MM-Fi | No | No | No | No |
| Wi-Pose | No | No | No | No |

All experiments currently use **synthetic CSI-like data**. This will be updated as real-data integration progresses.

---

## Notes on Dataset Validation

- Inclusion of a dataset in this catalog does **not** imply clinical validation.
- Inclusion does **not** imply fall-detection validation.
- Dataset claims (accuracy, performance, subject counts) are **not independently verified** by this repository.
- MM-Fi and Wi-Pose are categorized as **related datasets** — not as current validation sources.
- Any future integration will require: license review, data verification, baseline documentation, and citation compliance.

---

## Future Additions

The following dataset categories are candidates for future catalog entries:

- **Fall detection datasets:** FallDeFi, and other WiFi CSI fall-detection corpora
- **Activity recognition datasets:** Widar3.0, UT-HAR, SignFi
- **Vital sign / health sensing datasets:** WiFi-based respiration and heart rate datasets
- **Pose estimation datasets:** Additional WiFi CSI pose datasets

See `datasets/future_datasets/README.md` for the structured candidate list and review checklist.

---

*Last updated: May 2026*
