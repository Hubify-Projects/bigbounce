# Referee Handoff — P1B (MCMC / NaMaster / ALP Reproducibility Companion)

`arxiv/paper1b_mcmc_companion.tex` · slug `paper-1b` · **current version: v1B.0.102 (2026-07-07)**

## Headline result

A coordinated reproducibility / consistency-check companion to Paper 1A. The one original
contribution is a **derived ΔN_eff ~ 1e-43 bound** — i.e. the ECH/torsion sector does not spoil
BBN/CMB (negligible). Supporting analyses: a stock-CAMB ΛCDM consistency proxy (MCMC), a
NaMaster synthetic-sky B-mode validation, and a GR+ALP literature-data accommodation. The paper
is scoped up front as a technical companion that offers **zero direct ECH-sector verification** —
this framing is deliberate and answers the standalone-novelty objection.

The exploratory w0wa (overlap-uncorrected supernova) appendix was **cut** (at v1B.0.95) — it was
orthogonal to the core ECH/torsion + NaMaster + ALP results and was the basis of an earlier
Gemini REJECT; cutting it was zero-cost to the science. Core analyses untouched.

## Convergence status

P1B has reached the LLM-refereeing floor: **0 genuinely-new real findings** across the FINAL
(2026-07-05) and POSTPOLISH (2026-07-06) truth-audited EXT+API rounds
(`project-context/peer-reviews/FINAL_SIGNOFF_AUDIT_2026-07-05.md`). On the identical v1B.0.102
PDF the verdicts span the full range: **grok-4.3 (API) MINOR REVISIONS**; **Grok (EXT) / Gemini
MAJOR REVISIONS**; **ChatGPT REJECT and openai gpt-5.5 MAJOR REVISIONS**. Every REJECT/MAJOR
rests on a **standalone-novelty / venue** judgment or a disclosed limitation — the exact
objection a *companion* framing answers — not a factual error. Grok verifies the ΔN_eff number
independently (1.68e-43, 3 sig-figs) and calls the derivation "the standout original
contribution"; Gemini concedes it is "structurally supported by the analytic first-principles
derivation." No correctness defect survives truth-audit.

> Integrity note (per the 2026-07-04 verifiable-review reset): this paper is **not** dispositioned
> as "CONVERGED / Gemini ACCEPT." The honest current state is a coordinated companion at the
> LLM-refereeing floor with a live standalone-novelty/venue objection from the harshest referees,
> handed to a human referee / cover-letter decision.

## Recurring objections a human referee / cover letter should adjudicate

1. **Scope-vs-venue: is a reproducibility/consistency-check companion a standalone PRD article,
   or supplementary to Paper 1A?** (the dominant objection)
   - Concern: the paper validates a stock-CAMB ΛCDM proxy + synthetic NaMaster pipeline + a
     GR+ALP literature accommodation, not the ECH/torsion sector directly; "adjacent cross-check,
     not independent evidence."
   - Disclosed: retitled and scoped up front as a technical reproducibility / consistency-check
     companion; the abstract's "Scope, stated up front" paragraph and §III both state the analyses
     offer zero direct ECH-sector verification.
   - Options: **(a)** post as a coordinated companion to Paper 1A (current plan,
     `SUBMISSION_NOTE.md` — reciprocal arXiv-ID swap); **(b)** merge the ΔN_eff derivation +
     reproducibility material into P1A as appendices and drop P1B; **(c)** route to a methods venue
     (ApJS reproducibility note). The standalone-novelty REJECT is answered by (a) or (b), not by
     shipping P1B as a standalone PRD physics paper. **This is a pure structure call for the author.**

2. **ΔN_eff derivation rigor.**
   - Concern: the ΔN_eff bound is "only dimensional power-counting; drops sign/spin/flavor structure."
   - Disclosed: the paper labels it a first-principles **order-of-magnitude** estimate. Grok
     (EXT+API): "parametric estimate … standard and sufficient for the order-of-magnitude claim,"
     and independently reproduces 1.68e-43. Disclosed as OOM.

3. **NaMaster synthetic-only validation + ALP consistency-check scope.**
   - Concern: NaMaster validation is on foreground-free synthetic skies only (cannot break the
     β–α degeneracy); the ALP check uses a Gaussian summary likelihood of a single published β.
   - Disclosed: the paper explicitly concedes both ("foregrounds absent by construction"; "the
     author admits this summary approximation omits E/B covariance"). Grok: "explicit statement …
     correct and important" / "balanced and appropriately modest." Disclosed limitations.

## What is NOT in question

No genuinely-new correctness defect remains. With the w0wa appendix cut, the remaining
null/consistency results are truth-audited sound within their disclosed scope: the NaMaster
synthetic-sky validation (foreground-free + β–α degeneracy scope note), the honestly-quantified
ALP tuning (Table IV: 13% posterior mass, ~25×/100× tuning), and the ΔN_eff null-consistency
bound are all labeled by-design-limited, not hidden errors.

## Recommended venue / next step

**Coordinated companion to Paper 1A** (or fold into P1A as appendices). In the cover letter, frame
P1B as a PRD companion / supplementary reproducibility note to Paper 1A, and note the
standalone-novelty MAJOR/REJECT is an addressed venue/scope opinion. The standalone-vs-fold
decision is the single structural call the author must make; no further science work is gated on it.
