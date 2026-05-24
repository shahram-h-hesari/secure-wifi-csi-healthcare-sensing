# Wi-Pose Download Instructions

> **Warning:** Do not commit downloaded dataset files to this repository. All Wi-Pose data must remain local only.

---

## Official Download and Access Sources

Wi-Pose is a publicly available WiFi CSI pose estimation dataset. Use only the official sources listed below:

- **Official dataset repository:** [https://github.com/NjtechCVLab/Wi-PoseDataset](https://github.com/NjtechCVLab/Wi-PoseDataset)
  - Contains WiFi CSI data and pose annotations in `.mat` format
  - Described as publicly available in the associated CSI-Former paper
- **Associated paper (MDPI Entropy — CSI-Former):** [https://www.mdpi.com/1099-4300/25/1/20](https://www.mdpi.com/1099-4300/25/1/20)

> **Important:** Always download Wi-Pose from the official dataset repository above. Do not use unofficial mirrors or re-hosted versions without verifying they are authorized by the original dataset authors.

> **Official links are provided for convenience and reproducibility planning. Dataset files are not stored in this repository.**

---

## Recommended Local Storage

After downloading from the official source, store Wi-Pose data locally at:

```
data/external/wi-pose/
```

Example structure (verify against the actual directory layout from the official repo):

```
data/
  external/
    wi-pose/
      raw/
      processed/
      annotations/
      README_local.md   <-- your local notes on the download
```

The `data/external/` path is excluded from Git via `.gitignore`. This data will **not** be committed or pushed to the repository.

---

## Do Not Commit Dataset Files

**Critical rule:** Never add Wi-Pose data files to Git.

- `data/external/` is listed in `.gitignore`
- Common file extensions are also gitignored: `.mat`, `.npy`, `.npz`, `.h5`, `.zip`, `.tar`
- Do not add exceptions or force-add dataset files with `git add -f`
- If you accidentally stage dataset files, run: `git reset HEAD data/external/`

---

## Private Backup Policy

After downloading Wi-Pose from the official source, a **private backup** may be kept in Google Drive or another personal cloud storage service for convenience:

- A private backup is acceptable for **personal use only**
- Do **not** publish or share a private backup link unless the Wi-Pose dataset license explicitly permits redistribution
- Do **not** add a public Google Drive or cloud link to this repository unless redistribution is confirmed as permitted
- Always refer others to the official sources listed above

---

## Verification Checklist

Before using Wi-Pose in any experiment, complete all items:

- [ ] Review the official dataset repository: https://github.com/NjtechCVLab/Wi-PoseDataset
- [ ] Review the associated paper: https://www.mdpi.com/1099-4300/25/1/20
- [ ] Read and record the official license (update `LICENSE_SUMMARY.md`)
- [ ] Confirm whether redistribution is permitted
- [ ] Confirm whether registration or institutional access is required
- [ ] Download from the official source only
- [ ] Verify file integrity (checksums if provided)
- [ ] Verify folder structure and `.mat` file layout from official repo
- [ ] Verify pose keypoint schema and annotation format
- [ ] Confirm and record the correct citation (update `DATASET_CARD.md`)
- [ ] Record download date and version in `data/external/wi-pose/README_local.md`

---

## Future Loader Plan

Once Wi-Pose is downloaded and verified locally, a dataset loader may be added at:

```
scripts/load_wipose.py
```

or integrated into the main pipeline at:

```
src/data/
```

The loader should:
- Read from `data/external/wi-pose/` (local only, not committed)
- Parse `.mat` files per the official dataset repository structure
- Return standardized arrays compatible with the existing synthetic data pipeline
- Include assertions for expected file structure and pose keypoint schema

**Current status: No loader exists yet. This is planned future work.**

---

*Last updated: May 2026*
