# P3_v3142 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0930pt_P3_v3142_R4_R-round_real
**Wall time**: 105.8s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=58149, completion=8043, reasoning=6214, total=66192

---

## PAPER-GPT-B1 — BLOCKER — Dedup arithmetic cannot produce the headline count

**Section:** Table 1 footnote `^\|`, §4.3 Cross-Survey Matches, Conclusions item 8, §6.3 deferral (a)

| Claim | Audit | Verdict |
|---|---:|---|
| Path-C detections sum to 388,493 and dedup to 378,280 | 388,493 − 378,280 = **10,213** collapsed detections | Arithmetic true |
| §4.3 reports 637 multi-survey coincidences, all pairwise, no triples | Pairwise-only union-find compression = **637**, so unique should be **387,856** | Contradiction |
| “637 clusters” and “10,213 duplicates” both describe the same 5″ dedup | They cannot both be true unless there are unreported within-survey duplicates or high-multiplicity clusters | BLOCKER |

**Issue:** The headline catalog size is numerically unreconciled. The paper itself flags this as deferred, but still uses 378,280 as the primary result.

**Fix:** Release/recompute the union-find manifest with `cluster_id`, multiplicity, surveys, and per-cluster detection count; either revise the 637 coincidence statement or revise the 378,280 headline. Do not headline the unique count until this closes.

---

## PAPER-GPT-B2 — BLOCKER — DESI OOD validation contradicts the absolute S>5 threshold

**Section:** §2.2 Training and Scoring, “In-sample scoring and held-out validation”; §6.3 deferral (b)

| Quantity | Paper value | Consequence |
|---|---:|---|
| DESI validation MSE mean | 0.0287 | Used to define S |
| DESI S>5 threshold | MSE ≈ 0.143 | Claimed absolute catalog cut |
| OOD 100k median MSE | 0.178 | Median is **above** threshold |
| OOD fraction above 5×val MSE | 52.8% | Consistent with threshold being below median |
| Claimed OOD anomaly rate | 0.87% preserved | Impossible under same absolute MSE/S cut |

**Issue:** If the OOD median MSE is 0.178 and the DESI S>5 cut is MSE≈0.143, then more than half of the OOD sample should exceed the catalog threshold, not 0.87%. The statement that the threshold “captures the upper tail” is false: it lies below the OOD median.

**Fix:** Report the actual OOD fraction above the production S>5/MSE threshold using the same `(μ_val, σ_val)`. If a different normalization or percentile threshold was used, state it and remove the absolute-threshold/anomaly-rate claim.

---

## PAPER-GPT-M1 — MAJOR — The 378,280 catalog count mixes incompatible threshold policies

**Section:** §2.2 threshold policy; Table 1 caption and footnotes; §3.2 SDSS; §3.3 LAMOST; Conclusions item 8

| Survey/count used in headline | Threshold actually used | Problem |
|---|---|---|
| DESI 195,829 | absolute S>5 | coherent |
| SDSS 77,905 | native S≥0.1060, ≈96th percentile | not S>5; only **12** objects pass S>5 |
| LAMOST 113,342 | top 1% | exploratory; only **2,054** pass S>5 |
| Planck/Gaia/NEOWISE | fixed top 1% or mask-retained top 1% | predetermined quota |
| eROSITA 298 | score-knee/top 0.03% | separate detector axis |

**Issue:** The headline “388,493 detections → 378,280 anomalies” is not a uniform anomaly catalog; it is a mixture of absolute cuts, arbitrary top-percentile quotas, a SDSS bookkeeping slice, and exploratory LAMOST. The reported global 1.01% anomaly rate is therefore not a statistical detection rate.

**Fix:** Define one preregistered headline tier with consistent threshold logic and gate requirements, or publish separate tiers only. Remove the global anomaly-rate interpretation for the mixed-threshold aggregate.

---

## PAPER-GPT-M2 — MAJOR — Deferral list is stale and does not cleanly enumerate the 6 open items

**Section:** date block; §6.3 “Real cross-vendor R-round deferrals”

| Required carried item | Date block | §6.3 deferral list | Verdict |
|---|---|---|---|
| 378,280 dedup arithmetic | present | present | open |
| DESI OOD MSE normalization | present | present | open |
| σ(fNL) zero-systematics scope | present | present but stale | open |
| NANOGrav KDE covariance/Savage-Dickey | present | present | open |
| GR projection effects on multi-tracer fNL | present | **missing** | not carried |
| BigAE-vs-IsolationForest “strict subset” verification | present | **missing** | not carried |

**Issue:** The central caveat/deferral section still lists only the old four v3.1.40 items and says “to v3.1.41”; it omits the two R3 deferrals. It also contradicts §5 by retaining the obsolete asymmetric fNL envelope `[5.91, 12.92]` after §5 retracts it in favor of the symmetric linear interval.

**Fix:** Replace §6.3 with a single six-row deferral table giving status, closure criterion, artifact, and whether closed/open. Delete the stale `[5.91, 12.92]` text.

---

## PAPER-GPT-M3 — MAJOR — Fisher arithmetic is fixed, but propagation tails and systematics remain misframed

**Section:** §5 Cosmological Applications; Appendix “Sensitivity to Bias Enhancement”

| Check | Audit | Verdict |
|---|---:|---|
| Linear propagation | \|−3.66\| × 0.65 = **2.379** | correct |
| Full-sample 95% α CI | α∈[−1.08,1.46] maps to σ(fNL)≈[3.64,12.93] | acceptable rounding |
| Quoted ±2.37 | propagates α jackknife only | not total forecast error |
| Gold+Silver forecast | σ(fNL)=2.28±7.43 | lower tail is negative; unphysical |
| GR projection effects | deferred but not modeled | contaminates local-fNL k⁻² signal |

**Issue:** The Fisher rewrite itself is mathematically correct, but the paper still presents α-only propagated scatter as if it were a meaningful forecast uncertainty in several places. The Gold+Silver linear propagation produces an impossible negative σ(fNL) tail, and the forecast still omits relativistic projection terms that mimic local-fNL scale-dependent bias.

**Fix:** Report the full-sample result as “zero-systematics α-sensitivity only.” For Gold+Silver, propagate through the actual Fisher grid or log σ(fNL) with positivity enforced; add GR light-cone/projection nuisance terms before any SPHEREx detection-significance statement.

---

## PAPER-GPT-M4 — MAJOR — NANOGrav likelihood-ratio framing still rests on an invalid independent-KDE likelihood

**Section:** §5.2 NANOGrav Bounce Consistency; Appendix PTA MCMC

| Claim | Audit | Verdict |
|---|---|---|
| Uses `Σ_i log KDE_i` over 30 bins | Treats marginal posterior KDEs as independent likelihood factors | invalid joint likelihood |
| Quotes exp(10)≈2.2×10⁴ parameter-shift ratio | Computed from marginal γ Gaussian distance only | not evidence ratio |
| Says not a Bayes factor | correct disclaimer | insufficient for “favored/disfavored” language |
| Covariance/Savage-Dickey deferred | yes | still open |

**Issue:** The paper correctly says the number is not a Bayes factor, but the underlying “likelihood” is still a product of marginal posterior KDEs with ignored inter-bin covariance and prior/Jacobian effects. The “SMBHB strongly disfavored” phrasing overstates what this approximation supports.

**Fix:** Reduce the claim to marginal γ-distance only, or perform the proper joint evidence/Savage-Dickey calculation with the free-spectrum covariance and SMBHB amplitude prior. Remove the exp(10) ratio from the main narrative until then.
