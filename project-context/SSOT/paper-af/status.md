# AF (anomaly flagship) status — current authoritative section

**Current candidate:** vAF.0.8 · `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.tex`
**Directive-P readiness:** 80 (COMPUTED, author's reasoned estimate — no automated
calculator exists for this draft-registry paper; Convex disabled) — lane LAF5 (2026-09-22)
closed DAF-19 by adopting lane LAF4's corrected (spherical-embedding) taxonomy as the
paper's own (vAF.0.7), then ran the directive-R2-authorized board on that exact PDF
(Grok REJECT, Gemini ACCEPT WITH MINOR CORRECTIONS, Claude-opus verdict-blind MAJOR
REVISIONS), closing 9 genuinely-new-real findings with real edits and one real new
computation (10,000-draw permutation null) to vAF.0.8. NOT CONFIRMED — directive R2's
board budget is spent again this wave; no further board without another intervening
science/scope decision. Full account below in "LAF5 DAF-19 closure + board wave"; prior
wave in "LAF3 R2 confirmation wave".

## LAF5 DAF-19 closure + board wave (vAF.0.6 → vAF.0.7 → vAF.0.8, 2026-09-22)

Lane LAF5. Co-director decision: adopt lane LAF4's corrected re-clustering
(`reclustering_2026_09_22/`, spherical sky embedding eliminating the RA-wrap defect,
every hyperparameter and seed reused verbatim from the published run) as the paper's
Table VIII/IX, replacing the published (RA-wrap-defective) taxonomy rather than citing
it as a disclosed robustness check — this is the directive-R2 intervening-science
decision that authorizes one further board.

**Verification before adoption.** Every number was independently re-derived from
LAF4's committed JSONs by rerunning the real assembly pipeline against the corrected
taxonomy (new committed script, `taxonomy_adoption_2026_09_22/`), not by trusting
`PROPAGATION_NOTE.md`'s prose. Two propagation defects were caught and fixed before
adoption that neither LAF4's own report nor a naive prose swap would have caught: (1)
the shared RA-span computation is a naive max−min span — reusing it unmodified would
have reintroduced the exact wrap defect DAF-19 fixed into the "corrected" tables;
substituted the wrap-aware per-family span instead. (2) the taxonomy's own per-object
descriptor text can name the wrong dominant (survey, programme) cell (a
marginal-mode-vs-joint-mode labelling bug) — verified the true empirical joint mode
directly against the merged dataframe and used that throughout instead.

**DAF-19 CLOSED (vAF.0.7).** 25→23 clusters, 8→9 families, ARI 0.603/AMI 0.626 against
the published partition (moderate restructuring, no family reproduced unchanged),
ARI/AMI 0.257/0.256 against a (survey,programme)-only baseline (not a relabelling),
largest wrap-aware RA span 350.4°→331.6° — the not-a-compact-sky-region conclusion is
reinforced, not undermined. Every downstream number re-derived, not hand-edited: family
evidence, family-sky spans, V6 (made dynamic), V12's latent silhouette (recomputed on
corrected labels), the "two families worth starting with" narrative, and the
FT-B/FT-C/FT-E follow-up references (30 distinct objects/33 tier rows, was 32/35).

**Board (vAF.0.7 → vAF.0.8).** Grok API `grok-4.3` + Gemini API `gemini-3.1-pro-preview`
(ApJS-CATALOG profile) + one Claude-opus verdict-blind referee (Fable was out of usage
credit; opus substituted per lane brief). Verdicts: Grok REJECT, Gemini ACCEPT WITH
MINOR CORRECTIONS, Claude-opus MAJOR REVISIONS (17 ESSENTIAL/17 MAJOR/27 MINOR — by far
the most exhaustive single-leg report this paper has received). All three converged on
the manuscript's own leaked internal review-process prose. 9 genuinely-new-real items
closed (DAF-32 through DAF-40): the leaked "confirmation board" language and
bibliography-audit trail removed from the body/Acknowledgments/abstract; a
self-contradiction in the taxonomy's hyperparameter-provenance sentence resolved; Table
VIII's caption now defines every column and explains why two families can share a
printed summary; the corrected taxonomy's separate (non-sealed-chain) provenance
disclosed with its real SHA-256; feature standardisation (StandardScaler) disclosed;
the permutation null bumped from 50 to 10,000 draws at zero marginal cost; §VI A/§VI B
reconciled in one sentence; three broken cross-references fixed; one PDF-rendering
kerning artifact fixed. Two more cheap MINOR-tier fixes folded in (a false "uncorrelated
with the other two" figure caption; a training-set-size number inferred from a
filename). 5 findings independently FALSIFIED against source (Grok repeated its R1-era
backwards-date error; claimed-missing abstract statements that are already present
verbatim; a claim that the comparison partition is unhashed when it is Table I's own
artifact #6). 12 further findings (DAF-41 through DAF-52) are genuinely real per
independent verification but need new computation, a literature search this lane
cannot responsibly perform, or expand well beyond this lane's DAF-19-propagation
remit — named honestly in DISPOSITIONS/AF.md for future dedicated closure lanes, not
silently dropped or fabricated shut. A few editorial/genre-reframing asks (Grok's
recommendation to reject an honestly-scoped null result; abstract length vs. AAS house
style) are OPINION/OUT-OF-SCOPE, consistent with prior rounds.

**Directive-G bundle.** `\paperVersion` vAF.0.6→vAF.0.7→vAF.0.8; `\paperTimestamp`
unchanged (September 22, same day both bumps). 4-pass `pdflatex`, 0 errors, 0 undefined
refs/citations, 0 overfull hboxes >10pt, 19 pages (up from 18 — real new disclosure
content, not padding). Visual render of every touched page (1, 2, 10, 11, 12, 13, 15,
16, 17) — no overflow, no overlap. 37 cited == 37 bibitems throughout. Standalone
tarball-style compile reproduces the served build's text byte-for-byte identically at
both vAF.0.7 and vAF.0.8 (discarded after each smoke test). 5-way md5-verified mirror
(source dir, `site/public/papers/` versioned+alias, `public/papers/` versioned+alias)
at `795bba62d57aada93bdf9428388c06bd` (vAF.0.8).

- **PDF:** `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` — MD5
  `795bba62d57aada93bdf9428388c06bd`, SHA-256
  `8308bb6950795a942598875c8c2b8ce0bed4231d85caffc4cc2d38509b3dc5c1`.
- **New committed script:**
  `pipelines/p1_highz_tracers/anomaly_flagship_draft/taxonomy_adoption_2026_09_22/`.
- **Convex:** DISABLED (spending limit). Intended mutations queued to
  `project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md`.
- **Dispositions:** DAF-19 CLOSED; DAF-29 re-scoped (not re-opened); DAF-32 through
  DAF-52 added in `project-context/peer-reviews/DISPOSITIONS/AF.md`.
- **Directive R2:** board budget spent this wave (the DAF-19 closure was the
  intervening-science decision that unlocked it). No further board without another
  intervening science/scope decision.

**What genuinely remains, and who/what unblocks each (supersedes the vAF.0.6 list
below where it repeats):**
- **DAF-41** (abstract-drift sweep: 5 load-bearing sentences) — a dedicated
  abstract-calibration closure lane, text-only but touches many load-bearing sentences
  at once.
- **DAF-42** (wavelength-to-bin calibration / training corpus, re-flag of DAF-20's root
  cause) — recover the calibration array or downgrade the claims; real work.
- **DAF-43** ($f_{\rm NL}=-35/16$ uncited) — needs a citation or in-paper derivation.
- **DAF-44** (recovery benchmark match-radius asymmetry, 1.5″ vs 3″) — a cheap re-run,
  new computation.
- **DAF-45** (frame-concentration test has no null/effect size) — new computation from
  the sample's own redshift distribution.
- **DAF-46** ("five independent measures" overstates independence) — new computation
  (correlation matrix or effective-dof statement).
- **DAF-47** (stellar-mass systematic floor citation / $|f_{\rm NL}|\sim30$
  extrapolation) — literature citation + a re-run of the committed abundance script.
- **DAF-48** (Table IV schema internal inconsistencies) — a data-audit task.
- **DAF-49** (FT-A/FT-C rules under-specified; Table X missing columns) — add released
  columns to a table, real but bounded work.
- **DAF-50** (OT-1 template-spectrum source unspecified) — needs a literature-sourced
  template library.
- **DAF-51** (reference-class footprint area uncited) — needs a DESI DR1 footprint-area
  figure from the literature.
- **DAF-52** (no external recovery-rate benchmark comparison) — needs a literature
  search.
- **OT-1 selection function, Zenodo DOI** — unchanged from prior waves (GPU compute /
  Houston-only respectively).

---

## LAF3 R2 confirmation wave (vAF.0.5 → vAF.0.6, 2026-09-22)

Campaign lane LAF3. Directive-G pre-check on vAF.0.5 PASS before dispatch (fresh 4-pass
recompile matched the served build byte-for-byte in text content; the raw PDF md5 only
differs by pdflatex's embedded build timestamp). Board: Grok API `grok-4.3` + Gemini API
`gemini-3.1-pro-preview` (`tools/v3_native_pdf_review.py`, `ApJS-CATALOG` profile — the
paper's own registered catalogue/data-release referee profile) + one Claude-opus
verdict-blind referee, all against the exact vAF.0.5 PDF (sha256 `ea81ef41...`). Raws
saved and read in full before any verdict recorded.

**Verdicts (words diagnostic only, per directive H):** Grok REJECT, Gemini MAJOR
REVISIONS, Claude-opus MAJOR REVISIONS. All three converged on the flux-to-magnitude
arithmetic error and the missing LoVerde/Eisenstein-Hu/Planck citations; opus alone
caught the round's most consequential finding.

**The single most consequential finding (DAF-22):** the abstract/§I/§XI claimed "the
blue arm alone accounts for R²=0.78 of the score's variance" — but §V C's own body text
correctly computes R²=0.78 for the FULL three-camera regression, collapsing to R²=0.01
when the blue arm is dropped. What the blue arm explains in isolation (a univariate
regression) is a different, previously uncomputed number. Independently computed fresh
(new committed script `confirm_round_2026-09-22.py`): the blue arm alone gives R²=0.198
— roughly 4× lower than what the summary locations attributed to it. All three summary
locations now state both numbers explicitly and distinguish them; no headline conclusion
changes (the blue arm still dominates by every measure), but the specific number
attributed to "alone" is now the one actually computed for that quantity.

**8 further findings closed with real edits or new committed computation:** the flux-to-
magnitude conversion "≈20.6 AB mag" corrected to "≈20.9" (arithmetic error, all 3 legs
convergent); LoVerde 2008/Eisenstein & Hu 1998/Planck 2018 added to the bibliography
(named in prose, uncited, all 3 legs convergent); leftover version-history language ("we
no longer report one of them as supported") removed; the §IV.C morphology census
completed (441 PSF + 316 REX + 406 empty summed to 1,163, not the released 1,244 — the
missing 81 are EXP/SER/DEV, verified against `draft_numbers.json`); "a referee should
read V10 as..." reworded to address the reader, not a referee; Appendix A's
bibliography-verification arithmetic ("4+26=30") corrected to reconcile against the
actual 37-entry bibliography; the abstract's reproducibility claim scoped precisely to
the catalogue's selection (score/gate/threshold) rather than reading as a blanket promise
the taxonomy section's own honest disclosure immediately contradicts; and a real,
independently-computed Spearman statistic (ρ=0.009, p=0.85, n=502) added to the existing
"no visible trend of score with redshift" claim. A separate, purely presentational defect
was also found and fixed by rendering the PDF (not by reading the source): revtex's
`description` environment appends its own colon after a bracketed `\item` label, so
`\item[Refuted.]`-style labels (7 total) rendered as "Refuted.:" — fixed by dropping the
redundant in-bracket periods.

**Findings FALSIFIED against source, not real:** the claim the paper never states the
null result's effect size (the abstract already states "95% upper limits up to 12.5%");
the claim only an aggregate UL is reported, not per-class (Table VII already reports a
per-class Wilson 95% CI for all five reference classes); the claim the phase-3-v2 landing
receipt post-dates the paper (it precedes it by 18 days); a claimed body/abstract
significant-figure inconsistency on `5.7×10⁻⁵` (all three occurrences already match).

**Genuinely real, left honestly open (not closable without fabricating a threshold or an
uncited physical claim):** how much of the catalogue a "simple blue-arm quality cut"
would remove (no such cut is defined anywhere in the release); the expected $f_z/f_r$
ratio for a Gunn-Peterson trough at z≈6 (needs a literature-sourced number this lane
cannot responsibly attach without risking a misremembered citation); an explicit
Legacy-Survey noise-floor value for the "orders of magnitude above" claim (same
reasoning, non-blocking MINOR).

**Re-flags of already-disclosed content, no change:** the taxonomy's non-physical
stratification and RA-wrap (re-flag of DAF-19, still DISCLOSED-NOT-CLOSED); the Zenodo
DOI placeholder (re-flag of DAF-05, Houston-only); the internal `vAF.0.5`-style version
tag on the title page (re-flag of R1's Gemini AF-N1, OPINION/OUT-OF-SCOPE, deliberate
lab-wide convention). Full item-by-item ledger in
`project-context/peer-reviews/DISPOSITIONS/AF.md` (DAF-22 through DAF-31).

**Directive-G bundle.** `\paperVersion` vAF.0.5→vAF.0.6; `\paperTimestamp` September
21→22, 2026. 4-pass `pdflatex`, 0 errors, 0 undefined refs/citations, 0 overfull hboxes
>10pt, 18 pages (unchanged). `/latex-audit` full visual pass on all 8 touched pages plus
the OT-list page — no overflow, no overlap. `/artifact-link-verify`: all 6 GitHub links
(extracted from the compiled PDF's link annotations) resolve on `main`, unchanged.
Standalone tarball-style compile (`.tex` + `figures/` + `tables/` only) reproduces the
served build's text byte-for-byte identically; discarded after the smoke test per
protocol. 5-way md5-verified mirror at `47fca3cb5d827518aebde7499b8dc810`.

- **PDF:** `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` — MD5
  `47fca3cb5d827518aebde7499b8dc810`, SHA-256
  `e3099173d5f0f96ac3d179a3a16abf0c7a14dc043bfb4626c8609ed4560365b2`.
  Mirrored byte-identically to `site/public/papers/anomaly_flagship_vAF.0.6.pdf`,
  `site/public/papers/anomaly_flagship.pdf`, `public/papers/anomaly_flagship_vAF.0.6.pdf`,
  `public/papers/anomaly_flagship.pdf`.
- **New committed script:**
  `pipelines/p1_highz_tracers/flagship_assembly_2026-09-18/scripts/confirm_round_2026-09-22.py`
  → `outputs_blue_arm/confirm_round_2026-09-22.json`.
- **Convex:** DISABLED (spending limit) for the duration of this lane. Intended mutations
  (`paperVersions:bump` vAF.0.5→vAF.0.6 with the real md5/sha256/pages;
  `rRounds:create` for this confirmation board; `externalReviews:upsertByLabelDate` × 3;
  `papers:setReadinessCap` 77→80; `activityFeed:add`) queued to
  `project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md`.
- **Dispositions:** DAF-22 through DAF-31 added in
  `project-context/peer-reviews/DISPOSITIONS/AF.md`.
- **Git:** lane LAF3 commit(s), this bundle.

**What genuinely remains, and who/what unblocks each (unchanged from vAF.0.5 except as
noted):**
- **OT-1 selection function** — needs GPU injection-recovery compute (RunPod or
  equivalent); fully specified in-paper, not agent-closable without that compute.
- **Zenodo DOI** — Houston-only (external account action to mint the deposit).
- **DAF-17** (dedup near-threshold sensitivity) — needs new analysis on the raw
  pre-dedup data.
- **DAF-19** (taxonomy RA-wrap / missing UMAP-HDBSCAN hyperparameters) — needs a
  corrected re-clustering run.
- **DAF-20** (archived model's training corpus/architecture) — confirmed absent from
  every artifact in the repo; genuinely undocumented, not recoverable by agent-side work.
- **DAF-30** (new) — blue-arm quality-cut removal quantification: needs someone to
  pre-declare a cut threshold before it can be computed honestly.
- **DAF-31** (new) — Gunn-Peterson expected f_z/f_r ratio: needs a literature-sourced
  citation, ideally from a lane with live literature-search access.
- **Directive R2: round 2 of 2 spent.** No further board on paper-af without an
  intervening science/scope decision (e.g., landing OT-1's compute, a corrected
  re-clustering for DAF-19, or Houston's Zenodo DOI).

---

## LAF2 non-review TODO closure (vAF.0.4 → vAF.0.5, 2026-09-21) [superseded by vAF.0.6 above; kept for history]

**Directive-P readiness (as of vAF.0.5, historical):** 77 (COMPUTED) — lane LAF2
(2026-09-21) closed DAF-16 fully and completed the bibliography verification LR1
started; no review board run (directive R2: round 1 of 2 still spent, unchanged from
R1). Directive-G bundle re-verified clean at vAF.0.5.
`project-context/peer-reviews/DISPOSITIONS/AF.md` for the canonical per-item ledger.

Campaign lane LAF2. Scope: close every remaining agent-closable open item on paper-af and
run a full directive-G hygiene bundle. Explicitly NOT a review round (directive R2: R1
remains round 1 of 2; no board dispatched).

**DAF-16 fully closed (was PARTIALLY CLOSED).** The released-column schema table
(`tab_catalogue_schema.tex`, Table IV) previously documented 183 of 192 released columns,
with the remaining 9 named only as "internal joins and derived colours/flags not yet
grouped." This lane reconstructed the actual master frame by running
`assemble_flagship_evidence.py::build_master()` directly and diffing its 192 real columns
against every column already grouped in the schema generator
(`make_draft_figures.py::tab_catalogue_schema`) — confirming exactly 9 remain:
`mean_fiber_ra`, `mean_fiber_dec`, `gr_color`, `rz_color`, `w1w2_color`,
`is_point_source`, `is_star_candidate`, `crossmatch`, `snr_med`. Their exact definitions
were read out of the committed `enhanced_18M_inference.py` (colour/flag derivations from
already-released flux/parallax/morphtype columns) and `assemble_flagship_evidence.py`
(the `crossmatch` matched/unmatched join tag and `snr_med`, the assembly-time median of
the three per-band SNR columns) — real, committed, deterministic functions, not new
computation. Added a new schema group ("derived colours, flags & join tags") to the
generator script (never hand-edited the table) and reran the full assembly pipeline
(`assemble_flagship_evidence.py` → `make_tables.py` → `make_draft_figures.py` →
`blue_arm_diagnostics_2026-09-19.py`); every validation-contract status (V1–V12,
DEFECT-1/2/3) and every previously reported number reproduced byte-for-byte identical
except `n_columns_joined` (183→192, the intended change). Table IV now reads "all 192
released columns accounted for"; main.tex §IV A gained one paragraph naming and defining
all 9 columns. No science number changed.

**Bibliography verification completed.** LR1 (vAF.0.3) ADS-verified 4 of ~30 bibliography
entries (the ones the paper's own Appendix A flagged as unconfirmed against committed
artifacts). This lane verified the remaining 26 via live ADS/journal lookups (not
memory): every journal, volume, page, and year matches exactly, including the three
hardest-to-verify entries — Nicolaou et al. 2026 (MNRAS 547, page-ID `stag010`, OUP's
continuous-publication identifier, confirmed genuine not a typo), the DESI DR1 release
paper (AJ 171, 285, 2026), and Guy et al. 2023 (AJ 165, 144). Three entries have no fixed
journal record to check (Redrock: still "in preparation" per DESI's own papers page,
matching the bib's own non-claim; DESIBitmasks and ApacheArrow: living-docs/URL
citations) — correctly cited as such already. No bibliography text changed. Appendix A
extended with a verification statement naming the three hardest cases.

**OT-1 (selection function) and Zenodo DOI: reconfirmed genuinely not agent-closable, left
untouched.** Read the existing §"Open tests" OT-1 entry and the recovery-benchmark
section (§V D) to check whether the already-landed known-object recovery benchmark could
substitute for or partially satisfy OT-1. It cannot: the recovery benchmark measures
threshold-recovery of *known* reference-class objects already in the released catalogue
(a different, narrower question), while OT-1 is a controlled injection-recovery
experiment across a signal-to-noise grid into raw DR1 coadds — the paper's own "What this
catalogue is not" section is explicit that the two are not interchangeable, and
conflating them would be exactly the kind of fabricated-adequacy this lane was told not
to produce. OT-1's existing specification (inject each of the five reference classes'
template spectra at a grid of S/N into real DR1 sky/noise realizations, re-score with the
hash-bound model) was already complete and honest from LR1; left unchanged. Zenodo DOI
minting is Houston-only (an external account action, not a repo edit); left unchanged.

**Directive-G bundle.** `\paperVersion` vAF.0.4→vAF.0.5; `\paperTimestamp`
September 19→September 21, 2026. 4-pass `pdflatex`, 0 errors, 0 undefined refs/citations,
0 overfull hboxes >10pt, 18 pages (up from 17 — the new schema paragraph, no padding).
`/latex-audit` full visual pass (title page, the two touched pages, bibliography/appendix)
— no overflow, no overlap. `/artifact-link-verify`: all 6 `\artifact{}`/`\artifactdirlink{}`
GitHub links resolve on `main` (4 files, 2 directories). `tools/verify_pdf_mirror_integrity.py`:
0 findings after the site-data update (was 5: two stale hrefs, one stale version field in
papers.ts, one stale md5, one stale version field in live-status.ts). arXiv tarball
rebuilt from scratch in `/tmp` (main.tex + 9 figures + 11 tables, no stale-.bbl risk —
this paper uses inline `thebibliography`, cite/bibitem keys reconcile exactly, 0
missing/unused) and standalone-smoke-tested: 4-pass recompile, 0 errors, 0 undefined
refs, 18 pages, matches the served build exactly (tarball discarded after the smoke test
per protocol, not committed as a binary).

- **PDF:** `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` — MD5
  `60de7e9dbfbcc77336b3050ee788e68e`, SHA-256
  `ea81ef413503d25291853a2be714226d3b47fe680ead2f01727aaabe961140ca`.
  Mirrored byte-identically to `site/public/papers/anomaly_flagship_vAF.0.5.pdf`,
  `site/public/papers/anomaly_flagship.pdf`, `public/papers/anomaly_flagship_vAF.0.5.pdf`,
  `public/papers/anomaly_flagship.pdf` (five-way md5 verified, including the source dir).
- **Registry:** `project-context/draft_paper_registry.json` (AF block: version, pages,
  date, sha256, md5, served_aliases, status) and `project-context/paper_registry.json`
  (companion_manuscripts.AF served_aliases) both updated.
- **Site:** `site/src/data/papers.ts` (AF block: version, lastUpdated, pages, readiness
  75→77, pdfMeta, both PDF hrefs, remainingWork, new vAF.0.5 changelog entry) and
  `site/src/data/live-status.ts` (AF row: version, readiness, pendingWork) — AF's own
  rows only. `npx tsc --noEmit` clean.
- **Convex:** DISABLED (spending limit) for the duration of this lane. Intended mutations
  (`paperVersions:bump` for vAF.0.5 with the real md5/sha256/pages;
  `papers:setReadinessCap` 75→77; `activityFeed:add` for this bundle) queued to
  `project-context/CONVEX_BACKFILL_QUEUE_2026-09-21.md` with exact function names and
  args, per the standing Convex-outage instruction.
- **Dispositions:** DAF-16 entry updated from PARTIALLY CLOSED to CLOSED in
  `project-context/peer-reviews/DISPOSITIONS/AF.md`.
- **Git:** lane LAF2 commit(s), this bundle.

**What genuinely remains, and who/what unblocks each:**
- **OT-1 selection function** — needs GPU injection-recovery compute (RunPod or
  equivalent); fully specified in-paper, not agent-closable without that compute.
- **Zenodo DOI** — Houston-only (external account action to mint the deposit).
- **DAF-17** (dedup near-threshold sensitivity) — needs new analysis on the raw
  pre-dedup data (878,740 removed rows), not a text-edit closure.
- **DAF-19** (taxonomy RA-wrap / missing UMAP-HDBSCAN hyperparameters) — needs a
  corrected re-clustering run (spherical embedding, stated hyperparameters/seed).
- **DAF-20** (archived model's training corpus/architecture) — confirmed absent from
  every artifact in the repo by search; genuinely undocumented, not recoverable by
  agent-side work.
- **What an R2 board would need:** verify this lane's closures on the exact vAF.0.5 PDF,
  and assess whether DAF-17/19/20's disclosures are sufficient as final published
  limitations or require the named follow-up work before further readiness advance.
  Directive R2: still round 1 of 2 spent (this lane did not run a board).

## R1 INT board closed (vAF.0.3 → vAF.0.4, 2026-09-19)

Campaign lane LR1. Board: Claude opus (INT, verdict-blind, exact vAF.0.2 sha8
`b972d890`) + Grok API `grok-4.3` + Gemini API `gemini-3.1-pro-preview` (both via
`tools/v3_native_pdf_review.py`, `ApJS-CATALOG` profile, exact vAF.0.3 sha8 `d85487e9`).

**Verdicts (words diagnostic only, per directive H):** Claude opus MAJOR REVISIONS (6
BLOCKER, 16 MAJOR, 16 MINOR, 9 NIT). Grok REJECT (9 ESSENTIAL across 2 passes, 3 MAJOR, 2
MINOR, 1 NIT). Gemini MAJOR REVISIONS (6 ESSENTIAL/MAJOR across 2 passes, 3 findings, 1
NIT). **All three legs independently converged on the same core defects** — the
validation-contract pass-count error (13 claimed vs. 11 actual), the abstract-vs-body
mismatch on statistical power and the blue-arm origin, and the title not carrying the
paper's own null result — a strong triangulation signal, not one reviewer's
idiosyncrasy.

**Orchestrator verification (before any closure, per the standing truth-audit rule):**
every BLOCKER and the highest-impact MAJOR findings were independently re-derived from
the committed artifacts (`validation_contract_results.json`,
`flagship_sample_v2_enriched.parquet`, `flagship_sample_v2.parquet`) — not accepted from
reviewer text alone. 10/10 spot-checks reproduced the reviewer's numbers exactly.

**The single most consequential finding (DAF-03/04):** the abstract's "supports one"
z≈4.3 quasar candidate is, on independent verification, a row inside the paper's own
disclosed 406-row photometric-join defect (empty `morphtype`, exact-zero WISE/shape
columns) whose own r/z flux ratio is physically backwards for the redshift it would need
to support. Downgraded from "Supported" to "Undecidable"; the abstract's headline
follow-up outcome is now "refutes one of four, cannot decide the other three" (was
"refutes one, supports one, cannot decide two").

**17 of 20 canonical findings closed with real edits or new, independently-verified
computation** (no science number changed without a committed computation, per directive):
validation pass count 13→11 (V1 marked partial pass); provenance-chain caption corrected
to state exactly what V2 vs. V3 each verify; title changed to
"...selection, validation, and a null known-object recovery benchmark"; abstract/§I/§XI
rewritten in all three summary locations for the monotonicity qualifier, the blue-arm
evidence, and the benchmark power caveat; **new committed script**
`blue_arm_diagnostics_2026-09-19.py` (independently written and run by the orchestrator)
adds a real variance decomposition (mean_mse on rB/rR/rZ: R²=0.777, dropping rB collapses
it to 0.006) and a rest-frame-vs-observed-frame concentration test (IQR/median 0.39 vs.
0.68) — both lean instrumental without closing the blue-arm origin question; Table VII's
BAL enrichment fixed at the generator script (not hand-edited), 4.2×→3.3× against the
correct science-target denominator; the "Supported"→"Undecidable" downgrade above;
matched/unmatched score difference reframed as confounded by brightness with the real
medians/p-values; Table IV schema gains `residual_kurtosis` and an explicit
constant-placeholder-column disclosure; the f_NL paragraph now cites a real,
already-committed derivation script (`research/anomaly_map/ledger6_png_highz_abundance.py`)
with a corrected order-of-magnitude comparison (was arithmetically wrong: 0.3 dex ≈
factor 2, not >10×); NED/VizieR/AllWISE/Redrock citations added; the 2 remaining raw
`[placeholder:]` blocks (OT-1, Zenodo DOI) rewritten to honest specified-but-not-executed
prose.

**3 findings honestly disclosed as open, not fabricated or hidden** (real further work,
correctly out of scope for a text-edit closure): the archived model's undocumented
training corpus/architecture (confirmed absent from every artifact in the repo by
search); the physically-arbitrary deduplication rule's unquantified near-threshold
membership effect; the taxonomy's RA-wrap artifact and missing UMAP/HDBSCAN
hyperparameters (a corrected re-clustering is real follow-up work).

**Hygiene (directive G):** `\paperVersion` vAF.0.3→vAF.0.4; `\paperTimestamp` unchanged
(September 19 — same day). 4-pass `pdflatex`, 0 errors, 0 undefined refs/cites, 0 overfull
hboxes >10pt, 17 pages (up from 15 — real new content, not padding). `pdftoppm -r 110`
full render of every page inspected — no overflow, no overlap.

- **PDF:** `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` — MD5
  `4ae6347c1a4c48538241d3397a5653dd`, SHA-256
  `6a475b3cbc10856a2ccaf648cd0fef670d7d9101416a1eceaf4843b803f060e9`.
  Mirrored byte-identically to `site/public/papers/anomaly_flagship_vAF.0.4.pdf`,
  `site/public/papers/anomaly_flagship.pdf`, `public/papers/anomaly_flagship_vAF.0.4.pdf`,
  `public/papers/anomaly_flagship.pdf` (four-way md5 verified).
- **Convex:** `paperVersions:bump` id `k577hk30b41tj8zxk99a6pa1k58eqbea` read back
  verified; `rRounds:create` id `ks78f5h45pgfhv49ay38qrrnf58epytk`;
  `externalReviews:upsertByLabelDate` × 3 (claude-opus, Grok_brutal, Gemini_cosmology);
  `activityFeed:add` id `j57f9gkm6metczt6y1wb11asq18eqbw9`;
  `papers:setReadinessCap` → 75, read back verified via `getPaperState`.
- **Registry:** `project-context/draft_paper_registry.json` and
  `project-context/paper_registry.json` (companion_manuscripts.AF) both updated
  (version/pages/sha256/md5/served_aliases/review_paths).
- **Dispositions:** full item-by-item ledger (21 canonical items, DAF-01 through DAF-21)
  in `project-context/peer-reviews/DISPOSITIONS/AF.md`.
- **Git:** lane LR1 commits (this bundle + the earlier vAF.0.2→vAF.0.3 registration
  commit `f7e85cd3` and the mirror-integrity regex fix `5566ba9d`).

**Directive R2:** round 1 of 2 spent. An R2 board, if run, should verify these closures on
the exact vAF.0.4 PDF and assess whether the 3 disclosed-open items need their named
follow-up work before further readiness advance. No further board is authorized without
either an R2 dispatch or an intervening science/scope decision.

## Registration (lane LR1, 2026-09-19)

LA (2026-09-19 00:06–00:09 PT) assembled the first full draft, vAF.0.2: 15 pp, revtex4-2,
9 figures, 11 tables, 0 undefined refs, compiled clean, `REPRODUCIBILITY_MANIFEST.md`
complete. It was **not yet** a Convex-tracked paper, not mirrored to any served path, and
`site_slug` was `null` in `project-context/draft_paper_registry.json`.

Lane LR1 registered it:

- **Convex:** `papers:upsert` (slug `paper-af`, number `AF`, target journal `other` — ApJS
  is not one of the four literal enum values, so `other` is used with the real target
  journal named in `target`/`article_type` text) + `paperVersions:bump` for vAF.0.2 then
  vAF.0.3, both read back and verified.
- **Served mirrors:** `site/public/papers/anomaly_flagship.pdf` (canonical alias) and
  `anomaly_flagship_vAF.0.3.pdf` (versioned alias), mirrored identically to `public/papers/`.
  Four-way md5-verified (fresh compile == both served roots == Convex).
- **`project-context/paper_registry.json`:** added `companion_manuscripts.AF` (like `P1C`
  and `P1B-MCMC`) so `tools/verify_pdf_mirror_integrity.py`'s reverse-direction
  PDF-mirror-integrity gate recognizes the served mirrors as canonical rather than
  orphaned. **Gotcha found and fixed this lane:** AF's `\paperVersion` tokens (`vAF.0.2`,
  `vAF.0.3`, …) use a letter-only prefix — no leading digit before the letter, unlike
  every other letter-suffixed paper in this repo (`v4P.0.9`, `v3M.0.26`, `v1S.0.11`,
  `v1N.0.6` all have digit-then-letter). `served_pdf_policy.immutable_archive_name_patterns`
  requires a leading digit, so AF's versioned aliases do **not** match it — the
  `companion_manuscripts` registration is the only path that makes them pass the gate.
  Future lanes touching AF's version macro: do not "fix" this to a digit-first token without
  checking every site reference and the registry regex first; it is a known, worked-around
  quirk, not a defect to silently rename.
- **`project-context/draft_paper_registry.json`:** `AF.site_slug` set to `paper-af`,
  `served_aliases` extended, sha256/md5/version bumped to vAF.0.3, `status` narrated.
- **Site surfaces** (`site/src/data/papers.ts`, `live-status.ts`, `publish.ts`, `tracks.ts`,
  `reviewTimeline.ts`, `SSOT/index.md` top board): reconciled by lane L7c (continuation of
  L7b, the site-sync reconciler lane), commit `4bad8124`, from Convex's
  `listAllPaperStates` ground truth — readiness 60, 0 boards closed. LR1 did not hand-edit
  these files after discovering L7c's concurrent, more detailed edit already landed the same
  block (avoided a duplicate `paper-af` entry in `papers.ts` — see lesson below).

**Lesson for future lanes:** this session briefly produced two `paper-af` blocks in
`site/src/data/papers.ts` — LR1's own (written before checking for a concurrent editor) and
L7c's (richer, written independently from the same committed vAF.0.3 artifacts). LR1 deleted
its own duplicate rather than fight the collision. Read the file immediately before editing
(as the campaign brief already instructs) and re-check with `grep -c 'slug: "<slug>"'` after
any insert into a shared array — a tool's "file modified on disk since you last read it"
notice is not decorative, it means re-read before trusting your own diff.

## vAF.0.2 → vAF.0.3 (lane LR1, 2026-09-19): 2 of LA's 4 open TODOs closed

LA's first draft carried four explicit `\TODO{}` placeholders (never hidden, all four named
in-paper). LR1 closed two, non-science, no number changed:

1. **ADS bibliography verification.** The paper's own Appendix A named exactly four
   citations not recorded in any committed benchmark artifact: Ref.~`RitterKolb2003`'s
   journal/volume/page, and the three software citations `Pedregosa2011`, `Hunter2007`,
   `Ginsburg2019`. All four verified against ADS/JMLR/publisher records (2026-09-19, web
   search, not memory): Ritter & Kolb 2003, A&A 404, 301 (ADS `2003A&A...404..301R`);
   Pedregosa et al. 2011, JMLR 12, 2825; Hunter 2007, CSE 9, 90 (ADS `2007CSE.....9...90H`);
   Ginsburg et al. 2019, AJ 157, 98 (ADS `2019AJ....157...98G`, arXiv:1901.04520). **All four
   entries already carried the correct values — no bibliography text changed.** The `\TODO`
   was replaced with a verification statement naming the ADS bibcodes.
2. **Acknowledgements.** Replaced the placeholder with: the DESI DR1 standard
   funding/land acknowledgement (verbatim match to the sister P3-ApJS paper's, which uses
   the same DESI DR1 release); SIMBAD/NED/VizieR service acknowledgements; a compute-cost
   acknowledgement (GPU scan stage ≈$1.31 on RunPod, CPU assembly stage <60 s at $0); and
   the lab's standard AI-assisted-methodology disclosure paragraph (no vendor names, to stay
   clear of the directive-G leak-gate's `ChatGPT|Gemini|Grok` pattern — matches the
   `DISCLOSURE_PAT` exemption via the phrase "cross-checking and adversarial").

**Still open (2/4), correctly left open (need Houston or new GPU compute, not something an
agent lane should silently fabricate):**

- **Zenodo DOI** for the public deposit — not minted.
- **OT-1 selection function** (completeness/purity for this model–substrate pair) — does not
  exist; requires GPU compute. The paper is explicit that no population-level claim depends
  on it (§"What this catalogue is not").

**Hygiene (directive G):** `\paperVersion` vAF.0.2→vAF.0.3; `\paperTimestamp` unchanged
(September 19, 2026 — same day). 4-pass `pdflatex`, 0 errors, 0 undefined refs/citations, 0
overfull hboxes >10pt, 15 pages (unchanged). `pdftoppm -r 110` full render of the three
touched pages (acknowledgements, Appendix A software section, bibliography) — no overflow,
no overlap.

- **PDF:** `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` — MD5
  `078505552a563eccee07ddd7ca81e811`, SHA-256
  `d85487e97f6856040d12ef78b78ab57ce4d74fc6420d6664013cdc9651c17b41`.
  Mirrored byte-identically to `site/public/papers/anomaly_flagship_vAF.0.3.pdf`,
  `site/public/papers/anomaly_flagship.pdf`, `public/papers/anomaly_flagship_vAF.0.3.pdf`,
  `public/papers/anomaly_flagship.pdf`.
- **Convex:** `paperVersions:bump` id `k579zbnetq62twebstgy1gq64h8epgq3` read back verified.
- **Git:** commit `f7e85cd3` (tex + pdf + mirrors + draft_paper_registry.json);
  `project-context/paper_registry.json` companion-manuscript registration and campaign-log
  lines landed inside lane L7c's `4bad8124` (shared git-index hazard — staged alongside
  L7c's own files at commit time; content verified intact post-commit, nothing lost).

## R1 INT board — dispatch notes (superseded by "R1 INT board closed" above)

Review profile: `ApJS-CATALOG` (the closest existing lab profile — a catalogue + method
paper with a large public data product; no dedicated "anomaly catalogue" profile exists
yet in `tools/v3_native_pdf_review.py`'s profile table, so `ApJS-CATALOG` was reused
as-is). Focus questions given to every leg, drawn from the draft's own honest
self-assessment: (1) does the title carry the null/no-discovery framing overtly; (2) is
the blue-spectrograph-arm result's instrumental-vs-astrophysical origin argued
convincingly; (3) is the recovery-benchmark's low statistical power stated strongly
enough in the abstract, not just the body. All three were confirmed real findings — see
DAF-07, DAF-09/10/11, and DAF-12 above.

The Claude leg reviewed the exact vAF.0.2 PDF (sha8 `b972d890`) while Grok/Gemini reviewed
the exact vAF.0.3 PDF (sha8 `d85487e9`) — the only difference between those two versions
is the acknowledgements section and one Appendix-A bibliography-verification sentence; no
science content differed, so this was not a scope mismatch for any of the three focus
questions. The Grok+Gemini dispatch was blocked twice by `tools/bigbounce_preflight.py`'s
shared-checkout clean-tree gate (other concurrent lanes' files, not AF's own — PSU and
site-data files mid-edit); retried successfully once those lanes committed. Also
discovered and fixed in the same session: `tools/verify_pdf_mirror_integrity.py`'s
`served_pdf_policy.immutable_archive_name_patterns` regex rejected AF's letter-only
version-token naming (`vAF.0.2` has no leading digit, unlike every other paper's
`v4P.0.9`/`v3M.0.26`/`v1S.0.11`/`v1N.0.6`) — widened non-breaking in
`project-context/paper_registry.json` (commit `5566ba9d`) so AF's served mirrors pass the
gate going forward.

## Open gates

- Directive R2: round 1 of 2 spent. A round 2 board is authorized only to verify these
  closures on the exact vAF.0.4 PDF, or if an intervening science/scope decision occurs.
- 3 findings genuinely open (DAF-17 dedup near-threshold sensitivity, DAF-19 taxonomy
  RA-wrap/hyperparameter re-clustering, DAF-20 archived-model training-corpus
  archaeology) — each needs real further work (data analysis, a corrected re-clustering
  run, or historical documentation search) beyond a text-edit closure pass.
- Zenodo DOI, OT-1 selection-function injection-recovery experiment: genuinely open, need
  Houston (DOI minting) or new GPU compute (OT-1).
- Houston sign-off: not sought (readiness 75, below the 95-agent-gate ceiling).
