# Threat Model: Physical-Layer Security for WiFi CSI-Based Fall Detection

> **Status:** Conceptual notes for early-stage research prototype. All scenarios described here are based on synthetic data and theoretical analysis only.

---

## 1. What is WiFi CSI?

WiFi Channel State Information (CSI) describes how a wireless signal propagates from a transmitter to a receiver through a multipath channel. In IEEE 802.11 (WiFi) systems, CSI is estimated at the **physical layer** using:

- **OFDM preamble symbols** — known training sequences transmitted at the start of each packet
- **Long Training Fields (LTFs)** — used for channel estimation per subcarrier
- **Pilot subcarriers** — embedded reference tones used for tracking channel variation over time

The receiver uses these known symbols to estimate the complex channel response for each OFDM subcarrier, yielding amplitude and phase information that reflects the physical environment — including the presence and movement of people.

**Key point:** CSI is extracted at the radio hardware level, **before any encryption or higher-layer security mechanisms protect the payload**. This means CSI is accessible to any receiver that can receive the 802.11 frames, regardless of whether the payload is encrypted.

---

## 2. Why CSI-Based Sensing May Be Vulnerable

Because CSI is derived from the physical layer before cryptographic protections apply, CSI-based sensing systems face an underexplored attack surface:

- The sensing system trusts that the CSI it receives reflects the true physical environment.
- An adversary with access to the RF environment can potentially manipulate what CSI measurements look like.
- Unlike payload data, CSI cannot be easily authenticated using standard WiFi encryption (WPA2/WPA3).
- Machine learning models trained on CSI data may be sensitive to distribution shift caused by environmental manipulation.

---

## 3. Example Threat Scenarios

### Scenario 1: RF Channel Manipulation
**Description:** An adversary physically alters the RF propagation environment to change CSI measurements. This could involve placing RF reflectors, absorbers, or other objects that shift the multipath channel profile.

**Potential impact:**
- The sensing system may no longer detect falls correctly because the channel fingerprint has changed.
- A fall event may no longer produce the expected CSI signature.

### Scenario 2: Spoofed Signal Injection
**Description:** An adversary transmits fabricated 802.11 frames at the operating frequency, injecting false CSI measurements into the receiver's channel estimation process. This exploits the fact that CSI is derived from received training symbols without authentication.

**Potential impact:**
- The receiver may process adversarially crafted CSI instead of (or blended with) true channel measurements.
- The sensing model could be fed manipulated input data without any indication of tampering.

### Scenario 3: Synthetic CSI Perturbation (Adversarial ML)
**Description:** An adversary with knowledge of the trained ML model applies small, carefully designed perturbations to CSI input features — analogous to adversarial examples in computer vision.

**Potential impact:**
- A fall event producing a recognizable CSI signature could be subtly perturbed to be misclassified as normal activity.
- The perturbation may be imperceptible in signal space but sufficient to fool the classifier.

---

## 4. Possible Safety Impacts

| Threat | Safety Impact |
|---|---|
| Missed fall detection | A real fall is not detected; no alert is sent to caregivers |
| False alarm generation | Normal activity is misclassified as a fall; unnecessary emergency response |
| Alert suppression | A real emergency triggers no notification, delaying intervention |
| Time-to-alarm delay | Detection is delayed beyond clinically acceptable response windows |

In eldercare or clinical monitoring contexts, any of these outcomes could have serious consequences for patient safety.

---

## 5. Current Scope of This Repository

This repository currently demonstrates concepts using **synthetic, simulated CSI-like data only**. It does not:
- Implement real adversarial attack methods
- Use real WiFi hardware or real CSI captures
- Evaluate attack effectiveness on real sensing deployments

The threat model presented here is a **conceptual research framework** to guide future work on robust and secure WiFi-based health sensing systems.

---

## 6. Planned Future Work

- Implement synthetic adversarial perturbation examples using scikit-learn and later PyTorch
- Evaluate classifier robustness under input perturbation
- Explore signal authentication concepts for CSI-based systems
- Review cross-layer defense strategies

---

> **Disclaimer:** This document describes conceptual threat scenarios for research purposes. It is not a security audit, penetration test, or clinical risk assessment.
