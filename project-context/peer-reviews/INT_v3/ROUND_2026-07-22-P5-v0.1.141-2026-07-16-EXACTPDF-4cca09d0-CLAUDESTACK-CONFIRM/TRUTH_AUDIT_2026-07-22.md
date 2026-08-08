# TRUTH AUDIT — P5 v0.1.141-2026-07-16 CONFIRM board (2026-07-22)

**Round:** ROUND_2026-07-22-P5-v0.1.141-2026-07-16-EXACTPDF-4cca09d0-CLAUDESTACK-CONFIRM
**Paper:** P5 — *A Catalog-Native DESIVAST Test of Classifier-Labelled Spiral Chirality in DESI DR1*
**PDF sha256 (all three legs agree):** `4cca09d0aa963ae18b908bc17f57e9b1bf8f91e4ec8555f4c18d2e413a7580ac`
**Tex audited:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` (commit 44b666cb / 4cca09d0 PDF)
**Reviewer verdicts:** Grok ACCEPT · Gemini MINOR-REVISIONS · Claude-INT MINOR-REVISIONS
**Auditor:** Opus truth-audit agent, source-cited verdict per finding.

Verdict enum: ALREADY-TRACKED-GATE / DISCLOSED-RE-FLAG / SCOPE-VENUE-OPINION / FALSIFIED / GENUINELY-NEW-REAL (in doubt → GENUINELY-NEW-REAL).

---

## Per-finding verdict table

| # | Source leg | Finding (severity) | Verdict | Source-cited evidence |
|---|-----------|--------------------|---------|-----------------------|
| 1 | Claude-INT | Verification ledger (~15 PASSED checks: headline contrast flow, sample flow, Eq.4 8-term budget, multiplicity bound N=23 pglobal=0.82, forward-leakage 77–88%, σ-from-half, contingency tables, ASTRA overlap, DESIVAST variants, monopole self-corroboration, version stamps) | *confirmation, not a defect* | Independently spot-verified: sample flow 604,032+90,610=694,642 and 56741/113829−15873/31937=+0.00147 reconcile; [A45]–[A48] artifact map lines 5422–5425 present. No defect. |
| 2 | Claude-INT MINOR-1a | Orphan reference **[4] Paper II** (`golden_fnl_2026`, SPHEREx f_NL forecast) never cited in body | **GENUINELY-NEW-REAL** | `grep 'golden_fnl_2026'` → only `\bibitem` at line 5452; **0** non-comment `\cite` occurrences. Genuine uncited bibitem = AJ/ApJ copyedit defect. Not in DISPOSITIONS/P5.md; no back-patch macro (`\paperIVarxiv` exists for Paper IV, none for Paper II). Real, low-severity. |
| 3 | Claude-INT MINOR-1b | Orphan reference **[8] Hamaus** (`Hamaus2014`) never cited in body | **FALSIFIED** | `Hamaus2014` **is** cited in active prose at line 2929 (`universal void velocity profile~\cite{Hamaus2014}`), the RSD Zel'dovich reconstruction paragraph; `sed -n 2929p \| grep '^%'` = 0 (non-comment). Closed & integrated per DISPOSITIONS/P5.md line 114 (v0.1.122 CLOSURE). Claude's "[8]=0 occurrences" count is factually wrong. |
| 4 | Claude-INT MINOR-2 | [A45]/[A46] stamped `v0_1_140` inside a v0.1.141 paper while [A47]/[A48] are `v0_1_141` | **SCOPE-VENUE-OPINION** | On-disk files genuinely named `global_multiplicity_bound_v0_1_140.py/.json` (ls of analysis/). `\href` targets (lines 5422–5423) point to the real filenames; stamp is **accurate provenance** (multiplicity bound created in v0.1.140 closure, unchanged in v0.1.141 which only added forward-leakage). Documented in version-history comment block lines 65–80. Re-stamping would falsify provenance and break the live href. Cosmetic; not a defect. Optional one-line note is a preference. |
| 5 | Claude-INT MINOR-3 | Monopole significance "≈9σ" (§I / Table I) vs "∼9.5σ" (§VIII G) vs "−9.47σ" (App A) | **GENUINELY-NEW-REAL** | Verified: line 922 `$\approx\!9\sigma$` (§I), line 1055 `${\approx}9\sigma$` (Table I) vs line 3783 `$\sim\!9.5\sigma$` (§VIII G) and line 5097 `$-9.47\sigma$` (App A). Same quantity, two roundings; 9.47 rounds nearer 9.5. Real in-text presentation inconsistency (harmonize). NOTE: not in the abstract (ends line 906) — Claude's "abstract" attribution is imprecise; the drift is §I + Table I. |
| 6 | Claude-INT (self-labelled tracked gate) | Focal contrast depends on unpublished Paper IV `class_eq` labels | **ALREADY-TRACKED-GATE** | Disclosed §II, §XIII, App A, App C: labels/weights public CC-BY-4.0, headline Δf_CW monopole-invariant/refereeable from public DESI/DESIVAST/GZ1, pre-submission re-verification gate stated. Claude records no verdict change. |
| 7 | Grok MINOR | Title/first para could restate "catalog-specific, not physical-handedness" scope in one more sentence | **DISCLOSED-RE-FLAG** | Scope already explicit — abstract + §I lines 934–937 ("not a real-space or physical handedness constraint and does not discriminate cosmological models"). Grok itself calls it "already explicit." Additive style suggestion. |
| 8 | Grok MINOR | §V B: add footnote with exact date of the post-review hierarchy change | **DISCLOSED-RE-FLAG** | Post-hoc hierarchy change already disclosed in abstract + §V B (Claude ledger line 55–59; DISPOSITIONS/P5.md L778 estimand-plan entry). Re-flag of disclosed content. |
| 9 | Grok MINOR | RSD sensitivity "fixed-geometry only"; move statement to abstract | **DISCLOSED-RE-FLAG** | Already noted; moreover a full first-order Zel'dovich reconstruction WAS performed (v0.1.122 closure, DISPOSITIONS/P5.md line 114; §VIII, line 2929). Placement preference on already-disclosed content. |
| 10 | Gemini **MAJOR** | Unpublished Paper IV dependency ⇒ "should not be accepted until Paper IV is public" | **ALREADY-TRACKED-GATE** | Same gate as #6. Disclosed §II/§XIII/App A/App C; headline algebraically monopole-invariant and refereeable from public data; pre-submission gate binds re-verification against published Paper IV. Not a genuinely-new defect; the venue-timing condition is the known back-patch gate, not an internal-consistency or scope-honesty failure. |
| 11 | Gemini MINOR | Inline artifact citations [A41-A42] disrupt narrative flow; move to footnotes | **SCOPE-VENUE-OPINION** | Pure typographic/placement preference; the artifact-pointer system is intentional open-science provenance (Gemini calls it "outstanding"). No defect. |
| 12 | Gemini MINOR | Figures 3, 5, 9 axis/tick/annotation fonts too small for AJ typeset | **SCOPE-VENUE-OPINION** | Subjective legibility judgment from a downscaled raster render; a D-round (visual/typeset) item, not an R-round science/consistency/scope defect. Cannot be verified as a defect from source; scoped to the design round if pursued. Not confirmation-board-blocking. |
| 13 | Gemini MINOR | §VI.D/E dense; add a high-level summary sentence (2.1σ filament sign-flip = imaging/selection systematics) | **DISCLOSED-RE-FLAG** | The conclusion is already stated — T-Web/filament sign-flip repeatedly demoted to survey-shell/selection-systematics (Claude scope-honesty note lines 162–168; §VI.D/E + §XIII). Readability preference on already-present conclusion. |

---

## Verdict-class counts

- ALREADY-TRACKED-GATE: **2** (#6, #10 — Paper IV public-release dependency)
- DISCLOSED-RE-FLAG: **4** (#7, #8, #9, #13)
- SCOPE-VENUE-OPINION: **3** (#4 stamp-provenance, #11 artifact placement, #12 figure fonts)
- FALSIFIED: **1** (#3 — [8] Hamaus is cited, line 2929)
- GENUINELY-NEW-REAL: **2** (#2 orphan Paper II [4]; #5 ≈9σ harmonization)
- (Ledger #1: ~15 passed confirmation checks, no defect)

**No BLOCKER, no MAJOR survives truth-audit.** Gemini's lone MAJOR is the disclosed Paper IV tracked gate. Two genuinely-new REAL items, both presentation/copyedit tier — neither touches a science number, estimand, interval, or scope claim.

---

## GENUINELY-NEW-REAL FIX LIST (exact tex edits)

All edits in `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`. Both are presentation-tier; zero science-value change. After applying, recompile (0 undef-refs) + `/latex-audit` + directive-G PDF hygiene (version bump, mirror, Convex md5) per the standing round protocol.

### FIX-1 — Cite orphan Paper II [4] (`golden_fnl_2026`) in §I (or remove the bibitem)

Recommended: cite it at the natural bounce-vs-inflation scope sentence (§I, line ~933–936).

- **old_string:**
  `redshift-space estimand. Accordingly, the analysis measures dataset- and`
- **new_string:**
  `redshift-space estimand; the companion SPHEREx $f_{\rm NL}$ forecast (Paper~II)~\cite{golden_fnl_2026} targets a distinct primordial-non-Gaussianity discriminant, not this catalog-labelled estimand. Accordingly, the analysis measures dataset- and`

  (Alternative, if the author prefers removal over citation: delete the `\bibitem{golden_fnl_2026}` block at lines 5452–5455. Citation is preferred — it strengthens the program cross-reference and satisfies the AJ uncited-reference copyedit rule.)

### FIX-2 — Harmonize monopole counting significance to ≈9.5σ (§I + Table I → match §VIII G / App A)

Two edits; leave §VIII G (`$\sim\!9.5\sigma$`, line 3783) and App A (exact `$-9.47\sigma$`, line 5097) as the authoritative values.

- **Edit 2a (line 922, §I):**
  - old_string: `significant in pure counting terms ($\approx\!9\sigma$) and is treated`
  - new_string: `significant in pure counting terms ($\approx\!9.5\sigma$) and is treated`

- **Edit 2b (line 1055, Table I):**
  - old_string: `\quad counting significance & ${\approx}9\sigma$ \\`
  - new_string: `\quad counting significance & ${\approx}9.5\sigma$ \\`

---

## Auditor note

The board is CONFIRM-tier: Grok ACCEPT, Gemini + Claude MINOR-REVISIONS with only presentation/copyedit and one disclosed-gate item. After FIX-1 + FIX-2 land, the two genuinely-new items close; the remaining reviewer findings are all tracked-gate, disclosed re-flags, or venue/design-round opinions. Consistent with directive-K/H convergence (0 genuinely-new REAL science findings) once the two copyedits are applied.
