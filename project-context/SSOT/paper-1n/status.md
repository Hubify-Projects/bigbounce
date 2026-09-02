# P1N status — current authoritative section

**Current candidate:** v1N.0.2 · 2026-09-02 ·
`arxiv/paper1bc_ech_note/main.tex` — **R1 closure complete.**

## R1 closure (v1N.0.1 → v1N.0.2, 2026-09-02)

**Audit:** `project-context/peer-reviews/INT_v3/ROUND_2026-09-02-P1N-v1N.0.1-EXACTPDF-2287537b-R1/P1N_v1N.0.1_R1_truth_audit.md`
(Claude INT major-revisions, Grok API REJECT, Gemini API REJECT, Perplexity
ABSENT/401). 42 finding-rows audited → 3 REGRESSION, 16 distinct
GENUINELY-NEW-REAL (29 rows deduped), 3 RE-FLAG-OF-DISCLOSED, 3 FALSIFIED,
4 OPINION/GENRE → **19 canonical real items (R1–R19), all closed this
round.** Disposition ledger: `project-context/peer-reviews/DISPOSITIONS/P1N.md`
(all 19 rows update from OPEN to CLOSED in this commit bundle).

**Item → edit closure table:**

| ID | Item | Closure |
|---|---|---|
| R1 | (O1,O6) on-shell-branch regression | Restored branch split + `O1=O6=−O2+½O4` on shell, verbatim content from P1C v1C.0.16 `main.tex:2087–2098`, in Sec. VI (operator-list section). |
| R2 | Dual O5 normalization regression | Single READING-I/Eq.(E2) normalization stated once in Sec. II; `O5^{[4]}=−3κ[γ²/(1+γ²)](J⁵·J⁵)` used consistently throughout (no `−3/2κ` value anywhere). |
| R3 | R13-M3 P-even/trace-vector regression | Restored P-even-off-shell clause + `T^a{}_{ab}J^{5b}=3β(J⁵·J⁵)`, `β=κγ/[4(1+γ²)]`, and the not-excluded statement, in Sec. VI. |
| R4 | Poplawski over-claim, no signature bridge | Replaced "identical"/"algebraically identical" language with the audit's drafted γ→∞-scoped sentence (abstract, Intro, Sec. II, Discussion, Conclusions): exact only as γ→∞, 0.053 suppression and 2.11× trace-vector ratio stated at γ=0.2375, no formal signature bridge asserted. |
| R5 | Hehl–Datta uncited | Cited `HehlDattaNJL1971`+`Hehl1976` at Eq. (3); added Kibble1961, Sciama1964, Shapiro2002 (torsion review), BoehmerBurnett2008 (torsion cosmology). |
| R6 | Standalone evaluability | Route-2/Route-3 arithmetic (Eq. r2_ratio, Benedetti–Speziale β-function, numeric evaluation) brought in-paper; O1–O6 defined explicitly (Eq. dim4_defs); Fierz exchange row displayed (Eq. fierz_row); all `\artifact{}` links pinned to commit SHA `ded46bc5df8d39bbaac7bfbee16b07f0376bab34` (no Zenodo DOI existed for P1C to mint in this session — SHA-pin is the audit's stated fallback); P1C source linked directly as a pinned artifact. |
| R7 | O1–O6 never defined | Explicit Eq. (dim4\_defs) added in Sec. VI. |
| R8 | Version-history/meta language, directive Q1 | Stripped "consolidating/merges/supersedes/earlier catalog draft/earlier draft" language from abstract, Intro, Sec. II, VI, Data Availability; `\date` no longer prints `\paperVersion`; "this Note" → "this paper" throughout; header comment block rewritten to keep provenance internal-only. |
| R9 | Eq.(4) drops γ-factor | `G_s=−(3κ/16)[γ²/(1+γ²)]` now the primary stated result (Eq. Gs) with explicit γ→∞ limit clause; P1A's declared-interaction clause cited. |
| R10 | `∝` pair mis-divides | Added explicit derivation clause showing the two `∝` statements alone give `1/γ`, and the correct `1/(2γ)` requires the explicit constants. |
| R11 | `s_H` unfixed | `s_H=+1` fixed explicitly in Eq. (ech\_onshell\_torsion) clause. |
| R12 | Trace-vector 2.11× understated | Stated at γ=0.2375 in abstract, Sec. II, Discussion. |
| R13 | `3.6e-69` inconsistent | Recomputed to `3.884e-69` with full arithmetic shown (κn²=9.954e-80 eV⁴ / ρ_Λ=2.563e-11 eV⁴); old value's 2.29 meV normalization noted, not used. |
| R14 | `ρ_crit` undefined | Restored `0.27–0.41 ρ_Pl` window (P1A `main.tex:1527–1529`) inline at B12. |
| R15 | Table I Src legend missing | Legend added to Table I caption (7 foundations, 6 branches, I/K skip explained). |
| R16 | "closed operator-level" contradicts Table II | Restated "closed at the operator level modulo the spanning assertion (Tier-II)". |
| R17 | `\artifact{}` filename-invisible | Macro changed to print the artifact filename as link text (`\artifactbase`); un-floated into an `itemize` list in Data & Code Availability. |
| R18 | 95 unused bib entries | `references.bib` pruned from 113 to 26 entries (exactly the cited set, incl. 4 new R5 citations). |
| R19 | `β_obs` significance/caveat dropped | Restored ≈3.6σ/2.9σ + "statistical indications rather than established detections" caveat in Route 4. |

**Venue form:** CQG **Paper**, not Note (7725 words / 10 pp, well above
the CQG Note ceiling of 2500 words) — per audit closure plan (3), Option
A (grow and submit as a Paper). Recorded in
`project-context/draft_paper_registry.json` `P1N.target_journal` and
`P1N.venue_form`.

**Page target:** audit recommended 12–16 pp; this closure reached **10
pp / 7725 words** (up from 6 pp / 4144 words, +86% by word count) via
real added content only (explicit operator definitions, in-paper
Route-2/Route-3 derivations, explicit Fierz row, second-order Holst
verification, expanded per-barrier entries, "what is/is not established"
subsection) — no padding. Short of the audit's upper recommendation;
flagged as a residual open item for a future round if a referee still
finds a barrier/route step insufficiently self-contained.

**Compile/QA (this closure):** 4-pass pdflatex+bibtex, **0 undefined
refs/citations**, **0 `Overfull \hbox` > 10pt** (one 4.5pt overfull,
under the gate), `tools/p1c_consistency_check.py` **4/4 PASS**, all 10
pages visually spot-checked via `pdftoppm -r 100` (title/date, barrier
table + Src legend, theory section, operator-list equations, Data &
Code Availability artifact list, references) — no column overflow, no
floated/detached artifact block.

**PDF:** `arxiv/paper1bc_ech_note/main.pdf`, **v1N.0.2**, 10 pages,
sha256 `790795fe3d0cd5c3ba68234ddf3a5336d11fbfa1d402c9bc9d4b3be3013f125d`,
md5 `5f41629b370a55991a4c25937925a281` — verified byte-identical across
`arxiv/paper1bc_ech_note/main.pdf`, `site/public/papers/paper1bc_ech_note_v1N.0.2.pdf`,
`public/papers/paper1bc_ech_note_v1N.0.2.pdf` (v1N.0.1 kept alongside,
not deleted).

**Not done in this closure (out of scope per work order):** no review
board was run; site code/Convex untouched; P1A/P1C source files
untouched (frozen, read-only, used only as restoration sources).

---

## Pre-R1 record (v1N.0.1, superseded by the closure above)

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

## R2 closure — 2026-09-02 (v1N.0.2 → v1N.0.3)

**Audit:** `project-context/peer-reviews/INT_v3/ROUND_2026-09-02-P1N-v1N.0.2-EXACTPDF-790795fe-R2/P1N_v1N.0.2_R2_truth_audit.md`
(sha256 of audited PDF `790795fe3d0cd5c3ba68234ddf3a5336d11fbfa1d402c9bc9d4b3be3013f125d`).
Legs: Claude INT (major-revisions, 7 MAJOR/13 MINOR) / Grok API (REJECT,
3 ESSENTIAL/3 MAJOR/2 minor — 2 of 3 ESSENTIALs FALSIFIED, 3rd = DP1N-41
at MINOR) / Gemini API (MAJOR REVISIONS, 1 ESSENTIAL/2 MAJOR/5 minor) /
Perplexity ABSENT. 23 canonical items opened (DP1N-21…43; 8 MAJOR, 14
MINOR, 1 NIT), independently recomputed in
`research/theory_audit/p1n_r2_checks_2026_09_02.py` (all 6 checks PASS).

**Science/scope decisions taken (orchestrator, per directive R2):**
- **DP1N-21** — adopt the corrected coefficient
  $\mathcal O_4^{[4]}=-24\pi\kappa\gamma^3/(1+\gamma^2)^2=
  -192\pi^2G\gamma^3/(1+\gamma^2)^2$ (was printed
  $-3\kappa\gamma^3/(1+\gamma^2)^2$, wrong by exactly $8\pi$); ratio
  $\mathcal O_4/\mathcal O_5=8\pi\gamma/(1+\gamma^2)=5.650$ at
  $\gamma=0.2375$ — O4 is the *larger* operator, inverting the printed
  $\simeq0.22$ ordering. The no-go conclusion is unaffected (both remain
  the same $\MPl^{-2}$-suppressed Fierz-closed contact structure).
- **DP1N-22** — keep the six-member deliberately redundant generating
  list; state five distinct densities, rank four, one null direction
  being the exact $\mathcal O_1\equiv\mathcal O_6$ tetrad-conversion
  duplication, only $2\mathcal O_1+2\mathcal O_2-\mathcal O_4=0$ carrying
  content.
- **DP1N-23** — $\mathcal O_5$ is parity-*even* off shell as well as on
  shell; admitted by the $\varepsilon$-construction rule, not by being
  P-odd; the list is mixed-parity, not strictly parity-odd.
- **DP1N-25** — added an explicit half-page subsection
  (Sec.~V.A, "Engaging Pop{\l}awski's own dark-energy proposal")
  mapping Pop{\l}awski's proposed torsion-Λ mechanism onto Route~1 and
  closing it quantitatively (same $10^{-69}$-level amplitude suppression
  and repulsive-sign gap-equation argument as this paper's own Route 1).

**Item → edit summary:**
| Item(s) | Edit |
|---|---|
| DP1N-21 | Eq. (13)/(15) corrected + surrounding size sentence rewritten; P1C internal erratum recorded (not re-issued) |
| DP1N-22 | Rank/count paragraph + abstract + Conclusions restated (five distinct densities, one duplication) |
| DP1N-23 | O5 parity sentence corrected in both places it appeared |
| DP1N-24 | Citations added to B1–B6, B8, B10, B11, B13 (Hayashi–Shirafuji, Blagojević–Hehl, Shapiro, Weinberg 1989, Kibble, Sciama, Böhmer–Burnett, Hehl 1976); B9 given explicit Liouville-theorem statement |
| DP1N-25 | New Sec. V.A subsection |
| DP1N-26 | B7 restated as fixed parameter (not varying), cross-ref repointed to B12, Ashtekar2011/GhoshMitra2005 cited |
| DP1N-27 | Route-3 scaling relation displayed as Eq. (route3_scaling) with explicit numeric propagation, labeled Tier-III |
| DP1N-28 | Explicit mean-field gap equation (Eq. gap) + 3-line no-solution argument added |
| DP1N-29 | Table I caption: "gravitational coupling κ" |
| DP1N-30 | "chiral-count bound" clause replaced with reference to Eq. (route3_scaling) |
| DP1N-31 | Four `.bib` URLs pinned to `\repoSHA` |
| DP1N-32 | READING-I tag and provenance "note" fields removed/rewritten |
| DP1N-33 | Clarifying sentence: 58-order figure is the doubly-normalized ratio |
| DP1N-34 | One sentence stating the Shapiro–Teixeira result explicitly |
| DP1N-35 | Explicit $\rho+3p<0$ sign argument displayed |
| DP1N-36 | R1–R4 defined at head of Sec. IV |
| DP1N-37 | Abstract tightened (435 → ~380 words; still above the 250–300 CQG guidance, residual) |
| DP1N-38 | Theorem/proof environment (H1–H5 hypotheses, numbered) |
| DP1N-39 | Holst 1996 positioning sentence + citation added |
| DP1N-40 | `\paperVersion` now printed in Data/Code Availability |
| DP1N-41 | Ashtekar2011 cited at first abstract use of γ=0.2375 |
| DP1N-42 | G=1/M_Pl², M_Pl=1.22e19 GeV stated explicitly in Route 3 |
| DP1N-43 | En-dash replaced with "which evaluates to" |

**Hygiene:** `\paperVersion` → v1N.0.3, `\date` = September 2, 2026 (unchanged,
already current). 4-pass pdflatex + bibtex, 0 undefined refs/citations.
`tools/p1c_consistency_check.py` 4/4 PASS. Overfull hboxes: 2 fixed (>10pt,
via `align` line-breaks in Eq. gap and Eq. O4); 1 residual (4.5pt, below
the >10pt fix threshold). `pdftoppm -r 60` rendered and visually
spot-checked pages 1, 3, 6, 8 — clean, no overflow, theorem/proof
environment and corrected equations render legibly.

**PDF:** `arxiv/paper1bc_ech_note/main.pdf` — **11 pages**, 433339 bytes.
sha256 `c758664b4485a45752cd79e2ab695c6b09d9f82f2b283dd8db5a2af6721f7027`;
md5 `8725f40c69027c53c7a0f6a38f05587d`. Mirrored byte-identical to
`site/public/papers/paper1bc_ech_note_v1N.0.3.pdf`,
`public/papers/paper1bc_ech_note_v1N.0.3.pdf`
(older `v1N.0.1`/`v1N.0.2` copies retained). Registry
`project-context/draft_paper_registry.json` key `"P1N"` updated.

Next: R3 is now permitted per directive R2 (the three science/scope
decisions above were taken). Convex `paperVersions:bump` +
`activityFeed:add` recorded below.

**Convex:** `paperVersions:bump` id `k57cjc4y022k16m92vy3nae80n8dmgqv`;
`activityFeed:add` id `j57f2ezrnx1b7m80eanhstmvps8dm5pa`. texCommit
`453d663e67082f6c804a34b3adf9b14109e5575e`.
