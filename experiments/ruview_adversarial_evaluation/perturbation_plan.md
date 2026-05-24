# Perturbation Plan

> **Status:** Planned only. These are synthetic/offline research tests. No experiments have been executed. No real physical-layer attacks are implemented.

---

## Purpose

This document defines planned offline perturbation experiments for studying the robustness of RuView's WiFi sensing pipeline. All tests apply synthetic perturbations to data files or model inputs offline. No real network traffic is modified.

---

## Important Constraints

- All perturbation experiments are **offline and synthetic research tests only**
- No real WiFi hardware, real networks, or real devices are targeted
- No clinical validation of results is claimed
- Findings are for academic research purposes only, connected to PhD research at Portland State University
- These tests must only be run after baseline simulation is successfully reproduced (see `run_ruview_baseline.md`)

---

## Perturbation Types Planned

### 1. Random Noise Perturbation

**Description:** Add zero-mean Gaussian noise to CSI amplitude values at the input data stage.

**Target:** Raw CSI amplitude data files

**Parameters to vary:**
- Noise standard deviation: [0.01, 0.05, 0.1, 0.2, 0.5]
- Noise distribution: Gaussian, uniform

**Expected measurements:**
- Classification output change (fall detected / not detected)
- Confidence score change
- Threshold for output flip

**Status:** Planned — pending baseline simulation

---

### 2. Burst Perturbation

**Description:** Insert a short burst of anomalous values (e.g., spike or dropout) into the CSI time series.

**Target:** Raw CSI amplitude time series data

**Parameters to vary:**
- Burst duration: [1, 5, 10, 20 samples]
- Burst magnitude: [2x, 5x, 10x nominal value, or zero dropout]
- Burst position: beginning, middle, end of input window

**Expected measurements:**
- Whether burst causes missed detection
- Whether burst causes false alarm
- Output sensitivity to burst position

**Status:** Planned — pending baseline simulation

---

### 3. Subcarrier Perturbation

**Description:** Modify amplitudes of a specific subset of WiFi subcarriers in the CSI input.

**Target:** Per-subcarrier CSI amplitude values

**Parameters to vary:**
- Number of subcarriers perturbed: [1, 5, 10, all]
- Perturbation type: zero out, amplify, or random replacement
- Subcarrier selection: adjacent subcarriers vs. randomly selected

**Expected measurements:**
- Output change vs. number of perturbed subcarriers
- Identification of most sensitive subcarriers

**Status:** Planned — pending baseline simulation

---

### 4. Feature-Level Perturbation

**Description:** Modify extracted features at the model input stage (post-preprocessing, pre-model inference).

**Target:** Extracted feature vector before model input

**Parameters to vary:**
- Feature perturbation magnitude
- Which features are perturbed (single vs. all)

**Expected measurements:**
- Output change vs. feature perturbation magnitude
- Identification of most influential features for adversarial impact

**Status:** Planned — pending feature extraction review

---

### 5. Phase Distortion

**Description:** Add synthetic phase noise to CSI phase measurements.

**Target:** CSI phase data (if accessible)

**Parameters to vary:**
- Phase noise magnitude: [5°, 15°, 30°, 90°]
- Phase noise distribution: Gaussian, wrapped Gaussian

**Expected measurements:**
- Whether phase distortion affects amplitude-based features
- Output sensitivity to phase distortion

**Status:** Planned — pending review of whether RuView uses phase data

---

## Output Impact Metrics

For each perturbation experiment, record:

| Metric | Description |
|---|---|
| Output class change | Did the classification label change? |
| Confidence delta | How much did the confidence score change? |
| Missed detection rate | What fraction of fall events were missed? |
| False alarm rate | What fraction of non-fall events were falsely flagged? |
| Perturbation threshold | Minimum perturbation magnitude causing output change |

---

## Connections to Safety Research

In a real deployment (not implemented here), missed fall detections could have clinical safety implications for vulnerable individuals. This research frames perturbation testing as a robustness stress test to:

1. Quantify the sensitivity of WiFi sensing models to input perturbations
2. Identify defense opportunities (input preprocessing, anomaly detection, smoothing)
3. Connect findings to adversarial robustness literature for secure health monitoring systems
4. Contribute to PhD research on cybersecurity for wireless medical networks

> All findings will be reported as synthetic/offline research results only. No clinical guidance is derived.

---

*Plan created: May 2026. No perturbation experiments have been executed.*


---

## Dependency on Baseline Verification

> **Perturbations should only be applied after the input data format and baseline outputs are understood.**

This section defines the dependency chain that must be satisfied before any perturbation experiment is executed:

### Before Starting Perturbation Experiments

- [ ] Baseline simulation has been reproduced successfully (see `run_ruview_baseline.md`)
- [ ] Input data format is identified and documented
- [ ] Model weights source is identified and documented
- [ ] Baseline output format is documented (labels / scores / visualizations / placeholders)
- [ ] Dataset provenance table in `run_ruview_baseline.md` is completed

### Data Type Labeling Rules

| Data Type Available | Required Result Labeling |
|---|---|
| Simulated data only | **Synthetic/simulation-only results** — not real-data evaluation |
| Recorded CSI (local) | **Locally-recorded CSI results** — not a peer-reviewed public benchmark |
| Public dataset (verified) | **Results on [dataset name]** — must cite dataset paper and verify split |
| Unknown / unverified | **Preliminary results — data source unverified** |

### Ethical Considerations for Real CSI Data

If real CSI data is used in future experiments (beyond simulation):

- Authorization must be obtained for any data collected from real environments
- Informed consent requirements must be assessed for any human-subject data
- Institutional review board (IRB) or ethics board guidance should be followed
- No data should be collected from environments or individuals without authorization
- All real-data experiments must be documented with collection protocol, subject count, and consent status

> This section applies only if and when real CSI data is used. All current planned experiments use simulated data only.

---

*Baseline verification dependency section added: May 2026. No perturbation experiments have been executed.*
