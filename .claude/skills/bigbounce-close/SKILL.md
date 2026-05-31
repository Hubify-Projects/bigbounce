---
name: bigbounce-close
description: Atomically close a Bigbounce R-round finding or §pathc_caveats item via the bigbounce MCP. Enforces the closureStatus enum (closed-by-real-action / closed-by-truth-audit-falsification / closed-by-artifact-verification / deferred-genuine) and REQUIRES a closure artifact path + git commit SHA for real-action closures. Site re-renders on Convex subscription within seconds — no more hand-editing papers.ts + live-status.ts + SSOT + .tex comment block + per-page focusAreas.
---

# /bigbounce-close <findingId-or-caveat> <method>

Single mutation, single commit, single re-render. Replaces the previous 4-7-file-edit dance.

## Usage

```
# Close an R-round finding by real action
/bigbounce-close finding:k57z8h2 real-action --commit=e12a1e56 --artifact=pipelines/p3_pta_mcmc/savage_dickey_2026-05-29.json --note="B_mb/SMBHB = 7138 decisive"

# Close a §pathc_caveats item by truth-audit falsification
/bigbounce-close caveat:paper-3/h truth-audit-falsified --note="Table I caption already had the disclosure; reviewer misread"

# Close by artifact verification (existing on-disk artifact already proves the closure)
/bigbounce-close caveat:paper-3/g artifact-verified --artifact=pipelines/p3_anomaly_engine/pathc_desi_kfold/results/kfold_stability_summary.json --note="full-pool scoring convention confirmed"
```

## Anti-pattern guard

`text-only-no-real-action` closure method is permitted but PRINTS A WARNING and requires explicit `--anti-pattern-ack` flag. Houston 2026-05-29: "simply disclosing deferred items and caveats IS NOT REAL SCIENCE." Prefer real-computation / artifact-verification / truth-audit-falsification.

## Behavior

1. Validate findingId / caveat label exists + is in open or in-progress state.
2. If finding: enforce that `truthAuditVerdict` is set first. If not, prompt to run `/bigbounce-truth-audit` first.
3. Call the corresponding Convex mutation (`findings.close` or `pathcCaveats.close`).
4. Print confirmation + the resulting computed-readiness delta for the affected paper.
