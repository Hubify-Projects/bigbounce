# 2025 Legacy Archaeology + Cosmic-Fate / Daughter-Universe lanes — campaign plan

**Opened:** 2026-09-18 · **Director:** Claude (Fable 5.1) orchestrating session in `~/Desktop/CODE_YOU`
**Authorization:** Houston, 2026-09-18: "continue and don't stop until all the new plans and lanes are
fully executed documented and running live with live monitoring for all spawned subagents sessions and
research and site improvements and everything" — after the director raised the sign-off-queue and
portfolio-decision concerns and Houston reaffirmed.

## Hard constraints (non-negotiable)
1. **No edits to active manuscripts** (P1A/P1B/P1N/P2/P2L/P3/P4/P4P/P5/A3M/SU `.tex`), no version bumps,
   no Convex `paperVersions`/`rRounds`/`externalReviews` writes from this campaign.
2. **Existing nulls stay nulls.** Popławski spin-axis dipole is EXCLUDED (2026-09-02); galaxy-spin dipole
   is NULL (P4/P5); ECH dark-energy routes are CLOSED (P1N). Nothing here reopens them.
3. Old Notion/ChatGPT prose is provenance only. Every citation resolves or is quarantined.
4. New science enters the public **Current Science** layer only through the normal R→D→P gate. This
   campaign publishes to **Open Questions** (`/speculations`) and **Research Genealogy** (new page) only.
5. Houston's preference for a regenerative universe is motivation, never a prior.

## Workstreams and models
| W | Lane | Model | Output |
|---|---|---|---|
| W1 | Archaeology source map (repo + git history) | sonnet | `SOURCE_MAP.md` |
| W2 | Verified bibliography (resolve all 11 dump citations + lane-critical refs) | sonnet | `bibliography/VERIFIED_BIBLIOGRAPHY.md` |
| W3 | Cosmic-fate technical memo (turnaround conditions, model taxonomy, current constraints) | opus | `memos/COSMIC_FATE_MEMO.md` |
| W4 | Black-hole daughter-universe memo (causal taxonomy, literature map, morphology sidebar) | opus | `memos/DAUGHTER_UNIVERSE_MEMO.md` |
| W5 | Parent–child mass/energy/entropy bookkeeping + Popławski reproduction | fable | `memos/PARENT_CHILD_BOOKKEEPING_MEMO.md` + `outputs/` |
| W6 | Legacy hypothesis ledger (A–G dispositions) + retired-hypotheses ledger | sonnet (after W1, W2) | `LEGACY_HYPOTHESIS_LEDGER.md` |
| W7 | Site: speculations cards, Learn explainer, genealogy page, activity feed | sonnet (after W3–W6) | `site/src/app/**`, Convex activityFeed |
| W8 | Ledger items #20–#22, SSOT queue note, prompts log, You.md memory | director | `project-context/**` |

## Live monitoring
- `STATUS.md` in this directory is the single live status board; the director updates it on every
  worker transition. Each worker appends a dated line to `STATUS.md` on start and on finish.
- Public: one Convex `activityFeed:add` event on campaign open and one on campaign close, plus one per
  memo landing (type `research`, tag kind `lane`). The site's activity page renders these live.
- Git: the context-sync cron auto-commits every ~2 min; the director bisects and pushes at milestones.

## Definition of done
Every item in the dump's §DEFINITION OF DONE, restricted by the hard constraints above, plus:
site built clean, pushed to `origin/main`, live URLs curl 200, ledger #20–#22 present, STATUS.md
shows every worker `DONE` with artifact path and commit hash.
