# P2 2026-06-04_R3clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 29.4s

---

Referee report on P2 — “Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook”  
Round: 2026-06-04_R3clean

I have audited the statistical methodology, internal arithmetic, derivation chain and systematic-error propagation through the full text supplied.  My findings follow, grouped by severity.

────────────────────────────────────────
ESSENTIAL (paper cannot be accepted without these fixes)
────────────────────────────────────────

ID P2-E1  (Abstract p. 1)  
Problem  The headline Bayes-factor envelope “BF ≈ 10–17” is obtained by combining:  
(a) a delta-function prior for the bounce model (maximises BF) and  
(b) a broad [−15,+15] flat prior for the “multifield competitor”.  
Any finite theoretical uncertainty around fNL = −35/8 collapses that upper figure.  Yet the 3 × 10^5 Monte-Carlo ensembles that are claimed to “validate” the BF all keep the prior fixed.  
Required fix  (1) State one and only one pair of priors as the fiducial choice; (2) recompute BF with that pair after marginalising over the quoted 1–8 % ε correction, the c1–c6 null-space scatter and the convention ambiguity (Li-Brandenberger).  Report that single, prior-consistent BF; withdraw the 17 upper bound unless it survives.

ID P2-E2  (§III B, §IV)  
Problem  The ±0.13 absolute scatter in the template-overlap factor r from the 10 000 coefficient realisations is not propagated into the 5.2–5.5 σ “optimistic” detection claim.  The text instead adopts r = 0.84 ± 0.02 (noise weighting only), ignoring the much larger shape-function uncertainty.  
Required fix  Propagate the full coefficient-space variance into σ(fNL) and hence into the quoted detection significances.

ID P2-E3  (Abstract p. 1, line 26)  
Problem  The ratio |f bounceNL|/|f infNL| is stated to be ≈ 290.  4.375/0.015 = 291.67.  
Required fix  Correct the numeric or justify the rounded value explicitly.

ID P2-E4  (§VII B, Fig. 5)  
Problem  σ(fNL) values from three incommensurable estimators (CMB Fisher, SPHEREx bispectrum, LSS SDB) are compared on the same plot and in the same sentences as if they were directly comparable.  
Required fix  Separate the σ curves by estimator, or rescale them to a common effective volume before plotting.  State explicitly which σ is used in every significance conversion.

ID P2-E5  (Throughout; e.g. §VI “R42 Gemini 3.1-Pro P2 BLOCKER B-3”; Abstract ¶5)  
Problem  Multiple internal review-log artefacts and version-history comments remain.  
Required fix  Delete every trace of internal audit strings, “previous draft” comments, TODO notes, and similar review residue.

ID P2-E6  (Data-availability statement)  
Problem  The reproducibility path “https://github.com/Hubify-Projects/bigbounce/tree/paper2-v1.7.40/…” is not public.  
Required fix  Provide a DOI-tagged, public archival copy of the exact code and input data used to generate every figure and number, or deposit them as ancillary files.

ID P2-E7  (§III A)  
Problem  Primary estimator is not defined prior to result quoting.  Only later do we learn that a KSW-type estimator was used for the injection test, whereas the forecast relies on Heinrich et al.’s Fisher matrix.  
Required fix  Declare, in a dedicated “Methods” subsection before any results, exactly which estimator(s) are used for each claim and whether they were fixed before looking at synthetic data.

ID P2-E8  (Abstract p. 1, last ¶)  
Problem  Convention-halving discussion mixes σ(fNL) from the Cai normalisation with that from the Li-Brandenberger normalisation but keeps the same error bar, giving a halved significance that is arithmetically inconsistent.  
Required fix  Recompute σ(fNL) under the c = 1 convention (the fiducial P(k) normalisation doubles) or remove the “halved” claim.

ID P2-E9  (§VIII B, eq. 9)  
Problem  κ1 range 5.6–80 is inserted into eq. (9) but no propagation to Fig. 6 or to the 1–8 % statement is shown.  
Required fix  Demonstrate with explicit error propagation that eq. (9) indeed limits fNL to the [−4.35,−4.02] band quoted.

────────────────────────────────────────
MAJOR (significant revision required)
────────────────────────────────────────

P2-M1  (Abstract; §III B)  
r = 0.84 ± 0.02 is obtained under a single noise model.  Survey systematics (masking, 1/f systematics, calibration ripples) alter the triangle-weight distribution and hence r.  Provide a survey-realistic Monte-Carlo (with at least a Planck-2020 Galactic mask) or widen the uncertainty accordingly.

P2-M2  (§VII C, Table III)  
GR marginalisation is treated as a Gaussian shift σGR added in quadrature.  Jolicoeur et al. show that the correction is scale- and tracer-dependent and non-Gaussian.  Re-run the Fisher with the full relativistic kernels, or clearly flag σGR as notional.

P2-M3  (§IV)  
The Heinrich et al. σ(fNL) = 0.7 forecast assumes bϕ fixed by universality.  You quote 3–5 σ inclusive of a 20–50 % “possible” bϕ inflation, but never supply an updated Fisher number.  Provide a two-parameter (fNL,bϕ) Fisher or tone down the claim.

P2-M4  (§V)  
MegaMapper significance “3–7 σ” is speculative (concept not yet approved).  Either supply a complete input table (n(z), b(z), kmin (z), σz , ƒsky ) in the paper or label every MegaMapper number “illustrative only”.

P2-M5  (Appendix A)  
The operator-algebra derivation is valuable but you still rely on Cai’s numerical integration for the final amplitude.  Supply an independent numeric evaluation for at least one non-benchmark triangle or qualify the statement “confirms”.

P2-M6  (whole text, many places)  
Duplicate phrases and word echoes (“signal-only signal-only”, “template mismatch mismatch”, “arithmetic arithmetic”) remain.  Please run a pass for redundant duplication.

────────────────────────────────────────
MINOR (should be addressed but editor may allow)
────────────────────────────────────────

P2-m1  (Abstract)  “A SPHEREx null would disfavor … at > 4σ”.  This depends on adopting r=0.84 and σ=0.7, both optimistic.  Rephrase to “could disfavor”.

P2-m2  (§II C)  “exact within the scalar-only Einstein-Cartan-Holst class” — clarify what happens when fermions are included.

P2-m3  (§III A)  Equation (4) missing explicit units (Mpc/h).  Add.

P2-m4  (Table I)  Supply the numeric values to 3 sig.fig. not just rational fractions.

P2-m5  Footnote “a rhetorical > 6×10^5 figure …” is inappropriate in published text.  Delete or move to code appendix.

────────────────────────────────────────
NIT (fix if time permits)
────────────────────────────────────────

P2-n1  Several sentences run > 80 words.  Shorten.

P2-n2  Missing comma before “respectively” in many lists.

P2-n3  Typo “prefactors weighthing”.

P2-n4  Planet symbol “◦” sometimes rendered as superscript 0, sometimes unicode  °; unify.

────────────────────────────────────────
Length
────────────────────────────────────────
22 typeset pages is acceptable for a methods/catalogue article, but the Bayes-factor material could be tightened; 18–19 pages should suffice.

────────────────────────────────────────
Summary recommendation
MAJOR REVISIONS

The manuscript presents an ambitious and timely forecast but currently mixes incommensurable σ values, over-states Bayes-factor evidence, and leaves key internal uncertainties un-propagated.  Once the essential arithmetic and prior-dependence corrections are made, and the internal audit debris is removed, the paper should be publishable.