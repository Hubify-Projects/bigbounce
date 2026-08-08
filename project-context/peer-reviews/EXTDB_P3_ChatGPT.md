# EXTDB P3 ChatGPT — chat: https://chatgpt.com/c/6a3f84dc-9698-83e8-9115-77c46ee2a004

Provider: ChatGPT
Model/Tier: Instant (fast, gpt-4o)
PDF: /tmp/EXTDB_P3.pdf
Submitted: 2026-06-27
Harvested: 2026-06-27
Round: EXTDB (DE-BIASED)

---

Referee Report (MNRAS / PRD / JCAP)

1. Recommendation
MAJOR REVISIONS

The paper is ambitious and unusually transparent, but not yet acceptable at MNRAS/PRD/JCAP bar because several headline catalog claims depend on heterogeneous, partly exploratory tiers, non-uniform thresholds, unreproducible score axes, and incomplete validation. The authors disclose many of these issues, but disclosure does not fully cure their effect on the headline framing.

2. BLOCKERS

B1 — Headline catalog size conflates validated and exploratory products.
The abstract/headline emphasizes 378,280 Path-C unique anomalies, but the paper itself says LAMOST is exploratory, Gaia fails stability/injection checks, eROSITA is membership-only with irreproducible score axis, and Planck is map patches rather than point sources. Fix: make the primary headline the robust tier only, with exploratory tiers separate.

B2 — DESI "73×" scale claim is not like-for-like.
The paper states DESI-only is ~73× the Liang et al. benchmark, while its own science-class recount gives only 2,468 science-target anomalies, about 0.9× the benchmark. This is acknowledged, but the favorable number remains prominent. Fix: remove or demote the 73× claim from headline/abstract.

B3 — eROSITA score axis is unreproducible.
A catalog component with no reproducible per-object score axis cannot support score-based downstream analysis. Fix: release eROSITA strictly as an exploratory membership list and exclude it from catalog-grade counts unless score provenance is restored.

B4 — Validation gates are heterogeneous and partly not detector-sensitivity tests.
NEOWISE "100% recovery" is a mask-geometry QA pass by construction, not anomaly-detector recovery. DESI lacks injection-recovery; LAMOST/Gaia/eROSITA fail relevant gates. Fix: define separate validation classes and avoid aggregating them as equivalent "passes."

3. MAJORS

M1 — Non-uniform thresholds undermine cross-survey rate interpretation.
DESI uses S>5, SDSS uses a fixed-size continuity slice, LAMOST/Gaia use top-percentile cuts, Planck/NEOWISE fixed top-1%, and eROSITA fixed top-298. The catalog is still useful, but the total "rate" is bookkeeping, not a measured anomaly frequency.

M2 — DESI anomaly population is dominated by non-primary science spectra.
The finding that ~98.7% of DESI anomaly clusters are not primary science-class targets is scientifically important and should be central, not caveated after headline scale claims.

M3 — Full-catalog novelty is not established.
The valid novelty estimate is 17.8% for DESI top-1,000 only. The paper should not let SIMBAD-unmatched rates or broader catalog language imply discovery rates beyond that stratum.

M4 — Cosmology applications are over-attached to a catalog paper.
The fNL and NANOGrav sections are careful but distract from the catalog validation burden. The empirical multi-tracer result is consistent with no improvement; NANOGrav is model-illustrative and not catalog-derived in a strong sense. Move to appendix or sharply shorten.

M5 — Single-architecture dependence remains a major limitation.
DESI, SDSS, and LAMOST lack independent architecture confirmation. For a catalog-grade anomaly product, at least the primary DESI tier should have an independent detector or robust ablation.

4. MINORS

m1 — The abstract is overloaded and reads like a correction log.
It contains many caveats but buries the actual clean result.

m2 — "Largest" claim needs tighter wording.
Use "largest by sources processed under this specific framework, to our knowledge," and keep benchmark caveats adjacent.

m3 — Figure 2 is cross-transfer baseline, not Path-C catalog.
This risks visual mismatch with the headline result. Add a Path-C map or demote Fig. 2.

m4 — SDSS terminology is confusing.
The paper alternates between cross-transfer, native re-score, top-1%, continuity slice, and strict S>5. Add a compact table of which SDSS set is used for each analysis.

m5 — Public release language should be finalized.
"Will be publicly released" and DOI placeholders are acceptable pre-arXiv, but journal review should require persistent identifiers before acceptance.

5. Strengths

1. The paper is unusually transparent about failure modes, especially LAMOST, eROSITA, ACT, and DESI target-class recounts.
2. The Path-C native-retrain framework is a real methodological improvement over naive cross-transfer anomaly detection.
3. The DESI stability checks are substantive: 5-fold Jaccard and OOD production-vs-control Jaccard are meaningful robustness evidence.
4. The catalog, even after caveats, is potentially valuable as a triaged discovery/follow-up resource.
5. The paper's distinction between SIMBAD absence and genuine archival novelty is scientifically responsible.
