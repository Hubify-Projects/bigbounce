# P2 2026-06-04_R6clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 56.0s

---

# Referee report for PRD – Methodology audit

I read the manuscript “Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook” in full.  
Below I list all methodology problems detected, following the requested classification.

--------------------------------------------------------------------
ESSENTIAL
--------------------------------------------------------------------

P2-E1  | Abstract & §IV, p. 1–8  
Problem:  Detection significance is obtained by simply scaling the Heinrich et al. bispectrum error bar σ(fNL)=0.7 with the shape-overlap factor r=0.84 (Eq. 5).  This assumes that a local-template KSW estimator remains unbiased when the true sky is *not* local, and that the covariance contributed by the orthogonal part (1-rcos²≈0.06) may be ignored.  In reality the estimator mean gets rescaled by the *inner product of inverse-covariance–weighted shapes*, not by the raw Fisher overlap, and extra variance from leakage of the orthogonal component enters the Fisher matrix.  The paper therefore under-states σ(fNL) and over-states the 5.2–5.5 σ headline significance.  
Fix: Provide a full covariance calculation (or at minimum cite an existing one) that includes orthogonal-shape noise and shows the actual σ(fNL) of a local estimator on a bounce signal.  If not available, retract the 5.2–5.5 σ figure and state only the r|fNL|=3.7 amplitude difference without converting it into σ.

P2-E2  | §II B vs. §III B, p. 3 & 7  
Problem: Two incompatible uncertainty ranges for the amplitude-recovery factor are used.  From the 10 000 coefficient scan, r = 0.85 ± 0.13 (range 0.55–1.14), but the subsequent forecasts use r = 0.84 ± 0.02.  The larger ±0.13 spread is not propagated into the quoted detection significances nor the Bayes factors.  
Fix: Use the same r distribution everywhere and include its full variance in all downstream error propagation, or justify statistically why the ±0.13 dispersion can be ignored.

P2-E3  | §VI, p. 10–12  
Problem: The Bayes-factor analysis treats *forecast* numbers (σ(fNL)) as if they were data.  A Bayes factor is a function of an actual measurement, not of a prospective 1 σ error bar.  Presenting BF≈10–17 as “model selection power” before any data exist is methodologically unsound.  
Fix: Remove all Bayes-factor numbers, or re-label them explicitly as *expected* Bayes factors conditional on a future detection exactly at the fiducial value, and stress that they are not evidence.

P2-E4  | §VII B, Figure 5  
Problem: σ(fNL) degradation due to unknown PNG-bias parameter bϕ is estimated by inflating the Fisher error bar by a hand–drawn factor (20 % → 50 %).  No derivation is provided for the mapping “20 % prior ⇒ 1.2× σ”.  
Fix: Supply the explicit two-parameter Fisher matrix used and the algebraic expression for the marginal error, or drop the quantitative degradation factors.

P2-E5  | §II, footnote  
Problem: The “commutator doubling” argument is used to fix the factor-of-two dispute, but the four cubic-action integrals are *not* recomputed.  The paper’s conclusion that −35/8 is correct therefore rests only on reproducing three published numbers, not on an independent derivation.  
Fix: Either perform the full in-in integral (or supply code) or clearly downgrade the claim to “we *assume* Cai et al. is correct”.

P2-E6  | σ(fNL) mixing  
Problem: The manuscript alternates between bispectrum σ=0.7 and scale-dependent-bias σ=0.5–1.5 values when quoting significances, without always making clear which channel is being used.  This violates the instruction “null-model σ values must be on comparable scales”.  
Fix: Tabulate the exact σ used in every significance statement and keep channels separate.

--------------------------------------------------------------------
MAJOR
--------------------------------------------------------------------

P2-M1 | Abstract  
Over-long (≈850 words).  PRD limit is ~600.  Cut repetitions and in-line meta-discussion.

P2-M2 | §IV, p. 7  
Injection/recovery test uses full sky (fsky=1).  Realistic SPHEREx has fsky≈0.75 after Galactic cut.  Stated 19 % degradation is only a back-of-envelope.  Provide a masked simulation or remove the claim.

P2-M3 | §VII A, Fig. 4  
The “GR degradation” parameter σGR is floated between 0 and 1 with no sourcing.  Need either an external calculation or a justification of the adopted 10–30 % range.

P2-M4 | Throughout  
The phrase “UV-completion independent” is repeatedly used, but Sec. II C lists six model-dependent assumptions.  This is internally inconsistent.  Rephrase to “independent *within the scalar-only Wilson-Ewing subclass*”.

P2-M5 | §III A  
Equation (3) omits the factor (2/3) Ωm H0² present in the standard SDB kernel.  Check dimensional consistency.

P2-M6 | §VI  
Heavy use of unpublished references (Heinrich et al. 2024, Jolicoeur et al. 2025) prevents verification.  Upload pre-prints or replace by public sources.

--------------------------------------------------------------------
MINOR
--------------------------------------------------------------------

P2-m1 | Eq. (5) uses left-hand superscript “measured”, right-hand “local”.  Ambiguous.  Define clearly.

P2-m2 | Duplicate phrase “multi-tracer multi-tracer” (p. 6, l. 3).  Remove.

P2-m3 | Table II caption: “row is the same competitor prior ... and the two tables are numerically consistent” – unreadable; shorten.

P2-m4 | Several references cited as “2026” pre-prints.  Update arXiv numbers.

P2-m5 | Missing units on k (h Mpc⁻¹) in Fig. 4 axis labels.

--------------------------------------------------------------------
NIT
--------------------------------------------------------------------

P2-n1 | Typo “re-definition” → “redefinition” in §II B.  
P2-n2 | Eq. (9) missing factor 1/8 in first term (should be (ns−1)/8?).  
P2-n3 | Random boldface in Eq. (A6).  
P2-n4 | Extra space before comma in several places (“bounce , not”).  
P2-n5 | Inconsistent notation for spectral tilt: ns vs. n_s.

--------------------------------------------------------------------
Too long?

Main text is 22 pages for a single-forecast paper; could be cut to ≤15 by relegating Bayes-factor material and the mega-mapper speculation to appendices.

--------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

The manuscript contains interesting cross-checks but the headline detection significance and Bayes-factor evidence are based on un-validated assumptions (E1–E4).  These must be corrected or the corresponding claims withdrawn before the paper can be considered.