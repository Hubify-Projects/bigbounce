# EXTDB2 P1B Gemini — chat: https://gemini.google.com/u/0/app/51ccd47a75973156

Provider: Gemini Flash
PDF md5: dbf1d9d374f4923fd33c7e30cbd36ad5
Harvested: 2026-06-28

---

Referee Report
Manuscript Title: Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+Neff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
Author: Houston Golden (Independent Researcher)
Date of Review: June 28, 2026

1. Recommendation
MAJOR REVISIONS

Justification: This companion manuscript presents a solid and reproducible technical evaluation suite supporting a wider cosmological program. The work displays an admirable commitment to open science, providing deterministic seeds, public code repositories, and hosted MCMC chain data. However, the manuscript currently contains several critical methodological vulnerabilities, unstated assumptions, and presentation strategies that over-inflate physical results or mask systematic limitations. Notably: (1) combining the overlapping DES-SN5YR and Pantheon+ catalogs through a naive product likelihood artificially compresses the parameter errors, generating a >4σ tail displacement from ΛCDM that does not reflect robust observational reality; (2) the ALP alignment fine-tuning and non-minimal photon couplings are minimized or selectively partitioned in text summaries to preserve a more favorable "consistency" headline.

2. Blockers

BLOCKER 1 — Artificially Compressed w0wa Likelihood and Extrapolated Significances: In Section V (and Table II), the author combines the DES-SN5YR and Pantheon+ supernova datasets using a direct product likelihood without a joint cross-covariance matrix. Because these catalogs share ~20% of their event samples, this approach double-counts these common supernovae, introducing an unquantified inward pull on the errors and narrow constraints. The resulting +4.3σ departure in w0 and −3.6σ departure in wa from ΛCDM are explicitly flagged as inflated marginal-tail extrapolation distances on an unsampled model point. Headlining these figures in a companion paper without providing the independent control chains or a rigorous joint covariance is a major blocker.
Resolution: The author must either replace this product likelihood with a valid joint covariance structure or re-center the Section V narrative entirely around the separate control chains (e.g., DESI DR2 + Planck + Pantheon+ only) to state correct, un-inflated statistical deviations.

3. Majors

Major 1 — Axion Alignment Fine-Tuning and Selective Subsection Filtering: The cosmic birefringence analysis claims that the spectator ALP model safely accommodates the observed Eskilt-Komatsu joint WMAP+Planck signal (β=0.342°±0.094°). However, Section VI and Table IV reveal that maintaining the ALP as a subdominant spectator field (Ωa<0.01) requires compressing the initial misalignment angle down to the sub-natural sliver θi~0.1. This is an explicit ~25× fine-tuning against the natural flat-prior midpoint (θi~0.5). Only 13% of the broad posterior mass sits within this spectator-safe corridor. The headline conclusion downplays this structural fine-tuning burden.
Resolution: The abstract, Section VI, and conclusions must be harmonized to clearly state that the model requires independent fine-tuning on both the misalignment initial condition (~25×) and a non-minimal photon coupling (Caγ≈8–10, outside the standard KSVZ/DFSZ O(1) benchmarks).

Major 2 — Invalid Usage of Savage-Dickey Density Ratio Estimates: The text notes that a Savage-Dickey density ratio readout at the ΛCDM point (w0,wa)=(−1,0) fails because the Metropolis-Hastings chain left the point completely unsampled. Yet the manuscript heavily relies on marginalized-tail Gaussian posterior-extrapolation distances (+4.3σ and −3.6σ) to claim compatibility with a quintom-B scenario. Reporting extrapolated tail distances as proxy "compatibility measures" when the under-sampled KDE estimator breaks down is statistically inconsistent.
Resolution: Remove the specific σ-tail exclusion distances from Table II and text headlines. Rely strictly on a qualitative statement regarding the posterior mean trajectory until the deferred nested-sampling evidence (lnB) is calculated.

4. Minors

Minor 1 — Fixed Background Hubble Rate Systematic in Ωa Calculation: During the MCMC evaluation of the ALP parameter space, the derived axion energy fraction Ωa relies on a fixed background Hubble rate (H0=67.68 km/s/Mpc) evaluated at the Cobaya mean, rather than marginalizing over the full Planck 1σ interval. While the author asserts this induces a sub-dominant ~3% shift on Ωa, this constitutes an uncontrolled approximation systematic in the chain post-processing.
Resolution: Explicitly document this fixed-background parameter limitation within the caption of Table IV.

Minor 2 — Multiplicative Under-Recovery of NaMaster Pipeline: Section IV reports a ~12% multiplicative under-recovery bias (Δβ̂=−0.032° to −0.040°) across the pseudo-Cl pipeline validation suite. While properly carried forward empirically as a pipeline systematic floor, the bias source (unweighted template fit's equal treatment of noise-dominated high-l bins) should be mentioned in the Abstract.
Resolution: Add a sentence to the Abstract clarifying that the pseudo-Cl validation demonstrates a stable, sky-fraction-independent multiplicative under-recovery of ~12% driven by the canonical baseline estimator choice.

Minor 3 — Structural Mangle of Text Units: On page 1, under analysis (1), the text prints "(67.68±1.06 full-tension; 67.78±1.09 Planck+BAO+SN, both in kms−1Mpc−1 the ΔNeff extension..." — missing a closing parenthesis and proper text spacing for standard velocity-distance units.
Resolution: Fix the typo and convert the text to standard LaTeX math block formatting for units.

5. Strengths

1. Exemplary Open-Science and Reproducibility Infrastructure: The inclusion of an explicit reproducibility manifest in Appendix A, complete with active Hugging Face dataset repositories for frozen chains, deterministic seeds (seed_base=42), and execution scripts (reproduce_cosmology.sh), sets a phenomenal standard for cosmological simulation reporting.

2. Honest Disclosure of Data Limits and Software Bugs: The author highlights a critical off-by-one column-index bug in the legacy parameter_summary.json file, warning users to implement the parameter_summary_CORRECTED.json artifact. This level of documentation is rare and highly commendable.

3. Methodological Rigor via Likelihood Robustness Sweeps: The implementation of the c15 execution block as an independent compute pod rerun — substituting planck_2020_lollipop.lowlE and planckpr4lensing to bound pairing-induced code bias — demonstrates exceptional vigilance in verifying Boltzmann code configurations.
