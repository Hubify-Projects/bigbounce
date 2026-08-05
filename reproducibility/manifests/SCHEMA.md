# BigBounce reproducibility manifests — schema v1

**Directive Q2 (Houston, 2026-08-05).** Every research program and every
individual experiment/simulation/compute run carries a manifest sufficient for
a stranger (or Hubify) to reproduce it: what data, what code, what compute,
what it costs, how long it takes, and how to verify the result. The
full-reproduction pass is the final pre-publication test of the lab.

Layout:

```
reproducibility/manifests/
  SCHEMA.md                     ← this file
  experiment.schema.json        ← JSON Schema for experiment manifests
  program.schema.json           ← JSON Schema for program manifests
  programs/
    bounce-theory.json
    anomaly-discovery.json
    galaxy-chirality.json
  experiments/
    <experiment-id>.json        ← one per experiment/run
```

## Experiment manifest (`experiment.schema.json`)

One JSON file per discrete experiment, simulation, derivation, training run,
scan, or analysis. Required fields:

| Field | Meaning |
|---|---|
| `manifest_version` | `"bigbounce-experiment/v1"` |
| `id` | stable kebab-case id, e.g. `p4-g1-vit-retrain` |
| `title` | plain-English one-liner |
| `program` | `bounce-theory` \| `anomaly-discovery` \| `galaxy-chirality` \| `lab-infra` |
| `paper` | `P1A` \| `P1B` \| `P2` \| `P3-support` \| `P4` \| `P5` \| `anomaly-flagship` \| `none` |
| `kind` | `derivation` \| `training` \| `inference-scan` \| `validation` \| `crossmatch` \| `mcmc` \| `analysis` \| `figure-generation` \| `packaging` |
| `inputs[]` | each: `name`, `type` (`external-dataset` \| `internal-artifact` \| `model`), `locator` (URL for external — HF/DESI/Zenodo/etc. — or repo path), `checksum` (sha256/md5/revision when known), `license` if external |
| `apis[]` | services called at run time: `name`, `endpoint`, `auth_required` (bool). Empty list = fully offline. |
| `code[]` | each: `path` (repo-relative), `entrypoint` (exact command), `sha256` optional pin |
| `environment` | `python` deps list or requirements path; `hardware` minimum (`cpu-only`, `gpu-24gb`, …) |
| `original_run` | `venue` (`local` \| `runpod`), `gpu` (or null), `pod_id`/host if recorded, `date`, `wall_clock` if recorded, `actual_cost_usd` if recorded — `null` for any value NOT actually evidenced; never invent |
| `reproduction` | the forward-looking estimate: `recommended_venue`, `est_wall_clock`, `est_cost_usd` (0 for local CPU-scale), `parallelizable` (bool), `resume_support` (bool), `notes` |
| `outputs[]` | each: `locator` (repo path or public URL), `type` (`dataset` \| `catalog` \| `model` \| `figure` \| `result-json` \| `receipt`), `checksum` when fixed |
| `verification` | how to confirm a reproduction matches: exact hashes, receipt tooling command, or numeric tolerances (state which) |
| `status` | `runnable-now` \| `needs-data-restore` \| `superseded` |
| `provenance` | pointers into SSOT / status docs / commits backing every claim above |

Rules:

- **Never fabricate** an original-run cost/time/venue: if it wasn't recorded,
  set the field to `null` and put the estimate under `reproduction`.
- Local CPU-scale runs are treated as ~free: `est_cost_usd: 0`.
- `superseded` manifests are kept (they document lineage) but marked so Hubify
  won't offer them as live reproduction targets.
- Every experiment named in a paper's methods/validation must have a manifest
  before that paper's final pre-publication reproduction pass.

## Program manifest (`program.schema.json`)

One per research program:

| Field | Meaning |
|---|---|
| `manifest_version` | `"bigbounce-program/v1"` |
| `id` / `title` | program id + public title |
| `question` | the program's research question (one sentence) |
| `papers[]` | lead + supporting works with roles |
| `experiments[]` | ordered experiment ids (the reproduction DAG: each entry `id` + `depends_on[]`) |
| `external_data[]` | deduplicated union of external sources with links |
| `full_reproduction` | end-to-end estimate: `est_wall_clock`, `est_cost_usd`, `order` notes |
| `hubify` | portability block: `lab_slug`, module mapping notes (kept minimal until the Hubify import contract is pinned) |

## Hubify portability

Manifests are plain JSON with stable ids — the Hubify import maps
`program → lab research program`, `experiment → reproducible run card`, and
uses `reproduction.est_cost_usd`/`est_wall_clock` for the run-cost display.
No Hubify-specific fields beyond the `hubify` block; the lab stays the source
of truth and Hubify consumes it.

## Verification discipline

An experiment counts as REPRODUCED only when its `verification` block passes
on a fresh run (hash-identical outputs, receipt verification, or documented
numeric tolerance). Reproductions get appended to the experiment's
`provenance` — never overwrite the original-run record.
