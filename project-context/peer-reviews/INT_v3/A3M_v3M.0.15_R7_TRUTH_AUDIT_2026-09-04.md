# A3M v3M.0.15 — R7 truth-audit (skeptical, 2026-09-04)

**Plan header.** Auditor was given no expected outcome. Exact artifact bound: sha256
`909cf789…`, md5 `4f2bf5e8…`, 17 pp; source-dir `main.pdf` == served
`site/public/papers/a3_multichannel_arxiv_v3M.0.15.pdf` (verified). Legs: Grok_brutal (REJECT),
Gemini_cosmology (MAJOR REVISIONS), Claude Fable 5.1 INT (major-revisions, 5M/14m/5Q).
Board: `../A3M_v3M.0.15_R7_BOARD_2026-09-04.md`.

Method: fingerprint every finding from all three legs; class
(a) genuinely-new-real · (b) re-flag-of-already-addressed · (c) falsified ·
(d) opinion/genre/venue · (e) disclosed-limitation/out-of-scope.
Prior canonical: `../DISPOSITIONS/A3M.md` (R6 audit, directive R2 STOP in force).
Physics verification targets this round: Fable M1 (Cai+2009 ×2 localisation), M2 (scheme-dependent
r_after in S2), M3 (PBH sign vs Table V), M4 (Ref. [25]), M5 (c_s window), plus Grok/Gemini ESSENTIALs.

*(sections appended below as the audit proceeds)*

---

## Per-leg counts (fingerprinted)

| leg | verdict | raw findings | (a) new-real | (b) re-flag | (c) falsified | (d) opinion | (e) disclosed |
|---|---|---|---|---|---|---|---|
| Grok_brutal | REJECT | 10 | 1 (M2, shared) | 1 | 5 | 3 | 0 |
| Gemini_cosmology | MAJOR REVISIONS | 9 | 4 (E1,E2,E5,E6) | 2 | 2 | 1 | 0 |
| Fable INT | major-revisions | 24 (5M/14m/5Q) | 11 | 3 | 2 | 4 | 4 |
| **canonical union** | — | **43 raw → 27 distinct** | **16** | **4** | **9** | **6** | (4 carried) |

## (a) GENUINELY-NEW-REAL — canonical list

**`R7-01` MAJOR — `r=16ε=24` "exactly, bounce-invariant" is a scheme-S1 statement.**
`main.tex:46` (abstract) and `:1232–1233`. `row10_r_ns/results.json` computes the tensor
transfer on all three backgrounds (`mu_T_over_mu_S_at_handoff`, `max_abs_T_h_over_T_zeta_minus_1
= 7.98e-5`) against the **S1** scalar transfer (`T_zeta` = 5.115 poly, 4.000 LQC, 6.061
Quintin-type = the S1 `λ_ζ` of `main.tex:368`); `row14_cs_window/results.json` likewise pairs
`lambda_tensor` with the S1 `lambda_scalar` (`lambda_ratio_minus_1 ≤ 5.6e-13`). The paper's own
S2 raw-ADM continuation transmits `|λ_ζ|=0.97` (`main.tex:364`, `:543`) while tensors are
scheme-free (`z_T=a`), so on the Quintin-type background
`r_after[S2] = 24·(6.06/0.97)² = 9.37e2`. Fable M2/Q1 is correct; this is a scoping
**correction**, not editorial. The no-go survives *a fortiori* (S2 makes `r` worse).

**`R7-02` MAJOR — auditor-originated (directive I6): the embedded Fig. 1 PNG is stale.**
`paper/sigw_nhz_from_lab_spectrum_2026_09_04.png` md5 `8e749a23…` (Sep 4 16:20, commit
`044ea88c`) ≠ `outputs/…png` md5 `af783c0a…` (17:18, commit `87e3d6e2`, the R6-02 Channel-I
pairing fix). Rendered: the paper's copy legends the NANOGrav curve `A=2.4×10⁻¹⁵`, the
**superseded** γ=13/3-fixed amplitude; the current generator prints `A=6.46×10⁻¹⁵`
(`sigw_nhz_from_lab_spectrum_2026_09_04.py:264`). Same failure class as the P1A Fig-1 trap that
created directive I6. No reviewer named this.

**`R7-03` MAJOR — the `c_s` sign change is committed but absent from the paper.**
`row14_cs_window/results.json → window.f_NL_sign_change_c_s = 0.8876`, with the committed note
"`f_NL^pre < 0 for c_s > 0.8876 and > 0 below it, so the flagship negative sign does not survive
on the tensor-viable branch`". The abstract's `f_NL`-allowed window is `c_s ≥ 0.444`
(`main.tex:53–54`); on `c_s ∈ [0.444, 0.888)` the k-essence prediction is **positive**. Nowhere
in `main.tex` (grep `0.888` → only a γ_cr table cell). Fable M5 confirmed.

**`R7-04` MAJOR — the window formula drops `Δf_NL^bounce`.**
`row14_cs_window.py:185 cs_for_fnl_after` applies `T × f^pre(c_s)` only, while every other
transmitted number in the paper is `T f^pre + Δ` (Eq. 7, derived at `c_s=1`). Numerically
immaterial (`Δ=−0.14` vs 5.1) but the paper asserts full `c_s`-independence of "the
transmission", verified only for the LINEAR transfer. State the formula used and its scope.

**`R7-05` MAJOR — bibliography entry `CaiXue2011` is internally inconsistent with the lab's own
source-of-record.** `main.tex:1798–1800` prints "Cai, Xue, Brandenberger, *Non-Gaussianity in a
Matter Bounce*, JCAP **05**, 011 (2011), arXiv:0912.2951", and the body attributes the curvaton
result (`−320/π⁴`, "Eqs. (62)–(64)") to it; the lab's committed curvaton adjudication
(`research/theory_audit/curvaton_matter_bounce_adjudication_2026_09_04.md:13,39`) reads
**arXiv:1101.0822 (CXB11)** in full as the source of those equations. Fable M4 independently
reports 0912.2951 resolves to an unrelated MNRAS paper (not verified here). Either way the
citation must be rebuilt from `1101.0822` and the quoted equation numbers re-checked against it.

**`R7-06` minor — abstract `|f_NL| ≤ 5.1` must read `|f_NL^after|`** (`main.tex:53–54` vs
Table VII / Sec. VIII, which apply the bound to the transmitted amplitude). Gemini E1.

**`R7-07` minor — abstract's no-go lacks the body's scope qualifier.** `main.tex:55–57` vs
`:1261+` ("on the backgrounds and channels used in this paper"). Gemini E2 = Grok M2.

**`R7-08` minor — Table V rows vs "suppresses throughout".** `main.tex:947–949` states the
adjudicated result correctly (`row11_pbh_residuals` item (a): the IR-finite `O(ε)` term
suppresses at every γ_cr; the enhancement is the IR-divergent `½ν⁴(6γ_cr²−1)ε²` branch). But the
γ_cr = 0.766 row prints `f_PBH(−35/16)=3.5e3` — which reproduces `row11`'s own
`β/β_G = 3.5e+3` at that γ_cr — i.e. the table's `γ_cr ≲ 0.8` rows at the flagship amplitude sit
on exactly the branch the text disqualifies, unlabelled and uncapped. Fable Q3 answered: `A_*`
IS per-point Gaussian-calibrated (`row11_choudhury_sign.py` part B). Fix is labelling, not physics.

**`R7-09` minor — NANOGrav reference amplitude inconsistent.** `main.tex:754,782` uses
`Ω_GW h²(f_yr)=2.622e-8`; `outputs/r5_15_tensor_omega_nhz.json:25` uses `3.6235e-09` (factor
7.2), and the "10^5.3 below" / "8–9 orders" statements come from that JSON. Fable m2.

**`R7-10` minor — an unpublished companion draft is cited by repo path.** `main.tex:1621`
("imported from this lab's companion Fisher-forecast draft at …"). Gemini E5.

**`R7-11` minor (RESIDUAL of `DA3M-08`/`R6-06`, 3rd recurrence) — internal version-history
prose.** `main.tex:968` "noted in earlier drafts", `:1254–1255` "appeared in earlier drafts of
this program; it is withdrawn here", `:1151` "(open item `DESI-4`)". Gemini E6.

**`R7-12` minor — abstract `n_s=1 exactly` beside `n_T=n_s−1=−0.035`.** `main.tex:47–48`. At the
Planck-anchored ε the committed value is `r=23.93`, not 24 (`row10 results.json →
analytic.planck_anchored: w=−0.0029, eps=1.49565, r=23.9304`). Fable m1.

**`R7-13` minor — a false statement and a non-existent argument.** `main.tex:793–796`:
"`T_B≈2.3 GeV` … below the QCD scale — excluded by this paper's own baryogenesis argument".
2.3 GeV is *above* the QCD transition (~0.15 GeV), and `grep baryogen main.tex` returns only
this line. Fable m3.

**`R7-14` minor — the Cai conversion sentence attributes a formula Cai do not print.**
`main.tex:221` says the shape function "is converted to the quoted amplitude via
`f_NL=(20/3)A/Σk³`". The lab's own adjudication states this as *effective*
(`fnl_matter_contraction_adjudication_2026_09_02.md:32`, "effectively their Eqs. 38–40"), and the
committed definition is `(10/3)` (`…adjudication_2026_09_02.py:36,477`). Insert "effectively".
Fable M1(a) is right on the wording, wrong to call it an error of substance.

**`R7-15` minor — the (37)=(4.19) claim is repeated at `:222–223` without its qualifier.** The
distinct-monomial reading is stated once at `:211–213`; the second statement reads unconditional.
Under the six-permutation reading the difference is `−(99/128)Σk³` and the squeezed limit is
`−305/64` — exactly Fable M1(b), and exactly what the committed script prints as the *alternative*
reading (`…adjudication_2026_09_02.py:448–453`). Repeat the qualifier.

**`R7-16` nit — auditor-originated:** Fig. 1's log minor-tick labels collide on the x-axis
(`3×10⁰` overprints `4×10⁰`; same at `3×10¹`/`4×10¹`). Fix in the regeneration for `R7-02`.

## (c) FALSIFIED — with citation

`C1` **Grok E1** "the paper claims an exact/scheme-independent transmitted amplitude" — `:41–43`
prints *both* schemes in the abstract ("S1 gives `[−0.65,−0.50]`, S2 gives `≈−1.25`"). 4th
consecutive recurrence (`R4-F1`/`R5-F1`/`R6-F1`).
`C2` **Grok E2** "`γ_pred` and the NANOGrav posterior juxtaposed without the qualifier" — `:651`
carries it verbatim ("differently-conditioned cross-check, not directly comparable to it").
`C3` **Grok E4** "Table VI's S2 row lacks the qualifier" — `:501–502` carries it.
`C4` **Grok M3** "the `296×` disjointness has no numerical integral or code pointer" — `:1665`
cites `row14_cs_window.py`+`results.json`; the value `296.0` is in that JSON.
`C5` **Grok N1** "'scheme-qualified linear transfer' repeated verbatim in three consecutive
paragraphs" — the string does not occur in `main.tex`.
`C6` **Grok N3** future date — `DA3M-F3`, **11 consecutive rounds, 100% falsified**.
`C7` **Gemini M1** "Fig. 1's plotted line sits at `~10⁻¹⁴`, i.e. the primordial not the induced
background" — the plotted lab curves are at `1.38–1.76e-23` (anchored) and `5.88e-23` (pure
dust): `outputs/sigw_nhz_from_lab_spectrum_2026_09_04.json → curves_Omega_GW_h2`, confirmed by
rendering the embedded PNG. The `~10⁻¹⁰–10⁻⁸` band is the NANOGrav/γ=3 reference curves. The
figure is nevertheless defective for a different reason — see `R7-02`.
`C8` **Gemini E7** "the the" at Sec. IX.C — no such string (`grep -E '\bthe\s+the\b'` and a
whitespace-insensitive perl scan both return nothing). LaTeX line-break artifact; same class as
`R6-F4`.
`C9` **Fable M1(b)** "not reproducible / (37) ≠ (4.19)" — both readings of the `(5,2,2)` sum are
computed and printed by the committed script (`…adjudication_2026_09_02.py:448–461`); under the
distinct-monomial reading the difference is 0, under the six-permutation reading it is
`−(99/128)Σk³`. The residual is wording only (`R7-15`).

## (b) RE-FLAG-OF-ALREADY-ADDRESSED

`B1` **Grok E3** (γ_cr grid truncated at 0.63; cutoff systematic not in the ±) — `:955–967`
prints the 255-point `[0.196,0.968]` scan (`1.83±0.05`, range `[1.61,1.91]`), the coverage-restricted
`1.84±0.03`, and the 27-point `1.732±0.050` with "must not be quoted as universal". `RF1` class,
4th recurrence.
`B2` **Gemini E3 + Fable m13** frozen-release DOI / journal versions — `RF8`, carried packaging
(a git commit hash IS pinned, `:1652–1655`).
`B3` **Gemini E4** "`free_spectrum_real_2026-05-01/` predates the paper" — that is the provenance
date of the NANOGrav 15-yr free-spectrum chain run, not staleness; one clarifying clause closes it.
`B4` **Fable M3 second half** ("demote `1.84±0.03` out of the abstract") — `:940–950` already
disqualifies the enhancement branch and `:962–966` already restricts the quoted interval to the
model's own coverage. Re-flag; the labelling residual is `R7-08`.

## (d) OPINION / GENRE / VENUE — no edit required

`D1` Grok M1 "17 pp for an incremental result / a 4–5 page note would do" — `O1` recurrence.
`D2` Grok N2 Fig. 1 prefactor — the kernel and normalisation are given (Sec. IV D, generator
docstring lines 22–39).
`D3` Grok M2 tail (rhetorical strength of "newly expose") beyond the real scope clause `R7-07`.
`D4` Gemini M2 quantify "weakly" in the Table V caption — a slope number is cheap; folded into (i).
`D5` Fable m4, m10, m11 (presentation of `r<0.036` vs 11.5/23; `n_T` as a class relation; Table IV
extra column) and Q5 (1σ vs 95% Planck bound — the no-go holds either way).
`D6` Fable m14 (promote App. A's `f_map`/boundary term, or relabel the appendix).

## (e) CARRIED — real-shaped but UNVERIFIED this round; verify in the v3M.0.16 lane

`E1` Fable m5 (state the `r_dec` interval behind `f_NL^curv ∈ [+9.30, −1.25]`) ·
`E2` m6 (Li *et al.* cited as 2016 and 2017 in the same abstract — harmonise) ·
`E3` m7 (Table II `|f_NL|`=112/1216 vs the "no order-10³ plateau" claim at `:435–439`, and the
Sec. V C range mixing the `kη_B=3` and `10` rows) · `E4` m8 (post-bounce evaluation time behind
the four-digit S2 values) · `E5` m9 (the `Ω_DM=0.674` footnote vs the Gaussian calibration,
`:1008–1013`) · `E6` m12 (the DESI `0.06σ` uses the reproduction's own σ — say the two are not
independent) · `E7` Fable Q2/Q4 (Cai multiplicity convention; `c_s`-dependence of
`Δf_NL^bounce`) — Q4 is a science question, routed to (ii).

## Integrity note

No leg was told an expected outcome; verdict words were read from the raw text, not from labels.
Every classification above cites a committed file+line or a JSON key. Two reviewer MAJORs
(Grok's REJECT rationale, Gemini's Fig. 1) rest on findings falsified against committed
artifacts; the strongest real finding of the round (`R7-02`, the stale figure) was found by the
audit, not by any reviewer.

---

# CLOSURE PLAN

## (i) Editorial / real edits for v3M.0.16 — exact lines

1. `main.tex:46` — "`r=16ε=24` exactly, bounce-invariant" → "`r=16ε=24` **before the bounce**;
   the transfer is scheme-dependent — `r_after=24` in S1 (tensor and scalar share `z=a`, so the
   equality is structural there, `|T_h/T_ζ−1|≤8×10⁻⁵`), while S2's raw-ADM continuation gives
   `r_after≈9.4×10²` on the Quintin-type background. The no-go is unaffected (S2 worsens `r`)."
   Same scoping at `:1232–1233`, and in Sec. VIII where Quintin *et al.*'s scalar-only
   amplification is dismissed — say that test is available only in S1. [`R7-01`]
2. Regenerate Fig. 1 from `sigw_nhz_from_lab_spectrum_2026_09_04.py` **with the publication
   labels/title of commit `044ea88c`**, i.e. re-apply those labels to the current
   (post-`87e3d6e2`, `A=6.46×10⁻¹⁵`) curves; widen/thin the x minor-tick labels; mirror
   byte-identical into `paper/` and `outputs/`; verify by rendering p. 8 of the recompiled PDF,
   not by filename. [`R7-02`, `R7-16`; directive I6 + G]
3. `main.tex` Sec. VIII / Table VII — add: "`f_NL^pre(c_s)=−165/16+65/(8c_s²)` changes sign at
   `c_s=0.8876`; on `c_s∈[0.444,0.888)` the constant-`c_s` k-essence branch predicts a
   **positive** local amplitude, so the flagship negative sign survives only for `c_s≳0.89`."
   [`R7-03`]
4. Same section — state the window formula actually used (`T×f^pre`, no `Δf_NL^bounce`), why
   (Eq. 7 derived at `c_s=1`), and that `Δ=−0.14` vs the 5.1 bound. [`R7-04`]
5. `main.tex:1798–1800` — rebuild `\bibitem{CaiXue2011}` from **arXiv:1101.0822** (Cai,
   Brandenberger & Zhang, *The Matter Bounce Curvaton Scenario*, JCAP **03**, 003 (2011)), the
   source the lab's own curvaton adjudication reads; re-check the `−320/π⁴` quote and the
   "Eqs. (62)–(64)" pointer against it, or drop the quote. Add bibliography entries for
   Lyth–Ungarelli–Wands, Sasaki–Väliviita–Wands, and the Planck 2018 `f_NL` used in Table VII.
   [`R7-05`, Fable M4]
6. `main.tex:53–54` — `|f_NL|` → `|f_NL^{after}|`. [`R7-06`]
7. `main.tex:55–57` — append "on the backgrounds and channels evaluated here". [`R7-07`]
8. Table V (`tab:pbh`) — label the `γ_cr ≲ 0.8` rows "**non-perturbative branch**
   (`1.2|f_NL|σ_r ≈ 0.5–2`; IR-cutoff-dependent, see Sec. V B)", state that `A_*` is
   **per-point** Gaussian-calibrated, and mark the `f_PBH>1` entries as uncapped ratios. Reword
   `:947–949` "suppresses … throughout" → "suppresses at first order in `ε=(6/5)f_NLσ_r` at every
   `γ_cr`". Add the requested slope for "decreases … weakly". [`R7-08`, `D4`]
9. Pick ONE NANOGrav reference amplitude and propagate: `main.tex:754,782` (`2.622e-8`) vs
   `outputs/r5_15_tensor_omega_nhz.json:25` (`3.6235e-09`); restate the "`10^5.3` below" and
   "8–9 orders" figures against it. [`R7-09`]
10. `main.tex:1621` — remove the repo-path import of the companion Fisher draft; state the shape
    overlap as an explicit assumed value with its provenance, and keep Table VI's entries labelled
    upper bounds. [`R7-10`]
11. `main.tex:968`, `:1151`, `:1254–1255` — delete all version-history/audit prose
    ("noted in earlier drafts", "(open item DESI-4)", "appeared in earlier drafts … withdrawn
    here"); state the withdrawn `r=0.84` as a plain statement of what the quantity is. [`R7-11`;
    directive Q1]
12. `main.tex:47–48` — "`n_s=1` exactly (pure dust); the observed `n_s=0.9649` fixes
    `w=−0.0029`, hence `ε=1.4957`, `r=23.93`, `n_T=−0.035`". Use `23.9` or `ε=3/2` consistently.
    [`R7-12`]
13. `main.tex:793–796` — delete "below the QCD scale" (2.3 GeV is above it) and the appeal to a
    baryogenesis argument the paper does not make; keep the `T_B` number and its real
    consequence. [`R7-13`]
14. `main.tex:221` — "converted … via" → "**effectively** converted … via". [`R7-14`]
15. `main.tex:222–223` — repeat the distinct-monomial qualifier on the second `(37)=(4.19)`
    statement, and add one clause: under the six-permutation reading the difference is
    `−(99/128)Σk³` (squeezed `−305/64`), which is why the reading must be stated. Cite the
    committed script. [`R7-15`, `C9`]
16. `B3` clarify the `2026-05-01` chain directory as the run date of the NANOGrav free-spectrum
    reduction. `E1`–`E6` verified-then-closed in the same lane.

Then: `/paper-compile-revtex` (0 undef-refs) → `/latex-audit` → directive-G restamp
(`\paperVersion` v3M.0.16, `\date`), re-mirror to all served paths byte-identical, Convex
`paperVersions:bump` with real md5/pages, and a `reviewTimeline` entry for R7.

## (ii) SCIENCE items — named exactly

- **`A3-S2r` — the S2 tensor transfer.** Tensors carry no scheme ambiguity (`z_T=a`), so
  `λ_T=6.06` on the Quintin-type background carries over and `r_after[S2]=24(6.06/0.97)²≈9.4×10²`
  is arithmetic from committed numbers. **Required lane (small):** a `row10b_s2_tensor/` script
  that evolves `h''+2(a'/a)h'+k²h=0` across the **S2 raw-ADM handoff convention** on the same
  background and prints `λ_T`, `r_after[S2]` per `kη_B`, so the quoted `9.4×10²` rests on a
  committed artifact rather than on a hand ratio. Owner lane; does not touch `main.tex`.
- **`A3-cs-bounce` (Fable Q4) — the `c_s` dependence of `Δf_NL^bounce`.** The cubic k-essence
  action carries `(1/c_s²−1)` operators; Eq. (7) was derived at `c_s=1` only. At the `r`-viable
  end (`c_s=1.5×10⁻³`) the window numbers `6–9×10⁵` would move by `O(1/c_s²)` if the bounce term
  scales like the contraction term. Compute `Δf_NL^bounce(c_s)` on the S1 background, or state
  explicitly that the window is quoted with the `c_s=1` bounce term and bound the error.
- **`A3-1e`** (Choudhury `γ_cr ≲ 0.85` sign, analytic route only) — **now CLOSED** by
  `row11_pbh_residuals` item (a); it leaves only the Table V labelling of `R7-08`. Ledger row 9's
  bounce-scale enhancement at `kη_B~1` is unaffected.
- Carried from R6 and still open: `A3-ns` (Eq. (A3) at the `n_s=0.9649` ε), `A3-dN` (mechanism of
  the second-order δN piece), `DESI-4` (wide-angle + the 3 blocked systematics splits).

## R2 statement (directive R2)

R7 is the **fourth consecutive verification round** on A3M. It produced **no physics error**
except `R7-01`/`R7-03` (both scoping/disclosure of quantities the lab had already computed and
committed) and `R7-02` (a stale embedded figure). Both reviewer verdict words rest substantially
on findings falsified above (`C1`–`C8`). **After v3M.0.16 closes the 16 (i) items, rounds STOP on
A3M** until a science decision is taken on the (ii) ledger — `A3-S2r`, `A3-cs-bounce`, `A3-ns`,
`A3-dN`, `DESI-4`. No further round may be dispatched on A3M on editorial grounds alone.
**Clean-wave count: 0** (16 genuinely-new-real findings this round).
