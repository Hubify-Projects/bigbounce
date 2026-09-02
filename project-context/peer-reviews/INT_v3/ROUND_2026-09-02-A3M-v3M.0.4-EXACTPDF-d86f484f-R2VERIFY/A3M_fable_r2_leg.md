# A3M v3M.0.4 — INT referee leg R2 (verification pass, Claude Fable)

- **Reviewer:** Claude Fable (INT leg, independent PRD-standard referee; not told any expected verdict)
- **Model:** claude-fable (claude-fable-5-1)
- **Manuscript:** `research/track_a3_multichannel/paper/main.pdf` — v3M.0.4, 8 pages, dated September 2, 2026 (page 1 render confirms version stamp and date)
- **sha256 (computed this session, binding):** `d86f484f5d4f83fb7b4a339cced6a9c4bf9482f5f5bc206a55bdbfe2270e277c`
- **Round:** `ROUND_2026-09-02-A3M-v3M.0.4-EXACTPDF-d86f484f-R2VERIFY`
- **Date:** 2026-09-02
- **Method:** all 8 pages rendered at 300 DPI (`pdftoppm -r 300`) and read; `main.tex` grepped line-by-line for every closure; `pta_gamma_reproduce.py` re-run (0.6 s; only diff vs committed JSON was `wall_seconds`, restored by `git checkout`); chain census and z-scores recomputed directly from `chain_real_freespec.npy`; continuity scan and ratio summary read from `outputs/pbh_compaction_fnl.json`; DESI/SPHEREx arithmetic recomputed; arXiv 2306.16213 and 1712.08148 fetched live. `main.log`: 0 undefined refs, 1 overfull hbox (≤ 2.7 pt, cosmetic).

---

## 0. Independent recomputation (this session)

| Object | My computation | Paper | Status |
|---|---|---|---|
| Chain shape | (320 000, 2) | 3.2×10⁵ samples | ✓ |
| γ marginal | mean 2.56647, std 0.38183, median 2.59129, [q16,q84] = [2.3041, 2.8822] | 2.567 ± 0.382, median 2.591, [2.304, 2.882] | ✓ |
| Tail census | N(γ≥5) = **0**, chain max **4.7048**; N(γ≥13/3) = **9**; N(γ>3) = 28 719 → P(γ>3) = **8.97 %** | 0 of 320,000; max 4.70; 9 samples; 8.97 % | ✓ |
| Official posterior σ | 0.6/1.645 = 0.3647 | ≈ 0.365 | ✓ |
| z vs official | γ=3: **0.548**; 13/3: **3.107**; γ=5: **4.935** | 0.55σ; 3.1σ; 4.94σ (table 4.9σ) | ✓ |
| Refit vs official | (2.567−3.2)/√(0.365²+0.382²) = **−1.199** | 1.20σ | ✓ (quadrature-combined — see m-R2-4) |
| z vs refit | 1.135, 4.627, 6.373 | 1.14, 4.63, 6.37 | ✓ |
| Savage–Dickey | B(3) = 3.2276; B(13/3) = 4.52×10⁻⁴; B_MB/SMBHB = 7137.6, log₁₀ = 3.8536 | 3.23; 4.5×10⁻⁴; 7.1×10³; +3.85 | ✓ |
| Injection validation | `results.json` synthetic recovers 3.1925 ± 0.4233 | 3.19 ± 0.42 | ✓ |
| PBH ratio | JSON summary: n=27, mean 1.73202, min 1.60975, max 1.80862, std 0.05016 | 1.732 [1.610, 1.809], std 0.050 | ✓ |
| Continuity scan | f_PBH(A*): 1 → 2.4×10⁻² (−0.02) → 7.50×10⁻⁵⁵ (−0.35) → 3.62×10⁻¹⁴ (−35/16) → 1.57×10⁻² (−35/8) → 89 (−6) → 2.6×10⁶ (−10): ~55-decade fall, ~53-decade rise | "~55-decade minimum near −0.35 … climbs ~53 decades" | ✓ |
| DESI | (−2.1875+3.6)/9.0 = 0.157; (3.5+2.1875)/7.4 = 0.769; 2.1875/9.0 = 0.243 | 0.16σ; 0.77σ; 0.24 | ✓ |
| Reach (bare) | 2.1875/{0.7, 0.5, 1} = 3.125, 4.375, 2.19; at −35/8: 6.25, 8.75, 4.375 | 3.13, 4.38, 2.19; 6.25, 8.75, 4.38 | ✓ |
| Ref. [7] | arXiv:1712.08148 = Agullo, Bolliet, Sreenath, PRD 97, 066021 (2018) (live fetch) | identical | ✓ |
| NANOGrav interval | arXiv:2306.16213 abstract uses median + 90 % credible intervals; γ_HD = 3.2 ± 0.6 on 14 bins per R1 audit's source-PDF check | "posterior median and 5–95 % interval" | ✓ |
| Fig. 1 | `pbh_compaction_fnl.png` 1110×780, single axes; caption now single-panel | — | ✓ |

No number in the manuscript failed recomputation. No fabricated derivation found.

---

## A. Verification of the 20 R1 canonical items (DISPOSITIONS/A3M.md)

Legend: **CLOSED** = edit present and correct on the exact v3M.0.4 PDF; **PARTIAL** = edit present but incomplete/inconsistent; **NOT CLOSED** = no edit.

### MAJOR (8)

| Item | Verdict | Evidence (tex line / PDF page) |
|---|---|---|
| DA3M-01 official posterior primary | **CLOSED** | §IV B L343–353 (p. 4): official 14-bin γ_HD = 3.2⁺⁰·⁶₋₀.₆ stated as median + 5–95 %, σ≈0.365; 0.55σ / 3.1σ / 4.94σ; NANOGrav "moderate tension … 99 % credible boundary" quoted. Refit labelled "secondary, differently-conditioned" (L355), offset 1.20σ (L370). Table II gains z_off column (L395–399). Abstract L61–66 leads with official numbers. Injection-validation subsection §IV C (L413–419). Decision D1 implemented. |
| DA3M-02 KDE tail extrapolation | **PARTIAL** (residual is a self-inconsistency, see m-R2-1) | B(γ=5)/"6.37σ" removed from abstract (L67–68 now "zero of 320,000 chain samples reach γ≥5"); Table II row 3 B = "n/a" with caption explanation (L388–391); text L375–380 explains bandwidth sensitivity. BUT L379–380 says the 13/3 factor "is quoted to one significant figure" while Table II prints **4.5×10⁻⁴** (two s.f.) and L409–410 still prints log₁₀B = **+3.85** to two decimals and 7.1×10³. |
| DA3M-03 "universal" T bound / (A4) | **CLOSED** | `grep -c universal main.tex` = 1, at L302 in the negation "not a universal property". (A4) stated verbatim L277–282; end-time-independence reconciliation L271–274; "under assumption (A4), 0<T≤1/2" L292; abstract L50–56 "within a handoff scheme … no bound on the physical post-bounce f_NL follows"; §VII A L678–681 matches. Handoff-conditional wording is complete and correct. |
| DA3M-04 PBH non-monotonicity / "robust" scope | **CLOSED** | "Regime of validity" L528–535 (anti-correlated γ_cr>0, J>1 branch; per-candidate excursions); "Non-monotonicity" L535–544 (55-decade minimum at ≈−0.35, both candidates on rising ζ_G<0 branch); "robust" now scoped "robust to spectrum shape … a result within a stated regime, not a claim of general validity" L525–528; abstract L73–79 carries the disclosure; §VII B L695–697. Decision D3 implemented; ratio kept as result. |
| DA3M-05 factor-of-two contradiction | **CLOSED** | `grep -c CLOSED main.tex` = 0. One wording in all four places: abstract L46–49; scope statement L250–263 ("within the in-in method … method-independent … remains open"); §VII A L668–671; §VII B L702–704; §VII C (ii) L715–717. |
| DA3M-06 r = 0.84 unsourced | **CLOSED** (option b) | §VI B L629–637: r sourced to the companion Fisher draft, explicitly "rather than re-derived at the −35/16 fiducial"; r-projected column dropped from Table IV (L648–654 bare only; caption L644–646); abstract L84–86 quotes only bare 3.13σ with the pending-projection caveat. |
| DA3M-07 Ref. [7] | **CLOSED** | bib `\bibitem{AgulloBolliet2017}`: PRD **97**, 066021 (2018), arXiv:**1712.08148** — verified live. Other IDs spot-checked (0903.0631, 1612.02036, 2306.16213, 2409.18983, 2411.17623, 2311.13082) consistent with R1 fetches. |
| DA3M-08 internal tags / repo URLs | **CLOSED** | `grep -n "A3-[0-9]\|superseded\|prior version\|CLOSED" main.tex` → 0 hits in body. Markdown-note path remains only as a reproducibility pointer (L603–605), which is Data-Availability-appropriate. Repo URLs consolidated in the Reproducibility statement (L733–737). AI-usage disclosure retained (L768) — acceptable; venue may move it to the cover letter. |

**MAJOR closure count: 7 CLOSED, 1 PARTIAL (DA3M-02), 0 NOT CLOSED.**

### MINOR (15; DA3M-m01…m15)

| Item | Verdict | Evidence |
|---|---|---|
| m01 Fig. 1 caption two panels | CLOSED | caption L581–589 single panel; PNG single axes |
| m02 1.14σ Gaussian z | CLOSED | L404–406 "Gaussian approximations … P(γ>3)=8.97 %" |
| m03 ESS convention | CLOSED | L360–362 τ=(58.1,58.0), ESS=N/max(τ) |
| m04 "≤3×10⁻¹⁵ from archived record" self-reproduction wording | **NOT CLOSED** | Table II caption L387–388 unchanged |
| m05 "leverage grows" | CLOSED (folded into 04) | L535–544 |
| m06 per-candidate perturbativity ranges | CLOSED | L531–532 (0.54–1.01 / 1.09–2.02) |
| m07 A* normalization | CLOSED | L546, caption L584 A* = 0.131446 |
| m08 DESI prior non-comparability, asymmetric errors | CLOSED | L616–622 |
| m09 §II C vs adjudication note on localising Cai's ×2 | **NOT CLOSED** | L225–227 "without identifying the exact algebraic line"; note localises to Eqs. (38)–(40). Softer wording retained; documents still disagree. |
| m10 same definition / different evaluation | CLOSED | L155–157 |
| m11 Table I ζ(∂ζ)² row "0" leading-order qualifier | **NOT CLOSED** | L207, caption L197–199 unqualified |
| m12 complex r, |r|≫1 | **NOT CLOSED** | L283–288 formula written for real r; "|r|" used but r's complex nature not stated |
| m13 Li 2016→2017 | CLOSED | L41–42 |
| m14 full chain SHA-256 | CLOSED | L758–760, two halves, 64 hex |
| m15 "nested factor" undefined | **NOT CLOSED** | L410–411 "the nested factor is prior-sensitive" still without definition (Savage–Dickey ratio is defined L373–374 but the word "nested" is not tied to it) |

**MINOR closure count: 10 CLOSED, 5 NOT CLOSED** (m04, m09, m11, m12, m15 — none listed in the SSOT item→edit table, so these are omissions, not mis-closures).

### Re-flags / falsified / genre (not re-raised)
DA3M-R1…R5 remain correctly disclosed (R5: L551–555 now names the −35/8 fiducial ✓). F1–F8 stand. G1–G3: abstract still ≈ 500 words (G2); bibliography style still mixed (G1); "operative uncertainty is internal" L699–700 still undefined (G3).

**Reference metadata:** Ref. [7] correct; Li et al. year consistent (2017) between abstract and bibliography; remaining bibliography items unchanged from R1 and previously verified.

**R1 closure summary: 17 of 20 canonical items CLOSED as specified (7 MAJOR + 10 MINOR); 1 MAJOR PARTIAL; 5 MINOR unaddressed. Decisions D1, D2, D3 are implemented faithfully; no closure introduced a new factual error.**

---

## B. Fresh referee read — new findings on v3M.0.4

Classification per directive R2: **SUBSTANTIVE** vs **GENRE/LENGTH/VENUE**.

### MAJOR
None.

### MINOR

**m-R2-1 — Internal precision inconsistency on the 13/3 Savage–Dickey factor.** *Location:* §IV B L379–380 vs Table II L398 and L409–410 (p. 4). *Defect:* text says the 13/3 factor "is quoted to one significant figure for the same reason" (9 tail samples), but Table II prints 4.5×10⁻⁴ (two s.f.) and the text prints B_MB/SMBHB = 7.1×10³, log₁₀B = +3.85 (two decimals). *Evidence:* my KDE gives 4.52×10⁻⁴ / 3.8536, but with 9 samples the statistical precision is ~±0.2 dex (R1 M3, undisputed). *Fix:* print 5×10⁻⁴, ~7×10³, log₁₀B ≈ 3.9 (or "+3.9 ± 0.2"). Residual of DA3M-02. **SUBSTANTIVE** (precision claim inconsistent with its own stated rule).

**m-R2-2 — Garbled sentence in Next steps (ii).** *Location:* L715–718 (p. 7): "…derivation of Eq. (1), settling the factor of two with the contraction phase's own cubic term settling the factor of two;". *Defect:* duplicated clause; "with the contraction phase's own cubic term" is a leftover from the R1 rewrite and is not meaningful (item (v) separately covers the bounce's cubic term). *Fix:* "…derivation of Eq. (1), giving the method-independent confirmation of the factor of two;". **SUBSTANTIVE** (unreadable sentence in a results-bearing section; introduced by the R1 closure).

**m-R2-3 — "(deviation D1 above)" refers to a label never defined in the paper.** *Location:* L516 (p. 5). *Defect:* the D1–D5 deviation list exists only in `PBH_COMPACTION_NOTE_2026-09-02.md`; the paper first mentions "deviations (D1–D5)" at L603, *after* L516, and never says what D1 is. A reader cannot resolve the pointer. *Fix:* "(the unreconstructible source spectrum, Sec. V B)" or define D1 in-text. **SUBSTANTIVE** (dangling internal reference; directive-Q1 class internal-note leakage).

**m-R2-4 — Mislabelled range "the refit's 3.1–4.6σ".** *Location:* §IV D L427 (p. 4). *Defect:* 3.1σ is the official-posterior tension, 4.63σ the refit's; the range spans the two conditionings, not "the refit's". Also L370 "sits 1.20σ from the official posterior" should say the σ is the quadrature-combined 0.53. **SUBSTANTIVE** but trivial (one clause each).

**m-R2-5 — Logically inverted "bare … once a shape-overlap projection is derived".** *Location:* §VII A L683–684 (p. 7): "SPHEREx reaches 3.13–4.38σ bare once a shape-overlap projection is derived". *Defect:* the bare significance does not depend on the projection; the projected value does. *Fix:* "3.13–4.38σ bare (the shape-overlap-projected reach awaits re-derivation at this fiducial)". **SUBSTANTIVE** but trivial.

**m-R2-6 — Five R1 minors left open** (m04, m09, m11, m12, m15 above). Each is a one-clause edit. **SUBSTANTIVE** (m11, m12 are correctness qualifiers), the rest presentation.

**m-R2-7 — Abstract length ≈ 500 words; PRD will require ≈ 250.** GENRE/LENGTH (= DA3M-G2). Deferred by design until content stabilised; it is now stable.

**m-R2-8 — Bibliography style mixed (JCAP 1703 vs JCAP 07 (2019)); AI-usage section placement.** GENRE/VENUE (= DA3M-G1 / DA3M-08 residual).

**m-R2-9 — Tex header comment (L2–3) still reads "SKELETON … stubs pending".** Not in the PDF; source hygiene only. GENRE.

### Falsified during this read (recorded)
- "official interval might be 68 %": abstract of 2306.16213 uses 90 % credible intervals throughout; paper's 5–95 % reading stands.
- "P(γ>3) = 8.97 % contradicts 1.14σ": one-sided Gaussian tail at z = 1.135 is 12.8 %; the 8.97 % from the chain is the honest number and the paper labels the z as approximate. Consistent.
- "continuity-scan decades wrong": log₁₀(7.5×10⁻⁵⁵) = −54.1 (fall ≈ 54–55 dex); rise to 1.6×10⁻² ≈ 52.3 dex. "~55" and "~53" are fair.

---

## C. Assessment

The three R1 decisions are implemented as written and correctly. The PTA channel now leads with NANOGrav's official posterior and every tension I recomputed matches (0.55σ, 3.1σ, 4.94σ; 0 of 320 000 at γ≥5; 9 at γ≥13/3). The transmission bound is stated as (A4)-conditional throughout, with "universal" gone. The PBH ratio carries its regime and the 55-decade non-monotonicity. Reference [7] is fixed. What remains is a short list of self-consistency and copy defects — one precision inconsistency the paper's own rule flags, one garbled sentence, one dangling label, two mislabelled clauses, and five R1 minors that were not carried into the edit — plus the genre items (abstract length, bibliography style). None affects a number, a claim, or a conclusion.

## Verdict

**MINOR REVISIONS.** MAJOR: 0. MINOR: 9 (6 substantive, 3 genre/length/venue).

**Substantive findings remaining: 6** (m-R2-1, m-R2-2, m-R2-3, m-R2-4, m-R2-5, m-R2-6[= R1 m04/m09/m11/m12/m15]). All are single-sentence edits requiring no new computation; after them, only GENRE/LENGTH/VENUE items (abstract length, bibliography style, AI-disclosure placement) remain, which per directive R2 is the stop condition for review rounds.
