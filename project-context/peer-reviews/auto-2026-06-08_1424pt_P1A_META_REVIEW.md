# P1A auto-2026-06-08_1424pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 458.6s

---

META-REVIEW: new issues not caught by any of the 5 prior referees

P1A-META-E1
- Severity: ESSENTIAL
- Location: Sec. IV.B (Eq. 15 narrative), p. 9–10
- Why others missed it: They focused on dimensional consistency and the 10^−60 vs 10^−33 ambiguity, but not on the specific coupling used.
- Problem: The text inserts an electromagnetic loop factor αem/(4π) into a purely gravitational/fermion one‑loop estimate for a Holst/Nieh–Yan–induced operator. Quote: “The dimensionless coefficient is O(αem/4π)…” There is no EM field in the Route‑2 operator θNY–J5, so αem is not the appropriate loop factor; one expects a pure 1/(16π^2) (times gravitational/matter couplings), not αem.
- Required fix: Replace αem/(4π) by the correct loop normalization for the gravity–fermion sector (1/16π^2 with the appropriate dimensionless vertex factors), re-derive the amplitude, and update the suppression estimate and conclusions accordingly. If an EM loop is genuinely intended, show the explicit chain from θNY–J5 to photon-sector birefringence with the correct gauge couplings.

P1A-META-E2
- Severity: ESSENTIAL
- Location: Sec. IV.B (Eq. 14) and surrounding narrative, p. 9–10
- Why others missed it: They challenged dimensions and the mapping to EB but not the ontological status of θ.
- Problem: The manuscript treats “θ(x) is the Nieh–Yan pseudoscalar” as a propagating field with ∂μθ ∼ H0 today, without introducing a dynamical Immirzi field or propagating torsion. In minimal EC with constant γ and non-propagating torsion, θNY is a density built from torsion/contorsion and is not a free field with time evolution. Using ∂μθ as if it were a slowly varying background scalar is unjustified.
- Required fix: Either (i) promote γ to a bona fide dynamical pseudoscalar (with a kinetic term) and show how θ acquires dynamics, or (ii) drop the ∂μθ J5 operator as a late-time source and remove the birefringence comparison based on it. State clearly what θ is and is not in the minimal EC–Holst theory.

P1A-META-E3
- Severity: MAJOR
- Location: Sec. II.A.2, Eq. (6), p. 6; Eq. (5) prior line
- Why others missed it: They flagged general notation issues, but not this specific internal–spacetime index swap.
- Problem: Index structure is inconsistent between the 4‑form eI ∧ eJ ∧ FIJ (internal indices, εIJKL) and the component rewrite with εμνρσ eIμ eJν FIJρσ (spacetime epsilon). Holst-like terms use the internal Levi-Civita εIJKL; contracting with εμνρσ as if it were equivalent is not correct without showing the intermediate steps and density weights. This mistake propagates into the dimensional counting that follows.
- Required fix: Rewrite the component expansion with explicit internal εIJKL (and tetrad determinants) or keep differential-form notation. Show one clean derivation of the component expression from e ∧ e ∧ F with the correct epsilon and measure factors.

P1A-META-E4
- Severity: MAJOR
- Location: Sec. X.A–C, p. 14–15
- Why others missed it: They accepted the scalar/tensor framing and did not interrogate completeness by sector.
- Problem: The “perturbation-transparency” statement is advertised as “at all perturbation orders,” but it only treats scalar and tensor modes. Vector perturbations are not discussed at all, yet the headline phrasing implies full perturbation-space coverage.
- Required fix: Either extend the transparency proof to vector modes (explicitly showing vanishing torsion source and Holst-sector inertness) or amend the statement everywhere to “for scalar and tensor perturbations,” and add a brief note explaining why vector modes do not change the observables considered.

P1A-META-E5
- Severity: ESSENTIAL
- Location: Sec. II.C.1, p. 6–7 (“Order-of-magnitude matching” paragraph)
- Why others missed it: They focused on the ad hoc (Treh/MGUT)3/2 factor, not on the algebraic error in the scaling argument itself.
- Problem: The text claims “this holds at the cubic axial-current operator level because the cube of the fermion bilinear scales as the cube of the fermion number density.” There is no cubic axial-current operator in minimal EC (torsion ∝ J5; the induced contact is ∝ J5·J5). The appearance of “cube” is a conceptual error — torsion scales linearly with J5, and the induced four-fermion energy density scales like (J5)^2 ∝ nψ^2, not like the cube of a bilinear.
- Required fix: Remove the “cubic axial-current operator” language and correct the scaling discussion: specify cleanly how torsion, the contact term, and any effective energy contribution scale with a, and which operator is being diluted (J5 or J5·J5). Re-derive Dinf with the corrected scaling chain.

P1A-META-E6
- Severity: MAJOR
- Location: Sec. II.A.2, Eq. (6), p. 6
- Why others missed it: They flagged dimension inconsistencies in Appendix B, but not the measure double counting in Eq. (6).
- Problem: The component form includes √−g εμνρσ eIμ eJν FIJρσ. With tetrads present, ε-tensors and the determinant are tightly related; writing both √−g and εμνρσ together with eIμ eJν risks double counting the density weight. As written, the integrand is not clearly a scalar density of weight one.
- Required fix: Provide a consistent density bookkeeping: either work with tensor densities (no √−g and use Eμνρσ ≡ √−g εμνρσ), or insert the internal epsilon and tetrad determinants properly to yield a scalar density. Then redo the mass-dimension count on the corrected integrand.

P1A-META-M1
- Severity: MAJOR
- Location: Data and Code Availability (p. 18) vs. Sec. I (p. 5) and throughout
- Why others missed it: They focused on reliance on “in preparation” works but not on the contradiction with the availability claim.
- Problem: The paper states “All materials necessary to reproduce the cosmological and galaxy spin results are publicly available at … GitHub.” Yet the cosmological posteriors, NaMaster validation, ALP fits, and galaxy-spin nulls are explicitly deferred to “companion works in preparation” and not actually present in this manuscript. The availability claim is therefore overstated and internally inconsistent.
- Required fix: Align the availability statement with reality. Either move the essential MCMC chains, configs, and chirality-catalog code/results into this submission (supplement) or revise the statement to clarify which artifacts are available now and which are pending companion papers.

P1A-META-M2
- Severity: MAJOR
- Location: Sec. II.C, Eq. (10) and paragraph below, p. 6
- Why others missed it: They objected to the rotation’s irrelevance, not to the misuse of the cited bound.
- Problem: The bound (ω/H)0 < 5×10^−11 is quoted to dismiss the cω ω^2 term. The cited Saadeh et al. 2016 bound constrains Bianchi-type anisotropy/rotation parameters; mapping that directly to a rigid global rotation ω/H with this numerical value is not justified in the text. “Completely negligible” follows from an apples-to-oranges comparison.
- Required fix: Provide the explicit mapping from the Bianchi constraints to your ω parameter (with definitions and units), or remove the ω-term entirely from Eq. (10) and the surrounding discussion.

P1A-META-M3
- Severity: MAJOR
- Location: Sec. III.A, p. 7–8 and Conclusions, p. 18
- Why others missed it: They debated significance arithmetic but not the calibration degeneracy baked into the measurement.
- Problem: The manuscript uses WMAP+Planck EB results as “isotropic birefringence” evidence without acknowledging the calibration–birefringence degeneracy and the specific self-calibration technique (Minami–Komatsu) used to separate them. Presenting β as a clean cosmological observable here glosses over instrument-angle systematics central to the measurement.
- Required fix: Add a short paragraph noting the calibration–birefringence degeneracy, the role of EB self-calibration in Minami–Komatsu/Eskilt–Komatsu, and that any comparison to theoretical β must account for such degeneracies. Adjust the language around “consistency with observed β” accordingly.

P1A-META-M4
- Severity: MAJOR
- Location: Sec. IV.D, Eq. (17) and narrative, p. 10
- Why others missed it: They checked dimensionality but not the time‑integration regime.
- Problem: For mθ ∼ H0, the ALP is still slow-rolling (not oscillating) between recombination and today. Using θ0 ≈ √(2ρθ)/mθ to estimate Δθ between z ≈ 1100 and 0 overstates the accumulated rotation unless the field actually evolves by an O(1) fraction of θ0 in that interval. The paper treats θ0 as Δθ without solving the slow-roll equation, biasing the β–ρ–m relation.
- Required fix: Solve the ALP background equation in the mθ ∼ H0 regime to compute Δθrec→today and re-express β = (α/2M) Δθ with that integral. Update the mθ ~ H0 “naturalness” discussion accordingly.

P1A-META-M5
- Severity: MINOR
- Location: Sec. XIV.D and surrounding, p. 17; also Sec. II.C
- Why others missed it: They accepted the bounce-to-SPHEREx scaling qualitatively.
- Problem: The mapping kphys,bounce ∼ kphys,SPHEREx eNtot–Nexit implicitly assumes a trivial post-inflationary thermal history for the whole interval between horizon exit and today. A complete mapping for SPHEREx-relevant comoving modes requires accounting for reheating temperature and subsequent changes in g∗(T). None of this bookkeeping is shown, yet the conclusion (“definitively erased”) relies on it.
- Required fix: Include the standard thermal-history transfer (Nreh, wreh, g∗) in the mode-mapping argument or recast the claim as qualitative, with an explicit caveat that precise thresholds depend on reheating history parameters.

P1A-META-m1
- Severity: MINOR
- Location: Sec. III.B, p. 8; Sec. V, p. 11
- Why others missed it: They focused on “in preparation” dependence rather than apples-to-oranges comparability.
- Problem: The paper “refutes Shamir’s 3% asymmetry” using a full DR8 classifier without demonstrating footprint/depth/morphology matching to Shamir’s spiral subsamples. As stated, the comparison risks an apples‑to‑oranges critique (different selection, redshift and magnitude cuts).
- Required fix: Add a sentence clarifying how the DR8 sample is matched (or not) to Shamir’s selection (footprint, depth, redshift, morphology). If unmatched, rephrase as “we find no evidence for a dipole in our sample,” and avoid framing it as a direct refutation.

P1A-META-m2
- Severity: MINOR
- Location: Eq. (12), Sec. III.A, p. 7
- Why others missed it: They checked dimensionality but not the practical approximation.
- Problem: For small β, CℓEB ≈ 2β(CℓEE − CℓBB) is fine, but in practice EB ≈ 2β CℓEE (since unlensed CℓBB is negligible). Using CℓEE − CℓBB here is harmless but invites confusion when relating to observed spectra where lensing BB is present.
- Required fix: Add a parenthetical “for β ≪ 1, EB ≈ 2β CEE (since CBB ≪ CEE prior to lensing)” to align the analytic formula with practical usage.

Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews (the five prior referee reports plus this meta-review), the blocker count is high: multiple essential issues (dimensional mismatches, wrong operator identities, reliance on unpublished companions, mis-specified couplings, and unproven dynamical assumptions about θ) plus several major methodological gaps (incomplete sector coverage of the “theorem,” misuse of external bounds, and insufficiently justified mappings to observables). My confidence that the paper would survive independent external peer review in its current form is low. With a thorough rewrite that (i) makes the manuscript self-contained, (ii) corrects the operator identities and loop factors, (iii) removes unjustified mappings to EB without a dynamical θ, and (iv) recasts the perturbation-transparency claim with precise scope, the core qualitative message could become publishable. However, substantial technical and presentational work is required.