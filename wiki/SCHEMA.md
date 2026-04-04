---
title: Wiki Schema & Conventions
type: meta
last_updated: 2026-04-04
---

# BigBounce Wiki Schema

This wiki is the project's persistent, interlinked knowledge base. It has three layers:

1. **Raw sources** (read-only): `project-context/`, `research/`, `pipelines/`, `reproducibility/`
2. **Wiki** (LLM-maintained): this directory, structured markdown with YAML frontmatter
3. **Schema** (this file): conventions, workflows, lint rules

---

## File Naming

- Kebab-case: `fnl-prediction.md`, `desi-dr1.md`
- Every file has YAML frontmatter:

```yaml
---
title: Human-readable title
type: entity | concept | source | comparison | meta
tags: [survey, anomaly, fnl, bounce, paper]
last_updated: YYYY-MM-DD
sources:
  - project-context/active_pods_and_pipelines.md
  - pipelines/p1_highz_tracers/outputs/tracer_purification_mvp.json
---
```

## Directory Structure

```
wiki/
  SCHEMA.md          # This file
  index.md           # Categorized catalog with one-line summaries
  log.md             # Chronological event log
  entities/          # Surveys, papers, pipelines, infrastructure
  concepts/          # Scientific concepts, methods, predictions
  comparisons/       # Side-by-side analyses
```

## Cross-References

Use double-bracket syntax: `[[entity-name]]` (no path, no extension).

Examples:
- `[[desi-dr1]]` links to `entities/desi-dr1.md`
- `[[fnl-prediction]]` links to `concepts/fnl-prediction.md`
- `[[bounce-vs-inflation]]` links to `comparisons/bounce-vs-inflation.md`

Resolution order: entities/ -> concepts/ -> comparisons/ -> root.

## Index Structure

`index.md` is organized by category:
- **Entities**: surveys, papers, pipelines
- **Concepts**: scientific predictions, methods
- **Comparisons**: side-by-side analyses
- **Meta**: schema, log

Each entry: `- [[page-name]] -- one-line summary`

## Log Format

`log.md` uses this structure:

```markdown
## [YYYY-MM-DD] action | Subject

Brief description. Links to [[relevant-pages]].
```

Actions: `started`, `completed`, `updated`, `closed`, `opened`, `pivoted`, `published`

## Ingest Workflow

When new research results arrive:

1. **Read source** -- identify the raw file(s) with new information
2. **Discuss takeaways** -- what changed, what's new, what's confirmed/refuted
3. **Write summary** -- create or update the relevant wiki page(s)
4. **Update index** -- add new pages to `index.md`
5. **Revise entity/concept pages** -- propagate changes to all affected pages
6. **Append to log** -- add a dated entry to `log.md`

## Query Workflow

When answering a question from the wiki:

1. **Search relevant pages** -- find all pages related to the question
2. **Synthesize** -- combine information across pages
3. **Cite** -- reference specific wiki pages with `[[page-name]]`

## Lint Rules

Run periodically to maintain wiki health:

| Rule | Check | Fix |
|------|-------|-----|
| No orphans | Every page in a subdirectory appears in `index.md` | Add missing entries |
| No stale pages | `last_updated` within 30 days | Review and update or mark `stale: true` |
| No missing cross-refs | Every `[[ref]]` resolves to an existing file | Create stub or fix reference |
| No contradictions | Numbers cited on multiple pages must agree | Trace to source, fix the stale one |
| Frontmatter complete | Every file has title, type, tags, last_updated | Add missing fields |

## Lint Workflow

```
1. List all .md files in wiki/
2. Parse all [[cross-refs]]
3. Check each ref resolves to a file
4. Check each file appears in index.md
5. Check last_updated < 30 days ago
6. Check key numbers (anomaly counts, sigma values) are consistent across pages
7. Report: orphans, stale pages, broken refs, contradictions
```
