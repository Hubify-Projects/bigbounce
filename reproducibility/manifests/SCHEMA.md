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
| `paper` | `P1A` \| `P1B` \| `P2` \| `P3-support` \| `P4` \| `P5` \| `anomaly-flagship` \| `none` \| `A2` \| `A3` \| `P1N` \| `P4P` \| `P2-support` |
| `kind` | `derivation` \| `training` \| `inference-scan` \| `validation` \| `crossmatch` \| `mcmc` \| `analysis` \| `figure-generation` \| `packaging` |
| `inputs[]` | each: `name`, `type` (`external-dataset` \| `internal-artifact` \| `model` \| `external-literature`), `locator` (URL for external — HF/DESI/Zenodo/etc. — or repo path), `checksum` (sha256/md5/revision when known), `license` if external |
| `apis[]` | services called at run time: `name`, `endpoint`, `auth_required` (bool). Empty list = fully offline. |
| `code[]` | each: `path` (repo-relative), `entrypoint` (exact command), `sha256` optional pin |
| `environment` | `python` deps list or requirements path; `hardware` minimum (`cpu-only`, `gpu-24gb`, …) |
| `original_run` | `venue` (`local` \| `runpod`), `gpu` (or null), `pod_id`/host if recorded, `date`, `wall_clock` if recorded, `actual_cost_usd` if recorded — `null` for any value NOT actually evidenced; never invent |
| `reproduction` | the forward-looking estimate: `recommended_venue`, `est_wall_clock`, `est_cost_usd` (0 for local CPU-scale), `parallelizable` (bool), `resume_support` (bool), `notes` |
| `outputs[]` | each: `locator` (repo path or public URL), `type` (`dataset` \| `catalog` \| `model` \| `figure` \| `result-json` \| `receipt` \| `document` \| `log`), `checksum` when fixed |
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

## Schema v1 additive extensions (2026-09-02)

Six new manifests (Track A2/A3, P1N, P4P/P4', P2-support) required three
additive-only enum extensions — `additionalProperties: false` still holds
everywhere, no existing value was removed or renamed:

- `paper` enum gained `A2`, `A3`, `P1N`, `P4P`, `P2-support` for the four new
  portfolio codes surfaced by directive R's ledger-driven science work.
- `inputs[].type` enum gained `external-literature` — a manifest whose input
  is a set of cited published values/equations (not a downloadable dataset,
  not an internal repo artifact) now records that explicitly rather than
  overloading `external-dataset` or dropping the citation.
- `outputs[].type` enum gained `document` (a markdown brief/writeup output,
  e.g. a `_BRIEF_*.md`) and `log` (a raw run-log file, distinct from a
  `receipt`, which implies a verification record).

**Hubify importer note:** `site/src/lib/reproLab.ts::paperSlugForCode`
(referenced by `project-context/HUBIFY_REPRO_IMPORT_SPEC_2026-08-05.md` §`paper`)
does not yet have slug entries for `A2`, `A3`, `P1N`, or `P4P` — manifests
using those codes will import with `paper` set but no linked paper page until
`PAPER_CODE_TO_SLUG` is extended. Tracked as a follow-up, not blocking schema
conformance.

## Current population (directive Q2, first full pass — 2026-08-05)

52 experiment manifests + 3 program manifests, validated 0 errors via
`tools/validate_repro_manifests.py` (structural check; `jsonschema` optional).

**By program:**

| Program | Experiments | runnable-now | needs-data-restore | superseded |
|---|---|---|---|---|
| bounce-theory | 12 | 10 | 1 | 1 |
| galaxy-chirality | 23 | 19 | 3 | 1 |
| anomaly-discovery | 17 | 12 | 5 | 0 |
| **Total** | **52** | **41** | **9** | **2** |

**Open evidence gaps carried over from the inventory (TODOs — not yet closed):**

1. **P1 highz_tracers `clean_rerun` full scan (AUG-011)** — scan-stage venue/cost evidence is closed: 36,634/36,634 shard receipts verified, 45.5h on RunPod A4000, and about $7.74. The open reproducibility gap is retention/access: the full shard and receipt corpus is absent from this checkout, so a fresh remote integrity check and the downstream selected-sample, validation, taxonomy, and manuscript stages require an authorized corpus source. The completed scan must remain a distinct generation and must never be tuned toward historical counts.
2. **P3 NANOGrav PTA MCMC (`free_spectrum_real_2026-05-01/emcee_freespec.py`)** — 192,000-sample run with a full results JSON and chain file, but no RunPod pod ID, GPU/CPU class, $/hr, or wall-clock anywhere in `pipelines/p3_pta_mcmc/` or the referencing SSOT sections found.
3. **P5 cosmic-web / DESIVAST + r24conf "pod session" scripts (`24_r24conf_pod_session.py`, `36_desivast_native_selection_control.py`, etc.)** — script names imply RunPod use but no pod ID, GPU class, cost, or runtime was found in `pipelines/p5_desi_chirality/` or in the reachable sections of `paper-5/status.md`.
4. **P3 multi-survey raw per-survey outputs (`pipelines/h200_results/pod_backup_20260408_full/…`, `pod1_namaster_umap_2026-04-29/`, and ~28 sibling `h200_results/` subdirectories)** — dozens of historical H200-pod artifact directories exist with result JSONs but essentially no accompanying $/hr or wall-clock manifest; venue is inferable only from directory naming convention ("h200_results"), not from a receipt.
5. **P4 empirical b/a DR8 morphology cross-match** (`edge_on_contamination_metric.json`) — status.md states it ran on "a spot A4000 that is now EXITED" with no dollar figure or duration recorded, and the NOIRLab Astro Data Lab TAP query parameters (the external API call itself) aren't captured as a standalone provenance artifact.

**Path corrections made during population** (inventory cited a path that didn't exist; corrected and noted in the affected manifest's `provenance[]`):

- `p1a-ntot-sensitivity-mc`: inventory cited `research/sensitivity_scan/` (does not exist); actual script is `research/theory_audit/vacuum_scale_sensitivity_scan.py`.
- `p4-gz1only-retrain-dipole-null`: inventory cited `train_chirality_gz1only.py` (not preserved anywhere in the repo); nearest surviving scripts are `pipelines/p2_chirality/run_dipole_gz1only_fullN.py` and `pipelines/p2_chirality/scripts/gz1_stratified_confusion.py` — status set to `needs-data-restore`.
- `p3-erosita-scaler-leakage-control`: no script generating `erosita_scaler_refit.json` was found via grep across `pipelines/p3_anomaly_engine/`; only the result JSON survives — status set to `needs-data-restore`.
- `p3-umap-multiseed-stability`: no `.py` script exists under `pipelines/h200_results/pod1_namaster_umap_2026-04-29/`, only the results JSON — status set to `needs-data-restore`.
- `p5-systematics-analysis` / `p5-cosmic-web-desivast-void`: the inventory's "scripts 05-09" bundle actually maps to `05_analysis_redshift.py`, `06_analysis_density.py`, `07_analysis_healpix.py`, `09_systematics.py` — script `08` is `08_analysis_cosmic_web.py`, which belongs to the cosmic-web/DESIVAST experiment, not the redshift/density/HEALPix/systematics quartet.
- `p3-nanograv-pta-mcmc`: **content correction, not just a path fix.** The inventory's cited headline numbers (gamma=3.20+/-0.42, 192,000 samples, DeltaBIC=7.0) do not match the artifacts actually committed alongside `emcee_freespec.py`. The real committed `results.json`/`savage_dickey_2026-05-29.json` report gamma=2.5665+/-0.3818 on 320,000 samples (32 walkers x 10,000 production steps) with Savage-Dickey Bayes factors, not a Delta-BIC. The inventory's cited figures trace to a different script, `projects/nanograv/nanograv_improved_analysis.py` (outside this manifest's scope), per `project-context/SSOT/paper-3/status.md`'s Wave-14-RR note. The manifest documents the actual committed numbers and flags the discrepancy in `provenance[]`.
