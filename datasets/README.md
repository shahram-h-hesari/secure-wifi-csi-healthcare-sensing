# WiFi CSI Dataset Catalog

## Purpose

This folder catalogs public and research datasets related to WiFi CSI sensing. It is maintained as part of the `wifi-csi-fall-detection` repository to support transparent academic research, reproducibility planning, and future real-data benchmarking.

Full dataset files are not stored directly in this repository unless redistribution is explicitly permitted and files are small enough for GitHub. Instead, this repository provides dataset cards, download instructions, license summaries, citation notes, and future loader plans.

---

## Current Status

Current repository experiments use **synthetic CSI-like data only**. MM-Fi and Wi-Pose are cataloged as related datasets for future real-data benchmarking and robustness evaluation; they are **not yet integrated into the pipeline**.

Real CSI dataset integration is **future work**.

---

## Included Dataset Entries

| Dataset | Folder | Task Focus | Integration Status |
|---------|--------|------------|-------------------|
| MM-Fi | `datasets/mm-fi/` | Human sensing / pose / activity | Cataloged only; not integrated |
| Wi-Pose | `datasets/wi-pose/` | WiFi-based pose estimation | Cataloged only; not integrated |
| Future entries | `datasets/future_datasets/` | TBD | Placeholder |

---

## What Is Stored Here

- Dataset cards (metadata, task, format, subjects, labels)
- License summaries and access notes
- Download instructions with recommended local paths
- Future loader plans and integration notes
- Catalog index (`dataset_catalog.md`)

---

## What Is Not Stored Here

- Raw dataset files (`.mat`, `.npy`, `.npz`, `.h5`, `.zip`, `.tar`, etc.)
- Binary dataset archives
- Any data that cannot be freely redistributed
- Clinical or real-world validation datasets

---

## Local Data Storage Policy

If you download datasets locally for experimentation, store them at:

```
data/external/mm-fi/
data/external/wi-pose/
```

These paths are listed in `.gitignore` and will not be tracked by Git.

---

## Notes on Dataset Validation

- Inclusion of a dataset in this catalog does **not** imply clinical validation.
- Inclusion does **not** imply fall-detection validation.
- Dataset claims (accuracy, performance, subject counts) are **not independently verified** by this repository.
- MM-Fi and Wi-Pose are categorized as **related datasets**, not as current validation sources.
- Any future integration will require: license review, data verification, baseline documentation, and citation compliance.

---

## Future Additions

The following dataset categories are candidates for future catalog entries:

- **Fall detection datasets:** FallDeFi, and other WiFi CSI fall-detection corpora
- **Activity recognition datasets:** Widar3.0, UT-HAR, SignFi
- **Vital sign / health sensing datasets:** WiFi-based respiration and heart rate datasets
- **Pose estimation datasets:** Additional WiFi CSI pose datasets

See `datasets/future_datasets/README.md` for the structured candidate list and review checklist.
