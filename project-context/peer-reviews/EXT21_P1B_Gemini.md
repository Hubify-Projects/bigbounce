# EXT21 P1B Gemini — chat: https://gemini.google.com/u/1/app/1291796a89f15e90

Recommendation: MINOR REVISIONS

General Comments

This manuscript provides a meticulous technical verification layer for an underlying cosmological framework, detailing three main numerical validation tracks: a stock-CAMB ΛCDM+ΔNeff MCMC proxy exploration, a pseudo-Cl pipeline validation using NaMaster, and a spectator Axion-Like Particle (ALP) cosmic birefringence consistency check.

The paper is exceptionally transparent, rigorously documenting pipeline biases, tuning limitations, and dataset systematic limits that are frequently minimized in broader cosmological literature. The commitment to open science—exemplified by deterministic seeds, archived Hugging Face datasets, and explicit validation scripts—is exemplary and sets a high bar for reproducibility. The manuscript is well within the scope of MNRAS regarding data methods and cosmological pipeline verification. However, a few key methodological assumptions and framing points require clarification before publication.

Major Comments

1. SN Catalog Overlap and Product Likelihood Treatment

In the w0wa cross-check (Section V.C), the author couples the DES-SN5YR and Pantheon+ catalogs via a naive product likelihood without a joint covariance matrix. The text notes that because these catalogs share approximately 20% of their supernova events with different Malmquist-bias corrections, this treatment double-weights the overlapping data and introduces an artificial inward pull toward the combined mean.

While the author candidly declares this as a known limitation and makes no definitive model-selection claims, presenting marginalized posterior-tail distances of +4.3σ in w0 and −3.6σ in wa under an uncorrected product likelihood is statistically fragile.

Action Required: The author mentions that two SN-overlap control chains (DESI DR2 + Planck NPIPE + Pantheon+ only; and DESI DR2 + Planck NPIPE + DES-SN5YR only) were performed to evaluate robustness. The quantitative results or contours of these control chains should be briefly summarized in Section V.C or added as an appendix figure. This will allow the reader to verify that the qualitative direction of the trajectory (phantom crossing, w0+wa<−1) is genuinely robust against the shared-event systematic.

2. Framing and Nomenclature of the ECH Connection

The manuscript is titled as a companion to the Einstein-Cartan-Holst (ECH) spin-torsion program. However, the modules executed are entirely standard general relativity (GR) toolkits: stock CAMB with a generic radiation proxy (ΔNeff) and a standard GR+ALP Lagrangian. The author explicitly reminds the reader throughout the text that these runs do not solve torsion-modified Boltzmann equations and that the birefringence signal is not a distinctive ECH prediction.

While this candor is refreshing, the structural layout creates a slight narrative disconnect. A casual reader looking at the title and abstract might expect a novel modified gravity pipeline, rather than a standard GR baseline validation meant to map out a no-go parameter space.

Action Required: The author should slightly re-frame the introduction and abstract to explicitly clarify that this paper establishes the standard cosmological boundaries and pipeline validation benchmarks against which the phenomenological assertions of minimal ECH scenarios are checked.

3. ALP Fine-Tuning and Constraints

The spectator ALP consistency check (Section VI) yields a highly valuable null result: accommodating the published Eskilt & Komatsu joint WMAP+Planck cosmic birefringence signal (β=0.342°±0.094°) moves the posterior mass away from the natural prior envelope (m~H0) to a regime where m≫H0 (median m≃36H0). Furthermore, restricting the model to a true spectator state (Ωa<0.01) demands a ~25× fine-tuning of the initial misalignment angle (θi~0.1).

Action Required: This tuning requirement and the demand for non-minimal photon coupling parameters (Caγ~8–10, exceeding standard KSVZ/DFSZ benchmarks) are crucial takeaways. They show that the model accommodates rather than naturally predicts the signal. This conclusion should be clearly highlighted in the Abstract so that the paper's main physical insight is scannable at a glance.

Minor and Technical Comments

NaMaster Pipeline Recovery Bias: In Section IV, the pipeline shows a stable ~12% multiplicative under-recovery of the injected rotation angle (β̂=0.238° recovered from βinj=0.27°). The robustness battery successfully isolates the culprit as the equal weighting of noise-dominated high-l bins in the unweighted χ² template fit. While maintaining an unweighted fit is logical for direct comparison with published public drivers, a brief sentence should be added to remind future pipeline builders of the exact performance trade-off compared to the inverse-variance weighted alternative.

Column-Permutation Bug Disclosure: The author transparently notes in Section V.A that an earlier export of parameter_summary.json suffered from an off-by-one column-index bug, which was corrected in parameter_summary_CORRECTED.json. Please verify that all text figures and table values within this manuscript have been strictly mapped out from the corrected file.

Typographical Units: Ensure all instances of Hubble parameters match standard astrophysical formatting (e.g., km s−1 Mpc−1 with appropriate spacing) consistently throughout the text and tables.
