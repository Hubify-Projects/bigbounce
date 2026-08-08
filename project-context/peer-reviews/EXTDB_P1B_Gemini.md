# EXTDB P1B Gemini — chat: https://gemini.google.com/u/0/app/9e627a013241bfdb

Provider: Gemini
Model/Tier: Flash (regular)
PDF: /tmp/EXTDB_P1B.pdf
Submitted: 2026-06-27
Harvested: 2026-06-27
Round: EXTDB (DE-BIASED)

---

Referee Report (MNRAS / PRD / JCAP)

1. Recommendation
MINOR REVISIONS

2. Summary of the Work
This paper presents the technical verification layer and numerical consistency cross-checks supporting a structural-closure no-go program for Einstein-Cartan-Holst (ECH) spin-torsion dark energy scenarios. The author documents three distinct components: a stock-CAMB ΛCDM+ΔNeff MCMC proxy analysis; a NaMaster pseudo-Cl pipeline recovery validation exploring isotropic cosmic birefringence on synthetic CMB polarization skies; and an ultra-light axion-like particle (ALP) field-evolution consistency check evaluating literature claims of cosmic birefringence.

3. BLOCKERS
None. The manuscript is highly rigorous, explicitly self-aware of its scope limitations, and provides strong reproducibility manifests alongside archived public data products.

4. MAJORS

M1 — Overlap-Uncorrected Supernova Systematics Reporting.
In Section V and Section III, the w0wa trajectory shifts heavily into the phantom-crossing region (w0 = −0.8122 ± 0.0436, wa = −0.666 ± 0.1864). However, this configuration naively multiplies the DES-SN5YR and Pantheon+ likelihoods without accounting for a ~20% shared-event overlap, double-weighting these events.
Finding: The abstract presents the headline results as generic compatibility checks, but the main text relies heavily on "marginal-tail posterior-extrapolation distances" (+4.3σ in w0, −3.6σ in wa) where standard ΛCDM is completely unsampled.
Required Action: Include a clear warning in the abstract or the main text's headline results specifying that this apparent departure from ΛCDM is an uncorrected product-likelihood artifact. It should be framed strictly as an exploratory, illustrative exercise rather than highlighting the inflated σ-distances in isolation.

5. MINORS

m1 — Clarify ΔNeff One-Sided vs. Two-Sided Reporting Context.
The manuscript switches between quoting a two-sided mean consistent with zero (e.g., −0.020 ± 0.169 full-tension) and a post-processed one-sided upper bound (ΔNeff < 0.31). While footnote 1 clarifies the conservative sample-truncation post-processing method, explicitly mentioning in Section III why the physical boundary constraint changes the upper bound will prevent reader confusion.

m2 — Explicitly Flag Column-Permutation Export Bug in Text.
The text guides readers to extract values from parameter_summary_CORRECTED.json rather than the legacy parameter_summary.json due to an off-by-one column indexing bug. To safeguard future meta-analyses, this hardware/pipeline data-level discrepancy should be explicitly mirrored in the caption of Table I to avoid any accidental legacy extractions.

6. Strengths

1. Exceptional Reproducibility Standard: The inclusion of an explicit implementation map (IMPLEMENTATION_MAP.md), exact deterministic random seeds, and archived Hugging Face repositories containing converged chains sets a gold standard for technical cosmology notes.
2. Transparent Fine-Tuning Disclosure: The author meticulously demonstrates that a spectator ALP scenario requires an acute ~25× fine-tuning of the initial misalignment condition (θi ~ 0.1) to satisfy Ωa < 0.01, avoiding the temptation to oversell the model's naturalness.
3. Pipeline Scope Clarity: The NaMaster mock-sky pipeline validation explicitly emphasizes that its template-fit SNR of 20.32 is an indicator of algebraic recovery on foreground-free synthetic skies, not a claims expansion of the physical real-sky significance.
