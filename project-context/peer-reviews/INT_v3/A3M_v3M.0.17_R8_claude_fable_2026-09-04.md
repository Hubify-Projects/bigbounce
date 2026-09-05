# INT_v3 referee report — A3M v3M.0.17 — R8 — Claude Fable 5.1 — 2026-09-04

- PDF reviewed: `research/track_a3_multichannel/paper/main.pdf` (byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.17.pdf`)
- sha256: `5ada01728d4eb2ebc5c24e81c9c66fbf6dcf16f9164b1875e257056124d220f0`
- Pages: 18 (all read, incl. appendices)
- Date: 2026-09-04
- Venue standard: Physical Review D (regular article), independent skeptical referee
- Stance: no prior review history, SSOT, dispositions, or earlier reports consulted; no expected verdict given.

## Summary (5 lines)

1. The paper re-derives the matter-contraction squeezed amplitude f_NL = −35/16 vertex-by-vertex (Table I), attributes the factor of two in Cai et al. 2009 to their amplitude-normalization step, and adds a per-vertex/shift ([L]/[K]/[X]/[S]) reading of the δN discrepancy (Appendix A).
2. Transmission through three explicit bounce backgrounds is reported as a two-scheme band, S1 f_after ∈ [−0.65, −0.50], S2 (Quintin-type only) ≈ −1.25, with the bounce's own cubic term Eq. (7) now computed in S1.
3. The same background gives r = 24 (S1 identity) or ≈ 9.4×10² (S2), and a joint (r, f_NL) window in c_s (Eq. 16; Table VII) that is empty: c_s < 1.5×10⁻³ for r vs. c_s ≥ 0.60 for |f_after| ≤ 5.1.
4. A curvaton spectator is presented as the surviving route; PTA, PBH and SMBH-seed channels are honest nulls; a DESI DR1 QSO reproduction (−2.2 ± 25) is consistent but under-powered.
5. My own checks reproduce essentially every number in Tables III–VII and the PTA/PBH arithmetic; the problems are in (a) the operator content behind Eq. (16) for c_s ≠ 1, (b) an internally inconsistent label map in Appendix A, (c) a stale r = 0.84 "open item" in Sec. IV D that contradicts Sec. VII, and (d) several scope overstatements.

## Independent verification performed (own derivations + one committed script)

- Table I sum: −25/16 − 5/32 − 15/32 = −35/16; μ² coefficient −15/16 + 15/8 = +15/16. Correct.
- Eq. (A3) at ε = 3/2 gives −35/16 + (15/16)μ²; angular monopole −5(ε−3)(ε−6)/18 = −15/8; ρ-slice 5(ε−7)/8 = −55/16. All correct. The general-ε identity 5ε(9−ε)/18 = 5ε(9−2ε)/36 + 5ε/4 holds algebraically.
- Eq. (7)/Table III: Δf^bounce = −(5/24)(1−2T) gives −0.140/−0.104/−0.127 and f_after = −0.501/−0.651/−0.555 for T = 0.165/0.250/0.196; abstract's −85T/48 − 5/24 is the same expression. Correct. −35/8 row: −0.862/−1.198 → "[−1.20, −0.86]". Correct.
- Eq. (16): with the P(X,φ) ζζ̇² coefficient a³(ε/c_s⁴)(ε − 3 + 3c_s²) and ε_eff = 1/2, the ratio to c_s = 1 is exactly (6c_s² − 5)/c_s⁴, so the closed form follows from the stated vertex coefficient. I read the cited script `research/cubic_bounce_transmission/row18b_cs_bounce_cubic/row18b_cs_bounce_cubic.py` (+ its log/results.json): V2 (ζζ̇²) carries the total at every c_s (V1 ζ̇³ ≈ 10⁻⁷, V4 ≈ 10⁻³ relative), the c_s = 1 gate matches lane (b) to 3×10⁻⁶, and the window numbers (c_s ≥ 0.599665 → r ≥ 14.392; f_after(1.5×10⁻³) = 1.38×10¹¹) are reproduced by hand: at c_s = 0.6, T f_pre = 0.165×12.257 = 2.022, Δ = +3.059, sum 5.08. Correct. BUT the script explicitly sets λ → 0, η_sr → 0, s → 0 (docstring lines 20–22; results.json "validity"), and the paper never states the λ = 0 (P_XXX) assumption — see MAJOR 1.
- r = 16ε c_s^{2ν−2}: dust has ν = 3/2, so r = 24c_s; r(0.036) → c_s = 1.5×10⁻³; f_pre(1.5×10⁻³) = 65/(8c_s²) − 165/16 = 3.61×10⁶. Correct; 24c_s at c_s = 1 is consistent with r_after = 24 (S1 identity). S2: 24(6.06/0.970)² = 937. Correct.
- Curvaton Eq. (17): P_curv/P_adiab = (r_dec²/9)(8ε)/σ*² = (4/3)r_dec²(M_pl/σ*)² at ε = 3/2; f_NL^curv zero at r_dec = 0.581, −1.25 at r_dec = 1. Correct.
- PTA: γ = 5 − 2(n_s−1) = 5.070; z = (5.07−3.2)/0.365 = 5.1σ; refit z's 1.14/6.37/4.63/1.48σ and official 0.55/4.9/3.1/3.29σ all reproduce; quadrature σ = 0.528. Correct.
- PBH: ζ_max = −5/(12f_NL) + (3/5)|f_NL|σ² → 0.09524/0.19048; with σ = 0.1 → 0.1215/0.2036. Correct. 89149²/(2 ln 10) = 1.73×10⁹. Correct.
- DESI: 0.16σ, 0.77σ, 0.24, 0.06σ all reproduce. Table VI significances all reproduce from Table III and the quoted σ's.
- References spot-checked against arXiv: [1] JCAP 0905:011; [4] JCAP 1703:031 (arXiv Dec 2016); [6] EPL 101, 39001; [16] EPJC 85, 472 (abstract confirms 10⁻³ ≤ f_PBH ≤ 1 and the ≈ −60 perturbativity bound); [25] JCAP 1103:003. All correct. The −320/π⁴ attributed to [25] could not be confirmed from the abstract (see Questions).

## Verdict

**MAJOR REVISIONS.** The science is careful and nearly every number is reproducible, but four items must be fixed before PRD acceptance: an undisclosed λ = 0 assumption behind the k-essence no-go; an internally inconsistent label map in Appendix A (the paper's own "label-resolved" statement); a stale r = 0.84 "open item" in Sec. IV D that contradicts the r = 24 identity of Sec. VII; and a categorical "scheme-independent / no continuation rescues it" claim resting on two schemes and one S2 background.

## MAJOR

**M1 — Eq. (16) / Table VII / abstract (pp. 12–13): the "canonical or k-essence" no-go silently assumes λ ≡ P_XXX-type coefficient = 0 (and s = 0, η = 0).** The cited script `row18b_cs_bounce_cubic.py` sets `lambda -> 0` (docstring lines 20–22; results.json "validity" string: "P(X,phi) cubic action only ... f_NL^pre inherits Li+2016's kinetic sector"), so the ζ̇³ vertex enters only through Σ(1 − 1/c_s²). The paper states instead that "the whole effect is carried by the vertex coefficients, dominated (99.97%) by ζζ̇²" and concludes "the single-field matter bounce, canonical or k-essence, is therefore excluded". A general P(X,φ) has a free λ/Σ that multiplies the same ζ̇³ kernel; the paper neither states the assumption nor bounds the λ-term. Likewise Eq. (15) is quoted from Li et al. without stating which kinetic sector (λ) it assumes. *Resolves:* state the λ = 0, s = 0 assumption explicitly in Sec. VIII and the abstract's "k-essence" qualifier; since the script shows the ζ̇³ kernel contributes ~10⁻⁷ of V2 at λ = 0, add a one-line bound on how large λ/Σ would have to be to matter (the kernel is already computed), or restrict the no-go to the Li et al. kinetic sector by name.

**M2 — Appendix A §2 (p. 15, right column, lines around "f_map"): the printed second-order map is internally inconsistent with the sentence that describes it.** The text gives f_δNc = f_in-in/λ + f_map with λ = 1 − ε/3 and f_map = −5ε/4 + (5ε/4)μ², and calls this "an isotropic monopole of exactly −5 for every constant ε". (i) An expression containing μ² is not isotropic; (ii) −5ε/4 ≠ −5; (iii) evaluating at ε = 3/2: 2(−35/16 + 15/16 μ²) + (−15/8 + 15/8 μ²) = −25/4 + (15/4)μ², which is exactly the *final-position-label* value f^fin quoted two sentences later, not the initial-label −5. For the initial-label result to be −5 one needs f_map = −5/8 − (15/8)μ² at ε = 3/2. So either the printed f_map is the final-label map mislabeled as the initial-label one, or the "exactly −5" statement is wrong; as printed, the paper's "label-resolved" reconciliation of δN_c = −5 with the in-in −15/8 + (15/16)μ² does not close. *Resolves:* print both maps (initial-label and final-label) with their general-ε forms, show explicitly that f_in-in/λ + f_map^init = −5 (isotropic) and f_in-in/λ + f_map^fin = −25/4 + (15/4)μ², and correct the prose. Since Sec. II D and the Scope statement lean on this appendix, the correction must propagate there.

**M3 — Sec. IV D (p. 7, right column) contradicts Sec. VII (p. 12).** Sec. IV D says: "the unresolved r = 0.84 matter-bounce scenario (open item, not adopted). If the r = 0.84 of the unresolved matter-bounce item were confirmed ... resolving r for these backgrounds is an open item (Sec. IX)." Sec. VII then states r = 24 is an identity for this background and that "a tensor-sense r = 0.84 is not used here: it traces to the noise-weighted bispectrum shape-overlap coefficient of Sec. VI, a shape correlation and not a tensor-to-scalar ratio." Sec. IX C lists no such open item. A reader of Sec. IV D is told r is unresolved and possibly 0.84; the abstract and Sec. VII say r = 24 exactly. *Resolves:* delete the r = 0.84 tensor scenario from Sec. IV D (and Fig./caption text if any), replace with the first-order tensor background at r = 24 (which Sec. VII already propagates: Ω_GW h²(f_yr) = 1.7×10⁻¹⁴, 10^6.2 below NANOGrav), and fix the dangling "(Sec. IX)" cross-reference.

**M4 — Abstract, Sec. VII (p. 12) and Sec. VIII: "scheme-independent" and "no choice of scalar continuation through H = 0 rescues it" overstate what was computed.** S2 is evaluated on the Quintin-type background only (Table III, Table VI, Sec. IX C item iv); two continuations (z = a and the raw-ADM effective-fluid variable) were tested. The paper elsewhere is careful to say "which scheme's linear variable is physical at H = 0 remains an open theory question"; if that is open, a third continuation is not excluded by these two. The abstract's own final clause ("on the backgrounds and channels evaluated here") has the right scope; Sec. VII's "no choice of scalar continuation ... rescues it" does not. *Resolves:* rephrase to "in both continuations evaluated here (S1 on three backgrounds, S2 on one)"; state the structural reason if one exists (e.g. any continuation with λ_ζ ≤ λ_T worsens r; a rescue needs λ_ζ ≳ 26 λ_T, which the velocity-dip test bounds at λ_ζ ≤ 6.1 for the Quintin mechanism) — that would make the claim defensible without the categorical wording.

## Minor

1. Three different quantities are called r: tensor-to-scalar ratio (Secs. VII–VIII), the mode-mixing coefficient r = −9iA²I∞/k³ (Sec. III), and the bispectrum shape overlap (Sec. VI). Rename the latter two.
2. Table VII / Sec. VIII use "|f_after| ≤ 5.1 (Planck 1σ)"; Planck 2018 gives f_NL^local = −0.9 ± 5.1, so the 68% interval is [−6.0, +4.2]. The k-essence value at c_s = 0.6 is *positive* (+5.08), which sits 1.17σ from Planck's centre; using the actual interval moves the boundary to slightly larger c_s (stronger no-go). State which criterion is used and recompute.
3. Sec. IV D cites "§V B's T_B ≳ 10⁸ GeV"; the validity condition T_B ≳ 6×10⁹–6×10¹⁰ GeV is in §V C, and 10⁸ GeV is there labelled an illustrative value *below* the condition. Fix the cross-reference and the number.
4. Eq. (12) is displayed as the headline PBH ratio (1.732 ± 0.050) while the abstract quotes 1.84 ± 0.03 from the extended scan; Table V's caption explains, but the displayed equation should carry the number the abstract quotes.
5. Curvaton: the range "+9.30 to −1.25" corresponds to r_dec ∈ [0.113, 1]; the lower limit and its origin are not stated.
6. Reference [4] is called "Li et al. 2017" (abstract, Sec. IX A) and "Li et al. (2016)" / "Li, Quintin, Wang & Cai (2016)" (Secs. VIII, Table VII). Use one year.
7. Ledger jargon ("row 10", "row 14", "ledger row 18(a)/(b)", "lane9c2", "D-A3-9") appears in the body and captions; move to the reproducibility statement.
8. Table V footnote: the ΩDM = 0.6741 transcription error from [16] is knowingly propagated into the tabulated f_PBH and Fig. 2; use 0.264 and note the discrepancy with [16] in the footnote instead.
9. Sec. II D and Appendix A both state the Bianchi-I argument nearly verbatim; keep one.
10. Table IV lists "Matter bounce γ = 3" as a hypothesis row although the text establishes γ = 3 is not this model's prediction; relabel the row "Papanikolaou-type enhanced source (contrast)".
11. Reproducibility statement: code is pinned to commit 68309c8 for Secs. II–III but "at the current HEAD" for the row-9/S2 work; a journal version needs one immutable pointer (DOI) for all of it.
12. Fig. 1: axis/legend text is small at column width; the NANOGrav band and the two predicted lines should be labelled directly.

## Questions for the authors

Q1. Is it a coincidence that the linear map factor 1/(1 − ε/3) = 2 at ε = 3/2 (Eq. 5) equals the Cai et al. factor of two you locate at their normalization step? A sentence ruling out (or acknowledging) a connection would pre-empt referees.
Q2. Where in Ref. [25] does −320/π⁴ ≈ −3.29 appear, and what is the "order-of-magnitude estimate" it is arithmetic on? I could not confirm it from the abstract.
Q3. In S2 the growing mode is transmitted with |λ_ζ| = 0.97 while the tensor grows by 6.06. Since the post-bounce scalar amplitude is anchored to A_s, does the S2 pre-bounce amplitude (6.25× larger than S1's) remain within the perturbative regime of the cubic bounce-window integral you evaluate?
Q4. Eq. (15) is quoted from Li et al.'s Eq. 4.19: is their squeezed limit taken at fixed angle (μ = 0 isosceles) or angle-averaged? Your Eq. (4) shows these differ (−35/16 vs −15/8); the c_s-dependent version should say which.

## Integrity note

No prior review history, SSOT, dispositions, or earlier referee reports were consulted. Verification used my own algebra plus one committed script (`research/cubic_bounce_transmission/row18b_cs_bounce_cubic/row18b_cs_bounce_cubic.py`, its `.log` and `results.json`) and arXiv abstract pages for five references. All numerical checks listed above passed; the MAJORs are scoping/consistency issues, not arithmetic errors, and none is a fabricated-derivation flag. No expected verdict was supplied.
