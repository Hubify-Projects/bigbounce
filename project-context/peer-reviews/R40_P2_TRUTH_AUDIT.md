# R40 P2 — Truth Audit (pre-arXiv, v1.7.69)

**Paper:** P2 — "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook"
**Source:** `research/focused_paper_source_integration/02_full_draft.tex` (1171 lines), PDF md5=dbcc5834, 29 pp.
**Auditor:** Opus truth-audit + synthesis lead, 2026-06-18
**Reviewer legs:** OpenAI gpt-5 (methodology, MAJOR REVISIONS), Gemini 2.5 Pro (cosmology, ACCEPT w/ minor), Grok 4.3 (brutal, REJECT), Perplexity (FAILED — 100KB cap, zero findings), Claude Opus (ACCEPT, no actionable findings).

**Protocol note:** Reviewers are context-blind. P2 is an explicit **sensitivity recast** — "Fisher not independently recomputed / Fisher invariance" is a KNOWN category error and demoted on sight (paper says so at L575, L729). The v1.7.x changelog (L27–L472 comment block) records that most of these exact items were adjudicated in prior R/EXT rounds.

---

## Audit table

| ID | Vendor | Claim (severity) | On-disk verification | Verdict |
|----|--------|------------------|----------------------|---------|
| E1 | OpenAI | DOI is "inserted at submission" placeholder; artifacts unverifiable (ESSENTIAL) | True that DOI is a submission-time placeholder; standard for pre-submission. Zenodo DOI is minted at arXiv submission, not before. Not a content defect. | OUT-OF-SCOPE (submission-mechanical; resolves at submission) |
| E2 | OpenAI | 6-coeff polynomial fit from 3 benchmarks → r underdetermined (ESSENTIAL) | Paper explicitly discloses the 3-dim null space, runs a 10k-sample null-space scan, reports r∈[0.829,0.876] across schemes, r_cos>0.97 all samples (abstract L573, L697). Claude leg confirmed r self-consistency. Disclosed limitation of a recast, not a hidden flaw. | OPINION (scope demand beyond a recast) |
| E3 | OpenAI | 2D CMB-style injection test "validates" 3D r (ESSENTIAL) | Paper labels it a sanity check, not the binding validation; r enters as shape-weighted degradation (L575, L731). Reviewer wants it relegated — it already is. | OPINION |
| E4/N1 | OpenAI | B_NL / A_T parenthesization ambiguous (ESSENTIAL→typography) | Eqs as compiled are unambiguous in PDF (Claude leg flagged 0 such). Clarity preference. | OPINION |
| E5/E6/M4 | OpenAI | Fig 5 / b_phi-prior → σ(fNL) mapping not reproducibly tied to Fisher (ESSENTIAL/MAJOR) | Mapping IS given: L893, L898 caption, L731 give 20%→σ0.7, 30%→0.9–1.0, 50%→2.2, with the cross-term derivation. Tied to Heinrich+Barreira. Fig is labeled illustrative. | STALE (closed in EXT/Gem-M rounds; see L67, L152) |
| E7/N5 | OpenAI | Add closed-form P(BF>3) alongside MC (ESSENTIAL→MINOR) | MC + analytic both present (L797–L798 give exact-vs-approx with sub-% error). Closed form already shown. | STALE |
| M1 | OpenAI | κ_ε=5.6–80 needs derivation (MAJOR) | Changelog L556: derivation logged (80×0.0045/4.375≈8.2%). Range disclosed as order-of-magnitude (L592). | STALE |
| M2/M3 | OpenAI | weighting schemes / x3,min stability under-documented (MAJOR) | r-spread ±0.02 across schemes reported; squeezed-cutoff insensitivity is a real reported result. Documentation-density preference. | OPINION |
| M5 | OpenAI | App A symmetry factors not fully shown (MAJOR) | -2Im commutator identity verified symbolically (abstract L573, App A.1); Claude leg ACCEPT on this. Full Sv listing is a completeness nicety. | OPINION |
| E8/M8/N6 | OpenAI | Fig 4 SDB vs bispectrum comparability / r-usage labels (ESSENTIAL/MAJOR) | Paper already states SDB significances are \|fNL\|/σ (no r) vs bispectrum \|fNL\|r/σ; Fig captions carry "not directly comparable" framing (changelog L74, pattern-2 closed). | STALE |
| E9 | OpenAI | M(k,z) unit convention unstated (ESSENTIAL) | L692: k comoving in h/Mpc stated; δ_c, T(k), D(z) normalizations given. One-line c=1 note would be additive polish, not a defect. | OPINION (additive) |
| E10 | OpenAI | Fig/table → script provenance manifest (ESSENTIAL) | Same surface as E1 (resolves at Zenodo freeze). | OUT-OF-SCOPE / DUPLICATE of E1 |
| M6 | OpenAI | b_phi "fixed by UMF" vs "marginalized" inconsistency (MAJOR) | L729 ("fixed universality relation") and L893 ("marginalize…assuming UMF…fixes b_phi to single value per tracer") are consistent: marginalized WITH a UMF prior that pins it. Both readings reconciled in text. | MISLABELED |
| M7/M9 | OpenAI | shape-mismatch variance / 0.7-reuse covariance only heuristic (MAJOR) | Paper explicitly labels Eq.(7) "heuristic primordial-field scaling check, NOT a galaxy-covariance derivation" (L727) and flags it in the abstract (L575). Honest self-labeling; a full re-derivation is the recast's stated out-of-scope. | OPINION (recast scope, already hedged) |
| N2/N3/N4/T1–T6 | OpenAI | copy-edit, acronyms, fig legends, Hehl–Datta naming (MINOR/NIT) | Cosmetic; non-load-bearing. Hehl–Datta naming already qualified in body (L592). | OPINION |
| length | OpenAI/Grok-M1 | 29 pp too long for a recast (MAJOR/scope) | Editorial preference; not a correctness finding. PRD has no hard cap. | OPINION |
| G-M1/M2/M3 | Gemini | BF-bookkeeping abstract phrasing / Eq.9 derivation sketch / Table IV baseline (MINOR) | Abstract already disentangles r→1 vs noise-weighted (L575); BF closed-form derivation present (L845, eq:bf_exact). Clarity polish. | OPINION |
| **G-P9-m1** | Gemini | Text says fNL²Δ² but Eq.(7) shows fNL²Δ — extra power of Δ (MINOR arithmetic) | **FALSE.** L724 Eq.(7) = `\fnl^2\,\Delta_\zeta^2(k)` (HAS the square). L727 text = `\fnl^2\,\Delta_\zeta^2 ∼ 4×10⁻⁸`. Text and equation agree; reviewer dropped the square when reading. | MISLABELED (reviewer misread) |
| **G-P10-m2** | Gemini | f_cat dilution 0.008 should be 0.083 — factor-10 error (MINOR arithmetic) | **FALSE.** Paper formula (L733) is `f_cat²/(1+f_cat)² = 0.1²/1.1² = 0.00826 ≈ 0.008`. Correct as written. Reviewer evaluated `f_cat/(1+f_cat)²` (dropped numerator square). | MISLABELED (reviewer misread) |
| G-N1 | Gemini | houston@hubify.com is placeholder/non-institutional | **Canonical author email** per repo CLAUDE.md. Not a placeholder. | STALE/MISLABELED |
| G-N3 | Gemini | b_phi vs b_φ inconsistent | Body text uses `b_\phi` uniformly (grep). All "b_phi" hits are in `%`-comment changelog lines, not rendered. | STALE |
| Grok-E1 | Grok | Abstract buries 2.6σ floor, leads with 5.2–5.5σ (ESSENTIAL) | Abstract states BOTH and explicitly adopts "5.2–5.5σ optimistic AND 2.6–5σ realistic ranges as the headline forecast" (L575); null disfavors at the same 2.6–5σ. Floor is in the abstract ≥3×. Framing adjudicated across prior rounds (L226, L251, L258). | STALE / OPINION |
| Grok-E2 | Grok | -35/8 imported from Cai w/o independent derivation (ESSENTIAL) | Independent -2Im operator-algebra derivation in App A.1 (abstract L573); claim conditionalized on assumptions (a)–(f) and "Wilson-Ewing class" throughout (L592). | OPINION / MISLABELED |
| Grok-E3 | Grok | Remove all BF numbers from abstract — non-definitive (ESSENTIAL) | Abstract already says BF "illustrative…not definitive model-selection evidence" (L575). Total removal is a stylistic demand; Gemini+Claude treat as MINOR-clarity. | OPINION |
| Grok-M4 | Grok | MegaMapper bars not labeled speculative (MAJOR) | Labeled "proposed but not yet funded…illustrative 3–7σ design-uncertainty envelope" in abstract (L575), Fig caption (L738), and §megamapper (L748). | STALE |
| Grok-M2/M3 | Grok | r basis-invariance / quadrature independence not proven (MAJOR) | Dup of OpenAI E2/M7; quadrature labeled "transparent scoping choice whose conservatism a full joint Fisher would confirm" (L575). | DUPLICATE / OPINION |
| Grok-N2 | Grok | "Dated: June 14, 2026" anachronism | `\date{June 14, 2026}` (L26) is the actual v1.7.69 bump date. Cosmetic; will refresh at submission. | OPINION (cosmetic) |
| Perplexity | — | Reviewer call FAILED (100KB cap) | No findings produced. | N/A |

---

## Verdict

**ACCEPT — no VERIFIED-OPEN closures required before arXiv.**

- Two Gemini PASS-2 "arithmetic errors" (P9-m1, P10-m2) are reviewer **misreads of correct formulas** — both verified false against L724/L727 and L733.
- All OpenAI/Grok ESSENTIAL/MAJOR items are either (a) the known recast category error, (b) closed in prior R/EXT rounds per the changelog, or (c) OPINION (length, remove-BF-from-abstract, more-documentation).
- Gemini and Claude legs both return ACCEPT; OpenAI's "MAJOR REVISIONS" and Grok's "REJECT" rest on demanding an independent 3D Fisher recomputation that the paper explicitly and repeatedly scopes out as a sensitivity recast.
- Author email is canonical; date is the real version date; b_phi notation is uniform in body text.

**Merged final verdict: ACCEPT for arXiv at v1.7.69.** Zero load-bearing defects survive grounding. Optional, non-blocking polish if a no-op restamp is desired: refresh `\date{}` to the submission date and add a one-line c=1 unit note after Eq.(4) — neither gates submission.
