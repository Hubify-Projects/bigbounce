# INT Claude-subscription Review — P1U v1U.0.13 — claude-opus-4-8
paper: P1U  version: v1U.0.13  tex: arxiv/paper1_unified.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T15:03:00Z
context-note: FR1 fresh round on the July-11 restamped version (no content change since exit)

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've read the manuscript's core sections and independently recomputed the load-bearing numbers against the committed artifacts. Summary of verification:

- **R1 NJL suppression** (`arxiv/paper1_unified.tex:2618-2632`): recomputed — 100 cm⁻³ → 7.66×10⁻¹³ eV³; ρ_NJL = n²/M_Pl² = (7.66e-13)²/1.49e56 ≈ 3.9×10⁻⁸¹ eV⁴; /ρ_Λ(2.8e-11) ≈ 1.4×10⁻⁷⁰. ✓
- **R4 ALP** (`:3212-3233`): ρ_θ = 2m²β²/(α/M)² with m=1.5e-33 eV, β=6e-3, α/M=1e-30 eV⁻¹ → 1.62×10⁻¹⁰ eV⁴ ≈ 6ρ_Λ; matching point 0.41 H₀; overshoot 10²²/10³⁶. ✓
- **PTA** (`:4128`): (3.0−2.567)/0.382 = 1.13σ. ✓
- **LiteBIRD β** (`:4551`): 0.072/√(0.03²+0.094²)=0.73σ; 9σ=0.27/0.03. ✓
- **MCMC counts** (`:1578-1581`): 176,240+132,949=309,189; ×0.70=216,432. ✓
- **f_NL propagation**: companion P2 aux confirms full −35/8→−35/16 halving across all figures/tables (directive I6 satisfied).
- **Central transparency result** (`:3892-3907`): ε^{μνρσ}R_{μνρσ}=0 on Levi-Civita by algebraic Bianchi R_{μ[νρσ]}=0 — correct, correctly distinguished from the two-curvature Pontryagin density.
- Served PDF matches source (both 2,582,322 B, Jul 11 07:54); v1U.0.13 mirror current.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES:**

1. **[MINOR]** `arxiv/paper1_unified.tex:4123-4124` (and restated `:4548-4549`): The SPHEREx f_NL discriminator is presented as "σ(f_NL)≈0.7 … to ≈1.0 … yielding 1.3–2.75σ model separation." Taken at face value this invites the naive |f_NL|/σ reading, which gives |−35/16|/0.7 = 3.13σ down to /1.0 = 2.19σ — i.e. 2.2–3.1σ, **not** 1.3–2.75σ. The correct derivation (verified in the companion `research/focused_paper_source_integration/02_full_draft.aux`, Fig. 2) applies a template-overlap factor r=0.84 and an additive systematics budget; "1.3–2.75σ" is the *template-corrected, post-systematic-budget envelope*, not σ divided into f_NL. Paper 1 should state the r-factor and systematic-budget qualifier at the point of quotation so the number is not read as internally inconsistent with the σ(f_NL) it sits beside.

2. **[MINOR]** `arxiv/paper1_unified.tex:2583-2584`: R2 Planck suppression is quoted as "H₀/M_Pl ∼ 10⁻⁶⁰," but H₀=1.5×10⁻³³ eV over M_Pl=1.22×10²⁸ eV gives 1.2×10⁻⁶¹ (≈6×10⁻⁶¹ with the reduced M_Pl) — one order of magnitude smaller. The ≳30-order closure margin is unaffected, but the stated exponent should read ∼10⁻⁶¹ for consistency with the numbers used elsewhere (e.g. the R3 propagation at `:3060` correctly uses H/M_Pl ≈ 1.2×10⁻⁶¹ to get 3×10⁻⁶²).

3. **[MINOR]** `arxiv/paper1_unified.tex:3037-3042`: The R3 GUT-to-IR lever arm is given as "ln(μ_GUT/μ_IR)≈30–35" for μ_GUT∼10¹⁶ GeV, μ_IR∼1 GeV, but ln(10¹⁶)=36.8, which lies above the stated range (and pushes the representative 32/(12π²)≈0.27 estimate). Since this is explicitly a conservative upper-bound ansatz with ≳60 orders of margin, the closure is untouched, but the interval should bracket the actual value (~37).

4. **[MINOR — editorial]** `arxiv/paper1_unified.tex:1201-1330`: The abstract (~130 lines) and the "Scope" apparatus (`:2438-2533`) restate the same scope caveats — "channel-level, not operator-level"; "single-scale NDA, not a first-principles derivation"; "R4 is naturalness, not amplitude" — many times over. For PRD this is well past house length and readability norms; the defensive repetition should be consolidated to one clear scope statement. This does not affect correctness but a PRD editor will require condensation.

5. **[MINOR]** Title/abstract framing (`:1214-1218`, closure at `:3217-3222`): the title's "amplitude closure" strictly covers only R1–R3; the paper itself shows R4 with a *floated* coupling **reproduces both β_obs and ρ_Λ** and is closed only by an explanatory-deficit/naturalness argument. This is disclosed honestly and repeatedly, but the reader is asked to hold "closure" and "R4 technically reproduces the dark-energy density" simultaneously; a one-clause title/abstract qualifier ("amplitude closure of R1–R3; R4 by naturalness") would remove the residual tension.

**(3)** Yes — the central claim (a channel-level, assumption-conditional constraint on the four enumerated minimal-ECH dark-energy routes, anchored by the exact Bianchi-vanishing perturbation-transparency result) is supported: every load-bearing number recomputes correctly against the committed artifacts and the core identities are mathematically sound; the remaining issues are presentational/normalization clarifications, not defects in the result.
