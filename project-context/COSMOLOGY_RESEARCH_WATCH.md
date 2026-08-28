# Cosmology Research Watch

**Owner:** Houston Golden  
**Purpose:** Maintain a weekly, source-backed research watch for the BigBounce cosmology program and the Hubify research workflow.

## Scope

Prioritize worthwhile new papers, data releases, catalogs, methods papers, and substantive technical analyses relevant to:

1. DESI and SPHEREx survey cosmology, including BAO, redshift-space distortions, cross-correlations, calibration/systematics, and forecast-to-data transitions.
2. Galaxy chirality, handedness, spin asymmetry, parity-odd statistics, and observational or instrumental explanations for apparent asymmetries.
3. Dark-energy closure: consistency tests, equation-of-state constraints, modified gravity, tensions between probes, and what would close or falsify the current interpretation.
4. Primordial non-Gaussianity: bispectrum/trispectrum estimators, scale-dependent bias, multi-tracer methods, survey forecasts, and constraints.
5. Multi-survey anomalies: DESI/CMB/weak lensing/SNe/galaxy clustering tensions, shared systematics, look-elsewhere effects, null tests, and independent replications.

## Weekly brief contract

Each Friday, produce a concise shortlist rather than a news dump. Prefer roughly 3–7 items, ranked by practical importance. For every item include:

- Title, authors/collaboration, date, and direct link.
- Type: paper, data release, catalog, code/method, or substantive analysis.
- One-sentence result or contribution.
- Why it matters to the BigBounce program.
- What could change our interpretation, including the strongest caveat or known systematics.
- **Read first:** the exact section, figure, table, abstract, or companion artifact to open first.
- A priority label: **Read now**, **Track**, or **Skip unless relevant**.

Include a short closing section:

- **Top item to read first**
- **What changed this week**
- **Implications for current papers/experiments**
- **Open follow-up questions**

## Evidence and ranking rules

- Search the newest credible material since the prior brief, while resurfacing older work only when it materially changes interpretation.
- Prefer primary sources: arXiv papers, journal versions, DESI/SPHEREx collaboration releases, NASA/ESA/IPAC data documentation, official catalogs, and reproducible code/data repositories.
- Separate observation from interpretation. Explicitly distinguish detection, consistency result, forecast, null result, replication, and speculation.
- Do not treat a preprint, press release, or social-media claim as established evidence.
- Flag whether a result is independent of the BigBounce team’s work or potentially overlaps with it.
- Watch for duplicate papers, revised arXiv versions, conference abstracts without technical detail, and results that rely on unvalidated systematics.
- For anomalies, always check: sample selection, survey footprint, pipeline version, calibration, masking, covariance assumptions, multiple-testing/trial factors, and independent replication.
- For chirality/spin claims, always check classifier bias, handedness-label conventions, imaging artifacts, selection effects, redshift dependence, and north/south or survey-split null tests.
- For dark energy and non-Gaussianity, note parameter priors, model dependence, nuisance marginalization, scale cuts, tracer overlap, and whether the result is forecast or measured.
- Link each item to the relevant existing BigBounce paper, status note, task, or experiment when that relationship is clear.

## Durable archive

Append each delivered brief under a dated heading in this file, keeping the newest entries easy to find. Do not overwrite earlier briefs. Keep the archive concise: preserve the shortlist and decisions, not a full literature review.

## Project relationship

- BigBounce is the primary cosmology research and paper context.
- Hubify is the research-agent, review-loop, and reproducibility context.
- The weekly brief should inform paper triage, anomaly catalogs, chirality work, survey-data priorities, and review tasks without silently changing scientific claims or project plans.
- Any proposed change to a paper’s claim, analysis, or priority must be marked as a proposal for Houston to review.


---

## Ad hoc brief — 2026-08-24

### 1. Read now — DESI DR2 Lyα full-shape Alcock–Paczynski analysis

**[DESI DR2 Results IV](https://arxiv.org/abs/2607.27410)** · DESI Collaboration · 2026-07-29  
**Type:** Primary collaboration paper / new DR2 analysis.

DESI’s full-shape Lyα auto- and quasar-cross-correlation analysis reaches about 1% AP precision at z_eff = 2.33. Relative to the earlier Lyα BAO-only result, the central value shifts toward ΛCDM; the DESI+CMB preference for w0waCDM is 2.7σ, or 3.2σ with supernovae, and the DESI–CMB discrepancy is reduced from 2.4σ to 2.2σ.

**Why it matters:** This is the most important new result for the program’s dark-energy-closure and multi-survey-anomaly framing. It argues against treating the DESI evolving-dark-energy hint as a single monotonic signal across all tracers.

**Caveat:** The result still depends on Lyα full-shape modeling, fiducial-cosmology/AP treatment, nuisance parameters, and external-data choices. It is not a decisive ΛCDM confirmation.

**Read first:** Abstract; Sec. IV (validation); Fig. 7; Sec. VI.4 (extended models); then the DESI release summary [here](https://www.desi.lbl.gov/2026/07/30/new-desi-dr2-lyman-alpha-results-shed-light-on-dark-energy).

### 2. Read now — DESI DR2 chains and cosmology products

**[DESI DR2 cosmology chains and data products](https://www.desi.lbl.gov/2025/10/06/desi-dr2-cosmology-chains-and-data-products-released/)** · DESI · 2025–2026  
**Type:** Official data/product release.

DESI has released cosmology MCMC chains and posterior-maximization products for DR2, while the underlying DR2 spectra and redshifts are not yet public. The July 2026 Lyα release also provides 400 realistic validation mocks and supporting holography/modeling products.

**Why it matters:** This is the most actionable reproducibility input for BigBounce’s anomaly catalog, dark-energy closure, and future independent checks. It is also exactly the sort of immutable input/provenance layer Hubify should preserve.

**Caveat:** Chains are not equivalent to the complete raw survey release; independent re-analysis remains limited until spectra/redshifts and all relevant likelihood components are public.

**Read first:** The official release page’s product inventory, then the [DESI DR2 paper index](https://data.desi.lbl.gov/doc/papers/dr2/).

### 3. Read now — DESI DR1 quasar local PNG with assembly-bias prior

**[Assembly bias and local primordial non-Gaussianity from DESI DR1 quasars](https://arxiv.org/abs/2602.12357)** · Fondi et al. · 2026-02-12  
**Type:** DESI analysis plus simulation-calibrated nuisance prior.

Using IllustrisTNG and CAMELS to constrain the quasar assembly-bias response, the authors obtain f_NL = -3.3 ± 9.2 for DESI DR1 quasars.

**Why it matters:** It provides a concrete current benchmark for how DESI-scale PNG inference depends on the b_phi/assembly-bias prior. That is directly relevant to how BigBounce presents its primordial non-Gaussianity result: as a model-conditioned, reproducible constraint rather than a free-standing detection.

**Caveat:** The result is prior-sensitive; the mapping from halo assembly history to observed quasar selection remains an astrophysical modeling dependency.

**Read first:** Sec. 3 (simulation/prior construction), Sec. 4 (DESI likelihood), and the final constraint table.

### 4. Read now — HSC DR2 spin-parity null test

**[Spin Parity of Spiral Galaxies VI](https://arxiv.org/abs/2605.05570)** · Iye & Yagi · 2026-05-07  
**Type:** Independent galaxy-spin/chirality analysis.

The study analyzes 49,494 S/Z-annotated spirals across 46,247 3D search volumes and finds the observed spin-parity distributions consistent with random assignments and Monte Carlo expectations.

**Why it matters:** This is a valuable external null result for BigBounce P4/P5. It supports presenting any chirality asymmetry as a carefully bounded, survey- and estimator-specific signal requiring classifier, footprint, and selection controls—not as established cosmic handedness.

**Caveat:** It is not a direct replication of the DESI classifier/catalog or estimator, so agreement in the null does not settle cross-survey systematics.

**Read first:** Abstract; the S/Z labeling and volume construction; the CDF/Monte Carlo comparison; and the anomalous-volume count table.

### 5. Track — parity-odd galaxy shapes as a primordial PNG probe

**[Parity violation in galaxy shapes: Primordial non-Gaussianity](https://journals.aps.org/prd/abstract/10.1103/fxh6-hpmk)** · Kurita, Jamieson, Komatsu & Schmidt · PRD 2026  
**Type:** Theory/EFT + DESI/LSST forecast.

The paper develops a parity-odd intrinsic-alignment observable sensitive to the collapsed limit of a parity-odd primordial trispectrum and forecasts improved sensitivity from combining galaxy shapes with other probes.

**Why it matters:** It connects the galaxy-spin/chirality and primordial-PNG programs at the level of parity-odd observables and suggests a future cross-survey extension.

**Caveat:** The observable depends on undetermined EFT/bias parameters and is a forecast, not a detection in DESI or SPHEREx.

**Read first:** Abstract; the EFT operator/bias parameter section; and the DESI+LSST forecast figure.

### 6. Track — SPHEREx QR2 calibration and weekly data stream

**[SPHEREx Quick Release overview](https://irsa.ipac.caltech.edu/data/SPHEREx/docs/overview_qr.html)** · NASA/IPAC  
**Type:** Official data-release documentation.

SPHEREx is releasing spectral images weekly. QR2 replaced QR1 with substantially improved calibration; QR1 is retired, and April 2026 header updates corrected PSF-extension metadata issues.

**Why it matters:** This is the practical data-readiness watch for the SPHEREx side of the program and a reminder to pin calibration/reprocessing versions in any future PNG or cross-survey analysis.

**Caveat:** This is not yet a new public SPHEREx cosmology catalog or constraint, so it should not change current manuscript claims.

**Read first:** QR2 overview, calibration/reprocessing notes, and the current data explorer.

### What changed this week

The most consequential change is DESI’s DR2 Lyα full-shape result: it strengthens the high-redshift expansion anchor but moves the central value toward ΛCDM and slightly reduces the DESI–CMB discrepancy. The current evidence favors a more conditional, dataset-combination-specific dark-energy narrative.

### Implications for BigBounce

- Do not reopen P2/P4/P5 science solely because of these papers.
- Update the publication briefing to cite DESI DR2 Lyα as a live external context and explicitly distinguish BAO-only from full-shape evidence.
- Treat the HSC spin-parity paper as an external null/control reference for chirality framing.
- Use the DESI quasar PNG paper as a nuisance-prior benchmark when describing the scope and limitations of P2.
- Prioritize Houston’s bounded visual review and submission decisions over another broad review cycle.

### Implications for Hubify

Preserve DESI chains, SPHEREx calibration versions, mock catalogs, likelihood metadata, and paper-to-artifact links as immutable research inputs. The current Hubify MVP does not need a new research-missions feature to support this; a durable provenance/archive workflow is the higher-value next step.

### Top item to read first

DESI DR2 Results IV, especially the abstract, validation section, Fig. 7, and extended-model section.


---

## Weekly brief — 2026-08-28

Screened new primary material from 2026-08-24 through 2026-08-28. Items marked “resurfaced” predate the window but materially sharpen interpretation. No new credible direct galaxy-handedness detection surfaced this week.

### 1. Read now — Sequentially-Valid Reanalysis of DESI’s Dynamical Dark-Energy Signal (resurfaced)

**[Paper](https://arxiv.org/abs/2607.28918)** · Jinyoung Kim, David F. Mota & Andrius Tamosiunas · v2: 2026-08-19  
**Type:** Independent statistical reanalysis/method paper; not a new observation.

Using e-processes/e-values to account for repeated looks across DESI releases, the default running e-value reaches 33.97 at DR2, but leave-one-out evidence is concentrated in LRG2 (z_eff = 0.706): removing that bin reduces it to 0.49, while adding compressed Planck reduces it to 2.19.

**Why it matters:** This is the strongest current audit of whether the evolving-dark-energy significance survives sequential analysis, bin influence, and CMB combination; it directly informs BigBounce’s dark-energy-closure and anomaly framing.

**Strongest caveat:** The result is prior- and likelihood-dependent; the exact sequential guarantee assumes a year-scaling/nesting model, and the authors do not provide a canonical sigma conversion.

**Read first:** §4.1 and Fig. 3; Table 1; §5 Discussion/Conclusions; Appendix B.2 (martingale verification) and Appendix B.7 (BAO+CMB).

### 2. Read now — ACT DR6 Constraints on Anisotropic Screening and Birefringence

**[Paper](https://arxiv.org/abs/2608.27458)** · Darby M. Kramer et al. / ACT DR6 analysis · 2026-08-27  
**Type:** Primary CMB data analysis / parity and null test.

ACT DR6 finds no significant anisotropic-screening or cosmic-birefringence detection: baseline A_tau = 180 ± 157 with A_tau < 450 (95%), and A_CB = 0.05 ± 0.06 with A_CB < 0.15 (95%); one-frequency foreground evidence is consistent with extragalactic simulations.

**Why it matters:** It is a fresh external parity control for BigBounce P4/P5 and multi-survey-anomaly work; it provides no positive CMB parity evidence that would justify changing current claims.

**Strongest caveat:** Baseline results use science-grade dr6.01 rather than public dr6.02; foreground systematics are comparable to statistical error for screening, and birefringence depends strongly on the global-angle mean-field and ell_min choices.

**Read first:** §VI.1, Figs. 10–11 and Table 2 (screening); §VI.2, Figs. 12 and 14 (birefringence); §VII.1–VII.2 (systematics); §IX.

### 3. Read now — The Impact of the IGM Thermal State on the Lyα Flux 3D Power Spectrum

**[Paper](https://arxiv.org/abs/2608.24784)** · Tomáš Šoltinský, Gabriele Autieri, Vid Iršič & Matteo Viel · 2026-08-25  
**Type:** Hydrodynamic simulation/systematics paper relevant to DESI Lyα.

Across Sherwood/Sherwood-Relics simulations, inadequate optical-depth grid resolution can change small-scale power by up to about 35%, mass-resolution effects reach about 13%, photoheating changes large-scale power by about 4–8%, and numerical effects can match or exceed relic-astrophysics signatures.

**Why it matters:** It is a direct systematics control on the high-redshift DESI Lyα anchor used in dark-energy closure; it supports requiring convergence evidence before interpreting Lyα differences as new physics.

**Strongest caveat:** This is not a DESI measurement or a recalibrated DR2 likelihood; transfer to the DESI analysis depends on nonlinear modeling, thermal history, and nuisance implementation.

**Read first:** §4.2 (mass resolution); §4.4 (grid coarseness); Fig. 2; Fig. 16; §6; Appendices B–C.

### 4. Read now — Derivative Hierarchy as the Origin of Kernel-Dependent Trends in GP Reconstructions of H(z)

**[Paper](https://arxiv.org/abs/2608.26774)** · Afaq Maqsood · 2026-08-27  
**Type:** Gaussian-process methods/systematics paper.

Using CC32 and DESI DR2 BAO, smoother kernels produce systematically lower H0 and different H′(0): for example, Matérn 7/2 gives H0 = 68.8 ± 5.2, while the squared-exponential kernel gives 67.2 ± 4.8; the hierarchy is stable under jackknife but is a smoothness-prior effect.

**Why it matters:** Any BigBounce nonparametric H(z), derivative, or dark-energy argument should treat kernel robustness as a required systematic check; a GP crossing is not automatically model-free.

**Strongest caveat:** Kernel and hyperparameter priors, CC32 calibration/selection, and derivative amplification remain model dependencies; descriptive fit behavior is not evidence that one kernel is physically correct.

**Read first:** §III–§III.1; Figs. 3–4; Table 1; §IV.

### 5. Track — Spectral Map Making with SPHEREx, v2

**[Paper](https://arxiv.org/abs/2603.25790)** · Ari J. Cukierman et al. / SPHEREx team · v2: 2026-08-24  
**Type:** Primary mission map-making/data-readiness paper; ApJS 286, 22 (2026).

The pipeline produces preliminary 102-channel, 0.75–5 μm spectral cubes from roughly the first quarter of the mission; interpolation broadens the effective PSF by about 2.2× versus about 1.6× for binning, with some channels limited by detector-gain and long-wavelength noise.

**Why it matters:** It identifies the map-maker, PSF, masking, calibration, and foreground-provenance fields that must be version-pinned before BigBounce attempts SPHEREx PNG or cross-survey anomaly tests.

**Strongest caveat:** This is an early-data methods paper, not a cosmological catalog or constraint; source masking and foreground filtering may suppress or reshape signals, and the data are not yet full-mission.

**Read first:** §III and Fig. 4; §IV.5 and Fig. 8; §V.1 and Figs. 11–12; §VII.

### 6. Track — Assembly Bias from Nuisance to Probe II

**[Paper](https://arxiv.org/abs/2608.26262)** · Nelson Padilla, Dante Paz & Ivan Lacerna · 2026-08-26  
**Type:** DESI/SDSS observational and simulation-methods analysis.

Compensated conformity statistics from DESI BGS and SDSS MGS suppress nonlinear-clustering contributions and retain a more linear-matter-like shape, with an effective-mode gain of roughly 2.9×–4.4× in their tests.

**Why it matters:** It is a possible future assembly-bias/systematics cross-check for large-scale clustering and Ωm trends, and it is relevant to nuisance modeling in PNG analyses.

**Strongest caveat:** The paper is not a calibrated precision-cosmology measurement; results vary across MTNG, FLAMINGO, and MDPL2-SAG, and the exploratory Ωm fits are restricted one-parameter shape fits with survey-tuned mocks/covariances.

**Read first:** §3.1 and §3.3; §5.2–§5.4; Figs. 4, 7 and 8; §6.

### 7. Track — Probing Primordial Chirality in the Matter Distribution (resurfaced)

**[Paper](https://arxiv.org/abs/2607.26612)** · Fang-Na Shao, Hao-Ran Yu, Ming-Jie Sheng, Bing-Hang Chen & Huiyuan Wang · 2026-07-29  
**Type:** Helicity-estimator method plus simulation and SDSS/ELUCID null test.

The injected helical simulations retain a parity-asymmetric signal to late times, but the reconstructed SDSS/ELUCID local-universe analysis finds no coherent significant detection; localized ≈3σ features are not replicated as a robust signal.

**Why it matters:** This is the most directly relevant external method/null control for BigBounce P4: it reinforces that chirality conclusions must be classifier-, estimator-, reconstruction-, and survey-specific until independently replicated.

**Strongest caveat:** The injected signal is phenomenological, while the reconstruction imposes strong Gaussian/power-spectrum assumptions that may suppress real parity-odd structure; it is not a direct replication of the BigBounce catalog/classifier.

**Read first:** Abstract; Fig. 1 (estimator/simulation validation); Fig. 2 (SDSS/ELUCID result); the observational-examination section; Conclusion.

### 8. Skip unless relevant — PNG from tSZ–ISW Cross-Correlation

**[Paper](https://arxiv.org/abs/2608.25809)** · Ayodeji Ibitoye, Yin-Zhe Ma & Prabhakar Tiwari · 2026-08-26  
**Type:** New cross-correlation PNG analysis.

An unconstrained fiducial fit reports a large negative f_NL, but imposing the physical alpha_inj ≥ 0 condition gives f_NL = 86 ± 73, only about 1.2σ from zero; adding a Planck f_NL prior yields −1.4 ± 5.0 and is not an independent measurement.

**Why it matters:** It is a useful false-positive warning for BigBounce anomaly triage: apparent PNG significance can be driven by astrophysical energy-injection and scale-dependence degeneracies.

**Strongest caveat:** The result is highly model/prior dependent, with tSZ/CIB/energy-injection systematics and a strong f_NL–n_NL degeneracy; it is not a robust independent PNG detection.

**Read first:** Table 1; Appendix C; §IV summary.

### What changed this week

The newest material is mostly interpretive control rather than a new cosmological discovery: ACT DR6 adds a parity null, Lyα simulations quantify potentially large numerical/thermal systematics, GP work shows derivative/kernel prior sensitivity, and DESI/SDSS assembly-bias work offers a future nuisance cross-check. The tSZ–ISW paper is a cautionary apparent-PNG signal that collapses under a physical prior. No new direct galaxy-chirality measurement was found in the screened Aug. 24–28 material.

### Implications for current papers and experiments

- **Proposed for Houston’s review — no claim changed:** Add the sequential-look/LRG2 sensitivity result to the dark-energy-closure discussion and phrase DESI dynamical-dark-energy evidence as dataset-, prior-, and release-conditional.
- **Proposed for Houston’s review — no claim changed:** Add Lyα thermal/grid convergence and GP-kernel dependence to the systematic-risk checklist; do not promote either into a new physical explanation.
- Keep P4/P5 chirality language bounded to the measured classifier/estimator and retain HSC and Shao et al. as independent null/control context; no claim of cosmic handedness is strengthened.
- For P2, use the DESI/SDSS assembly-bias result as a future nuisance-model benchmark; do not treat it as a PNG detection or calibrated Ωm measurement.
- For SPHEREx work, freeze the map-maker version, PSF convention, masking/foreground choices, detector-gain/header fixes, and provenance before any cross-survey anomaly or PNG comparison.
- ACT DR6 is an external parity control only; it does not justify changing current BigBounce priorities.

### Top item to read first

Read the sequentially-valid DESI reanalysis first: §4.1/Fig. 3, Table 1, and Appendix B.7. It most directly tests whether the current evolving-dark-energy narrative survives repeated looks, influential bins, and CMB combination.

### Open follow-up questions

1. Can BigBounce reproduce the LRG2 leave-one-out result using the released DESI products and the exact prior/likelihood choices?
2. Should P2 report PNG constraints across multiple assembly-bias priors and explicitly separate measured constraints from simulation-calibrated nuisance assumptions?
3. Can P4 pass classifier swaps, handedness-label reversals, north/south and survey splits, redshift stratification, and an independent catalog/reconstruction?
4. Which SPHEREx QR2/map-maker/PSF and foreground version will be frozen as the reproducibility baseline?
5. Should the dark-energy papers present DESI Lyα BAO-only, Lyα full-shape, and lower-redshift full-shape/bispectrum results as separate evidence channels rather than one combined narrative?
