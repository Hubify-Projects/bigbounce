---
pattern_id: 042
status: draft
first_seen: R23conf
papers_observed: [P2, P4]
finding_count: 2 (confirmed recurrences in one round)
proposed_by: r-round-pattern-mine 2026-06-09
---

# Pattern 042 — Hardcoded-literal artifact scripts (DRAFT)

**Severity**: HIGH (the artifact exists, validates, and is cited as proof — but proves nothing).
**Shape**: A "verification" script or reproducibility anchor that ASSERTS literals instead of COMPUTING them. The repo contains an artifact, the paper cites it, the artifact "passes" — but the values it checks were typed in by hand, so the artifact can never disagree with the paper. This is the artifact-layer sibling of pattern-027 (headline claim without on-disk artifact) and pattern-036 (closure fabricates math justification): here the artifact EXISTS but is circular.

## Recurrence evidence (R23conf)

1. **P2 — `appendix_A1_wick_doubling.py` `benchmark_ratios`**: the script's
   benchmark-ratio list was an assigned literal list feeding the assertions,
   not a computation of the in-in operator identity it claimed to verify. The
   0.5000-ratio claim was reframed in the v1.7.46 closure as the −2 Im operator
   identity and the hardcoded literals removed (SSOT paper-2 closure (d)).
2. **P4 — `catalog_c_post_tta_dipole_summary.json`**: assertion-only
   reproducibility anchor — it recorded that the post-TTA dipole check passed
   but contained NO observed/null raw numbers, so nothing in it could be
   recomputed or falsified.

## Mechanical detection rule

For every artifact cited as verification of a "we checked / we verified X" claim:

```bash
# 1. Scripts: flag assigned literal lists/dicts that flow into assert/compare
grep -nE "^[a-z_]+ *= *\[ *[0-9.eE+-]+ *(, *[0-9.eE+-]+)*\]" <script>.py
# then check whether those names appear in assert / np.testing / == comparisons
# 2. JSON anchors: flag anchors with status/pass fields but no raw values
python3 -c "import json,sys; j=json.load(open(sys.argv[1])); \
  print('ASSERTION-ONLY' if not any(isinstance(v,(int,float,list)) and k not in ('status','pass','n') \
  for k,v in j.items()) else 'has raw values')" <anchor>.json
```

Heuristic: a verification artifact must contain at least one number that the
generating code COMPUTED from data (observed value, null value, residual) —
not only numbers that match the paper's printed values by construction.

## Prevention hook

- **Belongs in `/paper-pre-review-check`** (artifact-side gate) and in
  `/artifact-link-verify`: every "we checked/verified X" claim in the .tex must
  point to an artifact containing the COMPUTED values (observed + null + raw
  inputs), never asserted ones. An anchor that only asserts PASS is treated as
  a pattern-027 violation.
- Truth-audit rule: when a reviewer claims a verification script is circular,
  read the script — do not accept "the artifact exists" as a rebuttal.

## Related

- pattern-027 (headline claim without on-disk artifact) — artifact missing; here artifact circular.
- pattern-036 (closure fabricates math justification) — narrative-layer analogue.
- pattern-022 (closure narrative instead of derivation).

## Promotion criteria

≥2 more confirmed firings in later rounds (R24conf+) → promote to confirmed
pattern + add the grep gate to `/paper-pre-review-check`.
