# UT-HAR Dataset Card

> **Important:** Fields marked *Pending verification* have not been independently confirmed by this repository. All information should be verified against the official dataset page or associated paper before use.

---

## Dataset Summary

UT-HAR is a WiFi CSI-based human activity recognition dataset. It is tracked in this repository because the SenseFi/WiFi CSI Sensing Benchmark includes UT-HAR as a supported dataset.

SenseFi lists UT-HAR with seven activity classes: **lie down, fall, walk, pickup, run, sit down, stand up**. The inclusion of a fall class may make this dataset relevant to fall-detection benchmarking, pending verification from the original source.

> **Important:** This repository does not independently claim UT-HAR is a validated fall-detection dataset. Verification from the original dataset source is required before treating UT-HAR as a fall-detection benchmark.

---

## Official Source

- **SenseFi / WiFi CSI Sensing Benchmark GitHub:** [https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark)
- **Dataset paper reference listed by SenseFi:** [https://ieeexplore.ieee.org/document/8067693](https://ieeexplore.ieee.org/document/8067693)
- **Kaggle mirror / access page:** [https://www.kaggle.com/datasets/hylanj/wifi-csi-dataset-ut-har](https://www.kaggle.com/datasets/hylanj/wifi-csi-dataset-ut-har)

> **Note:** The Kaggle link is a mirror and not the original official source. Verify license and access terms from the original paper/dataset authors before using any version of UT-HAR.

> Official links are provided for convenience and reproducibility planning. Dataset files are not stored in this repository. License, exact access terms, and loader compatibility should be verified from the official sources before use.

---

## Associated Paper or Citation

> The associated paper is referenced by SenseFi at: https://ieeexplore.ieee.org/document/8067693
> Verify the full citation from the official publication before using in academic work.

```bibtex
% TODO: Add UT-HAR BibTeX citation after verifying official citation from the paper/project page
% Paper reference: https://ieeexplore.ieee.org/document/8067693
```

---

## Data Modalities

- **Primary modality:** WiFi CSI (pending verification from official source)
- **Sensing hardware:** Pending verification from official source

---

## Tasks

- **Primary task:** WiFi-based human activity recognition (HAR)
- **Activity classes listed by SenseFi:** lie down, fall, walk, pickup, run, sit down, stand up (7 classes)
- **Is this a fall-detection dataset?** Possibly — includes a fall class (per SenseFi), but this requires verification from the original source. This repository does not independently validate UT-HAR as a fall-detection benchmark.
- **Relevance to this repository:** UT-HAR may be relevant to fall-detection benchmarking, pending verification from the original dataset source.

---

## Subjects and Environment

- **Number of subjects:** Pending verification from official source
- **Collection environment:** Pending verification
- **WiFi equipment / setup:** Pending verification from official source

---

## File Formats

- **Format:** Pending verification from official source
- **Directory structure:** See official source or SenseFi benchmark repository for verified structure

---

## Labels and Annotations

- **Activity labels (per SenseFi):** lie down, fall, walk, pickup, run, sit down, stand up
- **Label schema:** Pending verification from official dataset documentation

---

## License and Access

- **License type:** Pending verification from official source
- **Access method:** Pending verification (see Kaggle mirror for community access; verify against official source)
- **Kaggle mirror:** This repository notes the Kaggle page as a potential access point, but it is not the official dataset source
- **Redistribution allowed:** Pending verification — do not redistribute without confirming license
- **Commercial use allowed:** Pending verification

See `LICENSE_SUMMARY.md` for the running access and license status.

---

## Intended Use in This Repository

If integrated in the future, UT-HAR may be used for:

- Fall-detection benchmarking (pending verification that the fall class is suitable)
- Activity recognition evaluation for the WiFi CSI pipeline
- Comparison against the SenseFi benchmark framework

**Current status: Cataloged only; not downloaded, not integrated, and not used for validation in this repository.**

---

## Related Third-Party Repository

- **SenseFi / WiFi CSI Sensing Benchmark:** `third_party/wifi_sensing/sensefi/` — includes UT-HAR as a supported benchmark dataset with 7 activity classes.

---

## Current Status

| Item | Status |
|------|--------|
| Cataloged in this repository | Yes |
| Official source links added | Yes |
| Downloaded locally | No |
| Loaded into pipeline | No |
| Used for model training | No |
| Used for validation | No |
| Used for benchmarking | No |
| License verified | Pending |
| Citation confirmed | Pending |

---

## Open Questions

- [ ] Verify exact license type and access requirements from the original UT-HAR source
- [ ] Confirm whether the original official source differs from the Kaggle mirror
- [ ] Is redistribution of any portion of UT-HAR permitted?
- [ ] Confirm WiFi hardware and CSI format used
- [ ] Confirm full list of activity labels from original paper
- [ ] Is the fall class suitable for fall-detection benchmarking? (check official paper)
- [ ] What is the correct BibTeX citation for UT-HAR?

---

*Last updated: May 2026*
