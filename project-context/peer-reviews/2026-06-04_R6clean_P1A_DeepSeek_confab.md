# P1A 2026-06-04_R6clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 155.3s

---

## Referee Report: Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter

### ESSENTIAL FINDINGS
**P1A-E1: Section IV, Page 8**  
- **Problem**: Internal review artifact: "Three substantive theory-derivation issues were identified during preparation of this paper and are documented here for the record" appears in body prose. This is version-history language inappropriate for final publication.  
- **Fix**: Remove this sentence entirely.  

### MAJOR FINDINGS  
**P1A-M1: Section IV D, Page 10**  
- **Problem**: Headline figure \(\beta \approx 0.27^\circ\) lacks traceable provenance. The text claims it is a "benchmark consistency point" from GR+ALP setups but provides no source (e.g., script/dataset) for this specific value. The midpoint of cited observations (\(0.342^\circ \pm 0.094^\circ\) and \(0.215^\circ \pm 0.074^\circ\)) is \(\approx 0.2785^\circ\), not \(0.27^\circ\).  
- **Fix**: Justify the value with a source (e.g., companion Paper I(b) ALP fitting script) or correct to the observational midpoint (\(0.28^\circ\)).  

**P1A-M2: Section IX, Page 12–14**  
- **Problem**: Barrier counts are inconsistent. The abstract claims "13 logically-independent" constraints, but Table II lists 14 barriers (B1–B14) and states B8 is "subsumed by B14," implying 13 independent barriers. However, B13 ("Gravitational Democracy") is not justified as logically dependent on others, creating ambiguity.  
- **Fix**: Reconcile the count: Either remove B13 if redundant or clarify its independence. Update all text/table to reflect exact logical dependencies.  

### MINOR FINDINGS  
**P1A-M3: Section II B, Page 6**  
- **Problem**: Critical density \(\rho_{\text{crit}} \simeq 0.27–0.41 \rho_{\text{Pl}}\) lacks provenance. The citation [11] (Ashtekar & Singh) quotes \(\rho_{\text{crit}} \simeq 0.27–0.41 \rho_{\text{Pl}}\) for \(\gamma = 0.2375\), but the paper uses \(\gamma_{\text{SU(2)}} \approx 0.274\) without deriving the extrapolation.  
- **Fix**: Provide a source (e.g., calculation script) for \(\rho_{\text{crit}}\) at \(\gamma = 0.274\) or cite a derivation.  

**P1A-M4: Section IV B, Page 9**  
- **Problem**: Dimensionally inconsistent suppression ratio: \(\Delta\theta_{\text{one-loop}} / \Delta\theta_{\text{obs}} \sim 10^{-58}\) to \(10^{-60}\) relies on \(H_0 / M_{\text{Pl}} \sim 10^{-61}\), but \(H_0\) is in eV while \(M_{\text{Pl}}\) is in GeV, requiring explicit unit conversion.  
- **Fix**: Add unit conversion (e.g., \(H_0 \approx 1.5 \times 10^{-33}\) eV, \(M_{\text{Pl}} \approx 1.2 \times 10^{18}\) eV) to reproduce the ratio.  

**P1A-M5: Section XIV D, Page 17**  
- **Problem**: Arithmetic irreproducibility: The scale ratio \(k_{\text{bounce}}^{\text{phys}} / k_{\text{SPHEREx}}^{\text{phys}} \sim e^{32}\) assumes \(N_{\text{tot}} \approx 92\) and \(N_{\text{exit}} \approx 60\) but omits the definition of \(N_{\text{exit}}\). With \(N_{\text{tot}} - N_{\text{exit}} = 32\), \(e^{32} \approx 7.9 \times 10^{13}\), but the text states \(\sim e^{32}\) without showing \(k_{\text{SPHEREx}}\) values.  
- **Fix**: Define \(N_{\text{exit}}\) (e.g., e-folds at CMB horizon exit) and provide \(k_{\text{SPHEREx}}\) ranges to verify \(e^{32} k_{\text{SPHEREx}}\).  

### NIT FINDINGS  
**P1A-N1: Section III A, Page 7**  
- **Problem**: Ambiguous phrasing: "CMB E-B cross-correlations" subsection lacks a clear connection between Eq. (12) and the ECH framework.  
- **Fix**: Clarify that Eq. (12) is a generic birefringence formula, not ECH-specific.  

**P1A-N2: Throughout**  
- **Problem**: Overuse of "companion work in preparation" for critical details (e.g., MCMC in Paper I(b), fNL forecast in Paper II). This impedes verification.  
- **Fix**: Include key results (e.g., \(\sigma(f_{\text{NL}})\) values, ALP fitting method) in supplementary materials.  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

### Justification  
The paper presents a valuable theoretical contribution by closing four minimal ECH dark-energy routes via 13(14) structural barriers and proving a perturbation-transparency theorem for scalar matter. However, major revisions are required due to:  
1. **Unsupported headline figures**: \(\beta \approx 0.27^\circ\) lacks provenance and conflicts with observational midpoints.  
2. **Internal artifacts**: Version-history language in Sec. IV undermines publication readiness.  
3. **Inconsistent logic**: Ambiguous barrier counts (13 vs. 14) and unreproducible arithmetic (e.g., scale ratios, suppression factors) weaken the core argument.  
4. **Provenance gaps**: Critical values (\(\rho_{\text{crit}}\), \(N_{\text{tot}} \approx 92\)) need explicit sources or derivations.  

The paper length (21 pages) is appropriate for the scope. Addressing these issues will ensure rigorous, reproducible results. Until resolved, the paper cannot be accepted.  

---  
**End of Report**