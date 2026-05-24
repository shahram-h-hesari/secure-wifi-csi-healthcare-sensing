# Third-Party References

This directory organizes related open-source work in WiFi sensing and WiFi sensing security that is referenced by this research repository.

---

## Purpose

Projects collected here serve the following research purposes:

- **Literature review**: Understanding the state of the art in WiFi-based sensing and security.
- **Technical comparison**: Evaluating different pipeline designs, signal processing approaches, and model architectures.
- **Reproducibility testing**: Running or inspecting third-party code to verify reported results.
- **Research inspiration**: Identifying gaps, limitations, and open problems that motivate this repository's direction.

---

## Structure

```
third_party/
├── wifi_sensing/          # WiFi CSI sensing, activity recognition, fall detection, and related applications
└── wifi_sensing_security/ # Adversarial attacks, CSI spoofing, privacy, and robustness evaluation
```

### wifi_sensing/

Contains references, submodule instructions, and review notes for WiFi CSI sensing projects (e.g., RuView). No third-party source code is copied directly into the main pipeline.

### wifi_sensing_security/

Tracks security-related repositories for future adversarial robustness evaluation. Currently referenced repositories include:

- **Attack_WiFi_Sensing** (https://github.com/Guolin-Yin/Attack_WiFi_Sensing): Adversarial evasion and robustness evaluation for WiFi sensing models.
- **Awesome-WS-Security** (https://github.com/Intelligent-Perception-Lab/Awesome-WS-Security): Curated literature on wireless sensing security.

> **Important:** Security-related repositories are tracked under `third_party/wifi_sensing_security/` **only after license review is completed**. No code from these repositories has been copied or adapted into this repository. They are referenced for literature review and future robustness evaluation planning only.

---

## License Policy

- All third-party code remains subject to its original license.
- No third-party code is relicensed under this repository's MIT License.
- Any code that is adapted or incorporated into the main pipeline will be clearly attributed with reference to the original source and license.
- Third-party projects are not part of the core fall-detection pipeline unless explicitly stated in the main README.

---

## Validation Disclaimer

Performance claims, accuracy figures, and system descriptions from third-party projects are not automatically treated as validated. Independent evaluation is required before any third-party results are cited as supporting evidence for this repository's claims.

See also: `THIRD_PARTY_NOTICES.md` at the repository root for the full attribution and license policy.
