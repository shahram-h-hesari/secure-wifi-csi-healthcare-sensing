# WiFi-CSI-Human-Pose-Detection — External Reference

## Repository Information

- **Name:** WiFi-CSI-Human-Pose-Detection
- **GitHub URL:** https://github.com/euaziel/WiFi-CSI-Human-Pose-Detection
- **Upstream Description:** Human pose estimation using WiFi Channel State Information (CSI) and deep learning — enabling camera-free sensing through walls.
- **License:** GPL-3.0 (confirmed from upstream repository)
- **Category:** WiFi CSI Sensing / Pose Sensing / Domain Generalization
- **Status:** External reference only — no code copied or adapted

---

## Placement Note

This folder is placed under `third_party/wifi_sensing/` (general sensing) because the upstream repository does **not** explicitly confirm adversarial domain generalization or adversarial robustness. The repository focuses on human pose estimation through walls using WiFi CSI and deep learning. No adversarial attack or defense framework has been confirmed in the upstream README.

---

## Purpose of This Folder

This folder is a tracking placeholder and attribution note for the `WiFi-CSI-Human-Pose-Detection` repository.
No source code, binaries, or dataset files from this repository have been copied into this project.

---

## Relevance to This Project

- **WiFi CSI Human Pose Sensing:** Directly relevant to fall-detection contexts where human body pose and movement are inferred from WiFi CSI signals, similar to the thesis goal of detecting falls in elderly home monitoring.
- **Through-Wall Sensing:** Through-wall CSI-based sensing is a key capability referenced in the thesis adversarial threat model — an attacker may exploit through-wall sensing for unauthorized surveillance.
- **Fall Detection Context:** Pose estimation via WiFi CSI can serve as a more granular baseline for fall-detection experiments, complementing activity classification approaches.
- **Elderly Monitoring Relevance:** Camera-free sensing is directly applicable to elderly home monitoring scenarios where privacy must be preserved.
- **Robustness / Domain Generalization:** The use of deep learning for WiFi CSI across diverse environments may inform future robustness and domain-generalization experiments.

---

## Important Limitations

- This repository is **not** classified as an adversarial attack or adversarial defense repository. No adversarial domain generalization has been confirmed in the upstream README.
- This repository is **not** a healthcare-specific or clinically validated repository.
- This repository has **not** been used in the current project implementation.
- The current project uses **synthetic CSI-like data only**.
- Dataset status: **Pending verification** — no confirmed public CSI dataset has been identified in the upstream repository.

---

## License Status

- **Upstream License:** GPL-3.0 (verified from upstream repository)
- **Usage in This Project:** None — external reference only
- **Future Reuse:** Any future code reuse, adaptation, or derivative work requires review of the GPL-3.0 license terms. GPL-3.0 imposes copyleft requirements on derivative works. Proper attribution to the original authors is mandatory.

---

## Dataset Status

- **Dataset Availability:** Pending verification
- **Notes:** The upstream repository may contain or reference CSI pose/through-wall data. No confirmed public downloadable dataset has been identified. A candidate entry has been added to `datasets/future_datasets/README.md` for future verification.

---

## Attribution

If any code or ideas from this repository are used in the future, proper attribution must be provided:

```
WiFi-CSI-Human-Pose-Detection by euaziel (Aziel S.)
GitHub: https://github.com/euaziel/WiFi-CSI-Human-Pose-Detection
License: GPL-3.0
```

---

*This README was created as part of the secure-wifi-csi-healthcare-sensing project's third-party reference tracking system.*
*Last updated: 2026-05-24*
