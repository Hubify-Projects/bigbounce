# P4_v1084_R5 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_1840pt
**Wall time**: 92.0s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=76039, completion=5958, reasoning=4660, total=81997

---

## PAPER-GPT-B1 — BLOCKER — Abstract; §§Dipole, Monopole-mask null, NaMaster appendix

**Issue:** The load-bearing “pre-MASTER \(+6.48\sigma\) collapses to \(-0.12\sigma\) once MASTER is applied on the same data” claim is not methodologically true as written. The pre-MASTER leakage test uses an **un-subtracted canonical-mask** \(f_{\rm CW}\) map, while the headline post-MASTER result uses a **monopole-subtracted** CW-deficit map on a different \(f_{\rm sky}=0.659\) subsample mask; the appendix also says \(\ell=0\) is excluded, so MASTER cannot itself remove \(\ell=0\to1\) leakage.

**Fix:** Recompute before/after on the exact same map, mask, weighting, and \(\ell=0\) treatment, or reframe the result as “monopole subtraction + mask choice + MASTER” rather than a pure MASTER collapse. Remove “same data” unless literally true.

## PAPER-GPT-M1 — MAJOR — §§Sensitivity, Conclusions, Abstract, Data Availability

**Issue:** The sensitivity floor is still internally inconsistent: abstract/table say 50%-recovery at \(3\sigma\) occurs at \(A=0.75\%\), while multiple places still say \(\gtrsim0.5\%\), “\(\sim0.5\%\) at \(3\sigma\),” or even “does not cross \(P(\sigma>3)\) at any tested amplitude,” contradicting Table IX. The injection sample definition is also inconsistent: \(N=471{,}049\) matches a stricter HC cut, but prose says \(p_{\rm eq}>0.6\) / \(|p_{\rm CW,eq}|>0.6\), which would not select symmetric CW+CCW HC spirals.

**Fix:** Globally state: full-amplitude empirical 50%-recovery-at-\(3\sigma\) threshold is \(A\simeq0.75\%\); \(A=0.5\%\) gives only \(P(\sigma>3)=0.03\). Specify the exact injection selection in code/prose, e.g. \(\max(p_{\rm CW,eq},p_{\rm CCW,eq})>X\), with matching \(N\).

## PAPER-GPT-M2 — MAJOR — §§Hemisphere, Hemisphere discussion, Fig. 9, Table IV

**Issue:** The LEE paragraph is not coherent. A Bonferroni/BH “post-LEE \(<1\sigma\)” statement and a direct max-statistic MC result \(p_{\rm LEE}\le10^{-4}\) cannot both be corrections of the same search; the paper alternates between treating them as different procedures and as mutually confirming. Numeric conventions also conflict: Fig. 9 says Table IV reports \(\max|A|=1.48\times10^{-3}\), but Table IV reports \(3.48\times10^{-3}\).

**Fix:** Define one hemisphere statistic, one amplitude convention, one direction grid, and one null as primary. If keeping both, explicitly label them as different tests and delete claims that direct MC “tightens” or confirms the Bonferroni/BH null-consistency result.

## PAPER-GPT-M3 — MAJOR — §Signal-hunt diagnostics, Table II/leg-confidence table

**Issue:** The DECaLS \(\times\) confidence result is under-diagnosed and currently undermines the “HC bins disappear” narrative: DECaLS has \(+4.50\sigma\) in \([0.5,0.6)\) and \(+3.76/+4.06\sigma\) in \([0.8,1.0)\), which survives a simple 15-cell trials accounting. Calling this “most plausibly depth/PSF” is not enough; it is a high-confidence, footprint-localized residual.

**Fix:** Add a DECaLS-only depth/seeing/PSF/brick-position regression or MASTER run, plus leave-one-leg-out headline dipoles. State the LEE-adjusted significance of the 15 leg-confidence cells and remove any blanket claim that the signal disappears at high confidence.

## PAPER-GPT-M4 — MAJOR — §Two-point chirality correlation / brick-boundary control

**Issue:** The brick-boundary closure is plausible but overclaimed. The \(0.50^\circ\) bin vanishing in the interior sample supports a boundary artifact, but the explanation of the \(+2.32\sigma\) at \(3.16^\circ\) as caused by “\(\sqrt{50000/18024}\)” larger variance is wrong for a z-score already normalized by its own null; smaller \(N\) increases raw variance, not the expected z distribution.

**Fix:** Report the full interior table with pair counts, null stds, and 10-bin LEE p-value; add matched random \(18{,}024\)-object subsamples from the baseline to show the \(0.50^\circ\) collapse is edge-distance-specific. Replace “conclusively” with “strongly supports” unless that matched-control test is shown.

## PAPER-GPT-m1 — minor — Intro/Comparison/Conclusions/Bibliography

**Issue:** Shamir 2022 sample-size and citation statements remain inconsistent: the text variously says “nearly \(1.3\times10^6\) spirals,” “\(\sim200{,}000\) spirals out of \(1.3\)M,” and the bibliography says “not all classified as spirals.” Some DESI-specific statements cite `Shamir:2022` instead of `Shamir:2022DESI`.

**Fix:** Use one verified comparator everywhere: either \(1.3\)M total DESI objects or the verified Ganalyzer spiral subset, not both. Cite `Shamir:2022DESI` for DESI Legacy claims and downgrade size-ratio claims if the spiral denominator is not like-for-like.
