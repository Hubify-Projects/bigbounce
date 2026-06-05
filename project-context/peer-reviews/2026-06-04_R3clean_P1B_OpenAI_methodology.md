# P1B 2026-06-04_R3clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 46.4s

---

Referee Report on P1B – “Technical Verification Companion to the ECH Spin-Torsion Program: …”

I have reviewed the manuscript from the standpoint of methodological rigour, statistical validity and internal numerical consistency.  The paper is well–written and considerably shorter than typical PRD catalogue/­methods articles (11 pp), but a number of hard technical problems remain.  All scalar results quoted in the Abstract and Conclusions were traced.  They are internally consistent, with the exceptions flagged below.

FINDINGS  
(ESSENTIAL = show-stopper, MAJOR = large revision, MINOR = small but should be fixed, NIT = cosmetic).

--------------------------------------------------------------------
P1B-E1   Sec. III, p.3–4 – Unphysical prior for ΔNeff  
Problem: The Cobaya YAML evidently uses a flat prior that allows negative
ΔNeff.  The posterior mean “−0.020 ± 0.169” straddles the unphysical
region Neff<0.  Allowing negative values changes the shape and width of
the likelihood‐weighted posterior and all derived H0 and σ8 numbers.  
Required fix: Impose the physically correct prior ΔNeff ≥ 0, rerun the
chains and update every derived scalar (Table I, Fig. 1, Abstract,
Conclusions).

--------------------------------------------------------------------
P1B-E2   Sec. III, p.3 (footnote 1) – Misleading sample-count inflation  
Problem: The text repeatedly quotes “309 189 frozen samples” by simply
adding two independent dataset combinations (176 240 + 132 949).  Those
samples live in different parameter spaces and cannot be pooled for any
statistical purpose.  
Required fix: Report effective post-burn-in ESS for each dataset
combination separately and remove all summed counts from the paper and
the Abstract.

--------------------------------------------------------------------
P1B-E3   Sec. V B, p.6 – Invalid “4.3σ” and “3.6σ” departures  
Problem: The chain never samples the ΛCDM point (w0,wa)=(-1,0).  The
quoted “+4.3σ” and “−3.6σ” significances are extrapolated from the KDE
tails, not from actual posterior samples.  This is not a valid measure
of tension and is presented throughout as hard significance (e.g. “phantom
crossing required”).  
Required fix: (i) Either run a chain that actually traverses the LCDM
point or (ii) remove all σ statements about w0/wa and all language about
“canonical quintom signature” and “phantom crossing required”.  If model
comparison is desired a proper nested-sampling Bayes factor or a
profile-likelihood Δχ² must be provided.

--------------------------------------------------------------------
P1B-E4   Throughout; e.g. p.4 (“fire #25”), p.3 (“gpu_20260305
stale.csv”) – Internal version-history artefacts  
Problem: The manuscript still contains private audit tags, file names,
and development notes.  PRD forbids inclusion of internal change logs in
the body text.  
Required fix: Remove every instance of file-path, internal timestamp,
“fire #…”, “v1A.0.22”, “stale.csv”, etc.  Supply a clean public-facing
provenance statement in an Appendix instead.

--------------------------------------------------------------------
P1B-E5   Abstract & Sec. IV – Mixing incomparable σ scales  
Problem: “20.32σ pipeline-recovery SNR” is quoted next to the published
“2.4–2.9σ sky detection” without a conversion factor; in the Abstract
both appear in one sentence.  These σ’s are on different null models
(MC injection vs. real-sky).  
Required fix: Express the pipeline SNR in plain S/N or give its σ in the
same units as the sky measurement and state this explicitly, or remove
the “20.32σ” language.

--------------------------------------------------------------------
P1B-M1   Sec. III, p.3 – No explicit declaration of the primary
estimator for H0 before looking at the data  
Fix: State in the Methods section that the posterior mean is the
pre-declared point estimator (or if using the MAP, say so).

P1B-M2   Sec. III, p.3 – Incomplete description of the ΔNeff prior  
Fix: Quote the exact Cobaya prior block, including upper bound.

P1B-M3   Sec. III, p.3 – Autocorrelation / ESS not reported  
Fix: Give the integrated ACT or ESS for every parameter.

P1B-M4   Sec. IV, p.5 – Only 500 MC realisations  
For a 0.03° systematic floor, 500 is marginal.  Demonstrate convergence
of the bias estimate or extend to ≥2 000 realisations.

P1B-M5   Sec. VI, p.6 – 25× fine-tuning claim not quantified  
Fix: Show the posterior on θi or a figure of merit quantifying the
fine-tuning.

P1B-M6   p.2–8 – Dimension analysis missing for β formula (αEM term).
Provide explicit rad/deg conversion in the text so readers can verify
the 0.29° number.

P1B-M7   Sec. VI – ALP parameter priors not reproduced  
Fix: Put the prior table now only in Appendix C into the main text or a
proper supplementary table referenced in the body.

--------------------------------------------------------------------
P1B-MINOR findings (representative, not exhaustive)

P1B-m1   Two occurrences of duplicated phrase “published Planck/ACT DR6
2.4–2.9σ” on p.2.  Remove duplication.

P1B-m2   Eqn. (3) uses “αEM × 8 /(4π)” – missing parentheses; insert
“(αEM/4π)×8”.

P1B-m3   Typo: “MC bias table” → “MC-bias table”.

P1B-m4   Please add units to χ² entries in Table II captions.

P1B-m5   Provide DOI for Planck PR4/NPIPE likelihood used.

--------------------------------------------------------------------
NITs

P1B-n1   PACS numbers are obsolete; replace with arXiv primary category
(astro-ph.CO).

P1B-n2   Consistently italicise Neff.

--------------------------------------------------------------------
LENGTH

11 journal pages is appropriate once the internal log material is
removed; no length reduction requested.

--------------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS

Core numerical claims can probably be made sound, but the current draft
uses an unphysical ΔNeff prior, quotes significance levels from an
unsampled tail, mixes SNR scales, inflates sample counts, and still
contains internal development artefacts.  These are correctable without
new physics, but they must be fixed before the paper can be published.