# P1N status — current authoritative section

**Current candidate:** draft v1N.0.1 · 2026-09-02 ·
`arxiv/paper1bc_ech_note/main.tex`

**Status: NEW MERGED DRAFT CREATED (v1N.0.1) — NOT YET REVIEWED.**
P1N is the single ≤12-page gr-qc / Classical and Quantum Gravity Note that
merges P1A into P1C per
`project-context/PORTFOLIO_DECISION_2026-09-02.md` Sec.3 Track B (B1) and
its Addendum: "what minimal Einstein--Cartan (ECH) spin-torsion gravity
does for the bounce -- the spin-spin contact repulsion (Pop{\l}awski's
torsion bounce) is the same contact term we derive -- and cannot do for
dark energy." Compiled clean, consistency-checked, mirrored, and
registered in this session; no INT/EXT review board has been run against
it yet, per instruction (this lane does not run review boards).

## Lineage

- **P1A** v1A.0.127 (`arxiv/paper1a_ech_nogo.tex`) — algebraic Cartan
  elimination, minimal axial--axial contact term
  $-(3\kappa/16)[\gamma^2/(1+\gamma^2)]J_5^2$, NJL sign result
  ($G_s=-3\kappa/16$, repulsive, no nonzero gap solution in the declared
  truncation), perturbation-transparency theorem. Archived at
  doi:10.5281/zenodo.21481838 (CC-BY-4.0). Not further submitted
  independently; superseded by P1N as the submission target.
- **P1C** v1C.0.16 (`arxiv/paper1c_nogo_survey/main.tex`, 25 pp, FROZEN,
  not edited) — 14-entry barrier catalog, Route-2/Route-3 amplitude-budget
  closures, six-member dimension-4 parity-odd operator list. Repository
  draft, not independently submitted; superseded by P1N.
- Merge performed 2026-09-02 per `PORTFOLIO_DECISION_2026-09-02.md` Sec.3
  Track B + Addendum ("The ECH Note is on-vision").

## What changed in the merge (beyond consolidation)

The operator-list and on-shell-torsion sections were corrected to match
the settled theory-audit record rather than P1C's earlier draft language:

- The six-member operator list $\{$O1--O6$\}$ is stated as a **rank-4
  spanning/generating list, not a linearly independent basis** (rank 2
  modulo total derivatives) — per
  `research/theory_audit/operator_basis_adjudication_2026_08_07.md`.
- The on-shell ECH torsion at finite Barbero--Immirzi $\gamma$ is stated
  as carrying **both an axial and a trace-vector irrep** (ratio
  $\beta/\alpha=1/2\gamma$; tensor irrep vanishes identically), correcting
  an earlier purely-axial reading that holds only in the strict
  Einstein--Cartan limit $\gamma\to\infty$ — per
  `research/theory_audit/ech_torsion_onshell_2026_08_08.md`.
- New framing content (not in either source): the Introduction and
  Discussion sections explicitly identify the derived contact term with
  Pop{\l}awski's spin-spin repulsion mechanism
  (arXiv:1007.0587, Phys. Lett. B 694, 181 (2010); arXiv:1102.5667,
  Gen. Rel. Grav. 44, 491 (2012)), stating the positive result (what
  minimal ECH does for the bounce) and the negative result (what it
  cannot do for dark energy) as two readings of the same algebraic
  elimination.

## Compile / QA record (this session, 2026-09-02)

- 4-pass compile (pdflatex/bibtex/pdflatex/pdflatex): **0 undefined
  references, 0 undefined citations.**
- Overflow audit: **0 `Overfull \hbox` > 10pt** after two fixes (a
  `p{}`-column tabular preamble bug that crashed the compile, replaced
  with `\parbox`-based cells matching P1C's proven pattern; the barrier
  table narrowed to `\footnotesize` to fit column width).
- Visual page-by-page render check (`pdftoppm -r 60`, all 6 pages read):
  no column overflow, both tables render inside their column/page bounds.
- `tools/p1c_consistency_check.py --tex arxiv/paper1bc_ech_note/main.tex`:
  **4/4 rules PASS** (constraint-count agreement, Tier-I count agreement,
  assert-vs-disclaim pairs, universal-closure claim vs self-declared
  non-closures). No rule logic was modified.
- **Pages: 6** (well under the ≤12 pp target; no cuts were needed beyond
  condensing the 14 barrier entries to 1--2 line summaries instead of
  P1C's full paragraph-per-entry treatment, and summarizing the
  Route-2/Route-3 derivations to their evidentiary-status conclusions
  rather than re-deriving them in full — both full derivations remain
  available in the archived/frozen source manuscripts cited above).

## Artifacts

- TeX: `arxiv/paper1bc_ech_note/main.tex`
- Bib: `arxiv/paper1bc_ech_note/references.bib` (deduped union of
  `arxiv/references.bib` + `arxiv/paper1c_nogo_survey/references.bib`,
  110 entries)
- PDF: `arxiv/paper1bc_ech_note/main.pdf`
  sha256 `2287537b1cf2420b2aa043b6d07da1281fb2844a82e296e7658467c7362747ba`
  (6 pages, 345050 bytes)
- Served mirrors (byte-identical, sha256 verified):
  `site/public/papers/paper1bc_ech_note_v1N.0.1.pdf`,
  `public/papers/paper1bc_ech_note_v1N.0.1.pdf`
- Registry: `project-context/draft_paper_registry.json` key `"P1N"`

## Open gates (not yet run in this session)

- No INT or EXT review board has been run against v1N.0.1.
- No Convex `paperVersions:bump` / `activityFeed:add` write yet — this
  lane did not touch site code or Convex per instruction; a follow-up
  session should register P1N on the live site once Houston reviews the
  merge.
- P1A and P1C remain on disk unedited (frozen); their own SSOT entries
  (`project-context/SSOT/paper-1/status.md`,
  `project-context/SSOT/paper-1c/status.md`) should be annotated by a
  follow-up session to point readers to P1N as the current submission
  target, without altering their historical record.
- Houston review of the merged framing (does the Poplawski identification
  read as precise, not overclaimed) is the next human-gated step before
  any review board is run.
