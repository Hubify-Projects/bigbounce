# P2 R7 — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 46.9s

---

# Referee report – Methodology audit  

Paper: “Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx Forecasts, with a MegaMapper Outlook”  

----------------------------------------------------------------  
FINDINGS  

ESSENTIAL (must be fixed before further processing)  
----------------------------------------------------------------  
P2-E1  Abstract & §IV, p.1–8  
Problem  The quoted detection range “5.2–5.5 σ optimistic before GR and bφ degradation, 3–5 σ after the combined systematic budget” is obtained by multiplying the Heinrich et al. Fisher error σ(fNL)=0.70 by a single amplitude-loss factor r=0.84.  All additional systematics (GR projection, bφ freedom, photo-z, polynomial null space, shape mismatch, etc.) are only stated qualitatively or as separate %-level “degradations”; no single combined covariance matrix is built.  The final 3–5 σ figure therefore mixes a rigorous Fisher number with ad-hoc linear scalings, violating comparable-σ requirement #7.  
Fix  Provide one consolidated covariance (Fisher or MC) that contains every degradation term simultaneously, or quote separate significances for each channel without combining unlike σ values.

P2-E2  §VI & Table II, pp.10–12  
Problem  A Bayes-factor envelope “∼10–17” is advertised as a headline discriminator yet is entirely prior-driven (delta prior vs. σtheory = 1) and model-class–boundary driven (competitor prior  [−15,+15] vs. [−5,+5]).  The larger 17 value is available only under the delta prior that the authors themselves call “not physically motivated”.  Presenting it as a headline over-states evidence.  
Fix  1) Choose one clearly justified bounce prior and one competitor prior, give THAT Bayes factor in the abstract and conclusions.  2) Relegate the envelope to a sensitivity appendix.

P2-E3  §II C, p.4  
Problem  The ϵ-correction coefficient κ1 is treated as 5.6–80 “order-of-magnitude range”, yet the resulting 1-8 % shift of fNL is inserted directly into the significance budget.  No derivation or citation is given for κ1 nor for how the 1–8 % number follows.  
Fix  Supply the analytic expression or numerical evaluation that produces κ1 , propagate it transparently, or treat the correction as an external theory uncertainty (which would weaken the Bayes factor).

P2-E4  §III B, p.6  
Problem  The shape-overlap factor is quoted as r = 0.84 ± 0.02 “across all physically motivated weighting schemes” but the full stated range is 0.829–0.876 (width 0.047, i.e. ±0.024). The uncertainty bar is therefore understated.  
Fix  Quote the actual half-range as the 1 σ dispersion or report the rms; redo any downstream σ multiplication using the corrected error.

P2-E5  §IV, p.7 & Table IV, App.A2  
Problem  The same σ(fNL)=0.70 forecast is used with two incompatible normalisation conventions (c=2 and c=1) without recalculating the Fisher matrix.  Because σ scales ∝1/c, the “halved significance” row is inconsistent: if the amplitude halves the Fisher σ must double.  
Fix  Either derive σ(c=1)=1.4 explicitly or drop the c=1 row.

P2-E6  Whole paper  
Problem  No estimator definition is frozen before simulations.  The local-template KSW-type estimator is chosen after the overlap study.  Requirement #8: primary estimator must be pre-declared.  
Fix  State explicitly at the start of §III that the fiducial estimator is the standard optimal local KSW estimator (give equation).

MAJOR (substantial revision)  
----------------------------------------------------------------  
P2-M1  §II B, p.3  
Under-determined six-coefficient polynomial: the paper treats the 3-D null space by an arbitrary radius-50 Euclidean ball.  Results (r-scatter, significance) depend on that choice.  
Fix  Justify the radius from a physical prior or re-sample with a Jeffreys/flat prior and quote the sensitivity.

P2-M2  §VII B, p.12 & Fig. 5  
bφ marginalisation: the ±20 % prior is taken from nowhere and acknowledged as “optimistic”.  Forecasts must be repeated for at least one literature-based prior (e.g. from Barreira 2022).  

P2-M3  §IV, p.7  
Injection-recovery test uses full-sky, isotropic Gaussian noise; real SPHEREx has fsky≈0.7 and a complex mask.  This biases rmeas upward.  
Fix  Repeat the test with the public SPHEREx mask or add the 1/√fsky factor to σ(fNL).

P2-M4  §II C, assumptions list  
Assumption (d) “faithful cubic-order transfer” is unverified; yet forecast claims are expressed as if unconditional.  
Fix  State explicitly in the abstract and conclusion that all numbers are conditional on cubic transfer holding.

P2-M5  §VI C  
The three 105-realisation ensembles are said to “validate” the analytic Bayes factor but the MC procedure is not described (proposal distribution, convergence test).  
Fix  Provide algorithmic details or move the statement to a disclaimer.

MINOR (should be addressed)  
----------------------------------------------------------------  
P2-m1  Abstract line 8  
|fNLbounce|/|fNLinf|≈290 : the exact ratio 4.375/0.015 = 291.7; 290 ok as rough but quote 292 or give “≈292”.  
P2-m2  §III A eq.(4)  Missing factor a(η) in M(k,z) or else define normalisation.  
P2-m3  Many places  “optimistic 5.2–5.5 σ” → one number would suffice; the range arises only from r variation already quoted.  
P2-m4  Duplicated phrase “idealized Fisher” appears three times in §IV; tighten.  
P2-m5  Typo p.5 “phase3 fisher overlap.json” (internal filename).  
P2-m6  Table III heading “GR Treatment” – last row labelled “sanity row” is non-scientific language.  
P2-m7  Several longs dashes “—” appear as “-”; use a single style.  

NIT (cosmetic)  
----------------------------------------------------------------  
P2-n1  Eq.(9) uses prime both for derivative and constant; clarify symbol.  
P2-n2  Footnote marker “3 2” in text mis-typeset.  
P2-n3  “sub-eV/super-Planck-coupled” needs clarification.  

----------------------------------------------------------------  
## Summary recommendation  

MAJOR REVISIONS  

The manuscript contains many useful cross-checks but presently mixes rigorously derived Fisher errors with heuristic, non-covariant degradations, and advertises a prior-dominated Bayes-factor envelope as headline evidence.  A full, self-consistent error propagation (or a clearly partitioned presentation) and a single justified prior choice are required before the claimed 3–5 σ discrimination can be considered reliable.