# P1A R52 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.78.pdf` md5=198cb994 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 66.3s

---

**Referee Report — P1A (Physical Review D)**

**P1A-E1**  
**Section:** Abstract (p. 1) + Sec. IV (pp. 10–13) + Sec. XV (p. 24)  
**Problem:** Abstract states “the surviving testable prediction is the matter-bounce \(f_{NL}=-35/8\)” and “spectator-ALP birefringence \(\beta\approx0.27^\circ\) is a benchmark consistency point, not an ECH prediction.” Body (Sec. IV D, Table I footnote c, Sec. XIII) explicitly labels both as *class-level* (scalar-only \(w=0\) matter bounce) and “not a distinctive ECH prediction.” The abstract therefore presents non-ECH results as the paper’s headline output.  
**Required fix:** Rewrite abstract to state only what the four enumerated minimal-ECH routes are shown to be closed at channel level; move \(f_{NL}\) and \(\beta\) claims to a separate “ECH-independent class tests” paragraph with explicit disclaimer.

**P1A-E2**  
**Section:** Abstract + Sec. I (p. 3) + Sec. IX–X (pp. 16–20) + all “in preparation [6]” citations  
**Problem:** Paper is not standalone. Every load-bearing numerical result (\(\Delta N_{\rm eff}\), MCMC posteriors, Fisher forecasts, NaMaster pipeline) is imported from unpublished companion(s) labeled “Paper I(b) (in preparation)” or “[6]”. STANDALONE-READER TEST fails on first page.  
**Required fix:** Either (a) absorb all necessary numerical content into the present manuscript or (b) withdraw and resubmit only after companions are public with fixed arXiv IDs.

**P1A-E3**  
**Section:** Title + Abstract + Sec. IV (pp. 10–13)  
**Problem:** Title claims “Channel-Level Closure of Four Minimal … Routes.” Body repeatedly qualifies the result as *channel-level amplitude-budget* closure under explicitly labeled scaling/ansatz assumptions and *not* an operator-level theorem. Title is therefore stronger than the calibrated claim.  
**Required fix:** Change title to “Amplitude-Budget Channel-Level Closure … under Scaling Ansatze” (or equivalent).

**P1A-M1**  
**Section:** Sec. II C (p. 7) + Appendix B (referenced but not shown)  
**Problem:** The central identification \(\rho_\Lambda=\Xi M_{\rm Pl}^4\) is admitted to be an on-shell scaling *ansatz*, not derived. All subsequent closure statements are conditional on this ansatz. No quantitative sensitivity study to off-shell dimension is supplied.  
**Required fix:** Provide explicit off-shell mass-dimension counting table and demonstrate that \(\pm1\) shifts in the ansatz do not reopen any of the four routes.

**P1A-M2**  
**Section:** Table I (p. 4) + Sec. IX (pp. 16–19)  
**Problem:** 13 “logically independent” barriers are listed; Barrier 8 (parity-even interaction) and Barrier 14 (perturbation transparency) are shown to be consequences of the same Bianchi-identity argument. They are therefore not independent. The catalog over-counts.  
**Required fix:** Merge or explicitly mark dependent barriers; recompute the “14-constraint” claim.

**P1A-M3**  
**Section:** Sec. X (pp. 19–20) + Fig. 1 (p. 5)  
**Problem:** Perturbation-transparency result is proven only for canonical scalar matter on a torsion-free branch. The paper’s own scope paragraph (p. 3) excludes fermion spin density, dynamical torsion, and boundary sectors. The central theorem therefore does not cover the parity-odd four-fermion sector advertised in the introduction.  
**Required fix:** Either restrict the theorem statement to the scalar sector throughout or supply the missing fermionic calculation.

**P1A-M4**  
**Section:** Sec. IV D (p. 13) + Sec. XI (p. 20)  
**Problem:** Route 4 is closed by a “naturalness/explanatory-deficit objection” rather than an amplitude mismatch. This is a philosophical criterion, not a dynamical no-go. It is inconsistent with the amplitude-budget standard applied to Routes 1–3.  
**Required fix:** Either convert the Route-4 argument to a quantitative amplitude bound or relabel it as an external philosophical filter.

**P1A-N1**  
**Section:** Date line (p. 1)  
**Problem:** Paper dated “June 18, 2026.”  
**Required fix:** Correct to actual submission date.

**P1A-N2**  
**Section:** Multiple figure captions (Figs. 3–6)  
**Problem:** Captions contain multi-sentence methodological asides and cross-references that belong in the main text.  
**Required fix:** Move explanatory prose out of captions.

**P1A-NIT**  
Minor typographic/notation inconsistencies (e.g., inconsistent use of \(\gamma_{\rm BI}\) vs. \(\gamma\)) exist but are not load-bearing.

## Summary recommendation
**REJECT**

The manuscript is not a self-contained calculation. Its headline claims rest on (i) unpublished companion papers, (ii) an admitted phenomenological scaling ansatz whose robustness is unquantified, and (iii) an abstract that materially misrepresents the scope and distinctiveness of the results actually proven. Even after the title and abstract are corrected, the work remains a catalog of conditional barriers rather than a rigorous operator-level closure theorem. These defects are structural and cannot be repaired by minor revision.