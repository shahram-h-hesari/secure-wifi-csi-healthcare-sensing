# MM-Fi Download Instructions

> **Warning:** Do not commit downloaded dataset files to this repository. All MM-Fi data must remain local only.

---

## Official Download Source

- **Official URL:** Pending verification
  - Search for "MM-Fi dataset WiFi CSI" on Google Scholar, GitHub, or the IEEE DataPort / Zenodo platforms
  - Once identified, update this file with the verified URL
- **Associated paper:** Pending verification (see `DATASET_CARD.md`)
- **Mirror or alternative:** Pending verification

> **Note:** Do not use unofficial mirrors or re-hosted versions of MM-Fi without verifying they are authorized by the original dataset authors.

---

## Recommended Local Storage

After downloading, store MM-Fi data locally at:

```
data/external/mm-fi/
```

Example structure (pending verification of actual directory layout):

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
- Common MM-Fi file extensions are also gitignored: `.npy`, `.npz`, `.mat`, `.h5`, `.zip`, `.tar`
- Do not add exceptions or force-add dataset files with `git add -f`
- If you accidentally stage dataset files, run: `git reset HEAD data/external/`

---

## Verification Checklist

Before using MM-Fi in any experiment, complete all items:

- [ ] Identify and record the official MM-Fi download URL
- [ ] Read and record the official license (update `LICENSE_SUMMARY.md`)
- [ ] Confirm whether redistribution is permitted
- [ ] Confirm whether institutional or personal registration is required
- [ ] Download from the official source only
- [ ] Verify file integrity (checksums if provided)
- [ ] Verify folder structure matches expected layout
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
- Parse `.npy` or other verified format files
- Return standardized arrays compatible with the existing synthetic data pipeline
- Include assertions for expected file structure and label schema

**Current status: No loader exists yet. This is planned future work.**

---

*Last updated: May 2026*
