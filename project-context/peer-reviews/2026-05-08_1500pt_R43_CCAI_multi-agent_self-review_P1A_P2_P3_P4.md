# R43 Review — Claude Cross-Agent Internal (CCAI) Multi-Agent Self-Review

**Date:** 2026-05-08, ~15:00 PT
**Round:** R43 (post-Wave-14-VVV)
**Reviewer scheme:** 4 parallel Claude `general-purpose` subagents, one per paper. Each fetched .tex source from GitHub raw URLs and produced an adversarial review without access to other reviewers' findings.
**Caveat (load-bearing):** All four reviewers are Claude (single vendor). This is a **self-critique pass**, not a true cross-vendor review. For the latter, paste the R44 prompt drafted earlier (in `prompt-history.md` or the chat transcript of this session) into fresh sessions of ChatGPT-5, Gemini 3.1 Pro, Grok-4, Perplexity. Two of the BLOCKERs below were caught by the Claude-on-Claude pass, so it had non-zero value, but the cross-vendor pass is still the load-bearing review.
**Excluded:** Paper 1B (cobaya DESI DR2 chain still converging — numbers will change post R-1 < 0.01).

## Summary

| Paper | Version | BLOCKER | MAJOR | MINOR | Total |
|-------|---------|---------|-------|-------|-------|
| P1A — ECH no-go | v1A.0.1 | 3 | 8 | 6 | 17 |
| P2 — f_NL forecast | v1.7.10 | 2 | 8 | 7 | 17 |
| P3 — anomaly catalog | v3.1.21 | 3 | 10 | 10 | 23 |
| P4 — chirality | v1.0.30 | 2 | 5 | 7 | 14 |
| **Total** | | **10** | **31** | **30** | **71** |

## BLOCKERs (priority for arXiv-blocking fixes)

### P1A — ECH no-go theorem (v1A.0.1)

**[CCAI-P1A-B1]** P1A republishes Paper 1B's MCMC headline (H0 = 67.68 ± 1.06 km/s/Mpc, 424,781 samples, ΔNeff ≈ 0). Theory paper should forward-reference 1B with `\cite{Golden2026P1b}`, not duplicate the value. Also: undefined "MCMC proxy" — load-bearing word for whether this is bespoke torsion-modified Boltzmann or vanilla CAMB. **Fix: TEXT-ONLY-EDIT.** Strip the explicit value + sample count from §3.2; replace with: *"MCMC verification with frozen Cobaya posteriors recovers standard ΛCDM (ΔNeff ≈ 0, H0 consistent with Planck 2018), reported in companion Paper I(b)~\cite{Golden2026P1b}."*

**[CCAI-P1A-B2]** ⚠️ STRUCTURAL — Title + abstract advertise *"Two mechanism-independent predictions survive ECH structural closure: (i) f_NL = -35/8 from the matter-bounce class"*. But §13 admits ECH structurally requires N_tot ≈ 92 e-folds (to suppress Λ to (2.3 meV)^4), and N_tot ≫ 60 erases the matter-bounce f_NL signature (standard inflationary mechanism). So the paper's own bookkeeping says the "surviving predictions of ECH" are NOT ECH predictions — they're bounce-class predictions, and ECH itself is structurally incompatible with the bounce class that produces them. The "treated as independent observational programs" hand-wave doesn't resolve this — it just defers. **Fix: FULL HARD FIX (text-level reframing).** Add a subsection explicitly named *"Why the surviving predictions are bounce-class predictions, not ECH predictions"* and forward-reference 1B for full bounce-class discrimination. Drop the implicit framing that ECH itself predicts f_NL = -35/8.

**[CCAI-P1A-B3]** Same B2 logic in the title: *"Structural Closure of Einstein–Cartan–Holst Dark Energy: ... Surviving Matter-Bounce Tests"*. A reader who only sees the title assumes ECH itself predicts f_NL = -35/8, which the paper contradicts. **Fix: TEXT-ONLY-EDIT.** Title: *"Structural Closure of Einstein–Cartan–Holst Dark Energy: A No-Go Theorem and the Matter-Bounce Tests It Does Not Predict."* Or drop the colon-clause about surviving tests.

### P2 — f_NL = -35/8 SPHEREx forecast (v1.7.10)

**[CCAI-P2-B1]** Table 1 reports *Equilateral (k1=k2=k3) | -3.984 | -255/64*. -255/64 = -3.984375 ✓, but **-255/64 is not the matter-bounce equilateral f_NL**. -35/8 = -280/64 is the squeezed value. No derivation chain in §2 connects -255/64 (equilateral) to -35/8 (squeezed); Cai+2009 Eq. (24) reports a different equilateral value (~-2.66). The "-255/64" comparison column shares units with the squeezed -35/8, which is unit-incompatible if -255/64 is actually a shape amplitude A_T(k,k,k). **Fix: FULL HARD FIX.** Either (a) add the explicit derivation showing how A_T(k,k,k) = -255/64 arises from the cubic action evaluated on the equilateral configuration, or (b) relabel Table 1 column as "A_T (shape amplitude)" — not "f_NL" — to remove the units-mismatched comparison.

**[CCAI-P2-B2]** *"Standard single-field slow-roll inflation predicts f_NL = (5/12)(1-n_s) ≈ +0.015"* combined with the abstract's *"|f_NL_bounce|/|f_NL_inf| ≈ 290"*. Maldacena's consistency relation in the squeezed limit is the **gauge-frame** prediction; Pajer/Schmidt/Zaldarriaga 2013 (PRD 88.083502) and Tanaka/Urakawa 2011 (JCAP 2011) show the **physical observable** in conformal Fermi coordinates is parametrically smaller (~ n_s^2). Comparing |f_NL_bounce| = 4.375 to 0.015 as if 0.015 were physical inflates the contrast 290×. A referee will eat this alive. **Fix: FULL HARD FIX (footnote-level addition).** Add: *"f_NL_inf ≈ 0.015 is the gauge-frame prediction; the physical observable in conformal Fermi coordinates is parametrically smaller (~ n_s^2). The bounce-vs-inflation contrast remains |f_NL_bounce| ≫ any single-field inflation observable."*

### P3 — Multi-survey anomaly catalog (v3.1.21) — these indict Wave 14-VVV

**[CCAI-P3-B1]** Headline α = 0.19 ± 0.65 doesn't match α = b − 1 = 0.27 from b = 1.27 ± 0.65. No equation in the visible text reconciling these. Reality (verified against the JSON I generated): 0.19 is the **jackknife mean** of the bias ratio (geomean over 30 JK realizations, gave b = 1.194 → α = 0.194); 0.27 is the **central-bin geomean** (b = 1.265 → α = 0.265) over the 3 signal bins. Both are valid stat estimates with the JK uncertainty (±0.65), but the paper doesn't say which is the headline or why they differ. **Fix: FULL HARD FIX.** Add an explicit equation defining α (e.g., "α ≡ b − 1, where b is the geomean ratio over jackknife realizations"). Show the arithmetic from per-bin values to the headlined 0.19 ± 0.65, and either reconcile with b − 1 = 0.27 or note explicitly which estimator produces the headline.

**[CCAI-P3-B2]** Abstract says *"σ(f_NL) = 8.27 ± 2.37 (an empirical 7.9% improvement over σ(f_NL)^std = 8.98 DESI QSO baseline, with the **±26% uncertainty on the improvement** set by the angular-projection noise floor"*. Three problems: (a) 2.37/8.27 = 28.7%, not 26%; (b) +1σ tail = 10.64 EXCEEDS the baseline 8.98 — meaning the "7.9% improvement" is not even 1σ above zero improvement; (c) the "±26%" framing and the ±2.37 absolute uncertainty are not the same statistical statement and the paper doesn't say which to use. **Fix: FULL HARD FIX.** Either restate as σ(f_NL) = 8.27 ± 2.37 = 28.7% fractional uncertainty (drop the 26% formulation) and add: *"The +1σ tail (10.64) exceeds the baseline 8.98; the empirical improvement is consistent with zero at < 1σ"*, or define precisely what "26% on the improvement" means and show the derivation.

**[CCAI-P3-B3]** α = 0.19 ± 0.65 is consistent with zero at 0.29σ. The Wave 14-VVV closure language ("no longer deferred") is technically defensible (we measured something) but the underlying measurement does NOT constrain the science. 95% CL on α covers [-1.08, +1.46]; the data does not exclude α ≤ 0 (which would *degrade* the forecast). The current symmetric ±2.37 hides this. **Fix: DEMOTE-TO-QUALITATIVE.** Demote σ(f_NL) = 8.27 ± 2.37 from headline to "central-value-only forecast"; add *"α is measured at 0.29σ significance — consistent with no enhancement"* in abstract and §VII; provide one-sided 95% CL on σ(f_NL) (which will likely include the no-improvement case); reframe as a methodology demonstration rather than a positive multi-tracer result.

### P4 — Galaxy chirality (v1.0.30)

**[CCAI-P4-B1]** ⚠️ Wave 14-FFF GZ1 Platt rebuttal of P4-CM-M1: paper says GZ1 CW fraction 48.4% vs Catalog C 49.7% is *"consistent ... at < 2σ under Poisson noise"*. **Actual stat: gap = 1.3 pp; binomial SE on N=46,017 (GZ1) = 0.00233; SE on the difference = sqrt(p(1-p)/N1 + p(1-p)/N2) = 0.00235; Z = 0.013/0.00235 = 5.5σ, not < 2σ.** Even if you (incorrectly) treat the two samples as nested and use only Catalog C's SE (0.000279), the gap is 4.7σ. There is NO reasonable error model that yields < 2σ for a 1.3 pp gap on these sample sizes. The R42 closure of P4-CM-M1 rests on this rebuttal. **Fix: FULL HARD FIX.** Replace "< 2σ" with the correct figure (~5.5σ) and reframe the rebuttal: the defensible argument is that BOTH samples sit within the same systematic floor band (~1% human-handedness bias in GZ1 + ~0.5% Catalog-C residual offset, both well below the 0.2% dipole-detection threshold). The argument is **monopole-floor agreement**, not stat-test consistency. Rewrite around the systematic floor framing.

**[CCAI-P4-B2]** Abstract reports CW fraction *"0.4974 ± 0.0003 global"*. (0.4974 - 0.5)/0.000279 = **-9.3σ from 50/50**. The paper later explains this as a monopole label-artifact (~1% GZ1 human-handedness bias) that doesn't drive the dipole, with the dipole being the actual parity-preference test. But the abstract doesn't say so — a casual reader sees -9.3σ and assumes detection. **Fix: TEXT-ONLY-EDIT.** Add one sentence to the abstract immediately after the CW-fraction value: *"The ~9σ deviation from 50/50 is monopole-only, spatially uniform across the footprint, and traces to ~1% human-handedness bias in the GZ1 training labels rather than physical parity violation; the parity-preference test is the dipole, not the monopole, and the dipole is null."*

## High-impact MAJORs (worth ranking near BLOCKERs)

- **CCAI-P1A-M2**: ALP β = 0.27° is a postdiction (α/M is admitted in Appendix B as a phenomenological scaling ansatz, fitted to the data). Selling β = 0.27° in the abstract as a "surviving prediction" is circular when the prediction is inside the 1σ band of the observation it's "predicting". Fix: demote to consistency check; the genuinely-predictive quantity is the spectral signature (frequency dependence, EB vs TB structure), not the central value.
- **CCAI-P1A-M4**: "$10^{120}$ → $10^5$ fine-tuning reduction" framing — paper itself admits this is *reparameterization*, not a solution to the CC problem. The $10^{-2}$ "structural" piece does no work; the rest is just $e^{-3 N_{\rm tot}}$ tracking N_tot. Fix: be direct — *"This is bookkeeping, not progress."*
- **CCAI-P1A-M5/M6**: Chirality numbers in P1A look duplicative with P4 and have a units/statistic mismatch ($f_{cw}^{eq} = 0.5012 ± 0.0006$ → $(0.0012)/(0.0006) = 2σ$, but paper claims 0.43σ "all-sky dipole"). Different statistics conflated. Fix: define them explicitly or move to P4 only.
- **CCAI-P2-M1**: Heinrich+2023 σ(f_NL) = 0.7 cited without specifying convention (Local/Equilateral/Orthogonal?), redshift range, b_φ marginalization. The 0.7 figure is for fixed-universality b_φ; the paper then *adds* 20-50% widening on top via §7.2 marginalization — that double-counts the b_φ degradation. Fix: cite Heinrich's exact configuration; treat the §7.2 marginalization as an *additional* degradation on top of an already-conservative baseline.
- **CCAI-P2-M2**: §4 invokes sample-variance cancellation (Seljak 2009, McDonald & Seljak 2009) without citing them, and then applies the argument to the **bispectrum-only** forecast. The cancellation argument is for the power spectrum; the bispectrum carries a different cosmic-variance kernel. Fix: cite Seljak 2009 + McDonald-Seljak 2009 for the power-spectrum claim, and Karagiannis et al. 2018 for the bispectrum-multi-tracer extension. Restrict the claim to "bispectrum + power spectrum joint" or remove sample-variance-cancellation from the bispectrum-only forecast.
- **CCAI-P2-M4**: Bayes factor = 8 ("substantial" on Jeffreys') is sold as "decisive". Multifield prior $[-15, +15]$ is paper-asserted with no citation; competing curvaton models naturally produce $|f_{NL}| \lesssim 5$. Setting the multifield prior to $[-5, +5]$ (the actual physical range) drops BF to ~2.7 — *not even substantial*. Fix: report sensitivity-to-prior-width row; drop "recommended physically motivated headline".
- **CCAI-P3-M1**: Title and abstract both round to "37.3 million sources" but reference 37,272,042 (Path-C, post-ACT-quarantine), while CLAUDE.md / SSOT cites 37,292,042. SSOT/paper drift of exactly 20,000 (the ACT patch count). Fix: align SSOT to paper; SSOT was probably written before ACT quarantine.
- **CCAI-P3-M2**: α measured on 5,384 QSO candidates of which only 12 are confirmed at z ≈ 6. The other 5,372 are unconfirmed candidates at unspecified redshifts. Multi-tracer f_NL forecasts depend on bias measured at high-z, where the bispectrum signal lives. The α-to-σ(f_NL) inference assumes the measured α applies at SPHEREx-relevant redshifts. Fix: report effective ⟨z⟩ for the 5,384 sample; restrict measurement to high-z subset (or add caveat).
- **CCAI-P3-M3**: Abstract says 17.8% genuine novelty *"likely represents an upper bound on the full-catalog novelty rate"*. Logic is reversed — highest-scored anomalies are *more* likely to be genuinely novel. Lower-scored anomalies have lower novelty rate. So 17.8% on top-1000 is a lower bound for high-S regime, not an upper bound for the catalog. Paper's own argument runs the wrong direction. Fix: rewrite — the full-catalog rate is *expected to be lower* because lower-scored anomalies are more often margin-of-known.
- **CCAI-P3-M8**: LAMOST has THREE different anomaly counts in the paper (44,075 cross-transfer, 113,342 top-1% slice, 2,054 native S>5). The 388,493 dedup arithmetic uses 113,342 — meaning Table 1 row (44,075) does NOT match the dedup arithmetic. A careful reader trying to reproduce 388,493 from Table 1 will hit a discrepancy. Fix: update Table 1 LAMOST row to 113,342 with footnote that 44,075 was the cross-transfer baseline.
- **CCAI-P3-M9**: SDSS DR18 same problem — native S>5 = 12 sources, but dedup arithmetic uses 77,905 (cross-transfer). Decide and state explicitly: are Table 1 rows cross-transfer or native counts? Make the table consistent across rows.
- **CCAI-P4-M1/M2**: Wave 14-KK 4-bin b/a reconciliation (53,862 NS-count + 3,445 raw→eq direction-flip count) referenced in SSOT/queue.md is **NOT in the published .tex**. Either commit the paragraph or update the SSOT. Currently SSOT says "Wave 14-KK closed" but the closure isn't in the manuscript.
- **CCAI-P4-M3**: §III.F deep-MLP AUC = 0.5656 ± 0.0004 ("integrates to zero over footprint" reframe) is a logical assertion, not a measurement. A scalar score CAN produce directional preference if it correlates with sky position — and the classifier *includes sky coords as features*, which is precisely what would inject sky-position structure. Fix: compute the per-pixel AUC residual map, project onto ℓ=1 spherical harmonic, report induced dipole power. The current "scalar → can't be directional" argument is wrong.
- **CCAI-P4-M4**: Abstract reports `p_LEE ≈ 10^-4` from MC. Actual MC: 0/10,000 nulls exceeded data → p_LEE < 10^-4 (one-sided upper bound at the 1/(N+1) resolution floor). Quoting 9.999×10^-5 with four-figure precision invites reading it as a measured probability. Fix: write `p_LEE < 10^-4 (Monte-Carlo resolution-limited; 0/10,000 nulls)`.

## Suggested fix priority order (post-restart)

1. **P3-B1 / P3-B2 / P3-B3** — Wave 14-VVV abstract caveats (sharpest indictment of recent work; one PDF recompile)
2. **P4-B1** — fix the GZ1 "<2σ" arithmetic error → reframe as monopole-floor agreement
3. **P4-B2** — abstract sentence on monopole vs dipole
4. **P3-M8 / P3-M9** — Table 1 row consistency vs dedup arithmetic
5. **P4-M1 / P4-M2** — commit the Wave 14-KK paragraph OR remove from SSOT
6. **P2-B1 / P2-B2** — Table 1 column relabel + gauge-frame footnote
7. **P1A-B1 / P1A-B2 / P1A-B3** — structural reframing of title/abstract (deepest, biggest edit; theory paper voice)
8. **P1A-M2 / P1A-M4** — demote ALP β = 0.27° postdiction; honest "bookkeeping not progress" framing
9. Remaining MAJORs and MINORs in batches per paper
10. Recompile all touched PDFs + mirror + SSOT + Wave 14-XXX commit

## Per-agent full transcripts

The four agents produced verbose findings that didn't all make this digest. Full per-finding text (with verbatim quotes, evidence, and suggested resolution paragraphs) is preserved in the conversation transcript at:
`~/.claude/projects/-Users-houstongolden-Desktop-CODE-2025-bigbounce/9cddefb0-5996-4de1-9b6e-798ed5d48ed8.jsonl`

(The Agent tool calls in that transcript contain the full ~17K-character per-paper findings.)

## Provenance

- 4 Claude `general-purpose` subagents launched in parallel via Agent tool, ~360s wall each
- Source: `https://raw.githubusercontent.com/Hubify-Projects/bigbounce/main/{paper-path}.tex` per paper
- Per-paper context provided: 65 R42 closures, R43 cheap-fast tier, current Wave-14 status, fiducial physics constants, Houston-only deferred items (NOT to re-flag)
- Total findings: 71 (10 BLOCKER, 31 MAJOR, 30 MINOR)
- Total token cost: ~321K tokens across 4 agents
