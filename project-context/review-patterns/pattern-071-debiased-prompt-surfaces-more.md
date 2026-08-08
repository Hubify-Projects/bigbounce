# Pattern 071 — De-biased referee prompt surfaces more findings (feature, not bug)

**Class:** review-instrument-calibration
**First observed:** EXT RS5 (2026-07-01)

## Observation
Replacing severity-steered referee prompts with a strictly de-biased, high-bar
prompt (no hint of desired outcome; "review to the standard of a real PRD
submission") raises the raw MAJOR/reject count sharply (RS5 vs prior rounds:
the verdict-trend chart shows the jump). This is CORRECT behavior — the stricter
instrument finds more — but it makes raw verdict counts misleading.

## Consequence / required companion
A de-biased prompt is only safe when paired with a source-cited truth-audit +
cross-vendor weighting (pattern-070). Without the audit, the higher raw counts
would either (a) trigger fake-accepts to escape them, or (b) cause thrashing on
phantom findings. WITH the audit, the de-biased prompt is a net upgrade: real
issues surface, noise is filtered, and the integrity audit (Lesson F) confirms
no severity-steering crept back in.

## Moat implication
The durable asset is not any single prompt — it is the INSTRUMENT + AUDIT
pipeline: de-biased elicitation → cross-vendor agreement → source-cited verdict →
signposted closure → integrity check. Each layer is an accumulated learning; the
pipeline as a whole is what turns noisy referee output into honest convergence.
