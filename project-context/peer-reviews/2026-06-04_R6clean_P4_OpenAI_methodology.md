# P4 2026-06-04_R6clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 41.1s

---

### Referee report – Methodology/Statistics  
Paper P4 — “Survey-Scale Galaxy Chirality with Equivariant TTA …”

--------------------------------------------------------------------
I have focused exclusively on methodology, internal arithmetic
consistency and statistical validity, as requested.

--------------------------------------------------------------------
KEY  
ESSENTIAL  paper cannot be accepted unless fixed  
MAJOR  significant revision required but potentially salvageable  
MINOR  should be addressed; editor may waive if time is short  
NIT  typography / style

--------------------------------------------------------------------
FINDINGS
--------------------------------------------------------------------

ID P4-E1  
Sec. III A, p. 6 (and repeated throughout)  
Problem σ-values from FOUR mutually incommensurable null
procedures (“per-pixel shuffle”, “label shuffle”, “monopole-only
binomial”, “bootstrap”) are quoted interchangeably in the prose
(e.g. abstract: “−0.12 σ … +0.43 σ … +3.64 σ”), sometimes in the
same sentence, without always restating which null is being used.
Although a disclaimer exists, placing the numbers on the same
σ-scale invites direct comparison that is mathematically invalid.  
Fix In every place a σ figure is quoted, append an unambiguous tag
(e.g. “σps” for pixel-shuffle, “σls” for label-shuffle, “σbin”,
“σboot”).  Add a one–line legend in the abstract and conclusions.
                                             ESSENTIAL

ID P4-E2  
Table II and surrounding text  
Problem The “headline” −0.12 σ result is from a *different* mask,
monopole subtraction scheme, and MC size than the +3.64 σ
“canonical” figure, yet the table presents them in one list as if
they were parallel.  This conflates two distinct estimands.  
Fix Split the table: one table contains only the pre-declared
primary estimator(s); a second contains all diagnostics.  Do **not**
mix them in one summary.                              ESSENTIAL

ID P4-E3  
Sec. VI C, pp. 36–38  
Problem Throughout the sensitivity discussion “0.2 % minimum
detectable dipole” is obtained from analytic Fisher scaling on the
half-modulation (A/2) whereas the MC‐based threshold of 0.75 %
refers to the full modulation A.  The manuscript later switches
back and forth.  This is dimensional inconsistency.  
Fix Choose one amplitude convention (recommend the full
amplitude A) and rewrite every threshold, floor and injection
statement in that convention.  Supply one equation defining it.
                                             ESSENTIAL

ID P4-E4  
Sec. IV C, footnote 9; Table VI  
Problem Shot-noise denominator is changed (Ntotal → Nspiral ),
altering the “6.48 σ” to “6.10 σ” yet earlier σ values still appear
elsewhere.  There is no guarantee no other quantities are affected.  
Fix Run a complete end-to-end recompute with the final
denominator and purge every earlier value.  Provide a machine
-readable table of all Cℓ before and after correction. ESSENTIAL

ID P4-M1  
Sec. III E, p. 10 & Sec. VI D  
Problem The arg-max label flips by 21 % under D4-TTA yet hard-
label diagnostics (hemisphere, confidence ladder, injection test)
do not propagate this extra noise into their error bars except by
an *ad-hoc* “∼1.21×” explanation.  
Fix Give a formal derivation of the additional variance term and
propagate it everywhere hard labels are used, or drop the hard-
label analyses altogether.                           MAJOR

ID P4-M2  
Sec. VI G, pp. 40–41  
Problem The linear-template fit used to “strongly disfavour”
interpretation (i) treats residuals as pixel-independent Gaussian,
then rescales σ by a block bootstrap picked *post hoc* (factor 14.7)
without an objective criterion.  The corresponding “264 σ” and
“18 σ” claims are meaningless.  
Fix Either supply a spatial-covariance model that is fitted once
(and report the χ² with its d.o.f.), or remove the 264 σ / 18 σ
language and state only the empirical p-value of the MC rank.
                                                     MAJOR

ID P4-M3  
Sec. IV B, Table V  
Problem The 9.5 σ “monopole” significance is repeatedly called
“formally significant” yet the authors concede it is almost surely
training-set bias.  Presenting a meaningless null-hypothesis test
as a sigma is misleading.  
Fix Replace the σ by a plain fractional excess and label it “known
systematic, not used for cosmology”.               MAJOR

ID P4-M4  
Whole paper (54 pages)  
Problem The manuscript is three times the length needed for its
single substantive result.  The reader must wade through large
blocks of narrative and repeated caveats.  
Fix Condense to ≤ 25 journal pages by moving: bias-suite
details, GPU throughput benchmarks, Git SHA lists, *etc.* to an
online appendix/repository.                           MAJOR

ID P4-M5  
Sec. III F, Table IV  
Problem Four of the eight “bias hardening tests” are merely
sanity checks (T3,T6,T7,T8).  Calling the whole set “passes 8/8”
over-advertises bias control.  
Fix Separate stress-tests from sanity-checks and report them
independently.                                     MINOR

ID P4-m6  
Many places  
Problem Moment-z sometimes quoted when null distribution is
non-Gaussian (e.g. single-ℓ MC).  Could mislead.  
Fix Whenever empirical MC is used give only rank-based two-sided
p; do not convert to σ.                               MINOR

ID P4-m7  
Sec. III C, Table III  
Problem Confusion matrix percentages not transposed correctly
(rows should sum to 100 %).                         NIT

ID P4-n1  
Typos: duplicate phrases (“canonical canonical-mask” once),
missing parentheses in equations (several).         NIT

--------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

The authors have assembled a valuable public catalogue and the
technical work is impressive, but the manuscript as written
conflates incommensurable σ, contains dimensional ambiguities,
over-interprets template regressions, and is needlessly long.
All ESSENTIAL items must be fixed and the paper tightened
substantially before it can be considered for publication.