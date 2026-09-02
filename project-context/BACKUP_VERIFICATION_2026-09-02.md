# Lab-wide backup verification — 2026-09-02

Read-only verification against every backup location named in
`project-context/SESSION_HANDOFF_2026-08-05_to_2026-08-28.md` §"Where the scan
corpus lives" and §2. No pushes, no stops, no writes to any remote store.

| Location | Expected | Found | Status | Command |
|---|---|---|---|---|
| GitHub origin (Hubify-Projects/bigbounce) main | tracks local | `origin/main = 821594e0`; local `main = 3c9c3684`; local is 3 commits ahead, origin has 0 unmerged commits | PASS (local ahead, unpushed lane commits — not a data-loss risk) | `git fetch origin main && git rev-parse origin/main` / `git rev-list --count origin/main..main` = 3 |
| GitHub upstream (houstongolden/bigbounce) main | tracks local | `upstream/main = 54057420`; local is 20 commits ahead of upstream; upstream is 1 commit ahead of local (diverged) | PARTIAL — upstream has 1 commit not in local `main` (needs review before any merge/push) | `git fetch upstream main && git rev-parse upstream/main` / `git rev-list --count main..upstream/main` = 1, `git rev-list --count upstream/main..main` = 20 |
| Backblaze B2 `aug-011-clean-rerun/shards/` | 36,634 objects | 36,634 objects, 603,584,753 bytes (0.56 GiB) | PASS | boto3 S3-compatible `list_objects_v2` paginated over `bucket=bigbounce`, prefix `aug-011-clean-rerun/shards/` |
| Backblaze B2 `aug-011-clean-rerun/receipts/` | 36,634 objects | 36,634 objects, 28,008,421 bytes | PASS | same, prefix `aug-011-clean-rerun/receipts/` |
| B2 bucket top-level inventory | — | `analysis1/, analysis4/, aug-011-clean-rerun/, bigbounce/, bounce-portfolio-2026-03-25/, catalogs/, chirality/, data/, desi_dr1_anomaly_catalog/, enhanced_18M/, enhanced_18M_catalog/, external_catalogs/, mcmc/, models/, results/, smith42_shards/, test/` | INFO | `list_objects_v2(Delimiter="/")` |
| HuggingFace `bamfai/bigbounce-aug-011-clean-rerun` (dataset) | `corpus_packed/` tar parts + `PACKED_SHA256SUMS.json`, `phase3/` present | Repo top level: `corpus_packed, phase3, receipts, results_2026-08-07, scan_state, sealed_2026-08-05, shards, .gitattributes`. `corpus_packed/`: 10 tar parts + `PACKED_SHA256SUMS.json` (11 entries, 763,076,319 bytes). `phase3/`: contains `phase3/2026-08-26` | PASS | `HfApi().list_repo_tree(repo_id, repo_type="dataset", recursive=False)` on root, `corpus_packed`, `phase3` |
| HuggingFace `bamfai/galaxy-chirality-v2` | `g1-retrain-2026-07-17/` present at top level | Repo is type **model** (not dataset — 404 on dataset lookup, succeeded as model). Top level: `g1-retrain-2026-07-17, gz1only, .gitattributes, README.md, chirality_model_v2_best.pt, v2_bias_audit.json, v2_calibration.json` | PASS (repo_type is `model`, not `dataset` — note for future scripts) | `HfApi().list_repo_tree("bamfai/galaxy-chirality-v2", repo_type="model")` |
| Local `~/Desktop/CODE_YOU/bigbounce_datasets/aug-011-clean-rerun/` | 36,634 shards + 36,634 receipts | 36,634 shards, 36,634 receipts, 1.5 GiB total. Only subdir of `bigbounce_datasets/` is `aug-011-clean-rerun/` | PASS | `ls shards \| wc -l`; `ls receipts \| wc -l`; `du -sh` |
| Zenodo 21481838 (P1A) | published record | HTTP 200, "Algebraic Cartan Elimination in Minimal Einstein–Cartan–Holst Gravity...", version 1A.0.124, 6 files | PASS | `curl https://zenodo.org/api/records/21481838` |
| Zenodo 21481842 (P1B, namaster-proof main) | published record | HTTP 200, "namaster-proof: Exact pseudo-Cl window inference...", version 2B.0.12, 6 files | PASS | same |
| Zenodo 21481753 (P1B, namaster-proof tool) | published record | HTTP 200, "namaster-proof 0.1.7: Exact NaMaster window operators...", version 0.1.7, 5 files | PASS | same |
| Zenodo 21461881 (P2) | published record | HTTP 200, "The Exact Matter-Contraction Non-Gaussian Amplitude...", version 1.7.125, 6 files | PASS | same |
| Zenodo 21461888 (P3) | published record | HTTP 200, "Public-ID Recovery for a Historical DESI DR1 Anomaly List...", version 3.2.0-r10, 6 files | PASS | same |
| Zenodo 21461899 (P4) | published record | HTTP 200, "An Observed-Label Chirality-Dipole Null in 949,584 High-Confidence DESI Spirals...", version 1.0.268, 6 files | PASS | same |
| Convex `brilliant-panther-471.convex.cloud` | responds, holds all papers | `status: success`, 6 papers: paper-1a, paper-1b, paper-2, paper-3, paper-4, paper-5 (title on paper-4 says "890,069" spirals vs Zenodo record's "949,584" — see Gaps) | PASS (responds; content-consistency gap noted) | `POST /api/query {"path":"papers:list","args":{}}` (confirmed via `grep -n "export const" convex/papers.ts convex/paperVersions.ts`) |
| RunPod | only pod `8ofv5d4ynu7hku` RUNNING | 7 pods total; only `8ofv5d4ynu7hku` (`bigbounce-aug011-phase3`, $0.17/hr) has `desiredStatus: RUNNING`; all others EXITED. Balance: $149.14 | PASS | GraphQL `myself{pods{id name desiredStatus costPerHr}}` and `myself{clientBalance}` to `api.runpod.io/graphql` |

## Gaps

1. **GitHub upstream diverged**: `upstream/main` (houstongolden/bigbounce) has
   1 commit not present in local `main`. Not reviewed/merged as part of this
   verification (read-only, no fetch-merge or push performed). Needs a
   deliberate look before any push to upstream to avoid silently overwriting
   that commit.
2. **Convex paper-4 title/count mismatch**: Convex `papers:list` returns the
   paper-4 title with "890,069" high-confidence DESI spirals, while the live
   Zenodo record (21461899) for the same paper is titled with "949,584."
   Likely a stale Convex title left behind a later count revision — flag for
   the P4 owner-agent to reconcile (not a backup-integrity issue, a
   content-freshness issue).
3. **No P1C row in Convex**: `papers:list` returns 6 papers (P1A/P1B/P2/P3/P4/
   P5); the resurrected P1C no-go survey (still in R-phase per the handoff)
   has no Convex `papers` row yet. Expected given its in-progress state, but
   worth confirming intentional before P1C nears convergence.
4. **No native B2/AWS/rclone CLI installed** on this machine (`b2`, `b2v4`,
   `aws`, `rclone` all absent). Verification used `boto3` against B2's
   S3-compatible endpoint instead — works, but any skill/runbook that assumes
   a `b2` CLI is present will fail here until one is installed.
