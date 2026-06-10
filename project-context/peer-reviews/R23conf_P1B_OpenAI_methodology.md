# P1B R23conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.51.pdf` md5=856fbad2 pages=13
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6472 chars)
**Wall time**: 411.9s

---

Referee report on “Technical Verification Companion to the ECH Spin‑Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of review
I evaluated the full 13‑page manuscript for methodological rigor, statistical validity, internal numerical and dimensional consistency, the correctness of all quoted significances and uncertainties, and the traceability of every load-bearing scalar in the abstract and conclusions to the body of the paper. I also audited figures, tables, captions, and equations for consistency and clarity.

Overall assessment
The manuscript is largely careful about scope and significance, repeatedly warning against over-interpretation of proxy and pipeline-validation results and distinguishing template-fit SNRs from sky-detection significances. Most headline numbers in the abstract and conclusions trace correctly to tables/sections and are arithmetically consistent when recomputed. However, I identified several issues that must be corrected before the paper meets PRD methodological standards. Two are essential: an internal inconsistency in the NaMaster validation narrative about negative-β injections, and a factor-of-ten error in a figure caption converting a mass prior to m/H0 bounds. I also flagged a few further major and minor issues detailed below.

Findings

ESSENTIAL

P1B-E1
- Location: Sec. IV, p. 6 (main text paragraph “Noise model and injections” and the paragraph beginning “Production 500-realization run (April 2026)”), and footnote 3 on p. 6.
- Problem: Internal inconsistency about negative-β validation. The main text states “Only non‑negative injections were run; a negative‑β injection (sign-symmetry/linearity check) is not part of the present MC suite and is an acknowledged validation gap.” But footnote 3 reports a dedicated 500‑MC rerun at fsky = 0.32 with β = −0.27° recovering −0.238° (|bias| = 0.032°), demonstrating sign symmetry and also reporting σβ = 0.046°.
- Required fix: Harmonize the narrative. Either:
  - Move the sign-symmetry result from footnote 3 into the main text and update the “acknowledged validation gap” sentence to state that the gap has been closed by a dedicated 500‑MC rerun; or
  - If you intend to keep the canonical run definition strict, explicitly state that the canonical archived run lacked negative injections, but a documented supplementary rerun addressed the sign-symmetry check, and cite the artifact path.
In either case, the paper must not simultaneously claim a validation gap and present its closure in a footnote.

P1B-E2
- Location: Fig. 4 caption, p. 10 (last two lines of caption).
- Problem: Factor‑of‑ten error in converting the log10(ma/eV) prior to the implied m/H0 bounds. The caption states that log10(ma/eV) ∈ [−35, −30] “corresponds to m/H0 ≈ 7×10−3 to 7×10^2 for H0 = 67.7 km/s/Mpc = 1.44×10−33 eV.” The lower bound is incorrect by a factor ~10. Using H0 ≈ 1.44×10−33 eV, the ratio spans:
  - m/H0 = 10^−35 / 1.44×10^−33 ≈ 6.9×10^−2 (not 7×10^−3),
  - to 10^−30 / 1.44×10^−33 ≈ 6.9×10^2.
- Required fix: Correct the caption to “m/H0 ≈ 7×10^−2 to 7×10^2” and verify that any related text using this range is consistent.

MAJOR

P1B-M1
- Location: Sec. III, p. 5 (“Independent cross-validation.” paragraph).
- Problem: Incorrect notation for quadrature combination of uncertainties. The text reads “agree with our Planck+BAO+SN chain at 0.5σ in H0 (|67.79−68.41|/√(1.092 + 0.322)) and 1.0σ in S8 (|0.831−0.812|/√(0.0182 + 0.0062)).” This mixes variances and standard deviations in the denominator and omits squares. The correct combined uncertainty should be σcomb = √(σ1^2 + σ2^2).
- Required fix: Replace the expressions with
  - H0: |67.79 − 68.41| / √(1.09^2 + 0.32^2) ≈ 0.62 / 1.14 ≈ 0.55σ,
  - S8: |0.831 − 0.812| / √(0.018^2 + 0.006^2) ≈ 0.019 / 0.019 ≈ 1.0σ,
and ensure the notation throughout uses quadrature (squares) for independent Gaussian errors.

P1B-M2
- Location: Sec. IV, p. 7 (paragraph beginning “The deconvolution is therefore unbiased…”).
- Problem: Misuse of “unbiased.” The text says “The deconvolution is therefore unbiased at the |Δβ̂| ≤ 0.040° level…,” but a nonzero bias has been measured (−0.032° to −0.040°). “Unbiased” is incorrect.
- Required fix: Rephrase to, e.g., “The deconvolution bias is bounded at |Δβ̂| ≤ 0.040° in the worst-case injection; we adopt 0.040° as the NaMaster systematic floor.”

P1B-M3
- Location: Sec. VI, Eq. (3) and surrounding paragraph, p. 9.
- Problem: The derivation of Eq. (3) relies on Δφ/fa ≈ 1.07 for m ≈ 2H0 and θi = 1 but the numerical origin (integration starting redshift, initial conditions, and background H(z) prescription) is not specified in the main text. Reproducibility should not require the reader to hunt through repository artifacts for essential ODE settings that determine the 17% “above natural envelope” statement later in the section.
- Required fix: Add a short methodological sentence in Sec. VI specifying the ODE setup sufficient to reproduce Δφ/fa: e.g., initial conditions (φi = fa θi at high z with φ̇i = 0), start redshift (or scale factor), numerical integrator and step control, and the background H(z) used (ΛCDM with explicit Ωm, ΩΛ values consistent with Table II or Table I).

MINOR

P1B-m1
- Location: Fig. 2a legend, p. 6.
- Problem: The legend label “SM ( Neff = 0)” is ambiguous, since the plotted parameter is ΔNeff. The Standard Model value corresponds to ΔNeff = 0, not Neff = 0.
- Required fix: Change the legend to “SM (ΔNeff = 0).”

P1B-m2
- Location: Sec. IV, footnote 3, p. 6 (“per‑realization angle‑recovery ratio β/σ̂β … measured … as 8.1 and 7.2”).
- Problem: The symbol β here denotes the recovered amplitude β̂ (since 0.238°/0.029° ≈ 8.2 and 0.236°/0.033° ≈ 7.2), not the injected β = 0.27°. This is potentially confusing.
- Required fix: Replace “β/σ̂β” with “|β̂|/σ̂β” to avoid ambiguity.

P1B-m3
- Location: Sec. IV, p. 6–7 (SNR discussion in main text and footnote 3).
- Problem: The paper carefully distinguishes template-fit SNR from sky-detection significance in several places, but in one spot the words “template-fit SNR = 25.71; for β = 0, the recovered angle is 0.000° with template-fit SNR 0.0 (null check)” appear without an explicit reminder that this SNR is not a sky significance. While this is stated elsewhere, adding a brief parenthetical here would eliminate any possible misreading.
- Required fix: Append “(pipeline template-fit SNR; not a sky-detection significance)” at this location.

P1B-m4
- Location: Sec. IV, p. 6 (“bins above the map band limit ℓ = 1024 carry noise only”).
- Problem: Slightly imprecise phrasing. Pixel-space white noise on a HEALPix grid has power to ℓ ≲ 3Nside. The statement is true as written for the simulated CMB signal but could be misunderstood.
- Required fix: Clarify that “CMB signal power vanishes above ℓ = 1024, while pixel white noise contributes up to ≈ 3Nside, so high-ℓ bins contain noise only.”

P1B-m5
- Location: Sec. III, p. 5 (MB–H0 joint‑posterior offset check).
- Problem: The computed constant “−28.415” differs slightly from direct recomputation (−28.418) due to rounding of log10(67.68). The stated 0.156 mag offset remains consistent to the stated precision.
- Required fix: Optional: either retain as-is with a note “(rounding at the 0.001 mag level)” or update the constant to −28.418 to match a more precise evaluation; the 0.156 mag offset can be stated as 0.154–0.156 mag depending on rounding.

NIT

P1B-n1
- Location: Throughout (e.g., multiple line breaks within words, such as “de￾convolution”).
- Problem: Hyphenation artifacts from PDF extraction.
- Required fix: Ensure final typeset copy has correct word breaks.

P1B-n2
- Location: Sec. V, p. 8 (“We do not report χ2eff, AIC, BIC, or ln B…”).
- Problem: Stylistic. Consider adding a one-sentence rationale in the main text (not just in the footnote) that a Savage–Dickey estimator is inappropriate when the null point lies beyond the sampled region, to underscore methodological prudence.

P1B-n3
- Location: Sec. IV, p. 6 (“deterministic seeds (seed base=42)”).
- Problem: While reproducibility is commendable, explicit seed values are better placed in the repository README or Appendix A to keep the main text focused.
- Required fix: Consider moving this parenthetical to Appendix A.

Audit highlights (selected recalculations verified)
- Table I abstract numbers: ΔNeff = −0.020 ± 0.169 and +0.065 ± 0.17; H0 = 67.68 ± 1.06 and 67.79 ± 1.09 (km s−1 Mpc−1). All match Table I and are internally consistent.
- Hubble tension significance: |73.04 − 67.68| / √(1.04^2 + 1.06^2) ≈ 3.61σ (stated ~3.6σ) — consistent.
- DES-Y3 S8 tension: |0.8245 − 0.776| / √(0.0089^2 + 0.017^2) ≈ 2.52σ — consistent with “2.5σ”.
- w0 departure: |−0.8122 + 1| / 0.0436 ≈ 4.31σ; wa departure: |−0.6666| / 0.1864 ≈ 3.58σ — consistent with +4.3σ and −3.6σ in Table II. wpivot = −0.952 ± 0.019; Δ/σ ≈ 2.6σ — consistent with +2.5σ claim.
- Inverse-variance combination of Planck NPIPE (0.30 ± 0.11) with ACT DR6 (0.215 ± 0.074): 0.242 ± 0.061 (3.95σ) — consistent with Eq. (4).
- ALP birefringence prefactor (Eq. 3): β ≈ (αEM/4π) Caγ Δφ/fa with αEM/(4π) ≈ 5.8×10^−4; with Caγ = 8, Δφ/fa ≈ 1.07 gives β ≈ 0.285° — consistent with “≈ 0.29°.”
- NaMaster multiplicative under-recovery: 0.238/0.27 ≈ 0.88 and 0.302/0.342 ≈ 0.88 — consistent with ~12% under-recovery. Absolute bias grows ≈ 25% from 0.032° to 0.040° — consistent.

Length
At 13 pages, the paper is within a reasonable range for a methods companion paper covering three distinct analyses. No length reduction is requested.

## Summary recommendation
MINOR REVISIONS

The work is methodologically careful overall and most numerical claims are internally consistent and properly scoped. However, before acceptance the authors must correct the internal inconsistency about negative‑β injections in the NaMaster validation (E1) and fix the factor‑of‑ten error in the Fig. 4 caption converting mass-prior bounds to m/H0 (E2). I also request correcting the error-combination notation and a few clarifying phrasing/label fixes. With these addressed, the manuscript would meet PRD methodological standards for a technical verification companion.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (fresh-eyes audit)

P1B-M4
- Class: E (null-procedure comparability) and H (unquantified hedge)
- Location: Sec. III, “Key finding.” paragraph (p. 5)
- Problem: “H0 consistent with Planck ΛCDM at 0.3σ” is ambiguous. It is unclear which Planck baseline value and uncertainty are used as the comparator (Planck 2018 baseline TTTEEE+lowE+lensing ≈ 67.4 ± 0.5 km s−1 Mpc−1? Some NPIPE value?). Using the two chains’ values against each other gives |67.68 − 67.79|/√(1.06^2 + 1.09^2) ≈ 0.07σ, not 0.3σ. The 0.3σ is plausible only if compared to a specific Planck baseline, but that comparator and the arithmetic are not shown.
- Required fix: State explicitly the comparator (value and σ) and show the calculation. If the intent was “consistent with the Planck 2018 baseline H0 = 67.4 ± 0.5,” write “|67.68 − 67.4|/√(1.06^2 + 0.50^2) ≈ 0.24σ (≈ 0.3σ).” If the comparand is different, specify it and recompute.

P1B-M5
- Class: B (figure-caption vs body claim) and J (stale numbers)
- Location: Sec. VI, auxiliary inverse-variance combination; Audit highlights
- Problem: Mixed values for the same two-number combination. The body text reports βcombined = 0.241° ± 0.061°, while your “Audit highlights” recomputation (and a fresh recompute) gives 0.242° ± 0.061°. The difference is small but avoidable.
- Required fix: Choose one rounded value consistently (e.g., 0.242° ± 0.061°) and use it everywhere (text, equations, audit notes).

P1B-m6
- Class: A (arithmetic phrasing)
- Location: Sec. IV, footnote 3, last sentence of the long paragraph
- Problem: “The standard error of the 500-MC mean is smaller by √N = 22.4.” As written, this can be read as multiplying rather than dividing.
- Required fix: Rephrase to “The standard error is the per-realization scatter divided by √N = 22.4.”

P1B-m7
- Class: D (internal cross-references/consistency)
- Location: Sec. IV, Fig. 3 caption (“adopted in Eq. 1–fn. 3”)
- Problem: The reference style “Eq. 1–fn. 3” is nonstandard and a bit opaque. Readers expect either “Eq. (1) and footnote 3” or explicit pointers in-text.
- Required fix: Replace with “adopted in Eq. (1) and footnote 3” (or cite the exact subsection/line where the floor is defined).

P1B-m8
- Class: C (equation dimensional clarity/notation)
- Location: Sec. VI, ALP equation of motion
- Problem: The EOM ϕ¨ + 3Hϕ˙ + m^2 fa sin(ϕ/fa) = 0 is dimensionally consistent in natural units, but most readers expect V′(ϕ) = m^2 fa sin(ϕ/fa) to be connected to V(ϕ) = m^2 f_a^2[1 − cos(ϕ/f_a)]. That link is only implicit.
- Required fix: Add a parenthetical “with V(ϕ) = m^2 f_a^2[1 − cos(ϕ/f_a)], so V′(ϕ) = m^2 f_a sin(ϕ/f_a).” This removes any ambiguity about normalization.

P1B-m9
- Class: E (null-procedure comparability)
- Location: Sec. VI, paragraph beginning “MCMC parameter estimation.”
- Problem: The text states “All three within 1σ” when comparing βALP, βfree, and βobs, but βfree is constrained by a Gaussian summary likelihood centered on βobs with nearly the same σ, so the agreement is tautological rather than an independent check (you do note this later, but the “within 1σ” phrasing can still mislead).
- Required fix: Add “trivially, because βfree is fit directly to the same Gaussian summary likelihood centered on βobs; this is an internal consistency check, not an independent confirmation.”

P1B-m10
- Class: F (abstract faithfulness/precision)
- Location: Abstract, sentence “Both frozen dataset combinations find ΔNeff consistent with zero and H0 consistent with standard ΛCDM…”
- Problem: As in P1B-M4, “consistent with standard ΛCDM” lacks the explicit comparator. Since the abstract front-loads this claim, it would help readers if the comparator (e.g., Planck 2018 baseline) is clearly stated in the body at first mention.
- Required fix: In Sec. III, immediately after the H0 numbers, specify which Planck baseline is meant and the resulting σ-distance (see P1B-M4). Optionally add a brief parenthetical in the abstract (“consistent with the Planck 2018 baseline within ~0.3σ”) once the body text is fixed.

P1B-m11
- Class: I (appendix vs main-text match) and terminology clarity
- Location: Footnote 2 (p. 3), strong-coupling scale description
- Problem: “Scale Λstrong ∼ MPl/√γBI set by the inverse Barbero–Immirzi parameter γBI.” Referring to γBI as the “inverse” Barbero–Immirzi parameter while writing Λ ∝ 1/√γBI is potentially confusing (is γBI ≡ 1/γ in your notation?).
- Required fix: Clarify the notation explicitly: e.g., “Λstrong ∼ MPl/√|γ|, with γ the (dimensionless) Barbero–Immirzi parameter.” Avoid calling γBI “inverse” if you then divide by √γBI.

P1B-m12
- Class: B (figure-caption vs body claim, units)
- Location: Sec. IV, “Mode-coupling matrix and binning” and associated Fig. 3 caption
- Problem: The text says “bins above the map band limit ℓ = 1024 carry noise only”; Fig. 3 relies on the template CEE,b in the SNR definition. If bins beyond 1024 are included in SNRtmpl, CEE,b for those bins must be set to zero (consistent with the simulation truncation), otherwise a small artificial SNR inflation could occur.
- Required fix: Add a sentence clarifying that the EB template uses CEE,b = 0 for bins with ℓ > 1024 (so they contribute noise only), or state explicitly that those bins are masked out in the template fit. This keeps the SNR definition fully aligned with the simulation setup.

P1B-n4
- Class: G (novelty), placement
- Location: Appendix A, “What is NOT included… Bayes factors and information criteria…”
- Problem: The rationale about why Savage–Dickey is inappropriate when the null point is unsampled is correct and important for readers; currently it is mainly in Appendix A and in Sec. V with a long paragraph.
- Required fix: Consider pulling a crisp one-sentence rationale into Sec. V (main text) at first mention: “Because the ΛCDM point lies >4σ into the joint marginal tails and is unsampled, a Savage–Dickey readout is unreliable; robust ln B requires nested sampling or thermodynamic integration.”

Explanation
I focused on fresh cross-checks of arithmetic, figure-caption/body alignment, dimensional/notation clarity, cross-reference precision, and comparability caveats. Most numbers remain internally consistent; the additional items above are clarity, consistency, and small-staleness issues that improve rigor and reproducibility. The two essential issues from the first review (negative-β inconsistency; m/H0 conversion factor) remain the only correctness-critical fixes.