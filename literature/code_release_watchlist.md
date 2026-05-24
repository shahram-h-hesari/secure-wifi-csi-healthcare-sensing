# Code Release Watchlist

**Project:** Secure WiFi CSI Healthcare Sensing
**Last Updated:** 2026-05-24
**Purpose:** Track papers and repositories that currently lack public code but represent high-value reproducibility targets. Monitor for future code releases.

> **Disclaimer:** This project uses **synthetic CSI data only**. No real patient data, clinical validation, or real hardware deployment is claimed. All watchlist items below are external references, not this project's own code.

---

## Watchlist

| Paper ID | Paper Title | Year | Venue | Expected Code | Watch Priority | Status | Last Checked | Notes |
|---|---|---|---|---|---|---|---|---|
| csi_bench | CSI-Bench: A Benchmark for WiFi CSI-Based Sensing | 2024 | arXiv | Dataset + code | High | No public code confirmed | 2026-05-24 | High-priority; benchmark paper; monitor arXiv + GitHub |
| noisec | NoiSec: Exploiting Noise for Adversarial Attacks and Defenses in WiFi Sensing | 2023 | ACM CCS | Attack/defense code | High | No public code confirmed | 2026-05-24 | ACM CCS papers often release code within 6-12 months |
| infocom_2023_wifi_ap | Exposing Wireless Eavesdropping Risks from WiFi APs | 2023 | IEEE INFOCOM | Attack demo | Medium | No public code confirmed | 2026-05-24 | Privacy risk paper; monitor IEEE Xplore author page |
| wicam_wicam2 | WiCam: Recognizing People Behind Walls Using WiFi | 2021 | ACM MobiSys | Sensing code | Medium | No public code confirmed | 2026-05-24 | ACM MobiSys; check author GitHub page |
| wiintruder | WiIntruder: Detecting Intrusions in WiFi-Based Vital Sensing | 2022 | IEEE SECON | Defense code | Medium | No public code confirmed | 2026-05-24 | IEEE SECON; monitor IEEE Xplore |
| unilateral_csi_entropy | Unilateral CSI Entropy Estimation for WiFi Sensing | 2023 | IEEE WCNC | Estimation code | Low | No public code confirmed | 2026-05-24 | Utility reference; lower priority |
| antieave_wifi_sensing | AntiEave: Defending Against Eavesdropping WiFi Sensing Attacks | 2023 | IEEE INFOCOM | Defense code | High | Placeholder only (https://github.com/example/antieave) | 2026-05-24 | Verify if real repo exists; Pending verification |
| wifi_adg | WiFi-ADG: Adversarial Defense Generation for WiFi Sensing | 2022 | IEEE GLOBECOM | Defense code | High | Placeholder only (https://github.com/example/wifi-adg) | 2026-05-24 | Verify if real repo exists; Pending verification |
| csigan | CSI-GAN: Generative Adversarial Network for CSI Augmentation | 2022 | IEEE Access | GAN code | Medium | Placeholder only (https://github.com/example/csigan) | 2026-05-24 | Verify if real repo exists; Pending verification |

---

## How to Update This Watchlist

1. Check the paper's GitHub, arXiv, or author page for a new code release
2. If code is released: update `papers.csv` `public_code_url` and `reproducibility_status` columns
3. Update `reproducibility_matrix.md` with new status
4. Move paper card from `paper_cards/no_confirmed_code/` to `paper_cards/with_public_code/`
5. Update this watchlist: change Status to **Released** and add release date
6. If license is confirmed, update `references.bib` note field

---

## Watch Priority Guide

| Priority | Meaning |
|---|---|
| High | Critical for thesis reproducibility or defense evaluation; check monthly |
| Medium | Useful reference; check quarterly |
| Low | Background reference; check annually |

---

## Recently Released (Graduates from Watchlist)

*None yet. Update when a watched item releases code.*

---

*Cross-referenced by `papers.csv`, `reproducibility_matrix.md`, and `paper_cards/`. Update all three files together when code is released.*
