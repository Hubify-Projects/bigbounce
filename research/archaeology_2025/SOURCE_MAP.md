# SOURCE_MAP.md — 2025 legacy-archaeology term mapping

Worker: W1r (relaunch of stalled W1). Method: `rg -il` over the working tree only
(no `git log -S/-G` — 4 GB pack stalled the prior worker); first-appearance dates
via `git log --diff-filter=A --format='%h %ad' --date=short -1 -- <path>`.
Facts only, no dispositions.

**NOTE (surprising, read before using this map):** `site/src/data/genealogy.ts`
was added **2026-09-18** (commit `ddf40b75`, "feat(site): add /genealogy — 2025
research lineage, four retired hypotheses, open questions #20–#22; link from
Learn") — the same day as the braindump. This means the director's correction
#4 ("the missing surface is a genealogy / retired-hypotheses page") is now
**stale**: a concurrent worker (likely W7/W7b per STATUS.md) already shipped
that page, including White Hole Sponge/ICBC, Black Hole Sponge, "Born in a
black hole," VCA/BCR/SBA, and open questions #20–#22. Every legacy term below
that shows a `site/src/data/genealogy.ts` hit is now live on `/genealogy`, not
merely absent from the site.

---

## 1. Summary table

| Concept | Files hit (count, up to 4 reps) | Where it lives now | First-appearance (oldest rep) | Already tested/closed? |
|---|---|---|---|---|
| White Hole Sponge | 4: `site/src/data/genealogy.ts`, `project-context/SSOT/queue.md`, `research/archaeology_2025/inputs/chatgpt_braindump_2026-09-18.md`, `research/archaeology_2025/memos/DAUGHTER_UNIVERSE_MEMO.md` | site genealogy page (retired) + archaeology memo | genealogy.ts 2026-09-18 (`ddf40b75`) | Not tested as physics; catalogued as retired 2025 Notion-era hypothesis |
| Black Hole Sponge | 2: `site/src/data/genealogy.ts`, `research/archaeology_2025/inputs/chatgpt_braindump_2026-09-18.md` | site genealogy page (retired) | genealogy.ts 2026-09-18 | Not tested; retired hypothesis label only |
| Omega Black Hole | 4: `site/src/data/genealogy.ts`, `project-context/SSOT/queue.md`, `project-context/NEXT_SCIENCE_LEDGER.md`, `research/archaeology_2025/memos/DAUGHTER_UNIVERSE_MEMO.md` | site genealogy page + ledger item | genealogy.ts 2026-09-18 | Not tested; open-question framing in ledger |
| Omega Singularity | 1: `research/archaeology_2025/inputs/chatgpt_braindump_2026-09-18.md` | archaeology inputs only | n/a (braindump 2026-09-18) | Zero-hit elsewhere — provenance only |
| Big Crunch | 8: `speculations.html`, `status.html`, `research/branch_V_bounce_evidence/05_top3_candidates.md`, `research/archaeology_2025/memos/COSMIC_FATE_MEMO.md` | active site page (`/speculations`) + closed research memo | memo/site predate braindump | **Closed**: `COSMIC_FATE_MEMO.md` (W3, 2026-09-18) — impossible under constant Λ>0 at Ω_m<1, any curvature |
| Big Freeze | 5: `speculations.html`, `site/src/data/genealogy.ts`, `status.html`, `research/archaeology_2025/memos/COSMIC_FATE_MEMO.md` | active site page + closed memo | — | Closed alongside Big Crunch in COSMIC_FATE_MEMO.md |
| heat death | 4: `research/archaeology_2025/bibliography/VERIFIED_BIBLIOGRAPHY.md`, `research/archaeology_2025/memos/DAUGHTER_UNIVERSE_MEMO.md`, `research/archaeology_2025/memos/COSMIC_FATE_MEMO.md` | archaeology memos only | — | Discussed as fate-scenario synonym in COSMIC_FATE_MEMO |
| Big Rip | 3: `research/outputs/lit_lqg_bounce_2024_2026.json`, `research/outputs/lit_desi_dark_energy_2024_2026.json`, `research/archaeology_2025/memos/COSMIC_FATE_MEMO.md` | literature-scan outputs + closed memo | — | Addressed in COSMIC_FATE_MEMO (CPL a→∞ gives ρ_DE→0⁺, no Rip) |
| ICBC | 4: `site/src/data/genealogy.ts`, `project-context/SSOT/queue.md`, `research/archaeology_2025/inputs/...`, `.../DAUGHTER_UNIVERSE_MEMO.md` | site genealogy page (retired) | genealogy.ts 2026-09-18 | Not physics-tested; retired-label only |
| Inverse Cosmic Boundary | 0 | absent (only "Inverted Cosmic Boundary" variant exists) | — | zero-hit, not even in braindump under this exact phrasing |
| Inverted Cosmic Boundary | 2: `site/src/data/genealogy.ts`, braindump | site genealogy page | genealogy.ts 2026-09-18 | Retired-label only |
| ICBP | 4: `site/src/data/genealogy.ts`, braindump, `.../DAUGHTER_UNIVERSE_MEMO.md`, `.../COSMIC_FATE_MEMO.md` | site genealogy page + memos | genealogy.ts 2026-09-18 | Discussed in both memos, not physics-tested |
| QGBW | 3: `site/src/data/genealogy.ts`, braindump, `.../COSMIC_FATE_MEMO.md` | site genealogy page + memo | genealogy.ts 2026-09-18 | Not physics-tested |
| QGIW | 1: braindump only | archaeology inputs only | — | Zero-hit elsewhere — provenance only |
| Vacuum Collapse Anomaly | 2: `site/src/data/genealogy.ts`, braindump | site genealogy page | genealogy.ts 2026-09-18 | Retired-label only |
| UMPBH | 3: `site/src/data/genealogy.ts`, braindump, `.../DAUGHTER_UNIVERSE_MEMO.md` | site genealogy page + memo | genealogy.ts 2026-09-18 | Discussed in memo |
| BHCP | 2: `site/src/data/genealogy.ts`, braindump | site genealogy page | genealogy.ts 2026-09-18 | Retired-label only |
| CTEF | 3: `site/src/data/genealogy.ts`, braindump, `.../DAUGHTER_UNIVERSE_MEMO.md` | site genealogy page + memo | genealogy.ts 2026-09-18 | Discussed in memo |
| GGSC | 3: `site/src/data/genealogy.ts`, braindump, `.../DAUGHTER_UNIVERSE_MEMO.md` | site genealogy page + memo | genealogy.ts 2026-09-18 | Discussed in memo |
| WHCIF | 3: `site/src/data/genealogy.ts`, braindump, `.../DAUGHTER_UNIVERSE_MEMO.md` | site genealogy page + memo | genealogy.ts 2026-09-18 | Discussed in memo |
| BHCIF | 2: braindump, `.../DAUGHTER_UNIVERSE_MEMO.md` | archaeology only (not on site) | — | Discussed in memo only |
| VCA | 2: `site/src/data/genealogy.ts`, braindump | site genealogy page | genealogy.ts 2026-09-18 | Retired-label only |
| BCR | 3: `site/src/data/genealogy.ts`, braindump, `.../DAUGHTER_UNIVERSE_MEMO.md` | site genealogy page + memo | genealogy.ts 2026-09-18 | Discussed in memo |
| SBA | 3: `site/src/data/genealogy.ts`, braindump, `.../DAUGHTER_UNIVERSE_MEMO.md` | site genealogy page + memo | genealogy.ts 2026-09-18 | Discussed in memo |
| M_crit (all 3 forms) | 65+ hits across `research/paper_1_01_archive/main.tex`, `arxiv/_retired/main.tex`, `research/branch_I_bounce_compatible_DE/horndeski_bounce_stability/01_problem_statement.md`, ~15 `project-context/peer-reviews/*P1A*` threads | retired archives + Horndeski branch (active research) + peer-review history | `paper_1_01_archive/main.tex` 2026-03-17 (`af25f807`); `arxiv/_retired/main.tex` path added 2026-09-02 (`2d93d0e4`, retirement commit) | **Parent-BH M_crit CLOSED**: sentence deleted per `R23conf_P1A_TRUTH_AUDIT.md` (META-m1, "no derivation/citation anywhere in repo; deriving one now would be fabrication (pattern-036)"); flagged by `auto-2026-06-08_1424pt_P1A_OpenAI_methodology.md` (P1A-M2) and its SYNTHESIS. Horndeski braiding-scale M_crit is a live, unrelated research proposal, not tested. |
| Einstein-Rosen | 4: braindump, `VERIFIED_BIBLIOGRAPHY.md`, `archaeology_2025.bib`, `.../DAUGHTER_UNIVERSE_MEMO.md` | archaeology bibliography/memo only | — | Not tested against current BigBounce claims |
| white hole | many: `site/src/data/genealogy.ts`, `research/outputs/lit_lqg_bounce_2024_2026.json`, `project-context/SSOT/queue.md`, `.../DAUGHTER_UNIVERSE_MEMO.md` | site genealogy page + literature scan | genealogy.ts 2026-09-18 | Generic term; not itself a closed claim |
| baby universe | many: `arxiv/_retired/main.tex`, `research/paper_1_01_archive/main.tex`, `site/src/app/speculations/page.tsx`, `speculations.html` | retired archives + active `/speculations` page | `paper_1_01_archive/main.tex` 2026-03-17 | Framing term inside retired parent-BH cosmology; superseded by current ECH framework |
| daughter universe | 8: `project-context/NEXT_SCIENCE_LEDGER.md`, `site/src/data/genealogy.ts`, `project-context/SSOT/ENDORSER_OUTREACH_2026-09-02.md`, `.../DAUGHTER_UNIVERSE_MEMO.md` | ledger item + site genealogy page + closed memo | — | **Closed**: `PARENT_CHILD_BOOKKEEPING_MEMO.md` (W5, 2026-09-18) — no invariant parent→child amplification ratio |
| universe in a black hole | many: `research/paper_1_01_archive/main.tex`, `arxiv/_retired/main.tex`, `research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py`, `submission/paper_1_2/main.tex` | retired archives + closed Track C1/P4′ analysis | `paper_1_01_archive/main.tex` 2026-03-17 | **Closed** (dipole route): `poplawski_dipole_exclusion_2026_09_02.py`, DESI A95 exclusion, 2026-09-02 |
| Planck star | 5: `research/outputs/lit_lqg_bounce_2024_2026.json`, braindump, `VERIFIED_BIBLIOGRAPHY.md`, `archaeology_2025.bib`, `.../DAUGHTER_UNIVERSE_MEMO.md` | literature scan + archaeology bibliography | — | Not tested against current BigBounce claims |
| particle production | many: `arxiv/_retired/main.tex`, `research/paper_1_01_archive/main.tex`, numerous active `research/branch_*` dirs | widespread active research use (generic physics term, not a legacy-specific concept) | pre-existing, widespread | Not a single closeable claim — generic mechanism used across branches |
| matter amplification | 1: braindump only | archaeology inputs only | — | Zero-hit elsewhere — provenance only |
| entropy reset | 1: braindump only | archaeology inputs only | — | Zero-hit elsewhere — provenance only |
| cosmological natural selection | 2: braindump, `.../DAUGHTER_UNIVERSE_MEMO.md` | archaeology memo only | — | Discussed, not tested |
| Poplawski/Popławski | 200+ hits: `research/paper_1_01_archive/main.tex`, `arxiv/_retired/main.tex`, `research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py`, `pipelines/p2_chirality/chirality_catalog_paper.tex`, dozens of `project-context/peer-reviews/*` threads, `project-context/PAPER_LINEAGE_2026-08-05.md`, `project-context/NEXT_SCIENCE_LEDGER.md` | active citation across P1-family + P4 + closed Track C1/P4′ dipole analysis | `paper_1_01_archive/main.tex` 2026-03-17 | **Closed** (spin-axis dipole route only): `poplawski_dipole_exclusion_2026_09_02.py` (2026-09-02); mass/energy/entropy bookkeeping question remains open per Director's correction #2 |

---

## 2. M_crit definitions

Three distinct historical definitions found, matching Director's correction #3 exactly (no 4th found):

**(a) Retired parent-BH mass threshold** — `research/paper_1_01_archive/main.tex:228` and `arxiv/_retired/main.tex:246` (identical wording in both):

> `The parent black hole mass must satisfy $M_{\rm BH} > M_{\rm crit} = (M_{\rm Pl}^4/\rho_{\rm vac})^{1/3}\approx 10^{-3}M_\odot$, easily satisfied by any astrophysical black hole.`

Interpretation: minimum progenitor black-hole mass (in the "our universe born inside a black hole" framing) required for the interior vacuum-energy density to exceed the value needed to source the claimed dark-energy scale $\rho_{\rm vac}$ — i.e. a bound on which astrophysical black holes could have birthed a universe like ours. **This definition was flagged as unsupported and later deleted from the live paper** (see peer-review citations below); it survives only in the two retired/archived `.tex` copies.

**(b) Horndeski braiding scale** — `research/branch_I_bounce_compatible_DE/horndeski_bounce_stability/01_problem_statement.md:73`:

> `"cubic Horndeski with braiding scale M < M_crit develops ghost instability at the bounce"` (listed as a hoped-for "strong success" outcome of a not-yet-executed derivation, not an existing result)

Interpretation: a mass/energy scale below which the braiding function in a cubic Horndeski dark-energy Lagrangian would destabilize (ghost mode) at the cosmological bounce — a stability-boundary parameter for a live, unrelated bounce-compatible-DE research branch. No numeric value given; this is a target for a calculation, not a closed derivation.

**(c) Notion-era $\Lambda c^2 r^3/3G$ form** — cited by Director's correction #3 as historical but **not found** as a literal `M_crit` occurrence in any repo file searched (rg found no match for this exact expression in working-tree files); it is referenced only in the Director's correction text and the braindump itself, not independently corroborated in-repo. Treat as Notion/ChatGPT-provenance only pending independent verification.

**No 4th M_crit definition found.**

**Peer-review files that flagged the retired parent-BH M_crit as underived** (names only):
- `project-context/peer-reviews/auto-2026-06-08_1424pt_P1A_OpenAI_methodology.md` (finding P1A-M2: *"'The parent black hole mass must exceed M_crit ≈ 10^−3 M⊙' is asserted without derivation or citation."*)
- `project-context/peer-reviews/auto-2026-06-08_1424pt_P1A_SYNTHESIS.md` (carries the same P1A-M2 finding forward)
- `project-context/peer-reviews/R23conf_P1A_TRUTH_AUDIT.md` (META-m1: disposition **VERIFIED**, closed by deletion — *"'M_crit ≈ 10⁻³ M⊙' (L683) had no derivation/citation anywhere in repo; deriving one now would be fabrication (pattern-036). Reviewer's delete option taken. ... CLOSED — sentence deleted; no other M_crit refs remain."*)

---

## 3. Popławski

**`research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py` docstring (3-line summary):**
1. Confronts the DESI Legacy DR8 chirality catalog's coverage-calibrated 95% sensitivity upper limit ($A_{95}^{\rm obs}=0.98\%$, $N_{\rm support}=887{,}472$, both read verbatim from the committed P4 source) against literature-claimed/implied amplitudes for a preferred galaxy-spin axis motivating Popławski's rotating-black-hole-universe model.
2. Computes, deterministically (no fitting/optimization): a calibrated $1/\sqrt{N}$ sensitivity-floor scaling law, whether each literature amplitude exceeds $A_{95}^{\rm obs}$ at face value and after an illustrative (explicitly non-established) $g=0.398$ observed-to-physical bridge, and a numbered-assumptions exclusion statement.
3. Explicitly not a re-run of the DESI pipeline and not a re-derivation of any cited paper's own statistics.

**Output JSON exclusion statement** (`research/bh_universe_dipole/outputs/poplawski_dipole_exclusion_2026_09_02.json`, key `exclusion_statement.statement`):

> "Under the toy closure above (observed dipole amplitude == alignment efficiency eta), the DESI Legacy DR8 catalog's coverage-calibrated observed-label sensitivity excludes eta > 0.98% at >=95% coverage on the primary HC real-space channel -- i.e. any preferred-axis alignment mechanism that would produce an observed-label dipole above ~1% on this sample is disfavored, while the model's own literature motivation (Longo 2011 ~7%; Shamir 2012/2020/2022 ~2-20%; Shamir 2025 JWST/JADES ~20-33%, N=263) sits 2-30x above that floor."

The JSON also records: no Popławski paper located (1007.0587, 1111.4595, 1410.3881, 1910.10819) gives a derived dipole amplitude — only a qualitative alignment-tendency claim — so the exclusion runs on a toy closure (amplitude ≡ alignment efficiency η), not a literal model prediction.

**P4 abstract sentence containing the dipole null** (`pipelines/p2_chirality/chirality_catalog_paper.tex`, `\begin{abstract}`):

> "The result is consistent with zero ($z_{\rm mom}=+0.635$, one-sided rank $p=0.23768$)."

(Full sentence context: primary high-confidence observed-label dipole on 887,472 supported-pixel rows; this null result is the P4 measurement that the Track C1/P4′ script above confronts against Popławski-motivated literature amplitudes.)

---

## 4. Zero-hit terms (Notion/ChatGPT provenance only)

5 terms found nowhere in the working tree except `research/archaeology_2025/inputs/chatgpt_braindump_2026-09-18.md` (or, for one, not even there):

1. **Omega Singularity** — braindump only
2. **Inverse Cosmic Boundary** — 0 hits anywhere, including the braindump under this exact phrasing (only the variant "Inverted Cosmic Boundary" exists in-repo)
3. **QGIW** — braindump only
4. **matter amplification** — braindump only
5. **entropy reset** — braindump only

---

## 5. Lineage paragraph

The black-hole-parent-universe framing originated in `bigbounce.md` (2025-07-22, commit `36cfb8d7`, Houston-authored initial draft) — per `project-context/PAPER_GENEALOGY_2026-09-02.md` line 29, this genesis document's abstract states the universe "originated from the interior of a rotating black hole" alongside JWST 65/35% galaxy-spin evidence claims. It was first formalized in LaTeX as `research/paper_1_01_archive/main.tex` on **2026-02-26** (commit `b4d4c601`, "feat: arXiv-ready LaTeX paper + preview page"; `git log --diff-filter=A` on this path returns the later dossier commit `af25f807` 2026-03-17, since the file was further developed under that name — see `PAPER_GENEALOGY_2026-09-02.md` line 32 for the earlier b4d4c601 origin). The same parent-BH $M_{\rm crit}$/baby-universe content persisted into `arxiv/_retired/main.tex`, whose retirement commit is `2d93d0e4` (2026-09-02, "chore(arxiv): retire stale v2.3.18 monolith main.tex to arxiv/_retired/") — a single-commit history for that path (git log shows only the retirement commit itself, i.e. the file was moved/created at that path in one shot rather than iterated there). `project-context/PAPER_GENEALOGY_2026-09-02.md` documents the broader replacement chain: the 2026-07-14 P1 split (M44 non-Anthropic review round; `P1_SPLIT_CLOSURE.md`) narrowed P1A to 3 retained results and explicitly retired the 14-barrier catalog, R2/R3 DE closures, ALP/MCMC material, and galaxy payload from the reader-visible paper (preserved unedited in `arxiv/paper1_unified.tex`), and the 2026-08-05 P1C spinoff extracted the barrier catalog into a standalone draft (`arxiv/paper1c_nogo_survey/main.tex`). What replaced the parent-BH origin framing on the live/active side: the current Einstein-Cartan-Holst (ECH) spin-torsion papers (`arxiv/paper1a_ech_nogo.tex` and siblings) carry no parent-BH $M_{\rm crit}$ claim (it was deleted per the R23conf truth-audit, Section 2 above); the black-hole-universe question itself now lives only as (a) the closed Track C1/P4′ dipole exclusion (`research/bh_universe_dipole/`, 2026-09-02) and (b) the new `/genealogy` site page (`site/src/data/genealogy.ts`, 2026-09-18) that presents White Hole Sponge/ICBC/Black Hole Sponge/"Born in a black hole" explicitly as retired 2025-era hypotheses.

---

## 6. W1 addendum — completed `git log -S` history sweep (all 40 terms, 5,064 commits)

A second W1 pass ran the git-history half of the protocol (`git log -S"<term>" -- ':!*.pdf' ':!*.png'` for all 40 terms, to completion) that the W1r relaunch above explicitly skipped. This section adds three corrections/enhancements on top of §§1–5 rather than replacing them; §§1–5 (W1r, working-tree `rg`) stand as delivered. The full original write-up (per-term git-history commit lists for all 40 terms, complete summary table, full M_crit/Popławski sections) is preserved at `research/archaeology_2025/SOURCE_MAP_git_history_W1.md`.

**(i) Pre-campaign vs. campaign-only hits — important disambiguation.** Almost every row in §1's "files hit" column includes `site/src/data/genealogy.ts`, `project-context/SSOT/queue.md`, `project-context/NEXT_SCIENCE_LEDGER.md` item text, and/or the archaeology memos — **all of these were written by this campaign on 2026-09-18** (the braindump-ingestion commit `95affd13`, the ledger-item commit `6fd06cdb`, the genealogy-page commit `ddf40b75`, and the memo commits). The completed git-history sweep shows the following terms have **zero commits before 2026-09-18** — i.e., zero organic repo presence prior to this campaign, full stop, not merely "not on the old site": White Hole Sponge, Black Hole Sponge, Omega Black Hole, Omega Singularity, Big Rip, Inverted Cosmic Boundary, ICBP, QGBW, QGIW, Vacuum Collapse Anomaly, UMPBH, BHCP, CTEF, GGSC, WHCIF, BHCIF, P_crit/Pcrit, matter amplification, entropy reset, cosmological natural selection, Einstein-Rosen (as a named term), Omega Black Hole. Two of these (**Omega Black Hole**, **Inverse Cosmic Boundary**) show literally **zero hits in git history at all**, including today's campaign commits — the exact phrase/casing was never committed even by the braindump ingestion (which likely uses "Omega BH" shorthand or paraphrases). Do not read §1's "files hit" counts for these terms as evidence of any pre-2026-09-18 repo life; they are this campaign's own provenance-quarantine artifacts, exactly as intended.

**(ii) Additional M_crit peer-review citations.** Beyond `auto-2026-06-08_1424pt_P1A_OpenAI_methodology.md`/`_SYNTHESIS.md` and `R23conf_P1A_TRUTH_AUDIT.md` (§2 above), two earlier rounds also flagged the same parent-BH `M_crit` sentence as underived, by filename only:
- `project-context/peer-reviews/2026-06-04_R4fixed_P1A_DeepSeek_confab.md` (finding P1A-N1: *"'Parent black hole mass must exceed Mcrit ≈ 10⁻³ M⊙' has no citation or derivation."*)
- `project-context/peer-reviews/2026-06-01_R-multi-true95_P1A_R-round_direct_GPT5_methodology.md` (flags the parent-BH-mass parameter-naturalness assumption as unclear/unjustified, one round before the DeepSeek/OpenAI findings above)

**(iii) Precise lineage origin, cross-checked.** `git log --follow --diff-filter=A --format='%h %ad %s' --date=short` on both `research/paper_1_01_archive/main.tex` and `arxiv/_retired/main.tex` independently returns the **same** first commit for both paths: `b4d4c601` (2026-02-26, "feat: arXiv-ready LaTeX paper + preview page + nav padding fix") — i.e. both archived copies trace to one origin commit, not two separate lineages, resolving §5's `af25f807`-vs-`b4d4c601` hedge in favor of `b4d4c601` as the true origin (`af25f807`, 2026-03-17, is a later dossier commit that also touches the file, not its creation).

**(iv) M_crit definition (a), fuller quote** (same source, `research/paper_1_01_archive/main.tex:228`, extending §2(a)'s quote with the sentence W1r's excerpt cut off before):

> "The parent black hole mass must satisfy $M_{\rm BH} > M_{\rm crit} = (M_{\rm Pl}^4/\rho_{\rm vac})^{1/3}\approx 10^{-3}M_\odot$, easily satisfied by any astrophysical black hole. For a parent with $M=10\,M_\odot$ and dimensionless Kerr spin $a_*=0.7$, the required dilution factor $\Omega_{\rm initial}/\Omega_{\rm BH}\approx 10^{-22}$ is naturally achieved through $\sim 50$ $e$-folds of inflation."
