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
