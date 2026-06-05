# P1A 2026-06-04_R2pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 21.9s

---

Referee report for:  
P1A – “Channel‐Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”  
Round: 2026-06-04_R2pt  

I have read the full 21-page manuscript with the mandate of auditing the mathematical/statistical consistency of every quantitative claim, the dimensional sound-ness of every formula and the evidential chain behind every number quoted in the Abstract and Conclusions.  Below I list the problems found, classified according to the journal’s four-level rubric.

FINDINGS  
––––––––––  

ESSENTIAL  

P1A-B1 §I p.1–2.  “We report 13 logically-independent mechanism-class constraints … (14 historical catalog entries …).”  
Problem The body still counts B8 and B14 as distinct barriers even after explicitly stating that “B8 is the observational consequence of B14” (Abstract lines 14–17; §IX heading).  They are therefore not logically independent.  
Fix Re-state the total as 12 independent constraints (or re-split B8 into a demonstrably independent mechanism).  All subsequent tallies (Abstract, Table I, Table II, Conclusions line 2) must be updated.

P1A-B2 Eq. (6) / Appendix B.  Off-shell mass dimension error.  
Problem The parity-odd operator is admitted to have dimension +1 but is nevertheless equated to a vacuum-energy density (dimension +4) via the ad-hoc scaling “[(α/M) MPl] MPl4”.  No derivation is provided and the putative factor of MPl3 is inserted by hand (Appendix B).  Without a controlled EFT derivation the amplitude constraints claimed on all four “routes” have no basis.  
Fix Either (i) supply a complete operator-level derivation showing how the missing three powers of mass arise, or (ii) drop every quantitative statement that relies on Eq. (6) being the dark-energy operator.  The channel-closure claims of §IV and the Ntot≈92 bookkeeping must be rewritten accordingly.

P1A-B3 §II C 1 “Reheating thermal-reset barrier”.  
Problem Authors simultaneously invoke exponential dilution e−3Ntot and total thermal erasure of the axial current.  If the thermal reset is exact, the e−3Ntot factor is irrelevant; if it is partial, a quantitative residual must be propagated.  The paper uses whichever gives the desired bound in each section without consistency.  
Fix Decide whether the reheating reset is complete or partial, quantify the residual torsion source ⟨J5⟩T including its variance, propagate that single choice through all amplitude budgets (Routes 1–4, Barriers 1–14, Table I, Fig. 1, Conclusions).

P1A-B4 Cross-referenced companion papers.  
Problem All numerical posteriors (H0, σ8, ∆Neff, β, γPTA, Fisher σ(fNL)) are said to reside in “companion work in preparation”.  None are available to the referee, hence none are auditable.  PRD policy forbids results that cannot be reproduced from the submitted document set.  
Fix Either append the necessary material to the present submission (data tables, MCMC chains, pipeline description, likelihood versions, convergence diagnostics) or remove every result that depends on unpublished companions.

P1A-B5 σ–mixing error (Instruction §7).  
Problem Abstract line 38 f–41 f compares the WMAP+Planck 3.6 σ birefringence detection with the ACT 2.9 σ detection and treats the combined significance as > 4 σ without any joint-likelihood construction (Sec. III A repeats the error).  These σ values arise from different data sets and analysis pipelines and are not on the same null scale.  
Fix Quote each significance separately or perform a proper combined-likelihood analysis.  Remove any statement that presents them as additive evidence.

P1A-B6 Primary estimator not pre-declared.  
Problem Route-2 closure (§IV B) uses the ratio ∆θone-loop /∆θobs but the definition of ∆θobs (WMAP+Planck central value or central±σ or ACT value?) is chosen a posteriori.  
Fix Specify the estimator explicitly before the calculation and lock the choice for all subsequent significance tests.

P1A-B7 Version-history artefacts in body text.  
Occurrences: title page “v1A.0.44”, various footnotes “earlier-draft”, “change-log”, “(queued)”.  PRD formatting rules forbid internal version markers.  
Fix Delete all version-tracking language.

MAJOR  

P1A-M1 Eq. (15) “dimensionless ratio” still carries an unresolved ambiguity noted by the authors themselves (“the factor-of-∼100 ambiguity reflects ε-correction scaling”).  An order-of-magnitude uncertainty of two orders kills the claimed 58–60-decade suppression.  Provide a definitive derivation or widen the error bar and weaken the conclusion accordingly.  

P1A-M2 Duplicate phrasing.  Examples: “canonical canonical scalar”, “structure structural”, “coherent coherent axial component”.  Clean for clarity.  

P1A-M3 Page-count padding.  The submission runs 21 pages but ≥7 pages are meta-discussion of limitations, future work, version history and repository logistics.  The actual technical content could be presented in ≲15 pp.  PRD encourages concision.  Recommend cutting to ≤17 pp.  

P1A-M4 No quantitative uncertainty on γSU(2)=0.274.  The “∼0.020” spread is described as “scheme” not “statistical” and is then dropped from all error propagation.  Nonetheless the ρcrit window 0.27–0.41 ρPl is later treated as a ±1 σ interval.  Provide a consistent treatment: either propagate a well-defined theoretical prior or refrain from quoting σ-values on ρcrit.  

P1A-M5 Table II counts 14 barriers but footnote says B8 is not independent; mismatch with ESSENTIAL finding B1.  

P1A-M6 Equation cross-referencing inconsistent.  E.g. §II A 2 refers to “Eq. 14” for one-loop coefficient but Eq. (14) in the manuscript is the Chern–Simons operator, not a coefficient derivation.  Audit all equation numbers.

MINOR  

P1A-m1 Typo Eq. (3) bracket location ψ̄γ [a γ bc] ψ → ψ̄γ [a γ b γ c] ψ.  
P1A-m2 Mis-cited reference numbers twice off by one (Ref. [4]–[5] in §III A).  
P1A-m3 Unexpanded acronym “KDE” appears before definition.  
P1A-m4 Sentence starts with lowercase “p” (“p through the back door”, §IV D).  
P1A-m5 Units missing for M∆ , Eq. (5).  

NIT  

P1A-n1 Footnote marker “*” on title page remains after author e-mail; PRD style uses superscript dagger for sole affiliation.  
P1A-n2 Extra space before % in “> 100 orders of magnitude”.  
P1A-n3 Reference [10] missing journal volume page.  

## Summary recommendation  
MAJOR REVISIONS  

While the manuscript contains interesting arguments about the (non-)visibility of the Holst sector in perturbation theory, the present version fails several essential methodological standards: dimensional consistency of the central operator, dependence on unpublished companion analyses, mixing of incommensurable significance values, and internal counting inconsistencies.  These issues must be rectified before any scientific conclusion can be trusted.