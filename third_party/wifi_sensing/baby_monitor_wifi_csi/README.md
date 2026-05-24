# baby-monitor-wifi-csi — External Reference

## Repository Information

- **Name:** baby-monitor-wifi-csi (BabyGuard)
- **GitHub URL:** https://github.com/mohosy/baby-monitor-wifi-csi
- **Upstream Description:** Contactless baby breathing monitor using WiFi Channel State Information (CSI). Turns an ESP32 + any WiFi router into a real-time infant apnea detection system — no wearables or cameras needed.
- **License:** MIT (confirmed from upstream repository)
- **Category:** Healthcare-Relevant WiFi CSI / Breathing Monitoring / Apnea-Style Sensing Baseline
- **Status:** External reference only — no code copied or adapted

---

## Purpose of This Folder

This folder is a tracking placeholder and attribution note for the `baby-monitor-wifi-csi` repository.
No source code, binaries, or dataset files from this repository have been copied into this project.

---

## Relevance to This Project

- **WiFi CSI Breathing / Apnea-Style Sensing:** The repository implements contactless infant breathing monitoring using WiFi CSI collected from an ESP32 device. This is directly relevant to the thesis goal of using WiFi CSI for vital-sign monitoring in healthcare settings.
- **Healthcare Sensing Baseline:** Provides a concrete example of real-world WiFi CSI-based healthcare sensing, useful as a baseline reference for comparing architectures and approaches for vital-sign detection.
- **Contactless Monitoring Context:** Camera-free, wearable-free vital-sign monitoring is a core motivation for the thesis. This repository demonstrates a practical implementation using commodity hardware.
- **Future Vital-Sign Experiments:** May inform future experiments on extending the current project's synthetic pipeline toward real WiFi CSI-based breathing and vital-sign detection.
- **ESP32 / Router CSI Pipeline:** The use of ESP32 CSI firmware and standard WiFi routers provides relevant context for understanding low-cost CSI collection platforms relevant to elderly home monitoring deployments.

---

## Important Limitations

- This repository is **not** classified as an adversarial attack or adversarial defense repository.
- This repository has **not** been clinically validated. It is a prototype/research-grade tool.
- This project does **not** treat `baby-monitor-wifi-csi` as clinically validated or as a medical device.
- This repository has **not** been used in the current project implementation.
- The current project uses **synthetic CSI-like data only**. No real ESP32 CSI data has been collected or used.
- Dataset availability: **Pending verification** — no confirmed public downloadable CSI breathing dataset has been identified in the upstream repository.
- This repository has **not** been used for validation, training, or benchmarking in the current project.

---

## License Status

- **Upstream License:** MIT (verified from upstream repository badge and license indicator)
- **Usage in This Project:** None — external reference only
- **Future Reuse:** Any future code reuse, adaptation, or derivative work requires review of the MIT license terms and proper attribution to the original authors.

---

## Dataset Status

- **Dataset Availability:** Pending verification
- **Notes:** The upstream repository implements a real-time sensing system. No confirmed public downloadable breathing/apnea CSI dataset has been identified. A candidate entry has been added to `datasets/future_datasets/README.md` for future verification.

---

## Attribution

If any code or ideas from this repository are used in the future, proper attribution must be provided:

```
baby-monitor-wifi-csi (BabyGuard) by mohosy
GitHub: https://github.com/mohosy/baby-monitor-wifi-csi
License: MIT
```

---

*This README was created as part of the secure-wifi-csi-healthcare-sensing project's third-party reference tracking system.*
*Last updated: 2026-05-24*
