# RBEXT P1B Grok — chat: https://grok.com/c/b4a60e0f-b752-4113-84ce-0f08105b9c36
VERDICT: MINOR REVISIONS

Provider: Grok (Expert tier)
PDF: RBEXT_P1B.pdf | md5: c85f8c7a9fac08711b6b57de0fcf6efa
Harvested: 2026-06-29

---

Referee Report: Technical Verification Companion to the ECH Spin-Torsion Program (P1B)

Recommendation: MINOR REVISIONS

This is a high-quality, technically rigorous companion paper that performs exactly the narrow verification role it claims. It is transparent, well-scoped, and unusually honest about limitations. The core analyses (ΔNeff proxy, NaMaster MC validation, spectator-ALP consistency) are competently executed and appropriately caveated. No blockers exist.

BLOCKERS: None.

MAJORS

w0wa cross-check (Sec. V.C, Table II) — presentation and emphasis
The DESI DR2 + Planck NPIPE + (DES-Y5 × Pantheon+) product-likelihood chain is presented with a full table of posterior means/widths and a "physics interpretation" paragraph, yet the paper itself states that the ∼20% shared-SN overlap introduces an uncontrolled systematic that artificially narrows the posterior and renders σ-distances or significance statements invalid. The chain also has the ΛCDM point unsampled, precluding a Savage-Dickey estimate.

Requested action: Either (a) move the entire w0wa exercise (including Table II) to an appendix labeled "exploratory / systematics-limited diagnostic – not used for any quantitative claim in the main text", or (b) remove the quantitative table and retain only a one-paragraph statement that a preliminary overlap-uncorrected run shows a quintom-B direction whose robustness requires the deferred overlap-controlled nested-sampling analysis.

Abstract and concluding framing of the ALP result
Add one explicit sentence in both the abstract and final paragraph of conclusions:
"Within the spectator-safe (Ωa < 0.01) subset the model accommodates the observed β only after a ∼25× fine-tuning of the misalignment angle relative to the natural prior midpoint and requires a photon coupling Caγ ≳ 9, well above standard KSVZ/DFSZ expectations; it therefore does not constitute positive evidence for an ALP explanation, let alone for ECH spin-torsion."

Reproducibility archival
Provide a permanent archive (Zenodo or equivalent) containing the frozen chains, Cobaya YAMLs, NaMaster driver scripts, ALP ODE integration grid, and chain summary files used to produce every number in Tables I–IV and Figs. 1–4. Add a "Data and Code Availability" subsection with the DOI.

MINORS

- Abstract length and density: The spectator caveat paragraph is necessary but could be split.
- Repetition of scope statements: Consolidate into a single box or prominently placed paragraph in the introduction.
- NaMaster section (Sec. IV): State explicitly that the unweighted χ² template fit was chosen to match the public NaMaster driver scripts used in the compared literature; inverse-variance-weighted result is diagnostic only.
- Table I caption: Move the column-permutation warning and burn-in reconciliation to a short appendix subsection.
- Minor typographical/LaTeX issues: Missing thin spaces around units, one "post erior-supported" line break artifact.

Strengths (≥3)

- Exceptional scoping and intellectual honesty. The paper repeatedly states what each analysis is not: not a direct test of the spin-torsion Boltzmann module, not a competitive sky measurement, not a distinctive ECH prediction, not a model-selection exercise. The ∼25× misalignment tuning is disclosed in the abstract and main text.
- Methodological rigor and documentation. Convergence diagnostics (R̂, ESS, burn-in reconciliation), 500-realization MC pipeline validation, explicit robustness battery (apodization scale, sky fraction, weighting scheme, BB template shape), independent re-run cross-check (c15), and one-sided limit post-processing are handled to high standard.
- Clear separation of pipeline-validation figures from sky-measurement claims. The NaMaster bias (−0.032° to −0.040°) is correctly labeled as a deconvolution-algebra bias on foreground-free synthetic skies, never conflated with published 2.7–2.9σ sky detections.
- Appropriate use of a stock Boltzmann solver for a proxy test. The ΛCDM+ΔNeff run tests only whether current data prefer an extra radiation-like degree of freedom; it does not verify any torsion-modified Boltzmann module.

Summary: P1B is a solid, technically sound verification companion. Principal weaknesses are presentational (over-emphasis on a systematics-limited w0wa chain and slightly diffuse ALP fine-tuning verdict framing), not methodological. Recommend MINOR REVISIONS.
