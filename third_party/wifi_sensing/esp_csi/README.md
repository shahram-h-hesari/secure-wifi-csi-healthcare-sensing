# ESP-CSI

> **Third-Party Notice:** ESP-CSI is an external open-source project maintained by Espressif Systems. It is not part of the original work in this repository. All code, claims, and results remain attributed to the original authors at https://github.com/espressif/esp-csi.

---

## Source

- **Original Repository:** https://github.com/espressif/esp-csi
- **Original Authors:** Espressif Systems and contributors
- **License:** To be verified before any code use (likely Apache 2.0 or similar; check original repository)
- **Maintained by:** Espressif Systems (makers of ESP32)

---

## Category

WiFi CSI collection and hardware — ESP32-based CSI extraction, wireless sensing examples, and real hardware prototyping.

---

## Why This Project Is Included

ESP-CSI is included in this repository as a **third-party open-source external reference** for the following research purposes:

1. Understanding real CSI collection workflows using commodity WiFi hardware (ESP32)
2. Reviewing hardware-level CSI extraction methods for future real-data experiments
3. Planning future prototyping and real CSI data collection for adversarial evaluation
4. Literature context for comparing synthetic CSI-like simulation to real hardware acquisition
5. Reference for future integration when moving beyond synthetic CSI-like data

This project is **not** presented as original work and is **not** independently validated within this repository.

---

## Relationship to This Repository

This repository (`wifi-csi-fall-detection`) is a WiFi CSI fall-detection research prototype that uses **synthetic CSI-like data only**. ESP-CSI provides tools for real CSI collection from ESP32 hardware.

| This Repository | ESP-CSI (Third-Party) |
|---|---|
| `src/` — original pipeline code | `third_party/wifi_sensing/esp_csi/` — documentation only |
| Synthetic CSI-like data | Real WiFi CSI from ESP32 hardware |
| Offline research prototype | Hardware-based real CSI collection |
| My original research work | Third-party reference |

---

## Current Use

- **Documentation and reference review only** at this time
- No ESP-CSI code has been copied, adapted, or mixed with the original `src/`, `notebooks/`, or `app.py` code in this repository
- Any future code reuse requires **license review and proper attribution**
- No Git submodule has been added; this folder serves as a placeholder and reference note only

---

## Validation Status

> **Important:** ESP-CSI's examples and results are **not independently validated** in this repository. All performance, accuracy, or capability claims in ESP-CSI's documentation represent the original authors' claims and have not been reproduced or verified here.

---

## License and Attribution

- The license of this repository must be verified independently before any code reuse.
- **No source code has been copied or adapted from ESP-CSI into this project.**
- Any future code reuse requires: (1) verifying the original license, (2) preserving the original license text, and (3) adding proper attribution in the relevant source files and `THIRD_PARTY_NOTICES.md`.
- See the repository root `THIRD_PARTY_NOTICES.md` for the full attribution and license policy.

---

*This file was created as part of the wifi-csi-fall-detection research prototype repository to track external WiFi CSI hardware and collection references.*
