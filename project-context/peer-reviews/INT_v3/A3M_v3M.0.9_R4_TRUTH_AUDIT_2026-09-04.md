# A3M v3M.0.9 — R4VERIFY truth audit (independent, verdict-first)

- **Round:** `ROUND_2026-09-04-A3M-v3M.0.9-EXACTPDF-6c543e5e-R4VERIFY`
- **Manuscript:** `research/track_a3_multichannel/paper/main.tex` + `main.pdf`, v3M.0.9, 12 pp
- **sha256 (re-verified this session):**
  `6c543e5e9885c6db58e07576482ed6f283b0307ad1499c6309a4651d3c26fb1a`
  — `shasum -a 256 site/public/papers/a3_multichannel_arxiv_v3M.0.9.pdf` matches the board and
  every leg header.
- **Board:** `INT_v3/A3M_v3M.0.9_R4_BOARD_2026-09-04.md`
- **Prior canon:** `DISPOSITIONS/A3M.md`; `INT_v3/A3M_v3M.0.8_R3_TRUTH_AUDIT_2026-09-04.md`
  (ids `DA3M-R3-*`, closures C1–C10 → v3M.0.9).
- **Auditor:** skeptical in both directions, told no expected outcome. Every verdict below is
  decided from a source — a `.tex` line, a committed script or JSON, an arXiv abstract fetched
  this session, or the auditor's own arithmetic — never from a leg's verdict word.
- **Protocol:** `/peer-review-truth-audit` + `/bigbounce-truth-audit`, patterns 061–066,
  directive H-refined, directive R2.

---

## 0. Independent verification performed by this auditor

Nothing in §2 is graded on a reviewer's say-so.

| Object | Command / source | Result |
|---|---|---|
| PDF binding | `shasum -a 256` on the served mirror | `6c543e5e…6fb1a` ✓ matches board + all leg headers |
| Leg census | board §"Leg census"; `api_legs_run.log` | 3 legs present, 0 `Reviewer call FAILED`, OpenAI + Perplexity **ABSENT** (recorded, never as clean) |
| Eq. (7) closed form | `f^{after} = -(85/48)T - 5/24` re-derived from `T(-35/16) - (5/24)(1-2T)` | `-85/48 = -1.770833` ✓; rows `T=0.165→-0.5005`, `0.250→-0.6510`, `0.196→-0.5554` reproduce the printed `-0.501/-0.651/-0.555` ✓ |
| `T=0.409` provenance | `research/cubic_bounce_transmission/a2_transmission_linear.json` + `A2_TRANSMISSION_BRIEF_2026-09-02.md` §4.1 row 4 | `0.409155` is **LQC background, scheme S2 (effective fluid)** — a *scheme variant of the same LQC background*, **not** a fourth background |
| S2 exclusion legitimacy | `main.tex:424–427`; brief §4.3 "Fluid-scheme pathology reproduced" (`K ~ d_cut^{-0.4998}`) | S2's `Δf_NL^bounce` is **divergent with no regulated value**, so `f_NL^after` is **not computable** for the `T=0.409` row ⇒ excluding it from the combined range is physics-legitimate |
| Post-bounce power spectrum under `\|r\|≫1` | brief §4.3 "Matter-bounce benchmark recovered": `Δ² ∝ k³\|α_post\|²` flat across the k grid to **1.2–4.2 %** | scale invariance survives `\|r\|≫1`; the reviewer's contrary worry is falsified |
| `T_fNL` meaning | brief §3: local ansatz uniformly rescaled by `λ(η_h)=ζ(+∞)/ζ(-η_h)` ⇒ `f_NL→f_NL/λ`; §4.1 gives `λ_ζ=4.0` at `T=0.250` | `T_fNL = 1/λ_ζ` exactly ✓ — it is the **f_NL** transfer; ζ *grows* by λ, which is why f_NL is suppressed |
| nHz ↔ k | `k = 2πf/c`, `f = 10⁻⁸ Hz`, `c = 9.716×10⁻¹⁵ Mpc/s` | `k ≈ 6.5×10⁶ Mpc⁻¹` — **above** Papanikolaou's `k<10⁴ Mpc⁻¹` scale-invariant range and **inside** §V C's flat extrapolation |
| Papanikolaou 2025 (arXiv:2504.11641) | abstract fetched this session | "nearly scale-invariant … on scales `k<10⁴ Mpc⁻¹`" **plus** "naturally enhanced curvature perturbations on very small scales", which "induce GWs … and collapse as well to form PBHs", with "a universal infrared (IR) frequency scaling of `f²`" |
| Ref. [9] identity | arXiv:1909.13728 abstract fetched this session | **"Universal infrared scaling of gravitational wave background spectra"**, Cai/Pi/Sasaki, PRD **102**, 083528 (2020) — the paper prints the title of the *other* Cai–Pi–Sasaki paper (PRL 122, 201101 (2019), arXiv:1810.11000) |
| Appendix A general-ε algebra | auditor re-derivation | monopole `-5(ε-3)(ε-6)/18` → `-15/8` at ε=3/2 ✓; isosceles `-5(ε²-6ε+12)/12` → `-35/16` ✓; μ² coeff `5ε²/12` → `15/16` ✓; gap `5ε(9-ε)/18` → `25/8` ✓. **All internally consistent; no fabrication.** |
| Angular decomposition | `(15/16)μ² = (15/16)[⅓ + (⅔)P₂]` | ℓ=2 Legendre coefficient is `5/8`, **not** `15/16` |
| Table IV arithmetic | `\|f^after\|/σ` at σ = 0.7/0.5/1.0 | `[0.50,0.65]→0.71–0.93 / 1.00–1.30 / 0.50–0.65` ✓; `[0.86,1.20]→1.23–1.71 / 1.72–2.40 / 0.86–1.20` ✓ — every printed cell reproduces |
| PBH shortfall | `outputs/inlab_delta2_zeta_2026-09-03.json → per_mass_scale…log10_ratio` | `7.020` (−35/16) and `6.748` (−35/8) at `M_H=10¹⁵ g` — the printed single value "7.0 … at both candidate f_NL values" is the −35/16 number |
| DESI z-scores | `(-2.1875+3.6)/9.0 = 0.157`; `(3.5+2.1875)/7.4 = 0.768` | printed `0.16σ` / `0.77σ` ✓ — computed against the **pre-bounce** amplitude |
| Fig. 1 | rendered `paper/pbh_compaction_fnl.png` | **no color bar exists**; axis labels consistent; `A` is dimensionless |
| Directive-Q1 residue | `grep -nE 'research/\|this lab.s\|directive Q' main.tex` | in-body/appendix hits at `:230`, `:566`, `:793`, `:855`, `:1022`, and `directive Q2` at `:1163` — C8's own verification gate ("hits only inside the reproducibility statement") is **not met** |

---

## 1. Class counts

### Per leg (raw findings → class)

| leg | raw findings | REAL (new) | REAL (residual) | RE-FLAG | FALSIFIED | OPINION/GENRE |
|---|---|---|---|---|---|---|
| Claude Fable INT (`major-revisions`) | 15 (5 MAJOR + 10 minor; minor 11 is a reference-verification confirmation, not a finding) | 10 | 1 | 3 | 2 sub-claims (inside M1, M3) | 1 |
| Grok API (`REJECT`) | 10 (4 E / 3 M / 3 N) | 1 | 1 | 2 | 5 | 1 |
| Gemini API (`MAJOR REVISIONS`) | 5 (2 E / 1 M / 2 N) | 2 | 1 | 1 | 1 | 0 |
| OpenAI / Perplexity | **ABSENT** (directive N pause / optional leg) — never faked, never counted clean | — | — | — | — | — |

### Canonical (after cross-leg fingerprint dedup and matching against `DISPOSITIONS/A3M.md`)

**15 outstanding REAL items** = **13 genuinely-new** (3 MAJOR + 10 MINOR) + **2 residuals of R3
items whose closures were incomplete** (`DA3M-R3-11`, `DA3M-R3-09`), plus **1 auditor-originated**
item included in the 13. Also: **5 RE-FLAG-OF-DISCLOSED**, **8 FALSIFIED**, **3 OPINION/GENRE**,
**1 carried-open packaging** (`DA3M-R2-11`), **0 BLOCKER**, **0 OUT-OF-SCOPE-disclosed**.

**Clean-wave count: 0.**

---

## 2. Canonical numbered findings

Severity is read from each leg's own per-item tag, never from its verdict word.

### GENUINELY-NEW REAL — MAJOR

---

**DA3M-R4-01 (MAJOR) — the quoted transfer interval `0.165–0.409` mixes schemes S1 and S2, while
every `f_NL^after` number downstream is S1-only, and the paper never says the `0.409` row is
excluded or why.**
*Legs:* Fable MAJOR 1; Grok E2 (same defect, reached from the "scheme-dependent by construction"
side).
*Classification:* **GENUINELY-NEW REAL — but narrower than either leg states.**
*Verdict citation, in three parts:*

1. **What `0.409` is.** `a2_transmission_linear.json` / `A2_TRANSMISSION_BRIEF_2026-09-02.md` §4.1
   row 4: `T = 0.409155` is the **LQC effective-dust background under scheme S2 (effective fluid,
   `z² = a²(ρ+p)/(c_s²H²)`)**. It is a *mode-function-convention variant of the LQC background
   already in the table at `T = 0.250` (S1)* — **not a fourth background**. `main.tex:352–356`
   says exactly this ("two mode-function conventions (geometric vs. effective-fluid) on the
   *same* LQC background"). The abstract's "`0.165`–`0.409` across three backgrounds"
   (`main.tex:53–54`) is therefore the sentence that is wrong: the interval spans three
   backgrounds **× two schemes**.
2. **Whether excluding it is legitimate — YES.** `main.tex:424–427`: scheme S2 "gives a divergent
   `Δf_NL^bounce` with no regulated value (`d_cut⁻¹` scaling as `d_cut→0`, the cubic-order
   restatement of the linear-order `z²` pathology) and is reported as a non-result"; brief §4.3
   reproduces the pathology numerically (`K ~ d_cut^{-0.4998}`, analytic `−1/2`). Because
   `f_NL^after = T·f_NL^before + Δf_NL^bounce` needs **both** pieces in the **same** scheme, the
   S2 row has **no computable `f_NL^after`**. The S1-only combined range `[-0.65,-0.50]` is the
   correct object.
3. **What is actually defective.** The paper never states (2) *beside the range*. A referee reading
   the abstract sees `T ∈ [0.165,0.409]` and `f_NL^after ∈ [-0.65,-0.50]` in the same sentence and
   cannot reconcile them — both legs independently failed to, which is the evidence that the
   omission is real.

*Falsified sub-claim (recorded as `DA3M-R4-F7` below):* Fable's demanded alternative — "widen the
range to `[-0.93,-0.50]`" — is **not available**: `-0.93` is obtained by feeding the **S2**
transfer into the **S1** cubic formula, a scheme mix the paper's own §III B forbids.
*Required closure:* **C1** (editorial; no computation).

---

**DA3M-R4-02 (MAJOR — SCIENCE) — the `γ=3` justification in §IV D and the PBH null in §V C assume
mutually inconsistent primordial spectra, and the source the `γ=3` attribution rests on gets PBHs
from its spectrum.**
*Legs:* Fable MAJOR 2.
*Classification:* **GENUINELY-NEW REAL, MAJOR, SCIENCE (closure-induced by R3's C4).**
*Verdict citation:*

- `main.tex:585–597` (§IV D, added by C4): "`Ω_GW ∝ P_R²` (Papanikolaou's Eq. (30)) combined with
  the source spectrum's own near-linear low-`k` growth **`P_R ∝ k`** (Eq. (8) there) gives
  `Ω_GW ∝ k² ∝ f²`".
- `main.tex:801–812` (§V C): the model's spectrum is "a near-scale-invariant power law,
  `n_s−1 = 12w/(1+3w)` … `n_s = 0.9649`, **extrapolated across the 10–15 decades to PBH scales**".
- These are different spectra. A flat `P_R` through the standard radiation-era induced-GW kernel
  gives `Ω_GW ∝ f⁰` (log-corrected), i.e. `γ = 5` in this paper's own convention
  `Ω_GW ∝ f^{5−γ}` (`pta_gamma_reproduce.py:22–31`) — the very row §IV disfavours at
  `3.1σ`/`4.63σ`.
- The nHz band sits at `k ≈ 6.5×10⁶ Mpc⁻¹` (auditor computation, §0), i.e. **inside** §V C's
  extrapolated region and **above** the `k < 10⁴ Mpc⁻¹` range over which Papanikolaou's spectrum
  is scale-invariant.
- Papanikolaou's abstract (fetched this session) is explicit that his `f²` IR tail belongs to a
  spectrum with "naturally enhanced curvature perturbations on very small scales" which "induce
  GWs … **and collapse as well to form PBHs**". The paper borrows his slope while asserting a
  spectrum that has no such enhancement — and §V C's headline is that the model's spectrum
  produces **no** PBHs (7 decades short). The two channels cannot both be describing this model.

This is load-bearing in both directions: if §V C's flat spectrum is the model, Channel I's `γ=3`
loses its stated derivation (and the honest reading is `γ≈5`, which the PTA data disfavour — a
channel-level *tension*, not a consistency); if the model carries Papanikolaou's small-scale
enhancement, §V C's null is not the model's prediction.
*Required closure:* **SCIENCE item — see CLOSURE PLAN (ii), ledger `A3-3`.** Not editable.

---

**DA3M-R4-03 (MAJOR → editorial) — Eq. (6) is asserted with three undefined symbols, an unstated
definition, and no pointer to its derivation.**
*Legs:* Fable MAJOR 3 (sub-claims a/b/c).
*Classification:* **GENUINELY-NEW REAL (MAJOR presentation defect); sub-claim (c) FALSIFIED.**
*Verdict citation:*
(a) **REAL.** `main.tex:334–344` calls `T_fNL` "the transmitted **bispectrum** amplitude". It is
not: brief §3 derives it as the **f_NL** transfer, `T_fNL = 1/λ_ζ` with
`λ_ζ = ζ(+∞)/ζ(−η_h)` — verified exactly by the auditor (`λ_ζ = 4.0` ↔ `T = 0.250`,
`5.1151 ↔ 0.1955`, `6.0604 ↔ 0.1650`, brief §4.1). The physical content the paper omits is that
**ζ grows** through the bounce by `λ`, which is *why* `f_NL` is suppressed — without that sentence
the reader (correctly, per Fable) computes that a rescale `ζ→Tζ` would *enhance* `f_NL`.
(b) **REAL.** `𝒜`, `I_∞`, and the origin of the `1+2r` denominator appear nowhere in the paper;
all three are defined in brief §3 (`α_-`, `β_-`, `C_1 = α_-(1+r)`, `C_2 = β_-`).
(c) **FALSIFIED** (→ `DA3M-R4-F8`): brief §4.3 "Matter-bounce benchmark recovered" shows the
post-bounce `Δ² ∝ k³|α_post|²` is **flat to 1.2–4.2 %** across the k grid under `|r| ≫ 1`. Scale
invariance is not spoiled, so `n_s = 0.9649` in §V C is not in conflict with §III on this ground.
*Required closure:* **C3** (transcription from the committed brief; no new science).

---

### GENUINELY-NEW REAL — MINOR

| id | item | leg(s) | verdict citation (source checked) | closure |
|---|---|---|---|---|
| **DA3M-R4-04** | Ref. [9] carries the wrong title | Fable M4 | `main.tex:1215–1217` prints "Gravitational Waves Induced by non-Gaussian Scalar Perturbations" with `PRD 102, 083528 (2020)`/`arXiv:1909.13728`. arXiv:1909.13728 (fetched) is **"Universal infrared scaling of gravitational wave background spectra"**, Cai/Pi/Sasaki, PRD 102, 083528 (2020). The printed title belongs to PRL **122**, 201101 (2019), arXiv:1810.11000. The identifiers match the citation's *use* (the IR causal floor); only the title is wrong — a merged bib record. | C4 |
| **DA3M-R4-05** | the abstract quotes only Table IV's *bispectrum-only* row, without that qualifier, and asserts "under `1σ` apart" which the paper's own `P+B` row reaches `1.1σ` | Gemini E1 | Abstract `:70–73` gives `0.7–0.9σ` / `1.2–1.7σ`; Table IV `:915–918` gives `1.0–1.3σ` / `1.7–2.4σ` for `SPHEREx, P+B target`. Body `:930–933`: `\|Δf^after\| ≈ 0.35–0.55` against `σ = 0.5–0.7` ⇒ separation `0.50–1.10σ` — **above `1σ` at the `σ=0.5` endpoint**. Gemini's read that the abstract picks the more favourable framing is supported by the paper's own table. Directive-F adjacent (headlining the more-favourable of two tabulated values): must not survive to submission. | C5 |
| **DA3M-R4-06** | "a monopole `−15/8` and a **quadrupole** `15/16`" mislabels the `μ²` coefficient | Fable m1 | `main.tex:176` and the App. A decomposition table (`:1063–1073`). `(15/16)μ² = (15/16)[⅓ + (⅔)P₂]` ⇒ the ℓ=2 Legendre coefficient is `5/8`. The monopole `−15/8` is correct. One-word fix ("`μ²` coefficient"). | C5 |
| **DA3M-R4-07** | "`T_B ≳ 10⁸–10¹⁰ GeV` — **seven** decades above the BBN scale used to bound the mass range elsewhere in this section" | Fable m2 | `main.tex:813–816` (text added by R3's **C2**). `10⁸ GeV` vs BBN `~1 MeV = 10⁻³ GeV` is **11** decades, and no other part of §V uses a BBN bound (`grep` on §V returns no second BBN use). Closure-induced error. | C5 |
| **DA3M-R4-08** | "a shortfall of **7.0** orders of magnitude … at both candidate `f_NL` values" | Fable m3 | `outputs/inlab_delta2_zeta_2026-09-03.json → per_mass_scale["M_H=1e15 g"].required_over_delivered`: `log10_ratio = 7.020` (`−35/16`) and `6.748` (`−35/8`). The single printed value is the `−35/16` number; "at both values" is not supported at one decimal. Quote a range or state which value `7.0` belongs to. (The 7-decade *conclusion* is untouched.) | C5 |
| **DA3M-R4-09** | Appendix A's general-`ε` formulas are printed with no domain of validity and do not reduce to the slow-roll/Maldacena result | Fable M5(b) | `main.tex:1099–1112`. At `ε→0`: `f^ρ = 5(ε−7)/8 → −35/8`, `f^c = −5`, and the in-in isosceles `−5(ε²−6ε+12)/12 → −5`; Maldacena's `(5/12)(1−n_s) → 0`. The formulas are correct **on the non-attractor growing branch** (`ζ̇ = −3ζ/η`, the branch the whole §II construction uses) and only there — the appendix must say so. Auditor re-derived every reduction at `ε = 3/2` and all four match the body (§0). | C5 |
| **DA3M-R4-10** | the abstract's "explained at the equation level"/"recorded identity whose mechanism is not derived" is read in opposite directions by two independent legs | Fable M5(a) + Gemini N2 | `main.tex:44–49` vs App. A `:1093–1098` ("a computed identity, **not a claimed mechanism**"). Fable reads it as over-claiming ("explained" ≠ "mechanism not derived"); Gemini reads it as under-claiming ("if it is computed, it is mathematically derived"). Both cannot be right, which is the diagnosis: the sentence is ambiguous, not false. Fix: say what is true in plain words — the linear-order relation is **derived** (App. A.1), the second-order coefficient is **computed and recorded** but its **physical mechanism is not identified**. | C5 |
| **DA3M-R4-13** | Table II has no `γ = 2` row although §IV D and §VII B now make the `γ = 2` causal floor a central comparator | Fable m5 | `main.tex:585–591` (the C4 text) introduces `Ω_GW ∝ f³` (`γ = 2`) as the universal floor; Table II lists only `γ = 3`, `13/3`, `5`. The comparison the paper now asks the reader to make is not tabulated. Mechanical: `pta_gamma_reproduce.py` already computes the z-distance and Savage–Dickey factor for an arbitrary `γ_*`. **Do not import the referee's quoted `3.3σ`/`1.5σ` — re-run the script and print what it emits.** | C6 |
| **DA3M-R4-14** | the §VI A DESI z-scores use one side of an asymmetric error without saying which | Fable m9 | `main.tex:869–876`. Auditor reproduced both: `(−2.1875+3.6)/9.0 = 0.157` (upper side) and `(3.5+2.1875)/7.4 = 0.768` (lower side) — the method is **correct**, just unstated. One clause. | C5 |
| **DA3M-R4-15** *(auditor-originated; no leg raised it)* | §VI A compares DESI DR1 to the **pre-bounce** `−35/16`, while §VI B declares the **transmitted** range "this paper's observable prediction for Channel III" | — | `main.tex:869–872` ("The prediction of Eq. (6) sits `0.16σ` from the former…") vs `:880–887`. Internal inconsistency introduced by R3's **C1(a)**, which converted the forecast half of Channel III to the transmitted amplitude and left the current-constraint half on the pre-bounce value. Not load-bearing — auditor recomputed at `f^after = −0.55`: `0.34σ` and `0.55σ`, still consistent under both priors — but the paper must use one convention or state why the two halves differ. | C5 |

---

### REAL — OUTSTANDING RESIDUAL (R3 item, closure incomplete; not counted as genuinely-new)

| id | item | leg(s) | verdict citation | closure |
|---|---|---|---|---|
| **DA3M-R4-11** *(residual of `DA3M-R3-11`; C8 incomplete)* | directive-Q1 material survives in the body, the appendix, and the reproducibility statement | Gemini M1 + Grok N2 (2-leg convergence) | C8's own verification gate was `grep -nE 'research/\|earlier draft\|supersed…' main.tex` → "hits only inside the reproducibility statement". Actual hits: `:566` and `:793` and `:855` (in-body `research/track_a3_multichannel/…` paths), `:1022` (in-appendix `research/theory_audit/…`), `:230` ("is this paper's own adjudication"), and — **new instance** — `:1163` "consistent with this lab's standing reproducibility policy (**directive Q2**)", an internal lab directive name printed in the manuscript. Gemini's additional targets: `:1157` "this lab's companion **P2** Zenodo record" (internal paper numbering) and `:891–894` "this lab's companion Fisher-forecast draft". *Scope note:* paths **inside the reproducibility statement** are C8-sanctioned and are **not** defects — Gemini's blanket demand to scrub them is declined; the in-body/appendix ones and `directive Q2`/`P2` are. | C7 |
| **DA3M-R4-12** *(residual of `DA3M-R3-09`; C7 incomplete)* | the `Ω_DM` footnote still asserts "Every result in this section is unaffected … so no number here changes with the correct value" | Fable m8 | `main.tex:780–789`. The **ratio** claim is true (`Ω_DM` cancels in Eq. (13) — verified structurally, and `pbh_compaction_fnl.py:267` enters `f_PBH` as `1/Ω_DM` multiplicatively). The **tabulated `f_PBH`** claim is false: `A_*` is calibrated so the Gaussian case gives `f_PBH = 1`, so correcting `Ω_DM 0.674 → 0.264` shifts `A_*` (R3 auditor's re-run: `0.131446 → 0.127901`, `−2.70 %`) and `f_PBH` depends **exponentially** on the amplitude, so the shift does not cancel (R3 re-run: `3.6e−14 → 6.3e−15`, `1.6e−2 → 5.7e−3`). R3's C7 chose option (a) (narrow the claim) but the printed wording still asserts option (b)'s conclusion. Directive I6 applies if (b) is taken: `pbh_compaction_fnl.png` renders `f_PBH` and would have to be regenerated. | C5 |

---

### RE-FLAG-OF-DISCLOSED (already in the paper; no closure required)

| id | item | leg | where the paper already says it |
|---|---|---|---|
| **DA3M-R4-R1** | "no derivation shows why the in-in and separate-universe routes must agree; the central claim rests on an unproven assumption that they compute the same quantity" | Grok M1 | = `DA3M-R3-R1`, and now materially closed by C3: `main.tex:271–276` scopes the in-in route, and **Appendix A** (`:1017–1116`) displays the linear identity's derivation, the `[L]/[K]/[X]/[S]` table, the `1/k_L` pole cancellation, the boundary term `f_b`, and the Bianchi-I argument for *why* the two routes compute different variables. Grok is reviewing the pre-C3 state. |
| **DA3M-R4-R2** | "official-posterior and refit `σ` values are not statistically comparable; the quoted `σ` distance is meaningless" | Grok M2 | = `DA3M-R3-R2`. `main.tex:583–588` says precisely this: "the latter should not be read as tighter than NANOGrav's own official assessment, since it conditions on a different (refit) marginal", and the abstract labels the refit "(refit)" beside the official posterior with its `5–95 %` interval type (`:64–67`, added by C6). |
| **DA3M-R4-R3** | "`f_PBH` moves by more than 100 decades — reads as a numerical pathology unless you say it is `exp(−δ_c²/2σ²)` at fixed `A`" | Fable m7 | `main.tex:688–692`: "because it depends **exponentially** on `γ_cr`, it moves by more than `100` decades across the grid at fixed target amplitude … tracking the unreproducible spectrum shape". The explanation Fable asks for is the same sentence. |
| **DA3M-R4-R4** | "the abstract quotes `≈1.7–1.9` while Table III gives `1.732 [1.610,1.809]`" | Fable m4 | `main.tex:806–812` states the widening explicitly ("widens from the lognormal grid's `1.732±0.050` to `1.7`–`1.9` across a threshold scan `C_th ∈ {0.4,0.5,0.6}`"), and C10 restored both caveats to the abstract (`:68–70`: "only marginally perturbative (`1.2\|f_NL\|σ_r ≈ 0.5–2`) with `f_PBH(f_NL)` non-monotonic"). `DA3M-R3-19` is therefore **CLOSED** — verified this round. |
| **DA3M-R2-11** *(carried-open, packaging)* | "a GitHub commit hash is insufficient for PRD data availability; mint the DOI now" | Gemini E2, Fable m10 | Not new. `main.tex:1152–1156` discloses it ("minting one is a maintainer action planned for the packaging stage"). Houston-gated Zenodo mint, P-round. Carried, not re-counted. |

---

### FALSIFIED (source shows the reviewer is wrong; recorded so no leg re-raises them)

| id | item | leg | why false — source |
|---|---|---|---|
| **DA3M-R4-F1** | "replace every occurrence of 'exact' with 'scheme-S1, commutator-ordered'; the value is recovered only inside one commutator ordering plus one transmission scheme" | Grok E1 | Two separate claims conflated. The `−35/16` **contraction-phase** value is a first-order in-in result validated against **two** independent literature limits with the same code — Maldacena's de Sitter bispectrum "matched term by term" and Namjoo–Firouzjahi–Sasaki's USR `f_NL = 5/2`, "Both match exactly" (`main.tex:150–158`) — and reproduced by an *independent classical route* (App. A); it is not ordering-contingent. The **transmission** result already carries both qualifiers in the abstract sentence Grok quotes from (`:51–56`: "within one cubic-vertex scheme (S1) and `kη_B ≲ 10⁻²` … a second scheme does not regulate"). Recurrence of `DA3M-R3-F1`. |
| **DA3M-R4-F2** | "the `1.7–1.9` ratio is an artefact of the truncated map; the paper itself labels the map an 'artefact'" | Grok E3 | **Inverted.** The "artefact" label belongs to the *first-pass Press–Schechter* result, which the paper **discards** (`main.tex:640–645`). The ratio comes from the **compaction-function** criterion, whose whole point is that "because `C_G` is an unbounded Gaussian variable, the map `ζ_G → C_lin` has **no** ceiling … the Eq. (11) artefact is removed **by construction**" (`:653–658`). Grok's required fix ("recompute with the untruncated map") is what the paper already did. Same species as `DA3M-R3-F2`. |
| **DA3M-R4-F3** | "the abstract lists the PBH channel among three 'consistent' channels without a null qualifier" | Grok E4 | The abstract does not say "consistent channels": it says "three channels, **each stated at the strength its evidence supports**" (`:57–58`) and then, for (ii), "the channel is a clean *null*: `7.0` orders of magnitude short … with `f_PBH = 0` exactly" (`:66–69`) — italicised in the source. The closing "No channel is in tension with another" is trivially true of a null. The qualifier Grok demands is printed verbatim. |
| **DA3M-R4-F4** | "Dated 'September 4, 2026'. Future date must be corrected." | Grok N1 | Today **is** 2026-09-04. Auto-FALSIFY Rule 3 (training-cutoff artifact). Recurrence of `DA3M-F3` / `DA3M-R3-F5` — now **8 consecutive rounds, 100 % falsified**. |
| **DA3M-R4-F5** | "several axis labels in Fig. 1 use inconsistent capitalization and the color bar is missing units" | Grok N3 | Auditor rendered `paper/pbh_compaction_fnl.png`: **the figure has no color bar** (three line curves + a shaded band + a legend). Axis labels are `lognormal curvature power-spectrum amplitude A` and `f_PBH`, both consistent and both dimensionless. Nothing to fix. |
| **DA3M-R4-F6** | "'regularized-renormalized- resummed' has a stray space after the second hyphen" | Gemini N1 | `main.tex:664–665` — a **source line break** inside a hyphenated compound; the compiled PDF renders it correctly and only text extraction shows the artifact (Rule 7). Recurrence of `DA3M-F5` / `DA3M-R3-F6`. |
| **DA3M-R4-F7** | "widen the headline range to `[-0.93,-0.50]` (and `[-1.83,-0.86]`), with `1.3σ` SPHEREx reach at `−35/16`" | Fable M1 (sub-claim) | `−0.93` requires feeding the **S2** transfer `T = 0.409` into the **S1** cubic formula `f^after = −(85/48)T − 5/24`. `Δf_NL^bounce[S2]` is **divergent with no regulated value** (`main.tex:424–427`; brief §4.3 `K ~ d_cut^{-0.4998}`), so no `f^after` exists for that row. The number is not computable in the paper's framework. (The residual real half — say so beside the range — is `DA3M-R4-01`.) |
| **DA3M-R4-F8** | "if `\|r\| ≫ 1`, the post-bounce `ζ` is dominated by a mode whose matter-contraction spectrum is not scale-invariant; how is `n_s = 0.9649` recovered?" | Fable M3(c) | `A2_TRANSMISSION_BRIEF_2026-09-02.md` §4.3, "Matter-bounce benchmark recovered": the post-bounce `Δ² ∝ k³\|α_post\|²` is **flat across the k grid to 1.2–4.2 %**, "as it must be", with the residual tilt identified as the same `(kη_B)²` finite-k truncation quantified elsewhere in that section. Scale invariance survives the `\|r\| ≫ 1` limit; this is a committed numerical check, not an assumption. (The residual real half — the paper never *states* this — is folded into `DA3M-R4-03`.) |

---

### OPINION / GENRE (no closure required; optional at the venue pass)

| id | item | leg |
|---|---|---|
| **DA3M-R4-G1** | "12 pp against a ~8 pp PRD norm; length driven by internal bookkeeping" | Grok M3. = `DA3M-R3-G1`. Length is an editor's call. The C7 Q1 cut reduces it as a side effect; note the page count **grew** 10 → 12 because C3 added a required derivation appendix, which is content a referee asked for. |
| **DA3M-R4-G2** | Table II caption's "differences from a self-reproduction run ≤ `3×10⁻¹⁵`" is not a validation | Fable m6. True as a matter of taste — it is a determinism check, and the caption should not imply more. Optional one-clause move to the reproducibility statement. |
| **DA3M-R4-G3** | "repeated self-referential phrases read as internal notes rather than journal prose" (genre half) | Grok N2. The directive-Q1 half is carried as `DA3M-R4-11`; the residual is a register preference for the venue pass. |

---

## 3. Corrections to earlier dispositions (recorded, never backfilled silently)

1. **`DA3M-R3-19` is CLOSED.** C10 restored the perturbativity diagnostic and the
   non-monotonicity caveat to the abstract (`main.tex:68–70`), verified this round. The R3
   regression is repaired; Fable m4 is now a re-flag (`DA3M-R4-R4`), not a live item.
2. **`DA3M-R3-11` is only partially closed; re-opened as `DA3M-R4-11`.** C8's own verification gate
   is not met — four in-body/appendix `research/…` paths remain, and the closure **added** a new
   instance of the same defect (`directive Q2` at `:1163`). Third consecutive round in which a
   Q1 sweep leaves or introduces Q1 material.
3. **`DA3M-R3-09` is only partially closed; re-opened as `DA3M-R4-12`.** C7's option (a) was
   selected but the footnote's printed wording still asserts option (b)'s conclusion.
4. **`DA3M-R3-04`'s closure (C4) introduced `DA3M-R4-02`.** Correcting the causal-floor claim was
   right; the *replacement* attribution (`P_R ∝ k`) contradicts §V C. Recorded as a
   closure-induced MAJOR — the second consecutive round in which a closure created a new finding
   (cf. `DA3M-R3-19` at R3). This is the pattern directive-G hygiene and this audit exist to catch.
5. **`DA3M-R3-01`/`-02` are CLOSED as stated defects.** The `kη_B` direction is now stated
   correctly and prominently (`main.tex:363–376`, `:944–948`), Table IV carries the transmitted
   rows with the pre-bounce row demoted to a labelled secondary (`:906–922`), and the abstract
   quotes the transmitted significances. Verified independently: every Table IV cell reproduces
   from `|f^after|/σ` (§0). `DA3M-R4-15` is the one residual seam left by that closure.

---

## 4. Convergence statement (directives H-refined, R2, P)

**NOT converged at v3M.0.9. Clean-wave count: 0.**

15 outstanding real items (3 MAJOR, 12 MINOR), of which 13 are genuinely-new and 2 are residuals of
R3 closures that did not fully land. Every one of the three legs' verdict words was ignored as a
gate; five of Grok's ten findings and one of Gemini's five are falsified against committed sources,
and two of Fable's five MAJOR sub-claims are falsified — but Fable's remaining MAJORs are real and
one of them (`DA3M-R4-02`) is the most consequential finding of the round.

**Directive R2 accounting.** R3 authorised exactly **one** verification round on the new PDF,
scoped to the C1 decision. This is that round, and its scoped question is answered: **C1's
propagation landed correctly** (`DA3M-R3-01`/`-02` closed, Table IV verified cell-by-cell). The
round also surfaced `DA3M-R4-02`, a genuinely-new MAJOR that is **science, not text**. Under R2 the
convergence budget is now spent: **v3M.0.10 closes the editorial list, and then rounds STOP** until
the `A3-3` computation/decision is taken. No further review round may be dispatched on editorial
grounds alone.

**Integrity.** No leg's verdict word was used as a gate. No finding was dispositioned non-real
without a cited source. No number in this audit was taken from a reviewer: Eq. (7)'s three rows,
the Table IV significances, the Appendix A general-`ε` reductions, the DESI z-scores, the nHz
wavenumber, the PBH `log10_ratio`s, the `λ_ζ ↔ T` correspondence, and the Legendre decomposition
were each re-derived or read from the committed artifact; the two arXiv records and Fig. 1 were
inspected directly. **No fabricated numbers were found in the manuscript** — every quantity the
auditor could recompute matched.

---

## 5. CLOSURE PLAN

### (i) Editorial / real edits — closable in **v3M.0.10** by a Sonnet lane

All in `research/track_a3_multichannel/paper/main.tex` unless stated. No new physics; no
reviewer-supplied number may be copied into the paper.

**C1 — state the S1/S2 scheme structure of the transfer interval (`DA3M-R4-01`).**
- Abstract `:53–54`: "`0.165`–`0.409` across three backgrounds" → "`0.165`–`0.409` across three
  backgrounds and two mode-function schemes; the combined post-bounce range below is scheme-S1
  only".
- `:352–362`: after the `0.165`–`0.409` sentence, add one clause naming the `0.409` row as the
  **LQC/S2 (effective-fluid)** value (`a2_transmission_linear.json` row 4).
- `:405–420` (the three-row table): add a footnote — the S2 row is **excluded from
  `f_NL^after`** because `Δf_NL^bounce[S2]` is divergent (`:424–427`), so no `f_NL^after` is
  computable in that scheme. Do **not** widen the range.

**C2 — reserved for the science item; no edit in v3M.0.10.** (See (ii).)

**C3 — define Eq. (6) and point at its derivation (`DA3M-R4-03`).** `:334–344`. Define
`𝒜`, `I_∞`, and the `1+2r` denominator (source: `A2_TRANSMISSION_BRIEF_2026-09-02.md` §3); state
that `T_fNL` is the **`f_NL`** transfer, equal to `1/λ_ζ` with `λ_ζ = ζ(+∞)/ζ(−η_h)` the linear
amplitude growth, and say in one sentence that `ζ` *grows* through the bounce (`λ_ζ = 4.0`, `5.12`,
`6.06` for the three backgrounds) which is why `f_NL` is suppressed. Add one sentence recording that
the post-bounce spectrum remains scale-invariant to `1.2–4.2 %` under `|r| ≫ 1` (brief §4.3) — this
answers referee question 1 and pre-empts `DA3M-R4-F8`'s recurrence.

**C4 — fix Ref. [9] (`DA3M-R4-04`).** `:1215–1217`: title → "Universal infrared scaling of
gravitational wave background spectra". Keep `PRD 102, 083528 (2020)`, `arXiv:1909.13728`. Check no
other entry inherited the merged record.

**C5 — nine one-clause corrections (`DA3M-R4-05, -06, -07, -08, -09, -10, -12, -14, -15`).**
- Abstract `:70–73`: add "(bispectrum only)" to the SPHEREx figures and replace "under `1σ` apart"
  with the honest span, `0.5`–`1.1σ` depending on the forecast configuration; make body `:930–933`
  agree.
- `:176` and App. A table `:1063–1073`: "quadrupole `15/16`" → "`μ²` coefficient `15/16`
  (Legendre `ℓ=2` coefficient `5/8`)".
- `:813–816`: "seven decades above the BBN scale used to bound the mass range elsewhere in this
  section" → "**eleven** decades above the BBN scale (`~1 MeV`)", and delete the false
  back-reference to a BBN bound used elsewhere in §V.
- `:830–834`: "a shortfall of `7.0` orders of magnitude … at both candidate `f_NL` values" →
  "`6.7`–`7.0` orders of magnitude (`log₁₀` ratio `6.75` at `−35/8`, `7.02` at `−35/16`)", sourced
  to `outputs/inlab_delta2_zeta_2026-09-03.json`.
- `:1099–1112`: add the domain clause — these general-`ε` expressions hold on the non-attractor
  growing branch `ζ̇ = −3ζ/η` and do **not** reduce to the slow-roll attractor result as `ε → 0`.
- Abstract `:44–49`: replace "explained at the equation level" with the two-part statement — the
  linear-order relation is **derived** (App. A.1); the second-order coefficient is **computed and
  recorded**, with its physical mechanism not identified.
- `:780–789`: narrow the `Ω_DM` footnote to what is true — the **ratio** (Eq. 13) and the §V C null
  are unaffected because `Ω_DM` cancels; the tabulated `f_PBH` column and Fig. 1 are quoted at a
  calibration that uses Choudhury *et al.*'s printed value. **If** the drafter instead recomputes at
  `Ω_DM = 0.264`, directive I6 applies: regenerate `pbh_compaction_fnl.png` and re-verify by
  rendering the figure page of the new PDF, not by grepping text.
- `:869–876`: state which side of each asymmetric DESI error is used (upper `9.0` for the merger
  prior; lower `7.4` for universality).
- `:869–872`: reconcile with `:880–887` — either compare DESI to the transmitted range
  (auditor's values to check against: `0.34σ` and `0.55σ` at `f^after = −0.55`) or state explicitly
  why the current-constraint comparison retains the pre-bounce amplitude.

**C6 — add a `γ = 2` row to Table II (`DA3M-R4-13`).** Re-run
`research/track_a3_multichannel/pta_gamma_reproduce.py` with `γ_* = 2` added to the comparison set,
re-emit `outputs/pta_gamma_reproduction.json`, and print **what the script emits**. The referee's
quoted `3.3σ`/`1.5σ` are not to be used.

**C7 — finish the directive-Q1 sweep (`DA3M-R4-11`).**
- Move the in-body/appendix paths at `:566`, `:793`, `:855`, `:1022` into the reproducibility
  statement (paths already **inside** that statement stay — they are C8-sanctioned).
- `:1163`: delete "consistent with this lab's standing reproducibility policy (directive Q2)".
- `:1157`: "this lab's companion **P2** Zenodo record" → a neutral phrase plus the DOI.
- `:891–894`: drop the "companion Fisher-forecast draft" reference; no result depends on `r`
  (`DA3M-R3-F7`), so the sentence can state the omission without invoking an unpublished draft.
- `:230`: "is this paper's own adjudication" → a neutral formulation.
- **Verification gate (must pass before commit):**
  `grep -nE 'research/|this lab|directive Q|earlier draft|supersed' main.tex` returns hits only
  inside the reproducibility statement.

**Post-closure gate (mandatory, directive G + I6).** Bump `\paperVersion` → `v3M.0.10` and
`\paperTimestamp`; recompile to 0 undefined references; run `/latex-audit`; re-mirror the new PDF
byte-identically to `site/public/papers/`; regenerate any figure whose numbers changed;
`paperVersions:bump` in Convex with the real new md5/pages; three-way md5 check
(fresh compile == served == Convex). **Do not dispatch a review round afterwards** — see below.

### (ii) SCIENCE — requires a ledger computation before any further round

**S1 — `DA3M-R4-02`: determine the model's own `P_R(k)` from the CMB/LSS pivot to the nHz band, and
reconcile Channel I with Channel II.**
- **Ledger id:** `A3-3` (`project-context/NEXT_SCIENCE_LEDGER.md`).
- **The computation, named exactly:** propagate the matter-contraction curvature spectrum through
  the S1 bounce transfer to obtain `P_R(k)` over `k ∈ [0.05, 10¹⁶] Mpc⁻¹` — in particular whether
  the transfer is scale-independent out to `k ≈ 6.5×10⁶ Mpc⁻¹` (the nHz band) — then feed that
  `P_R(k)` through the standard radiation-era induced-GW kernel to obtain `Ω_GW(f)` and read off
  its nHz-band slope. Existing machinery: `research/cubic_bounce_transmission/a2_transmission_linear.py`
  (transfer, k-dependence already parameterised), `research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.py`
  (the lab's own spectrum), `pta_gamma_reproduce.py` (slope conventions and the NANOGrav comparison).
  Local CPU; no GPU.
- **The three possible outcomes, all publishable, none allowed to be pre-judged:**
  (a) the model's spectrum carries a genuine small-scale feature at nHz scales → `γ = 3` is derived
  rather than borrowed, and §V C's flat extrapolation must be replaced (and its null re-tested,
  since Papanikolaou's enhanced spectrum *does* form PBHs);
  (b) the model's spectrum is flat at nHz scales → `Ω_GW ∝ f⁰`, `γ ≈ 5`, and Channel I becomes a
  **tension**, not a consistency; that must be stated as such;
  (c) the propagation is not decidable within the validated `kη_B ≲ 10⁻²` domain → both channels
  must be restated as conditional, and the `γ = 3` attribution to Papanikolaou dropped to a cited
  comparison rather than a derivation.
- **Blocking scope:** Channel I's headline consistency claim (abstract, §IV A, §IV D, §VII A) and
  §V C's null share this dependency. Until `A3-3` returns, neither may be strengthened.

**Directive R2 stop.** After v3M.0.10 lands and passes the post-closure gate, **review rounds
STOP**. The next round is authorised only by the `A3-3` science decision, not by the editorial
closure.

---

*Auditor's note on process:* two consecutive rounds have now produced a new MAJOR that was
*created by the previous round's closure* (`DA3M-R3-19` at R3, `DA3M-R4-02` at R4). Closures that
replace a wrong justification with a new one should be treated as new claims and checked against
the paper's other sections before the bundle commits — not left for the next referee wave to find.
