# Search Queries

**Project:** Secure WiFi CSI Healthcare Sensing — Systematic Review
**Last Updated:** 2026-05-24
**Status:** Draft v0.1

---

## Databases

| Database | URL | Access |
|---|---|---|
| IEEE Xplore | https://ieeexplore.ieee.org | Institutional |
| ACM Digital Library | https://dl.acm.org | Institutional |
| arXiv | https://arxiv.org | Open |
| Google Scholar | https://scholar.google.com | Open |
| Semantic Scholar | https://www.semanticscholar.org | Open |

---

## Primary Query Strings

### Query Set A: Core Domain + Adversarial

```
("WiFi" OR "Wi-Fi" OR "CSI" OR "channel state information") AND
("adversarial" OR "attack" OR "perturbation" OR "evasion") AND
("deep learning" OR "neural network" OR "CNN" OR "LSTM") AND
("sensing" OR "monitoring" OR "detection" OR "recognition")
```

### Query Set B: Healthcare Context

```
("WiFi" OR "Wi-Fi" OR "CSI") AND
("vital sign" OR "respiration" OR "heart rate" OR "fall detection" OR "activity recognition") AND
("adversarial" OR "robustness" OR "privacy" OR "security")
```

### Query Set C: Defense Methods

```
("WiFi" OR "Wi-Fi" OR "CSI" OR "channel state information") AND
("adversarial training" OR "input transformation" OR "noise injection" OR "certified defense" OR "adversarial purification") AND
("sensing" OR "monitoring")
```

### Query Set D: Reproducibility and Open Source

```
("WiFi" OR "Wi-Fi" OR "CSI") AND
("benchmark" OR "dataset" OR "open source" OR "public code" OR "reproducibility") AND
("adversarial" OR "attack" OR "robustness" OR "defense")
```

### Query Set E: Clinical Safety Metrics

```
("WiFi" OR "Wi-Fi" OR "CSI" OR "wireless sensing") AND
("false negative" OR "false alarm" OR "miss detection" OR "safety-critical" OR "clinical") AND
("adversarial" OR "attack" OR "robustness")
```

---

## Supplementary Queries (Manual / Forward-Backward Citation)

- Cited-by search on key papers: `attack_wifi_sensing`, `sensefi`, `antieave_wifi_sensing`
- Keyword search on arXiv: `cs.CR WiFi CSI adversarial`, `eess.SP WiFi sensing robustness`
- GitHub search: `WiFi CSI adversarial attack`, `WiFi sensing defense`

---

## Search Execution Log

| Date | Database | Query Set | Results Retrieved | Screened | Notes |
|---|---|---|---|---|---|
| 2026-05-24 | Manual / seed | A, B, C, D | 12 (seed papers) | 12 | Initial seed from project context; formal search not yet executed |

---

*Update this file each time a formal search is executed. Record exact query strings, dates, and result counts for PRISMA compliance.*
