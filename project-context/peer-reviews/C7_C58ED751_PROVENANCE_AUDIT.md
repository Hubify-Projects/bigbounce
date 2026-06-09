# C7 — Provenance audit of the remaining c58ed751 "close 4 future-work items" wave (FW-1, FW-2, FW-11)

**Date:** 2026-06-09 · **Auditor:** compute job C7 (research-integrity audit, no .tex edits)
**Trigger:** C2/C3 found that one product of commit `c58ed751` (P4's −0.122σ subsample-mask
MASTER null) was computed on a SYNTHETIC catalog and is being retracted
(see `P4_HEADLINE_PROVENANCE_SEV1.md`). This audit applies identical scrutiny to the
OTHER three items closed in that commit/wave: FW-1, FW-2, FW-11.

---

## 0. Commit forensics

```
commit c58ed751488aad9cc2bd2a628dad281054bbb70f
Date:   Wed Apr 29 00:06:49 2026 -0700
    feat: close 4 future-work items with real results (FW-1, FW-2, FW-11, P4-M6)

A  pipelines/p1_highz_tracers/fw11_results/fw11_nanograv_bayes.json
A  pipelines/p2_chirality/master_results/master_power_spectrum.json   ← P4-M6, RETRACTED (SEV-1)
A  pipelines/p2_chirality/master_results/edgeon_contamination.json
A  pipelines/p2_fnl_forecast/fw1_results/fw1_scale_dependent_fnl.json
A  pipelines/p2_fnl_forecast/fw2_results/fw2_gnl_trispectrum.json
A  pipelines/p3_anomaly_engine/fw6_hyperparameter_stability.py        ← only script in commit (FW-6, out of scope)
M  arxiv/main.tex · M  pipelines/p2_chirality/chirality_catalog_paper.tex
M  research/focused_paper_source_integration/02_full_draft.tex
```

Adjacent wave commit: `a4d9e1bb` (same night, 00:09:23 -0700) propagated FW-11 B=34.0
into `arxiv/main.tex` L949 and added `fw12_anisotropic_birefringence.json` (FW-12, P1 — out of C7 scope
but shares the same provenance pattern: JSON without script).

**Cross-cutting finding (applies to all three items).** All three committed JSONs are
**byte-identical** to the pod-session backup at
`pipelines/h200_results/pod2_priorsession_2026-04-29/results/{fnl_scale_dependent,gnl_trispectrum,nanograv_bayes}/`
(verified with `diff -q`, 2026-06-09). That is the **same pod session** whose
`results/logs/pod2_full.log` contains the SEV-1 smoking gun:

> `[3a] Generating galaxy catalog for power spectrum...`
> `  Using 5547858 galaxies (DESI Legacy footprint approximation), CW fraction=0.4974`

Per-item run logs exist (`results/logs/fw1_fnl.log`, `fw2_gnl.log`, `fw11_bayes.log` — each
ends `Results saved to /root/results/... DONE`), but **none of the four generating scripts
from that session was ever committed** — not for P4-M6 and not for FW-1/2/11. The repo-wide
search (`find` + `grep` over `*.py/*.mjs/*.sh` for `n_fNL`, `gnl_trispectrum`,
`scale_dependent_fnl`, `savage`/`Savage` outside the later P3 rerun) returns no producer
for any of the three artifacts.

---

## 1. FW-1 — scale-dependent f_NL joint Fisher forecast (feeds P2)

**Artifact:** `pipelines/p2_fnl_forecast/fw1_results/fw1_scale_dependent_fnl.json`
**Paper:** `research/focused_paper_source_integration/02_full_draft.tex` §"Joint (f_NL, n_fNL)
Forecast as a Stronger Discriminator" (L581) + cross-reference in abstract (L207, "idealized joint
(f_NL, n_fNL) … Fisher self-consistency check is discussed in §Discussion").

### (a) Generating script — **MISSING**
No script anywhere in the repo. Log `fw1_fnl.log` proves a script ran on the pod
(`Results saved to /root/results/fnl_scale_dependent/fw1_scale_dependent_fnl.json`) and was lost
with the pod.

### (b) Provenance fields — **ABSENT / INSUFFICIENT**
JSON records `survey: SPHEREx`, `f_sky: 0.75`, `z_bins`, `k_range: [1e-4, 0.2]`, `k_pivot: 0.05`
and the 2×2 Fisher matrix — but **no** n(z) per bin, no bias model b(z), no b_φ convention, no
shot-noise/volume inputs, no P(k) source, no date, no seed, no code version. The Fisher matrix
**cannot be reconstructed** from what is recorded.

### (c) Numbers trace to artifact — **YES, exactly**
Current P2 L581 quotes σ(n_fNL)=0.086, σ_marg(f_NL)=0.44, ρ=0.966, ~9.9σ, ratio 3.86, "testable
to ±0.09" — all match JSON fields `sigma_nfnl=0.085523`, `sigma_fnl_marginalized=0.443094`,
`correlation=0.966013`, `fnl_detection_sigma=9.87`, `degradation_factor=3.8685`.

### (d) Input data real? — **N/A (forecast)** but the Fisher matrix itself is unverifiable
No catalog input is required for a Fisher forecast, so this is not "synthetic data" in the P4-M6
sense. The integrity question is whether the posted Fisher matrix is a correct SPHEREx SDB
computation. Two checks:

1. **Internal arithmetic — VERIFIED (C7 rerun, <1 min CPU).** Inverting the posted matrix
   `F = [[76.22605, −381.50232], [−381.50232, 2046.09318]]` reproduces every derived number
   to 6 significant digits: σ_marg(f_NL)=0.4430939, σ(n_fNL)=0.0855234, |ρ|=0.9660125,
   σ(f_NL)-only = 1/√F₀₀ = 0.1145377, detection 9.8738σ, degradation 3.8685.
   The JSON is self-consistent — it all derives from that one 2×2 matrix.
2. **External plausibility — FAILS against literature.** The implied unmarginalized
   σ(f_NL)=0.114 is ~6× sharper than any published SPHEREx SDB forecast (Doré+2014,
   Heinrich+2024, Münchmeyer+2019, σ(f_NL)~0.5–0.9). The paper itself now flags this verbatim
   (L581): "*sharper than any published SPHEREx SDB forecast known to us … **requires** an
   independent published forecast or in-repo Fisher computation before it can be quoted as a
   measurement-grade detection significance*" and "*pending the companion-artifact Fisher-input
   release*". That companion artifact **does not exist** — this audit confirms the release the
   paper is "pending" was never made and cannot be made from what is on disk.

### Verdict: **SUSPECT**
Not fabricated in the P4 sense (no synthetic catalog involved; arithmetic is honest given the
matrix), but the load-bearing Fisher matrix has no committed script, no recoverable inputs, and
is ~6× more optimistic than the published literature. Prior R-rounds already forced heavy
hedging into P2 (v1.7.27 "9.9σ Fisher provenance disclosure"; v1.7.30 deferral list still carries
"compute-bound 6-bin SDB Fisher" — i.e. the verification rerun has been deferred since May).

---

## 2. FW-2 — g_NL trispectrum forecast (feeds P2)

**Artifact:** `pipelines/p2_fnl_forecast/fw2_results/fw2_gnl_trispectrum.json`
**Paper:** `02_full_draft.tex` L583 (trispectrum paragraph).

### (a) Generating script — **MISSING** (same pod session, `fw2_gnl.log`, never committed).

### (b) Provenance fields — **ABSENT**, plus the artifact is **internally broken**:
```json
"spherex_fisher": {
  "sigma_f_NL": 0.04857,
  "sigma_g_NL": 0.0,
  "sigma_tau_NL": 0.0,
  "g_NL_detection_sigma": 85877764.33, ...
```
`sigma_g_NL = 0.0` alongside a detection significance of 8.59×10⁷σ implies
σ(g_NL) = 27.5625 / 85,877,764 ≈ **3.2×10⁻⁷** — roughly **2×10¹¹ times better than Planck**
(σ(g_NL) ~ 6.5×10⁴). This is a numerically degenerate/garbage Fisher evaluation; the artifact's
own `note` field concedes "*sigma(g_NL) is approximate; full trispectrum Fisher requires
bispectrum covariance*". The `model_discrimination` separations (e.g. slow-roll at
85,877,764σ) are physically meaningless.

Also: the c58ed751 commit message claims "*Below Planck sensitivity (σ~5×10⁴)*" — **that number
appears nowhere in the artifact** and directly contradicts the artifact's own (absurd) σ.

### (c) Numbers trace to artifact — **NO LONGER.** The current P2 paragraph (L583) quotes only:
- (36/25)·f_NL² = 27.56 — **analytic, C7-verified** ((36/25)·4.375² = 27.5625 exactly);
- Planck τ_NL < 2800 (95% CL) — literature (`Planck:2019fnl`), not the artifact;
- and has **corrected** the original c58ed751 saturation claim into the inequality
  τ_NL ≥ 27.56 ("the matter-bounce bispectrum is not exactly local … so the prediction is the
  inequality … rather than saturation").

None of the artifact's `spherex_fisher` numbers ever propagated into the current draft. The
qualitative claim "below the reach of SPHEREx" actually *contradicts* the broken artifact (which
claims an 8.6×10⁷σ SPHEREx detection).

### (d) Input data real? — N/A (analytic consistency relation + broken Fisher).

### Verdict: **SUSPECT (artifact) / paper exposure: NONE**
The artifact is an orphaned, internally inconsistent computation and should be quarantined, but
every number in the current P2 trispectrum paragraph is independently verifiable
(analytic formula + cited Planck bound).

---

## 3. FW-11 — NANOGrav Savage-Dickey Bayes factor (fed P3 + P1 long-form)

**Artifact:** `pipelines/p1_highz_tracers/fw11_results/fw11_nanograv_bayes.json`
**Papers touched by the wave:** `arxiv/main.tex` L983 (c58ed751) + L949 (a4d9e1bb); the number
also circulated through earlier P3 drafts.

### (a) Generating script — **MISSING** for the pod run (`fw11_bayes.log`, `/root/results/...`).
However a **later, fully provenanced replacement exists**:
`pipelines/p3_pta_mcmc/savage_dickey_2026-05-29.py` + output
`free_spectrum_real_2026-05-01/savage_dickey_2026-05-29.json` (records script path, chain path,
n_samples=320,000, priors, KDE method).

### (b) Provenance — partial. The JSON does carry a source field:
```json
"combined_pta_posterior": { "gamma_mean": 3.2, "gamma_std": 0.42,
  "source": "Paper 3 §6 canonical (2026-04-17 v2b Fisher recompute)" }
```
But the repo's own forensic bundle (`reproducibility/p3_pta_mcmc/README.md`) establishes that
this input γ = 3.20 ± 0.42 (i) traces to `nanograv_ptarcade_summary.json`
(gamma_mean=3.1925, gamma_std=0.4233), (ii) is a fit to a **synthetic spectrum constructed from
the published NANOGrav power-law fit** ("the prior synthetic-power-law summary statistic
(γ = 3.20 ± 0.42 on the `nanograv_ptarcade.py` constructed spectrum)"), (iii) is **single-PTA,
CPU-only emcee, ~30 s, no GPU** — not "combined PTA" and not "GPU MCMC" as labeled, and (iv) the
"v2b Fisher recompute" tag refers to a §VI sensitivity-ladder fix, **not** a rerun of this
posterior ("the headline γ = 3.20 ± 0.42 was never re-run").

### (c) Numbers trace / arithmetic — **VERIFIED (C7 rerun, <1 min CPU).** Treating the posterior
as N(3.20, 0.42²) with prior U[0,7], C7 reproduces every JSON value:
B(bounce/SMBHB)=34.0332, B(bounce/free)=5.9363, B(SMBHB/free)=0.1744, tensions 0.4762σ/2.6984σ,
equal-prior posteriors 0.8348/0.0245/0.1406, analytic P(closer-to-bounce)=0.86674. The
Savage-Dickey arithmetic is exact and honest **given the input**.

### (d) Input data real? — **NO (synthetic-derived input, by the repo's own admission)**, and
**superseded everywhere that matters**:
- **P3** (`pipelines/p3_anomaly_engine/paper3_draft.tex` abstract L92 + §L517) now uses the
  real-KDE Zenodo-8060824 free-spectrum chain: γ = 2.567 ± 0.382, B_MB/SMBHB = 7.14×10³, with
  committed script, chain (320,000×2 float64), and Appendix `app:pta_mcmc`. No FW-11 number
  survives in P3 except the explicit "supersedes the synthetic-from-power-law … γ = 3.20 ± 0.42"
  caveat.
- **P1A** (`arxiv/paper1a_ech_nogo.tex` L1683–1688) uses γ = 2.567 ± 0.382 and states verbatim:
  "*This figure supersedes the earlier synthetic-Gaussian-likelihood value γ = 3.20 ± 0.42 used
  in pre-real-KDE drafts*". P1B reports no PTA Bayes factor at all.
- **Residual exposure:** `arxiv/main.tex` L983 — the **DEPRECATED** long-form P1 (per
  `SSOT/paper-1/status.md`: "legacy long-form arxiv/main.tex … DEPRECATED") — still asserts
  B = 34.0 / 83.5% / 2.70σ and, worse, mislabels the input as "*an independent reanalysis of the
  NANOGrav 15-year free-spectrum data … GPU MCMC over the per-frequency free-spectrum posteriors
  released by the NANOGrav collaboration*", which the repo's own README contradicts on all three
  counts (synthetic-from-power-law, not per-frequency posteriors; CPU not GPU; single-PTA not
  combined).

### Verdict: **SUSPECT (artifact + deprecated-text claim) / live-paper exposure: NONE**
Arithmetic clean; input synthetic-derived and mischaracterized; fully superseded in every live
paper by a provenanced real-data rerun that — notably — **moved the Bayes factor by ×210**
(34.0 → 7.14×10³) and flipped the bounce tension sign (−0.48σ → +1.13σ), demonstrating
concretely that the FW-11 input was not a faithful stand-in for the real likelihood.

---

## 4. Verdict table

| Item | Artifact | Script in repo | Provenance fields | Numbers trace to artifact in live tex | Input real? | **Verdict** |
|---|---|---|---|---|---|---|
| **FW-1** f_NL running Fisher | `p2_fnl_forecast/fw1_results/fw1_scale_dependent_fnl.json` | **NO** (pod log only) | **NO** (no n(z)/bias/b_φ/volume/seed/date) | **YES** — P2 L581 quotes 0.086 / 0.44 / 0.966 / 9.9σ / ±0.09 verbatim | N/A (forecast) — but Fisher matrix unreproducible & ~6× sharper than published SPHEREx SDB forecasts | **SUSPECT** |
| **FW-2** g_NL trispectrum | `p2_fnl_forecast/fw2_results/fw2_gnl_trispectrum.json` | **NO** (pod log only) | **NO**, artifact internally broken (σ(g_NL)=0 yet 8.6×10⁷σ detection ⇒ implied σ=3.2×10⁻⁷, 10¹¹× beyond Planck) | **NO** — current P2 L583 uses only analytic 27.5625 (verified) + Planck τ_NL<2800 | N/A | **SUSPECT (artifact); paper text CLEAN** |
| **FW-11** NANOGrav Bayes factor | `p1_highz_tracers/fw11_results/fw11_nanograv_bayes.json` | **NO** for pod run; later provenanced replacement `savage_dickey_2026-05-29.py` exists | Partial (`source` field, but mislabeled per `reproducibility/p3_pta_mcmc/README.md`) | **NO in live papers** (P3/P1A migrated to real-KDE γ=2.567±0.382, B=7.14×10³); **YES in deprecated `arxiv/main.tex` L983** | **NO** — input γ=3.20±0.42 is a synthetic-from-power-law fit by the repo's own forensics; arithmetic itself verified exactly | **SUSPECT (superseded); deprecated main.tex carries a falsely-labeled claim** |

For reference, P4-M6 (the fourth item of the same commit) is **SYNTHETIC/FABRICATED-input,
RETRACTING** per `P4_HEADLINE_PROVENANCE_SEV1.md`; this audit confirms FW-1/2/11 came from the
same un-committed pod-script session (byte-identical pod backups, same log directory).

---

## 5. Remediation actions

### FW-1 (the only item with live-paper exposure) — **priority**
1. **Write and commit the joint (f_NL, n_fNL) SPHEREx SDB Fisher script** with declared inputs
   (Doré+2014 n(z) & bias per z-bin, b_φ convention, CAMB/CLASS P(k), V_eff/shot noise per bin),
   regenerate the artifact with full provenance fields (inputs, date, code hash), and compare
   against the posted matrix `[[76.226, −381.502], [−381.502, 2046.093]]`.
   *Effort: human ~2 days / CC ~2–4 h (standard SDB Fisher; <10 min CPU runtime).*
   Likely outcome given the 6× literature gap: the regenerated σ's will be weaker; P2 L581
   numbers (0.086 / 0.44 / 9.9σ / ±0.09) would then need replacement via
   `/bigbounce-claims-table-sync`.
2. **Until that lands:** P2's existing hedging ("requires … in-repo Fisher computation before it
   can be quoted") is accurate but the paragraph still prints the specific numbers. The
   pre-arXiv decision is binary: land the script (preferred, per /no-future-work-defer) or strip
   the unverifiable numbers down to the qualitative degeneracy statement.

### FW-2
3. **Quarantine the artifact** — move `fw2_results/fw2_gnl_trispectrum.json` (and the pod-backup
   copy) into a `quarantine/` path or prepend a `"status": "BROKEN — degenerate Fisher,
   do not cite"` field, mirroring the SEV-1 handling. No paper edit required (current text is
   already artifact-independent and analytically verifiable). *Effort: 15 min.*

### FW-11
4. **Neutralize deprecated `arxiv/main.tex` L983** so the falsely-labeled B=34.0 claim
   ("independent reanalysis … GPU MCMC over the per-frequency free-spectrum posteriors") can
   never reach arXiv by accident: add a prominent DEPRECATED banner to the file header and/or
   replace L983 with the real-KDE numbers + supersession note already used in P1A L1683.
   *Effort: 15–30 min.*
5. **Annotate the FW-11 JSONs** (both copies) with a `"superseded_by"` field pointing at
   `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/savage_dickey_2026-05-29.json`.
   *Effort: 10 min.*

### Systemic
6. **Pod-script commit gate:** the root cause across P4-M6 + FW-1/2/11 (+ FW-12, same pattern)
   is pod-resident scripts producing committed JSONs and then dying with the pod. Standing rule
   for `/pod-backup-before-stop` + `/houston-method-v2`: an artifact JSON may not be committed
   unless its generating script is committed in the same commit and the JSON carries
   input-path/seed/date provenance fields. Audit FW-12
   (`pipelines/p1_highz_tracers/fw12_results/fw12_anisotropic_birefringence.json`, commit
   `a4d9e1bb`) under the same lens as a follow-up — it is outside C7 scope but matches the
   pattern (JSON, no script).
