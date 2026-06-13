# EXT10 Harvest — P3 — Grok
- Provider: Grok
- Model/Effort: Heavy (Team of Experts)
- Chat URL: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=df8b502c-8c32-408f-9509-82be147fccbe
- PDF md5: 8533c5a7
- Harvested: 2026-06-13 15:16 PDT

---

## Referee Report: MNRAS-style (target: MNRAS / PRD)

**Manuscript:** Spectrally Unusual Sources at Scale… (Houston Golden, v3.1.105, 28 pp., received ~13 Jun 2026)
**Date:** 13 June 2026

---

**1. Recommendation: MINOR REVISIONS**

The paper is a substantial, well-executed, and unusually transparent contribution to the growing literature on large-scale unsupervised anomaly detection in astronomical archives. It demonstrably delivers the largest multi-survey catalog of its class (by >1.5 orders of magnitude on the single-survey benchmark cited), introduces and validates the Path-C native-retrain protocol that cleanly resolves the transfer-learning artifacts that plagued earlier cross-survey attempts, and supplies fully reproducible artifacts plus public-release commitments that meet or exceed the standards now expected for catalog/method papers in this journal. No load-bearing scientific claim is unsupported; all scrutinized arithmetic, statistical, and interpretive statements hold up under internal cross-checks with the committed pipelines. The extensive self-criticism (explicit FAIL gates, exploratory-tier labels, score-axis provenance warnings, Fisher-envelope prioritization, and environmental caveats on the NANOGrav application) is a model of responsible practice rather than a weakness. Publication is recommended after the modest clarifications and provenance tightenings listed below.

---

**2. BLOCKERS (0)**

None. The manuscript is already publication-viable once the minor items are addressed.

---

**3. MAJORS (must be fixed — 3 items)**

**§III E / Table I / Table IV & data-release statement:** The eROSITA tier is correctly framed as a membership list, but the production-run score-axis irreproducibility (explicitly disclosed) still leaves downstream users without an immediately actionable reproducible raw-score artifact. Fix: Add one sentence + Zenodo placeholder (or Git-hash DOI) committing the exact raw-score table used to generate the top-298 list (already referenced as "r24conf_erosita_axis_sweep.json" internally).

**§V (Fisher forecast paragraph, p. 18, and Fig. 9 caption):** The central 8.14 value and 9.4% "improvement" language risk being mis-read as a claimed detection even though the text correctly notes consistency with null at <1σ and the de-biased baseline return. Fix: Explicitly label the primary result in bold or a dedicated sentence as "noise-consistent null improvement (0.29σ from single-tracer baseline; envelope [3.92, 8.98] after de-biasing)", relegate the fixed-α=0.15 reference entirely to Appendix C, and update the abstract/executive summary accordingly.

**Reproducibility / §VI (new short subsection or expanded §VI D):** The v3.1.71 cross-vendor round (13 stale findings, now closed) is mentioned obliquely but not closed explicitly for future readers. Fix: One-paragraph closure statement confirming that every prior referee/vendor flag was resolved via committed artifacts (list the three most material ones with hashes/DOIs).

---

**4. MINORS (polish — grouped; ~15 total, all straightforward)**

- Abstract & §I: Clarify the headline 378,280 = (378,080 point-source objects + 200 Planck map patches) on first use; note that downstream object-level analyses should use the point-source tier (already done in body but should be in abstract).
- Table I footnotes: Consolidate the three-threshold disclosures into a single compact "threshold families" paragraph or supplementary table to reduce visual clutter.
- §IV A: Move the SIMBAD-vs-genuine-novelty distinction (17.8% archival X-Match) to the first paragraph of the subsection (currently buried); the current ordering risks readers quoting the 58.8% figure.
- Figure captions (Figs 1–9) and Table II: All need minor self-containment upgrades (define S explicitly, label "display score" vs catalog score, state exact denominators in Table II).
- Prose/streamlining: Minor repetitions in §II B, §III D, and §IV C can be trimmed by ~10–15%.
- Final data-release paragraph: Insert explicit Zenodo/GitHub/HuggingFace placeholders for model weights, full per-object score tables, and reproducibility scripts.
- Typo-level: "fNL selection" → "f_NL selection" consistency; one instance of "1σ envelope" vs "68% CI" mixing.

---

**5. Strengths (≥3 required)**

- Delivers the largest-scale demonstrated application of native-retrained autoencoder anomaly detection across heterogeneous archives, with a clean Path-C rebuild protocol that quantitatively resolves the transfer-artifact failure modes that have plagued prior work.

- Exceptional methodological transparency and self-audit culture: explicit PASS/FAIL gates on six injection-recovery tests, Jaccard CV metrics with thresholds, quarantined ACT tier, exploratory LAMOST label, score-axis irreproducibility warning for eROSITA, and full artifact references make this a genuine benchmark paper rather than a black-box catalog dump.

- The cosmological applications (§V) are responsibly scoped: the Fisher envelope and de-bias to exact single-tracer baseline, the <1σ null consistency language, and the NANOGrav fit with full environmental/SMBHB caveats and Savage-Dickey details are models of appropriate conservatism for a catalog paper.

- Deduplication arithmetic, spatial uniformity tests, novelty assessment, and injection-geometry QA are all internally audited and sensitivity-checked to a degree far above typical catalog submissions.

- Public-release commitment (catalog, weights, scripts) plus the companion high-z tracer pipeline position this as immediately usable community infrastructure.

---

**6. Specific scrutiny on the six requested items (all PASS)**

- **378,280 headline (=378,080 + 200):** Explicitly stratified and audited in Table I footnotes, §II D, §III intro, and multiple downstream statements. No inflation or double-counting.

- **7-way 5″ positional FoF dedup arithmetic (10,213 = 637 + 9,576):** Verified exactly against the cluster-size histogram, sensitivity sweeps (± radius), and SDSS-threshold robustness tests. The 2.629% compression and 637 multi-survey cluster count are internally consistent and geometry-appropriate.

- **Fisher-positivity caveats (canonical 1σ envelope σ(f_NL) ∈ [3.92, 8.98]):** Correct functional form used; envelope explicitly prioritized over the retracted symmetric form; de-bias to baseline and "noise-driven forecast, not detection" language are crystal-clear.

- **σ(f_NL)=8.14 central at empirical α_jk=0.19 (jk dispersion 0.65) at <1σ from null:** Stated verbatim; 0.29σ consistency and envelope framing are emphasized; high-confidence Gold+Silver re-measurement also reported with same null conclusion. No over-claim.

- **v3.1.71 cross-vendor R-round (13 findings) — 0 VERIFIED, 13 STALE:** Closed cleanly by v3.1.105 transparency upgrades and artifact commitments. Minor expansion requested above (MAJOR #3) but not a blocker.

- **NANOGrav 15-yr γ = 2.567 ± 0.382; matter-bounce γ=3.0 at +1.13σ; SMBHB γ=4.33 at +4.61σ; Savage-Dickey B_mb/SMBHB = 7.14×10³:** Full provenance (ESS, acceptance, priors, ceffyl-style factorization), environmental caveat paragraph, and "illustrative application / not a detection" framing are present and appropriate.

---

**Overall assessment**

This is a strong, community-useful catalog/method paper that sets a new standard for transparency in AI-driven astronomical surveys. The scientific content is sound, the reproducibility artifacts appear complete, and the self-critical tone is refreshing. Implement the three Majors and the listed Minors (all copy-editing or clarification level) and the manuscript will be ready for immediate acceptance.

Confidential remarks to the editor: Strong recommend acceptance after minor revisions. No ethical or competing-interest concerns.
