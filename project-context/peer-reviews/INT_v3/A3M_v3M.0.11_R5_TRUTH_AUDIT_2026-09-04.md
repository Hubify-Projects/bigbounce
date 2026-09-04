# A3M v3M.0.11 — R5VERIFY truth audit (independent, verdict-first)

- **Round:** `ROUND_2026-09-04-A3M-v3M.0.11-EXACTPDF-790fafa6-R5VERIFY`
- **Manuscript:** `research/track_a3_multichannel/paper/main.tex` + `main.pdf`, v3M.0.11, 14 pp
- **sha256 (bound):** `790fafa691e1a6ef0c476309d8224c5f2af2a59e4a3966f6afa0cf9d9dff4105`
- **Board:** `INT_v3/A3M_v3M.0.11_R5_BOARD_2026-09-04.md`
- **Prior canon:** `DISPOSITIONS/A3M.md`; `INT_v3/A3M_v3M.0.9_R4_TRUTH_AUDIT_2026-09-04.md` (ids `DA3M-R4-*`).
- **Legs audited:** Grok API `grok-4.3` (REJECT, 3E/3M/2m/2N); Gemini API `gemini-3.1-pro-preview`
  (MAJOR REVISIONS, 4E/3M/1m/1N); Claude Fable 5.1 INT subagent (major-revisions, 5 MAJOR / 16 minor).
  OpenAI ABSENT (directive N pause); Perplexity ABSENT (quota) — recorded, never counted clean.
- **Auditor:** skeptical in both directions, told no expected outcome. Every verdict below is decided
  from a source — a `.tex` line, a committed JSON/script, or the auditor's own arithmetic.
- **Protocol:** `/peer-review-truth-audit` + `/bigbounce-truth-audit`, patterns 061–066,
  directive H-refined, directive R2.

## PLAN (this audit, in order)

1. Independent verification table — re-check the physics behind the five Fable MAJORs
   (M1 S1-only `0 ≤ T < 1/2` vs S2 `λ_ζ=0.97`; M2 `2.1–4.4 decades` vs `|f_NL|≈1.2e3` equilateral;
   M3 NANOGrav `6.3e-10` vs `3.6e-9` and the 13.6/14.3 gap; M4 δN normalisation; M5 Choudhury sign)
   and Grok's three ESSENTIALs + Gemini's four ESSENTIALs, each against a committed source.
2. Per-leg / per-class counts.
3. Canonical numbered findings with class + verdict citation + closure action.
4. Closure plan split (i) editorial/real edits for v3M.0.12 (Sonnet lane, exact file/lines,
   incl. the two >10pt overfull baselines) and (ii) SCIENCE items needing a ledger computation.
5. `DISPOSITIONS/A3M.md` update.

*(Sections appended below as each is completed and committed.)*

---

## 0. Independent verification performed by this auditor

Nothing below is graded on a reviewer's say-so. Line numbers are `main.tex` @ v3M.0.11.

| Object | Command / source | Result |
|---|---|---|
| PDF binding | `shasum -a 256 site/public/papers/a3_multichannel_arxiv_v3M.0.11.pdf` | `790fafa6…4105` ✓ board + all three leg headers |
| S2 transfer (Fable M1) | `lane9b2_s2_rawadm/results.json → headline/S2_f_NL_after_mean = -1.2461`, `S1_f_NL_after = -0.50025`; `main.tex:498–501` `\|λ_ζ\|=0.97` (S2) vs `6.06` (S1), net cubic `+1.0` (S2) | auditor arithmetic: `T·(-2.1875)+1.0 = -1.246 ⇒ T = 1.027 = 1/0.97`. **T_fNL[S2,Quintin] ≈ 1.03 > 1/2** — the printed bound is violated by the paper's own S2 row |
| Bound's scope | `:355–360` "under assumption (A4), `0≤T<1/2` since `ρ∈(0,1]`", `:433` "caps it at 1/2 within the (A4) handoff scheme" | the bound IS (A4)/S1-conditional in derivation, but the abstract `:52–56` and `:359–361` ("linear transfer can only suppress … never invert or amplify") state it unconditionally |
| "2.1–4.4 decades" (Fable M2) | `lane9c2_lqc_modes/LANE9C2_LQC_MODES_2026-09-04.md:255–261`: "`\|Δf\|` of order 0.2–3 (squeezed) and 0.3–10 (equilateral) **through the whole window `kη_B≲1`** … a deficit of **2.1–4.4 dex at and below `k_LQC`**" | the source **restricts the claim to `kη_B ≲ k_LQC η_B = 1.06`**; `main.tex:423–428` advertises it "across `kη_B∈[0.1,10]`" |
| The 1.2×10³ (Fable M2) | `lane9c2_lqc_modes/results.json → equilateral/10/S-lab/total = -1215.57` (η\*/η_B = 10) | §V C's `\|f_NL\|≈1.2×10³` is the **equilateral, `kη_B=10`** point — outside the "at and below `k_LQC`" window the §III sentence actually covers. Both statements are individually sourced; **as printed they contradict** |
| ABS comparison ratios | `results.json → abs_comparison/per_k/*/lab/S-lab/ratio_to_ABS` = `3.87e-5, 5.82e-4, 8.42e-4, 3.27e-2, 2.42e4` at `kη_B = 0.1,0.3,1,3,10` | at `kη_B=10` the lab value is **4.4 dex ABOVE** the ABS decay law, not below |
| NANOGrav amplitude (Fable M3) | `outputs/sigw_nhz_from_lab_spectrum_2026_09_04.json → nanograv_reference/Omega_GW_h2_at_f_yr = 3.6235e-9`; `log10_amplitude_shortfall_… = 14.3416` / `13.7352` | `main.tex:700–707` prints `6.3×10⁻¹⁰`. Auditor: `log10(6.3e-10/1.45e-23) = 13.64 ≠ 14.3`; `log10(3.62e-9/1.45e-23) = 14.40`. **The printed reference amplitude is unsupported by the paper's own artifact and inconsistent with its own quoted gap.** The `10^14.3`/`10^13.7` gaps ARE supported |
| Fig. 1 (Fable m14, Gemini N1) | auditor rendered `paper/sigw_nhz_from_lab_spectrum_2026_09_04.png` | y-axis **is** labelled `Ω_GW h²` ⇒ Gemini N1 falsified. Title reads "A3-3: induced GWs at nHz from the lab's own Δ²_ζ"; legend entries `MB_anchored_ns0.9649`, `pure_dust_ns1` ⇒ Fable m14 real. NANOGrav dashed line sits at ~3×10⁻⁹ at f_yr, confirming M3 |
| `kη_B≈3` reachability (Fable m7) | `sigw…json → transfer_validity/k_B_Mpc-1/"T_B=1e8 GeV" = 1.7143e15` | `kη_B=3 ⇒ k = 5.14×10¹⁵ Mpc⁻¹`, **inside** the paper's own `10¹⁵–10¹⁶ Mpc⁻¹` PBH band at the stated `T_B ≳ 10⁸ GeV`. Fable's stronger claim ("corresponds to `T_B~10⁶ GeV`, which §V C excludes") is **falsified**; only "say which `(T_B,k)`" survives |
| δN normalisation (Fable M4) | `:281–292` `δN_c=(1-ε/3)ζ_Mald` (= ½ζ at ε=3/2) + "at second order … no local `f_NL` relation … compares two different observables"; App. A.2 table `:1240–1252` prints `[L]=-25/8 … total -35/16`, `comoving δN … -5` | the paper **does** state they are different variables; it does **not** state what `f^ρ_NL`/`f^c_NL` are normalised against, while a `δN_c`-normalised `f_NL` differs by `1/(1-ε/3) = 2` at ε=3/2. Narrow real defect; no fabrication found |
| Choudhury sign (Fable M5) | `:864–870` verbatim: "our implementation instead finds *enhancement* … a genuine discrepancy left unresolved because it depends on which side of that crossover their (unreproducible) spectrum falls" | disclosed, and the demanded re-run at their parameter set is **unsatisfiable by construction** (= `DA3M-R3-R3`). Residual: the ratio's conditionality is stated only in §V B |
| refit vs official σ | `:560–588`: official = "the primary comparison"; refit = "a secondary, differently-conditioned cross-check" | substance present; the literal phrase "not directly comparable" is absent (3rd–4th recurrence of `DA3M-R3-R2`) |
| Grok M1 "no central value" | `:462–470` per-background table (`T_fNL`, `Δf^bounce`, `f^after` = `0.165/-0.140/-0.501`, `0.250/-0.104/-0.651`, `0.196/-0.127/-0.555`) | falsified — per-background fiducials are tabulated |
| Grok N3 "Eq. (1) = Eq. (3)" | `:151–153` is the `f_NL^local` definition; `:171–174` is the boxed `-35/16` result | falsified |
| Grok N4 "Fig. 1 caption cites a commit hash" | caption `:729–740` | falsified — it cites the JSON filename, no hash |
| Grok N1 "future date" | `:19` `\paperTimestamp{September 4, 2026}`; today **is** 2026-09-04 | falsified. **9th consecutive round**, 100 % falsified (`DA3M-F3`) |
| Q1 residue (Gemini E4, Grok N2) | `grep -nE 'research/\|this lab\|directive Q' main.tex` = 14 hits; in-body at `:63, :557, :560, :604, :679, :937, :1105`; internal history at `:421, :482` | `DA3M-R4-11` (C7) still **not closed** |
| Overfull hboxes | `main.log` | `56.74pt` @ `:697` (Eq. `gammapred`), `16.76pt` @ `:697–711`, `14.58pt` @ `:1240–1253` (App. A.2 tabular), plus `2.74pt` @ `:837`, `2.16pt` @ `:1063–1080` |

## 1. Class counts

| leg | raw | GENUINELY-NEW REAL | REAL residual (open earlier) | RE-FLAG | FALSIFIED | OPINION/GENRE | carried packaging |
|---|---|---|---|---|---|---|---|
| Grok API (`REJECT`) | 10 (3E/3M/2m/2N) | **0** | 1 | 3 | 6 | 0 | 0 |
| Gemini API (`MAJOR REVISIONS`) | 9 (4E/3M/1m/1N) | **3** | 1 | 1 | 2 | 1 | 1 |
| Claude Fable (`major-revisions`) | 21 (5 MAJOR/16 minor) | **15** | 1 | 3 | 2 sub-claims | 3 | 0 |
| OpenAI / Perplexity | ABSENT (directive N pause / quota) — never faked, never counted clean | — | — | — | — | — | — |

**Canonical after cross-leg fingerprint dedup:** **18 genuinely-new REAL** (3 MAJOR + 15 MINOR,
one of them auditor-originated), **2 REAL residuals of open R4 items** (`DA3M-R4-11`,
`DA3M-R4-12`), **1 carried packaging item** (`DA3M-R2-11`), **6 RE-FLAG-OF-DISCLOSED**,
**10 FALSIFIED**, **6 OPINION/GENRE**, **0 BLOCKER**.

**Clean-wave count: 0** (reset — genuinely-new real findings present).
