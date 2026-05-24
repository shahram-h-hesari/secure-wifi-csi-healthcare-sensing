# Research Roadmap

This document outlines the planned development trajectory for this repository, organized into phases aligned with the broader PhD research program.

> **Note:** Timelines are approximate and subject to change based on research priorities, hardware availability, and academic requirements.

---

## Phase 1 — Clean Repository Structure and Synthetic Baseline (Current)

**Status:** In progress

**Goals:**
- [x] Establish clean, professional repository structure
- [x] Implement synthetic CSI signal generator
- [x] Implement basic preprocessing pipeline (filtering, normalization)
- [x] Implement time-series feature extraction
- [x] Implement baseline ML model (Random Forest)
- [x] Add Jupyter notebook for CSI signal exploration
- [x] Create research documentation (context, validation status, threat model)
- [x] Organize third-party references with clear separation
- [ ] Refine src/ into submodule structure (data_generation, preprocessing, features, models)
- [ ] Add unit tests for core pipeline components
- [ ] Improve notebook with additional visualizations

---

## Phase 2 — Real Hardware CSI Integration

**Status:** Not started

**Goals:**
- [ ] Integrate real CSI capture pipeline (ESP32 / Nexmon / Intel 5300)
- [ ] Collect CSI data in controlled lab environment
- [ ] Validate preprocessing pipeline on real hardware data
- [ ] Evaluate baseline model performance on real CSI data
- [ ] Document hardware setup and data collection protocol

---

## Phase 3 — Advanced ML and Fall Detection Pipeline

**Status:** Not started

**Goals:**
- [ ] Implement CNN-LSTM architecture for temporal CSI classification
- [ ] Evaluate stacking ensemble approaches (RF + ANN)
- [ ] Integrate Dynamic Bayesian Network (DBN) components
- [ ] Cross-environment generalization testing
- [ ] Benchmark against published baselines

---

## Phase 4 — Security and Adversarial Robustness Extension

**Status:** Not started

**Goals:**
- [ ] Implement adversarial attack generation for CSI signals
- [ ] Evaluate model robustness under adversarial conditions
- [ ] Develop and test attack detection mechanisms
- [ ] Integrate defense methods into the sensing pipeline
- [ ] Document threat model and experimental findings

---

## Phase 5 — Privacy-Preserving and Federated Learning Extension

**Status:** Not started

**Goals:**
- [ ] Implement federated learning framework for distributed CSI sensing
- [ ] Integrate differential privacy mechanisms
- [ ] Evaluate privacy-utility tradeoffs
- [ ] Explore hierarchical federated learning for multi-site deployment

---

## Long-Term Vision

The ultimate goal is to contribute to the design of **secure, privacy-preserving, and clinically responsible WiFi CSI-based health monitoring systems** that can be deployed in real healthcare environments, with formal documentation of their threat model, limitations, and validation status.

---

*Last updated: May 2026*


---

## Phase 6 - Adversarial Robustness Stress Testing

**Status:** Completed

**Goals:**
- [x] Implement synthetic random noise perturbation
- [x] Implement synthetic burst perturbation
- [x] Implement synthetic subcarrier-level perturbation
- [x] Compare clean vs perturbed ML metrics
- [x] Compare clean vs perturbed safety metrics
- [x] Save results to results/adversarial_robustness_summary.md
- [x] Add adversarial robustness documentation
- [ ] Real physical-layer attack implementation (future work)
- [ ] Hardware-validated robustness experiments (future work)

---

## Phase 7 - Defense Methods and Robustness Hardening

**Status:** Completed

**Goals:**
- [x] Implement moving average smoothing defense
- [x] Implement median filter defense
- [x] Implement outlier clipping
- [x] Implement robust normalization (median/IQR)
- [x] Implement perturbation-aware augmentation prototype
- [x] Compare clean vs perturbed vs defended ML metrics
- [x] Compare clean vs perturbed vs defended safety metrics
- [x] Save results to results/defense_methods_summary.md
- [x] Add defense methods documentation
- [ ] Full adversarial training (future work)
- [ ] Certified robustness evaluation (future work)
- [ ] Real physical-layer defense validation (future work)

---

## Phase 8 - Streamlit Demo Dashboard

**Status:** Completed

**Goals:**
- [x] Create interactive Streamlit dashboard (app.py)
- [x] Synthetic CSI amplitude and phase visualization
- [x] Normal vs fall-like event comparison
- [x] Baseline classifier prototype demo
- [x] Clinical-safety-aware metrics display
- [x] Adversarial robustness comparison
- [x] Defense comparison
- [x] Sidebar controls for all key parameters
- [x] Synthetic-data-only disclaimer throughout
- [ ] Real CSI data file upload (future work)
- [ ] Deploy to Streamlit Cloud (future work)

---

## Phase 9 - GitHub Polish and LinkedIn-Ready Presentation

**Status:** Completed

**Goals:**
- [x] Polish README with badges, highlights table, quick start, and roadmap
- [x] Add docs/project_status.md
- [x] Add docs/linkedin_summary.md
- [x] Add docs/demo_dashboard.md
- [x] Add figures/dashboard_screenshot_placeholder.md
- [x] Update roadmap.md (this file)
- [ ] Add actual dashboard screenshot after local testing (next step)
- [ ] Add GitHub repository to LinkedIn Featured section (next step)
- [ ] Publish LinkedIn post introducing the project (next step)

---

## Phase 10 – Testing and Verification (Completed)

**Status:** Completed

**Goals:**
- [x] Create docs/testing_and_verification.md with full testing documentation
- [x] Implement scripts/smoke_test.py for end-to-end synthetic pipeline verification
- [x] Create tests/test_basic_pipeline.py with basic pytest unit tests
- [x] Add pytest to requirements.txt
- [x] Add Testing & Verification section to README.md
- [x] Update roadmap.md to reflect Phase 10 completion

**Notes:**
- All tests operate on synthetic data only
- Tests verify prototype pipeline logic, not real-world CSI performance
- Smoke test covers: data generation, preprocessing, feature extraction, model training, prediction, and adversarial robustness
- Unit tests cover: output shapes, prediction range, and above-chance accuracy on synthetic data

---

## Phase 10+ - Real CSI, Hardware, and Clinical Evaluation (Future Work)

**Status:** Not started

**Goals:**
- [ ] Collect real WiFi CSI measurements (Intel 5300, Nexmon, or ESP32)
- [ ] Evaluate pipeline on real CSI fall datasets
- [ ] Hardware deployment in controlled research environment
- [ ] Deep learning models (CNN, LSTM, Transformer)
- [ ] Federated learning with Byzantine robustness
- [ ] IRB approval and clinical feasibility study
- [ ] Real physical-layer attack experiments
- [ ] Certified robustness evaluation
- [ ] WiFi 7 multi-link operation security evaluation

---

*Last updated: Phase 10 - May 2026*
*See also: [research_context.md](research_context.md), [validation_status.md](validation_status.md), [security_motivation.md](security_motivation.md)*
