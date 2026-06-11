---
pattern_id: 046
status: active
first_seen: EXT1 (2026-06-10, first automated browser-tier external round)
papers_observed: [P1A, P1B, P2, P3, P4, P5]
proposed_by: EXT1 gap-mine 2026-06-10
---

# pattern-046: artifact-paper-cross-check

**Description**: On-disk artifacts (JSON summaries, convergence reports, frozen bundles) contradict paper numbers, units, or versions

**Evidence (EXT1)**: P1B F1 (Cobaya-normalised units read as physical), P1B F2 (burn-in 20% vs 30%), P4 F1 (commit hash 5 versions stale), P4 F5 (bootstrap mask description mismatch), P1A F6 (repro bundle v0.9.0 label)

**Prevention**: Internal rounds audit .tex only; nobody opens the artifacts a journal referee will download. Mechanical rule — run tools/artifact_crosscheck.py every round; for each artifact cited in Data Availability, verify existence + version label + units doc + headline-number consistency.
