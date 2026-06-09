# P4 R22prov — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 NO_NEW
**Wall time**: 52.4s

---

The submission does not currently meet Physical Review D standards. Below I list all issues I can identify from the provided text; many are serious but mostly textual/procedural rather than physics-errors, since only the manuscript text (not the actual reference list metadata) is available.

Because I cannot see the actual formatted reference list (journal, year, arXiv IDs, page ranges), I cannot fully execute the “verify every cited paper” requirement (arXiv IDs, DOIs, etc.). I focus instead on internal consistency, statistical recomputation, null-comparability issues, residual references to the withdrawn value, and any citation facts that can be checked from in‑text information.

---

### P4‑E1 (ESSENTIAL) – Mixed σ / p conventions and inconsistent Gaussian equivalents

- **Location:** Abstract p.1, §IV A/B/C, Table I, Table III, Appendix C/D.
- **Problem:**
  - The paper repeatedly reports “σ” values from *different null procedures* (Gaussian analytic, bootstrap, block-bootstrap, label-shuffle, binomial generative, look‑elsewhere corrected statistics, etc.), and occasionally gives “Gaussian-equivalent” σ from p-values. Some juxtapositions are clearly described as non-comparable, but others are ambiguous.
  - Example: Abstract “+3.64σ (z = ∆/σnull moment-ratio; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent…)” puts a “3.64σ” (moment-ratio) and “1.9σ Gaussian-equivalent” directly together without explicitly warning that these are *different σ definitions* on the same residual, beyond a parenthetical. In the main body, “+3.64σ (z = ∆/σnull moment-ratio; empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent…)” is the clearest mapping—but elsewhere only “+3.64σ” appears.
  - The MASTER apodized footprint line is reported as “+7.28σ vs. global label-shuffle, Wp = Nall; +7.13σ vs. depth-stratified null” in Abstract and Table I, while later also used in Appendix A/D in a broader discussion of systematic structure. The paper notes that σ values are “not directly comparable across estimators,” but that statement appears only once in the abstract and once in §IV, and not at every juxtaposition where σ from different nulls are shown side‑by‑side (real-space dipole vs canonical MASTER vs apod. MASTER vs hemisphere look‑elsewhere, etc.).
  - In Table III, the “Significance (σ)” column mixes single-mode C1 significance (apodized MASTER, label-shuffle null) with bandpower significances for different ℓ ranges, plus a joint χ²/dof, without explicit annotation that the σ are all under different covariance structures than, e.g., the 0.43σ real-space dipole.
- **Required fix:**
  - Enforce the stated rule rigorously: **whenever σ values from distinct null definitions or estimators appear on the same line, in the same table row, or in the same sentence, explicitly qualify that they are not directly comparable and specify the null for each.**
  - For the canonical-mask residual, prominently state in Abstract, §IV C/D, and Appendix D that “+3.64σ” is a *z-score under the moment-ratio null* and that the Gaussian-equivalent significance from the empirical p-value (0.030) is ≈1.9σ; avoid leaving “+3.64σ” unqualified anywhere.
  - In every place where the +0.43σ real-space dipole and any MASTER σ value (+3.64σ or +7.28σ/+7.13σ) are both mentioned, explicitly mark them as *different estimators with different nulls*, not comparable in σ.
  - Table I and III should gain columns or inline notes indicating the null definition for each σ and a footnote stating that σ values across rows are not directly comparable.

---

### P4‑E2 (ESSENTIAL) – Internal inconsistency / confusion in Table III and surrounding text

- **Location:** Table III p.7 and text immediately before/after.
- **Problem:**
  - The caption: “Rows 2–5 are bandpowers from the canonical-N MASTER recompute (fsky = 0.491). The canonical-N MASTER direct-MC at ℓ = 1 on the canonical mask yields +3.64σ (Sec. IV D)…”
  - Row 1 of Table III is labeled: “ℓ = 1 (single mode, apod. footprint) … +7.28σ”. Rows 2–5 are ℓeff=4,9,14,19,24 bandpowers.
  - The text in §IV C/D and Appendix A describes two different ℓ=1 estimators:
    - canonical-mask single-mode NA-MASTER with direct MC: +3.64σ.
    - apodized analysis footprint, Wp=N_all, label-shuffle null: +7.28σ.
  - The caption conflates these by saying “bandpowers from the canonical-N MASTER recompute” while the first row is *not* canonical-N but the apodized footprint, and does not show the canonical ℓ=1 (+3.64σ) anywhere in the table.
- **Required fix:**
  - Cleanly separate the two estimators in Table III:
    - Either: add a row for “ℓ=1 (single mode, canonical mask)” with its C1, σnull, and +3.64σ, and clearly label the first row as “ℓ=1 (single mode, apodized real analysis footprint, Wp=Nall)” plus “diagnostic only”.
    - Or: restrict Table III to canonical-N bandpowers only and move the apodized ℓ=1 diagnostic to its own table or to text only.
  - Rewrite the caption to avoid “canonical-N” wording for the apodized footprint estimator.

---

### P4‑E3 (ESSENTIAL) – Abstract and “headline” claims vs. load-bearing evidence are not fully aligned

- **Location:** Abstract p.1, §III A, §IV C/D, §VII, Appendix D.
- **Problem:**
  - The abstract allocates substantial space to the canonical-mask residual and the MASTER apodized diagnostic, even though the author insists that the headline scientific results are the real-space null and the WLS template exclusion. The text is mostly consistent on that point, but:
    - Some wording blurs the distinction, e.g. “The present null disfavors the Shamir ∼3% detection class by a factor of ∼6–12 under our pipeline” (Introduction and Conclusions) is stated as a “present null” without immediately reinforcing that this is **under a particular injection–recovery and classification noise model** and is not a formal likelihood comparison on matched data.
    - For the canonical residual, the paper gives a long systematic attribution chain, but the abstract’s short version (“is consistent with monopole leakage through survey geometry… and is not interpreted as a cosmological signal”) reads more definite than the actual evidence, which is more “strongly suggestive but not fully closed,” especially given that the WLS template fit still leaves a non-zero “best-fit dipole” (4.5×10⁻³) and only disfavors A=1.7% at |z|~18 under a particular block-bootstrap covariance and design matrix.
- **Required fix:**
  - In the abstract, explicitly say: “We *do not* interpret the MASTER-based excesses as independent cosmological constraints; all cosmological conclusions rest solely on the real-space dipole and WLS template-fit analysis.”
  - When referencing “disfavors the Shamir ∼3% class by a factor ∼6–12,” clarify that this refers to signal amplitude relative to the *empirical detection threshold* (A₅₀ ≈ 0.75%, A₉₅ ≈ 1.5–2%) under this classifier and null—not a direct reanalysis of Shamir’s data.
  - Make clear that the systematic attribution chain for the canonical residual is strong but not mathematically exhaustive (e.g., “we find the data favor a systematic interpretation; a truly primordial dipole at ∼1–2% cannot be absolutely ruled out without a full joint cosmological likelihood, which is beyond this paper”).

---

### P4‑E4 (ESSENTIAL) – Monopole-vs-dipole estimator comparison framed in a way that invites misinterpretation

- **Location:** §IV B, §IV C, Fig. 7, Appendix A, Appendix D.
- **Problem:**
  - The paper compares the 2.31σ real-space dipole and +6.48σ pre-MASTER pseudo-Cℓ for Catalog A, and emphasizes they collapse to 0.43σ and small residuals after TTA and MASTER. This is correct qualitatively, but the wording “the difference between Catalog A and Catalog C is the difference between a 2σ ‘detection’ and a clean null” (Fig. 7 caption) risks suggesting that the MASTER channel or other partial-corrected channels *could* be viewed as “detections” on their own, contrary to the stated position that they are purely diagnostics.
- **Required fix:**
  - Add explicit language near Fig. 7 and in §VI that **none** of the pre-MASTER or canonical-mask excesses should ever be interpreted as cosmological detections; they are entirely artifacts of mask+monopole coupling and classifier bias.
  - Where “2σ ‘detection’” is mentioned, explicitly label it as “spurious” or “artifact” in the same sentence.

---

### P4‑M1 (MAJOR) – Residual references to withdrawn synthetic-catalog result are not fully quarantined

- **Location:** Abstract p.1, Appendix A(d).
- **Problem:**
  - The abstract includes: “Withdrawal note: versions ≤1.0.165 of this paper reported a −0.122σ MASTER ℓ = 1 null… computed on a synthetic-footprint catalog and it is withdrawn…”
  - Appendix A(d) gives an extended provenance narrative naming paths like `pipelines/p2_chirality/outputs/canonical_provenance/...`.
  - While the text tries to be transparent, PRD-style papers rarely embed such detailed version-tracking and internal script path references. These read like internal audit logs and will become stale or confusing for readers. The instructions you received explicitly warn against internal bookkeeping tags; here, file-system paths and version numbers are effectively that.
- **Required fix:**
  - Keep a *very brief* withdrawal statement (one sentence) either in Introduction or an endnote, not in the abstract, e.g.: “An earlier internal analysis accidentally used a synthetic footprint; all results here use the real DESI footprint. Details are in the online repository.”
  - Remove the detailed run-log / path-level discussion from Appendix A(d) or move it to a data‑release note outside the main paper. Summarize instead in one or two sentences.
  - Ensure that no numerical value from the withdrawn analysis is shown in any table, figure, or equation—currently the −0.122σ number only appears in narrative, which is acceptable if clearly marked “withdrawn” but should be minimized.

---

### P4‑M2 (MAJOR) – Unclear dimensional consistency and normalization in some equations and narrative

- **Location:** Eq. (3) p.6, Appendix A(a,c), Appendix D(f).
- **Problem:**
  - The text uses two different normalizations for Ap:
    - In §IV C (Eq. 3) Ap is defined with denominator `NCW(p)+NCCW(p)` (spirals only).
    - In Appendix A(a) it defines Ap = (NCW − NCCW)/Ntotal with Ntotal = NCW + NCCW + NNS but *then* says that the field used for the monopole leakage channel is constructed *without* monopole subtraction.
  - The generative null footnote explicitly stresses that the “canonical” definition uses Nspiral(p), while a parallel rerun uses Nall; but in Appendix A the “field” definition uses Ntotal. It is easy to lose track of which Ap normalization is used in which analysis step (real-space dipole vs canonical MASTER vs apodized MASTER).
  - This affects dimensional consistency: Cℓ values (Table III) are given for Ap fields with different weighting and normalization; the caption does not clarify whether these share the same Ap definition as Eq. (3).
- **Required fix:**
  - Introduce a clear symbol distinction, e.g.:
    - A_sp(p) = (NCW − NCCW)/(NCW + NCCW)
    - A_all(p) = (NCW − NCCW)/Nall
  - State explicitly in §III A and Appendix A which version is used for:
    - real-space dipole;
    - canonical MASTER;
    - apodized MASTER diagnostic;
    - generative monopole-only null.
  - Ensure equations and footnotes use the same notation and do not silently switch definitions.

---

### P4‑M3 (MAJOR) – Some numerical claims cannot be recomputed from provided numbers

- **Location:** Various:
  - A50 and A95, recovery probabilities (§VI A, Abstract).
  - “factor of ∼6–12” discrepancy vs Shamir.
  - “10–15% reduction in effective sample size” from edge-on contamination.
- **Problem:**
  - The paper gives summary numbers for injection-recovery (P(σ>3)=0.55 at A=0.75%, 0.15 at A=0.5%), but does not show enough intermediate numbers (e.g., explicit σ distributions) to verify A50 ≈ 0.75% or A95 ≈ 1.5–2% exactly.
  - The “∼6–12×” mismatch vs Shamir’s ∼3% amplitude is loosely justified by those thresholds, but the exact mapping is not shown; a reader cannot recompute this factor from the tables alone.
  - The “10–15%” effective N reduction and corresponding “5–8% sensitivity penalty” are heuristic; no explicit calculation or data table is provided to verify.
- **Required fix:**
  - Add a small table or figure in §VI A (or Appendix) with:
    - injection amplitudes A tested;
    - P(σ>3) at each A;
    - the inferred A50 and A95 with uncertainties.
  - For the “factor 6–12” statement, either:
    - show a simple calculation, e.g. 3% / (A50 .. A95) or address Shamir’s stated amplitudes more explicitly; or
    - weaken the phrasing to “a factor of a few larger than our ∼1–2% sensitivity scale” if you do not want to lock in a precise ratio.
  - Either support the “10–15%” effective sample-size loss with a quantitative edge-on contamination calculation (using counts and classification noise), or rephrase as a qualitative statement without precise percentages.

---

### P4‑M4 (MAJOR) – Use of path-like artifacts and internal script names in the text

- **Location:** Appendix A(d), Appendix C and E footnotes, Data Availability.
- **Problem:**
  - Long path strings like `pipelines/p2_chirality/outputs/canonical_provenance/...` are not standard in PRD manuscripts. They are brittle, will not be meaningful to most readers, and read as internal audit logging.
- **Required fix:**
  - Replace explicit path names with higher-level descriptions, e.g. “see the provenance JSON file in the public repository (analysis/monopole_null_provenance.json).”
  - Reserve exact paths for the online code repository, not the main paper.

---

### P4‑M5 (MAJOR) – Potential overlength for the claimed contribution

- **Location:** Whole manuscript (15 pages + several long appendices in the main body).
- **Problem:**
  - For a results paper whose main contribution is a null dipole detection and a systematic interpretation of a single-channel residual, the text is quite long and sometimes reads more like an internal analysis notebook (extensive appendices, bias tests, provenance logs).
- **Required fix:**
  - Streamline:
    - Move much of Appendix B–E level operational detail (particular hyperparameters, many diagnostic tests, long provenance narratives) to an online supplementary or code documentation.
    - Focus the main text on:
      - data;
      - the classifier method with essential equivariance details;
      - the real-space dipole result;
      - the generative leakage null;
      - the template-fit exclusion;
      - the key systematic evidence for interpreting the canonical residual.
  - A target of ~10–12 journal pages for the main article (excluding online supplement) seems more proportionate.

---

### P4‑m1 (MINOR) – Some σ and p-value conversions could be clearer

- **Location:** Abstract, §IV D, Appendix C/D.
- **Problem:**
  - “empirical rank pMC = 0.030, i.e. ≈1.9σ Gaussian-equivalent” is fine, but the reader is never reminded whether one-sided or two-sided conversion is used; 0.03 two-sided corresponds to ≈1.88σ.
- **Required fix:**
  - Add a sentence in §IV: “Unless stated otherwise, we convert p-values to σ assuming a two-sided Gaussian tail.”

---

### P4‑m2 (MINOR) – A few ambiguous phrasings about novelty and “largest” dataset

- **Location:** Introduction p.2, §VII Intro.
- **Problem:**
  - Statements like “We have constructed and analyzed the largest galaxy chirality catalog to date: 8,474,531 galaxies…” are plausible given Jia et al. (2023) – 1.95M – but should be explicitly justified.
- **Required fix:**
  - Cross-check that no other published work has >8M chirality-labeled galaxies; if unsure, qualify as “to our knowledge” or “one of the largest”.

---

### P4‑m3 (MINOR) – Consistency check of a few recomputable numbers

1. **Binomial σ for global CW fraction (Table II):**
   - Nspiral = 3,201,160; p ≈ 0.5 → σ ≈ √(0.25/N) ≈ √(0.25/3.20116e6) ≈ 0.000279: matches table.
   - Dev. for Catalog C: (0.4974 − 0.5)/0.000279 ≈ −0.0026 / 0.000279 ≈ −9.3; text says 9.5σ: acceptable given rounding, but you might recompute with full precision and update to 9.3–9.4σ.

2. **MASTER apodized footprint C1 significance (Table III):**
   - C1 = 23.48×10⁻⁶ sr, σnull = 2.99×10⁻⁶ sr → z ≈ 7.85, not 7.28; but note that the quoted 7.28σ refers to label-shuffle null; σnull in the table may be from a different null or effective fsky. This is confusing.
   - Required: clarify in the caption which σnull the table uses, and ensure that the quoted “+7.28σ” is computed from those numbers or give *both* the raw ratio and the MC-based σ.

---

### P4‑m4 (MINOR) – Small notation and typographical issues

- **Location:** Multiple:
  - “[iso. boot. (10⁴)]” vs “NMC = 10,000” – unify notation.
  - “z ≈ −18” appears as a “z-score” in places; elsewhere “z ≈ −264.5” appears in Appendix D. Make sure “z” is always defined where used (z-score vs redshift vs any other).
  - Some hyphenation is inconsistent (“sub-percent”, “subpercent”, “per-pixel”, “per pixel”).
- **Required fix:**
  - Standardize notation and define all symbols once per section.

---

### P4‑n1 (NIT) – Style and readability

- **Location:** Across text.
- **Problem:**
  - Heavy use of in-line code-y details (e.g., “seed 42”, “NMC,null = 1000”) inside narrative paragraphs reduces readability.
- **Required fix:**
  - Move such low-level details to a concise experimental setup paragraph or a small table in an appendix.

---

## Summary recommendation

**MAJOR REVISIONS**

The scientific idea and overall analysis strategy (equivariant classifier, real-space dipole estimator, and monopole–mask leakage null) are interesting and potentially suitable for PRD, but the current manuscript has several issues: mixing of σ values from different nulls without sufficiently strong, repeated cautions; confusion between canonical and apodized MASTER ℓ=1 results in Table III; over-elaborate provenance discussion including a withdrawn synthetic-catalog result in the abstract; and some numerical inconsistencies that are not easily recomputable from the text alone. These must be corrected and the exposition significantly tightened before the paper can be considered at PRD’s standard.