---
title: Houston Method v2
type: concept
tags: [method, protocol, quality, completion]
last_updated: 2026-04-04
sources:
  - project-context/houston-method-v2.md
  - project-context/houstons-approach.md
---

# Houston Method v2: Research Completion Protocol

The mandatory completion loop for every experiment, analysis, and pipeline. Nothing is "done" after running a script.

## The 9-Step Loop

```
RUN -> QC -> ANALYZE -> INTERPRET -> CONNECT -> SYNC -> EXPAND -> BACKUP -> COMPLETE
 ^                                                        |
 +--------------------------------------------------------+
 (new tasks from EXPAND feed back into RUN)
```

1. **RUN** -- Execute computation, save raw outputs
2. **QC GATE** -- Automated quality checks (7 mandatory checks). If ANY fails, mark `needs-rerun`
3. **ANALYZE** -- Cross-match top anomalies against SIMBAD/NED/VizieR, classify, compute novelty
4. **INTERPRET** -- What does this mean for bounce cosmology? Does it improve f_NL, test birefringence, constrain quintom?
5. **CONNECT** -- Cross-reference with all other results, update portfolio table
6. **SYNC** -- Update ALL affected website pages within 24 hours
7. **EXPAND** -- Generate 3-10 new tasks from this result (the self-perpetuating engine)
8. **BACKUP** -- Results in 3+ locations before marking complete
9. **COMPLETE** -- Only after steps 1-8 are ALL done

## QC Gate Checks

| Check | Failure Condition |
|-------|------------------|
| Null coordinates | >5% of top anomalies at RA=0.0, Dec=0.0 |
| Training quality | val_loss > 1,000 or no convergence |
| Cluster degeneracy | >80% in a single cluster |
| Score explosion | max(anomaly_score) > 10^6 |
| Spatial concentration | All top 20 within 5 deg radius |
| Empty output | 0 anomalies or empty file |
| NaN/Inf values | Any NaN or Inf in scores/coordinates |

## Anti-Patterns

| What Happened | Why It's Not Complete |
|--------------|---------------------|
| Script finished | Step 1 of 9 |
| Results saved | Step 8 only (no analysis) |
| "COMPLETE" badge added | Badge without QC is a lie |
| Anomaly count reported | Count without classification is meaningless |
| "Null result" | What does it open? (Step 4) |
| No new tasks generated | Think harder (Step 7) |

## Core Principles

1. Never accept "publish the failure"
2. Always do more, not less
3. Optimize for speed and parallelism
4. Back up everything everywhere
5. Push past conservative AI recommendations
6. Bounce-model agnostic
7. Multi-model cross-validation
8. Emotional investment is a feature
9. THE COMPLETION LOOP (this document)

## Connections

- QC results across surveys: [[survey-anomaly-rates]]
- Applied to all entities in wiki/entities/
- Backup protocol documented in `project-context/active_pods_and_pipelines.md`
