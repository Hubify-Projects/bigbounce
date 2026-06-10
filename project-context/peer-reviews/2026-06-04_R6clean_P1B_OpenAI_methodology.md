# P1B 2026-06-04_R6clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 74.3s

---

Referee report on  
“Technical Verification Companion to the ECH Spin-Torsion Program:  
ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”  



FINDINGS  
(ordered by severity)

ESSENTIAL
-----------  
P1B-E1 Sec. III, p. 3 (“earlier reviewer concerns… YAML alias failure”)  
Version–history and referee-dialogue language appears inside the public manuscript. Instructions prohibit inclusion of such artefacts.  
Fix: Delete every sentence that refers to earlier reviewer comments, previous counts, YAML-alias accusations, or other internal editorial history.

P1B-E2 Sec. V & Table II (w0/wa claims)  
You quote “w0 departs by +4.3 σ” and “wa by −3.6 σ” and state that ΛCDM is disfavoured. Those σ’s are pure posterior-tail distances, not a frequentist null-test and not a Bayes-factor. Presently the paper still uses them rhetorically as a model-selection result (“disfavors… canonical quintom signature”).  
Fix: Either (i) remove every claim of preference over ΛCDM or statistical “disfavour” until you have a properly normalised evidence calculation (nested sampling or TI), or (ii) perform that calculation and quote the resulting ln B with estimated numerical accuracy.

P1B-E3 Sec. VI, eq. (3) / footnote 4  
The “spectator-consistent corner” requires θi ≈ 0.1, a 25× fine-tune relative to the scanned prior, but the baseline prediction range 0.17°–0.43° is still advertised as “natural”.  That mixes mutually exclusive priors.  
Fix: Re-compute the β envelope with the same prior volume you call “spectator”, or explicitly split the results: (a) θi < 0.2 spectator subset, (b) θi ≥ 0.2 dark-energy subset.  Quote separate ranges and state which one is used when confronting data.

P1B-E4 Throughout (ΔNeff prior)  
ΔNeff is allowed to be negative without any physical justification (negative radiation energy density).  The negative part of the posterior contributes non-negligibly to the quoted mean (–0.020).  
Fix: Impose the physically allowed prior ΔNeff ≥ 0 or argue explicitly (with citation) why negative values are permitted and how the Boltzmann code is modified to represent them.

P1B-E5 Abstract & Conclusions  
You list “20.32 σ” and “25.71 σ” pipeline-recovery significances in the same paragraph that cites the 2.4–2.9 σ and 3.6 σ sky detections without re-scaling.  That violates the PRD instruction against mixing σ values from incommensurable null-procedures.  
Fix: Remove the σ labels from the Monte-Carlo injection discussion or convert them to an explicit S/N figure with a disclaimer that it is not comparable to sky-measurement σ.

MAJOR
------

P1B-M1 Sec. III, p. 3 (sample-count explanation)  
The arithmetic walk-through of burn-in removal (309 189 → 216 432) is confusing and appears inconsistent with the figure caption (119 617).  Provide one unambiguous table: raw, burn-in cut, effective, per data-set, with the exact thinning factors used by GetDist.

P1B-M2 Table II caption (“mean-of-total χ2 … 0.1-unit rounding artifact”)  
If you report χ2 values they must add exactly.  Re-check the computation and quote every χ2 to the same numerical precision so the reader can reproduce the sum.

P1B-M3 Sec. IV (NaMaster setup)  
The map is degraded from Nside = 2048 to 512 but the 5-arcmin beam is not re-convolved.  At Nside = 512 the pixel window dominates >ℓ ≈ 500; the claimed bias floor 0.032° may therefore be under-estimated.  
Fix: Provide a validation plot of β bias versus ℓmax for at least two resolutions (512 and a control 1024) or convolve the input map with a beam matched to the degraded resolution and re-quote the bias.

P1B-M4 Sec. VI (Caγ prior)  
Only three discrete Caγ values (4, 8, 12) are tested, yet the final statement “required Caγ spans 9–51” is based on a continuous reinterpretation.  
Fix: Either sample Caγ continuously or restrict the conclusion strictly to the tested grid.

P1B-M5 Sec. III (H0 tension wording)  
The text repeatedly says the ∆Neff extension “cannot resolve” the Hubble tension, but no quantitative Δχ2 or Bayes-factor is supplied.  
Fix: Provide the exact posterior predictive tension (e.g. ΔH0/σcomb) and/or the χ2 contribution of the SH0ES likelihood so the reader sees the numerical statement.

MINOR
-----

P1B-m1 Eq. (3) αEM/(4π)=5.8 × 10-4 is quoted without uncertainty.  Give at least three significant digits or the CODATA value.

P1B-m2 Units Degrees and radians are mixed; write every β value once in degrees and once in radians where used inside formulae.

P1B-m3 Typo    “NaMaster’s spin-2 B-mode purification (purify b=True, purify e=False)” → snake-case keyword is purify_b, purify_e in the current public release. Correct for reproducibility.

P1B-m4 Duplicate word Abstract line “…published Planck/ACT DR6 2.4– 2.9σ [2, 3];a the pipeline SNR figures…” – stray “;a”.

P1B-m5 Reference [18] year should be 2025 not 2024 according to arXiv submission.

NIT
----

P1B-n1 Several long dashes are rendered as double hyphens in the PDF (e.g. “pseudo-Cℓ—The”).  Replace with proper en-dash (–).

P1B-n2 Page-wide footnote marks (fn. 4) are too far from call-outs; convert to end-notes or inline.

P1B-n3 Spelling “Ekpyrotic” once written “ekpyrotic” (capitalisation).

P1B-n4 Figure 1 axis label “m” should be “Ωm”.

P1B-n5 PACS numbers obsolete for PRD; drop or replace with Physics Subject Headings if journal requires.

## Summary recommendation  
MAJOR REVISIONS

The submission provides useful technical cross-checks but still contains internal review artefacts, uses posterior-tail “σ” values as if they were model-selection significances, mixes incomparable significance scales, and relies on an ALP prior that is inconsistent with the claimed spectator status.  These issues can be repaired without fundamentally new data, but they must be fixed for methodological rigour before the manuscript can be considered for publication.