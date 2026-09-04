# Ledger #4 — Independent reproduction of the DESI DR1 local-PNG constraint from scale-dependent bias

**Date opened:** 2026-09-03 · **Ledger row:** 4 · **Directives:** R1 (ledger-first), Q1 (pure-contribution framing), Q2 (per-experiment manifests)

**Status:** PLAN + first cheap step (in progress)

## 0. Why this item exists

Ledger #1 fixed the lab's flagship matter-contraction value at f_NL^loc = −35/16
= −2.1875 (vs Cai et al. 2009's −35/8 = −4.375). Ledger #3's survey-reach study
(`research/track_a3_multichannel/survey_reach_fnl.py`) established that the
**only** channel that separates those two numbers is the large-scale-structure
survey channel, and that **DESI DR1 reaches 0.16σ** on −35/16. So this item is
explicitly *not* a detection attempt. The deliverable is a **constraint with the
lab's own systematics budget**, an independent check of the published DESI DR1
result, and a posterior statement about −35/16 vs −35/8 overlap — or a reasoned
"not yet" recording the exact blocker.

(Sections 1–6 below: published target, inputs, method, compute, kill/success,
risks. Filled in this session.)

---

## 1. The published measurement being reproduced

**Primary target — Chaussidon et al. 2024, arXiv:2411.17623** ("Constraining
primordial non-Gaussianity with DESI 2024 LRG and QSO samples"; submitted
2024-11-26, revised 2025-07-02).

| Item | Value (verbatim from the paper) |
|---|---|
| Tracers | LRG: 1,631,716 objects, 0.6 < z < 1.1 · QSO: 1,189,129 objects, 0.8 < z < 3.1 |
| Statistic | Redshift-space power-spectrum multipoles P_0(k), P_2(k) |
| Fit range | 0.003 < k < 0.08 h/Mpc; Δk = 0.001 (monopole), Δk = 0.002 (quadrupole) |
| Headline | f_NL^loc = −3.6 (+9.0/−9.1), 68% CL — LRG universality + QSO merger model |
| Alternative | f_NL^loc = +3.5 (+10.7/−7.4), 68% CL — universality for both |
| PNG-bias parameterisation | b_Φ(z) = 2 δ_c (b_1(z) − p), δ_c = 1.686; **p = 1.0 for LRG** (universality), **p = 1.6 for QSO** (merger model, default) |
| Covariance | 1000 EZmocks (500 NGC + 500 SGC) |
| Software | `pypower` (estimator), `desilike` (inference), `cosmoprimo` (transfer function) |
| Novelties | first blinded PNG analysis of this type; improved radial integral-constraint window correction; angular integral constraint added to the window to absorb the imaging-systematics/target-selection coupling |

**Secondary cross-checks (independent-method literature anchors):**

- **Brown, Levi, Randall, Chaussidon et al. 2026, arXiv:2606.24651** — the same
  DR1 LRG+QSO samples analysed in *configuration space* (2pcf) with
  simulation-based modelling: f_NL = −3 (+12/−12) joint; −3 (+22/−21) LRG;
  0 (+17/−16) QSO. A genuine method-independent DR1 cross-check, and the
  natural benchmark for how much a *different* pipeline moves the answer
  (≈ +33% on σ, central values consistent).
- **Rezaie et al. 2023, arXiv:2307.01753** — photometric DESI LRG angular
  clustering; establishes that Galactic extinction, survey depth, and seeing
  are the dominant systematics and that neural-network (SYSNet-style)
  mitigation outperforms linear regression. This is the source of the
  lab's systematics-budget design in §3.4.

**Relevance to the flagship (ledger #1/#3):** at σ ≈ 9, DESI DR1 reaches
**0.16σ** on f_NL = −35/16 and 0.32σ on −35/8 (`survey_reach_fnl.py`). Neither
value is detectable, and the two are separated by only ~0.24σ. **This item can
therefore never be a detection or a discrimination.** Its honest deliverables
are (i) an independent constraint carrying the lab's own systematics budget,
(ii) a b_Φ-marginalised statement (the DESI headline is p-choice dependent at
the ~7-unit level, i.e. **the p-choice moves f_NL by comparable to its own
error bar** — that is the real physics message for a bounce prediction of
|f_NL| ≈ 2), and (iii) the explicit posterior-overlap statement for −35/16 vs
−35/8 vs 0.

## 2. Inputs — exact public DR1 files

Root: `https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.5/`
(sibling versions `v1.2/`, `v1.5pip/` exist; v1.5 is the current clustering release,
posted 2025-02-11). **Licence: CC BY 4.0** (DESI public data releases), with the
required acknowledgment "This research used data obtained with the Dark Energy
Spectroscopic Instrument (DESI)…" and citation of the DR1 release paper.

| File | Bytes | Role |
|---|---|---|
| `QSO_NGC_clustering.dat.fits` | 83,298,240 | QSO NGC data, weights included |
| `QSO_SGC_clustering.dat.fits` | 45,178,560 | QSO SGC data |
| `QSO_NGC_nz.txt` / `QSO_SGC_nz.txt` | 11,808 / 11,832 | n(z) for FKP weights |
| `QSO_SGC_0_clustering.ran.fits` | 735,863,040 | one randoms realisation, SGC (smallest QSO randoms file) |
| `QSO_NGC_0_clustering.ran.fits` | 1,312,021,440 | one randoms realisation, NGC |
| `LRG_NGC_clustering.dat.fits` | 143,196,480 | LRG NGC data |
| `LRG_SGC_clustering.dat.fits` | 64,272,960 | LRG SGC data |
| `LRG_SGC_0_clustering.ran.fits` | 520,781,760 | LRG randoms (smallest of all four caps) |
| `LRG_NGC_0_clustering.ran.fits` | 985,916,160 | LRG randoms |

Randoms realisations run `0..17` per cap. A DESI-fidelity analysis uses all 18
(random density ≫ data), which is the volume driver:

- **Step-1 (executed this session): QSO data both caps + n(z) + one SGC randoms ≈ 0.86 GB.**
- Full QSO (both caps, 18 randoms each): 18 × (1.312 + 0.736) GB + data ≈ **37 GB**.
- Full LRG (both caps, 18 randoms each): 18 × (0.986 + 0.521) GB + data ≈ **27 GB**.
- Full LRG+QSO: **≈ 64 GB**. Add the 1000 EZmock realisations for the covariance
  (`.../LSS/iron/mocks/` — not needed if the covariance is analytic, see §3.5):
  order **1–3 TB**, which is the single item that decides the compute plan.

Download cost: $0 (public HTTP, no auth, no egress charge). Observed rate on the
lab's link ≈ 100–200 MB/s from `data.desi.lbl.gov`, so 64 GB ≈ 10–20 min of
wall-clock, not a blocker. **Storage lives outside the repo** at
`~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/`.

Weight columns carried in the clustering catalogues: `WEIGHT` (total),
`WEIGHT_SYS` (imaging systematics), `WEIGHT_COMP` (fibre assignment /
completeness), `WEIGHT_ZFAIL`, `WEIGHT_FKP`, plus `NX`/`NZ`. The imaging weights
in v1.5 are the collaboration's re-determined weights for the DR1 clustering
analysis; §3.4 treats *their presence or absence* as the lab's primary
systematic lever rather than attempting to recompute them from imaging maps.

## 3. Method

### 3.1 Two estimators, on purpose
- **Track 1 (fidelity):** `pypower` FFT-based multipole estimator
  (Yamamoto/Bianchi–Scoccimarro), on the same catalogues, same k-binning
  (0.003–0.08 h/Mpc, Δk = 0.001), so any disagreement with the published
  P_0(k) is a bug in our usage, not a method difference. `desilike` +
  `cosmoprimo` for the likelihood/transfer function.
- **Track 2 (lab-native):** an independent estimator written in-repo — either a
  direct FKP-weighted spherical-harmonic sum over a coarse grid, or an angular
  C_ℓ analysis in thin z-shells (which is what Rezaie+ 2023 did and what the
  lab already has NaMaster machinery for, from P1A/P1B/P4). Track 2 is the
  actual scientific contribution: an independent implementation is the only way
  the reproduction says something the DESI paper does not already say.

### 3.2 The signal model
Scale-dependent bias, standard form:

    Δb(k, z) = 2 f_NL δ_c (b_1 − p) / α(k, z),
    α(k, z)  = (2/3) k² T(k) D(z) c² / (H_0² Ω_m)

with δ_c = 1.686, T(k) the Boltzmann transfer function (normalised T→1 as k→0)
from `cosmoprimo`/CLASS, D(z) the growth factor normalised to unity today
(matching the DESI convention — a D(z)-normalisation slip is a classic factor
error and gets an explicit unit test). Then

    P_0(k) ∝ (b_1 + Δb(k) + f μ² …)² P_lin(k)

with Kaiser + a linear-theory quadrupole over 0.003–0.08 h/Mpc. p = 1.0 (LRG)
and p = 1.6 (QSO merger model) reproduce the published numbers; **p is then
marginalised** over p ∈ [1.0, 1.6] (and wider) for the lab's own statement.

### 3.3 Window, integral constraints, wide angle
Reproduced, not re-invented: convolve the model with the survey window computed
from the randoms (`pypower`'s window matrix), apply the **radial integral
constraint** and the **angular integral constraint** as Chaussidon+ do — the
AIC term is precisely how the imaging-systematics/target-selection coupling is
absorbed into the window, and omitting it biases f_NL. Wide-angle corrections
enter at the odd multipoles and at the ~k_min end; included at first order.

### 3.4 Systematics budget — the lab's own contribution
The dominant systematic is imaging selection, entering exactly at the k < 0.01
h/Mpc scales that carry all the PNG signal. Planned tests, each producing a
Δf_NL:

1. **Weights on/off:** rerun with and without `WEIGHT_SYS`. Δf_NL from this is
   the headline systematic; Rezaie+ 2023 shows it is O(10) for photometric LRGs.
2. **Galactic-latitude splits:** |b| > 40° vs |b| < 40°, and NGC vs SGC
   separately. Consistency is the strongest cheap null.
3. **EBV split:** low- vs high-extinction halves of the footprint.
4. **Stellar-density split** (Gaia-derived stellar density map).
5. **Imaging depth / seeing splits** per band (the Rezaie+ triad: extinction,
   depth, seeing).
6. **Angular-integral-constraint on/off**, to quantify how much of the
   correction is doing the work.
7. **Randoms-realisation jackknife** across the 18 realisations (shot noise in
   the window itself).

Any split that moves f_NL by more than the statistical σ/2 is reported as a
systematic floor, not smoothed away.

### 3.5 Covariance
First pass: **analytic Gaussian covariance** on the window-convolved model
(cheap, adequate at k < 0.08 h/Mpc where the field is near-Gaussian), validated
against the published error bars. Only if the analytic σ disagrees with the
published σ by > 20% do we pull EZmocks — that is the 1–3 TB decision, and it
is deferred behind a concrete trigger rather than assumed.

## 4. Compute plan

| Stage | Venue | Wall clock | $ |
|---|---|---|---|
| Step 1 — download + sanity check (this session) | local M-series CPU | ~10 min | 0 |
| Full catalogue download (LRG+QSO, all randoms, 64 GB) | local | 10–30 min | 0 |
| `pypower` P_ℓ(k) per cap per tracer (grid 512³, 18 randoms) | local CPU, 16 GB RAM | ~1–3 h per tracer-cap; ~8 h total | 0 |
| Window + integral-constraint matrices | local CPU | ~2–4 h | 0 |
| Lab-native estimator (Track 2) | local CPU | ~4 h | 0 |
| Likelihood / MCMC on 4 data vectors, ~8 params, `desilike` + emcee | local CPU | ~2 h (the model is linear-theory-cheap) | 0 |
| Systematics grid (7 tests × 4 data vectors = 28 re-runs) | local CPU | ~1–2 days unattended, or RunPod CPU for parallelism | 0 local / ≤ $10 RunPod |
| **Contingency: EZmock covariance (1000 mocks)** | RunPod (storage + CPU), only if triggered | ~1–2 days | **$50–150** (dominated by 1–3 TB transfer + disk-hours) |

**Baseline: $0, entirely local, ~1 week of mostly unattended CPU.** No GPU is
needed — this is FFT and linear algebra, not inference over spectra. RunPod is a
contingency, not the plan. If a pod is used, directives E / `/backup-3plus`
apply (local + HF + B2 before any stop).

## 5. Kill / success conditions

Ledger row 4's stated criterion is "a constraint with our own systematics
budget, or a reasoned 'not yet'." Made machine-checkable:

**SUCCESS (the item closes as a result):**
- S1. Our P_0(k) for QSO NGC agrees with the published DR1 measurement over
  0.003 < k < 0.08 h/Mpc to within the published error bars (χ²/dof < 2).
- S2. Our posterior on f_NL recovers the published central value to within
  0.3σ_published for the published p-choices.
- S3. A systematics budget with ≥ 5 of the §3.4 tests executed, each with a
  quoted Δf_NL, and a stated total systematic σ_sys.
- S4. A b_Φ-marginalised constraint (p free over [1.0, 1.6]) and the explicit
  posterior-overlap statement for −35/16, −35/8, and 0.

**KILL (the item closes as a reasoned "not yet"):**
- K1. S1 fails and the disagreement traces to a product DESI does not release
  publicly (e.g. the exact blinding/unblinding chain, or an internal weight
  version) — record the exact missing product and stop.
- K2. The analytic covariance is inadequate AND the EZmock volume/cost exceeds
  the §4 contingency budget — record the exact TB and $ figure and stop at the
  P_ℓ(k) measurement level (which is still publishable as an independent
  measurement without a likelihood).
- K3. σ_sys from §3.4 exceeds σ_stat — then the honest output is "DESI DR1
  cannot constrain f_NL at the lab's own systematics standard," which is itself
  a result and closes the row.

In **all** branches the row closes with a written verdict; there is no branch in
which this item silently stalls (directive R1/Q4).

## 6. Risks, and what the lab can honestly add

**Risks**
- R-a. **The reproduction adds nothing if it is a re-run.** Mitigated by Track 2
  (independent estimator) and §3.4 (independent systematics budget). If Track 2
  is dropped for cost, the item is downgraded to a validation exercise and
  should not become a paper (directive Q1: a work whose thesis is "we re-ran
  someone else's pipeline" is not a contribution).
- R-b. **Blinding.** The published analysis was blinded; ours cannot be. We know
  the answer before we measure it. Mitigation: pre-register §3.4's test list and
  the k-range *in this file, before any P(k) is computed* — which this commit
  does — and never change them post hoc.
- R-c. **Integral-constraint modelling is the hard part** and is where an
  independent implementation is most likely to be simply wrong. Mitigation:
  validate the window/IC machinery against the published P_0(k) *first* (S1)
  before any f_NL is quoted.
- R-d. **Confirmation-bias hazard specific to this lab:** f_NL = −35/16 is
  negative and the headline DESI central value is negative. That is a
  coincidence at 0.16σ and must be stated as such every time it appears. It is
  **not** support for the bounce, and any phrasing suggesting otherwise is a
  directive-R6 violation.
- R-e. Version drift between v1.2 / v1.5 / v1.5pip catalogues; the paper's exact
  version is not stated in the text we could access. Recorded as an open input
  question; both v1.2 and v1.5 will be checked if S1 fails.

**What the lab can honestly add**
1. An **independent systematics budget** on the DR1 PNG measurement — the
   split-based tests above are cheap, are not all in the published paper, and
   directly quantify what the imaging weights are worth in f_NL units.
2. A **b_Φ-marginalised statement.** The published result swings from −3.6 to
   +3.5 purely on the p = 1.6 vs p = 1.0 choice — a 7-unit systematic on a
   ±9 measurement. For a theory predicting |f_NL| ≈ 2, the b_Φ prior *is* the
   measurement. Saying that clearly, with a marginalised posterior, is a real
   contribution.
3. The **−35/16 vs −35/8 posterior overlap**, stated honestly: DESI DR1
   separates them by ≈ 0.24σ, i.e. not at all; both are comfortably inside the
   68% interval; the survey channel does not become decisive until SPHEREx
   (σ ≈ 0.5–0.7, ledger #3). This is the "reasoned not yet" the ledger row
   anticipated, quantified.
4. A second **method-independent comparison point** against arXiv:2606.24651's
   configuration-space result — how much a different pipeline moves f_NL is an
   empirical systematic nobody has yet tabulated across all three analyses.

## 7. Execution log

**2026-09-03 — plan written; step 1 EXECUTED and PASSED.**

Downloaded (0.86 GB, $0, ~20 s) to
`~/Desktop/CODE_YOU/bigbounce_datasets/desi_dr1_lss/` — *outside the repo*:
`QSO_{NGC,SGC}_clustering.dat.fits`, `QSO_{NGC,SGC}_nz.txt`,
`QSO_SGC_0_clustering.ran.fits`. All five sha256s recorded in manifest
`reproducibility/manifests/experiments/ledger4-desi-dr1-lss-sanity.json`
(schema-validated).

`dr1_lss_sanity.py` (0.7 s, local CPU) results:

| Check | Result |
|---|---|
| Rows | QSO NGC 793,219 · SGC 430,172 · total 1,223,391 |
| In published 0.8 < z < 3.1 | **1,190,839 vs Chaussidon+ 2024's 1,189,129 → ratio 1.0014 (0.14%)** |
| Randoms | `QSO_SGC_0` 6,511,977 rows = 15.14× the SGC data |
| Weight columns | `WEIGHT`, `WEIGHT_SYS`, `WEIGHT_COMP`, `WEIGHT_ZFAIL`, `WEIGHT_RF`, `WEIGHT_FKP`, `NX` — all present in both caps |
| `WEIGHT_SYS` (NGC) | mean 0.9768, σ 0.0654, range [0.624, 1.594], 0 non-finite, 0 exactly-unity |

The 0.14% agreement with the published QSO count is a **provenance check, not a
measurement**: it confirms we hold the same sample the DR1 PNG analysis used.
The residual 1,710 objects are the paper's own further analysis selection and
are not claimed to be reproduced. The imaging-systematics weight is present and
non-trivial (7% RMS, 1.6× dynamic range), so §3.4 test 1 — the plan's primary
systematic lever — is executable on these files as downloaded.

Figures: `outputs/dr1_lss_sanity_zhist.png` (n(z) both caps against the fit
range), `outputs/dr1_lss_sanity_footprint.png` (equatorial Mollweide; the
expected DR1 tiled NGC/SGC footprint).

**No blocker encountered.** Next step: extend the download to the remaining 17
randoms realisations per cap plus the LRG catalogues (≈ 64 GB, still $0), then
Track-1 `pypower` P_0(k) on QSO SGC as the S1 validation target.
