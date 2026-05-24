# RuView Review Notes

> **Status:** Initial review template — **not complete**. All unverified items are marked as *Pending Review*. This repository has not independently validated RuView.

---

## Review Purpose

This document provides a structured technical review template for studying RuView as a third-party WiFi sensing project. The goals of this review are:

1. Understand what parts of RuView run with simulated data vs. real hardware
2. Identify data files, model files, and external dependencies included in the repository
3. Document reproducibility status of simulation outputs
4. Identify parts of the pipeline that could be studied for future adversarial robustness evaluation
5. Note any validation claims and assess whether they are supported by code, data, or tests

---

## Repository Structure Observed

> *Pending Review — complete after running `git submodule update` to pull the RuView code.*

| Folder/File | Observed Purpose | Status |
|---|---|---|
| `.claude-flow/` | Claude agentic workflow files | Pending Review |
| `.claude-plugin/` | Claude plugin configuration | Pending Review |
| `.claude/` | Claude configuration | Pending Review |
| `.github/` | GitHub Actions workflows | Pending Review |
| `.swarm/` | Swarm agent configuration | Pending Review |
| `.vscode/` | VS Code workspace config | Pending Review |
| `archive/` | Archived files | Pending Review |
| `assets/` | Assets (images, icons, etc.) | Pending Review |
| `dashboard/` | Dashboard/interface code | Pending Review |
| `data/` | Data files | Pending Review |
| `docker/` | Docker configuration | Pending Review |
| `docs/` | Documentation | Pending Review |
| `examples/` | Example files | Pending Review |

---

## Simulation Workflow

> *Pending Review*

- [ ] Does RuView include a simulation mode that does not require real WiFi hardware?
- [ ] Is there a Docker-based simulation environment?
- [ ] What are the entry points for running the simulation (e.g., `main.py`, `app.py`, Docker Compose)?
- [ ] What simulation parameters are configurable?
- [ ] Are simulation outputs deterministic (reproducible given the same inputs)?

**Notes:** *Not yet reviewed. To be completed after pulling RuView code via submodule.*

---

## Data and Model Files

> *Pending Review*

- [ ] What data files are included in the `data/` directory?
- [ ] Are sample or synthetic CSI-like data files included?
- [ ] What model files are included (e.g., `.pt`, `.pkl`, `.h5`, `.onnx`)?
- [ ] Does the project download models from external sources (Hugging Face, URLs)?
- [ ] What model weights are used and where are they stored?
- [ ] Are pretrained models included directly in the repository?
- [ ] What outputs can be reproduced without hardware?

**Notes:** *Not yet reviewed.*

---

## Hardware Requirements

> *Pending Review*

- [ ] What WiFi hardware is required for real-data operation?
- [ ] Does the project mention ESP32, Intel 5300, Nexmon, or other CSI-capable hardware?
- [ ] What parts of the pipeline require a CSI-capable WiFi chipset?
- [ ] Can any component be run in a purely software/simulation mode?
- [ ] Are there Docker or cloud-based alternatives for hardware-dependent components?

**Notes:** *From the repository description, RuView appears to use commodity WiFi hardware. Specific hardware requirements are pending review.*

---

## Reproducibility Status

> *Pending Review*

| Component | Reproducible Without Hardware | Status |
|---|---|---|
| Simulation mode | Unknown | Pending Review |
| Dashboard/UI | Unknown | Pending Review |
| Baseline inference | Unknown | Pending Review |
| Data collection | No (requires WiFi hardware) | Inferred |
| Model training | Unknown | Pending Review |

---

## Validation Claims

> *This repository does not independently validate any of RuView's claims.*

- [ ] What claims does RuView make about vital sign monitoring accuracy?
- [ ] What claims does RuView make about presence detection performance?
- [ ] What claims does RuView make about spatial intelligence?
- [ ] Which claims are supported by code, tests, or data in the repository?
- [ ] Which claims require hardware validation that cannot be reproduced here?
- [ ] Are there published papers or benchmarks supporting these claims?

**Notes:** *All claims in RuView's documentation are attributed solely to the original authors. No claims have been independently validated in this repository.*

---

## Open Questions

1. What parts of RuView run with simulated data?
2. What parts require real CSI-capable hardware?
3. What data files are included in the repository?
4. What model weights are used and where are they stored?
5. Does the project use Hugging Face models or external downloads?
6. What outputs can be reproduced without hardware?
7. Which claims are supported by code, data, tests, or documentation?
8. Which claims require independent verification?
9. What parts could be useful for adversarial robustness experiments?

---

## Next Review Tasks

- [ ] Add RuView as a Git submodule and pull the code (see `SUBMODULE_INSTRUCTIONS.md`)
- [ ] Review `data/` folder contents
- [ ] Review `docker/` configuration for simulation options
- [ ] Review `dashboard/` code structure
- [ ] Review `docs/` for API and architecture documentation
- [ ] Identify model file types and storage locations
- [ ] Determine which components can be exercised without real WiFi hardware
- [ ] Identify candidate pipeline points for offline perturbation experiments
- [ ] Document findings in this file under each section above

---

*Review started: May 2026. Review is incomplete. Do not use this document to make validation claims.*
