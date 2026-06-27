# EXT21 P5 Gemini — chat: https://gemini.google.com/u/1/app/edbc99c934c610c2

Recommendation: MINOR REVISIONS

General Assessment

This manuscript investigates the large-scale structure environment dependence of spiral galaxy chirality (clockwise vs. counterclockwise handedness). By leveraging an extensive catalog of 8,474,531 galaxies cross-matched with the DESI Data Release 1 spectroscopic redshift catalog, the author evaluates chirality fractions across voids, walls, filaments, and clusters.

The primary path utilizes a robust, three-algorithm DESIVAST void catalog, while a secondary cross-check implements a standard tidal-tensor cosmic-web classifier (T-Web). The overarching conclusion is a clean null result: spiral galaxy chirality displays no statistically significant dependence on its environmental framework once the catalog-wide classifier-monopole systematic (≈−0.26 pp) is explicitly subtracted.

The paper is exceptionally thorough, statistically sound, and commendably transparent regarding its data pipeline and reproducibility metrics. It warrants publication in MNRAS after addressing a few minor points and clarifications outlined below.

Key Strengths

- Methodological Rigor and Robustness Checks: The author does not rely on a single environmental metric. The analysis gracefully balances the deterministic T-Web classifier with a large-scale, multi-algorithm void cross-validation via DESIVAST (encompassing VoidFinder, V2-REVOLVER, and V2-VIDE), an independent SDSS DR10 Friends-of-Friends group catalog (Tempel et al. 2014), and the probabilistic ASTRA EDR environment catalog.

- Statistical Handling: The explicit propagation of classifier-monopole uncertainties, use of Jeffreys binomial credible intervals, look-elsewhere corrections (both parametric Bonferroni and empirical max-stat Monte Carlo nulls), and multi-bin checks reflect top-tier statistical discipline.

- Open Science and Reproducibility: Providing detailed directory maps, exact configuration files (config.yaml), fixed random seeds (20260515), and versioned GitHub manuscript tags makes this work remarkably reproducible and sets a high standard for independent researchers.

Comments and Revisions for the Author

1. Dependency on "Paper IV" (In Preparation)

The manuscript heavily ingests coordinates, labels, and global monopole predictions from Golden (in preparation), designated as Paper IV. Because Paper IV serves as the empirical bedrock for the catalog's systematic corrections, any modification to its pipeline could ripple into this work. The author should add a brief comment in Section II addressing how stable the current version (v1.0.166) is and clarifying if any subsequent shifts in Paper IV's final publication could structurally alter the propagated error bounds reported here.

2. Deconstructing Target-Program Non-Orthogonality

In Section VI.D, a two-way contingency test reveals a strong non-independence between T-Web classes and the DESI bright/dark target selection program (χ² = 4933, p ≪ 10⁻³⁰⁰).

While the primary DESIVAST path successfully immunizes the headline result by isolating the volume-limited z ≤ 0.24 BGS sample, the underlying filament sign-flip residual remains an intriguing feature.

The author notes that future Rubin/LSST + DESI DR2 data will amplify the cluster-restricted dark sample by a factor of 5. Expanding slightly on how this future sample will definitively untangle selection-function effects from minor astrophysical signals would heighten the impact of the Discussion section.

3. Redshift-Space Distortion (RSD) Caveats

The author acknowledges that the analysis is fundamentally a redshift-space statement. An elegant analytic bounding method estimates that the maximum class-flip boundary population under RSD is limited to ~3–5% (~2–4×10⁴ galaxies). However, because full quantification requires a formal real-space reconstruction (e.g., Zel'dovich or BAO reconstruction) which is deferred to future work, this limitation should be highlighted more transparently. It is suggested that the author explicitly append a sentence regarding the fixed-redshift-space constraint to both the Abstract and the final Conclusions section to ensure reader clarity.

4. Interpretation of Appendix A (Toy EFT Mapping)

The effective field theory mapping outlined in Appendix A is a valuable addition for theoretical model-builders. However, as the author rightfully notes, the toy operator breaks rotational invariance via the coordinate unit vector z-hat and lacks manifest gauge invariance. To prevent future literature from treating this schematic formulation as a rigid physical constraint, the author should slightly sharpen the wording in the opening of Appendix A, explicitly stating that it functions as an illustrative, slicing-dependent parameterization rather than a robust, covariant EFT bound.

5. Minor Typographical Clarification

In Section IV.A, step 5, the notation [Rs/cell] + 1 = 2 is used for the canonical dilation iteration count. For clarity, please write out the exact cell size (25.9 Mpc/h) or explicitly phrase it as a ceiling function ⌈Rs/cell⌉ + 1 directly within the text block, matching the notation deployed later in Section VII.
