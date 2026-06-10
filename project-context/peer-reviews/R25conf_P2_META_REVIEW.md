# P2 R25conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 371.5s

---

Meta-review (focus: blind spots not caught by the five referees)

P2-META-E1
- Severity: ESSENTIAL
- Location: Sec. III.B (pp. 7–8), projection-noise discussion; also used implicitly in Sec. IV and VII
- Why missed: Reviewers focused on r-weighting comparability and Bayes normalization; none audited the inner-product metric used to bound projection noise.
- Problem: The paper computes the shape cosine r_cos with a uniform, unweighted inner product on triangle shape space, then uses 1 − r_cos^2 ≲ 0.03 to argue “projection noise” is negligible for a local-template estimator. But projection (mismatch) variance enters through the estimator’s Fisher metric, not a uniform measure; the correct bound must use the same Fisher weight (survey covariance, triangle counts, redshift binning) as the estimator. As written, the r_cos bound is not tied to the operative covariance and may under- or overstate projection noise.
- Required fix: Recompute r_cos in the Fisher metric actually used for the SPHEREx bispectrum estimator (i.e., weight by the Heinrich et al. triangle/covariance kernel or a faithful surrogate) and update the 1 − r_cos^2 bound; or, if only the amplitude recovery r is to be used, drop the r_cos → projection-noise claim and state explicitly that no estimator-mismatch variance bound is provided.

P2-META-E2
- Severity: ESSENTIAL
- Location: Appendix A.1, Eq. (A7) (p. 22): “Bζ = −2 Im Σ_v Σ_σ (1/S_v) I_v^(σ) …”
- Why missed: Attention was on the −2 Im commutator doubling and Bayes factors; no one checked the vertex symmetry-factor placement.
- Problem: A 1/S_v “symmetry factor” is inserted for the cubic vertices, with S_ζ·ẋζ^2 = 2 for the identical ẋζ legs. In Maldacena’s cubic action the coefficients already reflect the correct operator combinatorics; introducing an additional 1/S_v division risks an extra 1/2 suppression of that vertex, i.e., exactly the class of factor-of-two errors the paper tries to resolve. No derivation is shown that the cubic Lagrangian used here requires an external 1/S_v division.
- Required fix: Justify the 1/S_v factor from first principles (show that the written L(3) lacks the conventional 1/2! for identical fields and therefore needs 1/S_v in the in-in expansion), or remove 1/S_v and absorb all symmetry/combinatoric factors into L(3) coefficients. Then recheck that the claimed −2 Im “doubling” is not being cancelled or compounded by an unintended 1/2 from ẋζ^2.

P2-META-M1
- Severity: MAJOR
- Location: Sec. II.A (pp. 3–5), null-space scan and “matches all three benchmarks exactly”
- Why missed: Referees noted basis dependence and range of r, but not the conditioning bias created by exact benchmark matching.
- Problem: The 10,000 coefficient realizations are explicitly conditioned to reproduce the three published benchmark configurations exactly, then used to infer the distribution of r and r_cos. This conditioning can artificially constrain the shape family and inflate r_cos (and suppress worst-case r) because the scan admits only coefficient sets that pass three stringent moment constraints. The small spread (rcos > 0.97) may therefore reflect the a posteriori constraint, not genuine model uncertainty.
- Required fix: Quantify the impact of this conditioning. For example, (i) repeat the scan allowing the three benchmarks to be matched within realistic numerical/measurement tolerances; (ii) add 2–3 additional “intermediate-shape” constraints (not used to pick coefficients) and report cross-validation errors; or (iii) generate coefficients from an explicit vertex-level Monte Carlo (numerical time integrals) at random triangles, then fit the polynomial and evaluate r. Report how r and r_cos change under these less-conditioned draws.

P2-META-M2
- Severity: MAJOR
- Location: Sec. IV (p. 8–9) and Sec. III.B (pp. 7–8)
- Why missed: Reviewers asked for more Fisher detail and noted non-comparability of pipelines, but no one required the definitive bias test.
- Problem: Missing test. The paper never runs, even in forecast form, a two-template joint fit (local + bounce-specific template) or a matched-filter cross-check to demonstrate that a local-only estimator is unbiased on a bounce signal and to quantify any variance inflation. Given that the forecast relies on projecting a non-identical shape onto the local template, this is the go/no-go test for estimator-induced bias and leakage from orthogonal shapes (including equilateral/folded contaminants).
- Required fix: Add a simple joint-template Fisher analysis (local and bounce jointly fit with realistic SPHEREx covariance) to report (i) the bias of a local-only fit to a bounce signal, (ii) the variance inflation from allowing the bounce template in the fit, and (iii) the correlation coefficient between the two templates under SPHEREx weighting. If infeasible now, state explicitly that the headline significance assumes zero estimator bias and provide an a priori bound on the bias from this correlation.

P2-META-M3
- Severity: MAJOR
- Location: Sec. VII.B (p. 14) and throughout where PNG-bias cross-terms are described
- Why missed: Reviewers questioned the size of bϕ-induced degradations, but not the field/units consistency of the cross-terms.
- Problem: Field-mixing ambiguity. The PNG cross-terms in the bispectrum section are described schematically as “fNL bϕ b1^2 P(k1)P(k2)”, but P here must be the matter power spectrum; elsewhere, Pζ and PΦ denote primordial spectra and are used in normalization statements. Without an explicit mapping (M(k, z), T(k), D(z)) tying Pζ/PΦ to P_m in the same normalization used by Heinrich et al., this shorthand risks hidden T(k)/M(k, z) omissions and unit inconsistencies in the bispectrum channel.
- Required fix: Write the explicit tree-level bispectrum terms used in the forecast with field labels (e.g., P_m vs P_ζ), including all M(k, z) or T(k)D(z) factors, and confirm they match the normalization in Heinrich et al. Clarify that bϕ carries δ_c where applicable, to avoid double counting in Δb and bispectrum cross-terms.

P2-META-M4
- Severity: MAJOR
- Location: Sec. IV (p. 8), injection–recovery paragraph
- Why missed: Others noted pipeline non-comparability; no one challenged the f_sky heuristic’s applicability to this specific test.
- Problem: The “slightly optimistic” caveat quantifies partial-sky degradation using the 1/√f_sky CMB heuristic for an ancillary 2D, flat-sky, tiled KSW-like test. But the noise model for that test is described as “SPHEREx photometric-z power spectra as the diagonal noise covariance,” i.e., not a CMB C_ℓ pipeline. The 1/√f_sky scaling is inapplicable to this construction even as a heuristic and could mislead readers about the magnitude of the optimism.
- Required fix: Remove the 1/√f_sky degradation claim for the injection–recovery test, or replace it with a test-specific window-function Monte Carlo (e.g., tile subset vs full tiling) that demonstrates the actual impact on the reported r_meas.

P2-META-M5
- Severity: MAJOR
- Location: Sec. IV (p. 8–9), assumption applying σ(fNL) at fNL = −4.375
- Why missed: One reviewer noted Fisher fiducial shifts qualitatively; none flagged the non-Gaussian covariance point.
- Problem: Hidden conditioning. Applying the Heinrich et al. σ(fNL) (computed at fNL ≈ 0 with Gaussian covariance) at fNL = −4.375 assumes the covariance remains Gaussian-dominated. At |fNL| ~ 4 the trispectrum-induced non-Gaussian covariance can contribute at the few–10% level for LSS bispectra, modifying σ and optimal weights. No check is presented.
- Required fix: Bound the non-Gaussian covariance correction at |fNL| ≈ 4 using a standard trispectrum scaling estimate (or cite one) and state how large a σ shift it could induce for SPHEREx. If potentially >O(5–10%), incorporate it into the systematic budget or justify neglect based on survey specifics.

P2-META-m1
- Severity: MINOR
- Location: Sec. II.A, Table I and caption (p. 5)
- Why missed: Prior reviews focused on coefficient bases and benchmarks but not on configuration categorization.
- Problem: The “Folded (k1 = 2k2 = 2k3)” row evaluates the strictly degenerate boundary k1 = k2 + k3, which is a measure-zero limit. Presenting it as a configuration without stating it is a limit may confuse readers (e.g., about integrability and estimator binning near folds).
- Required fix: Relabel the row explicitly as “Folded limit (k1 = 2k, k2 = k3 = k)” and note that the value is the limit of that sequence; clarify how this is handled in numerical integration (e.g., evaluate at a small offset from exact degeneracy).

P2-META-m2
- Severity: MINOR
- Location: Sec. III.B (pp. 7–8), “squeezed-limit cutoff is completely insensitive”
- Why missed: A reviewer suggested adding a rationale but did not catch the metric inconsistency.
- Problem: The stated cutoff insensitivity (<2×10^−4 shift in r when x_3,min varies from 0.001 to 0.2) is evaluated under a uniform-triangle measure, while the headline r for SPHEREx is derived under noise/Fisher weighting. The result therefore does not certify cutoff insensitivity for the SPHEREx-weighted r that underpins the forecast.
- Required fix: Repeat the cutoff test using the same Fisher weight used to define the SPHEREx r (or state explicitly that the cutoff-insensitivity claim applies only to the unweighted overlap and is not used in the forecast).

P2-META-N1
- Severity: NIT
- Location: Sec. II.A (p. 3), list of S3 degree-9 orbits
- Why missed: Others focused on basis dependence and SVD rank; no one sanity-checked the orbit enumeration.
- Problem: The orbit list mixes “P_i k_i^9” with “P_{i≠j} k_i^6 k_j^3”, etc., but never defines the precise normalization or multiplicity of each orbit (e.g., whether sums are over ordered or unordered pairs/triples and how equality cases are handled). This creates ambiguity for replication.
- Required fix: Provide a compact definition of each symmetric-orbit sum (ordered vs unordered, multiplicity weights) so that a reader can reconstruct the six basis polynomials exactly.

Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential and major issues: (i) Bayes-factor normalization and prior-sensitivity presentation (from prior reviews), (ii) a dimensionally inconsistent printed definition of BNL in Eq. (2) (prior), (iii) GR-degradation mapping (prior), and now (iv) a projection-noise bound built on an incorrect metric, and (v) a likely spurious symmetry factor in the in-in formula, plus (vi) a missing joint-template bias test that would shore up the estimator projection argument. Altogether I count 5–7 true blockers (2–3 essential, 3–4 major) that materially affect the headline conclusions or their evidentiary footing. My confidence that the paper can ultimately survive external peer review is moderate, provided the authors correct the normalization/definition issues, redo the Bayes calculations, quantify estimator mismatch under the proper Fisher metric, and cleanly separate conditioning and weighting assumptions. The scientific direction is promising; the analysis just needs to be tightened and made internally self-consistent.