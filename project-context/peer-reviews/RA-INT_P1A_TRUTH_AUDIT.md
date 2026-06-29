# RA-INT P1A — Truth Audit (Round A rigorous INT, neutral verdict-first)

**Date:** 2026-06-29
**Paper:** P1A `arxiv/paper1a_ech_nogo.tex` reviewed at v1A.0.87 (md5 b5197dc0, 32pp) → closed to **v1A.0.88**
**Reviewers dispatched (native-PDF):** OpenAI gpt-5 (methodology), Gemini 2.5-pro (cosmology), Grok-4.3 (adversarial, image-rasterized), Perplexity (citations — quota FAIL, no report).
**Own Opus end-to-end read:** yes (abstract, framework, four routes R1–R4, transparency theorem, barriers, Appendix B/C).

## Vendor recommendation lines (read literally)
| Vendor | Recommendation |
|--------|----------------|
| OpenAI gpt-5 | **MAJOR REVISIONS** (verified all arithmetic PASSED: ρNJL=4e-81 eV⁴, Δθ ratio ~1e-60, ρθ~1.6e-10 eV⁴, [(α/M)MPl]~3e-3 — all consistent) |
| Gemini 2.5-pro | **MAJOR REVISIONS** |
| Grok-4.3 | **REJECT** (harsh-outlier; pattern-064) |
| Perplexity | FAIL (401 insufficient_quota) |

## Verdict-first audit (against actual source)

### VERIFIED → CLOSED (2, honest non-fabricating fixes)
- **OpenAI E4** — ">100 orders of magnitude" galaxy-spin underprediction (L1623 + L1677). Asserted **twice** with NO derivation, NO source, NO mapping from α/M to spin-dipole amplitude A₀. Genuine unbacked false-precision overstatement. **FIX:** removed the OOM at both sites; reworded to honest qualitative "far below current observational sensitivity; no coupling→dipole mapping attempted." Did NOT fabricate the missing chain (`/never-fabricate-derivation`).
- **OpenAI E5** — fine-tuning scoreboard quintessence (10⁶⁰) / f(R) (10⁴⁰) in fig:naturalness caption carried NO citation/derivation, while ΛCDM (10¹²²) and spin-torsion (10⁵) ARE derived in-paper. **FIX:** added caption sentence flagging quintessence/f(R) as illustrative literature-level comparators, not derived here.

### FALSIFIED (pattern-063 rasterized-PDF extraction artifacts — actual source eqns dimensionally CORRECT)
- **Gemini E1** — claimed Eq.(onshell_rho) = (α/M)MPl⁴ (dim +3). Actual L3315: **(α/M)MPl⁵ ~ 1e-2 MPl⁴**, dim +4 CORRECT.
- **Gemini E2** — claimed Λ_eff = Ξ MPl⁴ (units mismatch). Actual L1419: **Λ_eff = Ξ MPl² + c_ω ω²**, dim +2 CORRECT, explicit units note L1425.
- **Gemini M4** — claimed Eq.(oneloop) equates dimensionless α. Actual L1316: equation is for **α/M (dim −1)** with δ_NY dim −1 — CONSISTENT.
- **Gemini N3** — fig 10¹²⁰ vs text 10¹²²: STALE, caption already 10¹²² (closed v1A.0.69).
- **OpenAI m7** — Appendix C "§VI8 broken xref": actually **§ VI + footnote 8** (valid coordinated-submission companion ref; footnote makes WKB self-contained).
- **Grok N1** — "future date June 28/29 2026": calibration — June 2026 is current.
- **Grok E2** — "abstract drops transparency scope limits": FALSIFIED, abstract L802-804 carries "(excluding propagating-torsion, dynamical-Immirzi-field, fermion-loop, and non-minimal-matter sectors)".

### OPINION / STALE / STRUCTURAL-SUBMISSION (not touched, per directive)
- Companion in-prep reliance (Grok E1, OpenAI E1/M1) — coordinated submission; tab:companion_inputs already isolates every imported number as non-load-bearing (standing-directive A). STRUCTURAL.
- Zenodo DOI deferred (OpenAI E2) — HOUSTON-DECISION, camera-ready.
- Title/abstract conditionality (Grok E3, Gemini M1) — already "channel-level assessment, not an operator-level theorem" + "conditional on this ansatz" in abstract. OPINION.
- Fig 3 H0=69.2 (Gemini m1, OpenAI E8) — closed v1A.0.85 (caption discloses H0-baseline domination). STALE.
- Cosmic-mean baryon line (OpenAI M2) — already present L1831. STALE.
- R2 alternative-ordering (OpenAI M3) — already "not used in the closure." OPINION.
- R3 ad-hoc β-function (OpenAI E7) — already labeled upper-bound EFT ansatz; Benedetti-Speziale cited as the real result. OPINION.
- Barrier 12 ΩGW ansatz (OpenAI E3) — already labeled "order-of-magnitude ceiling ansatz (not derived)" used only as ceiling (L2629). OPINION.
- Barrier naturalness/heuristic inflation (Grok M3, OpenAI M6/M8) — already disclosed in sec:barriers status paragraph (B5/6/7/9/13 general/heuristic). OPINION.
- R4 naturalness-not-amplitude (Grok M4) — deliberate honest framing, explicitly stated. OPINION.
- σ "not directly comparable" at every juxtaposition (Grok E4, OpenAI m1/m6, Gemini —) — primary σ-comparison sites (abstract L847, Sec IV L2120-2125, fig captions) all carry it; L2271 cites both measurements with NO σ-comparison so nothing misleading. OPINION/over-strict.
- Gemini M3 "vacuum energy" label on Fig 2 — paper internally consistent + explicit about D_inf∝e^-3N dilution; "vacuum energy" denotes the candidate role being tested by the no-go. OPINION (terminology).
- Paper length (Grok M2, OpenAI n3) — editorial. OPINION.

## Result
- **2 genuinely-VERIFIED items closed** (OpenAI E4, E5) with real honest fixes, no fabrication.
- All Gemini "dimensional inconsistency" ESSENTIALs FALSIFIED as rasterized-PDF misreads.
- Grok REJECT = clean harsh-outlier; zero genuine new VERIFIED items.
- v1A.0.87 → **v1A.0.88**; date → June 29 2026; recompiled ×3, **0 undef-refs, 0 overfull hboxes**, 32pp; page-1 stamp + both PDF edits verified.
