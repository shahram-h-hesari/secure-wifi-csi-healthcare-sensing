# Third-Party References

This directory organizes related open-source work in WiFi sensing and WiFi sensing security that is referenced by this research repository.

---

## Purpose

Projects collected here serve the following research purposes:

- **Literature review**: Understanding the state of the art in WiFi-based sensing and security.
- **Technical comparison**: Evaluating different pipeline designs, signal processing approaches, and model architectures.
- **Reproducibility testing**: Running or inspecting third-party code to verify reported results.
- **Research inspiration**: Identifying gaps, limitations, and open problems that motivate this repository's direction.

> **Important:** These folders are tracking placeholders and attribution notes only. Third-party code is **not** copied or vendored into this repository unless a license review and proper attribution have been completed. All entries marked as external references have not been used for training, validation, or benchmarking in the current project.

---

## Structure

```
third_party/
├── wifi_sensing/                      # WiFi CSI sensing, activity recognition, fall detection, and related applications
│   ├── ruview/                          # RuView: WiFi spatial intelligence and vital sign monitoring
│   ├── sensefi/                         # SenseFi / WiFi CSI Sensing Benchmark: deep-learning WiFi CSI benchmark
│   ├── esp_csi/                         # ESP-CSI: ESP32-based CSI collection and hardware prototyping
│   ├── wifi_csi_human_pose_detection/   # WiFi-CSI-Human-Pose-Detection: pose sensing / domain generalization (general sensing)
│   ├── mowa_wifi_sensing/               # mowa-wifi-sensing: WiFi CSI HAR / fall baseline (Nexmon CSI, BSD-3-Clause)
│   └── baby_monitor_wifi_csi/           # baby-monitor-wifi-csi: WiFi CSI breathing / apnea baseline (ESP32, MIT)
└── wifi_sensing_security/             # Adversarial attacks, CSI spoofing, privacy, and robustness evaluation
    ├── attack_wifi_sensing/             # Attack_WiFi_Sensing: adversarial evasion and robustness evaluation
    ├── awesome_ws_security/             # Awesome-WS-Security: curated wireless sensing security literature
    ├── antieave_wifi_sensing/           # AntiEave-WiFi-Sensing: anti-eavesdropping and scheduled spatial sensing defense
    ├── wifi_adg/                        # WiFi-ADG: adversarial WiFi sensing for privacy preservation
    └── goop_veil/                       # goop-veil: software-only WiFi CSI privacy defense (Apache-2.0)
```

---

## Folder Content Summary

### wifi_sensing/

| Folder | Description | License | Status |
|---|---|---|---|
| `ruview/` | WiFi spatial intelligence and vital sign sensing. | Pending verification | External reference only |
| `sensefi/` | Deep-learning WiFi CSI benchmark framework. | MIT | External reference only |
| `esp_csi/` | ESP32-based CSI collection and hardware prototyping. | Apache-2.0 | External reference only |
| `wifi_csi_human_pose_detection/` | Human pose estimation via WiFi CSI; through-wall sensing; pose/domain-generalization baseline. Placed here because no adversarial domain generalization confirmed in upstream. | GPL-3.0 | External reference only; dataset pending verification |
| `mowa_wifi_sensing/` | Real-time WiFi CSI-based HAR using Nexmon CSI extractor. Fall/HAR baseline candidate. Not an adversarial/security repo. | BSD-3-Clause | External reference only; dataset pending verification |
| `baby_monitor_wifi_csi/` | Contactless baby breathing monitor via WiFi CSI and ESP32. Breathing/apnea sensing baseline. Not an adversarial/security repo. Not clinically validated. | MIT | External reference only; dataset pending verification |

### wifi_sensing_security/

| Folder | Description | License | Status |
|---|---|---|---|
| `attack_wifi_sensing/` | Adversarial evasion attacks and robustness evaluation. | Pending verification | External reference only |
| `awesome_ws_security/` | Curated literature on wireless sensing security, attacks, privacy, and defenses. | Pending verification | External reference only |
| `antieave_wifi_sensing/` | Anti-eavesdropping and scheduled spatial sensing defense (IEEE PerCom 2023). | Pending verification | External reference only |
| `wifi_adg/` | Adversarial WiFi sensing for privacy preservation (IEEE Communications Letters 2019). | Pending verification | External reference only |
| `goop_veil/` | Software-only WiFi CSI privacy defense: detect, degrade, and document CSI surveillance. Router-side mitigation. | Apache-2.0 | External reference only; dataset not confirmed |

---

## Important Notes

- **No code is copied or vendored** from any of these repositories unless a license review and proper attribution have been completed.
- **No datasets** from these repositories have been downloaded or integrated into this project.
- These folders exist as **tracking placeholders** to document external references for future research, benchmarking, and reproducibility planning.
- The current project implementation uses **synthetic CSI-like data only**.
- See `THIRD_PARTY_NOTICES.md` for full third-party attribution and license notices.

---

*Last updated: 2026-05-24*
