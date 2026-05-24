# Widar / Widar3.0 Dataset Card

> **Important:** Fields marked *Pending verification* have not been independently confirmed by this repository. All information should be verified against the official Widar3.0 project page or associated paper before use.

---

## Dataset Summary

Widar3.0 is a WiFi CSI-based gesture-recognition dataset from Tsinghua University. It is referenced and used by both Attack_WiFi_Sensing and SenseFi/WiFi CSI Sensing Benchmark for gesture-recognition and robustness-related WiFi sensing experiments.

SenseFi describes Widar3.0 as a 22-class gesture dataset using BVP (Body-coordinate Velocity Profile) features.

**This is not a fall-detection dataset.** This repository does not claim Widar3.0 is a fall-detection dataset.

---

## Official Source

- **Official Widar3.0 project page:** [https://tns.thss.tsinghua.edu.cn/widar3.0/](https://tns.thss.tsinghua.edu.cn/widar3.0/)
- **Associated TPAMI paper page:** [https://www.computer.org/csdl/journal/tp/2022/11/09516988/1watWmznfRS](https://www.computer.org/csdl/journal/tp/2022/11/09516988/1watWmznfRS)
- **SenseFi benchmark reference:** [https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark](https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark)

> Official links are provided for convenience and reproducibility planning. Dataset files are not stored in this repository. License, exact access terms, and loader compatibility should be verified from the official sources before use.

### Download Links (from official Widar3.0 project page)

> Download links are listed here for reference only. Check the official Widar3.0 project page for current availability and access requirements.

- **IEEE DataPort:** See official IEEE DataPort link on the Widar3.0 project page
- **Tsinghua Disk:** See official Tsinghua Disk link on the Widar3.0 project page
- **Baidu Disk:** See official Baidu Disk link on the Widar3.0 project page (the project page lists a password for the Baidu Disk access)

---

## Associated Paper or Citation

> The associated paper is available via IEEE TPAMI: https://www.computer.org/csdl/journal/tp/2022/11/09516988/1watWmznfRS
> Verify the full citation from the official publication before using in academic work.

```bibtex
% TODO: Add Widar3.0 BibTeX citation after verifying official citation from the paper/project page
% Paper: Zheng et al., Zero-Effort Cross-Domain Gesture Recognition with Wi-Fi, IEEE TPAMI 2022
% DOI: https://doi.org/10.1109/TPAMI.2021.3105054
```

---

## Data Modalities

- **Primary modality:** WiFi CSI (pending verification from official source)
- **Feature type mentioned by SenseFi:** BVP (Body-coordinate Velocity Profile)
- **Sensing hardware:** Pending verification from official source

---

## Tasks

- **Primary task:** WiFi gesture recognition (22 classes, per SenseFi)
- **Is this a fall-detection dataset?** No. This repository does not claim Widar3.0 is a fall-detection dataset.
- **Relevance to this repository:** Potential use for future adversarial robustness evaluation, because Attack_WiFi_Sensing and SenseFi reference Widar3.0 for WiFi sensing experiments.

---

## Subjects and Environment

- **Number of subjects:** Pending verification from official source
- **Collection environment:** Pending verification (indoor, multiple rooms; see official project page)
- **WiFi equipment / setup:** Pending verification from official source

---

## File Formats

- **Format:** Pending verification from official source
- **Feature format used by SenseFi:** BVP arrays (pending confirmation of exact file format)
- **Directory structure:** See official project page for verified structure

---

## Labels and Annotations

- **Gesture labels:** 22 gesture classes (per SenseFi; pending verification from official source)
- **Label schema:** Pending verification from official dataset documentation

---

## License and Access

- **License type:** Pending verification from official project page
- **Access method:** IEEE DataPort, Tsinghua Disk, and Baidu Disk (see official project page for current links)
- **Redistribution allowed:** Pending verification — do not redistribute without confirming license
- **Commercial use allowed:** Pending verification

See `LICENSE_SUMMARY.md` for the running access and license status.

---

## Intended Use in This Repository

If integrated in the future, Widar3.0 may be used for:

- Adversarial robustness evaluation using real WiFi CSI gesture data (following Attack_WiFi_Sensing methodology)
- Baseline comparison against the SenseFi benchmark framework
- Reference for CSI feature extraction (BVP) and model architecture

**Current status: Cataloged only; not downloaded, not integrated, and not used for validation in this repository.**

---

## Related Third-Party Repositories

- **Attack_WiFi_Sensing:** `third_party/wifi_sensing_security/attack_wifi_sensing/` — references or uses Widar3.0 for adversarial attack experiments.
- **SenseFi / WiFi CSI Sensing Benchmark:** `third_party/wifi_sensing/sensefi/` — includes Widar3.0 as a supported benchmark dataset (22 gesture classes, BVP features).

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

- [ ] Verify exact license type and access requirements from the official Widar3.0 project page
- [ ] Is redistribution of any portion of Widar3.0 permitted?
- [ ] Confirm exact file formats and BVP feature extraction pipeline
- [ ] Confirm all 22 gesture class labels
- [ ] Verify IEEE DataPort download access and terms
- [ ] What is the correct BibTeX citation for Widar3.0?

---

*Last updated: May 2026*
