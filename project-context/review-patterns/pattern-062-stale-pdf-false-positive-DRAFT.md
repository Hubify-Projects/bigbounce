---
pattern_id: 62
status: draft
first_seen: R52 (2026-06-26)
papers_observed: [P1A, P1B, P5]
finding_count: 4
proposed_by: r-round-pattern-mine 2026-06-26
---

# pattern-062: stale-pdf-false-positive

**Description**: The PDF served to reviewers lags the canonical `.tex` source by one or
more versions. Reviewers flag items as "missing" or "wrong" that are already fixed in
the source but not yet in the served PDF. Truth-audit correctly marks these STALE, but
the triage cost is real.

**Root cause**: The PDF serving path (site/public/papers/) is updated less frequently
than the source `.tex`. After a D-round or minor patch bump, the served PDF may lag
by one or two versions while the `.tex` HEAD is ahead.

**Evidence (R52)**:
- P1A: `.tex` at v1A.0.79 (June 19); served PDF at v1A.0.78 (June 18). Visual-tier findings against v0.78 already STALE. F10 future-date finding STALE (date was in the past by review time).
- P1B: Served PDF `~v1B.0.74`; source at v1B.0.76. Grok N2 "June 14 2026 is future" STALE (source paperTimestamp = June 20).
- P5: Served PDF v0.1.82; source v0.1.83. S1 (Fig 8 colorbar) and S2 (Table VII dagger) both fixed in v0.1.83 before audit, marked STALE.

**Why it matters**: Each STALE finding costs ~10 min of truth-audit attention. With 4+
STALE findings per round from PDF drift, this accumulates to 40+ min of avoidable work.
Additionally, a PDF-ahead-of-source reviewer could introduce false positives on things
NOT in the served PDF.

**Detection rule (mechanical)**:
```bash
# Before dispatching vendor reports, confirm the served PDF version matches
# the source paperVersion macro:
SERVED_VERSION=$(pdfinfo site/public/papers/<paper>_v*.pdf | grep "Title\|Producer")
TEX_VERSION=$(grep -E '\\paperVersion|\\date' <source.tex> | head -3)
echo "Served: $SERVED_VERSION"
echo "Source: $TEX_VERSION"
# They must agree. If not, recompile and re-mirror before dispatch.
```

**Prevention**:
1. Run `/bigbounce-paper-pdf-mirror` after every bump to keep served PDFs in sync.
2. Add a pre-dispatch gate in `/cross-vendor-r-round`: compare served PDF md5 against
   the freshly compiled PDF; if they differ, re-mirror before sending to vendors.
3. Truth-audit preamble must state which PDF version reviewers saw AND which source
   version is current; stale-delta must be called out explicitly before triaging.

**Example sites**:
- P5 R52: v0.1.83 D-round patch (Fig 8 fix + Table VII dagger) landed BEFORE the R52
  dispatch; 2 findings already closed by the time the audit ran.

**Severity**: medium — each stale finding is cheap to dismiss but aggregates; also risks
confusing causality if the auditor doesn't know the served-vs-source delta.
