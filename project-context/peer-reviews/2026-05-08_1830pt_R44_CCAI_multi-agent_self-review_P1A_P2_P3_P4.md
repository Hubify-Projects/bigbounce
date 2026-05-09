# R44 Review — Claude Cross-Agent Internal (CCAI) Multi-Agent Self-Review

**Date:** 2026-05-08, ~18:30 PT (post-R43 fixes)
**Round:** R44 (post-Waves 14-WWW through DDDD)
**Reviewer scheme:** 4 parallel Claude `general-purpose` subagents, one per paper. Each fetched .tex source from GitHub raw URLs (the latest post-R43 versions: P1A v1A.0.3, P2 v1.7.12, P3 v3.1.23, P4 v1.0.32). Each ran independently; no shared findings between reviewers.
**Caveat:** All four reviewers are Claude — single vendor self-critique. For true cross-vendor adversarial review, paste the R44 prompt I drafted in the chat transcript into fresh ChatGPT-5 / Gemini 3.1 Pro / Grok-4 / Perplexity sessions.
**Excluded:** Paper 1B (cobaya DESI DR2 chain still converging at R̂−1 ≈ 0.083; numbers will change post R̂−1 < 0.01).

## Summary

| Paper | Version reviewed | BLOCKER | MAJOR | MINOR | NIT | Total |
|-------|------------------|---------|-------|-------|-----|-------|
| P1A — ECH no-go | v1A.0.3 | 3 | 6 | 4 | 0 | 13 |
| P2 — f_NL forecast | v1.7.12 | 2 | 5 | 3 | 1 | 11 |
| P3 — anomaly catalog | v3.1.23 | 0 | 5 | 5 | 2 | 12 |
| P4 — chirality | v1.0.32 | 0 | 7 | 5 | 2 | 14 |
| **Total** | | **5** | **23** | **17** | **5** | **50** |

## Comparison to R43

| Round | BLOCKER | MAJOR | MINOR | Total |
|-------|---------|-------|-------|-------|
| R43 | 10 | 31 | 30 | 71 |
| **R44** | **5** | **23** | **17 + 5 NIT** | **50** |
| Δ | -5 | -8 | -8 | -21 |

Real progress: BLOCKERs cut from 10 → 5 (half closed). MAJORs cut from 31 → 23. P3 and P4 returned 0 BLOCKERs in R44 — both papers are arXiv-ready modulo MAJOR cleanup. P1A and P2 still have 5 combined BLOCKERs from new findings (mostly arithmetic / propagation issues that survived R43's textual fixes).

## R44 BLOCKERs (priority for next batch)

### P1A v1A.0.3 — 3 BLOCKERs

**[CCAI-R44-P1A-B1]** R43 chirality strip was incomplete. Five quantitative chirality claims still in P1A (line 386, 412, 455–459, 911): 8,474,531 sample size, 93.7% validation accuracy, 8/8 bias tests, 4.3×/6.5× catalog ratios, 0.43σ all-sky dipole. **Fix: replace each with a forward-reference to Paper IV.**

**[CCAI-R44-P1A-B2]** §12.1 references a 100,000-sample Monte Carlo sensitivity scan in §15 that does not exist. The "Spearman |ρ_s|=0.996", "2.2% of parameter space", and "100,000 samples" claims are unsupported. **Fix: either add the scan as an appendix, or delete the claim and rely on the analytic e^{-3 N_tot} sensitivity argument.**

**[CCAI-R44-P1A-B3]** Table tab:bounce_disc has "Matter bounce (ECH-compatible)" with f_NL=-35/8 marked ✓. This contradicts the structural-incompatibility theorem (§14.4): N_tot ≈ 92 erases the matter-bounce signature. The R43 BLOCKER reframing to "bounce-class, not ECH-class" is undone by this single table row. **Fix: replace label with "Matter bounce (any host)" or drop the ECH qualifier; the row predicts a bounce-class observable, not an ECH-specific consequence.**

### P2 v1.7.12 — 2 BLOCKERs

**[CCAI-R44-P2-B1]** §10.4 "Joint (f_NL, n_fNL) Forecast" reports σ(f_NL) = 0.44 → 9.9σ for the marginalized SDB channel. This contradicts the 3-5σ headline by a factor of ~2-3×. The 9.9σ is bare SDB Fisher with neither template overlap nor any of the systematics. **Fix: drop the 9.9σ and replace with template+systematic-corrected value, OR explicitly disclose 9.9σ is uncorrected SDB Fisher and reconcile with headline.**

**[CCAI-R44-P2-B2]** Conclusion §11 quotes "1.5–2.5σ" for the convention-flip case while abstract quotes "2.6σ" for the same case. Two arithmetics that don't agree. **Fix: replace conclusion with "halves from the headline 5.2σ to ~2.6σ (template-corrected) or to ~1.5–2.5σ once GR-marginalization and b_φ widening are layered on" — and align abstract.**

### P3 v3.1.23 — 0 BLOCKERs ✓
### P4 v1.0.32 — 0 BLOCKERs ✓

## R44 MAJORs (per-paper, top-impact first)

### P1A v1A.0.3 — 6 MAJORs
- **M1**: Branch-count inconsistency ("17" vs "7+ECH gates" vs "17+") across abstract/§1.2/§15. Table tab:barriers explicitly cites only 6 distinct named branches. **Fix: pick "7 foundation studies + 7 observational branches" as the canonical phrasing throughout.**
- **M2**: LiteBIRD "9σ confirmation" framing is incoherent for a fitted central value. The β=0.27° was just demoted to consistency check; "9σ" mistakes instrumental sensitivity for prediction confirmation. **Fix: replace with "measure β to σ(β)≈0.03° and either confirm a non-zero β at high significance or rule out the spectator-ALP class."**
- **M3**: Four-route no-go ("NJL condensate, one-loop fermion EA, dynamical Immirzi, parity-CMB") is asserted in one paragraph with no derivations. Sole citation is `Golden2026supplement` (non-public author note). **Fix: write 3-4 page Appendix with one paragraph per route, OR cite published derivations (Hehl-Datta NJL, Mercuri α/M, Date-Kaul-Sengupta Immirzi-as-pseudoscalar, Lue-Wang-Kamionkowski parity-CMB).**
- **M4**: D_inf prefactor (T_reh/M_GUT)^{3/2} has no derivation. **Fix: add one sentence justifying the 3/2 power.**
- **M5**: §4 line 443 has three orphan section labels (sec:oneloopfull, sec:condensate, sec:cosmo_derivation) collapsed into a single empty stub. **Fix: populate or delete.**
- **M6**: Table tab:bounce_disc Quintom-B w_0w_a column shows ✓ but P1A line 800-801 disclaims "the w_0w_a extension was never implemented computationally." **Fix: replace ✓ with "consistent (no MCMC test)".**

### P2 v1.7.12 — 5 MAJORs
- **M1**: Bayes-factor abstract envelope still misframed: bullet "~17", Table tab:bayes "8-11", narrative "17". 17 vs 11 unexplained. **Fix: add a column to Table 2 with the multifield prior width per row, reconcile the values.**
- **M2**: Curvaton competitor prior [-15,+15] is wildly wider than realistic curvaton range (|f_NL|≲5). With prior [-5,+5], BF drops to ~3-4 (below "moderate evidence"). The 8-17 abstract framing is reviewer bait. **Fix: lead with [-5,+5]/σ_theory=1.0 BF (~3-4), demote [-15,+15]/delta to theoretical-maximum upper bound.**
- **M3**: Heinrich convention paragraph still lacks explicit normalization equation ζ = ζ_g + (3/5) f_NL ζ_g². **Fix: add one sentence citing Heinrich+2023 Eq. X for the c=2 convention.**
- **M4**: τ_NL = 27.56 saturating Suyama-Yamaguchi is a property of any single-source model (curvaton too), NOT a distinctive bounce prediction. **Fix: soften to "consistent with single-source non-Gaussianity but does not discriminate bounce from saturated single-source inflationary models."**
- **M5**: DBI inflation cited as a local-shape n_fNL competitor; DBI is equilateral-shape, not local. Category error. **Fix: replace with axion-curvaton with non-trivial spectral running (Byrnes/Choi/Hall 2010) or quasi-single-field inflation (Chen-Wang 2010).**

### P3 v3.1.23 — 5 MAJORs
- **M1**: Conclusions §6.5 still says "improve σ(f_NL) by ~6-20%" — pre-VVV positive-detection claim contradicting the demoted abstract. **Fix: replace with central-value-forecast language consistent with §VII.**
- **M2**: §VII has both 8.27 (demoted) AND 6.1%/16.4% positive claims side-by-side. **Fix: subordinate the legacy 6.1% to "for reference only" or delete.**
- **M3**: Three different σ(f_NL) normalizations (8.27 / 0.067-0.116 / 12-17 family) not reconciled. App B.1 uses confabulated σ=12-17 from fire #25 (CLAUDE.md acknowledged correction never propagated). **Fix: delete App B.1 / Fig. B11 entirely or rewrite with Heinrich+2023 σ=0.7 anchor.**
- **M4**: Table 1 footnote ♠ defines "primary tier" two ways (378,080 point-source vs 264,938 catalog-grade-excluding-LAMOST). **Fix: adopt one term per concept: "point-source tier" / "catalog-grade tier" / "exploratory tier".**
- **M5**: Wave 14-VVV α_jk = 0.19 ± 0.65 measured at low ⟨z⟩ (12 of 5,384 candidates spec-confirmed at z≈6); inserted into z>0.8 Fisher pipeline as if redshift-matched. The 8.27 figure is therefore "a number without meaning" at the SPHEREx multi-tracer regime. **Fix: demote to "illustrative central-value insertion only; not a forecast at the redshift relevant to SPHEREx."**

### P4 v1.0.32 — 7 MAJORs
- **M1**: p_LEE reported as point estimate "9.999×10^-5" in §V.A and footnote 12, but as upper bound "<1×10^-4" in abstract. Should be ≤ 1×10^-4 (95% CL upper bound ≈ 3×10^-4 by Clopper-Pearson). **Fix: harmonize all three sites.**
- **M2**: GZ1 Platt "identical to 4 sig figs" claim is suspicious — both fits land at A = 1/4.65 ≈ 0.2151, B = -1.58. Two independent L-BFGS fits on different label sets essentially never converge to identical parameters. **Fix: report actual GZ1-fit parameters with 6 sig figs and quantify |ΔA|, |ΔB|, OR drop the identity claim and rely on the binomial-difference test.**
- **M3**: GZ1 binomial uses unpaired SE √(2 p(1-p)/N), but GZ1 and Catalog C are PAIRED measurements on the same 46,017 galaxies. Correct test is McNemar's. The 5.5σ may underestimate; actual paired Z is likely 7-8σ. **Fix: replace with McNemar / paired binomial; report b, c, χ² and recomputed Z.**
- **M4**: Recall asymmetry (CW 93.8% vs CCW 92.6% on validation) and GZ1 1% bias are double-counted as separate explanations. Recall asymmetry alone predicts 0.64% excess, close to observed 0.79%. **Fix: do the decomposition explicitly; make the three candidate mechanisms in §IV.A mutually exclusive.**
- **M5**: Deep-MLP RA/Dec ablation never run. Agent argues this is a 1-pod-hour ablation, not future work. **Fix: retrain deep-MLP without RA/Dec, report AUC drop. If still > 0.55, coupling is morphology-real; if drops to 0.50, RA/Dec is doing the work and per-pixel projection becomes mandatory.**
- **M6**: §IV.B MDD = 0.2% assumes independent pixels but §IV.A explicitly warns "spatial correlations reduce N_eff < N_spiral". MDD inflates to 0.3-0.4% with N_eff/N = 0.5. **Fix: state MDD as "0.2% assuming independent classifications; N_eff corrections may inflate to 0.3-0.4%".**
- **M7**: 3-of-4 morphology axes FAIL 0.1% CW-flatness target at 10-bin granularity (size 0.32%, fracdev 1.41%, b/a 0.23%). The abstract MDD claim of 0.2% obscures this. **Fix: disclose morphology-bin flatness failure in abstract, or do dipole analysis split by morphology bin.**

## R44 MINORs + NITs

(Listed compactly per paper; full text in agent transcripts at `~/.claude/projects/-Users-houstongolden-Desktop-CODE-2025-bigbounce/9cddefb0-5996-4de1-9b6e-798ed5d48ed8.jsonl`)

- **P1A m1-m4**: c_ω ω² boxed but immediately dropped (m1); ~50 e-folds for rotation dilution unconnected to N_tot=92 (m2); NANOGrav γ canonical citation order P3-then-P2 (m3); 20% GR-projection figure has no citation (m4).
- **P2 m1-m3 + nit1**: "3-5σ realistic" never decomposed in single budget table (m1); anomaly-tracer "10-20%" floats with no Fisher matrix (m2); Jung+2025 PR4 "tightens by 2%" is implausibly small (m3); release tag v1.7.10-paper2 stale (nit1).
- **P3 m1-m5 + nit1-nit2**: α_geo=0.27 vs α_jk=0.19 difference unexplained (m1); "consistent with α=0.15 within 1σ" understates the constraint at 0.06σ (m2); SDSS 77,905 cross-transfer in dedup arithmetic (m3); CMB val_loss 0.4437 fails criterion (a) but glossed (m4); NANOGrav γ project SSOT mismatch (m5); "Munchmüller" misspelling — should be Münchmeyer (nit1); 637 multi-survey clusters dominated by LAMOST FAIL (nit2).
- **P4 m1-m5 + nit1-nit2**: "$-0.12σ$" signed-significance is meaningless (m1); N_MC=1,000 dipole vs 10,000 hemisphere inconsistent (m2); 69.91% spiral accuracy implies 30% error rate, not propagated to dipole-bias bound (m3); GZ1 ACW=CCW orientation convention not specified post-Iye+2020 (m4); Platt calibration is target-shift not bias-reduction (m5); abstract paren-mismatch typo (nit1); stray "PUSHBACK" loop directive in §III.F prose (nit2).

## Suggested fix priority (next batch)

### Wave 14-EEEE (already in flight): P1A v1A.0.3 → v1A.0.4 — R44 BLOCKERs B1/B2/B3 + MAJORs M1/M2

### Wave 14-FFFF: P3 v3.1.23 → v3.1.24
- M1: Conclusions §6.5 update to demoted language
- M2: §VII subordinate the 6.1%/16.4% legacy to "for reference"
- M4: "Primary tier" terminology cleanup
- nit1: Munchmüller → Münchmeyer

### Wave 14-GGGG: P4 v1.0.32 → v1.0.33
- M1: p_LEE harmonization (replace point estimates with upper bounds)
- M2: GZ1 Platt identity claim (drop or report 6 sig figs)
- M3: GZ1 binomial → McNemar paired test
- nit1: abstract paren-mismatch
- nit2: stray "PUSHBACK" prose token

### Wave 14-HHHH: P2 v1.7.12 → v1.7.13
- B1: 9.9σ n_fNL contradiction with headline
- B2: Conclusion 1.5-2.5σ vs abstract 2.6σ harmonization
- M1: Bayes factor table reconciliation
- M2: Curvaton prior [-5,+5] reframing
- M3: Heinrich Eq. X normalization citation
- M5: DBI → axion-curvaton or QSFI replacement

## Provenance

- 4 Claude `general-purpose` subagents launched via Agent tool, sequential (P1A returned first, then P2 explicit, then P3+P4 in background)
- Source: `https://raw.githubusercontent.com/Hubify-Projects/bigbounce/main/{paper-path}.tex`
- Wallclock: ~20 minutes for all 4
- Total findings: 50 (5 BLOCKER, 23 MAJOR, 17 MINOR, 5 NIT)
- Exit condition (<3 BLOCKER + <5 MAJOR total): NOT YET MET. Need at least one more round after applying the queue above.
