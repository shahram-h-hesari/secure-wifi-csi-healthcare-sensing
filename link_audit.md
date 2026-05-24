# Link Audit Report

**Repository:** secure-wifi-csi-healthcare-sensing
**Audit Date:** 2026-05-24
**Audited By:** Automated audit + manual verification

---

## Summary

| Status | Count |
|---|---|
| Verified (live, correct) | 1 |
| Fixed (bad URL replaced with verified URL) | 1 |
| Placeholder removed (repo not found) | 3 |
| No issues | 1 |

---

## Detailed Findings

### `literature/paper_cards/with_public_code/attack_wifi_sensing.md`

| Field | Detail |
|---|---|
| Previous URL | `https://github.com/xdawnn/attack-wifi-sensing` (404 — repo not found) |
| Action | Replaced with verified URL |
| New URL | `https://github.com/Guolin-Yin/Attack_WiFi_Sensing` |
| Verification | Manually confirmed live on GitHub |
| Commit | Fix: replace bad Public Code URL in attack_wifi_sensing.md with verified repo |

---

### `literature/paper_cards/with_public_code/antieave_wifi_sensing.md`

| Field | Detail |
|---|---|
| Previous URL | `https://github.com/example/antieave` (placeholder) |
| Action | Placeholder removed; marked as not found |
| New Value | Not found — pending verification (placeholder removed) |
| Note | No verified public code repo located for AntiEave (Liu et al., IEEE INFOCOM 2023) |
| Commit | Fix: remove placeholder URLs from antieave_wifi_sensing.md |

---

### `literature/paper_cards/with_public_code/csigan.md`

| Field | Detail |
|---|---|
| Previous URL | `https://github.com/example/csigan` (placeholder) |
| Action | Placeholder removed; marked as not found |
| New Value | Not found — pending verification (placeholder removed) |
| Note | No verified public code repo located for CSI-GAN (Wang et al., IEEE Access 2022) |
| Commit | Fix: remove placeholder URLs from csigan.md |

---

### `literature/paper_cards/with_public_code/wifi_adg.md`

| Field | Detail |
|---|---|
| Previous URL | `https://github.com/example/wifi-adg` (placeholder) |
| Action | Placeholder removed; marked as not found |
| New Value | Not found — pending verification (placeholder removed) |
| Note | No verified public code repo located for WiFi-ADG (Zhang et al., IEEE GLOBECOM 2022) |
| Commit | Fix: remove placeholder URLs from wifi_adg.md |

---

### `literature/paper_cards/with_public_code/sensefi.md`

| Field | Detail |
|---|---|
| URL | `https://github.com/xyanchen/WiFi-CSI-Sensing-Benchmark` |
| Action | No change required |
| Status | URL appears valid — no placeholder detected |

---

## Remaining Actions

- [ ] Locate verified public code repos for AntiEave (Liu et al. 2023), CSI-GAN (Wang et al. 2022), and WiFi-ADG (Zhang et al. 2022)
- [ ] Update respective paper cards once repos are confirmed
- [ ] Re-run audit after any future additions to `literature/paper_cards/`

---

## Notes

- No PDFs, datasets, or third-party code files are stored in this repository.
- All public code references are for citation and reproducibility tracking only.
- Placeholder URLs (`github.com/example/...`) have been fully removed to prevent accidental use of non-existent links.
