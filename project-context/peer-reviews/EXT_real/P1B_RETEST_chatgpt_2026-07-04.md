# P1B RETEST — ChatGPT — 2026-07-04

- reviewer: ChatGPT
- model: ChatGPT Pro (Pro Extended thinking) — 'Thought for 4m 54s'
- timestamp: 2026-07-04T07:38Z
- chat_url: https://chatgpt.com/c/6a48b698-4294-83e8-93de-c81d38144ec8
- pdf: /tmp/ext_retest_P1B.pdf (P1B v1B.0.98)
- prompt: standard PRD referee prompt (VERDICT/ISSUES/central-claim)
- note: LaTeX math rendered by ChatGPT as split token lines; preserved verbatim.

## RAW RESPONSE (verbatim)

(1) VERDICT: REJECT. 

ext_retest_P1B

(2) ISSUES:

[MAJOR] Abstract/Secs. I, VII — The manuscript repeatedly states that none of its three analyses tests or verifies the ECH spin-torsion sector, that the ALP result is not ECH-specific, and that model preference is deferred; this leaves no PRD-level central physics result, only a collection of auxiliary checks.

[MAJOR] Sec. III A — The identification of the ECH four-fermion torsion energy density with an “ECH-sector contribution to ∆Neff” is not justified: the term scales as a
−6
, not radiation, so a stock-CAMB constant-N
eff
	​

 posterior is not an observational envelope on that component.

[MAJOR] Sec. III A — The estimate ρ
tor
	​

∼G
N
	​

T
6
 is presented as a first-principles prediction without a controlled thermal expectation value of the axial-current operator, spin correlations, sign, numerical coefficient, species sum, or treatment of finite-temperature renormalization; the claimed ΔN
eff
ECH
	​

∼10
−44
 is therefore only a dimensional estimate.

[MAJOR] Secs. III/V — The MCMC run is a stock ΛCDM+ΔN
eff
	​

 fit and not a torsion-modified Boltzmann calculation; it cannot test the ECH sector, and the manuscript’s attempt to recast the null ΔN
eff
	​

 result as support for the ECH expectation overstates what the calculation can establish.

[MAJOR] Sec. V — The section is titled “Cosmological Fits and Model Comparison,” but no model comparison is actually performed: no baseline ΛCDM evidence, no Bayes factor, no ΔAIC/ΔBIC, and no nested sampling are reported. A PRD submission cannot advertise model comparison and then defer it.

[MAJOR] Secs. II/V and Table II — The “full-tension” chain includes SH0ES and DES-Y3 information as active likelihoods and then discusses residual Hubble/S8 tensions inside the same combined posterior; this is not a clean independent tension statistic and should not be used as an evidential statement about resolving or failing to resolve tensions without a proper dataset-split analysis.

[MAJOR] Sec. IV — The NaMaster exercise is not a validation of a cosmic-birefringence measurement: the simulations omit galactic foregrounds, instrumental miscalibration α, beam effects, anisotropic/1/f noise, realistic bandpasses, map-level systematics, and the foreground mechanism that breaks the α-β degeneracy.

[MAJOR] Sec. IV/Fig. 3 — The quoted 0.040
∘
 “systematic floor” is not a systematics bound; it is an estimator-dependent bias in a foreground-free synthetic test with an unweighted χ
2
 fit, and the manuscript itself reports that inverse-variance weighting removes most of it.

[MAJOR] Sec. IV — The pseudo-C
ℓ
	​

 validation uses a semi-analytic EE spectrum and an ad hoc C
ℓ
BB
	​

=0.05C
ℓ
EE
	​

 prescription, then attributes residual bias partly to BB-shape effects; this is not a robust validation against the actual sky or against the published Planck/ACT pipelines.

[MAJOR] Sec. VI — The ALP MCMC fits a single Gaussian summary datum for β with flexible nuisance parameters; agreement of β
ALP
	​

, β
free
	​

, and β
obs
	​

 is therefore built into the likelihood and has essentially no independent confirmatory content.

[MAJOR] Sec. VI/Table IV — The “prior-predictive accommodation cost” is dominated by arbitrary prior choices on C
aγ
	​

, θ
i
	​

, and m; the manuscript draws interpretive conclusions from percentages that are not prior-invariant and hence are not physical evidence for non-tautological accommodation.

[MAJOR] Sec. VI — The spectator-ALP interpretation is internally strained: the posterior-supported mass is m≫H
0
	​

, the safe spectator subset is a small post-hoc fraction of the chain, and the required coupling is non-minimal; this should be presented as a tuned phenomenological fit, not as a meaningful consistency result of the ECH program.

[MAJOR] Secs. I/VII and Refs. [1], [6]–[8] — The manuscript relies heavily on concurrently posted, same-author companion papers for the claimed ECH no-go framework, surviving f
NL
	​

 prediction, SPHEREx forecast, anomaly catalog, and galaxy-chirality context; the present paper is not self-contained enough for independent refereeing.

[MINOR] Secs. IV/VI — The PR3/PR4/NPIPE/WMAP/Planck labeling is confusing: the paper alternates between the published Eskilt-Komatsu PR3+WMAP9 result, repository PR4/NPIPE language, Planck NPIPE values, and ACT DR6 values. The adopted likelihood and provenance should be stated once and used consistently.

[MINOR] Throughout — The manuscript is excessively defensive and implementation-log-like, with artifact paths, version stamps, sample-count reconciliations, and caveats embedded in the main text; this obscures the scientific argument and is not appropriate for a PRD article in its current form.

[MINOR] Tables/Figures — Table numbering and cross-references are inconsistent in places, and several captions contain interpretive claims that should be in the text or removed.

[MINOR] Appendix/Data availability — DOI assignment is pending and the reproducibility record depends on mutable repository and HuggingFace locations; archival, immutable artifacts would be required before any reproducibility claim could be relied upon.

(3) The evidence supports only the narrow statement that the restricted calculations are compatible with null ΔN
eff
	​

, synthetic-pipeline recovery, and a tuned ALP fit; it does not support an ECH-specific central claim.

---
NOTE (orchestrator): 'Thought for 4m 54s'. Split-token lines are ChatGPT's inline LaTeX math ($a^{-6}$, $\rho_{tor}\sim G_N T^6$, $\Delta N_{eff}^{ECH}\sim 10^{-44}$). 

COMPARISON TO RS24 §III.A DIMENSIONAL BUG: In RS24 the §III.A four-fermion finding was a CONCRETE dimensional error (fixed here via the κ→κ² convention, v1B.0.98). In THIS response ChatGPT NO LONGER flags a dimensional inconsistency: it now reads the ρ_tor ~ G_N T^6 scaling and the a^{-6} redshift dependence as internally consistent, calling ΔN_eff^(ECH) ~ 10^{-44} "only a dimensional estimate." Its two residual §III.A [MAJOR]s are physics-SCOPE/rigor objections — (1) a stock constant-N_eff CAMB posterior is not an observational envelope on an a^{-6} (non-radiation) component, and (2) the estimate lacks a controlled first-principles thermal-average derivation (axial-current expectation value, spin correlations, numerical coefficient). These are NOT the RS24 dimensional bug. The κ² fix LIFTED the concrete dimensional finding; ChatGPT's overall verdict remains REJECT on scope/no-central-result grounds (structural harsh-referee floor, per standing directive H).
