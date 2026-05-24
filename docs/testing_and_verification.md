# Testing and Verification

> **Important note:** All tests in this repository use synthetic CSI-like data only. Successful test execution does not imply clinical validation, real CSI hardware validation, hardware deployment readiness, or medical-grade performance. This is a research prototype.

## Purpose

This document explains how to clone, install, and verify that the WiFi CSI Fall Detection Research Prototype runs correctly on a new machine. It is intended for collaborators, committee members, and GitHub visitors who want to reproduce or explore the prototype locally.

## Clone the Repository

```bash
git clone https://github.com/shahram-h-hesari/wifi-csi-fall-detection.git
cd wifi-csi-fall-detection
```

## Install Dependencies

Create a virtual environment (recommended) and install all dependencies:

```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

The `requirements.txt` includes:
- `numpy`, `pandas`, `scipy` - signal processing and data handling
- `matplotlib` - visualization
- `scikit-learn` - machine learning
- `streamlit` - interactive dashboard
- `jupyter` - notebook interface
- `pytest` - test runner

## Run the Notebook

Launch the full prototype pipeline notebook:

```bash
jupyter notebook notebooks/01_csi_signal_exploration.ipynb
```

Then select **Kernel > Restart & Run All** to execute all cells from top to bottom.

**Expected behavior:** All cells execute without errors. Figures are generated inline. Results are printed in output cells. Any figures or results saved to disk will appear in `figures/` and `results/`.

> **Note:** The notebook uses synthetic CSI-like data generated at runtime. No external data files are required.

## Run the Streamlit Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`.

**Expected behavior:** The dashboard loads without errors. Sidebar controls respond interactively. All plots, metrics, and tables render correctly.

See [`docs/demo_dashboard.md`](./demo_dashboard.md) for a full description of dashboard sections.

## Run the Smoke Test

The smoke test verifies that the core synthetic pipeline (data generation, preprocessing, feature extraction, classification) runs end-to-end without errors.

```bash
python scripts/smoke_test.py
```

**Expected output:**
```
[SMOKE TEST] WiFi CSI Fall Detection Research Prototype
[SMOKE TEST] All data is synthetic. This test does not validate real CSI or clinical performance.
[SMOKE TEST] Generating synthetic CSI-like data...
[SMOKE TEST] Preprocessing...
[SMOKE TEST] Extracting features...
[SMOKE TEST] Training baseline classifier...
[SMOKE TEST] Results (synthetic prototype only):
  Accuracy : 0.xxxx
  Precision: 0.xxxx
  Recall   : 0.xxxx
  F1-score : 0.xxxx
[SMOKE TEST] PASSED - Synthetic pipeline ran without errors.
```

## Run Basic Tests

Run the basic pytest suite to verify imports, data shapes, and minimal pipeline behavior:

```bash
pytest
```

Or run with verbose output:

```bash
pytest -v
```

**Expected output:** All tests pass with no failures or errors.

The test suite is located in `tests/test_basic_pipeline.py`. Tests cover:
- Required package imports
- Synthetic data array dimensions
- Feature extraction output structure
- Classifier fit-and-predict on synthetic data

## Expected Outputs

| Action | Expected Output |
|---|---|
| Notebook runs | All cells execute; inline plots appear |
| Dashboard loads | All sections render; sidebar controls work |
| Smoke test passes | Pipeline runs; metrics print to terminal |
| pytest passes | All tests pass with no failures |
| figures/ directory | May contain saved Matplotlib figures |
| results/ directory | Contains Markdown result summaries from notebook |

All outputs are synthetic prototype results only.

## Troubleshooting

### ModuleNotFoundError

Ensure all dependencies are installed in the active virtual environment:
```bash
pip install -r requirements.txt
```

### Streamlit command not found

Ensure `streamlit` is installed:
```bash
pip install streamlit
```

### Notebook kernel error

Ensure you are using the correct Python kernel. In Jupyter, select **Kernel > Change Kernel** and choose the environment where `requirements.txt` was installed.

### pytest not found

Ensure `pytest` is installed:
```bash
pip install pytest
```

### scipy import error

Ensure scipy is installed:
```bash
pip install scipy
```

### Windows path issues

On Windows, activate the virtual environment with:
```
venv\Scripts\activate
```

## Limitations

- All tests and scripts use synthetic CSI-like data only.
- Passing these tests does not validate real WiFi CSI performance.
- Passing these tests does not validate clinical fall-detection performance.
- Passing these tests does not validate adversarial defense effectiveness.
- No hardware device is required or tested.
- No patient data or clinical data is accessed by any script or test.

---

*This document is part of the WiFi CSI Fall Detection Research Prototype. All content is for academic research and prototype demonstration purposes only. Phase 10.*
