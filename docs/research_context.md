# Research Context

## Overview

This repository supports a PhD research program in **Electrical Engineering and Computer Science** focused on cybersecurity for wireless medical networks, with a specific emphasis on WiFi Channel State Information (CSI) sensing for healthcare and elderly monitoring.

## Research Domain

WiFi CSI-based passive sensing uses the fine-grained channel information available from commodity 802.11 hardware to infer physical events — including human activity, movement, respiration, and falls — without cameras or wearable devices. This makes it attractive for non-invasive elderly care and smart-home health monitoring.

## Core Research Questions

1. Can WiFi CSI signals be reliably used for fall detection in realistic environments?
2. How robust are CSI-based sensing systems against adversarial manipulation and signal spoofing?
3. What are the privacy implications of passive WiFi sensing in healthcare contexts?
4. How can federated learning and privacy-preserving techniques be integrated into CSI sensing pipelines?

## Research Gap

Existing work on WiFi CSI sensing largely focuses on detection performance in controlled lab environments. Key open problems include:

- Cross-layer linkage between physical-layer attacks and clinical sensing outcomes
- Real-time adversarial attack detection with adaptive defenses
- Privacy-preserving hierarchical federated learning for health monitoring
- Robustness evaluation under realistic environmental and adversarial conditions
- Security implications of WiFi 7 for continuous health monitoring

## Positioning of This Repository

This repository is a **research prototype** and **synthetic-data workflow**. It does not claim clinical validation or deployment readiness. Its purpose is to:

- Establish a clean, extensible baseline for CSI signal simulation and preprocessing
- Develop and evaluate baseline ML models for fall detection on synthetic data
- Create a foundation for future adversarial robustness and security extensions
- Document the research trajectory for academic review and reproducibility

## Institutional Context

- **Institution**: Portland State University, Department of Electrical and Computer Engineering
- **Program**: PhD in Electrical Engineering and Computer Science
- **Research Focus**: Cybersecurity for Wireless Medical Networks

---

*See also: [validation_status.md](validation_status.md), [security_motivation.md](security_motivation.md), [roadmap.md](roadmap.md)*
