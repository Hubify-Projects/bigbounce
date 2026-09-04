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
| Gemini API (`MAJOR REVISIONS`) | 9 (4E/3M/1m/1N) | **3** | 1 | 1 | 3 | 0 | 1 |
| Claude Fable (`major-revisions`) | 21 (5 MAJOR/16 minor) | **15** | 1 | 3 | 2 sub-claims | 3 | 0 |
| OpenAI / Perplexity | ABSENT (directive N pause / quota) — never faked, never counted clean | — | — | — | — | — | — |

**Canonical after cross-leg fingerprint dedup:** **18 genuinely-new REAL** (3 MAJOR + 15 MINOR,
one of them auditor-originated), **2 REAL residuals of open R4 items** (`DA3M-R4-11`,
`DA3M-R4-12`), **1 carried packaging item** (`DA3M-R2-11`), **6 RE-FLAG-OF-DISCLOSED**,
**11 FALSIFIED**, **6 OPINION/GENRE**, **0 BLOCKER**.

**Clean-wave count: 0** (reset — genuinely-new real findings present).

---

## 2. Canonical numbered findings

Severity is read from each leg's own per-item tag, never from its verdict word.

### GENUINELY-NEW REAL — MAJOR

**DA3M-R5-01 (MAJOR) — the `0 ≤ T_fNL < 1/2` bound and "linear transfer can only suppress" are
S1/(A4)-only statements, printed unconditionally, and the paper's own S2 row violates them.**
*Legs:* Fable M1 (+ minors 2, 3); Grok E1 reaches the same territory from a false premise (see F1).
*Class:* **GENUINELY-NEW REAL, editorial — no new computation.*
*Verdict citation:* `:355–360` derives `0≤T<1/2` from `T=(1-ρ)/2`, `ρ∈(0,1]`, **under assumption
(A4)** and in the `|r|≫1` limit; `:433` repeats "caps it at `1/2` within the (A4) handoff scheme".
But `:359–361` then asserts flatly "within this handoff scheme, linear transfer can only suppress
the amplitude, never invert or amplify its sign", and the abstract `:52–56` prints the bound with
no scheme tag. `:498–501` reports `|λ_ζ|=0.97` for S2 on the Quintin-type background and a net
cubic `+1.0`; with `f^after[S2] = -1.246` (`lane9b2_s2_rawadm/results.json → headline`) and
`f^before = -2.1875`, the auditor's own arithmetic gives `T = 1.027 = 1/0.97 > 1/2`. The bound is
therefore correct **only** where (A4) holds, and the paper never says S2 falls outside it. The
range `0.165–0.409` also omits this `≈1.03` value while `:377–379` calls it "the full set of three
backgrounds and two conventions".
*Closure:* **C1** — tag the bound "(scheme S1, assumption (A4))" in the abstract and at `:359`;
add the S2/Quintin `T_fNL ≈ 1.03` cell to the `:462–470` table (marking `Δf^bounce[S2]` "not
separately regulated", per `:510–515`); restate `:377–379` as "three backgrounds × two conventions,
S1 rows only".

**DA3M-R5-02 (MAJOR) — §III's "2.1–4.4 decades below the 10³ plateau across `kη_B∈[0.1,10]`"
overstates its own source's window, and §V C's `|f_NL|≈1.2×10³` from the same scan contradicts it
as printed.**
*Legs:* Fable M2.
*Class:* **GENUINELY-NEW REAL, editorial + one table — no new computation.**
*Verdict citation:* `LANE9C2_LQC_MODES_2026-09-04.md:255–261` states the deficit as "**2.1–4.4 dex
at and below `k_LQC`**", with `|Δf_NL^bounce|` "of order 0.2–3 (squeezed) and 0.3–10 (equilateral)
through the whole window `kη_B ≲ 1`". `main.tex:423–428` promotes this to the full scanned range
`kη_B∈[0.1,10]`. `results.json → equilateral/10/S-lab/total = -1215.57` is the `≈1.2×10³` §V C
`:980–982` quotes, at `kη_B=10` — where `abs_comparison/per_k/10/…/ratio_to_ABS = 2.42×10⁴` puts
the lab value **4.4 dex above** the ABS decay law. Both numbers are individually sourced; the two
sentences cannot both stand unqualified.
*Closure:* **C2** — scope `:423–428` to "squeezed configuration, at and below `k_LQC η_B ≈ 1.06`";
add a four-row table (configuration, `kη_B`, initial state, `|f_NL|`) covering `0.1…10` squeezed
and equilateral, cited from both §III and §V C; keep §V C's stress-test framing.

**DA3M-R5-03 (MAJOR) — the printed NANOGrav reference amplitude `6.3×10⁻¹⁰` is unsupported by the
paper's own artifact and inconsistent with the paper's own quoted gap.**
*Legs:* Fable M3 (integrity note).
*Class:* **GENUINELY-NEW REAL, numeric error, editorial fix.**
*Verdict citation:* `main.tex:700–707` "against NANOGrav's power-law value `6.3×10⁻¹⁰` at `f_yr` …
`10^{14.3}` (`10^{13.7}`, dust bracket)". `outputs/sigw_nhz_from_lab_spectrum_2026_09_04.json`
records `nanograv_reference/Omega_GW_h2_at_f_yr = 3.6235e-9` (from `A=2.4e-15, γ=3.2`) and
`log10_amplitude_shortfall_vs_NANOGrav_at_f_yr = 14.3416` / `13.7352`. Auditor arithmetic:
`log10(6.3e-10 / 1.4545e-23) = 13.64`, not 14.3 — the printed pair is internally inconsistent;
`log10(3.62e-9 / 1.4545e-23) = 14.40 ≈ 14.34` ✓. The rendered Fig. 1 dashed NANOGrav line sits at
`~3×10⁻⁹` near `f_yr`, agreeing with the JSON and not with the text.
*Closure:* **C3** — replace `6.3×10⁻¹⁰ → 3.6×10⁻⁹` at `:702` (state the `Ω_GW h²` convention);
the `10^14.3`/`10^13.7` gaps, abstract `:65`, `:1108` and the Fig. 1 caption need no change.

### GENUINELY-NEW REAL — MINOR

| id | finding | leg | verdict citation (source checked) | closure |
|---|---|---|---|---|
| `DA3M-R5-04` | **auditor-originated:** `:381–384` "S2 has no computable post-bounce `f^after`, so this value does not enter the combined range" is contradicted by `:482–501` ("Scheme S2, resolved", `f^after[S2]=-1.249`). A v3M.0.10 closure seam: the statement is now true only of the **LQC** background | — | `:381–384` vs `:471–473`, `:492–495` | C1 |
| `DA3M-R5-05` | abstract `:75–76` "widens the separation to `0.5–1.1σ`" vs body `:1086`, `:1131`, `:1134`, `:1172` "under `1σ`". Auditor: `\|Δf\|=0.35–0.55` over `σ=0.5–0.7` ⇒ `0.50–1.10σ`; the **body** is the wrong half (inverted residual of `DA3M-R4-05`/C5) | Fable m1, Gemini E1 | `:1172` vs Table IV `:1077` | C4 |
| `DA3M-R5-06` | `:243–245` "the first that reproduces this value from an independent, from-scratch vertex-by-vertex derivation" is contradicted two sentences earlier by `:230–231` (Li *et al.* redo the in-in calculation for general `c_s` and print the amplitude). The paper's real novelty is the **per-vertex attribution + factor-2 localization** | Gemini M1 | `:230–231` vs `:243–245` | C4 |
| `DA3M-R5-07` | the `-15/8 − (−5) = −25/8` gap accounting never states what `f^ρ_NL`, `f^c_NL` are normalised against; with `δN_c=(1-ε/3)ζ` (`:281–286`) a `δN_c`-normalised `f_NL` differs by `1/(1-ε/3)=2` at `ε=3/2` | Fable M4 (real part) | `:255–261`, App. A.2 `:1240–1252` | C4 |
| `DA3M-R5-08` | the §III A per-background table `:462–470` has no `\caption`/`\label` yet is cross-referenced as "the table in Sec. III A" | Fable m5 | `:462–470`, `:1054` | C4 |
| `DA3M-R5-09` | `:158` "All five [cubic pieces] are evaluated" vs `:453–455` "all six cubic attachments and boundary terms"; the sixth is never named | Fable m4 | `:158` vs `:453–455` | C4 |
| `DA3M-R5-10` | `:408–409` calls the finite-`k` transfer excursion `O(1)` while listing `0.058` (poly non-LQC) — a factor-17 suppression | Fable m6 | `:408–409` | C4 |
| `DA3M-R5-11` | `:1135` "the `3.13σ` apparent tension with the pre-bounce" — Table IV `:1077` gives `3.13σ` as a **forecast detection significance**, not a tension | Fable m12 | `:1077` vs `:1135` | C4 |
| `DA3M-R5-12` | Fig. 1 image carries internal labels: title "**A3-3**: … the lab's own `Δ²_ζ`", legend `MB_anchored_ns0.9649` / `pure_dust_ns1` (auditor rendered the PNG). Directive **I6** applies — regenerate the figure, do not patch text only | Fable m14a | `paper/sigw_nhz_from_lab_spectrum_2026_09_04.png` | C5 |
| `DA3M-R5-13` | source-verified typography: `:452–453` "`−5/24.` a closed-form" and `:471–473` "(below). so `\|f^after\|`" (lower-case after a full stop); "isoceles"; curly-quote `”moderate tension`; "Papanikolaou [8] derive" (single author) | Fable m15 | `:452`, `:471`, grep | C4 |
| `DA3M-R5-14` | `:1176–1177` "the not-yet-derived shape-overlap projection `r` would sharpen this somewhat but cannot by itself restore the pre-bounce-level `3σ` separation" — an uncomputed quantitative claim about an explicitly underived quantity | Gemini M3 | `:1176–1177` | C4 (bound it or drop the confidence clause) |
| `DA3M-R5-15` | **MINOR-SCIENCE:** the model's own **first-order** tensor `Ω_GW` at nHz is never stated, although Channel I compares only the induced (second-order) background and Table II's `γ=5` row is labelled "prim. tensors" | Fable m16 | `:602–622`, `:679–711` | **(ii)** — one ledger number or an explicit scope sentence |
| `DA3M-R5-16` | abstract `:57–59` prints the two-scheme band `[-1.25,-0.50]` without the "S2, Quintin-type background only" qualifier the body attaches at `:507–510` | Fable m2 | `:57–59` vs `:507–510` | C4 |
| `DA3M-R5-17` | §V C `:975–977` evaluates at `kη_B≈3` without naming the `(T_B,k)` it corresponds to. Auditor: at `T_B=10⁸ GeV`, `k_B=1.714×10¹⁵` ⇒ `k=5.1×10¹⁵ Mpc⁻¹`, inside the paper's own PBH band — legitimate, but unstated | Fable m7 (residual) | `sigw…json → transfer_validity` | C4 |
| `DA3M-R5-18` | the `1.7–1.9` ratio's conditionality on the unresolved Choudhury sign disagreement (`:864–870`) is stated only in §V B; and whether any of the 27 grid points fall at `γ_cr ≲ 0.85` is not reported | Fable M5 (residual) | `:838–870` | **(ii)-lite** — one re-run of `pbh_compaction_fnl.py` printing `γ_cr` per grid point, then a one-clause statement |

### REAL residual of an open earlier item (not counted genuinely-new)

| id | status | leg | citation |
|---|---|---|---|
| `DA3M-R4-11` *(C7 still incomplete)* | in-body "this lab's" at `:63, :557, :560, :604, :679, :937, :1105`; internal history at `:421` ("correcting an earlier statement in this program") and `:482` ("An earlier version of this program reported"). Paths **inside** the reproducibility statement (`:1328, :1337–1341`) are sanctioned and are NOT defects — Gemini's blanket scrub declined | Gemini E4, Grok N2 | `grep -nE 'research/\|this lab\|directive Q' main.tex` = 14 hits |
| `DA3M-R4-12` *(C5 pending)* | `Ω_DM = 0.674` footnote (h mis-used as `Ω_DM`) still propagates into the tabulated `f_PBH` and Fig. 2 | Fable m8 | `:780–789` |
| `DA3M-R2-11` *(carried)* | frozen-release DOI — Houston-gated P-round packaging action, disclosed in the reproducibility statement. Carried, not re-counted | Gemini E3 | reproducibility statement |

### RE-FLAG-OF-DISCLOSED

| id | finding | leg | disposition (source-cited) |
|---|---|---|---|
| `DA3M-R5-R1` | "official vs refit `σ` juxtaposed without a *not directly comparable* qualifier" | Grok E2, Gemini E2 | `:560–588`: official is "the primary comparison", refit is "a secondary, differently-conditioned cross-check", with both intervals' types printed. = `DA3M-R3-R2`/`R4-R2`, **3rd–4th recurrence**. Optional 1-line Table II caption add (C4) |
| `DA3M-R5-R2` | "no second-order `δN` cross-check; in-in treated as unique truth" | Grok M3 | `:286–292` — at second order the map is a non-local `∂⁻²` diffeomorphism, so **no local `f_NL` relation exists**; a second-order `δN` number is not a well-defined comparator. = `DA3M-R3-R1`/`R4-R1` |
| `DA3M-R5-R3` | "the Quintin Eq. (79) factor is constant by construction ⇒ not a check" | Fable m11 | `:411–415` already says exactly that, and that it is "not definable as a matter-sector effect on the two effective-fluid backgrounds" |
| `DA3M-R5-R4` | "`1.732±0.050 (n=27)` std understates the prior volume; report the range" | Grok M2 | `:838–842` gives the std over the 27 points **and** "a result within a stated regime, not a claim of general validity"; the abstract already quotes the **range** `1.7–1.9`. Grok's "four `r_p` values" misreads a 3×3×3 grid. = `DA3M-R4-R4` |
| `DA3M-R5-R5` | "`B=5×10⁻⁴` from 9 samples cannot carry `±0.2` dex" | Fable m9 | `:596–600` already refuses a `γ=5` factor outright and quotes the `13/3` factor **to one significant figure** for that reason |
| `DA3M-R5-R6` | "Fig. 2's `f_PBH > 1` region is unphysical" | Fable m14b | Table III caption `:872–877`: "the ***nominal (uncapped)*** `f_PBH` columns — evaluated at the Gaussian-calibrated amplitude `A_*` with no upper cutoff applied" |

### FALSIFIED (each against a committed source or the auditor's own arithmetic)

| id | claim | leg | falsifying source |
|---|---|---|---|
| `DA3M-R5-F1` | "the abstract presents `-35/16` as the exact, **scheme-independent** amplitude" | Grok E1 | abstract `:52–59` reads "Transmission through the bounce is **scheme-qualified** … a two-scheme band, `[-1.25,-0.50]`, **not S1 alone**". "Exact" attaches to the pre-bounce in-in amplitude (`:158–164`, two literature reproductions "Both match exactly"), never to transmission. = `DA3M-R4-F1`/`R3-F1`, recurrence |
| `DA3M-R5-F2` | "`f_PBH=0` holds only after the Gaussian-calibrated truncation; Table III shows non-zero" | Grok E3 | abstract `:70–72` conditions on "fed the lab's predicted spectrum"; `:966–968` `f_PBH` is "exactly zero in double precision at every point". Table III's non-zero columns are the disclosed "nominal (uncapped)" values at `A_*` (`:872–877`) — a different object (required-amplitude calibration, not the lab spectrum). = `DA3M-R4-F2`/`F4` family |
| `DA3M-R5-F3` | "no single reproducible central value per background; forecasts cannot be recomputed" | Grok M1 | `:462–470` tabulates `(T_fNL, Δf^bounce, f^after)` per background — `0.165/-0.140/-0.501`, `0.250/-0.104/-0.651`, `0.196/-0.127/-0.555`; Table IV gives per-candidate significances |
| `DA3M-R5-F4` | "the title contains the future date September 4, 2026" | Grok N1 | today **is** 2026-09-04 (`:19 \paperTimestamp`). Auto-FALSIFY Rule 3. **9 consecutive rounds, 100 % falsified** = `DA3M-F3` |
| `DA3M-R5-F5` | "Eq. (1) and Eq. (3) are identical; one is redundant" | Grok N3 | `:151–153` is the `f_NL^local` **definition**; `:171–174` is the boxed `-35/16` **result** |
| `DA3M-R5-F6` | "Fig. 1's caption cites a commit hash that post-dates the paper's date" | Grok N4 | caption `:729–740` contains no hash; it cites `outputs/sigw_nhz_from_lab_spectrum_2026_09_04.json` |
| `DA3M-R5-F7` | "Fig. 1's y-axis has tick values but no physical label or units" | Gemini N1 | auditor **rendered** `paper/sigw_nhz_from_lab_spectrum_2026_09_04.png`: the y-axis reads `Ω_GW h²`, the x-axis `f [nHz]` |
| `DA3M-R5-F8` | "`(the the shift…)` and `(the the T₃ bulk coupling…)` duplicate words in App. A 2" | Gemini N2 | `grep -n "the the" main.tex` → **0 hits**; `pdftotext main.pdf \| grep -i "the the"` → **0 hits**. The quoted text does not exist in the manuscript (fabricated quotation — record, do not act) |
| `DA3M-R5-F9` | "`r` is imported from an unpublished companion draft for a load-bearing parameter" | Gemini M2 | `:1170–1177` quotes **no numeral** for `r`; Table IV reports bare significances. = `DA3M-R3-F7`, recurrence. (The internal-path half is `DA3M-R4-11`, still open) |
| `DA3M-R5-F10` | "`kη_B≈3` corresponds to `T_B~10⁶ GeV`, which §V C excludes" | Fable m7 | `sigw…json → transfer_validity/k_B_Mpc-1["T_B=1e8 GeV"] = 1.7143e15` ⇒ `kη_B=3` at `k=5.14×10¹⁵ Mpc⁻¹`, inside the paper's own `10¹⁵–10¹⁶ Mpc⁻¹` PBH band at the stated `T_B ≳ 10⁸ GeV`. Only "say which `(T_B,k)`" survives (`DA3M-R5-17`) |
| `DA3M-R5-F11` | "run the paper's code at Choudhury *et al.*'s stated parameter set" | Fable M5 (primary ask) | `:864–870` — their spectrum is "unreproducible"; the demanded re-run is unsatisfiable by construction = `DA3M-R3-R3`. Residual survives as `DA3M-R5-18` |

### OPINION / GENRE (venue pass only — never a correctness finding)

| id | item |
|---|---|
| `DA3M-R5-G1` | "a `5.1σ` slope tension for a signal 14 decades down is not a test" (Fable m10) — abstract `:65–66` and `:709–711` already call it a null and print the amplitude gap beside it |
| `DA3M-R5-G2` | Table II's `γ=5` "prim. tensors" row is visually confusable with `γ_pred=5.07` (Fable m13) |
| `DA3M-R5-G3` | expand App. A.1 into a full derivation (Fable M4 tail) — the identity's derivation route is stated at `:286–290`; genuine improvement, not a defect |
| `DA3M-R5-G4` | missing-reference wish-list: Sasaki–Stewart, Lyth–Malik–Sasaki, Salopek–Bond, Brandenberger–Peter, the SPHEREx `σ=0.5` primary source (Fable, references section) — the last one is worth acting on with C4 |
| `DA3M-R5-G5` | self-referential register / 14 pp length (Grok summary, Gemini E4 genre half) |
| `DA3M-R5-G6` | Grok's "reconsider after (i)(ii)(iii)" framing rests on F1+F2+F3 and carries no separate content |

---

## 3. CLOSURE PLAN

### (i) Editorial / real edits — closable in **v3M.0.12** by a Sonnet lane, no new science

All line numbers are `research/track_a3_multichannel/paper/main.tex` @ v3M.0.11. Directive G applies
(bump `\paperVersion`→`v3M.0.12`, keep `\paperTimestamp` at today, recompile 0 undef-refs, re-mirror
byte-identical to every served path, Convex `paperVersions:bump`, three-way md5 check).

| id | edit |
|---|---|
| **C1** | `DA3M-R5-01` + `DA3M-R5-04`. Abstract `:52–56`: tag the bound "(scheme S1, assumption (A4))". `:359–361`: change "within this handoff scheme, linear transfer can only suppress …" to name (A4)+S1 and add one sentence: S2's raw-ADM continuation lies outside (A4) and transmits with `T_fNL ≈ 1.03` (from `\|λ_ζ\|=0.97`, `:498–499`). `:377–379`: "three backgrounds × two conventions (S1 rows only)". `:381–384`: scope "S2 has no computable post-bounce `f^after`" to **the LQC background**. `:462–470`: add the S2/Quintin row `(T_fNL≈1.03, Δf^bounce not separately regulated, f^after=-1.25)` |
| **C2** | `DA3M-R5-02`. `:423–428`: scope to "squeezed configuration, at and below `k_LQC η_B≈1.06`" (source: `LANE9C2…md:255–261`). Insert a small table (config, `kη_B`, initial state, `\|f_NL\|`) from `lane9c2_lqc_modes/results.json` (`abs_comparison/per_k` squeezed; `equilateral/*/S-lab/total` = `-0.539, -5.158, -9.807, -111.97, -1215.57`), referenced from `:428` and `:980` |
| **C3** | `DA3M-R5-03`. `:702`: `6.3\times10^{-10}` → `3.6\times10^{-9}` (`Ω_GW h²`, from `nanograv_reference/Omega_GW_h2_at_f_yr`). Leave `10^{14.3}`/`10^{13.7}`, `:65`, `:1108`, Fig. 1 caption unchanged |
| **C4** | `DA3M-R5-05..11`, `13`, `14`, `16`, `17`, `R1`, `G4`: body "under `1σ`" → "`0.5–1.1σ`" at `:1086, :1131, :1134, :1172`; narrow the `:243–245` novelty claim to per-vertex attribution; define `f^ρ_NL`/`f^c_NL` normalisation at `:255–261`+App. A.2; `\caption`+`\label` the `:462–470` table and fix `:1054`'s cross-ref; name the sixth cubic attachment at `:453–455` (or reconcile with `:158`); reword `:408` `O(1)`→"factor `0.06`–`2.2`"; `:1135` "apparent tension"→"forecast detection significance"; fix `:452` / `:471` sentence breaks, "isoceles", the curly quote, "Papanikolaou … derives"; bound-or-drop `:1176–1177`; qualifier "(S2, Quintin-type only)" in abstract `:57–59`; add "(at `T_B=10⁸ GeV`, `k≈5×10¹⁵ Mpc⁻¹`)" at `:975`; one clause in the Table II caption; cite the actual SPHEREx `σ=0.5` source |
| **C5** | `DA3M-R5-12` + `DA3M-R4-12`. **Directive I6:** regenerate `sigw_nhz_from_lab_spectrum_2026_09_04.png` from its generator with a publication title/legend (no "A3-3", no `MB_anchored_ns0.9649`); re-mirror byte-identical; verify by **rendering the figure page**. Close the `Ω_DM=0.674` footnote residual |
| **C6** | `DA3M-R4-11` (C7 residual). Replace in-body "this lab's" (`:63, :557, :560, :604, :679, :937, :1105`) with neutral wording; delete the internal-history clauses at `:421`, `:482` (keep the physics, drop "an earlier version of this program"). Paths inside the reproducibility statement stay. Gate: `grep -nE 'this lab\|earlier version of this program\|earlier statement in this program' main.tex` returns hits only inside the reproducibility statement |
| **C7** | **LaTeX overfull (baseline, >10 pt).** `main.log`: `56.74pt` @ `:697` — split Eq. `gammapred` (`:693–697`) into a two-line `gathered`/`split` instead of one `\qquad`-joined line; `16.76pt` @ `:697–711` — the following paragraph inherits it, re-check after the equation fix; `14.58pt` @ `:1240–1253` — App. A.2 `tabular{lp{2.9cm}p{2.3cm}}`: narrow to `p{2.6cm}p{2.1cm}` or wrap in `\small`. Re-run `/latex-audit` and confirm 0 overfull > 10 pt |

### (ii) SCIENCE — needs a ledger computation before it can be written

| id | item | what must be computed | cost |
|---|---|---|---|
| `DA3M-R5-15` | the model's own **first-order** tensor `Ω_GW h²` at nHz | the matter-bounce first-order tensor spectrum on the same background + the same nHz propagation as `sigw_nhz_from_lab_spectrum.py`; report it beside the induced background in §IV D and Table II, or state explicitly why Channel I compares only the second-order piece | small, local CPU (minutes); one new JSON in `outputs/` |
| `DA3M-R5-18` | the `1.7–1.9` ratio's exposure to the Choudhury sign disagreement | re-run `pbh_compaction_fnl.py` printing `γ_cr` at each of the 27 grid points; report how many (if any) fall at `γ_cr ≲ 0.85`, then state the ratio's conditionality outside §V B (abstract or Table III caption) | small, local CPU (minutes); extend the existing results JSON |

Both are lab-local and cheap; **neither blocks C1–C7**, and neither requires GPU/RunPod.
No item in this audit requires new physics beyond these two.

---

## 4. Convergence statement (R5)

**NOT converged.** 18 genuinely-new REAL findings (3 MAJOR + 15 MINOR) are outstanding on the exact
v3M.0.11 PDF, plus 2 real residuals of open R4 items and 1 carried packaging item. Clean-wave count
**reset to 0**. Three of the MAJORs are editorial-with-a-numeric-core (a printed reference amplitude
contradicted by the paper's own artifact; a bound printed without the assumption that makes it true;
a scan result promoted beyond its source's stated window) — none is a physics error in the
computations themselves: every number this auditor re-derived from the committed JSONs
(`headline/S2_f_NL_after_mean`, the S1 per-background table, `log10_amplitude_shortfall`,
`equilateral/*/total`, `transfer_validity/k_B`) reproduces. Directive R2 note: this is A3M's second
consecutive review round; after v3M.0.12 closes C1–C7 the remaining lane must be the **(ii)** science
items and the `NEXT_SCIENCE_LEDGER`, not a third verdict-word round.
