---
name: bigbounce-status
description: Read the live state of all Bigbounce papers from Convex via the bigbounce MCP. Returns each paper's computed readiness (derived from open findings + caveats, not hand-set), current version, last update, open BLOCKER/MAJOR/MINOR/CAVEAT counts, and status (active-drive-to-100 / paused-houston-external / submitted-arxiv / ...). The single canonical 'where are we?' check. Use this BEFORE editing any paper-state surface; the answer comes from Convex, not from drift-prone markdown / .tex comment blocks / static papers.ts.
---

# /bigbounce-status

Calls `bigbounce_list_papers` via the bigbounce MCP server. Prints a clean dashboard.

## Usage

```
/bigbounce-status                 # all 6 papers
/bigbounce-status paper-1a        # one paper, full state
/bigbounce-status open-findings   # all open R-round findings cross-paper
/bigbounce-status pods            # RunPod state
/bigbounce-status tasks           # open task queue
```

## Behavior

If the MCP server is not available (CONVEX_URL not set, or Convex deploy not done yet), falls back to reading `site/src/data/papers.ts` as the legacy source — but prints a ⚠️ banner that the fallback may be stale.

## Output format

```
PAPER  VERSION    READINESS  STATUS                       UPDATED      OPEN
1A     v1A.0.36   95         paused-houston-external      2026-05-28   0B 0M 0m 0C
1B     v1B.0.30   78         active-drive-to-100          2026-05-26   0B 0M 0m 2C
2      v1.7.37    81         active-drive-to-100          2026-05-24   0B 0M 0m 3C
3      v3.1.69    89         active-drive-to-100          2026-05-29   0B 0M 0m 4C
4      v1.0.139   95         paused-houston-external      2026-05-28   0B 0M 0m 0C
5      v0.1.32    82         active-drive-to-100          2026-05-26   0B 0M 0m 3C
```

`open` = open BLOCKER / MAJOR / minor / Caveat counts.
