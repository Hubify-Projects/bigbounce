# Hubify canonical-lab reconciliation gap — 2026-08-26

## What agrees

The BigBounce source projection and Hubify registry agree on the six pinned program identities, versions, PDF paths, and the unified science snapshot `d957c0cd`. Their level-3 claim remains explicitly narrow: P1B's lightweight NaMaster smoke test, not full reproduction of every research program.

## What does not agree

Credential-less Hubify Lab metadata for live slug `bigbounce` reports **5 experiments, 2 papers, and 3 surveys**. That cannot represent the current BigBounce source contract, which carries 52 experiment manifests and six program identities. Three reproduced BigBounce labs are present but are Level-0 shells (0 experiments, 0 papers, 0 surveys).

This is a live product-data/projection gap, not evidence that the scientific source is wrong. The source/registry parity tests prove the transport package; they do not prove that the authenticated product records were fully seeded.

## Repository consolidation — 2026-08-26

Hubify's active work was consolidated onto `main` and pushed. The recovered input-focus accessibility sweep is represented in `e6c26598` and its historical branch was merged without changing that settled content. All clean stale Claude worktrees and their merged remote branches were removed.

One detached worktree contained **9,721 uncommitted deletions across 49 registry/module files**. It was not merged or discarded. It is preserved for explicit review on `recovery/heuristic-franklin-uncommitted-20260826`; this recovery branch is intentionally the sole exception to the one-active-branch policy and does not alter the canonical lab contract.

## Required safe resolution

1. Obtain authenticated Hubify access and read the canonical `bigbounce` lab records and fork payload.
2. Reconcile or reseed from the pinned source projection without inventing missing experiment/paper records.
3. Fork once into a clean test lab and verify that the fork retains the manifest, paper, survey, and reproducibility-level contract.
4. Only then label BigBounce the canonical forkable Hubify example lab.

No Hubify product rows were mutated during this audit.
