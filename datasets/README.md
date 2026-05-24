# WiFi CSI Dataset Catalog — Secure WiFi CSI Healthcare Sensing Research Prototype

> **Important note:** This folder catalogs public and research datasets related to WiFi CSI sensing. It is maintained as part of the **Secure WiFi CSI Healthcare Sensing** research prototype. Current experiments use **synthetic CSI-like data only**. No real CSI dataset is integrated into the pipeline. No clinical validation, real hardware validation, or medical-device readiness is claimed.

## Purpose

This folder catalogs public and research datasets related to WiFi CSI sensing. It is maintained as part of the `secure-wifi-csi-healthcare-sensing` repository to support transparent academic research, reproducibility planning, and future real-data benchmarking.

Full dataset files are not stored directly in this repository unless redistribution is explicitly permitted and files are small enough for GitHub. Instead, this repository provides dataset cards, download instructions, license summaries, citation notes, and future loader plans.

---

## Current Status

Current repository experiments use **synthetic CSI-like data only**. MM-Fi, Wi-Pose, SignFi, Widar, UT-HAR, NTU-Fi HAR, NTU-Fi HumanID, AntiEave-WiFi-Sensing, and WiFi-ADG are **cataloged only** for future real-data benchmarking and robustness evaluation; they are **not yet integrated into the pipeline**. AntiEave-WiFi-Sensing and WiFi-ADG are security/privacy-focused references; they are not healthcare datasets and not fall-detection datasets.

Real CSI dataset integration is **future work**.

---

## Confirmed Cataloged Dataset Entries

The following datasets have full catalog cards in this repository. They are **cataloged only** and are not integrated into the current pipeline.

| Dataset | Folder | Task Focus | Integration Status |
|---------|--------|------------|-------------------|
| MM-Fi | `datasets/mm-fi/` | Human sensing / pose / activity | Cataloged only; not integrated |
| Wi-Pose | `datasets/wi-pose/` | WiFi-based pose estimation | Cataloged only; not integrated |
| SignFi | `datasets/signfi/` | Sign language gesture recognition (WiFi CSI reference) | Cataloged only; not integrated |
| Widar | `datasets/widar/` | Gesture recognition / cross-domain WiFi sensing (reference) | Cataloged only; not integrated |
| UT-HAR | `datasets/ut-har/` | Human activity recognition including fall class (reference) | Cataloged only; not integrated |
| NTU-Fi HAR | `datasets/ntu-fi-har/` | Human activity recognition (reference) | Cataloged only; not integrated |
| NTU-Fi HumanID | `datasets/ntu-fi-humanid/` | Human identification via WiFi (reference) | Cataloged only; not integrated |
| AntiEave-WiFi-Sensing Dataset | `datasets/antieave-wifi-sensing/` | Adversarial WiFi sensing / anti-eavesdropping security (reference; not healthcare; not fall-detection) | Cataloged only; not downloaded; license pending |
| WiFi-ADG Dataset | `datasets/wifi-adg/` | Adversarial WiFi sensing / privacy preservation (reference; not healthcare; not fall-detection) | Cataloged only; not downloaded; license pending |
| Future entries | `datasets/future_datasets/` | TBD | Placeholder |

---

## Candidate / Future Dataset Sources

The following are **candidate sources only** from newer tracked third-party repositories. These are **not confirmed datasets**. Dataset availability, license, file format, and access terms are **pending verification**. No data has been downloaded or integrated. These candidates are tracked for future investigation only.

| Candidate Source | Related Repo | Possible Task Relevance | Availability Status |
|-----------------|-------------|------------------------|--------------------|
| mowa-wifi-sensing CSI data | [mowa-wifi-sensing](https://github.com/oss-inc/mowa-wifi-sensing) | Fall detection / HAR baseline (pending verification) | Pending verification |
| BabyGuard / baby-monitor-wifi-csi breathing data | [baby-monitor-wifi-csi](https://github.com/mohosy/baby-monitor-wifi-csi) | Breathing / apnea-style healthcare sensing baseline (pending verification) | Pending verification |
| WiFi-CSI-Human-Pose-Detection CSI data | [WiFi-CSI-Human-Pose-Detection](https://github.com/euaziel/WiFi-CSI-Human-Pose-Detection) | Pose / through-wall sensing / fall-context baseline (pending verification) | Pending verification |
| CsiGAN-related CSI activity-recognition data | [CsiGAN](https://github.com/ChunjingXiao/CsiGAN) | GAN-based CSI augmentation / robustness support; not healthcare-specific | Pending verification |
| goop-veil live/router CSI data | [goop-veil](https://github.com/kobepaw/goop-veil) | WiFi CSI privacy-defense and router-side mitigation workflow | No public dataset confirmed |

> **Note:** These candidate sources are **not validated datasets**. They are tracking placeholders for future work. Do not treat them as confirmed training, validation, or benchmarking sources. See `datasets/future_datasets/README.md` for detailed candidate notes.

---

## What Is Stored Here

- Dataset cards (metadata, task, format, subjects, labels)
- License summaries and access notes
- Download instructions with recommended local paths
- Future loader plans and integration notes
- Catalog index (`dataset_catalog.md`)

## What Is Not Stored Here

- Raw dataset files (`.mat`, `.npy`, `.npz`, `.h5`, `.zip`, `.tar`, etc.)
- Binary dataset archives
- Any data that cannot be freely redistributed
- Clinical or real-world validation datasets

---

## Local Data Storage Policy

If you download datasets locally for experimentation, store them under the general pattern:

```
data/external/<dataset-name>/
```

Example local paths (for reference only — paths should remain gitignored):

```
data/external/mm-fi/
data/external/wi-pose/
data/external/signfi/
data/external/widar/
data/external/ut-har/
data/external/ntu-fi-har/
data/external/ntu-fi-humanid/
data/external/antieave-wifi-sensing/
data/external/wifi-adg/
```

These paths are listed in `.gitignore` and will not be tracked by Git. Raw dataset files are **not stored directly in this repository** unless redistribution is explicitly permitted and files are small enough for GitHub.

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
- **Vital sign / health sensing datasets:** WiFi-based respiration, heart rate, and apnea datasets
- **Pose estimation datasets:** Additional WiFi CSI pose datasets
- **Candidate sources from newer repos:** See the Candidate / Future Dataset Sources section above and `datasets/future_datasets/README.md` for full candidate notes.

See `datasets/future_datasets/README.md` for the structured candidate list and review checklist.

---

*Last updated: 2026-05-24*
