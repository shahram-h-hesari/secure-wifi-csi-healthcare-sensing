# Open-Source Landscape Gap Analysis
## Secure WiFi CSI Healthcare Sensing Research Prototype

> **Last Updated:** 2025  
> **Status:** Active research gap — no public repository fully closes this gap as of analysis date.

---

## Summary

This document presents a systematic analysis of the open-source landscape for **WiFi CSI-based healthcare sensing combined with adversarial robustness and clinical-safety evaluation**. The analysis is informed by a broad review of public GitHub repositories and academic resources.

**Finding:** A clear and significant research gap exists. No publicly available repository fully combines:

1. WiFi CSI-based healthcare sensing (fall detection / vital signs monitoring)
2. Adversarial robustness and evasion-attack stress testing
3. Clinical-safety-aware evaluation metrics (missed fall rates, false alarm rates)
4. Defense method taxonomy spanning preprocessing and model-level layers

This repository (`secure-wifi-csi-healthcare-sensing`) is designed to address that gap as a research prototype using **synthetic CSI-like data only**.

---

## Landscape Review by Category

### Category 1: WiFi CSI Sensing (General / Non-Security)

Several public repositories address WiFi CSI for human activity recognition (HAR) and fall detection in a general sensing context, without adversarial or clinical-safety components:

| Repository | Focus | Adversarial? | Clinical-Safety? | Notes |
|---|---|---|---|---|
| MM-Fi Dataset | Multi-modal CSI HAR benchmark | No | No | Real data; no adversarial component |
| Wi-Pose / Wi-Mesh | Pose estimation from WiFi CSI | No | No | Sensing only; no security layer |
| SignFi | WiFi gesture recognition | No | No | No adversarial robustness |
| Widar 3.0 | Cross-domain WiFi HAR | No | No | No clinical-safety metrics |
| UT-HAR | HAR benchmark dataset | No | No | Dataset only; no ML pipeline |
| NTU-Fi HAR / HumanID | Activity / identity recognition | No | No | No adversarial or safety component |
| WiFi-CSI-Human-Pose-Detection | Pose detection from CSI | No | No | External reference; sensing only |

**Gap:** None of these repositories include adversarial stress testing or clinical-safety evaluation.

---

### Category 2: Adversarial Attacks on WiFi Sensing

A small number of repositories address adversarial attacks specifically targeting WiFi sensing:

| Repository | Focus | Healthcare? | Clinical-Safety? | Notes |
|---|---|---|---|---|
| [Attack\_WiFi\_Sensing](https://github.com/Guolin-Yin/Attack_WiFi_Sensing) | Evasion attacks, adversarial training, robustness evaluation | No | No | Core adversarial reference; no healthcare framing |
| [AntiEave-WiFi-Sensing](https://github.com/topics/antieave) | Anti-eavesdropping for WiFi sensing | Partial | No | Privacy-preserving; not healthcare-safety focused |
| [WiFi-ADG](https://github.com/topics/wifi-adg) | Adversarial domain generalization | No | No | Domain robustness; no clinical outcomes |

**Gap:** Existing adversarial WiFi sensing work does not frame attacks in terms of clinical-safety outcomes (e.g., missed fall consequences, false alarm costs).

---

### Category 3: Physical-Layer Security / RIS Security

Repositories in this space address physical-layer attacks and reconfigurable intelligent surface (RIS) security:

| Repository | Focus | Healthcare? | CSI Sensing? | Notes |
|---|---|---|---|---|
| Awesome-RIS-Security | Physical-layer attack literature tracker | No | Partial | Literature aggregator; no implementation |
| NoiSec | Noise-based adversarial defense | No | Partial | Defense reference; no healthcare framing |
| unilateral-csi-entropy | CSI entropy for edge security | No | Yes | Cryptographic entropy; not sensing-safety focused |

**Gap:** Physical-layer security work does not integrate healthcare sensing or clinical-safety constraints.

---

### Category 4: Healthcare Sensing + ML (Non-WiFi)

Several repositories address healthcare sensing with ML but use different modalities (radar, UWB, camera):

| Repository | Modality | Adversarial? | Clinical-Safety? | Notes |
|---|---|---|---|---|
| Various radar fall detection repos | Radar | Rare | No | Different modality |
| Camera-based fall detection | Vision | Occasional | No | Privacy concerns; different threat model |

**Gap:** Healthcare sensing adversarial work in other modalities does not directly transfer to WiFi CSI threat models.

---

### Category 5: Benchmarks and Datasets (Future Candidates)

| Dataset/Benchmark | Focus | Access | Status |
|---|---|---|---|
| CSI-Bench | Real WiFi sensing benchmark | Pending verification | Future dataset candidate |
| MM-Fi | Multi-modal HAR | Academic access | Future dataset candidate |
| Widar 3.0 | Cross-domain WiFi HAR | Public | Future dataset candidate |

> **Note:** All datasets above are listed as **future candidates only**. This repository currently uses **synthetic CSI-like data only**. Integration of real datasets requires IRB review, data access agreements, and license verification.

---

## The Combined Gap

The table below summarizes the gap across all reviewed categories:

| Capability | General CSI Repos | Adversarial CSI Repos | Physical-Layer Security | This Repository |
|---|---|---|---|---|
| WiFi CSI sensing pipeline | Yes | Partial | No | Yes (synthetic) |
| Healthcare / fall detection framing | Partial | No | No | Yes (synthetic) |
| Adversarial robustness testing | No | Yes | Partial | Yes (synthetic) |
| Clinical-safety evaluation metrics | No | No | No | Yes (synthetic) |
| Defense method taxonomy | No | Partial | Partial | Yes (documented) |
| Open-source code availability | Yes | Partial | Limited | Yes |
| Real validated data | Yes (some) | No | No | No (future work) |

**This repository uniquely combines all five capabilities, albeit using synthetic data as a research prototype.**

---

## Research Implications

The identified gap has direct implications for PhD research positioning:

1. **Novelty:** No existing open-source repository combines healthcare CSI sensing with adversarial robustness and clinical-safety metrics.
2. **Contribution:** This prototype demonstrates a feasible pipeline architecture for this combined problem.
3. **Future Work:** Integration of real CSI datasets (CSI-Bench, MM-Fi, Widar) would substantially strengthen empirical claims.
4. **Community Need:** The gap suggests an unmet need for defense-aware, clinically-grounded CSI sensing tools.

---

## Methodology Notes

- Review conducted via GitHub search, academic paper cross-referencing, and open-source landscape analysis tools.
- All referenced repositories are **external references only** — no code or data has been copied.
- License statuses for new/candidate repos marked as **Pending verification** until confirmed.
- This analysis will be updated as new repositories are identified.

---

## Related Documents

- [`docs/related_projects.md`](related_projects.md) — Full external reference list by research area
- [`datasets/future_datasets/README.md`](../datasets/future_datasets/README.md) — Candidate real datasets
- [`docs/defense_methods.md`](defense_methods.md) — Defense taxonomy
- [`THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md) — Attribution and license notices

---

*Analysis conducted in support of PhD research at Portland State University — Secure WiFi Sensing for Healthcare IoT.*
