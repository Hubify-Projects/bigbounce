# /never-fabricate-derivation — anomaly flagship @ vAF.0.2

**Run:** 2026-09-19 · **Lane:** LA-anomaly-draft · **Mode:** `--strict`
**Target:** `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.tex`
**Diff base:** `c7d40bda` (vAF.0.1 skeleton). `main.tex` is a full rewrite at
vAF.0.2, so the added-lines diff degenerates to the whole file and the scan was
run whole-file (the skill's `--tex` path), not hunk-wise.

## Trigger sweep

| Line | Trigger | Context | Verdict |
|---|---|---|---|
| 48–50 | `[0-9]+!` | `linkcolor=blue!60!black` etc. | **FALSE POSITIVE** — `hyperref` colour syntax, not a factorial |
| 166 | `follows from` | "The framing follows from the benchmark." | **OK** — editorial, not a math claim; the benchmark it refers to is Sec.~V D with its own table and artifact |

## Math content of the manuscript

The manuscript contains exactly one display equation, Eq.~(1), the anomaly-score
definition $S = (\overline{\mathrm{MSE}} - \mu_{\rm MSE})/\sigma_{\rm MSE}$. It is
**not** a derived result: it is transcribed from the sealed calibration artifact's
own `anomaly_score_definition` field
(`pipelines/p1_highz_tracers/clean_rerun/sealed_2026-08-05/calibration.json`), and the
constants $(\mu_{\rm MSE}, \sigma_{\rm MSE}) = (0.8771, 1.3605)$ come from the same
file. The stability-check inequality quoted beside it is the artifact's own
`stability_check.rule` string, with its `observed_deviation` and `bound` values.

The only other quantitative relation asserted in prose is
$\lambda_{\rm obs} = \lambda_{\rm rest}(1+z)$ applied to Lyman-$\alpha$
(§VII B). It now carries an inline `% derivation:` stamp naming the per-object
computation (`make_draft_figures.py` → `outputs/draft_numbers.json`
`ft_a.lya_observed_angstrom`) and explicitly labels the quoted DECam band edges
as approximate and qualitative.

Every other number in the manuscript is a **read**, not a derivation: each carries a
trailing `%` comment naming the committed artifact it came from (see the provenance
block at the head of `main.tex`), and the derived ones are emitted by
`make_draft_figures.py` into `outputs/draft_numbers.json`.

## VERDICT: **CLEAN** — no closure-added math claim lacking citation, in-paper
derivation, or computation stamp. Three preamble false positives, listed above.
