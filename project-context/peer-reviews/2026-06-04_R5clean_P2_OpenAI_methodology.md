# P2 2026-06-04_R5clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 28.8s

---

Referee report – methodology/statistics audit for P2  
Testing the Matter Bounce with Primordial Non-Gaussianity  
Round: 2026-06-04_R5clean  
---------------------------------------------------------------------------  

FINDINGS  

ESSENTIAL (paper cannot be accepted without these corrections)  
--------------------------------------------------------------------------------------------------  
P2-E1  (Title page, line 4)  
Problem: The string “ROUND: 2026-06-04_R5clean  CHANGES SINCE LAST ROUND: R5: post-arXiv TODO table caption note abstract self-ref deferred-companion all fixed” appears in the manuscript body. This is internal version-history language forbidden by instruction 8.  
Fix: Remove every trace of version-log, TODO, change-log and similar housekeeping language from the final submission.

P2-E2  (Abstract, 1st paragraph)  
Problem: The quoted primary detection significance “5.2–5.5 σ” is obtained by applying the Heinrich-et-al. σ(fNL)=0.7 (computed for a *local*-template fiducial fNL = 0) to the *bounce* fiducial –4.375 without re-evaluating the Fisher matrix at that fiducial.  The linear-response assumption that Fisher(0)=Fisher(–4.38) is not demonstrated.  Because the entire headline significance rests on this, the numerical claim is unsubstantiated.  
Fix: Re-compute the full multi-tracer bispectrum Fisher matrix with the bounce template as fiducial, or furnish an explicit perturbative argument showing ΔF/F ≪ 1 when shifting the fiducial from 0 to –4.375 under the survey specifications.  Update every σ and σ-derived significance in abstract, conclusions, Table IV and Fig. 2 once the correct Fisher numbers are available.

P2-E3  (Sec. III B, Eq. 6 and surrounding text)  
Problem: The template-overlap factor r was evaluated with several *noise* weightings, none of which matches the weight used in the published Heinrich forecast, yet the average r = 0.84 is multiplied directly into that forecast.  This is mixing σ values from incommensurate weighting procedures (instruction 7).  
Fix: Use exactly the same ℓ/k weighting used by Heinrich et al. or recompute σ(fNL) with the weighting that produced r.  Otherwise state and propagate an additional conversion uncertainty term.

P2-E4  (Sec. II C, last paragraph)  
Problem: The “factor-of-two convention ambiguity” is said to halve the signal.  No final decision is made—two numerically incompatible values are carried forward to the conclusions.  A paper cannot be accepted while the normalization of the quantity being forecast is undecided.  
Fix: Commit to one convention, give a single fiducial (with an uncertainty band if justified) and remove the duplicate parallel results.  If the alternative convention is kept for context, confine it to an appendix and clearly label it “not used in forecasts”.

P2-E5  (Sec. A.1, derivation)  
Problem: All analytic manipulations end at Eq. (A7) *before* the time-integrals are evaluated.  Yet the paper later relies on numerical values obtained from a private code base.  The repo link given in “DATA AND CODE AVAILABILITY” does not resolve to a DOI-frozen archive, nor is any hash supplied.  
Fix: Deposit the full integration code and all Fisher notebooks in a permanent repository (Zenodo or equivalent) and cite the DOI in the manuscript.  The editor must be able to run “make test” and reproduce Table I and the overlap r to 1-digit accuracy.

MAJOR (significant revision required)  
--------------------------------------------------------------------------------------------------  
P2-M1  (Whole paper)  
Problem: The abstract is 480 words—more than double PRD guidance.  It contains survey history, mission schedules, referee rebuttal language and prior-round commentary.  
Fix: Reduce to ≤250 words containing only purpose, method, main numerical result, and its uncertainty.

P2-M2  (Sec. III A, first paragraph)  
Problem: The scale-dependent-bias kernel Eq. (4) is missing an overall factor T(k) in some later discussions (Fig. 4 caption uses “kmin” scaling as if T→1).  Dimensional consistence is lost.  
Fix: Verify all subsequent SDB significance numbers with the correct transfer function and update text and figures.

P2-M3  (Sec. VI, Bayes-factor discussion)  
Problem: Prior choices are partly data-dependent (σ drawn from [0.5,1.5] using the *forecast* uncertainty distribution).  This is “double-counting” experiment sensitivity inside the prior and inflates Bayes factors.  
Fix: Remove survey-performance parameters from the *model* prior.  Compute Bayes factors with priors independent of the data likelihood, then state a separate robustness test with hyper-priors if desired.

P2-M4  (Sec. VII B, PNG-bias uncertainty)  
Problem: The statement that a “20 % Gaussian prior on bφ is realistic” is unsupported.  Current literature finds order-unity uncertainty for most tracers.  
Fix: Quote and justify a concrete reference for the 20 % number, or propagate a wider prior (≥50 %) and show how the headline significance changes.

P2-M5  (Sec. IV, last paragraph)  
Problem: Shot-noise degradation for anomaly-selected tracers is asserted to be ≲15 % “simple Poisson estimate”, but no numbers are shown.  
Fix: Provide a table with n̄, b1, σshot and resulting σ(fNL) for the anomaly sample or remove the claim.

P2-M6  (Sec. VIII)  
Problem: The fNL–ns consistency relation Eq. (9) uses κ1 range 5.6–80 (an order of magnitude) yet later figures plot only the central curve.  
Fix: Show the full band in every figure that uses Eq. (9) and propagate the width into any derived rejection significance.

P2-M7  (Entire manuscript)  
Problem: Numerical values in abstract and conclusions (e.g. “84 % ± 2 %”, “±0.13 absolute”) are not traceable to a table or figure inside the main text as required.  
Fix: Add a summary table containing every scalar that appears in the abstract, with exact source section / computation script reference.

MINOR (should be addressed – editor may waive)  
--------------------------------------------------------------------------------------------------  
P2-m1  (p. 2, col. 1)  
Quote: “scalar-only matter-bounce class — Assumptions (e) and (f) in Sec. II C exclude prolonged post-bounce inflation and significant fermion-sourced torsion during contraction respectively”.  
Problem: The dash is doubled and “respectively” is unnecessary.  
Fix grammatical.

P2-m2  (p. 9, footnote 2)  
Footnote numbering restarts inside a section – numbering is inconsistent.  
Fix: Use continuous footnote numbering.

P2-m3  (multiple places)  
The tilde “∼” is used directly before numerals without a thin space (e.g. “∼25 months”).  
Fix: Insert thin space or write “approximately”.

P2-m4  (Eq. 5)  
The notation σ(fNL bounce) mixes subscript and superscript styles.  
Fix: adopt a single notation, e.g. σbounce(fNL).

P2-m5  (References)  
Several arXiv citations are missing journal info even though they are now published (e.g. Ref. [4]).  
Fix bibliography.

NIT (very minor)  
--------------------------------------------------------------------------------------------------  
P2-n1  Duplicate phrase “Planck PR4/NPIPE (CMB bispectrum)” occurs twice in the same sentence (Sec. VIII A).  
P2-n2  Occasional British/American spelling mix (“marginalisation” / “marginalization”).  
P2-n3  Extra spaces around ± symbols in Table I.

--------------------------------------------------------------------------------------------------  

## Summary recommendation  
MAJOR REVISIONS  

The manuscript contains an interesting and technically sophisticated attempt to forecast a bounce-cosmology signature, but several methodological foundations are still missing: (i) no Fisher matrix evaluated at the correct fiducial, (ii) σ values derived under mismatched weightings, (iii) unresolved normalization ambiguity carried into the headline significance, and (iv) internal version artefacts left in the text.  These issues must be fixed and the numerical results regenerated before the paper can be considered for publication.