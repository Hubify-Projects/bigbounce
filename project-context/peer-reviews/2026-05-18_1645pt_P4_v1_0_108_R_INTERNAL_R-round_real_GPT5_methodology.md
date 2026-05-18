# P4_v1_0_108_R_INTERNAL R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1645pt
**Wall time**: 69.0s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=88387, completion=4199, reasoning=3106, total=92586

---

## PAPER-GPT-B1 — BLOCKER — Abstract / §IV.D / Conclusions / NaMaster appendix

Canonical-mask $\ell=1$ status is incoherent: the paper simultaneously reports $+1.85\sigma$ as the canonical-mask residual, appendix-corrected $\sim+1.77\sigma$, and the new v1.0.108 proper-monopole-subtracted binomial-null result $+3.64\sigma$ / apodized $+3.57\sigma$ / bootstrap $-0.22\sigma$. These are not cleanly separated by data vector, monopole subtraction, mask, and null model, yet the abstract and conclusions still frame the canonical-mask result as merely “sub-detection-threshold $+1.85\sigma$.”

Fix: add one canonical-mask table with map definition, mask, monopole subtraction, null model, $N_{\rm MC}$, $C_1$, null mean/std, $z$, and artifact path; update abstract/conclusion to the v1.0.108 framing: binomial/apodized give $\sim3.6\sigma$, bootstrap gives null, therefore no detection under the adopted systematics-preserving null.

## PAPER-GPT-M1 — MAJOR — §IV.D multi-null verdict

The statement that bootstrap-null collapse $(-0.22\sigma)$ plus $\ell=2>\ell=1$ plus quartile washout “rule out” a real cosmological dipole is overclaimed. A pixel/bootstrap null built from the data can absorb real coherent sky signal into the null variance, mask leakage can make $\ell=2$ exceed $\ell=1$ for an injected dipole, and equal-N quartiles would only have $\sim1/2$ the full-sample SNR even for a real signal.

Fix: rephrase as “strongly disfavors a clean dipole under these diagnostics,” not “rules out”; demonstrate rejection of interpretation (i) with forward injections of $A\simeq1.7\%$ dipoles through the exact canonical mask/null battery and report the distribution of $\ell_2/\ell_1$, bootstrap $z$, and quartile $z$.

## PAPER-GPT-M2 — MAJOR — §IV.D / p4_multinull_battery.json citation

The “4-null battery” narrative is internally inconsistent: it lists apodized, multipole-spectrum, bootstrap, and quartile tests, but the summary also reports sky-rotation $+2.56\sigma$ without defining the sky-rotation null or its MC ensemble. The artifact is cited, but the paper does not expose enough of its contents to audit the result.

Fix: add a compact table sourced from `p4_multinull_battery.json` with all tests actually used: binomial, apodized, bootstrap, sky-rotation, multipole diagnostic, and quartiles; define each null, $N_{\rm MC}$, statistic, and whether it is used as a detection null or diagnostic.

## PAPER-GPT-M3 — MAJOR — Abstract / §IX.J Sensitivity / Table IX

Injection-recovery sample definition is contradictory. The abstract says the released `injection_recovery_extended.json` was run on $p_{\rm eq}>0.6$ with $N=2{,}107{,}494$, not the in-paper $P>0.9$ $N=471{,}049$ sample, while §IX.J and Table IX still claim the sweep uses $N=471{,}049$ HC spirals; elsewhere “HC-broad-0.6” is $N\simeq949{,}584$.

Fix: choose the actual injection sample from the JSON manifest and propagate that $N$, selection predicate, Fisher floor, and $0.75\%$ threshold consistently through abstract, §IX.J, Table IX, and conclusions; if multiple sweeps exist, tabulate them separately.

## PAPER-GPT-M4 — MAJOR — §IV.D / Conclusions null-model language

The binomial/per-pixel shuffle null is described as “systematic-inclusive-but-not-systematic-modeling,” but it explicitly fails to preserve depth, PSF, morphology, imaging-leg, and spatial covariance; this wording overstates the null’s protection against systematics. The bootstrap null is then treated as canonical without a clear statistical justification for why it is the correct null for a cosmological-dipole test rather than a variance-inflating empirical resample.

Fix: define a strict null hierarchy: binomial = shot-noise/occupancy null, bootstrap = empirical spatial-correlation variance diagnostic, systematics-preserving null = not yet done. Do not call the binomial null systematic-inclusive; make the bootstrap-null verdict conditional until a depth/PSF/morphology-preserving null is run.

## PAPER-GPT-m1 — minor — Conclusions / Table IX

Conclusion item 1 says Table IX has $P(\sigma>3)=0.50$ at $A=0.75\%$, but Table IX reports $0.55$. This is small but visible in a headline sensitivity statement.

Fix: change the conclusion to $0.55$ or state “$\approx0.5$” consistently.
