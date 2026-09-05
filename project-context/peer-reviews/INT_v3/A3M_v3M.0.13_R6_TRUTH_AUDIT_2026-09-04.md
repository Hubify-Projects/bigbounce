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
