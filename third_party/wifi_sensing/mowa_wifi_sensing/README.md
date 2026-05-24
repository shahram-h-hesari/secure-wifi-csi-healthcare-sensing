# mowa-wifi-sensing — External Reference

## Repository Information

- **Name:** mowa-wifi-sensing
- **GitHub URL:** https://github.com/oss-inc/mowa-wifi-sensing
- **Related Fork URL:** https://github.com/cheeseBG/wifi-sensing
- **Upstream Description:** Wi-Fi sensing model of MOWA — real-time Wi-Fi CSI-based human activity recognition using Nexmon CSI extractor.
- **License:** BSD-3-Clause (confirmed from upstream repository)
- **Category:** Healthcare-Relevant WiFi CSI / Fall Detection / Human Activity Recognition Baseline
- **Status:** External reference only — no code copied or adapted

---

## Purpose of This Folder

This folder is a tracking placeholder and attribution note for the `mowa-wifi-sensing` repository.
No source code, binaries, or dataset files from `mowa-wifi-sensing` have been copied into this repository.

---

## Relevance to This Project

- **WiFi CSI Fall/HAR Baseline:** The repository implements real-time WiFi CSI-based human activity recognition (HAR) using Nexmon CSI on Raspberry Pi. This is directly relevant to fall-detection baseline research, as HAR systems that classify fall-related activities are foundational for healthcare WiFi sensing.
- **Nexmon CSI Pipeline:** Uses the Nexmon CSI extractor for real device CSI collection — relevant context for understanding the gap between the current project's synthetic CSI-like data and real-world CSI collection pipelines.
- **Meta-Learning Support:** The upstream repository notes support for both supervised learning and meta-learning, which is relevant to the thesis interest in domain generalization for WiFi sensing across different environments.
- **Elderly Monitoring Context:** HAR with fall-related activity classes is a core sensing task for the thesis goal of detecting falls in elderly homes.
- **Future Baseline Comparison:** This repository is a candidate for future real-data baseline comparison once real WiFi CSI data is integrated into this project.

---

## Important Limitations

- This repository is **not** classified as an adversarial attack or adversarial defense repository.
- This repository is **not** a healthcare-specific or clinically validated repository.
- This repository has **not** been used in the current project implementation.
- The current project uses **synthetic CSI-like data only**. No real Nexmon CSI data has been collected or used.
- Dataset availability: **Pending verification** — the repository may expect real-time CSI input or domain-specific CSI folders (e.g., `csi_dataset/domain_A`, `domain_B`), but no confirmed public downloadable dataset has been identified.
- This repository has **not** been used for validation, training, or benchmarking in the current project.

---

## License Status

- **Upstream License:** BSD-3-Clause (verified from upstream `LICENSE` file)
- **Usage in This Project:** None — external reference only
- **Future Reuse:** Any future code reuse, adaptation, or derivative work requires review of the BSD-3-Clause license terms and proper attribution to the original authors (oss-inc / Jungik Jang, Pio).

---

## Dataset Status

- **Dataset Availability:** Pending verification
- **Notes:** The upstream repository uses Nexmon CSI data collected in real-time. It may reference or expect CSI dataset directories with fall/HAR activity classes. No confirmed public downloadable dataset has been identified. A candidate entry has been added to `datasets/future_datasets/README.md` as `mowa-fall-har` for future verification.

---

## Attribution

If any code or ideas from this repository are used in the future, proper attribution must be provided:

```
mowa-wifi-sensing by oss-inc (Jungik Jang, Pio)
GitHub: https://github.com/oss-inc/mowa-wifi-sensing
License: BSD-3-Clause
```

---

*This README was created as part of the secure-wifi-csi-healthcare-sensing project's third-party reference tracking system.*
*Last updated: 2026-05-24*
