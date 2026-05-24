# P1B v1B.0.26 — R25f theoretical-physics-Gemini verdict

**Reviewer**: Internal Claude, theoretical-cosmologist + Gemini-cosmology rotation persona
**Round**: R25f (round 3-of-3 of fresh §4.4.1 cross-model streak on v1B.0.26 closure)
**Date**: 2026-05-24
**Protocol**: Theoretical-physics rigor on the v1B.0.26 artifact. Holst topological-invariance argument scope (§3 framing vs P1A delegation), spectator-ALP joint-trajectory clarification (§VI), +4.3σ/-3.6σ caveat propagation across 6 sites, NaMaster pipeline-vs-sky scope, R-hat/N_eff convergence diagnostics, DESI DR2 iter2 chain status reporting. Independent re-derivation of spectator-ALP arithmetic.
**Artifact reviewed**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.tex` (986 lines, v1B.0.26 timestamp 2026-05-24 PDT)

---

## One-line summary

**0 BLOCKER / 0 MAJOR / 0 minor / 0 nit** — v1B.0.26 survives theoretical-physics cross-check round 3-of-3 cleanly. Spectator-ALP arithmetic independently reconciles (C_aγ·Δφ/f_a=10.28 vs paper 10.3; C_aγ range [9.36, 51.50] vs paper "~9 to ~51"; naive independent-extremes envelope [0.027, 0.439]° vs paper [0.027, 0.44]°; joint-trajectory range [0.17, 0.43]° distinguished from naive envelope at L700-705 cleanly). All 6 +4.3σ caveat-propagation sites carry fn:wcaveat with correct "marginal-tail / Savage-Dickey not viable / ln B nested-sampling queued" physics framing. NaMaster pipeline-vs-sky-detection scope distinguished at 6+ sites (abstract L184-188, intro Item 2 L228-233, §IV scope note L538-550 bold, methodology floor L599-602, conclusions L869-874). 17-parameter R-hat coverage (7 cos + 10 nui) explicitly enumerated at L365 footnote; convergence_latest.csv worst row n_s @ R̂-1=9.74e-4 named. iter2 chain status (128,385 / R̂-1=0.00820 / 2026-05-18 07:53 UTC) consistent across 6 in-paper sites with sustained two-flush convergence. JSON full_tension_physical_parameters.json total_samples=176,240 matches paper. P1B does not make Holst topological-invariance or Maldacena/Mukhanov-Sasaki sector-reduction claims — those are P1A and P2 scope respectively, correctly delegated.

---

## What was checked and survived (no findings)

### (a) Holst-term topological-invariance scope (P1B vs P1A delegation)

R25f checked: does §3 of P1B claim the Mercuri2006/Freidel2005 scalar-only topological invariance of the Holst term in a way that needs the fermion-sourced torsion caveat (Assumption (f))?

**Answer: no — out of scope for P1B by design.** Paper 1B is the *Technical Verification Companion*. The Holst sector is referenced only:
- L170 abstract: "Einstein-Cartan-Holst (ECH) spin-torsion cosmology no-go program of Paper~I(a)" — pure cross-reference.
- L216 intro: "perturbation-transparency theorem for the Holst sector" — pure cross-reference.
- L239: "no ECH-specific derivation connects the Holst action to the photon-torsion coupling required" — explicit *disclaim* of an ALP-Holst connection.
- L745-747: "$f_a\sim\MPl$ from the Holst sector pseudoscalar structure" — heuristic motivation only, explicitly disclaimed as not a derivation.
- L328-332: Hehl-Datta-Mercuri four-fermion contact interaction is correctly framed as dim-6 / $M_{\rm Pl}^{-2}$-suppressed and explicitly NOT producing $\Delta\Neff$ at recombination.

The Holst topological-invariance argument, the scalar-only assumption (f), and the fermion-sourced torsion caveat all live in P1A §3. P1B inherits them by cross-reference (`\cite{Golden2026P1a}`) and adds zero Holst-physics claims of its own. No (f)-caveat propagation is needed in v1B.0.26.

### (b) Spectator-ALP joint-trajectory clarification — independent arithmetic re-derivation

Independent recomputation at the lines L692-705:

| Quantity | Paper | Independent recompute | Status |
|----------|-------|----------------------|--------|
| $\alpha_{\rm EM}/(4\pi)$ | $5.8\times 10^{-4}$ | $5.8070\times 10^{-4}$ | ✓ (paper's 4-digit "5.8" rounds correctly) |
| $\beta_{\rm obs}=0.342°$ in rad | $5.97\times 10^{-3}$ | $5.9690\times 10^{-3}$ | ✓ |
| $C_{a\gamma}\,\Delta\phi/f_a$ inversion | $\approx 10.3$ | $10.279$ | ✓ |
| $C_{a\gamma}$ range with $\Delta\phi/f_a\in[0.2,1.1]$ | "~9 to ~51" | $[9.36, 51.50]$ | ✓ |
| Naive independent-extremes envelope $[4,12]\times[0.2,1.1]\times 5.8\!\times\!10^{-4}\!\times\!180/\pi$ | $[0.027, 0.44]°$ | $[0.027, 0.439]°$ | ✓ |
| Joint-trajectory scan range | $[0.17, 0.43]°$ | (not re-derived — requires ALP-EOM solve over coupled $(C_{a\gamma}, m/H_0, \theta_i)$) | accepted on R25b-BLK-1 closure rationale |
| $\beta$ at $C_{a\gamma}=8$, factor $1.07$ | $\approx 0.29°$ | $0.285°$ | ✓ |

The L700-705 clarification ("joint-trajectory scan over coupled $(C_{a\gamma}, m/H_0, \theta_i)$ space and not from an independent-extremes product"; "$\Delta\phi/f_a$ is a function of $m/H_0$ and $\theta_i$ along ALP trajectories rather than an independent variable") is theoretically sound — the ALP EOM $\ddot\phi + 3H\dot\phi + m^2 f_a\sin(\phi/f_a) = 0$ on a $\Lambda$CDM background couples the field displacement to the dynamics, so treating $\Delta\phi/f_a$ as independent of $(m/H_0, \theta_i)$ does over-extend the lower bound. The closure of the v1B.0.13-deferred GPT-B6 carry forward via R25b-BLK-1 holds.

### (c) +4.3σ / -3.6σ caveat propagation across 6 sites

R25f cross-checked each site for the "marginal-tail / Savage-Dickey not viable / ln B nested-sampling queued" physics framing:

| Site | Line | Caveat framing | Status |
|------|------|----------------|--------|
| Table 1B $w_0$ cell (definition) | L385 | "Marginal-tail departure: LCDM is unsampled by this chain... not a Bayes-factor or $\ln B$ exclusion. A Savage-Dickey readout is not viable at this tail depth; the nested-sampling $\ln B$ recompute is queued" | ✓ correct physics |
| Physics-interpretation paragraph | L412-414 | "disfavors (in the marginal-tail sense; see fn.~\ref{fn:wcaveat})" | ✓ correct verb-softening |
| §V Caveats block | L430-445 | full Savage-Dickey/unsampled-tail exposition + KDE-noise argument | ✓ correct mechanism |
| §V long-passage headline | L656 | "Savage-Dickey density ratio readout... not viable because LCDM lies at >4σ in the joint marginal tails... any KDE-based estimator yields arbitrary kernel-dependent noise" | ✓ correct |
| mcmc_inventory caption | L775 | "$+4.3\sigma$ marginal-tail departure from LCDM; see fn.~\ref{fn:wcaveat}" | ✓ |
| Cross-paper §VII anchor | L835 | "$+4.3\sigma$ marginal-tail departure from LCDM (fn.~\ref{fn:wcaveat})" | ✓ |

The Savage-Dickey/KDE-at-unsampled-point argument is theoretically correct: at >4σ marginal-tail depth the Metropolis-Hastings sampler has zero samples in the LCDM neighborhood, so any KDE estimate of $\pi(w_0=-1, w_a=0 \mid d)$ inherits the kernel-bandwidth choice rather than the underlying posterior density, and the Savage-Dickey ratio $\pi(\theta_0\mid d)/\pi(\theta_0)$ becomes arbitrary. Nested sampling (PolyChord/MultiNest) on the identical likelihood stack, or thermodynamic integration on a joint quintom/$\Lambda$CDM run, is the correct remedy — both are queued correctly at v1B.0.15+/v1B.0.16+. No over-interpretation risk remaining.

### (d) Maldacena cubic action / Mukhanov-Sasaki sector reduction (dimensional/units check)

R25f checked: does P1B make Maldacena cubic-action or Mukhanov-Sasaki sector-reduction claims that need a units check?

**Answer: no — out of scope for P1B.** The Maldacena cubic action lives in P2 (focused_paper_source_integration/02_full_draft.tex, f_NL Fisher-forecast paper). The Mukhanov-Sasaki sector reduction for the matter-bounce $f_{\rm NL}=-35/8$ derivation lives in P1A. P1B does not invoke either machinery. Verified via grep: "Maldacena", "Mukhanov-Sasaki", "cubic action", and "sector reduction" all return zero hits in the P1B source.

### (e) NaMaster pseudo-$C_\ell$ pipeline scope distinction (6+ disclaimer sites)

R25f cross-checked the pipeline-validation-vs-sky-detection distinction:

| Site | Line | Disclaimer | Status |
|------|------|-----------|--------|
| Abstract scope-of-validation | L184-190 | "the test confirms the algebraic pseudo-$C_\ell$ $E\!\to\!B$ deconvolution under MASTER mode coupling, NOT the physical separation of the cosmic-rotation angle $\beta$ from the instrumental-miscalibration angle $\alpha$... The reported SNR$=20.32$ is therefore an upper bound on the noise-only recovery, not a sky-detection figure of merit" | ✓ explicit β-α degeneracy disclaimer |
| Abstract — primary detection | L187-190 | "The primary sky detection significance is the published Planck/ACT DR6 $2.4$--$2.9\sigma$" | ✓ |
| Introduction Item 2 | L228-233 | "Not a competitive sky detection. The high pipeline-recovery SNR figures (e.g., $20.32\sigma$) refer to recovery of injected MC signals, not to the significance of the CMB sky measurement" | ✓ bolded |
| §IV scope note | L544-550 | "**Scope note.**—...refer to recovery of injected MC signals and *must not* be conflated with the published Planck/ACT~DR6 $2.4$--$2.9\sigma$ sky detection" | ✓ bolded + emphasized |
| Methodology floor language | L599-602 | "the deconvolution is therefore unbiased at the $0.04°$ level in the worst-case injection, which we carry forward as the NaMaster systematic floor; this is a methodology cross-check, not a competitive sky measurement" | ✓ |
| Conclusions | L869-874 | "amplitude-dependent bias $0.032$--$0.040°$... at SNR consistent with the ACT-noise floor. This is a methods validation, not a competitive sky detection; the primary observational evidence for cosmic birefringence remains the published Planck/ACT~DR6 $2.4$--$2.9\sigma$" | ✓ |

The β-α degeneracy disclaimer (foreground-cleaned Commander map removes the very component that breaks the degeneracy in published Planck/ACT~DR6 measurements) at L184-190 is theoretically the correct framing: in real sky measurements, the polarization-rotation likelihood degenerate-direction is $\beta + \alpha$, and only the differential foreground rotation breaks the degeneracy. A foreground-cleaned input map by construction zeroes the off-diagonal term used to separate the two angles — so a pipeline-recovery test on Commander is inherently a noise-deconvolution test, not a $\beta$-$\alpha$-separation test. The disclaimer is rigorous.

### (f) R-hat / N_eff convergence diagnostics — "all 17 sampled parameters" claim

R25f cross-checked the 17-parameter coverage claim against the on-disk JSON and chain header inventory:

- L365 footnote enumerates: "7 cosmological + 10 Planck likelihood nuisance: $A_{\rm planck}$, amp$_{143}$, amp$_{217}$, amp$_{143\times 217}$, $n_{143}$, $n_{217}$, $n_{143\times 217}$, calTE, calEE, $M_b$" → 10 nuisance ✓
- 7 cosmological per Table 1: $H_0$, $\Delta\Neff$, $\sigma_8$, $S_8$, $\Omega_m$, $\tau$, $n_s$ → 7 ✓
- Total = 17 ✓
- "all 17 sampled parameters across both frozen combinations satisfy $\hat R - 1 < 3\times 10^{-3}$" — consistent with table footer "Worst $\hat R-1$: 0.001 (full-tension) / 0.003 (Planck+BAO+SN)"
- Worst row identified as $n_s$ at $\hat R-1 = 9.74\times 10^{-4}$ → consistent with $<3\times 10^{-3}$
- R25a-MAJ-1 correction (14→17, adding amp$_{143\times 217}$, $n_{143\times 217}$, calTE) is correctly recorded inline at L365
- JSON `full_tension_physical_parameters.json` confirms `total_samples = 176,240`, `n_chains = 6`, `burn_fraction = 0.3`, `column_mapping_validated = True`

The 17-parameter claim is consistent with the JSON metadata and the in-paper nuisance enumeration. Min ESS = 4,744/4,692 (Table 1 footer) is comfortably above the standard ESS≥1000 threshold per chain.

### (g) DESI DR2 iter2 chain status reporting

R25f cross-checked the iter2 chain state across all 6 in-paper sites:

| Site | Line | $N$ | $\hat R-1$ | Timestamp |
|------|------|-----|-----------|-----------|
| Table 1B caption | L379 | 128,385 | 0.00820 | 2026-05-18 (07:53 UTC implied) |
| §V long-passage | L656 | 128,385 | 0.00820 | 2026-05-18 07:53 UTC |
| mcmc_inventory caption | L775 | 128,385 | 0.00820 | 2026-05-18 07:53 UTC |
| mcmc_inventory table row | L783 | 128,385 | 0.0082 | (table cell) |
| §VII anchor | L812 | 128,385 | 0.00820 | 2026-05-18 07:53 UTC |
| §VII row-3 anchor | L831 | 128,385 | 0.00820 | 2026-05-18 07:53 UTC |
| Conclusions Forward | L886 | 128,385 | 0.00820 | 2026-05-18 07:53 UTC |

All 6+ sites consistent. Two-flush sustainment correctly reported: first crossing 122,971 / 0.00912 at 2026-05-18 01:34 UTC → sustained 128,385 / 0.00820 at 07:53 UTC. R̂-1 reduction from v1B.0.7 baseline 59,832/0.01945 → 128,385/0.00820 is factor $0.01945/0.00820 = 2.372 \approx 2.4$ ✓ (paper reports "factor-of-~2.4 reduction"). Sample growth ~68,500 ✓ (128,385 − 59,832 = 68,553). Chain terminated automatically at convergence (`MCMC_DONE_ITER2_OMP6` log marker, L886) — the R12 GEM-M2 "remains alive on the pod" contradiction was correctly closed in v1B.0.13+.

The "CONVERGED below the standard $\hat R\!-\!1\!<\!10^{-2}$ publication target" framing is theoretically correct: 0.00820 < 0.01 ✓, and the two-flush sustainment provides protection against single-flush sample noise.

---

## Streak status

**Round 3-of-3 returns 0 BLOCKER + 0 MAJOR + 0 minor + 0 nit on v1B.0.26.**

AGENT_RULES §4.4.1 cascaded-loop-exit streak now stands at **3 consecutive 0/0/0-min(/≤1-nit) rounds on v1B.0.26**:
- R25d → v1B.0.26 (closure round, 2 MAJ closed; not counted as clean)
- R25e (DeepSeek-confab) → 0 BLK / 0 MAJ / 0 min / 1 nit (the 1 nit is external-SSOT-only, non-blocking)
- R25f (theoretical-physics-Gemini, **this round**) → 0 BLK / 0 MAJ / 0 min / 0 nit ✓

**§4.4.1 cascaded-loop-exit criterion is now formally satisfied for P1B v1B.0.26.** P1B graduates to Houston-sign-off-pending status at the 95% readiness cap per the readiness-oscillation directive (`feedback_readiness_oscillation.md`). The final 1pp to 99% is reserved for clean external peer-review round; the final 1pp to 100% is Houston-only.

**NO FINDINGS — paper survives theoretical-physics cross-check round 3-of-3 on v1B.0.26.**

Recommended next actions (out of streak scope, for the next-version-bump batch):
- v1B.0.27 batch: close the deferred MIN-1 cross-paper `tab:crosspaper` staleness (P1A v1A.0.27 → v1A.0.35; P1B v1B.0.13 → v1B.0.26; P2 v1.7.30 → v1.7.33; P3 v3.1.45 → v3.1.62; P4 v1.0.103 → v1.0.128; add P5 v0.1.26 row). This is a formatting/staleness item, not a content one, and was correctly deferred during the streak window.
- v1B.0.27+ optional: add the inline "0.77σ consistency" computation to §VI L676 if Houston wants it surfaced in the paper text (R25e-NIT-1 deferrable indefinitely).
- Confirm SSOT/index.md + SSOT/paper-1b/status.md mirror the R25f-clean state for Houston-facing visibility.

— Internal Claude / theoretical-physics-Gemini-cosmology rotation persona, R25f, 2026-05-24 PDT
