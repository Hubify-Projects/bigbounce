# Hubify reproducibility-manifest import spec

**Status:** implementation-ready contract, Hubify-side importer not yet built.
**Date:** 2026-08-05. **Owner:** BigBounce lab (source of truth), consumed by
Hubify Labs.
**Source data:** `reproducibility/manifests/` (this repo) — see
`reproducibility/manifests/SCHEMA.md` for the authoritative field definitions;
this document only adds the Hubify-side mapping on top of that schema. Do not
duplicate field semantics here — if the two ever disagree, `SCHEMA.md` wins
and this file is stale and must be corrected.
**Public surface:** `https://bigbounce.hubify.app/reproduce` renders the same
manifests for humans (site/src/app/reproduce/page.tsx, generated from
site/src/data/repro.ts by `site/scripts/sync-repro-manifests.mjs`). This spec
describes the machine-import path into Hubify, which is a separate consumer
of the same JSON — not a dependency of the site page.

---

## 1. Program → Hubify lab research program

Each file in `reproducibility/manifests/programs/*.json` (`manifest_version:
"bigbounce-program/v1"`) maps **1:1** onto a Hubify "lab research program."
There are exactly 3 today: `bounce-theory`, `galaxy-chirality`,
`anomaly-discovery`. A 4th value, `lab-infra`, is a valid `program` enum
member on experiment manifests (for shared/tooling runs not tied to a single
research question) but currently has no `programs/lab-infra.json` file — the
importer must not assume one exists; treat `lab-infra`-tagged experiments as
belonging to a synthetic "lab infrastructure" bucket with no question/papers/
external_data of its own until such a manifest is added.

The program's `hubify` block (`lab_slug`, `module_notes`) is the intended
integration point for anything Hubify-specific; today it only carries
`lab_slug: "bigbounce"` for all three programs (this repo is a single Hubify
lab with three programs, not three labs) plus free-text notes. Do not invent
additional Hubify-specific fields on the BigBounce side — extend the schema
(`program.schema.json`) deliberately if a new field is needed, never infer
one from the importer.

## 2. Experiment → reproducible run card

Each file in `reproducibility/manifests/experiments/*.json`
(`manifest_version: "bigbounce-experiment/v1"`) maps **1:1** onto a Hubify
"reproducible run card." A run card is scoped to one program (via
`experiment.program`) and, where applicable, one paper (via
`experiment.paper`). The card's position in its program's reproduction DAG
comes from the *program* manifest's `experiments[]` array
(`{ id, depends_on[] }`), not from anything on the experiment manifest itself
— the experiment file has no `depends_on` field. The importer must join
`programs/*.json.experiments[]` against `experiments/<id>.json` to get both
the DAG edges and the full card content; an experiment id present in a
program's DAG but missing its own manifest file is an import-time error, not
a silently-skipped row.

## 3. Field-by-field mapping

### Experiment manifest → run card

| BigBounce field (`experiment.schema.json`) | Hubify concept | Notes |
|---|---|---|
| `id` | run card id (stable) | Kebab-case, globally unique across the lab. Use as-is; never re-slug. |
| `title` | run card title | Plain-English one-liner, display as-is. |
| `program` | parent lab research program | Join key into `programs/*.json.id`. |
| `paper` | associated publication (optional) | `"none"` → no publication association. Enum values other than `none` map to a BigBounce paper slug the same way the site does (`site/src/lib/reproLab.ts::paperSlugForCode`; e.g. `P1A` → `paper-1a`, `P3-support` → `paper-3`). `anomaly-flagship` currently has **no** standalone paper page — do not synthesize a link. |
| `kind` | run card category/badge | Direct enum passthrough (`derivation`, `training`, `inference-scan`, `validation`, `crossmatch`, `mcmc`, `analysis`, `figure-generation`, `packaging`). |
| `inputs[]` | run card "sealed inputs" list | `type` distinguishes external-dataset / internal-artifact / model for display grouping. `checksum: null` means "not evidenced," not "no checksum required" — Hubify must render this as an open gap, never hide it. |
| `apis[]` | run card "external services called" list | Empty array is a positive signal ("fully offline") — Hubify should surface "offline / no live API dependency" rather than omitting the section. |
| `code[]` | run card entrypoint(s) | `path` MUST resolve inside the BigBounce repo tree at the pinned commit (see §4); `entrypoint` is the literal command to execute — display verbatim, do not paraphrase or "clean up." |
| `environment` | run card environment requirements | `python` is a free-text deps/requirements pointer (not a lockfile); `hardware` is a coarse tier string (`cpu-only`, `gpu-24gb`, `gpu-a4000-16gb`, …) — treat as informational, not a machine-schedulable spec, until BigBounce formalizes hardware tiers. |
| `original_run` | run card "provenance / actually happened" panel | Any field may be `null` — that is a hard schema rule (`SCHEMA.md`: "never fabricate an original-run cost/time/venue"). Hubify must render `null` as "not recorded," never as `0`, `"unknown"` synthesized text, or an inferred value. |
| `reproduction.recommended_venue` | run card "where to run it" display | Free text today (e.g. `"local"`, `"runpod (A4000-class GPU or CPU-strong instance, ~200GB volume)"`); not a Hubify venue-id yet. |
| `reproduction.est_wall_clock` | run-cost display (time) | Free text, sometimes a range or a qualitative statement ("NOT YET EXECUTED... multi-day estimate pending a real run"). Do not attempt to parse into a numeric duration without re-checking the string; several entries are deliberately non-numeric because no real run exists yet. |
| `reproduction.est_cost_usd` | run-cost display (dollars) | Numeric, `>= 0`. **`0` renders as "free (local)"** — this is the exact rule the site page uses (`formatCost()` in `site/src/lib/reproLab.ts`); Hubify's run-cost widget should match it verbatim so the number never reads as "unpriced" or "$0.00 error." |
| `reproduction.parallelizable` | run card badge/flag | Boolean passthrough. |
| `reproduction.resume_support` | run card badge/flag | Boolean passthrough. |
| `reproduction.notes` | run card expandable detail text | Free text; often carries the honest caveat that makes the estimate meaningful (e.g. "this is a rollup, not a literal sum") — do not truncate this field in a summary view without an expand affordance. |
| `outputs[]` | run card expected-artifacts list | `type` enum (`dataset`, `catalog`, `model`, `figure`, `result-json`, `receipt`) drives icon/grouping; `checksum: null` = not yet fixed, same non-fabrication rule as inputs. |
| `verification` | **acceptance check** | Free-text string: exact hash match, a named receipt-verification command, or a stated numeric tolerance. This is the literal pass/fail criterion Hubify should present to a user attempting the reproduction — "an experiment counts as REPRODUCED only when its verification block passes on a fresh run" (`SCHEMA.md`). Hubify must not infer a machine-checkable test from this string automatically; render it as the acceptance criterion text until/unless a structured `verification` sub-schema is added on the BigBounce side. |
| `status` | **run offerability** | See dedicated mapping below — this is the single field that decides whether Hubify offers the card as a live run. |
| `provenance[]` | run card "evidence trail" links | Repo-relative paths / doc section pointers, not URLs. Render as plain citations (optionally as GitHub-mirror links using the pinned commit, per §4), never as clickable relative links assuming a local checkout. |

### Status → offerability (the field Q2 calls out explicitly)

| `experiment.status` | Hubify run offerability |
|---|---|
| `runnable-now` | **Offerable run.** Hubify may present a "run this" affordance. |
| `needs-data-restore` | **Visible, not runnable.** Show the card (title, DAG position, why it's blocked — usually named in `reproduction.notes` or `provenance[]`) but disable/hide the run affordance. Never silently omit these cards; the lab-level rollup on `/reproduce` counts them explicitly and Hubify's rollup should match. |
| `superseded` | **Visible-but-not-runnable, lineage only.** Same treatment as `needs-data-restore` for offerability, but labeled distinctly ("superseded — kept for lineage") since the reason is "a better experiment replaced this one," not "this one is currently blocked." Per `SCHEMA.md`: "superseded manifests are kept (they document lineage) but marked so Hubify won't offer them as live reproduction targets." |

### Program manifest → lab research program

| BigBounce field (`program.schema.json`) | Hubify concept | Notes |
|---|---|---|
| `id` / `title` | program id / display title | Direct passthrough. |
| `question` | program's one-sentence research question | Direct passthrough, shown as the program's headline on both the site and (presumably) Hubify. |
| `papers[]` | program's associated publications | `role` is free text (`lead`, `support` today) — do not assume a closed enum; display as given. |
| `experiments[]` | the program's reproduction DAG | `{ id, depends_on[] }` per entry. **This array's order is already a valid topological order** of the DAG — the BigBounce site renders experiments in this literal order rather than re-deriving one (`site/src/lib/reproLab.ts::programExperimentsInDagOrder`). Hubify's importer should do the same rather than re-implementing topological sort, unless Hubify's UI needs a different traversal (e.g. a real graph widget), in which case `depends_on[]` is the edge list to build it from. |
| `external_data[]` | program's external-data-source list | Deduplicated union across the program's experiments; `link: "not-publicly-released"` is a real sentinel value (see `bounce-theory`'s SPHEREx covariance entry) meaning "no URL exists," not a broken link — do not render it as a dead hyperlink. |
| `full_reproduction.est_wall_clock` / `.est_cost_usd` | program-level run-cost rollup | **Explicitly a rollup estimate, not a literal sum of the individual experiment `reproduction.est_cost_usd`/`est_wall_clock` values** (stated in-schema and repeated in each program's `full_reproduction.order` text — e.g. galaxy-chirality's is "not a literal sum... several P4 legs are needs-data-restore/superseded and are not part of the live reproduction path"). Hubify must display the program-level number verbatim from this field, never recompute it by summing the child cards, or the two surfaces will silently disagree. |
| `full_reproduction.order` | program-level sequencing narrative | Free text describing execution order/parallelism across the DAG; render as the program's "how to run the whole thing" guidance. |
| `hubify.lab_slug` / `.module_notes` | Hubify-side lab id / integration notes | See §1. |

## 4. Sync direction

**The BigBounce lab repo (`CODE_YOU/bigbounce`, `reproducibility/manifests/`)
is the sole source of truth. Hubify consumes JSON; it never writes back into
this repo, and the importer is one-directional (BigBounce → Hubify).**

This spec inherits an existing, stricter safety constraint already in force
for Hubify↔BigBounce integration (see `project-context/` prior art —
"BigBounce lab isolated repro," 2026-07-23): **platform-side (Hubify)
ingestion and reproduction work must not read or mutate this authoritative
research repo directly.** The established pattern is an isolated,
read-only-over-source reproduction workspace
(`CODE_YOU/bigbounce-lab`, its own git repo) that hashes/mirrors the
publication-critical files at a pinned commit and is what Hubify actually
ingests from. Concretely, for the reproducibility manifests specifically:

1. **Commit pin.** The importer records the exact BigBounce commit SHA the
   manifests were read at (matching every `code[].path` in every experiment
   manifest to a real file at that SHA — a path that doesn't resolve at the
   pinned commit is an import-time error, not a warning).
2. **Read path.** Hubify reads the manifest JSON either (a) from the isolated
   `bigbounce-lab` mirror workspace once that workspace's manifest-mirroring
   is extended to include `reproducibility/manifests/` (it does not yet — as
   of 2026-08-05 that workspace mirrors the 740 publication-critical files
   captured 2026-07-23, predating this manifest population), or (b) from the
   public GitHub mirror (`https://github.com/Hubify-Projects/bigbounce`) at a
   pinned tag/SHA, which is already an existing, safe, read-only surface.
   Direct filesystem access to a live `CODE_YOU/bigbounce` checkout is
   **not** an acceptable Hubify-side read path under the isolated-repro
   safety directive, even though it is technically how the BigBounce site
   itself resolves the data (`site/scripts/sync-repro-manifests.mjs` reads
   `../reproducibility/manifests/` directly, but that script runs *inside*
   this repo's own build, not from Hubify).
3. **No round-trip.** Hubify never edits, annotates, or "corrects" a
   manifest and pushes it back. If Hubify surfaces an evidence gap (e.g. a
   `null` checksum, a missing wall-clock estimate), that observation is
   filed as a BigBounce-side task (this repo's `project-context/tasks.md` /
   SSOT), not written into the manifest by Hubify.
4. **Refresh cadence.** Out of scope for this spec until Hubify names one;
   record it here once decided rather than letting the importer silently
   pick a polling interval.

## 5. Versioning rule

Every manifest file carries a literal `manifest_version` string:
`"bigbounce-program/v1"` or `"bigbounce-experiment/v1"`. **The importer must
gate on this string before parsing anything else:**

- Unknown/missing `manifest_version` → **reject the file**, do not attempt a
  best-effort parse. Log it as an import error naming the file and the
  encountered value.
- Known `manifest_version` whose shape the importer wasn't built for (i.e. a
  future `v2` after the importer only understands `v1`) → **reject**, do not
  silently ignore new/renamed fields. A silent partial-parse of a newer
  schema is how "runnable-now" experiments quietly stop being offered or a
  cost figure goes stale without anyone noticing.
- A schema bump on the BigBounce side (`v1` → `v2`) is a breaking change by
  convention here — `reproducibility/manifests/SCHEMA.md` and
  `*.schema.json` are the source of the new shape, and this import spec must
  be updated in the same BigBounce commit that bumps `manifest_version`
  anywhere, per this repo's `/api-docs-guard` discipline (schema/contract
  changes require doc updates in the same change).
- Mixed-version corpora are expected during a rollout (e.g. some experiment
  files still on `v1` while a program file moves to `v2`): the importer
  processes each file against its own declared version independently; it
  never assumes uniform versioning across the corpus.

## 6. Known unknowns (Hubify-side; honest, not yet closed)

- **AUG-007 — Hubify lab-verification auth gap.** `hubify status` /
  `papers` / `tasks` / `agents` / `activity` currently fail unauthenticated:
  `.env.local` lacks `HUBIFY_TOKEN` although `.env.example` declares it
  (`project-context/tasks.md` AUG-007; `ops/PLAN.md` "Operational
  watchpoint"). This is an external authentication gap, not a blocker for
  BigBounce-side repo/site truth sync, but it **does** block actually
  exercising any Hubify-side importer against a live Hubify instance from
  this machine today. Acquire the token only through an approved secret
  source; never print or infer it.
- **No Hubify-side importer exists yet.** This spec is the contract for one;
  nothing in `hubify status`/CLI output today reflects
  `reproducibility/manifests/` content. Do not represent the `/reproduce`
  page or this spec as "already imported into Hubify" anywhere else in the
  repo.
- **`bigbounce-lab` mirror does not yet cover the manifests directory.** Its
  2026-07-23 Level 0 manifest hashes 740 publication-critical files
  predating this manifest population (2026-08-05); extending it to include
  `reproducibility/manifests/` is a prerequisite for read path (a) in §4 and
  is not yet done.
- **Hardware-tier and venue strings are free text, not a closed enum**
  (`environment.hardware`, `reproduction.recommended_venue`) — a
  machine-schedulable run (e.g. Hubify auto-provisioning a RunPod instance)
  needs a real enum/taxonomy on the BigBounce side first; today these are
  human-readable strings only, by design (schema allows any non-empty
  string).
- **No structured verification runner.** `verification` is prose today. A
  Hubify "click to verify" button that actually re-executes and diffs
  outputs would need either a convention for detecting hash-check vs.
  numeric-tolerance vs. named-tool verification, or a follow-up schema field
  (e.g. `verification_command`) — neither exists yet. Do not build a
  fake/partial automatic verifier against the current free-text field.

---

## Status 2026-09-02

**A dev-machine dry-run importer now exists on the Hubify side** —
`hubify/cli/src/repro-manifest-import.ts` + `commands-repro-import.ts`
(invoked as `hubify repro-import`), implementing this spec's §1–§5
contract: `manifest_version` gate (reject unknown/missing, no
best-effort parse), program→experiment DAG join (missing DAG id or
unresolvable `code[].path` is a hard error, not a skip), the
status→offerability mapping (§"Status → offerability"), and the
non-fabrication rule for `null` fields (reported as honest "gaps", never
inferred). 7 tests pass (`cli/test/repro-manifest-import.test.mjs`),
including a real-checkout integration test against this repo.

A dry run against this repo's current `reproducibility/manifests/`
(commit-pinned, per §4) produced: **3 programs, 52 experiments, 0 import
errors, 317 honest gaps** (mostly `checksum: null` and unset
`original_run` fields — expected, not a defect) — written to
`hubify/data/imports/bigbounce-manifests-2026-09-02.json`.

**What this is not yet:** per §4's stricter safety constraint, this
dry-run reads a live local checkout of this repo directly, which is
*not* the sanctioned Hubify-side read path (the isolated
`bigbounce-lab` mirror workspace, or the public GitHub mirror at a
pinned SHA — neither of which yet mirrors `reproducibility/manifests/`).
It also does not write to Convex — this remains a local validated
loader/CLI producing a JSON payload, not a live import.

**Remaining step (token-gated, not attempted):** pushing the validated
payload into Hubify's live Convex tables requires `HUBIFY_TOKEN`, which
is absent from `hubify/.env.local` (`.env.example` declares it but no
value is set) and is only obtainable via the You.md encrypted vault or
`hubify auth login` — both require Houston. No agent attempted to
acquire it. Once available, the remaining work is: (1) extend the
`bigbounce-lab` mirror to include `reproducibility/manifests/` (closing
the §4 read-path gap), and (2) wire the existing dry-run payload builder
to a real Convex mutation instead of a JSON file write.
