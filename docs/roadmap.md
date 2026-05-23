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

*See also: [research_context.md](research_context.md), [validation_status.md](validation_status.md), [security_motivation.md](security_motivation.md)*
