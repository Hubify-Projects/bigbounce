# P1A 2026-06-04_R4fixed — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 33.6s

---

Referee report on  
P1A “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”  
ROUND: 2026-06-04_R4fixed  
Role: methodology / statistical rigor

================================================================
FINDINGS
================================================================

ESSENTIAL = must be fixed before publication  
MAJOR     = scientifically important but not fatal  
MINOR     = desirable clean-up  
NIT       = cosmetic

----------------------------------------------------------------
P1A-E1  (Abstract, first paragraph)  
Problem  : “Through 7 foundation studies … we report 13 logically-independent … (the prior count of 14…)” The reduction from 14 to 13 is asserted but no reproducible catalogue or enumeration table is supplied in the present version; Table II still contains 14 numbered barriers.  
Required : Provide an unambiguous list that matches the narrative count. Either (i) drop B8 or (ii) keep it and revert to “14”. Show the logic-dependence audit.

----------------------------------------------------------------
P1A-E2  (whole manuscript)  
Problem  : Numerous internal version-control artefacts remain: e.g. “R4: condensate internal-version language, CHANGELOG.md reference fixed”, “hUBIFY-2026-002”, “companion paper, this volume”, “GPU MCMC”, “IMPLEMENTATION MAP.md”, “footnote row ‘DESI DR2 w0wa (new)’ is running”. Such material violates PRD style and breaks the archival record.  
Required : Delete ALL internal tracking language, GitHub paths, footnotes describing live jobs, and code-names. Supply stable arXiv numbers or remove the references.

----------------------------------------------------------------
P1A-E3  (Sec. II A 3, Parameter Naturalness; Appendix B)  
Problem  : The key operator of Eq. (6) is admitted to possess wrong mass-dimension (+1). The authors still map it to ρΛ via the phenomenological ansatz (B2). No EFT completion or regulator is given. Yet the Conclusions claim “channel-level closure” as if a mathematically valid operator existed.  
Required : Either supply a formally dimension-four completion (with explicit loop, symmetry or curvature insertions) or change all statements of “closure” to an explicitly conditional form: “If such a +4 operator exists … then the four enumerated routes are closed.”

----------------------------------------------------------------
P1A-E4  (Sec. IV E, Closure summary)  
Problem  : Route 2 closure uses the ratio ∆θone-loop /∆θobs . The numerator is treated as αem/(4π) H0/MPl while the denominator is (α/M)βobs . The factor H0/MPl is compared to α/M with α/M expressed in GeV−1, but the authors drop the conversion 1 GeV = 1.6×10−10 J. The resulting 10−58 suppression could shift by ≥8 orders.  
Required : Give the ratio in a fully dimensionless form with all constants and conversion factors shown; propagate numerical uncertainty.

----------------------------------------------------------------
P1A-E5  (Secs. III A & XIV B)  
Problem  : Birefringence significance is quoted from WMAP+Planck as 3.6σ. The quoted σ uses the published 1σ error but then in Sec. XIIIB a 0.73σ difference test is performed with the same variance assumed independent. The variance budget is mixture of WMAP+Planck and forecast LiteBIRD noise—these are statistically incommensurable.  
Required : Re-compute the χ2 or likelihood with independent noise terms or state explicitly that the two error bars are treated as independent and justify. Otherwise drop the 0.73σ claim.

----------------------------------------------------------------
P1A-E6  (Sec. V, Data Methods)  
Problem  : Galaxy-spin null result is asserted but no numbers are printed in this paper; all details are deferred to “Paper IV [23]” which is “in preparation”. The null enters later arguments (Barrier 8).  
Required : Supply at minimum: sample size, sky coverage, classifier accuracy, dipole amplitude A1 with 1σ and χ2 /p-value. Without these the inference chain is not auditable.

----------------------------------------------------------------
P1A-E7  (Abstract, Conclusions, Table IV)  
Problem  : H0 = 67.68±1.06, σ8, ∆Neff etc. are quoted but said to come from an “internal MCMC” in a companion work not yet on arXiv. Reproducibility requirement of PRD is violated.  
Required : Either publish the companion chain (arXiv reference + public link) or remove the numbers.

----------------------------------------------------------------
P1A-E8  (Sec. X, Perturbation-transparency “proof”)  
Problem  : The proof is a five-sentence sketch. Step 1 assumes scalar matter → J5 = 0 but neglects quantum spin density of the vacuum; Step 3 assumes Γ = Γ̊ without verifying that variation of Holst term with respect to metric still vanishes. No explicit perturbation expansion is shown.  
Required : Provide a detailed derivation: write the perturbed tetrad and connection to first order, show that the Holst contribution to δ2S vanishes, and that no boundary terms survive in the cubic action. Otherwise downgrade “theorem” to conjecture.

----------------------------------------------------------------
P1A-E9  (Sec. IX, Barrier catalogue)  
Problem  : Several “barriers” (e.g. B5, B6) are qualitative statements with no quantitative threshold. Yet the conclusions claim “closure at amplitude-budget granularity”.  
Required : For every barrier give either (a) an inequality of the form X < Xcrit with numbers, or (b) label it explicitly as heuristic and remove from the quantitative closure count.

----------------------------------------------------------------
P1A-E10  (Throughout)  
Problem  : Claims of 3-5σ SPHEREx sensitivity are copied verbatim from Heinrich et al. (2024) but the current work adds extra degradations (bφ, photo-z) without re-running the Fisher matrix. Numbers are therefore speculative.  
Required : Either re-run the Fisher forecast with the stated degradations and present the covariance matrix, or re-phrase as “expected to be O(1–5)σ based on external study.”

----------------------------------------------------------------
P1A-E11  (Sec. IV D)  
Problem  : The naturalness argument against Route 4 mixes the loop-matched α/M with the phenomenological fit α/Mfit ≈ 10−21 GeV−1. No uncertainty or prior range is specified, so the “overshoot” by 22–36 OOM is not statistically defined.  
Required : Provide a prior on α/M, propagate to ρθ, quote a confidence level for the overshoot, or re-classify the route as “not excluded, requires tuning”.

----------------------------------------------------------------
P1A-E12  (multiple locations)  
Problem  : Null-model σ values from different procedures are mixed: e.g. Planck suppression factors, Cℓ errors, LiteBIRD forecast errors. They are treated on the same “σ” scale.  
Required : State explicitly which σ belongs to which likelihood, stop comparing unlike σ in counts of “orders of σ”, or rescale to a common likelihood.

----------------------------------------------------------------
P1A-E13  (Formatting)  
Problem  : Duplicate phrases: “canonical canonical-mask”, “Goes goes”, “phys phys kbounce”.  
Required : Scan and remove duplicates.

----------------------------------------------------------------
MAJOR FINDINGS
----------------------------------------------------------------

P1A-M1  (Sec. II C 1)  
Uncertainty on (Treh/MGUT)3/2 prefactor is said to be “order-of-magnitude” but later used to claim Ntot ≈ 92±2. That precision is not supported. Quote Ntot with correct uncertainty (≈ ±10) or re-derive.

P1A-M2  (Sec. III A)  
Conversion 0.342° = 0.00597 rad is used once but later β is treated in degrees; maintain consistent units.

P1A-M3  (Sec. IV A)  
Four-fermion energy density bound “many orders below ρΛ” is asserted without calculation for recombination epoch. Provide density estimate with fermion abundance.

P1A-M4  (Sec. VI)  
Systematics list is qualitative. Provide a quantitative error budget for each term (GR projection, bias, photo-z).

P1A-M5  (Table IV)  
“Verified value” column lists γPTA = 2.567±0.382 from an unpublished “real-KDE GPU MCMC”. Needs citation or removal.

----------------------------------------------------------------
MINOR FINDINGS
----------------------------------------------------------------
P1A-m1  References [2],[6],[46] etc. labelled “in preparation” violate PRD reference policy.  
P1A-m2  ρcrit formulas use inconsistent γ values (0.2375 and 0.274) without showing derived numbers—supply both.  
P1A-m3  Footnote marker “1” in Sec. III B calls a footnote inside a footnote; re-structure.  
P1A-m4  Section numbering skips from X to XI without page break; check LaTeX \clearpage.  
P1A-m5  Several equations unnumbered but referenced (e.g. “Eq. 14” once appears as (14) and later as Eq. (15)).

----------------------------------------------------------------
NITS
----------------------------------------------------------------
P1A-n1  Typo “spectrally Unusal” → “Unusual”.  
P1A-n2  Comma splice in abstract lines 12–14.  
P1A-n3  PACS numbers deprecated—use 2020 Physics Subject Headings.  
P1A-n4  Wrong prime: h′′ij uses prime but earlier derivatives dot.

================================================================
## Summary recommendation
MAJOR REVISIONS

The manuscript presents an ambitious synthesis, but key methodological elements are either unpublished, internally referenced, or mathematically incomplete. The operator dimensionality mismatch, sketch-level “proof” of perturbation transparency, mixing of heterogeneous σ values and reliance on non-archived companion analyses must be rectified. With the essential fixes, the paper could become a useful negative result for the community, but in its present form it does not meet PRD reproducibility or methodological standards.