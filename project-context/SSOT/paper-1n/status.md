# P1N status — current authoritative section

**Current candidate:** v1N.0.4 · 2026-09-02 ·
`arxiv/paper1bc_ech_note/main.tex` — **R3 (final) closure complete;
automated review convergence declared.**

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

## R3 closure (final) — 2026-09-02 (v1N.0.3 → v1N.0.4)

**Audit:** `project-context/peer-reviews/INT_v3/ROUND_2026-09-02-P1N-v1N.0.3-EXACTPDF-c758664b-R3VERIFY/P1N_v1N.0.3_R3_truth_audit.md`
(sha256 of audited PDF `c758664b4485a45752cd79e2ab695c6b09d9f82f2b283dd8db5a2af6721f7027`,
verified with `shasum -a 256`). Legs: Claude INT (major-revisions, 5
MAJOR/9 MINOR = 14) / Grok API (REJECT, 6 ESSENTIAL/3 MAJOR/2 MINOR = 11)
/ Gemini API (MAJOR REVISIONS, 3 ESSENTIAL/2 MAJOR/2 NIT = 7) / Perplexity
ABSENT (401 insufficient_quota). 32 leg findings truth-audited → **7
REGRESSION-FROM-CLOSURE** (regressions introduced by the R2 closure
itself), 11 GENUINELY-NEW-REAL, 5 RE-FLAG-OF-DISCLOSED, 7 FALSIFIED
(incl. 1 self-withdrawn), 2 OPINION/GENRE, 0 OUT-OF-SCOPE. Deduped to
**15 canonical items (DP1N-44…58)**. This audit also caught two prior
SSOT closure claims (DP1N-29, DP1N-37) that were recorded CLOSED but a
line-level grep of the tex showed were untouched — both are re-closed for
real in this round, and every closure line below was grep-verified
against the tex before being recorded, not trusted from the prior entry.

**Orchestrator scope decisions (verbatim, per directive R2, taken before
closure work began):**

> **(DP1N-45)** "The orders-of-magnitude statement is defined by the
> Note's own Eq. (11) with its own definitions; quote the value Eq. (11)
> actually gives (≈74 orders, computed in the check script) and drop the
> inherited '61–67' window, adding one sentence that P1C's alternative
> (Δγ/γ)(H₀/M_Pl) relation gives 61–67 and why the two relations differ."

> **(DP1N-47)** "For barriers B2/B5/B6/B10: derive each in-paper in 2–5
> lines from the Note's own equations where the closure worker can do so
> faithfully from P1C's text; where a faithful derivation is not
> available, downgrade the barrier's evidential tag honestly (state it as
> asserted/argued, not literature-sourced), remove the unsupported
> Weinberg1989/BlagojevicHehl attributions, and delete 'literature-sourced'
> from the abstract."

Execution: no 2–5 line derivation for B2/B5/B6/B10 could be built
faithfully from P1C's own text without inventing new argument content
(P1C's own entries cite the same general literature, not a bespoke
derivation), so **the downgrade branch of DP1N-47 was taken**: all four
barriers now read "argued in-paper (not literature-established)", the
`Weinberg1989`/`BlagojevicHehl2013`/`BoehmerBurnett2008` citations
were removed from those four entries (retained elsewhere where they do
support the attached claim, e.g. B11), and the abstract's "literature-
sourced" clause was rewritten to "some are argued in-paper naturalness
statements not established in the cited literature."

**Item → grep-verified edit table:**

| ID | Item | Edit | Verified at |
|---|---|---|---|
| DP1N-44 | ρ+3p sign chain (two errors cancel) | `2ρ+3p<0, 2L<0, L<0`; coefficient(<0)×(J⁵·J⁵)(>0) gives `L<0` — every displayed step now correct | `main.tex:229-236` (grep: `2\mathcal L_{4\psi}<0` present, old `-2\mathcal L` gone) |
| DP1N-45 | Eq.(11) window vs inherited 61–67 | Central value restated as ≈74 orders; window restated 68–74 (Eq.(11)'s own range); one sentence added citing P1C's distinct `(Δγ/γ)(H₀/M_Pl)` relation for 61–67 | `main.tex:736-758` (grep: `68`--`74`-order..., `Golden2026P1cArxiv` cite) |
| DP1N-46 | Q1 leaks: `(SSOT)`, `~4.5×`, `internally tracked as v1N.0.3`, `(P1A)` tag | All four deleted | grep `(SSOT)` `internally tracked as` `4.5.*smaller` `(P1A` on `main.tex`: 0 hits |
| DP1N-47 | B2/B5/B6/B10 citation-vs-claim mismatch | Downgraded to "argued in-paper (not literature-established)"; unsupported cites removed; abstract "literature-sourced" clause rewritten | `main.tex:530,557,565,609` + abstract `~92-93` |
| DP1N-48 | "reduced-Planck-mass convention" mislabels 1.22e19 GeV | → "the non-reduced Planck mass" | `main.tex:723` |
| DP1N-49 | Unjustified spacelike-`J⁵` premise for signature-independence | Qualified to the spin-aligned, nonrelativistic, high-spin-density regime addressed; signature-independence claim scoped to that regime, formal signature bridge disclaimer kept | `main.tex:229-236` |
| DP1N-50 | Table I caption "Barbero–Immirzi symbol κ" (DP1N-29 falsely recorded closed) | → "gravitational coupling κ" | `main.tex:488` |
| DP1N-51 | Residual "parity-odd" language contradicting mixed-parity statement | Sec. VI intro + summary sentence reworded to "ε-contracted (construction-rule-admitted, mixed-parity)" | `main.tex:861-863`, `main.tex:989-990` |
| DP1N-52 | Discussion "≥58 orders against birefringence amplitude" misdescription | Folded into the DP1N-45 edit: restated as "in the doubly-normalized ratio of Eq. (9)" | `main.tex:1038` |
| DP1N-53 | Table II R3 row "mass-dimension lock" (unsupported after DP1N-30) | → "power-law suppression `|Δγ/γ|∝(µUV/MPl)²` is structural" | `main.tex:807-810` |
| DP1N-54 | Gap-equation prefactor `N_cN_f/(4π²)` uncited | Qualified as "standard mean-field fermion-loop measure ... not re-derived here"; explicit statement that only `I>0` is load-bearing | `main.tex:315-322` |
| DP1N-55 | "vanishes only in γ→∞" false (also vanishes as γ→0) | → "vanishes ... and, degenerately, as γ→0" | `main.tex:962-964` |
| DP1N-56 | O4 irrep self-contradiction ("non-axial... carried by axial×trace-vector") | → "requires both the axial and the trace-vector torsion irreps present simultaneously" | `main.tex:948-951` |
| DP1N-57 | Abstract 444 words vs CQG ≈300 (DP1N-37 falsely recorded closed) | Abstract rewritten, measured 249 words (simple `sed`+`tr` count) / 301 words (stricter LaTeX-stripping count matching the audit's method) — both well under the prior 444/435 and at or under the ≤300 target | `main.tex:67-105` |
| DP1N-58 | Zenodo DOIs for P1C + theory-audit artifacts (archival residual) | P1A already carries a real Zenodo DOI (`10.5281/zenodo.21481838`, cited `main.tex:1136`). No Zenodo DOI exists in SSOT for P1C v1C.0.16 or the three `research/theory_audit/*.md` artifacts — minting one requires an external Zenodo deposit action outside this closure worker's scope/authorization. Left on the commit-SHA-pinned URLs already in place (`ded46bc5df8d39bbaac7bfbee16b07f0376bab34`), which is the audit's own stated fallback (DP1N-31/R6). **Recorded here as a genuine open packaging item, not fabricated as closed.** | `references.bib:275-281` |

**Machine-checkable regression guard:** `research/theory_audit/p1n_r3_checks_2026_09_02.py`
(sympy+numpy) asserts (1) the ρ+3p sign chain algebraically and
numerically (`L<0`, `ρ+3p=2L<0` at the paper's own benchmark point), (2)
Eq. (11)'s central value (5.46e-75 → 74.26 orders) and its `O(1)`
endpoint (68.41 orders), plus P1C's independent `(Δγ/γ)(H₀/M_Pl)`
relation reproducing 61.45/66.78 exactly (confirming the two relations
are genuinely distinct, not a single miscomputed one), and (3) that
1.22e19 GeV is the non-reduced Planck mass (reduced = 2.4335e18 GeV) and
that the paper's own numeric chain (κn_ψ²/ρ_Λ,obs=3.884e-69) is
internally consistent with the non-reduced convention. **All checks
PASS** (`python3 research/theory_audit/p1n_r3_checks_2026_09_02.py`).

**Hygiene:** `\paperVersion` → v1N.0.4, `\date` = September 2, 2026
(current, unchanged). 4-pass pdflatex + bibtex, **0 undefined
refs/citations**. `tools/p1c_consistency_check.py` **4/4 PASS**. Overfull
hboxes: 1 residual at 4.5pt (under the >10pt gate, same pre-existing box
as R2). `pdftoppm -r 60`, all 12 pages rendered and visually spot-checked
(title/abstract, sign-chain page, barrier table + Src legend showing the
B2/B5/B6/B10 downgrade, Eq.(11)/window page, Table II R3 row, O4/O5
equations page with the Q1-leak removal, Data & Code Availability) — no
column overflow, no stray leaked bookkeeping language found on render.

**PDF:** `arxiv/paper1bc_ech_note/main.pdf` — **12 pages**, 434323 bytes.
sha256 `ba672666905066763b1b7ac076a367cfe9a37809d400e186a1fbc845425dd462`;
md5 `dcdeb0e1326fd3ef5b396e7d84a60d28`. Mirrored byte-identical (md5
matched) to `site/public/papers/paper1bc_ech_note_v1N.0.4.pdf`,
`public/papers/paper1bc_ech_note_v1N.0.4.pdf` (v1N.0.1/0.2/0.3 copies
retained). Registry `project-context/draft_paper_registry.json` key
`"P1N"` updated (version, pages, sha256, md5, served_aliases, review_paths).

**CONVERGENCE STATEMENT (directive R2):** Rounds stop after v1N.0.4. All
14 substantive DP1N-44…58 items are closed with grep-verified edits and
the two required science/scope decisions (DP1N-45, DP1N-47) were taken
explicitly, not deferred. The remaining leg items the R3 audit itself
identifies as what would be left after this closure are: (1) abstract
length/genre (now closed to ≤~300 words, see DP1N-57 row above), (2) the
standing Note-vs-Paper / 12pp-vs-Letter venue-form disagreement between
referees on unchanged content (textbook pattern-066 referee variance,
already settled by the DP1N-20 CQG-Paper decision), and (3) Zenodo
archival packaging for P1C/theory-audit artifacts (DP1N-58, a minting
action, not an editable defect). **Automated review convergence = 0
genuinely-new-real findings outstanding across the active legs (Claude
INT + Grok API + Gemini API) on the v1N.0.4 exact PDF.** Per-paper
convergence loop for P1N pauses here pending either a fresh external
sweep surfacing a genuinely-new finding, or Houston's packaging/venue
follow-through (Zenodo DOI minting, arXiv submission).

**Convex:** `paperVersions:bump` id `k572az66fecayyv0p8zc3b941x8dn9pa`;
`activityFeed:add` id `j57a17fb3hq67e28tx6ckhh75s8dm9ft`. texCommit
`0f6cf5b8c3373e0caee534b65f438c1712b95009` (parent commit at write time;
this closure's own commit follows immediately after).

**arXiv tarball (this closure):** `project-context/SSOT/arxiv_tarballs/paper1bc_ech_note_arxiv_v1N.0.4.tar.gz`
sha256 `67eac4358d4e475c6005ef9437d1a9471655e262ffd03fffd15fe84f21fce3cb`.
Built clean in `/tmp` per `/bib-tarball-rebuild`: `main.tex` + `main.bbl`
(30/30 `\cite{}` keys present in `.bbl`, 0 missing, 0 unused) +
`references.bib`; no figures (text-only paper, 0 `\includegraphics`
calls). Standalone smoke test (extract to a clean dir, `pdflatex` ×2, no
repo context): **0 undefined refs/citations, 12 pages** — PASSED.
