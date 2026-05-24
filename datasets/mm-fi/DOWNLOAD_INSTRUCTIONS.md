# MM-Fi Download Instructions

> **Warning:** Do not commit downloaded dataset files to this repository. All MM-Fi data must remain local only.

---

## Official Download and Access Sources

MM-Fi is a publicly released multi-modal human sensing dataset. Use only the official sources listed below:

- **Official project page:** [https://ntu-aiot-lab.github.io/mm-fi](https://ntu-aiot-lab.github.io/mm-fi)
- **Official GitHub / tooling repository:** [https://github.com/ybhbingo/MMFi_dataset](https://github.com/ybhbingo/MMFi_dataset)
  - Provides dataset libraries, usage examples, and tooling for loading and using MM-Fi
- **Associated paper (OpenReview):** [https://openreview.net/forum?id=1uAsASS1th](https://openreview.net/forum?id=1uAsASS1th)

> **Important:** Always download MM-Fi from the official project page or GitHub repository above. Do not use unofficial mirrors or re-hosted versions without verifying they are authorized by the original dataset authors.

> **Official links are provided for convenience and reproducibility planning. Dataset files are not stored in this repository.**

---

## Recommended Local Storage

After downloading from the official source, store MM-Fi data locally at:

```
data/external/mm-fi/
```

Example structure (verify against the actual directory layout from the official repo):

```
data/
  external/
    mm-fi/
      raw/
      processed/
      annotations/
      README_local.md   <-- your local notes on the download
```

The `data/external/` path is excluded from Git via `.gitignore`. This data will **not** be committed or pushed to the repository.

---

## Do Not Commit Dataset Files

**Critical rule:** Never add MM-Fi data files to Git.

- `data/external/` is listed in `.gitignore`
- Common file extensions are also gitignored: `.npy`, `.npz`, `.mat`, `.h5`, `.zip`, `.tar`
- Do not add exceptions or force-add dataset files with `git add -f`
- If you accidentally stage dataset files, run: `git reset HEAD data/external/`

---

## Private Backup Policy

After downloading MM-Fi from the official source, a **private backup** may be kept in Google Drive or another personal cloud storage service for convenience:

- A private backup is acceptable for **personal use only**
- Do **not** publish or share a private backup link unless the MM-Fi dataset license explicitly permits redistribution
- Do **not** add a public Google Drive or cloud link to this repository unless redistribution is confirmed as permitted
- Always refer others to the official sources listed above

---

## Verification Checklist

Before using MM-Fi in any experiment, complete all items:

- [ ] Review the official project page: https://ntu-aiot-lab.github.io/mm-fi
- [ ] Review the official GitHub repository: https://github.com/ybhbingo/MMFi_dataset
- [ ] Read and record the official license (update `LICENSE_SUMMARY.md`)
- [ ] Confirm whether redistribution is permitted
- [ ] Confirm whether registration or institutional access is required
- [ ] Download from the official source only
- [ ] Verify file integrity (checksums if provided)
- [ ] Verify folder structure matches expected layout from official repo
- [ ] Verify label schema and annotation format
- [ ] Confirm and record the correct citation (update `DATASET_CARD.md`)
- [ ] Record download date and version in `data/external/mm-fi/README_local.md`

---

## Future Loader Plan

Once MM-Fi is downloaded and verified locally, a dataset loader may be added at:

```
scripts/load_mmfi.py
```

or integrated into the main pipeline at:

```
src/data/
```

The loader should:
- Read from `data/external/mm-fi/` (local only, not committed)
- Parse `.npy` or other verified format files per the official tooling repo
- Return standardized arrays compatible with the existing synthetic data pipeline
- Include assertions for expected file structure and label schema

**Current status: No loader exists yet. This is planned future work.**

---

*Last updated: May 2026*
