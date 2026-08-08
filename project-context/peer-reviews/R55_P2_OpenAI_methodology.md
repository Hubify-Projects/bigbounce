# P2 R55 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R55_P2/02_full_draft.pdf` md5=6420ec92 pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7330 chars)
**Wall time**: 310.2s

---

Referee report on “Testing the Matter Bounce with Primordial Non‑Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope of review
- Role: methodology/statistics referee. I audited the derivation chains, dimensional consistency, estimator declarations, all quoted numerical factors and significances, and the consistency between abstract, body, tables, and figures. All page references below refer to the rendered PDF pages indicated in the submission.

Overall assessment
The manuscript presents a sensitivity recast of SPHEREx and speculative MegaMapper constraints on the matter-bounce prediction flocalNL = −35/8. It includes: (i) a template-overlap analysis showing the “matter-bounce” bispectrum is close to local (r ≈ 0.83–0.88 depending on survey weighting), (ii) a consolidated systematics budget for a SPHEREx bispectrum-only forecast using Heinrich et al. (2024) σ(fNL) ≈ 0.7 as baseline, and (iii) a closed-form Bayesian model comparison versus tuned multi-field competitors. Much of the numerical bookkeeping is careful, with explicit recomputable inputs and consistency checks.

However, there are multiple methodology-critical issues that must be resolved for PRD. The most serious are (a) reproducibility/provenance gaps (Zenodo DOI placeholder and lack of frozen code release), (b) several claims in the abstract labeled as “realistic” that are in fact based on a heuristic GR-nuisance parameter not calibrated to SPHEREx by a proper joint Fisher pipeline, and (c) unsupported performance claims (10–20% from anomaly-selected tracers) without a documented Fisher setup. In addition, several load-bearing internal calculations (e.g., “SPHEREx-like” weighting used to get r = 0.84, the injection–recovery setup) require fuller specification to be auditable, and the “Li vs Cai” operator-factor-of-two resolution should include at least one explicit vertex-level worked example to tie the general −2 Im identity to the specific integrands used in the literature.

Below I catalog all findings grouped by severity.

ESSENTIAL (must be fixed before the paper can be considered)
P2-E1. Data/code provenance placeholder
- Location: Data and Code Availability (p. 24)
- Problem: “archived at Zenodo (DOI inserted at submission)” is a placeholder. No DOI or frozen release tag is provided. Numerous artifacts are referenced in the body by filename (e.g., c9i epsilon ratio check.json, phase3 bispectrum shape overlap.json), but there is no immutable pointer to a specific release/commit.
- Required fix: Provide a permanent Zenodo DOI and the exact git commit hash/tag of the code used to produce every figure/table and all quoted numbers. Ensure the repository contains the named artifacts and a Reproduce.md mapping each paper result to a script and input. Remove all “inserted at submission” placeholders.

P2-E2. Abstract overstates realism of the 2.6–5σ range
- Location: Abstract (p. 1)
- Problem: “reducing to a realistic ∼ 2.6–5σ after the systematic budget” is derived from a parameterized GR-nuisance σGR added in quadrature (Table IV; §VII), explicitly labeled a “transparent scoping choice” and “stress-test amplitude grid,” not a SPHEREx-calibrated joint Fisher. Calling this “realistic” in the abstract is too strong.
- Required fix: Reword the abstract to make clear that 2.6–5σ is a scoping/stress-tested range under a parameterized systematics model (not a calibrated, survey-optimized joint Fisher). Suggested wording: “reducing to a plausible ∼2.6–5σ range under a parameterized systematics model (GR projection, bϕ marginalization, photo‑z), to be confirmed by a full joint Fisher.”

P2-E3. Unsupported 10–20% anomaly-tracer improvement claim
- Location: §IV (p. 10, “Anomaly-detected QSO candidates … offer an independent route … project a ∼10–20% improvement … upper bound pending the shot-noise-corrected Fisher analysis…”)
- Problem: The 10–20% improvement is asserted without a documented Fisher setup (volumes, number densities, biases, k-ranges, treatment of shot noise/catastrophic z). It is used as a motivator but lacks a derivation or reproducible artifact.
- Required fix: Either (a) provide a minimal Fisher calculation (inputs, equations, plots, and the exact script/commit) quantifying the gain, or (b) remove the numerical 10–20% claim and replace with a qualitative statement that anomaly-selected tracers could diversify multi-tracer analyses, with no quantitative promise.

P2-E4. Insufficient specification of “SPHEREx-like/LSS” weights used to obtain r = 0.84
- Location: §III.B (pp. 8–9) and Table IV (pp. 20)
- Problem: The central result r = 0.84 ± 0.02 hinges on “SPHEREx-like” and “LSS/SDB 1/k²” Fisher weights. The paper does not provide explicit weight formulas, k-cuts, redshift weighting, T(k), D(z), shot-noise terms, or photometric-z kernel used in these noise-weighted overlaps.
- Required fix: Provide the exact survey/Fisher weights used in the r computation: explicit w(k1,k2,k3; z) definition(s), kmin/kmax per bin, redshift weighting, transfer functions, growth factors, and any shot-noise/photo‑z kernels. Include a reference or post a small table summarizing the configurations and the resulting r values. Point to the code function and commit.

P2-E5. Provide at least one explicit vertex-level worked example for the Cai vs Li factor-of-two
- Location: Appendix A.1–A.2 (pp. 25–27) and §II.C–§II.A (pp. 6–7)
- Problem: The general −2 Im commutator identity is correct, but the paper does not show a concrete mapping for any one of the Maldacena cubic vertices demonstrating that Li et al.’s printed single-ordering integrand indeed reproduces exactly half of Cai et al.’s full commutator result for that integrand. Given this is a load-bearing resolution of a literature discrepancy, one explicit vertex-level numeric check is appropriate.
- Required fix: Add a short worked example (e.g., Lζ ż² term): write the single time-ordered integral Iv for a specific triangle (e.g., equilateral), evaluate numerically, show that doubling via −2 Im recovers the Cai et al. full result. Provide the script path/commit that performs this check.

MAJOR (significant revision required)
P2-M1. Injection–recovery details insufficient for the stated precision
- Location: §II.A (pp. 5–6)
- Problem: The flat-sky KSW injection–recovery reports rmeasured = 0.90 ± 0.01 from 200 realizations but omits key specifics: multipole range, patch size/tiling, pixelization/beam, noise normalization per patch, how “SPHEREx photometric‑z power spectra” were converted into a 2D diagonal noise covariance, and the estimator normalization. Without these, the quoted ±0.01 cannot be audited.
- Required fix: Provide the simulation details (ℓmin–ℓmax, pixelization, beam=1 or otherwise, normalization of the KSW filters), the exact mapping from 3D photo‑z noise to a 2D diagonal covariance, and the script/commit. Alternatively, demote this to a qualitative cross-check without reporting ±0.01 and move details to Supplement.

P2-M2. MegaMapper abstract claims need softening and clearer provenance
- Location: Abstract (p. 1) and §V (p. 11)
- Problem: The abstract’s “MegaMapper … could reach σ(fNL) ≈ 0.5 ideally, projecting an illustrative 3–7σ envelope…” is not tied to a specific instrument design. The 3–7σ range partly reuses SPHEREx systematics with no MegaMapper-specific calibration and is explicitly “illustrative” in the body. Abstract language should reflect this.
- Required fix: In the abstract, qualify MegaMapper numbers as “illustrative Stage‑V targets based on published ideal σ(fNL) ≈ 0.5 and our template‑mismatch correction; the 3–7σ envelope reflects design and systematics uncertainty.” Keep the detailed caveats in §V.

P2-M3. Photometric‑z catastrophic outlier degradation claim lacks derivation
- Location: §VII.D (pp. 18–19; “even with 10% catastrophic outlier fraction, σ(fNL) degrades by only ∼5% … follows from a first‑order Fisher correction”)
- Problem: No derivation, inputs, or simulation are provided, and the statement is used to downplay a known difficult systematic. A one-line heuristic with fcat lacks credibility without explicit modeling.
- Required fix: Provide the simple Fisher derivation (what cross-spectrum(s), how modes are scattered, which k bins, what fcat mapping was assumed), or remove the 5% number and simply state that “robustness to realistic photo‑z outliers must be validated with survey‑grade mocks; we expect bispectrum to be more robust than SDB.”

P2-M4. Joint (fNL, nfNL) SDB Fisher requires basic methods specification
- Location: §IX.D (pp. 21–22)
- Problem: Reported σ(nfNL) = 0.295 (fixed-bias) and σmarg(fNL) = 3.08/7.06, but the setup (number densities per bin, biases, volumes, k‑ranges, kmin, treatment of window/mask) is not specified in the text. Readers cannot audit the magnitudes.
- Required fix: Add a short methods paragraph with survey inputs (bin edges, fsky, n(z), b1(z), kmin/kmax, P(k) model), and point to the exact script and commit producing the Fisher matrices.

P2-M5. “SPHEREx-like” triangle-grid domain unspecified
- Location: §II.A (pp. 4–5)
- Problem: The 23,098 triangle grid is said to be dimensionless and “scale free,” but finite kmin/kmax and bin counts were used, and for noise-weighted overlaps these bounds matter.
- Required fix: State the (kmin, kmax) used to build the triangle grid for each weighting (or explicitly state that dimensionless triangle ratios only were used and how the weighting was made dimensionless), and confirm insensitivity with a quantitative test.

P2-M6. SVD conditioning statistic (σ3/σ1 ≈ 0.3) presented without context
- Location: §II.A (p. 4)
- Problem: The number is presented as a property of the 3×6 constraint matrix but cannot be checked. As it underpins the null-space dimension/scatter that propagates to r, a brief matrix snapshot is needed.
- Required fix: Provide the explicit 3×6 matrix (values of the six monomials at the three benchmark triangles), or include it in the repository and reference it.

P2-M7. Frequent references to internal artifact names in the main text
- Location: §II.A (p. 3–4), Appendix A (p. 26)
- Problem: Internal filenames like “c9i epsilon ratio check.json” appear in the prose. That is distracting and inappropriate for the body of a PRD article.
- Required fix: Move all artifact filenames to the Data and Code Availability section or Supplement. In the body, reference artifacts generically (“see the repository artifact validating X”).

MINOR (address but paper can proceed)
P2-m1. Clarify the use and meaning of “optimistic,” “realistic,” and “conservative”
- Location: Abstract (p. 1), §IV and Table IV (pp. 10, 20)
- Problem: Multiple bands are shown: 5.2–5.5σ (optimistic), 3.0σ (GR-only floor), 2.6–2.8σ (all-combined endpoint), and 2.6–5σ (realistic). This is mostly clear in the body, but the abstract could better map each number to the combination rule.
- Required fix: In the abstract, parenthetically map each band to the assumptions (e.g., “optimistic: r‑corrected σ=0.7 only; realistic: add σGR=0.5–1.0 and bϕ prior widening to σ=0.9–1.0”).

P2-m2. Confirm unit labels on all axes
- Location: Figures 1–5 (pp. 5, 11, 17–18)
- Problem: The text states k is in h Mpc−1 and BNL is dimensionless. Ensure all panel axes reflect units explicitly where applicable (k, kmin).
- Required fix: Verify and, if needed, update axis labels to include units.

P2-m3. Tiny arithmetic rounding
- Location: §II.A (p. 5): “4.4σ × (0.7/√(0.7²+1.0²)) ≈ 2.5σ”
- Problem: Numerically 0.7/√1.49 ≈ 0.573; 4.4×0.573 = 2.52σ. Within rounding; consider quoting 2.52σ → 2.5σ.
- Required fix: None strictly required; optional to standardize rounding style.

P2-m4. Consistent symbol usage for r (overlap) vs rt (tensor-to-scalar ratio)
- Location: §II.D (p. 7)
- Problem: The text introduces rt to avoid confusion; check that r is never used for tensor after that point.
- Required fix: Quick internal sweep; correct if any stray “r” denotes the tensor ratio.

P2-m5. Citations for PR4 Planck PNG constraint
- Location: §VIII.A (p. 18)
- Problem: Jung et al. (2025) cited with fNL = −0.1 ± 5.0; ensure this is consistent with the cited paper’s abstract/tables.
- Required fix: Verify citation numbers match the reference; if they differ, update.

NIT (cosmetic)
P2-n1. Overlong manuscript for a sensitivity recast
- Location: entire manuscript (28 pages)
- Problem: The contribution is a rigorous sensitivity recast plus a template-overlap study. At 28 pages, the narrative is verbose and repeats caveats many times.
- Required fix: Consider trimming to ~18–20 pages by moving long explanatory asides (e.g., extended curvaton/QSFI digressions, repeated caveats about GR parameterization, internal filename references) to an Appendix or Supplement.

P2-n2. Minor typographical and punctuation issues
- Location: scattered
- Examples: “M¨unchmeyer” (ensure proper LaTeX encoding), occasional hyphenation artifacts (e.g., “bispectrum￾only”), inconsistent use of en-dashes.
- Required fix: Run a final copy-edit pass to eliminate encoding artifacts and soft hyphen remnants from PDF extraction.

Arithmetic and consistency audit highlights (pass)
- Ratio |−4.375|/0.015 ≈ 292 (Abstract): correct at the quoted precision (“≈ 290”).
- Template-corrected significance: 4.375×r/0.7 ⇒ 5.19–5.47σ for r ∈ [0.829, 0.876]: consistent with 5.2–5.5σ.
- GR-only floor: 4.375×0.84/√(0.7²+1.0²) ≈ 3.01σ: matches 3.0σ.
- All-combined endpoints: with σ(fNL)=0.9–1.0 and σGR=1.0 give 2.73–2.60σ: matches 2.6–2.8σ.
- Planck PR4 recast to bounce template using rCMB = 0.876: σ → 5.7; offset 0.75σ from bounce and 0.02σ from zero: numerically consistent.
- Bayes factors: analytical results (Eq. 9–10) match the reported numbers (e.g., delta/broad σeff = 0.7 gives 17.1; rebooked σeff = 0.833 gives 14.4). The narrow-competitor entries correctly include finite CDF tails.
- τNL estimate (SY equality): (36/25)*(35/8)² ≈ 27.56: correct.

Dimensional analysis and estimator declarations
- Core equations (Eqs. 1–5) are dimensionally consistent. The primary observable channel is pre-declared: SPHEREx multi-tracer galaxy bispectrum with σ(fNL) = 0.7 (Heinrich et al. 2024), with local-template projection of a bounce-shaped bispectrum (r factor) — clearly stated as a sensitivity recast, not an independent Fisher computation. The SDB joint (fNL, nfNL) Fisher is presented as a secondary discriminator and not used for the main significance headline.

Abstract-last drift sweep
- Most abstract claims are supported and caveated similarly in the body, with one exception (P2-E2 above). The template-mismatch r range, the 5.2–5.5σ optimistic band, and the Bayes-factor ranges are backed by explicit equations/tables. The MegaMapper abstract claim needs softening as noted.

Provenance surfaces
- The code/data release must be frozen with a DOI and commit hash (P2-E1). Several results depend critically on code (null-space scan, triangle grids, ℓ-space Fisher overlap, Bayes-factor recompute).

Uncomputed-quantitative-claims check
- Most “robustness” assertions are quantified (e.g., rcos, percentile bands, σGR stress tests). Two remaining quantitative statements lack derivations (P2-M3 photo‑z 5% claim; P2-E3 anomaly-tracer 10–20% claim).

Standalone-reader test
- The analysis is mostly self-contained. Where it depends on Heinrich et al. (2024) (σ=0.7), the authors are explicit that they adopt rather than recompute the Fisher. The CMB-vs-LSS estimator caveats are present. The Li-vs-Cai operator identity needs one explicit worked example to fully close the loop (P2-E5).

Effect sizes
- Effect sizes are adequately stated (amplitudes in σ units; absolute fNL; fractional r; template overlap metrics).

## Summary recommendation
MAJOR REVISIONS

Justification
The core quantitative results (template overlap r, corrected significances, Bayes factors, and the consolidated systematics arithmetic) are internally consistent and well-presented for a sensitivity recast. However, several methodology-critical issues must be addressed for PRD standards: (i) reproducibility/provenance (missing DOI/commit), (ii) softening/clarifying abstract claims that rely on heuristic GR parameterization rather than a calibrated joint Fisher, (iii) removal or substantiation of unsupported performance claims (anomaly-tracer 10–20% gain; photo‑z 5% degradation), (iv) fuller specification of the survey weights used to obtain r = 0.84, and (v) an explicit vertex-level worked example closing the Li‑vs‑Cai factor-of-two within the exact integrands used. Addressing these will substantially improve the paper’s methodological rigor and reproducibility.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS ONLY (fresh-eyes audit)

ESSENTIAL

P2-E6. Inconsistent definition of the squeezed mode and x3 ratio
- Location: §II.A (p. 5) vs. §III.B (p. 8)
- Problem: Earlier the text defines the squeezed configuration with k1 as the long mode and k2 ≈ k3 ≡ k as the hard modes (k1/k → 0 in Fig. 1). Later, the “squeezed cutoff” is parameterized with x3 ≡ k3/k1 and the text states “x3 → 0 corresponds to the squeezed limit k3 ≪ k1 ≈ k2,” which flips the role of k3 to be the long mode and contradicts the earlier convention. This indexing inconsistency makes it unclear which side of the triangle is being cut in the “squeezed cutoff” tests, and raises questions about which convention the code implements.
- Required fix: Use one consistent indexing convention throughout (e.g., k1 is always the long mode). Update the x3 definition and the “x3 → 0” wording (or redefine x to be klong/khard) and confirm the code uses the same convention. If results were insensitive, show an explicit invariance check under index relabeling.

P2-E7. Misstatement about the location of k^2 in M(k, z)
- Location: §III.A (p. 7), second paragraph after Eq. (4)
- Problem: The text says “the explicit k^2 in the denominator of M […] makes the signal grow as Δb ∝ 1/k^2.” In Eq. (4), M(k, z) = [2 k^2 T(k) D(z)] / [3 Ωm H0^2]: k^2 is in the numerator of M, not the denominator. Δb ∝ 1/M ∝ 1/k^2 is correct, but the explanatory sentence is backwards.
- Required fix: Replace “in the denominator of M” with “since Δb ∝ 1/M and M ∝ k^2 on large scales.”

P2-E8. Contradictory narrative about which weighting upweights squeezed configurations
- Location: §III.B (pp. 8–9)
- Problem: The paper states that “signal-only CMB-Fisher weighting (w ∝ k^2) […] upweights the squeezed configurations where the bounce and local templates are most similar,” while LSS weightings (1/k^2, “SPHEREx-like”) “shift weight onto intermediate and folded configurations.” This explanation is inconsistent: w ∝ k^2 suppresses small-k (squeezed) triangles and emphasizes larger k; w ∝ 1/k^2 emphasizes small-k triangles. The observed numerical ordering rCMB = 0.876 > rLSS ≈ 0.83 could be correct, but the provided physical rationale is reversed and undermines confidence in the weighting implementation.
- Required fix: Correct the physical explanation and, preferably, show the actual triangle-weight distributions for each scheme (e.g., histograms of effective weight vs. squeezed ratio) to demonstrate which configurations dominate each weighting. Point to the exact code that computes the triangle weights.

P2-E9. IR-safety of the 1/k^2 weighting not demonstrated; “x3,min” variation alone is insufficient
- Location: §III.B (pp. 8–9)
- Problem: The LSS/SDB-motivated weighting includes factors ∝ 1/k^2, which are IR sensitive unless regulated by an absolute kmin (set by survey volume) and a clear triangle measure. The text only varies a dimensionless squeezed ratio cutoff x3,min ∈ [0.001, 0.2] and claims negligible effect on r. Without specifying the absolute k-range and measure used for the weighted average, this does not demonstrate IR safety. Independence from x3,min does not imply independence from absolute kmin.
- Required fix: Specify the absolute k-range, the triangle measure, and the survey window underlying the 1/k^2 weighting. Demonstrate convergence of r with respect to absolute kmin (e.g., kmin scans tied to realistic survey volumes) and show that the weighted average is finite and stable.

MAJOR

P2-M8. Mixing dimensionless triangle grids with dimensionful noise weightings needs a clear bridge
- Location: §II.A (pp. 4–5), §III.B (pp. 8–9)
- Problem: The triangle grid is described as dimensionless and “scale free,” while several of the “physically motivated” weights (SDB 1/k^2, “SPHEREx-like”) are dimensionful and depend on absolute scales through M(k, z), T(k), D(z), shot noise, and the survey window. It is unclear how these dimensionful weights were applied on a dimensionless grid without an explicit k-tiling and redshift weighting. This gap affects the central r = 0.84 ± 0.02 result.
- Required fix: Describe how absolute k-values and redshift distributions are assigned across the dimensionless triangle grid for each weighting, including kmin/kmax per redshift bin, the measure used for the average, and whether shot noise and photo-z kernels enter. Provide a minimal table or code reference that maps triangle ratios to absolute k’s and z-weights.

MINOR

P2-m6. Figure 1 vs. text consistency on squeezed ratio
- Location: Fig. 1 caption (p. 5) and §III.B (p. 8)
- Problem: Fig. 1 plots BNL(k1, k, k) vs. k1/k with k1 → 0 as the squeezed limit (consistent with §II.A). The later x3 definition (k3/k1 → 0 as “squeezed”) contradicts this. Even if numerics used a consistent convention, the reader sees two different “squeezed” directions.
- Required fix: Harmonize the squeezed-ratio variable across the paper (figure captions and text) and add a one-line note clarifying the index convention used throughout.

P2-m7. Clarify the negligible-dependence claim under 1/k^2 weighting
- Location: §III.B (p. 9)
- Problem: The text claims that varying the squeezed-limit cutoff x3,min from 0.001 to 0.200 changes r by < 0.0002 “confirming dominance by intermediate and folded configurations.” Under 1/k^2 weighting one would expect more influence from squeezed configurations unless the sampling measure or window de-weights them. Without the clarified weighting/mask (see P2-E9 and P2-M8), this conclusion is hard to audit.
- Required fix: After specifying the weighting and measure, add a small plot of r vs. x3,min for each weighting and, if applicable, r vs. absolute kmin, to substantiate the insensitivity claim.

P2-m8. Textual clarity in Appendix A.1 on symmetry factors
- Location: Appendix A.1, Eq. (A7) (p. 26)
- Problem: The correlator is written with a 1/Sv factor. While this may be correct depending on how Wick permutations are counted, it is uncommon enough to warrant a one-line explanation (are the Sv factors dividing out over-counting from identical legs in the explicit Wick sum?).
- Required fix: Add a parenthetical clarification for 1/Sv or refer to the notebook that verifies the combinatorics for at least one vertex.

P2-m9. Small terminology cleanup to avoid confusion
- Location: §III.A (p. 7), first sentence under “Scale-Dependent Bias”
- Problem: “Poisson–Newtonian transfer kernel” is nonstandard phrasing; most readers know M(k, z) as the Φ→δ transfer. Also, the subsequent “denominator of M” wording (see P2-E7) adds to confusion.
- Required fix: Consider replacing with “the Φ→δ transfer M(k, z) (δ = M Φ)” and fix the k^2 placement as in P2-E7.

Explanation
These are new issues not covered in my initial review. The most significant newly identified problems are: (i) an internal inconsistency in how the squeezed configuration is labeled and cut (P2-E6), (ii) a reversed physical explanation of the weighting schemes (P2-E8), and (iii) the absence of an IR-safety demonstration and absolute k-range specification for the 1/k^2 weighting that underlies the central r result (P2-E9, P2-M8). Together, they touch the core template-overlap calculation and should be addressed for PRD-level methodological rigor. All other arithmetic spot-checks I re-ran remain consistent at the quoted precision.