# P4_v1101 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0400pt_P4_v1101_R19_R-round_real
**Wall time**: 132.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=83526, completion=8462, reasoning=6732, total=91988

---

## PAPER-GPT-B1 — BLOCKER — Sec. Abstract; Sec. “Monopole+Mask Leakage Generative Null”; Table `monopole_mask_null`; Conclusions

**Issue:** The central “99.3% monopole-mask leakage” claim does not isolate the *classifier monopole* (`p_CW-0.5≈-0.0026`). The diagnostic uses the **un-monopole-subtracted CW-fraction map** `f_CW≈0.4974`, so the pseudo-`C_1` is dominated by leakage of the trivial DC level `≈0.5` through the mask. A parity-perfect `p_CW=0.5` null would reproduce essentially the same power; the classifier-monopole differential is only order `(0.4974/0.5)^2−1≈−1.0%` in power, not “99.3% of the observed power.”

**Fix:** Recompute the leakage diagnostic on `f_CW−0.5` or `A_p=2f_CW−1`, and report a paired `p=0.5` vs `p=0.4974` control. Attribute only the *differential* pseudo-power to the classifier monopole; otherwise call the current result “unsubtracted-DC mask leakage,” not a sub-percent classifier-monopole leakage channel.

| Truth audit | Verdict |
|---|---|
| Paper claim: small CW/CCW classifier monopole explains 99.3% of pre-MASTER `C_1` | False / not demonstrated |
| What current statistic proves | A nonzero mean fraction map leaks through a cut-sky mask |
| Blocking reason | This is the paper’s central mechanism and abstract-level claim |

## PAPER-GPT-M1 — MAJOR — Sec. Hemisphere Asymmetry; Sec. Hemisphere Discussion; Sec. Sensitivity; estimator hierarchy

**Issue:** The paper admits the direct max-over-directions random-label MC rejects the null at `p_LEE≤10^-4`, then continues using random-label / per-pixel-shuffle nulls as load-bearing calibration for dipole significances and injection recovery while calling the `0.75%` threshold “systematic-inclusive.” If the random-label null fails because it destroys depth/PSF/morphology/mask-edge label correlations, the same null family cannot support systematic-inclusive sensitivity claims without a systematics-preserving replacement.

**Fix:** Downgrade all such significances/thresholds to “conditional on random-label/per-pixel-shuffle null.” Add a systematics-preserving null stratified or blocked by imaging leg, depth, PSF, morphology, confidence, and mask edge distance before claiming systematic-inclusive sensitivity.

| Truth audit | Verdict |
|---|---|
| Paper claim: per-pixel/random-label MC gives systematic-inclusive threshold | Not supported |
| Paper’s own evidence | Random-label max-statistic null is rejected at `p≤10^-4` |
| Required closure | Systematics-preserving null or explicit downgrade |

## PAPER-GPT-M2 — MAJOR — Sec. `tta`; Conclusions “D4-TTA rotational-equivariance validation”

**Issue:** The manuscript correctly states the `N=1558` `D_4` holdout has a Poisson floor of `±1.3%` and cannot test the catalog’s `0.26%` monopole, but the Conclusions then say it “explicitly addresses” whether the `9.5σ` monopole survives `D_4` and answers yes. That is an overclaim; the holdout only rules out large percent-level rotation effects and shows a `1.35%` argmax CW-fraction shift on a small sample.

**Fix:** Replace the conclusion with: “The holdout is underpowered for the `0.26%` monopole; full-catalog or ≥`10^5` stratified `D_4` inference remains open.” Do not use the holdout as validation of full-catalog rotational invariance.

| Truth audit | Verdict |
|---|---|
| Paper caveat: holdout cannot resolve `0.26%` | True |
| Paper conclusion: holdout answers the monopole-survival question | False |
| Required closure | Larger `D_4` run or downgrade |

## PAPER-GPT-M3 — MAJOR — Sec. `dipole_symmetry_caveat`; Abstract; Table III caption; Conclusions

**Issue:** The parity/dipole cleanup is incomplete. The paper correctly says the `ℓ=1` chirality dipole is parity-even and tests anisotropy, but still uses “dipole-parity null,” “parity symmetry” for the post-MASTER `ℓ=1` result, “cosmological-principle parity test,” and “parity signal” language around `C_ℓ`/dipole diagnostics. That reattaches parity-violation interpretation to the dipole channel.

**Fix:** Globally replace dipole-channel language with “isotropy-breaking axial-vector dipole” or “anisotropy test.” Reserve “parity-odd” for signed monopole/even-`ℓ` diagnostics, not `|a_{ℓm}|^2` bandpowers or the `ℓ=1` dipole.

| Truth audit | Verdict |
|---|---|
| Paper’s symmetry derivation | Correct |
| Terminology elsewhere | Still inconsistent |
| Required closure | Global terminology pass |

## PAPER-GPT-M4 — MAJOR — Sec. Sensitivity; Table `mc_injection`; Conclusions

**Issue:** Sensitivity statements remain internally over-complicated and partly inconsistent. The only operational injection result is on the `N=471,049` HC subsample with `50%`-recovery near `A=0.75%`; the full `3.2M` catalog has only a Fisher floor (`≈0.29%` full-amplitude ideal, `≈0.4%` conservative with mask inflation), not an empirical full-catalog threshold. Several prose sites still blur “statistical floor,” “upper bound,” “systematic-inclusive,” and “minimum detectable dipole.”

**Fix:** Add one sensitivity table with four rows only: full-catalog Fisher ideal, full-catalog conservative Fisher, HC Fisher, HC empirical injection. State explicitly: “No full-catalog empirical injection threshold is measured.” Remove or subordinate all standalone `0.2%` “minimum detectable” prose.

| Truth audit | Verdict |
|---|---|
| HC empirical threshold `A≈0.75%` | Supported |
| Full-catalog empirical threshold | Not measured |
| Full-catalog Fisher floor | Theoretical only |

## PAPER-GPT-M5 — MAJOR — Multiple closure-regression numerical inconsistencies

**Issue:** Several numerical regressions remain:
- Sec. prereg / Conclusions canonical-MASTER argument: `P(σ>2)` at `A=0.5%` is quoted as `0.18`, but Table `mc_injection` gives `0.35`.
- Conclusions item 1: `P(σ>3)` at `A=0.75%` is quoted as `0.50`, but Table gives `0.55`.
- Sec. Comparison with Shamir: says `3.2M` is `~2.5×` larger than a `~200,000` Shamir spiral sample; that ratio is `~16×`. If using `1.3M`, then `~2.5×` is correct, but it is not the `200k` spiral count.
- Sec. `tta`: full `D_4` cost is described as `~72×` current single-flip throughput, while elsewhere it is `4×` augmentations / about `72 h`; `72×` is dimensionally wrong.

**Fix:** Reconcile every quoted probability and ratio directly from the frozen JSON artifacts; use one Shamir denominator consistently; change `72×` to `~4× compute` or `~72 h`, whichever is intended.

| Truth audit | Verdict |
|---|---|
| Table values | Internally authoritative |
| Prose values | Mixed stale snapshots |
| Required closure | One artifact-driven numerical pass before external review |
