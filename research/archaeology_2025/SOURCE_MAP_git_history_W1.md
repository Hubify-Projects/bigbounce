<!-- Recovered from the original W1 worker transcript (its on-disk write was overwritten by W1r in a last-writer-wins race). Full `git log -S` sweep version. -->

# SOURCE_MAP — 2025 legacy-concept archaeology (repo + git history)

**Worker:** W1 (sonnet) · **Date:** 2026-09-18/19 · **Scope:** repository working tree +
full git history (5,064 commits, first commit `36cfb8d7` 2025-07-22) for every term in
PLAN.md §1 / the braindump's search-term list. Facts only; no dispositions (W6 owns those).

## Methodology + coverage note (read before the table)

- **Git-history search:** `git log -S"<term>" --format='%h %ad %s' --date=short -- ':!*.pdf' ':!*.png' | tail -15`
  run for **all 40 terms, to completion**. `git log -S` is a **literal, case-sensitive
  substring** pickaxe search (not the case-insensitive regex the `rg -i` half of the
  protocol uses) — a term can show zero git-history hits and still exist in the working
  tree under different capitalization or wording. Flagged per-row where this matters.
- **Working-tree search (`rg -il`):** the real `rg` binary is **not installed** on this
  machine (`ripgrep` not in Homebrew, `rg` on PATH is a shell-function shim that either
  no-ops or hangs waiting on stdin when run detached/non-interactively — confirmed by two
  failed sweep attempts, see below). Substituted `grep -ril` (this system's `grep` is
  `ugrep`, ripgrep-equivalent semantics) with the same exclude set (`node_modules`,
  `*.pdf`, `*.png`, plus `.next`, `.git`, `.vercel*`, and large binary-data extensions:
  `*.jpg/.parquet/.npy/.npz/.gz/.pt/.pyc/.fits/.tar` — the repo carries ~26k tracked
  galaxy-cutout JPGs plus multi-GB pipeline/data dirs that make an unscoped tree walk
  impractically slow under current host load, `uptime` load average 225–305 at time of
  search). A full 40-term automated `grep` sweep across the whole tree did **not complete
  before the director's time-box** (repeated multi-minute stalls per zero-hit term on this
  loaded host). Per the time-box instruction, rows below use: (a) the git-history result
  (a reliable **superset** proxy — any term literally present in the current working tree
  must have been introduced by some commit, so a true zero across all 5,064 commits means
  zero in the tree too, modulo the case-sensitivity caveat above), plus (b) **manual,
  targeted `grep`/`Read` spot-checks** actually completed for the physics-load-bearing
  terms (M_crit, rho_crit, Big Crunch, Popławski, ICBC) and cited inline. Rows without a
  targeted spot-check say **"history search only; working-tree rg not completed
  (time-box)"** rather than being omitted, per the director's instruction.
- Every git-history hit dated **2026-09-18 or later** is this campaign's own commits
  (`95affd13` opened the workspace with the verbatim braindump file, which by
  construction contains every search term — so a hit that is *only* 2026-09-18+ means
  **zero pre-campaign historical presence**, i.e. the term lived in Notion/ChatGPT only).

---

## 1. Summary table

| Concept | First appearance (pre-campaign) | Later mutations | Where it lives now | Tested/closed by current BigBounce? |
|---|---|---|---|---|
| White Hole Sponge | **None.** Only campaign commits `6fd06cdb`, `95affd13` (2026-09-18). | — | `research/archaeology_2025/inputs/chatgpt_braindump_2026-09-18.md` (provenance only) | N/A — never entered the repo pre-campaign |
| Black Hole Sponge | **None.** Only `95affd13` (2026-09-18). | — | Same input file only | N/A |
| Omega Black Hole | **Zero hits, ever** (incl. today) — exact phrase never committed verbatim (repo likely uses "Omega BH" shorthand where it appears at all; not verified under time-box). | — | Braindump prose only (as "Omega Black Hole"/"Omega BH") | N/A |
| Omega Singularity | **None.** Only `95affd13`. | — | Braindump only | N/A |
| Big Crunch | **None pre-campaign** by exact-case git-history pickaxe. Working-tree `grep -il` (case-insensitive, spot-checked) hits: `status.html`, `speculations.html`, `research/branch_V_bounce_evidence/05_top3_candidates.md`, `research/outputs/lit_lqg_bounce_2024_2026.json`, `project-context/NEXT_SCIENCE_LEDGER.md`, plus this campaign's own `VERIFIED_BIBLIOGRAPHY.md`/braindump. | `project-context/NEXT_SCIENCE_LEDGER.md` and the ledger-item-#20 commit `6fd06cdb` (2026-09-18) are this campaign opening the lane, not a pre-existing lane. | `research/archaeology_2025/memos/COSMIC_FATE_MEMO.md` (W3, opus) — turnaround-condition derivation | **W3 result:** no Crunch under constant Λ>0 (flat or closed, Ω_m<1); only a DE-density zero-crossing can turn the universe around. See `memos/COSMIC_FATE_MEMO.md`. |
| Big Freeze / heat death | Pre-campaign hit only via `heat death`→`70e840db` is this campaign's own bibliography commit. No pre-campaign git-history hit for either phrase. | — | Braindump + `COSMIC_FATE_MEMO.md` (baseline comparison) | Documented as the ΛCDM default baseline in W3's memo |
| Big Rip | **None.** Only `95affd13`. | — | Braindump only | Not separately modeled; W3 memo covers phantom/quintom as one of several turnaround-model classes |
| ICBC | One pre-campaign hit, `f11eb418` (2026-08-03, "release(p4): package v1.0.274 candidate") — **spot-checked and NOT confirmed**: `git show f11eb418 | grep -i ICBC` returns nothing textual; likely a coincidental pickaxe byte-match inside a binary/base64 diff chunk, not the historical ICBC concept. Otherwise zero. | — | Braindump only | N/A — not a real prior hit |
| Inverse Cosmic Boundary | **Zero hits, ever.** | — | Braindump paraphrase of "ICBC" only | N/A |
| Inverted Cosmic Boundary | **None pre-campaign.** Only `95affd13`. | — | Braindump only | N/A |
| ICBP | **None pre-campaign.** Only `ddf40b75`, `70e840db`, `95affd13` (all 2026-09-18 campaign artifacts: genealogy page, bibliography, workspace). | — | Braindump + new `/genealogy` site page (W7a, as a named retired item) | N/A |
| QGBW | **None pre-campaign.** Only `ddf40b75`, `95affd13`. | — | Braindump + `/genealogy` | N/A |
| QGIW | **None.** Only `95affd13`. | — | Braindump only | N/A |
| Vacuum Collapse Anomaly | **None pre-campaign.** Only `ddf40b75`, `95affd13`. | — | Braindump + `/genealogy` | N/A |
| UMPBH | **None pre-campaign.** Only `ddf40b75`, `70e840db`, `95affd13`. | — | Braindump + `/genealogy` | N/A |
| BHCP | **None pre-campaign.** Only `ddf40b75`, `95affd13`. | — | Braindump + `/genealogy` | N/A |
| CTEF | **None pre-campaign.** Only `ddf40b75`, `70e840db`, `95affd13`. | — | Braindump + `/genealogy` (raw-archive-only per braindump) | N/A |
| GGSC | **None pre-campaign.** Only `ddf40b75`, `70e840db`, `95affd13`. | — | Braindump + `/genealogy` | Braindump itself notes current DESI spin-axis test (P4/P5) is null regardless |
| WHCIF | **None pre-campaign.** Only `ddf40b75`, `70e840db`, `95affd13`. | — | Braindump + `/genealogy` | N/A |
| BHCIF | **None pre-campaign.** Only `70e840db`, `95affd13`. | — | Braindump only | N/A |
| M_crit / Mcrit | **`b4d4c601` 2026-02-26** ("feat: arXiv-ready LaTeX paper...") introduces the parent-BH threshold text in the original monolith `main.tex` (this is the same commit that created both `research/paper_1_01_archive/main.tex` and `arxiv/_retired/main.tex` — see lineage §5). Also present by `af25f807` (2026-03-17, "complete project intelligence dossier"). | Carried through R-rounds (`40d0293d` 2026-06-01, `080339e4` 2026-06-08, `279ed4c7` 2026-06-09 P1A R23conf, `9c181447` 2026-06-10) until flagged and **deleted** at R23conf truth-audit (see §2 below). A **third, unrelated** M_crit-adjacent symbol (Horndeski braiding scale, `M_crit` in prose) appears in `research/branch_I_bounce_compatible_DE/horndeski_bounce_stability/01_problem_statement.md` (created within Branch I, dated 2026-03-16 in-file). | **Deleted from the active P1A** (`arxiv/paper1a_ech_nogo.tex` has no M_crit reference — confirmed by direct grep of all current `.tex` sources, zero hits outside `_retired`/archive copies and stale site mirrors). Still present in `research/paper_1_01_archive/main.tex` (archival snapshot, 2026-03-13), `arxiv/_retired/main.tex` (retired 2026-09-02), and **stale site mirrors** `site/public/arxiv_v2/main.tex`, `site/out/arxiv_v2/main.tex`, `.vercel/output/static/**` (these serve the old arXiv-v2 monolith as a historical/public artifact, not the current paper). | **Closed.** `project-context/peer-reviews/R23conf_P1A_TRUTH_AUDIT.md` finding META-m1: *"M_crit ≈ 10⁻³ M⊙ (L683) had no derivation/citation anywhere in repo; deriving one now would be fabrication (pattern-036). Reviewer's delete option taken."* → **CLOSED — sentence deleted.** W3 (COSMIC_FATE_MEMO.md) separately reidentifies the *different*, Notion-era `M_crit = Λc²r³/3G` as the established turnaround-radius relation (Pavlidou–Tomaras), a salvage distinct from the deleted parent-BH threshold. |
| P_crit / Pcrit | **None pre-campaign** except the coincidental `4dbf500c` (this campaign's own cosmic-fate memo commit, 2026-09-18). | — | Braindump only — no coherent repo-native P_crit definition found anywhere, pre- or post-campaign | Braindump's own conclusion (§5) stands: retire, no buried derivation exists |
| rho_crit | **`af25f807` era and earlier; earliest clean hit `b8e7e461` 2026-02-27** area is close but the oldest confirmed line is inside `research/paper_1_01_archive/main.tex` (`\rhocrit`, same 2026-02-26 origin commit `b4d4c601`) and `horndeski_bounce_stability/01_problem_statement.md` (ρ_crit ≈ 0.21 M_Pl⁴, Planck-scale bounce density). | Recurs through 2026-07-14 (`e2214288`, `3e68aee8`, `44303fe3` — P1A axial-current/convention audits) and `cc2b7f88` (2026-07-08, P1B merge into P1A). | **Active, legitimate, model-specific.** Used as the ECSK/LQC-style bounce critical density in the modified Friedmann equation `H² = (8πG/3)ρ[1 − ρ/ρ_crit]` (`research/paper_1_01_archive/main.tex` L~232) — exactly the braindump's own recommended usage ("keep model-specific ρ_bounce/curvature threshold, don't universalize"). | Not closed — it is a normal, currently-used physics symbol, distinct from the retired universal M_crit/P_crit. |
| Einstein-Rosen | **None pre-campaign.** Only this campaign's `fde6179a` (DAUGHTER_UNIVERSE_MEMO), `70e840db`, `95affd13`. | — | `memos/DAUGHTER_UNIVERSE_MEMO.md` (W4) — terminology-cleanup taxonomy | W4 memo separates classical ER bridge / Haggard–Rovelli black-to-white / Popławski daughter-universe as three non-synonymous constructions, per braindump §6 |
| white hole | **`6db2d877`/`78b647a9`/`f6eea7c9`/`e1620a51`/`584dafa1`/`c9820742`, all 2026-02-18** (site page regenerations) and **`ec5dcd9f` 2026-02-26** (homepage overhaul + explainer page). Then `2b0b0086` 2026-03-03 (148-paper literature sweep). | Recurs in this campaign's `fde6179a`, `ddf40b75`. | Historical site copy only (2026-02 era pages); not in the current active-paper `.tex` set per the M_crit-adjacent grep above | W4's daughter-universe memo (causal taxonomy) supersedes loose "white hole" usage with named constructions |
| baby universe | **`36cfb8d7` 2025-07-22 — the repo's very first commit** ("Initial commit: BigBounce project"), then `2f041057` (2025-07-23), `f17d5b9b` (2025-08-13), `538bde5d`/`e94dca76` (2025-11-11, "scholarly revisions"), `b4d4c601`/`cdccf24f`/`440ef499`/`43202605`/`837106a2` (2026-02-26/27), `9649f47c`/`076ed67c` (2026-02-18), `49098d4d` (2026-02-15). | Present continuously from day one of the repo through the Feb–Mar 2026 arXiv-paper push. | Not in the current active P1A/P1B/P2/P3/P4/P5 `.tex`; lives in `memos/DAUGHTER_UNIVERSE_MEMO.md` framing | W4 memo covers the concept under the causal-taxonomy framework |
| daughter universe | **`bdbe2c3b`/`cdaf5f53`/`7a0904ec`, 2026-02-18/27** (site restructure, math derivations), **`0428f65b`** 2026-06-10 (P1A R24conf), **`ac065a61`/`0b3cfaba`/`f9185bcd`** 2026-09-02 (P4′ black-hole-universe spin-axis test folding P5 into P4). | Directly continuous into the **currently active** P4′ line. | **Active** — P4′ (`ac065a61`, "P4' — P5 folded into P4 as the black-hole-universe spin-axis test") is the live paper testing the Popławski-style daughter-universe spin-axis prediction | **Closed/null**, not open: DESI A95 exclusion, `research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py` (see §3) |
| universe in a black hole | **`36cfb8d7` 2025-07-22** (initial commit), then `2f041057` (2025-07-23), `f17d5b9b` (2025-08-13), `49098d4d` (2026-02-15), `9649f47c`/`b4d4c601` (2026-02-18/26), `2b0b0086` (2026-03-03), `b56ecd59` (2026-05-01), `fb44f757` (2026-06-05), `a4ee4ac4` (2026-09-02). | Present from the repo's first day through the current 2026-09-02 P4′ lineup. | Both historical (2025 origin paper) and **active** (P4′ black-hole-universe spin-axis framing) | See daughter-universe row — closed/null via DESI A95 |
| Planck star | Weak: only `2b0b0086` (2026-03-03, 148-paper comprehensive literature sweep) pre-campaign. | — | Literature-sweep mention only; not developed into repo physics content | Not tested; W4 memo lists it among the mechanism-class literature map |
| particle production | **`8dffa6e4`** 2026-02-18, then continuously through `b4d4c601`/`cdccf24f`/`440ef499`/`43202605`/`4c1da7d5`/`fe09a79e` (2026-02-26), `bdbe2c3b` (2026-02-27), `2c717333`/`a66de827` (2026-03-02), `2b0b0086` (2026-03-03), `a2e966a3` (2026-03-17), `84ae5b23` (2026-03-22), `27ea860b` (2026-04-18). | Continuous ECH-era physics usage (inflationary particle production in the bounce dilution mechanism, distinct from Popławski's daughter-universe particle-production amplification). | Active P1A physics content (dilution/e-folds discussion) | Reproduced independently for the Popławski mechanism by W5 (`memos/PARENT_CHILD_BOOKKEEPING_MEMO.md`) — 15/8/3 reproduce/partial/fail split, no invariant amplification ratio found |
| matter amplification | **Zero pre-campaign hits.** Only `95affd13`. | — | Braindump + W5's bookkeeping memo (as the reframed question) | W5 (`PARENT_CHILD_BOOKKEEPING_MEMO.md`): daughter can hold arbitrarily more proper matter, but the excess is set by a free production coefficient β, not by the parent mass — no invariant "amplification ratio" exists |
| entropy reset | **Zero pre-campaign hits.** Only `95affd13`. | — | Braindump only | Not yet separately studied; flagged in braindump as "real problem, old solution invalid" |
| cosmological natural selection | **None pre-campaign.** Only `70e840db`, `95affd13`. | — | `VERIFIED_BIBLIOGRAPHY.md` (Smolin citation), braindump | Comparison-only per braindump; not adopted |
| Poplawski / Popławski | **`f6669470` 2026-02-15** ("[astro-nova-v1] research: Updated literature review with 2025-2026 advances in bounce cosmology"), then `6e07ba96` (2026-02-15, peer-review methodology session), and the 2026-02-17/18 site-regeneration commits (`2806a58e`,`6dfa40cc`,`a9027d11`,`d1b54397`,`78b647a9`,`cc23e765`,`c9bf6b9d`,`95ceedce`,`c77400f1`,`15a3881f`,`e8f0f0e5`,`a0418aef`,`069ea32e`). | Citation persists through site regenerations; formal reproduction only happens in this campaign. | `research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py` (2026-09-02, pre-campaign) + `memos/PARENT_CHILD_BOOKKEEPING_MEMO.md` (W5, this campaign) | **Closed for the spin-axis dipole route** (DESI A95 exclusion, 2026-09-02) and **independently reproduced for the mass/energy bookkeeping route** by W5 this campaign (§3 below) |
| VCA (bounded) | Coincidental substring hits only (`5e995aa2`, `0428f65b`, etc. — P4/P1A confirmation-round commits; "VCA" is not a real acronym match in these diffs, consistent with braindump's own instruction to skip it via plain `rg` due to false positives). | — | N/A | N/A |
| BCR (bounded) | Coincidental substring hits only (P3 R33conf, EXT3-stamp, P4 pod-session commits). | — | N/A | N/A |
| SBA (bounded) | Coincidental substring hits only (P4 R23conf, arxiv-kit tarball commits). | — | N/A | N/A |

**Rows explicitly time-boxed with "history search only; working-tree rg not completed":**
ICBC, ICBP, QGBW, QGIW, Vacuum Collapse Anomaly, UMPBH, BHCP, CTEF, GGSC, WHCIF, BHCIF,
P_crit/Pcrit, Big Rip, Omega Singularity, Black Hole Sponge, White Hole Sponge, Omega
Black Hole, Inverse/Inverted Cosmic Boundary, entropy reset, cosmological natural
selection, Planck star, Einstein-Rosen. For every one of these the completed
git-history sweep found **zero pre-campaign commits**, which (case-sensitivity caveat
aside) is strong evidence they never entered the repo before this campaign's own
provenance file. None were spot-checked with an independent case-insensitive
working-tree pass before the time-box; treat "zero pre-campaign" as a high-confidence
proxy, not a working-tree-verified certainty.

---

## 2. M_crit — the (at least) three distinct historical definitions

**Definition 1 — Notion-era universal collapse mass, `M_crit = Λc²r³/(3G)`.**
Not found verbatim anywhere in the repo or git history (it predates the repo). Per the
braindump (§5) and W3's independent turnaround derivation, the physically real content
hiding inside it is the **maximum turnaround radius** for a bound structure against a
positive Λ, `r = (3GM/Λc²)^{1/3}` (Pavlidou & Tomaras), not a "universe-collapse" mass.
See `research/archaeology_2025/memos/COSMIC_FATE_MEMO.md` for W3's full re-derivation.

**Definition 2 — retired parent-BH threshold, `M_crit = (M_Pl⁴/ρ_vac)^{1/3} ≈ 10⁻³ M_☉`.**
Exact quote, `research/paper_1_01_archive/main.tex` line 228 (and byte-identical in
`arxiv/_retired/main.tex` line 246, `site/public/arxiv_v2/main.tex` line 246):

> "The parent black hole mass must satisfy $M_{\rm BH} > M_{\rm crit} =
> (M_{\rm Pl}^4/\rho_{\rm vac})^{1/3}\approx 10^{-3}M_\odot$, easily satisfied by any
> astrophysical black hole. For a parent with $M=10\,M_\odot$ and dimensionless Kerr
> spin $a_*=0.7$, the required dilution factor
> $\Omega_{\rm initial}/\Omega_{\rm BH}\approx 10^{-22}$ is naturally achieved through
> $\sim 50$ $e$-folds of inflation."

Interpretation as written: a naturalness bound ensuring any astrophysical-mass parent
black hole's vacuum energy scale exceeds the Planck-density threshold needed for the
Einstein-Cartan bounce mechanism to apply, so that the claim "any astrophysical black
hole works" holds without fine-tuning. **This is the definition the review process
found unsupported and deleted** — `project-context/peer-reviews/R23conf_P1A_TRUTH_AUDIT.md`,
finding META-m1: *"'M_crit ≈ 10⁻³ M⊙' (L683) had no derivation/citation anywhere in
repo; deriving one now would be fabrication (pattern-036). Reviewer's delete option
taken."* → closed by deleting the sentence from the active paper. It survives only in
the archival/retired copies and the stale `arxiv_v2` static site mirrors, never in the
currently active `arxiv/paper1a_ech_nogo.tex`.

Earlier reviewer rounds that flagged this exact sentence as underived/uncited, by
filename only (facts, no disposition):
- `project-context/peer-reviews/2026-06-04_R4fixed_P1A_DeepSeek_confab.md` (finding
  P1A-N1: "'Parent black hole mass must exceed Mcrit ≈ 10⁻³ M⊙' has no citation or
  derivation.")
- `project-context/peer-reviews/2026-06-01_R-multi-true95_P1A_R-round_direct_GPT5_methodology.md`
  (parameter-naturalness / parent-BH-mass assumption flagged as unclear/unjustified)
- `project-context/peer-reviews/R23conf_P1A_TRUTH_AUDIT.md` (META-m1, the closing
  truth-audit that ordered the deletion)
- `project-context/peer-reviews/autonomous-2026-04-18/01_paper1_grumpy_prd.md` (earlier
  pass flagged the adjacent "easily satisfied by any astrophysical black hole" phrasing
  as needing qualification, without yet calling M_crit itself underived)

**Definition 3 — Horndeski braiding scale, `M_crit` (or `M < M_crit`) in
`research/branch_I_bounce_compatible_DE/horndeski_bounce_stability/01_problem_statement.md`.**
Exact quote (Success Criteria, "Strong success" item 1):

> "A nontrivial EXCLUSION of a common DE model class (e.g., 'cubic Horndeski with
> braiding scale M < M_crit develops ghost instability at the bounce')"

Interpretation as written: this is a **hypothetical placeholder criterion**, not a
derived value — it is offered as an example of what a "strong success" finding in
Branch I *would look like* if the Horndeski-vs-bounce compatibility test found one. The
same document separately tabulates the bounce's actual background quantities (H, Ḣ, R,
ρ, ρ_DE — including `ρ_crit ≈ 0.21 M_Pl⁴`, a distinct, real, model-specific density),
and notes the DE sector is ~10⁻¹²² of the bounce density at the bounce (scale
separation), which the same document flags as the likely reason all compatibility tests
trivially pass. This `M_crit` is a different physical quantity (a scalar-tensor
coupling-scale threshold, never assigned a number) from both Definition 1 and
Definition 2, and the three should never be conflated — exactly the braindump's own
instruction (director's correction #3).

---

## 3. Popławski — script, outputs, and the P4 abstract null

**`research/bh_universe_dipole/poplawski_dipole_exclusion_2026_09_02.py` — docstring summary (3 lines):**
1. Confronts DESI Legacy DR8's coverage-calibrated observed-label 95%-sensitivity upper
   limit (A₉₅ᵒᵇˢ = 0.98%, N=887,472, both read verbatim from the committed P4 source, not
   re-derived) against literature-reported galaxy-spin-axis dipole amplitudes that
   motivate Popławski's rotating-black-hole-universe (Einstein-Cartan torsion-bounce)
   model.
2. Deterministic arithmetic only — a calibrated 1/√N illustrative sensitivity-floor
   scaling law, a face-value and g=0.398-bridge comparison of each literature amplitude
   against A₉₅ᵒᵇˢ, and a numbered-assumptions exclusion statement; no fitting, no
   optimization, no randomness.
3. Explicitly documents that **no Popławski paper it could locate gives a closed-form or
   numerically evaluated amplitude** for the preferred-axis dipole — `arXiv:1910.10819`
   states only a qualitative alignment tendency — so the exclusion is stated under an
   explicit "toy closure" assumption (observed dipole amplitude ≡ alignment efficiency
   η), not as a literal quantitative-prediction rejection.

**`outputs/poplawski_dipole_exclusion_2026_09_02.json` — exclusion statement (verbatim):**

> "Under the toy closure above (observed dipole amplitude == alignment efficiency eta),
> the DESI Legacy DR8 catalog's coverage-calibrated observed-label sensitivity excludes
> eta > 0.98% at >=95% coverage on the primary HC real-space channel -- i.e. any
> preferred-axis alignment mechanism that would produce an observed-label dipole above
> ~1% on this sample is disfavored, while the model's own literature motivation (Longo
> 2011 ~7%; Shamir 2012/2020/2022 ~2-20%; Shamir 2025 JWST/JADES ~20-33%, N=263) sits
> 2-30x above that floor."

**P4 abstract sentence with the dipole null**, `pipelines/p2_chirality/chirality_catalog_paper.tex`
(`\begin{abstract}...\end{abstract}` block):

> "The result is consistent with zero ($z_{\rm mom}=+0.635$, one-sided rank
> $p=0.23768$)."

(Full abstract context: this is the primary high-confidence observed-label dipole test
on 887,472 quality-controlled DESI Legacy DR8 galaxies; the same abstract states the
$A_{95}^{\rm obs}\simeq0.98\%$ sensitivity floor used by the exclusion script above, and
explicitly flags it as "an observed-label sensitivity floor, not a physical
parity-amplitude bound," gated on the unresolved morphology transfer function.)

---

## 4. Terms with ZERO hits, repo + full git history (Notion/ChatGPT provenance only)

Confirmed by completed `git log -S` sweep across all 5,064 commits (case-sensitive
literal-string pickaxe; case-insensitive working-tree variants not independently
verified under the time-box — see methodology note above):

- **Omega Black Hole** (zero hits including this campaign's own commits — the exact
  phrase, this casing/spacing, was never literally committed even in the braindump
  ingestion; braindump likely uses "Omega BH" or paraphrases in places pickaxe didn't
  catch)
- **Inverse Cosmic Boundary** (zero hits at all, including campaign commits)
- **P_crit / Pcrit** (zero pre-campaign; braindump's own conclusion is that no coherent
  definition exists to preserve)
- **Matter amplification, entropy reset** — zero pre-campaign; both are this campaign's
  own reframings of older ideas, not repo-native terms
- **ICBP, QGBW, QGIW, Vacuum Collapse Anomaly, UMPBH, BHCP, CTEF, GGSC, WHCIF, BHCIF** —
  zero pre-campaign hits for all ten "Equations Part 1" / raw-AI-generated-ansatz terms
- **VCA, BCR, SBA** (as bounded acronyms) — no genuine historical hits; every git-history
  match found is a coincidental substring collision in unrelated commit content
  (confirming the braindump's own instruction to skip these via plain-text `rg` search)

## 5. Lineage as visible in git

The git history shows the "black-hole-parent-universe" framing was **never absent from
the repo** — it was present in the very first commit. `36cfb8d7` (2025-07-22, "Initial
commit: BigBounce project") already carries "baby universe" and "universe in a black
hole" language, consistent with the braindump's own account that by July 2025 Houston
had already moved past the March-2025 White-Hole-Sponge/ICBC Notion era into the
black-hole-parent/daughter-universe framing before the repo existed — the March 2025
Notion terminology (White Hole Sponge, ICBC, QGBW, Omega Black Hole, VCA, etc.) has
**zero presence anywhere in git history**, confirming it lived and died in Notion/ChatGPT
threads that predate this repository by roughly four months and were never committed.

The parent-black-hole framing was carried into the repo's first formal LaTeX paper at
`b4d4c601` (2026-02-26, "feat: arXiv-ready LaTeX paper + preview page + nav padding
fix") — the single commit that simultaneously created the text now preserved in both
`research/paper_1_01_archive/main.tex` (archived 2026-03-13, per its own
`ARCHIVAL_NOTE.md`, as a pre-reconsideration snapshot ahead of the four-route
dark-energy-derivation closure that produced "Paper 1.2") and, via later copies,
`arxiv/_retired/main.tex` (explicitly retired 2026-09-02, per its own `README.md`, as
"the June-2026 v2.3.18 unified monolith paper... superseded by the split-paper
architecture" — the same commit, `2d93d0e4`, states "The registered, actively
maintained P1A source is `arxiv/paper1a_ech_nogo.tex`," per
`project-context/paper_registry.json`). Both archived copies still carry the
now-deleted `M_crit ≈ 10⁻³ M_☉` parent-black-hole naturalness line (§2, Definition 2).
What replaced it in the currently active line: `arxiv/paper1a_ech_nogo.tex` (the ECH
no-go framing — the positive torsion-bounce mechanism retained, four dark-energy
derivation routes closed) for the theory side, and the **P4′** paper
(`ac065a61`, 2026-09-02, "P4' — P5 folded into P4 as the black-hole-universe spin-axis
test") for the observational side — which is where the daughter-universe framing is
still alive today, now as a closed/null result (DESI A95 spin-axis exclusion, §3) rather
than a live hypothesis. The `M_crit` sentence itself did not survive this transition; it
was deleted at `R23conf` (per the truth-audit quoted in §2) rather than carried forward
or re-derived.
