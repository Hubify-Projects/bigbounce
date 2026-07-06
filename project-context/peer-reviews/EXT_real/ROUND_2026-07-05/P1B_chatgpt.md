# EXT Review — P1B × ChatGPT
- paper: P1B
- version: v1B.0.99
- reviewer: ChatGPT
- model: Pro Extended
- timestamp: 2026-07-06T19:15:38Z
- chat_url: https://chatgpt.com/c/6a4bfd88-1d68-83e8-8c92-99ba7a780807
- pdf: /tmp/round_P1B.pdf

## Raw verbatim response

(1) VERDICT: REJECT

(2) ISSUES:

[MAJOR] Abstract/Introduction—The manuscript’s advertised connection to the ECH spin-torsion program is not supported by the analyses actually performed: it explicitly states that none of the three analyses implements or tests a torsion-modified theory module and that they are only adjacent null/compatibility checks, leaving the paper without a standalone PRD-level physics result. 

round_P1B

 

round_P1B

[MAJOR] Introduction/“Imported theory results”—The load-bearing ECH claims are imported from a concurrent Paper I(a), while this paper does not reproduce the derivations of the structural barriers, perturbation-transparency theorem, or surviving bounce prediction; this makes the submission non-standalone and unsuitable as an independent article in its present form. 

round_P1B

 

round_P1B

[MAJOR] Secs. III and V/ΛCDM+∆Neff proxy—The MCMC analysis is only a standard stock-CAMB ΛCDM+Neff run and, by the manuscript’s own statement, does not solve torsion-modified Boltzmann equations or verify the spin-torsion sector; therefore it cannot be used as evidence for, or a meaningful constraint on, ECH beyond the trivial statement that a negligible contribution is allowed. 

round_P1B

[MAJOR] Sec. III A/ECH-sector ∆Neff estimate—The claimed “first-principles” estimate is too heuristic for PRD: the replacement ⟨(ψγ5γµψ)²⟩T ∼ n²f is asserted without a controlled finite-temperature calculation, spin/axial-current contractions, sign/equation-of-state treatment, flavor factors, or renormalization discussion, yet it is used to reframe the entire MCMC exercise. 

round_P1B

[MAJOR] Sec. III A/Eq. (3)—The numerical values quoted for ∆N(ECH)eff use the unreduced Planck mass scale while the manuscript defines MPl as the reduced Planck mass: with MPl = 2.44 × 10¹⁸ GeV, (1 MeV/MPl)² ≈ 1.7 × 10⁻⁴³, not 7 × 10⁻⁴⁵, and (0.26 eV/MPl)² ≈ 1.1 × 10⁻⁵⁶, not 5 × 10⁻⁵⁸; the qualitative negligibility survives, but the central quantitative derivation is internally inconsistent. 

round_P1B

[MAJOR] Sec. IV/NaMaster validation—The CMB E/B analysis is not a realistic birefringence measurement: it uses synthetic foreground-free CMB-only skies, no beam, white isotropic noise, simplified spectra, and explicitly lacks the unrotated foreground information needed to break the β–α degeneracy, so it cannot support any real-sky systematic or detection claim. 

round_P1B

 

round_P1B

[MAJOR] Sec. IV/estimator bias—The canonical estimator has a measured ∼12% multiplicative under-recovery and a worst-case −0.040° bias, while the manuscript admits that inverse-variance weighting removes about 80% of this bias; retaining the knowingly biased unweighted estimator for comparability is not a sufficient methodological justification for a PRD analysis. 

round_P1B

 

round_P1B

[MAJOR] Sec. VI/ALP MCMC—The ALP posterior agreement with βobs is essentially circular because the likelihood is a Gaussian summary centered on the same published βobs value; the manuscript acknowledges this, but then still presents posterior agreement as a consistency result rather than only a prior-volume exercise. 

round_P1B

 

round_P1B

[MAJOR] Sec. VI/spectator-ALP interpretation—The “spectator” interpretation is not robust: only 13% of the posterior mass satisfies Ωa < 0.01, the strict θi ≤ 0.1 sliver has only 0.33% weighted mass, and the coupling required in that sliver piles toward the upper prior edge, so the viable spectator region is tuned and poorly sampled. 

round_P1B

[MAJOR] Sec. VI/ECH distinctiveness—The manuscript concedes that the same birefringence arises in standard GR with the same ALP and that minimal ECH does not derive the required photon-torsion coupling; thus the ALP section is not evidence for ECH and should not be presented as part of an ECH spin-torsion program except as an unrelated phenomenological aside. 

round_P1B

[MAJOR] Sec. V/“Model Comparison”—The section title promises cosmological fits and model comparison, but Bayes factors, AIC/BIC, and nested-sampling evidence are explicitly deferred; no model-preference inference is actually performed, despite the topic being central to whether the extra parameters or ALP accommodation have explanatory value. 

round_P1B

[MINOR] Data and Code Availability/Appendix A—For a paper whose main contribution is reproducibility, the repository state is not archival enough: DOI assignment is pending, the text relies on mutable GitHub/HuggingFace locations, and it describes deleted/corrected artifacts and column-permutation bugs rather than providing a clean permanent review package. 

round_P1B

[MINOR] Presentation/abstract and scope statements—The manuscript is dominated by caveats, cross-paper bookkeeping, artifact reconciliation, and program-wide material not used in this paper, which obscures the actual scientific content and should be moved to supplementary material or omitted.

(3) The evidence presented supports only the narrow claim that three limited, non-ECH-specific checks are internally compatible with null or literature-summary results; it does not support an ECH-specific physical claim.
