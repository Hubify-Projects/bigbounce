# P3 auto-2026-06-05_1717pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 self-critique (2717 chars)
**Wall time**: 63.6s

---

**Referee Report — P3**

**P3-E1 (ESSENTIAL)**  
Page 1, title block: “(Dated: June 2026)”. A manuscript submitted to PRD cannot carry a future date. This is either a preprint artifact or an internal draft marker that should never appear in a journal submission.

**P3-E2 (ESSENTIAL)**  
Abstract + §V (pp. 9–11): The paper claims a 7.9 % improvement on \(\sigma(f_{\rm NL})\) and states that the matter-bounce prediction “is testable at 3–5\(\sigma\)”. The anomalies are overwhelmingly training-set artifacts (LAMOST 98 % blue-excess, SDSS cool-dwarf inflation, etc.). No section demonstrates that the residual sample after artifact removal is cosmologically clean. The multi-tracer forecast therefore rests on an unproven premise.

**P3-E3 (ESSENTIAL)**  
Table I + §III D (p. 3): Three of the seven surveys (LAMOST, Gaia DR3, eROSITA) fail the native-retrain injection-recovery gate at 5\(\sigma\) (5.8 %, 5.2 %, 1.2 %). These surveys are nevertheless retained in the headline 378 280 catalog. The abstract does not disclose the failure rate.

**P3-E4 (ESSENTIAL)**  
§IV A (p. 8) and Fig. 5: The “genuine novelty fraction” of 17.8 % is obtained only after an extended CDS X-Match on the top-1 000 DESI objects. The abstract quotes the 58.8 % SIMBAD-unmatched fraction as if it were the discovery rate. These two numbers are not interchangeable; the abstract is therefore misleading.

**P3-M1 (MAJOR)**  
§II D (Path-C protocol): The entire catalog is the result of a six-step post-hoc “rebuild” whose thresholds (val-loss cuts, 99th-percentile slices, 5\(\sigma\) injection gates) were tuned after the first cross-transfer scan revealed massive LAMOST contamination. No pre-registered analysis plan or blind validation is presented.

**P3-M2 (MAJOR)**  
Fig. 2 (right) and §III C: SDSS DR18 scores span twelve orders of magnitude because the DESI-trained BigAE is applied outside its training domain. The paper never quantifies how much of the SDSS “anomaly” tail is simply domain shift rather than astrophysical rarity.

**P3-M3 (MAJOR)**  
§V B: The Fisher forecast uses a single scalar \(\alpha_{jk}=0.19\pm0.65\). The error bar already includes zero at <1\(\sigma\). The paper nevertheless headlines a “7.9 % improvement.” This is statistical over-claim.

**P3-M4 (MAJOR)**  
Table IV, item (d): The Savage-Dickey factor \(B_{\rm MB/SMBHB}=7.14\times10^3\) is presented as “decisive.” The same table shows that the matter-bounce index \(\gamma=3.0\) lies only +1.13\(\sigma\) from the posterior mean. These two statements are in tension; the paper does not reconcile them.

**P3-N1 (MINOR)**  
Multiple figure captions contain unresolved LaTeX placeholders (“Fig. ??” on pp. 2, 4, 5). These must be corrected.

**P3-N2 (MINOR)**  
Axis labels on Fig. 8 omit units on the horizontal axis (“Sparse tracer number density \(\bar n\)”).

**P3-N3 (NIT)**  
The phrase “Path-C unique” appears in the title and abstract without a concise definition; a one-sentence parenthetical would suffice.

**Summary recommendation: REJECT**

The manuscript fails on multiple essential counts: a future submission date, undisclosed high artifact fractions in three of seven surveys, and cosmological claims that rest on a sample whose dominant contaminants are explicitly documented in the text. Even after the Path-C rebuild, the catalog remains a mixture of training-set artifacts and known astrophysical populations rather than a clean high-bias tracer sample. These problems are structural, not cosmetic, and cannot be repaired by minor revision.

---

## PASS 2 — self-critique findings (what initial review missed)

**P3-E5 (ESSENTIAL)**  
Abstract (p. 1) and §V B (p. 10): the quoted “7.9 % improvement” on \(\sigma(f_{\rm NL})\) is arithmetically inconsistent with the displayed numbers. Using the stated central value 8.14 and single-tracer baseline 8.98 yields \((8.98-8.14)/8.98=9.35\%\), not 7.9 %. Table VII confirms the linear scaling that produces 6.1 % at \(\alpha=0.15\); the 7.9 % figure therefore cannot be recovered from the inputs given.

**P3-E6 (ESSENTIAL)**  
Table I footnote ¶ and §III D (p. 3): the Path-C unique count 378 280 is stated to be the sum of 378 080 point-source objects + 200 Planck patches. The arithmetic is correct, but the same footnote simultaneously asserts that the 200 Planck patches “contribute zero positional overlaps.” This internal contradiction (they are both added to the headline total and declared to contribute nothing) is never resolved.

**P3-M5 (MAJOR)**  
§V B and Appendix C: the Fisher forecast \(\sigma(f_{\rm NL})\) values in Table VII are computed under a 7-bin linear-bias model whose fiducial \(\alpha=0.15\) is taken from the single measured \(\alpha_{jk}=0.19\pm0.65\). No propagation of the \(\pm0.65\) uncertainty into the forecasted \(\sigma(f_{\rm NL})\) envelope is shown, so the quoted 1\(\sigma\) intervals [3.92,8.98] are formally incomplete.

**P3-M6 (MAJOR)**  
Fig. 8 caption vs. body text (§V B and Appendix C): the horizontal axis is labeled “Sparse tracer number density \(\bar n\) (Mpc\(^{-3}\))” in the caption but the body never states the units or the conversion from the 5-tracer Fisher matrix to \(\bar n\). The plotted curves therefore cannot be reproduced from the information supplied.

**P3-N4 (MINOR)**  
§II A (p. 2): the latent dimension is given as 128 for spectroscopy and 16 for photometry, yet the Planck/ACT convolutional encoder is described as having a “128-dim fully connected bottleneck.” The two 128-dim numbers refer to different layers; the text never clarifies which is which, producing an ambiguous architecture description.

**P3-N5 (MINOR)**  
Abstract sentence 4 claims “21.5× LAMOST rate compression after native retraining.” The only numerical support is the drop from 44 075 to 2 054 objects above the respective thresholds (Table I). The factor 21.5 is therefore threshold-dependent and is not an intrinsic compression ratio of the model; the abstract presents it as model-independent.

NO ADDITIONAL FINDINGS on equation dimensional consistency, cross-reference targets, or stale numbers beyond the arithmetic mismatch already flagged.

The new issues are structural (incorrect derived percentages, missing uncertainty propagation, ambiguous architecture statements) and reinforce the original recommendation of REJECT.