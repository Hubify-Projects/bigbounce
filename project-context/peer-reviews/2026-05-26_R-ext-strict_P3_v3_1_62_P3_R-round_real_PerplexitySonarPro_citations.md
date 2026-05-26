# P3 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-strict_P3_v3_1_62
**Wall time**: 23.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=68391, completion=1224, total=69615

---

## PAPER-PER-B1 — BLOCKER — Extensive audit-trail/meta-review prose inside manuscript body

The title page and preamble contain many paragraphs of version-history, AI-vendor, and “R-round” audit notes (e.g. “R15 5‑vendor on v3.1.53”, “GRO-B1 BLOCKER”, “Gemini argues…”, “next pod-pull cycle”), which is completely inappropriate for an MNRAS/PRD/JCAP research article body. These are internal workflow logs, not scientific content, and would be rejected on style/ethics grounds.  

Fix: Strip all AI-vendor names, version-history commentary, “BLOCKER/MAJOR” language, “R-round” descriptions, and “truth‑audit” notes from the TeX file, moving at most a single neutral “changes since vX” paragraph into a non-public change log on arXiv, not into the journal manuscript.

---

## PAPER-PER-B2 — BLOCKER — Mis-cited/ambiguous SPHEREx and Heinrich references

The text cites “SPHEREx satellite [SPHEREx2014]” and “Heinrich et al. [Heinrich2023] (anchored to the Heinrich+2024 σ_fNL ≈ 0.7 bispectrum-only forecast)” but the bibliography only lists the 2014 SPHEREx overview white paper and a single Heinrich et al. paper; no “Heinrich+2024 σ_fNL ≈ 0.7” publication is identifiable as a distinct work.   

Fix: (i) Make clear which concrete Heinrich et al. paper you mean (year, journal, arXiv ID) and ensure the bib entry matches a real published/arXiv paper; (ii) if “Heinrich+2024 σ_fNL ≈ 0.7” is an internal computation or conference note rather than a citable paper, rephrase as “following the private forecast of Heinrich et al. (in prep.)” or remove it from the citation chain, and do not imply a published “headline external benchmark” if none exists.

---

## PAPER-PER-M1 — MAJOR — Over-strong language about “largest” / “first multi-survey” vs. cited prior work

The abstract and introduction make strong claims like “largest-scale application… to date” and “first multi-survey anomaly detection campaign,” comparing to Liang et al. (2023) on DESI EDR but not surveying other contemporary multi-survey anomaly catalog efforts (e.g. other DESI BGS / Milky Way survey analyses or cross-survey machine-learning work).   

Fix: Soften all “largest/first” claims to explicitly scoped statements (“to our knowledge, within DESI-based spectroscopic anomaly catalogs…”), and ensure that Liang et al. (2023) and any other directly comparable efforts are described accurately as single-survey baselines rather than implicitly ruled out.

---

## PAPER-PER-M2 — MAJOR — Overstated cosmology “closure” given internal Fisher caveats

The cosmology sections repeatedly talk about “closing the prior deferral” and quote specific σ(f_NL) improvements while simultaneously admitting that systematics (photo‑z, fiber assignment, GR projection, nuisance-parameter Fisher block, etc.) are not fully marginalized and that a previous asymmetric Fisher interval was “hallucinated.” This is inconsistent with MNRAS/JCAP standards for a robust cosmological constraint.  

Fix: Reframe the cosmology discussion as exploratory sensitivity estimates only: (i) remove language like “therefore closes the prior deferral” and “load-bearing constraint”; (ii) clearly state once, early, that no joint nuisance‑marginalized model fit is performed and that numbers quoted are upper-limit Fisher sensitivities; (iii) move any detailed “Wave 14-X” internal pipeline descriptions and corrections to an appendix, with the main text giving only a conservative, systematically caveated forecast.

---

## PAPER-PER-M3 — MAJOR — Confusing use of internal labels as if they were external literature (Heinrich+2024, Wave 14‑VVV, etc.)

Throughout the cosmology and methods sections, internal pipeline labels (e.g. “Wave 14‑VVV”, “Wave 14‑II Fisher systematics”, “Wave 14‑KKKK”) and shorthand like “Heinrich+2024” are written in the same style as external literature citations, which makes it impossible for a reader or referee to trace these to published sources.   

Fix: Distinguish clearly between (a) published work (with standard citations) and (b) internal pipeline runs or in‑prep work (clearly marked as such, with no implication of peer‑reviewed status). Replace “Heinrich+2024 σ_fNL ≈ 0.7 as headline external benchmark” with a specific, published reference or remove the “headline” language if the benchmark is not yet in the literature.

---

## PAPER-PER-m1 — minor — Incomplete bibliographic detail and missing arXiv IDs in several key references

Several important references (e.g. “Nicolaou et al. 2026”, “DESI DR1 2025”, “SPHEREx2014” white paper) are cited with informal labels or year-only descriptions without clear journal venue or arXiv identifier, making citation-chain verification difficult.   

Fix: For every citation that underpins a quantitative or methodological claim (especially DESI DR1, LAMOST DR10, SDSS DR18, SPHEREx, Nicolaou et al.), ensure the bib entry includes full author list, year, title, journal, and arXiv ID where applicable, and that the in-text label matches that real paper exactly.
