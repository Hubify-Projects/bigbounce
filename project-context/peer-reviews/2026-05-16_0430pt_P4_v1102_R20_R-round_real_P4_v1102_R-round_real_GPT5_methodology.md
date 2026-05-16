# P4_v1102 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0430pt_P4_v1102_R20_R-round_real
**Wall time**: 106.9s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=84155, completion=6022, reasoning=4142, total=90177

---

# Review

## PAPER-GPT-B1 — BLOCKER — Primary real-space dipole estimator is internally inconsistent

**Location:** Abstract; Sec. `Dipole Analysis`; Sec. `Edge-On Galaxy Contamination`, Table `face_on`.

**Issue:** The same Catalog C full-sample real-space dipole is reported as `+0.43σ, p=0.30` and also as `+4.31σ, p=0.001`. The paper’s explanation (“different estimator/null”) is not acceptable for two quantities both used as dipole significances on the same data; this invalidates the headline “real-space dipole null” until the estimator hierarchy is made mathematically unique.

**Fix:** Declare one primary real-space dipole estimator and rerun every stratified/HC/systematics table with that same estimator and null. Move the other estimator to a diagnostic appendix only after showing by injection tests why it gives a 10× different significance.

| Truth audit | Check | Verdict |
|---|---:|---|
| Abstract headline | real-space dipole `0.43σ`, `p=0.30` | claimed null |
| Table `face_on` full Catalog C | `+4.31σ`, `p=0.001` | detection-like |
| Claimed reconciliation | estimator/null difference | insufficient |
| Severity | affects primary conclusion | **BLOCKER** |

## PAPER-GPT-M1 — MAJOR — MASTER “collapse” is not a like-for-like deconvolution result

**Location:** Abstract; Sec. `Dipole Analysis`; Table `multipole`; Sec. `NaMaster MASTER configuration`; Conclusions Table `l1_estimators`.

**Issue:** The manuscript repeatedly frames `+6.48σ → -0.12σ` as MASTER removal, but the two numbers differ in map definition, monopole subtraction, mask, and even mode/bin (`ℓ_eff=4`, `ℓ∈[2,6]` vs single `ℓ=1`). “Canonical” `f_sky` also drifts between `0.49005`, `0.491`, and `0.494`, with inconsistent `N_pix` values.

**Fix:** Present separate tables for each exact data vector: map, mask, monopole treatment, `N_pix`, `f_sky`, binning, null mean, and null std. Stop describing non-identical-input comparisons as a MASTER deconvolution collapse.

| Truth audit | Check | Verdict |
|---|---:|---|
| Pre-MASTER diagnostic | raw/asymmetry or CW-fraction maps, canonical mask | not same input |
| Headline post-MASTER | monopole-subtracted CW-deficit, subsample mask | not same input |
| Mode comparison | `ℓ_eff=4` bandpower vs single `ℓ=1` | not like-for-like |
| `f_sky` canonical | `0.49005 / 0.491 / 0.494` | propagation residual |
| Severity | methodological traceability | **MAJOR** |

## PAPER-GPT-M2 — MAJOR — Hemisphere look-elsewhere/statistical framing is invalid

**Location:** Sec. `Hemisphere Asymmetry`; Fig. `hemisphere`; Sec. `hemisphere_disc`; Table `monopole_mask_null`.

**Issue:** The direct max-over-directions MC gives `p_LEE ≤ 10^-4`; that already includes the look-elsewhere scan for its statistic. The paper then quotes a separate Bonferroni/BH result on a different grid/null to claim `<1σ` consistency, which is not a valid dilution of the direct-MC result. The monopole-only null also leaves a `+4.42σ` hemisphere residual.

**Fix:** Choose one primary hemisphere statistic and one null. If the direct MC is primary, report the hemisphere channel as a rejected random-label null / unresolved systematic, not “consistent with null”; add a depth/PSF/morphology-preserving null before using it as a null diagnostic.

| Truth audit | Check | Verdict |
|---|---:|---|
| Direct MC max-stat | `0/10000` nulls exceed data | random-label null rejected |
| Analytic Bonferroni/BH | different grid/null | not comparable |
| Monopole-only residual | `+4.42σ` | not exhausted by monopole |
| Claimed null consistency | uses incompatible correction | invalid |
| Severity | overclaims null in secondary sky statistic | **MAJOR** |

## PAPER-GPT-M3 — MAJOR — Sensitivity/upper-limit claims mix samples and amplitude conventions

**Location:** Title; Abstract; Sec. `Sensitivity`; Conclusions item 1; Data Availability limitations.

**Issue:** The operational `0.75%` 50%-recovery-at-`3σ` threshold is measured only on the HC-spiral subsample (`N=471,049`), not on the full `3.2M` catalog. The paper correctly notes this in places, but still uses the value as the catalog-level empirical sensitivity in headline prose; the full-catalog systematic-inclusive injection sweep is explicitly deferred.

**Fix:** Headline the `0.75%` threshold as “HC-subsample only.” For the full catalog, quote only the ideal Fisher floor (`≈0.29%` full-amplitude at `3σ`) and state that the empirical full-catalog systematic-inclusive threshold is unmeasured.

| Truth audit | Check | Verdict |
|---|---:|---|
| Injection sample | `N=471,049` HC spirals | not full catalog |
| Full catalog empirical sweep | deferred | unavailable |
| HC Fisher floor | `3√(3/471049)=0.76%` | matches `0.75%` |
| Full Fisher floor | `≈0.29%` | ideal only |
| Headline wording | often catalog-level | overclaim |
| Severity | sensitivity/upper-limit interpretation | **MAJOR** |

## PAPER-GPT-M4 — MAJOR — GZ1 validation denominators are inconsistent after training exclusion

**Location:** Sec. `Training Labels`, paragraph `Independent GZ1 cross-match`; Catalog B GZ1 validation paragraph; Abstract validation summary.

**Issue:** The text says `240,919` GZ1 objects cross-match, then excludes `6,637` training objects, leaving `234,282` external matches, but reports “independent” three-class accuracy as `141,438/240,919`. This denominator mismatch affects the load-bearing external accuracy, κ, and downstream dilution model.

**Fix:** Recompute and report all GZ1 metrics strictly on the training-disjoint set, with exact denominators for three-class accuracy, spiral-only CW/CCW agreement, κ, McNemar, and confidence intervals. Do not describe the Platt refit as “consistent” when its accuracy is `0.519`; call it uninformative.

| Truth audit | Check | Verdict |
|---|---:|---|
| Cross-match total | `240,919` | before exclusion |
| Training objects excluded | `6,637` | stated |
| External denominator | should be `234,282` | stated |
| Reported accuracy denominator | `240,919` | inconsistent |
| Severity | classifier validation / dilution budget | **MAJOR** |

## PAPER-GPT-m1 — minor — Parity and `w(θ)` fixes are mathematically correct, but parity language still leaks into dipole claims

**Location:** Title; Introduction; Sec. `wtheta`; Sec. `dipole_symmetry_caveat`; Conclusions.

**Issue:** The corrected parity rule `A^P(n)=-A(-n)` and coefficient transformation `a^P_{\ell m}=(-1)^{\ell+1}a_{\ell m}` are correct; the `w_CW(θ)=⟨A A⟩` classification as parity-even is also correct. But title/prose still repeatedly attach “parity violation/symmetry” to the `ℓ=1` dipole and pseudo-`C_ℓ` powers, which are isotropy/systematics diagnostics, not direct parity-odd tests.

**Fix:** Retitle/rephrase headline claims as “no large-scale chirality anisotropy / no isotropy-breaking chirality dipole.” Reserve “parity violation” for signed parity-odd observables or explicitly model-dependent transfer-function discussion.

| Truth audit | Check | Verdict |
|---|---:|---|
| Parity rule | `A^P(n)=-A(-n)` | correct |
| Harmonic sign | `(-1)^{ℓ+1}` | correct |
| `ℓ=1` dipole | parity-even axial-vector | correct in caveat |
| `w_CW(θ)` | parity-even two-point statistic | correct |
| Residual wording | title/conclusions still parity-loaded | minor residual |
