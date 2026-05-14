# P4_v1059 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_2000pt
**Wall time**: 62.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=57532, completion=3771, total=61303

---

## PAPER-GPT-B1 — BLOCKER — §IX.J Sensitivity; Abstract; Conclusions item 1

**Issue:** The amplitude-convention fix is not propagated. §IX.J correctly says the Fisher derivation is for the CW-fraction half-modulation \(A/2\), so full-amplitude floors are \(\sim0.29\%\) ideal and \(\sim0.4\%\) conservative, but later text still calls \(0.2\%\) the “minimum detectable dipole,” “statistical-only Poisson floor,” and even says “the \(0.2\%\) in the abstract” although the abstract now says \(0.29\%\).  
**Fix:** Replace all full-amplitude sensitivity claims of \(0.14\%-0.2\%\) with \(0.29\%\) Fisher / \(\sim0.4\%\) conservative, or explicitly label the old numbers as \(A/2\). Audit Introduction, §IX.J, Motloch comparison, future LSST scaling, and Conclusions.

## PAPER-GPT-B2 — BLOCKER — §IV.B Dipole Analysis; Table III; Conclusions “Canonical-\(N\) MASTER projection”

**Issue:** The load-bearing MASTER \(\ell=1\) result is not a direct canonical Catalog C run: it uses an analysis-subsample mask \((n=5{,}547{,}858, f_{\rm sky}=0.659)\) plus an analytic projection to the canonical \((N_{\rm spiral}=3{,}201{,}160, f_{\rm sky}=0.491)\). At the same time, Table III shows severe residual low-\(\ell\) failures (\(+6.10\sigma\), \(\chi^2/{\rm dof}=161.2/38\)) attributed to monopole leakage, so the MASTER pipeline is not measurement-grade as the primary statistic until the monopole/mask treatment is rerun directly.  
**Fix:** Before submission, run the single-mode canonical NaMaster \(\ell=1\) analysis on the exact Catalog C spiral sample, with the monopole subtracted or fit jointly including \(\ell=0\), and quote that direct MC result as primary. Demote the analytic projection to a cross-check.

## PAPER-GPT-M1 — MAJOR — §IV.C Hemisphere Asymmetry; Fig. 7; §IX.B

**Issue:** The LEE treatment is internally contradictory: the text says a \(3.05\sigma\) local peak “does not survive” Bonferroni/BH and becomes \(<1\sigma\), while the direct max-statistic MC gives zero/10,000 null exceedances and \(p_{\rm LEE}\le10^{-4}\), i.e. rejection of the random-label null. The prose also calls the MC result a “tightening” of the Bonferroni/BH conclusion, which is false because the two verdicts differ.  
**Fix:** Make the direct max-statistic MC the only LEE calibration for the hemisphere scan, and state separately that it rejects only the random-label null, not a systematic-preserving null. Remove the “does not survive LEE” and “tightening” language.

## PAPER-GPT-M2 — MAJOR — §IV.C Hemisphere Asymmetry; Abstract

**Issue:** The hemisphere amplitude conversion is not dimensionally consistent. For \(p_{\rm CW}(\hat n)=\tfrac12(1+A\cos\theta)\), the mean CW-fraction difference between opposite hemispheres is \(A/2\), and the half-difference is \(A/4\); a quoted half-difference of \(0.17\%\) does not imply \(A=0.853\%\).  
**Fix:** Recompute and define the hemisphere statistic precisely: local z-score, full hemisphere difference, half-difference, and equivalent dipole-template \(A\). Use one convention everywhere.

## PAPER-GPT-M3 — MAJOR — §IX.J Injection-Recovery; Conclusions item 1

**Issue:** The empirical sensitivity is overclaimed in places. The injection grid never reaches \(50\%\) recovery even at \(P(\sigma>2)\) for \(A=0.5\%\), and no \(P(\sigma>3)\) recovery threshold is demonstrated; nevertheless Conclusions says the catalog “achieve[s]” a \(\sim0.5\%\) minimum detectable dipole “at \(3\sigma\).” The injection also uses the HC-spiral subset \(N=471{,}049\), not the full canonical \(3.20\)M spiral sample, so it is not the all-catalog floor without qualification.  
**Fix:** State only \(A_{\rm dipole}>0.5\%\) as a lower bound on the empirical 50%-recovery threshold under the tested HC-spiral setup, or extend injections to larger \(A\) and require \(P(\sigma>3)>0.5\) on the canonical sample.

## PAPER-GPT-M4 — MAJOR — §IV.D Sky Region Balance; Table II

**Issue:** The sky-balance table uses stale snapshot regional counts totaling \(3{,}321{,}795\), while the canonical catalog has \(3{,}201{,}160\); the “All sky canonical” row simply inherits the old CW fraction and asserts uniform redistribution without showing the recompute. This table is used as evidence that the \(9.5\sigma\) monopole is spatially uniform and harmless, so stale denominators are not acceptable.  
**Fix:** Recompute all RA/Dec regional rows directly from canonical `class_eq` labels and report those counts/fractions only. Add imaging-leg splits or remove claims that equatorial slabs establish survey-leg uniformity.
