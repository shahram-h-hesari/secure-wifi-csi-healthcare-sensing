# Systematic Review Protocol

**Review Title:** Adversarial Robustness and Hardening of Deep Learning Wi-Fi Sensing for Healthcare Applications: A Systematic Review
**Protocol Version:** 0.1 (draft)
**Last Updated:** 2026-05-24
**Lead Reviewer:** Shahram H. Hesari (Portland State University)
**Status:** Planning phase — protocol not yet registered

> **Note:** This protocol is preparatory for a future systematic review paper. It is not yet registered with PROSPERO or any other registry. The scope may evolve as the PhD thesis develops.

---

## 1. Background and Rationale

Wi-Fi Channel State Information (CSI) sensing enables non-intrusive monitoring of vital signs and fall detection. This capability introduces privacy and adversarial attack risks, particularly in elderly home healthcare settings. No comprehensive systematic review of adversarial robustness and software-based hardening methods for deep learning Wi-Fi sensing in healthcare contexts has been identified. This review will fill that gap.

## 2. Review Questions

**Primary Question:**
What adversarial attacks and software-based defense methods have been proposed for deep learning-based Wi-Fi CSI sensing systems, and what is their applicability to healthcare monitoring contexts?

**Secondary Questions:**
1. What datasets and benchmarks exist for evaluating adversarial robustness in Wi-Fi CSI sensing?
2. What clinical safety metrics (e.g., false negative rates for fall detection, vital sign error rates) have been used to assess adversarial robustness?
3. What open-source code repositories support reproducibility of adversarial attack and defense experiments in this domain?
4. What gaps exist between adversarial ML research on Wi-Fi sensing and real-world healthcare deployment?

## 3. Scope

- **In scope:** Deep learning models for Wi-Fi CSI sensing; adversarial attacks on such models; software-based defenses; healthcare applications (vital signs, fall detection, activity recognition); reproducibility and open-source code availability
- **Out of scope:** Hardware-based defenses; non-Wi-Fi wireless sensing (UWB, radar, mmWave unless directly compared); non-healthcare applications unless methodology is transferable; proprietary systems with no accessible code or data

## 4. Search Strategy

See `search_queries.md` for full query strings.

**Databases to search:**
- IEEE Xplore
- ACM Digital Library
- arXiv (cs.CR, cs.LG, eess.SP)
- Google Scholar
- Semantic Scholar

**Search date range:** 2018–2026

## 5. Inclusion and Exclusion Criteria

See `inclusion_exclusion_criteria.md` for full criteria.

## 6. Screening Process

1. Title and abstract screening (independent review)
2. Full-text eligibility assessment
3. Data extraction
4. Quality assessment
5. Synthesis

See `prisma_tracking.csv` for screening records.

## 7. Data Extraction

For each included paper, extract:
- Paper ID, title, authors, year, venue
- Attack type (if applicable)
- Defense type (if applicable)
- Dataset used
- Evaluation metrics
- Open-source code availability
- Reproducibility status
- Clinical safety relevance
- Thesis chapter relevance

## 8. Quality Assessment

Quality will be assessed using a custom rubric adapted for adversarial ML papers:
- Reproducibility (code and data availability)
- Experimental validity (dataset quality, evaluation rigor)
- Relevance to healthcare context
- Clarity of threat model

## 9. Synthesis Plan

- Narrative synthesis of attack and defense taxonomies
- Reproducibility evidence table
- Gap analysis: open-source availability vs. claimed results
- Thesis-chapter evidence mapping (see `thesis_chapter_mapping.md`)

## 10. Planned Output

- Survey/systematic review paper (target venue: IEEE TIFS, IEEE Communications Surveys & Tutorials, or similar)
- Updated `papers.csv` and `reproducibility_matrix.md` as review progresses
- PRISMA-compatible screening log in `prisma_tracking.csv`

---

*This protocol is a living document. Update version and date with each significant revision.*
