# EXTDB2 P2 Gemini — chat: https://gemini.google.com/u/0/app/66d335cf3319eed5

Provider: Gemini Flash
PDF md5: 1da0518fa79894dfd68bbed7f93efc75
Harvested: 2026-06-28

---

1. Recommendation
MAJOR REVISIONS

Justification: The manuscript addresses a highly compelling and timely topic but is fundamentally structured as a sensitivity recast rather than an independent cross-Fisher matrix forecast. Because it inherits its baseline sensitivities from a single baseline study (Heinrich et al. 2024), several statistical and methodological shortcuts have been introduced. The manuscript cannot be accepted until the authors clear multiple severe presentation blockers, resolve an internal presentation asymmetry between text headlines and raw tabular endpoints, and better justify their heuristic handling of correlated systematics.

2. BLOCKERS

Blocker 1 — Asymmetrical Tabular Rebooking vs. Headline Discrepancy: There is an acute, systemic framing inconsistency between the abstract/prose headlines and the technical tables. The text quotes headline BF≈9–14 based on noise-weighted r≈0.84 template-mismatch correction applied to effective uncertainty. Yet Table II and Table III explicitly report the r→1 (no-rebooking) endpoints (BF≈10–17). The authors state they apply a "bookkeeping rebooking" σ_eff=σ(fNL_local)/r to generate text headlines from table entries. Technical tables must display the actual physical values corresponding directly to promoted headlines — not relying on readers to mentally map text conversions onto static raw values. Tables must be fully overhauled to transparently present the noise-weighted r=0.84 baseline entries prominently.

Blocker 2 — Uncontrolled Higher-Redshift Systematics for MegaMapper: The manuscript extends its recast to a speculative Stage-V survey, MegaMapper, quoting a wide detection envelope of 3–7σ. However, the text explicitly confesses that the systematic budget (σ_GR relativistic projection scale and b_φ uncertainty) has not been independently calibrated to MegaMapper's higher-redshift (z=2–5) sensitivities, where relativistic projection effects and lensing magnification are orders of magnitude more severe. Presenting a quantitative headline estimate for a future facility while using a frozen low-redshift systematic proxy represents an uncontrolled calculation.

3. MAJORS

Major 1 — Heuristic Additive Quadrature vs. Joint Fisher Contradiction: Throughout the text, the systematic budget is compiled via additive quadrature (σ_eff = sqrt(σ_base^2 + Σσ_i^2)). In Section VII and the SDB joint Fisher analysis, the authors state that co-marginalizing the linear biases and running index n_fNL actually loosens the SDB constraint by 2.0x to 4.6x due to steep anti-correlations (ρ=−0.87 to −0.97). This explicitly demonstrates that the additive-quadrature heuristic leaves out severe parameter space degeneracies. The choice to use an un-marginalized heuristic as the baseline headline metric over a self-consistent joint Fisher covariance requires a much more robust mathematical defense.

4. MINORS

Minor 1 — Fermion Torsion Scaling Omission: The matter-bounce prediction of fNL=−35/8 is conditional on Assumption (f): that fermion energy density during contraction is negligible, preventing dim-6 four-fermion contact term from activating torsion. The text states that "a rigorous order-of-magnitude bound on the threshold ρ_fermion/ρ_scalar... is not undertaken here." Given how heavily the paradigm-rejection claim relies on this decoupling, a basic analytical toy scaling or literature-derived upper limit on ρ_fermion must be supplied to bound this systematic.

Minor 2 — Exclusion Arithmetic Framing: The prose repeatedly emphasizes that "the exclusion arithmetic is symmetric." The authors must insert a brief caveat clarifying that this symmetry assumes the true universe resides precisely at fNL≈0 with identical covariance properties, as Fisher matrices evaluated at varying fiducial points can structurally shift.

Minor 3 — Mangled Character Rendering: Several typographical extractions from PDF processing (e.g., "5.2-5.50" instead of 5.2–5.5σ, "2.6-50" instead of 2.6–5σ, "vis finite" instead of ν is finite). Should be cleaned up for typesetting consistency.

5. Strengths

1. Rigorous Operator-Algebra Resolution of Literature Discrepancy: The explicit symbolic audit in Appendix A.1 utilizing the in-in operator identity i⟨[ζ3,Hint]⟩=−2Im⟨ζ3Hint⟩ definitively solves the factor-of-two divergence between Cai et al. (−35/8) and Li et al. (−35/16). Proving that the latter was simply an incomplete single time-ordering intermediate significantly clarifies the theoretical baseline.

2. Comprehensive Template Mismatch Quantifications: The exhaustive analysis tracking amplitude recovery factor r across 10 distinct physically motivated noise-weighting schemes — validated through logarithmic grids, 200 independent flat-sky injection-recovery realizations, and 10,000-sample null-space polynomial scan — provides exceptional transparency.

3. Excellent Public Reproducibility Standards: The inclusion of distinct named JSON structures, validation check scripts, and dedicated repositories (appendix_A1_wick_doubling.py, c9g_bf_table_recompute.py) archived via Zenodo sets an exemplary standard for computational cosmology pipelines.
