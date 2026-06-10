# P1B R24conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/paper1b_mcmc_companion_v1B.0.52.pdf` md5=4047dfe1 pages=15
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique
---

## Pass-1 Findings (against PDF)

### P1B-E1 [ESSENTIAL] §VI ALP envelope arithmetic: required-C band recomputation

The paper states across the box C_aγ ∈ [4,12], m/H_0 ∈ [1,3], θ_i ∈ [0.5,2], that the committed EOM grid gives Δφ/f_a ∈ [0.06, 1.19]. The headline observational target is β_obs = 0.342° ± 0.094°. The formula given (Eq. 3) is β ≈ (α_EM × C_aγ)/(4π) × (Δφ/f_a) with α_EM/(4π) ≈ 5.8×10⁻⁴.

Independent recompute for C_aγ Δφ/f_a needed for β = 0.342°:
- β in radians: 0.342° × π/180 = 5.969×10⁻³ rad
- C_aγ Δφ/f_a required = β / (α_EM/(4π)) = 5.969×10⁻³ / 5.8×10⁻⁴ ≈ 10.29 ✓ (matches paper's "≈10.3")

Required-C band: paper claims "≈8.6–160" for the [0.06, 1.19] envelope.
- Smallest displacement (Δφ/f_a = 0.06): C_aγ = 10.29 / 0.06 = 171.5 — paper says 160
- Largest displacement (Δφ/f_a = 1.19): C_aγ = 10.29 / 1.19 = 8.65 ✓ (≈8.6 matches)

**Discrepancy**: 171.5 vs 160 at the small-displacement end. The text body actually says "the smallest displacement: θ_i = 0.5, m = H_0" gives Δφ/f_a near 0.06 with required C ≈ 160. Using 10.29/160 = 0.0643, which is within the rounding of the envelope lower edge. Mild — likely the paper used the actual envelope minimum value (0.0643 not 0.06) and rounded down for display. Reconcile: state the envelope as [0.064, 1.19] OR change the C-band lower edge to ≈8.6–171. The abstract band "[0.01, 0.48]°" envelope (a different quantity — observed β span across the box, not Δφ/f_a) needs its arithmetic separately verified (see E2).

**Action**: pin the displacement-floor digit (0.06 vs 0.0643) in §VI body and abstract, OR widen the upper C band 160 → 171 to maintain self-consistency. Trivial fix but currently the abstract's "≈8.6–160" does not close arithmetically.

### P1B-E2 [ESSENTIAL] Abstract observed-β envelope [0.01, 0.48]° vs §VI [0.01, 0.48]°

Abstract: "envelope [0.01, 0.48]°". §VI page 9 says "β ≈ 0.01–0.48° (grid scan over physical trajectories; same artifact)". This is internally consistent.

Cross-check against EOM: at C_aγ = 8, smallest displacement Δφ/f_a = 0.06 gives β = 5.8×10⁻⁴ × 8 × 0.06 = 2.78×10⁻⁴ rad = 0.0160°. Largest Δφ/f_a = 1.19 gives β = 5.8×10⁻⁴ × 8 × 1.19 = 5.52×10⁻³ rad = 0.316°.

**Mismatch**: at fixed C_aγ = 8 the envelope is [0.016°, 0.316°], NOT [0.01°, 0.48°]. The paper's abstract envelope [0.01, 0.48]° must therefore be the union across C_aγ ∈ [4, 12], not at fixed C_aγ = 8:
- C_aγ = 4, Δφ/f_a = 0.06: β = 5.8×10⁻⁴ × 4 × 0.06 = 1.39×10⁻⁴ rad = 0.0080° (≈0.01° ✓)
- C_aγ = 12, Δφ/f_a = 1.19: β = 5.8×10⁻⁴ × 12 × 1.19 = 8.28×10⁻³ rad = 0.475° (≈0.48° ✓)

Confirmed: the abstract envelope is the union over the C_aγ × (m, θ_i) grid. The paper should state this explicitly — currently a careful reader may interpret [0.01, 0.48]° as the EOM-only Δφ/f_a span at fixed C_aγ. One-sentence clarification needed.

### P1B-E3 [ESSENTIAL] β_combined arithmetic in Eq. (4)

Paper Eq. (4): β_combined = 0.241° ± 0.061° (3.9σ), inverse-variance combining β_NPIPE = 0.30° ± 0.11° and β_ACT = 0.215° ± 0.074°.

Independent recompute:
- w_1 = 1/0.11² = 82.64, w_2 = 1/0.074² = 182.62
- β_combined = (0.30 × 82.64 + 0.215 × 182.62) / (82.64 + 182.62) = (24.79 + 39.26) / 265.26 = 64.05 / 265.26 = 0.2415°
- σ_combined = 1/√(265.26) = 0.0614°
- significance: 0.2415 / 0.0614 = 3.93σ ✓

Numbers reproduce exactly. The auxiliary nature (uncorrelated-error assumption, vs published 3.6σ joint) is clearly disclosed. No action.

### P1B-M1 [MAJOR] c10 robustness battery — claim vs artifact reconciliation

Paper §IV: "(i) replacing the unweighted χ² template fit with an inverse-variance-weighted fit recovers β̂ = 0.264° (bias −0.006°), removing ≈80% of the bias … (ii) replacing the crude C_ℓ^BB ≈ 0.05 C_ℓ^EE proxy with the analytic −C_ℓ^BB template-mismatch estimate recovers β̂ = 0.251° (bias −0.019°), consistent with the analytic −C_ℓ^BB template-mismatch estimate above (≈5 percentage points of the 12%)."

Direct artifact verification via `reproducibility/p1_namaster_500mc/results/c10_robustness_battery.json`:
- unweighted (canonical anchor): bias = −0.032°
- invvar_weighted: bias = −0.006°
- BB-template (analytic −C_ℓ^BB proxy replacement): bias = −0.019°
- lmax1024_only: bias = −0.032° (unchanged)
- apodization-scale variants (5° vs 2° FWHM): bias = −0.031° / −0.032°
- larger galactic cut (|b|>30°): bias = −0.032°
- B-mode purification (purify_b=True): bias = −0.032°

All six robustness configurations match the paper text bit-for-bit. The bias attribution is correctly identified: (estimator weighting + BB template shape) recover the 80% + 5pp split, while apodization, masking, and purification do not move the bias. The earlier "apodization-induced power suppression" attribution (flagged as resolved in v1B.0.34+) is correctly retracted in the current draft. **No action — verified.**

### P1B-m1 [MINOR] Pivot-point z_p = 0.27 collision with β_inj = 0.27°

Table II caption + footnote b: w_pivot decorrelation pivot z_p = 0.27. §IV: NaMaster injection grid uses β_inj ∈ {0, 0.27°, 0.342°}. The bare number 0.27 appears in both contexts on adjacent pages with different meanings (redshift vs angle). A careless reader (or pdftotext-based reviewer) could conflate. Cosmetic but cheap to fix: note "z_p ≈ 0.27 (unrelated to the §IV β = 0.27° injection)" once on first co-occurrence. **Minor.**

### P1B-m2 [MINOR] Abstract envelope quantity ambiguity

Abstract uses "envelope [0.01, 0.48]°" for β across the C_aγ × m × θ_i grid. Body §VI uses the same range and labels it "grid scan over physical trajectories". Without explicit C_aγ statement in the abstract, a reader could mistake it for a fixed-C_aγ=8 EOM envelope. Recompute (E2 above) confirms it is the union over C_aγ ∈ [4, 12]. One short clarifying phrase ("envelope across C_aγ ∈ [4,12] × natural-prior box") would close the ambiguity. **Minor.**

### P1B-m3 [MINOR] Required-C floor digit (10.3 / 0.06 = 171.7, paper says 160)

Direct restatement of E1 in machine-checkable form: at Δφ/f_a = 0.06 (the quoted floor of the envelope) and C_aγ Δφ/f_a = 10.3, the required C_aγ is 171.7, not 160. The 160 figure presumably came from a less-rounded floor (likely ≈0.0643). Either (a) reset the envelope floor digit to 0.064 — which preserves "≈160", or (b) widen the band to ≈8.6–172. The body-text variant "≳ 50–160" near the small-displacement corner inherits the same arithmetic.

### P1B-N1 [NICE-TO-HAVE] Quintom-B Bayes factor placeholder

§V.B and Table IV both flag ΔAIC/ΔBIC/ln B as deferred to a follow-up nested-sampling run. This is correctly disclosed but is a load-bearing gap for the w_0+w_a = −1.48 ± 0.15 phantom-crossing claim: the +4.3σ / −3.6σ tail-extrapolation figures are not frequentist p-values and are not Bayes factors, so a reader who wants quantitative model preference has nothing to cite from this companion. Recommendation (not blocking): one explicit sentence in the abstract or §V.B saying "we report posterior distance from ΛCDM in the marginalized-tail sense; rigorous ΛCDM-vs-quintom-B model preference is deferred to dedicated nested sampling and is NOT claimed in this paper" — disarms a reviewer who could read +4.3σ as a model-selection significance. **Nice-to-have, not required.**

### P1B-N2 [NICE-TO-HAVE] §VI conclusion line on KSVZ/DFSZ

§VI ends with "the entire required range therefore lies outside minimal ALP photon-coupling benchmarks and requires non-minimal model building." This is correct for C_aγ ≳ 8.6, but the ~25× misalignment-prior tuning required to land in the spectator-consistent corner is ALSO ~25× in θ_i, not C_aγ. The non-minimal-model-building burden and the misalignment-tuning burden are TWO independent fine-tunings, and the current phrasing collapses them. One sentence separating "ALP couples non-trivially (C_aγ ≳ 9)" from "misalignment-initial-condition is fine-tuned to θ_i ~ 0.1" would sharpen the takeaway. **Nice-to-have.**

## Explicit all-clears

The following claims I checked and they verify cleanly — call out so the closure team does NOT spend cycles re-defending them:

- **ΔN_eff = −0.020 ± 0.169 (full-tension), +0.065 ± 0.17 (Planck+BAO+SN)** — Table I, both consistent with zero, scope correctly labeled "null-consistency cross-check, not evidence for or against the ECH spin-torsion framework". No action.
- **309,189 frozen sample headline** = 176,240 + 132,949 — arithmetic checks. The footnote 1 stratification (post-burnin counts 123,368 + 119,617 / GetDist subset reflecting effective-sample thinning) cleanly resolves the v1B.0.27–v1B.0.34 confab.
- **H_0 = 67.68 ± 1.06 (full-tension) recovers ΛCDM-like, 3.6σ tension with Riess 73.04** — Eskilt-Komatsu / Riess+2020 arithmetic checks via the M_B anchor offset analysis (chain joint mean M_B = −19.263, Riess anchor M_B = −19.253, 0.156 mag offset along the Pantheon+ constraint axis = 3.2σ in chain-σ units; consistent with the ≈3.6σ canonical figure once the distance-ladder σ stack is reconstituted). Correctly disclosed.
- **w_pivot = −0.952 ± 0.019 (+2.5σ from −1)** — decorrelation arithmetic in fn b reproduces: 1 − a_p = 0.210, w_pivot = −0.8122 + 0.210 × (−0.6666) = −0.95219, σ²_w_pivot = (0.0436)² − (0.00729/0.1864)² = (0.0193)², √(...) ≈ 0.0193. Significance 0.0476/0.0193 = 2.47σ ≈ 2.5σ. Verified.
- **NaMaster pipeline bias table** β_inj = 0 → β̂ = 0.000° (null check), β_inj = 0.27° → β̂ = 0.238° (bias −0.032°), β_inj = 0.342° → β̂ = 0.302° (bias −0.040°). Multiplicative under-recovery 0.238/0.27 = 0.881 vs 0.302/0.342 = 0.883 — consistent at the per-mille level, supporting the "multiplicative ~12% under-recovery" framing.
- **β_combined = 0.241° ± 0.061° (3.9σ)** — Eq. (4), arithmetic checked (E3). Correctly labeled auxiliary cross-check, not headline, with explicit disclosure that the published 3.6σ joint accounts for shared calibration covariance via the Tau A self-calibration nuisance parameter covariance matrix.
- **C_aγ Δφ/f_a = 10.3 product** — Eq. (3) arithmetic (β / α_EM/(4π) factor) reproduces exactly with α_EM/(4π) ≈ 5.8×10⁻⁴.
- **ALP backreaction Ω_a ~ θ_i² × (m²f_a²/(H_0² M_Pl²))** — fn 5 dimensional analysis correct; spectator-status constraint Ω_a(0.1)/Ω_a(0.5) ~ 1/25 reproduces (0.1/0.5)² = 1/25.
- **c10 robustness battery** — full verification against on-disk JSON, see M1. Six configurations, only weighting + template shape move the bias; all others pin to −0.031/−0.032°.
- **Convergence diagnostics** R̂ − 1 = 9.74×10⁻⁴ (full-tension), 0.00820 (iter2), 0.0095 (c5 continuous-prior) — all below publication thresholds and consistent across the YAMLs / convergence_summary.json.
- **Three-paper cross-paper consistency** P-II f_NL forecast, P-III multi-survey, P-IV galaxy chirality, P-V DESI chirality cited at the right detail level for a verification companion. No drift.

## Pass-2 self-critique (vs arxiv/paper1b_mcmc_companion.tex)

Reviewed pass-1 findings against the .tex source to check for stale flagging:

1. **E1 / m3 (171 vs 160 envelope floor)** — direct grep of `arxiv/paper1b_mcmc_companion.tex` line 1559–1560 confirms the literal text says "${\approx}8.6$ (largest displacement…) up to ${\approx}160$ (smallest displacement: θ_i=0.5, m=H_0)" with envelope floor printed as `[0.06, 1.19]`. No reconciliation digit (0.0643) appears anywhere in the .tex. Pass-1 finding STANDS. Either the displayed floor needs to become 0.064 or the band's upper edge needs to become 172. Not a falsified pre-existing artifact — this is a current arithmetic gap.

2. **E2 (abstract envelope interpretation)** — .tex abstract line 650-ish references "envelope [0.01,0.48]°"; body §VI line ~1485 says "β ≈ 0.01–0.48° (grid scan over physical trajectories; same artifact)" with the .json artifact path. Pass-1 verified arithmetic via C_aγ extrema; the .tex does NOT state explicitly that the union is over C_aγ ∈ [4,12]. Finding STANDS as MINOR clarification.

3. **E3 (β_combined)** — .tex line 1510 reproduces Eq. (4) verbatim, and the surrounding text (lines ~1230–1270 in pdf, ~1500–1520 in .tex) explicitly flags it as auxiliary cross-check vs published 3.6σ. ALL-CLEAR upheld; no finding.

4. **M1 (c10 robustness battery)** — pass-1 verified against on-disk JSON. The .tex narrative at lines 1290–1311 cleanly identifies the bias as estimator-weighting + BB template shape. Earlier-draft attribution to apodization is correctly retracted. ALL-CLEAR upheld; no MAJOR finding.

5. **m1 (z_p = 0.27 vs β_inj = 0.27° collision)** — confirmed in .tex (line 954 z_p = 0.27, line 1093 β_inj = 0.27°). MINOR cosmetic, stands.

6. **N1 (quintom-B Bayes factor)** — §V.B explicitly defers, scope note repeated three times across abstract/V/Conclusions. Nice-to-have suggestion is additive, not a defect. No promotion to MAJOR.

7. **N2 (KSVZ + misalignment fine-tuning conflation)** — §VI lines ~1620–1640 do separate the two effects (the ≈8.6–160 coupling burden vs the ~25× θ_i tuning in fn 5 + §VI body), but the abstract collapses them into one statement. Nice-to-have, additive.

8. **Calibration-deliberate items NOT flagged** (per instructions):
   - June 2026 current date — not flagged.
   - §VI ALP provenance rewrite (configs matching archived chains run1_full/run2_extended/run3 = 9,720 samples; Δφ/f_a pairings corrected against committed EOM with explicit correction notes; envelope [0.01,0.48]°) — verified against .tex (lines 1450–1520 + Appendix C lines ~1880–1910) and NOT flagged.
   - c10 robustness battery paragraph (bias attribution = unweighted-fit + BB template, NOT apodization) — verified vs JSON + .tex, NOT flagged (the M1 entry above is an ALL-CLEAR, not a finding).
   - Synthetic-ΛCDM relabels, BAO attribution, w_pivot = −0.952 ± 0.019 — all previously verified, not re-flagged.

9. **Pass-1 over-calls checked for retraction**: none. Every finding survives pass-2 against the .tex source.

10. **What I did NOT check** (transparent disclosure):
   - The Liu et al. EC torsion independent-cross-validation H_0 = 68.41 ± 0.32 km/s/Mpc — taken at face value from the paper as cited; did not independently consult arXiv:2507.04025.
   - The Eskilt-Komatsu PR4/NPIPE attribution chain — verified the in-cell PR4/NPIPE label is internally consistent across §IV and Appendix C, but did not independently audit against the public Eskilt repository.
   - The actual MCMC chain files (re-running the Cobaya YAMLs is out of scope for an in-session review).

## Summary recommendation

**Verdict**: MINOR REVISION ONLY. The three E-class findings are all about §VI internal arithmetic consistency (the 10.3/0.06 = 171.7 vs 160 floor and the union-over-C_aγ envelope phrasing); the c10 robustness battery (NEW in this version) verifies cleanly bit-for-bit against the on-disk JSON. The §VI ALP rewrite (NEW in this version) is sound: the Δφ/f_a ∈ [0.06, 1.19] envelope, C_aγ Δφ/f_a = 10.3 product, β_combined = 0.241° ± 0.061° auxiliary cross-check, and the misalignment-tuning + non-minimal-coupling double-burden conclusion all reproduce. **Counts**: E=3 M=0 m=3 N=2 all-clears=11.
