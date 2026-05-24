# MM-Fi Dataset Card

> **Important:** Fields marked *Pending verification* have not been independently confirmed by this repository. All information should be verified against the official MM-Fi dataset page or associated paper before use.

---

## Dataset Summary

MM-Fi is described as a multi-modal WiFi sensing dataset with a focus on human activity and pose-related sensing. It is referenced in RuView documentation as a supported dataset for WiFi CSI-based human sensing research.

---

## Official Source

- **Official project page:** [https://ntu-aiot-lab.github.io/mm-fi](https://ntu-aiot-lab.github.io/mm-fi)
- **Official GitHub / tooling repository:** [https://github.com/ybhbingo/MMFi_dataset](https://github.com/ybhbingo/MMFi_dataset)
  - Provides dataset libraries and usage examples for loading MM-Fi
- **Associated paper (OpenReview):** [https://openreview.net/forum?id=1uAsASS1th](https://openreview.net/forum?id=1uAsASS1th)

> Official links are provided for convenience and reproducibility planning. Dataset files are not stored in this repository. License, exact access terms, and loader compatibility should be verified from the official sources before use.

---

## Associated Paper or Citation

> The associated paper is available at: https://openreview.net/forum?id=1uAsASS1th
> Verify the full citation from the official publication before using in academic work.

```bibtex
% TODO: Add MM-Fi BibTeX citation after verifying official citation from the paper/project page
```

---

## Data Modalities

- **Primary modality:** WiFi CSI (pending verification from official source)
- **Additional modalities:** Multi-modal (pending verification from official source)
- **Sensing hardware:** Pending verification

---

## Tasks

- **Primary task:** Human activity sensing / pose-related research (pending verification)
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

- **Format mentioned in RuView docs:** `.npy` (verify from official source/tooling repo)
- **Other formats:** Pending verification
- **Directory structure:** See official GitHub repository for verified structure

---

## Labels and Annotations

- **Activity labels:** Pending verification from official source
- **Pose annotations:** Pending verification from official source
- **Label schema:** Pending verification from official dataset documentation

---

## License and Access

- **License type:** Pending verification from official project page
- **Access method:** Pending verification (open access, request form, institutional access, etc.)
- **Redistribution allowed:** Pending verification — do not redistribute without confirming license
- **Commercial use allowed:** Pending verification

See `LICENSE_SUMMARY.md` for the running access and license status.

---

## Intended Use in This Repository

If integrated in the future, MM-Fi may be used for:

- Real CSI data benchmarking against the synthetic pipeline
- Adversarial robustness evaluation using real CSI signals
- Comparison of model generalization across synthetic and real data
- Reference for activity / pose sensing experimental design

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

- [ ] Verify exact license type and access requirements from the official project page
- [ ] Is redistribution of any portion of MM-Fi permitted?
- [ ] What activities/poses are labeled? (check official repo and paper)
- [ ] Confirm WiFi hardware and CSI format used
- [ ] Does MM-Fi include fall events? (not assumed by this repository)
- [ ] What is the correct BibTeX citation for MM-Fi?

---

*Last updated: May 2026*
