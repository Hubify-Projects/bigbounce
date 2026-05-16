# P4_v1096 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0200pt_P4_v1096_R15_R-round_real
**Wall time**: 112.4s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=81893, completion=5637, reasoning=4142, total=87530

---

No BLOCKER-grade findings.

## PAPER-GPT-M1 — MAJOR — Conclusions; Abstract; Secs. `dipole`, `monopole_mask_null`

**Issue:** The manuscript still overstates the pre-/post-MASTER comparison as if MASTER alone collapses the same data vector to `-0.12σ`. The leakage diagnostic uses an un-monopole-subtracted CW-fraction map on the canonical mask, while the headline `-0.12σ` uses a monopole-subtracted CW-deficit map on a larger subsample mask; the like-for-like canonical post-MASTER value is `+1.85σ`, not `-0.12σ`.

| Truth-audit item | Manuscript statement | Audit verdict |
|---|---|---|
| Same input map? | Implied in Conclusions “same data” / “once MASTER applied” | False: map definition changes |
| Same mask? | Implied causal comparison | False: canonical `f_sky≈0.494` vs subsample `f_sky=0.659` |
| MASTER-alone removal? | “fully removed by MASTER” in several places | Overclaim: full chain is map choice + monopole subtraction + mask + MASTER |
| Like-for-like canonical result | Secondary | `+1.85σ`, not `-0.12σ` |

**Fix:** Replace all “same data / MASTER removes / collapses to `-0.12σ`” language with “after changing to the monopole-subtracted CW-deficit map, larger subsample mask, and MASTER deconvolution.” State explicitly that the canonical-mask post-MASTER residual is `+1.85σ` and is sub-threshold, not removed to `-0.12σ`.

## PAPER-GPT-M2 — MAJOR — Sec. `edge_on`, Table `face_on`

**Issue:** Table `face_on` reports a full Catalog C dipole of `+4.31σ` under a weighted-LSQ / monopole-preserving null, while the headline real-space dipole is `+0.43σ`. A factor-10 discrepancy cannot be dismissed as “estimator definition and null-sample variance” without a quantitative reconciliation.

| Truth-audit item | Value | Audit verdict |
|---|---:|---|
| Headline real-space dipole | `+0.43σ`, `p=0.30` | Null |
| Table `face_on` full Catalog C | `+4.31σ`, `p=0.001` | Formal detection under stated diagnostic |
| Claimed reconciliation | Different estimator/null | Insufficient; this is methodology-critical |
| HC-cut collapse | `+0.62σ`, `+0.87σ` | Useful diagnostic, but does not erase full-sample discrepancy |

**Fix:** Recompute Table `face_on` with the exact headline Healpix dipole estimator and `N_MC=10,000` per-pixel-shuffle null, or provide an explicit derivation showing why the LSQ statistic is not a dipole-significance estimator. Until then, do not cite the full-sample `+4.31σ` table as reconciled.

## PAPER-GPT-M3 — MAJOR — Secs. `hemisphere`, `hemisphere_disc`; Fig. `hemisphere`

**Issue:** The hemisphere look-elsewhere interpretation is internally contradictory. The analytic Bonferroni/BH treatment says the local `3.05σ` peak becomes `<1σ`, while the direct max-statistic MC gives zero exceedances in 10,000 shuffles (`p_LEE≤10^-4`), i.e. rejection of the random-label null.

| Truth-audit item | Manuscript value | Audit verdict |
|---|---:|---|
| Local hemisphere peak | `3.05σ` | OK |
| Bonferroni/BH over ~650 directions | `<1σ` | OK only for independent-bin parametric approximation |
| Direct max-stat MC | `p_LEE≤10^-4` | Rejects random-label null |
| “Consistent with null after LEE” | Repeated in prose/captions | Overclaim unless “null” is redefined as systematics-preserving |

**Fix:** Make the direct MC max-statistic the primary LEE result for the random-label null: “random-label null rejected; not interpreted cosmologically because systematics-preserving null is absent and other dipole estimators are null.” Remove claims that the hemisphere statistic is simply “post-LEE consistent with null.”

## PAPER-GPT-m1 — minor — Sec. `sensitivity`; Conclusions item 1

**Issue:** The amplitude convention remains too tangled. The text alternates between half-modulation `A/2` floors (`0.14–0.2%`) and full-amplitude `A` floors (`0.29–0.4%`), then compares these to the `0.26%` monopole and `0.75%` injection threshold.

| Truth-audit item | Correct value | Manuscript risk |
|---|---:|---|
| Model | `p_CW = 1/2(1 + A cosθ)` | OK |
| 1σ Fisher on full `A`, full catalog | `sqrt(3/N)≈0.097%` | Sometimes stated via `A/2` |
| 3σ Fisher on full `A` | `≈0.29%` | Correct in abstract/conclusions, muddled in derivation |
| HC injection 50%-rec threshold | `A≈0.75%` full amplitude | OK |

**Fix:** Rewrite the sensitivity derivation entirely in full-amplitude `A` units; mention `A/2` only once parenthetically. Delete standalone “`0.2%` minimum detectable dipole” phrasing unless explicitly labeled as half-modulation.

## PAPER-GPT-m2 — minor — Sec. `comparison` / Shamir sample-size framing

**Issue:** The Shamir 2022 comparator arithmetic is inconsistent. The text says this paper’s `3.20M` spiral sample is `~2.5×` larger than Shamir’s DESI Legacy “spiral sample” while also describing that spiral subset as `~200,000`; `3.20M / 0.20M ≈ 16×`, not `2.5×`.

| Truth-audit item | Value | Audit verdict |
|---|---:|---|
| Present spiral count | `3,201,160` | OK |
| Shamir DESI total analyzed claim | `~1.3M` | Ratio `~2.5×` |
| Shamir Ganalyzer spiral subset as written | `~200k` | Ratio `~16×` |
| Current wording | Calls `~2.5×` a spiral-sample comparison | Arithmetic error |

**Fix:** Say either “`~2.5×` larger than Shamir’s total DESI analyzed catalog” or “`~16×` larger than the `~200k` Ganalyzer-spiral subset.” Do not mix the denominators.
