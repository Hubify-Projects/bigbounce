# P4 2026-06-04_R4fixed — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 111.0s

---

## Referee Report for PAPER P4

### ESSENTIAL Revisions

- **P4-E1 (Abstract, p1)**  
  Problem: Headline figure "99.3%/12%/88%/25%" decomposition lacks provenance and arithmetic consistency. The text claims monopole-only null reproduces 99.3% of pre-MASTER pseudo-Cℓ, post-MASTER residual is 88%, and 12% is attributed to monopole leakage, but 99.3% + 12% ≠ 100%. No JSON/script cited for these percentages.  
  Fix: Provide script (e.g., `pipelines/p2_chirality/outputs/canonical_provenance/master_decoupled_monopole_null.json`) in main text. Reconcile decomposition math: 99.3% (pre-MASTER leakage) and 12% (post-MASTER leakage) are not additive components; clarify they refer to separate stages.

- **P4-E2 (Abstract, p1; Conclusions, p45)**  
  Problem: σ values from different null procedures presented without qualification: −0.12σ (MASTER label-shuffle null) vs. +0.43σ (per-pixel-shuffle null) vs. +3.64σ (binomial monopole null). Abstract note (p1) warns they are incomparable, but Conclusions (p45) juxtaposes them without restating this.  
  Fix: Add explicit disclaimer in Conclusions when comparing σ values. Cite Table II (null mappings) in abstract/conclusions.

- **P4-E3 (Throughout)**  
  Problem: Version-history artifacts in body prose: "R4: date version string fixed", "wave14 labels removed", and internal paths like `pipelines/p2_chirality/r42_results/B20_B21_results.json`.  
  Fix: Remove all versioning tags and internal audit paths. Replace with immutable dataset/script references (e.g., HuggingFace `paper4-v1.0.154`).

- **P4-E4 (Abstract, p1)**  
  Problem: Duplicate phrase "canonical canonical-mask" (e.g., "canonical canonical-mask residual").  
  Fix: Replace with "canonical mask residual".

- **P4-E5 (Sec. IV.C, p18; Table VI)**  
  Problem: Central result −0.12σ (MASTER ℓ=1) lacks direct script provenance. Footnote references `master_power_spectrum.json` but buries it in auxiliary text.  
  Fix: Explicitly cite script in main results: "MASTER deconvolution performed via [script] yielding Cℓ=1 = [value]".

- **P4-E6 (Sec. VI.C, p36; Table XVI)**  
  Problem: Empirical 50%-recovery-3σ threshold (0.75%) is load-bearing for falsification criterion but cited via buried JSON (`wave_14_nn_injection_recovery.json`).  
  Fix: Directly reference script and dataset in main text/Sec. VI.C.

---

### MAJOR Revisions

- **P4-M1 (Sec. IV.B, p15; Table V)**  
  Problem: Global CW fraction (0.4974 ± 0.000279, 9.5σ from parity) attributed to GZ1 training bias without rigorous proof. Independent verification (e.g., SpArcFiRe cross-check) is deferred.  
  Fix: Strengthen evidence or rephrase as hypothesis. Remove "demonstrably" from conclusions (p45).

- **P4-M2 (Sec. VI.C, p36)**  
  Problem: Empirical sensitivity threshold (0.75%) conflicts with Fisher floor (0.29%). Justification ("systematics-inclusive") is vague; no quantitative error model links dilution factor (0.63) to threshold.  
  Fix: Derive empirical threshold formally from classifier error rates or drop Fisher comparison.

- **P4-M3 (Sec. IV.D, p21; Table VII)**  
  Problem: Hemisphere max-asymmetry (3.05σ) deemed non-cosmological but relies on conservative Bonferroni correction. Direct MC (pLEE ≤ 10⁻⁴) suggests significance; inconsistency unresolved.  
  Fix: Reconcile methodologies or clarify why Bonferroni is preferred.

- **P4-M4 (Paper length)**  
  Problem: 56 pages exceeds PRD methods/catalog norms (15-30pp). Redundancies in systematics discussions (e.g., Sec. IV.E–IV.K).  
  Fix: Condense to ≤30pp by:  
  (a) Moving bias tests (Sec. III.F) to supplement;  
  (b) Combining repetitive diagnostics (e.g., sky regions/leg systematics);  
  (c) Cutting ancillary content (e.g., D4-TTA holdout details in Sec. III.E).

---

### MINOR Revisions

- **P4-m1 (Abstract, p1)**  
  Problem: Abstract emphasizes monopole-mask leakage but buries its non-cosmological status.  
  Fix: Add: "The canonical-mask residual is systematic, not primordial."

- **P4-m2 (Sec. V, p32)**  
  Problem: Shamir comparison (Sec. V.A) implies amplitude discrepancy but notes classifier/pipeline differences. No like-for-like test.  
  Fix: Clarify: "Discrepancy is pipeline-specific; formal exclusion requires matched-footprint reanalysis."

- **P4-m3 (Fig. 7–14)**  
  Problem: Figures lack direct script/dataset provenance (e.g., HEALPix maps).  
  Fix: Add footnotes: "Generated via [script] using [dataset]."

---

### NIT Revisions

- **P4-N1 (Sec. III.E, p10)**  
  Problem: "peq" undefined at first use.  
  Fix: Define at introduction: "peq ≡ equivariant probability".

- **P4-N2 (Refs, p50)**  
  Problem: Inconsistent arXiv formatting (e.g., "[3]" vs. "arXiv:2208.13866").  
  Fix: Standardize to "Author et al. [X], arXiv:YYYY.ZZZZZ".

---

## Summary recommendation
**MAJOR REVISIONS**  
The paper reports a significant null result with robust systematics control, but requires major revisions to address provenance gaps, statistical inconsistencies, and length. Key results (−0.12σ dipole, monopole-mask leakage) are compelling but obscured by versioning artifacts, unresolved contradictions in significance metrics, and excessive detail. Condensing the paper, rigorously sourcing all numbers, qualifying σ comparisons, and clarifying the sensitivity threshold derivation are essential. The core science is sound and merits publication post-revision.