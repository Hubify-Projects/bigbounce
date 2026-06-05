# P4 2026-06-04_R3clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 37.9s

---

Referee report on P4 ‑ “Survey-Scale Galaxy Chirality with Equivariant TTA …”

----------------------------------------------------------------
GENERAL ASSESSMENT
----------------------------------------------------------------
The manuscript presents a 56-page methodology study that re-analyses 8.47 million DESI-Legacy galaxies with a ViT-Small classifier plus a two-fold flip test-time-augmentation (“Z₂-TTA”).  A catalogue of 3.20 million spirals is released and several dipole estimators are quoted.  The principal conclusion is that the parity–even ℓ = 1 chirality dipole is consistent with zero at −0.12 σ (MASTER, “sub-sample mask”) / +0.43 σ (real space), whereas a +3.64 σ signal on a patchier “canonical mask” is ascribed to a monopole × mask leakage channel.

The work is ambitious and potentially useful, but the statistical treatment is extraordinarily convoluted.  Several derivations are internally inconsistent, key sensitivities are quoted in incompatible conventions, and critical null-tests (e.g. pixel–shuffle vs monopole-only vs density-stratified) are mixed without a coherent likelihood.  A large number of quantitative statements cannot be traced to a single well-defined estimator.

Below I list all problems found.  Items marked ESSENTIAL must be fixed before the manuscript can be considered.  I recommend a complete statistical re-write and drastic length reduction.

----------------------------------------------------------------
FINDINGS
----------------------------------------------------------------

ESSENTIAL
----------

P4-E1 §VI C, p. 36  
The “0.20 % Fisher floor” is derived on the half-modulation A/2 but is then compared with full-amplitude injection values (0.75 %, 0.5 %).  Mixing the two conventions invalidates every sensitivity claim in the abstract, conclusions and falsification criterion.  
Fix: Re-calculate the Fisher floor and the injection thresholds in the SAME amplitude convention and propagate to every occurrence (Figures 8, 9; Table XVI; §VII 5).

P4-E2 §VI C, Eq. 7, p. 36  
σ(A) is scaled by √3/Npix, implicitly assuming three independent a₁m modes.  For a cut sky with MASTER inversion the covariance is non-diagonal; the √3 reduction is not justified.  
Fix:  Estimate the dipole variance from the same MC ensemble used for significance, or provide an analytic cut-sky covariance derivation.

P4-E3 §IV D, Table VII  
The 500-realisation monopole-only null is quoted to ±0.0068 × 10⁻².  With N=500 the relative SE on σnull is 3.2 %, therefore z = +1.68 is NOT significant at the quoted precision.  
Fix: Provide confidence intervals on all null moments or increase N until the SE is < 10 % of the quoted deviation.

P4-E4 §VII, headline conclusions  
The same “σ” symbol is used for four different nulls (label-shuffle, pixel-shuffle, monopole-only, bootstrap).  Even though the disclaimer is repeated, the abstract still compares them side-by-side (“−0.12 σ … +0.43 σ … +3.64 σ”) implying a common scale.  Rule #7.  
Fix: Replace all σ values in the abstract / conclusions by p-values or add an explicit sub-script (σ_label etc.)  and remove any cross-comparison.

P4-E5 §III E, p. 10  
The 21.4 % argmax flip rate is treated as “uncertainty” but no additional variance is propagated into the real-space dipole, into Table VI band-powers or into the injection test.  
Fix: Show how the flip noise changes σnull for every estimator that uses hard labels, or re-run those estimators on soft probabilities only.

P4-E6 §III G, §IV B  
The catalogue contains 3.20 M spirals but the Fisher calculation and injection test sometimes use 471 k (“HC”) and sometimes 3.20 M without any mapping.  Sensitivities cannot be checked.  
Fix: Provide a table that lists for EVERY estimator the exact Nspiral and the mask; use those numbers consistently.

P4-E7 §V C  
The claimed “SpArcFiRe null supports working hypothesis” is speculative because no galaxy-by-galaxy comparison is shown.  This is an unsubstantiated validation.  
Fix: Either drop the claim or supply a joint confusion matrix with numbers.

P4-E8 Throughout  
No pre-registration was done, yet the paper repeatedly uses language like “load-bearing estimator”.  HARK-ing risk.  
Fix: Re-label the hierarchy as post-hoc and remove any suggestion of preregistration.

P4-E9 Code availability  
The GitHub tag paper4-v1.0.153 cannot be cloned (repository private at submission) – reproducibility requirement fails.  
Fix: Make the tag public or attach a tar-ball in the submission.

P4-E10 Length  
56 pages (> 30 PRD pages) with massive duplicated text (e.g. §IV D reproduced in §VI G almost verbatim).  
Fix: Reduce to ≤ 30 manuscript pages, move code snippets, extended sweeps and repeated prose to a data-release note or supplementary material.

MAJOR
-----

P4-M1 §III C, Table III  
Validation accuracy is quoted against CE-ResNet pseudo labels, not against independent truth, so 93.7 % is circular.  Needs clearer flagging.  

P4-M2 §IV C, Table VI  
The ℓ=1 line mixes subsample mask (fsky=0.659) with the ℓ=2–5 rows (canonical mask fsky=0.491).  Present as two tables or split the row labels unambiguously.

P4-M3 §III E  
“Rotation stability” test T2 uses 60° steps but the production system uses only flips.  A true D₄ TTA run on the full catalogue is needed to support the statement that the monopole excess is rotation-invariant.

P4-M4 §VI B  
The look-elsewhere correction is handled two different ways (analytic Bonferroni and MC), giving opposite answers.  Provide a unified LEE procedure.

P4-M5 §VI D  
The morphology flatness test is performed on raw counts but the statistic of interest is the χ² of the bin deviations; currently only extremal ∆ values are shown.

P4-M6 Appendix VIII  
The exact apodization parameters (“C² 2°”) are not documented: bin size, cosine power, and mask edge definition required to replicate.

P4-M7 Typographic artifacts: many duplicated phrases (“spin dipole at ℓ = 1 AND ℓ = 2 directly favored”, appears twice in same sentence), audit tags (“wave_14_” file names) appear in the prose.  Clean.

P4-M8 Equation 6  
Uses 1/√(2 N) but this is correct only for p = 0.5; at p ≈ 0.497 the variance differs by 0.6 %.  Recompute, or justify approximation.

P4-M9 Injection test Table XVI  
P(σ>3) at A=0.05 % is listed as 0.01 but median σ = −0.37.  Check numbers.

P4-M10 “14.7 × bootstrap inflation”  
Derived with block size NSIDE = 8 but never used elsewhere.  Give a numerical covariance matrix or remove.

MINOR
-----

P4-m1  Footnote on p 20 mixes two unrelated observables.  
P4-m2  Units toggle between fraction and percentage without notice.  
P4-m3  Equation numbering resets inside appendix.  
P4-m4  Reference order not alphabetical; some arXiv links missing DOIs.  
P4-m5  Figures 8 & 9 legends unreadable at journal column width.  
P4-m6  Table I uses “strict-HC hard-label” before HC is defined.  
P4-m7  Stated CPU/GPU throughput not relevant for PRD; move to data-release note.  
P4-m8  “∼ 2.6× tighter” (sec IV D) – provide actual numbers.  
P4-m9  Typos: “cata- logue”, “classifiaction”, “monopole- subtraction”.  
P4-m10 Citing “Big-Bounce” GitHub seems unrelated.

NIT
---

P4-n1  PACS numbers obsolete; use PhySH.  
P4-n2  Use of “cf.” instead of “see” several times.  
P4-n3  Super-script minus signs missing in a few ×10-6 values.  
P4-n4  “Z2 2-fold flip TTA” ⇒ redundant “Z2”.  
P4-n5  Spell out first acronyms (e.g. HO in Table II).

----------------------------------------------------------------
SUMMARY RECOMMENDATION
----------------------------------------------------------------
MAJOR REVISIONS

The manuscript contains valuable data products, but the current statistical analysis is internally inconsistent and far too long.  The sensitivity floor, null-model hierarchy, and significance estimates must be re-derived in a single coherent framework and all essential items above must be addressed.  A ≤ 30-page streamlined methods paper with a clear derivation chain, one well-defined null per estimator, and full reproducibility would be publishable.