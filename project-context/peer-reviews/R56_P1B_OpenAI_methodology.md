# P1B R56 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/private/tmp/R56_P1B/paper1b_mcmc_companion.pdf` md5=f5f3c8ad pages=22
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8311 chars)
**Wall time**: 425.8s

---

Referee report: PRD methodology review for “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Scope of review
- Focus: statistical-method validity, internal arithmetic/consistency, estimator declaration, uncertainty propagation, and abstract-to-body calibration.
- I audited every scalar in the abstract and conclusions, recomputed quoted σ-levels and key ratios, and checked dimensional consistency of equations.
- I treat this as a standalone submission; reliance on companion papers must not be load-bearing for claims here.

Overall assessment
The MCMC proxy and NaMaster Monte Carlo sections are carefully scoped and most numerical claims are internally consistent. Several places, however, do not yet meet PRD standards. Chief issues: (i) the overlap-uncorrected SN product likelihood driving the w0wa “tail-distance” numbers; (ii) the characterization of a NaMaster “pipeline bias floor” that is in fact estimator-dependent and largely eliminated by inverse-variance weighting; (iii) absence of permanent, citable DOIs for the deposited artifacts; (iv) a few places where quantiles/units are ambiguous in tables or robustness statements lack a numeric bound.

Findings

ESSENTIAL

P1B-E1
- Location: Abstract, p.1; Sec. IV, pp. 9–11; Conclusions, p.16
- Problem: The abstract states “the worst-case bias … −0.040° … is carried forward as the observed pipeline bias floor,” and Sec. IV repeatedly labels this a “NaMaster pipeline bias (deconvolution-algebra bias).” However, the robustness battery shows ≈80% of this bias disappears under inverse-variance weighting (β̂ = 0.264°, bias −0.006°; p.11). The bias is therefore dominated by the unweighted χ2 template fit’s equal weighting of noise-dominated bins, not by the NaMaster E→B deconvolution or MASTER algebra.
- Required fix: Reword everywhere “pipeline bias floor”/“deconvolution-algebra bias” to “estimator-weighting-induced calibration bias for an unweighted template fit” and state explicitly in the abstract and conclusions that the bias is estimator-dependent and is reduced to −0.006° ± SE by inverse-variance weighting. Report the corresponding SE (standard error of the 500-MC mean) for both unweighted and weighted cases. Do not present −0.040° as a floor.

P1B-E2
- Location: Sec. III (Physics interpretation paragraph) pp. 4–5; Sec. V.C p.12; Table II p.6; Conclusions p.16
- Problem: The w0wa results are obtained with an overlap-uncorrected DES-SN5YR × Pantheon+ product likelihood despite ≈20% shared SNe and different Malmquist corrections. Tail-distance quotes (+4.3σ, −3.6σ; phantom crossing) hinge on this invalid likelihood, even though caveats are given.
- Required fix: Either (a) remove these w0wa σ-distances from the main text and move the entire overlap-uncorrected result to an appendix labeled “diagnostic only,” or (b) provide an overlap-aware joint SN covariance (or two separate, non-overlapping SN runs) and re-compute the posteriors. In either case, delete tail-σ claims from the abstract and conclusions and refrain from any apparent “exclusion” language until a valid likelihood stack is used.

P1B-E3
- Location: Data and Code Availability, p.17–18; Appendix A, pp. 18–19
- Problem: No permanent DOIs are provided for the code and data snapshots; text says “DOI assignment is pending.” PRD requires stable, citable archives for reproducibility.
- Required fix: Deposit frozen chains, NaMaster artifacts, and ALP chains in a permanent archive (e.g., Zenodo/Dataverse) and provide DOIs. Reference the exact tagged code release (git tag) matching the manuscript, not a moving branch. Remove “pending” language.

MAJOR

P1B-M1
- Location: Sec. IV, p.10–11
- Problem: Language conflates “NaMaster pipeline” with “template-fit estimator.” The robustness tests show apodization, purification, and sky fraction are not responsible; the bias is primarily due to unweighted fitting and (to a lesser extent) an injected-BB shape choice. Calling this a “deconvolution-algebra bias” suggests MASTER/NaMaster is at fault.
- Required fix: Throughout Sec. IV and the caption of Fig. 3, distinguish clearly between (i) pseudo-Cℓ deconvolution (NaMaster) and (ii) the separate amplitude estimator. Attribute the bias to the estimator configuration and BB-shape choice. Provide a one-line control stating that the decoupled spectra themselves are unbiased within MC error.

P1B-M2
- Location: Table IV, p.17; Sec. VI “Spectator-subset readout,” pp. 14–16
- Problem: The three-number entries in Table IV (e.g., “m/H0 4.7/37.7/264”) are unlabeled; it is unclear if they are 16–50–84 percentiles or 5–50–95. Ambiguity prevents independent readers from interpreting the subset summaries.
- Required fix: Label each triplet explicitly as 16–50–84 percentiles (or whatever it is) in the table caption, add units where needed, and ensure β medians carry an uncertainty (e.g., median ± MAD or 16–84% range).

P1B-M3
- Location: Sec. V.A, p.11–12 (Planck pairing); Abstract p.1 (numbers rely on this stack)
- Problem: Mixed Planck PR4 CamSpec high-ℓ with Planck 2018 low-ℓ TT/EE and 2018 lensing is called “standard” but still a release-mixing choice. A PR4-consistent re-run (lollipop.lowlE + pr4lensing) was done, but low-ℓ TT remains 2018.
- Required fix: Either (a) supply a fully PR4-consistent low-ℓ TT counterpart and report any shifts (even if negligible), or (b) justify quantitatively why low-ℓ TT pairing has negligible effect on ΔNeff/H0 at the quoted precision (provide a numeric bound, not only a statement).

P1B-M4
- Location: Sec. VI, pp. 13–16
- Problem: The ALP coupling inference asserts “median Caγ = 20.7 [7.3, 45.6]” under flat priors and later explores a cosθi prior, but the sensitivity of coupling to priors is only qualitatively discussed.
- Required fix: Add a short quantitative prior-sensitivity table for Caγ and θi under flat-θi vs flat-cosθi (show median and 16–84% bands and the fraction of mass in the Ωa < 0.01 subset under each prior). This anchors the “accommodation-not-natural” statement.

MINOR

P1B-m1
- Location: Sec. III, footnote 1, pp. 3–4; Table I p.5; Fig. 1 caption p.7
- Problem: Extensive version and bookkeeping language in the body (“30% burn-in,” “parameter_summary_CORRECTED.json,” “GetDist sum-of-weights,” etc.).
- Required fix: Move these logistics to Appendix A or a reproducibility note. Keep the main text focused on physics and methods.

P1B-m2
- Location: Sec. III, p.4
- Problem: One-sided 95% ΔNeff upper limits: text reports 0.4012 (Planck+BAO+SN) without uncertainty/robustness. A Gaussian analytic check gives ≈0.387 for mean 0.058, σ 0.179.
- Required fix: Add a parenthetical note stating that the chain posterior is mildly non-Gaussian and that a Gaussian analytic estimate would give ≈0.387; confirm the chain-derived value with 5000× bootstrap of weighted samples or report both.

P1B-m3
- Location: Sec. IV, p.9 (“σpix… no √2 factor”)
- Problem: The noise convention for Q and U could be misread.
- Required fix: Add the one-line conventional relation: “Each of Q and U is drawn with σpix defined above; ΔP is the per-Stokes RMS in µK·arcmin.”

P1B-m4
- Location: Sec. IV, Fig. 3 p.9
- Problem: Axes/units are not explicitly stated in the caption for both panels.
- Required fix: State axis labels and units in the caption (“Injected βinj [deg], Recovered β̂ [deg]”) so the figure is interpretable standalone.

P1B-m5
- Location: Sec. IV robustness battery, p.11
- Problem: Inverse-variance-weighted fit result (β̂ = 0.264°) lacks its SE (standard error of the 500-MC mean).
- Required fix: Report the SE for the weighted-fit mean (and σβ per realization as recorded), analogous to the unweighted case.

P1B-m6
- Location: Sec. VI, Eq. (9), p.16
- Problem: The small-angle approximation and the treatment for zosc ≤ 0 are correct but not explicitly flagged in the equation line.
- Required fix: Add “for θi ≪ 1 and zosc > 0” to Eq. (9) and retain the text for zosc ≤ 0 as a displayed case to avoid ambiguity.

P1B-m7
- Location: Sec. IV, p.10 (β = 0 injected → β̂ = 0.000°)
- Problem: Reporting “0.000°” can be misread as exact, not rounded.
- Required fix: Add “(500-MC mean rounded to 0.001°; individual realizations scatter with σβ ≈ 0.046° at fsky = 0.32)”.

P1B-m8
- Location: Sec. VI, Eq. (4), p.13
- Problem: Prefactor convention: αEM/(4π) vs αEM/(2π) varies by Lagrangian normalization.
- Required fix: Keep the present convention but add a citation and one sentence that β = (gaγ/2)Δφ with gaγ = Caγ αEM/(2π fa) so readers can translate conventions.

NITS

P1B-n1
- Location: Sec. VI, p.14
- Problem: Inverse-variance combination of Planck+ACT birefringence gives 0.241°, while a direct recomputation from the quoted numbers yields ≈0.243°; the discrepancy is 0.002° and not material.
- Required fix: Either recompute with full precision or note rounding.

P1B-n2
- Location: Throughout
- Problem: Occasional overuse of “canonical,” “anchor,” and internal path names in prose.
- Required fix: Light copy edit to streamline.

Arithmetic and consistency checks (passed)
- ΔNeff means/σ in Table I match the abstract; one-sided limits are consistent with the described truncation. The H0–SH0ES tension 3.6σ recomputes as 5.36/√(1.06^2+1.04^2) = 3.61.
- S8 tensions: 0.827±0.010 vs 0.776±0.017 → 2.6σ; full-tension 0.814±0.008 vs 0.776±0.017 → 2.0σ; match text.
- wpivot derivation from the chain covariance is correct: wpivot = −0.952 ± 0.019 with ap ≈ 0.790 (zp ≈ 0.27); w0/wa tail distances (+4.3σ, −3.6σ) recompute.
- NaMaster MC SE for 500 means: 0.046°/√500 ≈ 0.0021°, consistent with quoted ±0.002°; multiplicative under-recovery 0.238/0.27 = 0.882 (≈12%); same for 0.302/0.342 ≈ 0.883.
- ALP birefringence normalization: βrad = 5.81×10−4 × 8 × 1.06 = 4.93×10−3 rad → 0.283°; consistent. Required Caγ(Δφ/fa) ~ 10.3 from βobs recomputes.
- ρcrit,0 value 3H0^2 MPl^2 ≈ 3.7×10−11 eV^4 is dimensionally and numerically consistent.
- H(z=0.5) fractional effect size ≈ +1.7% (given the quoted CPL mean) is plausible and welcome as an effect-size statement.

Length
- The manuscript is dense with process details. After moving process/versioning content to Appendix A and removing the w0wa overlap-uncorrected σ’s from the main text (or replacing with overlap-aware results), the main paper could be kept at ≲18–19 pages without loss of scientific content.

## Summary recommendation
MAJOR REVISIONS

The ΛCDM+ΔNeff proxy and NaMaster MC validation are largely sound and well-scoped, but two issues prevent acceptance: (i) the unweighted-estimator “bias floor” is mischaracterized as a pipeline/MASTER bias in the abstract and conclusions despite being estimator-dependent and largely removed by proper weighting; (ii) the w0wa σ-level claims are based on an overlap-uncorrected SN product likelihood and must be removed from the main text or replaced by an overlap-aware analysis. Additionally, PRD requires permanent DOIs for the deposited artifacts. Addressing these, plus the minor clarity fixes above, will bring the manuscript to PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (new items only)

ESSENTIAL

P1B-E4
- Location: Abstract p.1; Sec. VI pp. 13–15
- Problem: Abstract says “the scan-prior m ∼ H0 region brackets the published joint WMAP+Planck signal β = 0.342° ± 0.094°,” which reads as if the m/H0 ∈ [1, 3], Caγ = 8 envelope spans the central value. In the body you later state β(Caγ=8) peaks at ≈0.32° within that envelope, and matching the 0.342° central value at Caγ = 8 requires m ≳ 4 H0 or larger coupling. The abstract phrasing is thus misleading with respect to the central value.
- Required fix: Replace “brackets the published signal” with a precise statement, e.g., “yields β ≈ 0.27–0.32°, i.e., within 1σ of the observed value but below the 0.342° central value at Caγ = 8; matching the central value requires m ≳ 4 H0 or larger coupling.” Make the same clarification wherever this “brackets” language appears.

P1B-E5
- Location: Abstract p.1; Sec. IV Fig. 3 and pp. 9–11
- Problem: “Worst-case bias across injections” is asserted from only two nonzero amplitude points (βinj = 0.27°, 0.342°). Calling −0.040° “worst-case” is not supported by an amplitude sweep; the bias may vary nonlinearly with β.
- Required fix: Either (a) run a modest amplitude sweep (e.g., βinj ∈ {±0.05°, 0.10°, 0.20°, 0.30°, 0.40°}) and report mean bias ± SE vs βinj, or (b) rephrase to “largest observed bias among the two tested injections” and drop “worst-case” language throughout.

P1B-E6
- Location: Sec. IV robustness battery, p.11
- Problem: The inverse-variance weights σb used in the “weighted fit” test are estimated from the same 500 realizations whose means are then reported. Using the same MC to set weights and to evaluate the mean can introduce small but real self-weighting bias.
- Required fix: Recompute the weighted-fit test with cross-validated weights (e.g., split the 500 realizations into two halves, use one half to estimate σb and the other half to measure the mean, and swap), or use analytic σb. Report the cross-validated β̂ and SE. If unchanged within SE, state the bound.

MAJOR

P1B-M5
- Location: Sec. IV, pp. 9–11; Fig. 3
- Problem: The manuscript concludes pseudo-Cl deconvolution is validated, but no quantitative check is shown that the decoupled spectra themselves are unbiased (e.g., 〈ĈEB,decoupled〉 = 0 within MC error for β = 0 across bins; 〈ĈEE,decoupled〉 matches input).
- Required fix: Add a panel or table with per-bin MC means and errors for EB (βinj = 0) and EE/BB residuals against the input template, and a single-sentence conclusion that the decoupled spectra are unbiased within MC error. This isolates deconvolution from the separate amplitude estimator.

P1B-M6
- Location: Sec. IV, “Simulated skies” and robustness battery, pp. 8–11
- Problem: The EE template used in the estimator is identical to the input EE spectrum used to make the maps. This removes template-mismatch effects (A s, n s shifts) that exist in real analyses. Only BB-shape dependence was varied.
- Required fix: Add a test injecting skies with small, realistic EE-shape offsets (e.g., ΔAs/As ≈ ±5%, Δns ≈ ±0.01 within Planck errors) while keeping the fit template fixed, and report the resulting β̂ shift ± SE. Provide a numeric bound showing the estimator’s robustness to EE-template mismatch.

P1B-M7
- Location: Sec. IV robustness battery, p.11; Fig. 3 caption
- Problem: Several robustness statements list means only (apodization 0.5°, 2°, 3°; |b| > 30°; purify_b=True) without SEs. “Unchanged” needs a numeric uncertainty.
- Required fix: For each robustness configuration, add the SE of the 500-MC mean (and σβ per realization if recorded). A one-line aggregate (e.g., “all shifts < 0.002° at 1σ”) is acceptable if supported by numbers in text or a small table.

P1B-M8
- Location: Sec. VI “Spectator-subset readout,” pp. 14–16; Appendix C
- Problem: The Ωa classification treats the zosc ≤ 0 branch (frozen field) correctly in text, but no quantitative breakdown is provided for how much posterior mass lies in the frozen vs oscillating regimes, and how that maps onto the Ωa < 0.01, 0.1 subsets.
- Required fix: Report the fraction of posterior mass with zosc ≤ 0 in the continuous-prior chain, and within each Ωa cut (e.g., “x% of Ωa < 0.01 samples are frozen”). This documents how the Ωa statistic is populated across dynamical regimes.

MINOR

P1B-m9
- Location: Sec. IV weighted-fit description, p.11
- Problem: It is not clear whether σb are computed once and reused across injections or recomputed per injection; this matters for comparability and for the self-weighting issue above.
- Required fix: State explicitly how σb are estimated and applied across tests (per-injection or common), and confirm that the choice does not alter β̂ within SE.

P1B-m10
- Location: Sec. IV estimator paragraph, p.9
- Problem: β-grid resolution (0.001°) is not justified against curvature of χ2(β) near the minimum; potential discretization error is not bounded.
- Required fix: Add a short check (e.g., parabolic interpolation around the best grid point) showing the discretization error is ≤ 5×10−4° (or your measured bound).

P1B-m11
- Location: Sec. IV binning, p.8
- Problem: The 20 linear bins from ℓ = 30 to 1536 are not fully specified (exact integer edges/centers).
- Required fix: List the exact integer bin edges (or provide a one-line reference to a committed artifact file with the edges) so the result is fully reproducible.

P1B-m12
- Location: Table IV, p.17
- Problem: Units for Caγ (dimensionless) and explicit labeling of percentile triplets are missing within the table itself.
- Required fix: Add “triplets are 16–50–84 percentiles” to the caption, and note “Caγ is dimensionless.” Also provide β subset uncertainties (e.g., median ± 16–84% half-width).

P1B-m13
- Location: Sec. VI robustness notes, pp. 14–15
- Problem: Several useful numeric robustness statements (e.g., BB-shape swap reducing the bias to −0.019°) are given without SE.
- Required fix: Add the SE of the 500-MC mean for these tests (mirroring P1B-m7).

P1B-m14
- Location: Sec. VI “Model-independent βfree,” p.14; Appendix C
- Problem: βfree uses only 720 accepted samples (ESS ≈ 265) yet is quoted as 0.344° ± 0.10°. This is flagged as “marginal,” but the same result is used for consistency checks.
- Required fix: Either increase the βfree ESS (e.g., to ≳ 1000) or attach a one-line caveat wherever the βfree number is used that its credible interval is based on limited ESS.

P1B-m15
- Location: Sec. IV footnotes/caption; Fig. 3
- Problem: Panel axes/units are still not self-contained in the figure; the text clarifies, but captions should.
- Required fix: Add explicit axis labels/units in the Fig. 3 caption: “x: injected βinj [deg]; y: recovered β̂ [deg].” Also add the note “β̂ = 0.000° means mean rounded to 0.001°; per-realization σβ ≈ 0.046° at fsky = 0.32” next to the βinj = 0 point.

NITS

P1B-n3
- Location: Sec. IV, p.10–11; Fig. 3
- Problem: You alternate between sin(2β)cos(2β) and ½ sin(4β) for the template without remark. They are equivalent but may confuse readers scanning quickly.
- Required fix: Add a parenthetical once: “sin(2β)cos(2β) = ½ sin(4β).”

P1B-n4
- Location: Sec. VI, Eq. (9), p.16
- Problem: You later clarify the zosc ≤ 0 branch in prose; a displayed two-case definition would reduce reader back-and-forth.
- Required fix: Present Eq. (9) as a two-case definition (oscillating vs frozen) while keeping the small-angle qualifier; the current prose is correct but slightly harder to parse.

P1B-n5
- Location: Sec. IV, “bins above the band limit carry zero template weight,” p.9
- Problem: The code-level mechanism for zeroing template power above ℓ = 1024 is not specified (hard-zero vs masking).
- Required fix: Add a one-liner referencing the exact code line/flag that sets CEE,tmpl,b = 0 above 2Nside, so others can mirror it.

Rationale for additional review
These items focus on (i) abstract-to-body fidelity about the ALP envelope vs the observed central value; (ii) amplitude coverage and weighting methodology of the NaMaster bias tests; (iii) explicit deconvolution sanity checks; and (iv) small but important numeric/uncertainty clarifications needed to make robustness claims quantitatively tight and fully reproducible. They were not covered in the initial pass and are required for PRD-level rigor.