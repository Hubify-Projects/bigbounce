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
