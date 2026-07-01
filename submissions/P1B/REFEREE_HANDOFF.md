# Referee Handoff — P1B (MCMC / NaMaster / ALP Verification Companion)

`arxiv/paper1b_mcmc_companion.tex` · slug `paper-1b`

## Convergence status
P1B has reached the RS11 LLM-refereeing floor: **0 genuinely-new real findings**.
RS11 verdicts — **Grok MAJOR REVISIONS**, **Gemini REJECT**. Both re-flag disclosed content. Gemini's
REJECT rests on (a) the overlap-uncorrected DES-Y5×Pantheon+ SN likelihood — already carried as an explicitly
*exploratory* appendix caveat — and (b) "lack of theoretical novelty," which the paper concedes *by design*
(it is retitled a consistency-check/reproducibility companion, not standalone torsion evidence). The RS10
"σ-overlap" item is a re-flag of caveat (e), not a new defect.

## Recurring objections a human referee should adjudicate

1. **Overlap-uncorrected SN likelihood in the exploratory w0wa appendix (drives the REJECT).**
   - Concern: the DES-Y5 × Pantheon+ product likelihood double-counts ~20% shared SNe, narrowing the Table IV
     posteriors; Gemini: "publishing a flawed treatment even if flagged fails PRD standards."
   - Disclosed: App A / §V.B is explicitly titled "Exploratory w0wa Analysis with Overlap-Uncorrected SN
     Likelihoods"; caveat (e) + `fn:wcaveat` at the headline state the widths are overlap-narrowed and σ-distances
     are PROVISIONAL point estimates with no extractable significance; SN-overlap control chains named as the
     required (out-of-companion-compute) follow-up.
   - Judgment call: **does a clearly-labeled, sign-only, significance-suppressed exploratory diagnostic belong
     in-paper (with the caveat), or should the overlap-uncorrected w0wa appendix be CUT before submission?**
     (This is the single most important editorial decision on P1B.)

2. **Scope-vs-title: companion does not test the torsion sector.**
   - Concern: the paper validates a ΛCDM proxy + synthetic NaMaster pipeline + GR+ALP scans, not the ECH/torsion
     sector; "adjacent cross-check, not independent evidence."
   - Disclosed: retitled to a consistency-check/verification companion (v87); §III states ΔN_eff via stock CAMB
     reflects baseline ΛCDM compatibility and offers zero direct ECH-sector validation.
   - Judgment call: **is a verification/reproducibility companion a standalone PRD article, or supplementary to
     Paper 1A?** (venue/scope)

3. **NaMaster synthetic-sky validation + ALP fine-tuning framing.**
   - Concern: the 500-real NaMaster MC runs on foreground-free synthetic ΛCDM skies, so the −0.040° bias is an
     estimator/deconvolution artifact, not a real-sky systematics-floor comparison; the spectator-ALP check needs
     ~25×/100× tuning.
   - Disclosed: §IV NaMaster scope note flags foreground-free + β–α degeneracy; ALP tuning quantified (25×/100×)
     with cut-dependence reported; Bayes factors honestly deferred to a nested-sampling follow-up.
   - Judgment call: **synthetic-sky pipeline validation + honestly-quantified ALP tuning — sufficient, or does it
     need unrotated-foreground skies / a model-comparison Bayes factor first?** (editorial)

## What is NOT in question
No genuinely-new correctness defect remains. The null/consistency results are truth-audited sound within their
disclosed scope; the contested items are all labeled exploratory or by-design-limited, not hidden errors.

## Recommended venue / next step
Best framed as a **PRD companion / supplementary** to Paper 1A (or an ApJS reproducibility note). The one honest
pre-submission decision worth making deliberately: **cut or keep the overlap-uncorrected w0wa appendix.** Cutting
it removes the entire basis of the Gemini REJECT at zero cost to the paper's core (MCMC-proxy + NaMaster + ALP)
results; keeping it requires the SN-overlap control chains to convert it from exploratory to derived.
