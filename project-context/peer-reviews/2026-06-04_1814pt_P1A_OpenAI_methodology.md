# P1A 2026-06-04_1814pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 24.0s

---

Referee report on  

P1A “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”  

PRD round 2026-06-04_1814pt  

Paper length = 21 pp  

================================================================  
FINDINGS  
================================================================  

ESSENTIAL (acceptance impossible until fixed)  
---------------------------------------------  

E1  Section II A, p.5 – Dimensional mismatch of the “parity-odd operator”  
     Quote: “the leading contribution reduces to … has naïve mass dimension +1.”   
     Problem: a dimension-1 operator cannot be inserted in the action density without three extra mass powers.  All subsequent quantitative statements (Eqs. 6, 10, B2, the Ntot≈92 hierarchy, “Planck-scale bounce densities”, etc.) depend on treating this term as if it were dimension 4.  No rigorous derivation, regulator or counter-term completion is supplied.  
     Required fix: Either (a) supply a complete EFT derivation that promotes the operator to dimension 4 with explicit coefficients and shows renormalisability, or (b) delete every claim that relies on the operator contributing an energy density or a CMB birefringence signal.   

E2  Abstract & Conclusions – Untraceable numerical scalars  
     H0 = 67.68 ± 1.06, ∆Neff≈0, σ8, Ntot≃92, Ξ≈10-123, β≈0.27°, γPTA = 2.567 ± 0.382 are quoted as results but are not reproduced, nor are the input chains supplied in the manuscript.  Only a pointer to an “in-preparation companion” is given.  
     Required fix: Provide in this manuscript (or clearly reference an already-public document) the full likelihoods, priors, data sets, codes, and convergence diagnostics that produce every number appearing in the abstract or conclusions.  PRD does not accept forward-references to unpublished material.  

E3  Whole text – Reliance on six “companion papers in preparation”  
     Essential parts of the method (MCMC chains, NaMaster validation, SPHEREx Fisher matrix, galaxy-spin classifier, PTA KDE) are deferred to other documents not yet on arXiv or in refereed journals.  
     Required fix: Either incorporate all methodological detail and results in the present submission or make those companion papers publicly available and cite them as arXiv numbers.  

E4  Section IV – “Four-route closure” not demonstrated quantitatively  
     For R1–R4 the paper asserts amplitude suppressions (Planck-2, Planck-1, 10-63, etc.) but gives no step-by-step calculation, no numerical values for densities or coupling constants and, in the case of R2, admits that the coefficient is only an “EFT ansatz”.  
     Required fix: Supply complete numerical estimates with clearly stated assumptions and error propagation, or retract the claim that the routes are closed at amplitude level.  

E5  Section X – Perturbation-transparency “theorem” proved only for vacuum; fermions are later invoked  
     The proof sets S = 0 (no spin), immediately contradicting later discussion of torsion-generated four-fermion vertices.  The theorem is therefore not general.  
     Required fix: Either extend the proof to include non-vanishing spin sources or downgrade the statement to a special case applying only to a single scalar field.  

E6  Mixing of σ levels from different null tests (Instructions #7)  
     Example: §XII states “LiteBIRD will detect β at 9σ” but later the same observable is said to differ from the WMAP+Planck central value by only 0.73σ.  The paper treats the two σ as commensurate when drawing conclusions.  
     Required fix: Recalculate all significances on a common likelihood and state clearly which null hypothesis each σ refers to.  

E7  Internal artefacts (Instructions #8)  
     Strings such as “HUBIFY-2026-001A”,  “v1A.0.44”, “CHANGELOG.md”, “Paper I(b) Table IV row ‘DESI DR2 w0wa (new)’ ”, etc., appear throughout.  
     Required fix: Remove every version-history, repository path, or internal review note from the body text.  

E8  Duplicate/contradictory count of barriers (Instructions #9)  
     Abstract: “13 logically-independent (14 historical) barriers”.  Sec. IX Table II lists 14 numbered barriers while stating B8 is subsumed by B14.  The count is inconsistent.  
     Required fix: Provide one definitive list with a consistent count and remove duplicate numbering.  

E9  Primary estimator not pre-declared (Instructions #8)  
     The paper shifts between EB cross-spectra, β, fNL, γPTA without stating at the outset which is the primary figure of merit.  
     Required fix: Declare, before any data are used, the principal estimator(s) on which the main claims will be judged.  

E10 Companion GitHub repository not archival  
     A moving GitHub target does not satisfy PRD data-availability policy.  
     Required fix: Upload a frozen DOI-tagged archive (e.g. via Zenodo) containing all scripts and raw chains and cite that DOI.  

MAJOR  
------  

M1  Section II C – “Reheating thermal-reset barrier” is asserted without a calculation of the scattering rate compared to H.  Provide explicit rates or weaken the claim.  

M2  Equation 15 – Dimensional “ratio” still contains an implicit energy scale M.  Clarify the contraction to a pure number and propagate unit conversions.  

M3  Use of naturalness rhetoric (“relocates the fine-tuning”, “book-keeping”) in place of quantitative Bayesian evidence.  Replace by a statistical statement or delete.  

M4  Many references are “in preparation”.  Replace with arXiv numbers or fully document in the present manuscript.  

M5  Mixed units (eV, GeV, Planck = 1) within single equations; e.g. Eq. (15) multiplies H0 in eV by α/M in GeV-1.  Standardise units.  

M6  Equation labels occasionally repeat (two “Eq. 6” in text vs appendix).  Renumber consistently.  

M7  Paper claims that the paper is “methodology” yet large sections are review or speculation (Secs. III, XIII).  Shorten or move to discussion.  

M8  Length could be reduced to ≤17 pages by cutting the repeated discussion of SPHEREx and LiteBIRD forecasts which are not computed here.  

MINOR  
------  

m1  Abstract still contains the phrase “not a prediction of ECH itself” – redundant and confusing.  

m2  Several phrases duplicated, e.g. “canonical scalar matter” repeated three times in a single sentence in Sec. X.  

m3  footnote markers appear inside math mode (“ψ̄γ a γ 5 ψ)2 ”).  Typeset footnotes separately.  

m4  Table IV mixes significant figures (H0 quoted to 0.01 km/s/Mpc but γ given to three decimals).  Adopt uniform precision.  

m5  Many acronyms defined twice (LQC, ALP).  Audit.  

m6  arXiv identifiers missing square-bracket field in several references (e.g. [46]).  

NIT  
---  

n1  “non-Singular” capitalised mid-sentence.  

n2  Space missing before “degree” symbol in β values.  

n3  Occasional UK/US spelling mix (“parameterisation/parameterization”).  

================================================================  
## Summary recommendation  
MAJOR REVISIONS  

The submission raises potentially interesting questions about torsion cosmology, but key quantitative elements are either missing, internally inconsistent, or deferred to unpublished companion papers.  The most serious issue is the use of a dimension-1 parity-odd operator as if it generated a dimension-4 vacuum energy, on which many central numerical claims rest.  Until a self-contained derivation, full data release, and consistent statistical treatment are provided, the methodology cannot be considered sound.