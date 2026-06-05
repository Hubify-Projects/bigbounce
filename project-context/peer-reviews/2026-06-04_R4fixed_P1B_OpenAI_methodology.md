# P1B 2026-06-04_R4fixed — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 31.0s

---

Referee report on P1B – Physical-Review-D methodology audit   
Round: 2026-06-04_R4fixed  

I have read the full 10-page manuscript and inspected the public repository.  
Below I list every methodological or presentation problem I found, classified as requested.  “Sect./p.” refers to the PDF numbering supplied by the authors.  The IDs are unique inside the P1B record.

--------------------------------------------------------------------
FINDINGS
--------------------------------------------------------------------

ESSENTIAL
---------

P1B-E1  Sect. IV p. 5 & Abstract  
Problem  The authors quote “pipeline-recovery SNR = 20.32σ” and “25.71σ” for the NaMaster Monte-Carlo injection in the same σ-notation that is used for the published 2.4–2.9σ sky detections.  Although a disclaimer exists, the identical σ unit implicitly places the numbers on the same perceptual scale, violating PRD policy against mixing incommensurate null models (instructions §7).  
Fix  Replace the “σ” label in all Monte-Carlo/injection contexts by “(SNR)” or an explicit χ2-based Z-score, and add a sentence that these values are not comparable to the sky-measurement significances.

P1B-E2  Sect. III p. 3, Table I  
Problem  The prior on ΔNeff is implicitly flat on (−∞,∞).  A negative ΔNeff is physically meaningless because Neff = 3.046 + ΔNeff must stay ≥0.  Allowing negative values artificially narrows the posterior and the quoted σ.  
Fix  Re-run both frozen chains with the physical prior ΔNeff ≥ −3.046 (or simply Neff ≥ 0) and update every number that propagates from those chains.

P1B-E3  Sect. VI p. 6  
Problem  The ALP “consistency” calculation is used to claim agreement with the 3.6σ birefringence detection, but the uncertainty on the calculated β (eq. 3) is not propagated.  Only a point value 0.29° is given.  Therefore the comparison has no statistical meaning.  
Fix  Propagate the scan priors on Caγ, m/H0 and θi to a proper posterior for β and quote βALP = mean ± σ.  Re-evaluate the consistency statement with that uncertainty.

P1B-E4  Version-history artefacts (multiple occurrences)  
Problem  The body of the paper still contains internal log language: “earlier reviewer concerns”, “v1A.0.22”, “iter2”, “promised a Savage-Dickey ratio”, “queued”.  These are strictly forbidden in the final publication.  
Fix  Remove every piece of version-history, review-log or promise language from the main text and foot-notes.

MAJOR
-----

P1B-M1  Sect. IV p. 5  
Problem  The NaMaster test injects noise at “ACT-noise level ΔP = 10 µK·arcmin” while the real Commander map noise is ≈ 70 µK·arcmin. The de-convolution bias found (0.03–0.04°) is therefore not validated at the noise level relevant for the data set that is later quoted.  
Fix  Repeat the 500 MC realisations with a Planck-equivalent noise level (or a range that brackets it) and report the bias at that level.

P1B-M2  Sect. III p. 2–4  
Problem  The authors characterise the LCDM point as “+4.3σ” and “−3.6σ” excluded, but this distance is read off single-parameter marginals and ignores their covariance.  That presentation over-states the tension.  
Fix  Quote the joint Mahalanobis distance or the equivalent Δχ2 between the best-fit point and the LCDM point, or remove the σ-language altogether.

P1B-M3  Sect. III p. 3, foot-note 1  
Problem  Burn-in removal is applied by a hard 30 % cut across all chains without demonstrating stationarity.  No trace-plots or R̂ evolution are provided.  
Fix  Supply trace plots and an R̂-history figure or justify the 30 % rule with an established convergence metric.

P1B-M4  Sect. V p. 6  
Problem  The paper repeatedly cites “phantom crossing required” but this relies on the w0 + wa posterior mean only; the distribution width (±0.15) still overlaps −1 at the 3σ level.  
Fix  Either remove the categorical wording or provide the full 2-D confidence region showing that w0 + wa = −1 is excluded at ≥ 95 % CL.

MINOR
-----

P1B-m1  Abstract line 5  
Text “full-tension; +0.065 ± 0.17 Planck+BAO+SN” – the two quoted σ values are given to only 2 significant digits while Table I keeps 3.  
Fix  Harmonise significant digits through-out.

P1B-m2  Sect. III p. 2 last paragraph  
Duplicate phrase: “Not a competitive sky detection” appears twice in the same paragraph.  
Fix  Remove duplication.

P1B-m3  Sect. VI p. 6, foot-note 4  
The foot-note attempts a qualitative back-reaction discussion but mixes symbols ρa and Ωa inconsistently.  
Fix  Write the scaling entirely in either Ωa or ρa notation.

P1B-m4  Table II caption  
“the mean-of-total χ2 here is GetDist’s weighted-sample average … which differs … by a 0.1-unit arithmetic-rounding artifact” – the difference is actually 0.1 in the table.  State the exact value (“0.1”) instead of “0.1-unit”.

P1B-m5  Sect. IV p. 5  
Beam description: a 143 GHz 5′ FWHM beam is quoted after downgrading the map to Nside=512 (pixel size 6.9′).  The beam no longer dominates and the effective window function is pixel-limited.  
Fix  Clarify that the beam is subsequently convolved with the pixel window or update the statement.

NIT
----

P1B-n1  Abstract, first line: “Einstein-Cartan-Holst (ECH) spin-torsion cosmology no-go program of Paper I(a)” – “no-go program” is jargon; consider re-phrasing for clarity.  
P1B-n2  Sect. II p. 2: the symbol fsky is used before definition.  
P1B-n3  Several places: put a thin space between numerical value and unit (e.g. “67.68 km s⁻¹ Mpc⁻¹”).  

--------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

While the manuscript is technically elaborate and the numerical work appears largely correct, the four ESSENTIAL defects must be fixed before the paper can enter the PRD archive, and the four MAJOR items materially affect the quantitative conclusions.  Once the statistical definitions are clarified, the MC validation is performed at a realistic noise level, and the internal review artefacts are removed, the work will be suitable for publication.