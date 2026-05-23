# Validation Status

> **Important:** This document explicitly documents the current validation status of this research repository. It is intended to prevent overclaiming and to provide transparency for academic review.

## Current Status: Research Prototype — Synthetic Data Only

As of May 2026, this repository operates exclusively on **synthetically generated CSI-like data**. It is a research prototype workflow and does **not** constitute a clinically validated system.

## What This Repository Currently Does

| Component | Status | Notes |
|---|---|---|
| Synthetic CSI signal generation | Implemented | Simulated amplitude/phase patterns, not real hardware captures |
| Signal preprocessing | Implemented | Filtering and normalization on synthetic data |
| Feature extraction | Implemented | Time-series features on synthetic signals |
| Baseline ML classification | Implemented | Random Forest / scikit-learn baseline on synthetic data |
| Visualization | Implemented | Notebook-based CSI signal exploration |
| Real hardware CSI data | Not included | No ESP32, Nexmon, or commercial CSI captures |
| Clinical validation | Not performed | No hospital, clinic, or real-environment testing |
| IRB / ethics approval | Not applicable | No human subjects involved at this stage |
| Peer-reviewed results | Not yet | Repository is pre-publication research infrastructure |

## What This Repository Does NOT Claim

- This system **cannot** be used for clinical fall detection without independent validation on real hardware and human subjects.
- Accuracy figures or model performance metrics produced here reflect **synthetic data only** and should not be generalized.
- This repository does **not** demonstrate that WiFi CSI systems are safe or effective for medical use.
- Results from third-party projects are **not** treated as validated unless independently reproduced.

## Path to Validation

Future validation phases (not yet started) would require:

1. Real CSI hardware capture (e.g., ESP32 with CSI firmware, Nexmon, or Intel 5300)
2. Data collection in realistic home or care facility environments
3. Human subjects protocols and appropriate ethics review
4. Cross-environment generalization testing
5. Peer review of methodology and results

## Academic Transparency

This validation status document is maintained to support honest academic representation of this repository's scope and maturity. It will be updated as the project progresses through validation phases.

---

*Last updated: May 2026*

*See also: [research_context.md](research_context.md), [roadmap.md](roadmap.md)*
