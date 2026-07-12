# P4 M2/M2b truth-audit — 2026-07-12T18:21:21Z

Paper: P4 (chirality catalog), v1.0.238 — FIRST external reads WITH the e2e
image-level injection integration (DP4-15 close). Raws READ verbatim: Grok M2
(VERDICT: MINOR REVISIONS, raw l.1); ChatGPT M2b (VERDICT: REJECT, raw l.1).

## e2e-ENGAGEMENT CHECK (task-required)
Grok M2: does NOT engage the new 8.47M e2e section — MINOR-only, presentation/
cross-check strengthen-requests (DP4-01/07/13/16).
ChatGPT M2b: DOES engage it — MAJOR #1 (raw l.25):
> "the injection begins in the final hard-label map, downstream of the image
> classifier, not-spiral triage, confidence cut, and spatially varying confusion
> matrix. Thus these numbers are neither controlled-false-alarm thresholds nor
> end-to-end sensitivities to a physical chirality dipole"
→ It READ the v1.0.238 e2e run and re-frames it: argues the injection point is still
downstream of the image classifier. This is the standing DP4-15/e2e disposition
class (the paper discloses the injection convention + A50/A95 as estimator-level,
not end-to-end-from-pixels; §VI B). RE-FLAG, not genuinely-new. The abstract's
"8,474,531 galaxies" 8.47M headline is only touched as a title-framing MINOR
(raw l.111), not a substantive new finding.

## ChatGPT M2b — REJECT (13 MAJOR + 2 MINOR; ledger_match 15/15)
All map to standing DP4: A50/A95 non-Gaussian + e2e (DP4-15), z≃−7.6 attenuation
(DP4-08), pre-reg/0.6-cut (DP4-09), pixel-permutation exchangeability (DP4-07),
D4-vs-Z2 21.4% hard-label rotation (DP4-14), GZ1 4.5-6.8% sensitivity (DP4-16),
diagnostic-vs-primary 47% residual (DP4-12), moment-z σ language (DP4-01),
nuisance/rank-deficient WLS (DP4-19), sign-definite systematic (DP4-21), Shamir
comparison (DP4-17), parity-even ℓ=1 physics (DP4-20).
### mask-count MAJOR (raw l.95) — RE-FLAG/misread, NOT genuinely-new
"3,200,420 in-mask + 740 outside vs Table XVI 3,201,160 all in-mask." Current tex
L950 EXPLICITLY reconciles: "all 3,200,420 in-mask ... the remaining 740 of the
catalog's 3,201,160 spirals lie in pixels below the N≥10 canonical-mask threshold"
→ 3,200,420+740=3,201,160. Self-consistent in-text; ChatGPT misreads Table XVI's
total as "all in-mask." Standing DP4 reproducibility-bookkeeping disposition.

## Grok M2 — MINOR (4 MINOR; ledger_match 4/4 → all RE-FLAG-DISCLOSED)
DP4-01 (template-disfavor qualifier), DP4-12 (53% forward-model residual),
DP4-16 (GZ1 coarse sensitivity), DP4-14 (D4 TTA subsample). Grok trend = SOFTENING
(MINOR-only), central claim "supported by the primary real-space HC estimator."

## FINAL COUNT
Genuinely-new real editable findings: **0**. ChatGPT holds its harsh-referee REJECT
floor (directive H) on honestly-disclosed content incl. the newly-integrated e2e;
every finding = source-cited standing DP4 re-flag. No broken refs, no orphans.

## Streak
0 genuinely-new → **streak 6 → 7** (directive-J clean-wave increment).

## Integrity
Both raws READ verbatim. e2e MAJOR quoted verbatim + checked against §VI B. mask
reconciliation checked against tex L950 (not filename). No ACCEPT faked, no math
fabricated, no dismissal without a source-cited DP4 verdict.
