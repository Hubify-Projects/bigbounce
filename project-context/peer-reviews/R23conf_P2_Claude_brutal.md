# P2 R23conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/paper2_fnl_forecast_v1.7.45.pdf` md5=d421f116 pages=22
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique
---

## Findings

### P2-E1 — Corrupted/unreadable text block in the flagship underdetermination scan (BLOCKING)
- **Location**: p. 3, §II.A, right column, "We then sampled 10,000 valid coefficient sets…" paragraph.
- **Problem**: The paragraph renders as garbled run-on text with all inter-word spaces stripped and a truncated quantitative claim: *"(radius 50 is approximately 0.TheradiusanduniformsamplingmeasureareconventionalchoicesspacespreadunderthisconventionratherthanasacalibrateduncertaintytheEuclidean norm of the full reference coefficient vector (2,7,3,−12,−69,19) (‖c_ref‖ ≈ 73)"*. The intended statement (apparently "radius 50 ≈ 0.7× the Euclidean norm…" plus a caveat that the radius/measure are conventional choices, not a calibrated uncertainty) is unrecoverable. This sits inside the paper's headline ±0.13 amplitude-scatter analysis — a load-bearing methods paragraph. Almost certainly unescaped prose inside math mode in the .tex source.
- **Required fix**: Repair the source (move the caveat sentence out of math mode), restate the truncated "radius 50 is approximately 0.7×‖c_ref‖" claim explicitly, recompile, and re-run the visual overflow/garble audit. This alone makes v1.7.45 unpublishable as-is.

### P2-M1 — Bayes-factor cross-table inconsistency: delta-prior/narrow-competitor cell does not reconcile across the four-corner grid, Table II, and Table III
- **Location**: p. 10–11 (§VI prose + four-corner table), Table II row 4 + footnote a, Table III rows 1–3 + caption.
- **Problem**: The same nominal configuration — delta bounce prior at −35/8 vs tuned multifield competitor with narrow [−5,+5] prior — is assigned three values that do not cohere: (i) the four-corner grid and §VI.A prose say **BF ~ 7**. I verified this is the pure closed-form Eq. (7) value with no GR: numerator 10 × N(−4.375; −4.375, 0.7) = 5.70; denominator ∫₋₅⁵ N(f; −4.375, 0.7) df = Φ(0.893) ≈ 0.814; B = 7.0 ✓ (broad [−15,+15] gives 30 × 0.5699 = 17.1 → "~17" ✓; σ_theory=1.0 narrow gives ≈ 4.0 ✓). (ii) Table III row 1 ("Ideal, no GR") gives BF-vs-Tuned = **10.9** for the same delta/narrow no-GR cell. (iii) Table II row 4 footnote a fixes the σ_GR = 0.5 value at **9.4**. So at no-GR the paper reports both 7.0 (analytic) and 10.9 (Table III), a 56% discrepancy in the same cell, and the footnotes assert consistency ("consistent with the narrow→broad sweep BF ~7→17") without ever reconciling 7 vs 9.4–10.9. If the Table III machinery (mock-detection realizations, nuisance draws) systematically inflates the delta/narrow BF relative to the closed form, that mechanism must be stated and quantified; if not, one of the numbers is wrong.
- **Required fix**: Recompute the delta/narrow cell in both pipelines on identical assumptions; either correct the discrepant value or add an explicit reconciliation sentence quantifying why the realization-marginalized BF (10.9/9.4) exceeds the closed-form 7.0. Update footnote a of Table II accordingly.

### P2-m1 — §IX.D bias-marginalized triple (1.53, 7.06, ρ = −0.97) is internally inconsistent under the stated marginalization identity
- **Location**: p. 16, §IX.D, first paragraph.
- **Problem**: The fixed-bias chain is clean: 1.53/3.08 ⇒ |ρ| = 0.868 → "−0.87" ✓; 3.08/1.53 = 2.0× ✓; 4.375/3.08 = 1.42 → 1.4σ ✓; 4.375/7.06 = 0.62 → 0.6σ ✓; σ(n_fNL) = 0.295/0.596 vs "testable at ±0.30/±0.60" ✓. But the bias-marginalized chain quotes the 4.6× degradation **relative to the fixed-bias** σ_unmarg = 1.53 while pairing it with ρ = −0.97. Via σ_marg = σ_unmarg/√(1−ρ²): 1.53 and 7.06 imply |ρ| = 0.976 → should round to **−0.98**, not −0.97; conversely ρ = −0.97 and σ_marg = 7.06 imply a bias-marginalized baseline σ_unmarg ≈ 1.72 and a degradation of **4.1×**, not 4.6×. The three numbers cannot simultaneously hold in a 2-parameter identity; with extra bias nuisances the simple identity is not exact, but then the text should not invite the reader to apply it against the fixed-bias 1.53.
- **Required fix**: Quote the bias-marginalized unmarginalized baseline explicitly (≈1.7?) and reference the degradation to it, or change ρ to −0.98, or add one sentence noting the identity is inexact once per-sample biases are co-marginalized. Pick one; currently the paragraph fails its own arithmetic audit at quoted precision.

### P2-m2 — "slightly weaker" misdescribes a 2.2× degradation
- **Location**: p. 16, §IX.D: "The SDB-only σ_unmarg(f_NL) = 1.53 is consistent with (slightly weaker than) the bispectrum-only σ(f_NL) = 0.7 baseline".
- **Problem**: 1.53 is 2.2× weaker than 0.7. "Slightly" is minimizing language a referee will read as spin.
- **Required fix**: "consistent in scaling with, though ≈2.2× weaker than, the bispectrum-only baseline, as expected for the SDB channel."

### P2-m3 — b_φ degradation endpoint 4.5σ not reproducible from the stated rule
- **Location**: p. 12, §VII.B: "degrades the headline 5.2–5.5σ … to ~4.0–4.5σ at the central 30% degradation point and to ~3.5–3.7σ at the conservative 50% end."
- **Problem**: The 50% endpoint checks exactly as ÷1.5 (5.2/1.5 = 3.47, 5.5/1.5 = 3.67 → "3.5–3.7" ✓), but the same rule at 30% gives 5.2/1.3 = 4.0, 5.5/1.3 = 4.23 → "4.0–4.2", not 4.0–**4.5**. The upper endpoint is inconsistent with the rule that generates the adjacent range.
- **Required fix**: Change to ~4.0–4.2σ, or state the actual (non-÷(1+x)) mapping used.

### P2-m4 — ε-correction window endpoint −4.35 vs stated 1–8% correction
- **Location**: p. 5 (§II.C) and p. 15 (post-Eq. 9): "f_NL ∈ [−4.35, −4.02] (a 1–8% correction…)".
- **Problem**: A 1% less-negative shift from −4.375 gives −4.331 → −4.33; the quoted −4.35 corresponds to ≈0.6%. The 8% endpoint (−4.025 → −4.02) is fine. Same mismatch in both locations.
- **Required fix**: [−4.33, −4.02], or relabel the window 0.6–8%.

### P2-N1 — Abstract length far exceeds PRD norms
- **Location**: p. 1–2. The abstract runs ~1.5 pages with inline section/table cross-references. PRD expects a single paragraph (~5% of paper length). This will be the first thing an editor flags.
- **Required fix**: Compress to ≤300 words; move the convention-halving caveat and four-corner BF bookkeeping into the introduction/conclusion.

### P2-N2 — Bibliography capitalization/annotation nits
- **Location**: Refs [23] ("weirdest sdss galaxies"), [38] ("cosmoglobe dr1 results. ii. … wmap and planck lfi"). Lowercase proper nouns — missing braces in the .bib. Also refs [33], [38] embed editorial annotations ("table 2.7: σ(f_NL) ≈ 3–5…", "reports β = 0.35°±0.70° … (no ACT)") inside the reference entries; PRD copy-editing will strike these — move to footnotes if the content matters.

## Explicit all-clears (areas scrutinized and found clean)

- **§IX.D rewritten SDB paragraph — core arithmetic**: 0.295/0.596 fixed/bias-marginalized labels match throughout; 1.4σ = 4.375/3.08 ✓; 0.6σ = 4.375/7.06 ✓; 2.0× = 3.08/1.53 ✓; fixed-bias ρ = −0.87 self-consistent ✓; subordination to the bispectrum headline is explicit and repeated ✓; the "two distinct Fisher analyses" disambiguation paragraph (why r = 0.84 does not apply to the SDB Fisher) is correct and well-argued ✓. Only the bias-marginalized triple (m1) and wording (m2) fail.
- **Correction note**: journal-neutral, states the withdrawn σ(n_fNL) = 0.086 / ~9.9σ, the non-reproducibility reason, the Doré-lineage validation (all-sample 1.02 vs published ~0.9), and code release. Acceptable deliberate disclosure; no flag.
- **Cai-convention factor-of-two audit (App. A + Table IV)**: the operator-algebra −2 Im commutator identity (A3), Wick expansion (A5), doubling (A7), and the empirical 0.5000 ε-decomposition ratio form a coherent resolution; Table IV arithmetic exact (4.375×0.84/0.7 = 5.25σ; 2.1875×0.84/0.7 = 2.63σ) ✓; conclusion-section halving (3.1σ raw; ~2.6–2.75; ~1.5–2.5) consistent with the abstract ✓.
- **Systematic-budget chain to the 3–5σ headline**: 6.25σ naive → ×0.876 = 5.475 → 5.5σ ✓; ×0.83 = 5.19 → 5.2σ ✓; GR (σ_GR = 1.0) + widened b_φ → 3.0σ floor ✓; §VII GR 10–30% literature anchoring coherent; only the m3 endpoint fails.
- **Bayes-factor table priors**: Eq. 7 closed form correct; σ_theory = 0.5/1.0/2.0 bullets verified (13.91→~14, 9.80→~10, 5.65→~6; 4.375σ exclusion of −2.1875 at σ=0.5 ✓; 1.09σ at σ=2.0 ✓); SSFSR point prior at f_NL ≈ 0.015 defined in Table II caption ✓; "wider bounce prior ⇒ smaller BF" monotonicity stated and correct ✓. Only the cross-table cell (M1) fails.
- **Abstract faithfulness**: every abstract number (r range [0.829, 0.876], 5.2–5.5σ, 3–5σ, BF 10–17/4/7, 8–11 GR spread, MegaMapper 3–7σ, convention halving, 84%±2% template recovery) traced to a body location and matches ✓ (modulo M1's underlying ambiguity).
- **Figures**: Fig. 1 benchmarks (−4.375/−3.984/−2.250) match Table I ✓; Fig. 2 error-bar endpoints now defined in caption ✓; Figs. 4/5 captions define panels and the b_φ 20%/50% markers ✓; Fig. 6 error bars defined ✓.
- **Other spot checks**: Planck recast (−0.1/0.876 = −0.11, 5.0/0.876 = 5.7, 0.75→0.7σ, 0.02σ) ✓; birefringence 0.072/0.094 = 0.766 → 0.77σ and 0.342/0.094 = 3.6σ ✓; τ_NL = (36/25)(4.375)² = 27.56 ✓; calibrated refs 2603.13924 / 2511.09466 / 2509.13654 not flagged per round calibration.

## Pass-2 self-critique

- E1 re-verified visually: the corruption is real, not an extraction artifact (spaces stripped mid-paragraph, sentence truncated at "approximately 0.").
- M1: I re-derived the four-corner analytic values from Eq. 7 myself before flagging; ~7/~17/~4/~10 all reproduce, which localizes the inconsistency to Table III's 10.9 (no-GR) / 9.4 (σ_GR = 0.5) vs the closed form — this is a genuine unreconciled discrepancy, not referee confusion, though the fix may be one explanatory sentence rather than a recompute if the MC machinery legitimately differs.
- m1: softened from M after noting the 2-parameter identity is inexact under additional bias nuisances; the required fix is presentational, but at quoted precision the printed triple still fails the check the paper invites.
- m3/m4: pure arithmetic, double-checked; both stand.
- Considered flagging the SDB validation gap (1.02 vs ~0.9 Doré, 13%) — declined: it is disclosed as a lineage cross-check, not a claimed reproduction.

## Summary recommendation

**Major revision (borderline minor).** The physics core — the −35/8 prediction, convention audit, template-overlap machinery, systematic budget, and the rewritten subordinate SDB section — is sound and the headline 3–5σ claim survives scrutiny. But v1.7.45 cannot go out with E1 (corrupted methods paragraph in the flagship underdetermination scan) and M1 (an unreconciled factor-of-~1.5 discrepancy in the delta/narrow Bayes-factor cell across three tables). Fix E1, reconcile M1, repair the §IX.D bias-marginalized triple (m1) and the two endpoint arithmetic slips (m3, m4), tone down "slightly weaker" (m2), and compress the abstract (N1). All fixes are local; no recomputation of the headline forecast is required unless the M1 reconciliation uncovers a pipeline bug.
