# P4 R10v3 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high
**Wall time**: 89.6s

---

Referee report for
“Survey-Scale Galaxy Chirality with Equivariant TTA …”
(P4 | Round R10v3, 10 pages)

I have read the complete PDF (v3) and audited every scalar, equation, table and statistical claim as requested.  Findings are grouped by severity.

----------------------------------------------------------------
ESSENTIAL FINDINGS  – must be fixed before further consideration
----------------------------------------------------------------
P4-E1 Sec. IV B, p. 3 (Table II, Tier A “Dev. (σ)”)  
  • Offending text “28.8”  
  • Problem With N=3 201 160 and f_CW = 0.5079,   
    σ_binom = √[p(1-p)/N] = 0.0002795.  
    (0.5079-0.5000)/0.0002795 = 28.32, not 28.8.  Same
    mis-rounding propagates to the verbal 28.8 σ claim in
    Sec. VI.  
  • Required fix Re-compute and correct the σ value (28.3 σ
    to one decimal) everywhere it appears and adjust
    downstream text.

P4-E2 Sec. IV B, p. 3, line 19 (“3.86× asymmetry-suppression
factor from raw +2.05 % to equivariant –0.53 %”)  
  • Problem The raw excess is +0.79 %, the equivariant shift
    is –0.26 %.  The change in magnitude is 1.05 % and the
    suppression factor |–0.26| / 0.79 = 0.33 (i.e. a 3.0×
    reduction), not 2.05 % or 3.86×.   
  • Required fix Correct both the quoted percentage
    difference and the suppression factor and propagate the
    correction to Sec. VI (where the same numbers re-appear).

P4-E3 Sec. VI A, p. 6 (“Fisher Poisson floor at 3 σ is
∼ 0.29 % … σ(A/2)≈0.048 %”)  
  • Problem For N=3 201 160 and p=0.5 the standard error on
    the mean asymmetry is 0.0279 %, not 0.048 %.  A 3 σ
    detection threshold is therefore ≈ 0.167 %, not 0.29 %.  
  • Required fix Re-derive the Fisher lower bound, display
    the algebra, and correct both quoted numbers.

P4-E4 Sec. IV C a, p. 4 (“Simple dipole … significance
0.43 σ”)  
  • Problem Only the significance is given; the dipole
    amplitude (Δf_CW), its uncertainty and the direction
    (in Galactic or equatorial coordinates) are not
    reported, yet later sections rely on this value.  
  • Required fix Quote the fitted dipole amplitude,
    1-σ error bar, and the dipole axis in a reproducible
    coordinate system.

P4-E5 Throughout – sigma from different nulls shown side-by-side
  • Example Table I juxtaposes –0.122 σ (label-shuffle null)
    and +3.64 σ (per-pixel shuffle null) in the same column
    without an explicit reminder that the numbers are not
    cross-comparable.  
  • Required fix Add a footnote to every table/figure that
    lists multiple σ values from different nulls stating
    clearly “σ refers to the specific null in the
    ‘Null’ column and must not be compared across rows”.

P4-E6 Monte-Carlo sample size for high-σ estimates  
  • Problem Several σ values >3 are quoted from only
    N_MC = 500 permutations (e.g. the +3.64 σ canonical
    residual).  With 499 degrees of freedom the sampling
    error on the variance is ≈ 10 %, so the quoted σ has a
    ±0.36 systematic uncertainty – too large for
    “third-decimal” precision.  
  • Required fix Increase all permutation/null ensembles
    that feed into reported σ or p < 0.01 to at least
    N_MC = 10 000 or quote a bootstrap error on σ and
    propagate it to the significance.

P4-E7 Sec. IV D, p. 4 (Table IV)  
  • Offending numbers Data 1.696 × 10⁻²; Null mean
    (1.685 ± 0.007) × 10⁻²; z = +1.68.  
  • Problem (1.696 – 1.685)/0.00007 = 1.57, not 1.68.  
  • Required fix Re-calculate z or correct the tabulated
    σ_null.

-------------------------------------------------
MAJOR FINDINGS  – significant, but not fatal issues
-------------------------------------------------
P4-M1 Sec. A, p. 7: statement that monopole subtraction
“increases σ from +1.85 to +3.64” although the amplitude
decreases.  This requires an explicit explanation of why
σ_null shrinks by > (3.64/1.85)² ≈ 3.9 between the two
runs; otherwise the change is unintuitive.

P4-M2 Table I, p. 4: the “Null” column mixes
“pp-shuffle”, “label-shuffle”, “isotropic bootstrap” and
“monopole-only” but the algorithms are not defined
anywhere.  Provide precise definitions (what quantity is
shuffled, whether shuffles are within-pixel or global,
etc.) and the seeds.

P4-M3 Sec. IV D: the claim that the monopole-only null
“reproduces 99.3 % of the observed amplitude” is hard to
audit because the definition of “amplitude” (pseudo-C_ℓ,
un-binned, or band-power?) is not repeated here.  Spell out
the exact statistic and show the single-number ratio.

P4-M4 Figures 2 & 3 (low-ℓ spectra): vertical axes lack
units (“sr” is given only in Table III).  Axis labelling
must match the units in the tables.

P4-M5 The paper is 10 text-dense pages plus five
appendices but contains only one primary scientific
result (the null dipole).  A reduction to ≲ 7 PRD pages
would improve clarity.

-------------------------------
MINOR FINDINGS  – should be fixed
-------------------------------
P4-m1 p. 2, col. 2: “3.86× asymmetry-suppression factor”
appears twice with inconsistent capitalisation of “factor”.

P4-m2 Duplicate phrase “canonical-mask residual is
interpretation (ii) systematic” occurs on pp. 1 and 4.

P4-m3 p. 5, Table III caption: “ℓ= 1 (single mode) anchors
the dipole-isotropy null” – grammar (“anchors”) unclear.

P4-m4 p. 8, App. C, part d: minus sign missing before “0.03 σ”.

P4-m5 Reference [12] year incorrect – Dosovitskiy et al.
(2021 not 2020).

---------------------
NITS  – cosmetic only
---------------------
P4-n1 p. 1, PACS numbers out of date; PRD now uses
“Physics Subject Headings”.

P4-n2 Several inline URLs break across lines without
\url{} wrapping (pp. 2 and 9).

----------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

The manuscript presents a careful analysis and a valuable
public data-set, but seven essential numerical and
statistical inconsistencies must be corrected and several
major clarifications added before the work can be relied
upon.