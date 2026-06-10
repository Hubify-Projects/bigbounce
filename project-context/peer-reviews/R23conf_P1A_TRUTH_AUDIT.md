# R23conf P1A — TRUTH AUDIT (META-REVIEW + SYNTHESIS)

**Auditor**: Claude (in-session) · **Date**: 2026-06-09 · **Target**: `arxiv/paper1a_ech_nogo.tex` (post-INSESSION closures)
**Scope**: all META_REVIEW findings + remaining SYNTHESIS consensus groups. INSESSION findings (m1, m3, m4+m6, m5, m7) already closed — not re-audited.

## META-REVIEW findings

| ID | Sev | Verdict | Evidence / arithmetic | Disposition |
|----|-----|---------|----------------------|-------------|
| META-E1 | E | **VERIFIED** | Paper adopts `−¼(α/M)θFF̃` (L1158) but used β=(α/M)Δθ. Standard small-rotation result for that normalization is β=(α/2M)Δθ (Harari–Sikivie). Inversion becomes ρθ=2mθ²β²/(α/M)². Recompute: 2·(1.5e-33)²·(6e-3)²/(1e-30)² = 1.62e-10 eV⁴ = 5.8 ρΛ (ρΛ=(2.3 meV)⁴=2.8e-11) — reviewer's "~6× over ρΛ" confirmed. Matching point shifts to mθ≈0.42 H₀. Endpoint overshoots (~22/~36 OOM) unchanged at OOM level. Supersedes INSESSION-m1 arithmetic (4.0e-11). R4 closure logic (naturalness, not amplitude) unaffected; "within a factor of unity" honestly weakened to "within an order of magnitude (≈6ρΛ)". | CLOSED — Eq. `eq:beta_bound` + inversion + ρθ value + matching-point parenthetical edited |
| META-E2 | E | **PARTIAL** | Current .tex (L1610) already reads `h''+2𝓗h'+k²h=0` with conformal `\mathcal{H}` — NOT cosmic H as reviewer read from PDF rendering. However primes/𝓗 were never defined → ambiguity real. | CLOSED — added "(primes = d/dη, 𝓗≡a′/a; cosmic-time form ḧ+3Hḣ+(k²/a²)h=0)" |
| META-M1 | M | **VERIFIED** | θ used for both NY pseudoscalar (Eq. oneloop_parity_odd) and spectator ALP (Eq. beta_bound). Real collision. | CLOSED — NY field renamed ϑ_NY (3 occurrences) + explicit no-identification clause |
| META-M2 | M | **VERIFIED** | Closure summary pointed condensate "quantitative closure" at `\ref{sec:transparency}` (Sec. X, perturbation transparency); actual NJL quantitative closure lives in `sec:r1_njl` (Sec. IV A). | CLOSED — cross-ref corrected to `sec:r1_njl` |
| META-M3 | M | **VERIFIED** | No θ(t)-regime statement existed near Eq. beta_bound. Physics check: rotation depends only on endpoints θ(today)−θ(rec); mθ≲H₀ frozen/slow-roll → monotonic; mθ≫H₀ oscillation redshift-dilutes amplitude (ρθ∝a⁻³) → suppresses β at fixed ρθ → larger ρθ needed → overshoot conclusion conservative. | CLOSED — regime sentence added at Eq. beta_bound |
| META-M4 | M | **STALE** | L696–708 already label 0.27 ρPl as "internal extrapolation across counting schemes (not a value quoted in Ashtekar–Singh)" and the 0.27–0.41 window as scheme-dependent (reviewer option ii). Barrier 12 propagates the full window: 0.27²–0.41² = 0.073–0.168 ✓ matches stated 0.07–0.17. | No edit |
| META-M5 | M | **VERIFIED** (minor) | Eq. ClEB retains C_BB but regime unstated. Paper performs NO independent EB β-fit (values quoted from Minami2020/Eskilt2022 estimators, which retain lensing BB). | CLOSED — small-angle/uniform-β regime + C_BB sentence added after Eq. ClEB |
| META-m1 | m | **VERIFIED** | "M_crit ≈ 10⁻³ M⊙" (L683) had no derivation/citation anywhere in repo; deriving one now would be fabrication (pattern-036). Reviewer's delete option taken. Same as OpenAI-M4. | CLOSED — sentence deleted; no other M_crit refs remain |
| META-m2 | m | **VERIFIED** (minor) | Identity e∧e∧R = −NY + T∧T correct given NY≡d(e∧T) (=T∧T−e∧e∧R), but boundary-term definition was unstated. At T=0: NY=d(0)=0 pointwise ✓, Bianchi gives pointwise vanishing ✓. | CLOSED — NY≡d(e_I∧T^I) definition + pointwise-vs-boundary clause added (Sec. X D body; not a \caption/\footnote edit) |
| META-m3 | m | **STALE** | Footnote at eq:beta_bound already contains the unit-consistent worked example: g_naive = α_em/(2π·1.2e19 GeV) = 9.5e-23 ≈ 1e-22 GeV⁻¹ vs fitted 1e-21 → 10× gap demonstrated with explicit γ_SU(2), M_area-gap, f_a, c_γ. E1's factor-2 shifts fitted α/M by 2 (OOM-stable, "~10⁻²¹" unchanged). | No edit |
| META-n1 | n | **VERIFIED** (nit) | `\widetilde{R}(Γ̊)` for Holst dual collided with `R∧R̃` Pontryagin notation (rendered "Re(Γ̊)" in PDF). Single occurrence. | CLOSED — renamed `\mathcal{R}_{\rm H}(Γ̊) ≡ ½ε^{μνρσ}R_{μνρσ}` |
| META "REJECT" rec | — | **HOUSTON-DECISION** | Overall recommendation aggregates companion-reliance + scope opinions; technical items now closed/queued. | Noted for Houston |

## SYNTHESIS consensus groups (non-INSESSION remainder)

| Group / ID | Sev | Verdict | Evidence | Disposition |
|------------|-----|---------|----------|-------------|
| audit_artifact / Grok-M2 (enumeration circular) | M | **STALE** | Scope paragraph (L943–962) explicitly discloses omitted dim-6 operators (Jackiw–Pi, parity-odd 4-fermion partner) as NOT closed; channel-level framing already adopted (R-multi GRO-M1 precedent). | No edit |
| audit_artifact / OpenAI-E4 (one-loop ratio) | E | **PARTIAL** | Displayed formula internally consistent: 10⁻³·10⁻⁶¹/(10⁻²·6e-3) = 1.7e-60 ✓ → 10⁻⁵⁸–10⁻⁶⁰ with the now-defined ε-correction (INSESSION m4). Reviewer's 10⁻⁶² estimate omits the R4-fitted M_Pl(α/M)~10⁻² denominator the text states. Deeper first-principles derivation of the normalization remains open → queue. | Queued (COMPUTE_QUEUE #1) |
| audit_artifact / OpenAI-M1 (NJL numeric bound) | M | **VERIFIED** | No number existed. Recomputed: n_b(z=1100) = 2.47e-7·1101³ = 330 cm⁻³ = 2.5e-12 eV³; ρ_NJL = n²/M_Pl² = 4.3e-80 eV⁴ = 1.5e-69 ρΛ. | CLOSED — numeric bound inserted in sec:r1_njl |
| audit_artifact / OpenAI-M2 (Δγ/γ underived) | M | **STALE** | L1120–1131 already reframe Eq. gamma_running as "chiral-count EFT bound, not full perturbative result" + cite Benedetti & Speziale — reviewer's "weaken to dimensional upper bound" option already on disk. | No edit |
| companion / Grok-E4, Grok-M1, Grok-m1 | E/M/m | **HOUSTON-DECISION** | Companion refs are deliberate TODO-SUBMISSION placeholders ("posted concurrently on arXiv"); fNL=−35/8 + β central value imports are the declared program structure. Per standing rule, companion-reliance demands go to Houston. (companion/Claude-m7 already CLOSED in-session.) | Noted |
| table_ii / Claude-N2 (13 vs 14 wording) | N | **STALE** | "13 logically-independent (14 historical catalog entries, B8 subsumed by B14)" now standard from abstract → conclusion → Table II caption (12+ sites). | No edit |
| table_ii / OpenAI-E6 (independence proofs) | E | **PARTIAL** | B8/B14 non-independence disclosed everywhere; remaining 13 have no dependency matrix. Constructing one is a real derivation artifact, not a text patch. | Queued (COMPUTE_QUEUE #2) |
| table_ii / OpenAI-M7 (PTA line + w₀wₐ chain-status footnote) | M | **HOUSTON-DECISION** | Footnote (L~1689) is deliberate work-in-progress disclosure; removal = disclosure-removal demand → Houston per standing rule. PTA γ row sourced from companion real-KDE reanalysis. | Noted |
| OpenAI-E9 (version-history/correction notes in body) | E | **HOUSTON-DECISION** | Correction-note/disclosure-removal demand by definition (p.2 footnote, Sec. X footnote 3 are deliberate erratum-transparency). | Noted |
| OpenAI-E5 (companion arXiv IDs) | E | **HOUSTON-DECISION** | Same companion-placeholder policy as Grok-E4. | Noted |
| OpenAI-M9 (condense to 12–14 pp) | M | **OPINION** | Length/scope judgment; PRD has no hard page cap for regular articles. | No edit |
| OpenAI-n3 (AI acknowledgment) | n | **OPINION** | Permissible per reviewer himself. Bonus: n3's scalar audit independently CONFIRMS paper numbers (ρcrit 0.27/0.41 ✓, ω/H bound ✓, β significances 3.64σ/2.90σ ✓). | No edit |

**Counts**: 23 audited → 9 VERIFIED (all closed), 3 PARTIAL (2 closed-in-part, 2 queued), 5 STALE, 2 OPINION, 5 HOUSTON-DECISION, 0 FALSIFIED (no future-date or Perplexity-citation findings in scope; Perplexity returned 0 findings this round).
