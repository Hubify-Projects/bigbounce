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

**Corrected outcome line (superseded — see the ADJUDICATION section below):** as
of 2026-07-24, P1A / P1B / P2 / P3 have 0 genuinely-new-real outstanding on
ACTIVE legs. **P4 and P5 each carry undispositioned reviewer MAJORs from the
2026-07-23 re-sweep and are NOT evidenced as converged** until those carry
source-cited verdicts.

---

# ADJUDICATION of the three remaining missed MAJORs — 2026-07-24

**These three items were MISSED in the original 2026-07-23 pass and are
adjudicated here on 2026-07-24.** They are not a silent backfill: for roughly
one day the 07-23 line "0 genuinely-new-real outstanding across all six papers"
stood on a disposition set that never touched them. The root cause is the one
already recorded above — the P4-Gemini and P5-Grok legs carry `PARSED VERDICT:
MINOR REVISIONS` headers while their issue lists contain `[MAJOR]`-tagged items,
and the 07-23 triage keyed on the verdict word. The process fix is encoded in
the canonical skills (see "Process fix landed" at the end of this section).

Read-only adjudication: no paper `.tex` was edited by this pass. Each
GENUINELY-NEW-REAL item carries a closure plan for the owning paper lane.

---

## P4 — Gemini (gemini-3.1-pro-preview) `[MAJOR]` — verbatim

Source: `INT_v3/ROUND_2026-07-23-P4-v1.0.270-EXACTPDF-ac7b39ba-CLAUDESTACK-RESWEEP/API_P4_gemini.md` L18.
Exact-PDF binding sha256 `ac7b39baca9a…` matches the round manifest; leg present
and non-empty.

> **[MAJOR] Readability and inline provenance tracking (Throughout, e.g., Sec 2.2, Sec 3, Sec 4.1):** The extensive insertion of raw SHA-256 hashes, exact script file paths (e.g., `pipelines/p2_chirality/outputs/...`), and JSON filenames directly into the main narrative severely disrupts the readability of the manuscript. While the commitment to computational closure and open science is exemplary, these identifiers belong in footnotes, a dedicated provenance table, or the Data Availability section, rather than mid-sentence in the primary text.

### Verdict — **GENUINELY-NEW-REAL** (as a presentation defect; escalated from a twice-dismissed MINOR)

The tempting disposition is SCOPE-VENUE-OPINION, and the ledger has twice taken
it. That is exactly what AGENT_RULES §2.4 forbids: *"Never push back on
stylistic grounds."* The prior dismissals are recorded and are the reason the
same referee escalated.

**Prior history (this is a re-flag that has been escalating, not a first
sighting):**

| Round | Leg | Severity | Disposition then |
|---|---|---|---|
| GEM1-INT 2026-07-11 (v1.0.235) | Gemini | `[MINOR]` "Excessive inline repo paths" | PROCESS-NIT (style) — `DISPOSITIONS/P4.md` L210 |
| later wave (v1.0.2xx) | Gemini | `[MINOR]` "inline filepath artifacts" | DP4-13 / PROCESS-NIT — `DISPOSITIONS/P4.md` L319 |
| **2026-07-23 re-sweep (v1.0.270)** | **Gemini** | **`[MAJOR]`** | **(none — the miss)** |

Same referee, same substance, MINOR → MINOR → MAJOR on content that was never
changed in response. Under directive H-refined this is *not* pattern-066
referee noise: pattern-066 is a flip on *unchanged-but-already-addressed*
content; here the content was unchanged and *never* addressed. Twice dismissing
a finding on style grounds and then treating its escalation as noise is the
`/review-integrity-audit` Check-2 failure mode in its exact shape.

**Source verification — the complaint is factually accurate.** Verified against
`pipelines/p2_chirality/chirality_catalog_paper.tex` on 2026-07-24 (live text
only; `%`-comment and `\iffalse` regions excluded programmatically):

| Assertion in the finding | Verified against source | Result |
|---|---|---|
| raw SHA-256 mid-narrative | 11 live lines carry a ≥12-char hex literal | CONFIRMED |
| exact script/output paths inline | 9 live lines carry a `\texttt{…/…}` path or `\path{}` | CONFIRMED |
| JSON filenames inline | 24 live lines name a `.json` / `.py` / `.csv` / `.npz` file | CONFIRMED |
| "mid-sentence in the primary text" | **tex L1614 — the paper's single primary-result paragraph** — carries a full 40-hex HF revision `911316f31c21f2c4b933a2f3a761274cfe85c6d6` and the release path `apjs-release/v1.0.259-strict-primary/` in the same sentence run as the headline null ($z_{\rm mom}=+0.635$, $p=0.23768$) | CONFIRMED — worst instance sits on the most load-bearing sentence in the paper |
| §Training Labels density | tex L1010 + L1012 carry six truncated `SHA-256 \texttt{…}` insertions plus bare manifest filenames inside running prose | CONFIRMED |

**What is NOT real in the finding, recorded for honesty:** the typographic half
does not hold. `pipelines/p2_chirality/chirality_catalog_paper.log` has **0
`Overfull \hbox`** — the inline paths are not breaking the two-column layout
(that is Gemini's separate MINOR-4, which IS falsified on the log). The defect
is density and placement, not overflow.

### Closure plan — **prose/structure only. NO re-analysis, NO compute, $0.**

Owner: the P4 lane. Target version **v1.0.271 → v1.0.272**. Every hash stays in
the paper — this is relocation, not deletion; deleting provenance would break
`/artifact-link-verify` and directive-G.

1. **tex L1614 (highest priority).** Lift the 40-hex HF revision and the
   `apjs-release/v1.0.259-strict-primary/` path out of the primary-result
   sentence into either a footnote on that sentence or the existing Data
   Availability list (tex L1907–L1914), leaving a prose pointer
   ("…at the immutable release revision recorded in Data Availability").
   The headline sentence must read as a result, not as a manifest.
2. **tex L1010 + L1012 (§Training Labels / CE-composition adjudication).**
   Replace the six inline `SHA-256 \texttt{…}` insertions and the bare manifest
   filenames with the existing `\artifact{}` macro pointer plus **one provenance
   table**: either three new columns on the existing
   `tab:training_provenance` (tex L1702) or a new `tab:artifact_provenance`
   holding artifact-ID → path → SHA-256. Prose keeps the artifact ID; the table
   holds the hash.
3. Sweep the remaining live-text hex/path/JSON hits from the counts above
   (11 / 9 / 24) and route each to the same table or to Data Availability. Keep
   `\artifact{}` pointers inline — those are the paper's designed mechanism and
   are not what the referee objected to.
4. Directive-G chain: `\paperVersion` + `\date` + `\paperTimestamp` bump,
   recompile 0 undef refs / 0 overfull, `/latex-audit`,
   `/artifact-link-verify` (mandatory — step 1 moves URLs), 13-path mirror,
   Convex `paperVersions:bump`, `DISPOSITIONS/P4.md` DP4-13 flipped to
   CLOSED-BY-EDIT (v1.0.272) with this escalation recorded.

**Files that change:** `pipelines/p2_chirality/chirality_catalog_paper.tex`
only, plus the standard hygiene surfaces. **Compute required: none.**

---

## P5 — Grok (grok-4.3) `[MAJOR]` #1 — verbatim

Source: `INT_v3/ROUND_2026-07-23-P5-v0.1.142-2026-07-22-EXACTPDF-c2b72da7-CLAUDESTACK-RESWEEP/API_P5_grok.md` L17.

> [MAJOR] Section V B and abstract: Post-review/post-inspection re-ranking of the focal released GALZONE/OUT=0 estimator over the author-constructed any-hole path (explicitly declared as changed after data inspection) introduces selection bias risk in an otherwise exploratory analysis; the paper must add an explicit sensitivity table showing the any-hole result side-by-side with the focal estimate before claiming hierarchy independence.

This is a selection-bias / post-hoc-analysis charge, the class that legitimately
sinks a paper. It was audited as such, hardest-version-first, against the git
history rather than against the paper's own account of itself.

### The hard question, answered from chronology

**Was the estimator re-ranked after seeing results, in a way that could bias the
reported significance?** The re-ranking is real and is not disputed. Chronology,
reconstructed from git and the `.tex` changelog block (not from the prose):

| Version | Commit | Date | What changed |
|---|---|---|---|
| v0.1.129 | `f4c26f81` | 2026-07-14 | frozen chirality parent intersected with the released 694,642-TARGET DESIVAST GALZONE universe; covariate-adjusted + overlap-weighted controls fitted |
| **v0.1.130** | **`0842dfc6`** | **2026-07-14** | **"released GALZONE OUT=0 adjusted estimator promoted as the sole designated observational primary; any-hole/T-Web/Tempel/ASTRA demoted"** — the re-ranking itself |
| v0.1.131 | `e2e842d0` | 2026-07-14 | "designated primary" framing replaced by *focal exploratory/descriptive estimate*; estimand flow + model/covariance contract moved ahead of secondary results |
| v0.1.135 | `0a46753d` | 2026-07-15 | K=13/G=50 CR1 + 99,999-draw wild-cluster ADDED as sensitivities alongside the K=78 fit |
| **v0.1.136** | **`3e5e27bf`** | **2026-07-15** | **"promotes the rank-defensible K=13/G=50 CR1 + wild-cluster result to the focal estimator; demotes K=78"** — the nuisance-model change of MAJOR #2 |

So: post-review, post-inspection, confirmed, twice. There was never a
pre-registration to violate — `\S`V B tex L1508 states *"No timestamped analysis
plan predates inspection of these data."* That is the honest position, not a
dodge.

### Verdict on the bias half — **FALSIFIED** (and this is the decisive part)

The selection-bias hypothesis is that the author re-ranked toward the estimator
that best supports the headline. The headline is a **non-detection**, so the
most-favorable path is the one with the **largest** $p$. The paper did the
opposite. Verified against source on 2026-07-24:

| Path | $\Delta f_{\rm CW}$ | $p$ | Status in the paper | Source |
|---|---|---|---|---|
| Any-hole, unrestricted ($k=20$) | $+0.0007$ | **0.76** | demoted to sensitivity | Table XVII `tab:bonferroni5_family` row 1, tex L3676 |
| Any-hole, footprint-restricted (exact) | $+0.0018$ | 0.43 | demoted to sensitivity | §VIII B, tex L3188–L3192; Table XIII `tab:desivast_canonical` |
| **Focal released-parent, 13-column** | $+0.00145442$ | **0.66085** (wild-cluster 0.67345) | **promoted to focal** | Table VI `tab:focal_model_contract` L1869; §VI A L1519 |

The **most null-favorable path available ($p=0.76$) is the one that was
demoted.** A re-ranking driven by the result would have kept it. This is not an
argument from the paper's disclosures; it is arithmetic on the paper's own
tabulated numbers.

Three further checks, all passing:

1. **Nothing was suppressed.** The demoted any-hole result is retained in full —
   exact integer counts in Table XIII (tex L3164ff), $\Delta f$/SE/$z$/$p$ at
   tex L3188–L3192, a row in Table XVII, and named in the abstract with its
   sample size ($N_{\rm void}=57{,}081$, tex L937). Demotion ≠ deletion.
2. **The headline is algebraically monopole-invariant, so the parent swap cannot
   manufacture it.** The estimand is a *difference*,
   $\Delta f_{\rm CW}=f^{\rm non\text{-}void}-f^{\rm void}$; a uniform classifier
   monopole cancels exactly. §V B (tex L1541–L1551) states and uses this: the
   large raw $|\sigma_{\rm from\,half}|$ excursions ($-5.28$, $-4.75$) "measure
   the single catalog-wide classifier monopole … which is not the environmental
   null this paper tests"; monopole-subtracted the same regions return
   $|\sigma_{\rm obs}-\sigma_{\rm pred}|\le1.55$. Changing which parent defines
   the monopole therefore cannot move the environmental contrast except through
   composition — and the measured composition effect is 0.035–0.08 pp (below).
3. **There is no significance to bias.** Every path in the tree has $|z|<0.8$
   and a CI containing zero; the spread across the entire hierarchy is
   $\le 0.08$ pp against SEs of 0.23–0.33 pp. The whole-tree Bonferroni bound
   over the $N=23$ declared paths gives $p_{\rm global}\le0.82$ (§V B,
   artifacts [A45]/[A46]) — a selection-immune statement that already covers
   every path Grok is worried about.

**Grok's stated precondition is also not met.** The demand is triggered "before
claiming hierarchy independence." The paper claims the opposite, in the two
places Grok cites: abstract tex L992–L993 — *"not evidence for
environment-independence and not a physical, real-space, or model constraint"* —
and §V B tex L1531 — *"a null in this exploratory tree does not establish
environment-independence or an exclusion limit."* The re-ranking is disclosed in
the abstract (tex L936–L941), in §V B (L1508–L1513), and in the caption of
Table IV `tab:analysis_tree` (L1735).

### Verdict on the requested remedy — **GENUINELY-NEW-REAL** (bounded)

The bias charge is falsified; the *evidence artifact Grok asks for does not
exist*, and that half survives the falsification. Verified by enumerating every
table label in the source: **no single table places the focal estimate beside the
any-hole estimate.** The numbers live in Table VI (focal), Table XIII (any-hole
exact counts), §VIII B prose (any-hole $\Delta f$/SE/$p$), and Table XVII (five
void-definition variants, focal absent). Table XIV `tab:systematic_budget`
carries a "Sphere-PIS vs. GALZONE — 0.37 pp — membership sensitivity" row, which
is the closest existing artifact but is a sign-free magnitude with no SE or $p$.

A referee must currently assemble the comparison from four locations to check
that the hierarchy choice does not drive the null. Under AGENT_RULES §2.4 (in
doubt → the more severe bucket; "analysis already exists in the paper" is a
legitimate pushback only when it *does* exist as cited) this is a real,
closable evidence-presentation gap, and the closure is the thing that actually
answers the referee. Recording it as an OPINION and moving on would be the §4.6
dodge.

### Closure plan — **one table from already-computed numbers. NO re-analysis, NO compute, $0.**

Owner: the P5 lane. Target version **v0.1.144 → v0.1.145**.

1. Add `tab:hierarchy_sensitivity` in §V B `sec:primary_path`, immediately after
   the post-hoc hierarchy-change paragraph (tex L1508–L1513) — i.e. at the exact
   place the referee reads the disclosure. Three rows, all values transcribed
   from existing artifacts, none recomputed:

   | Path | $\Delta f_{\rm CW}$ | SE | 95% CI | $p$ | Source artifact |
   |---|---|---|---|---|---|
   | Focal released-parent OUT=0, 13-col adjusted | $+0.00145442$ | $0.00331502$ | $[-0.00504290,+0.00795174]$ | $0.66085$ (wild-cluster $0.67345$) | [A41]–[A44] |
   | Any-hole, footprint-restricted (exact) | $+0.0018$ | $0.0023$ | $[-0.0027,+0.0064]$ | $0.43$ | [A15] |
   | Any-hole, unrestricted ($k=20$) | $+0.0007$ | — | $[-0.0036,+0.0050]$ | $0.76$ | [A10] |

2. Add two sentences under it: (a) the maximum spread across the hierarchy is
   0.035 pp (focal ↔ footprint-restricted) and 0.08 pp (focal ↔ unrestricted),
   both far inside every quoted SE; (b) **the demoted unrestricted path carries
   the larger $p$ (0.76 vs 0.66085)** — state plainly that the re-ranking moved
   *away from* the most null-favorable option, which is the direct answer to the
   selection-bias reading. Do not soften this into a caveat; it is a
   verifiable claim about the paper's own numbers.
3. Cross-reference the new table from the abstract's hierarchy-change sentence
   (tex L936–L941) and from Table IV's caption.
4. Directive-G chain + `/latex-audit` + mirrors + Convex; append the closure to
   `DISPOSITIONS/P5.md` (new D-id; DP5-13 is the bias class and stays
   RE-FLAG-DISCLOSED, the new id is the consolidation closure).

**Files that change:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`
only, plus hygiene surfaces. **Compute required: none — every number already
exists in [A10], [A15], [A41]–[A44].**

---

## P5 — Grok (grok-4.3) `[MAJOR]` #2 — verbatim

Source: same leg, L18.

> [MAJOR] Section VIII A and Table VI: The focal 13-column linear nuisance model (and its NSIDE=4 cluster sandwich) is declared "post-review"; the manuscript must state the pre-review model specification and show that the null conclusion is unchanged under the originally planned spline/fixed-effect specification.

### Verdict — **FALSIFIED** (the requested content is in the very table the finding cites)

Grok's own pointer resolves it. Table VI is
`tab:focal_model_contract` (tex L1863; confirmed as "TABLE VI" in the rendered
PDF via `pdftotext -layout`, /tmp cross-check 2026-07-24), and it already
carries the pre-existing specification and its result as a dedicated row:

> **Flexible sensitivity [A37]** — 78-column spline/fixed-effect model with
> Moore–Penrose bread inverse, $G=50$ NSIDE$=4$ clusters:
> $\Delta f_{\rm CW}=+0.00125636$, ${\rm SE}=0.00341274$, 95% CI
> $[-0.00543249,+0.00794522]$, normal $p=0.71277$; rank-fragile because
> $K=78>G=50$
> — tex L1871, verbatim

That is: the spline/fixed-effect specification is stated, its contrast is
reported, its interval contains zero, and its $p=0.71277$ is a non-detection —
i.e. "the null conclusion is unchanged," exactly the demonstration demanded. The
surrounding prose states the same in words at tex L1828 ("The older A37
spline/sky-fixed-effect model is retained only as the flexible sensitivity in
Table VI") and tex L1882–L1885 (the K=78 fit "is retained only as a
flexible-model sensitivity, not as the headline interval"). §2.4's second
legitimate-pushback clause applies verbatim: *"Analysis already exists in the
paper (cite section / equation / appendix)."*

**The finding's premise is additionally wrong, and this matters.** There is no
"originally planned" specification. The 78-column spline/fixed-effect fit is not
a pre-review plan — it is the *earlier post-review* fit on the same post-review
released-parent construction (v0.1.131 `e2e842d0`, 2026-07-14 → demoted at
v0.1.136 `3e5e27bf`, 2026-07-15). The construction it fits did not exist before
review. The paper says so at tex L1880–L1881: the 13-column specification "was
declared after review and inspection of the data and is therefore exploratory,
not preregistered." Grok is asking the paper to produce a pre-registration the
paper explicitly and correctly denies having.

**Direction check, same test as MAJOR #1 and same answer.** The switch moved the
reported $p$ from **0.71277 (K=78) → 0.66085 (K=13)** — again *away from* the
more null-favorable value. The point estimate moved $+0.00125636 \to
+0.00145442$ (0.02 pp); both CIs contain zero. The stated rationale is
structural and result-independent — $K=78>G=50$ makes the CR1 normal
approximation rank-fragile, so the K=13 fit is the only one admitting both CR1
*and* null-imposed wild-cluster inference (tex L1877–L1885). Robustness of the
adopted fit is tabulated at NSIDE = 2, 4, 8 and under 3,750 nearest-MAXIMALS 3-D
clusters, point estimate $+0.00145442$ throughout, every interval containing
zero (Table VI, [A43]–[A44]).

**No closure work. No compute.** The correct handling is a source-cited response
line in the round reply, not an edit. Append as a new RE-FLAG-DISCLOSED D-id in
`DISPOSITIONS/P5.md` with the Table VI L1871 citation and the fingerprint
`13-column, 78-column, spline, fixed-effect, A37, pre-review, nuisance, Table VI`
so the next wave auto-matches it instead of re-deriving this.

---

## Honest per-paper convergence statement — 2026-07-24

- **P4 — NOT CONVERGED.** One genuinely-new-real MAJOR outstanding (Gemini,
  inline provenance in narrative). It is a prose/structure closure with zero
  compute, but it is unclosed, and it was twice dismissed on style grounds
  before it escalated. P4 becomes evidenced-converged on active legs when
  v1.0.272 lands with the relocation + provenance table and the directive-G
  chain passes. **P4 is also the paper this campaign's D3 back-patch gate on P5
  waits on, so this is on the critical path for both.**
- **P5 — NOT CONVERGED.** Of the two Grok MAJORs: #2 is FALSIFIED and needs no
  work; #1 splits — its selection-bias charge is FALSIFIED on the paper's own
  arithmetic (the demoted path carries the larger $p$), but its requested
  side-by-side sensitivity table is GENUINELY-NEW-REAL and unclosed. P5 becomes
  evidenced-converged on active legs when v0.1.145 lands
  `tab:hierarchy_sensitivity`. The two pre-existing tracked gates
  (Paper-IV back-patch, P5 deposit DOI) are unchanged and remain
  ALREADY-TRACKED-GATE, not convergence blockers under directive M-AMENDED.
- **P1A / P1B / P2 / P3 — unchanged from the corrected line above:** 0
  genuinely-new-real outstanding on ACTIVE legs (P1B via the v2B.0.16 closure
  recorded earlier in this document).

**The 2026-07-23 "0 genuinely-new-real across all six papers" line is
definitively retired.** The evidenced state on 2026-07-24 is: four papers clear,
two papers each carrying exactly one open genuinely-new-real item, both of them
closable with prose/table work and no compute.

**Completeness re-check after this pass** (the check the 07-23 pass lacked):

| Paper | MAJORs in raw across all legs | MAJORs dispositioned | Match |
|---|---|---|---|
| P1A | 0 | 0 | ✔ |
| P1B | 1 | 1 | ✔ |
| P2 | 0 | 0 | ✔ |
| P3 | 0 | 0 | ✔ |
| P4 | 1 | 1 | ✔ |
| P5 | 5 (Gemini 3 + Grok 2) | 5 | ✔ |
| **Total** | **7** | **7** | **✔** |

0 `[BLOCKER]` tags anywhere in the round. All 18 legs present and non-empty.

## Process fix landed (2026-07-24)

The verdict-word-vs-item-tag bug is encoded so it cannot recur silently:

- `~/.claude/scistack/hubstack/learning-loop/peer-review-truth-audit/SKILL.md` —
  new **Rule 8** (severity is read from per-item tags, never from the leg's
  summary verdict word) + a mandatory completeness table in the hard gates.
- `~/.claude/scistack/hubstack/learning-loop/review-integrity-audit/SKILL.md` —
  new **CHECK 0 — DISPOSITION COMPLETENESS**, run before the three bias checks;
  an incomplete disposition set is an automatic ENGINEERED verdict.
- `~/.claude/scistack/astrostack/bigbounce-r-round/SKILL.md` — §3 severity-source
  rule and a §5 gate precondition requiring the paper × leg × MAJORs-in-raw ×
  MAJORs-dispositioned table to balance before any convergence claim.
- `tools/major_completeness_check.py` — machine-checkable version; exits 2 with
  the offending rows when raw and dispositioned counts disagree.

---

# ADJUDICATION of an EIGHTH missed MAJOR — P5 / Gemini §VI.E.d — 2026-07-24

**Provenance, recorded because it is the point.** This item was missed **twice**:
once in the original 2026-07-23 pass, and again in the 2026-07-24 completeness
adjudication above — the very pass whose stated purpose was to find exactly this
class of gap, and whose closing table asserts "P5 · 5 MAJORs in raw · 5
dispositioned · ✔". It was surfaced by `tools/major_completeness_check.py`, the
executable gate built in that same pass:

```
$ python3 tools/major_completeness_check.py \
    project-context/peer-reviews/INT_v3/ROUND_2026-07-23-P5-…-RESWEEP \
    --audit project-context/peer-reviews/INT_v3/TRUTH_AUDIT_RESWEEP_2026-07-23.md
API_P5_gemini.md          0      3      2  MAJOR REVISIONS
API_P5_grok.md            0      2      2  MINOR REVISIONS  <-- verdict word understates item tags
CLAUDE_INT_P5_raw.md      0      0      1  MINOR-REVISIONS
TOTAL across 3 legs: 0 BLOCKER, 5 MAJOR
INCOMPLETE — 1 tagged item(s) with no trace …  (exit 2)
```

**The executable gate outperformed two human-directed manual passes on the same
round.** That is the durable finding here, independent of how this particular
item adjudicates.

## The MAJOR — verbatim

Source: `INT_v3/ROUND_2026-07-23-P5-v0.1.142-2026-07-22-EXACTPDF-c2b72da7-CLAUDESTACK-RESWEEP/API_P5_gemini.md` L18.
Leg present and non-empty; exact-PDF binding sha256 `c2b72da7b8b5…` matches the
round manifest; model `gemini-3.1-pro-preview`.

> 2. **[MAJOR] Section VI.E.d (Target-program leakage and deferred mocks):** The manuscript identifies a $\sim 2.1\sigma$ sign-flip in the filament class between BGS-bright and dark targets. The text attributes this to imaging-leg and BGS-selection-function systematics but explicitly declines to run the required "end-to-end injection–recovery mock" to prove this, deferring it to a "DR2 validation step." Relying instead on a "bounded surrogate" leaves residual ambiguity. If the mock cannot be run for DR1, this un-modeled leakage and the residual ambiguity regarding a program-by-environment interaction must be much more prominently caveated in the abstract and conclusion.

## First: is the gate reporting a false positive? **Partly — and the flag was still correct in substance.**

Honesty first, because a false positive in a new gate is itself a finding. The
item is **not** wholly untraced. The 07-23 pass contains one line touching it,
under DISCLOSED-RE-FLAG:

> P5 Gemini MAJOR-2 (deferred DR2 mock): the paper's own disclosed limitation;
> bounded-surrogate injection [A47]/[A48] closure stands (DP5-19 class).

So the checker's literal message — "no trace in the audit" — is **wrong**, and
the mechanism is exactly the documented one: `--audit` is a token-overlap
heuristic at `--threshold 0.40`, and the 07-23 line paraphrases so heavily that
the item's distinctive tokens are all absent. Measured overlap for the three
Gemini MAJORs against the pre-existing audit text: **0.421 (MAJOR-1, passes),
0.275 (MAJOR-2, flagged), 0.486 (MAJOR-3, passes)**. The tokens the paraphrase
drops are `leakage`, `target-program`, `sign-flip`, `filament`, `BGS-bright`,
`program-by-environment`, `interaction`, `end-to-end`, `recovery`, `surrogate`,
`caveated`. The tool behaved exactly as its docstring promises and its threshold
was not lowered.

**But the flag was substantively right anyway, for a reason the tool cannot see:
the 07-23 disposition is *partial*.** Gemini's finding is a conditional with two
limbs — (a) the deferred DR2 mock, and (b) *"If the mock cannot be run for DR1,
this un-modeled leakage and the residual ambiguity regarding a
program-by-environment interaction must be much more prominently caveated in the
abstract and conclusion."* The 07-23 line dispositions limb (a) and is silent on
limb (b) — it disposes of the excuse for the remedy while never adjudicating the
remedy. Since the mock indeed was not run for DR1, limb (b) is the **operative**
half of the finding, and it had no verdict. **Net: a low-precision flag that
landed on a real, still-open item. Reported as such rather than dismissed as
tool noise — and rather than papered over as "already dispositioned."**

## Verdict — **DISCLOSED-RE-FLAG** on the leakage mechanism (DP5-14/DP5-19, verified against v0.1.145) + **GENUINELY-NEW-REAL** on the operative remedy limb

Under AGENT_RULES §2.4 (ambiguous → the more severe bucket) the operative
disposition is **GENUINELY-NEW-REAL**, and it closes with a real edit.

### Taking "leakage" seriously — what §VI.E.d actually does, and whether a leakage path is real

**It is not ML target/label leakage, and that distinction is load-bearing.**
"Target program" here is the DESI *target selection program* (BGS-`bright` vs
LRG/ELG/QSO-`dark`), not the target variable. Checked directly rather than
assumed:

| Leakage path | Verified against | Real? |
|---|---|---|
| Outcome → exposure definition | `class_eq` CW/CCW labels come from Paper IV's ViT trained on GZ1/SDSS human labels (App A); void membership comes from the externally released DESIVAST VoidFinder hole catalog (Rincón et al. 2025, ApJ 982; tex L2979) | **No path** — neither input can see the other |
| Author-tuned parent chosen to suppress the residual | The focal parent is catalog-native: released GALZONE `TARGET` universe (694,642 TARGETIDs) ∩ `OUT`$=0$ ∩ exact VoidFinder hole-union (tex L1879ff). Its volume-limited $z\le0.24$ restriction — the property that "minimizes target-program mixing by construction" (tex L4637) — is **inherited from the external DESIVAST release**, not an author cut | **No** — the mixing-minimization is a property of a published external catalog |
| Chronology: was the program residual known before the parent was fixed? | Yes, and it is disclosed. The bright/dark split landed 2026-05-22 (`207737c9`, v0.1.14); the released-parent construction landed 2026-07-14 (`f4c26f81`, v0.1.129) | Known-but-benign: the parent is externally defined, and the truth audit's direction check above shows the re-ranking moved toward the **smaller** $p$ |
| Selection-program systematics contaminating the environment contrast | **Real, and the paper says so.** BGS-`bright` $f_{\rm CW}=0.4970$ vs `dark` $0.5051$ (0.81 pp, $\vert z\vert=1.95$ unique-galaxy, tex L4629); T-Web class is *not* independent of the split ($\chi^2=4933$, Cramér's $V=0.078$, tex L2478) | **Yes — a genuine residual** |

On the last row, the paper's handling is substantive, not rhetorical:

1. **The focal estimand is algebraically monopole-invariant** — it is a
   *difference*, $\Delta f_{\rm CW}=f^{\rm non\text{-}void}-f^{\rm void}$, so a
   uniform classifier monopole cancels exactly (`sec:p4`, tex L1541–L1551). A
   program-*mean* offset therefore cannot manufacture the contrast.
2. **The marginal-mixture term is bounded and tiny** — void 0.82% dark vs
   non-void 0.94% dark is a 0.12 pp differential, so the induced scale is
   $0.81\,{\rm pp}\times0.0012\approx0.001$ pp, three orders below the focal
   interval (tex L2578–L2586). The paper states explicitly that this is
   **not a maximum leakage bound** and does not constrain an interaction.
3. **The interaction is honestly *not* bounded.** [A43]–[A44]
   (`scripts/39_focal_interaction_clustering_robustness.py`, which does fit
   `void * C(program)` — verified in the pipeline code) gives a
   `dark`-minus-`bright` void contrast of $+0.09776$ on $n_{\rm dark}=237$ with
   95% CI $[-0.06637,+0.26190]$; the `other` stratum occupies one NSIDE$=4$
   block and admits no angular cluster inference. Note also that **`program` is
   not among the focal 13 nuisance columns** (tex L1913–L1922: void, $z$, $r$,
   $\log R$, confidence, extinction, `PHOTSYS`, morphology, GALZONE edge) — the
   residual is handled by sensitivity, not by adjustment.
4. **The declined mock is correctly scoped** — it bears on the **secondary**
   T-Web diagnostic sign-flip, not on the focal contrast (tex L2509–L2512).
5. **The bounded surrogate is real and committed** — `tab:forward_leakage` /
   [A47]–[A48] forward-predicts each large deviation from the committed
   per-program monopoles and reproduces **88% of the filament bright-vs-dark
   sign-flip** ($z_{\rm pred}=-1.87$ vs $z_{\rm obs}=-2.13$, residual $z=-0.26$),
   with 77–133% coverage across rows and every residual non-significant.

**Conclusion on the mechanism half: DISCLOSED-RE-FLAG of DP5-14 (T-Web /
selection contamination, the class the bright/dark sign-flip has mapped to since
M6) and DP5-19 (adjustment-in-lieu-of-regression), and the disposition still
holds at v0.1.145.** No re-analysis is required and none is manufactured.

### Why the remedy limb is nevertheless GENUINELY-NEW-REAL

The paper's own most severe statement about this residual lives at
`sec:systematics`, tex L4632–L4646:

> "This residual **has not been shown to leave the focal DESIVAST result
> unaffected**" … "so **substantial program-by-environment interaction effects
> are not excluded**."

That sentence was already present in the reviewed v0.1.142 (added at
`81b7bd56`), so Gemini read it and asked for prominence anyway — correctly.
Verified by grep over the **live text** of v0.1.145 (`%`-comment regions
excluded):

| Surface | Occurrences of program / leakage / interaction / bright / dark |
|---|---|
| Abstract (tex L951–L980) | **0** |
| §XIII Limitations `sec:limitations` (tex L4741–L4920) | **0** |
| §XV Conclusions `sec:conclusions` (tex L4934–L5077) | **0** |

So the body concedes an unexcluded systematic that it cannot show leaves the
focal result unaffected, while the abstract, the Limitations list — the canonical
place a referee looks for exactly this — and the Conclusions are all silent. An
abstract-only reader gets a stronger null than the body supports. That is the
`/review-integrity-audit` Check-3 failure mode (headlining the more favorable of
two available readings), not a presentation preference, and AGENT_RULES §2.4
forbids disposing of it as SCOPE-VENUE-OPINION. **GENUINELY-NEW-REAL.**

**The local incentive was to make this go away** — P5 had just closed two Grok
MAJORs and the sixth-paper table was about to balance. It is recorded instead.

### Closure — v0.1.145 → **v0.1.146** (2026-07-24). Prose only. No re-analysis, no compute, $0.

Every value transcribed from text already in the manuscript; **zero reported
numbers changed**; no new derivation (`/never-fabricate-derivation` clean).

1. **Abstract** — the caveat sentence now reads "…T-Web intervals omit cosmic
   variance and spatial covariance, all environment assignments remain in
   redshift space, **and a target-program-by-environment interaction is not
   excluded.**" Rendered abstract **244 words**, under the AAS/AJ 250-word cap
   (measured on `pdftotext` output of the compiled page 1, not on source).
2. **§XIII Limitations** — new bullet *"Unmodelled target-program leakage; a
   program-by-environment interaction is not excluded"* carrying the 0.81 pp /
   $\vert z\vert=1.95$ residual, the $\chi^2=4933$ / $V=0.078$ non-independence,
   **both** partial bounds with their limits stated (0.12 pp differential →
   $\approx$0.001 pp marginal mixture, explicitly not a maximum bound; the
   [A43]–[A44] fit with its $n=237$ dark stratum, $[-0.06637,+0.26190]$ CI, and
   single-block `other` stratum), the [A47]–[A48] surrogate at 77–133% coverage,
   and the deferred DR2 mock — closing "Readers should treat the focal
   non-detection as conditional on that unclosed systematic."
3. **§XV Conclusions** — new sentence: "One systematic remains open rather than
   bounded… so the focal non-detection is conditional on that unclosed
   systematic."

**Directive-G hygiene (all verified 2026-07-24, `tools/directive_g.sh` PASS):**
`\paperVersion` v0.1.146-2026-07-24 + `\paperTimestamp` July 24, 2026, 19:05 PT
+ `\date` macro-bound · recompile **0 undefined refs / 0 errors / 0 Overfull
`\hbox` / 0 Overfull `\vbox`**, 43 pages (P5's overfull count stays at 0) ·
leak-gate clean · §4.7 visual audit: pages **1, 34, 35** (page 1 + every changed
page) rendered at 110 dpi with `pdftoppm` and read — no column overflow, no
gutter crossing, `\date` on one line, all new cross-refs resolve (§XI, §VI E,
§XIII, §XIV, Table XI) · mirrored byte-identical (md5
`3717017920458a944a2a8bfa7de17d7d`) to **13 served paths, 1 distinct md5** ·
append-only retention snapshot
`project-context/pdf-archive/manifests/2026/07/20260725T020559Z-a9154145681c.json`
· Convex `paperVersions:bump` row `k57b2h4r6zpnv14zsgbxzmybhs8b62bm`, read-back
verified current == v0.1.146-2026-07-24 / md5 match · arXiv tarball rebuilt as
`project-context/SSOT/arxiv_tarballs/paper5_arxiv_v0.1.146-2026-07-24.tar.gz`
(11 members, same convention as v0.1.143/144/145) and **standalone-compiled in an
isolated `/tmp` extract with no repo on the path**: 0 errors, 0 undef refs, 0
overfull hboxes, 0 overfull vboxes, 43 pages, page 1 carrying
`v0.1.146-2026-07-24`; proof
`paper5_arxiv_v0.1.146-2026-07-24.proof.json`.

Ledger: `DISPOSITIONS/P5.md` — **DP5-28** (this closure), plus the two sub-items
the P5 lane left open for want of write ownership: **DP5-27** (the v0.1.145
`tab:hierarchy_sensitivity` closure of Grok MAJOR #1, including the reasoned
**decline** of the abstract cross-reference — AAS 250-word cap, `\ref` unresolvable
in standalone abstract rendering, and the cross-ref's purpose already served by
the `sec:primary_path` pointer sentence and the `tab:analysis_tree` caption) and
**DP5-29** (Grok MAJOR #2, FALSIFIED, fingerprinted so the next wave auto-matches).

## Corrected completeness table — after this pass

| Paper | MAJORs in raw across all legs | MAJORs dispositioned | Match |
|---|---|---|---|
| P1A | 0 | 0 | ✔ |
| P1B | 1 | 1 | ✔ |
| P2 | 0 | 0 | ✔ |
| P3 | 0 | 0 | ✔ |
| P4 | 1 | 1 | ✔ |
| P5 | 5 (Gemini 3 + Grok 2) | 5 | ✔ |
| **Total** | **7** | **7** | **✔** |

The counts are unchanged from the table above — **the earlier table was not
wrong about the arithmetic; it was wrong that a paraphrase one clause wide
constitutes a disposition.** The gate's residual weakness is therefore not its
false-positive rate but the reverse: a *partial* disposition that happens to
share enough tokens will pass it silently. Recorded as a known limit of
`--audit`, not fixed by threshold tuning.

## Honest P5 convergence statement — 2026-07-24, superseding the line above

**P5 — evidenced-converged on ACTIVE legs as of v0.1.146.** All five
2026-07-23 `[MAJOR]` tags now carry source-cited verdicts: Gemini-1 and Gemini-3
ALREADY-TRACKED-GATE (Paper-IV back-patch; P5 deposit DOI), Gemini-2
DISCLOSED-RE-FLAG + GENUINELY-NEW-REAL **closed v0.1.146** (DP5-28), Grok-1
FALSIFIED-bias + GENUINELY-NEW-REAL **closed v0.1.145** (DP5-27), Grok-2
FALSIFIED (DP5-29). 0 `[BLOCKER]` anywhere. The two tracked gates remain
ALREADY-TRACKED-GATE and are not convergence blockers under directive M-AMENDED.
**P4 is unchanged and still NOT CONVERGED** — its Gemini `[MAJOR]` closure plan
(v1.0.272) belongs to the P4 lane and was not touched here.
