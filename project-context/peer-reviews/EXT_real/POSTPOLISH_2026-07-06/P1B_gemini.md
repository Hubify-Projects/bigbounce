# EXT POSTPOLISH 2026-07-06 — P1B — Gemini

- **Provider:** Gemini (houston@bamf.com, Ultra, /u/1/)
- **Model/effort:** 3.5 Thinking
- **Chat URL:** https://gemini.google.com/u/1/app/744449189a60872e
- **PDF:** P1B_v1B.0.102.pdf (md5 ddaf880631a9c063a0f87b3dad17bd33)
- **Harvested:** 2026-07-07
- **Parsed verdict (from response):** MAJOR REVISIONS
- **Note:** verdict rendered as "VERDICTMAJOR REVISIONS" (no colon) in the DOM.

## Raw verbatim response

VERDICT: MAJOR REVISIONS
ISSUES:

[MAJOR] Section I & VII (Standalone Publication Merits): The manuscript is framed strictly as a "Technical Reproducibility and Consistency-Check Companion Note" to a concurrently submitted "Paper I(a)". Given that the numerical core relies entirely on stock CAMB without implementing custom torsion-modified Boltzmann equations, and does not offer a new cosmological sky measurement, the manuscript lacks sufficient independent physical or methodological novelty to justify a standalone publication in Physical Review D. The author should consider consolidating this material directly into Paper I(a) as an appendix or an integrated section.

[MAJOR] Section IV (Realism of Pipeline Validation): The NaMaster pseudo-Cl validation uses idealized, foreground-free synthetic skies. Because separating the cosmic rotation angle β from the instrumental miscalibration angle α requires unrotated galactic foregrounds to break their mathematical degeneracy, evaluating the pipeline without modeling these components or beam-mismatch effects severely diminishes the utility of the derived systematic bias budget (Δβ̂ ∼ −0.040°) for practical CMB applications.

[MINOR] Section III.A (Approximation in Torsion Density Derivation): The evaluation of the contributed energy density ρtor ∼ GN·T^6 relies on a parametric estimate where O(1) coefficients are dropped rather than a rigorous Nambu–Jona-Lasinio finite-temperature calculation. A more mathematically precise justification or formal boundary verification is required to anchor the definitive claim of ΔNeff(ECH) ∼ 10^−44.

[MINOR] Section VI (Incomplete Parameter Marginalization): In computing the derived ALP energy fraction Ωa for spectator-status classification across the posterior chain, the Hubble rate H0 is held fixed at the Cobaya posterior mean (67.68 km s−1 Mpc−1) rather than being dynamically marginalized. A fully self-consistent Bayesian framework requires propagating the active H0 uncertainty at each MCMC step, rather than substituting a post-processing mean approximation.

[MINOR] Section V & Appendix A (Journal Prose Formalism): The text explicitly documents repository-level debugging history, such as an off-by-one column-index bug in a deleted parameter_summary.json file. While GitHub changelog transparency is excellent practice, detailed accounts of expunged or permuted file structures belong in repository documentation rather than formal journal prose.

The central claim that the minimal Einstein-Cartan-Holst spin-torsion sector yields a strictly negligible, Planck-suppressed radiation-era contribution (ΔNeff(ECH) ∼ 10^−44) is structurally supported by the analytic first-principles derivation, though the accompanying MCMC analyses function as standard baseline null tests rather than independent observational evidence for the underlying gravitation theory.
