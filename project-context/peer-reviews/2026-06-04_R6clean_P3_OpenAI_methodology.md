# P3 2026-06-04_R6clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 42.6s

---

# Referee report on P3   “Spectrally Unusual Sources at Scale …”

I have read the manuscript with the mandate of a methodology-referee for PRD, i.e. to audit the internal numerical and statistical consistency of every quoted scalar in the abstract and conclusions, to check the derivations that lead to them, and to flag any place where the statistical claims are not justified by the procedure that was actually carried out.  
Below I list all issues found, ordered by severity.

------------------------------------------------------------------
ESSENTIAL (must be fixed before the paper can be considered)

E-1  (Abstract, p.1)  Mixing of in-commensurable “σ” scales  
Quote: “The empirical α is statistically consistent with zero at 0.29σ … the 1σ envelope is σ(fNL) ∈ [3.92,8.98] … The local-linear σ(fNL)=8.27±2.37 … etc.”  
Problem: Three different uncertainty scales are shown side-by-side:  
(a) the jack-knife σ on α,  
(b) the Fisher curvature in the α2 model,  
(c) a linear propagation σ.  
The text inter-compares numbers that live in those different conventions without always reminding the reader which one is being used.  This violates instruction #7 (“Do not mingle σ values from different null procedures as if they were on the same scale”).  
Required fix: keep a single “information-preserving” mapping (your   1/σ2 = F0+cα2 ) everywhere; remove the linear 8.27±2.37 and every statement that mixes it with the quadratic envelope.

E-2  (§V, p.30)  No pre–registered primary estimator for α  
The catalogue was sifted, then after looking at the data the authors chose a particular angular range (θ∈[0.04°,0.25°]), three Landy-Szalay bins, 30 jack-knife regions, and then decided to adopt the jack-knife geomean instead of the bin-geomean.  Nothing in §II or in any preregistration states that this is the primary α estimator.  
Required: State unambiguously, *before* the measurement is shown, which statistic constitutes the primary estimator; document that choice in §II.  Otherwise α=0.19±0.65 is a post-selection result.

E-3  (Section II D & Table I)  Surveys that fail the Path-C 5σ gate are still kept in the headline  
LAMOST, Gaia and eROSITA do not reach the ≥50 % recovery at 5σ, but their anomalies are nevertheless included in the 378 280 catalogue that feeds the cosmology exercise.  The reader must be told how many of the objects used for the α measurement and for the novelty statistics come from a detector that demonstrably fails the sensitivity gate.  
Required: either (i) drop the gate-fail surveys from every science headline, or (ii) re-run their native detectors until they pass, or (iii) give a fully propagated systematic penalty showing how keeping them changes α and σ(fNL).  Simply flagging them as “FAIL-with-diagnostic” is insufficient.

E-4  (§III C, p.10)  SDSS native threshold is arbitrary and data-dependent  
The “top–77 905 at S≥0.1060” slice is chosen *because* it numerically matches the previous cross-transfer count.  That constitutes circular, post-hoc thresholding.  
Required: adopt a principled cut (e.g. top-1 % or S>5) and propagate *that* set everywhere, or prove that the cosmology results are insensitive (α and σ(fNL) variation < 10 %).  

E-5  (Section V A)  PTA likelihood uses per-bin KDE as if un-correlated  
The 30 free-spectrum points are correlated (published NG15 covariance).  The likelihood in Eq.(E2) multiplies per-bin KDEs, i.e. assumes independence.  The quoted σγ =0.382 and the Bayes factors therefore cannot be trusted.  
Required: redo the fit with the full bin-covariance or remove the PTA part from the paper.

------------------------------------------------------------------
MAJOR

M-1  (entire MS)  Length vs contribution  
The paper is 49 pages.  >15 pages are taken by colour plates of image galleries (App. D) that do not belong in PRD.  Recommend: cut the manuscript to ≤30 pages including appendices; move galleries and most code-style discussion to a data-release note.

M-2  (§IV A)  “17.8 % genuine novelty” is a single stratum yet is advertised in abstract  
The abstract repeatedly highlights 17.8 % as *the* novelty fraction although in §VI C the authors admit the full-catalogue rate is un-measured and could be lower *or higher*.  That is an over-claim.  
Fix: limit the claim to “at the top-1000 DESI score stratum”.

M-3  (§VI D (i))  Cross-validation on only the 47 k training spectra is not an OOD test  
The 5-fold Jaccard is carried out on the very same subsample that trained the autoencoder(s).  The “held-out” 100 k SPARCL test is aborted at 103 k/1M.  Therefore no quantified out-of-distribution performance is provided.  
Action: finish the 1 M random scoring (or a statistically defensible subsample) and quote the OOD anomaly rate.

M-4  (Table VI and Fig.12)  The Fisher engine used for the α–dependence does not include redshift uncertainties nor fibre weights, yet the impact of those is discussed qualitatively only.  Need a quantitative systematic table or clearly state the cosmology section is purely illustrative.

------------------------------------------------------------------
MINOR

m-1  p.2 paragraph beginning “The catalog stratifies…” repeats the same sentence almost verbatim three times – please compress.

m-2  Table I caption: the dagger (†) and § symbols are used twice with different meanings.  Use unique footnote markers.

m-3  Units: throughout the paper the authors use “score units” or “standardised units” without explicitly stating that σval is computed in *per-spectrum* MSE space.  Add a single equation showing the dimensional mapping.

m-4  Equation labels missing for several equations (e.g. the definition of the two quality criteria in §II D 1).

m-5  Typo p.15 “inflation-tensor case γ = 5 sits at zγ = +6.37σ and is excluded at Binfl/free = 1.86 × 10−24” – γinfl = 5?  Should be 5?3?  Clarify.

------------------------------------------------------------------
NITPICKS

n-1 Use consistent significant figures: e.g. σ(fNL)=8.14 yet α=0.19±0.65 – the precision implies σ(fNL) to 0.01 but α only to 0.1.

n-2 Spell out every acronym at first occurrence: XV, IF, OOD.

n-3 Figure 3 legend colour bar overlaps axis numbers in the pdf.

------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

The release of a very large cross-survey anomaly catalogue is valuable, but several methodological points are still unresolved: (i) surveys that fail the injection-recovery gate are nevertheless part of the headline, (ii) the primary α estimation is not pre-declared, (iii) the PTA likelihood is internally inconsistent, and (iv) the SDSS threshold is post-hoc.  These are fixable but require a non-trivial revision.