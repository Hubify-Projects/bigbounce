# Truth audit — 2026-07-23 routine re-sweep (six closure versions)

18 legs (6× Grok API + 6× Gemini API + 6× Claude Opus INT, exact-SHA-bound).
Verdicts: Grok A/m/A/A/m/m · Gemini m/m/m/m/m/M · Claude A/A/m/m/m/m
(P1A,P1B,P2,P3,P4,P5). **Grok's first-ever ACCEPT on P2**, plus ACCEPT on P1A
and P3; Claude ACCEPT on P1A and P1B with zero findings.

## GENUINELY-NEW-REAL (1 class, 3 papers)
- **Version-stamp drift in Data-Availability prose** — "the present manuscript
  is v1.7.126 / v3.2.0-r11 / v1.0.269" vs current v1.7.127 / r12 / v1.0.270
  (P2/P3/P4; Claude legs, confirmed by grep). Root cause: the self-reference is
  a hardcoded literal the version-bump flow doesn't touch. Fix: bind to the
  \paperVersion macro (can never drift again) + align the deposit-tense to the
  truthful "will be added on the next re-stage" convention. → closures
  v1.7.128 / v3.2.0-r13 / v1.0.271.

## FALSIFIED
- P5 Claude MINOR "[8] Hamaus never cited": \cite{Hamaus2014} live in body at
  tex:2943 (non-comment). Second falsification of the same re-flag (07-22
  audit, finding #3). Referee misses the parenthetical citation.
- P4 Grok MINOR "Zenodo DOI stated without identifier": DOI
  10.5281/zenodo.21461899 rendered 3× incl. Data Availability, curl-verified
  (07-22 Claude leg). Re-flag.

## ALREADY-TRACKED-GATE
- P5 Gemini MAJOR-1 (Paper-IV unpublished): the D3 back-patch gate — closes at
  P4 arXiv submission.
- P5 Gemini MAJOR-3 (no P5 DOI/tag yet): the tracked fail-closed P5 deposit
  gate (waits on the Paper-IV back-patch); disclosed in-paper.

## DISCLOSED-RE-FLAG / SCOPE-VENUE-OPINION
- P5 Gemini MAJOR-2 (deferred DR2 mock): the paper's own disclosed limitation;
  bounded-surrogate injection [A47]/[A48] closure stands (DP5-19 class).
- P5 Gemini minors (abstract density = venue opinion; ASTRA clarification =
  disclosed differing-tracers discussion). P1B Grok minors (macOS-untested vs
  POSIX design are compatible, deliberate honesty closure; §7 docs pointer =
  presentation opinion). P4 Grok minors (CE summary-table readability opinion;
  commit hash pinned in deposit manifest + Data Availability).

**Outcome:** after the three stamp closures land, 0 genuinely-new-real
outstanding across all six papers on ACTIVE legs (directive M-AMENDED).

---

# CORRECTION — appended 2026-07-24

**The outcome line above was not fully evidenced when it was written.** The
original pass on 2026-07-23 dispositioned P1B's Grok *minors* under
DISCLOSED-RE-FLAG but **never dispositioned P1B's Grok `[MAJOR]`**, and a
subsequent completeness sweep found three further undispositioned MAJORs on
other papers (§Sibling completeness sweep below). This section adjudicates the
P1B MAJOR — **missed in the original 2026-07-23 pass, adjudicated 2026-07-24**
— and records the sibling gaps for separate scoping. This is a correction, not
a backfill: the 07-23 conclusion stood on an incomplete disposition set for
about a day, and P1B's JORS bundle was assembled during that window.

Root cause of the miss: the P1B and P5 Grok legs each carry a `PARSED VERDICT:
MINOR REVISIONS` header while their issue lists contain `[MAJOR]`-tagged items.
A triage that keys on the leg's verdict word rather than on per-item severity
tags silently drops those findings. **Process fix: severity must be read from
the per-item tags in the raw text, never from the leg's parsed verdict word.**

## P1B — Grok (grok-4.3) `[MAJOR]` — verbatim

> `[MAJOR]` Title page (and abstract) state version v2B.0.14 while sections 6,
> 10, and 11 repeatedly claim "Version 0.1.7" (with matching test count, Python
> requirement, archive DOI, and commit pin), creating an irreconcilable
> internal contradiction.

Source: `INT_v3/ROUND_2026-07-23-P1B-v2B.0.14-EXACTPDF-4b7c752f-CLAUDESTACK-RESWEEP/API_P1B_grok.md` L17.
Leg present and non-empty; exact-PDF binding sha256 `4b7c752f79…` matches the
round manifest. This is an escalation of the same substance Grok raised as
MINOR-1 on 2026-07-22 (FALSIFIED in that round's truth audit, finding #3).

### Verdict — **GENUINELY-NEW-REAL** (the literal claim is FALSIFIED; the defect underneath it is real)

The finding splits cleanly, and both halves are recorded rather than letting the
false half suppress the true one.

**(a) The literal claim — "irreconcilable internal contradiction" — is
FALSIFIED.** Every software-version string in the manuscript agrees with the
released package and with the archive, verified against source on 2026-07-24:

| Assertion in paper | Verified against | Result |
|---|---|---|
| software version 0.1.7 | `packages/namaster-proof/pyproject.toml` L3 `version = "0.1.7"` | MATCH |
| " | `packages/namaster-proof/codemeta.json` `"version": "0.1.7"` | MATCH |
| " | `packages/namaster-proof/CITATION.cff` `version: 0.1.7` | MATCH |
| " | `packages/namaster-proof/src/namaster_proof/__init__.py` L36 `__version__ = "0.1.7"` | MATCH |
| " | Zenodo record 10.5281/zenodo.21481753 — API `metadata.version` = `"0.1.7"`, title `"namaster-proof 0.1.7: …"` | MATCH |
| "41 automated tests … 39 run standalone, 2 skip" | `pytest --collect-only` = 41 collected (cli 2, example 1, legacy_equivalence 2, multipoles 13, receipts 12, retained_integration 1, windows 10); the 2 skipping tests are exactly `test_legacy_equivalence.py` | MATCH |
| "Python 3.10 or later" | `pyproject.toml` L10 `requires-python = ">=3.10"` | MATCH |
| commit pin `0a587b583f8e86c4ce1ee4a20526fcdcd8035fe6` | `git cat-file -t` → `commit` (resolves in repo) | MATCH |
| "deposited July 21, 2026" | Zenodo `created` = `2026-07-22T00:17:51Z` = 2026-07-21 17:17 PT | MATCH |

Grok's premise — that the title-page stamp and the body's software version
*must* agree — is false. `\paperVersion` is a document-revision stamp;
`0.1.7` is a software release. Two namespaces, correctly used. Also factually
wrong in the finding: the **abstract states no version at all** (tex L95–110,
confirmed in the rendered PDF page 1), and the third cited section is §10 not
§11 (the Archive paragraph lives inside §10 Availability).

**(b) The legibility gap underneath it is GENUINELY-NEW-REAL, and closes here.**
Falsifying the premise does not dispose of the finding, because the manuscript
gave a reader nothing to falsify it *with*. As of v2B.0.15 the paper:
- rendered the title-page stamp as a bare `July 24, 2026 --- v2B.0.15`, with
  no word identifying it as a document revision (tex L91);
- stated the software version three times as a bare `Version 0.1.7`
  (tex L237 §6, L355 §10, L378 §10), never as *the software's* version;
- contained **no sentence anywhere** telling a reader the two numbers are
  different kinds of thing.

Two independent referee passes stumbled on exactly this (07-22 Grok MINOR-1,
07-23 Grok MAJOR). A reader-facing ambiguity that reproducibly misleads
referees is a real presentation defect, not referee noise — and JORS assesses
metadata correctness as a formal review criterion, so an ambiguous version
story is a substantive risk at this paper's actual submission venue. Per
directive H-refined and AGENT_RULES §2.4 (in doubt → GENUINELY-NEW-REAL; never
push back on stylistic grounds to dodge work), this closes with a real edit.

### Closure — v2B.0.15 → **v2B.0.16** (2026-07-24)

1. Title page: `\date{July 24, 2026 --- \paperVersion}` →
   `\date{July 24, 2026 --- manuscript revision \paperVersion}`. Stays a single
   short line per AGENT_RULES §4.7 item 5.
2. New `\paragraph{Software version.}` opening §10 Availability, stating the
   two-namespace distinction explicitly, naming the four metadata files and the
   Zenodo record that pin 0.1.7, and binding the document stamp to the
   `\paperVersion` macro so it can never drift — the same root-cause fix used
   for the P2/P3/P4 stamp-drift closures of this same re-sweep.
3. All three bare `Version 0.1.7` occurrences qualified to
   `\software{} version 0.1.7`. Zero unqualified `Version 0.1.7` strings remain
   in either rendering.

**Directive-G hygiene (all verified 2026-07-24):** `\paperVersion` v2B.0.16 +
`\paperTimestamp` 2026-07-24 18:20 PT + `\date` July 24, 2026 · recompile 0
undefined refs / 0 Overfull `\hbox` / 0 Overfull `\vbox`, 6 pages · §4.7 visual
audit: pages 1, 3, 4, 5 (page 1 + every changed page) rendered at 110 dpi with
`pdftoppm` and inspected — no column overflow, no gutter crossing, `\date` on
one line · pypdf page-1 verify: `manuscript revision v2B.0.16` present,
`v2B.0.15` absent · mirrored byte-identical (md5 `6d20df58e70261c805cd2ce2f9a4d5d3`)
to `arxiv/paper1b_namaster_proof.pdf`, `public/papers/paper1b_namaster_proof.pdf`,
`public/papers/paper1b_namaster_proof_v2B.0.16.pdf`,
`site/public/papers/paper1b_namaster_proof.pdf`,
`site/public/papers/paper1b_namaster_proof_v2B.0.16.pdf` — 5 paths, 1 distinct
md5 · arXiv tarball rebuilt as
`project-context/SSOT/arxiv_tarballs/paper1b_namaster_proof_arxiv_v2B.0.16.tar.gz`
and standalone-compiled in an isolated `/tmp` extract: 0 errors, 0 undef refs,
0 overfull hboxes, 6 pages, `pdftotext`-identical to the served PDF.

**JORS bundle kept in sync (mandatory — the bundle was assembled 2026-07-24 and
must not ship a defect we just fixed):** the equivalent change was applied to
`arxiv/jors_submission/paper1b_namaster_proof_jors.tex` (header
`CANONICAL SOURCE` → v2B.0.16; `\paperVersion`/`\paperTimestamp` bumped; the
same Software-version paragraph added to (2) Availability / Software location;
both bare `Version 0.1.7` occurrences qualified). Recompiled: 0 undef refs, 0
overfull hboxes, 8 pages; pages 1, 3, 5, 6 rendered and inspected.
Content-equivalence re-verified against the canonical v2B.0.16 PDF: the count
of byte-verbatim carried sentences is **unchanged from the v2B.0.15 baseline
(45/45)**, and every new divergence is a `pdftotext` heading/page-number
artifact except one deliberate adaptation — the canonical says the stamp sits
"on the title page", the JORS rendering says "carried in this document's page
header", each correct for its own layout. `README-JORS-SUBMISSION.txt` updated.
Bundle rebuilt as `arxiv/jors_submission/paper1b_jors_submission_v2B.0.16.tar.gz`
and standalone-compiled in an isolated `/tmp` extract: 0 errors, 0 undef refs,
0 overfull hboxes, 8 pages, `pdftotext`-identical to the shipped PDF.

## Sibling completeness sweep — all six papers, 2026-07-23 re-sweep

Every raw leg file of all six rounds was re-read and every `[MAJOR]`/`[BLOCKER]`
tag extracted, then matched on substance against the dispositions above.
18/18 legs present and non-empty; **0 `[BLOCKER]` tags anywhere.**

| Paper | Leg | Verdict word | MAJOR in raw | Dispositioned 07-23 | Gap |
|---|---|---|---|---|---|
| P1A | Grok | ACCEPT | 0 | — | no |
| P1A | Gemini | MINOR REVISIONS | 0 | — | no |
| P1A | Claude INT | ACCEPT | 0 | — | no |
| P1B | Grok | MINOR REVISIONS | **1** | 0 | **YES — closed above, v2B.0.16** |
| P1B | Gemini | MINOR REVISIONS | 0 | — | no |
| P1B | Claude INT | ACCEPT | 0 | — | no |
| P2 | Grok | ACCEPT | 0 | — | no |
| P2 | Gemini | MINOR REVISIONS | 0 | — | no |
| P2 | Claude INT | MINOR-REVISIONS | 0 | — | no |
| P3 | Grok | ACCEPT | 0 | — | no |
| P3 | Gemini | MINOR REVISIONS | 0 | — | no |
| P3 | Claude INT | MINOR-REVISIONS | 0 | — | no |
| P4 | Grok | MINOR REVISIONS | 0 | — | no |
| P4 | Gemini | MINOR REVISIONS | **1** | 0 | **YES — open, needs scoping** |
| P4 | Claude INT | MINOR-REVISIONS | 0 | — | no |
| P5 | Grok | MINOR REVISIONS | **2** | 0 | **YES ×2 — open, need scoping** |
| P5 | Gemini | MAJOR REVISIONS | 3 | 3 | no |
| P5 | Claude INT | MINOR-REVISIONS | 0 | — | no |

**Totals: 7 MAJORs in raw · 3 dispositioned on 07-23 · 4 gaps.** One (P1B) is
closed above. The remaining three are recorded verbatim below and are
**deliberately NOT adjudicated here** — they belong to other papers' lanes and
are being edited concurrently. They are scoping items, and until each carries a
verdict the 07-23 "0 genuinely-new-real outstanding" line does not hold for P4
or P5.

**P4 — Gemini `[MAJOR]`** (`ROUND_2026-07-23-P4-…-RESWEEP/API_P4_gemini.md` L18):
> **[MAJOR] Readability and inline provenance tracking (Throughout, e.g., Sec 2.2, Sec 3, Sec 4.1):** The extensive insertion of raw SHA-256 hashes, exact script file paths (e.g., `pipelines/p2_chirality/outputs/...`), and JSON filenames directly into the main narrative severely disrupts the readability of the manuscript. While the commitment to computational closure and open science is exemplary, these identifiers belong in footnotes, a dedicated provenance table, or the Data Availability section, rather than mid-sentence in the primary text.

Note: the 07-23 audit's "P4 Grok minors (CE summary-table readability opinion…)"
line is a **different leg and a different finding** and does not cover this.

**P5 — Grok `[MAJOR]` #1** (`ROUND_2026-07-23-P5-…-RESWEEP/API_P5_grok.md` L17):
> [MAJOR] Section V B and abstract: Post-review/post-inspection re-ranking of the focal released GALZONE/OUT=0 estimator over the author-constructed any-hole path (explicitly declared as changed after data inspection) introduces selection bias risk in an otherwise exploratory analysis; the paper must add an explicit sensitivity table showing the any-hole result side-by-side with the focal estimate before claiming hierarchy independence.

**P5 — Grok `[MAJOR]` #2** (`ROUND_2026-07-23-P5-…-RESWEEP/API_P5_grok.md` L18):
> [MAJOR] Section VIII A and Table VI: The focal 13-column linear nuisance model (and its NSIDE=4 cluster sandwich) is declared "post-review"; the manuscript must state the pre-review model specification and show that the null conclusion is unchanged under the originally planned spline/fixed-effect specification.

The 07-23 audit's P5 section dispositions Gemini's three MAJORs and Gemini's
minors only; it contains **no reference to Grok's P5 findings at all**. Both are
substantive analysis-specification concerns (post-hoc selection bias), not
presentation opinions, and should be scoped accordingly.

**Corrected outcome line:** as of 2026-07-24, P1A / P1B / P2 / P3 have 0
genuinely-new-real outstanding on ACTIVE legs. **P4 and P5 each carry
undispositioned reviewer MAJORs from the 2026-07-23 re-sweep and are NOT
evidenced as converged** until those carry source-cited verdicts.
