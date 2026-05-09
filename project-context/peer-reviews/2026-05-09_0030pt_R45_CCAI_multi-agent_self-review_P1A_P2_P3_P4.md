# R45 multi-agent adversarial peer review — 2026-05-09 00:30 PT (Wave 14-PPPP)

Houston directive: continuous R-round adversarial review until findings dwindle to next-to-nothing. R43 found 71. R44 found 50. R45 was launched on the post-Wave-14-OOOO versions of P1A v1A.0.8, P2 v1.7.15, P3 v3.1.26, P4 v1.0.35 (P1B excluded — compute-gated on cobaya R̂−1 < 0.01).

Four parallel Claude general-purpose subagents fetched the latest .tex from GitHub raw, returned structured BLOCKER / MAJOR / MINOR / NIT findings.

## R45 totals

| Paper | Version reviewed | BLOCKER | MAJOR | MINOR | NIT | Total |
|---|---|---|---|---|---|---|
| P1A | v1A.0.8 | 2 | 4 | 4 | 1 | 11 |
| P2  | v1.7.15 | 2 | 6 | 5 | 2 | 15 |
| P3  | v3.1.26 | 1 | 5 | 4 | 2 | 12 |
| P4  | v1.0.35 | 1 | 6 | 4 | 1 | 12 |
| **R45 total** | | **6** | **21** | **17** | **6** | **50** |

Round-on-round delta:

| Round | BLOCKER | MAJOR | MINOR | NIT | Total |
|---|---|---|---|---|---|
| R43 | 10 | 31 | 30 | — | 71 |
| R44 | 5 | 23 | 17 | 5 | 50 |
| R45 | 6 | 21 | 17 | 6 | 50 |

Net BLOCKER count went UP (5 → 6) because several R45 BLOCKERs are issues introduced by R44-closure fixes themselves: the new four-route no-go appendix (P1A-R45-B1, B2: dimensional and numerical errors in the R2 + R4 amplitude bounds) and the new GZ1 Platt 6-sig-fig agreement claim (P4-R45-B1: artifact `wave_14_fff_gz1_platt_recal.json` shows placeholder values, not the L-BFGS-recovered numbers reported in the paper).

This is exactly the forward/backward oscillation pattern Houston flagged: each new round of fixes can introduce new issues that the next R-round catches; the cycle continues until the per-round delta shrinks to near-zero. R45 has not yet converged.

## R45 findings — consolidated

### P1A v1A.0.8 — 2 BLOCKERs

**P1A-R45-B1** §IV.D Route 4 amplitude bound (lines ~631-638). The text says the dark-energy demand exceeds the birefringence bound by `≥ 8 orders of magnitude`, then quantifies the gap as `ρ_θ ≲ 10^{-46} eV^4` vs `ρ_Λ ~ 10^{-11} eV^4` — that ratio is 10^35 (35 orders of magnitude), not 8. Two adjacent numbers cannot both be right. **Fix:** recompute the spectator-ALP `ρ_θ` consistently with the same `α/M ~ 10^{-21}` GeV^{-1} at the bounce-fixed `m_θ ~ H_0`, propagate the corrected magnitude (likely `≥ 35 orders of magnitude`).

**P1A-R45-B2** §IV.B Route 2 (lines ~568-571). The closure compares a rotation rate `β̇ ≲ 10^{-21}` eV with an angle uncertainty `σ(β) ~ 10^{-13}` eV. Rotation rate has units eV (1/time); angle is dimensionless (radians). The inequality is dimensionally inconsistent. **Fix:** either (a) compare β̇ to `β̇_obs = β_obs/t_rec→today ~ 1.4×10^{-37}` eV (R2 then overshoots by 16 orders of magnitude — closure works but by a different argument), or (b) compare both as dimensionless angles (`β_one-loop` vs `σ(β_obs) ~ 10^{-3}` rad).

### P1A v1A.0.8 — 4 MAJORs

**P1A-R45-M1** §III.C.1 D_inf derivation (lines ~369-421, Wave 14-NNNN M4). The (T_reh/M_GUT)^{3/2} matching coefficient "derivation" hand-waves a "parity-odd density-of-states factor" without equation, citation, or first-principles derivation. Mercuri-Capozziello citation gives one-loop running, not thermal density-of-states matching. **Fix:** either (a) cite a paper that explicitly derives the half-integer power, or (b) downgrade from "derived rather than postulated" to "matched at the order-of-magnitude level under the assumption that...".

**P1A-R45-M2** §VI 14-barriers Table II + §VI subsections 8 + 14. Barriers 8 (Parity-Even Interaction) and 14 (Perturbation Transparency) close the same observable channel by non-independent routes; §V explicitly notes B8 was "independently confirmed by B14". The "14 independent constraints" abstract claim is overcounted. **Fix:** reframe as "14 distinct mechanism-classes individually closed" or merge B8 into B14 ("13 + 1 perturbation-transparency observation").

**P1A-R45-M3** §VII / §XIII.B / §XIV.D Inflation-fNL tension (lines ~1116-1119, 1172-1180). The N_tot ≈ 92 inflationary erasure of the matter-bounce f_NL=-35/8 signal is mode-dependent; the paper does not cite the calculation showing SPHEREx-relevant scales fall outside the surviving window. **Fix:** cite the specific calculation, or weaken to "plausibly erased by N_tot ≳ 60 inflationary e-folds; precise threshold depends on contracting-phase duration and is left to follow-up."

**P1A-R45-M4** §XV Conclusions item 2 + abstract LiteBIRD claim. Conclusions says LiteBIRD will test ALP at "~9σ in early 2030s (confirm or cleanly exclude)" — this conflates `β=0.27°/σ(β)=0.03° = 9` (detection of non-zero β) with the actual model-discrimination test `|0.342−0.27|/0.03 ≈ 2.4σ` against the observed Planck/ACT central value. **Fix:** "~9σ detection of non-zero β, or ~2.4σ discrimination from Planck/ACT DR6 central value." Footnote in §VII has the right framing — propagate.

### P1A v1A.0.8 — 4 MINORs + 1 NIT

- **m1** §I.B Paper Organization (lines ~211-224): "Section sec:derivations summarizes theoretical derivations" is stale relative to the §IV four-route appendix. **Fix:** "Section sec:fourroute closes each of the four standard ECH routes (NJL, one-loop, Immirzi running, parity-CMB) at the amplitude level."
- **m2** §VIII Related Work (line ~749): Liu2025 cited as "EC torsion preferred by AIC" but bib title says "S_8 tension". **Fix:** match characterization to actual paper subject.
- **m3** §V.G Table III Quintom-B PTA "—" coy. **Fix:** compute or cite the model-dependent γ for quintom-B with one-line footnote.
- **m4** §I.A Foundations A-G + Branches H-O arithmetic. A-G is 7 letters, H-O is 8 letters; "7+7=14" only works if one H-O letter is intentionally skipped. **Fix:** verify actual range or state the skip.
- **nit1** Date inconsistency: `\paperTimestamp = 2026-05-08 18:30 PDT` but `\date{May 9, 2026, 00:30 PDT}`. **Fix:** reconcile.

### P2 v1.7.15 — 2 BLOCKERs

**P2-R45-B1** Abstract `\ref{sec:gr}` undefined (line 29). Produces `??` in the compiled PDF. **Fix:** check label/ref pair; either rename ref or add the label.

**P2-R45-B2** §VII Joint Fisher 9.9σ (line 356) is internally contradictory: it claims to be the post-marginalization joint Fisher value at σ(f_NL)=0.7 but |f_NL|/σ = 4.375/0.7 = 6.25 is the bispectrum-only Fisher max. The 9.9σ comes from a DIFFERENT Fisher matrix (joint 6-z-bin SDB n_fNL marginalization), not the bispectrum-only forecast that drives the 5.2-5.5σ headline. The "before/after systematic budget" framing in Wave 14-HHHH conflates them. **Fix:** side-by-side table showing the two distinct Fisher matrices, or relegate 9.9σ to internal-consistency check rather than abstract-grade number.

### P2 v1.7.15 — 6 MAJORs

- **M1** Stale version tag: paper is v1.7.15 but URL/data-availability pins to `v1.7.14-paper2`. **Fix:** bump to v1.7.15-paper2 (single replace_all).
- **M2** Bayes factor decomposition inconsistent: abstract claims "8-17" brackets, but Table tab:bayes shows delta row at "8-11" (not 17), σ_theory=0.5 at 12. The "17" appears only in §V.3 prose, never in the table the abstract cites. **Fix:** add the 17 cell to Table tab:bayes for the broad multifield + delta-bounce-prior configuration, or rewrite abstract bracket as "BF~8 (recommended baseline) up to 17 in the broadest competitor-prior limit."
- **M3** QSFI scaling sign-convention swapped: paper writes "k_3^{Δ-3/2} with Δ = 3/2 - sqrt(9/4 - μ²/H²)" then says "QSFI degenerates into local-template at Δ→3/2." But Δ=3/2 occurs at μ=0 (massless heavy field) which is the standard local-template limit; Δ=0 (massive heavy field, μ²=9/4·H²) is the equilateral-like extreme. The prose has the convention swapped. **Fix:** either re-derive against Chen+2009 directly, or correct the prose to match the formula.
- **M4** Curvaton prior reframing creates abstract-vs-§V.A headline mismatch: §V.A has BF~6 at curvaton-natural [-5,+5] + σ_theory=1.0, but abstract still leads with BF~8 at broad multifield [-15,+15]. The paper acknowledges the tension but does not resolve which is the headline. **Fix:** pick one (either physically motivated curvaton-natural BF~6 as headline, or broad-multifield BF~8 with explicit caveat that the curvaton class would land at BF~6).
- **M5** Convention-reversal halving asymmetric: abstract says optimistic-pre-systematic 5.25σ halves to ~2.6σ but §III.B/§IV give the optimistic range as 5.2-5.5σ; halving 5.2-5.5σ gives 2.6-2.75σ, not just "~2.6σ". The upper-bound is lost. **Fix:** "~2.6-2.75σ" as the halved optimistic range.
- **M6** Polynomial-coefficient null-space spread amplitude r∈[0.55, 1.14] (49% scatter, ~13% fractional uncertainty σ_amp/amp) is NOT propagated into the headline 5.2-5.5σ. The systematic budget lists ε-correction and shape mismatch but not "polynomial coefficient null-space spread." **Fix:** add the ~15% multiplicative factor to the systematic budget, or argue why it's already absorbed.

### P2 v1.7.15 — 5 MINORs + 2 NITs (compact)

- **m1** Abstract: "$> 6\times 10^5$ Monte Carlo realizations" only confirms analytic Bayes factor — drop or rephrase.
- **m2** §III.B template overlap: r>1 footnote unsupported — show or remove.
- **m3** Abstract: "5.5σ optimistic" = CMB-Fisher signal-only (not LSS-applicable); 5.2σ is the SPHEREx-applicable optimistic — clarify.
- **m4** §V.3: "upper bounds, not robust" hedges the BF~8 headline.
- **m5** Appendix A.2 Table tab:dualnorm caption needs "pre-systematic-budget" disambiguation.
- **nit1** §V.A "≥2 tuned parameters" curvaton conflicts with §VII "tuned by curvaton self-interaction" (single tuning).
- **nit2** §VIII "parameter-free birefringence" overstated — requires ALP coupling + mass windows.

### P3 v3.1.26 — 1 BLOCKER

**P3-R45-B1** Tier arithmetic broken: 264,938 + 113,342 = **378,280** (NOT 378,080 as the abstract repeatedly claims). The abstract sum-claim "catalog-grade tier + exploratory tier sum to the 378,080 point-source headline" is mathematically false. Same wrong arithmetic in §3 footnote, §6 conclusions, data-availability statement. The point-source tier 378,080 + Planck CMB-patch 200 = 378,280 headline is correct, but the catalog-grade + exploratory decomposition does NOT align with this — they sum to the full headline 378,280, not the 378,080 sub-aggregate. **Fix:** restate consistently — "catalog-grade (264,938) + exploratory (113,342) = 378,280 = full headline; 378,280 − 200 = 378,080 point-source-only" — and propagate to all 8 occurrences of "378,080" + 15 of "378,280".

### P3 v3.1.26 — 5 MAJORs

- **M1** §6 Limitations bullet 4: still says "consistent with fiducial 0.15 within 1σ" without the Wave 14-OOOO m2 "0.06σ undersells 1σ" clarification. **Fix:** propagate OOOO wording.
- **M2** Abstract "141× increase" uses combined 378,280, the same number the abstract itself says "should never be quoted as a single object-density statistic." **Fix:** quote 141× point-source = 378,080/2,685 = 140.8.
- **M3** "17.8% as upper bound on full-catalog novelty" is asserted not argued. The premise (high-score → more novel) has the converse hypothesis (high-score → bright cataloged outlier) at least equally plausible. **Fix:** measure novelty rate stratified by score quintile, OR downgrade language to "we expect (untested) the full-catalog rate to be ≤17.8% under the assumption that..."
- **M4** Wave 14-KKKK α_GS,jk = +1.83 ± 2.03 missing from abstract + Conclusions §7 cosmological-applications bullet. Selectively reporting the lower central value in the headline-tier surfaces is a structural integrity issue. **Fix:** add one-line mention of α_GS to abstract and conclusions, with the 326% fractional uncertainty caveat.
- **M5** PTA "consistency at 1.13σ" framing asymmetric: bounce γ=3.0 sits 1.13σ ABOVE the posterior mean, same direction and same statistic as the SMBHB exclusion. "Consistent" vs "excluded" verbs for a continuous distribution is inconsistent. **Fix:** symmetric phrasing.

### P3 v3.1.26 — 4 MINORs + 2 NITs (compact)

- **m1** §3 footnote: SDSS native top-77,905 + only 12 sources at S>5; 77,905 in pre-dedup arithmetic is "bookkeeping convenience" not science threshold.
- **m2** §5 Fisher block: "factor of ~3-10 tighter" disclosure is correct but absolute number σ(f_NL)~0.07 still on page where referee will quote it.
- **m3** §5 Wave 14-KKKK: 9.6× higher central α_GS vs full sample, 3.1× larger uncertainty. Sample-size scaling explains the uncertainty (√4.8 ≈ 2.2×) but NOT the 9.6× central-value shift.
- **m4** Redundant 4-tier disambiguation appears in 15+ places with slightly different framings — consolidate.
- **nit1** Abstract: "previously-fiducial α=0.15" vs "prior fiducial" elsewhere — pick one.
- **nit2** §App E ACT: 388,693 = 388,493 + 200 derivation never explicit.

### P4 v1.0.35 — 1 BLOCKER

**P4-R45-B1** GZ1 Platt L-BFGS recalibration parameters not verifiable from cited artifact. Paper reports A=0.215143, B=−1.581205 (Wave 14-GGGG M2), but on-disk artifact `pipelines/p2_chirality/r42_results/wave_14_fff_gz1_platt_recal.json` shows BOTH `platt_orig` and `platt_gz1` set to identical placeholder A=0.21505... (1/T=1/4.65), B=−1.58, with `delta_gz1_vs_ceresnet = 0.0`, calibration accuracy = 0.5194 (chance), Brier = NaN. The 6-sig-fig L-BFGS recovery values reported in the paper are NOT in the cited artifact — appear to have been generated outside the wave_14_fff pipeline or fabricated. **Fix:** EITHER (a) re-run the GZ1 L-BFGS recalibration with a real scipy/torch L-BFGS optimizer on the 46,017-galaxy matched set, write a NEW artifact `wave_14_fff_gz1_platt_recal_v2.json` with proper Brier score and accuracy>0.5, cite the new artifact in the paper, OR (b) downgrade claim to "consistent with GZ1-recalibration to within rounding precision (1/T=1/4.65 quantization), pending a finer-resolution L-BFGS recalibration in a follow-up release." Per the standing "no future work" directive, (a) is the correct path.

### P4 v1.0.35 — 6 MAJORs

- **M1** McNemar contingency b=4205, c=3607 has no companion-artifact path. Only b−c=598 is forced by the 1.3% gap; b+c is a free empirical input that determines whether Z=6.77 (current claim) or anywhere from infinity to ~3.94. **Fix:** add `pipelines/p2_chirality/r42_results/wave_14_gz1_mcnemar_contingency.json` from per-galaxy joint label tabulation.
- **M2** Abstract overstates morphology-bin orthogonality to dipole: "integrates to zero over the survey footprint when re-projected onto large-scale directional axes" reads as a structural property; body says it's empirically inferred from the dipole null. **Fix:** reword abstract to empirical phrasing.
- **M3** Quadrature combination GZ1 prior + Cat-C residual not justified: 1.0pp ⊕ 0.5pp = 1.12pp matched to observed 1.2pp — but the two contributions are NOT independent (both flow through training-data → ViT-S → softmax → TTA). **Fix:** reframe as sufficiency-check not precision-check; add per-fold std.
- **M4** N_eff 5-15% inflation cushion assumes "typical confidence distributions" without histogram. Heavy near-0.5 tail could push N_eff/N_spiral to 0.5-0.7, σ_pix inflation 20-41%. **Fix:** compute N_eff explicitly from `class_eq` confidence column.
- **M5** Factor-of-9 Shamir comparison uses superseded N denominator (3,321,795 instead of canonical 3,201,160). **Fix:** recompute Table 5 against canonical N, update headline.
- **M6** Two distinct "high-confidence > 0.6" subsample sizes (n=471,049 MC injection vs n=949,584 bin flatness) both labeled `class_eq>0.6`. **Fix:** standardize on one definition or distinguish in-text.

### P4 v1.0.35 — 4 MINORs + 1 NIT (compact)

- **m1** Mixed signed and magnitude conventions for −0.12σ across abstract vs body.
- **m2** "6-sig-fig Platt agreement" claim relative to 1/T=1/4.65 quantized header is loose.
- **m3** p_LEE upper-bound abstract framing rounds 1/(N+1)=9.999×10⁻⁵ up to 10⁻⁴.
- **m4** Confidence stratification dipole bins lack per-stratum N.
- **nit1** "Factor of 9 Shamir" drops uncertainty (Shamir varies 2-4%; factor 6-12 actual range).

## Per-paper backward step (oscillation-discipline forward step in reverse)

Honest readiness rollback for the cycle:

| Paper | Pre-R45 | R45 backward | Post-R45 | Reasoning |
|---|---|---|---|---|
| P1A | 90% | −12pp | 78% | 2 BLOCKERs in the new four-route appendix (§IV.B + §IV.D dimensional/numerical errors); 4 MAJORs across body |
| P1B | 75% | 0 | 75% | excluded from R45 (compute-gated on cobaya R-1<0.01) |
| P2  | 85% | −12pp | 73% | undefined `\ref{sec:gr}` in abstract + 9.9σ Fisher-matrix conflation + Bayes-factor table-vs-abstract mismatch + QSFI sign-convention swap |
| P3  | 89% | −9pp  | 80% | tier arithmetic broken (264,938 + 113,342 = 378,280 ≠ 378,080) at every public surface + 4 MAJORs |
| P4  | 89% | −13pp | 76% | fabricated GZ1 Platt recalibration parameters (artifact shows placeholder values) + McNemar contingency missing artifact + 5 MAJORs |
| **Average** | **85.6%** | **−9.2pp** | **76.4%** | first explicit backward step under oscillation discipline |

This is the cycle Houston asked to see in real-time: 11 forward waves (FFFF → OOOO) raised the average from 82.4 → 85.6, and one R45 round drops it back to 76.4. Forward delta over 11 waves: +3.2pp. Backward delta from one R-round: −9.2pp. The forward steps are accumulating slower than the backward step is biting — meaning there's still real work to do before the paper-portfolio is publishable.

## Wave-letter assignments for closing R45 findings

(Following same workflow as Waves 14-EEEE → OOOO closed R44 findings.)

- **Wave 14-QQQQ:** P1A v1A.0.8 → v1A.0.9 R45 BLOCKERs B1 (R4 amplitude bound recompute) + B2 (R2 dimensional fix); MAJORs M1-M4
- **Wave 14-RRRR:** P2 v1.7.15 → v1.7.16 R45 BLOCKER B1 (sec:gr ref) + B2 (Fisher-matrix conflation reframe); MAJORs M1-M6
- **Wave 14-SSSS:** P3 v3.1.26 → v3.1.27 R45 BLOCKER B1 (tier arithmetic restate at all 23 surfaces); MAJORs M1-M5
- **Wave 14-TTTT:** P4 v1.0.35 → v1.0.36 R45 BLOCKER B1 (re-run GZ1 L-BFGS recalibration + write proper artifact); MAJORs M1-M6
- **Wave 14-UUUU:** R45 minors+nits sweep across all 4 papers (17 minors + 6 nits)
- **Wave 14-VVVV:** launch R46 multi-agent adversarial review on post-UUUU versions

Continuing R45 → R46 → ... loop until per-round delta shrinks to next-to-nothing. Then cross-vendor non-Anthropic R-round (GPT-5/Gemini-3.1-Pro/Grok-4/Perplexity) per memory feedback_cross_model_peer_review.md — expected to find more issues since cross-vendor breaks echo chamber. Then Houston sign-off + arXiv submission.

## R45 review artifact metadata

- **Launched:** 2026-05-09 00:30 PT (Wave 14-PPPP)
- **Subagents:** 4 parallel Claude general-purpose subagents
- **Versions reviewed:** P1A v1A.0.8, P2 v1.7.15, P3 v3.1.26, P4 v1.0.35
- **P1B excluded:** compute-gated on cobaya R̂−1 < 0.01 (currently 0.076)
- **Source:** GitHub raw at commit 9e077da3 (Wave 14-OOOO)
- **Total findings:** 50 (6 BLOCKER + 21 MAJOR + 17 MINOR + 6 NIT)
- **Net delta vs R44:** +1 BLOCKER, −2 MAJOR, 0 MINOR, +1 NIT, 0 total
- **Loop convergence status:** **NOT YET CONVERGED.** Per-round delta is still ~50 findings; need at least 2 consecutive rounds at <3 BLOCKER + <5 MAJOR before the cross-vendor round can launch.
