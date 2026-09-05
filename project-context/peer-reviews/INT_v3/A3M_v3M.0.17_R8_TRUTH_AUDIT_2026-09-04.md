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

## (a) GENUINELY-NEW-REAL — canonical list (15)

**`R8-01` MAJOR — the `k`-essence no-go silently assumes `λ = 0` (and `s = 0`, `η_sr = 0`).**
[Fable M1] `row18b_cs_bounce_cubic.py` docstring lines 20–22 and `results.json.scheme`
("S1 (geometric, z = a, eps_eff = 1/2, eta_sr = 0, s = 0, lambda = 0; c_s retained)") state the
assumption; `grep` of `main.tex` finds **no** statement of it anywhere, while the abstract
(`:63–65`) concludes "the single-field matter bounce, canonical or `k`-essence, is jointly
excluded". A general `P(X,φ)` carries a free `λ` (the `P_XXX` coefficient) multiplying the same
`ζ̇³` kernel. REAL disclosure gap, not an arithmetic error.

**`R8-02` MAJOR — Appendix A prints the final-label map as the initial-label one.**
[Fable M2] `main.tex:1639–1641` (verified independently above). The paper's own "label-resolved"
reconciliation of `δN_c = −5` with the in-in `−15/8 + (15/16)μ²` does not close as printed.
Correctable by printing both maps; §II D and the Scope statement lean on it, so the fix
propagates.

**`R8-03` MAJOR-lite — `Υ` and `Δt_B` used undefined.** [Gemini M1] `main.tex:435–436`
("evaluated for this program's `Υ` and `Δt_B`, the required amplification factor is exactly 1");
neither symbol is defined nor given a value anywhere in the paper. Breaks standalone readability
of a load-bearing claim.

**minor (12):**

| id | item | evidence |
|---|---|---|
| `R8-04` | `[S]` row "0 (suppressed)" has no scaling or bound | `main.tex:1610` [Gemini M2] |
| `R8-05` | "committed, at the current HEAD" is a moving pointer | `main.tex:1706` [Gemini E2a, Fable m11] |
| `R8-06` | Eq. (12) displays `1.732±0.050` while the abstract headlines `1.84±0.03` | `:924` vs `:74`, `:976` [Fable m4] |
| `R8-07` | "`|f_after| ≤ 5.1` (Planck 1σ)" is not Planck's 68% interval (`−0.9 ± 5.1` → `[−6.0, +4.2]`); the `c_s = 0.6` value is **positive** (+5.08) | `:60`, `:1358` [Fable m2] |
| `R8-08` | cross-reference error: "§V B's `T_B ≳ 10⁸` GeV" — the condition is §V C, `6×10⁹–6×10¹⁰` GeV | [Fable m3] |
| `R8-09` | three distinct quantities named `r` (tensor ratio, mode-mixing `r`, bispectrum shape overlap) | Secs. III, VI, VII–VIII [Fable m1] |
| `R8-10` | curvaton range "+9.30 to −1.25" ↔ `r_dec ∈ [0.113, 1]`; lower limit unstated | [Fable m5] |
| `R8-11` | Ref. [4] cited as "Li et al. 2017" and "Li et al. (2016)" | abstract/§IX A vs §VIII, Table VII [Fable m6] |
| `R8-12` | Table IV row labelled "Matter bounce, γ = 3" although `:740`/`:773` establish γ=3 is borrowed, not this model's prediction | `:684` [Fable m10] |
| `R8-13` | §II D and Appendix A restate the Bianchi-I argument nearly verbatim | [Fable m9] |
| `R8-14` | Fig. 1 axis/legend text small at column width; NANOGrav band and the two predicted lines unlabelled | [Fable m12] |
| `R8-15` | §IX A juxtaposition `0.5–1.1σ` vs `3.13σ` lacks an explicit "not directly comparable" tag (the existing "a naive reading … would suggest" is weaker than the tag used at `:516`, `:665`) | `:1483–1487` [Gemini E3] |

## (b) RE-FLAG / RESIDUAL of an open canonical disposition (4) — real, but not genuinely-new

- **`DA3M-06` residual (MAJOR, still open).** [Fable M3] `main.tex:790–791` still carries
  "the unresolved `r = 0.84` matter-bounce scenario (open item, not adopted) … resolving `r` for
  these backgrounds is an open item (Sec. IX)", contradicting `:1292` ("a tensor-sense `r = 0.84`
  is not used here: it traces to the noise-weighted bispectrum shape-overlap coefficient of
  Sec. VI") and the `r = 24` identity of Sec. VII. §IX C lists no such open item, so the
  cross-reference dangles. Fingerprint matches `DISPOSITIONS/A3M.md § DA3M-06`. **Must close in
  v3M.0.18** — it is the paper's only surviving internal contradiction on its headline quantity.
- **`DA3M-08` residual (MAJOR — presentation, both external legs rank it ESSENTIAL).**
  [Gemini E1, Fable m7] 14 hits of ledger/round jargon remain in body prose and captions
  (`row18a`, `row18b`, `row14_`, "ledger row", `LEDGER4_RESULT_v3_…`, `r5_15`, `r11_pbh`,
  `D-A3-9`, `lane9c2`). Fingerprint matches `DA3M-08`. **Must close in v3M.0.18.**
- **`DA3M-01` re-flag (not real as stated).** [Grok E2] Table IV's caption (`:658–665`) already
  declares the official posterior the *primary* comparison and the 30-bin refit a "secondary,
  differently-conditioned cross-check, **not directly comparable to it**". The abstract quotes the
  declared primary statistic, which is the paper's own stated convention, not the
  more-favourable of two comparable numbers.
- **`DA3M-04` re-flag (already disclosed).** [Grok E3] Table V daggers the non-perturbative rows,
  its footnote reads "†non-perturbative: `f_PBH > 1` uncapped" (`:1002`), and `:976–983` state
  explicitly that `1.732 ± 0.050` "must not be quoted as" the headline while the abstract's
  `1.84 ± 0.03` is the shape-resolved, `γ_cr`-covered value. The perturbativity cut is applied,
  not ignored. (The residual editorial mismatch is logged separately as `R8-06`.)

## (c) FALSIFIED against source (6)

- **Grok E1** ("no explicit statement that S1 and S2 are not directly comparable"): FALSE.
  Abstract `:41–42` — "Transmission through the bounce is **scheme-qualified**: S1 gives …,
  S2 gives …"; body `:516` — S2 "is a different continuation and **is not directly comparable to
  the S1 rows above it**".
- **Grok M2** ("S2 diverges or requires an ad-hoc cutoff"): FALSE. S2 is the raw-ADM continuation
  with `|λ_ζ| = 0.97` (`row18a_s2_tensor/results.json:lam_zeta_S2 = 0.96958`); no cutoff appears
  in the S2 lane. Same falsification as E1 for the "symmetric" charge.
- **Grok M3** ("recovered central value shifts to `−2.2 ± 2.5`"): misquotes the paper. `:1162`
  reports `f_NL^local = −2.2 ± 25` — the error bar is ~2.8× the published `+9.0/−9.1`, which is
  why the paper labels the reproduction consistent but **under-powered**, exactly the assessment
  Grok says is missing.
- **Grok M4** ("effect-size information is missing"): FALSE. The amplitude ratio between the two
  candidates *is* the effect size and is the abstract's headline (`1.84 ± 0.03`, `:74`), tabulated
  at `:976` and `:1073`.
- **Grok E4** ("the no-go is presented as background-independent"): FALSE. The abstract scopes it
  "on the backgrounds and channels evaluated here" (`:63–65`), and Eq. (16)/Table VII are computed
  on **all three** backgrounds (`row18b …/results.json` → `quintin`, `lqc`, `poly` blocks). Eq. (17)
  is the surviving-route curvaton sketch, not a premise of the no-go.
- **Grok m1** ("future date September 4, 2026 … inconsistent with a 2024–2025 submission cycle"):
  the date is the true compile date; the reviewer's assumed submission cycle is not a paper fact.

## (d) OPINION / GENRE / VENUE (7)

Grok M1 (18 pp → "should be a 6–8 page letter"); Grok m2 (Table II caption phrasing); Grok m3
(restate `ε = 3/2` on every page); Grok's three nits ("Quintin-type" vs "Quintin et al. [3]",
figure-axis units, one missing journal ref — the last is worth a free fix); Gemini N1
(the honesty-grading sentence in §I is "overly conversational"). None is a defect in the science.

## (e) DISCLOSED LIMITATION / OUT OF SCOPE (4)

- **Gemini E2b** (no frozen-release DOI): the paper says so itself at `:1752` and assigns it to the
  packaging stage. Real for a journal submission, out of scope for the current arXiv-track state;
  it is a P-round action, not a v3M.0.18 text edit.
- **Fable m8** (`Ω_DM = 0.674` transcription from [16]): `:1029–1039` already footnotes the
  transcription, gives the correct `≈0.264`, states the ratio is independent of it, and quantifies
  the `2.55×` rescaling of the tabulated `f_PBH`. Disclosed, not a defect.
- **Fable Q1–Q4**: referee questions, routed to the ledger (below), not paper defects.
