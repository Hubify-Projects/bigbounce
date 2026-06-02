---
status: confirmed
proposed_by: r-round-pattern-mine
proposed_date: 2026-06-02
confirmed_date: 2026-06-02
review_target: Houston
first_observation_corrected: 2026-05-15
---

# Pattern 017 — Review-log artifacts in body prose (not `%`-comments)

**First seen**: P4 v1.0.66 2026-05-15 Houston external 4-vendor round
(consolidated convergent BLOCKER B1 across all 4 vendors: Gemini-B1,
Gemini-DR-G2, Grok-I-1, ChatGPT-B-6 + H-1 + I-4). Independently re-observed
on P1A v1A.0.35-36 in the 2026-06-02 external 3-reviewer round (Gemini
BLOCKER 2.1 + ChatGPT MAJOR M9), which is where the pattern was first
catalogued in DRAFT form. Pattern existed in the campaign 18 days before
it was recognised — itself an instance of pattern-018.
**Severity**: high (BLOCKER-grade per Gemini; "instant desk-reject at any
serious journal"; "creates the impression that the manuscript is an
unedited auto-generated log file"; "unprofessional, unpublishable")
**Frequency**: 4-vendor convergent BLOCKER on P4 v1.0.66 (multiple sites
in Section VII Conclusions + footnotes); 9 distinct body-text occurrences
in P1A v1A.0.35-36; cross-paper count unknown until grep sweep runs across
P1B/P2/P3/P5
**Detection**: literal body-text statements (NOT `%`-comments) like
"...per R23 Gemini-3.1-Pro PAPER-GEM-M1 closure...",
"Three vendors in the second cross-vendor R-round (R2) independently flagged...",
"(v1A.0.28 R7 GPT-m1 closure: prior...)",
"...via the OpenRouter unified API on 2026-05-14...".

This is **distinct from pattern-014**, which catches `%`-comment artifacts.
Pattern 014 invisibly survived 8 internal R-rounds with 0 verified findings.
Pattern 017 catches the same shape but in compiled-into-the-PDF prose,
which is what external reviewers actually read.

## What it looks like

Examples extracted from P1A v1A.0.36 verbatim (see
`project-context/peer-reviews/external/2026-06-02_P1A_houston_external_grok_gemini_chatgpt.md`):

```
Sec. II.A.2 (Source 296): ...v1A.0.28 R7 GPT-ml closure: prior M~... inverted the scaling

Sec. II.C.1 (Source 337): ...per R23 Gemini-3.1-Pro PAPER-GEM-M1 closure,
                          the prior draft incorrectly equated this...

Sec. IV (Source 384):     A multi-vendor adversarial-review round
                          (GPT-5.5 / Gemini-2.5-Pro / Grok-4-fast / Perplexity
                          Sonar Pro / DeepSeek-V3.2, all queried via the
                          OpenRouter unified API on 2026-05-14) surfaced three
                          substantive theory-derivation BLOCKERs...

Appendix B (Source 740):  Three vendors in the second cross-vendor R-round (R2)
                          independently flagged this...

Appendix B (Source 753):  v1A.0.29 R8+R9 convergent BLOCKER closure:
                          Grok-B4/B1 + Perplexity-B4/B5 + GPT-M2...
```

These render in the compiled PDF. They look like science prose to a
domain-physics reviewer (who happily ignores them as "scratchpad") but
look like editorial collapse to a journal-style reviewer.

## Why pattern-014 didn't catch this

Pattern-014 grep:
```
grep -nE '^%.*\b(BLOCKER|MAJOR|MINOR|...)\b' <tex>
```

The `^%` anchor only matches lines that start with `%`. The body-prose
artifacts above are NOT in comment lines — they were lifted out of the
review-log and into the manuscript text during closure edits. Each
closure-edit that referenced "the R23 Gemini-3.1-Pro PAPER-GEM-M1 closure"
when re-stating the context survived as inline prose.

## Truth-audit verdict

VERIFIED (Gemini-B2.1 + ChatGPT-M9; nine distinct body-text occurrences
identified by external reviewers; trivially confirmable in the .tex).

## Examples observed

- **P4 v1.0.66 2026-05-15 Houston external 4-vendor (FIRST OBSERVATION,
  18 days before pattern was named)**: convergent BLOCKER B1 across all
  4 vendors (ChatGPT/GPT-5, Gemini Deep Research, Gemini, Grok). Section VII
  Conclusions and various footnotes contain raw text including:
  ```
  Real cross-vendor adversarial-review (v1.0.53)
  The DeepSeek-B1 / DeepSeek-M3 deferral...
  A multi-vendor adversarial round on v1.0.51 (GPT-5.5, Gemini-2.5-Pro,
    Grok-4-fast, Perplexity Sonar Pro, DeepSeek-V3.2...)
  v1.0.62 closure
  v1.0.55 analytic projection
  ```
  Vendor verdicts: ChatGPT REJECT-AND-RESUBMIT, Gemini DR REJECT-AND-RESUBMIT,
  Gemini MAJOR REVISION, Grok 5-must-fix-then-preprint. Houston:
  "got blasted as totally no-go unpublishable by everyone." Source:
  `project-context/peer-reviews/external/2026-05-15_P4_v1066_houston_external_4vendor_consolidated.md`.
- **P1A 2026-06-02 external Gemini-B2.1**: BLOCKER-grade flagging of all
  nine sites. Recommended "must be completely purged from academic text".
- **P1A 2026-06-02 external ChatGPT-M9**: MAJOR flag, "make the paper read
  like a revision log rather than a journal article".
- **P1A 2026-06-02 external (implied across multiple findings)**: the
  presence of these artifacts undermined ChatGPT's confidence in the
  manuscript's editorial rigor, contributing to its "REJECT" recommendation.

## Root cause

Closure protocol for past internal R-rounds wrote closure-summary prose
DIRECTLY into the .tex body to "show the work" for future reviewers. This is
the same instinct that drove pattern-014 (review-log in `%`-comments) but
escaped the comment block via copy-paste into closure paragraphs. Once in
body prose, the artifact compiles into the PDF and is visible to anyone
reading the final paper.

## Pre-review check

Before any external review:

1. **Assert** (BODY-prose grep — `^%` anchor REMOVED):
   ```
   grep -nE '\b(R[0-9]+ closure|PAPER-(GEM|GRO|GPT|PER|CGT|DEE)-[A-Z][0-9]+|cross-vendor R-round|multi-vendor adversarial-review|OpenRouter unified API|Gemini-?[0-9]\.[0-9]-?[A-Za-z]*|Grok-[0-9]|Perplexity Sonar|DeepSeek-V|GPT-[0-9]\.[0-9])\b' <tex> | grep -v '^[0-9]*:%'
   ```
   Any non-empty match → BLOCKER. Strip before review.
2. **Assert** version-history sentinels in body prose:
   ```
   grep -nE '\b(v[0-9]+\.[0-9]+\.[0-9]+ [A-Z]?[0-9]+|prior draft|earlier draft|previous version) (closure|flagged|revision)' <tex> | grep -v '^[0-9]*:%'
   ```
3. **Assert** no "convergent BLOCKER closure" / "convergent silence" /
   "BLOCKER → VERIFIED" phrasing in body prose. Allowed in comment block
   only (pattern-014 governs comment block).
4. **Allowed**: Acknowledgments section may state "AI tools assisted in
   manuscript preparation" once, generically, journal-appropriate.

Standing rule: **review-log lives in .md files OR `\iffalse...\fi` blocks;
NEVER in compiled body prose, even paraphrased.**

## Related patterns

- **Pattern 014** (parent): `%`-comment block artifacts. Same root cause,
  different surface.
- **Pattern 018** (sibling, new): internal R-rounds blind to editorial
  artifacts. Pattern 017 is one specific case of the pattern-018 meta-gap.
- **Pattern 005** (overclaim): some review-log artifacts also carry
  overclaim language ("BLOCKER closure", "definitive"). Closure of 017
  often also closes 005 in the same site.
