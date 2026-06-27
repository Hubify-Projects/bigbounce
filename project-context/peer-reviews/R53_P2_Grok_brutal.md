# P2 R53 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/R53_P2/02_full_draft.pdf` md5=7a1425ed pages=28
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 86.8s

---

**Referee Report**

**Paper:** P2  
**Journal target:** Phys. Rev. D  
**Round context:** First read (adversarial)

**P2-E1 (ESSENTIAL)**  
**Location:** Abstract (p. 1), lines beginning “We obtain bispectrum-only 5.2–5.5σ … reducing to a realistic ∼2.6–5σ after the systematic budget”  
**Problem:** The headline interval 5.2–5.5σ is obtained only under the specific noise-weighted central value r = 0.84 (Table IV, row “template-corrected baseline”). The same paragraph immediately juxtaposes this number with the post-systematic range without an explicit qualifier that the two figures are not directly comparable because one uses a different weighting scheme and the other folds in additional nuisance marginalization. PRD requires every such juxtaposition to carry an on-the-spot “not directly comparable” clause.  
**Required fix:** Insert the clause after every occurrence of the 5.2–5.5σ interval (abstract + §IV + §VII) or recompute a single, uniformly weighted significance that already includes the full budget.

**P2-E2 (ESSENTIAL)**  
**Location:** Abstract (p. 1) and §VI.C (p. 12–13), Table II  
**Problem:** The abstract states “Bayes factor BF ≈ 9 (recommended σ_theory = 1.0 …) up to BF ≈ 14”. Table II shows that BF = 9–14 is obtained only for the broad [-15, +15] multifield competitor prior; the narrow [-5, +5] competitor yields BF ≈ 4–7. The abstract therefore reports the upper envelope of a prior-sensitivity scan as the headline result without stating the prior width that produces it.  
**Required fix:** Either (a) quote only the recommended σ_theory = 1.0, narrow-competitor value (BF ≈ 4) or (b) add an explicit sentence “BF range 9–14 assumes the broadest competitor prior; the physically motivated narrow prior gives BF ≈ 4–7”.

**P2-M1 (MAJOR)**  
**Location:** §II.B (p. 3–4) and null-space scan (p. 4)  
**Problem:** The six-monomial basis is declared 3-dimensional after three benchmark constraints, yet the SVD singular-value ratio σ_3/σ_1 ≈ 0.3 is presented as an “empirical property” with no analytic proof that the null-space dimension remains exactly three under a generic linear reparametrization of the monomials. A change of basis inside the same polynomial ring can alter the numerical conditioning and therefore the recovered r distribution.  
**Required fix:** Provide either an analytic rank proof or a Monte-Carlo test over random GL(6) transformations of the monomial basis showing that the recovered r scatter remains ≤ 0.13.

**P2-M2 (MAJOR)**  
**Location:** §IV (p. 9) and Fig. 2  
**Problem:** The SPHEREx forecast headline 5.2–5.5σ is obtained with a 2-D flat-sky Fisher matrix on tiled patches; the text explicitly states that a “complete validation with realistic SPHEREx mocks, sky masking, and photometric-z scatter would be required before claiming a data-analysis result.” No such validation is performed.  
**Required fix:** Either downgrade the forecast to “projected ideal sensitivity” throughout or supply at least one end-to-end mock pipeline result.

**P2-M3 (MAJOR)**  
**Location:** §V (p. 10–11) and MegaMapper paragraphs  
**Problem:** MegaMapper is repeatedly described as “proposed, not yet funded.” All numerical forecasts (3–7σ) are therefore purely illustrative. The paper nevertheless places these numbers on equal visual footing with SPHEREx results in Fig. 2 and the abstract.  
**Required fix:** Move all MegaMapper numbers to a clearly labeled “speculative outlook” subsection and remove them from the abstract and from the main detection-significance figure.

**P2-N1 (MINOR)**  
**Location:** Eq. (6) (p. 8) and surrounding text  
**Problem:** The quoted uncertainty r = 0.84 ± 0.02 is the standard deviation across four weighting schemes; the per-realization scatter from the 200-injection test is ±0.01. The two error bars are never distinguished in the text.  
**Required fix:** Label the ±0.02 as “scheme-to-scheme variation” and the ±0.01 as “Monte-Carlo statistical uncertainty.”

**P2-N2 (MINOR)**  
**Location:** Table IV caption (p. 18)  
**Problem:** The table mixes “acts on numerator” and “acts on denominator” rows without a uniform sign convention for the resulting σ.  
**Required fix:** Add a single column “Effect on σ(f_NL)” with explicit ± or “degrades to” language.

**P2-NIT1 (NIT)**  
**Location:** Title page, “Dated: June 19, 2026”  
**Problem:** Future date on a manuscript under review. Cosmetic only.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript is a careful but purely recast forecast whose headline numbers (5.2–5.5σ, BF ≈ 9–14) are obtained only after a chain of weighting choices, prior widths, and unvalidated flat-sky approximations. Two essential fixes are required: (1) explicit non-comparability language wherever differently weighted significances are juxtaposed, and (2) removal or clear isolation of all MegaMapper numbers that rest on an unfunded facility. Until these are addressed the paper does not meet PRD standards for a methods forecast.