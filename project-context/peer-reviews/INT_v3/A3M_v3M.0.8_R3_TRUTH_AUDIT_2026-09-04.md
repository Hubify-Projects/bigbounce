# A3M v3M.0.8 — R3 truth audit (independent, verdict-first)

- **Round:** `ROUND_2026-09-04-A3M-v3M.0.8-EXACTPDF-8cf429e0-R3`
- **Manuscript:** `research/track_a3_multichannel/paper/main.tex` + `main.pdf`, v3M.0.8, 10 pp
- **sha256 (re-verified this session):** `8cf429e002d44c97308ccc994c9378a93b066e094de865d48f850d5e72291b9a`
  — matches every leg header **and** the served mirror `site/public/papers/a3_multichannel_arxiv_v3M.0.8.pdf` byte-for-byte.
- **Board:** `INT_v3/A3M_v3M.0.8_R3_BOARD_2026-09-04.md`
- **Auditor:** Opus, skeptical in both directions. Every verdict below is decided from a
  source — the `.tex` line, the committed script, the committed JSON, a literature value, or
  the auditor's own re-execution — never from a leg's verdict word and never by assertion.
- **Protocol:** `/peer-review-truth-audit` + `/bigbounce-truth-audit`, patterns 061–066,
  directive H-refined. Canonical ledger: `project-context/peer-reviews/DISPOSITIONS/A3M.md`.

---

## 0. Independent verification performed by this auditor

Nothing in §2 is graded on a reviewer's say-so. This is what was actually executed or read.

| Object | Command / source | Result |
|---|---|---|
| PDF binding | `shasum -a 256` on source PDF + served mirror | both `8cf429e0…1b9a` ✓ |
| Receipt integrity | `preflight_receipt.json` | `verdict: PASS`, HEAD `8d5ca7c8`, no `Reviewer call FAILED` in `api_legs_run.log` ✓ |
| **kη_B window direction** | `research/cubic_bounce_transmission/lane_b_numerical/LANE_B_NUMERICAL_2026-09-03.md:107–111, 152` | validity band is `kη_B ≲ 10⁻²` with rows flagged invalid for **`kη_* > 0.3`** — an **upper bound on k**. There is no long-wavelength (small-k) cutoff anywhere in the lane-B note. |
| Comoving horizon at BBN | auditor computation: `aH ∝ 1/a ∝ T` in RD, anchored at `k_eq ≈ 0.01 Mpc⁻¹` at `T ≈ 0.8 eV` | `a_B H_B(1 MeV) ≈ 1.2×10⁴ Mpc⁻¹` ⇒ `kη_B ≲ 10⁻²` admits only `k ≲ 10² Mpc⁻¹`. Covering `k ~ 10¹⁵–10¹⁶ Mpc⁻¹` (a 10¹⁵ g PBH) needs `a_B H_B ≳ 10¹⁷–10¹⁸ Mpc⁻¹`, i.e. **`T_B ≳ 10⁸–10¹⁰ GeV`**. |
| Post-transmission LSS reach | auditor arithmetic from `main.tex:363–370` table | `f_NL^after(−35/16) ∈ [−0.65,−0.50]`; propagating `−35/8` through the same `T` and `Δf_NL^bounce` gives `[−1.20,−0.86]`. Bare SPHEREx (σ=0.7): **0.7–0.9σ** and **1.2–1.7σ**; separation `|Δf_NL| ≈ 0.35–0.55` against σ=0.5–0.7 ⇒ **< 1σ discrimination**. |
| Eq. (7) / `ρ_B` | `main.tex:353, 363–370` vs `T=(1−ρ)/2` | `ρ_B = 1−2T` reproduces all three rows exactly: `T=0.165→ρ_B=0.670→Δ=−0.1396` (paper −0.140); `0.250→0.500→−0.10417` (−0.104); `0.1955→0.609→−0.1269` (−0.127) ✓. Also `f_NL^after = −(85/48)T − 5/24` reproduces −0.651 at T=0.25 ✓ |
| "28–39 %" | `LANE_B_NUMERICAL_2026-09-03.md:125–128` ratios | `0.13982/0.360949 = 0.387`; `0.10431/0.546875 = 0.191`; `0.12711/0.427659 = 0.297` ⇒ **19–39 %**, not 28–39 %. The source note carries the same error. |
| `T` interval | `main.tex:315–318` | text states `T=(1−ρ)/2` with `ρ∈(0,1]` and then `0<T≤1/2`. Directly: `ρ=1⇒T=0`, `ρ→0⁺⇒T→1/2⁻` ⇒ **`T ∈ [0, 1/2)`**. Both endpoints inverted. |
| `n_s−1` formula | `main.tex:743`; `inlab_delta2_zeta_2026-09-03.py:24` | both print `n_s−1 = 12w/(1+w)`. Standard contracting-phase result (Wands 1999; Cai et al. 2009) is **`12w/(1+3w)`**. Numerically inert here: `n_s−1=−0.0351` gives `w=−0.00293` vs `−0.00290`. |
| Ω_DM footnote | `main.tex:716–726`; auditor re-ran `pbh_compaction_fnl.py` | footnote claims "every result in this section is unaffected". **False for Table III/Fig. 1.** Re-solving the Gaussian calibration at `Ω_DM=0.264`: `A_* : 0.131446 → 0.127901` (**−2.70 %**), and `f_PBH(−35/16) : 3.6×10⁻¹⁴ → 6.3×10⁻¹⁵`, `f_PBH(−35/8) : 1.6×10⁻² → 5.7×10⁻³`. The **ratio** is unaffected, exactly as claimed; the tabulated `f_PBH` column is not. |
| Injection pull scatter | `outputs/pta_injection_30bin_realkde_2026_09_02.json → summary` | `13/3`: mean pull `+0.0155`, **std `0.0993`** (5 realizations ⇒ SEM `0.044`); `3.0`: mean `+0.0326`, **std `0.1203`** (SEM `0.054`). Paper quotes only the means. |
| μ / isosceles | `main.tex:157–200` (Eq. 2, k₂=k₃) vs Eq. (4); `research/theory_audit/fnl_monopole_adjudication_2026_09_03.md:41` | the lab's own note states "Same μ definition throughout (μ = k̂_L·k̂_S); **isoceles μ=0**". So the μ²-dependent Eq. (4) is not the exact-isosceles configuration. |
| δN_c derivation status | `fnl_monopole_adjudication_2026_09_03.md:25, 39, 57, 72, 76` | note says `δN_c/ζ_Mald = 1−ε/3` is "**asserted**"; the second-order piece is "recorded as an exact identity, **mechanism not derived**"; and the note's own summary is "the δN discrepancy **explained at the equation level** rather than reconciled away". The paper (`main.tex:277–285`) escalates this to "a **derived identity** rather than an unresolved discrepancy". |
| δN gap arithmetic | auditor | a pure linear rescale `ζ→λζ` maps `f_NL→f_NL/λ`, so `δN_c=½ζ` would give `2×(−15/8) = −15/4`, **not** `−5`. Gap ratio is `8/3`, not 2 ⇒ Eq. (5) alone cannot account for the gap; the note's own decomposition `25/8 = 5/4 ([X]) + 15/8 ([L]−δN_c)` confirms Eq. (5) supplies only the linear-order half. |
| Abstract vs §II D wording | `main.tex:44` vs `238–241` | abstract: "A classical, **gradient-expansion** route"; §II D: "the **gradient-expansion assumption** `N_i=O(∇)` … **fails** here". Direct self-contradiction. |
| Induced-GW IR slope | `main.tex:417–418, 545–547`; `pta_gamma_reproduce.py:22–31` | the `γ=3 ↔ Ω_GW∝f²` identification is **cited** to Papanikolaou 2025 (arXiv:2504.11641) as a matter-bounce SIGW result — that part is sourced. The defect is the **generality** claim at `545–547` ("the causality-limited infrared slope common to scalar-induced backgrounds of essentially any origin"). The universal causality-limited IR tail of an induced background from a finite-duration source is `Ω_GW ∝ k³` (γ=2), with `k³ln²k` for narrow peaks — Cai, Pi & Sasaki, PRD **102**, 083528 (2020), arXiv:1909.13728. `f²` is *shallower* than the causal floor, so it is not "causality-limited" and is not generic. Repeated at `main.tex:879`. |
| Abstract scheme qualifiers | `main.tex:47–50` | abstract **does** carry "within one cubic-vertex scheme (S1) and `kη_B≲10⁻²`" and "a second scheme does not regulate". |
| Abstract PBH caveat | `main.tex:62–68` | the v3M.0.8 abstract quotes "shape-robust required-amplitude ratio ≈1.7–1.9" with **no** perturbativity or non-monotonicity caveat. The v3M.0.4 abstract carried both (DA3M-R2-F3). **Regression introduced by the abstract rewrite.** |
| `r = 0.84` status | `main.tex:809–820`, Table IV caption `822–829` | the numeral **and** the projected column are gone ("so no numeral is quoted here"); Table IV reports bare significance only. Nothing depends on `r`. |
| "regularized-renormalized-" | `main.tex:609` | source line break inside a compound; PDF-extraction artifact (Rule 7) — recurrence of `DA3M-F5`. |
| Today's date | system clock | **2026-09-04**. "September 4, 2026" is today, not a future date — recurrence of `DA3M-F3`, auto-FALSIFY Rule 3. |

---

## 1. Class counts

### Per leg (raw findings → class)

| Leg | raw | GENUINELY-NEW REAL | RE-FLAG-OF-DISCLOSED | FALSIFIED | OPINION/GENRE | OUT-OF-SCOPE | BLOCKER |
|---|---|---|---|---|---|---|---|
| Claude Fable (`major-revisions`) | 19 (4 MAJOR / 15 minor) | **18** (4 MAJOR / 14 minor) | 0 | 0 | 1 | 0 | 0 |
| Grok (`REJECT`) | 10 (4E / 3M / 1m / 2N) | **3** (E1, N3, + the residual of E2) | 3 (M1, M2, E4-residual) | 4 (E2-main, E3, E4-main, N1) | 2 (M3, N2) | 0 | 0 |
| Gemini (`MAJOR REVISIONS`) | 5 (4E / 1N) | **2** (E3, E4) | 1 (E1 = carried-open packaging) | 2 (E2, N1) | 0 | 0 | 0 |
| **Total raw** | **34** | | | | | | |

### Canonical (after cross-leg fingerprint dedup and matching against `DISPOSITIONS/A3M.md`)

**19 canonical genuinely-new-real items: 4 MAJOR + 15 MINOR** (`DA3M-R3-01` … `DA3M-R3-19`),
plus **4 OPINION/GENRE**, **6 FALSIFIED**, **4 RE-FLAG-OF-DISCLOSED**, **1 carried-open packaging item**
(`DA3M-R2-11`), **0 OUT-OF-SCOPE**, **0 BLOCKER**.

**Clean-wave count: 0.** The paper is **NOT converged at v3M.0.8**.

Note the structure of the result: **every one of the four MAJORs lands on content that did not
exist at R2** (§II D's method-independence closure, §III A's computed bounce cubic term, §V C's
lab-own-spectrum null, and the §VI/§VII A reach framing that those two sections newly interact
with). This is what directive R2 anticipates when a science closure intervenes — the R2
"rounds stop" statement applied to the *then-current* content, and R3 is a review of new science,
not a re-litigation of dispositioned material. Independent confirmation: **zero** of the 19 new
canonical items fingerprint-matches an existing R1 or R2 disposition.

---

## 2. Canonical numbered findings

Severity is read from each leg's own per-item tag, never from its verdict word (Rule 8).

### GENUINELY-NEW REAL — MAJOR

---

**DA3M-R3-01 (MAJOR) — the `kη_B ≲ 10⁻²` validity window is applied in the wrong direction, and the
headline LSS discrimination rests on that inversion.**
*Legs:* Fable MAJOR 1; Gemini E4 (same defect reached independently, from the pre/post-bounce
amplitude side rather than the window side).
*Classification:* **GENUINELY-NEW REAL.**
*Verdict citation:* `kη_B` is monotonically increasing in `k`. `LANE_B_NUMERICAL_2026-09-03.md:107–111`
sets the band by two requirements that both fail at **large** `k` (`J(η_*)→I_∞` and `kη_*≪1`), and flags
rows invalid for `kη_* > 0.3`; §8 assumption (A1) is `kη_B ≪ 1`. There is **no small-`k` cutoff**.
The CMB/LSS pivot `k = 0.05 Mpc⁻¹` is the **smallest** `k` in the paper — 5 to 16 decades below every
PBH scale — so it is the scale **deepest inside** the validated window. `main.tex:866–868` nevertheless
asserts the pivot "lies far outside that validated `kη_B` window", and on that basis §VI Table IV and
the abstract headline SPHEREx at `3.13–4.38σ` using the **pre-bounce** `−35/16`, while `main.tex:749–750`
simultaneously claims the window *is* satisfied at every (far larger-`k`) PBH scale. The two statements
cannot both hold, and the one that is geometrically correct is the opposite of the one the abstract
relies on. Consequence, computed by this auditor: with the S1 transfer applied at the pivot,
`|f_NL^after| ∈ [0.50,0.65]` for `−35/16` and `[0.86,1.20]` for `−35/8`; bare SPHEREx significance
falls to **0.7–0.9σ** (σ=0.7) and the separation between the two candidates falls **below 1σ** — i.e.
"this channel alone discriminates the two candidate amplitudes" (abstract; `main.tex:869–872`)
collapses. This is the paper's only discriminating channel, so the defect is load-bearing.
*Required closure:* see CLOSURE PLAN **C1**. A science decision is required — this is not a wording fix.

---

**DA3M-R3-02 (MAJOR) — "satisfied at every PBH mass scale … for any bounce energy above the BBN
scale" is wrong by 11–13 orders of magnitude in energy.**
*Legs:* Fable MAJOR 4.
*Classification:* **GENUINELY-NEW REAL.**
*Verdict citation:* `main.tex:749–750`. Auditor computation (§0): with `aH ∝ T` in radiation domination
anchored at `k_eq ≈ 0.01 Mpc⁻¹`, `T_B ~ 1 MeV` gives `a_B H_B ≈ 1.2×10⁴ Mpc⁻¹`, so `kη_B ≲ 10⁻²`
admits only `k ≲ 10² Mpc⁻¹`. The PBH scales the section actually uses span `k ~ 10⁴ Mpc⁻¹`
(10⁴ M_⊙) to `~10¹⁵–10¹⁶ Mpc⁻¹` (10¹⁵ g) — **none** of them qualifies at BBN energy. The condition is
`T_B ≳ 10⁸–10¹⁰ GeV` to cover the lightest mass quoted. The claim as printed is the exact inverse of
the true scaling and is the same root cause as DA3M-R3-01.
*Required closure:* **C2**. (Note: the 7-decade shortfall of the null is very likely insensitive to the
transfer assumption, but the paper currently *asserts* the transfer applies rather than showing the
null survives without it — that has to be shown, not assumed.)

---

**DA3M-R3-03 (MAJOR) — the "method-independent confirmation" and "derived identity" claims are
asserted in-paper, contradicted in one word by the abstract, and stronger than the lab's own note.**
*Legs:* Fable MAJOR 2 (three sub-claims a/b/c); Grok M1 (weaker form, dispositioned as re-flag —
its substantive half folds here).
*Classification:* **GENUINELY-NEW REAL.**
*Verdict citation:* three independent confirmations.
(a) `main.tex:44` calls it "A classical, **gradient-expansion** route" while `main.tex:238–241` states
the gradient-expansion assumption `N_i = O(∇)` **fails** in a non-attractor phase — that failure is
precisely the paper's own diagnosis of the δN defect. Terminology self-contradiction, one word.
(b) `main.tex:277–285` says "the residual gap to every separate-universe δN value is accounted for by
Eq. (5), **a derived identity** rather than an unresolved discrepancy", while `main.tex:270–274` in the
same paragraph concedes that at second order the map is non-local and "**no local f_NL relation**
between δN_c and ζ_Mald exists". Both cannot be true: an identity that admits no local `f_NL` relation
cannot account for an `f_NL` gap. Auditor arithmetic: a linear rescale `δN_c=½ζ` maps `f_NL→2f_NL`,
giving `−15/4`, not the δN value `−5`; the gap ratio is `8/3`. The lab's own note
(`fnl_monopole_adjudication_2026_09_03.md:39`) decomposes `25/8 = 5/4 ([X] monopole) + 15/8
([L]−δN_c)` and labels the second piece "recorded as … a computed identity, **not a claimed
mechanism**"; `:25` labels the linear relation "**asserted**"; `:76` says the discrepancy is
"**explained at the equation level**". The paper is strictly stronger than its own source.
(c) The classical `O(k⁰)` solution, the `[L]/[K]/[X]/[S]` bookkeeping, the `1/k_L` pole cancellation,
the final-time re-threading boundary term, `f_NL^ρ = 5(ε−7)/8`, `f_NL^c = −5` for all ε, and the
Bianchi-I zero-monopole statement appear in the PDF with **no equation, no intermediate step and no
appendix** — only two `\texttt{}` script paths (`main.tex:286–291`). For a PRD paper whose headline
is "the factor-of-two adjudication is closed", a reader cannot check the closing argument.
*Required closure:* **C3** (minimal appendix — every ingredient already exists in the note; this is
transcription, not new science).

---

**DA3M-R3-04 (MAJOR) — the induced-GW infrared slope physics is misstated in §IV D and §VII B.**
*Legs:* Fable MAJOR 3.
*Classification:* **GENUINELY-NEW REAL** (scoped: the *generality* claim is wrong; the channel's
`γ=3` framing survives and is in fact strengthened).
*Verdict citation:* `main.tex:545–547` — "`Ω_GW ∝ f²` is the causality-limited infrared slope common to
scalar-induced backgrounds of essentially any origin"; echoed at `main.tex:879` ("a slope that any
scalar-induced background shares"). The universal, causality-enforced IR tail of a scalar-induced
background from a source of finite duration is `Ω_GW ∝ k³` — i.e. `γ = 2` in this paper's own
convention `Ω_GW ∝ f^{5−γ}` — with a `k³ln²k` correction for narrow peaks (Cai, Pi & Sasaki, PRD
**102**, 083528 (2020), arXiv:1909.13728). `f²` is **shallower** than the causal floor, so it cannot be
the causality limit and is not generic; it requires a specific broad / near-scale-invariant source.
Importantly, the paper's `γ=3` prediction itself is **not** falsified: `pta_gamma_reproduce.py:22–31`
and `main.tex:417–418` cite it to Papanikolaou 2025 (arXiv:2504.11641) as a matter-bounce SIGW result,
and the paper's `γ=3` vs `γ=13/3` vs `γ=5` arithmetic is untouched. The error is a self-inflicted
*weakening*: §IV D disclaims as generic a slope that is actually discriminating, while §IV A and the
abstract call it "the bounce prediction". Correcting §IV D makes the channel stronger and removes an
internal contradiction between §IV A and §IV D.
*Required closure:* **C4**.

---

### GENUINELY-NEW REAL — MINOR

| id | item | leg(s) | verdict citation (source) | closure |
|---|---|---|---|---|
| **DA3M-R3-05** | "at **28–39 %** of the transmitted contraction term" is arithmetically wrong | Fable m4 | `main.tex:374–375`; ratios from `LANE_B_NUMERICAL:125–128` are `0.387 / 0.191 / 0.297` ⇒ **19–39 %**. The source note carries the identical error and must be corrected in the same pass. | C5 |
| **DA3M-R3-06** | `n_s − 1 = 12w/(1+w)` is the wrong contracting-phase formula | Fable m5 | `main.tex:743` and `inlab_delta2_zeta_2026-09-03.py:24`. Correct: `12w/(1+3w)` (Wands 1999; Cai–Easson–Brandenberger 2012, already in the script's own citation block). Numerically inert (`w: −0.00293 → −0.00290`) but a formula error in a paper whose subject is exactness. | C5 |
| **DA3M-R3-07** | `0 < T_fNL ≤ 1/2` has both endpoints inverted | Fable m2 | `main.tex:315–318` (and abstract `:49`): `T=(1−ρ)/2` with `ρ∈(0,1]` gives `T ∈ [0, 1/2)`. `T=1/2` is *excluded*; `T=0` is *attained*. | C5 |
| **DA3M-R3-08** | `ρ_B` in Eq. (7) is never defined | Fable m3 | `main.tex:353`. Auditor verified `ρ_B = 1−2T` reproduces all three `Δf_NL^bounce` rows exactly, making `f_NL^after = −(85/48)T − 5/24` a one-parameter function of `T` — more informative than three tabulated numbers. | C6 |
| **DA3M-R3-09** | the Ω_DM footnote's "every result in this section is unaffected" is false for Table III / Fig. 1 | Fable m6 | `main.tex:716–726`. Auditor re-ran `pbh_compaction_fnl.py`: correcting `Ω_DM 0.674→0.264` moves the Gaussian calibration `A_* : 0.131446 → 0.127901` (−2.70 %) and the tabulated `f_PBH : 3.6e−14 → 6.3e−15` and `1.6e−2 → 5.7e−3`. The **ratio** is genuinely unaffected, exactly as the footnote claims for it. | C7 |
| **DA3M-R3-10** | the configuration behind the μ-dependent Eq. (4) is not stated; exact isosceles forces μ=0 | Fable m1 | `main.tex:157–200` (Eq. 2 sets `k₂=k₃`) vs Eq. (4)'s `+(15/16)μ²`. The lab's own note `fnl_monopole_adjudication_2026_09_03.md:41`: "Same μ definition throughout (μ = k̂_L·k̂_S); **isoceles μ=0**". So Eq. (3) is the μ=0 value and Eq. (4) requires relaxing `k₂=k₃` at `O(k₁)`. | C6 |
| **DA3M-R3-11** | revision-history prose and inline filesystem paths in the body (directive Q1) | Fable m12 **+ Grok E1 + Grok N3 + Gemini E3** (3-leg convergence) | `main.tex:218` (§II D title "…: closed"), `:275` ("left open in earlier drafts of this work"), `:286–291` (two `research/theory_audit/…` paths in body text — Grok N3's "twice on p.3"), `:530–534` ("This also supersedes an earlier, misdescribed claim in this section…"), `:609` + §V A ("why it had to be redone"). R1's `DA3M-08` closed the *audit tags*; the R2 and v3M.0.8 closures **re-introduced** narration of the lab's own corrections. Directive Q1 forbids exactly this. | C8 |
| **DA3M-R3-12** | injection-recovery pulls quoted without their scatter | Fable m10 | `main.tex:515–521` quotes mean pulls `+0.016σ`/`+0.033σ` and concludes "unbiased at well under `0.1σ`". `outputs/pta_injection_30bin_realkde_2026_09_02.json → summary` gives `std_pull = 0.0993` and `0.1203` over 5 realizations ⇒ SEM `0.044` and `0.054`. The claim is supported at the `~0.05σ` level, not tighter. | C6 |
| **DA3M-R3-13** | Table III lists `f_PBH = 3.5×10³` and `2.2×10⁸` — not physical abundances | Fable m8 | `main.tex:690–691`. These exceed unity by 3 and 8 decades; they are nominal uncapped values at the Gaussian-calibrated amplitude, which the column heading does not say. | C6 |
| **DA3M-R3-14** | `γ_cr ≡ σ_cr²/(σ_c σ_r)` — the subscripts `c`, `r` and their windows are undefined | Fable m7 | §V B, `main.tex:590–668`; `γ_cr` appears in Table III and in the `≷0.85` crossover discussion without the variances ever being defined. | C6 |
| **DA3M-R3-15** | the `\|r\| ≫ 1` limit's k-range and the three backgrounds' parameters are unstated; "poly (analytic non-LQC)" is undefined | Fable m11 | `main.tex:310–314`: `r = −9i𝒜²I_∞/k³` is explicitly k-dependent, so `\|r\|≫1` holds only below some k; no range given. Table at `:363–370` names a background never defined. | C6 |
| **DA3M-R3-16** | §II C's central bookkeeping claim is described rather than displayed | Fable m13 | `main.tex:201–217`: the claim that Cai et al.'s printed shape function gives `−35/16` in the squeezed limit while their Eqs. (38)–(40) print `−35/8` is the paper's core literature contribution and should be shown (their polynomial, the limit, the prefactor). Equation numbers in Li et al. [4] and Quintin et al. [3] are also not given, and the paper does not say whether Li et al. treat it as an error or a convention. (Related to the still-open `DA3M-m09`.) | C9 |
| **DA3M-R3-17** | Table I footnote "`O(k²S²)`" — `S` is undefined | Fable m14 | `main.tex:197` (`\footnotetext[1]`). Residual of the R1 item `DA3M-m11` closure, which added the qualifier but not the symbol's definition. | C6 |
| **DA3M-R3-18** | the abstract prints `γ_HD = 3.2^{+0.6}_{-0.6}` without its interval type | Grok E2 (residual — Grok's stated form is falsified below) | `main.tex:56–57`. The body and Table II caption give `σ ≈ 0.365`, which is only correct because ±0.6 is a **5–95 %** half-width (`pta_gamma_reproduce.py:53–58`). A reader who reads ±0.6 as 1σ gets `0.33σ`, not the abstract's `0.55σ`. `DA3M-01`'s closure put the interval type in §IV; the abstract was not covered. | C6 |
| **DA3M-R3-19** | **regression:** the abstract's "shape-robust ratio ≈1.7–1.9" lost the perturbativity and non-monotonicity caveats it carried at v3M.0.4 | Fable m9 | `main.tex:62–68`. At v3M.0.4 the abstract carried "1.2\|f_NL\|σ_r ≈ 0.5–2" and the ~55-decade non-monotonicity verbatim — that text is what **falsified** Grok E2 at R2 (`DA3M-R2-F3`). The v3M.0.8 abstract rewrite (which changed `1.732±0.050` → `1.7–1.9`) dropped both. Robustness to lognormal *shape* is not robustness to truncation of the local ansatz. | C10 |

---

### RE-FLAG-OF-DISCLOSED (already in the paper; no closure required)

| id | item | leg | where the paper already says it |
|---|---|---|---|
| **DA3M-R3-R1** | "the factor-of-two resolution is not independent — no second public bispectrum code, no check against Cai's own Hamiltonian; the 'first computation' claim is unsupported" | Grok M1 | `main.tex:271–276` — the scope statement already limits the in-in route to "**within the in-in method**" and names its two published agreements (Li et al.'s `c_s=1` limit, Quintin et al.'s quoted value). = `DA3M-R4`. The one substantive half — whether the *classical* route is genuinely independent and adequately shown — is not dismissed; it is carried as **DA3M-R3-03(c)**. |
| **DA3M-R3-R2** | "official-posterior and refit σ values are juxtaposed in Table II without a not-directly-comparable qualifier" | Grok M2 | `main.tex:451–453` (the `1.20σ` offset with its quadrature σ), `:486–489` ("Gaussian approximations to a marginal that is not itself Gaussian … `P(γ>3)=8.97 %`"), Table II caption `:466–473`. = `DA3M-R2-R4`. The genuine residual (interval type missing **from the abstract**) is carried as **DA3M-R3-18**. |
| **DA3M-R3-R3** | "no table or figure shows the amplitude ratio under the exact spectrum used by Choudhury et al." | Grok E4 (residual) | `main.tex:737–740` — their spectrum "is not reconstructible from their published paper", which is *why* §V C replaces it with the lab's own. The request is unsatisfiable by construction and the paper says so. |
| **DA3M-R2-11** (carried-open, packaging) | "no frozen-release DOI; a GitHub commit hash is insufficient for PRD data availability" | Gemini E1 | Not new — this is the R2 item, explicitly left open as a Houston-only P-round action (`main.tex:958–962`; SSOT R2 closure row). Venue/packaging, not science. Carried, not re-counted. |

---

### FALSIFIED (source shows the reviewer is wrong; recorded so no leg re-raises them)

| id | item | leg | why false — source |
|---|---|---|---|
| **DA3M-R3-F1** | "the abstract omits the scheme and cutoff restrictions; the transmission result is advertised as model-independent" | Grok E3 | `main.tex:47–50` — the abstract reads "within one cubic-vertex scheme (S1) and `kη_B≲10⁻²`, a linear handoff bound … **a second scheme does not regulate**". Both restrictions Grok says are missing are in the sentence he is quoting from. Grok also mis-renders the paper's own §VII B, which repeats the qualifier. |
| **DA3M-R3-F2** | "the PBH channel is a clean null only after an unreproducible spectrum shape … `n_s = 1 − 12w/(1+w)`, `w = 0.9649`" | Grok E4 (main claim) | Inverted. `main.tex:737–741` uses the **lab's own** predicted spectrum *precisely to remove* the dependence on Choudhury's unreconstructible one; the 7-decade shortfall is computed on the lab's own model, not on a fitted stand-in. Grok also garbles the formula: the paper writes `n_s−1 = 12w/(1+w)` with `n_s = 0.9649`; `w ≈ −0.003`. (The formula is separately wrong — but for the reason in `DA3M-R3-06`, not Grok's.) |
| **DA3M-R3-F3** | "the abstract presents the refit `γ = 2.567±0.382` as the primary result without the 'under the authors' refit prior' qualifier" | Grok E2 (main claim) | `main.tex:55–58` — the abstract labels it "**(refit)**", gives the official posterior beside it "**(official 14-bin posterior, γ_HD = 3.2⁺⁰·⁶₋₀·₆)**", and quotes both z-distances. The qualifier Grok demands is printed. (Residual real bit → `DA3M-R3-18`.) |
| **DA3M-R3-F4** | "the abstract asserts `f_PBH = 0` exactly while the body shows the ratio 1.732 only after an ad-hoc Gaussian normalization" | Grok E2 (second half) | Two different sub-results, both disclosed. `f_PBH = 0` is the null on the **lab's own spectrum** (`main.tex:757–762`); `1.7–1.9` is the required-**amplitude ratio** on the lognormal stand-in at the disclosed Gaussian calibration `A_* = 0.131446` (`main.tex:664–668`). No contradiction, and the calibration is neither ad hoc nor hidden — R1's `DA3M-m07` put `A_*` in the paper. |
| **DA3M-R3-F5** | "the abstract date 'September 4, 2026' and future-dated Zenodo records are future-dated; the document was never cleaned" | Grok N1 | Today **is** 2026-09-04. Auto-FALSIFY Rule 3 (training-cutoff artifact). Recurrence of `DA3M-F3` — now **7+ consecutive rounds, 100 % falsified**. |
| **DA3M-R3-F6** | "'regularized-renormalized- resummed' has a stray hyphen and space" | Gemini N1 | `main.tex:609` — a source line break inside a hyphenated compound; the PDF renders correctly and only text extraction shows the artifact (Rule 7). Recurrence of `DA3M-F5`. |
| **DA3M-R3-F7** | "`r` is imported from an unpublished draft for a load-bearing parameter; either derive it or remove the reliance" | Gemini E2 | Already done at R2. `main.tex:809–820`: "not re-derived at the −35/16 fiducial used in this paper — **so no numeral is quoted here**"; Table IV (`:822–840`) reports **bare** significance only and its caption states the projected column is omitted. `DA3M-R2-10` closed this; no result depends on `r`. Gemini is reviewing a state of the manuscript that no longer exists. |

---

### OPINION / GENRE (no closure required; optional at the venue pass)

| id | item | leg |
|---|---|---|
| **DA3M-R3-G1** | "length-to-contribution ratio excessive: 10 pp vs 6–7 pp typical" | Grok M3. Length is an editor's call, not a referee finding; but the **C8** Q1 cut and the §V A first-pass compression will reduce it as a side effect. |
| **DA3M-R3-G2** | abstract ~380 words and dense with paper-internal labels ("scheme S1", "(A4)", "zero-shift-threading") | Fable m15. = `DA3M-G2` / `DA3M-R2-G1`, still unblocked. Do this **after** C1–C4, so the trim encodes corrected claims. |
| **DA3M-R3-G3** | Fig. 1 axis label "lognormal curvature power-spectrum amplitude `A`" does not define the normalization constant in the caption | Grok N2. = `DA3M-R2-G5`; `A_*` is now printed at `main.tex:664–668`, so this is a caption cross-reference at most. |
| **DA3M-R3-G4** | frozen-release DOI (`DA3M-R2-11`) — restated here for the P-round checklist | Gemini E1. Packaging; Houston-gated Zenodo mint. |

---

## 3. Corrections to earlier dispositions (recorded, never backfilled silently)

1. **`DA3M-R2-F3` is superseded for v3M.0.8.** At R2 it falsified Grok's "the abstract quotes
   `1.732[1.610,1.809]` stripped of its regime-of-validity caveat" because the v3M.0.4 abstract carried
   the perturbativity range and the 55-decade non-monotonicity verbatim. The v3M.0.8 abstract rewrite
   **removed both**. The R2 verdict was correct for v3M.0.4 and is **no longer true of the current
   manuscript**; the defect is re-opened as **`DA3M-R3-19`** and flagged as a closure-induced
   regression. This is exactly the failure mode directive-G hygiene exists to catch.
2. **`DA3M-08` (R1, "internal audit tags … CLOSED") is partially re-opened as `DA3M-R3-11`.** R1's
   closure verified `0` body hits for audit tags. The R2 and v3M.0.8 closures re-introduced a different
   species of the same defect — narration of the lab's own corrections ("supersedes an earlier,
   misdescribed claim", "left open in earlier drafts", "why it had to be redone") plus two inline
   `research/theory_audit/…` paths. Same directive (Q1), new instances, three legs concur.

---

## 4. Convergence statement (directives H-refined, R2, P)

**NOT converged at v3M.0.8. Clean-wave count: 0.**

19 genuinely-new-real items outstanding (4 MAJOR, 15 MINOR), none of which fingerprint-matches an
existing disposition. Two MAJORs (`R3-01`, `R3-02`) share a single root cause — the direction of the
`kη_B` inequality — and one of them invalidates the abstract's headline discrimination claim until a
science decision is taken. Two MAJORs (`R3-03`, `R3-04`) are claim-strength/derivation defects that
close with in-paper work and no new computation.

**Directive R2 accounting.** R2 declared the 2-round budget consumed *for the v3M.0.5 content*. Three
science closures landed between v3M.0.5 and v3M.0.8, which is the intervening science decision R2
requires; R3 therefore reviews new content and does not re-litigate. After C1–C10 close, **one**
verification round on the new PDF is warranted (specifically to confirm C1's decision did not
introduce a new inconsistency and that the corrected reach numbers propagate to abstract, Table IV,
§VII A and §VII B). Rounds stop after that unless the C1 decision changes a headline number again.

**Integrity.** No leg's verdict word was used as a gate. No finding was dispositioned non-real without
a cited source. No number in this audit was taken from a reviewer — every one was re-derived, re-run,
or read from the committed artifact. Two reviewer claims that *sounded* like fabrication risks
(Grok E4's "unreproducible spectrum", Gemini E2's "unpublished draft") were checked against the
manuscript and found to be reviewing superseded states of the paper.

---

## 5. CLOSURE PLAN

Ordered. **C1 requires an orchestrator/Houston science decision before any edit.** C5–C10 are
mechanical and can run as one Sonnet lane once C1's decision is recorded, because C1 changes the
numbers C10 must carry. Do not start C10 before C1.

### C1 — resolve the `kη_B` direction and decide what the LSS channel headlines (**DA3M-R3-01**) — DECISION REQUIRED
*Files:* `research/track_a3_multichannel/paper/main.tex` (§V C `:749–750`, §VI `:790–845`, §VII A
`:855–876`, §VII B `:877–896`, abstract `:36–74`); `research/track_a3_multichannel/survey_reach_fnl.py`;
`research/track_a3_multichannel/outputs/survey_reach_fnl.json`.

First, state the true direction once, in §III A: `kη_B ≲ 10⁻²` is an **upper bound on `k`**, so it is
satisfied *most easily* at the largest scales and *hardest* at PBH scales
(`LANE_B_NUMERICAL_2026-09-03.md:107–111`, assumption (A1)). Delete the §VII A sentence
"which lies far outside that validated `kη_B` window" — it is false.

Then choose **one**:

- **(a) Propagate (preferred; it is what the paper's own physics says).** Add
  `f_NL^after` rows to Table IV: for each of the three backgrounds compute
  `T·(−35/16)+Δf_NL^bounce` and `T·(−35/8)+Δf_NL^bounce` and the bare significances
  `|f_NL^after|/σ` at σ = 0.7, 0.5, 1.0. Auditor's precomputed values for the drafter to check
  against: `−35/16 → [−0.65,−0.50]`, `−35/8 → [−1.20,−0.86]`; SPHEREx bispectrum-only bare
  `0.7–0.9σ` and `1.2–1.7σ`. Keep the pre-bounce row as a clearly-labelled secondary
  ("pre-bounce amplitude, i.e. assuming `T_fNL = 1`"). Rewrite the abstract's
  "this channel alone discriminates the two candidate amplitudes, with SPHEREx reaching `3.13σ`"
  to the transmitted statement, and rewrite §VII A's "separates them by more than `3σ`" and §VII B's
  parenthetical "(using the pre-bounce, not the transmitted, amplitude)" to match. Extend
  `survey_reach_fnl.py` with the `f_NL^after` rows and re-emit its JSON.
- **(b) Justify a genuine exemption.** Only if a *physical* reason exists why the S1 super-Hubble
  transfer does not apply at `k = 0.05 Mpc⁻¹` — an IR cutoff on the S1 calculation, a mode that never
  reached the relevant regime, a breakdown of (A4) at large scales. "Outside the window" is **not**
  such a reason and cannot be reused. If (b) is taken, the §V C sentence extending the transfer to all
  PBH scales must be deleted in the same edit, because the two claims are mutually exclusive.

Record the decision verbatim in `project-context/SSOT/paper-a3m/status.md` before editing.

### C2 — correct the bounce-energy condition (**DA3M-R3-02**)
*File:* `main.tex:749–750`. Replace "for any bounce energy above the BBN scale" with the actual
condition, stated as a requirement on `T_B` (or `H_B`) at the **smallest** PBH mass used: covering
`10¹⁵ g` (`k ~ 10¹⁵–10¹⁶ Mpc⁻¹`) needs `a_B H_B ≳ 10¹⁷–10¹⁸ Mpc⁻¹`, i.e. `T_B ≳ 10⁸–10¹⁰ GeV`. Either
(i) restrict the null's stated scope to the mass range that qualifies at the bounce energy the paper is
willing to assume, or (ii) show the 7-decade shortfall is insensitive to the transfer assumption
(plausible — a scale-independent `T ≤ 1/2` cannot close 7 decades — but it must be *shown*, one
sentence with the arithmetic, not assumed). Same edit must state the direction correctly (see C1).

### C3 — add the derivation appendix and correct two claim words (**DA3M-R3-03**)
*Files:* `main.tex` (abstract `:44`; §II D `:218–291`; new Appendix A);
source: `research/theory_audit/fnl_monopole_adjudication_2026_09_03.md` §§1–4.
1. Abstract `:44`: "A classical, gradient-expansion route" → "A classical super-Hubble (`O(k⁰)`) route,
   with the non-local shift terms retained". (The paper's own §II D says the gradient expansion fails.)
2. Abstract `:46–48` and `main.tex:277–285`: replace "the gap … is now a **derived identity**" with
   the note's own framing — the two calculations compute **different variables**; the linear-order
   relation is Eq. (5); the second-order part of the threading map is a **recorded identity whose
   mechanism is not derived** (`fnl_monopole_adjudication:39, 72`); at second order no local `f_NL`
   relation exists, so the naive squeezed-limit comparison is invalid rather than reconciled.
3. New Appendix A, transcribing the note (no new science required):
   (i) `N = 1 + ζ̇/H`, Friedmann at fixed φ ⇒ `δH/H = −(ε/3)ζ̇_L/H`, `δK = −∂²ψ/a² → −εζ̇_L`,
   `δN_c = ∫(K/3)dτ = ζ + b` with `ḃ = δK/3` ⇒ `b = −(ε/3)ζ_L` ⇒ **Eq. (5)**, with its sign
   convention stated explicitly (this also answers the referee's question 2);
   (ii) the `[L]/[K]/[X]/[S]` decomposition table with the `1/k_L` pole cancellation shown in the sum
   over vertices, and the final-time re-threading boundary term
   `f_b = (ε/2ℋ)[∂ζ∂χ̃ − ∂⁻²∂_i∂_j(∂_iζ∂_jχ̃)]` and what it subtracts/adds
   (`fnl_monopole_adjudication:41`);
   (iii) the general-ε formulas `f_NL^ρ = 5(ε−7)/8`, `f_NL^c = −5`, and the in-in
   `5ε(9−ε)/18` monopole with its reduction to `−35/16 + (15/16)μ²` at `ε = 3/2`
   (`fnl_monopole_adjudication:63–72`);
   (iv) the Bianchi-I statement with the one-line reason (shear is `O(k_L⁰)` and traceless; no
   traceless linear-in-`ζ_L` response supplies a monopole) — this answers referee question 5.
4. Keep the script paths **only** in the reproducibility statement (see C8).

### C4 — correct the induced-GW IR-slope statement (**DA3M-R3-04**)
*File:* `main.tex:545–547` and `:879`. Replace "the causality-limited infrared slope common to
scalar-induced backgrounds of essentially any origin" with the correct pair of statements: the
universal causality-limited IR tail of an induced background from a finite-duration source is
`Ω_GW ∝ f³` (`γ = 2`), with `f³ln²f` for narrow peaks — cite Cai, Pi & Sasaki, PRD **102**, 083528
(2020), arXiv:1909.13728 (add to `mainNotes.bib`) — and `Ω_GW ∝ f²` (`γ = 3`) follows here from the
matter bounce's broad, near-scale-invariant scalar source, citing the specific equation in
Papanikolaou 2025 (arXiv:2504.11641) that yields it. State whether the `f²` scaling holds across the
full NANOGrav band or only asymptotically. Then fix `:879` ("a slope that any scalar-induced background
shares") and make §IV A / §IV D consistent: `γ = 3` is more distinctive than §IV D currently concedes.

### C5 — three numeric/formula corrections (**DA3M-R3-05, -06, -07**)
- `main.tex:374–375`: `28`–`39 %` → **`19`–`39 %`**; and correct the same sentence in
  `research/cubic_bounce_transmission/lane_b_numerical/LANE_B_NUMERICAL_2026-09-03.md:125–128`.
- `main.tex:743` **and** `research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.py:24` (docstring)
  and its `.md`: `n_s−1 = 12w/(1+w)` → `12w/(1+3w)`; re-run the script and confirm the tabulated
  `Δ²_ζ` values are unchanged at quoted precision (`w` moves −0.00293 → −0.00290), and re-emit
  `outputs/inlab_delta2_zeta_2026-09-03.json`.
- `main.tex:315–318` and abstract `:49`: `0 < T_fNL ≤ 1/2` → **`0 ≤ T_fNL < 1/2`**.

### C6 — eight one-clause definitional/labelling fixes (**DA3M-R3-08, -10, -12, -13, -14, -15, -17, -18**)
All in `main.tex`:
- `:353` define `ρ_B ≡ ρ(η_B) = 1 − 2T_fNL` and state `f_NL^after = −(85/48)T − 5/24`.
- `:157–200` state the configuration for Eq. (4) (`k₂ = k₃` relaxed at `O(k₁)`; `μ = k̂_L·k̂_S`) and say
  explicitly that Eq. (3) is the `μ = 0` value, **not** the angular average `−15/8`.
- `:515–521` add the standard error of the mean pull: `+0.016 ± 0.044σ` and `+0.033 ± 0.054σ`
  (`std_pull` 0.0993 / 0.1203 over 5 realizations, from the committed JSON); soften "well under 0.1σ"
  to what that supports.
- Table III `:684–695` relabel the two `f_PBH` columns as the **nominal (uncapped)** value at the
  Gaussian-calibrated amplitude, or report `β` instead.
- §V B define `γ_cr ≡ σ_cr²/(σ_c σ_r)` with the compaction and curvature variances and their windows.
- `:310–314` give the k-range over which `|r| ≫ 1` holds, and define the three backgrounds including
  "poly (analytic non-LQC)".
- `:197` define `S` in the Table I footnote `O(k²S²)`.
- abstract `:56–57` label the official interval: `γ_HD = 3.2^{+0.6}_{-0.6}` (**5–95 %**, `σ ≈ 0.365`).

### C7 — scope or recompute the Ω_DM footnote (**DA3M-R3-09**)
*Files:* `main.tex:716–726`; optionally `pbh_compaction_fnl.py:156` + `outputs/pbh_compaction_fnl.json`
+ Table III + Fig. 1.
Either (a) narrow the footnote's claim to what is true — the **ratio** and the §V C null are unaffected
(`Ω_DM` cancels), while the tabulated `f_PBH` column is quoted at the calibration that uses Choudhury's
printed value — or (b) recompute at `Ω_DM = 0.264`, which the auditor has already done and which the
drafter can check against: `A_* : 0.131446 → 0.127901`, `f_PBH(−35/16) : 3.6e−14 → 6.3e−15`,
`f_PBH(−35/8) : 1.6e−2 → 5.7e−3`. If (b), regenerate `pbh_compaction_fnl.png` — directive I6: a text
sweep cannot see a value baked into the figure.

### C8 — directive-Q1 sweep: remove all revision history and inline paths from the body (**DA3M-R3-11**)
*File:* `main.tex`. Rewrite to present results, not process:
- `:218` §II D title "…: closed" → a neutral title (e.g. "Cross-check by an independent classical route").
- `:275` "left open in earlier drafts of this work is now closed" → state the result directly.
- `:286–291` move both `research/theory_audit/…` paths out of the body into the reproducibility
  statement (the appendix from C3 replaces their in-body function).
- `:530–534` delete the "This also supersedes an earlier, misdescribed claim in this section…"
  passage entirely; report only the current 30-bin real-KDE injection result. The superseded synthetic
  run may stay as an unnarrated secondary cross-check, or be dropped.
- §V A: remove "why it had to be redone" framing and compress the first-pass Press–Schechter
  discussion to one paragraph stating why the truncated quadratic map fails.
Verification: `grep -nE 'research/|earlier draft|supersed|had to be redone|prior version' main.tex`
should return hits only inside the reproducibility statement.

### C9 — display the Cai bookkeeping (**DA3M-R3-16**)
*File:* `main.tex:201–217`. Display Cai et al.'s printed shape function, take its squeezed limit, and
show the prefactor, so the `−35/16` vs `−35/8` localization is checkable on the page. Add the equation
numbers in Li et al. [4] and Quintin et al. [3] where `−35/16` appears, and state whether Li et al.
describe the factor as an error or a convention difference. Closes the long-open `DA3M-m09` at the same
time.

### C10 — abstract pass, LAST (**DA3M-R3-19**, and G2 if desired)
*File:* `main.tex:36–74`. **Run only after C1–C4 are settled**, because C1 changes the reach numbers
and C3/C4 change two claim sentences. Restore the perturbativity diagnostic (`1.2|f_NL|σ_r ≈ 0.5–2`)
and the non-monotonicity caveat alongside the `1.7–1.9` ratio — these were present at v3M.0.4 and were
dropped by the v3M.0.8 rewrite. Optionally trim toward the PRD ~250-word norm and de-jargon
"scheme S1"/"(A4)"/"zero-shift-threading" (`DA3M-R3-G2`) in the same pass.

### Post-closure gate (mandatory, directive G + I6)
Bump `\paperVersion` and `\paperTimestamp`; recompile to 0 undefined references; run `/latex-audit`;
re-mirror the new PDF byte-identically to `site/public/papers/`; regenerate any figure whose numbers
C7 changed; `paperVersions:bump` in Convex with the real new md5/pages; three-way md5 check
(fresh compile == served == Convex). Then one verification round on the new exact PDF, scoped to C1.
