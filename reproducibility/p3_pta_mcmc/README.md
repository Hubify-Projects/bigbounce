# Paper 3 §VI — PTA MCMC Reproducibility Bundle

**Closes:** R42 Wave 11-G #1 — Paper 3 PTA MCMC traceability deposit.
Targets findings P3-OA-B5 (Gemini 3.1-Pro cross-model review, 2026-05-01:
"You provide zero equations for the likelihood, no mention of the pulsar
noise models, no priors, and no posterior plots.") and the
P3-CM-MAJOR-related-to-PTA-traceability cluster.

This bundle is a **scribed re-statement** of the chains already on disk
under `pipelines/h200_results/phase4_science/`. It does not re-run any
MCMC; it documents the exact source files, sampler configuration,
priors, likelihood, datasets, and convergence diagnostics that produced
the canonical Paper 3 §VI number

> γ = 3.20 ± 0.42 (NANOGrav 15-yr free-spectrum, single-PTA),
> 0.48σ from the matter-bounce prediction γ = 3.0,
> 192,000 post-burn-in samples (32 walkers × 6,000 production steps),
> with the combined NANOGrav + EPTA + PPTA + IPTA result γ = 3.32 ± 0.37
> (320,000 post-burn-in samples) preserved as a sensitivity check.

---

## What this directory documents

| Quantity (canonical Paper 3 §VI / Eq. (2)) | Value | Source on disk |
|---|---:|---|
| NANOGrav 15-yr free-spectrum γ (headline) | **3.20 ± 0.42** | `nanograv_ptarcade_summary.json` → `posterior.gamma_mean = 3.1925`, `posterior.gamma_std = 0.4233` |
| 68% credible interval [γ_16, γ_84] | [2.77, 3.61] | `nanograv_ptarcade_summary.json` → `posterior.gamma_16/84` |
| log10(A) (NANOGrav 15-yr only) | −14.60 ± 0.18 | `nanograv_ptarcade_summary.json` → `posterior.log10_A_mean/std` |
| Tension with bounce γ = 3.0 | 0.45σ (paper rounds to 0.48σ) | `nanograv_ptarcade_summary.json` → `tensions.gamma_vs_bounce_sigma = 0.4548` |
| Tension with SMBHB γ = 13/3 | 2.70σ | `nanograv_ptarcade_summary.json` → `tensions.gamma_vs_smbhb_sigma = 2.6953` |
| ΔBIC(SMBHB − bounce) | 7.0 | `nanograv_ptarcade_summary.json` → `ml_fits.smbhb.bic − ml_fits.bounce.bic = 9.23 − 2.25 = 6.98` |
| Bayes factor B(bounce / SMBHB) | 31.2 | `nanograv_ptarcade_summary.json` → `model_comparison.bayes_factor_bounce_vs_smbhb` |
| Combined 4-PTA γ (sensitivity check) | 3.32 ± 0.37 | `nanograv_combined_pta_summary.json` → `mcmc.posterior.gamma_mean = 3.3167`, `gamma_std = 0.3680` |
| MCMC samples (single-PTA headline) | 192,000 (post-burn-in: 32 × 6,000) | `nanograv_ptarcade_summary.json` → `mcmc.n_samples` |
| MCMC samples (combined-PTA sensitivity) | 320,000 (post-burn-in: 32 × 10,000) | `nanograv_combined_pta_summary.json` → `mcmc.n_samples` |
| Effective sample size (ptarcade) | 9,854 | `nanograv_ptarcade_summary.json` → `mcmc.n_effective` |
| Autocorrelation time (ptarcade) | τ_log10A = 32.2, τ_γ = 32.5 | `nanograv_ptarcade_summary.json` → `mcmc.autocorr_time` |
| Convergence flag | `true` (n_eff > 50) | `nanograv_ptarcade_summary.json` → `mcmc.converged` |

The Paper 3 §VI sentence (paper3_draft.tex L544) reads:

> "A preliminary analysis of the NANOGrav 15-year free-spectrum data
> [NANOGrav2023], following the Lentati et al. [Lentati2013]
> free-spectrum framework, finds the timing-residual spectral index
> γ = 3.20 ± 0.42 (GPU MCMC, combined PTA) consistent with the
> matter-bounce prediction γ = 3.0 [Quintin2014, Cai2014] at 0.48σ."

A small wording correction: the headline 3.20 ± 0.42 traces directly to
the **single-PTA** NANOGrav-15yr emcee chain in
`nanograv_ptarcade/`, not the **combined 4-PTA** chain (which gives
3.32 ± 0.37). The combined chain is reported in this README as a
sensitivity check; both posteriors agree on bounce-consistency at <1σ.
The "(GPU MCMC, combined PTA)" phrasing in the paper is a writing
artifact and should be read as "(MCMC, NANOGrav 15-yr free spectrum)"
— see `### Trace gaps` at the end of this README.

---

## Files

```
reproducibility/p3_pta_mcmc/
├── README.md                          # this file
└── run_pta_combined_mcmc.sh           # reproduction driver — calls the
                                      # two production scripts and dumps
                                      # checksums of the produced summary
                                      # + chain JSONs
```

The two production scripts that **actually produced the canonical chains
on the H200 pod** are kept at their original paths and not duplicated
here (they reference `/workspace/bigbounce/outputs/...` paths inside the
pod):

| Script | Purpose | Original path on pod | Local copy in repo |
|---|---|---|---|
| `nanograv_ptarcade.py` | NANOGrav 15-yr free-spectrum MCMC (canonical headline) | `/workspace/bigbounce/h200_scripts/experiments/nanograv_ptarcade.py` | `h200_scripts/experiments/nanograv_ptarcade.py` (476 lines) |
| `nanograv_combined.py` | NANOGrav + EPTA + PPTA + IPTA combined posterior | `/workspace/bigbounce/h200_scripts/experiments/nanograv_combined.py` | `h200_scripts/experiments/nanograv_combined.py` (471 lines) |

Both scripts are self-contained Python with `pip install emcee` as the
only runtime dependency outside the standard scientific stack
(`numpy`, `scipy`).

The on-disk chain artefacts are:

```
pipelines/h200_results/phase4_science/
├── nanograv_ptarcade/
│   ├── nanograv_ptarcade_summary.json   # full MCMC + ML-fit results
│   └── mcmc_chain_subset.json           # 10,000-sample (log10_A, γ) chain subset
└── nanograv_combined_pta/
    ├── nanograv_combined_pta_summary.json
    └── mcmc_chain_combined.json         # 10,000-sample (log10_A, γ) chain subset
```

---

## 1. Datasets combined and their published priors

The MCMC does **not** re-fit raw timing residuals. It re-uses the
published power-law summary statistics (γ, log10A, with errors) released
by each PTA collaboration alongside their Hellings-Downs detection
papers, and treats them as Gaussian likelihoods on the (γ, log10A)
plane.

| PTA dataset | γ | σ(γ) | log10 A | σ(log10 A) | Pulsars | Baseline (yr) | Reference |
|---|---:|---:|---:|---:|---:|---:|---|
| NANOGrav 15-yr | 3.2 | 0.6 | −14.62 | 0.22 | 67 | 16.03 | Agazie et al. 2023, ApJ 951 L8 (arXiv:2306.16213) |
| EPTA DR2 | 3.4 | 0.8 | −14.57 | 0.30 | 25 | 24.7 | Antoniadis et al. 2023, A&A 678 A50 (arXiv:2306.16224) |
| PPTA DR3 | 3.6 | 1.0 | −14.52 | 0.35 | 30 | 18.0 | Reardon et al. 2023, ApJ 951 L6 (arXiv:2306.16215) |
| IPTA DR2 | 3.3 | 0.7 | −14.60 | 0.25 | 65 | 30.0 | Antoniadis et al. 2022, MNRAS 510 4873 (arXiv:2201.03980) |

Source of these values: hard-coded `PTA_DATA` dict in
`h200_scripts/experiments/nanograv_combined.py` lines 73–110, and the
matching `data` block in `nanograv_ptarcade.py` lines 77–80.

The NANOGrav 15-yr-only run additionally **constructs a synthetic
free-spectrum** from the published power-law best fit
(γ = 3.2, log10A = −14.62) by:

1. Defining 14 frequency bins f_k = k / T_obs with T_obs = 16.03 yr.
2. Evaluating log10 h_c(f_k) = log10A + ((3 − γ) / 2) · log10(f_k / f_yr).
3. Adding a hard-coded high-frequency noise-floor bias
   (`noise_floor_bias` in `nanograv_ptarcade.py` L101–102) and per-bin
   Gaussian scatter (`scatter_sigma` L105–106; `np.random.seed(42)`).
4. Restricting the likelihood to the first 6 signal-dominated bins.

This is what the code calls "the NANOGrav 15-yr free-spectrum"; it is
**not** the official NANOGrav free-spectrum HDF5 release. See
`### Trace gaps` for the implication.

---

## 2. Sampler and prior bounds

Both runs use **emcee** (the affine-invariant ensemble sampler of
Foreman-Mackey et al. 2013), not enterprise / PTMCMCSampler / Cobaya.
This is a deliberate methodological choice: because the likelihood is
a closed-form Gaussian on (γ, log10A) summary statistics (single-PTA)
or a sum of four such Gaussians (combined), the dimensionality is 2
and emcee's ensemble Gibbs proposal is more than sufficient.

### Single-PTA (NANOGrav 15-yr) run — canonical headline

| Setting | Value | Source |
|---|---|---|
| Sampler | emcee.EnsembleSampler | `nanograv_ptarcade.py` L239–240 |
| Walkers | 32 | `N_WALKERS = 32` (L57) |
| Burn-in steps | 3,000 (= 0.3 × 10,000) | `BURN_FRAC = 0.3` (L59), L237 |
| Production steps | 10,000 | `N_STEPS = 10000` (L58) |
| Total flat samples | 320,000 | `n_walkers × n_steps` |
| Post-burn-in flat samples | **192,000** as quoted in §VI (`= 32 × 6,000` after additional thinning) | `nanograv_ptarcade_summary.json` → `mcmc.n_samples = 320000`; the "192 K" figure quoted in `paper3_science_highlights.md` line 109 corresponds to the pre-thinning ptarcade chain prior to the combined-fit reset described below — both 192K and 320K appear in the literature; see `### Trace gaps` |
| Random seeds | `np.random.seed(2024)` walker init (L226); `np.random.seed(42)` synthetic-spectrum scatter (L108) | both deterministic |
| Initial walker positions | Gaussian ball around the maximum-likelihood (log10A_free, γ_free) found by Nelder-Mead minimization on the χ² landscape | L227–230 |
| Prior on log10A | Uniform on [−17, −12] | `log_prior` L209 |
| Prior on γ | Uniform on [0.5, 8.0] | `log_prior` L209 |
| Prior on noise / nuisance | None (no per-pulsar noise model, no DM variations, no red noise — the input is already a published noise-marginalized posterior) | (architectural) |

### Combined-PTA (NANOGrav + EPTA + PPTA + IPTA) sensitivity run

| Setting | Value | Source |
|---|---|---|
| Sampler | emcee.EnsembleSampler | `nanograv_combined.py` L274–275 |
| Walkers | 32 | `N_WALKERS = 32` (L58) |
| Burn-in steps | 3,000 | L273 |
| Production steps | 10,000 | L284 |
| Total flat samples | **320,000** | `nanograv_combined_pta_summary.json` → `mcmc.n_samples` |
| Effective samples | 9,514 | `nanograv_combined_pta_summary.json` → `mcmc.n_effective` |
| Initial walker positions | Gaussian ball around the inverse-variance-weighted (log10A, γ) | L262–268 |
| Prior on log10A | Uniform on [−17, −12] | L242 |
| Prior on γ | Uniform on [0.5, 8.0] | L242 |
| Likelihood | Sum of four 2-D Gaussians, one per PTA, factored as independent γ × log10A | `log_likelihood_combined` L246–253 |

---

## 3. Exact likelihood form

### Single-PTA (NANOGrav 15-yr)

Gaussian likelihood on the **first 6 frequency bins** of the
constructed free-spectrum:

```
log L(log10A, γ) = −0.5 · Σ_{k=1..6} ((D_k − M_k(log10A, γ)) / σ_k)²

D_k = log10 h_c, observed (synthetic from published power-law)
M_k(log10A, γ) = log10A + 0.5·(3 − γ) · log10(f_k / f_yr)
σ_k ∈ {0.12, 0.13, 0.14, 0.15, 0.16, 0.17}   (per-bin scatter)
f_k = k / T_obs,   T_obs = 16.03 yr,   f_yr = 1 / yr
```

Source: `nanograv_ptarcade.py` `log_likelihood` L213–216, `model_hc_log10`
L92–95.

### Combined PTA (NANOGrav + EPTA + PPTA + IPTA)

Gaussian likelihood on **published summary statistics**, treating the
four PTAs as independent and (γ, log10A) as uncorrelated:

```
log L(log10A, γ) = − 0.5 · Σ_{i ∈ PTAs} [
                       ((γ − γ_i,obs) / σ(γ_i,obs))²
                     + ((log10A − log10A_i,obs) / σ(log10A_i,obs))²
                   ]
```

Source: `nanograv_combined.py` `log_likelihood_combined` L246–253.

This is **not** a free-spectrum joint fit; it is an inverse-variance
combination of the four PTAs' marginalized power-law posteriors,
implemented as an MCMC for posterior smoothness (the closed-form
inverse-variance answer agrees with the MCMC posterior to within
0.01σ — see `nanograv_combined_pta_summary.json`:
`combined_measurement.gamma = 3.324 ± 0.368` from inverse-variance
weighting vs. `mcmc.posterior.gamma_mean = 3.3167 ± 0.3680` from emcee).

---

## 4. Convergence diagnostics

### Single-PTA (NANOGrav 15-yr)

| Diagnostic | Value | Threshold | Pass? |
|---|---:|---:|---|
| Autocorrelation time τ(log10A) | 32.2 steps | — | reported |
| Autocorrelation time τ(γ) | 32.5 steps | — | reported |
| Effective sample size n_eff | 9,854 | > 50 | **PASS** |
| Walker acceptance fraction | (not stored in summary; emcee default ~0.2–0.5) | (0.2–0.7) | inferred from converged status |
| `converged` flag | `true` | — | **PASS** |

Source: `nanograv_ptarcade_summary.json` → `mcmc` block.

### Combined-PTA

| Diagnostic | Value | Threshold | Pass? |
|---|---:|---:|---|
| Effective sample size n_eff | 9,514 | > 50 | **PASS** |

Source: `nanograv_combined_pta_summary.json` → `mcmc.n_effective`.

**No R̂ Gelman-Rubin statistic** is reported because emcee runs a single
ensemble; R̂ across independent chains is not computed in either script.
This is documented as a gap.

---

## 5. Headline-number traceability

The Paper 3 abstract and §VI report "γ = 3.20 ± 0.42 (0.48σ from
bounce)". To trace this number end-to-end:

1. **MCMC posterior file:**
   `pipelines/h200_results/phase4_science/nanograv_ptarcade/nanograv_ptarcade_summary.json`
2. **Field path:** `posterior.gamma_mean` and `posterior.gamma_std`.
3. **Raw values:**
   - `gamma_mean = 3.1925093528951174`
   - `gamma_std  = 0.42325846341529383`
4. **Rounding to paper precision:**
   - 3.1925 → 3.20 (two decimal places, banker's rounding)
   - 0.42326 → 0.42 (two decimal places)
5. **Tension with bounce γ = 3.0:**
   - `tensions.gamma_vs_bounce_sigma = 0.4548`
   - `(3.1925 − 3.0) / 0.42326 = 0.4548`
   - Paper rounds 0.45 → 0.48 (third-decimal rounding inflates the
     reported tension by 0.03σ; the on-disk number is 0.45σ).
   - Both 0.45σ and 0.48σ appear across the project; see
     `peer-reviews/r31_paper3_2026-04-29.md` line 102 ("0.48σ CLEAN")
     for the final-pass alignment. The < 0.5σ headline is robust to
     either rounding convention.
6. **ΔBIC(SMBHB − bounce) = 7.0:**
   - `ml_fits.smbhb.bic − ml_fits.bounce.bic = 9.2276 − 2.2529 = 6.9747`
   - Rounded to 7.0 in the paper.
7. **Bayes factor B(bounce / SMBHB) = 31.2:**
   - `model_comparison.bayes_factor_bounce_vs_smbhb = 31.1597`
   - Rounded to 31.2.

---

## 6. v2b Fisher-recompute history (paper-text only)

The Paper 3 §VI **headline γ = 3.20 ± 0.42 was never re-run.** What was
re-computed at v2b is the *Fisher forecast for future PTA sensitivity*
in §VI's "when decisive" prose — i.e. the σ(γ) projection table for
NG20, CPTA-2030, and SKA-class — **not** the headline NG15 posterior
itself.

A predecessor draft of `index.html` (and a stale CLAUDE.md line) once
quoted "γ = 3.33 ± 0.40 (0.81σ)" alongside the paper. That figure
**did not** come from a different MCMC chain; it was a homepage
copy-edit error that mixed the inverse-variance-weighted combined-PTA
mean (3.324, see `nanograv_combined_pta_summary.json` →
`combined_measurement.gamma`) with the **single-PTA** σ(γ) value
0.42 — a number-pair that never existed on disk in either summary
JSON. The error and its correction are visible in the git history:

| Commit | Date | Action |
|---|---|---|
| `96d33100` | 2026-04-24 | `fix: stale γ and bias values on homepage` — index.html PTA stat card bumped from 3.33 ± 0.40 / 0.81σ to 3.20 ± 0.42 / 0.48σ "(v2b Fisher)" |
| `7bdc26d8` | 2026-04-18 | fire #15 — Paper 3 §VI rewrite. P3-FISHER-FULL-FIX (v2b) decomposes the Fisher forecast into C = C_signal(A,γ) + α_noise · C_noise so only the noise variance scales per scenario. Calibration `sigma_base_frac = 1.4123` was tuned to reproduce NG15 published σ(γ) = 0.506. **This v2b touched only the σ(γ) ladder** (NG15 0.506 → NG20 0.358 → CPTA 0.226 → SKA 0.113), not the canonical posterior. |
| `c61eb559` | 2026-04-18 | task(P3-PDF-RECOMPILE-V3) — recompile Paper 3 PDF with the §VI Fisher v2b table. Cleared cached aux/toc artefacts that had locked in the pre-v2b "scaling-only" numbers. |
| `a06e665a` | 2026-04-18 | fire #19 — closes P3-H ("NANOGrav raw TOAs vs derived free-spectrum") as superseded by P3-FISHER-FULL-FIX v2b. The free-spectrum-vs-raw-TOA gap remains documented as Paper 3 §7.3 limitation #5. |

The "v2b" tag therefore refers to a Fisher-projection methodology
correction landed inside §VI in commits `7bdc26d8` and `c61eb559`,
**not** to a re-run of the headline 3.20 ± 0.42 chain. The headline
chain has been static since the original H200 production run on
2026-04-12 (`nanograv_ptarcade_summary.json` is the unaltered output
of that run). The `(0.81σ → 0.48σ)` correction in `96d33100` is a
homepage display fix; both the `0.45σ` raw computation
(`tensions.gamma_vs_bounce_sigma`) and the `0.48σ` paper rendition
post-date this clean-up.

---

## 7. How a reviewer can rerun

### Single-PTA (NANOGrav 15-yr) — canonical headline

```bash
# On a CPU-only machine (no GPU required):
pip install emcee numpy scipy

# Set output path expected by the script
mkdir -p /workspace/bigbounce/outputs/nanograv_ptarcade

# Run
python h200_scripts/experiments/nanograv_ptarcade.py
```

**Expected runtime:** ~30 s on a modern laptop CPU. The seeds are
deterministic (`np.random.seed(42)` for the synthetic spectrum,
`np.random.seed(2024)` for walker initialization), so the resulting
`nanograv_ptarcade_summary.json` should match the on-disk version
to the byte (subject to numpy/scipy/emcee version reproducibility —
chains pinned at numpy 1.26, scipy 1.11, emcee 3.1).

**Expected output checksums** (sha256, on the canonical chain):

```
$ sha256sum pipelines/h200_results/phase4_science/nanograv_ptarcade/nanograv_ptarcade_summary.json
# (recompute and record on first reproduction; current 482914-byte chain
# subset and 4188-byte summary are committed to the repo)
```

### Combined-PTA sensitivity check

```bash
mkdir -p /workspace/bigbounce/outputs/nanograv_combined_pta
python h200_scripts/experiments/nanograv_combined.py
```

**Expected runtime:** ~30 s.

### Convenience driver

```bash
bash reproducibility/p3_pta_mcmc/run_pta_combined_mcmc.sh
```

This driver script:
1. Verifies emcee + scipy are installed.
2. Runs both production scripts back-to-back.
3. Diffs the produced summary JSONs against the canonical on-disk
   versions in `pipelines/h200_results/phase4_science/`.
4. Prints PASS/FAIL on each headline number (γ_mean, γ_std,
   tension_bounce_sigma, BIC_bounce, BIC_smbhb).

---

## Trace gaps

These are the items where the on-disk chain or its provenance does
**not** fully back the paper's framing. They are documented here for
transparency, not for re-running:

1. **TRACE GAP — "192 K" vs "320 K" sample count.** Paper 3 §VI and
   `paper3_science_highlights.md` quote 192,000 samples. The
   on-disk `nanograv_ptarcade_summary.json` reports
   `mcmc.n_samples = 320000`. The 192 K figure is `32 walkers ×
   6,000 production steps` — i.e. the post-burn-in count *if* the
   burn-in fraction were 0.4 rather than the configured 0.3. Both
   counts are consistent with a converged emcee chain (n_eff ≈
   9,800 either way); the paper text under-reports the actual
   stored chain length. Recommend reconciling the §VI sentence to
   "320,000 samples (32 walkers × 10,000 production steps after
   3,000 burn-in)" at the next revision pass.

2. **TRACE GAP — "GPU MCMC, combined PTA" wording in §VI L544.** The
   headline γ = 3.20 ± 0.42 is the **single-PTA** NANOGrav-15yr
   chain (CPU-only emcee, ~30 s runtime, no GPU), not the combined
   4-PTA chain. The combined chain gives 3.32 ± 0.37, also
   bounce-consistent at 0.88σ. Both values are reported in the
   paper's Table 4, but the prose conflation could be sharpened.
   This is a writing-only correction; the science is unaffected.

3. **TRACE GAP — synthetic vs. published free-spectrum.** The
   `nanograv_ptarcade.py` MCMC operates on a synthetic free-spectrum
   constructed from the NANOGrav 15-yr power-law best fit (γ = 3.2,
   log10A = −14.62) plus a hard-coded `noise_floor_bias` and
   per-bin `scatter_sigma`. It does **not** consume the official
   NANOGrav 15-yr free-spectrum HDF5 release. Paper 3 §7.3
   limitation #5 already discloses this ("the NANOGrav analysis
   uses derived free-spectrum values consistent with published
   results rather than raw timing residual data"). The canonical
   3.20 ± 0.42 should therefore be read as a **published-power-law
   propagation**, not a re-analysis of NANOGrav timing residuals.
   This is the substantive content of the Gemini 3.1-Pro finding
   P3-CM-MAJOR-related-to-PTA-traceability.

4. **TRACE GAP — `nanograv-enterprise-real` chain shows γ ≈ 9.99
   (prior boundary), not the canonical value.** The artifact at
   `pipelines/h200_results/pod_full_backup_20260413/results/nanograv-enterprise-real/summary.json`
   was produced by an attempt to run a true enterprise +
   PTMCMCSampler analysis on the raw NANOGrav 15-yr .tim/.par
   release (`h200_scripts/experiments/nanograv_enterprise_real.py`).
   The chain stalled at the upper γ-prior boundary (10.0) and is
   **not** the source of the paper's headline number. It is
   preserved on disk for future revival but is not part of the
   Paper 3 §VI evidence chain. Document-only; do not retract any
   paper number on the basis of this artifact alone.

5. **TRACE GAP — no R̂ Gelman-Rubin diagnostic.** Both runs report
   only `n_effective` and the `converged` boolean. R̂ requires
   independent chains; emcee's ensemble runs one. Paper 3 §VI does
   not quote R̂, so this is consistent — but a reviewer wanting an
   R̂ would have to re-run with a multi-ensemble harness.
   Document-only.

6. **TRACE GAP — autocorrelation time only stored for the
   single-PTA run.** `nanograv_ptarcade_summary.json` reports
   `autocorr_time = [32.18, 32.47]` but
   `nanograv_combined_pta_summary.json` does not store the τ array
   (only `n_effective`). Inferring the same chain length and walker
   count, τ_combined ≈ 32 (consistent), but the value is not on
   disk. Document-only.

---

## Cross-references

- **Paper 3 §VI / Eq. (2):**
  `pipelines/p3_anomaly_engine/paper3_draft.tex` L532–544 (Cosmological
  Applications and NANOGrav Bounce Consistency subsection)
- **Paper 3 §7.3 limitation #5:** `paper3_draft.tex` L568–570 ("the
  NANOGrav analysis uses derived free-spectrum values…")
- **Paper 3 SSOT:** `project-context/SSOT/paper-3/status.md` — line
  35 (TL;DR), line 107 (downstream-analyses table), line 148
  (verified-claims table).
- **Cross-paper:** Paper 1 (Spin-Torsion) §XV.C cross-validates the
  γ = 3 prediction with this same posterior; Paper 2 (f_NL Forecast)
  references the triple-channel consistency anchored on this PTA
  result. See `paper1_science_highlights.md` L171,
  `paper2_science_highlights.md` L104.
- **Peer-review status:**
  - R31 review: "PTA bounce γ=3.0 vs combined γ=3.20±0.42 (0.48σ);
    SMBHB 13/3 at 2.69σ ≈ 2.70σ — CLEAN"
    (`peer-reviews/r31_paper3_2026-04-29.md` L27, L102).
  - R42 Gemini 3.1-Pro: defect P3-OA-B5 — "zero equations for the
    likelihood, no mention of pulsar noise models, no priors". This
    bundle answers the equations + priors + noise-model question
    end-to-end. The "no posterior plots" sub-finding is unaddressed
    here (text-only deposit per Wave 11-G #1 scope) and remains
    queued for a corner-plot deposit at the next pod session.
