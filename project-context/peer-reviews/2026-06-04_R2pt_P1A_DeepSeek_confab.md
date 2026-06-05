# P1A 2026-06-04_R2pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 162.6s

---

## Referee Report: Confabulation-Hunter Mode  

**Paper:** P1A  
**Round:** 2026-06-04_R2pt  
**Referee:** Confabulation-Hunter (Reasoning Mode)  

### I. GENERAL ASSESSMENT  
The paper presents a channel-level amplitude closure of four minimal Einstein-Cartan-Holst (ECH) dark-energy routes, anchored by a perturbation-transparency theorem for scalar matter. While the structural argument is ambitious, critical load-bearing scalars lack traceable provenance, and key claims rely on phenomenological ansätze without derivation. The paper acknowledges limitations (e.g., Appendix B), but this does not resolve the fundamental issue: central quantitative claims are unsupported by reproducible computations or datasets. Internal consistency is adequate, but the absence of provenance for headline figures and reliance on unpublished companion works undermine reproducibility.  

---

### II. FINDINGS  

#### **ESSENTIAL FINDINGS**  
**P1A-E1: Abstract & Sec. II C (p. 6); Sec. IX; Appendix B**  
- **Problem:** The dark-energy mapping relies on the scaling ansatz \(\rho_\Lambda = \Xi M_{\text{Pl}}^4\) with \(\Xi \equiv (\alpha/M) M_{\text{Pl}} D_{\text{inf}}\) (Eq. 10, 24), where \(D_{\text{inf}} \propto e^{-3N_{\text{tot}}}\) (Eq. 11). The value \(N_{\text{tot}} \approx 92\) is fitted to match \(\rho_\Lambda \sim (2.3 \text{ meV})^4\) but is derived from a phenomenological ansatz (Appendix B) lacking first-principles ECH derivation. The ansatz’s mass-dimension mismatch (\([\mathcal{L}_{\text{odd}}] = +1\) vs. required \(+4\)) is noted but not resolved, making \(N_{\text{tot}}\) untraceable.  
- **Fix:** Derive the scaling from ECH dynamics or provide a reproducible script (JSON/Python) demonstrating the fit to \(\rho_\Lambda\).  

**P1A-E2: Sec. IV B (p. 9); Sec. III A**  
- **Problem:** The closure of Route 2 (one-loop graviton corrections) claims suppression \(\Delta\theta_{\text{one-loop}}/\Delta\theta_{\text{obs}} \sim 10^{-58}\)–\(10^{-60}\) (Eq. 15), but the derivation silently omits a factor of \(M_{\text{Pl}}\) in the numerator (restored as \(H_0/M_{\text{Pl}}\)), invalidating the dimensionless ratio. The value is irreproducible from displayed inputs alone.  
- **Fix:** Provide explicit dimensional analysis showing unit consistency and a script verifying the suppression ratio.  

**P1A-E3: Sec. X (p. 14)**  
- **Problem:** The perturbation-transparency theorem (Sec. X) claims torsion vanishes at "all perturbation orders" for scalar *and* tensor sectors but only proves the scalar case (Sec. X B). Tensor-sector decoupling is asserted without proof (Sec. X C), overclaiming the result.  
- **Fix:** Extend the proof to tensor perturbations or qualify the theorem as scalar-only.  

---

#### **MAJOR FINDINGS**  
**P1A-M1: Abstract; Sec. IV E (p. 11); Sec. IX**  
- **Problem:** The "13 logically-independent barriers" (Table II) are presented as closing all minimal ECH routes, but Barrier 8 (parity-even interaction) is explicitly subsumed by Barrier 14 (perturbation transparency). Counting them as independent overstates the constraint catalog rigor.  
- **Fix:** Revise to 12 independent barriers or justify the duplication.  

**P1A-M2: Sec. II B (p. 6); Sec. IX N**  
- **Problem:** \(\rho_{\text{crit}} \simeq 0.27–0.41 \rho_{\text{Pl}}\) (quantum bounce density) cites Ashtekar & Singh (2011) but extrapolates \(\rho_{\text{crit}} \simeq 0.27 \rho_{\text{Pl}}\) for \(\gamma_{\text{SU(2)}} \approx 0.274\) without a published source. This value affects Barrier 12 (GW energy ceiling) and is not reproducible.  
- **Fix:** Provide a calculable formula or cite a derivation for \(\rho_{\text{crit}}(\gamma)\).  

**P1A-M3: Sec. XIII (p. 16); Sec. III A**  
- **Problem:** The ALP birefringence benchmark \(\beta \approx 0.27^\circ\) is presented as a "consistency point" but lacks provenance. It is neither derived from ECH nor traceable to a dataset/script (e.g., is it the midpoint of \(0.215^\circ\)–\(0.342^\circ\)?).  
- **Fix:** Clarify its origin and provide a matching script or reference to companion work [6].  

---

#### **MINOR FINDINGS**  
**P1A-m1: Sec. II A 2 (p. 5); Sec. IV A**  
- **Problem:** The parity-odd coefficient \(\alpha/M \sim 10^{-21} \text{ GeV}^{-1}\) (motivated by one-loop estimates) is used in amplitude closure (Route 4) but not verified against a reproducible calculation (e.g., Eq. 7).  
- **Fix:** Provide a script computing \(\alpha/M\) from Eq. 7 or cite a public code.  

**P1A-m2: Sec. XIV D (p. 17)**  
- **Problem:** The tension between dark energy (\(N_{\text{tot}} \approx 92\)) and bounce \(f_{\text{NL}}\) (erased for \(N_{\text{tot}} \gtrsim 60\)) states \(k_{\text{bounce}}^{\text{phys}} \sim e^{32} k_{\text{SPHEREx}}\) but omits the exponent base (\(a^{-1} \propto e^{-N}\)), making the factor \(e^{32}\) irreproducible from text alone.  
- **Fix:** Clarify \(k_{\text{bounce}}^{\text{phys}} / k_{\text{SPHEREx}}^{\text{phys}} = e^{N_{\text{tot}} - N_{\text{exit}}}\) with \(N_{\text{exit}} \approx 60\).  

---

#### **NITS**  
**P1A-N1: Header (p. 1)**  
- **Problem:** Version-history artifact ("v1A.0.44") appears in the date line.  
- **Fix:** Remove version tag.  

**P1A-N2: Sec. IV (p. 8)**  
- **Problem:** "canonical canonical-mask" typo (likely "canonical mask").  
- **Fix:** Correct to "canonical mask".  

---

### III. LENGTH ASSESSMENT  
The 21-page length is appropriate for a methods paper of this scope. No reduction recommended.  

---

### IV. CONFABULATION CHECKS  
- **σ-values:** No σ-values presented as comparable across null procedures.  
- **Version-history:** Flagged as NIT (P1A-N1).  
- **Duplicate phrases:** Flagged as NIT (P1A-N2).  
- **Abstract accuracy:** The abstract accurately summarizes the perturbation-transparency theorem and route closures but notes limitations (e.g., ansatz in Appendix B).  

---

## SUMMARY RECOMMENDATION  
**MAJOR REVISIONS**  

### Justification  
The paper’s core contribution—a channel-level closure of four ECH dark-energy routes via a perturbation-transparency theorem—is conceptually valuable. However, **load-bearing scalars** (\(N_{\text{tot}} \approx 92\), \(\rho_{\text{crit}}\), \(\beta \approx 0.27^\circ\)) lack traceable provenance, relying on unpublished companion works [2,6] or phenomenological ansätze without derivation. The Route 2 suppression claim (P1A-E2) and tensor-sector transparency (P1A-E3) are unverified, and the "13 barriers" catalog (P1A-M1) overcounts. Addressing these issues is essential for rigor. While the paper acknowledges limitations (e.g., Appendix B), revisions must provide reproducible foundations for key numbers or explicitly label them as assumptions. Companion works [2,6] should be made public to verify MCMC/ALP fitting claims.