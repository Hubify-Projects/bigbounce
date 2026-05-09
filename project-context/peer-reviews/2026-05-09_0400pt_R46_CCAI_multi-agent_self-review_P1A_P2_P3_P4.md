# R46 multi-agent adversarial peer review — 2026-05-09 04:00 PT (Wave 14-VVVV)

Houston directive: continuous R-round adversarial review until findings dwindle to next-to-nothing. R43→R44→R45 ran the loop; R46 is the convergence test (R44=50, R45=50; R46 expected smaller if maturing).

Four parallel Claude general-purpose subagents fetched the latest .tex from GitHub raw at commit c6c27da1 (post Wave 14-UUUU); P1B excluded (compute-gated on cobaya R-1 < 0.01).

## R46 totals

| Paper | Version | BLOCKER | MAJOR | MINOR | NIT | Total | R45 prior |
|---|---|---|---|---|---|---|---|
| P1A | v1A.0.10 | 1 | 3 | 3 | 2 | 9 | 11 |
| P2  | v1.7.17  | 1 | 4 | 4 | 2 | 11 | 15 |
| P3  | v3.1.28  | 1 | 4 | 4 | 3 | 12 | 12 |
| P4  | v1.0.36  | 0 | 4 | 3 | 2 | 9 | 12 |
| **R46 total** | | **3** | **15** | **14** | **9** | **41** | **50** |

**Round-on-round convergence trajectory:**

| Round | BLOCKER | MAJOR | MINOR | NIT | Total | Δ vs prior |
|---|---|---|---|---|---|---|
| R43 | 10 | 31 | 30 | — | 71 | — |
| R44 |  5 | 23 | 17 |  5 | 50 | −29% |
| R45 |  6 | 21 | 17 |  6 | 50 |  0% |
| R46 |  3 | 15 | 14 |  9 | 41 | −18% |

**This is the first measurable convergence after the R44→R45 plateau.** Total findings down 18%, BLOCKER count halved (6 → 3), MAJOR count down 29% (21 → 15). However, loop is NOT yet at the <3 BLOCKER + <5 MAJOR exit condition.

**The three R46 BLOCKERs are issues introduced by R45-closure fixes:**

- **P1A-R46-B1**: Wave 14-QQQQ's Route 2 β̇→Δθ "fix" is dimensionally broken (β̇ in eV is a rate in natural units; multiplying by t in SI seconds without ℏ-conversion factor 1.519×10^15 s^-1·eV^-1 silently treats eV·s as dimensionless). Either β̇~10^-21 eV gives Δθ~6.7×10^11 rad (not 0.06°), or β̇ is in 1/s and the bound should be ~10^-37 s^-1.
- **P2-R46-B1**: Wave 14-RRRR's QSFI parenthetical "(equilateral-like / strongly squeezed)" is internally contradictory — equilateral shapes vanish in the squeezed limit; the (k₃/k₁)^(-3/2) divergence is super-squeezed / long-mode-enhanced, not equilateral.
- **P3-R46-B1**: Wave 14-SSSS's tier arithmetic 264,938 + 113,342 = 378,280 is clean BUT logically requires LAMOST native to have ZERO cross-survey overlaps — directly contradicts §5 conclusions item 8 ("637 multi-survey clusters ... dominated by the SDSS×LAMOST spectroscopic overlap that the native retrain unlocked"). Tier sub-decomposition needs cluster-level rebuild.

**P4 is the cleanest paper at R46** (0 BLOCKERs) because Wave 14-TTTT's honest GZ1 Platt downgrade matches the artifact and held up under R46 scrutiny. The 4 P4 R46 MAJORs are residual issues with the R45 fixes (paragraph self-contradiction in §IV.C, negative-correlation case in §III.D quadrature, factor-of-9 vs ~6–12 inconsistency between abstract and §I/§VIII.A, b+c=7,812 contingency claimed without artifact).

## Per-paper findings

### P1A v1A.0.10 — 9 findings (R45→R46: 11→9, −18%)

**B1 (BLOCKER)** §IV.B Route 2 β̇→Δθ conversion dimensionally inconsistent. β̇ in natural units (eV) and t in SI (seconds) silently treated as dimensionless pair. With ℏ-conversion: β̇=10^-21 eV/ℏ ≈ 1.5×10^-6 rad/s, Δθ over t_rec→today ≈ 6.7×10^11 rad. The "0.06°" number doesn't survive. **Fix:** either restate β̇ in s^-1 with explicit ℏ-conversion, or rederive bound from α_em/(4π)·(H_0/M_Pl). The R2 closure flips: amplitude-suppressed by α_em/(4πM_Pl) ≪ β_obs, NOT amplitude-comparable.

**M1 (MAJOR)** §IV.D vs §IV.B: ρ_θ at R4-bounded coupling does NOT equal 10^-46 eV^4. With α/M=10^-21 GeV^-1, m_θ=H_0=1.5×10^-33 eV, β_obs=5×10^-3 rad, ρ_θ = m_θ²β²/[2(α/M)²] = 2.8×10^-11 eV^4 = ρ_Λ. The "35-OOM mismatch" claim is false at the very values the paper quotes. **Fix:** state actual closure logic — at R4 bound + m_θ~H_0, ρ_θ=ρ_Λ to 1%, so the spectator-ALP route is a CC-problem solution only by re-importing CC-tuning as m_θ~10^-33 eV.

**M2 (MAJOR)** Abstract + §XIV.D say "would be erased" while §IIB + §XIII say "plausibly erased". R45 M3 fix only landed in 2 of 4 locations. Mixed framing across sections.

**M3 (MAJOR)** D_inf "order-of-magnitude matching" downgrade not propagated to §XII (sec:gdp), where the (T_reh/M_GUT)^{3/2}≈0.03 prefactor is still presented as a calculated number. The 10^5 fine-tuning residual inherits the order-of-magnitude status.

**m1-m3** date stamp 1 day in future; "8 OOM in α/M" arithmetic wrong (should be 17.5 OOM); Table II w0wa column asymmetry between matter bounce ✗ vs quintom-B "consistent†".

**n1-n2** abstract "14 distinct mechanism-class" vs Table II "B8 ⊂ B14" caption note; "35 OOM" depends on m_θ choice not stated.

### P2 v1.7.17 — 11 findings (R45→R46: 15→11, −27%)

**B1 (BLOCKER)** §VIII.D QSFI parenthetical "(equilateral-like / strongly squeezed)" — those are physically opposite shapes. (k₃/k₁)^(-3/2) divergence is super-squeezed/long-mode-enhanced, not equilateral. **Fix:** delete or replace with "(super-squeezed / long-mode-divergent)".

**M1 (MAJOR)** Joint-Fisher 9.9σ reported without template-overlap correction r=0.84 that is mandatory for every other significance figure. Either 0.84×9.94=8.35σ should be reported, or the prose must explain why SDB-Fisher is exempt from r-correction.

**M2 (MAJOR)** 13% polynomial null-space scatter added to §II.D (Wave 14-RRRR M6) but not propagated to abstract systematic budget. Realistic 3-5σ headline becomes 2.6-4.4σ if propagated.

**M3 (MAJOR)** BF~17 still doesn't appear in Table 4 cells. Caption explanation deflects rather than fixes. **Fix:** add a column "BF vs tuned multifield, broad [-15,+15]" to populate the delta row with 17.

**M4 (MAJOR)** Curvaton-natural BF~6 still not in abstract — abstract leads with broad-multifield BF~8.

**m1-m4** "exactly half the full polynomial" claim no per-config table; 600,000 MC count rhetorical decoration; "Corrected (10% residual)" row identical to "Ideal" by construction; Cai polynomial 3 valid solutions not cleanly attributed.

**n1-n2** release tag pinned to v1.7.15-paper2 while paper at v1.7.17; Maldacena 0.015 should be quoted as gauge-frame value with conformal-Fermi caveat in same sentence.

### P3 v3.1.28 — 12 findings (R45→R46: 12→12, 0%)

**B1 (BLOCKER)** Tier arithmetic 264,938 + 113,342 = 378,280 logically requires LAMOST native to have ZERO cross-survey overlaps with any of (DESI, SDSS native, eROSITA, Planck, Gaia, NEOWISE) at 5″. Directly contradicts §5 Conclusions item 8: "637 multi-survey 5″ coincidence clusters ... dominated by the SDSS×LAMOST spectroscopic overlap that the native retrain unlocked." Both claims cannot both be true. **Fix:** rebuild catalog-grade vs exploratory partition from actual cluster manifest, OR drop the sub-decomposition entirely and keep only the 378,080 + 200 stratification.

**M1 (MAJOR)** 17.8% novelty rate has FOUR mutually inconsistent labels: abstract "upper bound", §sec:simbad "primary novelty metric", §sec:limitations "single-sample point estimate", Conclusions item 2 "novelty floor". R45 M3 fix only landed in §sec:limitations.

**M2 (MAJOR)** α_GS,jk numerical inconsistency: §sec:fnl line 551 reports b_GS/b_full,jk = 1.19 ± 0.65 (which would give α_GS,jk = 0.19, not 1.83) AND b_GS/b_full,geo = 3.17 (per-bin geomean). Three different "central" b-ratios.

**M3 (MAJOR)** PTA sign convention inconsistent: abstract + conclusions use "+1.13σ above" / "+4.61σ above" (Wave 14-SSSS M5 reframe), but §sec:nanograv body still says "−1.13σ" and §sec:bounce_implications says "−1.13σ" / "−4.6σ". Old sign convention persists in 2 of 4 locations.

**M4 (MAJOR)** α_GS sigma-from-zero asymmetric reporting: abstract reports α_full at 0.29σ-from-null but α_GS only at "<1σ" without naming 0.90σ explicitly. Body has 0.90σ.

**m1-m4** 9.6× α-ratio not b-ratio; title still has "319,443 Cross-Transfer Baseline" parenthetical; γ rounding 3.20 vs 3.193; Wave 14-VVV→KKKK 9.6× central-value shift physical-plausibility narrative absent.

**n1-n3** §sec:limitations missing "prior" qualifier in fiducial; 4.6σ vs 4.61σ rounding; orphan ◊ footnote in Table tab:survey_summary.

### P4 v1.0.36 — 9 findings (R45→R46: 12→9, −25%; CLEANEST)

**(0 BLOCKERS)** Wave 14-TTTT's honest GZ1 Platt downgrade held up.

**M1 (MAJOR)** §IV.C lines 858-862 self-contradiction: same paragraph that downgrades "the L-BFGS converged at the starting point because the GZ1 binary labels lacked recalibration leverage" still asserts "the convergence ... indicates that the CE-ResNet consensus labels carry no detectable systematic chirality bias". The optimizer's failure to move proves only that the loss is flat, not that CE-ResNet is unbiased.

**M2 (MAJOR)** §III.D quadrature-add bound "[1.12, 1.5]pp under any plausible correlation assumption" is mathematically too strong. Negative correlation (ρ=-1) gives |1.0-0.5|=0.5pp, factor of 2 below observed 1.2pp.

**M3 (MAJOR)** Factor-of-9 Shamir comparison reported as single number in §I (line 211) and §VIII.A (line 1498) while abstract concedes range ~6-12. Inconsistent specificity.

**M4 (MAJOR)** McNemar b=4205, c=3607 split asserted four times as if tabulated, but §IV.C line 841 admits "joint-label tabulation companion artifact is required to pin down the exact value (deferred)". Self-contradiction.

**m1-m3** 3.32M vs 3.20M canonical N denominator inconsistency in CE-ResNet sensitivity comparison; bootstrap 28.80σ "external peer-review-required uncertainty" framing oversells (it's a self-consistency check); §VII.B confidence stratification uses P>0.9 strict cut without HC-spiral/HC-broad disambiguation.

**n1-n2** "structurally parity-asymmetric" hangover phrase from old M2 framing; Footnote 4 occupies 16 lines for a result that adds nothing.

## Per-paper backward step (R46 oscillation cycle launch)

Honest readiness rollback after R46 launch:

| Paper | Pre-R46 | R46 backward | Post-R46 | Reasoning |
|---|---|---|---|---|
| P1A | 86% | −8pp | 78% | 1 BLOCKER (β̇ dimensional) + 3 MAJORs (R4 ρ_θ contradiction, plausibly-erased propagation, D_inf to-§XII) |
| P1B | 75% |  0  | 75% | excluded from R46 |
| P2  | 83% | −7pp | 76% | 1 BLOCKER (QSFI parenthetical) + 4 MAJORs (joint-Fisher r-correction, 13% systematic to abstract, BF~17 table column, curvaton in abstract) |
| P3  | 89% | −9pp | 80% | 1 BLOCKER (LAMOST overlap contradiction) + 4 MAJORs (17.8% 4-way framing, b-ratio numerical, PTA signs, α_GS 0.90σ) |
| P4  | 84% | −4pp | 80% | 0 BLOCKERs + 4 MAJORs (paragraph self-contradiction, quadrature bound, factor-of-9, b+c artifact) — gentlest backward step |
| **Average** | **83.4%** | **−5.6pp** | **77.8%** | **smaller backward step than R45 (−9.2pp)** |

**Cycle convergence visible:** R45 launch took the average from 85.6 → 76.4 (−9.2pp); R46 launch takes 83.4 → 77.8 (−5.6pp). The per-round backward step is shrinking by ~40%, suggesting the loop is genuinely converging. Three more rounds at this convergence rate would bring the per-round backward to ~1pp, at which point the "<3 BLOCKER + <5 MAJOR for two consecutive rounds" exit condition becomes plausibly reachable.

## Wave-letter assignments for closing R46 findings

- **Wave 14-WWWW:** P1A v1A.0.10 → v1A.0.11 R46 BLOCKER B1 (Route 2 ℏ-conversion) + 3 MAJORs
- **Wave 14-XXXX-r46:** P2 v1.7.17 → v1.7.18 R46 BLOCKER B1 (QSFI parenthetical) + 4 MAJORs (renamed to avoid clash with cobaya-gated XXXX wave)
- **Wave 14-YYYY:** P3 v3.1.28 → v3.1.29 R46 BLOCKER B1 (LAMOST overlap contradiction) + 4 MAJORs
- **Wave 14-ZZZZ:** P4 v1.0.36 → v1.0.37 R46 4 MAJORs
- **Wave 14-AAAAA:** R46 minors+nits sweep (14 minors + 9 nits)
- **Wave 14-BBBBB:** launch R47 multi-agent adversarial review on post-AAAAA versions

Continuing R46 → R47 → ... loop until per-round delta shrinks to <3 BLOCKER + <5 MAJOR for two consecutive rounds. Then cross-vendor non-Anthropic R-round (GPT-5/Gemini-3.1-Pro/Grok-4/Perplexity) per memory feedback_cross_model_peer_review.md. Then Houston sign-off + arXiv submission.

## R46 review artifact metadata

- **Launched:** 2026-05-09 04:00 PT (Wave 14-VVVV)
- **Subagents:** 4 parallel Claude general-purpose subagents
- **Versions reviewed:** P1A v1A.0.10, P2 v1.7.17, P3 v3.1.28, P4 v1.0.36
- **P1B excluded:** compute-gated on cobaya R̂−1 < 0.01 (currently 0.076)
- **Source:** GitHub raw at commit c6c27da1 (Wave 14-UUUU)
- **Total findings:** 41 (3 BLOCKER + 15 MAJOR + 14 MINOR + 9 NIT)
- **Net delta vs R45:** −3 BLOCKER, −6 MAJOR, −3 MINOR, +3 NIT, −9 total (−18%)
- **Loop convergence status:** **CONVERGING but not yet converged.** Per-round backward step shrinking ~40% (R45 −9.2pp → R46 −5.6pp). Exit condition <3 BLOCKER + <5 MAJOR for two consecutive rounds plausibly 2-3 more rounds away.
