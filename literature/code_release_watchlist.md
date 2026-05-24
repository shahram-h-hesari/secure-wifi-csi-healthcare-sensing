# Code Release Watchlist

**Project:** Secure WiFi CSI Healthcare Sensing
**Last Updated:** 2026-05-24
**Purpose:** Track papers without confirmed public code that represent high-value reproducibility targets. Monitor for future code releases.

> **Disclaimer:** This project uses **synthetic CSI data only**.
> No real patient data, clinical validation, or real hardware deployment
> is claimed. All watchlist items below are external references, not this project's own code.

> **Rule:** No fake GitHub links are assigned to any watchlist entry. If no confirmed public repo exists, the code field says "No confirmed public GitHub found".

---

## Section A: Public Code Found but Not Tested

These projects have confirmed public GitHub repositories. They are **not** on the no-code watchlist.
They are listed here for reference. See `reproducibility_matrix.md` for full status.

| Paper ID | Project Name | Confirmed GitHub URL | License | Status |
|---|---|---|---|---|
| attack_wifi_sensing | Attack\_WiFi\_Sensing | https://github.com/Guolin-Yin/Attack_WiFi_Sensing | Pending verification | Public GitHub available; not tested locally |
| sensefi | SenseFi / WiFi CSI Sensing Benchmark | https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark | Pending verification | Public GitHub available; not tested locally |
| antieave_wifi_sensing | AntiEave-WiFi-Sensing | https://github.com/MoWiNG-Lab/AntiEave-WiFi-Sensing | Pending verification | Public GitHub available; not tested locally |
| wifi_adg | WiFi-ADG | https://github.com/siwangzhou/WiFi-ADG | Pending verification | Public GitHub available; not tested locally |
| csigan | CsiGAN | https://github.com/ChunjingXiao/CsiGAN | Pending verification | Public GitHub available; not tested locally |
| csi_bench | CSI-Bench Real WiFi Sensing Benchmark | https://github.com/guozhen-jenn-zhu/CSI-Bench-Real-WiFi-Sensing-Benchmark | MIT (verified) | Public GitHub available; not tested locally |
| noisec | NoiSec | https://github.com/shahriar0651/NoiSec | MIT (verified) | Public GitHub available; not tested locally |

---

## Section B: No-Code Watchlist — Primary (High Priority, Paper Cards Exist)

These papers have paper cards in `no_confirmed_code/` but no confirmed public GitHub as of 2026-05-24.

| Paper ID | Short Name | Year | Venue | Expected Code Type | Watch Priority | Status | Last Checked | Monitoring Actions |
|---|---|---|---|---|---|---|---|---|
| infocom_2023_wifi_apnea_attack | Adversarial Attack and Defense for WiFi-based Apnea Detection System | 2023 | IEEE INFOCOM 2023 Workshops (pending verification) | Attack/defense code | High | No public code confirmed | 2026-05-24 | Check IEEE Xplore; check author lab pages; check Papers With Code |
| mobicom_2024_preamble_perturbation | MobiCom 2024 preamble/packet perturbation attack | 2024 | ACM MobiCom 2024 (pending verification) | Attack code | High | No public code confirmed | 2026-05-24 | Check ACM DL artifact page; check author GitHub pages |
| wicam_wicam2 | WiCAM / WiCAM 2.0 | Pending verification | Pending verification | Adversarial sensing code | Medium | No public code confirmed | 2026-05-24 | Verify paper identity; check author pages; check GitHub search for WiCAM |
| wiintruder | WiIntruder | Pending verification | Pending verification | Adversarial attack/defense code | Medium | No public code confirmed | 2026-05-24 | Verify paper identity; check GitHub search for WiIntruder |

---

## Section C: No-Code Watchlist — Background References (Paper Cards Pending)

These papers have been identified as potentially relevant background references but no paper cards have been created yet.
All metadata is pending verification. No fake GitHub links are assigned.

| Short Name | Year | Venue | Expected Code Type | Watch Priority | Status | Monitoring Actions |
|---|---|---|---|---|---|---|
| WiAdv | Pending verification | Pending verification | Adversarial WiFi sensing attack code | Medium | No confirmed public GitHub found | Check Papers With Code; GitHub search for WiAdv |
| Wi-Spoof | Pending verification | Pending verification | WiFi sensing spoofing attack code | Medium | No confirmed public GitHub found | Check Papers With Code; GitHub search for Wi-Spoof |
| SecureSense | Pending verification | Pending verification | Adversarial robustness code | Medium | No confirmed public GitHub found | Check Papers With Code; GitHub search for SecureSense WiFi |
| RIStealth | Pending verification | Pending verification | RIS covert attack code | Low | No confirmed public GitHub found | Check author lab pages; conference artifact pages |
| LeakyBeam / BFIAttack | Pending verification | Pending verification | Beamforming feedback attack code | Low | No confirmed public GitHub found | Check author lab pages; conference artifact pages |
| IRShield | Pending verification | Pending verification | RIS-based defense code | Low | No confirmed public GitHub found | Check author lab pages |
| Physical-World Attack toward WiFi Behavior Recognition | Pending verification | Pending verification | Physical-world adversarial code | Medium | No confirmed public GitHub found | Check Papers With Code; GitHub search |
| Towards Trustworthy Wi-Fi CSI-based Sensing | Pending verification | Pending verification | Survey / framework code | Low | No confirmed public GitHub found | Check Papers With Code; author pages |

---

## When to Promote an Entry

When a confirmed repo is found for any watchlist item:
1. Verify the repo URL is the official one from original authors (not a fork or informal copy)
2. Move the paper card from `no_confirmed_code/` to the appropriate category folder
3. Update `papers.csv` code_status to `Public GitHub available`
4. Move the paper from Section B or C above to Section A
5. Update `reproducibility_matrix.md`
6. Do NOT claim code is tested unless it has actually been tested

---

## Monitoring Schedule

| Priority | Re-check interval |
|---|---|
| High | Every 3 months |
| Medium | Every 6 months |
| Low | Every 12 months or when manually triggered |

**Last Updated:** 2026-05-24
