# Wi-Pose

## Source

Wi-Pose is a public WiFi CSI-based pose estimation dataset. It is referenced in RuView documentation as a supported dataset.

> **Source verification required.** Please refer to the official Wi-Pose dataset page or associated paper for authoritative metadata, subject count, license, and download instructions.

---

## Why This Dataset Is Included

Wi-Pose is included as a related WiFi CSI sensing dataset entry in this repository's catalog because:

- RuView (a third-party WiFi sensing project referenced in this repository) mentions Wi-Pose support in its documentation.
- Wi-Pose is relevant to the research area of WiFi CSI sensing and pose estimation.
- It may be valuable for future real-data benchmarking and robustness evaluation work related to CSI-based human pose inference.

---

## Relationship to This Repository

- Wi-Pose is cataloged as a **related dataset** for future planning purposes.
- This repository has **not yet independently integrated, downloaded, or evaluated** Wi-Pose.
- Wi-Pose is **not claimed as a fall-detection validation dataset** for this repository.
- Inclusion does **not** imply clinical validation or endorsement of Wi-Pose's performance claims.

---

## Current Integration Status

| Item | Status |
|------|--------|
| Dataset downloaded locally | No |
| Dataset integrated in pipeline | No |
| Used for fall-detection validation | No |
| Used for benchmarking | No |
| License independently verified | Pending |
| Citation confirmed | Pending |

Current repository experiments use **synthetic CSI-like data only**. Real-data integration is **future work**.

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `README.md` | This overview file |
| `DATASET_CARD.md` | Dataset metadata card with verified and pending fields |
| `LICENSE_SUMMARY.md` | License and access status summary |
| `DOWNLOAD_INSTRUCTIONS.md` | Safe download instructions and recommended local paths |

**Not present in this folder:**
- Raw dataset files
- Compressed dataset archives
- Binary data

---

## Limitations

- Dataset details (file formats, subject counts, pose annotation schema) have not been independently verified by this repository.
- All metadata fields marked 'Pending verification' should be confirmed against the official dataset source before use.
- Do not redistribute Wi-Pose data without verifying the official license.
- This repository does not make performance claims about Wi-Pose.
- Wi-Pose is a **pose estimation** dataset; it is not assumed to be a fall-detection dataset unless verified.

---

*Last updated: May 2026*
