# Reproducibility Matrix

**Project:** Secure WiFi CSI Healthcare Sensing
**Last Updated:** 2026-05-24
**Status:** Active — initial seed populated; reproducibility verification in progress

> **Disclaimer:** This project uses **synthetic CSI data only**.
> No real patient data, clinical validation, or real hardware deployment is claimed.
> All reproducibility assessments below reflect the status of external references only.

> **Important:** "Public GitHub available" does NOT mean code has been tested, reproduced, or integrated.
> All entries below default to **Tested Locally: No** and **Reproducibility Status: Not tested** unless evidence exists in this repository.

---

## Status Legend

| Score | Meaning |
|---|---|
| A | Official code + dataset available; installation tested; baseline reproduced locally |
| B | Official code available; dataset available or documented; not yet reproduced locally |
| C | Code available but dataset missing, unclear, or license/access unresolved |
| D | Paper available but no confirmed public code |
| E | Unverified or weak relevance; watchlist/background only |

> **Note:** Scores should be conservative. Do not assign A unless code actually runs locally and results are reproduced.
> Most entries begin at B, C, D, or Pending verification.

| Reproducibility Status | Meaning |
|---|---|
| Not tested | Public code or paper exists but code has not been run locally |
| Not reproducible from public code yet | No confirmed public code found; cannot reproduce |
| Pending verification | Status unknown; not yet assessed |

---

## Section 1: Public Code Available but Not Tested

These projects have a confirmed public GitHub repository but code has **not been tested or reproduced** in this repository.

| Paper ID | Project Name | GitHub URL | License | Tested Locally | Reproducibility Status | Score | Notes |
|---|---|---|---|---|---|---|---|
| attack_wifi_sensing | Attack\_WiFi\_Sensing | https://github.com/Guolin-Yin/Attack_WiFi_Sensing | Pending verification | No | Not tested | B | Core adversarial attack/defense reference |
| sensefi | SenseFi / WiFi CSI Sensing Benchmark | https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark | Pending verification | No | Not tested | B | Key WiFi CSI benchmark; DOI: 10.1016/j.patter.2023.100764 |
| antieave_wifi_sensing | AntiEave-WiFi-Sensing | https://github.com/MoWiNG-Lab/AntiEave-WiFi-Sensing | Pending verification | No | Not tested | B | Defense paper; IEEE PerCom 2023 |
| wifi_adg | WiFi-ADG | https://github.com/siwangzhou/WiFi-ADG | Pending verification | No | Not tested | C | Dataset via external Baidu link; access pending verification |
| csigan | CsiGAN | https://github.com/ChunjingXiao/CsiGAN | Pending verification | No | Not tested | B | CSI data augmentation; DOI: 10.1109/JIOT.2019.2936580 |

---

## Section 2: Dataset and Benchmark Candidates

These repositories provide datasets or benchmarks that are **candidates** for future integration but have not been downloaded, integrated, or used in this repository.

| Paper ID | Project Name | GitHub URL | License | Tested Locally | Dataset Status | Score | Notes |
|---|---|---|---|---|---|---|---|
| csi_bench | CSI-Bench Real WiFi Sensing Benchmark | https://github.com/guozhen-jenn-zhu/CSI-Bench-Real-WiFi-Sensing-Benchmark | MIT (verified) | No | Candidate dataset / benchmark pending verification | B | Benchmark repo available; not tested; not downloaded |

---

## Section 3: Defense-Method References

These repositories provide defense methods referenced in the thesis but **not implemented** in this repository.

| Paper ID | Project Name | GitHub URL | License | Tested Locally | Reproducibility Status | Score | Notes |
|---|---|---|---|---|---|---|---|
| noisec | NoiSec | https://github.com/shahriar0651/NoiSec | MIT (verified) | No | Not tested | B | Noise-based defense; WiFi CSI applicability pending verification |

---

## Section 4: Important Paper-Only Works with No Confirmed Public Code

These papers are high-relevance references but no confirmed public code repository has been found. They cannot be reproduced from public artifacts.

| Paper ID | Short Name | Year | Venue (pending verification) | Confirmed Public Code | Reproducibility Status | Score | Notes |
|---|---|---|---|---|---|---|---|
| infocom_2023_wifi_apnea_attack | Adversarial Attack and Defense for WiFi-based Apnea Detection System | 2023 | IEEE INFOCOM 2023 Workshops | No confirmed public GitHub found | Not reproducible from public code yet | D | High relevance: healthcare WiFi CSI; adversarial attack/defense; clinical safety |
| mobicom_2024_preamble_perturbation | MobiCom 2024 packet/preamble perturbation attack | 2024 | ACM MobiCom 2024 | No confirmed public GitHub found | Not reproducible from public code yet | D | Physical-layer WiFi sensing attack; all metadata pending verification |
| wicam_wicam2 | WiCAM / WiCAM 2.0 | Pending verification | Pending verification | No confirmed public GitHub found | Not reproducible from public code yet | D | Adversarial WiFi sensing reference; all metadata pending verification |
| wiintruder | WiIntruder | Pending verification | Pending verification | No confirmed public GitHub found | Not reproducible from public code yet | D | Adversarial WiFi sensing / perturbation attack reference; all metadata pending verification |
| wiadv | WiAdv | Pending verification | Pending verification | No confirmed public GitHub found | Not reproducible from public code yet | E | Adversarial WiFi sensing background reference; code not confirmed |
| wi_spoof | Wi-Spoof | Pending verification | Pending verification | No confirmed public GitHub found | Not reproducible from public code yet | E | WiFi sensing spoofing attack background reference |
| securesense | SecureSense | Pending verification | Pending verification | No confirmed public GitHub found | Not reproducible from public code yet | E | Adversarial robustness for WiFi sensing background reference |
| ristealth | RIStealth | Pending verification | Pending verification | No confirmed public GitHub found | Not reproducible from public code yet | E | RIS-based covert attack background reference |
| leakybeam_bfiattack | LeakyBeam / BFIAttack | Pending verification | Pending verification | No confirmed public GitHub found | Not reproducible from public code yet | E | Beamforming feedback attack background reference |
| irshield | IRShield | Pending verification | Pending verification | No confirmed public GitHub found | Not reproducible from public code yet | E | RIS-based defense background reference |
| physical_world_attack_wifi | Physical-World Attack toward WiFi Behavior Recognition | Pending verification | Pending verification | No confirmed public GitHub found | Not reproducible from public code yet | E | Physical-world adversarial WiFi sensing attack background reference |
| trustworthy_wifi_csi | Towards Trustworthy Wi-Fi CSI-based Sensing | Pending verification | Pending verification | No confirmed public GitHub found | Not reproducible from public code yet | E | Trustworthy WiFi CSI sensing survey background reference |

> **Note:** Entries marked E above are background references that have been identified as potentially relevant but not yet formally screened or paper-card created. Metadata is pending verification. No fake GitHub links are assigned to these entries.

---

## Summary Counts

| Category | Count |
|---|---|
| Public GitHub available (URL confirmed) | 7 |
| Public GitHub available, tested locally | 0 |
| No confirmed public GitHub found (paper-only, tracked) | 4 |
| No confirmed public GitHub found (background / watchlist) | 8 |
| Total tracked in papers.csv | 11 |

---

## Next Reproducibility Tasks

In priority order:

1. **attack_wifi_sensing**: Clone and run `ATKMethods.py` baseline; verify environment setup
2. **sensefi**: Clone and run benchmark evaluation pipeline; verify dataset access
3. **csi_bench**: Verify dataset accessibility and download protocol
4. **noisec**: Clone and verify installation; assess WiFi CSI applicability
5. **antieave_wifi_sensing**: Clone and verify installation; check git-lfs dataset access
6. **csigan**: Clone and verify installation; check SignFi dataset access
7. **wifi_adg**: Clone and verify installation; check Baidu dataset link
8. **infocom_2023_wifi_apnea_attack**: Search for paper release; check IEEE Xplore and author pages
9. **wicam_wicam2**: Verify paper identity; search for code release
10. **wiintruder**: Verify paper identity; search for code release

**Last Updated:** 2026-05-24
