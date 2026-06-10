# P1B R23conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/paper1b_mcmc_companion_v1B.0.51.pdf` md5=856fbad2 pages=13
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique
---

## Pass 1 — brutal referee findings

### P1B-M1 — §IV body text contradicts fn. 3 on the negative-β injection
- **Location**: p. 6, §IV *Noise model and injections* paragraph vs. fn. 3 (same page) and source `paper1b_mcmc_companion.tex` line 1165 vs. lines 1207–1211.
- **Problem**: The body text states verbatim: "Only non-negative injections were run; a negative-β injection (sign-symmetry/linearity check) **is not part of the present MC suite and is an acknowledged validation gap**." Footnote 3 in the *same section* reports exactly that run: "The same rerun injects β = −0.27° and recovers −0.238° (bias +0.032°): recovery is sign-symmetric," with artifact `reproducibility/p1_namaster_500mc/results/c9f_negative_beta.json`. This is a stale pre-sign-symmetry-run sentence that survived the v1B.0.51 honesty wave. A referee reading linearly will conclude either the gap disclosure or the footnote is false.
- **Required fix**: Delete/rewrite the body sentence to: "A negative-β injection (β = −0.27°) was run as a dedicated sign-symmetry check (fn. 3); recovery is sign-symmetric with bias magnitude identical to the +0.27° injection." Keep the gap list honest by removing it from "acknowledged validation gap" status.

### P1B-m1 — Eq. (3) rounding: 4.97×10⁻³ rad is 0.28°, not 0.29°
- **Location**: p. 9, Eq. (3); tex line 1391.
- **Problem**: 4.97×10⁻³ rad × (180/π) = 0.2848°, which rounds to 0.28°. The displayed "≈ 0.29°" over-rounds by a full hundredth in a displayed equation. Compounding: the abstract/§I say the headline 0.27° is "taken at scan-prior midpoint values," but the m/H₀ ∈ [1,3] midpoint is 2.0 (which Eq. 3 evaluates, giving 0.28°), while the text says the 0.27° fiducial corresponds to m ≈ 1.8H₀. Three nearby numbers (0.27°, 0.28°, 0.29°) for "the midpoint prediction" invite a referee query.
- **Required fix**: Change Eq. (3) to "≈ 0.28°" and harmonize the midpoint phrasing (e.g., "near-midpoint m ≈ 1.8H₀ gives β ≈ 0.27°; the exact m = 2H₀ midpoint gives 0.28°").

### P1B-m2 — Fig. 3(b) omits the now-measured σ_β at f_sky = 0.32
- **Location**: p. 7, Fig. 3(b) + caption vs. fn. 3 (p. 6).
- **Problem**: The caption states "per-realization σ_β was not recorded in the canonical f_sky = 0.32 artifact, so that point carries the mean only" — but fn. 3 reports a dedicated f_sky = 0.32 MC rerun that measures σ_β = 0.046° directly (with |β̂|/σ_β = 5.2). The figure and the footnote tell different stories about whether the 0.32 per-realization scatter exists. The measured 0.046° bar should appear on the plot (or the caption must cite the rerun value and explain why the canonical point is plotted bare).
- **Required fix**: Add the rerun's σ_β = 0.046° error bar at f_sky = 0.32 to panel (b), or amend the caption: "a dedicated rerun (fn. 3) measures σ_β = 0.046° at this point."

### P1B-m3 — Appendix C does not list the continuous-prior (c5) configuration's priors
- **Location**: p. 12, Appendix C vs. p. 9 ("full priors and likelihood details in Appendix C") and Fig. 4 caption.
- **Problem**: §VI directs the reader to Appendix C for "full priors and likelihood details," but Appendix C only itemizes the 3 fixed-C_aγ benchmark configs (θ_i ∈ [0.5,2], m/H₀ ∈ [1,3]) and the β_free fit. The headline continuous-prior c5 configuration's priors (C_aγ ∈ [4,60], θ_i ∈ [0.01,π], log₁₀(m_a/eV) ∈ [−35,−30]) live only in the Fig. 4 caption and §VI running text. The appendix promise is unfulfilled for the most load-bearing chain (8,955 samples, the "full required coupling range" verdict).
- **Required fix**: Add a third prior block to Appendix C for the c5 chain.

### P1B-m4 — 12% under-recovery attribution ignores the C_ℓ^BB template-mismatch contribution
- **Location**: p. 6 (§IV *Simulated skies* + *Noise model and injections*), p. 7 attribution to "apodization-induced power suppression."
- **Problem**: The injected skies carry C_ℓ^BB = 0.05 C_ℓ^EE, so the rotation-induced EB signal is sin(2β)cos(2β)(C_ℓ^EE − C_ℓ^BB), while the fit template is sin(2β)cos(2β)C_ℓ^EE only. The omitted −C_ℓ^BB term by itself predicts a ~5% multiplicative under-recovery — i.e., nearly half of the measured ~12% amplitude-independent bias is plausibly template mismatch, not mask apodization. Since the validation carries the bias forward empirically as a systematic floor, the *number* is safe, but the stated physical attribution ("apodization-induced power suppression," "sky-fraction-independent property of the apodized pipeline") is incomplete — and the template mismatch being f_sky-independent actually *explains* part of the observed f_sky-independence.
- **Required fix**: Decompose or hedge the attribution: note the −C^BB template term contributes ≈5 pp of the ≈12% multiplicative bias, with the remainder from apodization-induced mode-coupling power suppression.

### P1B-m5 — Appendix B is an empty header; Table IV never cited in text
- **Location**: p. 12 ("Appendix B: Claims Classification" header, no body) and p. 13 Table IV.
- **Problem**: Appendix B contains zero sentences; Table IV floats to p. 13 with no in-text reference anywhere in the manuscript. PRD production will query an appendix with no content and an uncited table.
- **Required fix**: Add one sentence under Appendix B: "Table IV classifies every quantitative claim in this companion by type and verification status."

### P1B-N1 — fn. 3 says SNR values "equal" the √(f_sky) scaling; they differ by 0.4–0.5%
- **Location**: p. 6, fn. 3.
- **Problem**: 20.32×√(0.85/0.32) = 33.12 (artifact: 32.98); 20.32×√(0.65/0.32) = 28.96 (artifact: 28.81). "equal" should be "consistent with (within 0.5%)".
- **Required fix**: Soften the verb.

### P1B-N2 — "0.8× the standard error" sentence cherry-picks the closer sweep point
- **Location**: p. 7, *Sky-fraction sweep*.
- **Problem**: The −0.033° (f_sky = 0.85) point is 0.001° = 0.8×SE from the canonical −0.032°; the −0.034° (f_sky = 0.65) point is 0.002° ≈ 1.4× its SE (0.033°/22.4 = 0.0015°). Both remain statistically indistinguishable, but the sentence quotes only the more favorable comparison.
- **Required fix**: Quote both ("0.8× and ≈1.4× the respective standard errors").

### P1B-N3 — Loose cross-reference: "systematic floor adopted in Eq. 1–fn. 3"
- **Location**: p. 7, Fig. 3 caption.
- **Problem**: Eq. (1) reports only β̂ = 0.238°; neither Eq. (1) nor fn. 3 "adopts" 0.040° as a floor. The floor is adopted in the §IV closing paragraph and §VII.
- **Required fix**: Point the caption at the §IV text ("carried forward as the NaMaster systematic floor; Sec. IV").

### P1B-N4 — "widened from the earlier [1,30]" is half-true
- **Location**: p. 10, Fig. 4 caption.
- **Problem**: C_aγ ∈ [4,60] is widened above (30→60) but *narrowed* below (1→4). "Widened" alone misdescribes the lower edge; the 22%-below-C_aγ=9 mass statement depends on that lower cut.
- **Required fix**: "shifted and extended to [4,60] to cover the full EOM-required band" + one clause justifying dropping [1,4).

## All-clear statements (checked areas with no finding)

- **w_pivot Table-II row + fn. b algebra**: VERIFIED end-to-end. ρ = −0.00729/(0.0436×0.1864) = −0.897 ≈ −0.90 ✓; 1−a_p = 0.00729/0.1864² = 0.210 ✓; z_p = 1/0.790 − 1 = 0.266 ≈ 0.27 ✓; σ²: 0.0436² − (0.00729/0.1864)² = (0.0193)² ✓ (source tex correctly squares the Cov term); mean −0.8122 + 0.210×(−0.6666) = −0.952 ✓; (1−0.952)/0.019 = 2.53 → +2.5σ ✓. Consistent with the chain-verified DESI DR2 correction.
- **Sample-count stratification**: CONSISTENT everywhere. 176,240 + 132,949 = 309,189 ✓ (abstract, p.3, fn.1, §VII); 0.7-burnin = 123,368 + 93,064 = 216,432 ✓; 123,129 within 0.2% of exact ✓; 119,617 getdist-thinned subset consistent Fig. 1 vs fn. 1 ✓; Planck-only 114,992 @ R̂−1≈0.05 consistent p.3/§VII and correctly excluded from the 309,189 headline ✓; ALP 9,720 = 3×3,240 ✓ (p.9, App. C, p.12); continuous-prior 8,955 consistent (p.10, App. C) ✓.
- **NaMaster figure-vs-text**: Fig. 3(a) annotations (+0.000°, −0.032°, −0.040°) match Eq. (1) and text ✓; multiplicative 0.238/0.27 = 0.302/0.342 = 0.88 ✓; absolute-bias growth 0.032→0.040 = 25% ✓; sweep ratios 8.1/7.2/5.2 ✓; √f_sky scatter scaling 0.029×1.63 = 0.047 ✓; √500 = 22.4 ✓; sign-symmetry numbers internally exact (−0.238°, bias +0.032°) ✓.
- **Commander / EB-spectrum claims**: NONE in the PDF. §IV scope note, abstract, p.12 ("enters at the level of the published β posterior, not as a direct re-analysis of the EB spectra") all correctly labeled synthetic-ΛCDM / summary-likelihood. Source-tex grep confirms "Commander" appears only in a comment asserting its absence. Site `figures.ts`/data not re-audited here (PDF scope).
- **ALP likelihood unification**: Eskilt–Komatsu Gaussian summary (β_obs = 0.342° ± 0.094°) used identically in §VI, Fig. 4 caption, Appendix C, p.12 ✓; ACT DR6 0.215° ± 0.074° correctly quarantined to the auxiliary inverse-variance cross-check ✓; Eq. (4): IV-mean 0.2415 ± 0.0614 → 0.241° ± 0.061°, 3.95σ ≈ 3.9σ ✓, correctly demoted below the published 3.6σ joint analysis.
- **ALP arithmetic chain**: α_EM/(4π) = 5.81×10⁻⁴ ✓; C_aγΔφ/f_a = 5.97×10⁻³/5.81×10⁻⁴ = 10.3 ✓; 10.3/8 = 1.29, 17% above 1.1 ✓; band [10.3/1.1, 10.3/0.2] = [9.4, 51.5] ≈ [9, 51] ✓; naive envelope 4×5.8e−4×0.2 rad = 0.027°, 12×5.8e−4×1.1 rad = 0.44° ✓; 25× tuning = (0.5/0.1)² ✓; spectator-subset 0.5σ: 0.062/√(0.094²+0.10²) = 0.45 ✓; Fig. 4 mass conversion H₀ = 1.44×10⁻³³ eV, m/H₀ ∈ [7×10⁻³, 7×10²] ✓.
- **BAO attribution**: Table III `bao.sixdf_2011_bao + bao.sdss_dr7_mgs + bao.sdss_dr16_baoplus_{lrg,qso,lyauto,lyxqso}` matches the §V.A prose (SDSS DR16 + DR7 MGS + 6dFGS) ✓; DESI DR2 BAO correctly confined to the iter2 w₀wₐ chain ✓.
- **Tension cross-checks**: w₀ +4.3σ (0.1878/0.0436), wₐ −3.6σ ✓; σ(w₀+wₐ) = √(0.0019+0.0347−0.0146) = 0.1486 ✓ Table II's 0.1485; S₈ vs DES-Y3 0.049/0.019 = 2.5σ ✓; M_B–H₀ offset −28.571/−28.415 → 0.156 mag = 3.2σ ✓; Liu et al. 0.5σ/1.0σ ✓; χ²_BAO/13 ≈ 0.8 ✓; χ² sum footnote correct at 0.1-unit ✓.

## Pass 2 — what-did-I-miss self-critique
1. **Initially misread the χ² footnote as claiming a "1.0-unit" rounding artifact** (sum 14037.5 vs total 14037.4 is 0.1). Source check confirms the tex says "0.1-unit" — render ambiguity, NOT a finding. Withdrawn.
2. **Initially suspected fn. b printed Cov(w₀,wₐ)/σ²_wₐ without the square**. Source tex line 917 has `\mathrm{Cov}^2(w_0,w_a)/\sigma_{w_a}^2` — correct. Withdrawn.
3. Re-verified Eq. (3): 4.97×10⁻³ × 57.2958 = 0.2848 — m1 stands.
4. Re-checked the M1 contradiction against source (tex 1165 vs 1207–1211) — both sentences present in the compiled v1B.0.51; M1 stands.
5. Figure-text match re-scan: Fig. 2 caption sample counts (176,240/132,949), Fig. 1 (119,617), Fig. 4 prior box and β_ALP = 0.336°±0.107° all match text — no additional findings.

## Summary recommendation
**Minor revision.** Zero errors of substance (E): the headline numbers, the w_pivot algebra, the sample-count ledger, and the honesty relabeling all survive brutal scrutiny. One internal-consistency Major (**M1**: the stale "negative-β injection is an acknowledged validation gap" sentence directly contradicted by the new sign-symmetry rerun in the same section — a one-sentence fix, but a referee-visible self-contradiction), five minors (m1–m5: Eq. 3 rounding, Fig. 3(b)/fn. 3 σ_β mismatch, missing c5 priors in App. C, incomplete 12%-bias attribution, empty Appendix B), four nits (N1–N4). All are textual/presentational; none threaten the scientific claims. Fix M1 + m1–m5 and this companion is publication-clean.

**Counts**: E:0 · M:1 · m:5 · N:4
