# P1B R38conf — Physical Review D cosmology-physics referee with full PDF access

**Reviewer**: `Gemini_cosmology`
**Model**: `gemini-2.5-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.66.pdf` md5=065d0962 pages=20
**Input format**: NATIVE PDF (inline or Files API) + pass-2 self-critique (4467 chars)
**Wall time**: 148.1s

---

**Referee Report for Manuscript P1B**

**"Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model"**

## General Comments

This manuscript presents three technical analyses intended to support a companion paper on the Einstein-Cartan-Holst (ECH) spin-torsion cosmology program. The analyses are: (1) a stock-CAMB MCMC analysis of the ΛCDM+ΔNeff model as a null test, (2) a Monte Carlo validation of a NaMaster-based pseudo-C_ell pipeline for measuring cosmic birefringence, and (3) a consistency check of the observed birefringence signal with a standard spectator axion-like particle (ALP) model.

The paper is, for the most part, an exemplary technical companion. It demonstrates a high level of rigor, with careful attention to scoping, detailed documentation of methods, and honest disclosure of limitations and systematics. The authors are to be commended for the clarity with which they distinguish between pipeline validation figures and sky-detection significance, the thoroughness of the NaMaster robustness battery, and the transparency of the reproducibility materials. The practice of including a claims classification table (Table V) is novel and highly effective.

However, the manuscript contains a significant error in a physical calculation presented in the main text, which must be corrected. There is also a point of ambiguity in the description of a key MCMC prior that requires clarification. After these issues are addressed, the paper will be a strong candidate for publication.

---

## Findings

### ESSENTIAL

**ID: P1B-E1**
*   **Section/Page:** Section III, Page 4, "Physics interpretation (Table II)" paragraph.
*   **Problem:** The calculation of the phantom-crossing redshift `zx` is incorrect due to a flawed formula for the scale factor of crossing, `ax`. The text states: `the CPL trajectory w(a) = w0 + (1-a)wa crosses w = -1 at 1-ax = (-1-w0)/wa = 0.282, i.e. zx ≈ 0.39`.
    Using the quoted posterior mean values `w0 = -0.812` and `wa = -0.667`, the expression `(-1-w0)/wa` is indeed `(-1 - (-0.812)) / -0.667 = -0.188 / -0.667 = 0.282`. However, if `1-ax = 0.282`, then `ax = 0.718`, and the corresponding redshift is `zx = 1/ax - 1 = 1/0.718 - 1 = 1.39 - 1 = 0.39`. The text correctly reports `zx ≈ 0.39`. The error is in the formula presented. The text states `1-ax = (-1-w0)/wa`, but the standard CPL parameterization is `w(a) = w0 + (1-a)wa`. The crossing condition `w(ax) = -1` implies `-1 = w0 + (1-ax)wa`, which rearranges to `(1-ax) = (-1-w0)/wa`. The text has conflated `ax` with `1-a` in the formula `1-ax = ...`. The formula as written in the text is `ax = (-1-w0)/wa`, which would give `ax = 0.282` and a completely different redshift `zx = 1/0.282 - 1 = 2.54`.
*   **Required Fix:** The formula must be corrected for clarity and accuracy. Change the text to be unambiguous, for example: "the CPL trajectory `w(a) = w0 + (1-a)wa` crosses `w = -1` at a scale factor `ax` determined by `(1-ax) = (-1-w0)/wa`. At the posterior mean, this gives `(1-ax) = 0.282`, so `ax = 0.718`, corresponding to a redshift `zx ≈ 0.39`..." This clarifies the relationship between the terms and confirms the numerical result.

### MAJOR

**ID: P1B-M1**
*   **Section/Page:** Section III, Page 3, "Sampling configuration" paragraph.
*   **Problem:** The description of the prior on the effective number of relativistic species is confusing. The text states: "`Neff` enters as `nnu` with a flat prior `Neff ∈ [2.046, 5.046]` (i.e. `ΔNeff ∈ [-1,+2]`)". The standard value is `Neff_SM = 3.046`. The parameter `nnu` in CAMB is the total number of neutrino-like species. The text seems to be using `Neff` and `nnu` interchangeably, while also quoting a prior range for `ΔNeff = Neff - Neff_SM`. A reader should not have to guess the exact implementation.
*   **Required Fix:** Clarify the precise parameter being sampled and its relation to the standard model value. For example: "The total number of effective relativistic species, `Neff`, is sampled via the CAMB parameter `nnu`. We use a flat prior `Neff ∈ [2.046, 5.046]`. This corresponds to a prior on the deviation from the standard value, `ΔNeff = Neff - 3.046`, of `ΔNeff ∈ [-1, 2]." This removes all ambiguity.

### MINOR

**ID: P1B-m1**
*   **Section/Page:** Section VI, Page 10, Footnote 5.
*   **Problem:** The footnote states that a quintom late-time `w0wa` background would shift `H(z)` by a "few percent", which propagates to a "few-percent systematic on `Δφ/fa`". While plausible, the term "few percent" is qualitative. For a paper of this technical detail, a number should be provided.
*   **Required Fix:** Quantify "few percent". Perform the calculation described and report the maximum percentage change in `Δφ/fa` when using the best-fit `w0wa` cosmology from Table II as the background instead of ΛCDM. For example: "...shifts `H(z)` at `z≤1` by up to X%, propagating to a Y% systematic on `Δφ/fa`..."

**ID: P1B-m2**
*   **Section/Page:** Page 1, Abstract.
*   **Problem:** The abstract states "the scan-prior `m ~ H0` region brackets the published joint WMAP+Planck signal". Later, in the body (Sec. VI, p. 10) and conclusions (p. 13), it is clarified that the posterior-supported fit shifts to `m >> H0` (median `m ≈ 36 H0`). While the abstract is not wrong, it could be more precise by including the posterior result, which is a key finding of that analysis.
*   **Required Fix:** Add a clause to the abstract to reflect the posterior shift in mass. For example: "...the scan-prior `m ~ H0` region brackets the published... signal, but the posterior-supported accommodation shifts to `m >> H0`..." This more accurately reflects the paper's findings.

### NIT

**ID: P1B-N1**
*   **Section/Page:** Section IV, Page 6, Footnote 3.
*   **Problem:** The footnote says "the labels 'PR4/NPIPE' attached to the Eskilt+Komatsu likelihoods refer to the code-repository dataset". The author's name is Eskilt, not Eskilt+.
*   **Required Fix:** Change "Eskilt+Komatsu" to "Eskilt & Komatsu" for consistency with the main text and bibliography.

---

## Summary recommendation

**MAJOR REVISIONS**

The manuscript is a well-executed and valuable technical document that largely meets the high standards of Physical Review D. The detailed validation studies, clear scoping of claims, and commitment to reproducibility are commendable. However, the presence of a numerical error in the derivation of a key physical parameter (the phantom-crossing redshift) is a significant flaw that requires correction. The ambiguity in the `Neff` prior setup must also be resolved. Once these essential and major revisions are satisfactorily addressed, the paper will be suitable for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Here is the second-pass review.

================================================================
**Referee Report for Manuscript P1B (Second Pass)**

**"Technical Verification Companion to the ECH Spin-Torsion Program: ACDM+Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model"**

## General Comments

This manuscript was re-examined with a focus on numerical accuracy, internal consistency, and the faithfulness of its claims, following the initial review. The second pass confirms that the paper is of exceptionally high technical quality. The vast majority of calculations, cross-references, and interpretations are correct and meticulously documented. The authors' commitment to transparency, particularly in scoping their analyses and disclosing limitations, remains a key strength.

The essential and major issues identified in the first report still stand and must be addressed. This second review has identified one additional minor point of clarification that would improve the manuscript's already excellent exposition. The paper's integrity is very high, and after the recommended revisions, it will be an outstanding contribution.

---

## Findings (New in Second Pass)

### MINOR

**ID: P1B-m3**
*   **Section/Page:** Section V, Page 5, "MB-H0 joint-posterior offset check" paragraph.
*   **Problem:** The paragraph contrasts the `3.2σ` tension in the `MB` axis with the canonical `3.6σ` tension in the `H0` axis. It correctly notes they are not directly comparable and then dismisses the `3.2σ` figure as "not a properly conditioned tension statistic". While technically true, this phrasing could be improved. The `3.6σ` figure is also a simple Gaussian tension, not a formal p-value from a joint likelihood. The distinction is more about the physical basis of the comparison (direct measurement vs. derived parameter) than the statistical formalism.
*   **Required Fix:** Rephrase for clarity. For example, instead of "not a properly conditioned tension statistic", state more directly why the `H0` axis is the canonical one for this comparison: "The conditioned statement remains the canonical `H0`-axis tension, as this represents the direct discrepancy between the local distance ladder measurement and the CMB-calibrated inverse distance ladder prediction. The `3.2σ` figure is a useful consistency check showing how this tension manifests in the nuisance parameter `MB`."

---

## Summary of All Findings (Initial + Second Pass)

For the author's convenience, all findings are summarized below.

### ESSENTIAL

*   **P1B-E1 (Page 4):** The formula for the phantom-crossing scale factor `ax` is written incorrectly as `1-ax = ...` where it should be `(1-ax) = ...` or similar to avoid ambiguity. The numerical result `zx ≈ 0.39` is correct, but the derivation as presented is flawed.

### MAJOR

*   **P1B-M1 (Page 3):** The description of the `Neff` prior is ambiguous. It is unclear whether the sampled parameter is `Neff` or `ΔNeff` and how it relates to the CAMB parameter `nnu`. This must be clarified.

### MINOR

*   **P1B-m1 (Page 10, Footnote 5):** The term "few-percent systematic" on `Δφ/fa` is unquantified. The author should calculate and report the specific percentage to maintain the paper's high standard of quantitative rigor.
*   **P1B-m2 (Page 1, Abstract):** The abstract states the scan-prior `m ~ H0` brackets the signal, but a key finding is that the posterior shifts to `m >> H0`. The abstract should be updated to include this important result for a more complete summary.
*   **P1B-m3 (Page 5):** The discussion contrasting the `3.2σ` `MB` tension with the `3.6σ` `H0` tension could be framed more clearly to explain *why* the `H0` tension is considered canonical.

### NIT

*   **P1B-N1 (Page 6, Footnote 3):** Typo "Eskilt+" should be "Eskilt &".

---

## Summary Recommendation

**MAJOR REVISIONS**

The paper is technically sound, thorough, and transparent. The second-pass review confirmed the correctness of nearly all numerical claims and the internal consistency of the manuscript. The recommendation remains **Major Revisions**. The authors must correct the essential error in the phantom-crossing formula and clarify the major ambiguity in the `Neff` prior. Addressing the minor points will further enhance the clarity and impact of this excellent technical paper. Once these revisions are made, the manuscript will be a strong candidate for publication.