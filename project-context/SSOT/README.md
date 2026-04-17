# BigBounce SSOT — protocol

**SSOT = Single Source of Truth.** Per-paper canonical status files that consolidate everything we've learned about a paper into one place, so we stop relying on drifted wikis / stale status dashboards / outdated dossier sections.

This directory is the **authoritative reality check** for the four BigBounce papers. If something contradicts a file here, the file here wins. If something here contradicts observed repo state, the file here is wrong — fix it.

## Layout

```
project-context/SSOT/
├── README.md         ← this file · protocol
├── index.md          ← cross-paper dashboard · read first
├── queue.md          ← prioritized, tagged close-the-gap task queue
├── paper-1/status.md ← Spin-Torsion Cosmology (stub · sweep pending)
├── paper-2/status.md ← f_NL Forecast (stub · sweep pending)
├── paper-3/status.md ← Multi-Survey Anomaly Catalog (sweep complete, 99 %)
└── paper-4/status.md ← Galaxy Chirality Catalog (sweep complete, 97 %)
```

## When to read

- **Any time you touch a paper** — read the paper's `status.md` first. Do NOT infer status from `CURRENT_STATUS.md`, `wiki/entities/`, dossier files, or site HTML. Those are downstream surfaces that are frequently stale.
- **Before you start any research or coding work on a paper** — check `index.md` for program-level context and `queue.md` for current priorities.
- **At session start** — glance at `index.md` if you expect the work to involve any of the papers.

## When to write

Update the relevant `status.md` any time you:

1. Produce a new verified result (new σ, new count, new figure).
2. Discover that a prior claim in the paper doesn't match the artifacts on disk.
3. Close or open a "close the gap to 100 %" item.
4. Change the canonical `.tex` location or compile the PDF.
5. Sync (or fail to sync) a downstream surface — site, wiki, related paper cross-refs, external catalogs (HF/Convex/B2).

Update `queue.md` any time you add, complete, reprioritise, or block a task.

Update `index.md` whenever any paper's headline % or one-line status changes.

## Anti-patterns (do not do)

- ❌ Do not write research-progress notes into `CURRENT_STATUS.md`. That file should become a mirror of `index.md`, not its own moving part.
- ❌ Do not add "Remaining Work" lists to `wiki/entities/*.md`. Wiki entries are entity references; remaining-work tracking belongs in the SSOT `status.md` and `queue.md`.
- ❌ Do not create new top-level `project-context/paperN_*.md` status files. Put them under `SSOT/paper-N/`.
- ❌ Do not ship a paper to arXiv if its SSOT still has unchecked boxes in the "close-the-gap" section unless the box is explicitly waived with a one-line note from Houston.
- ❌ Do not trust a headline "% ready" that is more than 48 h old. Check the `Last authoritative update` line at the top of the SSOT.

## How to audit SSOT freshness

```bash
for f in project-context/SSOT/paper-*/status.md; do
  grep -H "Last authoritative update" "$f"
done
grep -H "Last authoritative update\|last_updated" \
  project-context/SSOT/index.md \
  project-context/SSOT/queue.md
```

If any date is > 7 days old, read the relevant paper's `.tex` + `git log` since that date and refresh the file. Do it before doing any new work.

## Principle 10 hook

Every `status.md` MUST contain a "Future-work audit per Principle 10" section. The grep list to run against each paper's `.tex`:

```
future work | leave to future | defer | will be presented | in preparation |
forthcoming | we plan to | beyond the scope | further study | next step |
would benefit | in a follow-up | follow-up paper | follow.up | could be |
may be | should be | merits | warrants | invites | remains to | yet to be |
not yet | more data | larger sample | future surveys? | future observations? |
upcoming | next-generation | next generation | we leave | we expect
```

Every hit is classified DO-NOW / SIMULATE-AUGMENT-NOW / TRULY-BLOCKED. Only TRULY-BLOCKED items may remain in the paper. Everything else is a queue task.

## Pointer files

These files at their old locations are kept as one-liner pointers so old references still resolve:

- `project-context/paper3_anomaly_catalog_status.md` → `SSOT/paper-3/status.md`
- `project-context/paper4_chirality_status.md` → `SSOT/paper-4/status.md`

Do not delete them. Do not expand them — they exist only to bounce readers to the real SSOT.
