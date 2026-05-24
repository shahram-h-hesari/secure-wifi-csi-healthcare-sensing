# Run RuView Baseline Simulation

> **Status:** Planned steps only. All commands marked **Pending Verification** until actually tested in a real environment.

---

## Purpose

This document outlines planned steps for running the RuView baseline simulation. The goal is to reproduce RuView's basic simulation output in a controlled local environment before designing any perturbation experiments.

---

## Prerequisites

> *Pending Verification*

- [ ] Git installed and RuView submodule initialized (see `third_party/wifi_sensing/ruview/SUBMODULE_INSTRUCTIONS.md`)
- [ ] Docker Desktop or Docker Engine installed (if Docker-based)
- [ ] Python 3.10+ (if running directly without Docker)
- [ ] Sufficient RAM and disk space for model downloads (if applicable)

---

## Step 1: Clone and Initialize Submodule

> *Pending Verification*

```bash
# If cloning fresh with submodule:
git clone --recurse-submodules https://github.com/shahram-h-hesari/wifi-csi-fall-detection.git

# Or initialize submodule in existing clone:
git submodule update --init --recursive

# Navigate to RuView directory:
cd third_party/wifi_sensing/ruview/RuView
```

**Notes:** *Not yet tested. Mark as verified after running successfully.*

---

## Step 2: Review RuView Installation Instructions

> *Pending Verification*

- [ ] Review `docs/` folder in RuView for installation guide
- [ ] Check if `requirements.txt` or `pyproject.toml` is present
- [ ] Check if Docker Compose file is present in `docker/`
- [ ] Note any environment variables or configuration required

**Notes:** *Not yet reviewed.*

---

## Step 3: Environment Setup (Docker Method)

> *Pending Verification — Commands not yet tested*

```bash
# Navigate to docker directory (if present):
cd docker/

# Review Docker Compose configuration:
cat docker-compose.yml

# Build Docker image (if Dockerfile present):
docker build -t ruview-local .

# Start with Docker Compose (if available):
docker-compose up
```

**Notes:** *Docker commands are placeholders. Verify against actual RuView docker/ configuration before running.*

---

## Step 4: Environment Setup (Direct Python Method)

> *Pending Verification — Commands not yet tested*

```bash
# Create virtual environment:
python -m venv ruview_env
source ruview_env/bin/activate  # Linux/Mac
# or: ruview_env\Scripts\activate  # Windows

# Install dependencies:
pip install -r requirements.txt

# Run main entry point (placeholder - verify actual entry point):
python main.py
```

**Notes:** *Entry point not yet verified. Review RuView docs before running.*

---

## Step 5: Observe and Record Outputs

> *Pending Verification*

- [ ] What does the baseline simulation output?
- [ ] Are outputs written to files, terminal, or a dashboard?
- [ ] What format are the outputs (JSON, CSV, plot, dashboard URL)?
- [ ] What inputs did the simulation use?
- [ ] Were any model downloads triggered?

**Notes:** *Record observations here after running.*

---

## Expected Observations (Placeholder)

| Observation | Value | Status |
|---|---|---|
| Simulation starts without error | TBD | Pending |
| Output format | TBD | Pending |
| Hardware required | TBD | Pending |
| Model files loaded | TBD | Pending |
| Baseline inference output | TBD | Pending |

---

## Troubleshooting Notes

> *Add notes here after attempting to run RuView.*

---

*Document created: May 2026. All steps are planned and pending verification.*


---

## Data and Model Provenance Checklist

> **Complete this checklist before designing any perturbation experiments.**

### Data Source

- [ ] Dataset status: simulated / recorded CSI / public dataset / unknown
- [ ] Input file paths: (document exact paths once identified)
- [ ] Input file format: (CSV, NumPy, HDF5, proprietary format, etc.)
- [ ] Whether sample data is included in the repository or must be downloaded/recorded
- [ ] Whether inputs can be replayed offline without real WiFi hardware

### Model Source

- [ ] Model source: local / downloaded / pretrained / external service / unknown
- [ ] Model file paths: (document exact paths once identified)
- [ ] Model file format: (.pt, .pkl, .h5, .onnx, etc.)
- [ ] Training dataset: (must be verified from model card or official documentation — TBD)
- [ ] Evaluation dataset: (must be verified from model card or official documentation — TBD)
- [ ] Whether model weights are available offline or require runtime download

### Reproducibility Status

- [ ] Reproducibility status: reproduced / partially reproduced / not reproduced / pending
- [ ] Whether baseline inference runs without errors
- [ ] Whether outputs are deterministic given the same inputs
- [ ] Whether hardware is required for claimed sensing outputs
- [ ] What outputs are produced: labels / predictions / visualizations / simulated placeholders

### Provenance Summary Table

| Field | Value | Status |
|---|---|---|
| Dataset status | simulated / recorded CSI / public dataset / unknown | Pending |
| Input file | TBD | Pending |
| Input format | TBD | Pending |
| Model source | local / downloaded / pretrained / unknown | Pending |
| Training dataset | TBD — verify from model card | Pending |
| Evaluation dataset | TBD — verify from model card | Pending |
| Reproducibility status | reproduced / partially / not reproduced / pending | Pending |
| Hardware required | Yes / No / Partial / Unknown | Pending |
| Output type | labels / predictions / visualizations / placeholders | Pending |

---

*Data and model provenance checklist added: May 2026. Fill in after running baseline simulation.*
