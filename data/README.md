# Data Directory

## Purpose

This directory is for small metadata, configuration placeholders, and local dataset organization documentation only. Large dataset files must **not** be committed to this repository.

For the dataset catalog and download instructions, see [`datasets/`](../datasets/README.md).

---

## Current Data Status

This repository currently uses **synthetic CSI-like data only**, generated programmatically in the notebook and source files, including:

- `notebooks/01_csi_signal_exploration.ipynb`
- `src/simulate_csi.py`

No external data files are required to run the current version.

---

## Local External Data

If you download public WiFi CSI datasets locally for experimentation (e.g., MM-Fi, Wi-Pose), store them at:

```
data/external/mm-fi/
data/external/wi-pose/
```

The `data/external/` path is excluded from Git via `.gitignore`. Local data will **not** be committed or pushed to the repository.

See `datasets/mm-fi/DOWNLOAD_INSTRUCTIONS.md` and `datasets/wi-pose/DOWNLOAD_INSTRUCTIONS.md` for dataset-specific storage instructions.

---

## Git Policy

- `data/external/` is listed in `.gitignore` and will not be tracked by Git.
- Common large file extensions are also gitignored: `.mat`, `.npy`, `.npz`, `.h5`, `.hdf5`, `.zip`, `.tar`, `.tar.gz`, `.pkl`.
- Do **not** force-add large dataset files with `git add -f`.
- Do **not** commit binary data archives of any kind.
- Small metadata files (e.g., label maps, README_local.md notes) are acceptable if they do not contain sensitive or large data.

---

## Recommended Structure

```
data/
  README.md              <-- this file (committed)
  external/              <-- NOT committed; gitignored
    mm-fi/
      raw/
      processed/
      annotations/
      README_local.md    <-- local download notes (not committed)
    wi-pose/
      raw/
      processed/
      annotations/
      README_local.md    <-- local download notes (not committed)
```

---

## Data Privacy and Safety

This repository does **not** include:

- Real patient data
- Real clinical data
- Private health information
- Personally identifiable information
- Validated WiFi CSI measurements
- Data collected from real eldercare or healthcare environments

---

## Disclaimer

This repository currently uses synthetic CSI-like time-series data for demonstration purposes. It does not use real patient data, real clinical data, or validated WiFi CSI measurements. Results are intended only to demonstrate the research workflow and should not be interpreted as clinical or real-world fall detection performance.

---

## Future Data Policy

Future versions may add real public WiFi CSI datasets only if they are:

1. Publicly available
2. Properly licensed for research use
3. Ethically appropriate
4. Clearly cited and attributed
5. Documented with source, license, and usage limitations

Any future real dataset will be kept separate from synthetic examples and will include clear documentation about its origin, license, and intended research use. See `datasets/` for the current catalog and planning.

---

## Author

**Shahram H. Hesari**  
PhD Candidate, Electrical and Computer Engineering  
Portland State University

---

*Last updated: May 2026*
