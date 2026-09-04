# Paper lineage: where every paper concept went

**Date:** 2026-08-05
**Scope:** Directive Q4 (`CLAUDE.md`) — "Nothing viable gets lost." Any
narrowing/split/retirement of a paper must preserve a documented disposition
trail; periodically audit history for viable unpublished science and either
resurrect it under a program or record explicitly why not.

**This document is that audit's record.** It is the canonical answer to "what
happened to X paper/section/claim" going forward — check here before
re-deriving, re-litigating, or assuming something is lost. It supersedes
memory and assumption; every claim below cites a file, and every file was
opened and checked before being cited, not re-derived from the git log alone.

Tone note, matching `project-context/PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`:
this is a blunt inventory, not a marketing document. Some of it says "this was
correctly cut and should stay cut." Some of it says "this was cut for
process reasons unrelated to its scientific merit and Houston should decide
whether to revive it."

---

## 1. Purpose

The Big Bounce program has gone through repeated splits, salvages, and
narrowings since March 2026: a broad Paper 1 became P1A + P1B, a
268,519-outlier anomaly draft became a public-ID recovery note, a "14 no-go
pathways" catalog was retired at the P1 split, and more. Each of these was a
legitimate scientific or editorial decision at the time it was made. But
"legitimate at the time" is not the same as "nothing worth publishing was
left on the floor," and directive Q4 exists precisely because this program
has cut real content for reasons (claim-discipline, scope, review pressure)
that are about the *container* the content was in, not the content's
validity.

This document is the audit trail. Section 2 is the lineage table. Section 3
gives the narrative for each concept. Section 4 makes explicit resurrection
recommendations, applying directive Q1 (pure-contribution framing — a
resurrected paper must be framed as a positive result, not as "here's what we
messed up and are now fixing"). Section 5 directly answers the three things
Houston flagged as possibly missing.

---

## 2. Lineage table

| Concept | Origin | Current disposition | Preserved location | Viable-unpublished-content verdict |
|---|---|---|---|---|
| 14-barrier / 13-mechanism-class no-go catalog | `arxiv/paper1_unified.tex` §`sec:barriers` (P1U, frozen 6,898-line pre-split draft) | Retired from the live paper at the P1 split (2026-07-14); not carried into P1A or P1B | `arxiv/paper1_unified.tex` lines 3529–3900ish (`tab:barriers`, `fig:barrier_map`, per-barrier `\item[B1]`…`[B14]` details); ancestor derivation in `research/paper1_salvage_alp/01_salvage_map.md`, `05_claims_table.md`, `final_verdict.md` (2026-03-17) | **Viable, unpublished. Resurrection recommended — see §4(a).** |
| R2/R3 dark-energy route closures | Same §`sec:barriers`, Table `tab:barriers` rows mapping Foundations A–G / Branches H,J,L,M,N,O to Routes R1–R4 | Retired with the barrier catalog at the P1 split | `arxiv/paper1_unified.tex` (TikZ figure `fig:barrier_map`, ~lines 3596–3665) | Bundled into the same no-go survey — not separable from §4(a) |
| Operator-basis-completeness argument | Same section, B10 (UV→IR specificity) and related naturalness barriers | Retired with the barrier catalog | `arxiv/paper1_unified.tex` B5/B6/B7/B10/B13 descriptions (general naturalness/classification arguments, explicitly labeled as such in-text) | Bundled into §4(a) |
| Galaxy-spin dipole null (Shamir CW/CCW) | P1U §`sec:data_galaxy`, citing Shamir 2022/2024 CW/CCW counts | The *primary* analysis (classifier, catalog, dipole significance) already lives in **Paper IV** (`Golden2026P4`), which is live and in the active roster. P1U only cited P4's result as motivation. | `arxiv/paper1_unified.tex` lines ~3414–3429 (references Paper IV, does not duplicate the analysis) | Not orphaned — it's a working citation into a live paper. See §4(b) for the narrow framing point. |
| Spectator-ALP birefringence (β≈0.27°) | `research/paper1_salvage_alp/final_verdict.md` (2026-03-17) — ancestor of the P1 program | **Survived and shipped** into P1B | `arxiv/paper1b_mcmc_companion.tex` (see row below) + `arxiv/paper1b_namaster_proof.tex` lineage | Not an orphan — already published, no action |
| Multi-survey anomaly draft (268,519 outliers / 37.3M scanned) | `pipelines/p3_anomaly_engine/paper3_draft.tex` | Deprecated in favor of a narrow, public-ID-first DESI catalog note, committed at `3f5582c2` ("docs(p3): publish focused DESI catalog manuscript", 2026-07-14) | `pipelines/p3_anomaly_engine/paper3_draft.tex` (old draft, left in place as history); live paper is `pipelines/p3_anomaly_engine/paper3_apjs.tex` | Correctly narrowed for provenance reasons — genuine discovery science is being rebuilt, see next row |
| DESI DR1 anomaly discovery science | `pipelines/p1_highz_tracers/`, `projects/desi-dr1-anomalies/` | **Actively rebuilding**, not lost. Sealed-contract "AUG-011" clean rerun in progress (contract sealed commit `568a33bf`, 2026-08-05) | `project-context/ANOMALY_FLAGSHIP_MANUSCRIPT_ARCHITECTURE_2026-08-05.md`, `project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md`, `project-context/SSOT/queue.md` item 3 | Not an audit target — already being actively resurrected |
| P1B MCMC companion manuscript | `arxiv/paper1b_mcmc_companion.tex` | **Alive and registered**, but not surfaced as its own paper card on the site — only a secondary "Legacy validation dossier" link under the P1B *namaster-proof* entry | `arxiv/paper1b_mcmc_companion.tex`/`.pdf`; registry entry `project-context/paper_registry.json` → `companion_manuscripts.P1B-MCMC`; site link `site/src/data/papers.ts` line 277 | Not lost, but the registry itself flags a real gap — see §5 |
| "Paper 7" self-improving-review meta-paper | Idea only | Never drafted | `project-context/FUTURE_PAPERS.md` lines 8–90 (two working variants: an academic methods paper and a Hubify marketing case study) | Idea-stage only — no content to lose, no action needed beyond what `FUTURE_PAPERS.md` already tracks |
| Golden 2026 geometric-dark-energy PDF (v2.1.0 per audit brief) | Public download `public/downloads/golden-2026-geometric-dark-energy-spin-torsion.pdf` | **Could not locate the file anywhere in the current repo tree** (checked `public/downloads/`, `backups/`, `versions/`, full-tree `find`). Only surviving reference is in two old snapshot docs describing it as "v1.2.0, current" as of March 4 | `research/final_paper_prep/website_data_snapshot.md`, duplicate in `research/final_paper_prep/review_package_20260309_1852/website_data_snapshot.md` | Content is not separately valuable — it was an early full draft of what became P1U/P1A/P1B; the science is accounted for elsewhere in this table. Flagging the missing file as a housekeeping note, not a resurrection candidate. |
| `paper3_barriers_ech_transparency` companion note | Standalone barrier-catalog write-up | Superseded — content folded into P1U's `sec:barriers`, then retired with it at the P1 split | `research/focused_paper_source_integration/paper3_barriers_ech_transparency.pdf`/`.tex` (dated 2026-06-26) | Same disposition as §4(a) — this file is one of the source artifacts for the resurrection candidate |

---

## 3. Detailed per-concept sections

### 3.1 The 14-barrier / 13-mechanism-class no-go catalog

**What it was.** A systematic survey of every route the minimal
Einstein–Cartan–Holst (ECH) framework could plausibly use to derive dark
energy internally. `arxiv/paper1_unified.tex` §`sec:barriers` (label
`sec:barriers`, beginning line 3529) tests 7 "foundation" mechanism classes
(A–G) and 6 observational branches (H, J, L, M, N, O), producing 14 catalog
entries that the text is explicit collapse to **13 distinct mechanism-class
constraints** (B8 is subsumed by B14 — both close the same
primordial-tensor-chirality channel). These feed into four closed dark-energy
routes, R1–R4, shown in a TikZ flow figure (`fig:barrier_map`) and a formal
table (`tab:barriers`, `\begin{table*}`). Two entries (B1 torsion
mass-coupling lock, B14 perturbation transparency) are first-principles
derivations; the rest are naturalness/classification arguments or one
heuristic closure (B9, Liouville conservation), and the text is careful to
label the difference in-line rather than overclaim uniform rigor.

**Why it narrowed.** `project-context/peer-reviews/INT_v3/ROUND_2026-07-13-M44-NONANTHROPIC/P1_SPLIT_CLOSURE.md`
(2026-07-14) records the decision: M44 non-Anthropic external review found
that P1U's broad four-route rhetoric didn't match what was actually derived
with rigor. Rather than relabel the mismatch, the closure cut everything not
tightly supported. P1A was reduced to three retained results (torsion
elimination, the Planck-suppressed axial contact operator, and a classical
transparency identity on one branch); the barrier catalog, R2/R3 closures,
operator-basis-completeness rhetoric, ALP/MCMC material, and the galaxy
payload were all explicitly retired from the reader-visible paper. The
closure doc says this plainly: "Reader-visible R2/R3 dark-energy closures,
operator-basis-complete rhetoric, single-scale dark-energy ansatz,
ALP/NaMaster/MCMC material, barrier catalog, galaxy payload, and forecast
claims were retired."

**Where the content sits.** Nothing was deleted — `arxiv/paper1_unified.tex`
was explicitly *not edited* by the split closure ("Historical unified
source... was not edited"). The full 14-entry catalog, the formal table, the
TikZ figure, and all per-barrier prose are intact at their original line
numbers. An earlier ancestor version (13 barriers, dated 2026-03-17, before
the fourteenth was added) lives in `research/paper1_salvage_alp/01_salvage_map.md`,
`05_claims_table.md`, and `final_verdict.md`, which independently concluded
this was one of the two strongest results in the whole salvage effort (the
other being the spectator-ALP birefringence prediction, which did ship). A
standalone write-up also exists at
`research/focused_paper_source_integration/paper3_barriers_ech_transparency.tex`/`.pdf`.

**What would be needed to resurrect it.** The catalog is already written,
tabulated, and figured — the work is extraction and reframing, not
re-derivation. See §4(a).

### 3.2 Galaxy-spin dipole null (Shamir CW/CCW)

**What it was.** P1U cites a Vision-Transformer chirality classifier applied
to DESI Legacy Imaging galaxies, testing Shamir's (2022/2024) claimed 1–3%
CW/CCW asymmetry. P1U's own text (lines ~3414–3429) is explicit that this
analysis — catalog construction, sample size, validation accuracy, bias-audit
suite, and dipole significance — is reported in **Paper IV**
(`Golden2026P4`) and *not duplicated* in P1U. The stated result: the all-sky
dipole is null on the spiral-classified subsample, and Shamir's 3% claim is
disfavored by a factor of ~6–12 (matched-footprint reanalysis needed for a
likelihood-level exclusion).

**Disposition.** This is not an orphaned result — P4 is live, in the active
six-paper roster, and already carries the primary analysis. P1U's mention is
a citation, not independent content. The only "loss" from the P1 split is
that the no-go catalog's own narrative thread connecting the null result to
"one more closed route" disappeared along with the rest of §`sec:barriers`.

### 3.3 Multi-survey anomaly draft → narrow P3

**What it was.** `pipelines/p3_anomaly_engine/paper3_draft.tex` is a draft
manuscript built around a much larger claim: 268,519 validated outliers out
of a 377,482-row (stated in the abstract as "37.3M" scanned-volume) DESI/LAMOST/SDSS-cross-survey
scan. The file's own changelog comments (lines 63–211) show this number was
under sustained internal/external review pressure over multiple rounds —
provenance reconciliation issues (LAMOST released-but-excluded rows, Gaia
excision, "37.3M vs 36.93M" read/scored mismatches) kept surfacing.

**What replaced it.** Commit `3f5582c2` ("docs(p3): publish focused DESI
catalog manuscript", 2026-07-14) cut `pipelines/p3_anomaly_engine/paper3_apjs.tex`
from 2,387 lines of the old broad framing down to a public-ID-first,
provenance-first catalog note (813 net insertions replacing 1,777 deletions,
plus a new `P3_structural_recovery_closure.md`). This is the live P3 today.

**Where the discovery science actually lives.** `pipelines/p1_highz_tracers/`
and `projects/desi-dr1-anomalies/` hold the working pipeline and catalog code
for the genuine anomaly-discovery program, and it is being actively rebuilt
under a sealed-contract clean rerun ("AUG-011," contract sealed 2026-08-05,
commit `568a33bf`, completed 2026-08-07 with 36,634 verified receipts,
45.5h wall-clock, about $7.74 total cost, and 52,188 `S>5` candidates). The
plan for the rebuilt flagship manuscript is
`project-context/ANOMALY_FLAGSHIP_MANUSCRIPT_ARCHITECTURE_2026-08-05.md`,
itself derived from `project-context/ANOMALY_SCIENCE_CLAIM_INVENTORY_2026-08-03.md`
and `project-context/SSOT/queue.md` item 3. That architecture doc is explicit
that no number in it was invented — every historical figure is lifted from
the inventory and every new-generation number is reserved for the follow-on
selected sample, cross-match, and taxonomy stages.

**Disposition verdict.** Correctly narrowed. This is not a case of losing
viable content — the old draft's headline numbers had real, disclosed
provenance problems, and the actual discovery-science program is not
abandoned, it's mid-rebuild with a cleaner data contract.

### 3.4 P1B MCMC companion manuscript

**What it is.** `arxiv/paper1b_mcmc_companion.tex` is a real, current
manuscript, registered in `project-context/paper_registry.json` under
`companion_manuscripts.P1B-MCMC` with `tex_path`/`pdf_path` both pointing at
`arxiv/` and a note the registry itself authored: *"Not one of the six
campaign papers, but its PDF is mirrored under served roots, so it needs a
canonical owner or its mirrors read as orphans."*

**Site surfacing (checked directly).** `site/src/data/papers.ts` references
`paper1b_mcmc_companion.pdf` exactly once, at line 277, as a secondary
`"Legacy validation dossier"` artifact link nested inside the **paper-1b**
entry (`slug: "paper-1b"`, title *"namaster-proof: Exact pseudo-Cℓ Window
Inference..."*). It does **not** have its own `slug`/card/route on the site.
So: the manuscript is not lost or hidden, but it is also not surfaced as a
first-class publication — it rides along as a link under a different paper's
detail page, and the paper registry that tracks it has already flagged that
setup as needing a decision, not just a passive mirror.

### 3.5 "Paper 7" self-improving-review meta-paper

**What it is.** `project-context/FUTURE_PAPERS.md` lines 8–90 sketch two
variants of a meta-paper about the review process itself: an academic framing
("A Self-Improving Internal/External Review Loop for Scientific Papers")
targeting a measured INT/EXT gap-to-zero result across the six-paper
campaign, and a Hubify marketing/case-study framing. Both list concrete data
sources already in the repo (`site/src/data/reviewTimeline.ts`, the pattern
catalog, `INTEGRITY_AUDIT_2026-06-26.md`).

**Disposition.** Idea-only, never drafted, nothing to audit for lost content.
Flagged here only because the audit brief asked for it explicitly — this
section is confirmation that `FUTURE_PAPERS.md` is still the sole home for
the idea and no draft manuscript exists elsewhere.

### 3.6 Golden 2026 PDF and the retention-archive artifacts

Two artifacts named in the original audit brief were checked directly:

- `research/focused_paper_source_integration/paper3_barriers_ech_transparency.pdf`/`.tex`
  — **confirmed present**, dated 2026-06-26. This is a standalone write-up of
  the barrier catalog and is one of the source documents for §4(a)'s
  resurrection candidate.
- `golden-2026-geometric-dark-energy-spin-torsion.pdf` (audit brief cited
  "v2.1.0") — **could not be located anywhere in the current repo tree.** A
  full-tree `find` (excluding `node_modules`) turned up nothing, and
  `public/downloads/`, `backups/`, and `versions/` (36KB and 124KB
  respectively — too small to hold a 1.69MB PDF) don't have it either. The
  only surviving references are two copies of
  `research/final_paper_prep/website_data_snapshot.md`, which describe it as
  "v1.2.0, current" as of **March 4**, not v2.1.0 — so either the audit
  brief's version number reflects a later snapshot that has since been fully
  removed from disk, or this is an early full draft of the program that
  predates the P1U/P1A/P1B naming and was cleaned up during a later site
  restructure without a dedicated retirement note. Either way, its scientific
  content (bounce cosmology + DE routes + galaxy spin) is already accounted
  for elsewhere in this table (rows 1, 2, 4, 5), so there is nothing
  independently at risk here — just a filesystem gap worth noting so nobody
  goes looking for a file that isn't there.

---

## 4. Resurrection recommendations

Applying directive Q1 (pure-contribution framing): a resurrected paper must
be presented as a positive, self-contained result — never as "here's what we
cut from Paper 1 and are now redoing."

### (a) RECOMMEND: standalone no-go survey paper — Houston decision

**Recommendation:** Resurrect the 14-barrier / 13-mechanism-class catalog
(§3.1) as its own standalone specialist paper. Working title: **"A
structural no-go survey of minimal spin-torsion routes to dark energy and
bounce phenomenology."**

**Why this clears the bar:**
- It is genuinely novel — a systematic, tabulated survey of failure modes
  across 7 foundation classes and 6 observational branches is not a
  byproduct of some other result, it's a contribution in its own right (the
  kind of paper that gets cited as "the barrier catalog" by later work).
- It is self-contained — the content already exists as prose, a formal
  table, and a TikZ figure inside `arxiv/paper1_unified.tex`, plus an
  independent standalone draft at
  `research/focused_paper_source_integration/paper3_barriers_ech_transparency.tex`.
  Extraction, not re-derivation.
  This is a **pure-contribution reframe**, not a "we cut it, now we're
  un-cutting it" narrative: the paper's thesis becomes "here is a structural
  no-go survey," full stop — it does not need to mention the P1 split at
  all in its own text.
- It is currently unpublished — the retirement removed it from every
  reader-visible surface; no version of it has been submitted anywhere.
- The manuscript's own internal honesty language is reusable almost
  verbatim: the "13 distinct mechanism-class constraints, not 13 independent
  rigorous theorems" framing already exists and was written specifically to
  avoid overclaiming, which is exactly the bar a no-go paper needs to clear
  with reviewers.

**What resurrection requires:** extracting §`sec:barriers` (table, figure,
per-barrier descriptions) into a standalone manuscript shell, writing a
fresh intro/conclusion framed around the no-go survey itself (not the ECH
dark-energy program's failure), and a fresh claims/scope check against
directive Q1. This is an editorial/writing task, not new science — the
physics is already derived and stated.

**Flag:** this is a Houston decision, not something to execute
unilaterally. It's a "spin up a new paper" call, and the program is mid-way
through a publication-architecture reset (`PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`)
that is already trying to reduce, not multiply, in-flight paper count.

### (b) LOWER PRIORITY: Shamir CW/CCW dipole null

As established in §3.2, the actual analysis already lives in P4, which is
live and active. There is no orphaned science to resurrect here. The only
optional move is a short section or appendix in the no-go paper from (a)
that restates the null result as one more closed route (R4, tensor-chirality
naturalness) with a citation into P4 rather than a re-derivation. Flagging
as lower priority because it adds no new science — it's connective tissue
for the no-go paper's narrative completeness, not a standalone contribution.

### (c) Everything else: no resurrection needed

- **Spectator-ALP birefringence (β≈0.27°):** already shipped into P1B/the
  MCMC companion. Live science, not lost.
- **Multi-survey anomaly draft (268,519/37.3M):** correctly narrowed for
  disclosed provenance reasons; the underlying discovery-science program is
  mid-rebuild (AUG-011), not abandoned. Resurrecting the *old* draft's
  numbers would be scientifically wrong — the whole point of AUG-011 is that
  those numbers had reconciliation problems.
- **"Paper 7" meta-paper:** idea-stage only, nothing to lose, already
  tracked in `FUTURE_PAPERS.md`.
- **Golden 2026 PDF:** its content is redundant with rows already covered
  above; the missing file is a housekeeping gap, not a science-loss event.

---

## 5. FAQ — what Houston saw missing

**"What happened to the no-go paper?"** It was retired at the P1 split
(`P1_SPLIT_CLOSURE.md`, 2026-07-14) because the broader P1U manuscript's
rhetoric outran what was tightly derived, and the closure chose to cut
rather than relabel. The content — full catalog, table, figure, per-barrier
derivations — is fully intact in `arxiv/paper1_unified.tex` (which was
explicitly not edited by the closure) and in a standalone source file at
`research/focused_paper_source_integration/paper3_barriers_ech_transparency.tex`.
It is genuinely unpublished, genuinely novel, and this document recommends
resurrecting it as its own paper (§4(a)) — pending a Houston go/no-go, since
opening a new paper track cuts against the program's current
consolidation-not-expansion posture.

**"What happened to the MCMC companion?"** Nothing — it's alive, current,
and registered (`project-context/paper_registry.json` →
`companion_manuscripts.P1B-MCMC`, `arxiv/paper1b_mcmc_companion.tex`). What's
worth Houston's attention is surfacing: it has no card of its own on the
site, it only appears as one secondary link on the P1B *namaster-proof*
page (`site/src/data/papers.ts` line 277), and the registry's own note
already flags that its current setup ("mirrored under served roots" without
"a canonical owner") reads as an orphan even though the manuscript itself
isn't one.

**"What happened to the anomaly science?"** It's not lost — it's being
actively rebuilt. The old 268,519-outlier draft
(`pipelines/p3_anomaly_engine/paper3_draft.tex`) had real, disclosed
provenance problems and was replaced by a narrow, defensible P3 at commit
`3f5582c2`. The genuine discovery-science program lives on in
`pipelines/p1_highz_tracers/` and `projects/desi-dr1-anomalies/`, and is
completed under a sealed AUG-011 contract as of 2026-08-07, with a full
manuscript architecture already drafted
(`project-context/ANOMALY_FLAGSHIP_MANUSCRIPT_ARCHITECTURE_2026-08-05.md`)
waiting only on the follow-on sample-selection, cross-match, and taxonomy
numbers to fill in its remaining placeholders.

## Decision record — 2026-08-05 (agent-executed under Houston's explicit full delegation)

Houston granted full decision authority ("make all the decisions on the next
steps for me… continue long-running", verbatim in prompt-history 2026-08-05).
Decisions taken:

1. **No-go survey paper: RESURRECT.** The 14-barrier catalog (sec:barriers of
   `arxiv/paper1_unified.tex`) becomes a standalone bounce-theory specialist
   paper, extracted under directive Q1 pure-contribution framing. Working id:
   P1C. Status: extraction started 2026-08-05.
2. **MCMC companion: first-class site card.** `arxiv/paper1b_mcmc_companion.tex`
   gets its own card under the bounce-theory program (supporting validation
   dossier role), ending its buried-link status.
3. **Reproducibility surface: build.** Public per-program reproduce view from
   `reproducibility/manifests/` + Hubify import spec — the lab-level final test
   per directive Q2.

---

## Decision record — 2026-09-02 (portfolio restructure, directive R3)

Source: `project-context/PORTFOLIO_DECISION_2026-09-02.md` §3, §5 and
Addendum; `project-context/PAPER_GENEALOGY_2026-09-02.md`. Each row below is a
directive-R3 lineup-change record: original claim beside new claim, source
file(s), and the decision-doc citation.

| # | Change | Original claim | New claim | Source file(s) |
|---|---|---|---|---|
| a | P1A → merge into P1C | Standalone algebraic no-go result (torsion elimination, axial contact operator, transparency identity), `arxiv/paper1a_ech_nogo.tex` v1A.0.126 | Merged into P1C as one ≤12 pp Note (id **P1N**), `arxiv/paper1bc_ech_note/` (new); P1C frozen at v1C.0.16, review churn stopped after R13 | `arxiv/paper1a_ech_nogo.tex`, `arxiv/paper1c_nogo_survey/main.tex` |
| b | P5 → fold into P4 | Standalone 46-pp DESIVAST chirality-environment companion, `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.142 | One section inside P4′ (id **P4P**), `pipelines/p4prime_chirality_test/paper/` (new), reframed as the largest test of the black-hole-universe spin-axis prediction | `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`, `pipelines/p2_chirality/chirality_catalog_paper.tex` |
| c | P2 → rescope to P2′ | Full-length four-vertex derivation paper, `research/focused_paper_source_integration/02_full_draft.tex` v1.7.130, f_NL = −35/16 | ≤6 pp Letter (id **P2′**), gated on the ledger-#1 independent second-method derivation before submission | `research/focused_paper_source_integration/02_full_draft.tex` |
| d | MCMC companion → retire to Zenodo | First-class supporting-validation-dossier manuscript, `arxiv/paper1b_mcmc_companion.tex` (registry id `P1B-MCMC`, per `PAPER_LINEAGE_2026-08-05.md` §3.4 and `project-context/SSOT/index.md` line 217) | Retired to a Zenodo dataset deposit, cited (not carried as a manuscript) by the P1N ECH Note | `arxiv/paper1b_mcmc_companion.tex`, `project-context/paper_registry.json` → `companion_manuscripts.P1B-MCMC` |
| e | `arxiv/main.tex` → retired | Stale June monolith, v2.3.18, f_NL = −35/8, mis-cited this session as "P1A" | Moved to `arxiv/_retired/main.tex` (already executed on disk as of 2026-09-02; this row formalizes the decision) | `arxiv/_retired/main.tex` |
| f | NANOGrav free-spectrum MCMC → reclaimed into A3 | Filed as "P3 support," appears in no paper (γ = 2.57 ± 0.38 vs. matter-bounce prediction 3, Savage–Dickey B ≈ 3.2) | Reclaimed into Track A3 (multi-channel consistency paper) as one of three channels alongside PBH abundance and SPHEREx/MegaMapper reach | `pipelines/p3_pta_mcmc/` |
| g | "Three research programs" → retired framing | Public site/CLAUDE.md framing: bounce theory / survey discovery / galaxy chirality, three co-equal programs (`PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`) | Retired in favour of "flagship line (Track A) + closed-line note (Track B) + data products (Track C)" | `project-context/PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`, site copy |
| h | Anomaly line (P3 / AUG-011) → redirected | Supporting-release DESI public-ID recovery note plus an unwritten discovery-flagship characterization cohort (3,810 TARGETIDs, `anomaly_score >= 8.0`) | Redirected to the early-universe anomaly map (Track C2); catalogue paper contingent on ledger #8 (known-object recovery benchmark) | `pipelines/p3_anomaly_engine/paper3_apjs.tex`, `project-context/ANOMALY_FLAGSHIP_SELECTION_DECISION_2026-08-26.md` |

### (a) P1A → merged into P1C

`arxiv/paper1a_ech_nogo.tex` (v1A.0.126, standalone algebraic no-go result)
is merged into `arxiv/paper1c_nogo_survey/main.tex` (frozen at v1C.0.16) to
form a single ≤12 pp gr-qc/CQG Note at the new path
`arxiv/paper1bc_ech_note/` (working id **P1N**), stating what minimal ECH
does for the bounce and cannot do for dark energy. P1C's review churn (R10–
R13, genre/length rejections per `PORTFOLIO_DECISION_2026-09-02.md` §3) stops
after R13; one INT board runs on the merged Note before submission.
(`PORTFOLIO_DECISION_2026-09-02.md` §3 Track B, §5.2; Addendum "The ECH Note
is on-vision.")

### (b) P5 → folded into P4

`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (v0.1.142, a
46-page post-hoc chirality-vs-void-environment null that no model predicts)
is folded into `pipelines/p2_chirality/chirality_catalog_paper.tex`
(v1.0.270) as one section of a new ≤15 pp paper at
`pipelines/p4prime_chirality_test/paper/` (working id **P4P**), reframed as
the largest test of the rotating-black-hole-universe galaxy-spin-axis
prediction (Popławski torsion bounce; Shamir/JWST claim), not as a bare data
product. (`PORTFOLIO_DECISION_2026-09-02.md` §3 Track C1, §5.3; Addendum
"P4′ is on-vision.")

### (c) P2 → rescoped to P2′

`research/focused_paper_source_integration/02_full_draft.tex` (v1.7.130,
full-length four-vertex derivation, f_NL^local = −35/16) is rescoped to a
≤6 pp Letter (PRD-L/JCAP), working id **P2′**. Submission is gated on ledger
item #1 (`project-context/NEXT_SCIENCE_LEDGER.md`) — an independent
second-method derivation (Salopek–Bond gradient expansion or δN) reproducing
−35/16 by a route no reviewer has verified. (`PORTFOLIO_DECISION_2026-09-02.md`
§3 Track A1, §5.5.)

### (d) MCMC companion → retired to Zenodo

`arxiv/paper1b_mcmc_companion.tex` (registry id `P1B-MCMC`; supporting
validation dossier, per `PAPER_LINEAGE_2026-08-05.md` §3.4 and
`project-context/SSOT/index.md` line 217 "the MCMC companion, P1A/P1B are
P1U") retires from manuscript status to a Zenodo dataset deposit, cited by
the P1N ECH Note rather than carried as a paper of its own.
(`PORTFOLIO_DECISION_2026-09-02.md` §3 Track B, §5.2.)

### (e) `arxiv/main.tex` → retired

The stale June monolith (v2.3.18, still f_NL = −35/8, the pre-correction
value) that this session's P1C reviewer prompts mis-cited as "P1A" is retired
to `arxiv/_retired/main.tex` — already executed on disk as of 2026-09-02;
this row is the directive-R3 record of that decision.
(`PORTFOLIO_DECISION_2026-09-02.md` §1 "Two process errors surfaced today," (a).)

### (f) NANOGrav free-spectrum MCMC → reclaimed into Track A3

`pipelines/p3_pta_mcmc/` (γ = 2.57 ± 0.38 vs. the matter-bounce prediction 3,
Savage–Dickey B ≈ 3.2 for matter bounce over free spectrum) — the one
genuinely on-vision positive result filed as "P3 support" and appearing in no
paper — is reclaimed into Track A3, the multi-channel consistency paper, at
−35/16. (`PORTFOLIO_DECISION_2026-09-02.md` §1 "Two process errors," (b); §3
Track A3.)

### (g) "Three research programs" → retired public framing

The `PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md` framing of bounce theory /
survey discovery / galaxy chirality as three co-equal research programs is
retired in favour of "flagship line + closed-line note + data products" (site
copy update pending). (`PORTFOLIO_DECISION_2026-09-02.md` §2, §5.1.)

### (h) Anomaly line (P3 / AUG-011) → redirected

`pipelines/p3_anomaly_engine/paper3_apjs.tex` (supporting-release DESI
public-ID recovery note) and the unwritten AUG-011 discovery-flagship
characterization cohort (3,810 TARGETIDs at `anomaly_score >= 8.0`, per
`project-context/ANOMALY_FLAGSHIP_SELECTION_DECISION_2026-08-26.md`) are
redirected to the early-universe anomaly map (Track C2, ledger #4/#6/#8); the
autoencoder catalogue is one instrument of that map, publishable only when
ledger #8's known-object recovery benchmark is earned.
(`PORTFOLIO_DECISION_2026-09-02.md` §3 Track C2; Addendum "The anomaly line is
redirected.")
   per directive Q2.

## Decision record — 2026-09-02 (evening): P2′ Letter → theory section of the A3 multi-channel paper

The R1 board and truth-audit establish that −35/16 is already printed by Li et al. 2016
(Eq. 4.19) and quoted by Quintin et al. 2015, and that the μ² orientation dependence is
contained in Li's polynomial. The Letter's genuine contribution — an independent
from-scratch in-in confirmation with a per-vertex table, the location of the uniform
factor 2 in Cai et al. 2009, and the δN/comoving reconciliation — is a confirmation, not
a discovery, and does not carry a standalone PRD Letter. Decision: close the Letter's real
defects to an honest v2L.0.2 as the archived theory record, and fold that content into the
A3 multi-channel paper (`research/track_a3_multichannel/paper/`) as its theory section,
where the positive near-term test lives. A standalone Comment on Cai et al. 2009 stays as
an option if a referee or the authors request it.

**ORIGINAL CLAIM:** "exact matter-contraction f_NL = −35/16 correcting Cai et al.'s
−35/8, with a new orientation-dependent squeezed limit."

**NEW CLAIM:** "independent confirmation of −35/16 with the ×2 in Cai et al. 2009
located, δN reconciliation, consistent with Li et al. 2016."

**Convergence budget:** one round run (`ROUND_2026-09-02-P2L-v2L.0.1-EXACTPDF-e1501145-R1`);
rounds stop here for the Letter (directive R2). Closure detail:
`project-context/SSOT/paper-2l/status.md` §"R1 closure — 2026-09-02 (evening)".

## Decision record — 2026-09-03: Anomaly catalogue (P3/AUG-011) → DATA RELEASE (ledger #8 answered)

**ORIGINAL CLAIM (item (h) above, 2026-09-02):** the AUG-011 discovery-flagship
anomaly-characterization cohort was redirected to the early-universe anomaly
map (Track C2), "publishable only when ledger #8's known-object recovery
benchmark is earned."

**PRE-DECLARED CRITERION** (`NEXT_SCIENCE_LEDGER.md` row 8): "Recovery rates +
one confirmed class → paper; else release," with the confirmed-class bar set
at ≥1 reference class, >10× enrichment, ≥5 positional matches.

**MEASURED (2026-09-03, v2 science-only sample, S>3, n=1,244, provenance-gate
clean — supersedes the v1 SAMPLE-V1-CONTAMINATED run):**
- VizieR reference-class cross-match: 1 BAL-quasar match at 4.2× enrichment
  (5,285 in-footprint references); 0 matches each for Roma-BZCAT blazars,
  CV/white-dwarf binaries, LAEs, SLSN host galaxies.
- Exit rule (≥1 class, >10× enrichment, ≥5 matches): **NOT MET** — the one
  nonzero cell clears neither the enrichment nor the match-count bar.
- SIMBAD/NED: 569/1,244 (45.7%) matched, 675/1,244 (54.3%) unmatched.
- Taxonomy: 25 UMAP+HDBSCAN clusters roll up to 8 descriptive families over
  the 675 unmatched objects (302/87/71/61/44/38/36/36).

**NEW DISPOSITION:** the anomaly catalogue is a **data release**, not a
standalone paper — the pre-declared success condition is unmet on the only
non-contaminated sample. Consistent with
`PUBLICATION_ARCHITECTURE_RESET_2026-08-03.md`'s framing of P3 as integrated
supporting material rather than a standalone candidate. Release document:
`pipelines/p3_anomaly_engine/release/ANOMALY_CATALOGUE_RELEASE_v2_2026-09-03.md`.
Full benchmark: `pipelines/p1_highz_tracers/clean_rerun/results_2026-08-07/phase3_v2/recovery_benchmark/PHASE3_V2_BENCHMARK_SUMMARY.md`;
landing receipt: `project-context/PHASE3_V2_LANDING_2026-09-03.md`.

**WHAT WOULD REOPEN THE PAPER:** a confirmed class from a future closed-loop
follow-up — i.e. a reference class clearing the pre-declared bar (>10×
enrichment, ≥5 positional matches) on a subsequent characterization pass, or
an independently-derived discriminator (per ledger #6) confronted with this
catalogue's candidate families. Absent that, the catalogue stands as public
data-release infrastructure for the lab's early-universe anomaly-map line.

## 2026-09-04 — A3 multi-channel paper (Track A flagship): claim change, transmitted amplitude becomes the observable

**ORIGINAL CLAIM (v3M.0.5–0.8):** the matter-contraction local f_NL = −35/16
(pre-bounce) is the flagship prediction; the SPHEREx bispectrum channel
"alone discriminates" −35/16 from Cai+2009's −35/8 at 3.13σ.

**NEW CLAIM (v3M.0.9, closure decision C1 = propagate, recorded in
`SSOT/paper-a3m/status.md`):** the observable prediction is the transmitted
post-bounce amplitude f_NL^after = T·f_NL^pre + Δf_NL^bounce, scheme S1,
validity kη_B ≲ 1e−2 (satisfied at the LSS/CMB pivot): f_NL^after ∈
[−0.65, −0.50] for −35/16 and [−1.20, −0.86] for −35/8 across the three A2
backgrounds (ledger #2, lanes a/b/c, 2026-09-03). At that amplitude SPHEREx
reaches 0.7–0.9σ (−35/16) / 1.2–1.7σ (−35/8): the factor-two is NOT separable
at current reach; −35/16 remains the pre-bounce input (ledger #1 closed;
monopole adjudication 2026-09-03). The paper's contribution is the
transmission-corrected prediction plus a multi-channel consistency map with
two honest nulls (PBH from the lab's own spectrum; PNG high-z abundance).

**Why:** R3 board (Fable M1 ≡ Gemini E4) showed the paper's own validity
window includes the pivot; claiming the pre-bounce reach was a claim above its
evidence (VISION.md R6). Nothing retired; the science is the same, stated at
its strength.
