# P4 R25conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 499.4s

---

META-REFEREE REPORT (new issues not caught by the five prior referees)

P4-META-E1
- Severity: ESSENTIAL
- Location: Appendix A, item a (pp. 13–14), and Sec. IV C b (pp. 8–10)
- Why others missed it: Prior reviews focused on null taxonomy and unit conventions but not on the definitional consistency of the field versus the footprint mask.
- Specific problem (quote + explanation):
  • “The MASTER diagnostic estimator … uses a single declared data vector: the monopole-subtracted CW-deficit map fCW(ˆn) − 0.5 on the real analysis footprint (Nall ≥ 1 …). The asymmetry field is Ap = (NCW − NCCW)/Nspiral (Eq. 3; spirals-only denominator). The … mask assigns Wp = Nall …”
  • This mixes an Ap field (undefined where Nspiral(p) = 0) with an analysis footprint defined purely by Nall ≥ 1. On that mask, many pixels will have Nspiral = 0 (since ~62% of objects are NS), so Ap is undefined in some footprint pixels. The manuscript never states whether such pixels are masked out a second time (Nspiral ≥ 1) or assigned Ap = 0 (which would bias mean subtraction and coupling). This is a definitional inconsistency between the declared field and footprint.
- Required fix:
  • Explicitly state the effective field mask used for all harmonic-channel computations (e.g., “analysis footprint Nall ≥ 1 intersected with Nspiral ≥ 1”).
  • Recompute and report the ℓ = 1 diagnostic statistics using a field/mask pair that is self-consistent (Ap with a mask that requires Nspiral ≥ 1), or demonstrate via a quantitative check that including Nspiral=0 pixels (if set to Ap=0) does not bias C1 (show ΔC1 and Δσ under Nspiral-weighted masks).


P4-META-E2
- Severity: ESSENTIAL
- Location: Appendix A, item a (pp. 13–14)
- Why others missed it: Prior reviews flagged unit and null inconsistencies but not the internal contradiction in the field description itself.
- Specific problem (quote + explanation):
  • “uses a single declared data vector: the monopole-subtracted CW-deficit map fCW(ˆn) − 0.5 … The asymmetry field is Ap = …”
  • The text claims one “single declared data vector,” but then refers to two different field definitions (monopole-subtracted fCW−0.5 versus Ap with a separately quoted monopole subtraction ⟨A⟩mask,gw = −0.005294). It is unclear which field (and which normalization) underlies the specific C1 values quoted in Sec. IV C b and Table III.
- Required fix:
  • Unambiguously define the data vector used in each harmonic result (e.g., “All canonical-mask values use Ap (spiral-only) with galaxy-weighted mean subtraction; all apodized-footprint values use fCW−0.5, …”). Add a small table mapping each reported C1 to its exact field, mask, weight, and whether a monopole subtraction was applied.


P4-META-M1
- Severity: MAJOR
- Location: Sec. VI A (pp. 11–12), Table V; also Sec. IV C a (pp. 6–8)
- Why others missed it: Prior reviews noted axis priors and nulls but not the generative specification for the injection itself relative to the non-50/50 monopole.
- Specific problem (quote + explanation):
  • “The injection–recovery sweep … scorer’s σ convention … against a fixed calibration of 1000 per-pixel binomial label-shuffle realizations nCW(p) ∼ Binomial(Nspiral(p), pglobalCW) … Each injection draws an independent random dipole axis …”
  • The manuscript never states the exact probability model for the injected signal when the global monopole is not 0.5. Is pCW(n̂) = pglobalCW + (A/2) cos θ (baseline=0.4974), or pCW(n̂) = 0.5 + (A/2) cos θ and then re-centered? This matters because A is defined as a full-amplitude perturbation around 0.5, yet the null realizations preserve pglobalCW ≠ 0.5. Without the explicit injection formula, mapping between “A in %” and the realized Ap field is ambiguous.
- Required fix:
  • Specify the injection generative model explicitly (baseline probability, how A is added, treatment of probabilities outside [0,1]).
  • Re-run, or at least verify, that using pglobalCW versus 0.5 as the baseline does not shift A50/A95 materially; if it does, report both variants and use the physically appropriate one going forward.


P4-META-M2
- Severity: MAJOR
- Location: Appendix C, item c (p. 16)
- Why others missed it: Reviewers noted look-elsewhere framing but did not spot the double application of LEE corrections.
- Specific problem (quote + explanation):
  • “The direct-MC look-elsewhere test (N = 10,000 random-label shuffles of the maximum statistic) gives pLEE ≤ 10−4 … The Bonferroni correction multiplies the smallest per-direction p by the 648 tested directions … the Benjamini–Hochberg step-up FDR … yields the same verdict — both reduce the post-LEE significance to < 1σ.”
  • This applies an additional Bonferroni/BH pass after already computing the null distribution of the max statistic by direct Monte Carlo (which already incorporates the trials). This is a double (over-)correction that can confuse readers and distort interpretation.
- Required fix:
  • Report only the direct-MC max-statistic pLEE (with its uncertainty from finite NMC). Remove the extra Bonferroni/BH application, or move it to a footnote as a nonstandard, super-conservative bound with an explicit warning not to interpret it as a second, necessary correction.


P4-META-M3
- Severity: MAJOR
- Location: Appendix A, item a (p. 13–14)
- Why others missed it: Prior reviews questioned the σ change after monopole subtraction but not the weighting mismatch inherent in the mean subtraction for Ap.
- Specific problem (quote + explanation):
  • “Field: … Ap … with galaxy-weighted mask-mean subtraction ⟨A⟩mask,gw = −0.005294.” Earlier in the same item, “The … mask assigns Wp = Nall …”
  • The Ap field uses spiral-only counts in numerator and denominator, but the mean subtraction is performed with weights Wp = Nall (all galaxies). This is a non-matching choice: deep pixels with many non-spirals drive the mean subtraction of a field that is defined only on the spiral subset. This could materially change the effective removal of the monopole and the resulting low-ℓ coupling.
- Required fix:
  • Repeat the harmonic-channel Ap analysis with mean subtraction weighted by Nspiral (and also with uniform weights) and report the change in C1 and its σ under each choice. Adopt the weighting that is consistent with the field definition (Nspiral) as the default, or justify why Nall-weighting is superior for this purpose.


P4-META-M4
- Severity: MAJOR
- Location: Appendix B, item d (p. 15), Test T5; and supporting text immediately following
- Why others missed it: Reviewers accepted T5 at face value; the circular-variable pitfall is easy to overlook.
- Specific problem (quote + explanation):
  • “T5 metadata leakage (|r(pCW, RA/Dec)| < 0.10).” Pearson correlation with raw RA is not a proper test for directional coupling because RA is a circular variable (0° ≡ 360°), and linear correlation with RA can be artificially small even with strong azimuthal patterns.
  • Although a low-ℓ Yℓm regression is later presented as a “stronger, map-level supplement,” T5 is still advertised as a passed test in the main bias-hardening list.
- Required fix:
  • Replace T5 with a circularly appropriate test (e.g., regression on sin(RA), cos(RA), or explicit Yℓm up to ℓ=3), and report those coefficients and σ. If retaining T5, explicitly state its limitations and do not count it as an independent pass criterion.


P4-META-M5
- Severity: MAJOR
- Location: Sec. VI A & Table V (pp. 11–12)
- Why others missed it: Others focused on axis priors and nulls but not on sampling error presentation.
- Specific problem (quote + explanation):
  • Table V reports P(σ > 3) values (e.g., 0.55 at A = 0.75%) from NMC,inj = 100 injections per amplitude, but no binomial uncertainties are shown. Near the 50% crossing, the standard error is ~5% (√[p(1−p)/100]), which is material for quoting A50 to two decimals.
- Required fix:
  • Add binomial error bars (e.g., ±1σ or 68% Clopper–Pearson intervals) to P(σ > 3) in Table V and reflect this uncertainty in the quoted A50 and in the “falsification” sentence.


P4-META-m1
- Severity: MINOR
- Location: Sec. IV C a (p. 7) and Appendix A, item a (pp. 13–14)
- Why others missed it: Several reviewers discussed comparability but not this specific juxtaposition.
- Specific problem (quote + explanation):
  • On p. 7: “AUL95 = 6.8 × 10−3 in Ap units …” and in Appendix A: “Monopole subtraction reduces decoupled C1 … and increases σ from +1.85 to +3.64 (the canonical-mask number).”
  • The “AUL95” estimator-level rank bound is reported for the real-space estimator; the 3.64σ canonical harmonic result (with mean-subtracted field) is reported elsewhere. Nowhere is it stated whether these two bounds are computed on identically normalized fields (they are not), nor is a cross-map of the amplitudes provided in one unit convention in a single place for the reader.
- Required fix:
  • Add a compact “amplitude conventions at a glance” box that lists, side-by-side, the headline real-space amplitude (Adip), its 95th-percentile null bound, and the corresponding master-channel C1 amplitudes with their field definitions and unit conversions (Ap vs fCW vs full-amplitude A). This will prevent misreadings across sections.


P4-META-m2
- Severity: MINOR
- Location: Appendix C, item c (p. 16)
- Why others missed it: Others asked for grid detail but not the statistical reproducibility metadata.
- Specific problem (quote + explanation):
  • The 10° grid is described as “36 × 18 = 648 directions,” but the random-label max-statistic null uses N = 10,000 realizations without stating whether the same seed/grid ordering is used for both data and null (relevant for bitwise reproducibility), nor whether poles/edge latitudes are included.
- Required fix:
  • Add one sentence specifying the exact latitude vector (e.g., from −85° to +85° in 10° steps with poles excluded), the longitude step (e.g., 10° starting at 0°), and that the same grid and seed protocol are used for all max-statistic null draws.


P4-META-m3
- Severity: MINOR
- Location: Sec. IV C a (p. 7)
- Why others missed it: Others focused on estimator comparability; this is a clarity nit.
- Specific problem (quote + explanation):
  • “The regenerated 10^4-permutation null array also yields a formal upper limit … max(Aobs, A95UL) coincides with it since Aobs < A95UL …”
  • The “max(Aobs, A95UL)” construction is introduced without a defined inferential purpose and could be misread as a confidence interval edge; it is not.
- Required fix:
  • Remove “max(Aobs, A95UL)” from the main text or re-label it explicitly as a descriptive estimator-level bound with no coverage guarantee, and do not use it in any scientific conclusion.


P4-META-n1
- Severity: NIT
- Location: Appendix D, g. WLS (pp. 16–17)
- Why others missed it: Focus was on the z ≈ −18 exclusion, not block bootstrap geometry.
- Specific problem (quote + explanation):
  • “block-bootstrap at NSIDE = 8 (Nboot = 1000, 440 super-pixels) … inflates σ(Adipole) … by 14.7×.”
  • The text does not specify the resampling scheme (with/without replacement of super-pixels, how mask holes are handled, whether weights are re-normalized per resample). Given the large inflation factor, these details matter.
- Required fix:
  • Add two lines describing the block bootstrap protocol (resampling unit; replacement; re-weighting; handling of mask edges) and, ideally, verify that using NSIDEdir alternatives (e.g., 6, 10) leaves σboot within stated tolerance.


## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, the blocker count remains high: several ESSENTIAL/MAJOR issues (field/mask inconsistency for Ap on Nall≥1, contradictory field declaration fCW vs Ap in the same estimator, unspecified injection generative model relative to a non-50/50 monopole, double look-elsewhere correction, and mean-subtraction weighting mismatch) must be clarified and, where necessary, recomputed. My confidence that the paper would survive external, non-lab peer review is moderate provided these are addressed: the core real-space null seems robust, but the harmonic-channel diagnostics and injection-recovery sections need the above clarifications and small re-analyses to meet PRD standards of reproducibility and internal consistency.