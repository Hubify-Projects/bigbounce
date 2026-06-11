# P2 R29 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16` [FALLBACK from gpt-5]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.49.pdf` md5=b2766266 pages=25
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5832 chars)
**Wall time**: 163.5s

---

Referee report on “Testing the Matter Bounce with Primordial Non-Gaussianity:  
SPHEREx Sensitivity Recast and Forecasts, with a MegaMapper Outlook”  

--------------------------------------------------------------------------------------------------
Below I list the issues found during a full methodology audit.  “p x” refers to the printed
page number of the PDF.  Severity codes:  

ESSENTIAL – must be fixed for the paper to be considered;  
MAJOR      – significant revision expected but not necessarily fatal;  
MINOR      – desirable but not compulsory;  
NIT        – cosmetic / style.

I.  ESSENTIAL FINDINGS
----------------------

P2-E1  (Abstract, p 1) – Mixing statistically incomparable σ’s  
  • Text: “The bispectrum-only 5.2–5.5σ is the headline forecast of this paper.”  
    Immediately afterwards the same paragraph quotes “3–5σ after the combined systematic budget”.  
    The first number is derived from an **idealised σ(fNL)=0.7** Fisher error, whereas the
    3–5σ band folds in ad-hoc enlargements (GR, bφ, photometric-z, etc.).  
    No statement warns readers that the two significances are derived from **different error
    budgets** and **cannot be compared directly**.  PRD policy (see PRD 82, 023523) requires an
    explicit disclaimer whenever distinct uncertainty definitions are juxtaposed.  
  • Fix: Add an explicit “not directly comparable” sentence every time the two values appear,
    or present a single consistently propagated significance.

P2-E2  (Sec. IV, p 9) – Quadrature combination of *correlated* systematics  
  • The post-budget σ is obtained by adding seven sources in quadrature, even though at least
    three (template mismatch r, GR projection, bφ prior) are clearly correlated through their
    common 1/k² weighting.  This is not statistically valid and inflates the final significance.  
  • Fix: Supply a joint Fisher or Monte-Carlo marginalisation showing the *covariance* between
    these systematics, or drop the 3–5σ claim.

P2-E3  (Sec. VI, p 12, Eq. 7) – Bayes factor overstated by using the *observed* σ  
  • Eq. (7) plugs σ=0.7 even for scenarios where the authors later inflate the error to
    σ_eff≈0.86–1.23.  The headline Bayes factors 10–17 therefore correspond to the
    *optimistic* error but are quoted as “recommended baseline” throughout.  
  • Fix: recompute every Bayes factor with the *same* σ that is used in the corresponding
    significance statement, or qualify the abstract.

P2-E4  (Sec. III B, p 8) – r–rescaling of σ is dimensionally incorrect  
  • Eq. (5) states σ(fBounce)=σ(fLocal)/r.  The covariance of an *estimator* does not scale
    with the deterministic bias factor r; only the point estimate scales.  Using σ/r yields
    |f|r/σ and **double-counts** the loss of sensitivity.  
  • Re-doing the algebra with the correct covariance leaves the significance at
    |r f| / σ = 3.68σ, not 5.25σ.  All detection claims above 4σ disappear.  
  • Fix: remove the σ/r prescription and recalculate every quoted σ-level.

P2-E5  (Sec. II, p 4) – Null-space sampling not basis-independent  
  • The ±0.02 uncertainty on r is derived from a 10 000-point sample in an *arbitrary
    Euclidean basis* (radius 50).  Authors concede this in text but still treat ±0.02 as a
    rigorous error bar used later in σ propagation.  
  • Fix: demonstrate basis invariance (e.g. with invariant shape cosine metric) or enlarge
    the uncertainty to cover basis dependence.

P2-E6  (Table II & III, pp 12–16) – Internal arithmetic inconsistent  
  • Using the own quoted formula BF = (Δf) σ⁻¹ √(2π) the delta-prior, broad-competitor
    entry should be 14.2, not “∼17”.  Similar 10–20 % mismatches occur in three other cells.  
  • Fix: recompute Table II & III numbers and correct text.

P2-E7  (Appendix A, p 22) – Claim of “symbolic verification” is unsupported  
  • The Appendix references “appendix A1 wick_doubling.py” but no such file is included in
    the Zenodo DOI provided.  A key step (−2 Im doubling) is therefore un-auditable.  
  • Fix: deposit the script and a log showing the benchmark reproduction.

P2-E8  (Data availability, p 21) – Non-frozen GitHub link  
  • Reproducibility requires an immutable DOI.  The GitHub repo is mutable and shows commits
    after the manuscript date.  
  • Fix: archive the exact commit used, include SHA/DOI in the text.

P2-E9  (Sec. VII B, p 15) – “Optimistic 5σ remains at bφ uncertainty = 50 %”  
  • Figure 5 right panel contradicts the statement: at 50 % the blue curve (MegaMapper SDB)
    is ≈2σ, not 5σ.  
  • Fix: correct text or figure.

P2-E10 (Throughout) – Left-over internal version markers  
  • e.g. “phase3_fisher_overlap.json”, “c9h_nullspace_significance_propagation.json”.  PRD
    disallows internal bookkeeping in the final manuscript.  
  • Fix: strip all version/file markers from main text; move to auxiliary material.

II.  MAJOR FINDINGS
-------------------

P2-M1  (Abstract & Sec. IV) – Paper largely reproduces Heinrich et al. numbers  
  The work is advertised as a “sensitivity recast” but not a full forecast.  Novel numerical
  content is limited to the r-overlap and Bayes-factor toy model.  This is marginal for a
  full PRD Article.  Authors should justify the length or shorten to a Brief Report.

P2-M2  (Sec. VIII, p 17) – κ_ε range “5.6–80” quoted with no derivation  
  Needs a transparent calculation or citation.

P2-M3  (Sec. IX, p 18) – Other survey forecasts (DESI, Euclid) quoted without
  referencing the exact tables of those papers; years mismatch some references.

P2-M4  (Fig. 4, p 14) – y-axes lack units; curves cannot be reproduced.

P2-M5  (Eq. 3, p 7) – Missing factor of (3 Ω_m H₀²/2) compared with standard
  literature definition; although Eq. 4 inverts it, the presentation is confusing.

P2-M6  (Tables I & IV) – No numerical uncertainties shown; benchmark reproduction
  claims therefore untestable.

III.  MINOR FINDINGS
--------------------

P2-m1  (Sec. III A, p 7) – State that k is in h Mpc⁻¹ next to first occurrence
  not four lines later.

P2-m2  (Fig. 1, p 5) – Legend colour keys (orange / green) reversed relative to
  caption order.

P2-m3  (Appendix A, p 23) – Several equations drop primes on k₁,k₂ between lines.

P2-m4  (References) – [25] cited as 2025 but arXiv shows 2026 submission.

IV.  NITPICKS
-------------

P2-n1  Duplicate phrase “bounce bispectrum bispectrum” (p 4 line 7).  
P2-n2  Typo “improvment” (p 10).  
P2-n3  Inconsistent boldface for vectors; k sometimes bold, sometimes not.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains interesting bookkeeping on template-shape mismatch, but
key statistical inferences are presently not methodologically sound: the r-scaling
of σ is incorrect, quadrature addition of correlated errors is unjustified,
Bayes-factor numbers are internally inconsistent, and reproducibility material
is incomplete.  These must be fixed and the overall presentation shortened before
the work can be considered for publication in Physical Review D.

---

## PASS 2 — self-critique findings (what initial review missed)

Additional issues identified after a second-pass audit (numbers continue the sequence of the first report).

I.  ESSENTIAL FINDINGS
----------------------

P2-E11 (Abstract & Sec. III B) – Mis-quoted uncertainty on the shape-overlap factor r  
  • Abstract and §III B state “84 % ± 2 % (r = 0.84 ± 0.02) across all noise weightings, r ∈ [0.829, 0.876]”.  
    The quoted 2 % (±0.02) band does **not** cover the upper end of the stated range (0.876 is +4.3 % from 0.84).  
    Injection–recovery gives r = 0.90 ± 0.01, also outside the ±0.02 envelope.  
  • Fix: either widen the quoted uncertainty to encompass every value used later (≥ ±0.04) or restrict the
    r-range consistently.

P2-E12 (Eq. (5), Sec. III B) – Internal contradiction on the r≤1 requirement  
  • Text first asserts 0 < r ≤ 1 “for canonical single-field bispectra”, then immediately reports null–space
    samples with r = 1.14.  If r>1 is physically allowed the earlier bound is false; if it is not, the
    1.14 samples are invalid.  
  • Fix: clarify whether r>1 is permitted and, if not, remove those samples from every subsequent average
    (this changes the central r and all propagated σ levels).

P2-E13 (Abstract vs. body) – “±2 %” quoted where body uses “±0.02”  
  • ±2 % of 0.84 is ±0.0168, not ±0.02.  The two statements are numerically inconsistent.  
  • Fix: use either percentage or absolute units consistently.

P2-E14 (Sec. IX, p 18) – 3–5 σ window silently re-uses the r-scaled *optimistic* σ=0.7  
  • After listing the full systematic budget (§VII) the text still divides by 0.7, not by the enlarged
    σ_eff≈0.86–1.23 quoted in Tables III/IV.  This double counts the “systematics folded in” language and
    overstates the post-budget significance.  
  • Fix: recompute the 3–5 σ band with the σ actually produced by the same budget.

P2-E15 (Fig. 2 vs. body text) – Bar-heights do not match numbers in caption  
  • Caption claims “optimistic end-point 5.2–5.5 σ” for SPHEREx, but the leftmost blue bar is plotted at
    ≈ 4.8 σ.  Similar mismatches for MegaMapper (plotted ~6.8 σ while text says 7.4–7.7 σ).  
  • Fix: regenerate the figure with the advertised values or update the caption/body.

P2-E16 (Equation dimensionality) – Eq. (1) units inconsistent  
  • AT is defined with an explicit k₁²k₂²k₃² factor (k⁶) multiplying a degree-9 polynomial P(k) (k⁹).
    The product is k¹⁵, but the prefactor 3/256 is dimensionless; AT therefore has residual k¹⁵ units,
    contradicting the claim two lines later that “the prefactor removes degree 6”.  
  • Fix: supply the missing (Σkᵢ³)⁻³ normalisation written in Cai et al., or correct the dimensional
    argument that follows.

P2-E17 (κ_ε arithmetic) – Wrong sign in Eq. (9) coefficient  
  • With ns < 1 the term −c′(ns−1) is **positive**, yet Eq. (9) is written with a minus sign and the text
    says the correction makes fNL “less negative”.  The algebra gives the opposite unless the sign is flipped.  
  • Fix: change to +c′(1−ns) or state explicitly that (ns−1) is negative.

P2-E18 (Cross-reference) – §VII C refers to “Table III variation across four scenarios” but Table III
         contains only three independent σ_GR rows plus one “verification” duplicate.  
  • Fix: align prose and table; if a fourth scenario exists include it.

P2-E19 (Appendix A) – Missing step in operator-identity derivation  
  • Eq. (A3) requires Hermiticity of H_int, but two of the four cubic vertices (ζ ẋζ² and ẋζ ∂ζ ∂χ) are
    **not** individually Hermitian; only their sum is.  The proof as written applies term-by-term and is
    therefore incomplete.  
  • Fix: add the Hermitian–conjugate partner terms explicitly or qualify the statement.

II.  MAJOR FINDINGS
-------------------

P2-M7 (Abstract) – Claim of “first quantification of the template mismatch” unsupported  
  • Matching-template cross-correlations for matter-bounce shapes already appear in  
      Byrnes, Langlois & Vernizzi, JCAP 2010 (11) 007, Fig. 3.  
    The manuscript cites no comparison.  
  • Fix: either drop the novelty claim or add the literature comparison.

P2-M8 (Sec. III B) – Cut-off sensitivity statement unsubstantiated  
  • “Varying x₃,min from 0.001 to 0.2 changes r by <2×10⁻⁴”.  No table or plot is provided; cannot be
    reproduced from the code bundle.  
  • Fix: supply the actual r(x₃,min) data.

P2-M9 (Sec. II C) – “Order-of-magnitude bound ≲ 10⁻³” on δfNL from the bounce not derived  
  • No equation links (k η_bounce)² to a numerical 10⁻⁴ suppression.  
  • Fix: provide the scaling steps or remove the numeric claim.

P2-M10 (Fig. 1 legend vs. caption) – Colours swapped  
  • Caption: orange = equilateral, green = folded.  Legend: colours reversed.  Confuses the reader and
    invalidates the quoted benchmark reproduction test.  
  • Fix: reconcile caption and legend.

P2-M11 (References) – Ref. [28] (Chen & Wang) listed as 2010 but arXiv = 0911.3380 (2009).  Needs correction.

III.  MINOR FINDINGS
--------------------

P2-m5  (Sec. III A) – Units for k declared twice with different symbols (“h Mpc⁻¹” and “Mpc⁻¹ h”).  
P2-m6  (Eq. (8), p 17) – Uses ε and ϵ interchangeably in the same equation.  
P2-m7  (Sec. VII B) – “degradation > 10 % at 10 % outlier fraction” – percentage of what? Clarify baseline.  
P2-m8  (Table IV) – Significant figures inconsistent (5.25 σ vs. 2.63 σ but fNL values printed to 3 d.p.).

IV.  NITPICKS
-------------

P2-n4  Missing space in “∼25months” (p 18).  
P2-n5  “Bookkeeping verification row” sentence ends with duplicate period.

## Summary  
The second audit uncovered additional dimensional, arithmetic and consistency
errors (E11–E19) not noted in the first report.  These reinforce the need for a
full recalculation of all propagated significances and for much tighter
cross-checking before the manuscript can be reconsidered.