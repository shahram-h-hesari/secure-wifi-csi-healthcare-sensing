# Wi-Pose Dataset Card

> **Important:** Fields marked *Pending verification* have not been independently confirmed by this repository. All information should be verified against the official Wi-Pose dataset page or associated paper before use.

---

## Dataset Summary

Wi-Pose is a WiFi CSI-based pose estimation dataset. It is referenced in RuView documentation as a supported dataset for WiFi CSI-based human pose inference research.

---

## Official Source

- **Official dataset repository:** [https://github.com/NjtechCVLab/Wi-PoseDataset](https://github.com/NjtechCVLab/Wi-PoseDataset)
  - Contains WiFi CSI data and pose annotations in `.mat` format
  - Described as publicly available in the associated CSI-Former paper
- **Associated paper (MDPI Entropy — CSI-Former):** [https://www.mdpi.com/1099-4300/25/1/20](https://www.mdpi.com/1099-4300/25/1/20)

> Official links are provided for convenience and reproducibility planning. Dataset files are not stored in this repository. License, exact access terms, and loader compatibility should be verified from the official sources before use.

---

## Associated Paper or Citation

> The associated CSI-Former paper is available at: https://www.mdpi.com/1099-4300/25/1/20 (MDPI Entropy, 2023)
> Verify the full citation from the official publication before using in academic work.

```bibtex
% TODO: Add Wi-Pose / CSI-Former BibTeX citation after verifying official citation from the paper page
```

---

## Data Modalities

- **Primary modality:** WiFi CSI (pending verification from official source)
- **Additional modalities:** Pose-related annotations (pending verification from official source)
- **Sensing hardware:** Pending verification

---

## Tasks

- **Primary task:** WiFi-based human pose estimation (pending verification)
- **Secondary tasks:** Pending verification from official source
- **Is this a fall-detection dataset?** Not claimed by this repository. Do not assume fall-detection validation.

---

## Subjects and Environment

- **Number of subjects:** Pending verification from official source
- **Age range:** Pending verification
- **Collection environment:** Pending verification (indoor, number of rooms, etc.)
- **WiFi equipment / setup:** Pending verification

---

## File Formats

- **Format mentioned in RuView docs:** `.mat` (verify from official dataset repository)
- **Other formats:** Pending verification
- **Directory structure:** See official GitHub repository for verified structure

---

## Labels and Annotations

- **Pose keypoints / skeleton:** Pending verification from official source
- **Activity labels:** Pending verification from official source
- **Label schema:** Pending verification from official dataset documentation

---

## License and Access

- **License type:** Pending verification from official dataset repository
- **Access method:** Pending verification (open access, request form, institutional access, etc.)
- **Redistribution allowed:** Pending verification — do not redistribute without confirming license
- **Commercial use allowed:** Pending verification

See `LICENSE_SUMMARY.md` for the running access and license status.

---

## Intended Use in This Repository

If integrated in the future, Wi-Pose may be used for:

- Real CSI data benchmarking against the synthetic pipeline
- WiFi pose/CSI benchmarking and pose inference experiments
- Adversarial robustness evaluation using real CSI signals
- Comparison of model generalization across synthetic and real data

**Current status: Cataloged only; not downloaded, not integrated, and not used for validation in this repository.**

---

## Current Status

| Item | Status |
|------|--------|
| Cataloged in this repository | Yes |
| Official source links added | Yes |
| Downloaded locally | No |
| Loaded into pipeline | No |
| Used for model training | No |
| Used for validation | No |
| Used for benchmarking | No |
| License verified | Pending |
| Citation confirmed | Pending |

---

## Open Questions

- [ ] Verify exact license type and access requirements from the official dataset repository
- [ ] Is redistribution of any portion of Wi-Pose permitted?
- [ ] What pose keypoints and activities are labeled? (check official repo)
- [ ] Confirm WiFi hardware and CSI format details
- [ ] Does Wi-Pose include fall events? (not assumed by this repository)
- [ ] What is the correct BibTeX citation for Wi-Pose / CSI-Former?
- [ ] How many subjects and environments are included?

---

*Last updated: May 2026*
