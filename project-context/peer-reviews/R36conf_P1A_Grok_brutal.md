# P1A R36conf — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.66.pdf` md5=5dff8674 pages=28
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 79.6s

---

**Referee Report**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Journal target:** Phys. Rev. D

**Date of review:** based on rendered PDF (28 pp. + front matter)

**Findings**

**P1A-E1 (ESSENTIAL)**  
**Location:** Abstract (p. 1) and every reference to “companion work in preparation [6]”, “Paper I(b)”, “Paper II”, “Paper III”, “Paper IV”.  
**Problem:** The paper is not self-contained. The central MCMC verification, Fisher forecasts, ALP parameter fitting, NaMaster pipeline validation, and all numerical \(\sigma(f_{NL})\) and \(\beta\) values are deferred to unpublished or “in-preparation” documents. The argument repeatedly states “MCMC details in companion work in preparation [6]” and “the 2.6–5\(\sigma\) realistic range reflects two forecast regimes”. A standalone reader cannot recompute or verify any headline significance.  
**Required fix:** All load-bearing numerical results and statistical claims must be reproduced inside the present manuscript (or the paper must be withdrawn until the companions exist and are cited with fixed arXiv numbers).

**P1A-E2 (ESSENTIAL)**  
**Location:** Abstract (p. 1) sentence “the central result is a perturbation-transparency result: for canonical scalar matter, torsion vanishes at all classical metric/scalar perturbation orders…”.  
**Problem:** The abstract claim is stronger than, and ordered differently from, the body’s final calibrated statement. The body (Sec. X, p. 18–19) explicitly restricts the result to “canonical scalar matter” and excludes “propagating torsion, dynamical Immirzi field, fermion-loop, and non-minimal-matter sectors”. The abstract omits these caveats.  
**Required fix:** Rewrite the abstract sentence to match the body’s final, restricted statement exactly.

**P1A-E3 (ESSENTIAL)**  
**Location:** Sec. X (pp. 18–19) and the Bianchi-identity step used to prove decoupling.  
**Problem:** The proof that the Holst dual contraction vanishes identically on the Levi-Civita connection (\(T=0\)) by the algebraic Bianchi identity \(R_{\mu[\nu\rho\sigma]}=0\) is applied inside a theory whose defining feature is torsion. The step is therefore circular for any configuration in which torsion is non-zero at linear order. The paper never demonstrates that the torsionful connection satisfies the same identity at the required order.  
**Required fix:** Provide an explicit, torsion-inclusive derivation or retract the “all orders” claim.

**P1A-M1 (MAJOR)**  
**Location:** Title, abstract, and Sec. IV (pp. 10–14).  
**Problem:** The title and abstract repeatedly use the word “closure”. The body (abstract + Sec. IV Scope paragraph) explicitly states that the four routes are examined only at channel/amplitude level under labeled scaling assumptions and that “we do not claim a full operator-basis closure”. The framing is therefore misleading.  
**Required fix:** Change title and all “closure” language to “amplitude-level no-go under stated scaling assumptions” or equivalent.

**P1A-M2 (MAJOR)**  
**Location:** Fig. 3 (p. 7) and associated text.  
**Problem:** The plotted \(\Delta H/H_{\Lambda\mathrm{CDM}}\) is \(\lesssim 3\%\) across the entire observable range and the two curves are visually indistinguishable. The paper presents this as a viable dark-energy route while simultaneously showing that the model is degenerate with \(\Lambda\)CDM at all current and near-future precision. No quantitative forecast of distinguishability is supplied inside the manuscript.  
**Required fix:** Either remove the claim that the construction solves the dark-energy problem or add an explicit, self-contained forecast demonstrating a detectable deviation.

**P1A-M3 (MAJOR)**  
**Location:** Sec. II C and Appendix B (pp. 7–8).  
**Problem:** The identification \(\rho_\Lambda=\Xi M_{\mathrm{Pl}}^4\) with \(\Xi\sim10^{-123}\) is labeled a “phenomenological scaling ansatz, not a derivation”. All subsequent fine-tuning claims rest on this ansatz. The paper never shows that the ansatz survives renormalization or is stable under the very Holst-sector corrections it discusses.  
**Required fix:** Either derive the scaling from the ECH action or demote all fine-tuning numerology to “illustrative only”.

**P1A-N1 (NIT)**  
**Location:** Front matter (p. 1).  
**Problem:** The submission date is given as “June 12, 2026 PDT — v1A.0.66”. A 2026 date on a manuscript under review in the present is an obvious internal bookkeeping artifact.  
**Required fix:** Remove the future date and version tag.

**P1A-N2 (NIT)**  
**Location:** Table I caption and footnote a (p. 4).  
**Problem:** Footnote a states the result is “reparameterized as sensitivity to \(N_{\mathrm{tot}}\); not solved.” This directly contradicts the abstract’s implication that the CC problem is addressed.  
**Required fix:** Align caption language with the body’s explicit admission.

**Summary recommendation**  
**REJECT**

The manuscript is not a self-contained, rigorously derived no-go theorem. It relies on unpublished companion papers for every statistical claim, its headline “perturbation-transparency” and “closure” language exceeds what the body actually proves, the Bianchi-identity argument is applied inside a torsionful theory without justification, and the only concrete prediction shown (Fig. 3) is visually indistinguishable from \(\Lambda\)CDM. These are first-read fatal defects for Phys. Rev. D.