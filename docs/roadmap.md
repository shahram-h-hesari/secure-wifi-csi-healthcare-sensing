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

## Phase 11 – Third-Party WiFi Sensing Integration: RuView (Completed)

**Status:** Completed

**Goals:**
- [x] Add RuView as a third-party WiFi sensing experimental target
- [x] Create `third_party/wifi_sensing/ruview/` documentation folder
- [x] Add README.md, LICENSE_SUMMARY.md, REVIEW_NOTES.md, EXPERIMENT_PLAN.md, SUBMODULE_INSTRUCTIONS.md
- [x] Create `experiments/ruview_adversarial_evaluation/` workspace
- [x] Add run_ruview_baseline.md, perturbation_plan.md, results_template.md
- [x] Update THIRD_PARTY_NOTICES.md with complete RuView entry
- [x] Update docs/related_projects.md and README.md

**Notes:**
- RuView is cataloged as a third-party reference only; no code copied into src/
- No clinical or independent validation claimed
- Dataset and validation protocol for RuView remain pending independent verification
- Adversarial experiments require completed baseline documentation first

---

## Phase 12 – WiFi CSI Dataset Catalog (Completed)

**Status:** Completed

**Goals:**
- [x] Create `datasets/` catalog folder structure
- [x] Add `datasets/README.md` — catalog purpose, policy, and current status
- [x] Add `datasets/dataset_catalog.md` — table-based dataset index
- [x] Add MM-Fi catalog entry: `datasets/mm-fi/` with README, DATASET_CARD, LICENSE_SUMMARY, DOWNLOAD_INSTRUCTIONS
- [x] Add Wi-Pose catalog entry: `datasets/wi-pose/` with README, DATASET_CARD, LICENSE_SUMMARY, DOWNLOAD_INSTRUCTIONS
- [x] Add `datasets/future_datasets/README.md` with candidate list (Widar3.0, FallDeFi, SignFi, UT-HAR)
- [x] Update `data/README.md` with external data storage policy
- [x] Update `.gitignore` to exclude `data/external/` and common large dataset file extensions
- [x] Update `README.md` with Dataset Catalog section
- [x] Update `docs/roadmap.md` (this file)

**Notes:**
- Dataset files are NOT stored in this repository
- MM-Fi and Wi-Pose are cataloged as related datasets, not current validation datasets
- Current experiments still use synthetic CSI-like data only
- Real-data integration remains future work
- Catalog entries include license, citation, and download guidance placeholders requiring manual verification

**Future tasks (Phase 13+):**
- Verify official sources, licenses, and citations for MM-Fi and Wi-Pose
- Write local dataset loaders (scripts/load_mmfi.py, scripts/load_wipose.py)
- Add FallDeFi, Widar3.0, and other candidate dataset entries
- Connect real CSI datasets to synthetic pipeline for benchmarking

*Last updated: Phase 12 - May 2026*
*See also: [research_context.md](research_context.md), [validation_status.md](validation_status.md), [security_motivation.md](security_motivation.md)*


---

## Future Tasks — Third-Party Repository Integration (Added 2026-05-24)

The following tasks were added after four new external repositories were cataloged in `third_party/`. These tasks are for future investigation and integration planning.

### Third-Party Repository Inspection Tasks

- [ ] **Inspect goop-veil for license compliance and potential integration**
  - Review the Apache-2.0 license terms for any code or ideas you wish to adapt.
  - Compare `goop-veil`'s router-side privacy defense approach with this project's planned software-only defense framework.
  - Determine if any detection or degradation methods from `goop-veil` can inform the thesis adversarial defense pipeline.
  - Verify whether any live CSI data examples or test traces are publicly available.

- [ ] **Decide whether mowa-wifi-sensing can be used as a fall/HAR baseline**
  - Inspect the upstream repository for dataset availability (real-time Nexmon CSI; domain-specific HAR folders such as `csi_dataset/domain_A`, `domain_B`).
  - Verify whether fall-related activity classes are included in the HAR data.
  - Verify the BSD-3-Clause license terms for data and code use.
  - If dataset is confirmed and license allows, plan a future experiment to compare synthetic pipeline performance against a real-data HAR baseline.

- [ ] **Decide whether baby-monitor-wifi-csi can inform apnea/vital-sign experiments**
  - Inspect the upstream repository for recorded CSI breathing traces or data download links.
  - Verify the MIT license terms for data and code use.
  - If relevant data is confirmed, plan a future experiment extending the synthetic vital-sign pipeline toward real WiFi CSI breathing detection.
  - Assess whether ESP32 CSI collection methodology is compatible with this project's hardware plans.

- [ ] **Inspect WiFi-CSI-Human-Pose-Detection for dataset and integration potential**
  - Inspect the upstream repository for confirmed CSI pose/through-wall dataset links.
  - Verify the GPL-3.0 license copyleft implications before any code adaptation.
  - Determine whether pose-based CSI features can enrich fall-detection baseline experiments.
  - If adversarial domain generalization content is found in future exploration, consider reclassifying to `third_party/wifi_sensing_security/`.

### Dataset Candidate Verification Tasks

- [ ] **Verify dataset candidates in `datasets/future_datasets/README.md`**
  - Manually check each of the four new candidate entries:
    1. `goop-veil live/router CSI data` — confirm or rule out public dataset.
    2. `WiFi-CSI-Human-Pose-Detection dataset` — confirm or rule out public CSI dataset.
    3. `mowa-fall-har` — confirm availability of fall/HAR CSI data with activity classes.
    4. `baby-monitor-wifi-csi breathing/apnea CSI data` — confirm or rule out public dataset.
  - For each confirmed dataset: create a full `DATASET_CARD.md` following the style of `datasets/mm-fi/DATASET_CARD.md`.
  - For each ruled-out candidate: update the candidate entry with a "Not available" or "Dataset not publicly distributed" note.

---

## Phase 10 — Open-Source Landscape Integration and Repository Alignment

**Status:** Completed (2025-05-24)

**Goals:**
- [x] Conduct open-source landscape analysis and identify the research gap
- [x] Retitle repository to Secure WiFi CSI Healthcare Sensing
- [x] Create `docs/open_source_gap.md` with 5-category landscape analysis
- [x] Add NoiSec, Awesome-RIS-Security, unilateral-csi-entropy as external defense references
- [x] Add CSI-Bench as high-priority future dataset candidate
- [x] Expand defense taxonomy to two-layer structure (preprocessing + model-level)
- [x] Update THIRD_PARTY_NOTICES.md with all new external references
- [x] Update references.md with Gemini-derived references (all Pending verification)
- [x] Update docs/project_status.md with Phase 10 tracking

**Outcome:** Repository now reflects the broader Secure WiFi CSI Healthcare Sensing research direction. Open-source gap is formally documented. All new items are external references only with Pending verification status.

---

## Phase 11 — External Reference Verification and Dataset Candidate Integration

**Status:** Not started

**Goals:**
- [ ] Verify NoiSec repository URL, license, and access method
- [ ] Verify Awesome-RIS-Security repository URL and license
- [ ] Verify unilateral-csi-entropy repository URL and license
- [ ] Verify CSI-Bench repository URL, license, and data-access method
- [ ] If CSI-Bench verified: create `datasets/csi-bench/DATASET_CARD.md` and update catalog
- [ ] Verify Attack\_WiFi\_Sensing, CsiGAN, AntiEave, WiFi-ADG licenses
- [ ] Update all Pending verification items with confirmed statuses
- [ ] Create third_party README stubs for NoiSec, Awesome-RIS-Security, unilateral-csi-entropy

---

## Phase 12 — Code Release Watchlist and Advanced Defense Implementation

**Status:** Not started

**Goals:**
- [ ] Create `docs/code_release_watchlist.md` to track paper-only references awaiting public code release
- [ ] Implement wavelet denoising defense (Tier 1, Layer 1)
- [ ] Implement PGD-style adversarial training (Tier 2, Layer 2)
- [ ] Evaluate NoiSec-style noise injection defense on synthetic pipeline (if license confirmed)
- [ ] Implement ensemble defense experiments
- [ ] Expand clinical-safety evaluation to additional healthcare sensing tasks

---

*Last updated: 2026-05-24*
