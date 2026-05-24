# SenseFi / WiFi CSI Sensing Benchmark

> **Third-Party Notice:** SenseFi / WiFi CSI Sensing Benchmark is an external open-source project. It is not part of the original work in this repository. All code, claims, and results remain attributed to the original authors at https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark.

---

## Source

- **Original Repository:** https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark
- **Original Authors:** xyanchen and contributors
- **License:** To be verified before any code use
- **Also known as:** SenseFi benchmark

---

## Category

WiFi CSI sensing benchmark — deep-learning-based WiFi CSI human sensing evaluation framework.

---

## Why This Project Is Included

SenseFi / WiFi CSI Sensing Benchmark is included in this repository as a **third-party open-source external reference** for the following research purposes:

1. Reviewing benchmark methodology for deep-learning-based WiFi CSI human sensing
2. Understanding evaluation protocols and dataset splits used in the community
3. Identifying potential victim models for future adversarial robustness evaluation
4. Literature context for comparing approaches in WiFi CSI activity and fall detection
5. Planning future baseline comparisons for robustness and attack evaluation

This project is **not** presented as original work and is **not** independently validated within this repository.

---

## Relationship to This Repository

This repository (`wifi-csi-fall-detection`) is a WiFi CSI fall-detection research prototype that uses **synthetic CSI-like data only**. SenseFi is an external benchmark framework that uses real WiFi CSI datasets.

| This Repository | SenseFi (Third-Party) |
|---|---|
| `src/` — original pipeline code | `third_party/wifi_sensing/sensefi/` — documentation only |
| Synthetic CSI-like data | Real WiFi CSI datasets |
| Offline research prototype | Published benchmark framework |
| My original research work | Third-party reference |

---

## Current Use

- **Documentation and reference review only** at this time
- No SenseFi code has been copied, adapted, or mixed with the original `src/`, `notebooks/`, or `app.py` code in this repository
- Any future code reuse requires **license review and proper attribution**
- No Git submodule has been added; this folder serves as a placeholder and reference note only

---

## Validation Status

> **Important:** SenseFi's benchmark results and performance claims are **not independently validated** in this repository. All performance, accuracy, or capability claims in SenseFi's documentation represent the original authors' claims and have not been reproduced or verified here.

---

## License and Attribution

- The license of this repository has not yet been independently verified for this entry.
- **No source code has been copied or adapted from SenseFi into this project.**
- Any future code reuse requires: (1) verifying the original license, (2) preserving the original license text, and (3) adding proper attribution in the relevant source files and `THIRD_PARTY_NOTICES.md`.
- See the repository root `THIRD_PARTY_NOTICES.md` for the full attribution and license policy.

---

*This file was created as part of the wifi-csi-fall-detection research prototype repository to track external WiFi sensing references.*
