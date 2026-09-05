# A3M v3M.0.13 R6 — Truth Audit (skeptical, independent)

**Exact artifact:** `site/public/papers/a3_multichannel_arxiv_v3M.0.13.pdf` (= `research/track_a3_multichannel/paper/main.pdf`), 15 pp, sha256 `c6f9bb57f9acb755dfe6a3bda12955038ffcf46c86a5cea9809dabff5031a34c`
**Date:** 2026-09-04 · **Auditor stance:** not told any expected outcome; verdict-first per patterns 061–066, directive H-refined.

## Legs audited (raws)
| Leg | Raw | Verdict word |
|---|---|---|
| Grok_brutal (grok-4.3) | `../ROUND_2026-09-04-A3M-v3M.0.13-EXACTPDF-c6f9bb57-R6VERIFY_A3M_Grok_brutal.md` | REJECT |
| Gemini_cosmology (gemini-3.1-pro-preview) | `../ROUND_2026-09-04-A3M-v3M.0.13-EXACTPDF-c6f9bb57-R6VERIFY_A3M_Gemini_cosmology.md` | MAJOR REVISIONS |
| Claude INT (fable) | `A3M_v3M.0.13_R6_claude_fable_2026-09-04.md` | major-revisions (5M / 15m) |

## Classification scheme
- **(a) GENUINELY-NEW REAL** — real defect, not previously dispositioned, on this exact PDF.
- **(b) RE-FLAG** — matches a canonical disposition in `DISPOSITIONS/A3M.md`; page + id cited.
- **(c) FALSIFIED** — contradicted by the committed source/PDF, which is checked and cited.
- **(d) OPINION / genre / venue** — length, framing, journal-fit preference.
- **(e) OUT-OF-SCOPE, DISCLOSED** — a real limitation the paper already states as such.

## Plan (sections committed incrementally)
1. Canonical numbered finding list (all three legs, fingerprinted + deduped).
2. Physics verification of the Fable MAJORs: M1 tensor-channel r inconsistency; M2 PBH γ_cr grid + Choudhury sign; M3 5.1σ PTA framing; T_B factor-100; S1/S2 band framing.
3. Verification of Grok ESSENTIALs and Gemini ESSENTIALs.
4. Per-class counts per leg.
5. DESI DR1 v3 reproduction — recommended §VI sentence at evidential strength.
6. CLOSURE PLAN: (i) editorial/real edits for v3M.0.14; (ii) SCIENCE items for the ledger.
7. R2 statement (directive R2: rounds stop after v3M.0.14 pending a science decision).

*(sections below are appended as they are verified)*

---

# 1. Canonical findings — GENUINELY-NEW REAL (class a)

Line numbers are `research/track_a3_multichannel/paper/main.tex` at v3M.0.13.

**`R6-01` (MAJOR) — §V C bounce-temperature condition is wrong by ~2 decades.**
`:1023–1027`: "$a_BH_B\gtrsim10^{17}$–$10^{18}$ Mpc$^{-1}$, i.e.\ $T_B\gtrsim10^{8}$–$10^{10}$ GeV — eleven
decades above the BBN scale". The paper's own committed mapping
(`outputs/inlab_delta2_zeta_2026-09-03.json`, key `k_B_Mpc-1_if_T_B_GeV`: `1.714e17` at
`T_B=1e10`, `1.714e21` at `1e14`, `1.714e23` at `1e16`) is `k_B ≈ 1.7143e7 · T_B[GeV] Mpc^-1`.
Auditor recompute: `1e17 → T_B = 5.83e9 GeV`; `1e18 → 5.83e10 GeV`. **Correct condition:
`T_B ≳ 6×10^9–6×10^10 GeV` (`10^10–10^11` to the nearest decade), which is THIRTEEN decades
above 1 MeV, not eleven.** The stated 10^8 lower end is wrong by a factor ≈ 58 (~10^1.8).
Null verdict unaffected (the true condition is strictly stronger); a quoted quantitative
condition is wrong. Legs: Fable M4, Gemini N3 (quotes the same sentence). REAL **residual of
`DA3M-R3-02`**, whose closure corrected the "any bounce above BBN" claim but left this sentence.

**`R6-02` (MAJOR-lite) — Channel I mixes two different NANOGrav fits.**
`sigw_nhz_from_lab_spectrum_2026_09_04.py:72`: `NG_A_YR, NG_GAMMA = 2.4e-15, 3.2`. `A = 2.4e-15`
is NANOGrav's $\gamma=13/3$-**fixed** amplitude; the slope compared against, $\gamma_{\rm HD}=3.2$,
is the **free-$\gamma$** posterior, whose own median is $\log_{10}A\approx-14.19$ ($A\approx6.4\times10^{-15}$).
Propagates to `:752`, `:756`, `:771`, `:1186–1187`, abstract `:58` ("$\sim10^{14}$ below"), and the
Fig. 1 legend. Using one fit consistently moves the shortfall $10^{14.3}\to\approx10^{15.2}$ —
the null is unaffected and in fact strengthened. Legs: Fable M3(iii)+m7. Not in any prior
disposition (`DA3M-R5-03` concerned a different, already-corrected value).

**`R6-03` (MINOR) — abstract conflates bare detection significance with candidate separation.**
Abstract `:74–78`: "SPHEREx bispectrum-only reaches $0.7$–$0.9\sigma$ … combining power spectrum
and bispectrum **widens this to** $0.5$–$1.1\sigma$." The body is correct (`:1211–1215`: "widens the
**candidate separation** to only $0.5$–$1.1\sigma$"); Table VI's P+B *bare* significance is
$1.0$–$1.3\sigma$; and $0.5$ is not wider than $0.7$. Legs: Gemini E1, Fable m1, Grok E5 (partial).
Adjacent to `DA3M-R5-05` (inverted-residual class) but a distinct metric conflation.

**`R6-04` (MINOR) — abstract mis-attributes the SMBH-seed exclusion.**
Abstract `:62–64`: "SMBH-seed high-$z$ abundance: three orders of magnitude short — a third honest
null." Body `:1066–1077` is two-part: the **required** seed amplitude is FIRAS-excluded by three
orders *independently of this model*, while **this model's** spectrum falls short by ~7 decades.
The abstract fuses them into one number attached to the model. Legs: Gemini E2.

**`R6-05` (MINOR) — `:1099` sign-of-comparison prose is backwards.**
"using the upper side of the merger-response error ($+9.0$, since the prediction lies **below** the
central value)": prediction $-2.1875$, central $-3.6$ (`:1091`) — the prediction lies **above**.
The arithmetic ($0.16\sigma$ using $+9.0$) is correct. Legs: Gemini N2.

**`R6-06` (MINOR) — version-history prose in §VII C.**
"…listed as open in earlier versions, are now carried out in Secs. VI and IV D…". A published
paper must not reference its own draft states. Legs: Gemini E5. **Recurrence of `DA3M-08`**
(internal audit tags / version-history prose) — that item was closed for tags but not for this clause.

**`R6-07` (MINOR, auditor-originated) — the excursion thresholds are unsourced.**
`:1059–1062` prints "$3162\sigma$", "$3364\sigma$", "$408\sigma$". `grep -rn '3364' research/`
returns **main.tex only** — no committed artifact carries them. They *are* one-line derivable
(a 7.0-decade shortfall in $\Delta^2_\zeta$ is $10^{3.5}=3162$ in $\sigma$), so this is not
fabrication, but under `/never-fabricate-derivation` a printed number needs either a derivation in
the text or a committed artifact. Compounding it, the adjacent "$\log_{10}\beta\approx-1.7\times10^{9}$"
is at a **different mass** ($M_H=10^{20}$ g), which is exactly what made a referee call the two
incompatible (see `F3`). Trigger: Gemini E6.

**`R6-08` (MINOR) — abstract calls $[-1.25,-0.50]$ "a two-scheme band".**
Abstract `:53–54` vs §III A, which establishes S1 and S2 as "genuinely physically inequivalent
continuations through $H=0$", and §VII C(i), which leaves which is physical open. "Band" reads as a
bracketed uncertainty. Legs: Grok E3, Fable M5. Residual of `DA3M-R5-16` (whose "S2/Quintin-only"
half **is** closed — the abstract does name the background).

**`R6-09` (MINOR, verification task) — Ref. [8] attribution unverified.**
`:1504–1506` Papanikolaou, arXiv:2504.11641, single author. This auditor could not verify the
author list or identifier offline; the flag stands as a pre-submission check, not as a confirmed
error. Legs: Fable m14.

**`R6-10` (MINOR, editorial with a science tail) — the $r=0.84$ scenario is reported but never
tested against the bound the same paragraph quotes.**
`:762–774` **does** compute the tensor channel in both cases and cites
`outputs/r5_15_tensor_omega_nhz.json` (Case B: $r=0.84$, $\Omega^{(1)}_{\rm GW}h^2(f_{\rm yr})=5.94\times10^{-16}$,
$6.79$ decades below NANOGrav) — so "the tensor sector is omitted" is false (`F6`). What is missing
is one sentence: if the open A3-4 value $r=0.84$ is right, that background is already excluded at
$k_*$ by the same BICEP/Keck bound quoted two lines earlier ($r<0.036$), far more decisively than
any of the three channels. Legs: Fable M1(a).

**`R6-11` (MINOR) — abstract "shape-robust" carries none of the body's conditionality.**
Abstract `:61` vs body `:942–950`, which now states in full (from `outputs/R5_18_GAMMACR_NOTE_2026-09-04.md`):
grid $\gamma_{\rm cr}\in[0.766,0.968]$ straddling the $0.85$ sign flip (9/27 below), ratio
$1.732\pm0.050$; this model's own shape at $\gamma_{\rm cr}\in[0.27,0.63]$ is **outside** coverage
and gives $1.85$–$1.89$; the whole thing conditional on the unresolved Choudhury sign disagreement
(`:929–930`). Abstract-only defect. Legs: Fable M2 (its "the body does not establish this" half is
falsified — `F8`), Grok M1 (partial).

**`R6-12` (MINOR) — `:1076` "largely excluded" is a qualitative word for a quantified statement**
already itemized in the preceding two sentences (`:1071–1075`). Legs: Gemini M1.

**`R6-13` (MINOR) — "5.1σ" is printed as a tension, not as what it is.**
`:57`, `:755`, `:802`, `:1186`. It is a Gaussian-equivalent $z$-distance built from a **5–95%**
interval width ($\sigma\approx0.6/1.645=0.365$, `:607–609`) extrapolated into the tail of an
asymmetric posterior — the paper's own Savage–Dickey paragraph (`:637–641`) explains why tail
statements there are unreliable, and declines to quote a Bayes factor at $\gamma=5$ for exactly
this reason. Quoting $5.1$ to two figures is inconsistent with that stance. Legs: Fable M3(ii),
Grok E2 (partial), Grok N2. Same class as `DA3M-R5-11` ("$3.13\sigma$ mislabelled a tension").

**`R6-14` (MINOR)** `:381–384` "S2 has no computable post-bounce $f^{\rm after}$ on the LQC
background" — the **linear** S2 transfer on LQC exists ($T=0.409$); only the **cubic** does not.
Legs: Fable m10. Residual of `DA3M-R5-04`.

**`R6-15` (MINOR)** sentence fragment in the paragraph after Eq. (7) (begins "so
$|f_{\rm after}|\in[0.50,0.65]$…" following "(below)."). Legs: Fable m11.

**`R6-16` (MINOR)** Table VI entries should be captioned **upper bounds**: the shape overlap
$r<1$ between the $\mu^2$-dependent squeezed shape and the local template is acknowledged but not
computed, and it can only *reduce* every entry. Legs: Fable m15.

# 2. RE-FLAG-OF-DISCLOSED (class b)

| id | finding | leg | page / disposition |
|---|---|---|---|
| `RF1` | "enlarge the PBH grid to ≥100 points" | Grok M1 | `=DA3M-R4-R4/R5-R4`, **3rd recurrence**; `:942–950` now prints the coverage, the straddle, and the out-of-coverage evaluation explicitly |
| `RF2` | "the classical/δN route is not independent — same separate-universe assumption" | Grok E6 | `=DA3M-R3-R1/R4-R1/R5-R2`, **4th recurrence**; §II D + `:286–292` already state the two routes compute *different variables* |
| `RF3` | "present a scheme-marginalized LSS forecast" | Grok M2 | `:1200–1206` + §VII C(i) state the scheme dependence; marginalizing over a *convention* (not a measured nuisance) is not a defined operation — half re-flag, half opinion (`O4`) |
| `RF5` | "a factor 0.058 is a 17× suppression, not an excursion" | Fable m9 | `=DA3M-R5-10`, closed at `:413–415` with "(not order-unity in the strict sense)" and the three explicit ratios |
| `RF6` | Table V uncapped $f_{\rm PBH}>1$ should be in the column header | Fable m8 | `=DA3M-R5-R6`; caption `:872–877` already says it; header placement is style |
| `RF7` | "refit vs official σ qualifier" | Fable m6 | `=DA3M-R3-R2/R4-R2/R5-R1`, **5th recurrence**; `:616–618`, `:645–650` frame official as primary |
| `RF8` | frozen-release DOI / SHA-256 / "current HEAD" | Grok E4, Gemini E3+E4, Fable m13 | **carried packaging item** (P-round). The paper *does* pin a git commit hash and declares DOI minting a maintainer action; Gemini E3's "no frozen hash" half is false. Real only as a submission-stage prerequisite, not a v3M.0.14 science defect |
| `RF9` | §II D "resolved rather than merely bounded" vs Appendix "a computed identity, not a claimed mechanism" | Fable m2 | `=DA3M-R3-03` class; the Appendix wording is the honest one and is present. Harmonizing is cheap and is folded into the (i) list as optional |

# 3. FALSIFIED — committed source checked (class c)

| id | claim | leg | why it is false (source) |
|---|---|---|---|
| `F1` | "abstract presents $-35/16$ as exact/scheme-independent, body says scheme-dependent" | Grok E1 | `:49–54` explicitly labels transmission "scheme-qualified" and prints BOTH schemes. $-35/16$ is the **pre-bounce in-in** value; the scheme dependence is of $f^{\rm after}$, which the abstract states. `=DA3M-R5-F1/R4-F1`, **3rd recurrence** |
| `F2` | "future date / affiliation is unusual for PRD" | Grok N1 | `=DA3M-F3`. **10th consecutive round, 100% falsified.** Compile date is today's date |
| `F3` | "$3162\sigma$ and $\log_{10}\beta\approx-1.7\times10^{9}$ are mathematically incompatible (factor ~800 in the exponent)" | Gemini E6 | They describe **different mass scales**. `inlab_delta2_zeta_2026-09-03.json:252–253` gives `n_sigma_to_threshold = 89149.44`, `log10_beta_gaussian_estimate = -1.7258e9` at $M_H=10^{20}$ g — self-consistent: $89149^2/(2\ln 10)=1.726\times10^{9}$ ✓. The $3162\sigma$ is the 7.0-decade deficit at the $10^{15}$–$10^{16}$ g end ($10^{3.5}=3162$ ✓). No arithmetic error. (Editorial residual → `R6-07`.) |
| `F4` | "regularized-renormalized- resummed: punctuation artifact" | Gemini N1 | `main.tex:863` contains no stray space; the gap in the PDF is a LaTeX line break at a compound hyphen |
| `F6` | "the tensor sector is OMITTED from a multi-channel consistency assessment" | Fable M1 (first half) | `:762–774` computes it for both $r<0.036$ and $r=0.84$, citing `outputs/r5_15_tensor_omega_nhz.json` (Case A `2.54e-17`, Case B `5.94e-16` at $f_{\rm yr}$; shortfalls 8.15 and 6.79 decades). Only the *exclusion* sentence is missing → `R6-10` |
| `F7` | "the paper must cite the exact statement in [11] fixing the ±0.6 convention" | Fable M3(i) | `:607–609` already does: "quoted explicitly as a posterior median and $5$–$95\%$ interval~\cite{NANOGrav15}" |
| `F8` | "'shape-robust' is not established for the model's own spectrum; the paper carries none of this conditionality" | Fable M2 (second half) | The **body** establishes and states it in full at `:942–950` (from `outputs/R5_18_GAMMACR_NOTE_2026-09-04.md`), including the out-of-coverage $\gamma_{\rm cr}\in[0.27,0.63]$ and the sign-disagreement conditionality. Only the abstract word survives → `R6-11` |

# 4. OPINION / GENRE / VENUE (class d) and DISCLOSED-LIMITATION (class e)

`O1` Grok M3 — 15 pp too long for the increment; "6–8 page note" (venue/length; the paper itself
credits Li *et al.* 2017 and Quintin *et al.* 2015 at `:230–231`, `:40–42`) ·
`O2` Grok N2 — "honest null" undefined (style; partly addressed by `R6-13`) ·
`O3` Grok N1 second half — institutional/ORCID preference ·
`O4` Grok M2 tail — see `RF3` ·
`O5` Gemini E4 "mint the DOI now" — packaging-stage preference, see `RF8` ·
`O6` Fable m3 + m12 — move the Eq. (5) derivation and the full shape function from the repo note
into the paper/supplement (venue-format preference; the science is committed and cited) ·
`O7` Fable m4 + m5 — Table IV row labelling ($\gamma_*=5$ vs $5.035$) and an added ABS-plateau
column (both wish-list; `m4` `=DA3M-R5-G2`) ·
`O8` Fable Q5 — "is $1.732=\sqrt3$ a coincidence?" is a question, not a finding.

**Class (e), disclosed and unchanged:** the Choudhury *et al.* $\gamma_{\rm cr}\lesssim0.85$ sign
disagreement (`:929–930`, "a genuine discrepancy left unresolved"); the unreproducibility of
Choudhury *et al.*'s spectrum (`:1010–1012`, `=DA3M-R5-F11/R3-R3`); which of S1/S2 is physical
(§VII C(i)); scheme-S1 assumption A4 through $H=0$ (`:355–361`).

# 5. Per-class counts per leg

Every finding in every raw is mapped exactly once. Legs: Grok API (11 findings), Gemini API
(10 findings, 7 questions n/a), Claude Fable (20 findings; 7 questions excluded).

| leg | verdict word | findings | new-real | re-flag | falsified | opinion/genre | carried packaging |
|---|---|---|---|---|---|---|---|
| Grok_brutal (grok-4.3) | REJECT | 11 | **3** (E2→`R6-13`, E3→`R6-08`, E5→`R6-03`+`R6-04`) | 3 (E6,M1,M2) | 2 (E1,N1) | 2 (M3,N2) | 1 (E4) |
| Gemini_cosmology (gemini-3.1-pro-preview) | MAJOR REVISIONS | 10 | **6** (E1,E2,E5,M1,N2,N3) | 0 | 2 (E6,N1) | 0 | 2 (E3,E4) |
| Claude Fable 5.1 (INT) | major-revisions | 20 | **11** (M1h,M2h,M3ii,M3iii,M4,M5,m1,m10,m11,m14,m15; m7 dup of M3iii) | 4 (m2,m6,m8,m9) | 3 halves (M1,M2,M3i) | 4 (m3,m4,m5,m12) | 1 (m13) |

**Canonical totals:** **16 genuinely-new REAL** (`R6-01`…`R6-16`; 1 MAJOR + 1 MAJOR-lite + 14 MINOR),
of which `R6-01` is a REAL residual of `DA3M-R3-02`, `R6-06` a recurrence of `DA3M-08`, `R6-14` a
residual of `DA3M-R5-04`, `R6-08` a residual of `DA3M-R5-16` · **8 RE-FLAG** · **7 FALSIFIED** ·
**8 OPINION/GENRE** · 1 carried packaging · **0 BLOCKER**. **Clean-wave count: 0.**

**Physics status.** No physics error was found in the paper's derivations: every number this
auditor recomputed from the committed JSONs reproduces, and the Fable leg's independent hand-check
of Tables I/III/IV/V/VI and Eqs. (3),(4),(7),(11),(A2),(A3) also reproduces. Exactly ONE quantitative
statement is numerically wrong against the lab's own committed artifact — `R6-01`, the §V C bounce
temperature — and its error direction makes the paper's null *stronger*, not weaker. `R6-02` is a
reference-value mismatch with the same property. Everything else is abstract-vs-body calibration,
attribution, and sourcing. Both reviewer verdict words (REJECT / MAJOR REVISIONS) rest on findings
that this audit classes as falsified, re-flag, or abstract-wording (see `O4`, `F1`): **no leg
identified a defect in the physics.**

# 6. DESI DR1 reproduction v3 — the sentence §VI may state

Source: `research/desi_png_reproduction/LEDGER4_RESULT_v3_2026-09-04.md` (official
data.desi.lbl.gov QSO `full-shape-bao-clustering/v1.0` window matrix, full-18-randoms measured
$P_\ell$, and EZmock covariance; $z=0.8$–$2.1$; $k\in[0.003,0.08]$, 46 dof; $b_1$ and $f_{\rm NL}$
free, $n_{\rm shot}$ fixed at 0).

**Recommended sentence (at evidential strength — this is the strongest form the artifact supports):**

> An independent re-analysis of the public DESI DR1 QSO sample using DESI's own published window
> matrix, full-randoms $P_\ell$, and EZmock covariance ($z=0.8$–$2.1$, $k\le0.08\,h\,{\rm Mpc}^{-1}$,
> 46 dof) returns $\fnlloc = -2.2\pm25$ at $p=1.6$ — $0.06\sigma$ from DESI's published
> $-3.6^{+9.0}_{-9.1}$ — which reproduces the published constraint's *sign and scale* while showing
> that DR1's constraining power at this configuration is an order of magnitude too weak to separate
> $-35/16$ from $-35/8$, from zero, or from the published central value; the near-coincidence of the
> recovered central value with $-35/16$ is a coincidence, not evidence.

Mandatory accompanying caveat (one clause or a footnote — do **not** drop it): the reproduction's
$\sigma=25$ is ~2.8× the published $9.0$ because wide-angle corrections
(`PowerSpectrumOddWideAngleMatrix`) are not applied and only 2 of 5 imaging-systematics splits were
run; artifact `research/desi_png_reproduction/`, ledger `LEDGER4_RESULT_v3_2026-09-04.md`.

**What §VI may NOT say:** that the reproduction *confirms*, *supports*, or *is consistent with*
$-35/16$ specifically (the 0.0007σ distance to $-35/16$ is meaningless at $\sigma=25$ — the fit is
equally 0.086σ from zero); that it validates this paper's own LSS forecast; or that it is a DESI
collaboration result. It is a lab reproduction of a published constraint, and its value here is
exactly that: it establishes that the pipeline this paper's Channel III forecasts rest on
reproduces the published DR1 number on official products.

# 7. CLOSURE PLAN

## (i) Editorial / real edits for v3M.0.14 — exact lines

All against `research/track_a3_multichannel/paper/main.tex` at v3M.0.13. Directive-G hygiene
(version + date bump, 4-pass recompile, byte-identical mirror to every served path, Convex
`paperVersions:bump`, three-way md5) applies to the bundle; directive I6 (figure regeneration)
applies to item 4.

| # | line(s) | edit | closes |
|---|---|---|---|
| 1 | `:1023–1027` | replace "$T_B\gtrsim10^{8}$–$10^{10}$ GeV — eleven decades above the BBN scale" with "$T_B\gtrsim6\times10^{9}$–$6\times10^{10}$ GeV — thirteen decades above the BBN scale", and print the mapping once: "$k_B\simeq1.71\times10^{7}\,T_B[{\rm GeV}]\,{\rm Mpc}^{-1}$ (\texttt{outputs/inlab\_delta2\_zeta\_2026-09-03.json})" | `R6-01` |
| 2 | `:784–786` (§IV D) | "$T_B\gtrsim10^{8}$–$10^{10}$ GeV condition" → "$T_B\gtrsim10^{10}$–$10^{11}$ GeV condition"; recompute the "$7.6$ decades below" → **$9.6$ decades below** | `R6-01` |
| 3 | `:1051–1053` | keep the worked $T_B=10^{8}$ GeV / $k_B=1.714\times10^{15}$ point but relabel it "an illustrative bounce energy **below** §V C's validity condition" so it does not read as satisfying it | `R6-01` |
| 4 | `sigw_nhz_from_lab_spectrum_2026_09_04.py:72` | pair $A$ and $\gamma$ from the **same** NANOGrav fit (free-$\gamma$: $\log_{10}A\approx-14.19$, $\gamma=3.2$); rerun; update `:752`, `:756`, `:771`, `:1186–1187`, abstract `:58` ($\sim10^{14}\to\sim10^{15}$); **regenerate `sigw_nhz_from_lab_spectrum_2026_09_04.png`** (legend carries $A=2.4\times10^{-15}$) and re-mirror it | `R6-02` |
| 5 | abstract `:74–78` | "…combining power spectrum and bispectrum widens this to $0.5$–$1.1\sigma$" → "…the P+B **candidate separation** is $0.5$–$1.1\sigma$ (P+B bare significance $1.0$–$1.3\sigma$, Table VI)" | `R6-03` |
| 6 | abstract `:62–64` | two-part: "the **required** SMBH-seed amplitude is itself FIRAS-excluded by three orders of magnitude, and this model's own spectrum falls $\sim7$ decades short of supplying it either way" | `R6-04` |
| 7 | `:1099` | "lies below the central value" → "lies **above** the central value" | `R6-05` |
| 8 | §VII C | delete "…listed as open in earlier versions, are now carried out in Secs. VI and IV D…" | `R6-06` |
| 9 | `:1059–1062` | add the one-line derivation ("a $7.0$-decade shortfall in $\Delta^2_\zeta$ is $10^{3.5}=3162$ in $\sigma$") and label the mass scale of BOTH numbers ($3162\sigma$ at $M_H\sim10^{15}$–$10^{16}$ g; $\log_{10}\beta=-1.7\times10^{9}$ at $M_H=10^{20}$ g, $n_\sigma=89{,}149$); commit the three thresholds to a JSON | `R6-07`, pre-empts `F3` |
| 10 | abstract `:53–54` | "a two-scheme band $[-1.25,-0.50]$" → "two scheme-dependent answers, $-1.25$ (S2) and $[-0.65,-0.50]$ (S1) — not a bracketed uncertainty" | `R6-08` |
| 11 | abstract `:61` | "shape-robust amplitude ratio $1.7$–$1.9$" → "an amplitude ratio stable at the $\sim10\%$ level ($1.732\pm0.050$ over the scanned $\gamma_{\rm cr}\in[0.766,0.968]$ grid; $1.85$–$1.89$ at this model's own out-of-coverage shape), conditional on an unresolved sign disagreement with Ref.~[16]" | `R6-11` |
| 12 | after `:769` (§IV D) | add: "If the $r=0.84$ of the unresolved matter-bounce item were confirmed, that background would already be excluded at $k_*$ by the same BICEP/Keck bound quoted above, independently of any of the three channels; resolving $r$ for these backgrounds is an open item." | `R6-10` |
| 13 | `:1076` | "largely excluded" → the itemization already at `:1071–1075` | `R6-12` |
| 14 | `:381–384` | "no computable post-bounce $f^{\rm after}$" → "no computable **cubic** $f^{\rm after}$" (the linear S2 transfer on LQC, $T=0.409$, exists) | `R6-14` |
| 15 | ¶ after Eq. (7) | repair the sentence fragment beginning "so $|f_{\rm after}|\in[0.50,0.65]$…" | `R6-15` |
| 16 | Table VI caption | label the entries **upper bounds** (shape overlap $r<1$ can only reduce them) | `R6-16` |
| 17 | `:1504–1506` | verify Ref. [8] author list + arXiv identifier against the arXiv listing before submission | `R6-09` |
| 18 | `:57`, `:755`, `:802`, `:1186` | label each "$5.1\sigma$"/"$4.9\sigma$"/"$3.13\sigma$" a **Gaussian-equivalent $z$-distance** from a $5$–$95\%$ interval width, consistent with the paper's own Savage–Dickey stance at `:637–641` | `R6-13` |
| 19 | §II D / Appendix A2 (optional) | harmonize "resolved rather than merely bounded" to the Appendix's weaker, honest wording | `RF9` |
| 20 | §VI | insert the DESI DR1 v3 sentence of §6 above with its mandatory caveat | new evidence |

**None of (i) changes a scientific conclusion.** Every edit either corrects a number against a
committed artifact (1–4, 9), calibrates the abstract to the body (5, 6, 10, 11, 18), or fixes prose
(7, 8, 12–17, 19). Item 20 adds committed evidence.

## (ii) SCIENCE items — for `NEXT_SCIENCE_LEDGER.md`, not for a review round

| id | item | why it is science, not editing | named blocker / cost |
|---|---|---|---|
| `A3-4` | **Re-derive $r$** for the three bounce backgrounds under the same S1 prescription used for $f_{\rm NL}$, and test against $r<0.036$ | The paper currently carries $r=0.84$ as an unresolved imported number (`DA3M-06`, open since R1). Until it is derived, the fourth-channel statement of item (i)-12 is a conditional, and the honest completeness of "three nulls" cannot be settled | tensor mode functions through the bounce on all three backgrounds; local CPU, days of derivation, not a re-run |
| `A3-1e` | **Resolve the Choudhury sign disagreement** at $\gamma_{\rm cr}\lesssim0.85$ | `:929–930` records that this implementation finds *enhancement* where Ref. [16] reports *suppression*, and the model's own shape ($\gamma_{\rm cr}\in[0.27,0.63]$) sits entirely in that regime — so the headline PBH ratio is conditional on an unresolved sign | **Blocker: their spectrum is not reconstructible from the published paper** (`DA3M-R5-F11`, `R3-R3`), so a re-run at their parameters is impossible. Realistic route: analytic diagnosis of the $J(\gamma_{\rm cr})$ sign structure in `pbh_compaction_fnl.py` step (4). **Extending the 27-point grid does NOT address this** and is not the fix (Grok has now asked for it 3 rounds running) |
| `A3-ns` | **Evaluate Eq. (A3) at the $\epsilon$ that gives $n_s=0.9649$** via $n_s-1=12w/(1+3w)$ and quote the shift in $f_{\rm NL}$ | The propagated spectrum uses $n_s=0.9649$ while Eq. (1) is the $w=0$ value; the shift is expected $O(1\%)$ but is currently unstated. It is a **new number**, so it is (ii) even though it is cheap | one evaluation of the committed general-$\epsilon$ formula; local CPU, minutes |
| `A3-dN` | **Identify the mechanism of the second-order $\delta N$ piece** (currently "a computed identity, not a claimed mechanism") | The only route that would *close* the factor-of-two adjudication rather than bound it (Fable Q2, Grok E6 substance) | open theory question; no committed path |
| `DESI-4` | Wide-angle corrections (`PowerSpectrumOddWideAngleMatrix`) + the 3 blocked systematics splits (E(B−V), stellar density, depth) | Would shrink the reproduction's $\sigma=25$ toward the published $9.0$ | splits blocked on locating the DR9/Legacy imaging pixweight VAC (`LEDGER4_RESULT_v3` §6) |

# 8. Directive-R2 statement

**After v3M.0.14, rounds STOP on A3M.** R6 is the third consecutive verification round on this
paper, and its yield confirms what R5 already indicated: the reviewer legs have stopped finding
physics. Of 41 findings across three legs, **zero** identified an error in a derivation; the single
numerically-wrong statement (`R6-01`) is a unit-conversion slip whose correction makes the paper's
own null stronger, and every remaining real item is abstract-to-body calibration, attribution, or
sourcing — precisely the genre/presentation residue directive R2 names as the signal to stop. The
verdict words (REJECT, MAJOR REVISIONS) are not evidence to the contrary: Grok's REJECT rests on
`F1` (falsified for the third time), `O1` (length), and abstract wording; Gemini's MAJOR REVISIONS
rests on two abstract sentences, a DOI, and one arithmetic claim that is itself falsified (`F3`).
Another round would re-flag `RF1` a fourth time and `RF7` a sixth. **The remaining movement on A3M
is a science decision, not a review decision:** `A3-4` (does this background predict $r=0.84$, and
is it therefore already excluded?) and `A3-1e` (is the PBH ratio's sign structure right at the
model's own shape?) are the two items that would change what the paper can claim. v3M.0.14 closes
the (i) list; no further round may be dispatched on A3M until a decision is taken on (ii).
