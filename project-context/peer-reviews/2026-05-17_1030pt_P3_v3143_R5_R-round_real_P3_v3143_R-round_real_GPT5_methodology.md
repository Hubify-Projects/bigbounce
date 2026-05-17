# P3_v3143 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_1030pt_P3_v3143_R5_R-round_real
**Wall time**: 138.3s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=58919, completion=6483, reasoning=4834, total=65402

---

## PAPER-GPT-B1 — BLOCKER — Headline dedup count is arithmetically impossible

**Section:** Title; Abstract; Table 1 footnote `^\|`; §4.3; §6.4(a); Conclusions item 8; Data availability

| Truth-audit item | Paper claim | Audit result |
|---|---:|---:|
| Survey-level detections | 388,493 | stated |
| Multi-survey coincidences | 637, all pairwise, no triples | stated |
| Unique count implied by stated coincidences | 388,493 − 637 = **387,856** | not 378,280 |
| Paper headline | **378,280** | short by **9,576** |

**Issue:** The paper admits this incompatibility in §6.4(a) but still uses `378,280` as the title/abstract/conclusion/data-release headline. A known possibly-wrong count cannot be the primary result.

**Fix:** Recompute and publish the union-find cluster manifest before submission. Either revise the headline to 387,856, document 9,576 intra-survey duplicate collapses, or report the true ≈10,213 duplicate-detection reduction with cluster multiplicities.

---

## PAPER-GPT-B2 — BLOCKER — DESI OOD threshold arithmetic contradicts the 0.87% anomaly rate

**Section:** §2.2 “In-sample scoring and held-out validation”; §6.4(b)

| Truth-audit item | Paper claim | Audit result |
|---|---:|---:|
| DESI `S>5` MSE threshold | ≈0.143 | stated |
| 100k OOD median MSE | 0.178 | stated |
| Consequence if same scale | >50% exceed threshold | unavoidable |
| Paper claim | 0.87% anomaly rate preserved | incompatible |

**Issue:** If the OOD median MSE is above the `S>5` threshold, the OOD anomaly fraction cannot be 0.87%. The text mixes raw MSE, “rescaled standardized units,” and `S` without a reproducible mapping.

**Fix:** Report `μ_val`, `σ_val`, raw-MSE threshold, OOD `S` distribution, and exact `N(S>5)` on the 100k OOD sample. If the scales differ, rename them and stop comparing the numbers directly.

---

## PAPER-GPT-B3 — BLOCKER — DESI k-fold Jaccard validation is internally impossible

**Section:** Abstract; §2.2; §6.4(i)

| Truth-audit item | Version A | Version B |
|---|---|---|
| Abstract protocol | each fold scores full 47,000 pool | top sets are comparable |
| §2.2 / §6.4(i) protocol | each fold scores held-out 9,400 only | folds are disjoint |
| Claimed top-1% size | 470 per fold | only possible for full 47k, not held-out 9.4k |
| Claimed overlap | 399 objects in all five folds | impossible for disjoint held-outs |

**Issue:** The validation alternates between “score the full pool” and “score only held-out folds.” The reported Jaccard, union size 546, and “73% appear in all five folds” are impossible under the held-out-only protocol.

**Fix:** State one protocol and recompute. Use a common external holdout scored by every fold, or score the full pool while labeling which objects were in-training for each model; then recompute Jaccard on the same object universe.

---

## PAPER-GPT-B4 — BLOCKER — Path-C catalog counts are not a coherent statistical selection

**Section:** §2.2; §3 Table 1 and footnotes; §3.2–3.5; §6.4(v); Conclusions item 8

| Survey | Paper’s count used in 388,493 | Audit problem |
|---|---:|---|
| SDSS | 77,905 | native `S>5` gives only **12**; 77,905 is a bookkeeping slice at `S≥0.1060`, ≈96th percentile / ≈4% of scored spectra |
| LAMOST | 113,342 | detector fails 5σ gate; retained as exploratory but included in headline as anomalies |
| Planck | 200 | Table says 20,000 patches/top 1%; §3.5 says native re-score used 200,000 patches, so 200 is top 0.1%; total processed is off by 180,000 |
| Gaia | 500 | explicitly exploratory due 41% stability, still included in primary headline |

**Issue:** The “Path-C unique anomalies” mix absolute `S>5`, percentile cuts, arbitrary continuity slices, failed-gate exploratory sets, and a Planck denominator mismatch. The resulting headline is not a well-defined anomaly catalog.

**Fix:** Define one primary tier with predeclared per-survey thresholds and validation requirements. Move failed/exploratory/continuity slices outside the headline, recompute `N_total`, rates, raw sum, and dedup count.

---

## PAPER-GPT-B5 — MAJOR — R4 “strict subset” closure regressed in Table 1 / caveat text

**Section:** Table 1 footnote `^\S`; §3.4 eROSITA; §6.4(v), §6.4(f)

| Truth-audit item | Paper location | Status |
|---|---|---|
| Softened wording “high overlap” | §3.4 | correct |
| “published catalog ... is a strict subset” | Table 1 footnote `^\S` | regression |
| “9,303-object set ... strict superset of published 298-source catalog” | §6.4(v) | regression |
| exact intersection count | queued for v3.1.44 | not available |

**Issue:** The R4 closure did not hold globally. The paper still asserts strict subset/superset without the intersection verification it says is missing.

**Fix:** Replace every strict subset/superset claim with “high overlap, exact intersection pending,” or add the actual `298 ∩ 9303` verification table now.

---

## PAPER-GPT-B6 — MAJOR — Fisher CI propagation closure is inconsistent in the deferral tail

**Section:** §5; §6.4(c); Abstract; Conclusions item 5

| Truth-audit item | Paper claim | Audit result |
|---|---|---|
| §5 corrected CI | `[3.64, 12.93]` | consistent with `8.98 − 3.66α` using rounded α endpoints |
| §6.4(c) deferral | asymmetric envelope `[5.91, 12.92]` | stale, explicitly retracted in §5 |
| α uncertainty | `0.19 ± 0.65` | consistent with zero; not informative |
| “fiducial agreement far tighter than within 1σ” | repeated | overclaims central-value proximity as precision |

**Issue:** The propagation-tail closure failed: the old `[5.91,12.92]` interval remains in §6.4(c). The text also treats a noisy central value near α=0.15 as “tight agreement,” which is statistically meaningless when σ_α = 0.65.

**Fix:** Delete the stale `[5.91,12.92]` line everywhere. State only: α-only propagation gives `σ(f_NL)=8.27±2.37` and 95% `[3.64,12.93]`; this excludes observational-systematics uncertainty and is not a detection or precision validation of α=0.15.
