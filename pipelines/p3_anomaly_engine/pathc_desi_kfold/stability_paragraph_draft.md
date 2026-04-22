# Paper 3 §3.1 (`sec:desi`) — DESI k-fold stability paragraph draft

**Status:** DRAFT · authored fire #153 · ready-to-insert pending the on-pod A100 5-fold
run (criterion #4 launch step, SDSS-gated). Numeric TBD placeholders are bracketed
`[TBD-<slug>]` and must be filled from `outputs/desi_kfold/kfold_stability_summary.json`
(produced by `aggregate_kfold.py`) + the 5 per-fold `training_log.json` files
(produced by `train_desi_kfold.py`) before recompile.

**Insertion point:** `pipelines/p3_anomaly_engine/paper3_draft.tex`, at the end of
`\subsection{DESI DR1}\label{sec:desi}` (around L236 before the high-$z$ QSO
paragraph) OR as a new `\paragraph{Path-C $k$-fold stability.}` block inside
`\subsection{Path-C Native-Retrain Rebuild}\label{sec:pathc}` near the SDSS +
LAMOST + CMB supersession paragraphs — the latter is preferred so the whole
Path-C story stays in one section.

---

## Draft text (LaTeX-ready, placeholders bracketed)

```latex
\paragraph{Path-C $k$-fold stability for DESI DR1.}\label{par:desi_kfold}
The DESI DR1 anomaly catalog is the one survey of the eight whose native-trained
autoencoder reports \emph{in-sample} scores: the $47{,}000$ normal-spectrum
training sample is drawn from the same $22.5\times 10^{6}$-spectrum parent
population that is then scored, so a naive top-$1\%$ threshold cannot disentangle
``out-of-distribution with respect to the training manifold'' from ``fit
imperfection on the training sample itself.'' We therefore cross-validate the
DESI headline under a $5$-fold holdout protocol: we partition the $47{,}000$
training sample into $5$ disjoint folds at seed $20{,}260{,}420$
($\texttt{np.array\_split}$, fold sizes $=9{,}400$ each, all disjointness
and reproducibility invariants verified in
\texttt{fold\_split\_dryrun.json}), train a fold-specific
$\BigAE{}(n_{\text{in}}=496,\,n_{\text{lat}}=128)$ on the $37{,}600$-spectrum
complement under a $90/10$ inside-train/inside-validation split with the same
architecture, optimiser, and early-stop patience-$5$ schedule as the published
DESI native training, and require $\text{val\_loss}\le 0.30$ (identical gate
to the SDSS and LAMOST native retrains for apples-to-apples comparison).
Each of the $5$ fold checkpoints is then inference-scored across the full
$22.5\times 10^{6}$-spectrum DESI DR1 catalog, producing $5$ parallel
$(\texttt{source\_id},\texttt{ra},\texttt{dec},\texttt{anomaly\_score})$ tables
for pairwise comparison. The resulting per-fold validation losses are
$\langle \text{val\_loss}\rangle = $[TBD-valloss-mean]$\pm$[TBD-valloss-std]
(min $=$[TBD-valloss-min], max $=$[TBD-valloss-max]), with all $5$ folds
[TBD-gate-word-pass-or-fail] the $0.30$ convergence gate; the fold-mean
agrees with the published non-$k$-fold DESI training
value~\cite{Golden:2026anomaly} to within [TBD-valloss-delta-to-published].

Cross-fold stability is quantified via the pairwise Jaccard similarity
$J_{ij} = |A_i \cap A_j| / |A_i \cup A_j|$ of the top-$1\%$ anomaly sets
$A_k = \{\text{top $225{,}049$ sources by }\texttt{anomaly\_score}_k\}$
extracted from each of the $5$ fold-score tables
($5 \choose 2$ $=10$ pairs). The mean pairwise Jaccard is
$\bar{J} = $[TBD-jaccard-mean] (min $=$[TBD-jaccard-min],
max $=$[TBD-jaccard-max]), with the fold-consensus set (sources appearing
in $\ge 3/5$ fold top-$1\%$ lists) containing [TBD-consensus-n] objects
([TBD-consensus-fraction-of-union]\% of the union of the $5$ fold top-sets).
We adopt the same gate semantics encoded in the
\texttt{aggregate\_kfold.py} interpretation field: $\bar{J} \ge 0.70$
(strong stability) implies the published $195{,}829$-anomaly DESI headline
stands unchanged under training-sample reshuffling;
$0.50 \le \bar{J} < 0.70$ (moderate stability) implies the headline stands
but is reported alongside the consensus-set count as a stability footnote;
$\bar{J} < 0.50$ (weak stability) would require the headline switch from
the single-training-sample top-$1\%$ count to the fold-consensus count.
The measured $\bar{J} = $[TBD-jaccard-mean] places the DESI DR1 selection
in the [TBD-stability-bucket] regime, and
[TBD-headline-implication-sentence].

The full protocol, per-fold validation losses, and per-pair Jaccard matrix
are provided in the \texttt{pipelines/p3\_anomaly\_engine/pathc\_desi\_kfold/}
directory of the companion repository; the $5$ per-fold score parquets
and the consensus-set parquet are deposited on HuggingFace as
\texttt{desi\_dr1\_pathc\_kfold\_fold\_\{0--4\}\_scores.parquet} and
\texttt{desi\_dr1\_pathc\_kfold\_consensus.parquet} alongside the other
Path-C artefacts (\S\ref{sec:data-availability}).
```

---

## Placeholders and their on-pod sources (fill-in checklist)

| Placeholder                          | Source file                                                                 | Field                          | Example (Scenario B synthetic dry-run fire #150) |
|--------------------------------------|-----------------------------------------------------------------------------|--------------------------------|--------------------------------------------------|
| `[TBD-valloss-mean]`                 | `outputs/desi_kfold/training_summary.json`                                  | `best_val_mean`                | `0.XXX`                                          |
| `[TBD-valloss-std]`                  | `outputs/desi_kfold/training_summary.json`                                  | `best_val_std`                 | `0.XXX`                                          |
| `[TBD-valloss-min]`                  | `outputs/desi_kfold/training_summary.json`                                  | `min(per_fold[k].best_val)`    | `0.XXX`                                          |
| `[TBD-valloss-max]`                  | `outputs/desi_kfold/training_summary.json`                                  | `max(per_fold[k].best_val)`    | `0.XXX`                                          |
| `[TBD-gate-word-pass-or-fail]`       | `outputs/desi_kfold/training_summary.json`                                  | `all_folds_pass_gate`          | `PASS` / `FAIL`                                  |
| `[TBD-valloss-delta-to-published]`   | difference vs `best_val` in published DESI training log                     | computed                       | `< 0.01`                                         |
| `[TBD-jaccard-mean]`                 | `outputs/desi_kfold/kfold_stability_summary.json`                           | `mean_pairwise_jaccard`        | `0.856` (PASS scenario B)                        |
| `[TBD-jaccard-min]`                  | `outputs/desi_kfold/kfold_stability_summary.json`                           | `min_pairwise_jaccard`         | `0.818`                                          |
| `[TBD-jaccard-max]`                  | computed from `pairwise_jaccard` matrix                                     | `max(off-diag)`                | `0.890`                                          |
| `[TBD-consensus-n]`                  | `outputs/desi_kfold/kfold_stability_summary.json`                           | `counts.consensus_ge_3_of_5`   | `99`                                             |
| `[TBD-consensus-fraction-of-union]`  | `outputs/desi_kfold/kfold_stability_summary.json`                           | `consensus_fraction_of_union`  | `0.847`                                          |
| `[TBD-stability-bucket]`             | derived from `gate_pass` + mean_jacc bucket                                 | `strong` / `moderate` / `weak` | `strong` (if $\ge 0.70$)                         |
| `[TBD-headline-implication-sentence]`| choose from the three-branch gate semantics                                 | see below                      | see below                                        |

### Three-branch headline implications (pick one at fill-in time)

- **Strong ($\bar{J} \ge 0.70$):** "…so the $195{,}829$-anomaly headline count
  reported in Table~\ref{tab:survey_summary} stands unchanged under training-sample
  reshuffling, and the [TBD-consensus-n] fold-consensus sources are flagged as
  maximally robust sub-selection for SPHEREx follow-up."
- **Moderate ($0.50 \le \bar{J} < 0.70$):** "…so the $195{,}829$-anomaly headline
  count reported in Table~\ref{tab:survey_summary} is retained but accompanied
  by a stability footnote reporting the fold-consensus count
  [TBD-consensus-n] as the training-sample-reshuffle-robust sub-selection."
- **Weak ($\bar{J} < 0.50$):** "…so the DESI DR1 Table~\ref{tab:survey_summary}
  entry is \emph{updated} from the single-training-sample $195{,}829$-anomaly
  count to the fold-consensus count [TBD-consensus-n]; all downstream
  cross-survey products (SIMBAD novelty, dedup, multi-tracer Fisher forecast)
  are re-computed on the consensus subset."

---

## Integration checklist (post-launch fire)

1. Run `train_desi_kfold.py` (5 fold × ~30 min = ~2.5 GPU-h on A100).
2. Run `score_desi_kfold.py` (5 fold × ~25 min = ~2.1 GPU-h on A100).
3. Run `aggregate_kfold.py` on the 5 `fold_{k}_scores.parquet` files
   (local CPU, ~60 s).
4. Read `training_summary.json` + `kfold_stability_summary.json` +
   per-fold `training_log.json` and fill the 12 placeholders above.
5. Pick one of the three-branch headline-implication sentences based on
   `gate_pass` + bucket.
6. Insert the filled paragraph into `paper3_draft.tex` (preferred:
   as `\paragraph{Path-C $k$-fold stability for DESI DR1.}` inside
   `sec:pathc`, after the LAMOST native-rescore paragraph around L336 –
   keeps all Path-C supersession narrative in one section).
7. Trigger the criterion #9 recompile (gated on this + SDSS native
   rescore + Table 1 numeric row refresh).
8. Upload `desi_dr1_pathc_kfold_fold_{0..4}_scores.parquet` +
   `desi_dr1_pathc_kfold_consensus.parquet` to the HuggingFace Path-C block
   (criterion #10 final push).
