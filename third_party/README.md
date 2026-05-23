# Third-Party References

This directory organizes related open-source work in WiFi sensing and WiFi sensing security that is referenced by this research repository.

## Purpose

Projects collected here serve the following research purposes:

- **Literature review**: Understanding the state of the art in WiFi-based sensing and security.
- **Technical comparison**: Evaluating different pipeline designs, signal processing approaches, and model architectures.
- **Reproducibility testing**: Running or inspecting third-party code to verify reported results.
- **Research inspiration**: Identifying gaps, limitations, and open problems that motivate this repository's direction.

## Structure

```
third_party/
├── wifi_sensing/          # WiFi CSI sensing, activity recognition, fall detection, and related applications
└── wifi_sensing_security/ # Adversarial attacks, CSI spoofing, privacy, and robustness evaluation
```

## License Policy

- All third-party code remains subject to its original license.
- No third-party code is relicensed under this repository's MIT License.
- Any code that is adapted or incorporated into the main pipeline will be clearly attributed with reference to the original source and license.
- Third-party projects are not part of the core fall-detection pipeline unless explicitly stated in the main README.

## Validation Disclaimer

Performance claims, accuracy figures, and system descriptions from third-party projects are not automatically treated as validated. Independent evaluation is required before any third-party results are cited as supporting evidence for this repository's claims.

---

*See also: [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) at the repository root for the full attribution and license policy.*
