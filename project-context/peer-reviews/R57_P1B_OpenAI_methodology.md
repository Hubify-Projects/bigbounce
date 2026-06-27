# P1B R57 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R57_P1B/paper1b_mcmc_companion.pdf` md5=653da036 pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5275 chars)
**Wall time**: 325.4s

---

Referee report on: “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of review
- Focus: methodological rigor, statistics, internal arithmetic, dimensional analysis, estimator validity and pre-declaration, convergence criteria, figure/table consistency, abstract-vs-body alignment.
- I audited every load-bearing number in the abstract and conclusions against the body; recomputed quoted σ-distances and key ratios; checked equations for dimensional consistency; and examined all figures and tables for labeling and consistency.

General assessment
- The manuscript is primarily a methods companion reporting three verification exercises. Much of the statistical and numerical work is carefully scoped as “compatibility-only,” and many non-comparabilities are stated. That said, several items fall short of PRD methodological and presentation standards and must be corrected. The most serious issues are (i) an abstract-level cross-reference to a footnote; (ii) a quantitative “≳100× fine‑tuning” claim that is not derived and is inconsistent with the cited footnote; (iii) an axis mislabel in a load‑bearing figure (ΔNeff vs Neff); and (iv) the use of ephemeral repository/commit/version identifiers in the body in lieu of a frozen, citable archival release.

Findings

ESSENTIAL

P1B-E1
- Location: Abstract, p. 1
- Issue: Abstract cites “fn. 3 in Sec. IV” (“…PR3‑vs‑PR4/NPIPE disambiguation is given in fn. 3 in Sec. IV…”).
- Problem: Abstracts must be self-contained; cross-referencing footnotes is not acceptable for PRD.
- Required fix: Remove the footnote cross-reference from the abstract. If absolutely necessary, replace with a brief, self-contained sentence clarifying the PR3 vs PR4 provenance, or move the nuance to the main text only.

P1B-E2
- Location: Sec. VI, p. 12–13 (“Note (spectator-status caveat, main text).”)
- Issue: Claim of “≳100× fine‑tuning of the misalignment initial condition under a cos θi‑flat prior (equivalently ∼25× relative to θi≈0.5; quantitative derivation in fn. 6)”.
- Problem: The body provides a 25× tuning argument (Ωa ∝ θi^2; θi=0.1 vs 0.5) in fn. 6, but no derivation or quantitative basis is given for the “≳100×” claim. The cited fn. 6 does not derive ≥100×; it supports 25×. The later rerun under the cos θ prior reports a reduction of the θi≤0.1 posterior fraction to 0.068%, but this does not quantify a ≥100× fine-tuning in the stated sense nor is it linked to that claim.
- Required fix: Either (a) provide a clear quantitative derivation of the “≳100×” figure (e.g., probability measure under the cos θ prior for θ≤0.1 vs a stated reference range, with the exact ratio and its uncertainty), or (b) remove the “≳100×” language and retain only the demonstrated 25× tuning (and/or a rigorously computed measure-based factor with numbers). Ensure every “fine‑tuning” multiplier in the manuscript is defined consistently (tuning of energy density vs tuning in prior measure).

P1B-E3
- Location: Fig. 2, p. 8 (caption and panel a axis)
- Issue: The figure is described in the caption as “ΔNeff marginal posterior…” and marks “Standard-Model value ΔNeff = 0,” but the x-axis is labeled “Neff” and the annotation reads “SM (Neff = 0)”.
- Problem: Mislabeling of the axis and SM marker: the plotted quantity is ΔNeff, not Neff. SM Neff ≈ 3.046, not 0. The current labeling is misleading and conflicts with the caption and text.
- Required fix: Relabel the x-axis to “ΔNeff” and change the annotation to “SM (ΔNeff = 0)”. If the plotted variable is actually Neff, then the caption and the text must be corrected accordingly (and the SM marker must be at 3.046). Ensure consistency across caption, labels, and text.

P1B-E4
- Location: Data and Code Availability, p. 17–18; Appendix A, p. 18–19
- Issue: Reliance on ephemeral repository state (“in-tex v1B.0.78 stamp”, commit SHA b22f8cc9, “DOI assignment is pending”), path-like artifacts, and change-log language inside the main text.
- Problem: PRD requires archival stability. Commit hashes and “pending” DOIs are not acceptable as the sole provenance anchors in the published paper. Version-history/bookkeeping language does not belong in the body text.
- Required fix: Create a frozen, citable archival release (e.g., Zenodo/OSF/Dataverse) with a DOI that contains: all frozen chains used for the main results; the exact NaMaster scripts and configs; and the ALP-MCMC chains/configs. Replace commit hashes and “pending” language in the paper with the final DOI(s) and release tag. Move any change-log, internal pipeline-bug notes, and path listings to Supplementary Material or to the repository only; purge them from the main text.

MAJOR

P1B-M1
- Location: Sec. VI (pp. 12–16) and Appendix C (p. 20–21)
- Issue: Inconsistent notation for the axion mass: “m” in the main text and “ma” in the appendices; both are used with H0 without an explicit unit convention on first use.
- Problem: This invites confusion about whether “m” and “ma” are identical and about unit conventions when comparing to H0.
- Required fix: Use a single symbol for the axion mass throughout (e.g., ma), define units clearly (e.g., ma/H0 with H0 converted to eV ≈ 1.44×10−33 eV), and audit the text so every occurrence is consistent. Update the figures/tables if applicable.

P1B-M2
- Location: Abstract, p. 1; Sec. IV, pp. 8–11; Conclusions, p. 16
- Issue: The “observed pipeline bias floor 0.040°” for the NaMaster validation is reported prominently without specifying in all headline locations that it depends on the deliberately unweighted estimator; the inverse-variance-weighted fit reduces the bias by ≈80% (to −0.006°) per the robustness battery.
- Problem: Readers may interpret 0.040° as a generic NaMaster-pipeline bias. It is estimator-specific.
- Required fix: Wherever the 0.040° floor is a headline number (abstract, conclusions), qualify it explicitly as “for the unweighted template-fit estimator.” Provide, side-by-side in Sec. IV and in the abstract/conclusion, the corresponding bias for the inverse-variance-weighted estimator, and state which estimator you recommend for analysis. If the goal is methods validation against the published drivers that used the unweighted fit, say so explicitly in each headline appearance.

P1B-M3
- Location: Table IV, p. 17
- Issue: Columns for m/H0, θi, and Caγ list triplets such as “4.7/37.7/264” without an explicit legend in the table that these are 16/50/84 percentiles (elsewhere you do use “16–84%” notation).
- Problem: Ambiguity in summary statistics presentation.
- Required fix: Add a column header or footnote in Table IV stating that triplets are the 16/50/84 percentiles. Prefer the standard notation “median [p16, p84]” for clarity (e.g., 37.7 [4.7, 264]).

P1B-M4
- Location: Sec. V.B, p. 11–12
- Issue: The “release-pairing robustness rerun” (c15) is used to assert 0.04σ agreement in ΔNeff, but the stated convergence is R̂−1 = 0.0147 (above the authors’ own 0.01 target).
- Problem: Using a sub-converged chain to support a quantitative equivalence claim is not ideal.
- Required fix: Either extend the c15 rerun to R̂−1 < 0.01 and re-quote the agreement, or downgrade the statement to an indicative check with an uncertainty band large enough to account for sub-convergence.

P1B-M5
- Location: Figs. 1–2, pp. 7–8
- Issue: Several axis labels appear typeset inconsistently (“8” instead of “σ8” on parts of Fig. 1; “m” without context, etc.).
- Problem: Ambiguous or incomplete labeling on axes in summary plots.
- Required fix: Ensure all axes use standard, unambiguous symbols with units where applicable (σ8, S8, Ωm, ns, H0 [km s−1 Mpc−1], ΔNeff, etc.). Re-export figures with corrected labels.

MINOR

P1B-m1
- Location: Sec. IV, pp. 8–11
- Issue: You assert B‑mode purification (purify_b=True) yields the same recovered β̂ (0.238°) but do not provide the numerical uncertainty.
- Required fix: Give the numerical β̂ ± SE for the purification test or cite the exact artifact line where it appears, to quantify “no change” (e.g., 0.238° ± 0.002°).

P1B-m2
- Location: Sec. VI, pp. 13–16
- Issue: The small-angle quadratic approximation is used to compute Ωa; you state corrections are ≲8% at θi ∼ 1 and ≲1% for the Ωa≤0.01 subset.
- Required fix: Provide a one-line quantitative bound (e.g., maximum fractional difference over the posterior-supported Ωa ≤ 0.01 subset from a direct EOM integration) to substantiate the “≲1%” statement.

P1B-m3
- Location: Sec. V.C, pp. 12–13; Table II
- Issue: The lensing likelihood variant (“native” vs “.clik”) is a non-trivial implementation detail but is not fully specified in Table II or caption.
- Required fix: Add an explicit sentence/footnote in Table II clarifying the lensing likelihood used (native vs clik) and, if available, a brief check that swapping them does not materially change the w0wa posterior at the quoted precision.

P1B-m4
- Location: Acknowledgments, p. 17
- Issue: Vendor-specific computing details (“RunPod H200 instances”) and the mention of an AI assistant are unusual for PRD and not needed for reproducibility.
- Required fix: Remove vendor names and model names, or move to a data-availability note if the editors permit. If the AI assistant statement is retained, confirm it complies with PRD policy; otherwise remove.

P1B-m5
- Location: Throughout (e.g., p. 1, p. 16)
- Issue: Several hyphenation/typography inconsistencies (e.g., “3.6σ” vs “3.6 σ”, “µK · arcmin” vs “µK·arcmin”) and occasional stylistic duplication in phrasing that could be tightened.
- Required fix: Standardize typography and units journal-wide; run a careful copy edit.

NITS

P1B-n1
- Location: Sec. IV, p. 9–11
- Issue: Several file path references (e.g., reproducibility/.../namaster_500mc.py) in the main body disrupt readability.
- Required fix: Move these to Supplementary Material or the repository README; keep main text method descriptions high-level, with a single pointer to the archive/DOI.

P1B-n2
- Location: Eq. (9), p. 16
- Issue: Minor clarity: state explicitly that for zosc ≤ 0 the (1+zosc)−3 dilution is not applied and ρa=V(θi).
- Required fix: Add “for zosc>0; for zosc≤0 use ρa(0)=V(θi)” inline with the equation or as a footnote.

Arithmetic, consistency, and dimensional checks (passed)
- H0 tension: (73.04 − 67.68)/sqrt(1.06^2+1.04^2) = 3.61σ (quoted 3.6σ): OK.
- S8 tension: 0.827±0.010 vs 0.776±0.017 ⇒ 2.59σ (quoted 2.6σ): OK.
- Weighted combination S8: 0.827±0.010 ⊗ 0.776±0.017 ⇒ 0.814±0.0086 (quoted 0.814±0.009): OK.
- w0 departure: (−0.8122 − (−1))/0.0436 = +4.31σ; wa departure: 0.6666/0.1864 = 3.58σ: OK.
- Phantom-crossing redshift z× ≈ 0.39: recomputed from (−1−w0)/wa = 0.2817 ⇒ a× = 0.7183 ⇒ z× = 0.39: OK.
- H(z=0.5) fractional change ≈ +1.74% for the quoted (w0,wa) at fixed Ωm: OK.
- NaMaster multiplicative under-recovery: 0.238/0.27 ≈ 0.882 and 0.302/0.342 ≈ 0.883: OK.
- EB template relation sin(2β)cos(2β) = ½ sin(4β) used in Eq. (1): OK.
- Noise conversion ΔP=10 μK·arcmin ⇒ σpix=10/√47.21=1.455 μK at Nside=512: OK.
- ALP birefringence β = (αEM/4π) Caγ Δφ/fa with Caγ=8, Δφ/fa=1.06 → β ≈ 0.28°: OK.
- Caγ Δφ/fa required for βobs=0.342°: 0.342°×π/180 / (αEM/4π) ≈ 10.27: OK.
- Ωa scaling and dimensions: Eq. (9) dimensionless and consistent; small-angle factor 1/6 correct: OK.

Length
- At 22 pages for a methods companion, the paper could be tightened. The current inclusion of commit hashes, file paths, and workflow minutiae in the main text contributes to length without improving scientific clarity.
- Recommendation: Reduce to ≤18 pages by moving implementation-path details and change-log/commit references to Supplementary Material or the archived repository documentation.

Abstract-last drift sweep
- Generally faithful to the body, with correct caveats distinguishing MC pipeline recovery from sky detections, and the ΔNeff null result. Two exceptions:
  1) Footnote cross-reference (P1B-E1) must be removed.
  2) Where the “pipeline bias floor” is quoted, qualify it as unweighted-estimator-specific (P1B-M2).

Provenance surfaces
- Replace “pending DOI” and commit SHA references with finalized DOIs (P1B-E4).

Effect sizes
- Effect sizes are generally present and correctly computed (e.g., fractional H changes, S8 differences). No action needed.

## Summary recommendation
MAJOR REVISIONS

The methodology is largely solid and carefully caveated, but several essential corrections are needed before this can meet PRD standards: remove non-self-contained abstract elements, correct the ΔNeff figure labeling, fix the unsupported “≳100×” fine-tuning claim (or provide a derivation), and replace ephemeral repository references with a permanent archival DOI. Clarify that the quoted 0.040° pipeline bias is estimator-specific and present the inverse-variance-weighted result alongside it in all headline locations. Unify notation and clean up table/figure labeling. After these changes, the paper could be acceptable as a methods companion.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-audit pass)

ESSENTIAL

P1B-E5
- Location: Sec. VI, “LiteBIRD forecast,” p. 16
- Issue: Quadrature in the significance estimate is written as |0.342 − 0.27|/√(0.032 + 0.0942).
- Problem: The first term under the square root is missing the square; it should be 0.03^2, not 0.032. As written, the expression is dimensionally inconsistent even though the final 0.7σ number happens to be approximately correct.
- Required fix: Replace with |0.342 − 0.27|/√(0.03^2 + 0.094^2) and state the numeric evaluation explicitly (0.73σ).

P1B-E6
- Location: Abstract, p. 1 (spectator-ALP “brackets the published signal” claim)
- Issue: “For a field with fa ∼ MPl, the scan-prior m ∼ H0 region brackets the published joint WMAP+Planck signal β = 0.342° ± 0.094°.”
- Problem: At fixed Caγ = 8 (used repeatedly elsewhere), the m ∼ H0 region (m/H0 ∈ [1,3]) yields β ≲ 0.28° (e.g., Δφ/fa ≈ 0.35–0.42 at m ≈ 1.8–2 H0 gives β ≈ 0.09–0.11°), which does NOT bracket 0.342° within 1σ. The body later clarifies that reaching 0.342° at Caγ=8 requires m ≳ 4 H0 or larger coupling.
- Required fix: Qualify the abstract to match the body: the box across Caγ, m/H0, θi brackets the observed value, but at Caγ = 8 the m ∼ H0 region does not; reaching 0.342° requires heavier mass and/or larger coupling. State this in the abstract or remove the bracketing claim there.

MAJOR

P1B-M6
- Location: Eq. (1), Sec. IV, p. 9
- Issue: Objective is denoted χ^2 but is an unweighted sum of squared residuals in μK^4 units.
- Problem: A χ^2 is dimensionless by construction (requires division by the per-bin variance). Using χ^2 notation for a dimensional objective can mislead readers about optimality and statistical interpretation.
- Required fix: Rename as “sum-of-squares objective” S(β) or explicitly note that this is a dimensionful, unweighted objective chosen to match public drivers; do not imply statistical χ^2 optimality.

P1B-M7
- Location: Sec. III “Key finding,” p. 7
- Issue: “H0 consistent with Planck ΛCDM at 0.3σ.”
- Problem: The reference Planck ΛCDM value and its uncertainty are not stated, so the 0.3σ cannot be independently reproduced. Using Planck 2018’s 67.4 ± 0.5 km s−1 Mpc−1 would give ≈0.6σ for 67.68 ± 1.06.
- Required fix: Provide the exact Planck reference value/σ (PR3/PR4, which likelihood), show the calculation, or drop the “0.3σ” figure and state “consistent with Planck ΛCDM” without a quantified tail distance.

MINOR

P1B-m6
- Location: Sec. IV, Noise model, p. 8
- Issue: Pixel area value quoted as Ωpix = 47.21 arcmin^2 for Nside=512.
- Problem: The exact value from 4π/(12 Nside^2), converted to arcmin^2, is ≈47.28 arcmin^2. The 0.15% discrepancy is immaterial but the 5 s.f. presentation suggests unwarranted precision.
- Required fix: Either give the exact formula (preferred) or round to 47.3 arcmin^2.

P1B-m7
- Location: Sec. IV, Noise model, p. 8
- Issue: Statement “no √2 factor; independent Gaussian realizations with the same σpix for Q and U.”
- Problem: Different collaborations define ΔP variously (per Stokes vs per polarization pair). Without a citation, readers may question the convention.
- Required fix: Add a short citation or sentence stating the convention adopted (ΔP is per Stokes parameter Q and U) and that this matches e.g. Planck/ACT map-making conventions.

P1B-m8
- Location: Sec. IV, Robustness battery, p. 11
- Issue: Claim that lensed BB is “negligible against the synthetic EE template amplitude” is qualitative.
- Required fix: Provide a representative numeric ratio (e.g., max over bins of CBB/CEE in the fit range) or cite the artifact line reporting it, to substantiate “negligible.”

P1B-m9
- Location: Fig. 3 caption, p. 9
- Issue: “Pipeline-recovery bias carried forward as the observed NaMaster pipeline bias” could be read as generally applicable despite the text’s caveats.
- Required fix: Add “for the unweighted estimator on the synthetic, foreground-free configuration” in the caption itself (you do state this in-text; mirroring it in the caption avoids misinterpretation when the figure is read standalone).

P1B-m10
- Location: Sec. IV, Estimator grid, p. 9–11
- Issue: β is evaluated on a 0.001° grid; SE of the 500-MC mean is ≈0.002° at fsky = 0.32.
- Required fix: Note that discretization error is bounded by ≈step/√12 ≈ 0.0003°, well below the reported SE, to preempt questions about grid quantization.

P1B-m11
- Location: Sec. III, “Independent cross-validation,” p. 7
- Issue: Differences quoted vs Liu et al. are “0.5σ” (H0) and “1.3σ” (S8).
- Check: Recompute gives 0.55σ and 1.29σ. Fine numerically, but add the explicit combined-σ formula for transparency (it’s given elsewhere in the paper for other tensions).

NO OTHER DISCREPANCIES FOUND
- I rechecked all other displayed percentages, σ-distances, products, and unit conversions against the adjacent inputs and found them consistent at the stated precision.
- Figure-to-text consistency (beyond the ΔNeff/Neff mislabel already flagged) is acceptable; the remaining figure captions match their body descriptions and units.
- Displayed equations (besides the χ^2 notation) are dimensionally consistent; Eq. (9) already includes the special-case handling in the prose, which I asked to mirror inline in my initial review (P1B-n2).