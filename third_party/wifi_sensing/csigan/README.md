# CsiGAN — External Reference

## Repository Information

- **Name:** CsiGAN
- **GitHub URL:** https://github.com/ChunjingXiao/CsiGAN
- **Upstream Description:** An implementation for the paper: "CsiGAN: Robust Channel State Information-based Activity Recognition with GANs" (IEEE Internet of Things Journal, 2019). Semi-supervised Generative Adversarial Network (GAN) for WiFi Channel State Information (CSI)-based activity recognition.
- **Associated Paper:** Chunjing Xiao et al. "CsiGAN: Robust Channel State Information-based Activity Recognition with GANs." *IEEE Internet of Things Journal*, 2019.
- **License:** No LICENSE file detected in upstream repository (as of 2026-05-24). License status: **Pending verification — do not use or adapt code until license is confirmed.**
- **Category:** WiFi CSI Sensing / Data Augmentation / Robustness Support
- **Status:** External reference only — no code copied or adapted

---

## Purpose of This Folder

This folder is a tracking placeholder and attribution note for the `CsiGAN` repository.
No source code, binaries, or dataset files from `CsiGAN` have been copied into this repository.

---

## Relevance to This Project

- **GAN-Based Data Augmentation for CSI Activity Recognition:** CsiGAN implements a semi-supervised GAN framework for augmenting WiFi CSI data in activity recognition tasks. This is directly relevant to future experiments addressing class imbalance, limited labeled data, and synthetic-to-real CSI variation in this project.
- **Robustness Support for Victim Models:** Augmenting training data with GAN-generated CSI samples may improve the robustness and generalization of victim fall-detection models in the thesis adversarial evaluation pipeline.
- **Synthetic-to-Real CSI Gap:** CsiGAN's approach to learning CSI data distributions using GANs provides a reference for bridging the gap between synthetic CSI-like data (used in the current project) and real WiFi CSI hardware measurements in future experiments.
- **Semi-Supervised Learning Context:** The semi-supervised GAN architecture is relevant to scenarios with limited labeled fall or vital-sign data, a realistic constraint in elderly home monitoring deployments.
- **Augmentation Baseline Reference:** CsiGAN can serve as a baseline augmentation method for comparison with future GAN-based or diffusion-based data augmentation experiments in this project.

---

## Important Limitations

- This repository is **not** healthcare-specific. It focuses on general WiFi CSI-based activity recognition.
- This repository is **not** an adversarial attack repository.
- This repository is **not** an adversarial defense repository.
- This repository has **not** been used in the current project implementation.
- The current project uses **synthetic CSI-like data only**. No CsiGAN-generated or real CSI data has been used.
- This repository has **not** been used for training, validation, or benchmarking in the current project.

---

## License Status

- **Upstream License:** No LICENSE file detected in the upstream repository as of 2026-05-24. The task specification notes MIT as a candidate, but this must be verified manually before any code use.
- **License Status:** **Pending verification** — do not copy, adapt, or build upon this code until the license is confirmed.
- **Usage in This Project:** None — external reference only.
- **Future Reuse:** Any future code reuse, adaptation, or derivative work requires verifying the upstream license terms and providing proper attribution, including citation of the associated IEEE IoT Journal 2019 paper.

---

## Dataset Status

- **Dataset Availability:** Pending verification
- **Notes:** CsiGAN uses CSI activity-recognition datasets (potentially SignFi or similar). No dataset files are stored in this repository. A candidate entry has been added to `datasets/future_datasets/README.md` for future verification.

---

## Attribution

If any code or ideas from this repository are used in the future, proper attribution must be provided:

```
CsiGAN by ChunjingXiao (Chunjing Xiao et al.)
GitHub: https://github.com/ChunjingXiao/CsiGAN
Paper: Chunjing Xiao et al. "CsiGAN: Robust Channel State Information-based Activity Recognition with GANs."
        IEEE Internet of Things Journal, 2019.
License: Pending verification
```

---

*This README was created as part of the secure-wifi-csi-healthcare-sensing project's third-party reference tracking system.*
*Last updated: 2026-05-24*
