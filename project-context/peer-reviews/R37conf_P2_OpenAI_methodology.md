# P2 R37conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.60.pdf` md5=a961bf1c pages=27
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8480 chars)
**Wall time**: 376.7s

---

Referee report on “Testing the Matter Bounce with Primordial Non‑Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope of review
- I audited methodology, statistics, derivation chains, dimensional consistency, and internal arithmetic across the full 27-page manuscript, figures, tables, equations, and the abstract.
- I recomputed the quoted σ, ratios, and selected Bayes factors from the stated inputs.
- Findings below are itemized with severity tags and exact locations (page numbers refer to the rendered PDF you provided).

Top-line assessment
The paper presents a sensitivity recast (not a full survey Fisher re-forecast) for the matter-bounce prediction fNL = −35/8, including shape-overlap studies, a pragmatic systematics budget, and a Bayes-factor comparison. The overall structure is thoughtful and many quantitative claims check out. However, there are several critical issues that must be fixed before the paper can meet PRD methodological standards: a dimensionally inconsistent definition of the core observable BNL (Eq. 2), a factual error about Planck PR4 “strengthening” consistency with the bounce, an inconsistent narrow-prior Bayes factor, and incomplete reproducibility of the numerical pipeline (missing DOI and fixed release). I also flag a contradiction in the shot-noise degradation discussion and several clarity/reproducibility gaps around weighting definitions and GR “variance inflation.”

Detailed findings

ESSENTIAL

P2-E1 (Sec. II.A, p.3): Dimensionally inconsistent Eq. (2); numerator/denominator inverted
- Quoted text/equations: “BNL = (10/3) P/AT Σi k^3_i → −35/8 … Here Σi k^3_i ≡ k1^3 + k2^3 + k3^3, and BNL is dimensionless by construction: P has degree 9, the prefactor of Eq. (1) removes degree 6, and the Σi k^3_i denominator removes the remaining degree 3.”
- Problem: With AT as defined in Eq. (1): AT = (3/256)(P / (k1^2 k2^2 k3^2)). Your Eq. (2) as written gives BNL ∝ [P/(AT Σk^3)] ∝ [(P) / ((P/k^6) · k^3)] ∝ k^3, which is not dimensionless. The accompanying paragraph asserts the opposite. The dimensionally correct form is BNL ∝ AT / Σk^3 (up to the overall 10/3 factor), not P/AT.
- Required fix: Replace Eq. (2) with the dimensionally consistent expression:
  BNL(k1,k2,k3) = (10/3) AT(k1,k2,k3) / (k1^3 + k2^3 + k3^3),
  and update any downstream references where the symbolic structure of Eq. (2) is used. Keep the explanatory paragraph showing the degree count (9 − 6 − 3 = 0). If your internal code uses the correct form already, state this explicitly and confirm no plotted/evaluated numbers change.

P2-E2 (Sec. VIII.A, p.18): Incorrect statement about Planck PR4 “strengthening” consistency with bounce
- Quoted text: “The earlier PR3 Planck constraint was fNL = −0.9 ± 5.1; the PR4 NPIPE reanalysis tightens the error bar by ∼2% and shifts the central value toward zero, strengthening consistency with the matter-bounce prediction.”
- Problem: Shifting the central value toward zero makes the measurement farther from the bounce prediction (−4.375), not closer. Quantitatively (including your own r-recasting by 0.876): PR3 gives |−4.375 + 0.9|/5.1 ≈ 0.68σ; PR4 gives |−4.375 + 0.1|/5.0 ≈ 0.86σ. PR4 is less consistent with the bounce than PR3.
- Required fix: Correct the sentence to reflect that PR4 is slightly less consistent with the bounce prediction than PR3 (but both are comfortably consistent with either model).

P2-E3 (Secs. VI.C/Table III, pp.12–17): Inconsistent Bayes factor for the narrow competitor prior [−5, +5]
- Quoted text: Table III (row “Ideal (no GR)”, “BF vs. Tuned” column shows 7.0). Related text repeatedly cites ~7.0 for the delta bounce prior vs a narrow [−5, +5] uniform competitor.
- Problem: For a Gaussian likelihood centered exactly at −4.375 with σ = 0.7 (your r → 1 endpoint), the closed-form BF for a delta prior vs a uniform prior of width W is BF = W / (√(2π) σ). With W = 10 and σ = 0.7, BF = 10/(2.5066×0.7) ≈ 5.7, not 7.0. Your own formula (Eq. 8) implies this result. The same inconsistency propagates into several narrative places (e.g., p.12 and Table II footnotes referencing 7.0 under “no GR”).
- Required fix: Recompute and correct all instances of this narrow-prior Bayes factor (should be 5.7 at σ = 0.7; with σeff = 0.833 after r = 0.84 rebooking it should be ≈ 4.8–4.9). If you used a different σ for that cell, state it explicitly and propagate consistently.

P2-E4 (Data and Code Availability, p.23): Missing frozen release and DOI; placeholder text
- Quoted text: “archived at Zenodo (DOI inserted at submission)”
- Problem: The DOI placeholder renders the analysis non-reproducible as submitted. There is no immutable release tag/commit, no DOI, and therefore no verifiable provenance of the artifacts (JSONs, notebooks) referenced throughout.
- Required fix: Provide an actual Zenodo DOI (or equivalent immutable archive) and the exact Git commit hash/tag corresponding to the submitted manuscript. Ensure that every referenced artifact (e.g., c9i epsilon ratio check.json, phase3 fisher overlap.json, tables recompute scripts) is present in that release.

P2-E5 (Sec. IV, Shot-noise caveat, p.10): Contradictory shot-noise degradation magnitudes
- Quoted text: “a simple Poisson estimate gives a ∼15–30% degradation in σ(fNL) … scaling as σshot/σCV ∼ √(1 + 1/(nP0)). For n ∼ 10−5 h^3 Mpc−3, P0 ∼ 10^4 h−3 Mpc^3, 1/(nP0) ∼ 10, giving σ inflated by √11 ≈ 3.3× … while the bispectrum estimator effective degradation at the squeezed-limit modes that dominate fNL sensitivity is moderate, 15–30%.”
- Problem: You first quantify a ~3.3× inflation under Poisson scaling and then assert an effective 15–30% degradation for the bispectrum estimator without a derivation linking the two. As written, these statements are contradictory.
- Required fix: Either (i) provide a quantitative derivation/weighting argument showing how the 3.3× Poisson inflation maps to only 15–30% net σ(fNL) degradation in the actual bispectrum estimator (with equations, k-weighting, and triangle weighting), or (ii) revise the text to remove the 15–30% claim and report the conservative Poisson-scaled expectation with an explicit caveat that a dedicated bispectrum Fisher including shot noise would be needed to refine it.

P2-E6 (Abstract and passim; Table IV p.19): Explicit reproducibility of the “SPHEREx-like” and “LSS/SDB” weightings for r
- Quoted text: Multiple places give r values under “SPHEREx-like” and “LSS/SDB” noise weighting (e.g., r = 0.829, 0.830, 0.835; Eq. 6 and Sec. III.B).
- Problem: The exact Fisher weight definitions and all inputs needed to reproduce these numbers (noise model, redshift binning, triangle sampling domain, binning scheme, and any cuts) are not fully specified. This is load-bearing for the headline 5.2–5.5σ.
- Required fix: Provide the precise mathematical definitions of the weighting kernels w(k1,k2,k3) you used for each case, the k/range and triangle grid, and a pointer to the exact configuration file(s) in the archived repository that reproduce r = 0.829/0.830/0.835 and 0.876. A short supplementary table is sufficient.

MAJOR

P2-M1 (Abstract, Sec. IV, Table IV, many locations): Treatment of GR “contamination” as Gaussian variance inflation
- Quoted text: “GR marginalization (σGR added in quadrature…) … ‘realistic’ ∼2.6–5σ after the systematic budget” (Abstract; also Table IV).
- Problem: Relativistic projection effects generally induce biases (and additional correlated covariance terms), not simple zero-mean Gaussian variance. Although you clearly label σGR as a scoping parameter and not a calibrated Fisher, you still use it to define the paper’s “realistic” headline.
- Required fix: Strengthen the caveat everywhere this “realistic” range is used (Abstract, Sec. IV, Fig. 2 caption) to state that it is a stress-test envelope assuming a zero-mean Gaussian nuisance added in quadrature, not a forecast with a calibrated nuisance model. Alternatively, provide a minimal two-parameter Fisher toy model (fNL + a GR template amplitude) to justify the quadrature mapping in Table IV.

P2-M2 (Secs. III.B–IV, pp.8–10): Derivation of Eq. (5) mapping r to σeff
- Quoted text: “fmeasured = r fbounce, σ(fbounce) = σ(flocal)/r.”
- Problem: This mapping assumes that the estimator is optimal for the local template and that projection of the non-local residual shape contributes negligibly to the variance. You acknowledge this heuristically via rcos, but no quantitative bound enters the σ.
- Required fix: Add a short derivation or a standard reference showing the conditions under which σ scales as 1/r. If you rely on the shape cosine bound, add a quantitative inequality (e.g., σ^2 ≤ σloc^2/r^2 + ε with ε bounded by 1 − rcos^2 under your shape metric) or state explicitly that this mapping neglects off-template projection noise.

P2-M3 (Fig. 1, p.5): Axis label ambiguity
- Quoted text: x-axis labeled “k/k” in the figure.
- Problem: Ambiguous variable. In the text you use k1/k for the squeeze ratio.
- Required fix: Relabel the x-axis to the precise ratio used (e.g., k1/k or x ≡ k1/k3), and state it in the caption.

P2-M4 (Secs. II.A–II.B, pp.3–6): Under-determined polynomial and basis mapping reproducibility
- Quoted text: Basis/coefficients discussion incl. “the printed coefficients … are not directly transplantable… our coefficients are fixed from the three published benchmark values themselves.”
- Problem: This is central to your null-space scan and r-distribution. While you provide a qualitative description and code pointer, there is no minimal, explicit linear map or benchmark-evaluation table in the text to let a reader verify that your chosen coefficient set exactly reproduces the three Cai benchmarks.
- Required fix: Add a compact supplementary table showing your six coefficients and the predicted BNL values at the three benchmarks (squeezed/equilateral/folded), side-by-side with Cai et al.’s, to substantiate the claim without requiring code execution.

P2-M5 (Sec. III.B, p.8): ℓ-space Fisher overlap “r = 0.878 ± 0.012, stable across ℓref = 50–950”
- Problem: The role of ℓref is not defined; the weighting kernel, noise model, and the precise normalization used in the overlap are not specified. This hinders reproducibility of the quoted ±0.012 precision.
- Required fix: Define the ℓ-space Fisher inner product you used (integrand, weight, and noise), and explain the dependence on “ℓref”. Provide a pointer to the exact configuration file used, in the archived repo.

P2-M6 (General, multiple sections): Paper length vs. contribution
- Problem: At 27 pages, this is long for a sensitivity recast with one main headline (SPHEREx bispectrum-only significance after mismatch and a scoping systematics envelope). Several long excursions (e.g., extended basis-orbit taxonomy, multi-page Bayes-factor corners) could be condensed without loss of substance.
- Required fix: Consider reducing to ≤ 18–20 pages by moving lengthy internal-audit narrative (JSON artifact names, repeated caveats) to an appendix or the repository README, keeping only what is essential for a stand‑alone reader.

MINOR

P2-n1 (Sec. II.C, p.6): Assumption (f) wording
- The ECH/BI-parameter caveat is very detailed here. It could be tightened to one concise paragraph; as written it reads like a review footnote. Not a blocker, but consider streamlining.

P2-n2 (Sec. IV, p.10): “Naive uncorrected” 6.25σ bar appears in Fig. 2
- You do mark it “shown only for reference, not used in any headline,” which is good. Consider graying it further or moving it to an inset to avoid any chance of inadvertent “sigma inflation” by casual readers.

P2-n3 (Sec. VI.C, p.12): “median Bayes factor” wording
- Since your Bayes factors are closed-form, consider removing “median” phrasing except where you actually report Monte Carlo marginalizations over σeff or nuisances.

P2-n4 (Sec. VII.D, p.18): “O(10–30%)” degradations
- Where numbers exist (e.g., photo‑z 5%), prefer numbers over “O(·)” to avoid ambiguity. You already give some; harmonize language.

P2-n5 (Appendix A.2, p.26): Clarify that Table V significance change is not a normalization (c) change
- You do state this, but a one-sentence reiteration that the two rows differ by physical time‑ordering content, not by c‑rescaling, would prevent misreadings.

NIT

P2-nt1: A few instances of informal wording (“rebooked,” “headline,” “scoping choice”) could be formalized for PRD style.

P2-nt2: Ensure consistent hyphenation for terms like “post‑bounce,” “photo‑z,” “multi‑tracer.”

Arithmetic spot-checks that pass
- Naive significance: 4.375/0.70 = 6.25 (Fig. 2 “naive” bar): OK.
- Template-corrected significance: 4.375×0.84/0.70 ≈ 5.25; with r = 0.876 gives ≈ 5.48 (“5.2–5.5σ”): OK.
- GR-inflated σeff: √(0.7^2 + 1.0^2) ≈ 1.221 → 4.375×0.84/1.221 ≈ 3.01 (“~3.0σ”): OK.
- Combined bϕ 30% (σ=0.9) + GR 1.0: σeff = √(0.9^2 + 1^2) ≈ 1.345 → 2.73σ (“~2.7σ”): OK.
- MegaMapper ideal: 4.375×0.84/0.5 ≈ 7.35; with r = 0.88 gives 7.7 (“7.4–7.7σ”): OK.
- Bayes factor vs SSFSR: exp[(4.375/0.7)^2 / 2] ≈ 3.3×10^8; your 3.5×10^8 is consistent: OK.
- Consistency relation window: ns − 1 = −0.0351, c′ ∈ [0.7,10] ⇒ ΔfNL ∈ [+0.025, +0.351] ⇒ [−4.35, −4.02]: OK.

Abstract-last drift sweep
- Most abstract claims are traceable and appropriately caveated in the body (especially the explicit “sensitivity recast” language and the quadrature systematics caveat). Two corrections are required: (i) fix the Planck‑PR4 “strengthening” error (P2-E2), and (ii) add one line in the abstract that the “2.6–5σ realistic” range is a stress‑test envelope based on quadrature addition of a Gaussian GR nuisance (not a full joint Fisher with GR templates), to avoid overclaim.

Bibliography spot checks
- Heinrich et al. 2024 (Phys. Rev. D 109, 123511) for σ(fNL) ≈ 0.7: OK.
- Planck 2018 parameters ns: OK.
- Cai et al. 2009; Li et al. 2016; mapping c = 2 vs 6/5 in ζ: consistent.
- DESI DR1 LRG/QSO recent arXiv entries [34], [35]: plausible and consistent with the text-level precisions quoted.

## Summary recommendation
MAJOR REVISIONS

The paper contains substantive methodology and generally good arithmetic control, but cannot be accepted in its current form due to (i) a dimensionally inconsistent core equation (Eq. 2), (ii) a factual error about Planck PR4 consistency with the bounce, (iii) an inconsistent narrow‑prior Bayes factor, (iv) missing immutable code/data release (DOI), and (v) a contradiction in the shot‑noise degradation discussion. Addressing the ESSENTIAL items (E1–E6) and the key MAJOR items (notably clarifying the GR-variance treatment and the exact weightings used to compute r) will bring the manuscript to PRD methodological standards. I also encourage trimming length and tightening style.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (fresh pass)

ESSENTIAL

P2-E7 (Sec. V, p.11; Abstract; Fig. 2 caption): Misapplication of the template‑mismatch factor r to MegaMapper’s SDB forecast
- Quoted text: “The significance for a detection at fNL = −4.375 ranges from 7.4–7.7σ at the published ideal σ(fNL) = 0.5 with template‑mismatch correction only (r = 0.84–0.88; without template correction the naive significance is 8.75σ).”
- Problem: The r factor quantifies a bispectrum-template projection loss for a local-template bispectrum estimator. It does not apply to power-spectrum scale‑dependent bias (SDB) constraints, where the observable is Δb ∝ fNL/k^2 with no bispectrum-shape projection. The MegaMapper σ(fNL) ≈ 0.5 forecast is SDB‑dominated; applying r underestimates the true significance.
- Required fix: Remove the r rescaling for SDB-based forecasts. The ideal MegaMapper significance should be 8.75σ (not 7.4–7.7σ) if σ = 0.5. Any “template‑corrected” language for MegaMapper should be deleted or explicitly restricted to a hypothetical MegaMapper bispectrum analysis (which is not what [15] forecasts).

P2-E8 (Sec. VI.C, p.13, worked example): Incorrect statement about Bayes‑factor sensitivity to competitor prior width
- Quoted text: “Widening [−15, +15] to [−20, +20] adds ∆BF ≲ 1…”
- Problem: For a uniform competitor prior of width W, the evidence scales linearly with W in the delta‑bounce vs uniform‑competitor comparison (and also in the Gaussian‑bounce‑prior case, the denominator integral is ∝ W). Increasing W from 30 to 40 boosts BF by a factor 4/3, not by an additive ≤ 1. For the cited BF ≈ 9.2 case, this implies BF ≈ 12.3 (∆BF ≈ +3.1), not ≤ +1.
- Required fix: Correct the width dependence (BF ∝ W for a uniform competitor prior) and update the stated ∆BF accordingly in the worked example and any other places this claim appears.

MAJOR

P2-M7 (Fig. 4 caption/body, p.15): Mixing non‑comparable σ values on one axis without an explicit “not directly comparable” qualifier
- Issue: The left panel plots σ(fNL) vs kmin for MegaMapper SDB (orange) and SPHEREx SDB‑only (blue), then overlays a dotted horizontal line σ = 0.7 labeled “SPHEREx bispectrum channel.” Those σ values derive from different observables (SDB power spectrum vs bispectrum) and null procedures.
- Required fix: Either remove the σ = 0.7 bispectrum line from the SDB plot or add an explicit in‑panel note and caption sentence that the dotted σ is from a different estimator and is not directly comparable to the SDB curves.

P2-M8 (Sec. III.A, Eqs. (3)–(4), p.11): Unit‑system ambiguity in M(k, z)
- Quoted text: “M(k, z) = 2 k^2 T(k) D(z) / (3 Ωm H0^2), with k quoted in h Mpc−1 throughout.”
- Problem: With k in h Mpc−1 and H0 usually in km s−1 Mpc−1 (or s−1 in c = 1), a c factor is typically required for dimensional consistency. Many authors write M(k, z) = 2 k^2 T(k) D(z) / (3 Ωm H0^2) with c restored as H0 → H0/c. Your text mixes unit conventions without stating them.
- Required fix: State the unit system explicitly (e.g., c = 1 with H0 in h Mpc−1 units), or insert the appropriate c factors. Clarify that M is dimensionless under the stated units.

P2-M9 (Abstract, first paragraph last sentence; also Sec. IV text near Eq. (7)): Misplaced cross‑reference to Eq. (7)
- Quoted text (Abstract): “…systematics are combined additively in quadrature… (cf. Sec. VII and Eq. (7), labeled as a heuristic primordial‑field scaling check rather than a galaxy‑covariance derivation).”
- Problem: Eq. (7) addresses fNL‑induced non‑Gaussian covariance scaling (six‑point), not GR projection/variance inflation. Citing Eq. (7) in the GR‑systematics context is confusing.
- Required fix: Remove the Eq. (7) parenthetical from this GR‑systematics sentence or replace it with a pointer to the GR parameterization subsection (Sec. VII.C/Table III) only.

P2-M10 (Sec. II, III.B, injection–recovery paragraph on p.5): Null‑procedure comparability of rmeas = 0.90 ± 0.01
- Quoted text: A 2D flat‑sky CMB‑style KSW estimator with isotropic Gaussian noise and “SPHEREx photometric‑z power spectra as the diagonal noise covariance,” on tiled patches “covering the full sky.”
- Problem: This is not directly comparable to the 3D SPHEREx bispectrum estimator (tomographic redshift bins, survey window, photo‑z scattering). While some caveats are present, the 0.90 ± 0.01 is prominently listed among “validations” of r.
- Required fix: Add an explicit sentence that this 2D injection–recovery number is not an apples‑to‑apples validation for the 3D SPHEREx bispectrum pipeline and should be read as a CMB‑style Fisher cross‑check only. Consider moving the number to a supplement or clearly marking it as “illustrative, not used for pipeline validation.”

P2-M11 (Sec. V, p.11; Fig. 2 caption): “Template‑corrected” MegaMapper bar relies on SPHEREx‑specific r and GR budgets
- Issue: Beyond the r misapplication (P2‑E7), the “3–7σ envelope” for MegaMapper inherits GR and bϕ systematic budgets calibrated for SPHEREx’s z ≲ 2 bispectrum regime. The text says “for illustration only,” but the bar appears alongside SPHEREx with similar visual weight.
- Required fix: Strengthen the caveat in the caption and text that the MegaMapper “template‑corrected” bar applies SPHEREx‑motivated degradations to a different redshift/observable and is an illustrative placeholder, not a forecast.

MINOR

P2-n6 (Sec. III.B, p.9): Unsupported novelty claim on overlap quantification
- Quoted text: “a literature search confirming no prior quantification of this overlap exists for the matter‑bounce bispectrum (2009–2024).”
- Problem: This “no prior quantification” claim is broad and uncited. Even if true, PRD style prefers either a supporting citation sweep (databases searched, keywords) or softer language.
- Required fix: Rephrase to “to our knowledge” without implying an exhaustive search, or provide a brief literature‑search justification.

P2-n7 (Sec. IV, p.10): Anomaly‑tracer “∼10–20% improvement” lacks a documented Fisher setup
- Quoted text: “a preliminary Fisher forecast… projects a ∼10–20% improvement… an upper bound pending the shot‑noise‑corrected Fisher analysis…”
- Problem: No configuration (n(z), b(z), V, k‑cuts) or code pointer is provided for this claim.
- Required fix: Either give a one‑line Fisher setup and a repository pointer, or soften the text to a qualitative expectation without percentages.

P2-n8 (Sec. II/III.B injection–recovery paragraph, p.5): Wording inconsistency on geometry
- Quoted text: “full‑sky geometry” and “tiled flat‑sky patches covering the full sky” are used interchangeably.
- Required fix: Clarify that the test uses multiple flat‑sky patches approximating full‑sky coverage, not a true full‑sky spherical‑harmonic analysis.

P2-n9 (Sec. VII.B, p.16): “Per‑bin σ” phrasing for σ(fNL) = 0.7
- Issue: The Heinrich et al. σ(fNL) = 0.7 is the combined multi‑tracer bispectrum constraint, not a “per‑bin” σ. The phrase “per‑bin SPHEREx σ widens to ≈ 0.9–1.0” is confusing.
- Required fix: Rephrase to “the effective combined σ widens to ≈ 0.9–1.0 when bϕ is marginalized per tracer bin.”

P2-n10 (Fig. 2 caption, p.10): Make cross‑channel differences explicit
- Issue: The figure mixes SPHEREx bispectrum‑only bars with a MegaMapper SDB bar. The caption mentions channels implicitly but not explicitly.
- Required fix: Add “SPHEREx bars: bispectrum estimator; MegaMapper bar: SDB (power‑spectrum) estimator; the two are not directly comparable.”

NIT

P2-nt3 (Notation, multiple places): Reuse of “k” in BNL(k1, k, k) and axis label “k/k”
- While P2‑M3 already asks to fix the Fig. 1 axis, also comb the text to ensure all appearances specify the exact ratio (e.g., x ≡ k1/k3) to avoid confusion.

P2-nt4 (Units, Sec. III.A): Add “with c = 1” or explicit c where appropriate
- To prevent reader confusion in M(k, z), insert a brief parenthetical “we set c = 1” or include c explicitly.

Brief rationale for why these are new
- The first review focused on Eq. (2) dimensionality, Planck PR4 wording, a narrow‑prior Bayes‑factor inconsistency, DOI/release, shot‑noise contradiction, weighting reproducibility, GR variance modeling, σeff mapping assumptions, figure label, coefficient reproducibility, ℓ‑space overlap definition, and length/style. This fresh pass targeted cross‑channel comparability, prior‑width scaling in Bayes factors, unit conventions in transfer functions, figure/caption consistency, and novelty/support claims, which were not previously addressed.