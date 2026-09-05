# A3M v3M.0.17 — R8 truth-audit (skeptical, 2026-09-04)

**Plan header.** Auditor given no expected outcome. Exact artifact bound: sha256
`5ada0172…`, md5 `b18aafd1…`, 18 pp; source-dir `research/track_a3_multichannel/paper/main.pdf`
== served `site/public/papers/a3_multichannel_arxiv_v3M.0.17.pdf` (md5 verified identical).
Legs: Grok_brutal (REJECT), Gemini_cosmology (MAJOR REVISIONS), Claude Fable 5.1 INT
(MAJOR REVISIONS, 4M/12m/4Q). No leg raw contains "Reviewer call FAILED" (grep clean).
Board: `A3M_v3M.0.17_R8_BOARD_2026-09-04.md`; receipt dir
`ROUND_2026-09-04-A3M-v3M.0.17-EXACTPDF-5ada0172-R8VERIFY/`.

Method (patterns 061–066, directive H-refined): fingerprint every finding; class
(a) genuinely-new-real · (b) re-flag-of-already-addressed · (c) falsified ·
(d) opinion/genre/venue · (e) disclosed-limitation/out-of-scope. Prior canonical:
`../DISPOSITIONS/A3M.md` and `A3M_v3M.0.15_R7_TRUTH_AUDIT_2026-09-04.md`.
Physics verification targets: Δf_NL^bounce(c_s) = −(5/24)ρ_B(6c_s²−5)/c_s⁴ closed form;
r = 24c_s vs r_after = 24 identity at c_s = 1; the S2 statements; against
`research/cubic_bounce_transmission/row18a_*`, `row18b_*`, `row14_cs_window`, `row15_*`
notes + results.json, `research/theory_audit/curvaton_matter_bounce_adjudication_2026_09_04.md`,
`psu_gates_S1_S2_2026_09_04.md`.

*(sections appended below as the audit proceeds)*

---

## Per-leg counts (fingerprinted)

| leg | verdict | raw findings | (a) new-real | (b) re-flag/residual | (c) falsified | (d) opinion/genre | (e) disclosed |
|---|---|---|---|---|---|---|---|
| Grok_brutal | REJECT | 14 | 0 | 2 | 6 | 6 | 0 |
| Gemini_cosmology | MAJOR REVISIONS | 6 | 4 | 1 | 0 | 1 | 0 |
| Fable INT | MAJOR REVISIONS | 20 (4M/12m/4Q) | 12 | 3 | 0 | 1 | 4 (Q1–Q4 → ledger) |
| **canonical union** | — | **40 raw → 27 distinct** | **15** (2 MAJOR + 1 MAJOR-lite + 12 minor) | **4** | **6** | **7** | **4** |

## Physics verification (own algebra + committed artifacts)

- **Closed form.** `row18b_cs_bounce_cubic/results.json` model string:
  `f_NL^after(c_s) = T(−165/16 + 65/(8c_s²)) + Δ₁(6c_s²−5)/c_s⁴`, `Δ₁ = Δf^bounce(c_s=1)`
  = −0.139818 / −0.104311 / −0.127111 (Quintin/LQC/poly), V2-dominated 99.97%.
  Independent check: `Δ₁ = −(5/24)ρ_B` with `ρ_B = 1 − 2T` gives −0.13958 / −0.10417 / −0.12688
  for `T` = 0.16501 / 0.25000 / 0.19550 — the analytic closed form
  `Δf^bounce(c_s) = −(5/24)ρ_B(6c_s²−5)/c_s⁴` reproduces the numerically integrated `Δ₁` to
  ≤0.2% on all three backgrounds. The `(6c_s²−5)/c_s⁴` factor follows from the `P(X,φ)` `ζζ̇²`
  coefficient `a³(ε/c_s⁴)(ε−3+3c_s²)` at `ε_eff = 1/2`. **CONFIRMED.**
- **`c_s = 1` gate.** `gate_cs1` rel_diff to the lane-(b) totals = 3.3e−6 / 3.2e−6 / 3.9e−6.
  **CONFIRMED** (no tuning).
- **`r = 24c_s` vs `r_after = 24`.** `r = 16ε c_s^{2ν−2}`, dust `ν = 3/2` → `r = 24c_s`; at
  `c_s = 1` this equals the S1 identity `r_after = 24`. `row18a_s2_tensor/results.json`:
  `r_after_S1 = 23.99999999999937`, `λ_T/λ_ζ^S1 − 1 = −1.3e−14` at `kη_B = 10⁻³`.
  **CONFIRMED, and the R7 (ii) item `A3-S2r` is now closed by a committed artifact.**
- **S2.** `lam_zeta_S2 = 0.96958`, `lam_T = 6.05860` → `r_after_S2 = 937.11`; the paper's
  `≈9.4×10²` and "39× amplification" are exactly this row, no longer a hand ratio.
  **CONFIRMED.**
- **Window.** `cs_min = 0.599665 → r_min = 14.392` (Quintin), 0.60642/14.554 (LQC),
  0.60204/14.449 (poly); `c_s = 1.5×10⁻³ → f_after = 1.38×10¹¹` (Quintin), `1.03×10¹¹` (LQC).
  Abstract's `1.0–1.4×10¹¹`, `c_s ≥ 0.60`, `r ≥ 14.4` all trace. **CONFIRMED.**
- **Appendix A map — FAILS.** `main.tex:1639–1641` prints
  `f_{δN_c} = f^{in-in}/λ + f_map`, `λ = 1 − ε/3`, `f_map = −5ε/4 + (5ε/4)μ²`, and calls it
  "an isotropic monopole of exactly −5 for every constant ε". At `ε = 3/2`:
  `f^{in-in}/λ = 2(−35/16 + (15/16)μ²) = −35/8 + (15/8)μ²`; `f_map = −15/8 + (15/8)μ²`;
  sum `= −25/4 + (15/4)μ²`, which is the **final-label** value the same paragraph quotes at
  `:1652`, not −5, and is not isotropic. The initial-label map must be
  `−5/8 − (15/8)μ²` at `ε = 3/2`. Fable M2 is correct — see `R8-02`.
