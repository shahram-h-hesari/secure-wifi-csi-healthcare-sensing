# RuView Adversarial Evaluation

> **Status:** Planning and workspace setup only. No experiments have been executed.

---

## Overview

This folder is a dedicated experiment workspace for the future offline evaluation of RuView as a third-party WiFi sensing project.

The goals of this workspace are:

1. Reproduce RuView's baseline simulation in a controlled local or Docker environment
2. Identify RuView's input data, output data, and model pipeline structure
3. Design offline synthetic perturbation experiments against RuView's WiFi sensing pipeline
4. Evaluate the effect of perturbations on sensing outputs (missed detections, false alarms, robustness degradation)
5. Document all findings transparently as part of PhD research on adversarial robustness for secure WiFi CSI sensing at Portland State University

---

## Important Constraints

- **Synthetic and offline only:** This folder is for future offline evaluation using data files and model files only
- **No real physical-layer attacks:** No real network traffic is modified. No real devices are targeted
- **No clinical validation:** No clinical, hardware, or real-world validation is claimed
- **RuView is third-party:** All RuView code, claims, and results are attributed to the original authors at https://github.com/ruvnet/RuView
- **Separate from original pipeline:** This workspace is completely separate from this repository's original `src/`, `notebooks/`, and `app.py` code

---

## Folder Contents

| File | Purpose |
|---|---|
| `README.md` | This overview document |
| `run_ruview_baseline.md` | Planned steps to run RuView baseline simulation |
| `perturbation_plan.md` | Planned offline perturbation experiments |
| `results_template.md` | Results recording template (no results yet) |

---

## Connection to PhD Research

This evaluation workspace connects directly to PhD research at Portland State University on:

- Adversarial robustness of WiFi-based sensing systems
- Security threats to WiFi CSI health monitoring pipelines
- Defense methods against synthetic signal perturbations
- Cross-layer security analysis for wireless medical networks

See `third_party/wifi_sensing/ruview/EXPERIMENT_PLAN.md` for the full research experiment plan.

---

*Workspace created: May 2026. No experiments have been executed.*
