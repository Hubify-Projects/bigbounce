# P2 2026-06-04_R6clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 216.0s

---

## Referee Report

### ESSENTIAL Revisions

- **P2-E1: Systematic budget breakdown (Section VII, Abstract)**  
  Problem: The abstract states a "combined systematic budget" reduces the detection significance from 5.2–5.5σ to 3–5σ, but Section VII does not quantify how individual systematics contribute to this reduction. The budget includes noise-weighted shape mismatch, ϵ-correction, polynomial-coefficient scatter, photo-z degradation, PNG bias, \(b_\phi\) marginalization, and GR projection, but no arithmetic or error propagation is shown.  
  Fix: Provide a quantitative breakdown (e.g., Fisher-matrix marginalization or Monte Carlo simulation) showing how each systematic degrades \(\sigma(f_{\text{NL}})\). For example, specify the incremental \(\sigma\) increase from GR effects (\(\sigma_{\text{GR}} = 0.5-1.0\)) and \(b_\phi\) uncertainty (20–50% prior).

- **P2-E2: \(\sigma\) values without scale qualification (Section IV, Abstract)**  
  Problem: The abstract presents \(\sigma(f_{\text{NL}}) \approx 0.7\) (SPHEREx bispectrum) and \(\sigma(f_{\text{NL}}) \approx 0.5\) (MegaMapper ideal) as directly comparable, but SPHEREx uses LSS noise weighting while MegaMapper's "ideal" case lacks specification. This implies equivalence without qualifying noise models or weighting schemes.  
  Fix: Explicitly state that \(\sigma\) values are not on the same scale; clarify noise-weighting assumptions (e.g., "MegaMapper \(\sigma = 0.5\) assumes CMB Fisher weighting, while SPHEREx \(\sigma = 0.7\) uses LSS noise weighting").

### MAJOR Revisions

- **P2-B1: Template recovery range mismatch (Section III B)**  
  Problem: The text states \(r = 0.84 \pm 0.02\) but also reports \(r \in [0.829, 0.876]\) across weighting schemes. The interval \([0.829, 0.876]\) is not fully contained within \(0.84 \pm 0.02 = [0.82, 0.86]\) (e.g., 0.876 > 0.86), creating inconsistency.  
  Fix: Revise the central value or uncertainty to cover the full range (e.g., \(r = 0.85 \pm 0.03\)) and reconcile with the abstract's "84% ± 2%."

- **P2-B2: Headline significance provenance (Abstract, Section IV)**  
  Problem: The "headline" 5.2–5.5σ (optimistic) and 3–5σ (post-systematic) are not derived from displayed values alone. For instance, 5.5σ comes from \((4.375 / 0.7) \times 0.876\) (CMB Fisher), but the abstract does not cite Section III B for \(r = 0.876\) or Section IV for \(\sigma(f_{\text{NL}}) = 0.7\).  
  Fix: In the abstract, reference sections for all components (e.g., "5.2–5.5σ: Sec. IV [\(\sigma\)], Sec. III B [\(r\)]"). Show arithmetic for 3–5σ reduction in Section VII.

- **P2-B3: Convention sensitivity in abstract (Abstract, Conclusions)**  
  Problem: The abstract notes the Li & Brandenberger convention halves significance (to 1.5–2.5σ) but presents 3–5σ as the primary headline without clarifying that this assumes the Cai convention. This risks misinterpretation.  
  Fix: State prominently in the abstract: "Headline significance assumes Cai convention (Appendix A); Li & Brandenberger convention halves values."

- **P2-B4: Underdetermined polynomial scatter (Section II, Section II C)**  
  Problem: The \(\pm 0.13\) scatter in \(r\) (from \(c_1\)–\(c_6\) null space) is used in the systematic budget but lacks traceable code/data. The 10,000-sample scan is described, but no script/JSON is provided to reproduce \(r = 0.85 \pm 0.13\).  
  Fix: Publish code for the null-space scan and \(r\) calculation (GitHub link in paper) or include key outputs as supplementary material.

### MINOR Revisions

- **P2-M1: Ratio approximation (Abstract)**  
  Problem: The contrast ratio \(|f_{\text{NL}}^{\text{bounce}}| / |f_{\text{NL}}^{\text{inf}}| \approx 290\) is approximate; exact calculation gives \(4.375 / 0.015 \approx 291.7\).  
  Fix: Use the exact value or note rounding (e.g., "\(\approx 290\) [291.7 exact]").

- **P2-M2: Bayes factor prior dependence (Abstract, Section VI)**  
  Problem: The abstract cites Bayes factors BF ∼ 10–17 without emphasizing prior sensitivity (e.g., BF drops to ∼4 for narrow curvaton priors). This could mislead readers.  
  Fix: Add "prior-dependent" when reporting BF ranges (e.g., "BF ∼ 10–17 under broad multifield priors").

- **P2-M3: \(\epsilon\)-correction uncertainty (Section II C, Abstract)**  
  Problem: The \(\epsilon\)-correction uncertainty (1–8%) is quoted but not propagated in abstract significance ranges (5.2–5.5σ).  
  Fix: Specify if 5.2–5.5σ includes \(\epsilon\) uncertainty or adjust ranges to reflect it.

- **P2-M4: Injection-recovery test details (Section II)**  
  Problem: The 200 injection-recovery realizations use isotropic Gaussian noise and full-sky geometry, but realistic SPHEREx masking (\(f_{\text{sky}} \approx 0.7\)) is noted as a caveat without degradation quantification.  
  Fix: Add a footnote estimating the \(1/\sqrt{f_{\text{sky}}}\) noise penalty (e.g., "realistic masking degrades \(\sigma(f_{\text{NL}})\) by \(\sim 19\%\)").

### NIT Revisions

- **P2-N1: "convergence is verified" reference (Section II)**  
  Problem: The phrase "convergence is verified at radii 10, 100, and 500 below" implies unreferenced figures/appendices.  
  Fix: Clarify (e.g., "convergence tested at radii 10, 100, 500 [not shown]").

- **P2-N2: "Important scope" phrasing (Section II)**  
  Problem: The phrase "Important scope of the underdetermination" is awkward.  
  Fix: Rephrase (e.g., "The underdetermination has significant implications").

---

## Summary Recommendation  
MAJOR REVISIONS  

**Justification:** The paper presents a timely and valuable forecast for testing the matter bounce with SPHEREx/MegaMapper. However, major revisions are required to ensure reproducibility and clarity. Key issues include: (1) The systematic budget lacks quantitative breakdown (P2-E1), undermining the 3–5σ claim; (2) Template recovery ranges are inconsistent (P2-B1), and headline significances lack traceable arithmetic (P2-B2); (3) Critical convention sensitivities (P2-B3) and polynomial scatter (P2-B4) need better documentation. ESSENTIAL items must be fixed for validity. MINOR/NIT issues (e.g., prior sensitivity, phrasing) improve rigor. Addressing these will strengthen the paper's robustness and align with PRD's standards.