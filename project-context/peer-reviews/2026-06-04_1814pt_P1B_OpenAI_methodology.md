# P1B 2026-06-04_1814pt — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 32.9s

---

Referee report on HUBIFY-2026-001B (“Technical Verification Companion …”)

I have read the full 12-page manuscript and audited every quantitative claim that appears in the abstract and conclusions.  The paper is a compendium-style “methods appendix” to a broader programme (Paper I(a) etc.).  Most of the descriptive text is careful, but a number of methodological and statistical problems have to be fixed before the material can be cited as a valid technical foundation for the companion papers.

FINDINGS
========
(Each item: ID – Section / page – Problem – Required fix)

ESSENTIAL
---------

P1B-E1   §III, pp.2–3 and Table I  
“full-tension” likelihood stack simultaneously includes  
(i) Pantheon+ SN likelihood (which samples the absolute magnitude MB) and  
(ii) the SH0ES H0 prior expressed through the same MB,  
but no covariance term is supplied.  That double-counts essentially the same distance-ladder information, underestimates σ(H0), and contaminates the quoted ∆Neff posterior.  
Fix: supply the joint covariance between Pantheon+ and SH0ES or drop one of the two likelihoods; recompute all quoted numbers that enter the abstract.

P1B-E2   §IV, p.5  
Pipeline-recovery “SNR = 20.32σ” is printed without definition of the estimator.  It later becomes clear that the standard deviation used is taken from 500 Monte-Carlo realisations, not from an analytic covariance, and that the quoted “σ” is therefore not directly comparable with the 2.4–3.6 σ sky detections.  This is an explicit mixture of incommensurable σ definitions in the same paragraph.  
Fix: give the exact SNR formula, state explicitly that it is the MC σ of β̂rec−βinj, and scrap the “σ” symbol in the abstract unless it is on the same scale as the sky detection σ.

P1B-E3   §VI, pp.6-7  
The field is called a “spectator ALP” over the full prior box θi∈[0.5,2].  At θi≥0.5 the back-reaction fraction Ωa≈m²f_a²θ_i²/H₀²M_pl² is O(1) and the field is no longer a spectator.  Yet those samples are kept when quoting the envelope 0.17°–0.43°.  
Fix: restrict the posterior to θi that satisfy Ωa≪1 or clearly separate “DE-ALP” and “spectator ALP” regimes; recompute the allowed β range and the Caγ interval.

P1B-E4   Throughout (esp. §V)  
Paper repeatedly advertises “model-comparison statistics deferred” but still claims (abstract, conclusions) that ΛCDM+∆Neff is “consistent” while quintom is “preferred”.  Without an evidence value or ∆χ² the claim is unsupported.  
Fix: either (a) provide at least one properly converged nested-sampling run giving ln B or ∆AIC/BIC, or (b) remove every sentence that asserts preference / disfavour between models.

P1B-E5   Abstract, p.1  
States “NaMaster … NOT the physical separation of the cosmic-rotation angle β from the instrumental-miscalibration angle α”.  Yet in §IV the simulation injects only β and sets α=0, so the pipeline has no opportunity to demonstrate the claimed degeneracy handling.  
Fix: either simulate and fit α simultaneously or delete the claim that the pipeline validation says anything about β–α separation.

P1B-E6   Tables II & IV  
No effective sample size (ESS) is given although R̂−1 is <0.01.  With strong parameter degeneracies ESS can be one order of magnitude smaller than N/chain.  
Fix: quote the minimum integrated-autocorrelation ESS for every parameter set and show that it exceeds 250.

MAJOR
-----

P1B-M1   §III, p.4  
The text asserts that the joint posterior H0 = 67.69 ± 1.06 “exhibits the canonical 3.6 σ tension”.  The error bar is itself derived after the double-count noted in E1, so the tension figure is presently unreliable.  Must be recalculated after E1.

P1B-M2   §IV, p.5  
Mask apodisation bias is quoted as 0.032° for β=0.27°, then later as 0.040° at β=0.342°, but the abstract repeats only the first figure.  
Fix: give a single bias curve or state the injection-amplitude dependence and update the abstract number.

P1B-M3   §VI, p.7  
Equation (3) uses αEM/(4π) with αEM taken implicitly at q²=0.  Give the numerical value used (1/137? 1/128?) and propagate its uncertainty into β to show that it is negligible.

P1B-M4   §Data availability, p.10  
Repository tag “paper1b-v1B.0.36” does not yet contain the Cobaya YAML for the DESI DR2 w0wa chain or the NaMaster MC seeds (checked 4 June 2026, 18:14 PT).  
Fix: push the missing artefacts and place the exact git hash in the manuscript.

P1B-M5   Duplicate phrase check  
Found: “canonical canonical-mask” in §IV first paragraph.  
Fix typo.

MINOR
-----

P1B-m1   §III, footnote 1  
Arithmetic: 176,240×0.7=123,368 not 123,368±(“within ±1 %”).  Remove redundant words.

P1B-m2   §III, p.4  
“Boltz­mann” spelled “Boltz­mannn” once.

P1B-m3   Eq.(2)  
The tilde above Δϕ/fa clashes with the preceding prime; typeset with clearer spacing.

NIT
---

P1B-n1   §VII, Table III “Readiness” column mixes % signs with italics; format consistently.

P1B-n2   Random-seed files are text but lack end-of-line at EOF – git warning; add newline.

P1B-n3   Two occurrences of “pre-empt” spelt “preempt” and “pre-empt” – choose one.

Page-length
-----------  
For a pure methods appendix, 12 PRD pages are acceptable, but once the redundant narrative around fNL, quintom etc. is removed (cf. E4) the same content should fit in ≤9 pages.

## Summary recommendation
MAJOR REVISIONS

The manuscript contains several methodological flaws that materially affect the quoted numbers (double-counted SH0ES + Pantheon likelihood; mixture of incommensurate σ definitions; spectator-ALP inconsistency).  These must be repaired and the key numbers recomputed before the paper can serve as a reliable technical reference for the companion set.