# P2 2026-06-04_1814pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 29.1s

---

Referee report on  
P2 – “Testing the Matter Bounce with Primordial Non-Gaussianity: Forecasts for SPHEREx and MegaMapper”

--------------------------------------------------------------------
I list every issue I found, together with a severity tag
(ESSENTIAL / MAJOR / MINOR / NIT), an identifier, location, the
problem, and the required fix. Page numbers refer to the PDF
viewer count supplied by the arXiv automatic conversion (title page
is p. 1).

ESSENTIAL items must be resolved before the paper can be considered
for publication.

--------------------------------------------------------------------
ESSENTIAL FINDINGS
--------------------------------------------------------------------
P2-E1 (all sections; dozens of occurrences)  
Missing citations: “[?]”, “[??]”, “Sec. ??”, “Eqs. 34+35+36”, etc.  
Required fix: Replace every placeholder with an actual reference
and ensure that the bibliography contains the cited work.  No
methodology audit can be completed while the literature chain is
invisible.

P2-E2 Abstract, p. 1 and passim  
Mixing σ values from incommensurable estimators.  The abstract
juxtaposes
    “σ(fNL) ≈ 0.7 (Heinrich et al. 2023, galaxy bispectrum)
     …MegaMapper … σ(fNL) ≈ 0.5”
but later sections sometimes add the scale-dependent-bias (SDB)
forecast, sometimes not.  Several plots (Fig. 2, Fig. 4) fold the
two pipelines together as if the quoted σ were on the same scale.
Required fix: State explicitly, at the first appearance, which σ
belongs to which estimator, and never add or average them unless a
full joint Fisher matrix (with their covariance) is provided.
Otherwise the reader is left with apples-to-oranges σ values.

P2-E3 Sec. 6, p. 7 & Abstract  
Internal inconsistency in the quoted Bayes factors.  
Abstract: “over standard single-field inflation at Bayes factor ≳ 1”  
Sec. 6/Table 2: “>10^5”.  
Table 3: 3.3 × 10^6.  
Required fix: Re-compute once, with a single prior choice, and use
the same number everywhere.  If different priors are shown, label
them unambiguously and do not mix them in the prose.

P2-E4 Sec. 3.2, p. 4  
Recovery factor r quoted as “0.85–0.90” but later values of
detection significance use r = 0.876, r = 0.85, and r = 0.90 at
different points without justification.  
Required fix: Provide one survey-specific r per estimator, tabulate
it once, propagate consistently, and quote its numerical precision
with an error bar derived from the MC variance.

P2-E5 Sec. 6.3, eq. (6) & Monte-Carlo description, p. 6–7  
The Bayes factor is evaluated with a δ-function prior for the
bounce model and a uniform prior for competitors, then the MC
draws σ from a uniform [0.5,1.5].  This procedure mixes an
epistemic prior with an aleatoric error distribution, which is not
a legitimate likelihood comparison.  
Required fix: Either (a) fix σ to the survey forecast and do the
integral analytically, or (b) treat σ as a hyper-parameter and
marginalize it in both models.  Explain the prior choices.

P2-E6 Abstract & Sec. 10, p. 11  
Claim: “A null result from SPHEREx would disfavor the
quasi-dust matter bounce benchmark … at > 4σ significance.”  
This ignores the 15 % template-recovery loss r.  With σ = 0.7 the
rejection significance is (4.375 × 0.85)/0.7 = 5.3σ, not “> 4σ”.
Required fix: Re-state the number after applying r and include the
template mismatch in the null-rejection calculation everywhere.

P2-E7 Sec. A (appendix), p. 12  
Equation (9) defines the bispectrum with an unexplained constant
“c”.  The text claims c = 2 for Planck/Komatsu and c = 1 for the
alternative, but in eq. (9) the factor in front of fNL has already
been written as “c·fNL”.  This double use of c causes a factor-of-2
ambiguity in every subsequent amplitude and in Table 1.  
Required fix: Adopt one convention, state it once, and edit every
number (including Table 1) to that convention.  Provide an explicit
cross-walk equation.

P2-E8 All pages  
Unicode control character “” appears dozens of times
(“-correction”).  This is almost certainly a broken TeX macro.
Required fix: Remove the artefact and replace with readable text.

P2-E9 Throughout, especially Sec. 2.3 & 2.4  
A “92 % confidence” is quoted for the normalization – but no
statistical procedure is given.  If this is subjective it must be
labeled as such; otherwise derive it formally.  
Required fix: Either remove the percentage or supply the Bayesian
computation leading to 92 %.

P2-E10 Multiple places (e.g. Sec. 7.4)  
Forecasts use 20 % Gaussian prior on bφ and then conclude that the
bispectrum forecast is “nearly independent of bφ”.  With a 20 %
width that is not true for SDB but still partially true for the
bispectrum.  The quantitative 5 % degradation claimed in 7.4 is not
shown.  
Required fix: Supply the algebra or a plot of σ(fNL) vs. σ(bφ) for
the bispectrum channel, similar to Fig. 5 left panel for SDB.

--------------------------------------------------------------------
MAJOR FINDINGS
--------------------------------------------------------------------
P2-M1 Sec. 3.2, p. 4  
Injection/recovery uses 200 realizations yet quotes r = 0.90 ± 0.01.
Given the ∼10 % intrinsic scatter in most bispectrum estimators,
200 mocks cannot support a 1 % error bar.  
Fix: Increase the mock set (≥ 5000) or quote a statistically
correct uncertainty.

P2-M2 Sec. 4 & Fig. 2  
The figure shows combined bispectrum + SDB error bars for
SPHEREx/MegaMapper without giving the cross covariance.  The
forecast from Heinrich et al. 2023 assumes no covariance.  
Fix: Provide the covariance matrix or remove the combined points.

P2-M3 Sec. 2.1, polynomial derivation  
The six polynomial coefficients are given but no derivation is
shown and the reader is asked to trust “exact rational arithmetic”.
Provide at least one explicit intermediate step or attach a
computer-algebra notebook.

P2-M4 Sec. 7.3, Table 3  
GR systematic σGR is inserted as a nuisance parameter but no prior
shape is given except “uniform in [0,1]” in Sec. 6.3.  Different
priors change BF by orders of magnitude.  
Fix: Justify the prior on σGR or show BF as a function of that
prior width.

P2-M5 Sec. 8.1, p. 9  
Planck + DESI recast gives “fNLbounce = −1.3 ± 4.5”.  The algebra of
eq. (4) demands multiplication by r; if r = 0.88 the DESI number
changes.  
Fix: Show the full propagation formula and verify arithmetic.

P2-M6 Paper length  
The manuscript is 12 pp but spends ∼5 pp on a qualitative
inflation-vs-bounce discussion not needed for the forecasting
method.  Recommend ≤ 10 pp after removing narrative material.

--------------------------------------------------------------------
MINOR FINDINGS
--------------------------------------------------------------------
P2-m1 Abstract line 7  
“validated by `-space Fisher overlap” – include the range of ` used.
P2-m2 Sec. 5, p. 5  
“ideal conditions (3–7σ realistic)” – “ideal” and “realistic” are
used interchangeably; rephrase.
P2-m3 Sec. 2.3 last paragraph  
Confuses the symbol ϵ (slow-roll) and  (here contraction
parameter).  Harmonise notation.
P2-m4 Sec. 9.2 list  
CMB-S4 σ(fNL)=2.5 assumes internal‐linear combination noise,
cite the source.
P2-m5 Acknowledgments  
Mentioning the use of “Claude (Anthropic)” is unusual for PRD; move
to a footnote or delete.

--------------------------------------------------------------------
NITPICKS
--------------------------------------------------------------------
P2-n1 Title page: email address and personal URL are not required
by PRD style – optional.  
P2-n2 Duplicate word “phase phase” appears once in Sec. 1.
P2-n3 Fig. 1 y-axis label “|B|NL” – PRD prefers Bζ /[PζPζ] units.
P2-n4 Fig. 6 legend colour keys not colour-blind safe.
P2-n5 Typo: “quasi-dust contraction [?]) would push” – stray “?)”.

--------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

The paper contains an interesting forecast but the statistical and
methodological presentation is not yet audit-ready: missing
citations, inconsistent Bayes factors, mixing of σ values from
different estimators, and an undefined prior structure all prevent
a clean assessment.  These can be repaired without new data but do
require a thorough rewrite and re-calculation.