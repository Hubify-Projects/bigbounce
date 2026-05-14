# P4_v1062 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_2225pt
**Wall time**: 59.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=59137, completion=3299, total=62436

---

## PAPER-GPT-B1 — BLOCKER — Abstract/Sec. Dipole/Table III/Conclusions conflict on canonical MASTER closure

**Issue:** The abstract and Table III caption still say the canonical-$N$ $\ell=1$ NaMaster direct compute is a post-arXiv/TODO item and that the canonical projection is $+0.26\sigma$ with all endpoints within $|\sigma|<1$, while the v1.0.62 conclusions report the direct-MC result $+1.85\sigma$. This is a hard internal contradiction in the headline estimator chain.

**Fix:** Propagate v1.0.62 everywhere: abstract, Sec. Dipole, Table III caption, Fig. multipoles caption, and conclusions. Replace the “TODO / analytic projection” language with the direct-MC value and explicitly state that the former $+0.26\sigma$ is superseded.

## PAPER-GPT-M1 — MAJOR — $+1.85\sigma$ is overinterpreted as a systematic “rejection”

**Issue:** The v1.0.62 paragraph says the direct-MC result “catches” the depth/GZ1 systematic and refers to “rejection” of the random-label null at $\approx1.85\sigma$. A $1.85\sigma$ excess is at most mild tension, not a statistically secure diagnostic of a specific systematic channel.

**Fix:** Rephrase as “mild canonical-mask excess under the random-label null, consistent with leakage/systematics and not significant as a primordial detection.” Quote the corresponding one-/two-sided empirical rank p-value from the 500 MCs.

## PAPER-GPT-M2 — MAJOR — Amplitude mapping from $+1.85\sigma$ to “$\approx0.6\%$ half-modulation” is unsupported

**Issue:** The conclusions claim $+1.85\sigma$ implies $\approx0.6\%$ equivalent half-modulation $A/2$ and that injection recovery would have found a primordial dipole at that amplitude. This conflicts with the stated Fisher scale ($\sigma_{A/2}\approx0.048\%$ ideal) and with the empirical injection table, where even full-amplitude $A=0.5\%$ gives only $P(\sigma>2)=0.18$.

**Fix:** Remove the $0.6\%$ half-modulation claim unless derived explicitly from injected MASTER-$C_1$ calibration. Do not use the injection table to rule out a primordial interpretation at $1.85\sigma$; state only that it remains below the paper’s detection threshold.

## PAPER-GPT-M3 — MAJOR — Estimator table mixes incompatible $N$, masks, and “strict-superset” claims

**Issue:** The four-row estimator table compares canonical $N_{\rm spiral}=3.20$M to a “subsample-mask MASTER” row with $N=5.55$M and $f_{\rm sky}=0.659$, then claims the latter is a strict-superset mask that rejects a primordial signal. It is unclear whether $N=5.55$M is total galaxies, spirals, or pixels; larger $f_{\rm sky}$ does not by itself prove pixel-set containment or comparable weighting.

**Fix:** Define $N$ consistently as the number of chirality-tracer spirals used in the map, or split “galaxies” and “spirals” columns. Prove the mask inclusion with a pixel-set statement, or downgrade “strict-superset rejects” to “independent mask cross-check.”

## PAPER-GPT-M4 — MAJOR — Direct-MC closure provenance is not actually closed if null array remains only on pod

**Issue:** The conclusions say the companion JSON records all numerical inputs/outputs, but then state the 500-element \texttt{null\_distribution.npy} is archived only on the compute pod and will be mirrored later. For a 500-MC rank/null claim, the null draws are part of the result, not optional provenance.

**Fix:** Deposit \texttt{null\_distribution.npy} with checksum in the public provenance directory before submission, or remove “closed”/“archives all numerical inputs/outputs” language and mark the mirroring as still pending.

## PAPER-GPT-M5 — MAJOR — Sensitivity floor language still confuses half-modulation and full amplitude

**Issue:** The conclusions still say “the statistical-only Fisher floor is $\lesssim0.2\%$” without consistently qualifying that as the CW-fraction half-modulation $A/2$. Elsewhere the paper correctly says the full-amplitude Fisher floor is $\sim0.29\%$ ideal and $\sim0.4\%$ conservative, with empirical detection threshold $>0.5\%$.

**Fix:** Standardize every sensitivity sentence: $0.2\%$ = conservative half-modulation floor; $0.29\%$ = ideal full-amplitude Fisher floor; $\sim0.4\%$ = conservative full-amplitude statistical floor; $>0.5\%$ = empirical systematic-inclusive full-amplitude threshold.
