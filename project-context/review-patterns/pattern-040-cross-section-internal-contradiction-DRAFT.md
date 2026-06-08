---
pattern_id: 040
status: draft
first_seen: auto-2026-06-08_1354pt (fire 13)
papers_observed: [P1A, P2, P4]
finding_count: 4
proposed_by: r-round-pattern-mine fire-13 closeout
---

# Pattern 040 — Cross-section internal claim contradiction (meta-reviewer only)

**First seen**: fire 13 (auto-2026-06-08_1354pt) — surfaced by gpt-5-pro meta-reviewer.
**Severity**: HIGH (frequently ESSENTIAL or MAJOR).
**Frequency**: 4 firings across 3 papers in one fire (more under historical re-scan).
**Detection**: META-reviewer flags a claim in section X that directly contradicts a claim in section Y of the same paper. The 5 per-reviewer passes do not see this because they tend to focus on local content, not cross-section coherence.

## Why this pattern is reviewer-class-specific

The 5 per-vendor reviewers (Claude_brutal, Gemini_cosmology, Grok_brutal, OpenAI_methodology, Perplexity_citations) read each PDF section by section and look for local issues. They typically miss inconsistencies between sections that are >5 pages apart, especially when:

- The two sections use different vocabulary for the same concept ("fine-tuning of order 10^-61" vs "without fine-tuning")
- One section makes a quantitative claim and another section's text-only narrative implicitly contradicts it (paper claims "Ω_φ ≪ 1" in spectator framing but the formula `Ω_φ = (1/6)(m/H_0)^2 θ_i^2 ≈ 0.17` is shown elsewhere)
- One section adds an explanation footnote that contradicts what the rest of the section actually does (pseudo-Cℓ = masked; abstract writes "MASTER-deconvolved pseudo-Cℓ")
- A closure footnote justifies a deferred rerun with a logical claim that doesn't hold ("decoupling absorbs trial-count for a pre-MASTER statistic")

The gpt-5-pro meta-reviewer reads the WHOLE PDF + all 5 reviewer reports and is structured to look for "what the 5 prior reviewers missed". It systematically catches cross-section incoherence.

## Examples observed in fire 13

1. **P1A-META-M2** — Sec.IV.D calls m_θ~H_0 "precisely the cosmological-constant problem in disguise" and "a dimensionful tuning of order 10^-61"; Sec.XII says "without fine-tuning". Direct contradiction.
2. **P2-META-E2** — Discussion calls ALP a "spectator field"; energy-density formula on the SAME inputs gives Ω_φ ≈ 0.17 (not a spectator).
3. **P4-META-E2** — Abstract writes "MASTER-deconvolved single-mode pseudo-C_1 yields −0.122σ"; pseudo-C_ℓ by definition means masked NOT deconvolved.
4. **P4-META-E3** — §IV.D fn:binomial_nspiral footnote claims "mode-coupling decoupling absorbs the trial-count normalization for the headline pre-MASTER reproduction figure". Decoupling is POST-MASTER; cannot affect a pre-MASTER statistic.

## Detection rule (mechanical)

There is no fully-mechanical detection — that's why this pattern requires the META-reviewer. But two semi-mechanical pre-flight checks reduce the frequency:

1. **Pre-commit**: every section bump that adds a quantitative claim (β, Ω, σ, ratios) auto-runs a grep across the whole .tex for opposite-polarity claims using the same key variable (`without fine-tuning`, `spectator`, `pseudo-Cℓ`, `decoupling absorbs`, etc.). If both polarities exist, surface for author review.
2. **Pre-bump**: a small LLM pass that reads the SECTION ABSTRACT of each \section{} and checks for cross-section coherence against the introduction's stated scope.

Until these are built, the META-reviewer is the canonical detector. Standing rule for the autoloop:

> Every fire's META findings MUST be content-audited for cross-section contradictions, NOT just keyword-fingerprinted. The persistence_tracker's fingerprint-by-keyword approach will systematically MISS this pattern because contradictions reuse the existing keywords of the contradicted claim.

## Reviewer-time cost

Each instance costs ~30min to ~1h to fix (text rewrites). But the cost of NOT catching them is much higher: a paper that ships with `Holst → Pontryagin` as a mathematical claim, or with "spectator field with Ω_φ = 0.17", will be rejected at journal review with embarrassment. The autoloop is the FIRST process in the workflow to catch these — internal reviews, the per-vendor cross-reviewers, and CCAI did not.

## Promotion-to-prevention plan

Per `feedback_review_learning_loop`:
- **2 more firings** across additional papers → promote to `/paper-pre-review-check` as a structured prompt for the meta-reviewer ("explicitly enumerate all cross-section contradictions").
- **6+ firings + ≥80% verdict consistency** → promote to a dedicated `/cross-section-coherence-check` skill that runs pre-bump.

## Related

- `/peer-review-truth-audit` — should AUTO-PROMOTE any META finding flagged as cross-section contradiction (this pattern) to ESSENTIAL tier even if the per-vendor reviewers downgrade it.
- `feedback_review_learning_loop` — parent directive.
- `AUTOLOOP_IMPROVEMENTS.md` 2026-06-08 14:00pt entry — explains why the persistence_tracker missed this entire pattern.
