# WiFi-ADG Dataset Card

> **Important:** Fields marked *Pending verification* have not been independently confirmed by this repository. All information should be verified against the original source before use in academic work or model development.

---

## Dataset Summary

The WiFi-ADG dataset is associated with the WiFi-ADG repository (Siwang Zhou) and the IEEE Communications Letters paper *Adversarial WiFi Sensing for Privacy Preservation of Human Behaviors*. The upstream README describes nine datasets used for adversarial WiFi sensing and privacy-preservation experiments.

The upstream repository describes the following nine dataset files:

| File | Samples |
|------|---------|
| `data0.mat` | 4200 (pending verification) |
| `data1.mat` | 4200 (pending verification) |
| `data2.mat` | 4200 (pending verification) |
| `data3.mat` | 4200 (pending verification) |
| `data4.mat` | 4200 (pending verification) |
| `data5.mat` | 4200 (pending verification) |
| `data6.mat` | 4200 (pending verification) |
| `data7.mat` | 4200 (pending verification) |
| `resdata.mat` | 1080 (pending verification) |

> **Note:** Sample counts above are taken from the upstream README and must be independently verified. Exact file sizes and total dataset size (reported as large; verify before downloading) must be confirmed from the original source.

> **Important:** This is not a healthcare dataset. This is not a fall-detection dataset. This dataset has not been used for training, validation, or benchmarking in this repository. It is cataloged for literature review and future reproducibility planning only.

---

## Official Source

- **Official GitHub repository:** [https://github.com/siwangzhou/WiFi-ADG](https://github.com/siwangzhou/WiFi-ADG)
- **Dataset download link listed in upstream README (Baidu):** [https://pan.baidu.com/s/1fOhaYD1vq39JWXPExtsCIg](https://pan.baidu.com/s/1fOhaYD1vq39JWXPExtsCIg)
- **Associated paper DOI:** [https://doi.org/10.1109/LCOMM.2019.2952844](https://doi.org/10.1109/LCOMM.2019.2952844)

> **Important:** The Baidu download link is an upstream-provided access link only. It is NOT a repository-hosted dataset. License, access terms, redistribution rights, and commercial-use rights must be verified from the original source before any access or use.

> Official links are provided for convenience and reproducibility planning. Dataset files are NOT stored in this repository.

---

## Associated Paper or Citation

- **Title:** Adversarial WiFi Sensing for Privacy Preservation of Human Behaviors
- **Venue:** IEEE Communications Letters
- **DOI:** [https://doi.org/10.1109/LCOMM.2019.2952844](https://doi.org/10.1109/LCOMM.2019.2952844)

Placeholder BibTeX (TODO: verify and replace with official citation):

```bibtex
@article{zhou2019adversarial,
  title   = {Adversarial WiFi Sensing for Privacy Preservation of Human Behaviors},
  author  = {Zhou, Siwang and Pending verification},
  journal = {IEEE Communications Letters},
  year    = {2019},
  doi     = {10.1109/LCOMM.2019.2952844},
  note    = {Verify full citation details from original paper}
}
```

---

## Data Modalities

- WiFi Channel State Information (CSI)
- *Pending verification* — confirm exact CSI format, subcarrier count, and collection frequency

---

## Tasks

- Adversarial WiFi sensing / privacy-preserving human behavior recognition
- CSI-based human activity recognition (used as context for adversarial perturbation)
- *Pending verification* — confirm exact task scope from repository and paper

---

## Subjects and Environment

- *Pending verification* — number of subjects, environment type, and collection conditions must be confirmed from the original source

---

## WiFi Equipment and Setup

- *Pending verification* — confirm WiFi hardware, antenna configuration, and CSI extraction tool from the repository and paper

---

## File Formats

- `.mat` (MATLAB format) — 9 files: `data0.mat` through `data7.mat` and `resdata.mat` (*Pending verification* — confirm exact format and structure)

---

## Labels and Annotations

- *Pending verification* — confirm label structure (activity labels and adversarial perturbation annotations)

---

## License and Access

- *Pending verification* — License type not confirmed
- *Pending verification* — Baidu access terms not confirmed
- *Pending verification* — Redistribution rights not confirmed
- *Pending verification* — Commercial use rights not confirmed
- Dataset files are NOT stored or redistributed in this repository
- The Baidu link is an upstream-provided access link, not a repository-hosted resource
- See `LICENSE_SUMMARY.md` for license tracking details

---

## Intended Use in This Repository

- Cataloged for literature review and future reproducibility planning only
- Tracked because the WiFi-ADG repository is referenced as a WiFi sensing security and adversarial privacy-preservation research reference
- Not a healthcare dataset; not a fall-detection dataset
- Relevant to adversarial robustness, CSI privacy, and behavior obfuscation research context
- Dataset files will not be downloaded or integrated until license is verified and explicit integration is planned
- No redistribution occurs

---

## Related Third-Party Repository

- **WiFi-ADG:** `third_party/wifi_sensing_security/wifi_adg/` — adversarial WiFi sensing for privacy preservation of human behaviors

---

## Current Status

| Item | Status |
|------|--------|
| Cataloged in this repository | Yes |
| Official/source links added | Yes |
| Downloaded locally | No |
| Loaded into pipeline | No |
| Used for model training | No |
| Used for validation | No |
| Used for benchmarking | No |
| License verified | Pending |
| Citation confirmed | Pending |

---

## Open Questions

- [ ] What is the exact license type for the WiFi-ADG dataset?
- [ ] Are there academic-use-only restrictions?
- [ ] Is redistribution of any portion permitted?
- [ ] What are the exact Baidu access terms and extraction codes?
- [ ] What is the total dataset size?
- [ ] What is the correct BibTeX citation for the IEEE Communications Letters paper?
- [ ] How many subjects are included and what environment was used?
- [ ] What activity classes are included in the labels?
- [ ] What exactly is the format of the adversarial perturbation labels/metadata?

---

## Last Updated

*Pending — to be updated upon source and license verification*
