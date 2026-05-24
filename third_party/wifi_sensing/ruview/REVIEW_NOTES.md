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


---

## Dataset and Validation Status

> **Status:** Pending Review — This repository has not independently verified RuView's dataset, model provenance, or validation protocol.

RuView's dataset and validation status are not yet clearly established in this repository. The following sections document what is known, what is implied, and what requires further investigation before adversarial experiments should be designed.

**Key Statement:** Simulated or demo-mode data is not equivalent to validation on a real, labeled WiFi CSI dataset. Until a complete dataset, benchmark protocol, and reproducible evaluation are documented, RuView's sensing claims must not be treated as independently validated.

---

## Data Sources Mentioned or Implied

The following data sources are mentioned in, or implied by, RuView's repository, documentation, or description. None have been independently verified in this repository unless explicitly marked otherwise.

| Data Source Type | Status | Notes |
|---|---|---|
| Simulated / no-hardware demo data | Mentioned / pending verification | May support testing the interface without real hardware |
| User-recorded CSI sessions | Mentioned / pending verification | RuView may support live CSI recording workflows |
| Pretrained model weights | Pending verification | May be included or downloaded; training dataset not yet verified |
| Public WiFi sensing datasets (e.g., Wi-Pose, MM-Fi) | Mentioned or potentially relevant; not verified as main validation dataset | Must not be claimed as used unless directly documented |
| Peer-reviewed benchmark protocol | Not verified | No published paper or reproducible benchmark confirmed |

---

## Simulated Data

> *Pending Review*

RuView appears to support simulated or fallback data modes based on its repository structure and description. However:

- [ ] Has a simulation mode been confirmed to run without real WiFi hardware?
- [ ] What does simulated data represent? (Random noise, recorded replays, model-generated CSI?)
- [ ] Are simulation outputs labeled (fall / no-fall, presence / absence)?
- [ ] Are simulated outputs reproducible given the same seed or parameters?
- [ ] Is simulated data used for model training, evaluation, or only for interface demonstration?

**Important:** Simulated or demo-mode data is useful for testing the software interface but is **not equivalent to validation** on a real WiFi CSI dataset. Do not treat simulation outputs as validated sensing results.

---

## User-Recorded CSI Sessions

> *Pending Review*

RuView may support recording labeled CSI sessions from real WiFi hardware. However, this repository has not yet verified:

- [ ] Whether a complete public dataset (with labels, subject count, room setup, and benchmark protocol) exists for RuView.
- [ ] What file format recorded CSI sessions use.
- [ ] Whether labeled example recordings are included in the repository.
- [ ] What the train/test split is, if any.
- [ ] How many subjects and environments were used for any reported results.
- [ ] Whether recorded sessions can be replayed offline without real hardware.

**Important:** Even if RuView includes a data recording workflow, that is not the same as a publicly released, peer-reviewed validation dataset.

---

## Pretrained Models

> *Pending Review*

RuView may reference or use pretrained models for sensing tasks. However:

- [ ] What model files are included in the repository (`.pt`, `.pkl`, `.h5`, `.onnx`, etc.)?
- [ ] Are model weights available locally or downloaded at runtime?
- [ ] What dataset was used to train these models?
- [ ] What evaluation protocol was used to report model performance?
- [ ] Is a model card or training report available?
- [ ] Do pretrained models depend on external services (Hugging Face, API keys, cloud endpoints)?

**Important:** The dataset used to train a pretrained model must be verified before any adversarial evaluation can claim to apply to a specific data distribution.

---

## Public Datasets Mentioned

> *Caution: Do not claim use unless directly verified from primary sources.*

Some public WiFi sensing datasets may be relevant to RuView's work or may be mentioned in the context of WiFi sensing research. These are listed here as *potentially relevant* only:

| Dataset | Relevance to RuView | Status |
|---|---|---|
| Wi-Pose | WiFi-based pose estimation dataset | Mentioned or potentially relevant; not verified as used for training/evaluation |
| MM-Fi | Multi-modal WiFi sensing dataset | Mentioned or potentially relevant; not verified as used for training/evaluation |
| Other WiFi CSI datasets | Various academic datasets | Not yet reviewed |

**Rule:** A public dataset must be directly cited in RuView's README, model card, paper, or official documentation before it can be listed as the training or evaluation dataset. Mentions in GitHub issues, discussions, or examples are **not sufficient** evidence.

---

## Reproducibility Questions

- [ ] Can baseline inference be reproduced without real WiFi hardware?
- [ ] Are there runnable examples or demos with documented expected outputs?
- [ ] Are model files and input data provided, or must they be acquired separately?
- [ ] What dependencies are required (Python version, OS, drivers, hardware)?
- [ ] Are all claimed sensing results reproducible from the provided code and data?

---

## Dataset Review Checklist

| Item | Status | Evidence Needed | Notes |
|---|---|---|---|
| Simulated/no-hardware demo data | Mentioned / pending verification | RuView docs or runnable demo instructions | Useful for interface testing but not equivalent to real-data validation |
| User-recorded CSI sessions | Mentioned / pending verification | Data recording workflow, file format, labels, and example recordings | Need to determine if sample recordings are included and reproducible |
| Pretrained model files | Pending verification | Model card, weights, training dataset, evaluation protocol | Need to identify exactly what data trained the model |
| Public datasets such as Wi-Pose or MM-Fi | Mentioned or potentially relevant; not verified as main validation dataset | Direct documentation that RuView trained or evaluated on these datasets | Do not claim use unless directly verified |
| Peer-reviewed benchmark protocol | Not verified | Paper, benchmark split, metrics, subject/room details | Needed before treating claims as academically validated |

---

## Current Conclusion

> **Current conclusion:** RuView is useful as a third-party WiFi sensing reference and possible experimental target, but this repository has not yet verified a clear academic-style dataset, benchmark protocol, or independent validation result for RuView. Dataset and validation status remain **pending review**.

Specifically:
- This repository has **not independently reproduced** RuView's dataset pipeline or validation results.
- RuView should **not be cited as validated evidence** for any pipeline in this repository.
- Any adversarial robustness experiments against RuView must first document the baseline data source, model inputs, and output format.
- If only simulated data is available, adversarial results must be labeled as **synthetic/simulation-only** and clearly distinguished from real-data evaluation.
- Dataset and validation status must remain marked as *Pending Review* until all checklist items above are completed and verified.

---

*Dataset and validation review section added: May 2026. Review is incomplete. Do not use this document to make validation claims.*
