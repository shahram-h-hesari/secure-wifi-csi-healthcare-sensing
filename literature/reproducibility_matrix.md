# Reproducibility Matrix

**Project:** Secure WiFi CSI Healthcare Sensing
**Last Updated:** 2026-05-24
**Status:** Active — initial seed populated; verification in progress

> **Disclaimer:** This project uses **synthetic CSI data only**.
> No real patient data, clinical validation, or real hardware deployment
> is claimed. All reproducibility assessments below reflect the status
> of external references, not this project's own data.

---

## How to Read This Matrix

| Column | Meaning |
|---|---|
| Paper ID | Short key matching `papers.csv` |
| Public Code | GitHub URL or N/A |
| License | Verified license or Pending verification |
| Repro Status | Reproducible / Partially reproducible / Not reproducible / Pending |
| Dataset | Dataset used in original paper |
| Dataset License | License of dataset or Pending verification |
| Notes | Issues, gaps, or action items |

---

## Matrix

| Paper ID | Public Code | License | Repro Status | Dataset | Dataset License | Notes |
|---|---|---|---|---|---|---|
| attack_wifi_sensing | https://github.com/Guolin-Yin/Attack_WiFi_Sensing | MIT | Pending verification | Synthetic CSI | Pending verification | Verified URL; code not yet tested in this repo |
| sensefi | https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark | MIT | Pending verification | Multiple public CSI datasets | Pending verification | Verified URL; code not yet tested in this repo |
| antieave_wifi_sensing | N/A — not found | Pending verification | Pending verification | Real CSI (lab) | Pending verification | No confirmed public repo; defense reference only |
| wifi_adg | N/A — not found | Pending verification | Pending verification | Synthetic/lab CSI | Pending verification | No confirmed public repo; adversarial defense ref only |
| csigan | N/A — not found | Pending verification | Pending verification | Synthetic CSI | Pending verification | No confirmed public repo; GAN augmentation ref only |
| csi_bench | N/A | Pending verification | Pending verification | Multiple CSI datasets | Pending verification | No confirmed public code; high-priority future dataset |
| noisec | N/A | Pending verification | Pending verification | Lab CSI | Pending verification | Noise-based defense; WiFi CSI applicability not confirmed |
| infocom_2023_wifi_ap | N/A | N/A | Not reproducible from public artifacts | Lab CSI | Pending verification | Privacy risk reference only |
| infocom_2023_wifi_apnea_attack | N/A | N/A | Not reproducible from public artifacts | Lab CSI | Pending verification | Clinical adversarial attack reference; metadata pending |
| wicam_wicam2 | N/A | N/A | Not reproducible from public artifacts | Lab CSI | Pending verification | Privacy threat model reference only |
| wiintruder | N/A | N/A | Not reproducible from public artifacts | Lab CSI | Pending verification | Intrusion detection reference only |
| awesome_ris_security | Pending verification | Pending verification | N/A (curated list) | N/A | N/A | Curated reading list; no code to reproduce |
| unilateral_csi_entropy | N/A | Pending verification | Pending verification | Synthetic/lab CSI | Pending verification | Entropy estimation reference; no confirmed public code |

---

## Summary

| Status | Count |
|---|---|
| Verified public code (URL confirmed) | 2 |
| No confirmed public code | 10 |
| N/A (curated list / no code expected) | 1 |

**Last Updated:** 2026-05-24
