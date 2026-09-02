# A3M v3M.0.3 — INT referee leg R1 (Claude Fable)

- **Reviewer:** Claude Fable (INT leg, independent PRD-standard referee; not told any expected verdict)
- **Model:** claude-fable (claude-fable-5-1)
- **Manuscript:** `research/track_a3_multichannel/paper/main.pdf` — v3M.0.3, 7 pages, dated September 2, 2026
- **sha256 (computed this session, binding):** `7e35caa05825af0e2cac5cadb21b50b68e913c32583914ca4b07ca23c1e469bd`
- **Round:** `ROUND_2026-09-02-A3M-v3M.0.3-EXACTPDF-7e35caa0-R1`
- **Date:** 2026-09-02
- **Method:** all seven pages rendered at 300 DPI and read; `main.tex` grepped for every quoted equation/number; scripts re-run and numbers recomputed independently (Sec. 0); external sources fetched live (arXiv 2306.16213, 1712.08148, 1707.06661, 2311.13082, 2411.17623, 2504.11641, 2409.18983, 1612.02036).

---

## 0. What I recomputed myself (per channel)

| Channel | What I did | Result |
|---|---|---|
| **Theory (Sec. II)** | Re-ran `research/theory_audit/fnl_matter_contraction_adjudication_2026_09_02.py` from scratch (166.9 s, 8 workers). Hand-checked two rows: local field-redefinition part with ζ' = −3ζ/η, ℋ = 2/η gives 3/5·f = −3/2 → f = −5/2 (Table I row consistent); USR check η_sr = −6, ζ ∝ a³ gives 3 − 3/2 = 3/2 → f_NL = 5/2 ✓. | Verdict line reproduced verbatim: f_NL = −35/16; Cai's three amplitudes = exactly 2× the from-scratch values; only diff vs committed JSON is `wall_clock_seconds`. **Confirmed.** |
| **Transmission (Sec. III)** | Re-derived Eq. (5) from the stated premise ζ(η) = C₂[I_∞ + J(η)], J(−η_h) = −ρI_∞, J(+∞) = +I_∞: λ = 2/(1−ρ), T = 1/λ = (1−ρ)/2. Checked `a2_transmission_linear.json`: LQC/S1 ρ_B = 0.5000003 (analytic 1/2), poly ρ_B = 0.60900 (analytic), T ∈ {0.250, 0.1955, 0.1650, 0.4092}; 0.409/0.250 = 1.64, 0.409/0.165 = 2.48. | Arithmetic **confirmed**; the premise is the problem (finding M2). |
| **PTA (Sec. IV)** | Loaded `chain_real_freespec.npy` (320 000 × 2) directly: mean γ = 2.56647, std 0.38183, median 2.59129, [q16, q84] = [2.3041, 2.8822]; log₁₀A = −14.0252 ± 0.3796. z-distances (3 − 2.567)/0.382 = 1.135, (13/3 − 2.567)/0.382 = 4.627, (5 − 2.567)/0.382 = 6.373 ✓. Scott-KDE at γ = 3: B = 3.2276 ✓; at 13/3: 4.52×10⁻⁴ ✓; at 5: 1.86×10⁻²⁴ ✓ (numerically). **Tail census:** chain max γ = 4.705; **0 samples at γ ≥ 5**, 9 samples at γ > 13/3, 34 at γ > 4.0. Histogram density at 13/3 (bin 0.1) gives B = 6.6×10⁻⁴ (vs KDE 4.5×10⁻⁴). Also read the lab's own `results.json`: it records `agazie_2023_official: gamma 3.2 ± 0.6` and `delta_sigma = −1.48` against it — not in the paper. | Numbers reproduce; **two of the three Savage–Dickey rows are KDE-tail extrapolations** (findings M1, M3). |
| **PBH (Sec. V)** | Imported `pbh_compaction_fnl.py` and re-integrated Eq. (60) at the baseline point (Δ = 0.5, r_pk_p = 1, C_th = 0.5, A* = 0.131446): β(0) = 1.194×10⁻¹⁶ → f_PBH = 1.00; β(−35/16) = 4.323×10⁻³⁰ → 3.62×10⁻¹⁴ ✓; β(−35/8) = 1.873×10⁻¹⁸ → 1.57×10⁻² ✓; γ_cr = 0.888 ✓; 1.2|f_NL|σ_r = 0.74 / 1.48 ✓. **Branch split (mine):** the J < 0 branch contributes 0 (−35/16) and 3×10⁻¹³ of β (−35/8) — the reversal is *not* a J-sign artefact. Ratio A(−35/16)/A(−35/8) for f_PBH = 10⁻³ recomputed on the J > 0 branch: 0.21196/0.12227 = **1.7336** (paper 1.734 at this point) ✓. Read `f_NL_continuity_scan` in the committed JSON: f_PBH(f_NL) at fixed A* is **non-monotonic** — 1 → 2.4×10⁻² (−0.02) → 7.5×10⁻⁵⁵ (−0.35) → 3.6×10⁻¹⁴ (−35/16) → 1.6×10⁻² (−35/8) → 89 (−6) → 2.6×10⁶ (−10). Also re-ran the full script (background; results identical to committed up to timing). | Numbers reproduce exactly; the physics disclosure is incomplete (findings M4, m5). |
| **Survey reach (Sec. VI)** | 2.1875/0.7 = 3.125, ×0.84 = 2.625; /0.5 = 4.375, 3.675; /1 = 2.1875, 1.8375; 4.375/0.7 = 6.25, /0.5 = 8.75 ✓. DESI: (−2.1875 + 3.6)/9.0 = 0.157 ✓; (3.5 + 2.1875)/7.4 = 0.769 ✓; 2.1875/9.0 = 0.243 ✓. Live abstracts: Heinrich+2023 σ = 0.7 (bispectrum) and "on target for 0.5 once the power spectrum is included" ✓; Chaussidon+2024 −3.6^{+9.0}_{−9.1} and +3.5^{+10.7}_{−7.4}, N_LRG = 1,631,716, N_QSO = 1,189,129 ✓. r = 0.84 provenance: `survey_reach_fnl.json` says "this lab's P2 forecast"; P2 draft comments give "noise-weighted recovery 0.84 ± 0.02 (0.8354 → 0.84)"; the A3 brief's own item A3-4 flags it as *not yet re-derived at the −35/16 fiducial*. | Arithmetic **confirmed**; provenance issue (M6). |
| **References** | Fetched arXiv:1707.06661 — it is "The Graphical Horseshoe Estimator for Inverse Covariance Matrices" (Li, Craig, Bhadra, stat.ME). Agullo–Bolliet–Sreenath "Non-Gaussianity in loop quantum cosmology" is **arXiv:1712.08148, Phys. Rev. D 97, 066021 (2018)**. | Ref. [7] wrong (M7). |

---

## 1. Findings

### MAJOR

**M1 — PTA: the refit disagrees with NANOGrav's own published HD power-law posterior, and the paper does not say so; the SMBHB "rejection" is therefore overstated.**
*Location:* abstract; Sec. IV B, Eq. (7); Table II; Sec. VII A ("rejecting the two competing spectral shapes").
*Defect:* The paper reports γ = 2.567 ± 0.382 and a 4.63σ / log₁₀B = +3.85 rejection of γ = 13/3. The NANOGrav 15-yr HD-correlated power-law analysis (Agazie et al. 2023, ApJL 951 L8, the paper's Ref. [9]) reports γ = 3.2 (+0.4/−0.6 68%, ≈ ±0.6), fitted on the **lowest 14** frequency bins because the higher bins are white-noise dominated; the lab's own `results.json` records this official value and a −1.48σ offset of the refit from it. The refit here uses **all 30** bins (`emcee_freespec.py`, `N_BINS = 30`), which is the most plausible cause of the downward pull of γ and of the narrower error. Against the official posterior, 13/3 is only ≈ 1.9σ (2.8σ with the +0.4 side) away, and γ = 3 is 0.3σ away — NANOGrav itself describes the signal as *consistent* with SMBHB. A referee will regard the 30-bin refit as a non-standard analysis choice that must be (i) disclosed, (ii) compared with the official value in the text and in Table II, and (iii) tested by repeating the fit on the official 14-bin selection (a ≈ 25 s emcee run). Until then, "disfavouring the supermassive-black-hole binary value … by log₁₀B = +3.85" cannot stand in the abstract.
*Evidence:* my chain re-analysis (Sec. 0); `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/{emcee_freespec.py,results.json}`; arXiv:2306.16213.

**M2 — Transmission: T = (1−ρ)/2 and the "universal bound" are not a bound on the physical f_NL; the derivation assumes cubic sourcing switches off at an arbitrary handoff time.**
*Location:* abstract ("obeys a universal suppression 0 < T ≤ 1/2"); Sec. III, Eq. (5) and the sentence "linear transfer can only suppress the amplitude, never invert or amplify its sign".
*Defect:* Eq. (5) follows correctly from ζ = C₂[I_∞ + J(η)] **if** one takes a fully formed local ζ = ζ_L + (3/5)f ζ_L² at η_h and thereafter evolves ζ linearly. But Sec. II establishes that the in-in amplitude is *end-time independent* while the growing mode itself grows as η⁻³: in the pure contraction the linear growth factor between any two times is λ ≫ 1, yet f_NL stays at −35/16 because the cubic vertices keep sourcing in step with the growth. Applying Eq. (5)'s logic inside the contraction would predict f_NL → f_NL/λ, contradicting Sec. II. So the "suppression" is the artefact of amputating the cubic vertices at η_h, and the choice η_h = η_B ("natural handoff") is not fixed by any physical criterion — indeed T varies from 0.165 to 0.409 with handoff and scheme. Consequently "universal bound" and "linear transfer can only suppress" must be replaced by an honest statement: *within a model that freezes the contraction-phase bispectrum at the NEC boundary and evolves linearly thereafter, the amplitude is rescaled by (1−ρ)/2; the bounce-phase cubic term, which is of the same order as the terms that keep f_NL constant during contraction, is not computed, so no bound on the physical post-bounce f_NL follows.* The paper already concedes the cubic term is "open, potentially dominant"; the abstract's "bounded, not resolved" and "universal suppression" are inconsistent with that concession.
*Evidence:* Sec. 0 derivation; adjudication note §1 ("the limit is end-time independent at leading order"); `A2_TRANSMISSION_BRIEF_2026-09-02.md` §3.

**M3 — PTA: two of three Savage–Dickey factors and the "6.37σ" are extrapolations beyond the sampled posterior.**
*Location:* Table II rows 2–3; abstract ("excluded at 6.37σ").
*Defect:* The 320 000-sample chain contains **zero** samples at γ ≥ 5 (max 4.705) and only 9 above 13/3. B(5) = 1.86×10⁻²⁴ is the Gaussian-KDE tail (bandwidth 0.030) evaluated 0.3 units beyond the last sample — it is a statement about the kernel, not the data; the only defensible statement is B(5) < ~1/(N·7·Δγ) ≈ 10⁻⁵ (no samples) or a Gaussian-approximation z-score labelled as such. B(13/3) rests on 9 samples: quoting 4.52×10⁻⁴ to three figures (histogram gives 6.6×10⁻⁴) and log₁₀B_MB/SMBHB = +3.85 to two decimals is unwarranted; the honest precision is ±0.2 dex. The table caption's "differences from the archived record ≤ 3×10⁻¹⁵" advertises reproducibility of a number whose statistical precision is ~50%.
*Evidence:* tail census and histogram density in Sec. 0.

**M4 — PBH: the "reversal" and the 1.73 ratio sit in a regime the paper's own diagnostic calls non-perturbative, and the non-monotonic f_PBH(f_NL) that produces the reversal is not disclosed.**
*Location:* abstract (ii); Sec. V B, Eq. (9) and the paragraph "the Gaussian-case formation channel rides a correlated ridge…"; Sec. VII A ("that ratio is robust").
*Defect:* The committed `f_NL_continuity_scan` shows f_PBH at fixed amplitude falling by ~55 decades from f_NL = 0 to −0.35 and then *rising* by ~53 decades to −35/8 (and to 2.6×10⁶ at −10). Both candidate values lie on the rising branch, where formation is dominated by the anti-correlated region ζ_G < 0, J = 1 + 1.2 f_NL ζ_G > 1 (I verified this is the J > 0 branch, not the J < 0 sign-flip branch). That branch exists only because the quadratic map is applied at excursions 1.2|f_NL|σ_r ≈ 0.7–1.5 — exactly where the paper admits "the quadratic truncation is not always perturbatively controlled", and where a cubic (g_NL) term of natural size would change the leverage at O(1). So: (a) the qualitative headline "−35/8 out-produces −35/16" is a statement about the truncated map beyond its validity, of the same class as the ceiling artefact the paper rejects in Sec. V A; (b) "the one robust output" is robust to spectrum *shape* but not to the truncation, which the text conflates; (c) the mechanism (non-monotonic f_PBH, dominance of the anti-correlated channel) must be stated explicitly so a reader understands why the ordering differs from the perturbative literature (Young–Byrnes–Sasaki 2019; Kehagias+2019: negative f_NL suppresses). The honest ratio-level statement needs the qualifier "within the quadratic local map, at excursions where that map is uncontrolled".
*Evidence:* Sec. 0 branch split and continuity scan; `PBH_COMPACTION_NOTE_2026-09-02.md` §4.1.

**M5 — Internal contradiction on whether the factor of two is settled.**
*Location:* abstract, sentence "the factor of two between −35/16 and −35/8 itself has not been settled by an independent second method"; vs Sec. II D *Scope statement* "The factor of two … is CLOSED: the from-scratch in-in computation … *is* the independent second-method route"; vs Sec. VII B "settling the factor of two by an independent derivation is a prerequisite" and Sec. VII C (ii) "settling the factor of two with … (item A3-2)".
*Defect:* Three mutually exclusive statements in one 7-page paper. The defensible position (matching the adjudication note) is: the from-scratch in-in reproduces −35/16 and identifies Cai's ×2 in all three configurations, so the *value* is confirmed within the in-in method; what remains open is a *method-independent* (gradient-expansion / Bianchi-I δN) confirmation. Pick that wording and use it in all four places.
*Evidence:* `main.tex` lines 46–48, 249–262, 605–612, 624–627 (grepped).

**M6 — r = 0.84 is adopted without derivation, source, or definition in this paper, and the lab's own ledger says it has not been re-derived at the −35/16 fiducial.**
*Location:* abstract; Sec. VI B; Table IV column 4.
*Defect:* "we adopt the noise-weighted overlap r = 0.84" — no citation, no definition of the overlap (which bispectrum shape, which survey noise weighting, which template), no uncertainty (the P2 source has ±0.02). `survey_reach_fnl.json` attributes it to an unpublished lab draft; A3 item A3-4 (repeated in Sec. VII C (iv)) says it must be re-derived at this fiducial. The r-projected column, and the abstract's 2.63σ/3.68σ, therefore rest on an unsourced number the authors themselves flag as provisional. Either derive r here (a short appendix: the bounce shape of Cai Eq. 37 vs the local template under the SPHEREx noise weighting) or drop the projected column and state the caveat in words.
*Evidence:* Sec. 0 provenance trace.

**M7 — Reference [7] is wrong; it is the load-bearing citation for the "orders of magnitude enhancement" claim.**
*Location:* Sec. III; bibliography [7].
*Defect:* arXiv:1707.06661 is a statistics paper on horseshoe estimators (Li, Craig, Bhadra). The intended work is I. Agullo, B. Bolliet, V. Sreenath, "Non-Gaussianity in loop quantum cosmology," Phys. Rev. D **97**, 066021 (2018), arXiv:1712.08148 (the A2 brief cites it correctly). Also note the paper's Ref. [2] (Cai–Easson–Brandenberger 2012) is cited for the "definite parameter-free amplitude" but is a review that quotes −35/8.
*Evidence:* live arXiv fetch of both IDs.

### MINOR

**m1 — Fig. 1 caption describes two panels ("(top) … (bottom)"); the rendered figure has one panel** (f_PBH vs A at the baseline point). Either add the ratio-vs-grid panel or fix the caption. *(p. 5, verified on the 300-DPI render.)*

**m2 — "Consistent at 1.14σ" is a Gaussian z-score on a non-Gaussian, prior-bounded marginal**; state that z is Gaussian-approximate, and give the posterior probability P(γ > 3) directly from the chain (≈ 13%).

**m3 — "ESS = 5.5×10³" with τ ≈ 58 and 32 walkers**: ESS is computed as N/max τ; state this convention. Also "ESS" per walker is ~170 — fine, but the reader should see the autocorrelation time.

**m4 — Table II caption: "differences from the archived record are ≤ 3×10⁻¹⁵"** — this is a self-reproduction of the same script on the same chain, not a reproduction of a published result; re-label ("re-derived from the committed chain; identical to the archived record") to avoid implying an external reproduction.

**m5 — Sec. V B, "leverage *grows* with |f_NL|"** — true only beyond the minimum at f_NL ≈ −0.35; from 0 to −0.35 the leverage is a 55-decade *suppression*. Add the scan (a single sentence or one row of the continuity scan) so the reader can see where the two candidate values sit. (Follows from M4 but is a separable presentation fix.)

**m6 — Sec. V B, "1.2|f_NL|σ_r ≈ 0.5–2 across the grid"**: at the baseline point the values are 0.74 and 1.48; give the grid range per candidate (0.54–1.01 at −35/16, 1.09–2.02 at −35/8 per the note) so the reader sees that −35/8 is >1 everywhere.

**m7 — Sec. V B**, "for γ_cr ≲ 0.85 our implementation instead finds enhancement relative to Gaussian where they report suppression, a genuine discrepancy left unresolved" — the table shows f_PBH(−35/16) = 3.5×10³ > 1 at γ_cr = 0.766, i.e. enhancement *at both candidate values* there; state which f_NL Choudhury et al.'s "suppression" refers to (they only computed −39.95 and −35/8) before calling it a discrepancy.

**m8 — Sec. VI A**: DESI numbers are "at 68% confidence"; the σ used for the tension (9.0) is the upper error of an asymmetric interval; say so, and note that the prediction lies on the side where the error is 9.0 (merger) / 7.4 (universality).

**m9 — Sec. II C**, "without identifying which line of their derivation introduces it": the adjudication note localises it to their Eqs. (38)–(40) effectively f_NL = (20/3)𝒜/Σk³; either cite that (as the note does) or keep the softer wording, but the two documents should agree.

**m10 — Sec. II A**: Eq. (2) is defined "exactly as in Refs. [1, 4]" while Sec. II C says Cai's amplitude step is off by 2 — a reader will ask whether the *definition* or its *evaluation* differs. One clause resolving this ("same definition, Eqs. 20–21 of [1]; the slip is in the evaluation") is needed.

**m11 — Table I**: the ζ(∂ζ)² row is 0 "at leading order (O(k²S²))" per the note; the table says 0 without qualification. Add "(leading order)" in the caption.

**m12 — Sec. III**: r in T = [1 + r(1−ρ)]/(1+2r) is complex (r = −9iA²I_∞/k³ per the A2 JSON); the text writes |r| ≫ 1 but the formula as printed with a real r is a different expression. State that r is the (complex) branch ratio and the limit is taken in |r|.

**m13 — Reproducibility statement**: the chain SHA-256 is elided ("50abc38a…10fc"); print it in full (64 hex) or give the manifest path where it is printed. Directive Q2 compliance requires the full hash.

**m14 — Ref. [4]** journal volume "JCAP **1703**, 031 (2017)" is the old JCAP style; the arXiv record gives JCAP03(2017)031 — fine, but make style uniform with [1], [11]. Ref. [9] title correct; Ref. [17] should now carry its journal reference if published.

**m15 — Style**: "isosceles" is correct here (the P2L round had "isoceles"); "Savage–Dickey factors" for point hypotheses are Bayes factors for nested models — call them that consistently ("nested factor" in Sec. IV B is used without definition).

**m16 — Abstract length** (≈ 480 words) exceeds PRD's 600-character-ish norm by a wide margin and reads as a summary; the journal will require it cut to ~250 words. Move the per-channel numerics into the Introduction.

### Falsified during review (recorded so no one re-raises them)

- **F1** "The PBH reversal is a J < 0 (sign-flip) branch artefact" — my hypothesis; **refuted** by direct branch splitting (J < 0 contributes ≤ 3×10⁻¹³ of β). The reversal is the anti-correlated J > 1 channel (M4 as stated).
- **F2** "−35/16 arithmetic or Table I rows wrong" — **refuted**; script re-run reproduces every row; two rows hand-checked.
- **F3** "Survey-reach or DESI arithmetic wrong" — **refuted**; all 14 numbers recomputed exactly and abstracts fetched live.

---

## 2. Assessment against the seven referee questions

1. **Theory:** −35/16 under the stated definition is correct and independently reproduced; the Cai ×2 is attributed fairly (all three configurations); Li+2016 consistency is stated without novelty overreach (the paper explicitly says Eq. 4 "is not a new physical effect"). The δN reconciliation is sound. The section's only defects are the internal contradiction on "settled" (M5) and small wording items (m9–m11).
2. **Transmission:** T = (1−ρ)/2 is *derived* from a stated premise, but the premise (cubic sourcing frozen at η_h) contradicts the end-time independence proven in Sec. II, so "universal bound" is an overclaim (M2). Scheme labels are honest; the uncomputed cubic term is stated.
3. **PTA:** Identifying γ = 3 with the induced-GW IR slope is correct and correctly labelled non-discriminating; "insensitive to f_NL" is right at this order (the induced spectrum depends on P_ζ, with f_NL entering only at next order). The SMBHB comparison is overstated (M1, M3) because the refit differs from the official posterior and the tail factors are extrapolated.
4. **PBH:** The ratio-level presentation and the honest reversal of the first pass are appropriate in form; the 1.73 ratio reproduces exactly and is shape-robust; but the regime is uncontrolled and the non-monotonic mechanism is undisclosed (M4, m5–m7). The non-perturbative caveat is present but placed as a footnote to a "robust" headline.
5. **Survey reach:** all numbers correct and sourced; r = 0.84 is not (M6). DESI row correct.
6. **Joint statement:** "The three channels are mutually consistent" is at best trivially true — one channel is insensitive by construction, one yields no observable, and the third cannot yet test the value; the abstract's own last sentences concede this. The paper is honest that only Channel III discriminates, so the *consistency* wording is defensible provided M1/M2 are fixed; but "rejecting the two competing spectral shapes" (Sec. VII A) must be softened to match the official NANOGrav posterior.
7. **Self-containedness / references / presentation:** one wrong reference (M7), one missing derivation (r), one figure–caption mismatch, an abstract that must be shortened.

---

## 3. Verdict

**MAJOR REVISIONS.** MAJOR: 7. MINOR: 16.

The theory content (Sec. II) is sound and reproducible, and the paper's evidential grading is unusually careful in places. It cannot be accepted as is because (i) the pulsar-timing conclusion in the abstract contradicts the published NANOGrav posterior without disclosure and rests partly on KDE extrapolation into an unsampled tail; (ii) the "universal suppression bound" contradicts the paper's own end-time-independence result; (iii) the black-hole "robust ratio" is quoted from a regime the paper itself flags as uncontrolled, with the governing non-monotonicity hidden; and (iv) the load-bearing LQC citation is wrong. All seven majors are closable with real work of hours (14-bin refit, wording, one appendix for r, reference fix), not new science.
