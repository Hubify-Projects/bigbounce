# P4_v1064_R2 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-15_0200pt
**Wall time**: 77.7s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=58467, completion=1351, total=59818

---

**PAPER-DEE-B1**  
**Section: Abstract & §VI.D**  
**BLOCKER**  

The abstract states “the per-pixel random-label shuffle preserves per-pixel galaxy counts and per-pixel mask-edge positions while randomly permuting the CW vs CCW assignments globally across the catalog, so any *spatially correlated* chirality asymmetry that survives this shuffle reflects mask-geometry-driven leakage of the global monopole rather than a depth/label per-galaxy systematic.” This directly contradicts the description in §VI.D, which says the per-pixel shuffle “destroys any per-galaxy depth-vs-label or mask-edge-vs-label correlation that would source a true ‘depth-coupled’ systematic.” The two statements are mutually exclusive: one claims the shuffle preserves mask-edge correlations, the other says it destroys them. This is a fundamental inconsistency in the systematic-error narrative.  

**Fix:** Reconcile the language. Either clarify that “per-pixel shuffle” means shuffling labels *within each pixel* (preserving local depth correlations) or *globally across the catalog* (destroying them). The abstract must match the technical description in §VI.D.

---

**PAPER-DEE-M1**  
**Section: Abstract & §IX**  
**MAJOR**  

The abstract reports an “empirical injection-recovery sensitivity floor is \(|A_{\rm dipole}| > 0.5\%\)” and a “Fisher-floor statistical Poisson asymptote is \(|A_{\rm dipole}| \lesssim 0.29\%\)”. However, the derivation in §IX uses the half-modulation convention \(p_{\rm CW}(\hat n) = \tfrac12(1+A\cos\theta)\), so the Fisher floor of \(0.14\%\) on \(A/2\) corresponds to \(0.29\%\) on \(A\). The abstract correctly states the full-amplitude floor but then says “the earlier \(\lesssim 0.2\%\) figure in prior drafts conflated the half-modulation and full-amplitude conventions and is superseded.” This is confusing: the \(0.2\%\) figure appears nowhere else in the abstract, and the reader cannot trace which number is being superseded.  

**Fix:** Explicitly state in the abstract that the Fisher floor on the *full* amplitude \(A\) is \(0.29\%\) (statistical), and the empirical floor is \(>0.5\%\) (systematic-inclusive). Remove the dangling reference to “earlier \(\lesssim 0.2\%\) figure.”

---

**PAPER-DEE-M2**  
**Section: §VI.D (Table III caption)**  
**MAJOR**  

Table III caption says the \(\ell_{\rm eff}=4\) bandpower spans \(\ell\in[2,6]\) and “does *not* include \(\ell=1\)”. Yet the table lists a row for “\(\ell=1\) (single mode)” directly above it. This is misleading: the reader might think the \(\ell=1\) row is part of the bandpower table. In fact, the \(\ell=1\) result comes from a different analysis (subsample mask, \(f_{\rm sky}=0.659\)), while the bandpowers are from the canonical mask (\(f_{\rm sky}=0.491\)). The caption should explicitly separate the two analyses.  

**Fix:** Add a clear separator in the table or caption: “The first row is the single-mode \(\ell=1\) result from the subsample mask (\(f_{\rm sky}=0.659\)). Rows 2–5 are bandpowers from the canonical mask (\(f_{\rm sky}=0.491\)).”

---

**PAPER-DEE-M3**  
**Section: §IX (Conclusions)**  
**MAJOR**  

The conclusions state “the canonical-$N$ direct-MC value \(+1.85\sigma\) is a mild canonical-mask excess interpreted as a leakage-floor calibration, not as a primordial signal.” However, the text never defines what “canonical mask” is (presumably \(f_{\rm sky}=0.4938\)), nor explains why the \(+1.85\sigma\) excess is considered a “leakage-floor calibration” while the \(-0.122\sigma\) subsample-mask result is the “headline.” The reasoning is buried in a footnote and not clearly justified.  

**Fix:** Add a short paragraph in §IX explicitly defining “canonical mask” vs. “subsample mask,” and justify why the subsample-mask result is more robust (e.g., larger \(f_{\rm sky}\) reduces edge-leakage). Clarify that the \(+1.85\sigma\) is a calibration of mask-induced leakage, not a detection.

---

**PAPER-DEE-N1**  
**Section: Bibliography**  
**minor**  

The bibliography contains two arXiv entries that point to unrelated papers: Shamir (2022) previously linked to arXiv:2207.11885 (an optimization paper), and Jia et al. (2023) previously linked to arXiv:2211.03497 (a black-hole paper). The paper notes these were removed pending verification, but the current bib still lists them without resolved IDs. This is a minor but persistent metadata issue.  

**Fix:** Either remove the arXiv IDs entirely and keep only journal references, or verify and insert the correct arXiv IDs (e.g., Shamir 2022 likely should be arXiv:2207.11885v? [needs checking]; Jia et al. 2023 likely should be arXiv:2211.03497v? [needs checking]).

---

**PAPER-DEE-N2**  
**Section: §VI.D (footnote 1)**  
**nit**  

Footnote 1 describes three distinct Monte Carlo counts but uses ambiguous notation: “\(N_{\rm MC} = 10,000\) isotropic-null realizations” vs. “\(N_{\rm MC} = 500\) realizations” vs. “\(N_{\rm MC} = 1,000\) realizations.” The footnote explains the different contexts, but the variable \(N_{\rm MC}\) is reused for all three, which could cause confusion.  

**Fix:** Use distinct symbols, e.g., \(N_{\rm MC}^{\rm(dipole)}\), \(N_{\rm MC}^{\rm(MASTER)}\), \(N_{\rm MC}^{\rm(bandpower)}\), or simply spell out “500 MC realizations for MASTER,” etc., in the main text.
