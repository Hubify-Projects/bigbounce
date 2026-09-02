---
title: "Paper 2L SSOT — P2′ Letter: Exact Matter-Contraction f_NL"
type: ssot
paper: 2L
last_updated: 2026-09-02 — CREATED. v2L.0.1, 4 pp, md5 66a28438cc0f0b8dc347a3016389363f, 0 undef refs, 0 overfull hboxes.
canonical_source: arxiv/paper2prime_fnl_letter/main.tex
canonical_pdf: arxiv/paper2prime_fnl_letter/main.pdf (4 pp / 0 undef refs / md5 66a28438cc0f0b8dc347a3016389363f)
version: v2L.0.1 (2026-09-02, created)
registry_id: P2L (project-context/draft_paper_registry.json)
review_profile: PRD-LETTER
target_journal: Physical Review D — Letters (JCAP alternate)
headline_pct: not-yet-reviewed (agent gates: science 25 / evidence 0 / review-convergence 0 / packaging 20 = ~45; no INT/EXT board run yet)
submission_status: draft, unreviewed — first INT/EXT board pending
---

# P2L status — current authoritative section

**Origin.** Rescoped from Paper 2 (`research/focused_paper_source_integration/02_full_draft.tex`,
v1.7.130, 11 pp — **left unedited**) per `project-context/PORTFOLIO_DECISION_2026-09-02.md`
§3 Track A A1: "a short Letter (≤6 pp, PRD-L/JCAP): the exact matter-contraction amplitude
f_NL = −35/16, correcting Cai et al. 2009's −35/8." Unblocked by
`project-context/NEXT_SCIENCE_LEDGER.md` row #1, marked **CLOSED — REPRODUCES −35/16
(2026-09-02)** by the from-scratch in-in adjudication
(`research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.{md,py,json}`).

**What the Letter contains (all traceable to a committed artifact, directive Q1/never-fabricate):**
1. The from-scratch in-in derivation and per-vertex table (Table I), validated against the
   de Sitter (Maldacena 2003) and ultra-slow-roll (Namjoo–Firouzjahi–Sasaki 2012, f_NL=5/2)
   limits before use — `fnl_matter_contraction_adjudication_2026_09_02.md` §§2–3.
2. The resolution of Cai et al. 2009's −35/8: a uniform factor-2 in their amplitude-
   normalization step (their Eq. 37 shape function is correct monomial-by-monomial) —
   same source §4.
3. **New result:** the orientation-dependent squeezed limit
   f(μ) = −35/16 + (15/16)μ² (monopole −15/8, quadrupole 15/16), sourced by the non-attractor
   growing mode's shear — same source §§3, 6; framed against Namjoo–Firouzjahi–Sasaki 2012 and
   Chen–Namjoo–Wang 2013.
4. The δN cross-check on uniform-density slices, (5ε−35)/8 = −55/16 at ε=3/2, reconciled via
   ζ_ρ=2ζ_c at linear order — `fnl_matter_contraction_second_method_2026_09_02.md` +
   adjudication §5.
5. An honest transmission statement (NOT P2's assumption-(d)/T_c=1): linear transfer bound
   0 < T_fNL ≤ 1/2, scheme-dependent 1.64× on the same background, with the bounce's own
   cubic term (Agullo–Bolliet–Sreenath 2017: can enhance NG by orders of magnitude) explicitly
   flagged as not computed — `research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md`.
6. Survey reach table: DESI DR1 0.16σ tension (no discriminating power), SPHEREx 2.6–3.7σ
   separation between −35/16 and −35/8 — `research/track_a3_multichannel/A3_MULTICHANNEL_BRIEF_2026-09-02.md`
   §3 (Heinrich, Doré & Krause 2023 σ_fNL = 0.5–0.7).

**What was cut from P2 v1.7.130 and where it still lives (nothing deleted, all preserved
in the parent forecast paper, unedited):**
- The full nuisance-parameter (b_φ) ladder, universality-relaxation degradation bands,
  and Bayes-factor prior-sweep — stays in P2 (§§ III–VI of `02_full_draft.tex`).
- The model-specific torsion bound (Assumption f) and the dressed-metric transmission
  closure detail (G1, T_c(k)=1 for the constant branch) — stays in P2; the Letter instead
  reports the A2 brief's fuller linear-transfer result (T_fNL ≤ 1/2 for the physical,
  growing-branch-dominated mode), which supersedes the narrower P2 statement.
- The full SPHEREx/MegaMapper Fisher sensitivity recast across 15 survey configurations —
  stays in P2; the Letter reports only the two headline SPHEREx numbers needed to state
  discriminating power between −35/16 and −35/8.
- Zenodo DOI, AI-usage disclosure boilerplate, and companion-paper cross-references —
  retained in compressed form (Data/Code Availability + AI Usage Disclosure sections).

**Compile record:** 4-pass pdflatex + bibtex, tectonic-equivalent revtex4-2 [aps,prd,reprint]
matching P2's preamble construction. `pdftoppm -r 60` visual check of all 4 pages: clean,
no column overflow, no overfull hboxes (one 76pt overfull in the reach table fixed by
`\small` + shortened column head before final compile). 0 undefined refs/citations (bibtex
warnings are cosmetic "missing number" fields on 4 entries, not undefined-citation errors).
Abstract: 259 words (target ≤~250; within tolerance), no parenthetical citations (author-year
attributed in prose per PRD Letter convention).

**Figures/bib:** No P2 figure was reused (P2's `fig1_shape_function.png` was evaluated and
dropped in favor of two compact in-text tables, which fit the ≤6 pp Letter format better and
carry the same information — Table I per-vertex breakdown, Table II survey reach).
`references.bib` extends P2's `03_references.bib` entries (Cai:2009fn, Maldacena:2002vr,
Dalal:2007cu, Heinrich:2023, Dore:2014, copied unmodified) with new entries for
Li:2016, Quintin:2015, CaiEassonBrandenberger:2012, Namjoo:2012, Chen:2013aj,
AgulloBollietSreenath:2017, Papanikolaou:2025, Choudhury:2025 (real arXiv IDs verified
against the source briefs, e.g. Choudhury et al. 2025 = arXiv:2409.18983, EPJC 85:472),
plus three self-cite `@misc` entries pointing at the committed theory-audit/A2/A3 artifacts.

**Mirrors:** `site/public/papers/paper2prime_fnl_letter_v2L.0.1.pdf` and
`public/papers/paper2prime_fnl_letter_v2L.0.1.pdf`, both md5-verified byte-identical to
`arxiv/paper2prime_fnl_letter/main.pdf` (66a28438cc0f0b8dc347a3016389363f).

**Open (not done this session, directive-scoped out):** no INT/EXT review board has been
run on P2L yet (out of scope for this drafting task); no site/Convex wiring (explicitly
excluded from this task); Houston sign-off pending.

---

## R1 closure — 2026-09-02 (evening)

**Round:** `ROUND_2026-09-02-P2L-v2L.0.1-EXACTPDF-e1501145-R1` (Fable INT MAJOR REVISIONS
5 MAJOR/13 MINOR; Grok API REJECT 4E/4M/2N/1NIT/1STALE/1ARITH; Gemini API MAJOR REVISIONS
4E/4M/3N; Perplexity ABSENT). Truth-audit: 18 canonical items dispositioned
GENUINELY-NEW-REAL (5 MAJOR, 12 MINOR, 1 NIT), plus 5 leg claims FALSIFIED and 1
OUT-OF-SCOPE, all source-cited. Full audit:
`project-context/peer-reviews/INT_v3/ROUND_2026-09-02-P2L-v2L.0.1-EXACTPDF-e1501145-R1/P2L_v2L.0.1_R1_truth_audit.md`.

**Scope decision (Houston-orchestrator, recorded verbatim in
`project-context/PAPER_LINEAGE_2026-08-05.md`):** the Letter's genuine contribution is a
confirmation (independent in-in reproduction of −35/16, already printed by Li et al. 2016
Eq. 4.19 and quoted by Quintin et al. 2015), not a discovery, and does not carry a
standalone PRD Letter. Closed to an honest v2L.0.2 as the archived theory record; content
folds into the theory section of `research/track_a3_multichannel/paper/` (the A3
multi-channel paper). A standalone Comment on Cai et al. 2009 remains an option if a
referee/authors request it. Convergence budget: **one round run; rounds stop here for the
Letter** (directive R2).

**Item → edit table (all 18 GNR items closed in `main.tex`):**

| id | sev | edit |
|---|---|---|
| DP2L-01 | MAJOR | `f_{\rm NL}^\rho` corrected to `5(\epsilon-7)/8=-55/16` (boxed eq. in §III cross-check) |
| DP2L-02 | MAJOR | Title/abstract/§III/Summary reframed as independent *confirmation* consistent with Li+2016 Eq. 4.19; "new result" language removed |
| DP2L-03 | MAJOR | Table II rewritten: bare vs. `r=0.84`-projected columns, `r` defined+sourced+caveated (A3-4 not-yet-re-derived note), DESI DR1 σ≈9.0 row added |
| DP2L-04 | MAJOR | references.bib: Li:2016 → correct authors/title/JCAP 1703 031; Chen:2013aj → correct EPL 102 59001 paper; Choudhury:2025 given names fixed; unused `CaiEassonBrandenberger:2012` removed |
| DP2L-05 | MAJOR | `\zeta_\rho=2\zeta_c` and `T_{f_{\rm NL}}=(1-\rho)/2` derived in-text (§IV, §III cross-check); artifact links pinned to commit `68309c8` |
| DP2L-06/07 | MINOR | Abstract states 2.6–4.4σ by channel; DESI row filled σ≈9.0, cited Chaussidon+2024 (arXiv:2411.17623), 0.24 discriminating power printed |
| DP2L-08 | MINOR | isoceles → isosceles (all instances) |
| DP2L-09 | MINOR | `(§ 2311.13082)` → `arXiv:2311.13082` |
| DP2L-10 | MINOR | "This supersedes an earlier, narrower statement…" deleted |
| DP2L-11 | MINOR | μ²-vertex attribution named explicitly (field-redefinition −15/16μ², ζ′∂ζ·∂χ̃ +15/8μ²) |
| DP2L-12 | MINOR | "amplitude-normalization step" reworded to not over-localize the factor 2 |
| DP2L-13 | MINOR | δK sign convention stated (Maldacena ADM, used throughout) |
| DP2L-14 | MINOR | "not an independent check" reworded; states Li+2016 print −35/16 directly |
| DP2L-15 | MINOR | Table I caption defines `f^{\rm sq}(\mu)` |
| DP2L-16 | MINOR | Title/abstract "exact local" → "independent...confirmation"; μ-dependence disclosed |
| DP2L-17 | MINOR | Both 1.64× (same-background) and 2.48× (full-range) now stated |
| DP2L-18 | NIT | Retained (house-style preprint stamp is required for the repo/arXiv build per directive G) |

DP2L-F1…F5 (FALSIFIED leg claims) and DP2L-O1 (OUT-OF-SCOPE) recorded, no edit required.

**Hygiene:** `\paperVersion` v2L.0.2, `\date` September 2, 2026; 4-pass pdflatex, bibtex,
0 undefined refs/citations, 0 overfull hbox after `table*` fix for Table II; `pdftoppm -r
60` all 4 pages visually verified. md5 `718521c10032511339b334ff6f277629`, 4 pp, byte-identical
across `arxiv/paper2prime_fnl_letter/main.pdf`, `site/public/papers/paper2prime_fnl_letter_v2L.0.2.pdf`,
`public/papers/paper2prime_fnl_letter_v2L.0.2.pdf`.

**Readiness:** unchanged pending Convex/site sync + Houston review; content gate (R1) closed.

## Final review 2026-09-02 (orchestrator)
DEFER — archived theory record; content folded into A3 (see FINAL_REVIEW_RECOMMENDATIONS_2026-09-02.md).
