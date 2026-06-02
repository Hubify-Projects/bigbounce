# Pattern 015 — Gemini billing-failure skip (vendor-side, not paper-side silence)

**First seen**: P1A R-multi-true95 (Gemini-2.5-pro / 3.x FAILED on billing/auth)
**Severity**: informational (vendor outage, not paper signal)
**Frequency**: 19 (every single round from R1 through R8 across all 6 papers;
NEVER successfully fired)
**Detection**: Gemini-2.5-pro / 3.x returns `403 PERMISSION_DENIED` or
"Lightning dunning decision is deny" in <2s.
**Prevention**: track Gemini status separately from convergent-silence;
3-of-4 non-Anthropic vendors is acceptable when Gemini is vendor-blocked.

## What it looks like

> Vendor status table:
> | Google | gemini-2.5-pro | cosmology | FAILED (vendor billing; 403
> PERMISSION_DENIED in 0.9s)

> Round verdict: 3 of 4 attempted vendors returned. Sufficient signal for
> closure under the cross-vendor protocol (3 functioning vendors converging
> is the truth-audit minimum).

## Truth-audit verdict

Vendor-side billing failure. NOT a finding; NOT paper-side silence. Don't
count Gemini-skip toward convergent-silence in either direction.

## Examples observed

Every single round 1-8 across P1A/P1B/P2/P3/P4/P5: Gemini failed billing
authentication. Houston's standing protocol (per
`feedback_no_openrouter_excuse` + `feedback_peer_review_truth_audit_protocol`):

> 3-of-4 is acceptable when the absent vendor's past 10 rounds have been
> convergent-silent or polish-tier on this paper.

P1A Gemini history pre-true95: 0 BLOCKERs across 10 prior rounds (R23 etc.),
so Gemini-skip in true95+ rounds doesn't change the verdict.

## Root cause

The Google Lightning billing/dunning system rejected the project's API key
across all rounds. Houston was aware; the standing direction is to NOT
treat Gemini-skip as a blocker (per `feedback_no_openrouter_excuse` —
don't lean on OpenRouter cap; same principle for Gemini billing).

## Pre-review check

For each R-round:

1. Attempt all 4 non-Anthropic vendors (OpenAI/Google/Grok/Perplexity) via
   direct vendor SDKs.
2. If Gemini fails on auth/billing in <2s, log "Gemini-billing-skip" but
   **do not block the round**. 3-of-4 vendors is sufficient if the other 3
   returned.
3. Track the skip in the round's vendor-status table for audit transparency.
4. **Do NOT auto-retry Gemini** in the same round; the billing block
   persists until Houston reconciles.
5. The cascaded-loop exit criterion (`feedback_99_pct_readiness_cap`) treats
   "3+ of 5 vendors convergent-silent" — when Gemini is vendor-blocked, that
   reduces to "3+ of 4 vendors convergent-silent" with documented Gemini
   skip.

If Gemini ever returns successfully on a future round (billing reconciled),
flag the recovered vendor as "rejoined" and verify its first-round output
against the cumulative-silence claim.
