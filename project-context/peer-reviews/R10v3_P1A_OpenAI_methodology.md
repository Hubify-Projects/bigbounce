# P1A R10v3 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high
**Wall time**: 49.4s

---

Referee report for P1A (Round R10v3) ― Physical Review D  
All page numbers refer to the manuscript page footer.

--------------------------------------------------------------------
ESSENTIAL FINDINGS  (acceptance impossible without correction)
--------------------------------------------------------------------

P1A-E1 p. 1 (Abstract)  
Statement “we report 13 logically-independent mechanism-class constraints that collectively constrain the enumerated channels …”  
Problem One of the 14 numbered constraints (B8) is explicitly said to be the “observational consequence” of B14 and therefore not independent.  Claiming 13 independent constraints is internally contradictory.  
Required fix Either drop B8 or re-count B14 so that the number of independent constraints is correct and consistent in all places (abstract, Sec. IX and Table II).

P1A-E2 p. 1 (Abstract) & p. 18 (Data and Code Availability)  
Statement All numerical results (Cobaya chains, NaMaster pipeline, ALP MCMC, Fisher forecast) are “documented separately in companion work in preparation [6]”.  
Problem PRD requires that all analysis supporting headline numbers be available to referees.  None of the chains, likelihood files or scripts cited in Paper I(b)/Paper II were provided.  The public github repository advertised on p. 18 contains only a placeholder README.  
Required fix Upload every chain, likelihood, and analysis script used in the present paper to a permanent DOI-resolving repository and give a working link in the manuscript.  The material must be available during review, not “in preparation”.

P1A-E3 p. 6, Eq. (6)  
Statement Parity–odd operator written with overall coefficient α/M; off-shell mass dimension is +1.  
Problem A dimension-1 operator cannot be inserted in a 4-D action without additional powers of mass.  The mapping to a vacuum energy density in Eq. (B2) is therefore not an EFT derivation but a phenomenological guess; nevertheless it is used throughout the paper to set the amplitude budget and to obtain the “92 e-fold” requirement.  
Required fix (1) Either supply a self-consistent EFT operator of dimension 4 together with an explicit derivation of its coefficient, or (2) clearly remove any claim that Eq. (6) can yield a first-principles prediction for ρΛ.  If option (2) is taken, all subsequent numerical estimates that rely on Eq. (B2) must be re-evaluated or deleted.

P1A-E4 p. 7, Eq. (11)  
Statement Inflationary dilution factor Dinf = exp[−3 Ntot] ×(Treh/MGUT)3/2.  
Problem The exponent 3/2 is justified only by “phase-space aesthetics”; no derivation or citation is given.  Yet Dinf is used to translate the Planck-scale density to late-time ρΛ.  
Required fix Provide a derivation (e.g. from a Boltzmann calculation) or drop the (Treh/MGUT)3/2 factor and re-compute all numerical results that depend on it (notably Ntot).

P1A-E5 p. 10, Eq. (15)  
Statement Δθone-loop/Δθobs ratio evaluated as 10−58…10−60.  
Problem The equation misses a factor of 1/MPl in the numerator (dimension mismatch).  If restored, the quoted suppression becomes ≈1.2 × 10−60, not up to 10−58 as claimed.  
Required fix Insert the missing factor, recompute the range, and update every place (text, Table II, abstract) where the 10−58–10−60 figure is quoted.

P1A-E6 p. 11-12, Table II  
Problem Barrier 8 (“Parity-even interaction”) and Barrier 14 (“Perturbation transparency”) eliminate the same observable channel.  Listing both in the table as distinct barriers overstates the number of independent mechanisms blocked.  
Required fix Merge the two barriers or mark B8 as derivative (not independent).

P1A-E7 p. 15, §XIII  
Statement SPHEREx is forecast to detect fNL = −35/8 at “3–5 σ realistic”.  
Problem The Fisher numbers are taken from a companion study [2] that is “in preparation”.  No Fisher matrix, survey specifications, or systematic error model is provided here.  The uncertainty σ(fNL)=0.7 implies a 5.6 σ detection but the text quotes 3–5 σ without explaining the downgrading.  
Required fix Present the complete Fisher pipeline in an Appendix (k-range, bias priors, redshift bins, treatment of GR projection & photo-z errors) so that the quoted 3–5 σ range can be reproduced.

P1A-E8 p. 16, Table III  
Problem Table reports a PTA spectral index γ = 2.567 ± 0.382 obtained with a “real-KDE GPU MCMC” that is not described anywhere in the manuscript.  
Required fix Add a methods subsection that details the PTA data set, the likelihood construction, the KDE procedure, and chain diagnostics, or remove the number.

P1A-E9 Throughout (e.g. pp. 3, 5, 13)  
Problem Version-history and internal-review language (“this manuscript”, “earlier drafts”, “internal extrapolation”, “hUBIFY-2026-003”) appears repeatedly.  Such text is not permissible in a final PRD article.  
Required fix Strip all version-tracking, draft history, and companion-paper boiler-plate.

P1A-E10 Length  
The manuscript is 21 pages but ~30 % is meta-discussion and duplicate caveats, obscuring the actual derivations.  
Required fix Reduce to ≤14 typeset pages by removing repetition, internal notes, and forward references.

--------------------------------------------------------------------
MAJOR FINDINGS  (significant but not fatal if corrected)
--------------------------------------------------------------------

P1A-M1 p. 5, Eq. (2)  
The numerical spread “∼0.020” is called an “effective range” but later treated as an uncertainty.  Clarify that this is scheme dependence, not a statistical 1 σ error.

P1A-M2 p. 6, Step 3 (parity-odd effective action)  
Text says α/M is “motivated by” Shapiro & Teixeira [20] but reference [20] treats a different operator.  Provide the correct citation or an explicit derivation.

P1A-M3 p. 8, galaxy spin null  
The machine-learning classifier and its accuracy, purity, and systematics are deferred to Paper IV.  A one-paragraph summary is needed here; without it the reader cannot judge whether the “null” is statistically meaningful.

P1A-M4 Figs. 1 & 2  
Axes lack units; several arrows cross without labels; Fig. 2 needs a numeric scale.  Both figures must be redrawn for clarity or moved to Supplementary.

P1A-M5 References  
Several citations marked “(in preparation) (2026)” are nowhere accessible.  PRD requires that key supporting material be published or submitted.  Supply arXiv links or remove dependence on unpublished work.

--------------------------------------------------------------------
MINOR FINDINGS
--------------------------------------------------------------------

P1A-m1 p. 4, Table I caption “fNL = −35/8 (Paper II forecastb)” → move footnote ‘b’ into main caption to avoid confusion.

P1A-m2 p. 7, first paragraph: duplicate phrase “is aesthetic at this level rather than calculated” → remove duplication.

P1A-m3 p. 14, Eq. (23) missing factor of ½ in definition of Pontryagin density (check normalisation).

P1A-m4 p. 19, Appendix B first paragraph “do not arise from off-shell EFT counting but from on-shell scaling assumptions applied to a Planck-scale bounce geometry” – stylistically confusing; please re-phrase.

P1A-m5 Typos: “Domaga la–Lewandowski” → “Domagała–Lewandowski”; “Pop lawski” → “Popławski”.

--------------------------------------------------------------------
NITS
--------------------------------------------------------------------

P1A-n1 Repeated “tension resolution?” row in Table I ends with a dangling question mark; re-phrase.  
P1A-n2 Several occasions of “etc.” in technical sentences; replace by explicit items or delete.

--------------------------------------------------------------------
## Summary recommendation
MAJOR REVISIONS

The manuscript raises interesting questions about the viability of minimal Einstein–Cartan–Holst routes to dark energy, but the quantitative backbone of the argument cannot be verified because critical derivations, data products and numerical pipelines are either absent, deferred to unpublished “companion” papers, or based on ad-hoc dimensional guesses.  The paper also contains extensive draft-style text and exceeds a reasonable length for its current scientific content.  The above essential corrections―especially full public release of all numerical material and a self-consistent EFT construction for the parity-odd operator―must be addressed before the work can be considered for publication in PRD.