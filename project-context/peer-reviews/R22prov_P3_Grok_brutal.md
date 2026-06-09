# P3 R22prov — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 66.8s

---

**Referee Report**

**Paper:** P3 (Round R22prov) — “Spectrally Unusual Sources at Scale…”  
**Journal target:** Phys. Rev. D  
**Date of review:** first read

I have examined every page, figure, table, equation, caption, and the abstract in the rendered PDF. Below are all identified problems, classified strictly.

### ESSENTIAL (paper cannot be accepted without fixes)
**P3-E1** Abstract (p. 1) & §V (p. 12)  
The abstract states “7.9% improvement consistent with no improvement at <1σ”. The quoted central value σ(f_NL)=8.14 with envelope [3.92,8.98] is obtained only after inserting the measured α_jk=0.19±0.65 into the Fisher form. The single-tracer baseline is given as 8.98. The improvement is therefore 7.9% but lies well inside the 1σ uncertainty on α_jk itself. The abstract presents this as a positive multi-tracer result; it is not.  
**Required fix:** Remove all quantitative “improvement” language from the abstract and §V; report only the null-consistent result.

**P3-E2** Abstract (p. 1) & §V.A (p. 12)  
Abstract claims “NANOGRAV 15-yr KDE … γ=2.567±0.382; the matter-bounce prediction γ=3.0 sits at +1.13σ (marginally consistent)”. The same paragraph simultaneously quotes SMBHB γ=4.33 at +4.61σ. No statement appears that the two predictions are being tested under different assumptions or that the quoted significances are not directly comparable. This violates the explicit rule on juxtaposed σ values.  
**Required fix:** Delete the NANOGrav paragraph from the abstract or add an explicit “not directly comparable” qualifier at every juxtaposition.

**P3-E3** §II.D & Table I (p. 3–4)  
The Path-C “native retrain” protocol is presented as the core methodological advance, yet the only quantitative validation offered for the six injection-recovery gates is a binary PASS/FAIL label. No per-survey recovery curves versus injection amplitude are shown for the final native models (only the cross-transfer baseline appears in Fig. 10). The headline catalog numbers rest on these unshown curves.  
**Required fix:** Supply the full set of native-retrain recovery curves (or state that they are absent and downgrade all catalog claims accordingly).

**P3-E4** Fig. 7 & §IV.B (p. 11)  
The χ²=143936 (38 329 dof) test for spatial uniformity is reported without any modeling of the seven distinct survey selection functions. The text acknowledges the test is “as expected for a population that traces real astrophysical structures” but then uses the same non-uniform map to claim the anomalies are astrophysical. This is circular.  
**Required fix:** Either model the selection functions or remove the uniformity test and all cosmological-interpretation language that relies on it.

### MAJOR
**P3-M1** Abstract (p. 1)  
“largest-scale application of autoencoder anomaly detection across seven astronomical archives” is asserted. No quantitative comparison table to prior single-survey works (Baron & Poznanski 2017, Liang et al. 2023, Nicolaou et al. 2026) is provided. The claim is unsupported.  
**Required fix:** Either supply the comparison or delete the superlative.

**P3-M2** §V & Fig. 9 (p. 12–13)  
The multi-tracer f_NL forecast uses the empirical α_jk measured on the Gold+Silver subset (1 122 objects). The subset definition itself depends on the anomaly score threshold S>5. The Fisher matrix therefore contains an implicit selection bias that is never propagated.  
**Required fix:** Demonstrate that the reported σ(f_NL) remains stable when the subset definition is varied, or flag the result as illustrative only.

**P3-M3** Table IV (p. 15) & §VI.D  
Ten residual “caves” are listed, yet the text states “all ten items are closed”. Item (a) (10 213 duplicates) is resolved only by a post-hoc 7-way deduplication whose false-match rate is never quantified. The catalog headline number 378 280 therefore carries an unstated systematic uncertainty.  
**Required fix:** Provide the false-match budget or move the deduplication uncertainty into the catalog error budget.

### MINOR
**P3-m1** Fig. 3 caption (p. 6)  
The right-hand panel y-axis label “Probability density” is plotted on a log scale that spans 14 orders of magnitude; the lowest bin contains a single object. No Poisson error bar or “<1 event” annotation is shown.  
**P3-m2** §III.F (p. 6)  
“Plack CMB native … val_loss 0.4437 / 100% injection-recovery” — the number 0.4437 is given without units or comparison to the validation MSE scale used for the spectroscopic surveys. Inconsistent normalization.

### NIT
**P3-n1** Running header (every page)  
“(Dated: June 2026)” appears in the author block. This is an internal production tag that should have been removed.

**P3-n2** Multiple figure captions contain the phrase “see §VI.A” when the relevant discussion is actually in §IV.A or §V. Minor cross-reference drift.

## Summary recommendation
**REJECT**

The manuscript contains at least four essential violations of PRD standards: (1) statistically unsupported “improvement” language in the abstract, (2) side-by-side σ values presented without the required comparability qualifier, (3) headline catalog numbers resting on unshown validation curves, and (4) circular use of a spatial-uniformity test whose selection functions are never modeled. These are not cosmetic issues; they directly affect the central claims of both the anomaly catalog and its cosmological application. The paper also exceeds reasonable length for a methods contribution whose primary quantitative result is a null-consistent f_NL constraint. A substantially shortened Letter that removes all cosmological forecasting and reports only the catalog construction with full injection-recovery diagnostics might be reconsiderable, but the present submission does not meet PRD criteria.