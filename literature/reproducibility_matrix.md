# Reproducibility Matrix

**Project:** Secure WiFi CSI Healthcare Sensing
**Last Updated:** 2026-05-24
**Status:** Active — initial seed populated; verification in progress

> **Disclaimer:** This project uses **synthetic CSI data only**. No real patient data, clinical validation, or real hardware deployment is claimed. All reproducibility assessments below reflect the status of external references, not this project's own data.

---

## How to Read This Matrix

| Column | Meaning |
|---|---|
| Paper ID | Short key matching `papers.csv` |
| Public Code | GitHub URL or N/A |
| License | Verified license or Pending verification |
| Repro Status | Reproducible / Partially reproducible / Not reproducible / Pending verification |
| Dataset | Dataset used in original paper |
| Dataset License | License of dataset or Pending verification |
| Notes | Issues, gaps, or action items |

---

## Matrix

| Paper ID | Public Code | License | Repro Status | Dataset | Dataset License | Notes |
|---|---|---|---|---|---|---|
| attack_wifi_sensing | https://github.com/xdawnn/attack-wifi-sensing | MIT (pending confirmation) | Pending verification | Synthetic CSI | Pending verification | Primary attack reference; code not yet tested in this repo |
| sensefi | https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark | MIT (pending confirmation) | Pending verification | Multiple public CSI datasets | Pending verification | Key benchmark; multi-dataset; code not yet tested in this repo |
| antieave_wifi_sensing | https://github.com/example/antieave | Pending verification | Pending verification | Real CSI (lab) | Pending verification | Defense reference; real-data lab environment; cannot replicate with synthetic data |
| wifi_adg | https://github.com/example/wifi-adg | Pending verification | Pending verification | Synthetic/lab CSI | Pending verification | Adversarial defense generation; not tested |
| csigan | https://github.com/example/csigan | Pending verification | Pending verification | Synthetic CSI | Pending verification | GAN augmentation; not tested |
| csi_bench | N/A | Pending verification | Pending verification | Multiple CSI datasets | Pending verification | No confirmed public code; high-priority future dataset candidate |
| noisec | N/A | Pending verification | Pending verification | Lab CSI | Pending verification | Noise-based defense; WiFi CSI applicability not confirmed |
| infocom_2023_wifi_ap | N/A | N/A | Not reproducible from public artifacts | Lab CSI | Pending verification | Privacy risk reference only |
| wicam_wicam2 | N/A | N/A | Not reproducible from public artifacts | Lab CSI | Pending verification | Black-box attack reference only |
| wiintruder | N/A | N/A | Not reproducible from public artifacts | Lab CSI | Pending verification | Universal perturbation reference only |
| awesome_ris_security | https://github.com/example/awesome-ris-security | Pending verification | N/A (curated list) | N/A | N/A | Curated reading list; no code to reproduce |
| unilateral_csi_entropy | N/A | Pending verification | Pending verification | Synthetic/lab CSI | Pending verification | Entropy estimation reference; no confirmed public code |

---

## Summary Statistics

- **Total papers tracked:** 12
- **With public code URL:** 5
- **License confirmed:** 0 (all pending verification)
- **Reproducible (confirmed):** 0
- **Pending verification:** 9
- **Not reproducible from public artifacts:** 3

---

## Action Items

- [ ] Verify MIT license for `attack_wifi_sensing` and `sensefi` repos
- [ ] Test `attack_wifi_sensing` code against this repo's synthetic pipeline
- [ ] Test `sensefi` benchmark against this repo's model
- [ ] Verify DOIs for all entries in `references.bib`
- [ ] Check dataset licenses for all entries with public datasets
- [ ] Update status column as verification progresses

---

*This file is automatically cross-referenced by `papers.csv`. Update both files together.*
