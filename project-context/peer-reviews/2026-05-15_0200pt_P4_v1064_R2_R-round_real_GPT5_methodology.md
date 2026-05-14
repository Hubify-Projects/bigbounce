# P4_v1064_R2 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-15_0200pt
**Wall time**: 123.0s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=61311, completion=5572, total=66883

---

No BLOCKER-grade findings.

## PAPER-GPT-M1 — MAJOR — Abstract; §Hemisphere Asymmetry; §Conclusions canonical-$N$ MASTER item (iii)

**Issue:** The per-pixel/null language is still internally contradictory. The abstract and §Conclusions say the global label shuffle preserves per-pixel counts/depth/mask-edge geometry while destroying per-galaxy depth–CW correlations; elsewhere the manuscript says “per-pixel-shuffle nulls do not preserve depth, mask-edge, or other systematic spatial structures.”

**Fix:** Define distinct nulls with distinct names: e.g. “global label permutation at fixed positions” vs “pixel-value/asymmetry shuffle.” Replace the “do not preserve depth/mask-edge” statements with “do not preserve depth–label or mask-edge–label correlations” where the fixed-position label shuffle is meant.

## PAPER-GPT-M2 — MAJOR — §Hemisphere Asymmetry; Fig. 7 caption; Abstract hemisphere paragraph

**Issue:** The hemisphere amplitude accounting is still not clean. Text correctly says a 0.17% hemisphere half-difference corresponds to full dipole amplitude \(A\simeq0.34\%\), but Fig. 7 says “full dipole-amplitude \(\max|A|=0.853\%\),” conflating this with the separate max-over-768 weighted statistic.

**Fix:** Report one statistic per sentence/table row: local hemisphere half-difference \(0.17\%\Rightarrow A\simeq0.34\%\); separately report GPU max-over-768 \(\max|A|=0.008531\) with its own definition and null. Remove the Fig. 7 parenthetical equating the two.

## PAPER-GPT-M3 — MAJOR — §Hemisphere Asymmetry; §Hemisphere Discussion

**Issue:** The look-elsewhere accounting is statistically inconsistent. A local \(3.05\sigma\) one-sided fluctuation has \(p\sim10^{-3}\), so a same-statistic max-over-directions MC cannot yield \(p_{\rm LEE}\le10^{-4}\) unless the “3.05σ” and the MC max statistic are different observables or differently normalized; the manuscript alternates between “does not survive LEE” and “rejects the random-label null.”

**Fix:** Recompute the local \(Z\), Bonferroni/BH, and direct-MC LEE using the identical axis grid, amplitude definition, weighting, and null ensemble. Until then, present the MC result only as a separate systematic diagnostic, not as a tightening of the Bonferroni/BH result.

## PAPER-GPT-M4 — MAJOR — Abstract; Introduction; §Sensitivity; Conclusions item 1

**Issue:** The empirical sensitivity claim is over-stated. The injection table never demonstrates detection at \(A=0.5\%\): median significance is only \(0.68\sigma\), \(P(\sigma>2)=0.18\), and no tested amplitude reaches 50% recovery, let alone \(3\sigma\); yet the paper repeatedly says “\(\sim0.5\%\) at \(3\sigma\)” or “50%-recovery threshold.”

**Fix:** State the empirical result as a lower bound only: “the 50%-recovery threshold lies above \(0.5\%\) on the tested grid.” Do not call \(0.5\%\) a \(3\sigma\) empirical sensitivity unless higher-amplitude injections demonstrate the chosen recovery criterion.

## PAPER-GPT-M5 — MAJOR — §Dipole Analysis; Table III; Fig. 6 caption

**Issue:** The MASTER/multipole description mixes incompatible estimators. Table III labels the first row as a single-mode \(\ell=1\) result, while the prose says the lowest bandpower centered at \(\ell_{\rm eff}=4\), spanning \(\ell=2\)–6, is used as the cut-sky \(\ell=1\) recovery; meanwhile “all higher multipoles are consistent with null” contradicts the \(+6.097\sigma\) bandpower and \(\chi^2/{\rm dof}=161.2/38\).

**Fix:** Separate the single-mode \(\ell=1\) estimator from bandpowers in different tables or clearly label them as different analyses. Remove “all higher multipoles are null” and explicitly state that low-\(\ell\) bandpowers remain systematics-contaminated and are not used for the parity-dipole claim.

## PAPER-GPT-N1 — nit — Bibliography

**Issue:** No new fused/wrong arXiv-ID issue is apparent in the Shamir/Jia style caught previously, but the bibliography still contains uncited or irrelevant entries for this paper’s text flow, e.g. Mercuri, Freidel, Holst, and Walmsley:2022, and the order is not actually first-citation order.

**Fix:** Remove uncited references or cite them where used; reorder the bibliography consistently or stop claiming first-citation ordering.
