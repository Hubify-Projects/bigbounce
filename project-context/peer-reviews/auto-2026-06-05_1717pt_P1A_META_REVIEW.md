# P1A auto-2026-06-05_1717pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 388.4s

---

Meta-Referee report on “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”

New issues not raised by any of the five prior referees

P1A-META-E1
- Severity: ESSENTIAL
- Location: Sec. IV B, Eq. (14), p. 9
- Why missed: Others focused on the provenance of θ and the loop ambiguity but did not check the operator’s mass dimension explicitly.
- Problem: The postulated one‑loop operator Γone-loop ⊃ −(1/16π^2) β(γ) MPl−1 ∫√−g ∂μθ J5μ is dimensionally inconsistent for a dimensionless θ (the standard normalization θ ≡ a/fa). With θ dimensionless, ∂μθ J5μ has mass-dimension 4, so the coefficient must be dimensionless; the added factor 1/MPl wrongly reduces the operator to dimension 3. If θ is instead taken to have mass dimension 1, that must be stated and normalized consistently (θ/fa), and then the coefficient changes.
- Required fix: Specify θ’s normalization and mass dimension; either (i) drop 1/MPl and absorb all loop factors into a dimensionless coefficient when θ is dimensionless, or (ii) redefine θ=a with [a]=1 and write (1/fa)∂μa J5μ with a dimensionless coefficient. Recompute all downstream amplitude estimates with the corrected normalization.

P1A-META-E2
- Severity: ESSENTIAL
- Location: Notation across paper (e.g., Sec. II A.1, Eq. (2) p. 5; Sec. X G, p. 15; Table IV p. 20)
- Why missed: Each reviewer addressed different technicalities; none audited symbol reuse across disparate sections.
- Problem: γ is used for both the Barbero–Immirzi parameter and the PTA gravitational-wave spectral index (e.g., “γ = 2.567 ± 0.382” later in the text) with only sporadic disambiguation (γPTA appears only in Table IV). This invites misinterpretation when γ also controls ρcrit in Eq. (9) and four-fermion coefficients elsewhere.
- Required fix: Globally disambiguate: reserve γBI (or simply γ) exclusively for Barbero–Immirzi; use γPTA for the PTA spectral index everywhere. Correct all occurrences in text, tables, and figure captions.

P1A-META-M1
- Severity: MAJOR
- Location: Sec. XII B and XIII (e.g., p. 16) and Table IV
- Why missed: Other reviews challenged significance statements but not the origin of the benchmark number itself.
- Problem: The paper adopts “β ≈ 0.27°” as a “benchmark consistency point,” evidently a midpoint between 0.342°±0.094° (WMAP+Planck) and 0.215°±0.074° (ACT DR6), without any statistical combination. A midpoint is not a valid estimator; a weighted average would be ≈0.27° only incidentally if errors and covariances warrant (and they are not shown).
- Required fix: Either (i) quote each experiment separately, or (ii) present a proper inverse‑variance (or full covariance) weighted average with uncertainties, stating any independence assumptions and correlations. If no meta‑analysis is intended, remove the “benchmark 0.27°” altogether.

P1A-META-M2
- Severity: MAJOR
- Location: Sec. XIV D, p. 17; also Abstract and Sec. I A references to Ntot vs fNL
- Why missed: Prior reviews flagged the word “definitively” but not the k‑dependence of Nexit implicit in the mapping.
- Problem: The “erasure of fNL” argument fixes Nexit ≈ 60 while discussing SPHEREx modes spanning k ≈ 10−4–10−1 h/Mpc. Nexit is k‑dependent; using a single CMB‑pivot value for the full SPHEREx range is not justified and biases the claim of erasure across the band.
- Required fix: Provide Nexit(k) across the SPHEREx k‑range and recompute the physical scale shift kphys,bounce(k) ∝ eNtot−Nexit(k). Quantify for which k it remains a “vacuum‑inflationary” regime and where, if anywhere, contraction‑mode imprints could survive. Replace “definitively erased” with a k‑resolved statement supported by this computation.

P1A-META-M3
- Severity: MAJOR
- Location: Sec. II B (LQC bounce, p. 6) vs the ECH framework throughout
- Why missed: Reviewers critiqued the completeness of ECH closures but not the consistency of mixing ECH torsion with LQC holonomy dynamics.
- Problem: The paper adopts LQC’s effective Friedmann equation and ρcrit(γ) while independently invoking Einstein–Cartan torsion dynamics to motivate parity‑odd operators. It is not shown that the torsionful ECH sector and the torsionless LQC holonomy‑corrected dynamics can be consistently combined in a single effective description at the bounce (e.g., matter content, constraints, and connection choices differ).
- Required fix: State clearly whether the bounce dynamics used are strictly LQC (torsionless) or an ECH‑modified system; justify the hybridization with a citation or a brief derivation showing that adding algebraic torsion leaves the adopted LQC background equation intact in the regime considered. If such a demonstration is unavailable, either decouple the two (use LQC only as external context) or present the closure analysis without relying on LQC ρcrit.

P1A-META-M4
- Severity: MAJOR
- Location: Sec. II A.2 Eq. (5)–(6), p. 6; Appendix B, p. 19
- Why missed: Others focused on the off‑shell dimension and ansatz; none questioned the use of the area‑gap scale as a generic EFT mass in the coupling.
- Problem: The coefficient M is identified with the LQG area‑gap “mass scale” M∆ ≃ MPl/√γ and used as the UV scale in the effective operator α/M. Treating a kinematic area eigenvalue scale from LQG as the UV suppression scale of a low-energy EFT operator is nonstandard and unmotivated; it biases [(α/M)MPl] without justification.
- Required fix: Justify with references why M should equal M∆ in the EFT coefficient, or treat M as a generic EFT cutoff and provide a range with clear physical priors. Propagate the resulting uncertainty into all amplitude estimates and into the Ntot bookkeeping if retained.

P1A-META-M5
- Severity: MAJOR
- Location: Sec. II C.1 “Reheating thermal-reset barrier,” p. 6–7
- Why missed: Others noted the lack of rates and references; none checked dimensions of the stated fluctuation scaling.
- Problem: The text asserts “the post‑reheating mean torsion is set by the thermal expectation ⟨J5μ⟩T, whose r.m.s residual scales as ∼ √nψ/T1/2reh.” This scaling is dimensionally inconsistent for ⟨J5μ⟩ (mass-dim 3); √nψ/T1/2reh has mass-dim 1, not 3. As written, the fluctuation estimate cannot feed consistently into an algebraic torsion source term.
- Required fix: Replace with a kinetic‑theory based estimate of axial‑charge fluctuations (e.g., from susceptibilities χ5(T) and relaxation rates Γ5), showing the correct mass dimensions and the comparison to H(Treh). If such a derivation is out of scope, remove the dimensional claim and keep only the qualitative thermalization argument with proper citations.

P1A-META-M6
- Severity: MAJOR
- Location: Sec. IX, Table II p. 13 and surrounding text
- Why missed: Reviewers spotted only the B8/B14 dependence; none audited other overlaps.
- Problem: Several “barriers” are not logically independent beyond B8/B14. Barrier 1 (Mass‑Coupling Lock), Barrier 4 (Planck Suppression), and Barrier 11 (Decoupling Universality) are restatements of the same MPl‑suppression logic under different guises; similarly, Barriers 5 (Scale Separation) and 10 (UV→IR Specificity) heavily overlap. Treating them as distinct strengthens the closure rhetorically without adding independent constraints.
- Required fix: Consolidate overlapping barriers or explicitly demonstrate independence (e.g., construct counterexamples where one holds and the others fail). Update the “13 logically‑independent” count accordingly everywhere it appears.

P1A-META-m1
- Severity: MINOR
- Location: Sec. II C, Eq. (10), p. 6
- Why missed: Others focused on Λ vs ρΛ dimensions; none noted the undefined angle brackets.
- Problem: Ξ is defined as Ξ ≡ ⟨(α/M) MPl⟩ Dinf, but the angle brackets ⟨…⟩ are never defined (time average? ensemble? renormalization‑scheme average?).
- Required fix: Define precisely what the averaging denotes (if any), or remove the brackets and treat (α/M) MPl as a parameter with a stated prior/range.

P1A-META-m2
- Severity: MINOR
- Location: Sec. X F, p. 15 and Abstract
- Why missed: Others questioned ECH’s relation to birefringence but not this specific attribution.
- Problem: The sentence “tests of γ shift to nonperturbative parity‑violating channels (ALP birefringence, primordial GWs)” incorrectly conflates γBI with ALP phenomenology. ALP–photon birefringence does not test γBI unless a concrete γ‑dependent portal is exhibited.
- Required fix: Rephrase to say that, within the minimal ECH with canonical scalars, perturbations do not probe γBI; any surviving parity‑odd signatures (e.g., ALP birefringence) are independent of γBI unless a specific γ‑dependent coupling is introduced and derived.

P1A-META-m3
- Severity: MINOR
- Location: Sec. II B, p. 6; Appendix B, p. 19
- Why missed: Others noted scheme dependence; none flagged the statistical presentation.
- Problem: The spread of γ values from different counting schemes (U(1), SU(2), DLM) is treated as a quasi‑error bar in several places (e.g., a “∼0.020 figure” carried into parameter tables). This conflates theoretical scheme ambiguity with statistical uncertainty.
- Required fix: Present the values as distinct scheme choices without pseudo‑error bars. When a numerical range is used downstream (e.g., ρcrit window), label it explicitly as “scheme‑dependent range,” not as an uncertainty band.

P1A-META-m4
- Severity: MINOR
- Location: Sec. II A.2 Eq. (5)–(6), p. 6
- Why missed: Others critiqued operator content; none highlighted the physical interpretation.
- Problem: Using the area‑gap to define a “mass scale” M results in M ≈ MPl/√γ > MPl for γ<1, i.e., a super‑Planckian “EFT scale.” If retained, this requires an explicit statement because it is counterintuitive in an EFT context.
- Required fix: Acknowledge that M∆ > MPl for γ<1 and explain why using a super‑Planckian mass scale in the coefficient does not invalidate the EFT reasoning, or abandon M∆ as the EFT mass and adopt a physically motivated M with M ≤ MPl.

## Meta-review recommendation
REJECT

Even aside from the substantial concerns raised by the five referees, the additional issues above include two essential errors (operator dimensionality in Eq. (14) and symbol collision for γ) and several major conceptual gaps (k‑dependent Nexit ignored in the fNL–Ntot argument; unmotivated hybridization of ECH torsion with LQC holonomy dynamics; nonstandard use of the LQG area‑gap as an EFT mass; dimensionally inconsistent thermal fluctuation estimate; barrier double-counting). Collectively, these undermine both the correctness and the clarity of the paper’s central claims.

Given the union of all six reviews, there are well over a dozen independent blockers (at least 8 ESSENTIAL/MAJOR in the earlier reports plus the 6 new ones here). My confidence that the manuscript would survive external, non-companion peer review in its present form is very low. A viable resubmission would require a thorough rewrite: remove or rigorously derive all ansätze, make the work self-contained, correct dimensional analyses and notation, justify the ECH–LQC hybridization, and present unambiguous, reproducible amplitude calculations for each “route.”