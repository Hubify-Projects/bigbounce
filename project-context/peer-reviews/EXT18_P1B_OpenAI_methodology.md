# P1B EXT18 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=5a3c98e9 pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5434 chars)
**Wall time**: 438.7s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

I read the full manuscript carefully, including all figures, tables, equations, footnotes, and appendices. Below I list all methodological and numerical issues I found, classified by severity. For each, I quote the offending text, give the page/section, explain the problem, and state the required fix.

ESSENTIAL

P1B-E1 (Sec. VI, “ALP dark-energy fraction Ωa: definition and computation”; p. 13)
Problem: Incorrect ρcrit,0 value and an algebraic error in the small-angle approximation for Ωa.
Quotes:
- “ρcrit,0 = 3H0^2 MPl^2 ≈ 8.1 × 10−11 eV^4” 
- “For fa = MPl and small θi this gives Ωa ≈ m_a^2 θ_i^2 /(2 H0^2 (1 + zosc)^3) …”
Issues:
- With MPl the reduced Planck mass (as defined earlier: MPl = (8πG)−1/2 ≈ 2.44 × 10^18 GeV) and H0 = 67.68 km s−1 Mpc−1 = 1.444×10−33 eV, ρcrit,0 = 3 H0^2 MPl^2 ≈ 3.7–4.0 × 10−11 eV^4, not 8.1 × 10−11 eV^4. The quoted value is off by a factor ~2.
- The stated small-angle approximation omits the factor of 3 from ρcrit,0. Starting from V ≈ (1/2) m_a^2 f_a^2 θ_i^2 and ρcrit,0 = 3H0^2 MPl^2, for fa = MPl one obtains Ωa ≈ m_a^2 θ_i^2 / [6 H0^2 (1 + zosc)^3], not 1/2.
Required fix:
- Correct ρcrit,0 to ≈ 3.7–4.0 × 10−11 eV^4 (provide the exact value used in code with the adopted H0).
- Replace the small-angle expression with Ωa ≈ m_a^2 θ_i^2 / [6 H0^2 (1 + zosc)^3] for fa = MPl.
- State explicitly which numerical value and formula your code uses to compute Ωa at each MCMC step. If the erroneous numbers were used in code, all reported Ωa subset fractions (e.g., 44% for Ωa < 0.1; 13% for Ωa < 0.01 in Table IV) must be recomputed and updated accordingly.

P1B-E2 (Sec. V.C “w0wa cross-check…”; p. 10 and Conclusions p. 15)
Problem: Inconsistent Planck low-ℓ/lensing pairing for the w0wa chain with no demonstrated robustness; strong posterior-tail “σ” distances reported using that chain.
Quotes:
- “The iter2 chain uses planck 2018 lensing.native in place of planck 2018 lensing.clik … a dedicated release-pairing swap test … has not been performed and is left to a post-submission follow-up.”
- The main text and Table II then quote marginalized “tail-distances” of +4.3σ (w0) and −3.6σ (wa).
Issue: You correctly check release-pairing robustness for ΔNeff (c15 rerun), but you do not for the w0wa chain whose headline tail distances are emphasized in Sec. III and Table II. Since the low-ℓ EE and lensing pairings can shift τ and late-time parameters that correlate with w0, wa, the reported tail-distances require the same release-pairing robustness you performed for ΔNeff.
Required fix:
- Rerun the w0wa chain with PR4-consistent low-ℓ EE and lensing (e.g., planck 2020 lollipop.lowlE and planckpr4lensing), or demonstrate via a controlled swap test that the quoted w0, wa posteriors (and especially the “+4.3σ” and “−3.6σ” tail distances) are stable to this choice. If not rerun, remove/soften all tail-distance claims and clearly label the current values as pairing-dependent diagnostics only.

MAJOR

P1B-M1 (Sec. IV, pp. 7–9; Figs. 3; robustness battery)
Problem: Primary estimator choice (unweighted χ2 template fit) introduces a large, estimator-induced multiplicative bias; the “observed pipeline bias floor” is thus estimator-limited, not method-limited.
Quotes:
- “the fit is unweighted — all bins carry equal weight …”
- “replacing the unweighted χ2 template fit with an inverse-variance-weighted fit recovers β̂ = 0.264° (bias −0.006°), removing ≈80% of the bias …”
- “we carry the worst case |Δβ̂| = 0.040° forward as the observed NaMaster pipeline bias.”
Issue: As a methods paper, the baseline estimator should be the statistically efficient, inverse-variance-weighted fit (or equivalently the full bandpower-covariance MLE). Carrying forward a 0.040° “bias floor” that is largely an artifact of your choice to use an unweighted fit is misleading about the method’s intrinsic accuracy. Matching a historical public script is not sufficient justification.
Required fix:
- Make the inverse-variance-weighted estimator the primary baseline for the pipeline-validation results (report β̂ and bias for that case), and relegate the unweighted fit to a legacy cross-check; or, if you insist on unweighted as the baseline, relabel the 0.040° as an estimator-choice bias, not a method bias floor, and present both results side-by-side anywhere a “bias floor” is quoted. State clearly that the method’s intrinsic bias under standard weighting is ≤ 0.006° in your tests.

P1B-M2 (Sec. III p. 5; Table I caption p. 19)
Problem: Inconsistent S8-tension figures (2.5σ vs 2.6σ).
Quotes:
- Text: “sits 2.5σ above the DES-Y3 weak-lensing value S8 = 0.776 ± 0.017”
- Table I caption: “The Planck+BAO+SN marginal sits in 2.6σ two-Gaussian tension with DES-Y3”
Check: |0.827−0.776|/sqrt(0.010^2+0.017^2) = 0.051/0.0197 = 2.59σ ≈ 2.6σ.
Required fix: Harmonize the quoted number to 2.6σ everywhere (or quote to one decimal, 2.6σ) and ensure consistency across the manuscript.

P1B-M3 (Sec. III pp. 3–5; Sec. V.A p. 9; Table I p. 19)
Problem: ΔNeff constraints tied to BBN-consistent YHe only; no free-YHe control. 
Quote: “YHe follows the CAMB BBN-consistent default … no free-YHe control run was performed … the default BBN-consistent track is the standard choice for this type of proxy analysis.”
Issue: The ΔNeff limit can shift under a free-YHe analysis versus BBN-consistency. While the BBN-consistent choice is common, a quick free-YHe control (or a literature-based bound on the expected shift for this data combination) should be provided for robustness.
Required fix: Add a short free-YHe control run for Planck+BAO+SN (enough for posterior means/σ) and report the ΔNeff shift (or, at minimum, cite a recent robust analysis demonstrating the expected shift for this likelihood stack and justify that it is negligible at your precision).

MINOR

P1B-m1 (Sec. V.A/Table III; pp. 9, 20)
Problem: Inconsistent naming of Planck lensing likelihood (“.clik” vs “native”) without clarification of the practical difference.
Required fix: Standardize the naming and add a short note clarifying the distinction (and that your results are insensitive to this choice where applicable). If differences exist, quantify them.

P1B-m2 (Sec. IV, mask definitions; p. 8; Fig. 3 caption p. 7)
Problem: Slightly different declination cuts stated for ACT-like masks (e.g., dec ∈ [−65°, +25°] vs [−60°, +25°]) across sections.
Required fix: Harmonize the exact mask definitions in text and figure captions, or clearly label them as distinct masks used in different tests.

P1B-m3 (Appendix A, pp. 15–16)
Problem: Process/internal-artifact details (“parameter_summary_CORRECTED.json”, column-permutation bug) occupy substantial space in the main appendix.
Required fix: Condense this into a brief note and move operational details to the repository README or a short Supplementary Material, keeping the paper focused.

P1B-m4 (Sec. IV, Eq. (1), pp. 7–8)
Problem: The estimator is presented as an unweighted least-squares without an explicit uncertainty model for β̂. You later report per-realization σβ from MC, but the mapping from χ2 grid to β̂ uncertainty is not described.
Required fix: Add a sentence on how β̂ uncertainties are estimated in your MC (e.g., from per-realization scatter across N=500, not from curvature of χ2), so the reader can follow the logic unambiguously.

P1B-m5 (Sec. IV, “Canonical estimator choice”, p. 9)
Problem: The statement “adopted to match the estimator configuration used in the public NaMaster driver scripts … (e.g., [5])” needs a precise pointer.
Required fix: Cite a specific public script/release tag/line number in the cited repository that demonstrates this estimator choice, or soften the claim to “consistent with.”

P1B-m6 (Sec. VI, Eq. (4), p. 11)
Problem: You mention normalization conventions “αEM/(2π) appears in some Lagrangian normalizations.” Good to note, but add a one-line cross-check that your convention reproduces the β = (gaγ/2) Δϕ identity (you already state it, but a brief sentence tying both forms will help standalone readers).

NIT

P1B-n1 (Throughout)
Minor phrasing/grammar and occasional long hyphenations from PDF extraction (e.g., line breaks within words). A careful language pass will improve readability.

P1B-n2 (Length)
At 21 pages, the paper is long for what is fundamentally a verification companion. Consider trimming non-essential process narrative (Appendix A) and keeping core methodology/results. A target of ~15–17 pages would be appropriate without loss of substance.

Audit of abstract and conclusions vs. body (pattern-045): All abstract scalars and claims were traced to the body. The ΔNeff and H0 values match Table I. The pipeline-recovery biases (−0.032°, −0.040°) are consistent with Fig. 3 and Sec. IV. The SH0ES tension (~3.6σ) recomputes to 3.61σ from the quoted numbers. The ALP β ≈ 0.28° computation is numerically consistent. The “spectator-status caveat” aligns with Sec. VI. However, the Ωa subsection contains the ESSENTIAL error described in P1B-E1 and must be corrected.

Additional quantitative checks:
- Inverse-variance combination of Planck NPIPE and ACT DR6 birefringence: 0.241° ± 0.061° → 3.93σ (agrees with Eq. (5) “3.9σ upper bound”).
- Phantom crossing redshift from w0, wa: z× ≈ 0.39 (recomputed 0.392).
- Multiplicative under-recovery: 0.238/0.270 ≈ 0.882; 0.302/0.342 ≈ 0.883 (consistent).
- Per-realization σβ scaling with fsky: reported 0.029° and 0.033° match the expected √(0.32/fsky) scaling from 0.046° at fsky=0.32.

Bibliography spot checks:
- Eskilt & Komatsu (PRD 106, 063503, 2022; arXiv:2205.13962) matches text.
- Planck PR4/NPIPE birefringence (Phys. Rev. Lett. 128, 091302 (2022), arXiv:2201.07682) matches text.
- DESI DR2 arXiv ID and year are plausible given the manuscript date.

Standalone-reader test: The paper is largely self-contained regarding methods and numerical claims. References to Paper I(a) are contextual and not load-bearing for the reported analyses. After fixing P1B-E1 and P1B-E2, the manuscript will meet PRD methodological rigor on internal consistency.

Effect sizes and significance hygiene: The manuscript generally keeps distinct significances separate (pipeline SNR vs sky σ) and labels them as not directly comparable. The LiteBIRD “~9σ” extrapolation is framed as a forecast under assumptions and not a model discriminator. Good.

## Summary recommendation

MAJOR REVISIONS

The ALP energy-density subsection contains an essential numerical/algebraic error (ρcrit,0 value and a missing factor of 3 in the small-angle Ωa expression) that potentially impacts Table IV subset fractions; this must be corrected and the code’s implementation clarified. In addition, the strong w0–wa tail-distance claims require a release-pairing robustness test akin to what you already did for ΔNeff. Finally, for the NaMaster pipeline validation, either adopt the inverse-variance-weighted estimator as the primary baseline or clearly label the 0.040° as an estimator-choice bias and present both un/weighted results wherever a “bias floor” is discussed. Address the remaining minor items and harmonize the S8-tension numbers. Once these are fixed, the paper will be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

P1B-M4 (Sec. VI, “Spectator-subset readout” H0 marginalization note; p. 13)
Problem: Underestimation of H0 sensitivity of Ωa.
Quote: “Marginalizing H0 over the Planck 1σ interval shifts Ωa by ≲ 1% (Ωa ∝ H0−2) …”
Issue: If Ωa ∝ H0−2, the fractional shift from marginalizing over H0 = 67.68 ± 1.06 km s−1 Mpc−1 is ≈ 2×(1.06/67.68) ≈ 3.1%, not “≲ 1%.” While there is a secondary H(z) dependence through zosc, it cannot reduce the dominant explicit H0−2 scaling to below ~1% over a 1.6% H0 range without demonstration.
Required fix:
- Correct the stated sensitivity (≈3%) or provide a quantitative check (including the zosc dependence) showing that the net variation is ≤1% for the parameter region contributing to Table IV. If the shift is ≈3%, state it and confirm it does not affect any subset fraction (e.g., Ωa < 0.01, Ωa < 0.1) at the quoted precision.

P1B-m7 (Table IV and surrounding text; pp. 13, 21)
Problem: Ambiguous labeling of m/H0 column with “(Caγ = 8)” in a readout sourced from the continuous-prior chain.
Quotes:
- Table IV header: “m/H0 (Caγ = 8) …”
- Text: “Spectator-subset readout (same chain, no additional sampling) … the continuous-prior c5 chain …”
Issue: The subsets reported in Table IV are described as readouts from the continuous-prior (Caγ free) chain, but the column header tags m/H0 with “(Caγ = 8),” implying the values come from the fixed-coupling run. This is confusing and could be misread as mixing runs.
Required fix:
- Clarify the provenance: either (a) confirm the m/H0 statistics in Table IV are from the Caγ-free c5 continuous chain and remove “(Caγ = 8)” from the header, or (b) if those rows actually come from the Caγ=8 run, relabel them accordingly and separate them from the continuous-prior readouts.

P1B-m8 (Sec. VI, Ωa computation; pp. 12–13)
Problem: Missing specification of how Eq. (9) is handled when zosc ≤ 0 (field not yet oscillating).
Quote: “For ALP masses in the scan prior … the onset redshift ranges from zosc ≲ 0 … Energy density today … ρa(z) = ρa(zosc) [(1+z)/(1+zosc)]^3, z ≪ zosc.”
Issue: Eq. (8)/(9) apply only once oscillations start. The text notes zosc ≲ 0 can occur but does not state the rule used for such cases (e.g., set (1+zosc)^3 → 1, or compute ρa today directly from the EOM without the matter-like redshifting approximation).
Required fix:
- Add an explicit branch description for zosc ≤ 0: state how Ωa is computed in that regime (e.g., full EOM integration to z=0 or V(ϕ) evaluated today), and confirm that the implementation matches the stated rule.

P1B-m9 (Sec. IV, Noise convention; p. 8)
Problem: Potential ambiguity in the definition of ΔP and σpix for Q/U.
Quote: “… draws independent Gaussian realizations with the same σpix for Q and U (no √2 factor) …”
Issue: Different CMB-polarization conventions define ΔP either per Stokes (Q or U) or for P ≡ √(Q^2+U^2), which changes whether a √2 enters σpix for Q and U. You choose “no √2” (per-Stokes convention) but do not cite a source for the ACT-like 10 μK·arcmin number under this convention.
Required fix:
- Add a short citation or sentence explicitly stating that ΔP = 10 μK·arcmin is per Stokes (Q or U) in the ACT convention you emulate, so σpix = ΔP/√Ωpix applies to both Q and U without a √2.

P1B-m10 (Sec. IV, bins above the map band limit; pp. 7–8)
Problem: Explain explicitly why including ℓ-bins above the map’s band limit does not affect β̂.
Quote: “bins above the map band limit ℓ = 1024 carry zero template weight … the 20-bin sum is effectively restricted …”
Issue: With CEE,tmpl,b = 0 above ℓ=1024, the χ2 sum still contains additive, β-independent (CEB,decoupled,b)^2 terms from noise-only bins. The minimizer for β is unchanged, but this rationale is implicit.
Required fix:
- Add one sentence noting that the high-ℓ noise-only bins contribute a constant offset to χ2(β), so the β̂ that minimizes χ2 is unchanged; the check “Restricting … to ℓ ≤ 1024 changes nothing” empirically confirms this.

P1B-m11 (Sec. VI, equation context; pp. 11–12)
Problem: Small clarity gap in tying conventions in Eq. (4) to the β relation.
Quote: You already state “gaγ = Caγ αEM/(2π fa) and β = (gaγ/2) Δϕ.”
Issue: For a standalone reader, it helps to explicitly remark that substituting gaγ in β = (gaγ/2)Δϕ yields β = [αEM/(4π)] Caγ (Δϕ/fa), making clear why αEM/(4π) appears (this closes the loop between the two normalizations).
Required fix:
- Add a one-line algebraic substitution (or brief parenthetical) connecting the two forms to make the normalization fully explicit in-text.

P1B-m12 (Sec. IV, figure-mask text; pp. 7–8, Fig. 3)
Problem: Minor unit/extent consistency between text and caption when describing the sky-fraction sweep masks.
Issue: The text and caption generally agree but a brief reminder in the caption that apodization is always 2° FWHM for the sweep (as in the body) would reduce ambiguity.
Required fix:
- Add “(2° FWHM apodization in all cases)” in the Fig. 3(b) caption for completeness.

Explanation
The items above were not covered in my initial review. The most material is P1B-M4: the stated ≤1% sensitivity of Ωa to H0 is inconsistent with the explicit Ωa ∝ H0−2 dependence at the quoted Planck precision and should be corrected or justified with a quantitative check including zosc(H0). The remaining points are clarity/consistency issues that will help readers reproduce and interpret the results without ambiguity.