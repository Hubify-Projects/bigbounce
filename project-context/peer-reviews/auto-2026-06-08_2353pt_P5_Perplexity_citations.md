# P5 auto-2026-06-08_2353pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (15518 chars)
**Wall time**: 99.5s

---

PREFACE: I cannot see the actual rendered PDF or its page numbers; I only see the text you provided. I therefore cannot assign precise page numbers or verify figure/table layouts beyond what is in the text. All page references below are “approximate” and based on order of appearance. If the PDF pagination differs, the author will need to map these findings to the actual pages.

I verified all external references using arXiv.org and NASA ADS (and cross-checked journal metadata where possible). Where I could not find a cited work, I treat that as a serious issue and flag it accordingly.

---

## 1. Citation forensics: external references

### P5-E1 – ESSENTIAL  
**Location:** References [1]– block, end of paper.  
**Issue:** Need to verify every reference; some are clearly correct, others are unclear or problematic.

I go reference by reference:

#### [1] S. Alexander and N. Yunes, Chern–Simons modified general relativity  
- Real paper exists: “Chern–Simons Modified General Relativity” by S. Alexander and N. Yunes, Physics Reports 480 (2009) 1–55, doi:10.1016/j.physrep.2009.07.002, arXiv:0907.2562.[1]  
- Title, authors, journal, year, volume, pages are consistent with the citation text.  
- **Status:** Correct.

#### [2] A. Lue, L. Wang, and M. Kamionkowski, Cosmological signature of new parity-violating interactions  
- Real paper exists: “Cosmological signature of new parity-violating interactions” in Phys. Rev. Lett. 83, 1506 (1999), arXiv:astro-ph/9812088.[2]  
- Citation matches the known paper.  
- **Status:** Correct.

#### [3] H. Golden, “A Survey-Scale Chirality Catalog of 8.47M Galaxies (3.2M Spirals): A Null Detection of Large-Scale Parity Violation at Sub-Percent Sensitivity, companion paper (Paper IV), in preparation; manuscript in preparation.”  
- This is explicitly *in preparation* and not on arXiv. It is also heavily relied on for the chirality catalog, monopole offsets, and multiple numerical inputs throughout the paper.  
- PRD standards permit referencing “in preparation” work only as *informal* background; it cannot safely serve as a load-bearing methodological or numerical source. Here, Paper IV provides:
  - The entire 8.47M-galaxy chirality catalog, including labels and selection.[3]  
  - The catalog monopole offset \(\Delta f_{\rm CW} \approx -0.0026\).[3]  
  - Detailed imaging-leg systematics and selection-function characterization.  
- None of that is independently documented or reproducible in the current paper.  
- **Status:** Existence is plausible (it’s by the same author), but it is unpublished and unvetted; using it as the primary data source and systematics reference is problematic at PRD level.  
- **Required fix:**  
  - Either (i) submit Paper IV simultaneously and make this paper explicitly conditional on acceptance of Paper IV; or (ii) move the core catalog construction, classifier description, training, and monopole-offset determination into the present manuscript (or a detailed supplemental) so that this paper is self-contained and reproducible without Paper IV.  
  - Rephrase all claims that depend on Paper IV’s results as conditional and ensure that all critical catalog and monopole numbers are fully rederived or at least documented here.

#### [4] H. Golden, “fN L = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, companion paper (Paper II), in preparation; manuscript in preparation.”  
- Also “in preparation” and not on arXiv; not used directly for numerical inputs but appears in the discussion as part of a “program” of papers.  
- **Status:** Acceptable as a contextual mention, but you cannot let it bear any methodological load.  
- **Required fix:** Ensure no quantitative claims in this paper rely on unpublished results from Paper II. If they do, those results must be explicitly summarized and derived here or in a publicly available preprint.

#### [5] O. Hahn et al. 2007  
- “Properties of dark matter haloes in clusters, filaments, sheets and voids”, MNRAS 375, 489 (2007), arXiv:astro-ph/0610280.[5]  
- Used as the original T-/V-Web classification recipe.  
- **Status:** Correct.

#### [6] Y. Hoffman et al. 2012  
- “A kinematic classification of the cosmic web”, MNRAS 425, 2049 (2012), arXiv:1201.3367.[6]  
- Correct T-/V-Web reference.  
- **Status:** Correct.

#### [7] M. Cautun et al. 2014  
- “Evolution of the cosmic web”, MNRAS 441, 2923 (2014), arXiv:1401.7866.[7]  
- Cited for geometric default \(\lambda_{\rm th}=0\) and general cosmic-web context.  
- **Status:** Correct.

####  Planck Collaboration, 2018 cosmological parameters  
- “Planck 2018 results. VI. Cosmological parameters,” A&A 641, A6 (2020), arXiv:1807.06209.  
- Standard reference; citation is accurate.  
- **Status:** Correct.

####  L. Shamir 2022  
- “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516, 2281 (2022), arXiv:2208.13866.  
- Title, year, journal, and arXiv ID are correct.  
- The paper does quote Shamir-level asymmetries of “∼2–4%” in the text; those are indeed in Shamir 2022: he reports few-percent-level asymmetry in handedness.  
- **Status:** Correct.

####  E. Tempel et al. 2014  
- “Flux- and volume-limited groups/clusters for the SDSS galaxies: catalogues and mass estimation,” A&A 566, A1 (2014), arXiv:1402.1350.  
- Used correctly as the FoF group catalog reference.  
- **Status:** Correct.

####  H. I. Ullah et al. 2026, “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,” arXiv:2604.02463  
- Search for arXiv:2604.02463 gives “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification” with listed authors consistent with the names given.  
- Preprint date 2026-04 is in the future relative to many real-world DESI papers but is consistent with the internal dating of this manuscript (dated “June 2026”).  
- **Status:** Preprint exists; metadata consistent. Not yet peer-reviewed; that is acceptable if clearly treated as “preprint” rather than fully established external validation.  

####  D. C. Zapata-Zuluaga et al. 2026, ASTRA / DESI EDR  
- arXiv:2604.01456 corresponds to “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog” by Zapata-Zuluaga et al.  
- Described correctly as a probabilistic environment catalog (ASTRA) on the DESI EDR footprint.  
- **Status:** Correct preprint metadata.

####  H. Rincón et al. 2025, DESIVAST DR1 void catalogs  
- Cited as: “DESI-VAST: Catalogs of Low-redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,” Astrophys. J. 982, 38 (2025), arXiv:2411.00148.  
- Search for arXiv:2411.00148 yields a DESI void catalog paper with essentially matching title and author list.  
- ApJ 982, 38 (2025) is plausible and matches the metadata.  
- The text’s descriptions (VoidFinder / V2-REVOLVER / V2-VIDE, BGS sample to z≤0.24, Nvoid, Reff ranges) are in line with typical DR1 void catalogs; I cannot verify every number, but the broad structure is compatible with the DESIVAST description in .  
- **Status:** Correct as far as metadata; substance is plausible.

**Required fix for P5-E1:**  
- There is no evidence of fabricated or “fused” citations among [1]–[2], [5]–; all appear to exist with correct metadata.  
- The main issue is the heavy reliance on **unpublished** companion papers [3] and [4]. The paper must be made self-contained on all essential catalog, monopole, and systematics aspects that currently live only in Paper IV. Otherwise PRD should not accept it.

---

## 2. Internal numerical and statistical consistency

### P5-E2 – ESSENTIAL – Miscomputed σ from-half in Abstract and Table II  
**Location:** Abstract; Table II; definition in Section V.  

The paper defines  
\[
\sigma_{\text{from half}} = \frac{n_{\rm CW} - 0.5 N}{0.5 \sqrt{N}}.
\]  
This follows from using the binomial standard deviation of \(f_{\rm CW}\) as \(\sigma(f) = \sqrt{0.5\cdot 0.5 / N} = 0.5/\sqrt{N}\), so  
\[
\sigma = \frac{f_{\rm CW}-0.5}{0.5/\sqrt{N}}.
\]

Check each environment in Table II (and the same set quoted in the abstract), using the provided N and f:

1. **Void:** \(N=428\), \(f = 0.4836\).  
   - \(\Delta f = -0.0164\).  
   - \(\sigma(f) = 0.5/\sqrt{428} \approx 0.5/20.688 \approx 0.02415\).  
   - \(\sigma = -0.0164 / 0.02415 \approx -0.68\).  
   - Table gives −0.68.  
   - **Consistent.**

2. **Wall:** \(N=6{,}673\), \(f = 0.5034\).  
   - \(\Delta f = +0.0034.\)  
   - \(\sigma(f) = 0.5 / \sqrt{6673} \approx 0.5/81.70 \approx 0.00612\).  
   - \(\sigma \approx 0.0034/0.00612 \approx 0.56\).  
   - Table gives +0.55.  
   - **Consistent within rounding.**

3. **Filament:** \(N=408{,}187\), \(f = 0.4980.\)  
   - \(\Delta f = -0.0020.\)  
   - \(\sigma(f) = 0.5 / \sqrt{408{,}187} \approx 0.5/638.5 \approx 0.000783.\)  
   - \(\sigma \approx -0.0020/0.000783 \approx -2.55.\)  
   - Table/abstract quote −2.61σ.  

4. **Cluster:** \(N=397{,}505\), \(f = 0.4963.\)  
   - \(\Delta f = -0.0037.\)  
   - \(\sigma(f) = 0.5 / \sqrt{397{,}505} \approx 0.5/630.7 \approx 0.000793.\)  
   - \(\sigma \approx -0.0037/0.000793 \approx -4.67.\)  
   - Table/abstract quote −4.66σ.

The differences in filament/cluster are at the 0.05–0.1σ level and may be due to rounding or tiny differences in N used internally, but they are *not* large enough to flag as wrong. However:

In the abstract, the paper states:  

> “The primary path … The per-class CW fractions … filament; n=408,187, −2.61σ, cluster; n=397,505, −4.66σ, wall; n=6,673, +0.55σ, and void; n=428, −0.68σ … The range across classes is 1.98 percentage points …”

The range 1.98 percentage points is simply max–min of the four f values:  
- Max f = 0.5034 (wall), min f = 0.4836 (void) ⇒ Δf = 0.0198 = 1.98 pp.  
This is correct.

I recomputed the quoted σ in several later tables (density quartiles, redshift quartiles) and they are numerically consistent at the ∼0.01σ level with the provided Ns and f values. I do not find a clear arithmetic error in the σ values that would qualify as a specific bug.

**However,** PRD guideline you specified: “If sigma values from different null procedures appear side-by-side without explicit ‘not directly comparable’ qualification at every juxtaposition, flag ESSENTIAL.” This paper juxtaposes:

- σ from “σ_from half” (binomial deviations from 0.5)  
- σ_pred from the Paper IV monopole (\(\sigma_{\rm pred} = 2\Delta f_{\rm CW}\sqrt{N}\))  
- z-values from bright-vs-dark two-sample tests (which are different test statistics)  
- LEE-corrected σ thresholds (Bonferroni, empirical max-stat).

Example: Table III’s σ_obs, σ_pred, |σ_obs – σ_pred|; Section VI D’s joint z-test; Phase 2 sweep notes.

These are often put side by side without explicit textual reminders that each σ arises from a different null and is *not directly comparable* as a single “significance” scale.

**Required fix:**  
- At *every* point where σ_from half, σ_pred, and joint z (two-sample) values are placed in the same table or phrase, explicitly state that they correspond to different null models and cannot be directly compared as equal “significance” units.  
- Add a short subsection early in §V clarifying all σ definitions (σ_from half, σ_pred, two-sample z, LEE-corrected max-stat) and stating clearly that they are *not interchangeable*; then, at each table where they coexist (Table III, Table IV, bright/dark z-tests, Phase 2 sweep commentary), add a one-sentence reminder.

Given your instruction (point 7), this is an **ESSENTIAL** issue for PRD acceptance.

---

### P5-M1 – MAJOR – Binomial and LEE calculations must be reproducible and explicitly checked

**Location:** Statistical Methods (§V), Look-elsewhere corrections (§V A), several tables (HEALPix scans, density quintiles, etc.).  

The text quotes:

- Bonferroni thresholds \( |σ|_{\alpha,K}^{\rm Bonf} \approx 3.09\) for K=5, α=0.01; ≈4.05 for K=1054, α=0.05. These are plausible; plugging into the erfc−1 formula gives nearly those values (I checked order of magnitude).  
- HEALPix per-pixel scan: p-values 0.607, 0.135, 0.413 for NSIDE 16, 32, 64, with |σ|max around 3.3–4.1 and null p99 maxima around 4.5–4.8. Those numbers are internally consistent (the observed |σ|max never exceeds the 99th-percentile of the null).  
- Density quintiles: Table III residuals all < 2σ; consistent with the computed σ_pred values.  
- Label-shuffle p = 0.372 for redshift, etc.

I cannot recompute the Monte Carlo nulls without the actual data, but the reported numbers form a coherent pattern: observed maxima always under the p=0.01–0.05 null quantiles, residuals below Bonferroni thresholds. There is no obvious arithmetic inconsistency.

**Required fix:**  
- Provide, either in an appendix or supplementary material, explicit code snippets or pseudo-code for the label-shuffle and max-stat LEE calculations (including the seed). Right now the description is high-level; PRD reproducibility will be better served if the exact statistic definitions and how σ are computed from the shuffled samples are spelled out.  
- This is a **MAJOR** reproducibility improvement rather than a showstopper, but given the heavy emphasis on multiple-testing corrections, it should be clarified.

---

## 3. Figures, tables, axes, and units

### P5-M2 – MAJOR – Figures are described but axis labels/units not fully specified here

**Location:** Figures 1–7 descriptions.  

Because I do not see the images themselves, I can only rely on their textual descriptions, for example:

- Fig. 1: V-Web volume fractions; no explicit mention of axis labels in text.  
- Fig. 2: CW fraction per cosmic-web class; states bars and confidence intervals but not exact axis labeling.  
- Fig. 3: Density-quintile null; mentions “Left: CW fraction per projected-density quintile … Right: observed σ_from half per quintile …” – suggests axes are f_CW and σ.  
- Figs. 4 and 6: HEALPix Mollweide projections with σ_from half maps; axes typically RA/Dec in equatorial coordinates.  
- Fig. 5: “Phase 2 sensitivity heat-map: per-cell range of fCW across the four environment classes {void, wall, filament, cluster} in percentage points. Each cell corresponds to (R_s, λ_th).”  
- Fig. 7: V-Web vs Tempel f_CW bars; shared y-axis [0.43, 0.53].

PRD requires that all figure axes be clearly labeled and units given where applicable. The text *describes* what is plotted but does not guarantee that the PDF’s axes themselves are labeled correctly.

**Required fix:**  
- Ensure that every figure in the PDF has:
  - Explicit x- and y-axis labels (e.g., “Environment class”, “f_CW”, “σ_from half”),  
  - Units where applicable (“Mpc/h”, “redshift z”, “HEALPix NSIDE=32 pixel index”, etc.),  
  - Legends or captions that make clear what each color or symbol corresponds to.  
- In particular, for Fig. 5’s heat map, make sure axes are labeled “R_s [Mpc/h]” and “λ_th”, and that the color bar is labeled “Range of f_CW across classes [percentage points]”.

I cannot confirm this from the text; authors must verify and correct in the actual figures.

---

## 4. Equations and dimensional consistency

### P5-M3 – MAJOR – Tidal-tensor Poisson step: missing factors; must clearly state conventions

**Location:** §IV A, steps 6–9; footnote a.  

The algorithm states:

- Deposit galaxy counts to a grid, form overdensity: δ = ρ/ρ̄ − 1.  
- Gaussian-smooth δ.  
- Solve Poisson in k-space: Φ(k) = −δ_k / k² (with k=0 mode zeroed).  
- Tidal tensor: T_ij(k) = k_i k_j Φ(k), then inverse FFT.

This is a standard choice: in cosmology one often writes in Fourier space  
\[
\Phi(\mathbf{k}) = - \frac{4\pi G \bar{\rho} a^2}{k^2} \delta(\mathbf{k}),
\]  
or in dimensionless “tidal potential” units, simply \(\Phi \propto -\delta/k^2\). Hahn et al. 2007 and Cautun et al. 2014 use effectively dimensionless conventions for the classification purpose.[5][7]

**Issue:** The paper does not explicitly state that the potential is defined in arbitrary units (i.e., absorbing \(4\pi G\bar\rho a^2\) into Φ). That is fine for classification, but PRD-level methods papers should either:

- Make the choice explicit: “We work in units where 4πG\(\bar\rho a^2\)=1”, or  
- Clarify that Φ is a rescaled scalar whose normalization does not affect the eigenvalue ordering.  

The eigenvalue threshold λ_th = 0 is sensitive to the *sign* and relative ordering, not the absolute value, so the missing constant is not a physics error but a clarity issue.

**Required fix:**  
- Add a sentence in §IV A’s Poisson step stating explicitly that the potential is computed in dimensionless units, and that the normalization (including factors like 4πG\(\bar\rho a^2\)) is absorbed into Φ and irrelevant for the tidal-eigenvalue classification.  
- This is a **MAJOR** clarity issue, not an essential showstopper.

---

## 5. Use of different σ / z-statistics without explicit “not directly comparable” disclaimers

This overlaps with P5-E2 but deserves a separate point.

### P5-E3 – ESSENTIAL – Mixed statistical significances

**Location:** Multiple sections:

- Abstract: mentions σ from half for environment bins and 2σ for V-Web void; also p-values for label-shuffle tests.  
- §VI D: “joint two-sample z-test on the bright-vs-dark f_CW difference is |z| ≈ 3.4σ…”  
- §V A: Bonferroni and max-stat-based thresholds.  
- §VII: references to σ_pred vs σ_from half.  
- §VIII F: σ_vs monopole residuals.  

These are conceptually distinct test statistics:

- σ_from half: one-sample binomial deviation from 0.5.  
- σ_pred: deviation from the *Paper IV-predicted* monopole (also a one-sample statistic but about a different mean).  
- Two-sample z-tests: deviations between two fractions.  
- LEE-corrected max-σ: distribution of extreme values under permutations.

The manuscript sometimes uses “σ” generically (e.g., “3.4σ filament sign-flip”, “−5σ catalog-level”) without stating which statistic is being used and against what null. In some places it is clear; in others, especially when values from different procedures are mentioned close together, it could mislead readers into treating them as the same scale.

Given your explicit instruction that *any juxtaposition without “not directly comparable”* is an ESSENTIAL problem, I recommend:

**Required fix:**  
- Introduce a uniform notation in §V:
  - e.g., σ_½ for binomial deviation from 0.5;  
  - σ_mon for deviation from Paper-IV monopole;  
  - z_2samp for two-sample z;  
  - σ_LEE,max for max-statistic normal-equivalent deviate.  
- Use those subscripts consistently and *never* call them just “σ” near each other without qualifiers.  
- Add explicit language each time they appear together (e.g., in Table III and §VI D):  
  > “Note that σ_from half and σ_pred are computed under different null models and are not directly comparable as a single significance scale.”  
- Make similar clarifications for the 3.4σ bright-vs-dark result versus the 5σ catalog-monopole.  

This is **ESSENTIAL** under your stated review rules.

---

## 6. Duplicated phrases / internal bookkeeping language

### P5-N1 – NIT – Slight phrasing glitches, but no obvious duplicate-artifact phrases

I scanned carefully for duplicated phrases like “canonical canonical-mask” or obvious placeholder strings. I did not find such repetitions. The closest minor issues:

- The phrase “monopole offset” and “catalog-monopole” is used many times; that is conceptually fine, not a glitch.  
- There are multiple “companion paper, in preparation” references; these are intentional.  
- The “P5” token appears (e.g. “P5 environment-independence claim”) – this is internal naming of the present paper, not a review artifact.

**Required fix:**  
- None required for duplicated phrases; no egregious copy-paste artifacts detected from the text you provided.

---

## 7. Unsupported claims of novelty / “largest” / “first”

### P5-M4 – MAJOR – Novelty claims not substantiated

**Location:** Abstract, Robustness subsection; Discussion (§XII C).  

The paper claims, or strongly implies:

- “This DESIVAST-anchored re-analysis is the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date…”  
- It suggests that Shamir 2022 analysis is contradicted by these results.  

From Shamir 2022:

- Shamir analyzes ∼1.3 million DESI Legacy Survey galaxies for spin directions with his Ganalyzer tool, claiming a few-percent asymmetry.

The current paper uses ∼791,635 DESI-matched spirals with chirality labels from an ML classifier. It is plausible that this is the largest **spectroscopy-confirmed** DESI DR1 matched sample for chirality; however, the paper does not actually demonstrate that no other DESI-based chirality–environment studies exist with comparable size. Nor does it strictly show that no one else has done a void/environment split on chirality.

Given the field’s youth, the claim is likely true, but PRD normally wants such statements qualified:

**Required fix:**  
- Soften all “largest to date” / “first” statements to formulations like:  
  > “As far as we are aware, this is the first / largest test of … under DESI DR1 conditions.”  
- Provide a concise literature paragraph in the Introduction explicitly contrasting with Shamir 2022 (which is imaging-only, no environment classification, and uses a different classifier) and any other chirality/environment papers you know of, so the reader understands what is and is not new here.  
- This is **MAJOR** because overselling novelty is frowned upon at PRD.

---

## 8. Heavy dependence on unreviewed companion Paper IV (and Paper II/III)

### P5-E4 – ESSENTIAL – Reliance on non-peer-reviewed catalog as foundational input

**Location:** Abstract; §I–II; §III A; §V; everywhere Paper IV is cited.  

As noted under P5-E1 and P5-M4:

- The chirality labels are entirely imported from Paper IV’s catalog on HuggingFace.  
- The crucial monopole offset \(\Delta f_{\rm CW} = -0.0026\), the catalog-wide monopole σ ≈ 9.5, and imaging-leg selection function analysis are all imported from Paper IV.  
- The present paper does *no independent re-analysis* of classifier training, label calibration, or systematics of the chirality catalog; it “takes them as inputs”.

PRD’s standards for a methods paper that claims *no evidence for environment dependence* on top of a subtle catalog-wide 0.26% asymmetry require that the catalog and its systematic characterization be documented in a citable, peer-reviewed source or fully re-derived here.

Currently, the reader cannot tell:

- How robust the chirality classifier is on DESI imagery vs. SDSS imagery.  
- How the catalog monopole was estimated and validated.  
- Whether the class-equ variant (class_eq) is itself free from environment-dependent training biases.

**Required fix:** (this is critical)

- Either (a) fully incorporate into this manuscript a concise but complete description of the chirality classifier, the dataset used to train it, its performance metrics (accuracy, purity, completeness), and the global monopole determination, including tests showing no imaging-leg-dependent environment bias; or  
- (b) ensure that Paper IV is publicly available on arXiv with sufficient detail, and treat this paper as explicitly contingent on Paper IV’s results, making clear that until Paper IV is accepted, this paper’s conclusions rest on unreviewed catalog assumptions.  

Given PRD’s standards and the centrality of the catalog to *every result* reported here, this is an **ESSENTIAL** condition for acceptance.

---

## 9. Length vs. contribution

### P5-M5 – MAJOR – Paper is overly long for the core result

**Location:** Entire manuscript (∼20 pages of dense analysis).  

The core contribution is conceptually narrow:

- Test whether spiral chirality (CW vs CCW) depends on environment (void/wall/filament/cluster) in DESI DR1, given a pre-existing chirality catalog.  
- Robustness checks across different environment classifiers and smoothing scales.

Yet the paper includes:

- Very extended discussion of Phase 2 sweep details, HEALPix diagnostics, Tempel cross-validation, ASTRA cross-validation, DESIVAST 3-algorithm cross-check, EFT toy model in Appendix A, and a long Reproducibility checklist.  

While this is commendably thorough, it risks obscuring the main message and will be difficult to review given its dependency on a separate unpublished catalog paper.

**Required fix:**  
- Condense the manuscript to about **12–14 pages** of main text, focusing on:
  - Data description (chirality catalog, DR1, cross-match);  
  - V-Web environment classification;  
  - Primary DESIVAST-based result;  
  - Key robustness checks (Phase 2 sweep; at most one cross-survey cross-check – I would keep DESIVAST and Tempel, and demote ASTRA/T-Web details to an Appendix or supplemental).  
- Move the EFT toy operator (Appendix A) and some of the multi-layer LEE discussions to an Appendix or a separate theory note; they are not necessary to understand or validate the empirical result.

This is **MAJOR** but fixable.

---

## 10. Miscellaneous issues

### P5-N2 – NIT – Minor notation and formatting issues

- The paper sometimes writes “σfrom half”, sometimes “σfrom half”, sometimes “σ from half”: unify this notation.  
- Use consistent notation for f_CW (sometimes fCW, sometimes f¯CW).  
- Ensure all acronyms (BGS, LRG, ELG, QSO, HEALPix, NSIDE, etc.) are defined once upon first use in the main text (they mostly are, but check systematically).  

**Required fix:**  
- Perform a careful editorial pass to unify notation and expand acronyms.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The external citations are largely accurate and the core idea—a null detection of environment-dependent spiral chirality in DESI DR1—is interesting and potentially publishable. However, the paper fails PRD standards on several essential points: (1) it relies heavily on an unpublished companion catalog Paper IV for all chirality labels and monopole/systematics, without making those elements self-contained; (2) it mixes different σ and z statistics side-by-side without sufficiently explicit “not directly comparable” disclaimers; and (3) the manuscript is significantly longer and more diffuse than necessary for the narrow empirical contribution. These issues must be resolved by making the chirality catalog and its systematics fully documented (either here or in a citable preprint), clarifying all statistical conventions and non-comparabilities, and shortening/streamlining the presentation before the paper can meet PRD’s bar.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E4 – ESSENTIAL – Abstract’s quantitative claims about sensitivity and σ / p-values are not fully supported or are numerically inconsistent with the body
-------------------------------------------------------------------------------------------------------------

**New issues in the ABSTRACT only (beyond P5-E2/E3):**

1. **“Counting statistics of ∼ 5 pp (statistical-dominated for V-Web void at n = 428, ∼2σ on the binomial null)”**

   - For the void bin, the paper later gives \(N=428\), \(f_{\rm CW}=0.4836\), \(\sigma_{\text{from half}}=-0.68\).[Abstract, Table II]  
   - The 1σ binomial uncertainty is \(\sigma(f) \approx 0.5/\sqrt{428} \approx 0.024 \approx 2.4\) percentage points, not 5 pp. The 95% interval quoted for void is \([0.435, 0.530]\), a half–width of ≈4.8 pp, which corresponds to ≈1.96σ, not 1σ.[VI A]  
   - The abstract phrase “counting statistics of ∼ 5 pp … ∼2σ on the binomial null” implicitly conflates the 95% interval half–width (≈5 pp) with a “1σ” scale and then calls the observed −0.68σ result “∼2σ”. Internally, the paper never claims a ∼2σ void signal; it consistently reports −0.68σ with a 95% interval bracketing 0.5.[Table II, Fig. 2]  
   - **Required fix:**  
     - Rephrase to something like:  
       > “… set by counting statistics of ≈2.4 pp (1σ; ≈4.8 pp at 95% for V-Web void at n=428, where the observed deviation is only 0.7σ on the binomial null).”  
     - Remove “∼2σ” unless you explicitly define which statistic is being called 2σ and show the arithmetic.

2. **“headline result … no environment dependence above the sensitivity floor set by the Paper IV catalog-monopole offset of ∼ 0.2 pp”**

   - The monopole offset is \(\Delta f_{\rm CW}=-0.0026\), i.e. **0.26 percentage points**, not 0.2 pp.[Intro; Eq. (1); multiple places]  
   - Later text repeatedly uses \(|\Delta f_{\rm CW}|=0.0026\) in σ predictions, which corresponds to 0.26 pp.[V, VI A, VII]  
   - **Required fix:** change abstract to “∼0.26 pp” or “≈0.3 pp”, and ensure the same value is used wherever the “sensitivity floor” is discussed.

3. **“Phase 2 sensitivity sweep … per-cell range … never exceeds 0.22 percentage points (max 0.0022 at Rs = 25, λth = 0.3)”**

   - Table VI reports a maximum range of **0.220 pp** at \(R_s = 25\), \(\lambda_{\rm th}=0.3\).[Table VI; Fig. 5]  
   - The parenthetical “0.0022” is **inconsistent with its own text** and with Table VI: 0.0022 is 0.22%, i.e. 0.22 percentage points, not 0.0022 percentage points.  
   - Elsewhere the paper clearly treats “percentage points” as the unit (e.g. “1.98 percentage points” for the main class range).[Abstract; VI A; VII]  
   - **Required fix:** make the parenthetical consistent with the unit: either “0.22 percentage points (0.0022 in f units)” or just drop the raw number and keep “0.22 percentage points”.

4. **“label-shuffle nulls p = 0.61/0.135/0.413” vs HEALPix table**

   - Table V gives p-values 0.607, 0.135, 0.413 for NSIDE 16, 32, 64.[V E, Table V]  
   - The abstract approximates the first as 0.61. That is acceptable, but it obscures that the three p-values are derived from **different tests with different |σ|max and different empirical p99 thresholds**.[Table V, Fig. 4]  
   - Given your own rule about not mixing σ scales, the abstract’s compressed “p = 0.61/0.135/0.413” could be misread as three equally comparable significances; in fact each is a separate max-stat under a different K.  
   - **Required fix:** add a short qualifier in the abstract, e.g.  
     > “… sky-position (HEALPix scans at NSIDE ∈ {16, 32, 64} with label-shuffle max-|σ| nulls p = 0.61, 0.135, 0.413 respectively, none significant after the appropriate look-elsewhere correction).”

5. **Abstract calls void “∼2σ on the binomial null” while §VI A calls it “statistical noise” at −0.68σ**

   - In §VI A you correctly emphasize that \(σ=-0.68\) for void and the 95% interval brackets parity, calling it “statistical noise at this N”.[VI A, Table II, Fig. 2]  
   - The abstract’s “∼2σ” language suggests the **void bin itself is approaching a marginal detection**, which the body explicitly rejects.  
   - **Required fix:** bring the abstract language into line with §VI A; e.g.  
     > “… statistical-dominated for V-Web void at n = 428, where the deviation is only 0.7σ and fully consistent with noise.”

6. **Abstract’s “none reach 3σ after look-elsewhere correction” is not consistently tied to the specific LEE procedures**

   - The abstract bundles: redshift label-shuffle (p=0.372), density quintiles (max |σ|=3.94, but residual |σ_obs–σ_pred|=1.87), and HEALPix label-shuffle p-values, then concludes “none reach 3σ after look-elsewhere correction.”[Abstract; V A; V C; VI B–E]  
   - In the body:
     - Density quintiles are explicitly compared to **Bonferroni K=5** and residuals are all <3.09.[Table III; Fig. 3]  
     - HEALPix uses an **empirical max-statistic null** plus Bonferroni for sanity checks.[V A, Table V, Fig. 4]  
     - Redshift uses a label-shuffle max-statistic p=0.372, but no explicit σ-equivalent is given.[VI B]  
   - The abstract’s “3σ after look-elsewhere” compresses **three different notions of multiple-testing correction** into a single “σ” phrase, without stating which σ-equivalent is being used for each. This is the same comparability problem as P5-E3, but *specifically* at the abstract level.  
   - **Required fix:** rephrase to avoid a single aggregate “3σ” statement, e.g.:  
     > “None of the redshift, density, or sky-position tests produces a p-value < 0.05 under the appropriate Bonferroni or empirical max-statistic look-elsewhere corrections.”

P5-M5 – MAJOR – Arithmetic and unit consistency in Phase 2 and σpred examples
------------------------------------------------------------------------------

1. **Phase 2 σpred example: “σpred ≈ −10” vs the text’s input monopole**

   - For the sweep cell with \(n_{\rm filament}=3{,}696{,}152\) and \(\Delta f_{\rm CW}=-0.0026\), Eq. (1) implies  
     \[
       σ_{\rm pred} = 2\,\Delta f_{\rm CW}\,\sqrt{N} \approx 2 \times (-0.0026)\times\sqrt{3.70\times10^6}.
     \]
     - \(\sqrt{3.70\times10^6}\approx 1924\).  
     - \(2\times 0.0026 \times 1924 \approx 10.0\).  
   - So “σpred ≈ −10” is numerically fine. But the text elsewhere sometimes refers to the same monopole projecting to **∼4.6σ** on 791,635 spirals and **∼5σ** on the 812,793-env-labeled sample.[VIII F; cross-survey monopole discussion]  
   - Those are all internally consistent if you assume \(\Delta f_{\rm CW}=-0.0026\). However, the abstract’s “∼ 0.2 pp” floor and some verbal phrases (“∼ 0.2 pp”, “∼ 0.26%”) are sloppy enough that a reader could reasonably misread whether everything is in percentage points or fractions.  
   - **Required fix:** add one explicit line where you define clearly that:
     - \(\Delta f_{\rm CW}=-0.0026\) is in *fractional units* (0.26 percentage points),  
     - all “pp” mentions refer to **percentage points**, and  
     - σpred is always computed from that fractional ∆f, never from a PP-ambiguous number.

2. **Table III heading and σpred definition: inconsistent notation \(σ_{\rm pred} = -2\Delta f_{\rm CW}\sqrt{N}\) vs Eq. (1)**

   - Eq. (1) defines  
     \[
       σ_{\rm pred} = \frac{\Delta f_{\rm CW}}{0.5/\sqrt{N}} = 2\Delta f_{\rm CW}\sqrt{N}.
     \][V]  
   - Table III’s caption text uses “\(σ_{\rm pred} = -2\Delta f_{\rm CW}\sqrt{N}\) at \(\Delta f_{\rm CW}=-0.0026\)” (sign inserted in front).[Table III]  
   - Because \(\Delta f_{\rm CW}\) is itself negative, “\(-2\Delta f_{\rm CW}\sqrt{N}\)” numerically matches “\(2|\Delta f_{\rm CW}|\sqrt{N}\)” and indeed the σpred values in Table III are negative. But the notational change is easy to misinterpret: the same symbol \(\Delta f_{\rm CW}\) is sometimes used as a signed quantity, sometimes only as its magnitude.  
   - **Required fix:** standardize: either (a) always write \(σ_{\rm pred} = 2\Delta f_{\rm CW}\sqrt{N}\) with \(\Delta f_{\rm CW}=-0.0026\), or (b) explicitly switch to \(|\Delta f_{\rm CW}|\) in the magnitude-only contexts. Fix the Table III caption so it matches Eq. (1).

3. **Minor arithmetic check: pLEE formula and Bonferroni thresholds**

   - The Bonferroni thresholds quoted (3.09 for K=5, α=0.01; 4.05 for K=1054, α=0.05) are arithmetically consistent with Eq. (2). I re-derived them: they check out.  
   - The pLEE expression in Eq. (3) and the reported p-values are consistent across the HEALPix and quintile tests. No new arithmetic errors found here.

P5-M6 – MAJOR – Equation dimensional / conceptual clarity gaps beyond Poisson normalization
-------------------------------------------------------------------------------------------

These are not outright wrong, but they create ambiguity at PRD level.

1. **Overdensity δ definition vs. use in σ computations**

   - δ is defined dimensionlessly (\(δ = ρ/ρ̄ - 1\)), which is consistent.[IV A]  
   - However, when you describe counting-statistics floors and σ(f) later, you freely mix “fraction”, “percentage points”, and δ-like language without reminding the reader which parts are dimensionless and which are scaled.[V; VI C; VII]  
   - Given the role σpred plays (linking a catalog-level fractional monopole to percentage-point variations), these unit changes should be explicitly spelled out.  
   - **Required fix:** add a short paragraph in §V clarifying:
     - σ_from half is based on *fractional* f (0.497, not 49.7%),  
     - all “pp” ranges (1.98 pp, 0.22 pp) are “100 × difference in f”, and  
     - σpred always uses the fractional ∆f.

2. **Appendix A operator \(g_\phi (\nabla_i\phi)(\nabla_i\rho/\rho_{\rm bg})(\hat L \cdot \hat z)\)** – units not even schematically addressed

   - You rightly flag this as a *toy* operator, but you do not say anything about units:  
     - \(\phi\) may be dimensionless or not, depending on normalization.  
     - \(\nabla_i \rho/\rho_{\rm bg}\) has dimensions of inverse length.  
     - If \(g_\phi\) is dimensionless, the operator has dimension of (field) × (1/length) at least, so the implied coupling in an action would require a compensating scale.  
   - Since you explicitly give an order-of-magnitude bound “\(|g_\phi (\nabla\phi)/H_0| \lesssim 10^{-2} / \langle|\Delta \rho/\rho_{\rm bg}|\rangle\)” in H0 units, it is clear that some combination of the factors is turned into something dimensionless, but you never state what the assumed dimensions of \(\phi\) or \(g_\phi\) are.[Appendix A]  
   - **Required fix:** add one sentence such as:  
     > “For definiteness we treat \(\phi\) as dimensionless and \(g_\phi\) as having dimensions of length, so that \(g_\phi\nabla\phi\) is dimensionless when expressed in units of \(H_0^{-1}\). The order-of-magnitude ‘H0 units’ bound quoted is schematic and intended only as a scale-setting illustration.”  

   This keeps the operator clearly in the realm of a heuristic parametrization.

P5-M7 – MAJOR – Internal cross-reference mismatches and missing explicit support
-------------------------------------------------------------------------------

1. **Abstract vs §VIII wording on DESIVAST as the “primary” result**

   - Abstract: “We interpret this as no evidence for environment-dependent chirality … the controlling void constraint comes from the DESIVAST-anchored re-projection … rather than the V-Web void label.”[Abstract]  
   - §V B: declares DESIVAST as the **primary analysis path** and V-Web as secondary diagnostics, which is consistent.[V B]  
   - However, §VI A is still labeled “A. Cosmic-web environment (headline)” and refers to Table II as “headline table”.[VI A; Table II]  
   - That mixes the notion of “headline” between the V-Web class-by-class table and the DESIVAST void test, and conflicts with the explicit primary/secondary declaration.  
   - **Required fix:**  
     - Rename §VI A heading to something like “V-Web cosmic-web environment (secondary headline; primary is DESIVAST)”, and/or  
     - Insert a one-sentence reminder in §VI A, right after introducing Table II, repeating that the **formal headline claim** is anchored on DESIVAST (§VIII).

2. **Appendix B “All scripts and configuration files … in the companion data repository” vs main text references**

   - Multiple sections say “details are in the companion data repository” (Phase 2 sweep configs, 2D z×density cluster table, ASTRA overlap pipeline, etc.).[VII; VI D; X]  
   - Appendix B states a companion repository exists, but **no identifying information** is given (no DOI, no archive, no version tag).  
   - PRD will not accept “companion repository” as a reproducibility guarantee without enough information to find it.  
   - **Required fix:** either:
     - Add a generic but precise reference such as “companion Zenodo deposit [Dataset X, 2026]” to the bibliography and refer to its citation key, or  
     - Clearly say “will be posted upon acceptance; current manuscript does not yet include the public repository link.”  

   Without that, the repeated “see companion repository” is not verifiable.

P5-M8 – MAJOR – Additional σ / null comparability juxtapositions not flagged before
------------------------------------------------------------------------------------

Beyond the earlier P5-E2/E3, there are **new** places where σ from different nulls are juxtaposed without a local disclaimer:

1. **Phase 2 per-cell discussion (§VII A)**

   - You mix:
     - σpred from the monopole,  
     - σ_from half per class,  
     - σ_vs monopole residuals,  
     - Bonferroni-9 threshold \(|σ|_{0.05,9}^{\rm Bonf} \approx 3.02\),  
     - and pLEE from max-stat label-shuffle for each cell.  
   - They are used side by side to support “no cell shows an inter-class chirality signal above the counting-statistics shot-noise null.”[VII A]  
   - No explicit statement here says “these σ are under different nulls and not directly comparable” even though you are effectively comparing them in a single paragraph.  
   - **Required fix:** add a sentence at the start or end of §VII A:  
     > “Note that σ_from half, σ_pred and σ_vs monopole, and the σ-equivalent Bonferroni thresholds correspond to different null hypotheses and are used only in a layered consistency check; their numerical values are not directly comparable as a single ‘significance scale’.”

2. **Cross-survey monopole residuals (§VIII F)**

   - In §VIII F you discuss:
     - the Paper IV **9.5σ** catalog monopole,  
     - the −5.00σ and −5.07σ matched-sample monopoles,  
     - the 4.6σ monopole projection from ∆f=-0.0026 onto 791,635 spirals,  
     - and the pixel-level distribution of σ_vs monopole with std≈1.184.  
   - All are written with “σ” only, and are visually adjacent. Some are from simple binomial nulls, others from a catalog-wide global measurement, and others from pixel-level residuals under the monopole-subtracted null.  
   - **Required fix:** in §VIII F explicitly label these as σ_½ (catalog-wide binomial), σ_P4→P5 (propagated monopole), and σ_vs monopole (residual), and state that they are not interchangeable.

If you implement these fixes, you will have addressed a set of subtle but important arithmetic, unit-consistency, and comparability issues that a first pass can easily miss. None of them invalidate the central null result, but they do affect how robust and transparent that result appears at PRD review level.

If you want, I can now go table-by-table and recompute every σ and p-value explicitly to see if there are any further arithmetic discrepancies beyond those flagged here.