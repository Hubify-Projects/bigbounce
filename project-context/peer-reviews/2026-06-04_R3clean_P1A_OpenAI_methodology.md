# P1A 2026-06-04_R3clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 32.8s

---

Referee report on P1A – “Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter”  
Round: 2026-06-04_R3clean  

I have audited the manuscript with the remit of methodology rigor, statistical validity, dimensional and arithmetic consistency, and traceability of every scalar appearing in the abstract and conclusions.  Findings are listed below using the requested taxonomy.

------------------------------------------------------------------
ESSENTIAL
------------------------------------------------------------------

P1A-E1  (Abstract p.1 & Appendix B)  
Problem:  The mapping ρΛ ≃ [(α/M) MPl]MPl4 (text alternates between “power-4” and “power-5”) is dimensionally inconsistent.  Eq.(6) carries mass dimension +1, yet throughout the paper it is used as if it were a +4 operator, later “patched” by multiplying by ad-hoc factors MPl3 (Appendix B).  No unique prescription is followed, and both 10−2 MPl4 and 10−4 MPl4 appear.  
Required fix:  Provide a single, self-consistent operator-level derivation that yields a bona-fide dimension-four term OR delete every quantitative claim that depends on Eq.(6) (this includes Ntot=92, Ξ, Barrier-4 estimates, Table I first row, and Fig. 2).

P1A-E2  (Sec. IV pp.8-11)  
Problem:  Route-2 “one-loop” amplitude estimate divides β (deg) by βobs uncertainty (deg) but inserts H0 in eV without restoring MPl, mixing units in Eq.(15).  The claimed suppression “10−58 to 10−60” is therefore arbitrary.  
Required fix:  Re-derive Δθone-loop /Δθobs in a fully dimensionless form with all factors shown.  Provide a numerical spreadsheet in the supplementary repository so the referee can reproduce the figure.

P1A-E3  (Abstract, Sec. III A, Sec. XII A)  
Problem:  σ values from different null models are blended: present-day LiteBIRD forecast σ(β)=0.03° is compared to the current Planck-WMAP uncertainty 0.094° to claim a “9σ” detection.  The 9σ figure is meaningless because the forecast is against β=0 while the reference 0.094° is the posterior uncertainty conditional on a non-zero central value.  
Required fix:  Quote all significances with respect to the same null (β=0).  Re-compute the expected LiteBIRD signal-to-noise with (β=0.27°, σ=0.03°) → 9.0σ and remove the misleading comparison against 0.094°.

P1A-E4  (Galaxy-spin Sec. V p.11)  
Problem:  The primary estimator (ViT-Small chirality classifier) is not pre-declared and no ROC / accuracy table is provided.  The work relies on an unpublished “Paper IV” for all methodology.  
Required fix:  Summarise in this manuscript the architecture, training data, augmentation pipeline, achieved validation accuracy, and an ablation showing that the null is not an artefact.  The companion paper cannot be used as the only record.

P1A-E5  (All sections)  
Problem:  Numerous core numerical results (Cobaya MCMC posteriors, SPHEREx Fisher, PTA KDE) exist only in non-public “companion” papers.  The current submission is therefore not reproducible.  
Required fix:  Either include condensed but complete methods and results here or supply a permanently archived, DOI-tagged version of the cited companion papers.

P1A-E6  (Sec. X pp.14-15)  
Problem:  “Perturbation-transparency theorem” is asserted without giving the tensor algebra.  Vanishing of torsion is stated but no explicit variation of the full Holst+matter action is shown.  
Required fix:  Provide the Euler–Lagrange variation in an appendix, including the step where T λµν = 0 follows from S λµν =0 for a canonical scalar.  Give at least the quadratic action to confirm the claim.

P1A-E7  (Throughout; version artefacts)  
Problem:  The manuscript still contains internal review tags (“Barrier 8 subsumed by Barrier 14”, “hUBIFY-2026-001B”, “Round R3clean”, “CHANGELOG.md”).  
Required fix:  Remove all development and version-history language.

P1A-E8  (Abstract & Sec. XII A)  
Problem:  Arithmetic error in the Ntot count.  True hierarchy (MPl4 /ρΛ) ≈1.2×10122 implies Ntot≈94, not 92.  The text later says 92±2; origin of ±2 is nowhere derived.  
Required fix:  Once E1 is fixed, recompute Ntot with correct significant figures and propagate through the entire manuscript.

------------------------------------------------------------------
MAJOR
------------------------------------------------------------------

P1A-M1  (Sec. IV B)  
Route-2 parity-odd coefficient “αem /4π MPl−1” is introduced with no reference to an actual loop calculation (Mercuri & Capozziello derive a different structure).  Provide a bibliographically traceable derivation or qualify the equation as an ad-hoc upper bound.

P1A-M2  (Sec. IV D)  
Spectator-ALP fine-tuning argument mixes two free parameters (α/M and mθ) but later treats α/M as fixed by βobs.  Need a quantitative naturalness metric (e.g. Barbieri-Giudice) to justify “severe tuning”.

P1A-M3  (Table I, Table IV)  
H0 =67.68 ± 1.06 km s−1 Mpc−1 is quoted as “recovered” but no likelihood combination is specified.  Provide the dataset list and a covariance matrix.

P1A-M4  (Data availability statement)  
The GitHub link is not version-pinned and no release tag exists.  Without an archived zenodo release the code can change after publication.

P1A-M5  (Sec. IX barriers)  
Barriers 5,6,7,9 are philosophical rather than quantitative, yet they are used in the logical count “13 independent barriers”.  Either supply quantitative inequalities or move them to a discussion-only appendix and state that only nine are strictly quantitative.

------------------------------------------------------------------
MINOR
------------------------------------------------------------------

P1A-m1  (Abstract line 4)  “Jackiw-Pi gravitational Chern-Simons R ∧ R̃” → the correct attribution is Jackiw–Pi, 2003 PRD 68 104012.  Add citation.

P1A-m2  (Sec. I A p.3)  “3. Black hole universe origin…” citation [14] is Popławski 2016; list full reference once.

P1A-m3  Table II header says “14 barriers” but caption says “13 logically-independent”.  Clarify.

P1A-m4  Duplicate phrase “canonical canonical-mask” appears p.14 col.2.

P1A-m5  β is reported sometimes in degrees, sometimes radians with no conversion; adopt one convention.

------------------------------------------------------------------
NIT
------------------------------------------------------------------

P1A-n1  Eq.(11): missing factor of 2π in the GUT-scale relation.

P1A-n2  Footnote on p.17 has unmatched parenthesis.

P1A-n3  Typos: “Liouville” spelled “Liouvillee” once; “non-singular” missing hyphen twice.

------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

The idea of auditing all minimal ECH routes is interesting, but the quantitative backbone is presently unstable: the key operator is of the wrong mass dimension, several numerical estimates mix units, and essential derivations are deferred to unpublished companion material.  The paper cannot be accepted until the dimensional analysis, reproducibility, and missing proofs are corrected.