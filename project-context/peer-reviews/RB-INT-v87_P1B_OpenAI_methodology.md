# P1B RB-INT-v87 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=ce73d67c pages=24
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7106 chars)
**Wall time**: 301.0s

---

Referee report on “Technical Reproducibility and Consistency-Check Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Overall scope and fit for PRD
- The manuscript explicitly frames itself as a reproducibility/consistency-check companion, not as an independent test of the ECH spin-torsion sector. That framing is appropriate. However, PRD requires high methodological rigor and archival stability for any quantitative claims. Several issues below must be addressed before the paper can be considered.

Key strengths
- Clear separation of sky-measurement significance vs. Monte Carlo pipeline-recovery SNR.
- Extensive scoping statements limiting the interpretation of each numerical result.
- Many internal cross-checks and transparent disclosure of limitations.

That said, there are a number of essential fixes required for correctness, archival stability, and presentation at PRD standards.

Findings

ESSENTIAL

P1B-E1
- Location: Abstract (p.1), Sec. VI main text (pp.11–15)
- Issue: Misstated “25× fine-tuning relative to the natural cos θi-flat prior midpoint.” In the abstract: “constitutes a ∼25-fold fine-tuning of the misalignment initial condition relative to the natural cos θi-flat prior midpoint.” In the main text, the quantitative discussion consistently compares θi ≃ 0.1 to an ad-hoc midpoint θi ≃ 0.5 (a factor 5 in angle and 25 in energy density), and later contrasts a flat-θi prior to a flat-in-cosθi prior. The “cos θi-flat prior midpoint” is θ = π/2 ≈ 1.57, not 0.5. A 25× energy-density reduction is the ratio when moving from θi = 0.5 to 0.1, not from π/2 to 0.1 (which would imply ≳200× in ρa). As written, the abstract’s reference point is incorrect and inconsistent with the body text.
- Required fix: Correct the abstract language to match the body’s quantitative basis. For example: “...a ∼25-fold reduction in ALP energy density relative to a flat-θi midpoint θi ≃ 0.5 (i.e., θi ≃ 0.1), while a flat-in-cosθ prior would imply even stronger tuning relative to its midpoint θi = π/2.” Ensure the same reference point and factor are used consistently everywhere the 25× figure appears (abstract and Sec. VI).

P1B-E2
- Location: Data and Code Availability (p.16), Appendix B (pp.21–22)
- Issue: Archival stability. The paper relies on GitHub and HuggingFace with “DOI assignment is pending,” and cites a moving branch/commit (“in-tex v1B.0.87”, commit b22f8cc9). PRD requires final, citable, immutable archives of data and code that reproduce the results at acceptance time. “Pending” DOIs and branch commits that may change do not meet PRD’s archival standards.
- Required fix: Before acceptance, deposit all frozen chains, analysis scripts, and MC artifacts used to produce the Tables and Figures in immutable archives with minted DOIs (e.g., Zenodo or similar), and update the manuscript with those DOIs. Remove ephemeral commit/branch guidance from the paper body; keep such details in an online README. Ensure the archived materials are exactly sufficient to reproduce all table and figure numbers without relying on mutable external resources.

P1B-E3
- Location: Sec. IV (pp.6–10), Conclusions (pp.15–16)
- Issue: Potential confusion between pipeline “bias” and instrument/systematic “bias.” The text is careful in many places, but several phrases can still be misread as a real-sky systematic bound (e.g., “carry the worst-case |bias| = 0.040° forward as the observed NaMaster pipeline bias (deconvolution-algebra bias on foreground-free skies; not a real-sky bias bound)”). The word “observed” and “systematic floor” can be misconstrued as a claimed bound on observational systematics.
- Required fix: In all places where the 0.040° figure is referenced (Sec. IV, Conclusions), explicitly prepend “synthetic-sky pipeline-recovery bias” and remove “systematic floor.” Add a boxed or bolded sentence in Sec. IV clarifying: “This 0.040° applies only to our unweighted χ2 estimator on synthetic, foreground-free skies and should not be used as a bound on sky-measurement systematics.”

P1B-E4
- Location: Appendix A (pp.18–20), main text references to Appendix A (pp.10–11, 15–16)
- Issue: Overlap-uncorrected supernova product likelihood (DES-SN5YR × Pantheon+). The authors have done a good job caveating this. However, PRD requires that any posterior summaries not suitable for quantitative inference be unambiguously walled-off. A naïve reader could still construe the reported w0, wa numbers as meaningful constraints.
- Required fix: Add a clear visual or textual “Do not use for inference” banner at the start of Appendix A and a one-sentence warning in the main text where iter2 is first mentioned: “All w0wa results in Appendix A are not suitable for quantitative inference and are provided for diagnostic purposes only.” Suppress all quantitative sigma/tail language in Appendix A (retain means only) or move it to ancillary files. Alternatively, produce the overlap-controlled control chains or remove Appendix A from the main paper and provide as ancillary material.

P1B-E5
- Location: Data and Code Availability (p.16), Appendix B (p.21)
- Issue: Use of a corrected artifact “parameter_summary_CORRECTED.json” and warning about a prior “off-by-one column-index bug.” As it stands, the paper requires the reader to trust that the correction is correct, while the buggy file still exists in the same repo.
- Required fix: Deposit and cite only the corrected artifact in the immutable archive (see E2). Remove references to the buggy file name from the paper body; keep the bug log in a repository changelog only. Add a one-sentence statement in the paper that all reported numbers in Tables I/IV were recomputed from the corrected artifacts deposited under DOI XYZ.

MAJOR

P1B-M1
- Location: Sec. VI (pp.11–15), Appendix D (p.22–23)
- Issue: Fixed fa = MPl assumption is load-bearing for both β and Ωa. The coupling requirement and the spectator fraction depend strongly on fa. The manuscript motivates fa ∼ MPl heuristically from “Holst-sector pseudoscalar structure” but does not quantify how results scale with fa.
- Required fix: Add a brief scaling subsection in Sec. VI quantifying how β and Ωa scale with fa (e.g., β ∝ Caγ Δϕ/fa with Δϕ/fa depending weakly on fa through dynamics; Ωa ∝ (fa/MPl)^2), and provide a one-paragraph discussion of how the coupling requirement Caγ and the spectator fraction shift if fa is varied by, say, a factor of 3 up or down. Alternatively, include one small figure or table illustrating the dependence.

P1B-M2
- Location: Sec. IV (p.8–10), Fig. 3 caption (p.7)
- Issue: Statement that the bias is “attributed ... to the unweighted fit as the dominant driver” is supported by one robustness check, but the weight definition is only sketched in prose. For reproducibility and clarity, the precise weighting scheme for the “inverse-variance weighted fit” should be stated.
- Required fix: Add the explicit expression for the weighted χ2(β), specifying σb (the per-bin variance) and how it is estimated from the 500-MC ensemble. State whether you use diagonal-only errors (as implied) and confirm that including off-diagonal bin covariances did not change the result (or state that this was not tested).

P1B-M3
- Location: Sec. III (pp.3–6), Table I (p.5)
- Issue: One-sided ΔNeff bounds are quoted (0.31 and 0.40) based on truncation and renormalization. That is correct statistically, but the exact definition and the dependence on binning/smoothing of the posterior should be given more prominently in the main text where the bounds first appear.
- Required fix: Move the precise construction currently embedded in a paragraph (discard negative-weighted samples, renormalize, read 95th percentile of the truncated CDF) into a bulleted “Definition of one-sided bound” immediately after Table I or in Sec. III, and provide the resulting numeric with two significant figures and the numerical uncertainty due to finite chain length (e.g., via bootstrap or by quoting the binning resolution used).

P1B-M4
- Location: Sec. IV (p.8–10)
- Issue: The fit includes bandpowers up to ℓ = 1536 even though the map band limit is ℓmax = 1024. You note that bins above ℓ = 1024 carry zero template weight and thus do not change β. That is correct, but the practical effect (that these bins add a β-independent constant to χ2) should be made explicit to avoid confusion.
- Required fix: Add a one-sentence clarification: “Because CEE,tmpl
b = 0 for ℓ > 1024, the sum over these bins contributes a β-independent constant to χ2(β), and thus does not affect the argmin; we verified this explicitly by restricting to ℓ ≤ 1024, which yields identical βˆ.”

P1B-M5
- Location: Throughout (e.g., pp.7–9), Conclusions (p.15)
- Issue: Use of internal pipeline jargon and run-paths in the main text (“pod,” full pathnames, seed_base=42, etc.) is non-standard for PRD and distracts from the science.
- Required fix: Move all run-paths and pipeline operational details to a short Methods/Appendix paragraph or to the online repository README. In the paper, replace file paths with short artifact identifiers (which should resolve via DOIs post-fix E2).

P1B-M6
- Location: Acknowledgments (p.18)
- Issue: Acknowledgment of an “AI research assistant” (Claude) is unusual for PRD. If allowed by journal policy, fine; if not, it should be removed or rephrased as use of text-editing tools without implying scientific contribution.
- Required fix: Confirm with the editor whether such acknowledgments are permissible. If not, remove or restate as “The author used automated text-editing tools for grammar; all scientific content and analysis were performed by the author.”

MINOR

P1B-m1
- Location: Sec. II (p.3), Sec. V (pp.10–11), Table I (p.5)
- Issue: H0-tension computation. Using 67.68 ± 1.06 vs. 73.04 ± 1.04 gives Δ = 5.36 and σcomb = 1.485 → 3.61σ, consistent with the stated “∼3.6σ.” Add the exact computed value once (3.61σ) when first mentioned, to avoid “∼”.
- Required fix: Where the H0 tension is first quoted, give the computed value 3.61σ with the formula used (Δ/√(σ1^2 + σ2^2)).

P1B-m2
- Location: Fig. 2 caption (p.6–7)
- Issue: Caption ends with “Independent MCMC verification --- 2 frozen dataset combinations” which reads like an internal note, not a scientific caption.
- Required fix: Replace with a neutral caption sentence: “Both combinations independently recover ΔNeff consistent with zero.”

P1B-m3
- Location: Sec. IV (p.7–9)
- Issue: Periodicity sentence: “β ≡ β + n × 90° for E/B.” This is correct for EB which is ∝ sin(4β), but it would help to add one clarification that small-angle posteriors avoid wraparound issues.
- Required fix: Append: “Because our posterior support lies within |β| ≲ 0.7°, the 90° periodicity is irrelevant here.”

P1B-m4
- Location: Sec. VI, Eq. (9) (p.14)
- Issue: Small-angle approximation in the text omits the explicit (fa/MPl)^2 factor until the subsequent clause “For fa = MPl.” This is easy to miss.
- Required fix: Explicitly write the factor in the small-angle expression: “Ωa ≈ (fa/MPl)^2 m^2 θi^2 / [6 H0^2 (1 + zosc)^3]” and then set fa = MPl for the numerical discussion.

P1B-m5
- Location: Sec. VI (p.12–13)
- Issue: Statement “the same β ≈ 0.27° arises in any GR+ALP setup with the same parameters” could be read as implying parameter-independence.
- Required fix: Add “...with the same (ma, fa, Caγ, θi)” to avoid ambiguity.

P1B-m6
- Location: Sec. V, Table II (p.11)
- Issue: Lensing likelihood name is “planck 2018 lensing.clik” vs. “native” in iter2. A one-sentence clarification about the practical difference (native vs clik) would help readers.
- Required fix: Add footnote: “The ‘native’ lensing likelihood is the official 2018 release in the native framework; ‘.clik’ denotes the compiled wrapper. We verified that this choice does not materially impact ΔNeff at our precision.”

P1B-m7
- Location: Introduction (pp.2–3)
- Issue: Reference to the matter-bounce fNL = −35/8 as context is fine, but the text risks sounding like a result from this paper.
- Required fix: Add a parenthetical “not probed in this paper.”

NIT

P1B-n1
- Location: Throughout
- Issue: Hyphenation artifacts (re- line breaks like “re￾producibility”) reveal a PDF text-extraction issue. This is cosmetic but distracting.
- Required fix: Ensure final submission PDF has clean hyphenation.

P1B-n2
- Location: Sec. IV (p.8)
- Issue: Minor grammar: “The amplitude factor 1/2 sin(4β) is identical ... and is not omitted.” This reads oddly.
- Required fix: Rephrase to: “The normalization ½ sin(4β) is used consistently in both the equation and the code.”

P1B-n3
- Location: Bibliography
- Issue: Check that [4] and [18–19] reflect current versions (preprint vs published) at time of acceptance.
- Required fix: Update citations to final journal versions where available.

Length and focus
- The paper is long (24 pages) for a reproducibility/consistency-note with three limited cross-checks. Consider reducing to ≈15–18 pages by moving run-paths, pipeline operational details, and some of the internal chain-accounting footnotes to an online repository README or to Appendices. This is a recommendation, not a requirement, provided clarity is maintained.

Internal arithmetic and dimensional checks (selected)
- S8 combination: 0.827 ± 0.010 with 0.776 ± 0.017 gives combined 0.8138 ± 0.0086 — consistent with the text’s 0.814 ± 0.009 and full-tension 0.814 ± 0.008.
- DES-Y3 tension: Δ = 0.051; σcomb = 0.0197 → 2.59σ, consistent with “2.6σ”.
- MB–H0 degeneracy constant: −19.253 − 5 log10(0.7304) = −18.5695; chain mean: −19.263 − 5 log10(0.6768) = −18.4155; offset 0.154 mag ~ 3.1σ for σMB = 0.049. The paper’s 0.156 and 3.2σ are consistent within rounding and estimator differences noted.
- Pixel-noise conversion: Nside=512 → Ωpix = 47.2 arcmin^2; σpix = 10/√47.2 = 1.455 μK — matches text.
- β forecast significance: 0.27°/0.03° ≈ 9σ — matches text.
- Caγ Δϕ/fa = β/[α/(4π)] using β=0.342° = 5.97×10−3 rad and α/(4π)=5.81×10−4 gives 10.3 — matches text.
- One-sided ΔNeff bounds: construction is sound; numerical values plausible; please report two significant figures consistently and the precise definition (see P1B-M3).

## Summary recommendation
MAJOR REVISIONS

The manuscript is careful and well scoped, but it requires (i) correction of a central abstract statement about the misalignment fine-tuning reference point (E1), (ii) proper immutable archival DOIs replacing “pending” and commit references (E2), (iii) sharper labeling of the NaMaster “bias” as a synthetic-sky pipeline property only (E3), and (iv) a stronger wall around the overlap-uncorrected SN results (E4). Additionally, the dependence of conclusions on fa should be briefly quantified (M1), and a few methodological clarifications and presentation fixes are needed. With these addressed, the paper would meet PRD’s methodological standards for a reproducibility/consistency companion.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS

P1B-E6
- Location: Sec. VI Eq. of motion (p.12), Appendix D (pp.22–23), throughout Sec. VI
- Issue: Notation inconsistency for the ALP mass. The equation of motion uses “m2 fa sin(ϕ/fa)” while Appendix D and much of Sec. VI use ma. It is ambiguous whether m ≡ ma everywhere. This can lead to confusion when comparing formulas and priors, and it affects dimensional clarity of dV/dϕ.
- Required fix: Use a single symbol (ma) for the axion mass everywhere: V(ϕ) = m2
a f2
a [1 − cos(ϕ/fa)], EOM ϕ¨ + 3Hϕ˙ + m2
a fa sin(ϕ/fa) = 0, and in all text/tables. Add one sentence after the first appearance: “Hereafter m ≡ ma.”

P1B-M7
- Location: Sec. IV (pp.8–10), Fig. 3 caption (p.7), Conclusions (p.15)
- Issue: Ambiguity in bias-correction prescription. The text alternates between describing a multiplicative under-recovery of ≈12% (β̂/βinj ≈ 0.88) and carrying forward a worst-case absolute offset of 0.040°. These two corrections are not equivalent and can imply different adjustments depending on signal amplitude.
- Required fix: Choose a single prescription and state it unambiguously: either (i) a multiplicative calibration β̂ = (0.88 ± δ) βinj with δ quoted from MC, or (ii) an absolute offset β̂ = βinj − (0.032–0.040)°. If you retain both, clearly state which one is used in any downstream adjustment and that the other is shown only as a diagnostic. Reflect the choice consistently in Sec. IV and Conclusions.

P1B-M8
- Location: Sec. IV “Noise model and injections” (p.8–9)
- Issue: Polarization-noise convention (√2 factor) is not standardized across the literature. The manuscript adopts σpix = ∆P/√Ωpix with “no √2 factor” for Q and U, but many CMB conventions define ∆P at the map level such that σQ = σU = ∆P/√2/√Ωpix.
- Required fix: State explicitly which convention for ∆P is assumed (per-Stokes, not per-E/B) and add a short check (one-line note or small MC rerun) showing that swapping to the alternative convention (σQ,U = ∆P/√2/√Ωpix with the same ∆P value) does not materially change the recovered bias. This removes an avoidable reproducibility ambiguity.

P1B-M9
- Location: Table I (p.5) “Min ESS”, footnote 1 (pp.3–4), Sec. V.B (p.10)
- Issue: ESS definition ambiguity. “Min ESS” in Table I is not defined (Sokal/IAT vs. GetDist weight-based), while footnote 1 discusses both “post-burnin samples” and “GetDist sum-of-weights” for a different run. Readers cannot tell which estimator underlies Table I’s ESS=4744 and 4692.
- Required fix: Define the ESS estimator once (e.g., Sokal IAT on weight-expanded chains) and ensure all reported ESS values use the same definition. Add a brief sentence in Sec. V or the table caption clarifying the estimator and the effective sample computation.

P1B-M10
- Location: Sec. IV “Template-band treatment” (p.9)
- Issue: Pixel-window handling is asserted to “cancel” but not stated mathematically. Because decoupled spectra are not pixel-window-deconvolved, the template must include the same HEALPix pixel window squared to ensure invariance.
- Required fix: Add one explicit sentence: “We multiply C
EE,tmpl
ℓ by W
2
pix(ℓ;Nside=512) before binning so that both the measured C
EB
b and the template include the same pixel window; we verified that omitting this factor changes β̂ at < 10−3 deg.” If this multiplication was not done, please clarify precisely how the “cancellation” is ensured.

P1B-M11
- Location: Sec. IV “Mode-coupling matrix and binning” (p.8)
- Issue: Binning edges are described as “20 linear integer-edge bins from np.linspace(30, 1536, 21)”. np.linspace returns floats; “integer-edge” is ambiguous and can change which ℓ goes to which bin.
- Required fix: Specify the exact integer edges used (e.g., edges = np.arange(30, 1537, 75) or np.rint(np.linspace(...))). Ideally include the exact array in the text or caption, or reference a DOI’d artifact that contains it.

P1B-m8
- Location: Sec. VI (p.12), Fig. 4 caption (p.17), Appendix D (p.22)
- Issue: Minor inconsistency in H0 numerical value used for conversions. The body often uses H0 = 67.68 km s−1 Mpc−1, while Fig. 4 caption states H0 = 67.7 km s−1 Mpc−1. This is harmless numerically but can trip exact re-computations of derived quantities (e.g., ma/H0 prior mapping).
- Required fix: Use a single value of H0 throughout for conversions (e.g., 67.68) and note it once in Sec. VI.

P1B-m9
- Location: Fig. 3 caption (p.7), Sec. IV text (p.9)
- Issue: Reporting “β̂ = 0.000° at βinj = 0” appears exactly zero. For a finite 500-MC mean, exact zero is unlikely and can be misread as a coding clamp.
- Required fix: Report with meaningful precision (e.g., 0.000 ± 0.002°) and/or state “consistent with zero within 0.002° SE of the 500-MC mean.”

P1B-m10
- Location: Sec. IV “Mode-coupling matrix...” (p.8)
- Issue: Function names slightly inconsistent with the public API (“NmtWorkspace.compute coupling matrix”). This is minor but can hinder direct code matching.
- Required fix: Use the exact API spelling (e.g., NmtWorkspace.compute_coupling_matrix) or cite the specific NaMaster version and a DOI’d script snippet with the call signature.

P1B-m11
- Location: Sec. VI “H0 marginalization note” (p.14)
- Issue: Claim “Marginalizing H0 over the Planck 1σ interval shifts Ωa by ≲ 3% (Ωa ∝ H0−2)” is qualitative. If Ωa < 0.01 defines subsets, a 3% shift can flip a boundary sample’s classification.
- Required fix: Add one quantitative stability metric: the posterior weight within a ±3% band around the threshold (e.g., fraction with 0.0097 < Ωa < 0.0103). Report that fraction to show the Ωa < 0.01 subset is robust to H0 variation.

P1B-m12
- Location: Sec. VI (p.13–14)
- Issue: Small-angle anharmonic correction estimate “O(θi
2/12), i.e. ≲ 8% at θi ∼ 1” is correct, but the text then applies the quadratic Ωa expression more broadly than θi ≪ 1 in intermediate discussions (e.g., Ωa < 0.1 subset includes θi up to ~0.7).
- Required fix: Add a one-sentence reminder where Ωa is used for subset classification that the small-angle formula is an approximation above θi ≳ 0.5 and that you verified via spot EOM checks that the classification for Ωa < 0.1 is not altered at the quoted precision.

P1B-m13
- Location: Sec. VI (p.13)
- Issue: Inverse-variance combination in Eq. (5): “3.9σ upper bound” is correct numerically (0.241/0.061 ≈ 3.95) but the text does not explicitly state that 0.061° results from σ−2 addition.
- Required fix: Append “…with σcombined
−2 = σ−2
Planck + σ−2
ACT assuming zero correlation.”

Explanation
The initial review focused on scope, archival requirements, key clarifications for synthetic-sky bias, and the overlapping SN likelihood. The fresh audit above adds reproducibility-critical clarifications (notation, ESS definition, binning edges, pixel-window handling), removes a potential ambiguity in the pipeline bias calibration (absolute vs multiplicative), and ties off small but recurrent sources of confusion (polarization-noise convention, exact-zero reporting, consistent H0 for conversions). These items commonly trip PRD readers attempting to reproduce results and should be addressed for acceptance.