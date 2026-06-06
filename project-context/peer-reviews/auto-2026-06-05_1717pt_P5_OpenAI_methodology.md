# P5 auto-2026-06-05_1717pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9021 chars)
**Wall time**: 261.0s

---

Referee report on “Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Test on 56,981 Void Spirals with V-Web Cross-Check Across 791,635 DR1 Matched Spirals”

Scope of review
I reviewed the full 20-page manuscript, including all tables, figures, equations, captions, and the abstract. I checked arithmetic consistency, dimensional consistency, null-procedure usage, multiple-testing controls, and recomputed all quoted simple statistics (fractions, σ-from-half, ranges, p-values where determinable, and ratios) from the numbers provided.

Findings are grouped by severity as required.

ESSENTIAL

P5-E1 (Section V, page 4): Algebraic error in Eq. (1) defining σpred
- Offending text/equation: “σpred = ΔfCW/0.5/√N = 2·ΔfCW·√N (1)”
- Problem: As written, ΔfCW/0.5/√N equals 2ΔfCW/√N, not 2ΔfCW√N. The second equality is algebraically incorrect. The intended relation for your z-like statistic σfrom half = 2(fCW−0.5)√N implies σpred = 2ΔfCW√N, which is consistent with your later numerical use. The displayed “ΔfCW/0.5/√N” is wrong.
- Required fix: Correct Eq. (1) to an unambiguous, algebraically correct form, e.g.
  σpred = 2ΔfCW√N
  or equivalently σpred = (ΔfCW/0.5)·√N. Remove the erroneous chained division.

P5-E2 (Section V.B, page 5): Bonferroni z-threshold miscomputed for K=5 at α=0.05
- Offending text: “Treating the five DESIVAST estimators as a Bonferroni-5 family at α = 0.05, the per-test threshold is |σ|Bonf0.05,5 ≈ 2.81…”
- Problem: For a two-sided normal, Bonferroni per-test level α/K = 0.01 implies |σ| ≈ 2.576, not 2.81. Your own Eq. (2), |σ|Bonfα,K = √2 erfc−1(α/K), gives 2.576 for α/K=0.01. 2.81 corresponds to α/K≈0.005 (two-sided). This threshold error propagates to statements about “no DESIVAST estimator crosses it.”
- Required fix: Correct |σ|Bonf0.05,5 to ≈ 2.58 throughout; re-evaluate any “crosses/does not cross” statements that rely on 2.81. If you intend a different family-wise control (e.g. extra conservatism), state it explicitly and adjust Eq. (2) accordingly.

P5-E3 (Abstract; Section VIII.F, page 12): Data/code availability not actionable
- Offending text: “Analysis drivers are available in the companion data repository.” and Appendix B: “All scripts and configuration files are available in the companion data repository.” No URL/DOI is provided.
- Problem: PRD requires reproducibility. A vague “companion data repository” without a resolvable URL/DOI is not sufficient.
- Required fix: Provide stable, public DOIs/URLs for:
  - The “companion data repository” (code, configs, outputs)
  - Exact commit hashes or release tags for code
  - Any large intermediate products (e.g. V-Web grids, per-galaxy labels) that are not trivially reproducible from raw data
  If the repository is private, make it public upon submission or provide a Zenodo (or equivalent) archival DOI.

MAJOR

P5-M1 (Section VI.A, page 5): Miscomputed example σpred for filament class
- Offending text: “predicting σpred from ΔfCW = −0.0026 gives σpred(filament) ≈ −3.16 and σpred(cluster) ≈ −3.28…”
- Problem: With nfilament = 408,187, σpred = 2·(−0.0026)·√n ≈ −0.0052·638.9 ≈ −3.33, not −3.16. The cluster value −3.28 is consistent. The filament discrepancy is ~0.17σ and undermines trust in numeric care.
- Required fix: Recompute and correct the filament σpred (≈ −3.33). Audit the manuscript for any other σpred values computed from Eq. (1) and correct as needed.

P5-M2 (Section VII, page 9): Ambiguity and possible sample-size mismatch in “largest single-cell |σfrom half|”
- Offending text: “The largest single-cell |σfrom half| across the entire sweep is 11.32 (filament at Rs = 10, λth = 0, n = 3,696,152). This is the catalog-wide ΔfCW = −0.0026 monopole leaking through the largest sample bin and is predicted, not measured…”
- Problem: You present an “observed 11.32” on a sample with n = 3.7×10^6, but there are only 7.9×10^5 chirality-relevant matched spirals. It is unclear whether this 11.32 is computed on the 14.6M spectroscopic parent (which has no chirality labels) or on a subset. The phrase “observed” contradicts “predicted, not measured.”
- Required fix: Clarify explicitly:
  - On which dataset is |σ|=11.32 computed?
  - If it is a prediction using N from DR1 spectroscopic counts, do not label it “observed” and do not list a per-class n that is not a chirality-labeled sample. Provide the corresponding matched-spiral n and the measured σ if you want to juxtapose a measurement.
  - Alternatively, move this to a short “sanity check” paragraph that strictly presents predicted scaling only (no “observed”).

P5-M3 (Abstract; Section V.B, pages 1 and 5): Primary estimator declared post hoc
- Offending text: Abstract frames DESIVAST-anchored cross-check as “primary”; Section V.B admits “a single a priori preregistered analysis plan was not filed… we designate the DESIVAST-anchored void cross-check as the primary… post hoc.”
- Problem: PRD requires methodological clarity. Declaring the “primary” analysis after exploring multiple analyses is acceptable only if the claims are correspondingly tempered and the LEE/multiplicity is handled conservatively across all forks taken.
- Required fix: In the Abstract and Conclusions, explicitly state that the “primary” path was designated post hoc and that all look-elsewhere/multiplicity concerns were handled by treating other paths as diagnostics only. Tighten language that could be read as preregistered. Consider moving the “primary/secondary” declaration earlier (end of Introduction) and clearly marking which results are confirmatory vs. exploratory.

P5-M4 (Section VIII, pages 10–12): “Essentially RSD-immune” claim needs quantification or softening
- Offending text: “The DESIVAST primary path is essentially RSD-immune…” followed by a qualitative argument.
- Problem: The “essentially RSD-immune” statement is stronger than what is demonstrated. You provide order-of-magnitude displacement heuristics and then acknowledge anisotropic tidal-tensor deformations cannot be bounded without reconstruction. Even if the void/non-void binary is expected to be robust, this needs quantitative support.
- Required fix: Either (a) soften to “we expect RSD effects to be sub-dominant for the binary DESIVAST void/non-void membership at our precision; we do not quantify them here,” or (b) provide a quantitative bound (e.g., mock-based or via real/rec RSD toggling) that shows the void/non-void ΔfCW changes by < 0.1–0.2 pp under RSD.

P5-M5 (Section VI.D, page 6–7): χ2 contingency claim not reproducible as stated
- Offending text: “A two-way contingency test… gives χ2 = 4932, 3 d.o.f., p < 10−1000… Contingency-test reproduction is a χ2 on the env-class × tracer-program cross-tab derivable from the desi_env_vweb.parquet + matched-spiral catalog join documented in §IV A.”
- Problem: The manuscript does not provide the actual 4×2 table counts (or even per-class bright/dark counts), so the quoted χ2 cannot be verified from the paper alone. The “parquet” reference is to an unspecified repository (see P5-E3).
- Required fix: Add the 4×2 contingency table (counts) to the paper (main or appendix) so that χ2 is directly verifiable. Alternatively, supply it as a short machine-readable table with a DOI in the data repository and cite the DOI and filename.

MINOR

P5-n1 (Section III.D, page 3): “≤ 4% band” is not accurate
- Offending text: “{0.5, 1.0, 2.0, 3.0, 5.0}′′ produces {2.34, 2.35, 2.37, 2.39, 2.44}×10^6 matched-primary rows, a ≤ 4% band.”
- Problem: 2.44/2.34 ≈ 1.0427 → 4.27% change. The band slightly exceeds 4%.
- Required fix: Replace “≤ 4%” with “≈ 4.3%” (or “≈ 4%”).

P5-n2 (Table II; Section VI.A, page 5): Small discrepancies in computed σfrom half
- Observed: Recomputing σfrom half from the displayed class counts yields −2.54 (filament) and −4.71 (cluster), while the table shows −2.61 and −4.66. These are within rounding/precision, but please verify the exact numbers and ensure consistent rounding/display rules (e.g., report to 0.01σ).
- Required fix: Either reconcile the printed σ to match recomputation from n and nCW or specify rounding rules.

P5-n3 (Section V.A, page 4): Two-sided vs one-sided z conventions
- Offending text: Eq. (2) uses |σ|Bonfα,K = √2 erfc−1(α/K) but later mixes α=0.01 and 0.05 use cases without restating two-sided convention.
- Problem: Minor clarity. You appear to consistently use two-sided Bonferroni thresholds; make this explicit wherever thresholds are quoted to avoid ambiguity.
- Required fix: Add a brief sentence clarifying that all Bonferroni z-thresholds are two-sided unless stated otherwise.

P5-n4 (Section VIII.F, page 12–13): Internal shorthand “P5” in the body text
- Offending text: “the P5 matched-spiral catalog monopole fP5CW = 0.4972…”
- Problem: “P5” is internal-series shorthand and can confuse readers unfamiliar with your suite of companion papers.
- Required fix: Replace “P5” with “this paper” or “the DR1-matched sample in this work.” Retain “Paper IV” where it denotes the external companion dataset.

P5-n5 (Section VI.E/Table V; Abstract): Minor rounding mismatch in HEALPix p-values
- Offending text: Abstract “p= 0.61/0.135/0.413”; Table V lists 0.607/0.135/0.413.
- Required fix: Harmonize rounding (e.g., 0.61→0.607).

P5-n6 (Section XI, page 17): Ambiguous variable name
- Offending text: “confidence-threshold sweep pmaxcls_eq ∈ {0.4, …}”
- Problem: The variable name is unexplained in the main text; readers unfamiliar with your classifier code will not know what this is.
- Required fix: Define pmaxcls_eq clearly (e.g., “maximum softmax probability of the equivariant CW/CCW classifier”) at first use.

P5-n7 (Section X, page 16): Entropy-weighted ASTRA aggregation variance statement needs a cite or brief derivation
- Offending text: “sub-class variance Σi P^2_i/4 under the Bernoulli-0.5 null”
- Problem: This is plausible but not obvious. A one-line derivation or a citation would improve clarity.
- Required fix: Add a brief derivation in a footnote or cite a reference for probability-weighted Bernoulli variance aggregation.

NITS (cosmetic)

P5-N1 (Throughout): Formatting of Ngrid
- Offending text: “Ngrid = 2563”
- Problem: This is typographically ambiguous. It should be 256^3.
- Required fix: Replace “2563” with “256^3” throughout.

P5-N2 (Section IX.A, pp. 13–16): Figure 7 y-axis shared limits vs text
- Observation: You state the shared y-axis is [0.43, 0.53], which is quite wide given the plotted ranges. It is fine, but consider tightening for readability.
- Suggested fix: Optional; consider [0.47, 0.53] or annotate ranges directly.

P5-N3 (Section VI.D, page 6): Phrase “The class boundary is verifiable quantitatively from the table” reads informal
- Suggested fix: Replace with “The overlap in mean densities across quartiles confirms boundary overlap.”

P5-N4 (Section VI.D, page 7): Use of “p < 10−1000”
- Suggested fix: Replace with “p effectively zero within double precision (p < 10−300)” or provide an exact computed p-value to machine precision; extremely small p-values can be reported as “p ≪ 10−16”.

Length and focus
The manuscript is long (20 pages) for a largely null result whose core is the DESIVAST-anchored void/non-void ΔfCW ≈ 0.0007 null and a V-Web cross-check. I recommend tightening to ≲12–14 pages by:
- Moving detailed secondary diagnostics (e.g., some of the within-class quartile tables, redundancy across repeated null statements, and the ASTRA cross-check details) to an appendix or data repository, while keeping one succinct diagnostic paragraph each in the main text.
- Collapsing the Phase-2 sweep narrative by keeping the heat map plus one paragraph (move internal per-cell discussions to appendix).
- Trimming repeated restatements of the Paper IV monopole and focusing on the necessary quantitative carryover.

Audit of abstract and conclusion scalars
- Sample sizes (2,232,212 matched unique; 791,635 chirality-relevant; 14,622,283 in parent spectro sample) match Tables I and IV steps.
- Per-class fCW and σ in abstract match Table II.
- “Range across classes is 1.98 pp” recomputes as 0.5034−0.4836=0.0198: correct.
- Phase 2 max range “0.22 pp” matches Table VI (0.220). Parenthetical “0.0022” is consistent.
- Redshift null p=0.372: matches Section VI.B.
- Density quintiles |σ|max=3.94, residual |σobs−σpred|=1.87, Bonferroni: consistent with Table III and |σ|Bonf0.01,5 ≈ 3.09.
- HEALPix p-values 0.61/0.135/0.413: very close to Table V (0.607/0.135/0.413).
- DESIVAST void/non-void fCW 0.4964 vs 0.4971 and Δf=0.0007: matches Table VII.
- “Three-algorithm DESIVAST robustness |ΔfCW| < 0.002”: matches Table VIII.
- “Per-pixel Pearson r=+0.006 (p=0.88)”: matches Figure 6 caption/body.
- Caveat: The filament σpred ≈ −3.16 in the body is inconsistent (P5-M1). Ensure all such example σpred values are corrected.

## Summary recommendation
MAJOR REVISIONS

The core methodology is sound and the main numerical results are mostly consistent; however, the manuscript contains an algebraic error in a load-bearing equation (Eq. 1), a miscomputed illustrative σpred, an incorrect Bonferroni threshold for K=5 at α=0.05, and an ambiguous “observed” σ claim tied to a sample size that cannot possess chirality labels. In addition, data/code availability lacks a DOI/URL, and several clarity and reproducibility points require attention (contingency table counts, RSD claim softening or quantification). These are all fixable, but they must be corrected before the work can meet PRD’s methodological rigor standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDENDUM: Additional findings from a second-pass audit (new items only)

ESSENTIAL

P5-E4 (Section IV, throughout): Classifier misidentified as “V-Web” while implementing a T-Web-like tidal-tensor pipeline; sign convention ambiguity
- Offending text: Section IV repeatedly calls the method “V-Web tidal-tensor classifier,” cites Hahn+2007/Hoffman+2012/Cautun+2014, and algorithm Step 8–11 solves Poisson from density and builds Tij(k) = kikj Φ(k).
- Problems:
  1) V-Web (Hoffman+2012) is a velocity-shear classifier requiring the peculiar-velocity field (Σij), not the Hessian of the gravitational potential from density. What is implemented here (Poisson from δ, Hessian/eigenvalues, λ-threshold) is T-Web-like (Hahn+2007), not V-Web. The paper’s method labeling is therefore incorrect.
  2) The Fourier-space form of the Hessian is missing the conventional minus sign: ∂i∂jΦ ↔ −kikj Φ(k). With Φ(k) = −δ/k^2, the standard T-Web tensor becomes Tij ∝ (kikj/k^2) δ (sign-agnostic under λth = 0 up to a global positive factor), but the written Tij = kikj Φ(k) corresponds to −(kikj/k^2) δ, i.e., an overall sign flip relative to the usual T-Web convention. With λth = 0 a global sign flip can invert the “> 0”/“< 0” assignment and thus swap void/sheet/filament/knot counts unless you explicitly define the inequality relative to that sign.
- Required fix: Either (a) relabel the method as T-Web (and adjust citations accordingly), or (b) if you intend to follow V-Web, provide the velocity-field construction and velocity-shear tensor details. In all cases, correct the tensor’s Fourier sign and state explicitly how the sign/normalization affects class labels with λth = 0. Provide a short sanity check of class volume fractions under both sign conventions to prove invariance of the qualitative results.

P5-E5 (Section XI vs Section VI.D): Direct contradiction on BGS vs dark split
- Offending texts:
  - Section VI.D(b): bright fCW = 0.4970 vs dark 0.5051 (|z| ≈ 3.4σ difference).
  - Section XI: “target-class split (BGS vs. LRG-ELG-QSO) with BGS-only CW fraction within ±0.001 of LRG-ELG-QSO.”
- Problem: These two statements are incompatible. The measured bright–dark difference is ≈0.0081 (8.1 pp), not within ±0.001.
- Required fix: Correct Section XI to reflect the actual measured difference, or clarify that Section XI refers to a different dataset/cut. Provide the exact numbers or point to a DOI’d table.

MAJOR

P5-M6 (Section VIII.F, page 12–13): Undefined “env-label confidence” filter controlling the 812,793 vs 791,635 sample sizes
- Offending text: References to a “relaxed env-label confidence” for 812,793 and a “stricter env-class-uncertainty filter” for the 791,635 headline set.
- Problem: No definition of the confidence metric, no threshold value(s), and no per-class counts lost by the stricter filter are provided; the filter cannot be reproduced or audited.
- Required fix: Define the confidence metric formally (how computed, range, threshold), list thresholds used, give per-class counts before/after, and provide a DOI to the filtered/unfiltered lists. If based on interpolation distance, eigenvalue stability, or mask proximity, specify it.

P5-M7 (Multiple locations: Section VII table/caption; Abstract; IV A Sweep description): Notation/units consistency and table labeling in Phase-2 sweep
- Offending texts:
  - Table VI header says “fCW range (pp)” and values include 0.066, 0.220, etc. The Abstract also uses “0.22 percentage points (max 0.0022...)”.
  - Sweep description: “Rs ∈ {10, 25, 50} Mpc/h × Ngrid = 256 × λth ∈ {0.0, 0.1, 0.3}.”
- Problems:
  1) The table values are numeric fractions labeled as “pp.” 0.220 is 0.22 pp (i.e., 0.00220 in fractional units). Ensure every occurrence is explicitly stated in pp or fractional units, not both interchanged within the same context.
  2) “Ngrid = 256 × λth ∈ {...}” is likely a typographical error; Ngrid should be 256^3 and unrelated to λth.
- Required fix: Standardize units in table/captions (“pp” vs fraction) and correct the sweep description (“Ngrid = 256^3; λth ∈ {...}”).

P5-M8 (Section V.E; multiple locations): Pixel-selection criteria inconsistencies in HEALPix analyses
- Offending texts:
  - Table V: NSIDE=32, npix=3,303.
  - Figure 6 caption: bottom panel uses ≥200-spiral pixels: 1,496 valid pixels; correlation across n_both_pix = 727.
  - Section VIII.F: σvs-monopole distribution is “across the 1,821 valid pixels,” but no selection criterion is stated there.
- Problem: Different pixel counts (3,303; 1,496; 1,821; 727) are used for different statistics without consistently stating the selection thresholds (e.g., “≥ 200 spirals,” “≥ 1 maximal void,” or none). This blocks reproducibility and can change results.
- Required fix: For every HEALPix analysis, state the exact inclusion criteria (min spirals per pixel; DESIVAST-void occupancy requirement; footprint mask), and report the resulting npix for each statistic in-text. Add a small table (or DOI’d CSV) enumerating npix per criterion.

MINOR

P5-n8 (Section VI.A, page 6): Void-bin smallness explanation references the wrong volume fraction
- Offending text: “The void bin has only n = 428… (the small cluster volume fraction of 1% plus the sparse r ≤ 17.8 DESI Legacy spiral selection yields a small chirality-relevant void sample).”
- Problem: The sentence cites the cluster volume fraction when discussing the void bin size; this reads as a copy/paste error and confuses the rationale (few galaxies inhabit low-density void volumes, not that clusters occupy 1% volume).
- Required fix: Replace “cluster volume fraction of 1%” with a correct explanation tied to galaxy sparsity in void regions (e.g., “galaxies avoid void volumes despite their large volume fraction”).

P5-n9 (Section VIII.B, page 11): KDTree neighbor count justified with an unreferenced “24 Mpc/h maximum hole radius”
- Problem: You state k = 20 is “sufficient given the 24 Mpc/h maximum hole radius,” but elsewhere you cite larger effective radii for other algorithms (e.g., V2-REVOLVER max 43.5 Mpc/h; V2-VIDE 55.9 Mpc/h). The “24 Mpc/h maximum” is not supported in-text for VoidFinder holes.
- Required fix: Provide the actual measured maximum VoidFinder hole radius from the catalog (and the typical hole spacing), or remove the numeric justification and simply report a convergence check (e.g., results invariant for k = 20–100).

P5-n10 (Section IX.B, pages 15–16): T-Web vs your classifier volume-fraction comparison needs concrete numbers
- Offending text: “V-Web’s void fraction is higher than T-Web’s by +8–18 pp... and cluster lower by 3–5 pp.”
- Problem: These ranges are asserted without a side-by-side numeric table. The BGS example is inferable (0.244 vs ~0.16 → +8.4 pp), but “+18 pp” and “−5 pp” require showing the exact tracer/sample used.
- Required fix: Add a small 2×4 table with your in-footprint volume fractions vs the cited T-Web fractions per tracer (BGS/LRG/ELG) and explicitly compute the deltas stated in the text.

P5-n11 (Section VI.B, page 6): Logistic regression claim lacks uncertainty
- Offending text: “A logistic regression... gives a z-coefficient of 0.0059 with no significant intercept (0.000652)...”
- Problem: No standard errors or p-values are reported for the coefficients; “no significant” is unsupported.
- Required fix: Report coefficient estimates with standard errors and p-values (or CIs), and list covariate scaling so the magnitudes are interpretable.

P5-n12 (Section V, nulls; general): Position-shuffle null needs boundary handling description
- Problem: The position-shuffle “scrambles positions” but does not state whether shuffles are constrained to the footprint/mask (and how the mask is handled).
- Required fix: Specify whether positions are shuffled within the survey mask (and within-class counts preserved), or if another boundary correction is used.

NITS (cosmetic/clarity)

P5-N5 (Throughout IV/V): Clarify that all quoted Bonferroni thresholds are two-sided (you generally follow this, but please restate it at first use in each subsection to avoid confusion).

P5-N6 (Section V, Eq. labeling and typography): Use “256^3” instead of “2563” consistently (there are a few lingering occurrences beyond those already noted).

P5-N7 (Section VIII.D, page 12): “16,000–17,000 galaxies per algorithm” is imprecise; consider replacing with exact counts or move to an appendix table.

P5-N8 (Figure 7): Consider tightening the shared y-axis range for readability as previously suggested; alternatively annotate each panel with its numerical range.

Why these were missed initially
The first-pass focused on equation correctness, headline scalars, multiple-testing control, and code/data availability. The deeper second-pass comparison of the algorithmic description to the V-Web vs T-Web literature, cross-check of HEALPix selection thresholds across sections, and the internal consistency between Section VI.D and XI surfaced additional inconsistencies and mislabeling that were not apparent on a single linear read.