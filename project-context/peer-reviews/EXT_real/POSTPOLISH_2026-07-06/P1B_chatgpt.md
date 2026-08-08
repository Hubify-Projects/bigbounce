# EXT POSTPOLISH 2026-07-06 — P1B — ChatGPT

- **Provider:** ChatGPT (Pro), Big Bounce Book project
- **Model/effort:** Pro Extended
- **Chat URL:** https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a4caaf6-1450-83e8-827f-07821361378e
- **PDF:** P1B_v1B.0.102.pdf (md5 ddaf880631a9c063a0f87b3dad17bd33)
- **Harvested:** 2026-07-07
- **Thought for:** 8m 57s
- **Parsed verdict (from response):** REJECT

## Raw verbatim response

(1) VERDICT: REJECT
(2) ISSUES:

[MAJOR] Section I / standalone status: the manuscript depends on Paper I(a) for the actual ECH structural-closure theorem, perturbation-transparency result, barrier table, and bounce prediction, while those derivations are not reproduced here and the companion-paper arXiv identifier is still a placeholder; this is not a self-contained PRD submission.

[MAJOR] Section III A / "bespoke ECH-sector ∆Neff" claim: the derivation is only dimensional power counting, not a first-principles finite-temperature calculation of the thermal expectation value of the axial-current four-fermion operator; the sign, numerical coefficients, spin averaging, fermion-species content, Holst-parameter dependence, and renormalization/normal-ordering of ⟨AµAµ⟩ are not computed.

[MAJOR] Section III A / identification with ∆Neff: the torsion contribution is described as scaling like a stiff component, ρtor ∝ a−6, yet it is reported as an effective radiation contribution ∆Neff without deriving the mapping to the standard radiation-like Neff parameter; a ratio ρtor/ρrad at BBN is not by itself a valid Neff prediction.

[MAJOR] Sections III and V / stock-CAMB ΛCDM+∆Neff MCMC: the MCMC explicitly does not implement torsion-modified Boltzmann equations, so the reported ∆Neff posterior is only a standard ΛCDM+Neff constraint and provides essentially no test of the ECH spin-torsion sector; the claimed role as an "observational envelope" is scientifically trivial once the claimed theory value is ∼10−44.

[MAJOR] Sections III and V / likelihood and convergence claims: the "verification" rerun uses a different Planck low-ℓ/lensing release pairing from the frozen chains and has R̂−1 = 0.0147, yet is used to bound release-pairing bias at the quoted precision; one non-identical rerun with weaker convergence does not establish such a systematic bound.

[MAJOR] Section IV / NaMaster validation scope: the synthetic skies omit the essential ingredients of a real birefringence measurement—foregrounds, beam systematics, anisotropic/1/f noise, polarization-angle calibration, and the β–α degeneracy-breaking information—so the exercise validates only a toy pseudo-Cℓ algebraic recovery, not a physically meaningful CMB birefringence pipeline.

[MAJOR] Section IV / estimator choice: the canonical estimator is an unweighted χ² fit known in the manuscript to induce a ∼12% multiplicative under-recovery, while an inverse-variance-weighted version removes ≈80% of the bias; retaining the biased estimator for "comparability" invalidates the claim of a validated recovery pipeline.

[MAJOR] Section IV / "systematic floor" language: carrying a 0.040° foreground-free synthetic recovery bias forward as a pipeline bias is misleading because the manuscript itself states it is not a real-sky systematics bound; this number should not be used to contextualize observational uncertainties.

[MAJOR] Section VI / ALP posterior: the ALP MCMC is fit to a single Gaussian summary datum βobs = 0.342° ± 0.094° rather than to EB spectra, covariance, calibration nuisance parameters, or foreground systematics; agreement of βALP and βfree with βobs is therefore tautological and has no independent confirmatory value.

[MAJOR] Section VI / prior-predictive "accommodation cost": the 1σ and 2σ prior-hit fractions depend entirely on arbitrary prior ranges for Caγ, θi, and ma, including non-minimal couplings, so they do not establish that the model is non-tautological or naturally explanatory.

[MAJOR] Section VI and Table IV / spectator-ALP claim: the posterior-supported region is m ≫ H0, requires non-minimal Caγ, and needs post hoc spectator cuts; the manuscript further states that some Table IV mass-fraction and ESS entries are illustrative and not backed by a separate committed summary artifact, which is unacceptable for a paper whose main claim is reproducibility.

[MAJOR] Section VI / Ωa calculation: the spectator classification uses an approximate onset-of-oscillation prescription, fixed H0, ΛCDM background, and potential-dominated approximation in a regime where m ∼ H0–100H0 and θi can be O(1); a full per-sample EOM/backreaction treatment is required before claiming spectator safety.

[MINOR] Abstract and conclusions: the manuscript repeatedly states that none of the analyses verifies ECH, is not a sky measurement, and is not a distinctive ECH prediction, yet still uses promotional phrases such as "validated pipeline," "genuine result," and "genuine accommodation"; the presentation should be shortened and made internally consistent.

[MINOR] Data availability / archival standard: GitHub and HuggingFace links with DOI assignment "pending," deleted defective artifacts, and repository changelog provenance are not a stable archival record for PRD-level reproducibility; immutable releases with checksums and exact chain/code versions are required.

(3) The central claim is only weakly supported: the manuscript supports that limited stock-CAMB, toy NaMaster, and Gaussian-summary ALP exercises were performed, but not that these constitute a self-contained or publishable validation of ECH spin-torsion physics.
