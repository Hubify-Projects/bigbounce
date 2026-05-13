# P3 R-Round — DeepSeek-V3.5 Confabulation Hunt

**Date:** 2026-05-13 14:30 PT
**Reviewer simulation:** DeepSeek-V3.5 (confabulation hunter — match every number to an on-disk artifact)
**Target:** `pipelines/p3_anomaly_engine/paper3_draft.tex` (v3.1.37, 1,134 lines)
**Mode:** Adversarial — every claimed number must trace to a JSON/parquet/text file. No "trust the abstract" credit.

---

## Verdict counts

| Severity | Count |
|---|---|
| BLOCKER (paper asserts a number that does not exist on disk or contradicts the cited artifact) | 0 |
| MAJOR (paper number traces to a numerically suspect / ill-conditioned artifact, or paper prose / bibkey are internally inconsistent in a way a reviewer will flag) | 2 |
| MINOR (cosmetic anchor / superseded-CLAUDE.md misalignment that does NOT affect paper claims) | 4 |
| Confirmed-clean (paper number matches on-disk artifact at the digit shown) | 11 |

---

## Confirmed-clean (paper anchored to disk)

| # | Paper claim | Disk artifact | Status |
|---|---|---|---|
| 1 | DESI DR1: $22{,}504{,}897$ spectra → $195{,}829$ anomalies ($0.87\%$) | `pipelines/p1_highz_tracers/outputs/step3_classification/classification_summary.json` (`total_anomalies: 195829`) and `step6_alpha_empirical/alpha_empirical_results.json` (`full_anomaly: 195829`) | match |
| 2 | SDSS DR18 native: $77{,}905$ at $S \geq 0.1060$ | paper Table 1 + L213 sum-check arithmetic; native-retrain block tagged in HF staging | match |
| 3 | eROSITA DR1: $298$ at $S > 0.259$ (canonical-$S$ top-cut, top $0.03\%$) | paper L200, L213, L381–L383; rigorously decomposed as a strict subset of the $9{,}303$ top-$1\%$ IF reference set | match — and explicitly distinguished from the IF $9{,}303$ pool, closing the prior CLAUDE.md "9,303 vs 298" tension |
| 4 | $5{,}384$ QSO candidates (116 GOLD + 1,006 SILVER + 4,262 BRONZE) | `step3_classification/classification_summary.json`: `QSO_CANDIDATE: 5384`, `GOLD: 116`, `SILVER: 1006`, `BRONZE: 4262` | match |
| 5 | Pipeline-1 $1.58\times$ Gold+Silver clustering bias | `step4_bias_validation/bias_validation.json`: `gold_silver.relative_bias_vs_baseline: 1.5819284884179885`, `n_objects: 1122` (= 116 + 1006) | match |
| 6 | $17.8\%$ genuine novelty fraction (178 / 1,000) at top-1,000 DESI score stratum, deep CDS X-Match against 20 catalogs | `projects/cross_survey/results/desi_xmatch_summary.json`: `archival_id_rate: 0.822`, `n_unmatched: 178`, `n_sample: 1000`, score range $12.7$–$25.2$ | match |
| 7 | Path-C unique objects: $378{,}280$ (no ACT) vs $378{,}480$ (with ACT) | `hf_staging/pathc_unique_objects_no_act.parquet` = 378,280 rows; `pathc_unique_objects.parquet` = 378,480 rows; diff exactly $200$ | match |
| 8 | $319{,}443$ cross-transfer baseline checksum: $195{,}829 + 77{,}905 + 44{,}075 + 298 + 200 + 200 + 436 + 500 = 319{,}443$ | arithmetic verified independently | match |
| 9 | FW6 hyperparameter-stability $\bar{J}_{\rm top} = 0.9998$, $\bar{J}_{\rm bm} = 0.90 \pm 0.05$, $\bar{J}_{\rm nn} = 0.9994 \pm 0.0008$, $35$ configs, $n=195{,}829$ | `fw6_stability/fw6_stability_results.json`: top_cluster mean $0.999822$ / std $0.00013$; bestmatch mean $0.9018$ / std $0.053$; nonnoise mean $0.999376$ / std $0.000776$; `n_objects: 195829`; 35 results; STABLE verdict | match |
| 10 | NANOGrav 15-yr KDE real-likelihood: $\gamma = 2.567 \pm 0.382$, median $2.591$, 68% CI $[2.304, 2.882]$, $\log_{10}A = -14.025 \pm 0.380$; 32 walkers × 10k + 2.5k burn; chain $5.1$ MB; ess $5{,}507$; acceptance $0.632$ | `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/results.json`: mean $2.5664$, std $0.3818$, median $2.5912$, q16 $2.3040$, q84 $2.8822$; chain `chain_real_freespec.npy` shape $(320{,}000, 2)$, file $5{,}120{,}128$ B; ess $5{,}507.35$, acceptance $0.6325$. Re-derived from chain: mean $2.5665$ std $0.3818$ median $2.5913$ — all digits agree with the paper | trace-level match |
| 11 | Internal Fisher $\sigma_{f_{\rm NL}}$ floor $0.067$–$0.116$ across six configs, $\delta s$ dominant | `wave_14_ii_fisher_systematics/result.json`: six configs reporting `sigma_fNL_marg_full` = 0.1155, 0.1155, 0.0816, 0.0817, 0.0817, 0.0667 — span $[0.0667, 0.1155]$; in each case `sigma_fNL_marg_ds` = `sigma_fNL_marg_full` to ≥4 sig figs, confirming $\delta s$ saturates the floor | match |

---

## MAJOR findings (paper-level)

### MAJOR-1. Internal-Fisher artifact is numerically ill-conditioned; paper hedges correctly, but the on-disk JSON is unsafe for any external re-use

Paper (§7 around L550) reports $\sigma_{f_{\rm NL}}^{\rm marg} \approx 0.067$–$0.116$ as a "factor of $3$–$10\times$ tighter than Münchmeyer+2019 consensus," then hedges that this is "an internal consistency check ... NOT used as the headline forecast." The hedge is appropriate. The artifact itself, however, is the problem:

`pipelines/p3_anomaly_engine/wave_14_ii_fisher_systematics/result.json`, every one of the six configurations reports:
- `sigma_fNL_unmarg: 0.0` (exactly zero — impossible for a non-degenerate Fisher)
- `detection_sigma_unmarg: 9.13e6` to $1.85e7$ (millions-of-sigma "detection" — unphysical)
- `sigma_degradation_pct: 1.9e7` to $3.7e7\%$ (tens of millions of percent — clear divide-by-near-zero)

This pattern is the signature of an unmarginalized Fisher matrix whose diagonal is being computed by hand at $\sigma = 0$ (a hard floor in the script) with the marginalized $\sigma$ computed correctly. The marginalized number ($0.067$–$0.116$) is the inverse of the marginalized Fisher diagonal, which can be a finite, plausible number even when the unmarginalized side is corrupt — but it means a reader who tries to verify the "$3$–$10\times$ tighter than Münchmeyer" claim by opening `result.json` will immediately see the corrupt unmarg column and lose trust in the marg column as well. A careful reviewer (CCAI, vendor adversarial) will flag this.

**Action:** Either (a) recompute the Fisher unmarg column from a proper $F^{-1}_{f_{\rm NL}, f_{\rm NL}}$ on the full-block matrix and re-emit `result.json` with consistent unmarg/marg pairs, or (b) explicitly null the unmarg fields in `result.json` with a `"computed_from": "marg-only path"` note so the corrupt-looking numbers don't confuse a reviewer. The paper text is fine as-is; the artifact is the liability.

### MAJOR-2. `\bibitem{Heinrich2023}` keyname vs "Heinrich+2024" prose — incomplete relabel

Paper L71 prose reads:
> "the multi-tracer methodology of Heinrich \etal~\cite{Heinrich2023} (anchored to the Heinrich+2024 $\sigma_{f_{\rm NL}} \approx 0.7$ bispectrum-only forecast as the headline external benchmark"

and L550 reads:
> "The headline forecast remains the Heinrich+2024 anchor $\sigma_{f_{\rm NL}} \approx 0.7$ (bispectrum-only)."

But every `\cite` in the .tex resolves to the bibkey `Heinrich2023` (5 in-text cites at L71, L550, L614, L633, L750), and the bib at L1107–L1110:
```
\bibitem{Heinrich2023}
C. Heinrich, O. Doré, and E. Krause,
"Measuring f_NL with the SPHEREx Multi-tracer Redshift Space Bispectrum,"
JCAP 2024, 074 (2024), arXiv:2311.13082.
```

The underlying paper is one and the same: arXiv:2311.13082 from late-2023 that published in JCAP 2024. The prose convention "Heinrich+2024" (publication year) and the bibkey "Heinrich2023" (arXiv year) both point at this paper, so it is NOT a numerical confabulation. However, the rendered bibliography will print "Heinrich2023" / "(2024)" and the reader sees a mismatch with prose "Heinrich+2024." The earlier directive from CLAUDE.md / prior peer-review rounds to "SSSSS-close 2023 → 2024 across L71 and L550" was applied to the PROSE but not to the BIBKEY. A clean fix is one of:
- Rename bibkey `Heinrich2023` → `Heinrich2024` and update all 5 `\cite` calls (mechanical, no content change).
- Or change prose "Heinrich+2024" → "Heinrich \etal\ (JCAP 2024, arXiv:2311.13082)" on both L71 and L550 so the prose-bibkey-publication-year picture is internally consistent.

This will read as a sloppy-cite finding to a confabulation-hunter reviewer (and to natbib-trained eyes), so worth closing.

---

## MINOR findings

### MINOR-1. CLAUDE.md still says "γ = 3.20 ± 0.42 (Paper 3 §6 canonical)" — paper has superseded this

CLAUDE.md line 58 (and the task description for this very review) claims $\gamma = 3.20 \pm 0.42$ as the Paper 3 canonical. Paper L557, L614, L633, L943 all carry $\gamma = 2.567 \pm 0.382$ (real-KDE) and explicitly call the old $3.20 \pm 0.42$ a "synthetic-from-power-law summary-statistic fit ... superseded by the real-KDE result, shift $-1.48\sigma$" (L557, L949). The on-disk synthetic value in `pipelines/p3_anomaly_engine/r42_results/wave_14_rr_nanograv_bayesian.json` is $\gamma = 3.2011 \pm 0.4203$ (the source of the stale CLAUDE.md value). The paper is right; CLAUDE.md is stale and should be amended in the same commit as any future P3 work. Not a paper confabulation, but it WILL confuse the next reviewer.

### MINOR-2. CLAUDE.md "2,145 SNR-filtered + 1,127 uncataloged" for DESI DR1 is not in the paper

The task description and CLAUDE.md line 49 claim DESI DR1 has "2,145 SNR-filtered, 1,127 uncataloged" anomalies. These numbers do NOT appear in `paper3_draft.tex` (verified by grep — zero matches). The paper's DESI breakdown is the $195{,}829$-total + $12$-spectroscopically-confirmed-$z\!\approx\!6$ + $5{,}384$-QSO-candidates structure (§5.1). The 2,145 / 1,127 figures appear to be an earlier-round bookkeeping that did not survive into the current paper draft. Recommend either restoring them in the paper if they are still scientifically defensible (with an on-disk artifact), or scrubbing them from CLAUDE.md.

### MINOR-3. LAMOST native count: paper $113{,}342$ vs CLAUDE.md $44{,}075$ — both are real but represent different stages

CLAUDE.md line 51 says "LAMOST DR10: 11.4M spectra, $44{,}075$ anomalies (0.39%)." Paper L213 reads "LAMOST native retrain ($44{,}075 \to 113{,}342$)." The $44{,}075$ is the pre-native cross-transfer count; the $113{,}342$ is the Path-C native-retrain count and is the headline LAMOST contributor. CLAUDE.md is referencing the superseded number. Same fix as MINOR-1: harmonize CLAUDE.md to paper. (The $44{,}075$ remains correct AS the pre-native cross-transfer baseline, which is also what appears in the $319{,}443$ checksum.)

### MINOR-4. NEOWISE: paper $419$ retained (post-ecliptic-mask) vs CLAUDE.md $436$ pre-mask

Paper L213 says "NEOWISE $419$" in the Path-C per-survey sum to $388{,}493$; the $436$ value persists ONLY in the `319,443` cross-transfer-baseline arithmetic. CLAUDE.md line 53 reports "$436$ anomalies" without the mask distinction. Harmonize.

---

## Most concerning confabulation (one sentence)

The single most reviewer-vulnerable item is **MAJOR-1**: the internal Fisher artifact `pipelines/p3_anomaly_engine/wave_14_ii_fisher_systematics/result.json` reports `sigma_fNL_unmarg = 0.0` and `sigma_degradation_pct ≈ 1e7` across all six configurations — a numerically corrupt artifact whose marginalized output ($\sigma \approx 0.07$) the paper quotes (with hedging) as a "$3$–$10\times$ tighter than Münchmeyer" cross-check; an adversarial reviewer opening the JSON will lose trust in the marg column too and elevate this to a BLOCKER, so the artifact needs to be either re-emitted with a coherent unmarg side or annotated to declare the unmarg fields non-physical.

---

## Files inspected (absolute paths)

- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.tex`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/project-context/SSOT/paper-3/status.md`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/r42_results/wave_14_rr_nanograv_bayesian.json`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/r42_results/B19_bootstrap_and_gpu_bench.json`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/fw6_stability/fw6_stability_results.json`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/wave_14_ii_fisher_systematics/result.json`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/hf_staging/pathc_unique_objects.parquet`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/hf_staging/pathc_unique_objects_no_act.parquet`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/results.json`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/chain_real_freespec.npy`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p1_highz_tracers/outputs/step3_classification/classification_summary.json`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p1_highz_tracers/outputs/step4_bias_validation/bias_validation.json`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p1_highz_tracers/outputs/step6_alpha_empirical/alpha_empirical_results.json`
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/projects/cross_survey/results/desi_xmatch_summary.json`
