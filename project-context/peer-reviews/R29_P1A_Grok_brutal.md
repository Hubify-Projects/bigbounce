# P1A R29 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.57.pdf` md5=958587c7 pages=27
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 101.6s

---

**Referee Report**

**Paper:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Journal target:** Phys. Rev. D

**Date of report generation:** based on rendered PDF pages 1–27

**P1A-E1 (ESSENTIAL)**  
Section: Title + first paragraph (p. 1)  
Problem: Title asserts “Channel-Level Closure”; opening paragraph states the four routes “are not proven to be a complete diffeomorphism-invariant operator basis” and repeatedly labels the analysis “channel-level assessment, not an operator-level theorem”.  
Required fix: Rewrite title and all closure language to match the explicit scope limitation stated in the text, or supply the missing operator-level proof.

**P1A-E2 (ESSENTIAL)**  
Section: Abstract-equivalent text (p. 1) and Sec. X (p. 18)  
Problem: Abstract calls the central result “a perturbation-transparency theorem”; body restricts the result to “canonical scalar matter” and states the Holst term “decouples cleanly from scalar/tensor observables” only after five explicit assumptions (zero spin density, zero torsion, Levi-Civita reduction, Bianchi identity, no non-minimal couplings). No general proof is given.  
Required fix: Either prove the theorem without the five restrictions or downgrade the abstract claim to “result under stated assumptions.”

**P1A-E3 (ESSENTIAL)**  
Section: Multiple locations (pp. 1, 3, 4, 12, 13, 19, 23)  
Problem: >15 load-bearing numerical results (H₀ = 67.68 ± 1.06, ΔN_eff = −0.020 ± 0.169, f_NL = −35/8, β = 0.27°, N_tot ≈ 92, etc.) are imported from “companion work in preparation [2,6]” or “Paper I(b)”. No standalone derivation or table of inputs appears. Violates rule 18 (standalone-reader test).  
Required fix: All quantitative claims must be recomputed or tabulated inside the present manuscript with explicit frozen data vectors.

**P1A-E4 (ESSENTIAL)**  
Section: p. 1 (date line)  
Problem: Submission date listed as “June 10, 2026” with internal tag “v1A.0.57”. This is future-dated and contains version-control metadata inside the rendered PDF.  
Required fix: Remove all internal versioning strings and supply a current calendar date.

**P1A-M1 (MAJOR)**  
Section: Sec. IV (pp. 9–13) and Table II (p. 17)  
Problem: All four “closures” are performed at the amplitude-budget level using phenomenological ansätze (Eq. (B2), on-shell scaling +1, D_inf ∼ 10^{-121}). The text repeatedly states “not a derivation”, “ansatz, not a controlled EFT”. No explicit operator matching or counter-term calculation is supplied.  
Required fix: Either elevate the closures to operator level or re-label every route as “phenomenologically disfavored under ansatz X”.

**P1A-M2 (MAJOR)**  
Section: Sec. X (pp. 18–19) and Fig. 1 (p. 5)  
Problem: Perturbation-transparency proof (Eq. 23) uses the algebraic Bianchi identity on a torsion-free connection; the same identity is known to fail once the Holst term or non-minimal fermion couplings are retained. The paper excludes those sectors by fiat.  
Required fix: State the precise domain of validity in every equation and figure caption.

**P1A-M3 (MAJOR)**  
Section: Abstract (p. 1) and Sec. XIII (p. 21)  
Problem: Claims “two mechanism-independent tests survive”. Both tests (f_NL = −35/8 and β ≈ 0.27°) are explicitly labeled “not distinctive ECH predictions” and “class-level” (shared with any w = 0 matter-bounce). Effect-size quantification (Cramér’s V or fractional amplitude) is absent.  
Required fix: Remove “mechanism-independent” language or supply a quantitative discriminator that is unique to ECH.

**P1A-M4 (MAJOR)**  
Section: Sec. II C and Appendix B (pp. 7–8, 24)  
Problem: The on-shell identification ρ_Λ = Ξ M_Pl^4 with Ξ ∼ 10^{-123} is labeled an “ansatz, not a derivation”. All subsequent N_tot = 92 and fine-tuning scores rest on this single un-derived relation.  
Required fix: Derive the scaling from the ECH action or flag every downstream number as conditional on an external ansatz.

**P1A-N1 (MINOR)**  
Section: Fig. 5 (p. 15)  
Problem: Fine-tuning axis labeled “orders of magnitude” but the plotted values (10^5, 10^40, …) are not accompanied by the exact formula used to convert residual tuning into the plotted integer.  
Required fix: Add explicit formula in caption.

**P1A-N2 (NIT)**  
Section: Throughout  
Problem: Duplicate phrasing “canonical canonical-mask” does not appear, but repeated verbatim blocks (“the same coupling that produces β_obs requires an ultralight-mass tuning m_θ ∼ H_0”) occur on pp. 1 and 12.  
Required fix: None required for acceptance, but tighten prose.

**Additional audit notes**  
- No figure shows an actual computed power spectrum, bispectrum, or MCMC chain; all are schematic.  
- Bibliography entries for companion papers lack arXiv IDs or DOIs; several are labeled “in preparation”.  
- Abstract sentence “the central result is a perturbation-transparency theorem” is stronger than the calibrated statement on p. 18 (“restricted to canonical scalar matter”).  
- Rule 19 (effect sizes) violated for every σ claim.

**Summary recommendation**  
REJECT

The manuscript does not meet Physical Review D standards. It presents a catalog of phenomenological barriers rather than a controlled calculation, relies on unpublished companion papers for every quantitative result, and maintains a persistent mismatch between title/abstract claims of “closure” and “theorem” and the explicit limitations stated in the body. The work is not self-contained, contains future-dated internal metadata, and supplies no new observable prediction that is both distinctive to minimal ECH and rigorously derived from the action. A substantially revised, self-contained manuscript limited to ∼12 pages that derives (rather than assumes) its key scalings would be required before resubmission.