# RuView Experiment Plan

> **Status:** Planning stage only. No experiments have been executed. All planned experiments are offline, synthetic, and reproducibility-focused. No real physical-layer attacks are implemented or planned.

---

## Purpose

This document defines a future research plan for:
1. Reproducing RuView's baseline simulation in a controlled local or Docker environment
2. Identifying RuView's input data, output data, and model pipeline structure
3. Designing offline synthetic perturbation experiments against RuView's WiFi sensing pipeline
4. Evaluating the effect of perturbations on sensing outputs (missed detections, false alarms, robustness degradation)
5. Contributing findings to my PhD research on adversarial robustness for secure WiFi CSI sensing at Portland State University

> **Scope limitation:** This experiment plan covers offline and synthetic research only. It does not describe or enable attacks on unauthorized real devices, real networks, or real users.

---

## Research Questions

1. Can RuView's simulation be reproduced locally or through Docker without real WiFi hardware?
2. What data or model files does RuView use for simulation?
3. Which outputs are generated from real data, pretrained models, or simulated data?
4. Can CSI-like inputs or intermediate features be perturbed offline?
5. How do perturbations affect model outputs or sensing decisions?
6. Can output changes be mapped to missed detections, false alarms, or robustness degradation?
7. What defenses (preprocessing, smoothing, anomaly detection) could mitigate perturbation effects?

---

## Step 1: Reproduce Baseline Simulation

**Goal:** Confirm that RuView's simulation (or a relevant component) runs in a controlled environment without real hardware.

**Tasks:**
- [ ] Add RuView as a Git submodule (see `SUBMODULE_INSTRUCTIONS.md`)
- [ ] Review `docker/` configuration for simulation options
- [ ] Identify Docker Compose files and entry points
- [ ] Review `docs/` for installation and quickstart instructions
- [ ] Attempt to run simulation in Docker environment
- [ ] Document which components run successfully and which require real hardware
- [ ] Record software environment: OS, Python version, Docker version, dependencies

**Expected Outcome:** A working baseline simulation with known inputs and outputs, or a clear documentation of why hardware is required.

**Fallback:** If hardware is required for all components, document simulation-mode data files and use those as offline perturbation targets.

---

## Step 2: Identify Inputs, Outputs, and Model Pipeline

**Goal:** Map the RuView sensing pipeline from data input to final output.

**Tasks:**
- [ ] Identify raw input format (CSI amplitude, phase, subcarrier data, etc.)
- [ ] Identify preprocessing steps (normalization, filtering, segmentation)
- [ ] Identify model architecture (neural network type, layer structure)
- [ ] Identify model output format (classification label, probability, event type)
- [ ] Identify where in the pipeline perturbation could be applied offline
- [ ] Document the data flow diagram

**Notes:** *Pending review of RuView source code. Do not fabricate pipeline details.*

---

## Step 3: Dataset and Model Review

**Goal:** Understand what data and model files are included or downloaded by RuView.

**Tasks:**
- [ ] Review `data/` folder: file types, sizes, formats
- [ ] Check for sample or synthetic CSI-like data files
- [ ] Identify model checkpoint files (`.pt`, `.pkl`, `.h5`, `.onnx`)
- [ ] Check for Hugging Face model downloads or external URLs in code
- [ ] Document which data/model files are available offline vs. require download
- [ ] Note license and usage terms for any included datasets

**Notes:** *Dataset availability affects reproducibility of offline perturbation experiments.*

---

## Step 4: Synthetic Perturbation Experiments

**Goal:** Apply controlled synthetic perturbations to RuView's input data or intermediate features and measure the effect on sensing outputs.

> **Important:** All perturbations are applied offline to data files or model inputs. No real network traffic is modified. No real devices are attacked.

**Planned Perturbation Types:**

| Perturbation Type | Description | Target | Status |
|---|---|---|---|
| Random noise | Add Gaussian noise to CSI amplitude values | Input data | Planned |
| Burst perturbation | Insert a short burst of anomalous values | Input data | Planned |
| Subcarrier perturbation | Modify a subset of subcarrier amplitudes | Input features | Planned |
| Feature-level perturbation | Modify extracted features before model input | Feature vector | Planned |
| Phase distortion | Add synthetic phase noise | Input data | Planned |

**Measurement Targets:**
- Change in classification output (fall detected / not detected)
- Change in confidence/probability score
- Missed detection rate under perturbation
- False alarm rate under perturbation
- Perturbation magnitude vs. output change curve

---

## Step 5: Safety-Oriented Evaluation

**Goal:** Connect perturbation findings to safety-critical implications for WiFi-based health monitoring systems.

**Research Questions:**
- At what perturbation magnitude does the fall detection output change?
- Are certain perturbation types more effective than others?
- Do any preprocessing defenses reduce perturbation impact?
- What are the clinical safety implications of missed fall detections in a real deployment (not claimed here, but discussed as a research risk model)?

**Safety Framing:**
- This evaluation is framed as a robustness stress test, not an attack guide
- Findings will be documented as synthetic research results only
- Results will not be used to guide real attacks on medical devices
- Findings connect to PhD research on adversarial robustness for secure WiFi CSI sensing

---

## Step 6: Documentation of Results

**Goal:** Document all experiment results transparently.

**Tasks:**
- [ ] Record baseline simulation outputs
- [ ] Record perturbed outputs for each perturbation type
- [ ] Compute output change metrics
- [ ] Note any reproducibility issues
- [ ] Note all limitations clearly
- [ ] Do not fabricate or overstate results

See `experiments/ruview_adversarial_evaluation/results_template.md` for the results recording template.

---

## Limitations

- All experiments are based on offline synthetic perturbation of data files only
- No real WiFi hardware is used in these experiments
- No real CSI measurements are collected
- RuView's claims are not independently validated by these experiments
- Results apply only to the specific software version and data files studied
- Findings cannot be generalized to real-world deployment without further validation
- No clinical or safety validation is claimed

---

## Ethics and Safety

- All experiments are conducted on offline data files in a controlled research environment
- No real networks, devices, or users are targeted
- No real physical-layer attack is implemented
- Research is conducted in accordance with Portland State University research ethics guidelines
- Findings are documented for academic purposes only
- No clinical, medical, or safety-critical guidance is derived from these synthetic experiments

---

*Plan created: May 2026. No experiments have been executed. Plan is subject to revision after baseline simulation review.*
