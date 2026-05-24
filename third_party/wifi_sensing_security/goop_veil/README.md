# goop-veil — External Reference

## Repository Information

- **Name:** goop-veil
- **GitHub URL:** https://github.com/kobepaw/goop-veil
- **Upstream Description:** Software-only WiFi privacy defense: detect, degrade, and document potential CSI surveillance.
- **License:** Apache-2.0 (confirmed from upstream repository)
- **Category:** WiFi Sensing Security / Privacy Defense
- **Status:** External reference only — no code copied or adapted

---

## Purpose of This Folder

This folder is a tracking placeholder and attribution note for the `goop-veil` repository.
No source code, binaries, or dataset files from `goop-veil` have been copied into this repository.

---

## Relevance to This Project

`goop-veil` is relevant to this thesis project for the following reasons:

- **WiFi CSI Privacy Defense:** The repository implements a software-only WiFi privacy defense system targeting CSI-based surveillance. This directly connects to the thesis theme of adversarial threats to WiFi sensing and software-based mitigation strategies.
- **CSI-Based Surveillance Threat Awareness:** The project provides context for Wi-Spoof-style adversarial sensing threats, where an attacker uses CSI data to monitor individuals without consent — a key threat model in this thesis.
- **Router-Side Mitigation:** `goop-veil` focuses on router-side and firmware-level defense mechanisms (OpenWrt, Unifi, TP-Link platforms), offering a practical perspective on where privacy defenses can be deployed in WiFi sensing pipelines.
- **Software-Only Defense Framework Alignment:** The thesis explores software-based hardening of deep-learning WiFi sensing systems. `goop-veil` provides a reference point for adversarial defense design without hardware modification.
- **Privacy and Security Cross-Layer Context:** Relevant to the thesis goal of connecting physical-layer CSI attacks to clinical safety and privacy outcomes in elderly monitoring systems.

---

## Important Limitations

- This repository is **not** healthcare-specific. It focuses on general WiFi privacy defense.
- This repository has **not** been used in the current project implementation.
- The current project uses **synthetic CSI-like data only** and does not use live CSI collected with tools referenced by `goop-veil`.
- No dataset has been confirmed as associated with this repository. Dataset status: **Not confirmed / Pending verification**.

---

## License Status

- **Upstream License:** Apache-2.0 (verified from upstream `LICENSE` file)
- **Usage in This Project:** None — external reference only
- **Future Reuse:** Any future code reuse, adaptation, or derivative work requires review of the Apache-2.0 license terms and proper attribution to the original authors.

---

## Dataset Status

- **Dataset Availability:** Not confirmed
- **Notes:** `goop-veil` appears to operate on live/router-side CSI or WiFi privacy-defense workflows. No public recorded CSI dataset has been confirmed. A candidate entry has been added to `datasets/future_datasets/README.md` for future verification.

---

## Attribution

If any code or ideas from this repository are used in the future, proper attribution must be provided:

```
goop-veil by kobepaw
GitHub: https://github.com/kobepaw/goop-veil
License: Apache-2.0
```

---

*This README was created as part of the secure-wifi-csi-healthcare-sensing project's third-party reference tracking system.*
*Last updated: 2026-05-24*
