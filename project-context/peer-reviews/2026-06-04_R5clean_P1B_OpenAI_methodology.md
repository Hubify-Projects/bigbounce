# P1B 2026-06-04_R5clean — Physical Review D methodology referee

**Model**: `o3-2025-04-16`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 32.9s

---

# Referee report on P1B (Round 2026-06-04_R5clean)  
Methodology / statistical-rigour review – Physical Review D  

I read the manuscript, all tables and the three code/analysis appendices.  
Below I list every problem I found, classified according to the editorial instructions.

----------------------------------------------------------------
FINDINGS
----------------------------------------------------------------

ESSENTIAL = the paper cannot be accepted until fixed  
MAJOR     = substantive revision required, but not fatal  
MINOR     = should be addressed; editor may waive if time–critical  
NIT       = purely cosmetic

----------------------------------------------------------------
ESSENTIAL
----------------------------------------------------------------

P1B-E1  (Sec. V, pp. 6-7; Table II)  
Problem – “w0 departs by +4.3 σ and wa by −3.6 σ … phantom crossing required … the chain therefore disfavors ΛCDM.”  
Those “σ” values are differences expressed in units of the **posterior** standard deviation, while the ΛCDM point is **unsampled** by the chain (posterior density ≈0).  That is *not* a frequentist detection, nor a Bayes-factor model preference.  Presenting them as a “disfavouring” and quoting “σ” unqualified is statistically misleading.  
Fix – Either (i) provide a proper model comparison (nested-sampling or TI ln B with identical likelihood stack) **and** drop the σ language, or (ii) delete every statement that the chain “disfavors”, “rejects”, or “requires phantom crossing”, and instead state only the posterior means and 1-σ credible intervals.

P1B-E2  (Sec. IV, p. 5, ¶ “Independent verification”)  
Problem – SNR figures “20.32 σ”, “25.71 σ” are quoted for Monte-Carlo *injections* and later juxtaposed to the 2.4–2.9 σ Planck/ACT sky detections.  The two σ‐scales are incommensurable (null-sky vs MC-validation).  
Fix – Remove the σ notation for the MC validation, or explicitly label them “MC-only, not comparable with sky σ”.  A hard editorial instruction (Pt. 7) forbids mixing un-comparable σ values.

P1B-E3  (whole text, many places, e.g. Abstract line 5; Sec. III fn. 1; Appendix A)  
Problem – The manuscript still contains internal version-control tokens and review-log artefacts:  
“paper1b-v1B.0.36”, “v1A.0.22”, “iter2 converged 2026-05-18”, “hUBIFY-2026-00x”, etc.  
Fix – Strip every history tag, code-branch name, date–stamp and “this volume” pointer that is not part of the scientific narrative.  PRD forbids embedding change-log material in the body.

P1B-E4  (Sec. VI, p. 7; footnote 4; Appendix C)  
Problem – The “spectator-consistent” ALP corner (θi ≈ 0.1) is claimed, yet all ALP-MCMC priors are θi ∈ [0.5,2].  The stated consistency therefore uses parameter space **not sampled**.  
Fix – Either extend the prior to include θi ≲ 0.1 and show the posterior, or drop the “spectator-consistent” statement altogether.

----------------------------------------------------------------
MAJOR
----------------------------------------------------------------

P1B-M1  (Sec. III, p. 3-4)  
Problem – The abstract headline “309 189 frozen samples” conflates raw samples with post-burn-in counts.  Readers will interpret it as effective MCMC size.  
Fix – Quote **both** raw and post-burn-in (and thinning) numbers everywhere, and report the minimum Effective Sample Size (ESS) as the figure of merit.

P1B-M2  (Table I & Abstract)  
Problem – The two quoted σ8 values (0.803 ± 0.008; 0.812 ± 0.009) are never used later, yet the conclusions mention “σ8 consistent …”.  Readers cannot trace the statement.  
Fix – Add an explicit sentence in the conclusions giving the two σ8 numbers and their provenance.

P1B-M3  (Sec. IV, p. 5, “Pipeline configuration”)  
Problem – No quantitative error propagation on the 0.032°/0.040° bias is given.  The reader cannot judge whether the bias is significant relative to forecasted LiteBIRD σ(β)=0.03°.  
Fix – Provide the standard deviation of the recovered β̂ distribution over the 500 realizations and propagate it to a systematic-floor estimate.

P1B-M4  (Sec. V.A, p. 6)  
Problem – The *exact* likelihood combinations are not stated verbatim.  YAML file names are not sufficient for a methods audience.  
Fix – Insert a one-paragraph bullet list of the likelihood components (Planck LLF names, DESI BAO data vectors, Pantheon+ covariance revision, etc.) in the manuscript body.

P1B-M5  (ALL tables)  
Problem – Units missing for ∆Neff (dimensionless is fine but should be stated), τ, ns, σ8.  
Fix – Append “(dimensionless)” or “unitless” in the column header the first time each scalar appears.

----------------------------------------------------------------
MINOR
----------------------------------------------------------------

P1B-m1  (Sec. II, p. 2, first paragraph)  
“14 historical catalog entries; see Paper I(a) v1A.0.22” – version string is a soft reference, keep a DOI or arXiv number instead.  

P1B-m2  (Table II caption)  
“marg.-tail, +4.3σ” duplicates information already in the body; compress caption.  

P1B-m3  (Sec. VI, Eq. 3)  
The factor αEM/(4π)=5.8×10⁻⁴ is quoted without derivation.  Add one sentence showing 1/137/12.566=5.8×10⁻⁴.  

P1B-m4  Duplicate phrase  
“Not a competitive sky detection” appears verbatim twice in Sec. IV.  Remove one.  

P1B-m5  (Appendix A)  
The reproduction time “4–12 h on 4 CPU cores” is hardware-specific; phrase as “≈ few CPU-hours”.

----------------------------------------------------------------
NIT
----------------------------------------------------------------

P1B-n1  p. 3, footnote 2 – superfluous superscript “√” before MPl/γBI.  
P1B-n2  p. 4, Fig. 1 axis label “Neff” should be “∆Neff”.  
P1B-n3  Eq. 2 spacing: use \dot ϕ not ϕ̇ for uniform style.  
P1B-n4  Missing space before “H0.riess2020Mb” in two places.  
P1B-n5  Last reference [24] – journal issue number missing.

----------------------------------------------------------------
PAGE-COUNT
----------------------------------------------------------------
The paper is 10 pages.  Once version-history and duplicate explanatory text are deleted it will likely be 8 pages, which is appropriate.  No further compression requested.

----------------------------------------------------------------
## Summary recommendation  
MAJOR REVISIONS  

The core numerical work is sound and the authors are commendably careful in many places, but several methodological mis-statements remain.  Most serious are the presentation of Bayesian-posterior shifts as “σ” rejections (E1), the inter-mixing of incomparable σ scales (E2), and the un-sampled parameter region used for the ALP “spectator” claim (E4).  These must be corrected or removed, and the residual major items addressed, before the manuscript can be considered for publication in PRD.