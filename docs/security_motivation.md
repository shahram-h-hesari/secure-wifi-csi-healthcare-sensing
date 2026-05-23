# Security Motivation

## Why Security Matters for WiFi CSI Sensing

WiFi CSI-based sensing systems operate at the **physical layer** of wireless networks, inferring human activity, vital signs, and presence from radio frequency channel measurements. While powerful, this sensing modality introduces a distinct and underexplored set of **security and privacy vulnerabilities** that must be addressed before such systems can be responsibly deployed in healthcare settings.

## Threat Landscape

### 1. Adversarial Attacks on Classification Models

Machine learning models used for fall detection and activity recognition can be vulnerable to adversarial perturbations. An attacker with knowledge of the sensing system could craft RF signals or inject noise to cause:
- False negatives (missed fall detection)
- False positives (spurious alarms)
- Targeted misclassification of specific activities

### 2. CSI Signal Spoofing

An attacker in the RF environment could transmit signals designed to inject or manipulate CSI measurements, potentially overriding legitimate sensing data. This is particularly concerning in healthcare IoT environments where physical access to the radio environment may be limited.

### 3. Privacy Leakage

The same CSI properties that enable fall detection also enable:
- **Presence detection**: identifying whether someone is home
- **Activity inference**: tracking daily routines
- **Behavioral profiling**: long-term pattern analysis

Without privacy-preserving mechanisms, passive WiFi sensing becomes a surveillance vector, even when deployed with beneficial intent.

### 4. Physical-Layer Denial of Sensing

Jamming or interference attacks could degrade CSI quality to the point where fall detection is unreliable, creating a safety risk for monitored individuals.

## Research Direction

This repository is being developed with the following security objectives as future extensions:

- **Adversarial robustness**: Evaluating and improving model resistance to adversarial CSI perturbations
- **Attack detection**: Real-time identification of anomalous CSI patterns indicative of spoofing or injection
- **Privacy-preserving sensing**: Federated learning and differential privacy techniques to limit data exposure
- **Threat modeling**: Formal documentation of the attack surface for WiFi CSI healthcare sensing (see [threat_model.md](threat_model.md))

## Connection to Broader Research

This security focus aligns with the broader PhD research direction on **cybersecurity for wireless medical networks**, and positions this repository as a foundation for investigating the intersection of:

- Physical-layer wireless security
- Healthcare IoT safety and reliability
- Adversarial machine learning
- Privacy-preserving distributed sensing

---

*See also: [threat_model.md](threat_model.md), [research_context.md](research_context.md), [roadmap.md](roadmap.md)*

*Last updated: May 2026*
