# P2 R57 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R57_P2/02_full_draft.pdf` md5=7df88149 pages=28
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9929 chars)
**Wall time**: 225.8s

---

Referee report (Methodology/statistics-focused) for Physical Review D

Scope of this review
- Focus: statistical methodology, derivation chains, internal arithmetic, dimensional analysis, estimator declarations, and reproducibility.
- I audited every scalar in the abstract against body text or equations, recomputed the quoted significances and Bayes factors from the stated inputs, and checked figure/table captions for consistency with the text.

Overall assessment
This manuscript is an extensive sensitivity recast of published SPHEREx/MegaMapper local-type fNL constraints onto the “matter-bounce” prediction fNL = −35/8. It is explicit that the work is a recast (not a de novo Fisher forecast), and it is unusually careful about template mismatch, systematics budgeting, and the in-in normalization audit.

However, at PRD standards the paper still contains essential reproducibility and methodology gaps that must be corrected before publication. In particular: (i) the Data/Code section contains a placeholder “DOI inserted at submission” (no frozen artifact), (ii) several load-bearing quantitative degradations (e.g., mapping a widened bϕ prior to σ(fNL) → 0.9–1.0) are asserted without a shown Fisher re-evaluation or an explicit computation pointer, (iii) the joint (fNL, nfNL) Fisher result is presented without sufficient methodological detail to be reproducible from the paper alone, and (iv) the specific polynomial P(k1,k2,k3) used for numerical bounce–local overlaps is not written explicitly in the manuscript (only a coefficient vector is given), which hampers a text-only re-derivation check.

Below I list specific findings, with severity, page/section, the issue, and the required fix.

Findings

P2-E1 (ESSENTIAL) – Data/Code DOI placeholder
- Location: Data and Code Availability (p. 24)
- Text: “archived at Zenodo (DOI inserted at submission)”
- Problem: The DOI is a placeholder; no frozen version/hash is provided. PRD requires an immutable archive (DOI) of all analysis artifacts underpinning the numerical results.
- Required fix: Provide a working Zenodo (or equivalent) DOI, the exact Git commit hash of the frozen release, and a short manifest listing the key scripts and outputs used to generate each main quantitative result (e.g., which script produces Table IV numbers, Fig. 2 bars, Table II Bayes factors). Ensure the repository tag matches the cited DOI contents.

P2-E2 (ESSENTIAL) – Explicit specification of the bounce polynomial P
- Location: Sec. II.A, pp. 3–4; footnote 1
- Problem: The manuscript reports the monomial-coefficient vector (2, 7, 3, −12, −69, 19) and describes the six-orbit basis, but it never writes the explicit polynomial P(k1,k2,k3) used for numeric evaluation (with the precise mapping from the coefficient vector to monomials, including the orbit-sum normalization). A reader cannot reconstruct P unambiguously from the text alone.
- Required fix: Print the explicit expression for P(k1,k2,k3) in the paper with the exact normalization and orbit sums used in the code (i.e., P = c1∑i k9
i + c2∑i≠j k7
i k2
j + ... with explicit sums and any prefactors). Include a short table mapping each ci to its orbit and the permutation-count normalization actually applied. This is necessary for full text-level reproducibility.

P2-E3 (ESSENTIAL) – Justification of bϕ prior widening → σ(fNL) replacement
- Location: Sec. IV (p. 10), Sec. VII.B, Table IV (p. 20), Fig. 5
- Problem: The paper replaces σ(fNL)=0.7 by 0.9–1.0 to represent 30–50% bϕ-prior widening, citing Barreira [28] qualitatively. No explicit Fisher re-evaluation or computation pointer is provided to justify the specific replacements 0.9 and 1.0 in the bispectrum-only channel.
- Required fix: Either (a) provide an explicit Fisher-matrix calculation (or a documented surrogate calculation) showing how the SPHEREx bispectrum-only σ(fNL) degrades from 0.7 to ≈0.9–1.0 under 30–50% bϕ prior widening (include assumptions: triangle cuts, redshift bins, noise model), and point to the exact script/output in the released code; or (b) clearly label the 0.9 and 1.0 substitutions as scenario assumptions (not derived) and remove any implication that they result from a calculation. If (b), include a sensitivity table showing significance as a function of σ(fNL) over a small grid (e.g., 0.7, 0.8, 0.9, 1.0) so readers can map their own priors to your significance without assuming your replacements.

P2-E4 (ESSENTIAL) – Methodological details for the (fNL, nfNL) Fisher
- Location: Sec. IX.D (pp. 22–23)
- Problem: The joint SDB Fisher result (σ(nfNL)=0.295, σmarg(fNL)=3.08 [fixed bias], etc.) is new in this paper but lacks the necessary details to be reproduced from the text. Missing: exact tracer specifications (number densities per bin, b1(z), shot noise), k-range and k-binning, window functions, photo-z model, the precise form of the derivative of ∆b(k) with respect to nfNL (i.e., the fiducial pivot and running parameterization), and whether RSD terms and GR terms are included or neglected.
- Required fix: Add a concise methods appendix (or expand Sec. IX.D) with the explicit Fisher equations used, bin definitions, k-cuts, parameter vector, priors, and a table of the per-bin tracer inputs. Cross-reference to the code artifact that reproduces the quoted numbers. Without this, the joint result is not reproducible at PRD standards.

P2-E5 (ESSENTIAL) – SPHEREx-like weighting definition for r
- Location: Sec. III.B (pp. 8–9)
- Problem: The amplitude recovery factor r is reported for “SPHEREx-like” and “LSS/SDB” weightings, but the paper does not provide the explicit form of the weight w used in the overlap integral in each case (beyond qualitative descriptors), nor the k-domain and triangle sampling used for the LSS-weighted computation. This is a load-bearing number for the 5.2–5.5σ headline.
- Required fix: State the explicit weighting formulae used for each case (e.g., wCMB ∝ k2..., wSDB ∝ 1/k2 with specified k-cuts), the triangle sampling domain, and provide a pointer (script + JSON output) where these weightings are defined and used. Include the precise numerical r values for the three main weightings in the body (0.829, 0.830, 0.835, 0.876 are mentioned piecemeal; consolidate them in a small table).

P2-M1 (MAJOR) – Units/convention clarity for M(k,z)
- Location: Sec. III.A, Eq. (4) (p. 7)
- Problem: The standard kernel M(k,z) = 2k^2 T(k) D(z)/(3Ωm H0^2) is given, and “wavenumbers k are quoted in h Mpc−1 throughout”. To avoid unit confusion, one must specify whether H0 is in h km s−1 Mpc−1 and whether c=1 is assumed. Otherwise the dimensional analysis appears mixed (k^2 in (h/Mpc)^2 divided by H0^2 with different implicit units).
- Required fix: Add a one-sentence unit convention (e.g., comoving units with c=1, H0 in h Mpc−1, k in h Mpc−1) or state explicitly that M(k,z) is defined in the dimensionless cosmology-normalized form used in galaxy analyses. This prevents unit ambiguity.

P2-M2 (MAJOR) – Provide an explicit numerical check for the rcos tail bound
- Location: Sec. II (pp. 4–5)
- Problem: The text states “rcos = 0.985 ± 0.007; rcos > 0.97 for all 10,000 samples.” Given the quoted mean and RMS, the tail bound is plausible but not guaranteed by the RMS alone. For transparency, readers need either the minimum rcos observed or a histogram summary.
- Required fix: Report min/max rcos across the 10,000-sample scan (and at least the 5th/95th percentiles). A small inset histogram in a figure or a one-line statistic suffices.

P2-M3 (MAJOR) – Template-overlap reproducibility: squeezed cutoff insensitivity
- Location: Sec. III.B (p. 9)
- Problem: The statement “varying x3,min from 0.001 to 0.200 changes r by < 0.0002” is an unusually strong invariance claim and is an important diagnostic given the dominance of squeezed configurations in local PNG. No numeric table or figure is provided.
- Required fix: Provide the numeric r values at representative x3,min points (e.g., 0.001, 0.01, 0.05, 0.2) for at least one weighting scheme in an appendix table, or link to an artifact with these numbers.

P2-M4 (MAJOR) – Heuristic GR σGR handling in significance tables
- Location: Sec. IV (p. 10), Sec. VII.C, Table III (p. 18), Table IV (p. 20)
- Problem: The additive-in-quadrature GR-degradation model (σeff^2 = σbase^2 + σGR^2) is clearly presented as a scoping choice, which is good. However, the same σGR = 0.5 and 1.0 are subsequently used to produce precise-point significance values in Tables III–IV without an uncertainty bar. For clarity, those lines should be visually designated as scenario outcomes (not forecasts), and an uncertainty or sensitivity to σGR choice should be noted.
- Required fix: In Table IV, label the GR rows as “scenario (assumed σGR = …)” and add a one-line sensitivity bullet: “Significance scales as 1/√(σbase^2+σGR^2); e.g., σGR=0.3 → Xσ.” Alternatively, include an inset plot or a three-point mini-table.

P2-M5 (MAJOR) – Joint (fNL, nfNL): specify pivot and definition of nfNL
- Location: Sec. IX.D (pp. 22–23)
- Problem: The manuscript defines nfNL as d ln|fNL|/d ln k but omits the pivot scale k∗ and the implementation in the Fisher derivatives (e.g., fNL(k) = fNL(k∗)(k/k∗)nfNL). Without this, the reported σ(nfNL) is ambiguous.
- Required fix: State the pivot k∗ used, the parameterization of fNL(k), and whether the covariance is reported at fixed k∗. Include the value of k∗ in the figure or text.

P2-M6 (MAJOR) – Provide an explicit matcher for Planck convention mapping
- Location: Appendix A (pp. 24–26)
- Problem: The normalization audit is well-argued, but the reader would benefit from a compact summary mapping (c, field choice) → (fNL, σ(fNL)) used in the paper, to make it explicit that all quoted σ(fNL) = 0.7 numbers are in the ζ 6/5 convention.
- Required fix: Add a one-line table in Appendix A mapping Φ (c=2) ↔ ζ (6/5) and explicitly stating that the Heinrich et al. σ(fNL) = 0.7 is in the ζ 6/5 convention consistent with the adopted −35/8.

P2-M7 (MAJOR) – Injection–recovery: estimator and noise model details
- Location: Sec. II (p. 5)
- Problem: The 200-realization KSW-type injection–recovery test quotes rmeasured = 0.90 ± 0.01 but does not specify the exact estimator implementation (filters, weighting, flat-sky tiling, ℓ-range) nor the noise power normalization used for the “SPHEREx photometric-z power spectra” diagonal covariance.
- Required fix: Provide a short description of the estimator (filters Φℓ, bispectrum weight), ℓ-range used, and the noise model (per-bin noise power spectra, sky fraction assumed). Reference the exact script that generates the 200 realizations and the output file containing the per-realization recovered amplitudes.

P2-M8 (MAJOR) – Length relative to contribution
- Location: Whole manuscript (28 pages)
- Problem: For a sensitivity recast (not an original forecast), 28 pages is long. Much of Sec. VI (Bayesian grid prose) and Sec. II’s long basis/scan description could be compressed if detailed code artifacts are cited.
- Required fix: Consider reducing by 5–7 pages by moving extended Bayes-factor narrative (derivation repeats) and null-space scanning elaborations to an appendix, retaining in the main text only the final numbers, equations, and key assumptions.

P2-m1 (MINOR) – Arithmetic/consistency checks (passed)
- Location: Multiple
- Recomputations:
  - 5.2–5.5σ headline: 4.375×0.83/0.7 = 5.19; 4.375×0.876/0.7 = 5.48 → consistent with 5.2–5.5.
  - 3.0σ floor: 4.375×0.84/√(0.49+1.00)=3.01 → matches.
  - All-combined 2.6–2.8σ: 4.375×0.84/√(0.81+1.00)=2.73; with 1.00→2.60 → consistent.
  - 16th-percentile r=0.70: 4.375×0.70/0.7 = 4.375σ → “≈4.4σ” consistent.
  - Planck PR4 recast: 5.0/0.876=5.71 → matches σ ≈ 5.7; tension with bounce 4.375/5.71=0.77σ → “0.75σ” acceptable rounding.
  - Bayes factor (delta, W=30, σeff=0.7): 30/(√(2π)0.7)=17.10 → matches.
  - Bayes factor rebooked (delta, σeff=0.833): 14.37 → matches 14.36.
- No action needed; included here as confirmation that most load-bearing numerics are internally consistent.

P2-m2 (MINOR) – Clarify “optimistic vs realistic” labels wherever shown side-by-side
- Location: Fig. 2 caption (p. 11), Table IV (p. 20)
- Problem: The figure juxtaposes different null procedures (naive uncorrected vs template-corrected vs systematic-burdened). You note the first is “shown only for reference,” which is good. For avoidance of doubt, add “not directly comparable null procedure” in the caption for the hatched 6.25σ bar.
- Required fix: Minor caption edit to state explicitly that the hatched 6.25σ is not directly comparable and is not used anywhere.

P2-m3 (MINOR) – Explicitly state k-range for LSS-weighted r and for SDB Fisher
- Location: Sec. III.B (p. 9), Sec. IX.D (p. 22)
- Problem: The k-range used for the triangle grid and SDB Fisher is not printed in the text.
- Required fix: Add the k-range(s) used (e.g., k ∈ [kmin, kmax], with values) and the number of bins/triangles.

P2-m4 (MINOR) – Cite the precise source and year for SPHEREx σ(fNL)
- Location: Abstract (p. 1), Sec. IV (p. 10)
- Problem: You refer to Heinrich et al. [6] σ(fNL) ≈ 0.7. Add the journal reference and DOI if available, or at least the arXiv version/date so readers can verify the number.
- Required fix: Update the bibliography entry for [6] with final publication details if published.

P2-n1 (NIT) – Terminology polish: “commutator doubling”
- Location: Throughout
- Problem: The phrase appears many times. Consider adding a short definition only once and then refer to Eq. (A3) thereafter to reduce repetition.
- Required fix: None strictly required; stylistic suggestion.

P2-n2 (NIT) – Minor rounding harmonization
- Location: Table I (p. 5)
- Problem: Equilateral BNL reported −3.984; exact −255/64 = −3.984375. Consider either reporting exact fraction or rounding to −3.9844 to match the fractional form shown.
- Required fix: Optional.

P2-n3 (NIT) – Code-artifact filenames in body text
- Location: Multiple sections
- Problem: Frequent references to JSON filenames clutter the narrative.
- Required fix: Prefer moving detailed artifact names to a “Reproducibility Roadmap” appendix and keep the main text concise, pointing to that appendix.

Pattern-045 (Abstract-last drift sweep)

I re-read the abstract sentence by sentence and located the corresponding body support.

- “fNL = −35/8 ... in the scalar-only matter-bounce class ... assumptions (a)–(f)” → Backed in Sec. II.C with explicit list.
- “dual-pronged discrimination ... gauge-frame ratio ≈ 290; CFC statement ... not the on-sky observable” → Backed in Sec. I and X; correctly caveated.
- “We forecast tests ... recast ... Heinrich et al. baseline 0.7” → Backed in Sec. IV with repeated clarification that this is a recast.
- “template mismatch ... r ∈ [0.829, 0.876] ... validated via ℓ-space Fisher overlap, 200 injection–recovery realizations, and 10,000-sample null-space scan (shape cosine > 0.97)” → Backed in Secs. II–III.B; minor reproducibility gaps flagged above.
- “bispectrum-only 5.2–5.5σ ... reducing to ∼2.6–5σ after the systematic budget” → Numerically verified; budgeting caveats appear in Sec. VII and Table IV.
- “Bayes factor BF ≈ 9 ... up to 14 ... competitor priors specified” → Backed in Sec. VI and Table II. The rebooking to r≈0.84 is explained; minor preference change shown; OK.
- “SPHEREx null would disfavor ... same ∼2.6–5σ level” → Symmetry of the arithmetic noted in Sec. IX.C; OK.
- “Li et al. −35/16 ... single time-ordering ... not propagated into headline” → Backed in Appendix A and Table V; OK.

Conclusion: The abstract tracks the body with appropriate caveats; no overclaim relative to the body.

Additional checks

- Dimensional analysis: Eq. (1)–(2) produce a dimensionless BNL; verified by degree counting. Eq. (3)–(4) are standard; unit convention needs one clarifying sentence (see P2-M1).
- Figures/tables: Axes labeled, units present where applicable. Fig. 2’s “not directly comparable” bar should be explicitly labeled as such (P2-m2).
- Bibliography: Spot-checked key entries; years and arXiv IDs look consistent. Please add final journal info where available (e.g., [6]).

## Summary recommendation
MAJOR REVISIONS

The manuscript is careful and, in many places, exemplary about statistical caveats, but it lacks essential reproducibility items and some load-bearing methodological details. Before PRD publication, the authors must: (i) supply a frozen DOI and manifest for the analysis code, (ii) print the explicit bounce polynomial used, (iii) justify (or clearly reframe as assumptions) the σ(fNL) replacements used for widened bϕ priors, (iv) fully specify the (fNL, nfNL) Fisher setup (pivot, inputs, k-range), and (v) provide explicit definitions for the weightings used to compute r. Addressing these items will make the work reproducible at PRD standards and will remove the remaining methodological ambiguities.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW ADDITIONAL FINDINGS (second-pass audit)

P2-E6 (ESSENTIAL) – Ambiguity/possible typo in Appendix A symmetry factor
- Location: Appendix A.1, Eq. (A7)
- Issue: The full bispectrum is written with a factor 1/Sv multiplying each vertex integral, with Sv defined so that Sζẋζ2 = 2 (identical legs) and Sv = 1 otherwise. In many standard in-in derivations one multiplies by a symmetry factor rather than divides, or one absorbs it inside the vertex normalization. As written, 1/Sv would downweight the ζẋζ2 vertex by 1/2, which could be a sign/normalization slip.
- Required fix: Explicitly justify the 1/Sv factor with a short derivation (or correct to Sv if that was intended). Given the paper’s emphasis on a factor-of-two audit, this potential 1/2 on one vertex needs to be beyond any doubt.

P2-M9 (MAJOR) – Central value of r vs. the quoted “noise-weighted” entries
- Location: Sec. III.B (pp. 8–9), Eq. (6)
- Issue: The text sets a “noise-weighted” central value r = 0.84 ± 0.02. The three LSS/SPHEREx-weighted numbers listed explicitly are 0.829 (SDB), 0.830 (SPHEREx-like), and 0.835 (flat), with the signal-only CMB-Fisher 0.876 treated separately. The average of the three LSS-like values is ≈ 0.831, and their spread is ±0.003. It is not obvious how these support a central 0.84 ± 0.02 without additional weightings.
- Required fix: Either (a) show the full set of the “10 physically motivated weighting schemes” and their values that actually yield the 0.84 ± 0.02 summary; or (b) re-center the quoted “noise-weighted” central value to ≈ 0.83 ± 0.01 unless there is a documented reason to weight certain schemes more heavily. Consolidate the values in a small table for transparency.

P2-M10 (MAJOR) – Figure 5 label vs. body claim for the SPHEREx reference level
- Location: Fig. 5 (right panel) caption/legend vs. Sec. IV/III.B
- Issue: The figure uses a fixed “SPHEREx bispectrum (5.2 template-corrected)” horizontal reference, but the body repeatedly states a 5.2–5.5σ optimistic template-corrected range (r = 0.84–0.876). It is unclear whether the plot intentionally fixes to the 5.2σ endpoint or mixes endpoints.
- Required fix: State explicitly in the caption that the reference line is the noise-weighted endpoint (5.2σ), not the 5.2–5.5σ band, or plot a shaded band to reflect 5.2–5.5σ to match the body text.

P2-M11 (MAJOR) – ℓ-space Fisher-overlap methodology insufficiently specified
- Location: Sec. III.B (p. 9, “ℓ-space Fisher overlap using fiducial Cℓ with a Planck noise model”)
- Issue: The overlap r = 0.878 ± 0.012 is quoted, but the ℓ-range, beam, sky fraction/mask treatment, noise curves, and exact inner product (weight) used for the ℓ-space Fisher overlap are not specified. This is separate from the injection–recovery (already requested in P2-M7) and is needed to reproduce the ℓ-space cross-check.
- Required fix: Provide the ℓmin, ℓmax, beam/noise model used (e.g., Planck PR4 TT/TE/EE noise curves), fsky or mask handling, and the precise ℓ-space weight in the inner product. Point to the exact script and JSON/NPY output that yields r = 0.878 ± 0.012.

P2-M12 (MAJOR) – “CMB-Fisher weighting” nomenclature and definition
- Location: Sec. III.B (pp. 8–9)
- Issue: The paper uses “CMB Fisher weighting” and w ∝ k^2 as shorthand for a signal-only weighting that upweights squeezed configurations. However, an actual CMB bispectrum Fisher weight depends on Cℓ noise/beam and triangle-dependent shape weights, not simply ∝ k^2. The label may mislead readers into thinking a full CMB Fisher kernel was used.
- Required fix: Either rename this to “signal-only k^2 weighting” (and keep the Planck ℓ-space result as a separate cross-check), or provide an explicit mapping from the k^2 proxy to a true CMB Fisher weight and justify its use as a surrogate.

P2-M13 (MAJOR) – Realistic vs. post-budget range mixing
- Location: Abstract; Sec. IV (p. 10); Table IV (p. 20)
- Issue: The abstract and body sometimes use “realistic ∼ 2.6–5σ after the systematic budget.” In Table IV, once GR and bϕ degradations are included, the upper end does not reach 5σ; 5σ corresponds to the optimistic/no-GR case. The phrase “after the systematic budget” suggests all degradations are included, which would put the upper bound below ≈ 4.3σ (σGR=0.5 case) for the baseline.
- Required fix: Disentangle the labels: reserve “optimistic” for the 5.2–5.5σ template-corrected/no-GR case and reserve “post-systematic-budget” for the ranges that include GR and bϕ (e.g., ≈ 2.6–4.3σ depending on σGR and bϕ). Use consistent terminology in all places where these are juxtaposed.

P2-M14 (MAJOR) – MegaMapper “single-tracer” bar lacks numerical definition
- Location: Fig. 2 caption and Sec. V
- Issue: The MegaMapper panel shows a “single-tracer” bar but the text does not specify what σ(fNL) value, target selection, or assumptions define this bar. Without numbers, readers cannot assess or reproduce it.
- Required fix: State the σ(fNL) used for the single-tracer bar and the underlying assumptions (number density, area, redshift range, kmin, bϕ prior). If it is illustrative only, label it as such and give the numeric value.

P2-M15 (MAJOR) – Mixture of numerator and denominator systematics in significance accounting
- Location: Abstract; Sec. IV; Table IV
- Issue: The paper sometimes treats amplitude-side systematics (e.g., ϵ-correction on fNL) and denominator-side systematics (σGR, bϕ) within one “combined in quadrature” language. Table IV partly clarifies this (distributional vs. cumulative), but the abstract and some body text still read as if everything is lumped together homogeneously.
- Required fix: Add a one-paragraph accounting rule up front in Sec. IV clarifying which effects modify the numerator (|fNL| → |fNL| ± δ), which modify the denominator (σeff), and how each is propagated (linear vs. quadrature). Ensure every time a “post-budget” significance is quoted, it corresponds to a consistent application of that rule.

P2-M16 (MAJOR) – Column heading ambiguity in Table III
- Location: Table III (p. 18)
- Issue: The “BF vs. Tuned” column does not, in the column header, specify that the tuned multifield competitor prior is the narrow [−5, +5]; the footnote and text do say this, but the header itself is ambiguous.
- Required fix: Amend the column header to “BF vs. Tuned ([-5,+5])” to avoid misinterpretation.

P2-M17 (MAJOR) – Claim of 10–20% σ(fNL) improvement from anomaly-selected tracers is unsupported
- Location: Sec. IV (p. 11)
- Issue: The manuscript claims a preliminary 10–20% σ(fNL) improvement from anomaly-selected tracers (DESI–SDSS cross-matched), but provides no inputs (number densities, bias, redshift distribution, shot noise) or a pointer to a computation.
- Required fix: Either provide a brief Fisher estimate with the assumed inputs and a code pointer, or clearly mark this as speculative (“order-of-magnitude, not used in any forecast”) and move it to a brief outlook remark.

P2-m5 (MINOR) – Typographical glitch in squeezed-limit description
- Location: Sec. II.A (p. 3), around Eq. (2)
- Issue: The line “k∑1 ≪ k is the squeezed (long-wavelength) mode” appears to be a typesetting error; it likely should read “k1 ≪ k”.
- Required fix: Correct the typo to avoid confusion.

P2-m6 (MINOR) – Figure 4 axis and text alignment
- Location: Fig. 4 and text in Sec. VII.A
- Issue: The left panel is labeled “σ(fNL) vs. minimum accessible wavenumber” with kmin in h/Mpc (good). The caption states “SPHEREx bispectrum (σ = 0.7, dotted) is less sensitive to the ultra-large-scale fragility,” implying a constant dotted line. Make sure the legend or caption explicitly states that the dotted line is a constant σ = 0.7 reference (not derived from SDB), to avoid confusion with the SDB curves.
- Required fix: Clarify in the caption that the dotted line is a constant reference (the bispectrum-only baseline) and not from the kmin scan.

P2-m7 (MINOR) – Planck PR4 recast: state ℓ-range and component set
- Location: Sec. VIII.A (p. 19)
- Issue: You recast the Planck PR4/NPIPE number to the bounce template using rCMB. For reproducibility, specify whether this uses TT-only, TT+TE+EE, and the ℓ-range (or cite the exact PR4 analysis choice used for the σ = 5.0 number).
- Required fix: Add one sentence clarifying the component set/ℓ-range (or add the exact citation string of [32] with those details).

P2-m8 (MINOR) – Novelty phrasing
- Location: Sec. III.B (p. 9): “no prior quantification of this overlap exists for the matter-bounce bispectrum (2009–2024)”
- Issue: This is a novelty-adjacent claim without a structured literature comparison. While it may be true, PRD typically expects such statements either to be removed or supported by a brief survey.
- Required fix: Soften to “we are not aware of a prior quantification for the matter-bounce case” or provide a short supporting citation survey in a footnote.

P2-m9 (MINOR) – Consistent table–text linkage for r values
- Location: Sec. III.B; Eq. (6)
- Issue: The paper cites several r values (0.829, 0.830, 0.835, 0.876) in prose. Consolidating these into a small table (with weight definitions) would prevent hunting across paragraphs and reduce confusion with the 0.84 ± 0.02 summary.
- Required fix: Add a compact table listing: weighting name, mathematical weight, k-domain, and the resulting r.

Explanation
This second-pass focused on cross-checking arithmetic consistency, figure–caption alignment, equation normalization, and subtle comparability labeling. Most numerics in the first review remain consistent; the new issues above center on (i) a potential normalization typo in Appendix A, (ii) the precise centering of the noise-weighted overlap r, (iii) labeling and methodological specificity for ℓ-space and MegaMapper displays, and (iv) clearer accounting/labeling of “realistic vs. optimistic” significance ranges. Addressing these will further tighten methodological rigor and reproducibility.