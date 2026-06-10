# P2 R24conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/paper2_fnl_forecast_v1.7.46.pdf` md5=45ee3af4 pages=23
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique
---

## Pass 1 — native-PDF brutal-referee read

All deliberate calibration items (Table III caption correction note; σ(n_fNL)=0.295/0.596 withdrawal note; B_Φ(c=2)↔B_ζ(6/5) mapping in App A; "0.5000 ratio" reframing; κ_ε rename; c9h 16-84% propagation; c9j ~9-14 envelope; long abstract) **NOT flagged** per Houston calibration.

### P2-E1 — Existential: none found
After two passes the bounce-vs-inflation thesis, the f_NL=-35/8 prediction, the Cai-convention derivation, the Heinrich+2024 σ(f_NL)=0.7 baseline, the r=0.84 template-overlap projection, and the Bayes-factor closed-form Eq. (7) all hang together. No load-bearing equation, citation, or framing collapses under scrutiny.

### P2-M1 — MAJOR (verifiable, recompute-grade): Table III row labels are correctly recomputed but one claim about "Corrected (10% residual; verification)" row is a tautology, not an independent check
Page 15 (Table III) lists a fourth row "Corrected (10% residual; verification)" = 3.5×10⁸ / 7.0 / 99.9% — *identical* to row 1 "Ideal (no GR)". The caption says: "by construction, equal to 'Ideal' at this template-overlap order: a 10% residual GR contamination after correction has negligible impact on the Bayes factor at the reported significant-figure level (ΔBF<0.1). It is included as a verification row, not as an independent configuration, and the two rows are not independent scenarios but rather bookend the same GR-free regime." This is honest, but the row design is then misleading as printed — a reader scanning Table III sees four rows and naturally assumes four independent scenarios. **Fix**: either delete the redundant row from Table III and move its statement to a footnote/prose sentence, or relabel as "Corrected (= Ideal, verification only)" and visually distinguish (italics, indent). Currently the verification-row text lives only in the caption, which is exactly where readers don't look for "is this row different from row 1?".

### P2-M2 — MAJOR: Table III column-3 P(BF>3) values lack the noise floor disclosure that the prose elsewhere demands
Page 15 Table III: column "P(BF>3) vs. SSFSR" reports 99.9% / 99.0% / 93.1% / 99.9%. The recompute (`c9g_bf_table_recompute.py`) returns these to four-digit precision (0.9985, 0.9902, 0.9314). However, page 10 explicitly states "the spreads quoted in this paper come from prior and scenario variation, not from Monte Carlo noise" and that the realization count "is not a tightening of the underlying σ(f_NL)=0.7 ... it is the convergence-stability sample size, chosen to drive the analytic shot noise of the Bayes factor below the analytic shot noise." Given 2×10⁵ draws and binomial noise on P>3, 1σ stat on P≈0.93 is √(0.93·0.07/2e5) ≈ 5.7e-4 (i.e. ±0.06pp). That is well below the 93.1% reported precision, so the 3-significant-figure quote is fine — but **the paper never states this**, and a referee can legitimately ask "are these MC-noise-significant?". Add one sentence to the Table III caption: "P(BF>3) Monte Carlo standard errors are <0.1 percentage points at 2×10⁵ realizations and are below the quoted precision."

### P2-M3 — MAJOR: §VII.A page 13 right-column inline numbers for SDB b_φ degradation contradict the §III.B optimistic envelope
Page 13 Fig. 5 caption: "MegaMapper gives ~ 4σ; relaxing to 50% drops this to ~ 2σ. The bispectrum channel remains at ~ 5σ (optimistic) or ~ 3-4σ (after GR degradation) at fixed Heinrich et al. b_φ universality [4]; relaxing b_φ universality per tracer bin [26] degrades the optimistic 5.2-5.5σ headline to ~4.0-4.2σ (30% central) and ~3.5-3.7σ (50% conservative)." The 50%-prior figures (3.5-3.7σ bispectrum) sit at the lower edge of the abstract's "3-5σ" but **below** §VII.A.3 third-paragraph "the realistic range is ~ 3-5σ". A reader who only reads §VII.A.B will conclude the conservative endpoint is 3.5σ; a reader who skims the abstract sees "3-7σ" (page 8 right column). The numbers are mutually consistent under "envelope vs. point estimate" framing but never explicitly reconciled in one place. **Fix**: add a one-line crosswalk in §VII.D (Additional Systematic Considerations) or in the Caveats: "the abstract's 3-7σ envelope combines the conservative endpoint of the b_φ 50%-prior bispectrum (~3.5σ) with the MegaMapper optimistic ceiling (~7σ); the realistic SPHEREx-only window is 3-5σ."

### P2-m1 — minor: typo / grammar
Page 6 left column: "A factor-of-two discrepancy exists in the literature: Cai & Brandenberger [17] obtain f_NL=-35/16=-2.1875 when evaluated at c_s=1." This is fine, but the immediately following sentence starts "We performed a source-to-source normalization audit and established that this is a convention difference, not a physical one." — the antecedent of "this" is the discrepancy, not the value. Reads cleanly but could be sharpened to "this discrepancy."

### P2-m2 — minor: arXiv ref formatting
Page 22 [16] "M. Zhu and Y.-F. Cai, Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves, arXiv e-prints (2026), arXiv:2603.13924." — arXiv identifier 2603.xxxxx is impossible (arXiv format is YYMM.xxxxx and 2603 would be March 2026 which has not happened yet at submission). **Likely typo**: should be 2603 → 2403 (March 2024) or whatever the real preprint is. Verify with NASA ADS before submission.

### P2-m3 — minor: Eq. (8) right-hand side spacing
Page 14 right column Eq. (8): `f_NL(ε) = -35/8 - κ_ε(ε - 3/2) + O((ε - 3/2)²)`. The κ_ε rename (deliberate) is fine, but the inline definition above the equation says "κ_ε (not to be confused with the bispectrum polynomial coefficient c_1 of Sec. II)" — Sec. II uses (c_1,…,c_6); there is no c_1 conflict with κ_ε because κ uses a Greek letter. The disambiguation sentence is over-cautious noise and reads as defensive. Trim to "κ_ε depends on both the explicit ε-prefactors in the cubic action and the mode-function growth rate."

### P2-m4 — minor: §VIII.A Planck recast arithmetic
Page 14 right column: "Recasting the Planck PR4 constraint with the CMB Fisher template mismatch factor r=0.876 gives f_NL^bounce = -0.1 ± 5.7, which is 0.75σ from the bounce prediction (|-4.375 + 0.1|/5.71) and 0.02σ from zero". Check: 4.275/5.71 = 0.749 ✓, 0.1/5.71 = 0.0175 ≈ 0.02 ✓. Arithmetic is correct. **No issue.** (Including this as an explicit all-clear below.)

### P2-N1 — NEW (pass-2 only): the abstract's "3-7σ" headline is broader than any single number in the body
Pass-1 missed this; flagging on pass-2. The body justifies the headline as `optimistic ceiling (MegaMapper, ~7σ) + conservative floor (b_φ 50%, ~3.5σ)`. This is defensible but the headline is built from two **different facilities** (MegaMapper top, SPHEREx-with-50%-b_φ bottom). A reader pulling "3-7σ" out as "SPHEREx will detect at 3-7σ" is wrong: SPHEREx alone is 3-5σ (realistic) to 5.2-5.5σ (optimistic). MegaMapper carries the 7σ. **Recommend**: abstract sentence "MegaMapper (proposed) could reach σ(f_NL)≈0.5 ideally (3-7σ realistic …)" should be tightened to "MegaMapper (proposed) could reach σ(f_NL)≈0.5 ideally (5-7σ realistic at f_NL=-35/8, conditional on …)". This separates the SPHEREx 3-5σ from the MegaMapper 5-7σ rather than blurring them into one "3-7σ" envelope.

---

## Explicit all-clears (recompute-verified)

| Claim | Verified via | Result |
|-------|--------------|--------|
| Table III row 1: BF vs SSFSR = 3.5×10⁸, BF vs Tuned narrow = 7.0, P>3 = 99.9% | `c9g_bf_table_recompute.py` rerun | 3.47e8 / 7.001 / 0.9985 ✓ |
| Table III row 2: 4.5×10⁵ / 6.1 / 99.0% | same script | 4.52e5 / 6.05 / 0.9902 ✓ |
| Table III row 3: 6.4×10² / 4.7 / 93.1% | same script | 6.44e2 / 4.70 / 0.9314 ✓ |
| Table III row 4 = row 1 (verification) | same script | 3.47e8 / 7.001 / 0.9985 ✓ |
| App A mapping algebra: B_Φ(c=2) → B_ζ(6/5) | hand recompute | Φ=(3/5)ζ ⇒ P_Φ=(9/25)P_ζ ⇒ (5/3)³·2·(9/25)² f_NL [PP+perms] = (6/5) f_NL [PP+perms] ✓ |
| Eq. (A3) commutator: i⟨[ζ³,L]⟩ = -2 Im⟨ζ³L⟩ | operator identity from Hermiticity of H_int | ✓ (true for any Hermitian operator) |
| c9j rescale 17.1→14.4, 9.8→9.2, 7.0→6.2, 4.0→4.0 | `c9j_bf_template_rescale.json` | 14.36, 9.19, 6.19, 3.96 ✓ (paper rounds 3.96→4.0) |
| c9j measured-space 7.0→5.9 | same JSON | 5.87 ✓ |
| c9j abstract envelope "~9-14" | derived from 9.19 (low Gaussian) to 14.36 (high delta) | ✓ |
| §VIII.A Planck recast 0.75σ from prediction | (4.275)/5.71 | 0.749 ✓ |
| §IX.C "naive 6.25σ → 5.2-5.5σ" | (35/8)/0.7 = 6.25 ✓, ×r=0.83-0.876 = 5.19-5.48 | ✓ |
| c9h propagation 16-84% = 4.4-6.2σ | pre-template 6.25σ × r-percentile/r-central (0.75/0.84)·6.25=5.58 etc.; ALT interpretation post-template midline 5.25σ × (0.75/0.85)→4.63 and (0.94/0.85)→5.80 — paper's 4.4-6.2σ band is the more conservative pre-template propagation through extreme tails | ✓ (within rounding) |

---

## Pass-2 self-critique vs. `research/focused_paper_source_integration/02_full_draft.tex`

On pass 2 I diffed the PDF against the .tex source.

- Pass-2 hit: P2-N1 (abstract 3-7σ blends two facilities). Pass-1 missed it because I parsed the abstract sentence as one envelope; the body confirms 7σ is MegaMapper-only.
- Pass-1 was tempted to flag the "0.5000 ratio" reframing as suspicious — *suppressed per calibration* (deliberate).
- Pass-1 was tempted to flag the long abstract — *suppressed per calibration* (Houston decision).
- Pass-1 was tempted to flag the c9j ~9-14 envelope vs. abstract ~10-17 envelope as inconsistent — checked: paper explicitly notes "the abstract envelope BF~10-17 correspondingly reads ~9-14 in strict bounce-amplitude bookkeeping" and "no qualitative conclusion changes". **Deliberate, NOT a finding.**
- Pass-1 was tempted to flag the σ(n_fNL)=0.086/9.9σ withdrawal note as "why is this still in the paper" — suppressed per calibration (deliberate transparency).
- Pass-2 confirmed Table III caption correction note is deliberate and well-written.
- Pass-2 confirmed κ_ε rename (was κ_1) is internally consistent throughout — no orphan κ_1 references.
- Pass-2 found no fabricated math, no orphan refs (all 38 refs cited), no broken cross-refs in the rendered PDF.

## Summary recommendation

PRD **minor revision**. The paper is technically sound: every load-bearing calculation I could recompute matches the released scripts to 3 significant figures. The MAJOR findings are presentation issues (P2-M1 redundant Table III row, P2-M2 missing MC-noise disclosure on P(BF>3), P2-M3 unreconciled b_φ degradation numbers) that a referee will hit; none invalidate a result. The single NEW (pass-2) finding P2-N1 is a sharpening of the abstract envelope to separate SPHEREx (3-5σ) from MegaMapper (5-7σ). No existential (E#) findings. No new fabricated math, no convention errors beyond the deliberate Cai/Li-Brandenberger calibration that the paper already addresses head-on in App A.

**Counts: E=0, M=3, m=4, N=1 — minor revision**
