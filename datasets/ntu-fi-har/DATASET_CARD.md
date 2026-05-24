# NTU-Fi HAR Dataset Card

> **Important:** Fields marked *Pending verification* have not been independently confirmed by this repository. All information should be verified against the original source before use in academic work or model development.

---

## Dataset Summary

NTU-Fi HAR (Nanyang Technological University WiFi Human Activity Recognition) is a WiFi CSI-based dataset for human activity recognition collected at NTU Singapore. It is tracked in this repository because it is included as a supported benchmark dataset in the SenseFi / WiFi CSI Sensing Benchmark.

The dataset is associated with activities including lying down, falling, walking, running, sitting down, and standing up (*Pending verification* — confirm full activity list from original source).

> **Important:** This repository does not independently claim NTU-Fi HAR is a validated fall-detection dataset. The fall class inclusion and suitability for fall-detection benchmarking must be verified from the original dataset paper.

---

## Official Source

- **SenseFi / WiFi CSI Sensing Benchmark GitHub:** [https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark)
- **Dataset paper (via SenseFi):** *Pending verification* — confirm official publication and DOI from original authors
- **Official dataset page:** *Pending verification*

> Official links are provided for convenience and reproducibility planning. Dataset files are not stored in this repository. License, exact access terms, and redistribution rights must be verified before any use.

---

## Associated Paper or Citation

*Pending verification* — confirm full citation from the original NTU-Fi HAR paper.

Placeholder BibTeX (to be verified and replaced):

```bibtex
@article{ntufhar_placeholder,
  title  = {NTU-Fi HAR: WiFi CSI Human Activity Recognition Dataset},
  author = {Pending verification},
  year   = {Pending},
  note   = {Verify full citation details from original NTU publication}
}
```

---

## Data Modalities

- WiFi Channel State Information (CSI)
- *Pending verification* — confirm CSI format, subcarrier count, and collection frequency

---

## Tasks

- Human Activity Recognition (HAR)
- *Pending verification* — confirm whether fall detection is a supported task

---

## Subjects and Environment

- *Pending verification* — number of subjects, environment type, and collection conditions
- Collected at Nanyang Technological University, Singapore (*Pending verification*)

---

## WiFi Equipment and Setup

- *Pending verification* — confirm WiFi hardware, antenna configuration, CSI extraction tool

---

## File Formats

- *Pending verification* — confirm file format (.mat, .csv, .npz, or other)

---

## Labels and Annotations

- *Pending verification* — confirm full activity label list from original paper
- Reported activities may include: lie down, fall, walk, run, sit down, stand up

---

## License and Access

- *Pending verification* — License type not confirmed
- *Pending verification* — Redistribution rights not confirmed
- Dataset files are NOT stored or redistributed in this repository
- See `LICENSE_SUMMARY.md` for license tracking details

---

## Intended Use in This Repository

- Cataloged for literature review and future benchmarking reference
- Tracked because SenseFi includes NTU-Fi HAR as a supported benchmark dataset
- May be relevant for future comparative benchmarking of fall-detection models
- Dataset files will not be downloaded or integrated until license is verified and explicit integration is planned
- No redistribution occurs

---

## Related Third-Party Repository

- **SenseFi / WiFi CSI Sensing Benchmark:** `third_party/wifi_sensing/sensefi/` — includes NTU-Fi HAR as a supported benchmark dataset

---

## Current Status

| Item | Status |
|------|--------|
| Cataloged in this repository | Yes |
| Official source links added | Pending |
| Downloaded locally | No |
| Loaded into pipeline | No |
| Used for model training | No |
| Used for validation | No |
| Used for benchmarking | No |
| License verified | Pending |
| Citation confirmed | Pending |

---

## Open Questions

- [ ] Confirm official dataset publication and DOI
- [ ] Verify exact license type and access requirements
- [ ] Confirm full list of activity labels
- [ ] Is redistribution of any portion of NTU-Fi HAR permitted?
- [ ] Confirm WiFi hardware and CSI format used
- [ ] Is the fall class suitable for fall-detection benchmarking?
- [ ] What is the correct BibTeX citation for NTU-Fi HAR?
- [ ] Is NTU-Fi HAR the same as or different from NTU-Fi HumanID?

---

## Last Updated

*Pending — to be updated upon source and license verification*
