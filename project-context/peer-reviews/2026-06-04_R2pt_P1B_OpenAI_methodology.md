# P1B 2026-06-04_R2pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 30.2s

---

# Referee report on HUBIFY-2026-001B  (“P1B”)

The remit of this report is limited to methodology and numerical consistency.  I have not judged the theoretical motivation.

--------------------------------------------------------------------
FINDINGS
--------------------------------------------------------------------

ESSENTIAL = must be fixed before acceptance  
MAJOR     = substantial revision requested  
MINOR     = desirable but left to editor’s discretion  
NIT       = trivial

----------------------------------------------------------------------  
ESSENTIAL
----------------------------------------------------------------------  

P1B-E1  
Sec. III, Table I, Fig. 1 (pp. 3–4)  
Problem   
The “Full-tension” chain combines Planck high-ℓ likelihoods with the Riess2020 MB/H0 prior even though those data sets are in > 4 σ tension.  Stock Cobaya assigns full inverse–variance weight to both without a hyper-parameter or evidence–ratio re-weighting, so the posterior width on H0 (± 1.06 km s-1 Mpc-1) is artificially narrow and the ΔNeff error (± 0.17) is underestimated.  These numbers are quoted in the Abstract and Conclusions without warning.  
Required fix  
Either (i) rerun the “Full-tension” chain with a tension-robust combination method (e.g. Bayesian hyper-parameters, shift parameters, or an “H0-free” MB prior), or (ii) drop this chain from all headline numbers and leave only the internally consistent Planck+BAO+SN combination.

P1B-E2  
Sec. V.A (p. 6)  
Problem  
The paper repeatedly interprets departures from (w0, wa)=(-1,0) as “+4.3 σ” and “-3.6 σ” and states that “phantom crossing is required”, yet no *model comparison statistic* is supplied.  A plain Metropolis chain cannot give a Bayes factor when the reference point is unsampled.  The Conclusions nevertheless present these σ-values as evidence against ΛCDM.  
Required fix  
Either supply a valid comparison – nested sampling on the identical likelihood stack or thermodynamic integration – **or** remove every statement that interprets the quoted σ’s as model preference.  A one-dimensional σ on a highly correlated parameter pair is not enough.

P1B-E3  
Sec. IV (p. 5)  
Problem  
The NaMaster bias-injection test finds an amplitude-dependent bias (0.032° at β=0.27°, 0.040° at β=0.342°).  This bias is *not propagated* to any uncertainty budget, yet the paper later quotes ALP posteriors at the 0.01°–0.02° level.  
Required fix  
Include the 0.04° systematic floor in every β error quoted, or clearly label the MC values as *pipeline-only* numbers never combined with sky data.

P1B-E4  
Abstract, Sec. III, footnote 1  
Problem  
“309 189 frozen samples” is given as the total after burn-in, but footnote 1 shows that the figure is *pre* burn-in and that only 216 432 samples remain afterwards.  This scalar is carried into the Conclusions.  
Required fix  
Quote one unambiguous effective sample count (post burn-in, after any thinning) and use that single figure consistently throughout.

P1B-E5  
Several places, e.g. Sec. III (“4π” in denominator), Eq. (3) (p. 7)  
Problem  
In Eq. (3) β is computed with αEM / 4π but then converted directly to degrees without writing the conversion.  Units cancel numerically but the derivation is dimensionally incomplete.  
Required fix  
Write β(rad)=αEM Caγ Δφ/fa and then convert to degrees; include the factor 180/π explicitly to avoid dimensional ambiguity.

----------------------------------------------------------------------  
MAJOR
----------------------------------------------------------------------  

P1B-M1  
Sec. VI, footnote 4 (p. 7)  
The ALP prior θi∈[0.5,2] is called “natural”, yet the paper concedes that spectator status requires θi≈0.1 (25× tuning).  The chain samples the tuned-out region and then claims “natural parameters”.  
Fix: Restrict the prior to the physically allowed spectator range or re-label the result as *non-spectator*.

P1B-M2  
Sec. III (p. 3)  
The ΛCDM+ΔNeff scan does not vary Yp even though CAMB supports BBN consistency with ΔNeff.  Holding Yp fixed biases ΔNeff constraints at the ~0.1 level.  
Fix: enable BBN consistency (Yp varying) or demonstrate that fixing Yp changes ΔNeff by < 0.02.

P1B-M3  
Sec. III, Table II χ² rows  
The χ² numbers are taken as the *mean* over the posterior, not at the maximum-likelihood point, so they cannot be compared with literature goodness-of-fit.  
Fix: report χ² at the best-fit point or remove the comparison.

P1B-M4  
Repository statement (Appendix A)  
Chains are *not* provided; the user must re-run for 4–12 h.  PRD data-policy requires either provision of chains or an explicit reason (size, confidentiality).  
Fix: upload the thinned chains or supply a doi to a long-term archive.

P1B-M5  
Whole paper  
Version-control chatter (“v1B.0.42”, “R12 GEM-M2”, “fire #25”, “Wave 14”) appears in the prose.  
Fix: strip all internal audit tags and version jargon from the submitted manuscript.

----------------------------------------------------------------------  
MINOR
----------------------------------------------------------------------  

P1B-m1  
Sec. III, p. 4 “note that wpivot … is consistent with -1 at −1.1σ so the departure is dominated by wa” – the pivot redshift is not quoted.  
Fix: state zp or remove the sentence.

P1B-m2  
Eq. (4) inverse-variance combination uses the published individual errors but ignores shared calibration systematics already discussed earlier.  
Fix: add a parenthetical reminder that Eq. (4) is for illustration only.

P1B-m3  
Table IV mixes pre-burn-in and post-burn-in sample counts; footnotes mix units (samples vs “accepted”).  
Fix: harmonise notation.

P1B-m4  
Duplicate phrase “canonical quintom signature” occurs three times in two pages.  
Fix repeated phrasing.

P1B-m5  
Spelling: “unsampled-tail problem requires a dedicated nested-sampling run rather then [sic]”.  
Fix typo.

----------------------------------------------------------------------  
NIT
----------------------------------------------------------------------  

P1B-n1  p. 2 “fNL = −35/8” → strictly −4.375, consider giving decimal once.  
P1B-n2  p. 5 “ACT-noise level ΔP=10 µK·arcmin” – the Commander map noise is larger; a sentence of justification would help.  
P1B-n3  Table II footnote (b) “R8 GEM-B3 nit” should be deleted.  
P1B-n4  PACS codes are obsolete; replace with Physics Subject Headings if desired.  

--------------------------------------------------------------------
# Summary recommendation
MAJOR REVISIONS

The submission is close to a usable methodology companion, but the current draft mixes statistically inconsistent data, quotes biased significance statements without the required evidence computation, and omits systematic uncertainties discovered by its own pipeline tests.  These issues must be corrected for the numerical results to be trustworthy.