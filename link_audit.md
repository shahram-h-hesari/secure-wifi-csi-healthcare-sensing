# Link Audit Report

**Repository:** secure-wifi-csi-healthcare-sensing
**Audit Date:** 2026-05-24
**Audited By:** Automated audit + manual verification

---

## Summary

| Status | Count |
|---|---|
| Verified (live, correct) | 2 |
| Fixed (bad URL replaced with verified URL) | 1 |
| Placeholder removed (repo not found) | 5 |
| Pending verification (DOI/URL unconfirmed) | 10 |
| No public code (no_confirmed_code category) | 5 |

---

## Verified Links

### `literature/paper_cards/with_public_code/attack_wifi_sensing.md`

| Field | Detail |
|---|---|
| Previous URL | `https://github.com/xdawnn/attack-wifi-sensing` (404 — not found) |
| Action | Replaced with verified URL |
| New URL | `https://github.com/Guolin-Yin/Attack_WiFi_Sensing` |
| Verification | Manually confirmed live on GitHub |

### `literature/paper_cards/with_public_code/sensefi.md`

| Field | Detail |
|---|---|
| URL | `https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark` |
| Status | Verified live on GitHub |
| DOI | `https://doi.org/10.1016/j.patter.2023.100764` (confirmed) |

---

## Placeholder Links Removed

### `literature/paper_cards/with_public_code/antieave_wifi_sensing.md`

| Field | Detail |
|---|---|
| Previous URL | `https://github.com/example/antieave` (placeholder) |
| Action | Removed; no verified public repo found |
| Status | No confirmed public code for AntiEave (Liu et al., INFOCOM 2023) |

### `literature/paper_cards/with_public_code/csigan.md`

| Field | Detail |
|---|---|
| Previous URL | `https://github.com/example/csigan` (placeholder) |
| Action | Removed; no verified public repo found |
| Status | No confirmed public code for CSI-GAN (Wang et al., IEEE Access 2022) |

### `literature/paper_cards/with_public_code/wifi_adg.md`

| Field | Detail |
|---|---|
| Previous URL | `https://github.com/example/wifi-adg` (placeholder) |
| Action | Removed; no verified public repo found |
| Status | No confirmed public code for WiFi-ADG (Zhang et al., GLOBECOM 2022) |

### `literature/papers.csv` (multiple rows)

| Field | Detail |
|---|---|
| Previous values | Multiple `.example` DOI/URL placeholders |
| Action | Replaced all with "Pending verification" |
| Affected rows | attack_wifi_sensing, antieave_wifi_sensing, wifi_adg, csigan, |
| | csi_bench, noisec, infocom_2023_wifi_ap, wicam_wicam2, |
| | wiintruder, awesome_ris_security, unilateral_csi_entropy |

---

## No Confirmed Public Code (no_confirmed_code)

| Paper ID | Status |
|---|---|
| infocom_2023_wifi_ap | No public code found; metadata pending verification |
| infocom_2023_wifi_apnea_attack | No public code found; metadata pending verification |
| wicam_wicam2 | No public code found; metadata pending verification |
| wiintruder | No public code found; metadata pending verification |
| csi_bench | No confirmed code; listed as future dataset candidate |

---

## Pending Verification

The following DOIs and links have not yet been verified from official
sources (IEEE Xplore, ACM DL, arXiv). They are stored as
"Pending verification" in paper cards and papers.csv.

| Paper ID | DOI / URL Status |
|---|---|
| attack_wifi_sensing | IEEE TIFS DOI pending |
| antieave_wifi_sensing | IEEE INFOCOM 2023 DOI pending |
| wifi_adg | IEEE GLOBECOM 2022 DOI pending |
| csigan | IEEE Access 2022 DOI pending |
| csi_bench | arXiv URL pending |
| noisec | ACM CCS DOI pending |
| infocom_2023_wifi_ap | IEEE INFOCOM 2023 DOI pending |
| infocom_2023_wifi_apnea_attack | IEEE INFOCOM 2023 DOI pending |
| wicam_wicam2 | ACM MobiSys 2021 DOI pending |
| wiintruder | IEEE SECON 2022 DOI pending |

---

## Remaining Actions

- Verify DOIs for all pending papers via IEEE Xplore and ACM DL.
- Search for confirmed public repos for AntiEave, CSI-GAN, WiFi-ADG.
- Confirm `infocom_2023_wifi_apnea_attack` full metadata from IEEE.
- Re-run audit after future additions to `literature/paper_cards/`.

## Notes

- All public code references are for citation and reproducibility
  tracking only.
- Placeholder URLs (`github.com/example/...`) have been removed to
  prevent use of non-existent links.
- All paper cards in `no_confirmed_code/` have been reformatted to the
  standard paper card format as of 2026-05-24.
- `papers.csv` column mismatch (csi_bench row) has been fixed.

**Last Updated:** 2026-05-24
