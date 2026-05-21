# Physical-Layer Threat Model for WiFi CSI Sensing

This document summarizes conceptual security risks for WiFi Channel State Information (CSI)-based sensing systems. It is intended to support the research context of this repository and does **not** describe implemented attack tools, validated exploits, or instructions for compromising real systems.

## Purpose

WiFi CSI-based sensing systems use physical-layer wireless measurements to infer environmental or human activity patterns. In healthcare and eldercare applications, this may include contactless fall detection, respiration monitoring, heart-rate estimation, or activity recognition.

The purpose of this document is to frame potential physical-layer risks that could affect the reliability of CSI-based sensing pipelines, especially when those pipelines use machine learning models.

## What Is WiFi CSI?

WiFi Channel State Information describes how a wireless signal propagates from a transmitter to a receiver through the physical environment. CSI can capture changes in signal amplitude and phase across OFDM subcarriers.

In WiFi systems, CSI is derived from physical-layer information such as OFDM preamble symbols, training sequences, and pilot subcarriers. Because human motion, breathing, posture changes, and environmental movement can alter the wireless channel, CSI is often studied as a signal source for contactless sensing.

## Why CSI-Based Sensing Can Be Vulnerable

CSI reflects physical-layer channel behavior rather than application-layer payload content. Higher-layer security mechanisms can protect data payloads, but they do not necessarily protect the sensing features derived from the wireless channel itself.

This creates an underexplored attack surface for WiFi-based sensing systems. A sensing pipeline that depends on CSI may be affected by changes in the RF environment, spoofed or interfering signals, or perturbations that alter extracted signal features.

In safety-sensitive healthcare sensing, this matters because even small changes in the sensing input could affect downstream classification, detection, or alert-generation behavior.

## Example Threat Scenarios

The following scenarios are conceptual research examples. They are not implemented in this repository.

### 1. RF-Channel Manipulation

An adversary or environmental disturbance alters the RF propagation environment in a way that changes CSI measurements. For example, reflections, attenuation, interference, or movement near the sensing area could shift the observed signal patterns.

In a fall detection pipeline, this could reduce sensing reliability or cause the extracted features to differ from those observed during normal training conditions.

### 2. Spoofed Signal Injection

A sensing system may be affected if external RF signals create patterns that resemble expected activity signatures. In a safety-critical context, spoofed or misleading wireless patterns could potentially interfere with reliable event detection.

This repository does not implement spoofing. This scenario is included only to motivate the need for robust sensing and anomaly-aware evaluation.

### 3. Synthetic CSI Perturbation

CSI-based machine learning pipelines may be sensitive to perturbations in amplitude, phase, or derived features. Synthetic perturbation studies can help evaluate how much signal change is required before a baseline classifier changes its prediction.

In this repository, any future perturbation examples should remain synthetic and educational, using simulated data only.

### 4. Adversarial Manipulation of Sensing Features

Machine learning models trained on CSI-derived features may be vulnerable to adversarial changes in the feature space. For example, changes in statistical features such as energy, peak-to-peak range, variance, or maximum amplitude could influence a classifier’s decision boundary.

This is conceptually related to adversarial examples in other ML domains, but here the focus is on wireless sensing and signal-derived features.

## Possible Safety Impacts

### 1. Missed Falls

A genuine fall event may be incorrectly classified as normal activity. In an eldercare setting, this could delay assistance or prevent an alert from being generated.

### 2. False Alarms

Normal activity may be incorrectly classified as a fall. Repeated false alarms can reduce trust in the system and contribute to caregiver alert fatigue.

### 3. Suppressed Alerts

A sensing pipeline may fail to generate an alert when one is needed. In safety-critical monitoring, this type of failure is especially important to study.

### 4. Time-to-Alarm Delay

Perturbed or degraded CSI measurements may delay correct classification, increasing the time between an event and a response.

## Current Repository Limitation

This repository currently demonstrates only synthetic concept-level examples. It does not validate real-world attack feasibility, clinical impact, or real deployment behavior.

All signals are simulated. No real patient data, clinical data, private data, or validated WiFi CSI measurements are included. No real adversarial attacks are implemented. The threat scenarios described here are theoretical and are intended only to frame the research motivation.

## Relationship to the Current Notebook

The current notebook demonstrates a simple synthetic workflow:

1. generate synthetic CSI-like signals,
2. simulate normal and fall-like classes,
3. apply basic preprocessing,
4. extract simple features,
5. train a baseline scikit-learn classifier,
6. evaluate results on synthetic data.

The notebook does not test real attacks or real healthcare sensing performance.

## Author

**Shahram H. Hesari**  
PhD Candidate, Electrical and Computer Engineering  
Portland State University
