# Wi-Pose Download Instructions

> **Warning:** Do not commit downloaded dataset files to this repository. All Wi-Pose data must remain local only.

---

## Official Download Source

- **Official URL:** Pending verification
  - Search for "Wi-Pose dataset WiFi CSI" on Google Scholar, GitHub, or the IEEE DataPort / Zenodo platforms
  - Once identified, update this file with the verified URL
- **Associated paper:** Pending verification (see `DATASET_CARD.md`)
- **Mirror or alternative:** Pending verification

> **Note:** Do not use unofficial mirrors or re-hosted versions of Wi-Pose without verifying they are authorized by the original dataset authors.

---

## Recommended Local Storage

After downloading, store Wi-Pose data locally at:

```
data/external/wi-pose/
```

Example structure (pending verification of actual directory layout):

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
- Common Wi-Pose file extensions are also gitignored: `.mat`, `.npy`, `.npz`, `.h5`, `.zip`, `.tar`
- Do not add exceptions or force-add dataset files with `git add -f`
- If you accidentally stage dataset files, run: `git reset HEAD data/external/`

---

## Verification Checklist

Before using Wi-Pose in any experiment, complete all items:

- [ ] Identify and record the official Wi-Pose download URL
- [ ] Read and record the official license (update `LICENSE_SUMMARY.md`)
- [ ] Confirm whether redistribution is permitted
- [ ] Confirm whether institutional or personal registration is required
- [ ] Download from the official source only
- [ ] Verify file integrity (checksums if provided)
- [ ] Verify folder structure matches expected layout
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
- Parse `.mat` or other verified format files
- Return standardized arrays compatible with the existing synthetic data pipeline
- Include assertions for expected file structure and pose keypoint schema

**Current status: No loader exists yet. This is planned future work.**

---

*Last updated: May 2026*
