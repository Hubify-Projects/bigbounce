# EXTDB P2 Gemini — chat: https://gemini.google.com/u/0/app/3de6c937a93eeee0

Provider: Gemini
Model/Tier: 3.5 Flash (fast)
PDF: /tmp/EXTDB_P2.pdf
Submitted: 2026-06-27
Harvested: 2026-06-27
Round: EXTDB (DE-BIASED, R57 PDFs)

---

1. Recommendation
MAJOR REVISIONS

The manuscript provides an exceptionally thorough and sophisticated analysis, recasting galaxy survey sensitivities to test a clean, well-motivated non-Gaussian signal (fNL_local = −35/8) predicted by quasi-dust matter-bounce cosmologies. The paper distinguishes itself via highly detailed cross-checks, rigorous operator-algebra clarifications regarding the historical factor-of-two discrepancy with Li et al., and a comprehensive treatment of standard cosmological systematics. However, major revisions are required prior to publication.

2. Blockers (Crucial Issues)

BLOCKER 1 — Overlap Scaling and Boundary Excess Inconsistency:
In Section III.B, the author establishes that the local-template amplitude recovery factor is r = 0.84 ± 0.02 across noise-weighting schemes, yet the full untruncated 10,000-sample polynomial null-space scan yields r = 0.85 ± 0.13, with a range stretching up to r = 1.14. The author justifies retaining values where r > 1 because the squeezed limit is not the global maximum of BNL for those specific polynomial combinations. However, this introduces an unmitigated accounting conflict. Throughout the text, the baseline degradation of survey sensitivity is defined via σ_eff = σ(fNL)/r. If a null-space sample yields r = 1.14, the effective parameter uncertainty would artificially shrink below the optimal local-template baseline limit — a local template estimator cannot mathematically capture more than 100% of a signal that contains non-local configurations without introducing severe estimator mismatch variance.
Resolution Required: Either strictly truncate the null-space scan to physical constraints where r ≤ 1, or explicitly re-derive the estimator variance under a joint template cross-Fisher matrix to account for the leaked non-local power rather than using simplified 1/r linear scaling across the entire un-truncated distribution.

BLOCKER 2 — Systematic Quad-Additive Formulation vs. Joint Marginalization:
The headline "realistic" significance range (~2.6–5σ) is constructed by adding individual systematic budgets additively in quadrature. This is a heuristic check rather than a self-consistent cosmological forecast derivation. Nuisance parameters like linear galaxy bias b1 and the PNG bias bϕ are highly degenerate with fNL over large scales. In realistic galaxy survey pipelines, joint marginalization over non-linear bias and relativistic projections can drastically warp or tighten individual constraints depending on the sign of the covariance.
Resolution Required: Explicitly temper headline claims in the Abstract and Conclusion, clarifying that the headline constraints rely on a quadrature-stacking heuristic rather than a full joint multi-tracer covariance matrix derivation.

3. Majors

M1 — Scale-Dependent Bias Redshift Bin Disconnect:
The joint Fisher forecast for (fNL, n_fNL) uses six redshift bins spanning z = 0.1–1.5, while the foundational SPHEREx multi-tracer bispectrum baseline from Heinrich et al. (2024) targets emission-line galaxy population spanning z ≈ 0.5–2. The paper combines two completely different survey tracer distributions and redshift ranges for a singular unified complementary mapping.
Resolution Required: Harmonize the theoretical survey descriptions or include an explicit technical note mapping how a joint survey program would coordinate these distinct tracer boundaries without double-counting cross-correlations between the overlapping volumes (z = 0.5–1.5).

4. Minors

m1 — Abstract Headline vs. Table II Bookkeeping Discrepancy:
The abstract headlines BF ≈ 9–14, while Table II shows BF ~ 10 and BF ~ 17. The text explains that Table II preserves the r → 1 bookkeeping endpoint while the abstract actively applies noise-weighted r ≈ 0.84 rebooking — but headlining the more favorable numbers in primary data tables while promoting downgraded numbers in the abstract creates unforced legibility friction.
Resolution Required: Update Table II to show both the r → 1 limits and the explicit noise-weighted r = 0.84 rebooked columns side-by-side.

m2 — Shot-Noise Caveat Scope Framing:
Section IV includes an alternative multi-tracer strategy using anomaly-detected QSO and emission-line galaxy candidates with a 3.3× shot-noise inflation for low-density tracers (n̄ ~ 10⁻⁵ h³Mpc⁻³). While the headline 2.6–5σ significance does not rely on these anomaly tracers, including an uncalibrated, highly shot-noise-dominated speculative channel shifts the focus away from the core robust bispectrum analysis.
Resolution Required: Condense the anomaly tracer discussion or move quantitative Poisson scaling calculations to an appendix.

5. Strengths

S1. Definitive Normalization Audit — The resolution of the historical factor-of-two discrepancy between Cai et al. and Li et al. is exceptionally rigorous. Using symbolic in-in operator identities (i⟨[ζ³,L]⟩ = −2 Im⟨ζ³L⟩), the author definitively demonstrates that the halving stems from a single time-ordering intermediate rather than an alternative physical bispectrum branch.

S2. Thorough Template Mismatch Validation — Template projection mapped across 10 physically motivated noise-weighting schemes, tested across log grids up to 1.5 million triangles, and verified across 10,000-sample polynomial null-space scan. Shape cosine (r_cos > 0.97) resilience well established.

S3. Exceptional Technical Transparency — Admirable honesty regarding the limits of the framework: explicitly designates the study as a "sensitivity recast," meticulously flags the unverified status of third-order bounce transmission coefficients (Assumption d), and openly hosts all verification data packages via an accessible public repository.
