# SignFi Dataset Card

> **Important:** Fields marked *Pending verification* have not been independently confirmed by this repository. All information should be verified against the official SignFi dataset page or associated paper before use.

---

## Dataset Summary

SignFi is a WiFi CSI-based sign-language and gesture-recognition dataset. It is referenced and used by the Attack_WiFi_Sensing repository for adversarial attack and robustness evaluation experiments on WiFi sensing models.

**This is not a fall-detection dataset.** SignFi is relevant to this repository as a potential source of CSI data for future adversarial robustness evaluation, because Attack_WiFi_Sensing (a tracked third-party repository) uses or references it.

**Note:** The SignFi website states that users must agree to the dataset Terms of Use before downloading or using the dataset files.

---

## Official Source

- **Official GitHub / dataset page:** [https://github.com/yongsen/SignFi](https://github.com/yongsen/SignFi)
- **Project website:** [https://yongsen.github.io/SignFi/](https://yongsen.github.io/SignFi/)
- **Associated paper DOI:** [https://doi.org/10.1145/3191755](https://doi.org/10.1145/3191755)

> Official links are provided for convenience and reproducibility planning. Dataset files are not stored in this repository. License, exact access terms, and Terms of Use must be verified from the official sources before download or use.

### Download Links (from official SignFi GitHub page)

> Download links are listed here for reference only. Use the official Box links provided on the SignFi GitHub page. Direct links are not hard-coded here because they may require redirect or Terms of Use acceptance.

- `dataset_lab_276_dl.mat` — See official Box link on the SignFi GitHub page
- `dataset_lab_276_ul.mat` — See official Box link on the SignFi GitHub page
- `dataset_home_276.mat` — See official Box link on the SignFi GitHub page
- `dataset_lab_150.mat` — See official Box link on the SignFi GitHub page

---

## Associated Paper or Citation

> The associated paper is available at: https://doi.org/10.1145/3191755
> Verify the full citation from the official publication before using in academic work.

```bibtex
% TODO: Add SignFi BibTeX citation after verifying official citation from the paper/project page
% Paper: Ma et al., SignFi: Sign Language Recognition Using WiFi, ACM IMWUT 2018
% DOI: https://doi.org/10.1145/3191755
```

---

## Data Modalities

- **Primary modality:** WiFi CSI (pending verification from official source)
- **Sensing hardware:** Pending verification (Intel 5300 NIC commonly used in CSI sign-language work)
- **File format mentioned:** `.mat` (MATLAB format, based on dataset file names on official page)

---

## Tasks

- **Primary task:** Sign language / gesture recognition using WiFi CSI
- **Is this a fall-detection dataset?** No. SignFi is a sign-language / gesture dataset. Do not assume fall-detection validation.
- **Relevance to this repository:** Potential use for future adversarial robustness evaluation, because Attack_WiFi_Sensing uses or references SignFi.

---

## Subjects and Environment

- **Number of subjects:** Pending verification from official source
- **Collection environments:** Lab and home environments (based on dataset file names: `lab` and `home`)
- **Sign classes:** 276 signs in lab setting; 150 signs in lab setting (alternate); pending full verification
- **WiFi equipment / setup:** Pending verification from official source

---

## File Formats

- **Format:** `.mat` (MATLAB format, based on official dataset file names)
- **Files mentioned on official page:** `dataset_lab_276_dl.mat`, `dataset_lab_276_ul.mat`, `dataset_home_276.mat`, `dataset_lab_150.mat`
- **Directory structure:** See official GitHub repository for verified structure

---

## Labels and Annotations

- **Sign/gesture labels:** Pending verification from official source
- **Label schema:** Pending verification from official dataset documentation

---

## License and Access

- **License type:** Pending verification — the SignFi page states users must agree to Terms of Use before downloading/using
- **Access method:** Box file hosting (see official GitHub page for current links)
- **Terms of Use required:** Yes — users must agree to the SignFi Terms of Use before downloading or using the dataset files (per official SignFi page)
- **Redistribution allowed:** Pending verification — do not redistribute without confirming license and Terms of Use
- **Commercial use allowed:** Pending verification

See `LICENSE_SUMMARY.md` for the running access and license status.

---

## Intended Use in This Repository

If integrated in the future, SignFi may be used for:

- Adversarial robustness evaluation using real WiFi CSI gesture data (following Attack_WiFi_Sensing methodology)
- Baseline comparison for CSI model robustness against adversarial perturbations
- Reference for CSI data format and collection methodology

**Current status: Cataloged only; not downloaded, not integrated, and not used for validation in this repository.**

---

## Related Third-Party Repository

- **Attack_WiFi_Sensing:** `third_party/wifi_sensing_security/attack_wifi_sensing/` — references or uses SignFi for adversarial attack experiments on WiFi sensing models.

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

- [ ] Verify exact license type and Terms of Use from the official SignFi page
- [ ] Is redistribution of any portion of SignFi permitted?
- [ ] Confirm exact WiFi hardware and CSI format used
- [ ] Confirm number of subjects and full sign class list
- [ ] Confirm whether Attack_WiFi_Sensing uses the full dataset or a subset
- [ ] What is the correct BibTeX citation for SignFi?

---

*Last updated: May 2026*
