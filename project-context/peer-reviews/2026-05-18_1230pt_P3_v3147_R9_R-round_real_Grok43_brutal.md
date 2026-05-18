# P3_v3147_R9 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1230pt
**Wall time**: 40.8s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=57024, completion=3822, reasoning=2911, total=60846

---

**PAPER-GRO-B1**  
**Classification:** BLOCKER  
**Section:** Abstract + §5 (multi-tracer Fisher) + §6.4(i) deferral list  
**Issue:** The linear form \(\sigma(f_{\rm NL})(\alpha) = 8.98 - 3.66\alpha\) is still used to generate the quoted 95% envelope [3.62, 12.95] and the central forecast propagation, while the same section explicitly states that this extrapolation violates Fisher positivity. The \(\alpha^2\) form \(1/\sigma^2 = F_0 + c\alpha^2\) (with anchors at \(\alpha=0\) and \(\alpha=0.15\)) is only mentioned in the deferral, not substituted into the headline numbers.  
**Fix:** Replace the linear-extrapolated envelope with the positivity-respecting form throughout §5 and the abstract; report only the central value at \(\alpha=0.19\) (which agrees to ~2%) and flag the full CI as pending v3.1.48+ rerun.

**PAPER-GRO-B2**  
**Classification:** BLOCKER  
**Section:** §5 (Gold+Silver subset) + §6.4(j)  
**Issue:** The GS forecast \(\sigma(f_{\rm NL})^{\rm GS} = 2.28 \pm 7.43\) is retained as a quoted result even though the text acknowledges it produces an unphysical negative lower bound. The asymmetric remap [2.04, 3.40] under the positivity form is stated only in the deferral and not applied to the reported number.  
**Fix:** Remove the linear \(\pm 7.43\) from all headline text; replace with the positivity-remapped interval centered on the \(\alpha^2\)-form value at \(\alpha_{\rm GS}=1.83\).

**PAPER-GRO-M1**  
**Classification:** MAJOR  
**Section:** Abstract + §1 + §4.3 + Table 1  
**Issue:** The headline 378,280 is presented as the canonical unique-object count while §4.3 and the deferral list (a) explicitly document a 9,576-object arithmetic shortfall under the all-pairwise assumption and state that the union-find recompute is still pending. The stratification into 378,080 point sources + 200 patches is asserted as exact without the supporting manifest.  
**Fix:** Qualify every instance of 378,280 as “pending union-find verification; provisional upper bound 387,856 under pairwise assumption” or move the number to a footnote until the recompute lands.

**PAPER-GRO-M2**  
**Classification:** MAJOR  
**Section:** Abstract + §5 + §6.4(c)  
**Issue:** The multi-tracer improvement is repeatedly framed as a “central forecast” and “7.9% improvement” while the text simultaneously states it is consistent with zero at <1σ and assumes zero observational systematics. The load-bearing claim for downstream use is therefore the null result, not the percentage.  
**Fix:** Lead with “no statistically significant improvement detected (<1σ from null)” and relegate the 7.9% central value to a secondary sensitivity statement.

**PAPER-GRO-m3**  
**Classification:** minor  
**Section:** Title + Abstract + §1  
**Issue:** “Largest-scale application … to date” and “first multi-survey anomaly detection campaign at combined scale exceeding 37.3 million” are used without a systematic literature table showing prior single-survey scales and architectures. The 141× claim versus Liang+2023 is accurate only because the comparison mixes survey count with methodology.  
**Fix:** Add a one-row comparison table (prior max single-survey N, architecture, anomaly rate) or soften to “largest published multi-survey autoencoder search by source count.”

**PAPER-GRO-n1**  
**Classification:** nit  
**Section:** §6.4 preamble + deferral list  
**Issue:** The long on-record deferral list (a)–(j) is presented as transparent but functions as a reviewer-dodging device: compute-bound items are listed rather than fixed, and the paper continues to quote the affected headline numbers.  
**Fix:** Move all unverified arithmetic and Fisher numbers to an explicit “provisional” table or appendix; do not use them in the abstract or conclusions until closed.
