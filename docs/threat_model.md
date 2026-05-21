# Physical-Layer Threat Model for WiFi CSI Sensing

---

## Purpose

This document summarizes conceptual security risks for WiFi CSI-based sensing systems. It is intended as a research-level framing document to support the PhD research context of this repository. It does not describe implemented attack tools or validated exploits.

---

## What Is WiFi CSI?

WiFi Channel State Information (CSI) describes how a wireless signal propagates from a transmitter to a receiver through the physical environment. CSI is extracted at the physical layer from OFDM preamble symbols, training sequences, and pilot subcarriers. It captures amplitude and phase information across multiple subcarriers and can reflect changes in the environment caused by human motion, breathing, or other physical disturbances.

Because CSI is derived before higher-layer encryption and security mechanisms are applied, it represents a distinct and underexplored attack surface in WiFi-based sensing systems.

---

## Why CSI-Based Sensing Can Be Vulnerable

CSI is derived from the physical behavior of RF signals in the environment. Unlike application-layer data, which is typically protected by encryption (e.g., WPA3), CSI reflects raw channel conditions that:

- Can be observed or estimated without decrypting payload data
- Can be manipulated by altering the RF channel (e.g., introducing interference or reflectors)
- Can be perturbed by injecting synthetic signals into the wireless medium
- Can be adversarially crafted to fool machine learning models trained on CSI features

This means that a sensing pipeline built on CSI can potentially be attacked at the physical layer, bypassing application-layer security protections entirely.

---

## Example Threat Scenarios

### 1. RF-Channel Manipulation
An adversary physically alters the RF propagation environment to corrupt CSI measurements. Examples include introducing metallic reflectors, RF absorbers, or intentional interference sources near the sensing area. This can degrade CSI quality or shift signal characteristics in ways that confuse a fall detection classifier.

### 2. Spoofed Signal Injection
An adversary transmits RF signals that mimic the CSI patterns associated with normal activity, even during an actual fall event. If the sensing system cannot distinguish spoofed signals from genuine CSI, critical fall alerts may be suppressed.

### 3. Synthetic CSI Perturbation
An adversary adds carefully crafted perturbations to the CSI measurement stream. These perturbations are small enough to be imperceptible at the application layer but large enough to shift extracted features beyond a classifier's decision boundary, causing misclassification.

### 4. Adversarial Manipulation of Sensing Features
An adversary with knowledge of the ML model architecture and feature extraction pipeline crafts inputs that cause systematic misclassification. This is analogous to adversarial examples in computer vision but applied to the CSI feature domain (e.g., manipulating mean amplitude, energy, or peak-to-peak range features).

---

## Possible Safety Impacts

### 1. Missed Falls
A fall event occurs but the sensing system classifies it as normal activity due to signal manipulation. The fall is not detected and no alert is generated, potentially delaying emergency response.

### 2. False Alarms
Normal activity is classified as a fall event due to spoofed or perturbed CSI signals. Repeated false alarms can erode trust in the system and lead to alert fatigue among caregivers.

### 3. Suppressed Alerts
An adversary actively prevents the fall detection system from generating any alert, even when a genuine fall occurs. This is a denial-of-sensing attack targeting safety-critical functionality.

### 4. Time-to-Alarm Delay
CSI perturbations cause the system to take longer to classify an event correctly, introducing dangerous delays in emergency response time for elderly or vulnerable individuals.

---

## Current Repository Limitation

The current repository demonstrates only synthetic concept-level examples and does not validate real-world attack feasibility or clinical impact. All signals are simulated, no real adversarial attacks are implemented, and no real-world sensing environment has been tested. The threat scenarios described above are theoretical and are intended to frame the research motivation, not to describe validated vulnerabilities.

---

## Author

**Shahram H. Hesari**  
PhD Candidate, Electrical and Computer Engineering  
Portland State University
