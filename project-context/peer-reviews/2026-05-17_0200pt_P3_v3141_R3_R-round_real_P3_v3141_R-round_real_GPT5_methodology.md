# P3_v3141 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0200pt_P3_v3141_R3_R-round_real
**Wall time**: 73.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=58220, completion=4909, reasoning=3624, total=63129

---

## PAPER-GPT-B1 — BLOCKER — Sec. 2.2 “In-sample scoring and held-out validation”; Sec. 6.3 caveat (b)

**Issue:** DESI OOD MSE math is still contradictory. Eq. (2) says DESI \(S>5\) corresponds to \(\mathrm{MSE}\approx0.143\); the OOD median is \(0.178\) and 52.8% exceed \(5\times0.0287\approx0.1435\), so the OOD anomaly rate cannot simultaneously be “preserved” at 0.87%. This is not a wording issue; it is a threshold/count inconsistency.

**Fix:** Report the exact production threshold in raw MSE units, the exact OOD count above it, and the OOD \(S\)-distribution using the same \((\mu_{\rm val},\sigma_{\rm val})\). Remove the 0.87% OOD-preservation claim unless the recomputed count actually supports it.

## PAPER-GPT-B2 — BLOCKER — Sec. 2.2; Sec. 6.3 caveat (i); abstract DESI 5-fold paragraph

**Issue:** The DESI 5-fold Jaccard protocol is internally impossible as written. The abstract says each fold scores the full 47,000 pool, allowing five top-470 sets with union 546 and 399 objects in all five; Sec. 2.2 and caveat (i) say each fold scores only its disjoint held-out 9,400 spectra, in which case cross-fold Jaccard overlap and “appears in all five folds” are impossible.

**Fix:** Pick one protocol and rewrite all counts accordingly. If full-pool scoring was used, stop calling every scored object held-out; if held-out-only scoring was used, redo the stability statistic on comparable populations.

## PAPER-GPT-B3 — BLOCKER — Sec. 4.3; Table 1 footnotes; Sec. 7 item 8

**Issue:** The headline dedup arithmetic is unresolved. \(388{,}493 \rightarrow 378{,}280\) implies 10,213 collapsed duplicate detections, but Sec. 4.3 reports only 637 pairwise multi-survey coincidences and no triples; with only pairwise duplicates the unique count would be \(388{,}493-637=387{,}856\), not 378,280. The paper even preserves this as an “on-record deferral,” while still using 378,280 as the primary result.

**Fix:** Recompute and publish the union-find cluster manifest with multiplicity counts; either correct the 637 figure or correct the 378,280 headline. Do not submit with the catalog-size arithmetic unreconciled.

## PAPER-GPT-M1 — MAJOR — Table 1; Secs. 3.2–3.7; Sec. 7

**Issue:** The Path-C survey table mixes cross-transfer, native, scored-subset, and headline counts in incompatible ways. Examples: Planck native retrain scores \(2\times10^5\) patches but Table 1 keeps \(N_{\rm total}=20{,}000\); SDSS native “top-77,905” is 4.05% of 1,925,279 scored spectra, not the tabulated 3.38% of 2,304,830; Table 1 labels \(N_{\rm anom}\) as cross-transfer while footnotes call SDSS 77,905 and LAMOST 113,342 Path-C canonical. These inconsistencies make rates and totals non-auditable.

**Fix:** Split the table into explicit columns: cross-transfer count, native scored \(N\), native threshold, native anomaly count, masked count, and contribution to dedup headline. Recompute all rates using the matching denominator.

## PAPER-GPT-M2 — MAJOR — Sec. 5; Appendix “Sensitivity to Bias Enhancement”

**Issue:** The Fisher-error propagation explanation is mathematically wrong even though the final symmetric interval is close. If \(\alpha=0.19\pm0.65\) and \(\sigma_{f_{\rm NL}}(\alpha)=8.98-3.66\alpha\), then the \(1\sigma\) propagated uncertainty is \(3.66\times0.65=2.38\), not \(3.66\times0.65/1.96\); the text then invokes an unjustified \(\sqrt{2}\) factor. The appendix also introduces incompatible Fisher baselines (\(8.98\), \(12.72\), \(16.85\), \(0.067\)–\(0.116\)) without a clean separation of configurations.

**Fix:** State the propagation as \(\Delta\sigma_{f_{\rm NL}}=|d\sigma/d\alpha|\Delta\alpha=2.38\) and delete the /1.96 and \(\sqrt{2}\) rationale. Separate DESI-anomaly, SPHEREx, shot-noise, and internal-systematics Fisher configurations into distinct tables with non-interchangeable baselines.

## PAPER-GPT-M3 — MAJOR — Sec. 5.1; Appendix “PTA MCMC documentation”

**Issue:** The PTA result no longer matches the stated round/headline state and overstates discrimination. The paper replaces \(\gamma=3.20\pm0.42\) with \(\gamma=2.567\pm0.382\), then quotes SMBHB as \(4.61\sigma\) disfavored using a product of marginal per-bin KDEs while explicitly ignoring inter-bin covariance and model evidence. That is not a robust exclusion and should not be used as a cosmological-discrimination claim.

**Fix:** Demote the PTA paragraph to a non-headline diagnostic unless a joint covariance/evidence calculation is done. Quote only “parameter-shift under independent-bin approximation,” remove “strongly disfavored” language, and reconcile which \(\gamma\) result is canonical.
