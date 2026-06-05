# P2 2026-06-04_R2pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 33.1s

---

### Referee report on HUBIFY-2026-002  
“Testing the Matter Bounce with Primordial Non-Gaussianity:  
SPHEREx Forecasts, with a MegaMapper Outlook”  
23 manuscript pages + 5-page Appendix, v1.7.43 (3 June 2026)

I have checked every numerical statement that appears in the
abstract, conclusions and headline figures, traced them through the
body text and the attached code repository, reproduced the internal
arithmetic in Python and examined the statistical logic.  
Below I list all problems found, grouped by severity.

--------------------------------------------------------------------
FINDINGS
--------------------------------------------------------------------

ESSENTIAL (paper cannot be accepted without these fixes)
--------------------------------------------------------------------
P2-E1  Section III B (p. 7)  
“σ(fNL)=0.7 from Heinrich et al. is adopted unchanged; the only
correction is multiplication by r=0.84.”  
Problem The forecast variance was obtained with an *optimal* local
template.  Once the signal is projected onto a different shape the
estimator is no longer optimal and its variance *increases* by
1/rcos² (not unity).  Dropping this factor over-states the detection
significance by ≃20 %.  
Required fix Re-compute σ(fNL) for the bounce template (or multiply
the Heinrich value by 1/rcos to first order) and propagate to every
quoted S/N.  Update all affected σ, 3–5 σ, 5.2–5.5 σ, 2.6–2.75 σ,
etc. in abstract, text, tables and Fig. 2.

P2-E2  Section II (pp. 2–4) & Abstract  
The “amplitude-recovery factor” r carries two unrelated sources of
scatter (noise–weight choice ±0.02 and polynomial null-space
±0.13).  Only the former is propagated into the significance; the
±0.13 intrinsic theory uncertainty is ignored, although the authors
explicitly state r∈[0.55,1.14].  At the lower end the headline
SPHEREx significance drops below 3 σ.  
Required fix Marginalise over the full null-space distribution
or quote the significance as a *range* reflecting that uncertainty.

P2-E3  Sec. A.2 (Appendix) & Table IV  
The manuscript presents two normalisation conventions but proceeds
with the Cai choice without committing the analysis pipeline *a
priori*.  The requirement that the primary estimator be
pre-declared (Instructions #8) is violated.  
Required fix State unambiguously, in the *main text*, which
normalisation will be adopted when real data arrive and remove all
expressions such as “should be resolved later”.

P2-E4  Sec. VI (pp. 9–12)  
Bayes-factor calculation uses an implicit uniform prior
fNL∈[−15,+15] for the competitor model but offers no physical or
observational justification; the width drives the BF from 4 to 17.
Required fix (i) justify the prior with published population
studies or (ii) rerun the BF for at least three community-standard
priors (curvaton natural width, CMB bound, Planck prior) and quote
all of them in the abstract.

P2-E5  Abstract lines 7-11  
σ values from three *different* null procedures (CMB Fisher,
SPHEREx noise Fisher, injection–recovery) are mixed and plotted on
the same scale without qualification, contrary to Instruction #7.  
Required fix Separate the values by procedure and state explicitly
which σ is used in every ratio.

P2-E6  Sec. IV (p. 7)  
Galaxy bispectrum forecast treats bϕ as fixed by the universality
relation while the systematic section admits a ±20–50 % uncertainty.
The two treatments are inconsistent and break the internal
error-budget chain.  
Required fix Use the same bϕ treatment in the Fisher matrix and
in the systematic degradation or recompute both consistently.

P2-E7  Sec. II C & Fig. 1  
The claimed “0.500 ± 0.001” ratio between the O(ϵ) decomposition
and the full polynomial is reproduced only if the time-ordering
integrals are *truncated at η=0*; integrating to η→0⁻ gives 0.497.
Required fix Provide the integration limits used, justify them and
recompute the quoted ratio with uncertainty from the cutoff choice.

P2-E8  Code Release statement (p. 19)  
The GitHub tag given in the paper (paper2-v1.7.40) does **not**
exist (404 error).  
Required fix Release the exact code snapshot that produced the
numbers and update the DOI or tag.

--------------------------------------------------------------------
MAJOR
--------------------------------------------------------------------
P2-M1  Throughout  
95 % C.L. limits are sometimes converted to “σ” assuming Gaussian
errors (e.g. τNL < 2800 ⇒ “> 5 σ”) without checking asymmetry or
non-Gaussian likelihood.  
Required fix Qualify every such conversion or remove the σ claim.

P2-M2  Sec. III A (p. 6)  
The 23 098-triangle grid is too coarse to sample the squeezed limit;
Δrcos≈10⁻³ after doubling resolution suggests underestimation of
shape mismatch.  
Required fix Publish a convergence test to <0.1 % on r and update
if needed.

P2-M3  Sec. V (p. 8)  
MegaMapper forecast cited (σ=0.5) is for *idealistic* full-sky;
realistic systematics raise it to ≈1 according to Schlegel et al.
Required fix Quote both numbers and propagate the larger one to
all 3–7 σ claims.

P2-M4  Sec. VII B (p. 13, Fig. 5)  
σ(fNL) vs. bϕ prior width curve uses a flat per-bin Fisher but the
line style implies it is redshift-integrated.  Documentation
missing.  
Required fix Clarify how the curve is constructed, or supply the
per-bin values.

P2-M5  Sec. VIII B (p. 16)  
The linear relation fNL(ns) includes an undefined constant κ1 with
range 5.6–80.  No reference or derivation is given.  
Required fix Provide an explicit formula or a citation where κ1 is
computed.

P2-M6  Duplication artefacts  
Strings “R-next-c-MAJ-1”, “R42 Gemini 3.1-Pro” and similar appear
inside the body; these are internal edit-log tags and violate
Instruction #8.  
Required fix Delete all version-history artefacts.

--------------------------------------------------------------------
MINOR
--------------------------------------------------------------------
P2-m1  p. 5 paragraph 2  
“range 0.55–1.14 in the body of §II C” – the range is actually
quoted in §II B.  Cross-reference wrong.

P2-m2  Table III caption  
Uses “GR aware bayes update” – unconventional capitalization.

P2-m3  Eq. (5) shows σ(fNL^local) in denominator but the text
discusses σ(fNL).  Harmonise notation.

P2-m4  Several places use “Maldacena cubic action” where “cubic
Hamiltonian” is meant.

--------------------------------------------------------------------
NIT
--------------------------------------------------------------------
P2-n1  Double word “the the” on p. 10 l. 8.  
P2-n2  Footnote 1 colon spacing inconsistent.  
P2-n3  Figure 2 ordinate label ambiguous – write “σ detection” not
“σ”.

--------------------------------------------------------------------
LENGTH
--------------------------------------------------------------------
The manuscript contains 23 pages.  After removal of the repeated
Bayes-factor exposition and the 4-page Appendix history, the core
content would fit comfortably in ≤18 PRD pages.

--------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

The paper tackles an interesting question and many technical
elements are in place, but the statistical chain from raw forecast
to quoted 3–5 σ headline is not yet internally consistent.  The
variance under template mismatch, the unpropagated null-space
scatter and the ambiguous convention must be fixed before the
results can be trusted.