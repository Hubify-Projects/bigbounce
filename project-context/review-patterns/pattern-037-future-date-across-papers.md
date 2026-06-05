---
pattern_id: 037
status: active
first_seen: R10v3p1 / autoloop fire 1 cross-paper diff (2026-06-05)
papers_observed: [P1A, P1B, P2, P3, P4, P5]
finding_count: 6 (one per paper, universal)
proposed_by: r-round-pattern-mine 2026-06-05 (auto-detected by tools/v3_autoloop_summary.py)
severity: MINOR-MAJOR (depends on date specifics)
prevention_action: mechanical regex check before every R-round
---

# Pattern 037 — Future-dated submission line in every paper

## Symptom

Every reviewer (and many external reviewers) flags the `\date{June 2026}` (or similar future date) line on the title page. The complaint: a submitted manuscript dated in the future is implausible and reads as fabrication.

Cross-paper occurrence (autoloop R10v3p1, 2026-06-05):
- P1A, P1B, P2, P3, P4, P5 — all 6 papers had a `future_date` finding flagged by at least one reviewer.

## Root cause

`\date{\paperTimestamp}` macro is set to the current notional submission date. When papers are compiled "for submission" but not yet submitted, the date drifts ahead of the actual arXiv post date. External reviewers see this as a flag of submission staging vs actual readiness.

## Detection

```bash
grep -E "\\\\date\{.*20(2[6-9]|[3-9][0-9]).*\}|paperTimestamp.*20(2[6-9]|[3-9][0-9])" \
  <paper.tex>
```

(future date = current year + 1 or beyond; today is 2026-06-05 so flag any `20(26 future months)`/`20(27-)` reference in `\date{}` blocks.)

## Prevention

- Update `\date{}` to actual submission date the day before posting to arXiv.
- Or use `\date{\today}` if the submission target supports it.
- Add a mechanical pre-compile check to `/paper-pre-review-check`: WARN if `\date{}` contains a date in the future; BLOCK if more than 30 days in the future.

## Related
- [[pattern-038-version-history-language]] — internal versioning artifacts
- [[paper-pre-review-check]] — runtime gate
