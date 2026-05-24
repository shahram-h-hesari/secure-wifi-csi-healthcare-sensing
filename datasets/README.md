# WiFi CSI Dataset Catalog

## Purpose

This folder catalogs public and research datasets related to WiFi CSI sensing. It is maintained as part of the `wifi-csi-fall-detection` repository to support transparent academic research, reproducibility planning, and future real-data benchmarking.

This repository catalogs public and research datasets related to WiFi CSI sensing. Full dataset files are not stored directly in this repository unless redistribution is explicitly permitted and files are small enough for GitHub. Instead, this repository provides dataset cards, download instructions, license summaries, citation notes, and future loader plans.

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

The `data/external/` path is excluded from Git via `.gitignore`. Do **not** commit large dataset files to this repository.

---

## Future Dataset Integration

Future work may include:

- Downloading and verifying MM-Fi and Wi-Pose locally
- Writing dataset loaders under `scripts/` or `src/`
- Benchmarking against the synthetic CSI pipeline
- Evaluating adversarial robustness using real CSI data

See `datasets/future_datasets/README.md` for candidate future entries.

---

## Citation and License Responsibility

Inclusion of a dataset in this catalog does **not** imply clinical validation, fall-detection validation, or current use in this repository.

Users are responsible for reviewing each dataset's license and citation requirements before downloading or using any dataset. See each dataset's `LICENSE_SUMMARY.md` and official source for full terms.

---

*Last updated: May 2026*
