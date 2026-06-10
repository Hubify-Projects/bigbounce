# P2 R23conf — TRUTH AUDIT (remaining findings)

**Date**: 2026-06-09 · **Auditor**: closure agent (follow-on to session lead)
**Source audited**: `research/focused_paper_source_integration/02_full_draft.tex` (working tree, post-lead-closures)
**Scope**: every SYNTHESIS + META finding NOT in the lead's closed list (lead closed: OpenAI E1/E2/E4/E5/E6/M2/M4/M6/M7/M8/M9 + Claude E1/M1-table/m1/m2/m3/m4/N2-braces).
**Verdict counts (73 rows)**: VERIFIED 16 · PARTIAL 12 (9 closed with edits, 3 no-edit) · STALE 24 · FALSIFIED 7 · OPINION 12 · HOUSTON-DECISION 2.
**All VERIFIED + PARTIAL-closable items closed with exact-string edits. No recompile, no commit. New artifact: `scripts/c9j_bf_template_rescale.py` + `outputs/c9j_bf_template_rescale.json` (validated: reproduces the printed 17.10/7.00/9.80/4.01 BF grid exactly before rescaling).**

Auto-falsification rules applied: future-date findings falsified (it IS June 2026); Perplexity "citation doesn't exist" claims checked against `focused_paper_refs.bib` + live URL (15/15 prior false record holds). Correction-note complaints = deliberate transparent disclosure (Houston decision) — notes retained.

## OpenAI_methodology (31 remaining)

| ID | Claim | Verdict | Evidence / action (file = 02_full_draft.tex) |
|---|---|---|---|
| E3 | Correction-note/version-history prose in body (§IX.D, tab:gr caption) | **HOUSTON-DECISION** | Deliberate transparent disclosure of the withdrawn 9.9σ FW-1 artifact. NOT removed. |
| E7 | "0.500±0.001 reported in Sec II.C and Table I" but Table I has no ratios | **STALE** | Lead's M9 closure reframed the half-ratio as the in-in operator identity (App. A.1) + c9i artifact; abstract no longer claims per-configuration ratios in Table I (grep "0.500" → only a version comment survives). |
| E8 | ">4σ null" conflicts with paper's own 3–5σ post-budget envelope | **VERIFIED → CLOSED** | Null-exclusion arithmetic is symmetric to detection. Abstract L226: ">4σ" → "same ~3–5σ post-systematic-budget level as a detection (5.1–5.5σ pre-budget)". Body L600: both ">4σ" occurrences replaced with the 3–5σ post-budget envelope + symmetry rationale. No new numbers — paper's own envelope. |
| E9 | Table IV 5.25σ vs 2.63σ "contradicts convention independence" | **PARTIAL → CLOSED** | Lead's E5 closure proved the narrow invariance; residual mislabeling fixed at L714: the two rows differ by physical time-ordering content (−2 Im doubling), NOT a c-rescaling — which is why significances differ while c-invariance holds. |
| M1 | 2D KSW CMB estimator used for 3D LSS injection test | **PARTIAL → CLOSED** | Already scoped as CMB-weighted consistency check (lead E4). Strengthened L286: "two-dimensional flat-sky CMB-style estimator --- not the three-dimensional galaxy-bispectrum estimator a SPHEREx analysis would employ". |
| M3 | 10–20% anomaly-tracer improvement lacks forecast | **VERIFIED → CLOSED** | Text already had the shot-noise upper-bound caveat (§IV); added explicit cross-pointer at the claim site L372: "the quoted gain is an upper bound pending the shot-noise-corrected Fisher analysis described in the shot-noise caveat below". |
| M5 | MC ensembles: no convergence/uncertainty on BF | **PARTIAL → CLOSED** | Closed-form is primary (lead's Table III rebuild). Added at L414: closed-form values are deterministic; c9g JSON reports realization-marginalized mean/median/geo-mean over 2×10⁵ draws (e.g. closed-form 7.0 vs MC median 6.6 at σ_eff=0.7, from `outputs/c9g_bf_table_recompute.json`); spreads come from prior/scenario variation, not MC noise. |
| M10 | Figure axes/units/definitions | **PARTIAL → CLOSED** | All 6 figures visually inspected. fig1/fig2/fig3/fig5/bphi: axes + units present (kmin in h/Mpc, σ in σ-units, fNL dimensionless). Caption-level gaps fixed: fig1 caption L291 adds "(dimensionless, Eq.(2))"; fig4 caption L596 now defines all four shaded regions incl. the colloquial legend label "kills live lane". No figures regenerated. |
| M11 | P used for degree-9 polynomial AND power spectrum | **VERIFIED → CLOSED** | L262: three-argument P = polynomial only; power spectra always carry field subscript + single argument (P_ζ(k)/P_Φ(k)). Abstract template → B_ζ^local with P_ζ(k_i) (L226). |
| M12 | "radius 50 ≈ 7×‖c_ref‖" false + garbled | **STALE** | Current L272: "approximately 0.7× ... (‖c_ref‖ ≈ 73)" — 50/73 = 0.68 ✓; text reads cleanly. |
| M13 | Photo-z 0.70→0.74 claim lacks derivation/citation | **PARTIAL → CLOSED** | Pullen & Hirata + Giannantonio citations present; no committed script found → provenance softened L538: "A simplified Fisher degradation estimate indicates". |
| M14 | Eq.(2) grouping/dimensions unclear | **VERIFIED → CLOSED** | Added after Eq.(2) (L266): Σᵢkᵢ³ defined; degree bookkeeping 9−6−3=0 shown; explicit "no cancellation of P occurs between Eqs.(1) and (2)" (also inoculates META-E1). |
| M15 | "four-vertex evaluation discussed in Sec II.C" — wrong cross-ref | **FALSIFIED** | §II.C (sec:assumptions) DOES contain it: "Determining the precise coefficient requires evaluating all four cubic-action integrals simultaneously with numerically computed mode functions..." (L316). Cross-ref correct. |
| m1 | Garbled "0.Theradius..." text | **STALE** | Same locus as M12/Claude E1 (lead-closed); L272 clean. |
| m2 | Internal file names in prose | **VERIFIED → CLOSED** | Prose mentions of c9h JSON (L282) and phase3 JSON (L356) replaced with pointers; all named artifacts now listed in Data and Code Availability (L628). Footnote/caption occurrences untouched per hard rule. |
| m3 | Missing kmin, kmax, cosmology | **VERIFIED → CLOSED** | Verified in `null_space_analysis.py`: overlap computed in dimensionless ratio coordinates (23,098 = exact count of the masked grid) — scale-free, no physical k-range or cosmology enters. Sentence added L274; cosmology enters only the ℓ-space CAMB validation (already specified). |
| m4 | Frame nomenclature in conclusion | **STALE** | Conclusion fully restructured (v1.7.42 GEM-m2): gauge-frame = observable, CFC = separate theoretical point. |
| m5 | Clarify what P(k) is in abstract template | **VERIFIED → CLOSED** | Abstract → P_ζ (curvature, matching App. A mapping). L226. |
| m6 | Tone ("headline", "optimistic") | **OPINION** | Terms are defined where used; PRD copyedit territory. |
| m7 | Mission timeline language | **OPINION** | Dates factual; deliberate context. |
| m8 | Birefringence ¶ off-scope | **OPINION** | Deliberately retained with explicit "we do not perform EB cross-power analysis" scoping (v1.7.42 deferral stands). |
| m9 | Define weighting schemes | **PARTIAL → CLOSED** | L351: explicit kernels added for the three analytic schemes (w=1, w∝k², w∝1/k²) + w's role in r defined; SPHEREx/MegaMapper-like labeled as survey-noise variants (no committed kernel formula located — not fabricated). |
| m10 | Define all ± error bars globally | **PARTIAL (no edit)** | Key ± already defined contextually (r_cos sample SD, c9h percentiles, weighting-range spread at Eq. r_noise). A blanket definition would be false for the heterogeneous cases — declined to fabricate uniformity. |
| m11 | 0.500±0.001 vs "exact 0.5000" precision clash | **STALE** | Both phrasings removed by lead's M9 reframe (grep confirms). |
| m12 | Eq. (A2) typography/vacuum labels | **STALE** | App. A.1 uses standard commutator form, Hermiticity stated, vacuum kets explicit. |
| m13 | §IX.D mixed σ provenance | **STALE** | "Two distinct Fisher analyses... we distinguish them explicitly" block with (i)/(ii) labels present (L604). Correction note retained = Houston decision. |
| n1–n3, n5 | ~ overuse; hyphenation; length; figure resolution | **OPINION** | Style/structural; length is Houston's call; no figure regeneration in scope. |
| n4 | scipy.stats.norm mentions | **OPINION** | Retained as provenance audit-trail (repo standard). |

## META_REVIEW (10)

| ID | Claim | Verdict | Evidence / action |
|---|---|---|---|
| META-E1 | Eqs.(1)–(2) make P cancel out of B_NL — self-cancelling | **FALSIFIED** | Source Eq.(2) is B_NL = (10/3)·A_T/Σkᵢ³ — NOT (10/3)·P/(A_T Σkᵢ³) as the reviewer rendered it. B_NL ∝ P via A_T; matches `null_space_analysis.py` prefactor 10P/(256k₁²k₂²k₃²Σk³) exactly. Reviewer misread the PDF fraction. Prophylactic "no cancellation" sentence added (L266). |
| META-E2 | BFs use σ=0.7, ignoring Eq.(5) σ/r rescaling | **VERIFIED → CLOSED** | Real bookkeeping gap. New ¶ "Template-mismatch bookkeeping" (L479): σ_eff=0.7/0.84≈0.83 grid 17.1→14.4, 9.8→9.2, 7.0→6.2, 4.0→4.0 (envelope 10–17 → 9–14); measured-space alternative also given (7.0→5.9 narrow corner). All numbers from new committed artifact `c9j_bf_template_rescale.py` (validated against printed grid). No qualitative change. |
| META-M1 | Null-space measure ad hoc, basis-dependent ±0.13 | **PARTIAL → CLOSED** | Demotion strengthened L272: measure non-invariant under monomial reparametrization/null-space rotation; ±0.13 indicative-not-calibrated; basis-independent robust statement = r_cos stability. |
| META-M2 | B_NL symbol overloaded (squeezed param vs shape amplitude) | **PARTIAL → CLOSED** | Light-touch: Eq.(2) lead-in now "configuration-dependent nonlinearity amplitude, whose squeezed limit is the local nonlinearity parameter" (L262). Full symbol split (S_bounce/f_bounce) = invasive refactor, not required for correctness. |
| META-M3 | "Singular-value ratio bounded below by kinematic separation" unfounded | **VERIFIED → CLOSED** | Claim removed L270; replaced with empirical statement (σ₃/σ₁≈0.3 property of the benchmark rows; explicit "no theoretical lower bound" disclaimer). |
| META-M4 | P(BF>3) probability space undefined | **STALE** | tab:gr caption (lead's Table-III rebuild) defines it fully: fraction of 2×10⁵ draws f̂~N(−35/8,σ_eff) exceeding BF=3, script c9g cited. |
| META-m1 | Weighting kernels need explicit definitions | **PARTIAL → CLOSED** | Same closure as OpenAI m9 (L351). |
| META-m2 | z≈0.5–2 vs z=0.1–1.5 inconsistent | **VERIFIED → CLOSED** | Verified in `scripts/c8_fnl_running_fisher.py` (first six bins of SPHEREx public-products 11-bin structure). Justification added L604: different tracer selections by construction (SDB public-product bins vs Heinrich ELG sample). |
| META-m3 | Torsion caveat unquantified | **STALE** | Text already does the reviewer's option (b): prediction explicitly restricted to scalar-only class; fermionic models explicitly excluded pending a bound (§I + assumption (f)). |
| META-N1 | SVD monomial normalization undefined | **VERIFIED → CLOSED** | Defined from `null_space_analysis.py` L270: rows = B_NL prefactor × monomials at unit-scale triangles (1,1,1),(2,1,1),(10⁻⁴,1,1), no per-column rescaling. |

## Grok_brutal (9)

| ID | Verdict | Evidence / action |
|---|---|---|
| E1 (abstract BF prior qualifier) | **STALE** | Abstract states both priors inline + four-corner pointer. |
| E2 (convention-dependent abstract σ) | **STALE** | Abstract carries the full convention-halving caveat sentence. |
| E3 (assumptions d/e propagation) | **PARTIAL (no edit)** | δf_NL~10⁻³ scaling estimate labeled as such; cubic-transfer uncertainty explicitly folded into σ_theory=1.0 prior motivation (§VI). Full third-order bounce computation = genuine new research, tracked in SSOT queue, not a textual gap. |
| M1 (Fig 2 error-bar definition) | **STALE** | Caption defines optimistic/conservative endpoints (R22prov2 V7). |
| M2 (r scatter not folded into significance) | **STALE** | Lead's M2/c9h closure: 16–84% propagation 4.4–6.2σ in §II.A. |
| M3 (length vs novelty) | **OPINION** | Editorial judgment; Houston's call. |
| N1 (June 2026 date "in the future") | **FALSIFIED** | It IS June 2026. Auto-falsified per protocol. |
| N2 (red boxes around cross-refs) | **VERIFIED → CLOSED** | Bare `\usepackage{hyperref}` default link borders. L5 → `[colorlinks=true,allcolors=blue]`. Takes effect on next compile (recompile deliberately out of scope this round). |
| N3 (MegaMapper caveat repeated) | **OPINION** | Deliberate repetition of a critical funding-status caveat; wordings differ. |

## Perplexity_citations (22)

| ID | Verdict | Evidence / action |
|---|---|---|
| E1 (no PDF provided) | **FALSIFIED** | v3 harness sends native PDF to all 5 vendors; reviewer-side ingestion artifact. |
| E2 (−35/8 vs −35/16 refs) | **FALSIFIED** | `Cai:2009fn` (bib L1) + `CaiBrandenberger:2014` (bib L162) both exist with real IDs; convention chain resolved in App. A (lead-closed). |
| E3 (GitHub URL unverifiable) | **FALSIFIED** | `curl -I https://github.com/Hubify-Projects/bigbounce` → HTTP 200 (public, live). |
| E4 (σ mixing ambiguity) | **STALE** | Lead's E2 abstract-scoping closure spells out which r/ε enters each endpoint. |
| E5 (±0.13 phrasing inconsistent) | **STALE** | Current abstract: ±0.13 absolute ≡ ~15% relative at r̄=0.85 — 0.13/0.85=15.3% ✓ exact. |
| E6 (3–5σ construction mixes nulls) | **STALE** | §VII defines optimistic=σ_GR=0 vs realistic=σ_GR 0.5–1.0; b_φ chain explicit. |
| M1 (Zhu & Cai 2026 citation) | **FALSIFIED** | arXiv:2603.13924 verified in bib (v1.7.39 web-falsification record, 15/15). |
| M2 (ref formatting + embedded annotations) | **PARTIAL (no edit)** | Braces closed by lead (N2). Remaining `note=` field annotations are legitimate BibTeX, deliberate transparency; PRD copyedit may strike — flagged, not removed. |
| M3 (Fisher vs withdrawn 9.9σ) | **STALE** | Withdrawn + correction note (Houston decision) + committed c8 Fisher. |
| M4 (BF traceability) | **STALE** | Closed-form Eq.(bf) + c9g + four-corner grid (lead-closed). |
| M5 (mechanism-independent language) | **STALE** | UV-completion-independence conditional block in intro + §II.B. |
| M6 (σ 0.7 vs 0.5 bookkeeping) | **STALE** | §VIII.B disambiguation sentence (bispectrum-only 0.7 vs joint 0.5). |
| M7 (halving language) | **STALE** | Abstract states pre-/post-budget halvings separately with rationale. |
| M8 (r>1 vs Eq.(5)) | **STALE** | Dedicated r>1 footnote in §III.B (footnote untouched per hard rule). |
| M9 ("first time" novelty) | **VERIFIED → CLOSED** | L226: "for the first time to our knowledge" (body's 2009–2024 literature-search support stands). |
| M10 ("unprecedented precision") | **VERIFIED → CLOSED** | L243: → "precision substantially beyond current Planck bounds". |
| m11 (abstract r_cos parenthetical) | **OPINION** | Abstract>0.97 and body 0.985±0.007 are consistent; abstract edit beyond accuracy = Houston territory. |
| m12 (Fig 6 / null-threshold dependence) | **VERIFIED → CLOSED** | Same locus as OpenAI E8; L600 now carries the full pre/post-budget chain with symmetry rationale. |
| m13 (3–7σ MegaMapper opacity) | **STALE** | §V explains the envelope construction + design-uncertainty disclaimer. |
| m14 (Planck 0.7σ vs 0.75σ) | **STALE** | Lead's M8 closure: 0.75σ in §VIII.A ✓. |
| N1 (duplicate phrases) | **VERIFIED → CLOSED** | 8-gram scan run on source: one true intra-paragraph duplicate found in §IX.D QSFI passage ("comprehensive SDB+bispectrum joint analysis is required to map..." twice); redundant final sentence removed (L604). Remaining repeats are deliberate body/conclusion restatements. |
| N2 (length vs contribution) | **OPINION** | Houston's call. |

## Claude_brutal (1 remaining)

| ID | Verdict | Action |
|---|---|---|
| N1 (abstract length ~1.5 pages) | **HOUSTON-DECISION** | Untouched per round instructions. |

## Artifacts produced this wave
- `research/focused_paper_source_integration/scripts/c9j_bf_template_rescale.py` + `outputs/c9j_bf_template_rescale.json` — META-E2 BF bookkeeping rescale, validated against the printed grid.
- 25 surgical edits to `02_full_draft.tex` (audit-trail comment block under `\date`). No recompile, no commit (per round instructions); next compile must run `/latex-audit`.
