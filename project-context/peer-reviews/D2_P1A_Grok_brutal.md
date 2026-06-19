# P1A D2 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=fad68a47 pages=29
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 313.1s

---

**Referee Report**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Journal target:** Physical Review D

**Round context:** First-read adversarial review. All findings below are based solely on the rendered PDF pages provided.

**P1A-E1 (ESSENTIAL)**  
**Location:** Abstract (p. 1) + Sec. I (p. 3) + Sec. IV (pp. 10–13)  
**Problem:** Abstract states “the four enumerated minimal-ECH dark-energy routes … are closed” and presents \(f_{NL}=-35/8\) and \(\beta\approx0.27^\circ\) as headline results. Body repeatedly qualifies these as (a) channel-level only, (b) under explicit scaling ansätze and naturalness assumptions, (c) not operator-basis closure, and (d) not distinctive ECH predictions (matter-bounce class result; spectator-ALP fit). The abstract omits every one of these caveats.  
**Required fix:** Rewrite abstract to match the body’s final calibrated language exactly; move all numerical claims into a properly caveated sentence.

**P1A-E2 (ESSENTIAL)**  
**Location:** Abstract + Sec. XV (p. 25) + multiple “in preparation [6]” and “Paper I(b)” citations throughout  
**Problem:** Core numerical results (\(\Delta N_{\rm eff}\), MCMC posteriors, Fisher forecasts, LiteBIRD/SPhEREEx sensitivities) are imported from companion manuscripts that are not provided and are still “in preparation.” A standalone reader cannot verify any load-bearing number.  
**Required fix:** Either make the present manuscript self-contained or withdraw it until the companions are public and the chain of dependencies is frozen with DOIs.

**P1A-E3 (ESSENTIAL)**  
**Location:** Sec. X (pp. 20–21) + abstract claim of “perturbation-transparency result”  
**Problem:** The central theorem (Holst term decouples at all perturbative orders for canonical scalars) is proved only after assuming zero spin density and \(T=0\). The paper simultaneously states that realistic dark-energy routes require non-zero fermion content. The transparency result therefore does not apply to the very models whose closure is claimed.  
**Required fix:** Either restrict the transparency theorem to the stated assumptions or demonstrate it survives non-zero spin density.

**P1A-M1 (MAJOR)**  
**Location:** Table I (p. 4) + Sec. XIII (p. 23)  
**Problem:** \(f_{NL}=-35/8\) is listed as a “testable prediction” of the ECH framework. Body (Sec. XIII and XIV D) explicitly states it is a class-level matter-bounce signature, erased once \(N_{\rm tot}-N_{\rm exit}\gtrsim\mathcal{O}({\rm few})\), and survives only under Assumption (f) of a companion paper. No ECH-specific derivation or robustness test is supplied.  
**Required fix:** Remove from Table I or re-label as “ECH-independent class test.”

**P1A-M2 (MAJOR)**  
**Location:** Sec. IV D (p. 13) + abstract \(\beta\approx0.27^\circ\)  
**Problem:** The quoted birefringence angle is obtained by fitting a free spectator ALP with \(m_\theta\sim H_0\). The paper concedes this re-imports the cosmological-constant problem and is “not derived from the ECH action.” The abstract presents it as a benchmark consistency point of the ECH routes.  
**Required fix:** Remove numerical \(\beta\) claim from abstract or qualify it as an external ALP fit that does not close any ECH channel.

**P1A-M3 (MAJOR)**  
**Location:** Entire Sec. IX (pp. 16–20) — 14 “barriers”  
**Problem:** Barriers 8–14 are labeled “observational-channel branches” yet several (B8, B14) are simply re-statements of the perturbation-transparency result or of standard Planck suppression. The catalog therefore inflates the number of logically independent constraints.  
**Required fix:** Provide an explicit logical-independence matrix or reduce the count to the seven foundation classes that are genuinely distinct.

**P1A-M4 (MAJOR)**  
**Location:** Fig. 4 (p. 16) + Sec. VII  
**Problem:** Combined significance curves assume correlation coefficients \(\rho=0,0.3,0.5\) between \(f_{NL}\) and \(\beta\) without any justification or covariance matrix from the actual surveys. The 5\(\sigma\) projection is therefore not reproducible from the displayed information.  
**Required fix:** Either compute the joint covariance or remove the combined curves.

**P1A-N1 (NIT)**  
**Location:** Title page (p. 1)  
**Problem:** Date “June 19, 2026” is in the future.  
**Required fix:** Correct to actual submission/preprint date.

**P1A-N2 (NIT)**  
**Location:** Multiple figure captions (e.g., Fig. 5)  
**Problem:** Fine-tuning “score” axis is labeled in orders of magnitude but never defines the reference scale or the precise logarithmic measure used.  
**Required fix:** Add explicit definition in caption.

**Summary recommendation: REJECT**

The manuscript cannot be evaluated as a standalone contribution. Its headline numerical claims are either imported from unavailable companions or are explicitly not distinctive predictions of the ECH framework once all stated assumptions and caveats are restored. The abstract systematically overstates both the strength of the “closure” and the ECH-specificity of the surviving observables. Until the work is made self-contained and the abstract is brought into exact register with the body’s final calibrated statements, it does not meet the standards of Physical Review D.