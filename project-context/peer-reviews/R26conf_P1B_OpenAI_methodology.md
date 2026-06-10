# P1B R26conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.53.pdf` md5=86261d4b pages=16
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5938 chars)
**Wall time**: 613.5s

---

Referee report for PRD (methodology): “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model” (16 pages)

Scope of review
- Focus: methodology rigor (statistical validity, estimator specification, internal arithmetic, dimensional consistency), traceability of every scalar in abstract/conclusions to the body, treatment of significances, and reproducibility assertions.
- I verified all quoted scalars, simple ratios, and σ-levels from the values given in the text/tables, and checked dimensional consistency of equations.
- I do not evaluate scientific novelty; I assess whether the methods/claims meet PRD standards of rigor and clarity.

Overall assessment
- The stock-CAMB ΛCDM+ΔNeff MCMC proxy is carefully labeled as a null test; numbers in Table I are internally consistent with text and with the computations I reproduced.
- The NaMaster pseudo-Cℓ E→B pipeline test is clearly framed as a Monte Carlo (MC) methods validation, not a sky measurement. However, critical details of the EB template used in the β fit (treatment of pixel window/beam) need to be made explicit, and the choice to quote a “systematic floor” based on an intentionally suboptimal, unweighted estimator when an inverse-variance estimator removes ≈80% of the bias requires revision.
- The w0wa posterior (Table II) is clearly qualified as a posterior-distance statement (not Bayes-factor/model preference), but some phrasing still overstates preference. Either run the requested nested sampling or tone the language down further.
- The spectator-ALP consistency check is transparent about priors, misalignment tuning, and coupling demands. Arithmetic checks (e.g., Caγ Δφ/fa ≈ 10.3, degree–radian conversions) are correct. A couple of citations to standard ALP coupling benchmarks are missing.

Findings

ESSENTIAL

P1B-E1 (Sec. IV, pp. 6–8): EB template and pixel-window/beam handling not fully specified
- Problem: The β estimator fits decoupled C^EB_b to sin(2β)cos(2β) C^EE_b. The text claims “the synthetic skies and the recovery template share the same spectra… the decoupled spectra are not pixel-window-deconvolved, and no pixel-window mismatch enters the β estimate.” It is not explicitly stated how C^EE_b used in the template is obtained (theory C_ℓ vs. bandpowers from the same masked/pixel-windowed pipeline), nor whether the HEALPix pixel window and any beam are included in the NaMaster field/response.
- Required fix: Explicitly state the source of C^EE entering the template (theory C_ℓ smoothed by the Nside=512 pixel window; or the same decoupled-and-binned bandpowers from the pipeline). State clearly whether a pixel window and/or beam are passed to NmtField/NmtWorkspace. Add a short check (or figure) showing that including/excluding the pixel window and/or a mock symmetric beam leaves the recovered β unchanged at the ≤10^−3 deg level, or update the bias budget if it does not. This is required to validate the central “pipeline-recovery bias” claim.

P1B-E2 (Sec. IV, p. 8): Quoted “systematic floor” is based on a suboptimal estimator
- Problem: The unweighted χ^2 template fit yields a bias of −0.032° (−0.040° at larger injection). The robustness battery shows that switching to an inverse-variance-weighted fit reduces the bias by ≈80% (to −0.006°). Nonetheless, the manuscript carries forward −0.040° as the NaMaster “systematic floor.”
- Required fix: Adopt the inverse-variance-weighted estimator as the primary pipeline (or equivalently weight by the MC covariance), recompute the recovery results, and update the quoted systematic floor accordingly; or provide a compelling, experiment-specific reason to retain the unweighted estimator for the stated purpose and revise the framing from “systematic floor” to “floor for this deliberately suboptimal estimator.” As written, carrying forward the larger bias is not methodologically justified.

MAJOR

P1B-M1 (Sec. III, pp. 2–4; Sec. V.A, p. 9; Table I, p. 4): Mixed Planck release pairing; unquantified impact at quoted precision
- Problem: The ΛCDM+ΔNeff chains use PR4/NPIPE high-ℓ CamSpec with Planck 2018 low-ℓ TT/EE and 2018 lensing. The text acknowledges no “release-pairing swap test” with PR4-consistent low-ℓ/lensing was done and that any pairing-induced bias is unquantified. Yet S8 and ΔNeff are quoted at ~1×10^−2 absolute precision.
- Required fix: Add a robustness run replacing the 2018 low-ℓ and lensing with their PR4/NPIPE counterparts (or the best available PR4-consistent low-ℓ and lensing) and report the shift in ΔNeff, H0, S8. If impractical, explicitly weaken quantitative conclusions to reflect potential pairing-induced biases and move the most precise figures (e.g., S8 = 0.827 ± 0.010) to an appendix with a cautionary note.

P1B-M2 (Sec. III, p. 3; Table II, p. 5; Sec. V.B, p. 9): Overstated inference about w0wa
- Problem: Table II and text state the w0wa posterior “disfavors” ΛCDM with w0 = −0.812 ± 0.044 (+4.3σ from −1) and wa = −0.667 ± 0.186 (−3.6σ), “requiring phantom crossing,” and call this “the canonical quintom signature.” While footnote (a) clarifies this is a posterior-distance, not Bayes-factor, statement, the language risks being read as a preference claim.
- Required fix: Replace “disfavors,” “requiring,” and “canonical signature” with neutral language such as “posterior means lie >3σ from the ΛCDM point; this is a tail-distance statement only; model preference (Bayes factors) is not assessed here.” Alternatively, add a nested-sampling ln B computation on the same likelihood stack and report evidence values.

P1B-M3 (Sec. IV, Figs. 3a–b, p. 7; Sec. IV text, pp. 6–8): Concentrate reproducibility paths/filenames in an appendix
- Problem: The body text and figure captions include long repository paths (e.g., reproducibility/p1_namaster_500mc/results/c10_robustness_battery.json), which interrupts the flow and is atypical for PRD main text.
- Required fix: Move all explicit file paths and run IDs to Appendix A (reproducibility manifest), and reduce the in-body references to brief pointers (e.g., “see Appendix A, artifact c10”).

P1B-M4 (Sec. VI, pp. 9–12): Missing citations for “O(1)” benchmark values of Caγ
- Problem: The text states that required Caγ ≳ 9 lies beyond “standard KSVZ/DFSZ benchmark range, which predicts |Caγ| ~ O(1),” but gives no citation.
- Required fix: Add standard references (e.g., axion model reviews) that define the typical ranges of Caγ for KSVZ/DFSZ-like ALPs and note any assumptions (hypercharge assignments, E/N).

P1B-M5 (Sec. IV, p. 8): Angle convention in the fit
- Problem: The estimator uses sin(2β)cos(2β). It is not explicitly stated whether β in the fit is in radians (as required by trigonometric functions) while reported in degrees elsewhere.
- Required fix: State explicitly that β is in radians inside the template and converted to degrees only for reporting.

MINOR

P1B-m1 (Abstract, p. 1; Sec. IV, p. 6; caption of Fig. 3, p. 7): Cross-procedure significances
- Observation: The manuscript consistently warns that pipeline SNR values are not sky significances and that published 2.7–2.9σ detections are the primary evidence. This is correct. Keep these warnings at every juxtaposition (they currently appear in the abstract, Sec. IV, and Fig. 3 caption). If any future edits reflow text, ensure this qualification remains adjacent to any side-by-side significance numbers.

P1B-m2 (Table I caption, p. 4; Sec. VI, pp. 9–10; Appendix C, p. 14): Version-history/correction notes in body text
- Problem: Multiple “Correction note: an earlier version…” and “an earlier draft quoted…” appear in the main text and captions.
- Required fix: Remove version-history prose from the main text/captions. If needed, include a single consolidated “Corrections relative to preprint vX” paragraph in Appendix A or the arXiv ancillary description.

P1B-m3 (Sec. III, p. 6): CMB-S4 forecast citation
- Problem: “CMB-S4 (σ(Neff) ~ 0.03) will provide the first precision test” is uncited.
- Required fix: Cite a CMB-S4 forecast or instrument whitepaper for σ(Neff) ~ 0.03.

P1B-m4 (Sec. IV, pp. 6–8): ℓ-range/bandpower choices
- Problem: Only one ℓ-range and binning are exercised. This is fine for a methods check, but the bias attribution leans on it.
- Required fix: Add a short robustness note (e.g., restricting to 30≤ℓ≤1024 vs 30≤ℓ≤800) to demonstrate estimator stability, or state explicitly that the result applies to this binning only.

P1B-m5 (Sec. IV, Fig. 3b caption, p. 7): Label clarity
- Problem: Inner/outer error bars are explained in the caption; ensure axis labels include “deg” and that the legend differentiates injected vs recovered curves.
- Required fix: Verify final figure has units on axes and a legend keyed to text.

P1B-m6 (Sec. III, p. 4): “agreement at the 0.01σ level”
- Problem: The text claims the chain’s S8 = 0.814 ± 0.008 agrees with the two-Gaussian combination 0.814 ± 0.009 “at the 0.01σ level.” The means are equal (difference ≈ 0), so “0.01σ” is unnecessary and potentially confusing.
- Required fix: Rephrase to “the means agree to three decimals” or simply “the means coincide; widths differ by ~10%.”

P1B-m7 (Sec. III, p. 4–5): Overlap integrals
- Problem: Overlap integrals (0.05 and 0.12) are quoted without method.
- Required fix: Add a one-sentence definition (e.g., 1D integral of min of two Gaussians with stated means/variances) or move the numbers to Appendix with method.

P1B-m8 (Table III, p. 10): Lensing choice
- Problem: iter2 uses “planck 2018 lensing.native,” while ΔNeff chains use “.clik.” This is a minor inconsistency.
- Required fix: State briefly why native vs clik were chosen in each case and confirm they are numerically consistent for your purposes (or add a quick cross-check).

P1B-m9 (Sec. VI, p. 11): βfree chain length
- Problem: The model-independent βfree fit reports 720 accepted samples. While adequate for a 1-parameter Gaussian, a sentence justifying this (effective samples, R̂) would close the loop.
- Required fix: Add a brief note that R̂ < 0.01 and ESS ≫ 100 for βfree.

NITS

P1B-n1 (Throughout): Hyphenation/spaces in units
- Fix minor inconsistencies: “µK · arcmin” vs “µK·arcmin”; choose one.

P1B-n2 (Acknowledgments, p. 13): AI assistant mention
- PRD may have evolving policies on the use of generative AI in writing. Consider consulting the editor and, if needed, moving or rephrasing the acknowledgment.

P1B-n3 (Stylistic dashes): Excessive use of em–dashes
- Consider smoothing long em-dash chains into sentences for readability.

P1B-n4 (Typographic consistency): Thousands separators
- Use consistent thousands separators in figure legends/captions (e.g., “176,240 samples,” not “176 240”).

Arithmetic and dimensional audits (selected checks)

- ΔNeff posteriors (Table I): −0.020 ± 0.169 (full-tension) and +0.065 ± 0.17 (Planck+BAO+SN) match text and figures. H0 values and uncertainties are consistent; the 3.6σ H0 tension is correctly computed: |73.04−67.68|/sqrt(1.06^2+1.04^2)=3.61.
- S8 combination: Combining 0.827 ± 0.010 with 0.776 ± 0.017 gives 0.814 ± 0.0086 (weights 10,000 and 3,460), consistent with chain 0.814 ± 0.008.
- S8 tension vs DES-Y3: (0.827−0.776)/sqrt(0.010^2+0.017^2) = 2.59σ; quoted 2.6σ and overlap integral ≈0.05 are reasonable.
- w0wa pivot math (Table II footnote b): ap=0.790, zp=0.27, σ(wpivot)=0.0193, wpivot=−0.952—matched.
- EB pipeline: bias from 0.27° injection is −0.032° (0.238°/0.27° = 0.882), and from 0.342° injection is −0.040° (0.302°/0.342° = 0.883), i.e., ≈12% multiplicative under-recovery—matched. Per-realization σβ at fsky=0.32 of 0.046° gives SE ≈ 0.002° for N=500—adequate to quote millidegree biases.
- ALP birefringence normalization (Eq. 3): αEM/(4π)=5.80×10^−4, multiplied by Caγ=8 and Δφ/fa=1.06 gives 4.93×10^−3 rad, i.e. 0.282°—correct. Product Caγ Δφ/fa required by βobs=0.342°: 0.342°×π/180 / (αEM/4π) ≈ 10.3—correct. Required Caγ range from Δφ/fa ∈ [0.064,1.19] is [~160, ~8.6]—correct.
- Inverse-variance combo of Planck NPIPE 0.30±0.11 and ACT DR6 0.215±0.074 gives 0.241±0.061 (3.9σ)—correct, with appropriate caveat on correlations.

Length
- 16 pages is acceptable for a technical methods companion; however, moving reproducibility file-path details to Appendix A would improve readability of the main text.

## Summary recommendation
MAJOR REVISIONS

The core analyses are competently executed and carefully scoped, and the arithmetic checks out. However, for PRD-level methodological rigor, the NaMaster β-estimator specification needs to be explicit about the EB template (pixel window/beam handling) and should adopt the inverse-variance-weighted fit that removes ~80% of the bias before quoting a “systematic floor.” The mixed Planck release pairing requires either a quick robustness check or a clear caveat commensurate with the quoted precision. Language implying model preference in the w0wa section must be softened unless a Bayes-factor analysis is added. Several version-history notes should be removed from the main text. Addressing these will bring the manuscript up to PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes re-audit)

ESSENTIAL

P1B-E3 (Sec. III, Caveats (c), p. 4): Chain mix-up for H0 without SH0ES
- Problem: In the ΛCDM+ΔNeff section, Caveat (c) cites “the joint posterior H0 = 67.185 ± 0.455 km/s/Mpc is therefore the no-SH0ES result.” That value and precision match Table II (the separate w0wa DESI DR2 + DES-Y5 chain), not the ΛCDM+ΔNeff Planck+BAO+SN chain in Table I (67.79 ± 1.09). This blurs the chain identity within the ΔNeff section.
- Required fix: Replace the H0 number in Caveat (c) with the Planck+BAO+SN ΔNeff-chain value (67.79 ± 1.09), or move this caveat to the w0wa section with an explicit chain label. As written, it misattributes the H0 value to the ΔNeff chain.

P1B-E4 (Sec. III, “Independent cross-validation,” p. 6): Missing exponent-2 in σ-combination expressions
- Problem: The text shows √(1.092 + 0.322) and √(0.0102 + 0.0062) when computing combined uncertainties. These read as “1.092 + 0.322” and “0.0102 + 0.0062,” not 1.09^2 + 0.32^2 and 0.010^2 + 0.006^2. The final σ-levels reported are correct only if the squares are intended; the notation as printed is misleading and dimensionally wrong.
- Required fix: Explicitly write the squares in-line (e.g., √(1.09^2 + 0.32^2) and √((0.010)^2 + (0.006)^2)), or present the computed combined σ numerically to avoid confusion.

MAJOR

P1B-M6 (Fig. 4 caption vs Sec. VI text, pp. 10–12): Inconsistent “EOM-required coupling band” for Caγ
- Problem: The Fig. 4 caption states the continuous-prior Caγ ∈ [4, 60] “cover[s] the posterior-supported coupling band (median 20.7, 16–84% [7.3, 45.6]); the dropped [1, 4) interval lies entirely below the EOM-required minimum ≈ 8.6 — θi ∈ [0.01, π], log10(ma/eV) ∈ [−35, −30].” Elsewhere in Sec. VI, the text alternately calls the “full EOM-required band” [9, 51] (implied by adopting Δφ/fa ≥ 0.20 so that Caγ = 10.3/(Δφ/fa) ≤ 51.5) and also discusses the broader envelope up to ≈160 when Δφ/fa ≈ 0.064. These thresholds (0.17 vs 0.20) and numerical bounds ([9, 51] vs [9, 60] vs [8.6, 160]) are not reconciled.
- Required fix: Define precisely which Δφ/fa domain “EOM-required” refers to (full physical envelope vs posterior-supported subdomain), and use a single set of numbers consistent with that choice. If the intent is “posterior-supported Δφ/fa ≳ 0.17 implies Caγ ≤ 60,” then state that explicitly and update the caption/body bounds consistently.

P1B-M7 (Sec. VI, p. 12): Spectator-slice fraction inconsistency (weighted vs count fraction)
- Problem: The text states “the strict θi ≤ 0.1 sliver … carries only 0.33% of the posterior mass by MC weight (42 of the 8,955 raw samples).” The parenthetical sample fraction 42/8,955 ≈ 0.469%, not 0.33%. If 0.33% is a weight-weighted fraction, the mismatch with the count-based parenthetical is confusing.
- Required fix: Report both numbers explicitly (e.g., “0.33% by posterior weight; 0.47% by raw count”) and clarify which is used for subsequent statements.

P1B-M8 (Fig. 1 caption vs footnote 1, p. 6): Sample-count/thinning description unclear
- Problem: Fig. 1 caption says “119,617 post-burnin samples, getdist-thinned from 176,240 raw,” while footnote 1 quotes post-burnin counts of 123,129 and 123,368 (before thinning). The plotted sample count and thinning method (weight-based vs random) are not aligned between caption and footnote.
- Required fix: Provide a single, consistent description for the plotted set: raw count, post-burnin count, thinning factor/method, and final plotted N. This improves traceability of the plotted contours.

MINOR

P1B-m10 (Sec. IV, p. 8): Phrase implies observation-error dependence on fsky
- Observation: “The total bias remains well below the published observational uncertainty σobsβ = 0.094° at every sky fraction tested.” The observation σ does not depend on the simulation fsky; the intended point is the bias magnitude is < 0.094°.
- Suggested edit: “The measured pipeline bias is < 0.094° (the published observational uncertainty) for all simulated sky fractions.”

P1B-m11 (Conclusions, p. 12): Partially converged Planck-only chain mention
- Observation: The text mentions an accumulating Planck-only run (114,992 samples; R̂−1 ≈ 0.05). Mentioning a non-converged chain and its sample count in Conclusions distracts and may confuse readers.
- Suggested edit: Move this note to Appendix A or remove.

P1B-m12 (Sec. VI, Eq. (2), p. 9): Initial-condition specification
- Observation: Δφ/fa ≈ 0.42 is quoted “from recombination to today” at m = 2H0, θi = 1. The starting redshift and initial field velocity (e.g., frozen field with φ̇ ≈ 0) should be stated explicitly here (they are implicit in the ALP ODE integration, but not spelled out).
- Suggested fix: Add a short parenthetical: “(integration from z = 1100 to 0 with initial φ̇ ≈ 0 at recombination).”

P1B-m13 (Sec. IV, Fig. 3): Axis units and legend linkage
- Observation: While the caption explains inner/outer error bars, it is not explicit in the figure whether axes are in degrees and whether symbols/colors map to injected vs recovered. Ensure the final figure labels “deg” on axes and the legend matches the caption’s terminology.

P1B-m14 (Sec. VI, p. 12): LiteBIRD “will settle this at ~9σ”
- Observation: The text later correctly notes this is not a model-discrimination forecast, only a β ≠ 0 statistical precision statement. To avoid overstatement, keep “statistical” visible at the claim: “LiteBIRD is forecast to measure β at ~9σ statistical significance if β ≈ 0.27°.”

EXPLANATION
The fresh-eyes pass focused on:
- Arithmetic/notation slips that could mislead (E4),
- Cross-chain number leakage in the ΔNeff section (E3),
- Internal consistency of the ALP coupling-band narrative (M6),
- Weighted vs raw-count fraction clarity (M7),
- And a few presentation/traceability polish points (M8, m10–m14).

These items were not covered in the initial review and, if addressed, will further strengthen rigor and clarity.