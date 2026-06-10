# P4 2026-06-04_1814pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 26.7s

---

Referee report on P4 (Houston Golden, “Survey-Scale Galaxy Chirality with Equivariant TTA …”, v1.0.153, 4 Jun 2026)

I have audited the statistical methodology, derivation chains, dimensional units, internal arithmetic, error-propagation logic and the traceability of every scalar quoted in the abstract and conclusions.  The manuscript is longer than a typical PRD methods paper (56 pp vs 15–30 pp) and still contains review-log debris, path names and internal change-log language.

Below I enumerate the concrete problems.  Abbreviations: MC = Monte-Carlo; C1 = ℓ = 1 MASTER-deconvolved band-power; HC = high-confidence subsample; TTA = test-time augmentation.

FINDINGS  

ESSENTIAL  

P4-E1  (Abstract p.1)  
Statement: “σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators”.  In spite of this warning the abstract mixes 0.43 σ (isotropic p-shuffle null), −0.12 σ (MASTER label-shuffle null) and +3.64 σ (binomial null) in a single paragraph without error bars or qualifiers, inviting exactly the forbidden comparison.  
Fix: Every time a σ is quoted the associated null and mask must be restated or the number must be converted to a common scale (e.g. p-value).  The abstract must list p-values instead of sigmas or use a uniform null.

P4-E2  (§IV C p.17, Table VI)  
A factor-of-two slip between “full-amplitude A” and “half-modulation A/2” persists: the 0.14 % “minimum detectable dipole” is calculated on A/2 but is later compared with full-amplitude injections (0.50 %, 0.75 %).  The same confusion propagates into the Fisher floor figure (0.29 % vs 0.20 %).  
Fix: Re-derive the sensitivity floor with a single amplitude convention and correct every occurrence (abstract, §VI C, conclusions, falsification criterion).

P4-E3  (§III E p.8)  
The primary estimator (subsample-mask MASTER) and all secondary estimators were fixed only after “the first round of catalogue results” (v1.0.76).  That is data-dependent estimator selection.  No pre-registration exists.  
Fix:  Either supply an immutable public time-stamp that predates *any* look at the real DESI data, or downgrade every quoted significance to “exploratory” (no claim of frequentist coverage) and rewrite the abstract accordingly.

P4-E4  (§IV D p.21)  
Different MC nulls are averaged together when drawing physical conclusions (monopole-only, label-shuffle, pixel-shuffle).  The +3.64 σ canonical-mask result is directly compared with the −0.12 σ subsample-mask result although the null variances differ by 70 %.  
Fix: Either place all results on a single null scale or forbid all cross–null comparisons; mark the canonical-mask number as “diagnostic only”.

P4-E5  (many sections)  
Raw file-paths, git-hashes, version history and “wave_14_nn”, “p4_multinull_battery.json” etc. remain in the prose – several hundred tokens.  
Fix: Strip every internal artifact from the manuscript.  Provide a separate data-release note if needed.

P4-E6  (§VI D)  
The axis-ratio validation uses DR8 “shapeexp” parameters but those parameters are never documented: unit, cut, photometric band?  No dimensional definition → un-reproducible.  
Fix: Add a Data section explaining every external quantity used in the morphology tests.

P4-E7  (whole paper)  
56 pages is excessive.  At least 20 pages are path listings, JSON dumps and discussion of alternative seeds.  
Fix: cut to ≤ 32 typeset PRD pages.  Place the JSON/path discussion in an online appendix.

MAJOR  

P4-M1  (§III F)  
Four of the eight “bias-hardening” tests are only qualitative (“confidence calibration should look reasonable”).  No quantitative pass criterion.  
Fix: supply numerical thresholds for T3–T8.

P4-M2  (§VI G)  
“Look-elsewhere pLEE ≤ 10−4 ” is quoted from an MC with N = 104, but the analytic Bonferroni correction (≤ 1 σ) is also quoted.  Which one is adopted?  The paper cherry-picks the more dramatic figure in the conclusions.  
Fix: choose one procedure and stick to it.

P4-M3  (§IV C)  
Table VI mixes pre-MASTER pseudo-Cℓ band-powers and post-MASTER single bins.  The reader cannot tell which numbers correspond to which estimator.  
Fix: separate the two estimators.

P4-M4  (§VI C, Table XVI)  
Injection–recovery uses only *positive* injected dipoles.  A method-validity test must use ±A injections to check sign bias.  
Fix: add negative-amplitude injections.

P4-M5  (Sec. IX)  
The “public” catalog is on HuggingFace but no DOI is minted; long-term accessibility not assured.  
Fix: archive the exact release on Zenodo and cite the DOI.

MINOR  

P4-m1  Equation numbering resets (two Eq. 3’s).  
P4-m2  Footnote 9 uses an undefined symbol Neff.  
P4-m3  “Monopole-subtracted” is used inconsistently (sometimes galaxy-weighted, sometimes uniform).  
P4-m4  Many percentages are given with three decimals (over-precision relative to Poisson noise).  
P4-m5  Table captions frequently omit the MC seed that is said to guarantee reproducibility.

NIT  

P4-n1 duplicated phrase “canonical canonical-mask”.  
P4-n2 “ﬁt” spelled “fit” in one place.  
P4-n3 mismatched parentheses in Eq. (8).  
P4-n4 inconsistent spelling “equivarient”.

## Summary recommendation  
MAJOR REVISIONS  

The author has assembled an impressive catalogue and the central methodological point – that a monopole + mask couples into a fake dipole – is valuable.  However, the manuscript in its current form mixes incompatible nulls, changes estimator definitions after looking at the data, mis-states the sensitivity floor, and is cluttered with internal file paths and version logs.  After the essential corrections (E1–E7) and major clean-up (M1–M5) the paper could become publishable.