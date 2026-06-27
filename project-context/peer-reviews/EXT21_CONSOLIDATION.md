# EXT21 External-Review Consolidation Truth-Audit (Round R52)

**Date:** 2026-06-26
**Scope:** Did the external web-tier reviewers (ChatGPT Pro, Grok, Gemini) surface any NEW real defect that the INTERNAL R52 review did NOT already cover?
**Method:** Verdict-first against current source. INT closures already applied to the canonical .tex. Standard calibration applied (June 2026 dating valid; arXiv 25xx/26xx valid; correction notes / companion placeholders / labeled allowances deliberate; extraction-mangled math not a defect; catalog extensiveness not a defect; verdict actionable only if it means substantive rework, not polish).
**EXT21 verdicts:** all ACCEPT or MINOR REVISIONS (no MAJOR/REJECT). P4 Grok absent (upload failed — fine).

---

## Headline result

| Paper | New VERIFIED items warranting a closure edit |
|-------|----------------------------------------------|
| P1A | 0 — clean |
| P1B | 2 (both POLISH-tier wording/accuracy) |
| P2 | 1 (MINOR arithmetic) + 1 optional POLISH |
| P3 | 0 — clean |
| P4 | 0 — clean |
| P5 | 0 — clean |

Net: **3 NEW VERIFIED closure edits** across the whole portfolio (2× P1B POLISH, 1× P2 MINOR), plus 1 optional P2 POLISH label tweak. No new BLOCKER/MAJOR anywhere. No science rework. The thorough INT pass already covered the substance of every EXT MAJOR-tier signal; the residue is three printed-text accuracy defects INT happened not to catch.

---

## P1A

(a) Distinct EXT findings:

| Source(s) | Finding | Classification | If NEW: verdict |
|---|---|---|---|
| ChatGPT MINOR | Abstract too long / nested caveats | ALREADY-COVERED (INT F12 length=OPINION) | — |
| ChatGPT MINOR | Title consistency across metadata | ALREADY-COVERED (INT F2/F12 title) | — |
| ChatGPT MINOR | Fig. 1 ekpyrotic-row labels crowded | NEW | POLISH (D-round visual) |
| ChatGPT MINOR | Sec X.B proof step 5 reword | NEW | OPINION (already "mostly resolves it"; clarity polish) |
| ChatGPT MINOR | Fig. 5 panel title "RG Running of α/M" too definitive | NEW | POLISH (α/M already labeled ansatz in text) |
| ChatGPT MINOR | Figs 4/6 σ tracks invite over-reading | ALREADY-COVERED (INT F12 σ-caveat OPINION; L782–784) | — |
| ChatGPT MINOR | Data-availability load-bearing vs contextual | ALREADY-COVERED (INT F1 OUT-OF-SCOPE) | — |
| Grok MAJOR | Expand Sec X.D explicit leading-order perturbed Holst term | NEW | OPINION (Grok self-tags "presentation, not conceptual gap; result robust") |
| Grok MAJOR | Add companion-paper status/ID sentence | ALREADY-COVERED (INT F1 OUT-OF-SCOPE) | — |
| Grok MINOR | Move omitted-operator list into abstract | ALREADY-COVERED (INT F2; L789–794) | — |
| Grok MINOR | Footnote washout Boltzmann calc deferred | NEW | OPINION (labeled "conditional strengthening") |
| Grok MINOR | Eq.(15) confirm H0/MPl factor | ALREADY-COVERED (INT F3/F4 ansatz-labeled) | — |
| Grok MINOR | Barrier 9 Liouville assumptions footnote | ALREADY-COVERED (INT F7 ledger L2188–2194) | — |
| Grok MINOR | Typographic/extraction artifacts (γ_BI, ε^abcd) | ALREADY-COVERED (calibration: extraction-mangled) | — |
| Grok MINOR | "in preparation" vs "submitted" consistency | ALREADY-COVERED (INT F1/m4 submission-time) | — |
| Gemini | Heavy companion dependence / give arXiv IDs | ALREADY-COVERED (INT F1) | — |
| Gemini | Washout-rate plausibility sentence | NEW | OPINION (labeled conditional) |
| Gemini | MNRAS-readership gloss differential-form identities | NEW | OPINION (audience polish) |
| Gemini typo | p2 "programme mme" duplicate | NEW | STALE (L794 clean; extraction artifact) |
| Gemini typo | p6 fn1 "Eq. (1is not" missing paren | NEW | STALE (L1023 uses \eqref; extraction artifact) |
| Gemini | p13 §IV.D θ-vs-ϕ alternation | ALREADY-COVERED (INT F12; convention fn4 governs) | — |
| Gemini | Units LaTeX-in-prose consistency | NEW | POLISH (cosmetic) |

### NEW VERIFIED items

**P1A: clean — all EXT findings already covered or non-actionable.**

Both Grok MAJORs self-downgrade (Sec X.D = "presentation, not a conceptual gap, result robust"; companion-status = INT F1 OUT-OF-SCOPE). Gemini's two real typos are STALE/extraction artifacts: current source reads "complementary observational programme is hosted" cleanly at L794 (no "mme") and the footnote uses `\eqref{eq:torsion}` at L1023 (renders properly closed). ChatGPT returned ACCEPT; all its MINORs are figure-caption/abstract polish or already-audited OPINION. The recurring cross-vendor theme (companion dependence / arXiv IDs) is INT F1, a submission-timing program decision.

---

## P1B

(a) Distinct EXT findings:

| Source(s) | Finding | Classification | Verdict (if NEW) |
|---|---|---|---|
| ChatGPT m4, Gemini Maj1, Grok | w0wa Table II σ-distances need "diagnostic only" caveat | ALREADY-COVERED (INT MAJOR #1) | — |
| Gemini Maj1 | Summarize two SN-overlap control chains | ALREADY-COVERED (INT TRULY-BLOCKED, new MCMC) | — |
| ChatGPT m3, Gemini min | NaMaster bias carried as floor not correction | ALREADY-COVERED (INT MAJOR #2; "carried forward as observed pipeline bias") | — |
| ChatGPT m1 | Distinguish Ωa<0.01 subset from strict θi≤0.1 sliver | ALREADY-COVERED (separated L2468–2487; INT #5) | — |
| ChatGPT m2 | "across the spectator-consistent posterior" mislabels full-box span | **NEW** | **VERIFIED (POLISH)** |
| ChatGPT m6 | "every quantitative claim" vs 10-row subset | **NEW** | **VERIFIED (POLISH)** |
| ChatGPT m5, Gemini Maj3 | Tighten/front-load ALP-tuning conclusion | ALREADY-COVERED (L2701–2705) — OPINION | — |
| ChatGPT m7, Grok min4 | Finalize DOI / commit SHA | ALREADY-COVERED (submission-gated placeholder) | — |
| ChatGPT m8, Grok | Figure axis labels (ΔNeff/units) | ALREADY-COVERED (INT NIT #16) | — |
| ChatGPT m9, Grok min3 | Move burn-in detail to appendix | OPINION (length) | — |
| ChatGPT m10 | Companion placeholder title consistency | ALREADY-COVERED (deliberate placeholder) | — |
| Grok min1, Gemini Maj2 | Reinforce ECH-scope / re-frame intro | OPINION (scoping already judged exemplary) | — |
| Grok min2 | Notation β vs β̂ vs βinj | ALREADY-COVERED (INT polish sweep) | — |
| Gemini min | Verify values mapped from CORRECTED.json | ALREADY-COVERED (verification ask, not defect) | — |

### NEW VERIFIED items

**1. `arxiv/paper1b_mcmc_companion.tex:2323-2324` — mislabeled span (POLISH)**
The [0.01,0.48]° span is defined two sentences earlier (L2306-2308) as "the union over the full Caγ×(m/H0,θi) box" — the full scan-prior box, which is NOT spectator-safe by the paper's own Ωa<0.01 criterion (only the θi~0.1 corner is, L2315-2316). Calling the full-box union "spectator-consistent posterior" contradicts the paper's own definition.
- Current: `the committed grid scan gives $\beta_{\rm ALP}\in[0.01,0.48]^\circ$ across the spectator-consistent posterior.`
- Proposed: `the committed grid scan gives $\beta_{\rm ALP}\in[0.01,0.48]^\circ$ across the full scan-prior box (the benchmark EOM grid, not the spectator-consistent subset).`

**2. `arxiv/paper1b_mcmc_companion.tex:2851` — "every quantitative claim" overclaim (POLISH)**
Table V (L2867-2876) is a 10-row selection; it omits w0wa posterior distances, Ωa subset fractions (13%/44%), continuous-prior coupling posterior (median Caγ=20.7), θi≤0.1 sliver fraction (0.33%), c15-rerun deltas, LiteBIRD forecast numbers. "Every" is literally false.
- Current: `Table~\ref{tab:claims} classifies every quantitative claim made in this companion by claim type and verification status;`
- Proposed: `Table~\ref{tab:claims} classifies the principal load-bearing quantitative claims made in this companion by claim type and verification status;`

No new BLOCKER/MAJOR. All MAJOR-tier EXT verdicts already covered or non-actionable opinion; the two NEW items are genuine printed-text accuracy defects INT did not catch.

---

## P2

(a) Distinct EXT findings (all three EXT = MINOR REVISIONS, no BLOCKER/MAJOR):

| Source(s) | Finding | Classification | Verdict (if NEW) |
|---|---|---|---|
| ChatGPT M1 | Sec VI.C CDF-tail note (Φ≈0.006, "18% from each tail") mathematically misleading | **NEW** | **VERIFIED (MINOR)** |
| ChatGPT M2 | Add "headline convention" sentence near Table IV | ALREADY-COVERED (INT 3,6) | — |
| ChatGPT M3 | Shot-noise 15–30% vs √11 not derived | ALREADY-COVERED (INT 2) | — |
| ChatGPT M4 | b_φ "Heinrich marginalize" vs UMF-fixed contradiction | **NEW** | **FALSIFIED** — L896 already says Heinrich "adopt UMF universality to fix b_φ per tracer" | 
| ChatGPT M5 | Fig 6 legend "bounce excluded" too broad | **NEW** | VERIFIED but figure-layer → D-round (caption L1025 already scopes to "quasi-dust matter bounce") |
| ChatGPT M6 | Table V "Convention" header undermines time-ordering argument | **NEW** | VERIFIED, POLISH (optional) |
| ChatGPT M7 | Zenodo DOI before publication | ALREADY-COVERED (INT 18, submission-time) | — |
| Grok m1 | Front-load "recast not independent forecast" | ALREADY-COVERED (INT 3; L578) | — |
| Grok m2 | Strengthen additive-quadrature caveat | ALREADY-COVERED (INT 3; L578) | — |
| Grok m3 | Label SDB σ=1.53 as subordinate cross-check | ALREADY-COVERED (INT 7) | — |
| Grok m4 | Notation f_NL^local; Fig 2 caption; cross-refs | ALREADY-COVERED (INT 6) | — |
| Grok m5 | Data/code availability checklist | ALREADY-COVERED (INT 18) | — |
| Gemini 1 | Eq 7 δC/C add b2/trispectrum cross-term | ALREADY-COVERED (INT 12; L578 heuristic) | — |
| Gemini 2 | MegaMapper high-z GR projections more severe | **NEW** | VERIFIED but non-actionable (body already notes caveat; "emphasize more" = polish) |
| Gemini 3 | "five-coefficient r=0.867–0.888" vs 10k-sample scan reconcile | ALREADY-COVERED (INT 6) | — |
| Gemini 3b | k_i index labeling Eq 1 / Sec II | ALREADY-COVERED (INT 13) | — |

### NEW VERIFIED items

**1. `research/focused_paper_source_integration/02_full_draft.tex:803` — CDF-tail explanatory note arithmetic error (MINOR)**
Verified by direct computation: for the delta-prior narrow [-5,+5] competitor at f_obs=-35/8, σ_eff=0.7, the competitor-prior denominator is Φ((5+35/8)/0.7) − Φ((-5+35/8)/0.7) = Φ(13.4) − Φ(-0.893) = 1 − 0.186 = 0.814, and 5.69/0.814 ≈ 6.99 ≈ 7.0. The source's "Φ ≈ 0.006" and "≈18% correction from each tail" are both wrong: the relevant lower tail is 0.186 (≈18.6%), the upper tail is negligible (~10⁻⁴⁰), and only the lower tail contributes. Distinct from the EXT16 direction fix already applied; INT R52 did not touch it.
- Current (parenthetical (ii) clause): `($\Phi(-35/8\text{ relative endpoints}) \approx 0.006$, contributing $\approx 18\%$ correction from each tail; for the delta-prior narrow case these tail terms \emph{raise} $B$ from the large-$W$ approximation 5.69 to the exact 7.0 by reducing the competitor-prior denominator, while for the Gaussian-bounce case the reduction below 5.69 to 4.01 is dominated by the prior-width broadening)`
- Proposed: `(the competitor-prior denominator is $\Phi((5+35/8)/0.7)-\Phi((-5+35/8)/0.7)=\Phi(13.4)-\Phi(-0.893)\approx 1-0.186=0.814$, so the finite lower tail $\approx 0.186$ — the upper tail is negligible — reduces the denominator by $\approx 18\%$; for the delta-prior narrow case this \emph{raises} $B$ from the large-$W$ approximation 5.69 to the exact $5.69/0.814\approx 7.0$, while for the Gaussian-bounce case the reduction below 5.69 to 4.01 is dominated by the prior-width broadening)`
- Tier: MINOR. The tabled value B≈7.0 is itself correct (not load-bearing on any result), but this is a real arithmetic misstatement in printed text, not extraction mangling.

**2. (optional) `02_full_draft.tex:1159` — Table V column header (POLISH)**
Current header `Convention` → `Normalization / time-ordering branch` (or `Case`). The Li row is a single-time-ordering stress test, not an alternative convention. Genuine but cosmetic — section title (L1150), caption (L1156), and prose already disambiguate. Bundle if convenient, else D-round.

**Note:** ChatGPT M4 (b_φ "marginalize") is FALSIFIED against current source (L896 already states the fix ChatGPT requested). Fig 6 legend (M5) is a figure-layer/D-round item already mitigated by its caption.

---

## P3

(a) Distinct EXT findings (ChatGPT ACCEPT; Grok + Gemini MINOR REVISIONS; all explicitly no-blocker/no-reanalysis):

| Source(s) | Finding | Classification | If NEW: verdict |
|---|---|---|---|
| All three | DESI 195,829 / 73× side-by-side with science-target recount | ALREADY-COVERED (abstract L565; INT DESI) | — |
| All three | eROSITA membership-only non-reproducible mirrored in release sentences | ALREADY-COVERED (L565, §III.E, L1160, L1171; INT B/Q) | — |
| ChatGPT, Grok | "catalog-grade" 269,317 folds in injection-FAIL eROSITA/Gaia | ALREADY-COVERED (L565+L1160; INT B) | — |
| ChatGPT | Cramér's V renders √ next to un-squared fraction | ALREADY-COVERED (INT D FALSIFIED; L950 shows √; OCR-broken glyph) | — |
| ChatGPT, Grok | f_NL 8.98 vs 16.85 flag non-comparable | ALREADY-COVERED (L569 envelope; INT G) | — |
| ChatGPT | "No full-catalog novelty fraction claimed" in Conclusions | ALREADY-COVERED (L565; INT S) | — |
| Grok, Gemini | Gaia preprocessing lineage-inferred / list 20 features | ALREADY-COVERED (L625, L882, L1171; INT Q) | — |
| Grok | 269,317 vs 269,117 parenthetical | ALREADY-COVERED (L565 has the parenthetical) | — |
| ChatGPT | Recast §VI.B SDSS as historical baseline | ALREADY-COVERED (L640; native supersedes) | OPINION (polish) |
| Gemini | NANOGrav Savage-Dickey prior-sensitivity | ALREADY-COVERED (L569 + App-E) | — |
| Gemini | NEOWISE 100% = mask-geometry QA | ALREADY-COVERED (L567 + §III.H; INT B) | — |
| ChatGPT, Grok | Add catalog-tier-summary table / footnotes to appendix | NEW | OPINION (additive enhancement) |
| ChatGPT, Grok | Fig 8 / Fig 3 labels | ALREADY-COVERED as D-round (INT S) | — |
| Grok | "Path-C unique" vs "native-retrained" terminology | NEW | OPINION (polish) |
| Grok | Confirm 25xx/26xx arXiv IDs | ALREADY-COVERED (calibration: valid) | — |

### NEW VERIFIED items

**P3: clean — all EXT findings already covered or non-actionable.**

The load-bearing MAJOR-grade asks (DESI scope side-by-side, eROSITA membership-only framing, list the 20 Gaia features) are already satisfied verbatim in the current abstract (L565–567), §III.E, Conclusions (L1160), Data-availability (L1171), and release manifest. Cramér's V "missing √" is FALSIFIED (L950 applies the √; reviewer read an extraction-mangled glyph). The exact Gaia production script was lost, so a fuller feature listing is not achievable and the lineage-inferred disclosure is complete. Remaining items are additive presentation enhancements or D-round visual polish.

---

## P4

(a) Distinct EXT findings (ChatGPT ACCEPT; Gemini MINOR REVISIONS; Grok absent):

| # | Source(s) | Finding | Classification | If NEW: verdict |
|---|-----------|---------|----------------|------------------|
| C1 | ChatGPT MINOR | Fig 7 raw Catalog-A panel sparser than equivariant panel | NEW | OPINION/POLISH (D-round; reviewer: "does not affect the null result") |
| C2 | ChatGPT MINOR | Data Availability archival DOI future-tense | ALREADY-COVERED (INT B1 OUT-OF-SCOPE; L1003–1015) | — |
| C3 | ChatGPT MINOR | Significance terminology dense; add "only HC dipole + WLS primary" | ALREADY-COVERED (INT o3-M3/M4; L348/426/Table III caption) | — |
| C4 | ChatGPT MINOR | p_eq>0.6 threshold provenance not clean pre-registration | NEW | OPINION/POLISH (L605 names committed artifact + sweep) |
| C5 | ChatGPT MINOR | Shamir "excluded by a factor" needs matched-analysis caveat | ALREADY-COVERED (L365, 694, 710, 792 "under the present pipeline") | — |
| C6 | ChatGPT MINOR | "All 8 tests pass" soften for T1/T5 scope | ALREADY-COVERED (L503, 858, 861) | — |
| C7 | ChatGPT MINOR | App E edge-on: add b/a<0.3 sample size | ALREADY-COVERED (INT V8/o3-M7; L749/991) | — |
| C8 | ChatGPT MINOR | Long artifact paths interrupt text | ALREADY-COVERED (INT V4 lab convention) | — |
| G1 | Gemini MINOR | T5 circular-coord limitation; circular-linear metrics future | ALREADY-COVERED (L858 flags + low-ℓ Yℓm supplement) | — |
| G2 | Gemini MINOR | Edge-on sensitivity; future aspect-ratio cut | ALREADY-COVERED (INT V8; L749/991) | — |
| G3 | Gemini MINOR | Add Platt/temperature calibration advisory | ALREADY-COVERED (L1015 verbatim) | — |
| G4 | Gemini MINOR | "…would be" fragment + draft markers near pg 1→2 | NEW | FALSIFIED (extraction artifact; L348 sentence complete) |

### NEW VERIFIED items

**P4: clean — all EXT findings already covered or non-actionable.**

Both EXT reviewers recommend at most minor clarification; the INT R52 truth-audit (8 VERIFIED MINORs V1–V8 + nits closed) is strictly more thorough. C5 (the only EXT item with rework potential) is FALSIFIED-as-defect: the matched-footprint Ganalyzer caveat already appears at L365/694/710/792 with "under the present pipeline"; softening "excluded by a factor" → "inconsistent in amplitude" is pure wording (abstract L348/365 already uses "inconsistent in amplitude"). C1 (Fig 7 panel sparsity) is the only genuinely-new observation, a D-round figure item the reviewer himself flags as not affecting the result. G4 is a PDF text-extraction artifact. No .tex edits recommended on EXT grounds; P4 holds at ACCEPT.

---

## P5

(a) Distinct EXT findings (all three EXT = ACCEPT or MINOR REVISIONS, zero BLOCKER/MAJOR):

| Source(s) | Finding | Classification | Verdict |
|---|---|---|---|
| ChatGPT M1; Gemini | Abstract too dense | ALREADY-COVERED (INT length=OPINION) | — |
| ChatGPT M2; Grok #1 | Boxed primary=DESIVAST/secondary=T-Web statement | ALREADY-COVERED (INT V1 + §VB) | — |
| ChatGPT M3 | Table III caption n=428 "not primary" pointer | ALREADY-COVERED (L1298) | — |
| ChatGPT M4 | Table VIII k=20 vs exact-membership labeling | ALREADY-COVERED (INT V7/C7) | — |
| ChatGPT M5 | "0 maximal voids/pixel" plain-language gloss | NEW | OPINION (polish) |
| ChatGPT M6 | §IXA selection-corrected rebuild too long | ALREADY-COVERED (INT length=OPINION) | — |
| ChatGPT M7 | ASTRA "cross-validation"→"EDR-overlap diagnostic" | NEW | OPINION (polish) |
| ChatGPT M8 | §XI add monopole-subtracted residual column | ALREADY-COVERED (INT V4) | — |
| ChatGPT M9 | Fig 8 crowded | ALREADY-COVERED (INT S1 STALE — fixed v0.1.83) | — |
| ChatGPT M10; Grok #3; Gemini | Insert archival DOI | ALREADY-COVERED (INT D1/C10) | — |
| ChatGPT M11 | Artifact paths interrupt narrative | NEW | OPINION (polish) |
| ChatGPT M12; Gemini #4 | Appendix A rename "non-load-bearing toy EFT" | NEW | OPINION (already caveated L3514-3534) |
| Grok #2 | Quote max \|z_Δ\| across RSD MC | ALREADY-COVERED (max 1.93 stated; Grok concedes) | — |
| Grok #4 | Unify σ symbol / canonical caveat | ALREADY-COVERED (INT V4/C4) | — |
| Grok #5 | Optional 95% CI on Δf_CW | NEW | OPINION (optional) |
| Gemini #1 | §II note Paper IV stability ripple | ALREADY-COVERED (INT V1/C1) | — |
| Gemini #2 | Expand DR2/Rubin selection-effect untangling | NEW | OUT-OF-SCOPE (future-work) |
| Gemini #3 | RSD caveat in Abstract AND Conclusions | ALREADY-COVERED (abstract L618-624; conclusions L3453) | — |
| Gemini #5 | §IVA step 5 ceiling function | ALREADY-COVERED (L884 already `\lceil R_s/{\rm cell}\rceil + 1 = 2`) | — |

### NEW VERIFIED items

**P5: clean — all EXT findings already covered or non-actionable.**

Gemini #5 (ceiling notation) and #3 (RSD in abstract+conclusions) are already satisfied verbatim (L884, L618-624, L3453) — those reviewers read the older PDF. Gemini #1 / Grok #1 / ChatGPT M2-M3 (Paper IV dependence, primary/secondary emphasis) are the same signal INT closed as V1/C1. M4/M9/M10, Grok #2-#4 map 1:1 onto INT items already closed or queued. Appendix A rename is a title tweak on an already-caveated labeled allowance (L3514-3534). All length/density/wording/future-work items are OPINION/OUT-OF-SCOPE under calibration. No closure edit warranted.

---

## Closure plan for R52

Apply 3 NEW VERIFIED edits this round (all printed-text accuracy, no science impact):

1. **P1B** L2323-2324 — span relabel "spectator-consistent posterior" → "full scan-prior box (…not the spectator-consistent subset)" [POLISH]
2. **P1B** L2851 — "every quantitative claim" → "the principal load-bearing quantitative claims" [POLISH]
3. **P2** L803 — rewrite CDF-tail explanatory parenthetical with correct denominator arithmetic (0.814, lower tail 0.186) [MINOR]

Optional same-bundle: **P2** L1159 Table V header "Convention" → "Normalization / time-ordering branch" [POLISH].

Route to D-round (not this closure wave): P1A Fig 1/Fig 5 caption polish; P2 Fig 6 legend; P3 catalog-tier table; P4 Fig 7 panel; P5 Fig/density polish.

Per CLAUDE.md standing directive, add a `reviewTimeline.ts` entry for EXT21/R52 in the same commit bundle as these edits.
