# P4′ v4P.0.8 — exact-version re-verification board, truth audit (v4P.0.8 → v4P.0.9)

- **Round:** `ROUND_2026-09-19-P4P-v4P.0.8-EXACTPDF-e8f1969e-REVERIFY`
- **Reviewed PDF:** `pipelines/p4prime_chirality_test/paper/main.pdf`, v4P.0.8, sha256
  `e8f1969e415777622561dde0f21a8ac7d6398c3b2ef55f69200ba50a89d91cd2`, md5
  `b2399780320a50542279c35410b6b545`, 14 pages.
- **Why this board ran:** campaign 2026-09-18 lane L4 closed 7 MAJOR + 12 MINOR
  findings from an exact-v4P.0.7 confirmation board, producing v4P.0.8. Those
  closures had not themselves been independently reviewed. Directive R2
  permits exactly one further consecutive verification round on this content
  before an intervening science/scope decision is required — this is that
  round (lane L4b, `bb-L4b-p4p-reverify`). **No third round is authorized
  after this one.**
- **Legs run:** (1) Grok API (`grok-4.3`, rasterized-PNG native input), (2)
  Gemini API (`gemini-3.1-pro-preview`, native PDF + pass-2 self-critique),
  (3) Claude opus INT referee sub-agent (full repo/source access,
  verdict-blind, explicitly NOT shown the v4P.0.7→v4P.0.8 closure list or
  `DISPOSITIONS/P4P.md` before writing its report). Codex/OpenAI paused
  (directive N).
- **Raw receipts:** `API_P4P_Grok_brutal.md`, `API_P4P_Gemini_cosmology.md`,
  `P4P_claude_reverify_leg.md` (all in this round directory).
- **Preflight:** portfolio preflight receipt generated and verified
  immediately before dispatch (`tools/bigbounce_preflight.py run` →
  `verdict: PASS`); the first attempt went stale because a concurrent lane
  (A3M, R9) committed to shared site-data files between receipt generation
  and dispatch — regenerated and redispatched successfully on retry.

## Verdict matrix (words are diagnostic, not the gate — directive P)

| Leg | Verdict | MAJOR/ESSENTIAL | MINOR | NIT |
|---|---|---|---|---|
| Grok (`grok-4.3`) | REJECT | 4 (E1–E4) + 5 (M1–M5) | 3 | 3 |
| Gemini (`gemini-3.1-pro-preview`) | ACCEPT WITH MINOR CORRECTIONS | 0 | 1 | 1 |
| Claude opus INT (verdict-blind, cold read) | major-revisions | 6 (A1–A6) | 11 (B1–B11) | 7 (C1–C7) |

## Disposition method

Every MAJOR/ESSENTIAL finding was independently re-verified by the orchestrator
directly against the cited committed JSON/script/source-`.tex`, or by direct
recomputation (angular separations, arithmetic, quantile fractions) — not
accepted from reviewer text alone — per `/never-fabricate-derivation` and the
campaign's standing truth-audit rule. Genre/convention objections were checked
against `project-context/peer-reviews/DISPOSITIONS/P4P.md` fingerprints from
R1–R3 and the 2026-09-18 confirmation board before being re-dispositioned.

## GENUINELY-NEW-REAL — closed in v4P.0.9

All six Claude-leg MAJOR findings (A1–A6) were independently re-derived by the
orchestrator from the underlying committed artifacts (not merely accepted from
the referee's citations) and confirmed real:

1. **A1 — pixel-injection baseline named the wrong comparator sample and the
   wrong amplitude convention** (main.tex l.996–999, pre-edit). "The catalog's
   HC monopole ($f_{\rm CW}-\tfrac12=-0.265\%$)" is wrong on both counts:
   $-0.265\%$ is the paper's own §2.2-stated **catalog-wide** monopole, not
   the HC-selected sample's (which is $-0.395\%$ with unsafe rows retained, or
   $+1.2656\%$ for the primary channel) — confirmed by direct read of main.tex
   §2.2 (l.283–290, pre-edit). Fixed: names the catalog-wide sample
   explicitly, gives the correctly-doubled $A_p=-0.53\%$ comparator, and notes
   the HC-selected sample's own monopole is positive.
2. **A2 — "a third, near-antipodal axis" is quantitatively false, and the
   full pairwise pattern was selectively reported** (l.1055–1059, pre-edit).
   Recomputed all six pairwise angular separations among the four QC-sweep
   axes from `full_parent/row16ib_axis_shift.json`'s own `axis_ra_deg`/
   `axis_dec_deg` fields (haversine great-circle formula): C0–C1=119.94°,
   C0–C2=17.34°, C0–C3=107.51° (matches the JSON's own
   `axis_separations_deg.C0_vs_C3`), C1–C2=115.25°, **C1–C3=19.27°**,
   C2–C3=108.18°. Max separation is 119.9°, nowhere near antipodal (180°);
   the paper reported only the 107.5° figure and omitted that the
   `primary_hc`-relaxed excess axis (z=+9.13) sits 19.3° from the primary
   channel's own axis. Fixed: corrected the false "near-antipodal" claim and
   disclosed the two close-agreeing axis pairs.
3. **A5 — "density-tercile split" is a mislabeled 20/60/20 quintile split**
   (l.1138–1139, pre-edit). `chirality_structure/row16ivb_bgs_environment.py`
   l.66–68 bins on `np.quantile(dl, [0.2, 0.8])` and its own docstring says
   "quintile bins"; Table 8's own N's (24,284/72,849/24,284 of 121,417 =
   exactly 20/60/20%) prove it. Fixed: "tercile" → "quintile" with the
   correct bin definitions spelled out.
4. **A6 — the "0.79 correlation" is misattributed to the monopole channel**
   (l.580–586, pre-edit). Read `g3_joint_estimator_covariance_master_v2.json`
   directly: `estimator_names=[realspace, WLS, monopole, Cl1_master]`;
   monopole↔Cl1_master = $-0.061$, monopole↔realspace = $-0.037$; the $0.794$
   figure is realspace↔Cl1_master — nothing to do with the monopole, and the
   paper's own next sentence ("monopole is nearly uncorrelated with the other
   three") contradicts the parenthetical two lines above it. Fixed: removed
   the false monopole/FSC identification, correctly attributed the 0.79
   figure, and explicitly disclaimed that this bootstrap's in-sample "MASTER
   ℓ=1" channel (different sample/support/null) is not the same statistic as
   the §3 FSC ℓ=1 diagnostic.
5. **A3+A4 — the two most consequential caveats in §A.1 (the pixel-transfer
   tension and the primary channel's own leg-instability) have no forward
   reference from anywhere the headline claim is stated.** Confirmed by
   direct grep: `grep -n "robustness_disclosure" main.tex` (pre-edit)
   returned exactly two hits — the `\label` itself and one Data Availability
   pointer — with zero hits in the Abstract, §3, §5, §6, or §7. Fixed with
   four targeted insertions (not a rewrite of the disclosure content itself):
   one paragraph in §3's observed-label caveat block, one sentence in
   Assumption 2 (§5), one sentence in Discussion (§6), one sentence in
   Conclusions (§7) — each pointing at §A.1 and stating the two results'
   headline-qualifying implications plainly, without adopting them as
   corrections (consistent with the disclosure's own "not resolved here"
   framing). The Abstract was deliberately left untouched: it is already at
   the ApJS 250-word single-paragraph cap (confirmed by word count), and a
   reader following §1→§3→§5→§6→§7 now encounters the caveat before reaching
   the Conclusions regardless.

Also closed, real and cheap (verified against source before editing):

6. **B1** — "15 of 17" structure-battery count does not reconcile (17 declared
   − 1 unavailable = 16, not 15); source doc `ROW16IV` carries the same
   off-by-one. Fixed to "16 of 17" (both text occurrences).
7. **B4** — C3/primary-channel leg exceedances incompletely enumerated (paper
   named 2 of 6); recomputed from `row16ib_axis_shift.json`'s own `legs`
   block: 5 of 6 single-leg fits exceed $A_{95}^{\rm obs}=0.98\%$ (only
   BASS+MzLS z=+2.00 A=3.92%; only DECaLS z=+2.20 A=1.66%; drop DECaLS
   z=+4.19 A=2.21%; only DES z=+2.49 A=5.83%; drop DES z=+4.26 A=1.39%);
   only drop-BASS+MzLS (z=+1.02, A=0.66%) does not. Fixed: full enumeration.
8. **B5** — "except Shamir (2025)" is inconsistent with Table 5's own
   low-end-amplitude convention (Shamir 2025's 20% low end is below the
   ≈25.5–25.8% implied floor). Fixed to state the low-end convention
   correctly (all five rows' low ends fall below; only Shamir 2025's range
   straddles it).
9. **B6** — Data Availability's "not reproduced" list wrongly included
   T-Web, which §4/Fig. 3 does reproduce in this manuscript. Fixed: T-Web
   carved out of that list with a pointer to Sec. 4.
10. **B7** — the $0.1<z<0.4$ BGS window was attached to the wrong parent
    (231,549-spiral parent is $0<z<0.6$ per `ROW16IVB_BGS_ENVIRONMENT_2026-
    09-05.md` §4.2; the window is what *reduces* it to 121,417, not a
    property the 231,549-row parent already carries). Fixed.

## FALSIFIED / RE-FLAG / OPINION this board — do not re-open without new evidence

| Finding | Verdict | Source-cited basis |
|---|---|---|
| Grok E1/E4 — abstract/Table-5 g-bridge factor unestablished | **RE-FLAG-OF-DISCLOSED** | precedent DP4P-10, DP4P-24; body/Table-5 caption/Assumption-2 already state $g=0.398$ is illustrative and not adopted for strengthening |
| Grok E2 — Poplawski papers give only a qualitative tendency, $A_{\rm pred}\approx\eta$ is author-introduced | **RE-FLAG-OF-DISCLOSED** | main.tex l.93, l.734, l.827 (pre-edit) already state this in exactly these terms, and Eq. 4 is explicitly presented as a named Assumption, not a literature result |
| Grok E3 — $z_{\rm mom}$/FSC juxtaposed without "not comparable" qualifier | **FALSIFIED** | precedent (line 306, 358 of DISPOSITIONS/P4P.md, same finding twice before); main.tex still states "uses a different support" / "a distinct statistic ... neither supersedes the other" at both mentions |
| Grok M1 — manuscript overlength for an ApJS catalog paper | **OPINION/GENRE** | subjective page-count preference; 14pp including all tables/figures/appendix is within ApJS norms for a catalog+exclusion paper carrying full disclosure content |
| Grok M2 — DESIVAST void/non-void test is post-hoc, "hierarchy fixed after inspecting the data" | **FALSIFIED** | main.tex §4 (l.632–635, pre-edit) states this **verbatim**: "This test is exploratory and post-hoc (the void/non-void hierarchy was fixed after inspecting the data)" |
| Grok M3 — "largest test" claim conflicts with Shamir (2022)'s larger $N$ | **RE-FLAG-OF-DISCLOSED** | precedent DP4P-01; abstract and Discussion both explicitly except Shamir (2022) by name in the same sentence as the "largest" claim |
| Grok M4 — released classifier's $\kappa=0.40$ (69.91%) insufficiently disclosed | **RE-FLAG-OF-DISCLOSED** | precedent DP4P-04; Table 3 + §2.2 report $\kappa=0.40$/69.91% and explicitly distinguish it from the retrain's $\kappa=0.97$ |
| Grok M5 — Fig. 1 "no coherent structure" lacks a quantitative test | **OPINION/GENRE** | precedent (Grok M3, prior round); caption already hedges "visually apparent", and quantitative dipole/harmonic tests exist elsewhere (§3) |
| Grok m1 — Table 1 `score_eq_max` description "truncated" | **FALSIFIED** | main.tex l.220: `\texttt{score\_eq\_max} & $\max$ eq.\ class score ($p_{\rm eq}$)` — complete, normal terse table-column description |
| Grok m2 — Neyman-limit description missing "complementary" statement | **FALSIFIED** | main.tex l.466–474 (pre-edit) already states the full complementary-Neyman-inversion construction in one explicit sentence |
| Grok m3 — "this research program's own bounce papers" reads as self-promotional | **OPINION/GENRE** | sentence is a factual cross-reference explaining research motivation (l.140, pre-edit), not a promotional claim; no superlative or unsupported claim present |
| Grok NIT — "future date" September 18, 2026 | **FALSIFIED** | today's date is 2026-09-18 (session date); not a future date |
| Grok NIT — inconsistent one-sided/two-sided labeling | **FALSIFIED** | every occurrence (l.87, 91, 423, 485, 523, 639, 1177 pre-edit) explicitly labels its own tail |
| Grok NIT — Table 8 caption doesn't repeat null definition | **OPINION/GENRE** | caption cross-references the null defined in-text immediately above; not a defect |
| Gemini M1 — three URLs contain spaces mid-string | **FALSIFIED** | `main.tex` l.1209, 1232, 1351 (pre-edit) contain no spaces in any of the three URLs; this is a PDF-render column-wrap artifact of the reviewer's native-PDF read, same pattern as prior-round Gemini N3 (space in HF URL, also FALSIFIED) |
| Gemini N1 — internal version string non-standard in the journal date line | **OPINION/GENRE** | standard practice across every paper in this campaign; aids cross-referencing served PDFs to Convex/SSOT state; will be stripped at actual journal production if required |

**Claude opus leg minors deferred, not silently dropped (documented reason,
no further round authorized on this content without a scope decision per
directive R2):** B2 (full-parent channel's own 0.51% injection-calibrated
floor omitted — real, but requires a considered rewrite of how much of the
full-parent disclosure narrative to restructure, not a one-line fix), B3
(two different-seed null realizations of the C0 fit mixed in one sentence —
low severity, no in-text contradiction), B8 (CE-composition "67–72%" range
misattributed — requires re-deriving which two source quantities are being
compared), B9 (Table 4 "quoted verbatim" drops "(historical)" qualifiers),
B10 (training-provenance framing more pessimistic than its own cited source
now supports), B11 (spec-z⊂projected nesting asserted without a committed
intersection-count artifact — would need a new computation, out of scope for
a wording fix). NITs C1, C2, C4–C7 (space-gobbling macro, forward-reference
direction, manifest `"paper"` field inconsistency, pre-existing overfull
hbox, stuck-float warnings, Poplawski:2020 year-mismatch flagging) also
deferred as cosmetic. NIT C3 (undefined "C3" jargon label) was incidentally
resolved by the B4 rewrite, which dropped the label entirely.

## v4P.0.9 hygiene

`\paperVersion` v4P.0.8→v4P.0.9; `\paperTimestamp` September 18→September 19,
2026; 4-pass `pdflatex`,
0 undefined refs, one pre-existing 5.88pt overfull hbox (unchanged, below
the 10pt gate); 14→14 pages (unchanged). `pdftoppm -r 110` full render,
pages 1, 5, 6, 8, 9, 10, 11, 12, 13 (every page touched by an edit, plus the
abstract) visually inspected — no overflow, no overlap, no broken
table/figure.

- **PDF:** `pipelines/p4prime_chirality_test/paper/main.pdf` — MD5
  `e31da2ee9cc57fbf0344b8d5c3b9a330`, SHA-256
  `0224d3b8e85c8a26fd8ed8e6a715ff571e3d6483cce4eadfbdf87acafd17a5bf`.
  Mirrored byte-identically (four-way md5 verified: compile ==
  `site/public/papers/` == `public/papers/` == `site/out/papers/`) to
  `paper4prime_chirality_test_v4P.0.9.pdf`.
- **arXiv tarball:** rebuilt and standalone-compile-verified (extract +
  4-pass pdflatex, 0 undefined refs, 14 pages):
  `project-context/SSOT/arxiv_tarballs/paper4prime_chirality_test_arxiv_v4P.0.9.tar.gz`,
  sha256 `015552aa771bd5efb7fcaf2651ffaca501be8862110a647da05f255cd6a9f500`.
- **Artifact links:** all 12 `\artifact{}` paths in `main.tex` confirmed
  committed on `main` (`git ls-files`); HF dataset mirror and both Zenodo
  DOIs (versioned 21461899, concept 21461898) curl 200.
