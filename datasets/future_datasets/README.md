# Future Dataset Entries — Secure WiFi CSI Healthcare Sensing Research Prototype

## Purpose

This folder is a placeholder for WiFi CSI-related datasets that may be added to the catalog in future phases. It lists candidate dataset types and specific datasets relevant to the broader **Secure WiFi CSI Healthcare Sensing** research direction, including fall detection, vital-sign monitoring, apnea detection, and adversarial robustness evaluation.

> **Current Status:** This repository uses **synthetic CSI-like data only**. No real datasets have been downloaded, integrated, or validated.

**Future datasets should be added only after:**
1. Identifying the official source and verifying the license
2. Confirming task relevance to the repository's research focus
3. Completing IRB/data-access review as required
4. Confirming citation requirements
5. Creating a proper dataset card, license summary, and download instructions

**Datasets should first be cataloged before any integration into the pipeline.**

---

## Candidate Dataset Types

| Category | Relevance |
|----------|-----------|
| WiFi CSI fall detection | Direct: supports fall-detection evaluation |
| WiFi CSI activity recognition | Indirect: activity context for safety sensing |
| WiFi CSI pose estimation | Indirect: body position for fall inference |
| WiFi CSI vital signs / breathing / apnea | Direct/Indirect: health sensing research context |
| Multi-modal CSI datasets | Indirect: broader sensing research context |
| Adversarial WiFi sensing / privacy defense data | Indirect: security and robustness context |
| Standardized WiFi sensing benchmarks | Direct: evaluation and comparison baselines |

---

## High-Priority Candidate Datasets

### CSI-Bench (Real WiFi Sensing Benchmark)

- **Description:** A standardized benchmark for real WiFi sensing tasks, providing evaluation protocols across multiple sensing scenarios including activity recognition, fall detection, and pose estimation.
- **Source:** Pending verification (academic publication; GitHub repository under review)
- **License:** Pending verification
- **Relevance:** High-priority candidate for real-data validation phase. Provides standardized benchmarks that would allow direct comparison of synthetic prototype results against real-world sensing performance.
- **Access:** Pending verification (likely requires academic affiliation or data-use agreement)
- **Status:** Candidate — not downloaded, not integrated, not validated
- **Verification Required:** License, access method, citation, IRB applicability
- **Notes:** Identified via open-source landscape analysis (Gemini report 2025). See `docs/open_source_gap.md` for context.

---

## Candidate Dataset List

*Note: The datasets listed below are candidates only. None are currently downloaded, integrated, or validated by this repository.*

### Fall Detection Datasets

| Dataset | Description | Status | Notes |
|---------|-------------|--------|-------|
| FallDeFi | WiFi CSI-based fall detection dataset; published research on CSI fingerprinting for fall events. | Candidate | License: Pending verification |
| CSI-Bench | Standardized real WiFi sensing benchmark (multiple tasks including fall detection). | **High Priority Candidate** | License: Pending verification. See section above. |

### Activity Recognition Datasets

| Dataset | Description | Status | Notes |
|---------|-------------|--------|-------|
| Widar 3.0 | Large-scale WiFi CSI gesture and activity recognition dataset. | Candidate | Public academic release |
| UT-HAR | University of Toronto WiFi CSI human activity recognition dataset. | Candidate | Academic access |
| SignFi | WiFi CSI sign language recognition dataset. | Candidate | Public |
| MM-Fi | Multi-modal CSI HAR benchmark (WiFi + radar + vision). | Candidate | Academic release; IEEE publication |
| NTU-Fi HAR | NTU activity recognition WiFi CSI dataset. | Candidate | License: Pending verification |
| NTU-Fi HumanID | NTU human identity recognition WiFi CSI dataset. | Candidate | License: Pending verification |

### Vital Signs / Health Sensing Datasets

| Dataset | Description | Status | Notes |
|---------|-------------|--------|-------|
| WiFi vital sign datasets | Various published WiFi CSI datasets for respiration and heart rate monitoring. | Research ongoing | Multiple sources; license varies |

### Other WiFi CSI Datasets

| Dataset | Description | Status | Notes |
|---------|-------------|--------|-------|
| WiFi CSI pose datasets | Additional WiFi CSI datasets with pose or skeleton annotations. | Research ongoing | Multiple sources |
| mowa-fall-har | WiFi sensing for fall and HAR tasks. | Candidate | License: Pending verification |

---

## Integration Checklist (per Dataset)

Before integrating any candidate dataset:

- [ ] License verified and compatible with repository use
- [ ] Official source identified and documented
- [ ] Citation format confirmed
- [ ] IRB/data-use agreement reviewed (if applicable)
- [ ] Dataset card created in this folder
- [ ] Entry added to `datasets/dataset_catalog.md`
- [ ] No data files committed to repository
- [ ] Download instructions documented (not automated)

---

## Related Documents

- [`datasets/dataset_catalog.md`](../dataset_catalog.md) — Full dataset catalog
- [`docs/open_source_gap.md`](../../docs/open_source_gap.md) — Open-source landscape analysis
- [`docs/related_projects.md`](../../docs/related_projects.md) — External project references

---

*Maintained as part of the Secure WiFi CSI Healthcare Sensing research prototype at Portland State University.*
