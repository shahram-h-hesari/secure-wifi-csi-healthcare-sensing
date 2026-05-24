# WiFi-ADG — Third-Party Reference

> **Third-Party Notice:** This folder is a tracking placeholder and attribution note only.
> No source code from the WiFi-ADG repository has been copied, adapted, or vendored into this repository.
> Any future reuse requires a full license review and proper attribution.

---

## External Repository

- **Name:** WiFi-ADG
- **GitHub URL:** [https://github.com/siwangzhou/WiFi-ADG](https://github.com/siwangzhou/WiFi-ADG)
- **Author:** Siwang Zhou

---

## Associated Paper

- **Title:** Adversarial WiFi Sensing for Privacy Preservation of Human Behaviors
- **Venue:** IEEE Communications Letters
- **DOI:** [https://doi.org/10.1109/LCOMM.2019.2952844](https://doi.org/10.1109/LCOMM.2019.2952844)

---

## Reason for Tracking

This repository is tracked as an external reference relevant to the `wifi-csi-fall-detection` project for the following reasons:

- **Adversarial data generation:** Proposes adversarial CSI data generation (ADG) to prevent unauthorized behavior recognition from WiFi signals.
- **Privacy preservation:** Addresses privacy risks from WiFi-based human activity recognition by modifying CSI signals to obfuscate behavior.
- **CSI privacy / behavior obfuscation:** Directly relevant to the privacy and security threat model for WiFi sensing systems.
- **Adversarial WiFi sensing:** Provides methodology for generating adversarial perturbations in the WiFi CSI domain to preserve user privacy.

---

## Relevance to This Repository

| Topic | Relevance |
|-------|-----------|
| WiFi sensing security | High — adversarial CSI modification directly applicable |
| CSI privacy | High — privacy preservation of sensing behaviors |
| Adversarial data generation | High — adversarial perturbation techniques relevant to robustness work |
| Behavior obfuscation | High — countermeasure design against unauthorized inference |
| Activity recognition | Medium — context for the privacy attack surface |
| Fall detection | Indirect — understanding adversarial obfuscation in sensing robustness context |

---

## License Status

*Pending verification* — License type has not been confirmed. Any future use of code, models, or data from this repository requires a full license review.

---

## Usage Policy in This Repository

- This folder contains only this README tracking file.
- No code has been copied or adapted from WiFi-ADG.
- No models or datasets from WiFi-ADG have been integrated into the pipeline.
- This folder serves as a literature review reference and reproducibility planning note.
- Future integration (if any) requires explicit license verification and attribution.

---

## Dataset

The WiFi-ADG repository references nine datasets: `data0.mat` through `data7.mat` and `resdata.mat`.
The upstream README provides a Baidu download link for these datasets.
This dataset is cataloged separately in `datasets/wifi-adg/` with full provenance notes.
Dataset files are not downloaded or stored in this repository.

---

## Last Updated

*Pending — to be updated upon license verification or integration planning*
