# P4_v1098 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0230pt_P4_v1098_R16_R-round_real
**Wall time**: 90.3s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=83416, completion=5907, reasoning=4142, total=89323

---

## PAPER-GPT-B1 — BLOCKER — Sec. “Edge-On Galaxy Contamination”, Table `face_on`

| Truth audit | Paper claim/site | Observed in text | Verdict |
|---|---|---:|---|
| Headline real-space dipole | Sec. `dipole`, abstract, conclusions | `+0.43σ`, `p=0.30` | Claimed null |
| Same full Catalog C data, alternate real-space estimator | Table `face_on` | `+4.31σ`, `p=0.001` monopole-preserving; `+4.43σ`, `p=0.001` isotropic | Significant |
| Reconciliation | paragraph after Table `face_on` | “different estimators/null-sample variance” | Not adequate for 10× z discrepancy |

Concrete issue: The paper contains an unreconciled full-sample dipole detection at `+4.31σ` on the same Catalog C data while the headline says the real-space dipole is `+0.43σ`. Estimator choice/null variance cannot be hand-waved; one estimator is invalid or the headline null is conditional on rejecting a significant statistic.

Fix: Recompute both estimators on identical maps, masks, weights, amplitude conventions, and MC nulls; show amplitudes and covariance. If the LSQ statistic is invalid, remove it; if valid, the headline must become “systematic-contaminated full-sample dipole, HC cuts collapse it,” not an unconditional null.

## PAPER-GPT-M1 — MAJOR — Sec. “Sensitivity Floor and Minimum Detectable Signal”

| Truth audit | Paper claim/site | Observed in text | Verdict |
|---|---|---:|---|
| v1.0.98 closure | Abstract | HC empirical `0.75%` vs HC Fisher `0.76%`, ratio `≈1.0`; full-catalog comparison not meaningful | Correct |
| Regression | Sensitivity paragraph after Table `mc_injection` | “`~2.5×` gap between analytic Fisher floor and empirical MC threshold is the standard Fisher-vs-empirical factor” | Wrong / closure regressed |
| Relevant samples | Injection sweep | HC-spiral `N=471,049` | Not full catalog |
| Like-for-like Fisher | Abstract | `3√(3/N)=0.76%` | Matches empirical |

Concrete issue: The body still frames the `0.75%` empirical threshold as a Fisher-vs-empirical degradation relative to a full-catalog/half-amplitude Fisher floor. That is the deleted cross-sample arithmetic error.

Fix: Delete the `~2.5×` sentence. State only: HC injection threshold `0.75%` tracks the HC Fisher floor `0.76%`; no full-catalog systematic-inclusive injection threshold is measured.

## PAPER-GPT-M2 — MAJOR — Canonical-mask `f_sky` propagation

| Truth audit | Site | Value in text | Verdict |
|---|---|---:|---|
| Canonical JSON anchor | Table `monopole_mask_null` caption | `f_sky=0.49005` | Correct |
| Headline summary | Table `headline_summary` rows iii–v | `0.494` | Stale/inconsistent |
| Multipole caption | Table `multipole` | `0.4938`, `0.491` | Inconsistent |
| Conclusions | Table `l1_estimators` | `0.494`, `0.491` | Inconsistent |
| NaMaster appendix | Mask bullet | canonical `0.494` | Inconsistent |

Concrete issue: The canonical-mask sky fraction is not propagated. The paper alternates among `0.49005`, `0.491`, `0.4938`, and `0.494` without a mask-version table proving these are distinct products.

Fix: Add a single mask-definition table with artifact filename, pixel count, cut, apodization, and exact `f_sky`; update every canonical-mask site to `0.49005` unless it is demonstrably a different mask.

## PAPER-GPT-M3 — MAJOR — Parity/isotropy overclaim remains

| Truth audit | Site | Text pattern | Verdict |
|---|---|---|---|
| Symmetry caveat | Sec. `dipole_symmetry_caveat` | `ℓ=1` dipole is parity-even; tests isotropy | Correct |
| Contradictory conclusion | Conclusions item 1 | “parity-preference observable would be the dipole component, not the monopole” | Wrong |
| Body/captions | Intro, Motloch comparison, conclusions, captions | “null parity violation”, “parity-dipole”, “parity symmetry” for `ℓ=1` | Overclaim |

Concrete issue: The paper still repeatedly treats the `ℓ=1` dipole as a parity-violation observable, contradicting its own symmetry derivation. For the projected pseudoscalar chirality field, the dipole is parity-even; pseudo-`C_\ell` powers are parity-sign-blind.

Fix: Replace body-wide “parity-violating dipole/parity symmetry/parity-preference dipole” language with “isotropy-breaking axial-vector projection / chirality anisotropy.” Reserve parity-odd claims for signed monopole/even-`ℓ` diagnostics only.

## PAPER-GPT-M4 — MAJOR — v1.0.98 public-surface closure regressions

| Truth audit | Required closure | Site | Observed | Verdict |
|---|---|---|---|---|
| Data/code tag | `paper4-v1.0.98` | GZ1 footnote; Data Availability | `paper4-v1.0.97` | Regressed |
| Iye 2026 public status | arXiv `2605.05570`, no “in preparation” | Sec. `comparison` | “anticipated… remains in preparation” | Regressed |
| HC-broad nomenclature | `HC-broad-0.6` for 949,584 cut | Sec. `confidence`, `edge_on`, `bin_flatness` | still uses `HC-spiral_p>0.6` / “HC-spiral subsample N=949,584” and contradictory “counts confident-NS” text | Inconsistent |

Concrete issue: Several public-surface closures do not hold in the manuscript. This will fail the next external-surface crawl.

Fix: Update all release-tag prose/URLs to `paper4-v1.0.98`; remove “in preparation” language for Iye & Yagi 2026 and cite arXiv directly; standardize the 949,584 cut as `HC-broad-0.6` with one exact definition.

## PAPER-GPT-M5 — MAJOR — MASTER/mask-chain claims overstate what is demonstrated

| Truth audit | Site | Observed | Verdict |
|---|---|---|---|
| Abstract/conclusions claim | “MASTER decoupling drives residual to `-0.12σ`” | Compares different map, mask, monopole subtraction, and null | Not like-for-like |
| Table `multipole` | low-`ℓ` rows after stated MASTER context | `+2` to `+6σ`, joint `χ²/dof=161.2/38` | Not “fully removed” |
| Monopole null | Table `monopole_mask_null` | pre-MASTER un-subtracted CW-fraction map reproduces `99.3%` | Diagnostic only |
| Canonical direct MC | Conclusions | canonical `ℓ=1` is `+1.85σ`, `p=0.030` | Mild excess remains |

Concrete issue: The paper repeatedly says MASTER “fully removes” the raw pseudo-`C_\ell` excess, but the quoted collapse uses a changed data vector and mask, while canonical low-`ℓ` bandpowers remain highly discrepant. This is not a clean before/after deconvolution demonstration on identical inputs.

Fix: Present a strict same-map/same-mask pre- vs post-MASTER table with null means/covariance. Rephrase the headline as conditional on the monopole-subtracted subsample-mask estimator; do not claim MASTER alone removes the canonical-mask leakage.
