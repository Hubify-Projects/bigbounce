# P2 R25conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/paper2_fnl_forecast_v1.7.47.pdf` md5=a6ea2ee9 pages=24
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique
---

## Pages 1-6 findings

### P2-m1 — abstract paragraph length / single block
- **Location**: Page 1 abstract.
- **Problem**: Abstract is a single block of ~85 lines (per Houston decision per calibration), but reader is still hit with two distinct topical concerns: (i) the dual-pronged discrimination framing + CFC caveats, then (ii) Bayesian BF results. The hand-off "An idealized joint (f_NL, n_fNL) scale-dependent-bias Fisher self-consistency check is discussed in §IX" buries the n_fNL withdrawal note rather than acknowledging it inline.
- **Required fix**: Add one-clause flag in abstract that σ(n_fNL) is withdrawn pending bias-model fixes, citing §IX; or leave per Houston call but note in cover letter that abstract intentionally omits the withdrawal flag.

### P2-N1 — §II.A "(2,7,3,−12,−69,19)" reference solution
- **Location**: Page 3, last paragraph of §II.A; matches Table I.
- **Verification**: Confirmed P(1,1,1), P(2,1,1), P(10⁻⁴,1,1) reproduce −3.984, −2.250, −4.375 against Cai et al. values −255/64, −9/4, −35/8 (arithmetic verified: −35/8=−4.375, −255/64=−3.984375, −9/4=−2.25). All-clear.

### P2-N2 — §II.D quasi-dust n_s formula
- **Location**: Page 6, "n_s = 1 + 12w follows from the growing-mode solution".
- **Verification**: w=−0.003 → n_s = 1 − 0.036 = 0.964; matches quoted 0.964. All-clear.

### P2-N3 — Maldacena consistency value
- **Location**: Page 2, "f_NL ≈ (5/12)(1−n_s) ≈ 0.015".
- **Verification**: (5/12)(1−0.9649)=0.01463 ≈ 0.015. All-clear.

### P2-N4 — sky-coverage σ degradation
- **Location**: Pages 4–5, "1/√0.7 ≈ 1.19, a ~19% degradation".
- **Verification**: 1/√0.7 = 1.1952. All-clear.

### P2-m2 — Li-Quintin-Wang-Cai citation for −35/16
- **Location**: Page 6, "Li *et al.* [5] obtain f_NL = −35/16 = −2.1875 when evaluated at c_s = 1".
- **Verification**: Citation [5] present and used consistently; per calibration this is now correctly attributed to Li-Quintin-Wang-Cai JCAP 03(2017)031. All-clear pending bibliography check in later pages.

### P2-M1 — assumption (d) "cubic order verified only at linear order [10]"
- **Location**: Page 2 §II.B and page 5–6 §II.B/D restatements; explicit "Assumption (d) has been verified at linear order [10]. At cubic order, a semi-analytic order-of-magnitude estimate based on the superhorizon approximation … gives a correction δf_NL ~ 10⁻³ (negligible *if the superhorizon scaling holds*; this is a scaling estimate, not a derived bound)."
- **Problem**: The text correctly flags this as a scaling estimate, BUT the abstract and §II.C still call the prediction "robust across the bounce class without prolonged post-bounce inflation" without re-flagging that the third-order transfer through the bounce is only an order-of-magnitude argument. A reader who only reads the abstract + §II.C does not learn that the linchpin assumption (d) is unverified at the order being tested.
- **Required fix**: In §II.C "Assumptions" paragraph, add one sentence: "Assumption (d) is the weakest link of the present derivation — verified at linear order [10] and supported only by an order-of-magnitude superhorizon argument at cubic order; a full numerical computation of the bounce-modified Maldacena integrals is required to upgrade this to a derived bound." Without this, "robust" is overclaimed.

## Pages 7-12 findings

### P2-N5 — bispectrum-vs-inflation contrast 4.375/0.015 ≈ 290
- **Location**: Page 10 §VI.A, "|f_NL^bounce|/|f_NL^inf| = 4.375/0.015 ≈ 290".
- **Verification**: 4.375/0.015 = 291.67; quoted as "≈ 290". All-clear.

### P2-N6 — Bayes factor Li position calculations
- **Location**: Page 11, "Gaussian, σ_theory = 0.5 … positions f_NL = −4.375 at 1σ around the central value −4.375, which excludes the Li et al. value −2.1875 at 4.375σ"; "σ_theory = 1.0 … Li et al. value −2.1875 lies at 2.19σ"; "σ_theory = 2.0 … the Li et al. value −2.1875 lies at 1.09σ".
- **Verification**: |(−4.375) − (−2.1875)|/σ = 2.1875/{0.5, 1.0, 2.0} = {4.375, 2.1875, 1.09375}. All three match. All-clear.

### P2-N7 — Bayes factor 9.80, 13.91, 5.65 spot-checks
- **Location**: Page 11 bullet list (scipy.stats.norm BF values).
- **Verification**: These are point-prior likelihood-ratios that depend on prior width and observed f_NL. Cannot independently re-derive without the integration code, but they bracket the recommended BF ~ 10 (σ=1.0, broad) which is internally consistent with the surrounding prose. Noted as code-derived, all-clear at consistency level.

### P2-M2 — "the headline range ~10–17 quoted in the abstract" bracketing
- **Location**: Page 11 paragraph after the bullets: "The headline range ~ 10–17 quoted in the abstract therefore brackets the recommended baseline (σ_theory = 1.0, lower bound) and the delta-prior maximum (upper bound) at the broad multifield competitor prior [−15,+15]".
- **Problem**: The abstract reads "BF ≈ 10 (recommended σ_theory = 1.0 Gaussian bounce prior, broad multifield [−15,+15] competitor prior) up to BF ≈ 17 (delta bounce prior, same broad multifield competitor prior); the headline envelope is therefore BF ~ 10–17". This is fine ONLY if a reader interprets "headline" as covering recommended-to-theoretical-maximum. But the recommended is BF~10 and the BF~17 row is *explicitly* flagged in Table II footnote a/b as "theoretical-maximum upper bound … not the recommended headline." Quoting the upper bound as part of the "headline" envelope in the abstract conflicts with Table II's own footnote.
- **Required fix**: Either (a) drop the BF~17 endpoint from the abstract and quote BF ~ 10 (recommended) with BF ~ 7 (σ_theory = 1.0, narrow [−5,+5]) as the lower envelope, OR (b) re-label the abstract envelope as "recommended-to-theoretical-maximum" rather than "headline." Pick one; current language tells reader BF~17 is part of the headline while Table II says it isn't.

### P2-m4 — Fig 2 "−35/8B" typo
- **Location**: Page 9 Fig. 2 caption (rendered image): "FIG. 2. Detection significance for f_NL = −35/8B across survey configurations." The "B" appears to be a stray glyph in the figure title (rendered "−35/8B" instead of "−35/8").
- **Problem**: Image-embedded title text in the bar chart appears to render "−35/8B" — likely a TeX rendering artifact inside the matplotlib figure (a stray subscript/superscript or a leftover from "bounce"). Confirm by inspection of the source PNG/PDF figure title.
- **Required fix**: Rebuild Fig. 2 with title "f_NL = −35/8: Survey Detection Significance" or strip the stray glyph.

### P2-m5 — §IV "Heinrich Fisher matrix … leading-order linearization"
- **Location**: Page 8 §IV second paragraph: "applying the resulting σ(f_NL) ≈ 0.7 at the bounce-fiducial f_NL = −4.375 relies on the leading-order linearization that the Fisher matrix is approximately invariant under fiducial shifts of order the parameter uncertainty (a standard but non-trivial Fisher-forecast assumption). A re-derivation of the Heinrich Fisher matrix at the bounce-fiducial is a structural extension on the future work".
- **Problem**: The phrase "is a structural extension on the future work" triggers `/future-work-audit-paper` — this is a DO-NOW or SIMULATE-AUGMENT-NOW deferral risk. The σ(f_NL)=0.7 Fisher matrix could be linearly re-evaluated at f_NL = −4.375 trivially under the same assumptions; the text already admits the assumption is standard.
- **Required fix**: Replace "is a structural extension on the future work" with "would refine the present headline at the few-percent level; we adopt the leading-order assumption here because Fisher matrices for local-type f_NL are bias-parameter-dominated and weakly fiducial-dependent." Or simulate the re-evaluation now.

### P2-N8 — "84% ± 2% of the matter-bounce bispectrum amplitude"
- **Location**: Page 8 §III.B continuation: "A local-template estimator recovers 84% ± 2% of the matter-bounce bispectrum amplitude across all physically motivated weighting schemes."
- **Verification**: Matches r ∈ [0.829, 0.876] noise-weighted range with central 0.84 ± 0.02. All-clear.

## Pages 13-18 findings

### P2-N10 — §IX.D ρ=−0.87 degeneracy arithmetic
- **Location**: Page 18 §IX.D: "σ_unmarg(f_NL) = 1.53 due to a strong anti-correlated f_NL–n_fNL degeneracy (ρ = −0.87 fixed-bias, −0.97 bias-marginalized). With biases co-marginalized the n_fNL-fixed baseline is itself σ(f_NL) = 1.75 rather than 1.53, and the two-parameter identity σ_marg = σ_unmarg/√(1−ρ²) applied to that baseline reproduces the quoted value (1.75/√(1−0.9696²) = 7.06); the 4.6× factor above is referenced to the fixed-bias 1.53 for comparability with the fixed-bias column."
- **Verification**: 1.75/√(1−0.97²) = 7.199 ≈ 7.06 (paper says √(1−0.9696²) which uses ρ=0.9847; let me re-check: √(1−0.9696²)=√(0.0599)=0.2447; 1.75/0.2447=7.151 — close to 7.06 but off by ~1%); 1.53 × 1/√(1−0.87²) = 3.10 ≈ 3.08 (matches at quoted precision). The 0.9696 number in the paper is the *squared* correlation: ρ²=0.9696 → ρ=0.9847, but the prose says "−0.97 bias-marginalized." Confusion: is ρ=−0.97 or ρ²=0.9696?
- **Problem**: Inconsistency between ρ = −0.97 (prose) and √(1−0.9696²) in the formula (which would correspond to |ρ|=0.9847). If ρ=−0.97 then the formula should be √(1−0.97²) = √0.0591 = 0.2431, and 1.75/0.2431 = 7.20. The exponent on 0.9696 should be 1, not 2: √(1−0.9696) = √0.0304 = 0.1744, then 1.75/0.1744 = 10.03 — also doesn't match. Most likely the paper meant √(1−0.97²) and the "0.9696²" is a typo (should be "0.97²" giving 0.9409, and √(1−0.9409) = √0.0591 = 0.243; 1.75/0.243 = 7.20).
- **Required fix**: Replace "1.75/√(1−0.9696²) = 7.06" with "1.75/√(1−0.97²) ≈ 7.20" — and re-check whether the table/code emits 7.06 or 7.20. If 7.06, then ρ is not exactly −0.97 and prose should match the code value (e.g., ρ ≈ −0.971 or −0.969 explicitly).

### P2-N11 — detection significance 1.42σ and 0.62σ
- **Location**: Page 18 §IX.D: "the matter-bounce f_NL = −4.375 is detectable at only 1.4σ (fixed-bias) to 0.6σ (bias-marginalized) after marginalizing over n_fNL".
- **Verification**: |−4.375|/3.08 = 1.42 and |−4.375|/7.06 = 0.62. All-clear.

### P2-N12 — Planck PR4 0.75σ consistency
- **Location**: Page 16 §VIII.A: "f_NL^bounce = −0.1 ± 5.7, which is 0.75σ from the bounce prediction (|−4.375+0.1|/5.71)".
- **Verification**: 4.275/5.7 = 0.75. All-clear.

### P2-N13 — κ_ε bounds and prefactor scaling
- **Location**: Page 16 §VIII.B: "Explicit prefactor scaling alone gives κ_ε ≳ 5.6 (lower bound, holding mode functions fixed at ε = 3/2); the mode-function amplitude change adds a multiplicative correction at the singular point ε = 3/2 where the Hankel index diverges, which we bound schematically to ≈14× the prefactor-only value, giving κ_ε ≈ 80 as the upper endpoint."
- **Verification**: 80/5.6 = 14.29. All-clear.

### P2-N14 — Eq. (9) c' = κ_ε/8 ∈ [0.7, 10]
- **Location**: Page 17 Eq. (9): "c′ ≡ κ_ε/8 ∈ [0.7, 10]".
- **Verification**: 5.6/8 = 0.7; 80/8 = 10.0. All-clear.

### P2-N15 — κ_ε|Δε| = 0.36 ε-correction floor
- **Location**: Page 16 §VIII.B: "Even the conservative endpoint shifts f_NL by only κ_ε|Δε| ≈ 80 × 0.0045 ≈ 0.36".
- **Verification**: (1−0.9649)/8 = 0.00439 ≈ 0.0045; 80 × 0.0045 = 0.36. All-clear.

### P2-M3 — Table III "Corrected (10% residual)" row clarity
- **Location**: Page 15 Table III row 4 "Corrected (10% residual; = Ideal, verification only)^a".
- **Problem**: The table footnote a explains this row is identical to the Ideal row by construction at this template-overlap order, and "is included as a verification row, not as an independent configuration, and the two rows are not independent scenarios but rather bookend the same GR-free regime." This is honest, but the visual reader who looks at the table without footnote sees 4 rows of which 2 are numerically identical, which makes the table appear padded. The footnote helps but the row could just be deleted, OR the row should be visually de-emphasized (e.g., parenthesized headline, gray text in source not just italics).
- **Required fix**: Replace the "Corrected" row with a single inline note under the table: "Verification check: setting GR contamination to a 10% post-correction residual at this template-overlap order reproduces the Ideal row to within ΔBF < 0.1." Or keep the row but acknowledge in the caption that the table has 3 independent scenarios, not 4.

### P2-m6 — "structural extension on the future work" (also §IV)
- **Location**: Page 8 §IV (already flagged in P2-m5 above) AND page 17 §VIII.B "Narrowing this range requires evaluating all four cubic-action integrals simultaneously with numerically computed mode functions, preserving the cancellations that render the physical bispectrum finite."
- **Problem**: The §VIII.B sentence is also a future-work deferral (the §II.D-style admission that the κ_ε computation is incomplete). The text correctly bounds the impact ("by only κ_ε|Δε| ≈ 0.36 — well inside the recommended σ_theory = 1.0 bounce prior — so no Bayes-factor conclusion in Sec. VI hinges on the precise value"), so the deferral is acceptable, but the standing directive `/no-future-work-defer` says default class is DO-NOW. Since the impact is bounded and inside σ_theory, this is SIMULATE-AUGMENT-NOW / TRULY-BLOCKED edge case — explicitly state which.
- **Required fix**: Add one sentence: "This refinement is TRULY-BLOCKED in the present forecast scope because it requires a full four-vertex in-in computation that we validate against Cai et al. via cross-check rather than re-derive (Sec. II.D)."

### P2-M4 — Fig. 6 caption text "kills live lane"
- **Location**: Page 17 Fig. 6 caption: "dark red (legend label 'kills live lane') — measurement consistent with zero, disfavoring the quasi-dust matter bounce while remaining consistent with standard single-field inflation".
- **Problem**: "kills live lane" is informal jargon, unclear to a referee. The visible figure region in the image renders as "KILLS LIVE LANE" or similar — this is a developer-internal legend label that leaked into a publication figure caption.
- **Required fix**: Rename the legend label to "BOUNCE EXCLUDED" or "RULES OUT BOUNCE" and update caption accordingly.

### P2-N9 — degradation factors 1.14× / 1.20× / 1.21×
- **Location**: Page 8: "σ(f_NL) degradation factors are 1.14× (CMB Fisher), 1.20× (SPHEREx-like), and 1.21× (LSS/SDB)".
- **Verification**: 1/0.876 = 1.142, 1/0.835 = 1.198, 1/0.830 = 1.205, 1/0.829 = 1.206. Matches to two-figure precision. All-clear.

## Pages 19-24 findings

### P2-N16 — Eskilt 0.77σ and 0.766σ rounding
- **Location**: Page 19: "β_obs = 0.342° ± 0.094° at 0.77σ from the bounce prediction (where 0.77σ ≡ |0.342° − 0.27°|/0.094° = 0.072°/0.094° = 0.766σ, rounded to 0.77σ)".
- **Verification**: 0.072/0.094 = 0.766; rounds to 0.77. All-clear.

### P2-N17 — Table IV |f_NL|/σ ratios
- **Location**: Page 23 Table IV: "Cai et al.: 35/8 = 4.375 / 0.7 → 5.25σ; Li et al.: 35/16 = 2.1875 / 0.7 → 2.63σ".
- **Verification**: 4.375/0.7 = 6.25 — wait, but the table reports 5.25σ. Cross-check: the column "|f_NL| r/σ" — the post-r=0.84 template-corrected value: 4.375 × 0.84 / 0.7 = 5.25; and 2.1875 × 0.84 / 0.7 = 2.625 ≈ 2.63. All-clear.

### P2-N18 — τ_NL Suyama-Yamaguchi bound
- **Location**: Page 19: "τ_NL ≥ (6 f_NL/5)². The single-source / exact-local-template limit τ_NL = (36/25) f_NL² ≈ 27.56".
- **Verification**: (6/5)² × (35/8)² = (1.44)(19.14) = 27.56. All-clear.

### P2-m7 — Appendix A.2 Table IV "Li-Brandenberger row" reference
- **Location**: Page 22 A.2: "A reviewer who disputes the Cai convention should read the Li-Brandenberger row as the defensible lower bound".
- **Problem**: The Table IV row label is "Li et al. (single time-ordering)" but the prose calls it "Li-Brandenberger" — the bibliography entry [5] is Li, Quintin, Wang, Cai JCAP 03(2017)031, NOT Li-Brandenberger. Inconsistent vendor citation in the appendix prose.
- **Required fix**: Replace "Li-Brandenberger row" with "Li et al. row" in App. A.2 prose.

### P2-N19 — Wilson-Ewing prolonged-inflation citation [17]
- **Location**: Page 24 bibliography [17]: "M. Zhu and Y.-F. Cai, Smoking-gun signatures of bounce cosmology from echoes of relic gravitational waves, arXiv e-prints (2026), arXiv:2603.13924."
- **Verification**: Per calibration "arXiv 26xx valid for June 2026 current"; arXiv ID 2603.13924 fits June 2026 epoch. All-clear.

## Pass-2 self-critique

Cross-checked findings against `research/focused_paper_source_integration/02_full_draft.tex`:

- **WITHDRAWN — P2-N10 (ρ=0.969 vs 0.9696)**: The .tex source (line 631) reads `1.75/\sqrt{1-0.969^2}=7.06`, NOT `0.9696²`. I misread the PDF rendering at small font. 1.75/√(1−0.969²) = 7.08 ≈ 7.06 (matches within rounding). The prose ρ = −0.97 is a one-decimal round of −0.969, internally consistent. **DOWNGRADE** to a m-tier rounding nit (m-new): the formula uses 0.969 while the surrounding prose uses 0.97; either bump prose to "ρ = −0.969" or change formula to "1.75/√(1−0.97²) ≈ 7.20" with the table value updated correspondingly.
- **P2-m4 (Fig 2 "−35/8B")**: Cannot confirm against source `.png` from .tex alone (figure file is `fig2_survey_comparison.png`); caption text is correct in tex. **PARTIALLY WITHDRAWN** — flag as low-confidence visual-rendering nit pending png inspection; if rendering reads cleanly as "−35/8" in the rasterized PDF, ignore. Reduced confidence from m to low-m.
- **P2-M4 (kills live lane)**: CONFIRMED in tex line 623 — the legend label string is literally embedded. Stands.
- **P2-M2 (BF~17 vs Table II footnote)**: CONFIRMED — the abstract envelope text and Table II caption footnote conflict per .tex line 500. Stands.
- **P2-m5 (Fisher "structural extension on future work")**: CONFIRMED — the page-8 §IV phrasing "future work" triggers `/no-future-work-defer`. Stands.
- **P2-M1 (assumption d "robust" overclaim)**: CONFIRMED at line 343 — the "robust across bounce class" framing precedes the cubic-order caveat by many sentences. Stands.
- **P2-M3 (Table III padding row)**: CONFIRMED — the row "Corrected (10% residual; = Ideal, verification only)" is identical to the Ideal row by construction (caption admits it). Stands.
- **P2-m7 (Li-Brandenberger row)**: Stands per A.2 prose.

Updated P2-N10 → **P2-m8 (downgrade)**: rounding inconsistency between ρ = −0.97 (prose) and √(1−0.969²) (formula); pick one decimal precision and use it consistently.

## Explicit all-clears (with arithmetic)

| Item | Quote | Verification |
|---|---|---|
| Cai benchmark at squeezed | −4.375 | −35/8 = −4.375 ✓ |
| Cai benchmark at equilateral | −3.984 | −255/64 = −3.984375 ✓ |
| Cai benchmark at folded | −2.250 | −9/4 = −2.25 ✓ |
| Li single-time-ordering | −2.1875 | −35/16 = −2.1875 ✓ |
| Maldacena consistency | ≈ 0.015 | (5/12)(1−0.9649) = 0.01463 ✓ |
| Bounce-vs-inflation contrast | ≈ 290 | 4.375/0.015 = 291.67 ✓ |
| Sky-coverage degradation | ~19% | 1/√0.7 = 1.195 ✓ |
| Bayes Li position σ=0.5 | 4.375σ | 2.1875/0.5 = 4.375 ✓ |
| Bayes Li position σ=1.0 | 2.19σ | 2.1875/1.0 = 2.1875 ✓ |
| Bayes Li position σ=2.0 | 1.09σ | 2.1875/2.0 = 1.094 ✓ |
| ρ=−0.87 marg | σ_marg ≈ 3.08 | 1.53/√(1−0.87²) = 3.10 ✓ (close) |
| n_fNL marg detection | 1.4σ, 0.6σ | 4.375/3.08 = 1.42; 4.375/7.06 = 0.62 ✓ |
| Planck PR4 consistency | 0.75σ | 4.275/5.7 = 0.75 ✓ |
| κ_ε bounds | [5.6, 80], 14× | 80/5.6 = 14.3 ✓ |
| c' = κ_ε/8 | [0.7, 10] | 5.6/8 = 0.7; 80/8 = 10 ✓ |
| ε-shift bound | κ_ε|Δε| ≈ 0.36 | 80×0.0045 = 0.36 ✓ |
| Suyama-Yamaguchi limit | τ_NL ≈ 27.56 | (6×4.375/5)² = 27.56 ✓ |
| Eskilt rounding | 0.77σ | 0.072/0.094 = 0.766 → 0.77 ✓ |
| Table IV Cai significance | 5.25σ | 4.375 × 0.84 / 0.7 = 5.25 ✓ |
| Table IV Li significance | 2.63σ | 2.1875 × 0.84 / 0.7 = 2.625 ✓ |
| Local-amplitude recovery | 84% ± 2% | r ∈ [0.829, 0.876] noise-weighted ✓ |
| Degradation factors | 1.14×/1.20×/1.21× | 1/r = 1.14, 1.20, 1.21 ✓ |
| QSFI endpoints (per calibration) | μ/H=0 local, μ/H=3/2 suppressed | Confirmed per Chen-Wang Δ = 3/2 − √(9/4 − μ²/H²) ✓ |
| n_s formula | n_s = 1 + 12w → 0.964 | w = −0.003: 1 − 0.036 = 0.964 ✓ |

## Summary recommendation + counts line

**Recommendation**: Accept with minor revisions. The paper is arithmetically clean across 23 spot-checks; the §IX.D ρ-degeneracy is consistent at one-decimal precision once the .tex-source value 0.969 is recognized. The R24conf-edited regions (QSFI endpoints, Cai-Wang citation site, Table III with verification-row footnote, the −35/16 attribution to Li-Quintin-Wang-Cai) are now correct. Open items: M1 (assumption-d "robust" claim needs a forward-flag), M2 (abstract BF~10–17 envelope vs Table II footnote), M3 (Table III padding-row clarity), M4 (legend label "kills live lane" → publication-grade phrasing); plus m1–m8 minors and N16 normalization spot. All N-tier items are all-clears or notes.

**Counts: E:0 / M:4 / m:8 / N:19**

- **Location**: Abstract: "We quantify, for the first time to our knowledge, the template mismatch between the matter-bounce and local templates".
- **Problem**: "to our knowledge" hedge is acceptable, but Cai et al. [8] already quoted the squeezed-limit r=1 limit, so the *novel* element is the polynomial-coefficient null-space scatter ±0.13 and the injection-recovery validation, not the mismatch itself. The sentence as written can read as overclaim.
- **Required fix**: Tighten to "We quantify the polynomial-coefficient null-space contribution to the matter-bounce-vs-local template mismatch (±0.13 absolute scatter in r) for the first time to our knowledge". One word change.


