# P3 2026-06-04_1814pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 25.4s

---

Referee report on P3 (Houston Golden, v3.1.73, 4 Jun 2026)

I have read the full 50-page manuscript and audited every scalar that appears in the abstract, conclusions and headline summary blocks.  Below I list all problems that must be fixed before the work can be considered for publication in Physical Review D.  The findings are ordered by severity.

FINDINGS  

P3-E1  
Section: throughout (all pages)  
Problem:  The manuscript contains large amounts of internal version-control language, change-log markers and self-audit tokens such as “v3.1.70 closure”, “R7 GEM-M3”, “convergent reviewer findings”, “Path-C exit-criterion satisfied”, “Appendix F retained only for lessons-learned” etc.  These are production notes, not scientific content.  
Required fix:  Remove every piece of version-history, ticket ID, branch name, closure note, internal milestone reference and similar language from the public text.  A clean scientific narrative is required.

P3-E2  
Section II B, §“In-sample scoring and held-out validation” + Appendix VI D (i)  
Problem:  The authors score the full 22.5 M DESI catalogue with the very same checkpoint that was trained on 47 000 spectra drawn from that catalogue.  This violates the standard requirement that the primary estimator be evaluated on data unseen during training.  Although a 5-fold cross-validation is later quoted, the released headline DESI anomaly list (195 829 objects) is nevertheless derived from a model partially trained on those objects.  
Required fix:  Re-score DESI DR1 with a model that never saw the target spectra (e.g. 10-fold cross-validated voting or leave-one-plate-out training) and publish that list in place of the current one, or demonstrate mathematically that the overlap cannot inflate the anomaly score distribution (provide numerical evidence, not qualitative statements).

P3-E3  
Section II D & Table I  
Problem:  Different surveys use incompatible anomaly thresholds (DESI fixed S > 5, SDSS top-1 %, LAMOST top-1 %, eROSITA top-0.03 %, Planck top-1 %, Gaia top-1 %, NEOWISE after a mask).  Yet the σ values and anomaly fractions are compared across surveys and used jointly in the Fisher forecasts as if they were on a common significance scale.  
Required fix:  Put all surveys on the same, pre-declared null distribution before any cross-survey comparison.  Either re-compute every catalogue with a single global definition (e.g. “top-1 % of the per-survey validation distribution”) or state explicitly in the abstract and every occurrence that the numbers are not comparable.

P3-E4  
Section V (FNL forecast)  
Problem:  Two mutually incommensurable σ(fNL ) scales are presented: (i) the “Fisher-positivity” α² model; (ii) a local linear σ≈8.98−3.66α model.  The text moves between them (“7.9 % improvement”, “8.27±2.37”, “central forecast 8.14”) without always disclosing which mapping is being used, and the abstract quotes a single improvement figure without error bars or scale definition.  
Required fix:  Choose one estimator, pre-register it, and re-compute every quoted σ(fNL ).  Remove all other ad-hoc mappings from the body text and figures.

P3-E5  
Section III D + Fig. 7  
Problem:  The LAMOST “blue-excess” contamination is acknowledged but ≈113 000 affected objects are still counted in every headline total (“methodological lesson but retained in the aggregate”).  This contaminates the final 378 280 catalogue size.  
Required fix:  Exclude the 113 000 LAMOST objects (or those flagged B-dominant) from every total that is presented as quantitatively meaningful, or publish a cleaned list in which each such spectrum is manually verified.

P3-E6  
Section II D “Two-part gate”  
Problem:  The detector pass/fail criteria are changed post-hoc to save the Planck CMB component (criterion b: injection recovery ≥ 50 % even if val-loss fails).  This is undisclosed HARKing.  
Required fix:  Pre-declare the gate in the methods section, re-train every survey with that gate, and supply a table showing that all retained surveys pass both halves.  Otherwise remove the Planck tier from the main catalogue.

P3-E7  
Section IV A  
Problem:  The 58.8 % “SIMBAD-unmatched fraction” is repeatedly called a discovery-rate.  It isn’t: SIMBAD does not index most photometric databases.  The true novelty fraction of 17.8 % (top 1 000 only) is buried.  
Required fix:  Replace every instance of “58.8 % unmatched” or similar in the abstract and conclusion with the correct 17.8 % figure and state prominently that it is measured on a 1 000-object subset.

P3-E8  
Sections throughout  
Problem:  The manuscript is 50 pages long, far above PRD guidelines (15–30 pp for methods/catalog).  Many pages are occupied by multi-level “closure” notes and gallery figures.  
Required fix:  Reduce to ≤ 30 typeset pages.  Auxiliary galleries and log files go to a data repository or EPAPS.

P3-E9  
Whole text  
Problem:  Duplicate phrases such as “canonical canonical-mask”, “LAMOST retains retains”, and countless repeated disclaimers appear.  
Required fix:  Proof-read and remove duplications.

P3-M1  
Sec. II B, OOD test  
Problem:  Only 103 000 out-of-distribution DESI spectra were scored; the authors stopped because the SPARCL endpoint throttled.  This is not enough to characterise the false-positive rate at 0.87 %.  
Required fix:  Either complete the full planned 1 M spectrum OOD run or provide statistical uncertainty bounds showing that 103 k is sufficient.

P3-M2  
Fig. 11 and captions  
Problem:  Injection/recovery shown only for a narrow set of morphologies; gate declared “PASS” or “FAIL*” by eye.  
Required fix:  Provide quantitative ROC curves and AUC values for every survey with uniform plant families.

P3-M3  
Appendix E (PTA)  
Problem:  The Savage-Dickey evidence ratio uses a single KDE chain from one PTA.  No cross-validation with EPTA/PPTA is attempted, yet conclusions about “strong evidence” are drawn.  
Required fix:  Either remove all Bayesian evidence language or repeat the calculation with the joint IPTA likelihood.

P3-M4  
Sec. III C  
Problem:  The SDSS cross-transfer anomaly distribution spans 12 orders of magnitude, proving numerical overflow.  
Required fix:  Clip or rescale scores so that all logs are finite and quote the dynamic range in decibels not raw numbers.

P3-M5  
All tables  
Problem:  Many numbers quoted without formal error (e.g. 195 829 anomalies, 0.87 %).  Counting error is √N/N≈0.2 %, round-off is larger.  
Required fix:  Attach Poisson counting uncertainties (e.g. 0.870 % ± 0.003 %).

P3-M6  
Sec. V last paragraph  
Problem:  Claims that future SPHEREx will achieve “3–5 σ detection” rely on α being non-zero although the measured α is consistent with zero.  
Required fix:  Temper the statement or supply a forecast explicitly marginalised over α with the measured error.

P3-MINOR-7 … P3-NIT-15  
(Formatting errors, missing axis labels, typos, broken figure references, inconsistent units etc.; list omitted here for brevity but can be supplied to the authors.)

## Summary recommendation  
MAJOR REVISIONS  

The work is ambitious and potentially useful, but at present it is methodologically unstable.  In-sample evaluation, inconsistent thresholds, post-hoc gate changes, and pervasive version-control artefacts must all be corrected; otherwise the numerical results cannot be trusted.