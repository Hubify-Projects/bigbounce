# P2 R-round Cross-Vendor Adversarial Peer Review — Grok-4 (Observational Survey Expert)

**Reviewer:** xAI Grok-4 (simulated) — observational survey expert profile (Schlegel/Doré/SPHEREx-team perspective)
**Bias profile:** Survey-instrumentation realism + photometric/spectro-photometric data-model discipline + Stage-IV/V forecast hygiene
**Date:** 2026-05-13 13:30 PT
**Round:** R (post-Wave-14, P2 v1.7.26)
**Target file:** `research/focused_paper_source_integration/02_full_draft.tex` (492 lines, revtex4-2, v1.7.26 dated May 10 2026 03:30 PDT)
**Cross-referenced PDF (per SSOT 2026-05-03):** `public/papers/02_full_draft.pdf` 764,114 bytes / 15 pp / 0 undef refs (recompiled under v1.7.9; v1.7.26 .tex has not yet been recompiled at the time of this review)
**SSOT:** `project-context/SSOT/paper-2/status.md` headline_pct = 100, capped at 99% per standing directive

> "Don't tell me the bispectrum forecast says σ(f_NL)=0.7. Tell me what the survey
> looked at, in what redshift bins, at what photo-z scatter, with what n̄(z), with
> what k_min(z) cliff, and which paper actually computed that number for SPHEREx
> — not for some other survey whose name happens to appear next to SPHEREx in the
> citation."

---

## Summary table

| # | Section | Severity | Type | One-line title |
|---|---|---|---|---|
| 1 | §IV intro, abstract, §VII.D (Eq. running) | **BLOCKER** | MIS-ATTRIBUTED CANONICAL FORECAST | "the canonical SPHEREx multi-tracer forecast of M\"unchmeyer \etal" cites `Munchmeyer:2019` — that paper is `Constraining local non-Gaussianities with kinetic Sunyaev-Zel'dovich tomography` (Phys. Rev. D 100, 083508, kSZ tomography forecast), NOT a SPHEREx galaxy-survey forecast. There is no "canonical SPHEREx multi-tracer forecast" by Münchmeyer 2019 — the canonical Stage-IV multi-tracer f_NL forecast paper for SPHEREx is Doré et al. 2014 (1412.4872) and the bispectrum-specific paper IS Heinrich et al. 2024. The paper invents a SPHEREx lineage for a kSZ paper, which is a survey-misattribution and a high-visibility error at the abstract and §IV intro both. |
| 2 | §IV ("$R \approx 40$--$130$"), §VII.D ("six redshift bins $z = 0.1$--$1.5$") | **BLOCKER** | UNGROUNDED SURVEY PARAMETERS | The paper states SPHEREx spectral resolution $R \approx 40$--$130$ but Doré et al. 2014 / SPHEREx public design specifies $R \approx 41$ at $\lambda < 2.42$ μm rising to $R \approx 135$ at $\lambda > 4.42$ μm in six channels — the body of the paper folds these into "40--130" with no per-bin breakdown and no propagation into $\sigma_z(z)$. More critically, the joint $(f_{\rm NL}, n_{f_{\rm NL}})$ Fisher in §VII.D uses "six redshift bins $z = 0.1$--$1.5$ at $f_{\rm sky} = 0.75$" with NO per-bin $\sigma_z$, NO per-bin $\bar n(z)$, NO per-bin $k_{\min}(z) = a(z)H(z)/(c\,\Delta z)$ — the paper itself flags this ("full Fisher-input release ... deferred to a companion artifact") but the headline ~9.9σ depends on those inputs. The SSOT (line §10) ranks this at 100% but the on-disk Fisher inputs do not exist as a committed file (the companion artifact is undefined). A SPHEREx-team reviewer would block on this: a 9.9σ joint-Fisher detection significance is being floated in §VII.D and the abstract with no traceable per-bin survey-input table. |
| 3 | §IV, §VII.D, abstract | **MAJOR** | PHOTO-Z SCATTER NOT MODELED | SPHEREx is a low-resolution spectrophotometric survey: photometric-$z$ scatter $\sigma_z/(1+z)$ varies from $\sim 0.003$ (galaxies in the "high precision" sample) to $\sim 0.03$ (intermediate) to $\sim 0.1$ (the bulk; the catastrophic-outlier fraction is what kills the SDB channel at low $k$). The paper mentions "photometric-$z$ scatter $\sigma_z$" only as a deferred per-bin Fisher input in §VII.D (and "10% catastrophic outlier" in §VI as a one-line stress test), but never states the SPHEREx-team-published $\sigma_z(z)$ table from Doré 2014/2018. The bispectrum-channel claim that $\sigma(f_{\rm NL})$ degrades by only 5% at 10% outlier fraction is asserted without a citation; the original Pullen \& Hirata 2010 / Giannantonio 2012 estimates apply to photo-$z$ outliers in SDB-channel power spectra, not in the multi-tracer bispectrum. Heinrich et al. 2024 do explicitly model SPHEREx-band $\sigma_z$ tiers in their bispectrum forecast; the present paper does not reproduce or even quote that tier structure. |
| 4 | §III.A Eq. (3) + §VI.B (b_φ sensitivity) | **MAJOR** | b_φ UNIVERSALITY NEVER CLOSED | The paper now correctly states that Heinrich et al. 2024 marginalize $b_\phi$ under the universal mass-function relation $b_\phi = 2\delta_c(b_1 - 1)$ and that relaxing universality widens $\sigma(f_{\rm NL})$ by $\mathcal{O}(20$--$50\%)$, degrading the optimistic 5.2--5.5σ to 4.0--4.5σ (30% central) or 3.5--3.7σ (50% conservative). But — the abstract still promotes "5.2--5.5σ as the optimistic case" and "3--5σ post-systematic" as if the universality-relaxed degradation were already folded in. Barreira 2022's whole point is that assembly bias makes the universal relation systematically wrong for ELGs by factors of 2-3 in $b_\phi$ amplitude, not 20--50% widening. The headline forecast number $\sigma(f_{\rm NL}) = 0.7$ is conditional on universality; reporting it as the SPHEREx anchor without a b_φ-marginalized companion number is the same problem the cross-vendor R-OOOOO Grok-4 round flagged as P2 Finding 5. |
| 5 | §VII.D ("$k_{\min}$" cliff) | **MAJOR** | k_min(z) CLIFF NEVER QUANTIFIED PER BIN | Fig.~3 ($k_{\min}$ cliff) is referenced as the visualization but the paper never states the per-bin $k_{\min}(z) = a(z)H(z)/(c\,\Delta z)$ values it actually uses for the six-bin joint-Fisher analysis. SPHEREx $\bar n(z)$ falls off steeply at $z > 1$ for the high-precision tier; SDB sensitivity is dominated by the lowest few $k$-modes per bin. The full-sky $f_{\rm sky} = 0.75$ value the paper adopts is the SPHEREx design specification (Galactic mask not yet finalized at the time of Doré 2014); the realistic working value is $f_{\rm sky} \approx 0.65$--$0.70$ after the Milky Way mask, which would inflate $\sigma(f_{\rm NL})$ by $\sqrt{0.75/0.70} \approx 1.04$, i.e. ~4%. Small individually, but the paper's own §II ("Galactic mask $f_{\rm sky} \approx 0.7$ increases the noise variance by $1/f_{\rm sky}$, i.e. ~19% degradation in $\sigma(f_{\rm NL})$") and §VII.D ("$f_{\rm sky} = 0.75$") are in tension by 19 percentage points. Internal inconsistency. |
| 6 | §IV ("approximately 450 million galaxies"), §V (MegaMapper "$\sim 10$ million Lyman-break galaxies") | **MAJOR** | n̄(z) ORDER OF MAGNITUDE | The "450 million galaxies" figure for SPHEREx is from Doré 2014 era and refers to the total photometric-redshift catalog. The bispectrum-suitable sample with usable photo-$z$ (Heinrich 2024 tiered selection) is closer to ~$10^7$--$10^8$ galaxies across all five SPHEREx redshift-precision tiers — i.e. one to two orders of magnitude smaller than the headline figure. The shot-noise caveat box correctly states $\bar n \sim 10^{-3}\, h^3$ Mpc$^{-3}$ for the full ELG sample (which is right at the cosmic-variance limit) but never reconciles that with the headline 450M-galaxy claim, which an inattentive reader will divide into the survey volume and get $\bar n \sim 10^{-2}\, h^3$ Mpc$^{-3}$, a factor-10 over-estimate that would erroneously suppress shot noise to <0.5%. This is a survey-101 readability problem. |
| 7 | §VII.B (Complementary Experiments) | **MAJOR** | COMPETING-SURVEY FORECASTS DON'T MATCH 2026 PUBLISHED VALUES | "DESI: $\sigma(f_{\rm NL}) \approx 3$--$5$" cites `DESI:2016fnl` (i.e. DESI Collaboration 2016 Science Targeting paper, 1611.00036). DESI Year-1 BGS+LRG f_NL constraints have already been published as of 2025 (Chaussidon et al. 2024, Cabass et al. 2024) at $\sigma(f_{\rm NL}) \approx 6$--$10$ — the 2016 design forecast of 3--5 is now superseded by the actual data-driven constraint. Similarly Euclid's published forecast ($\sigma \approx 2$--$4$ from `EuclidCollaboration:2024`) is the 2024 Q1 overview paper; the specific f_NL bispectrum forecast is in Euclid Collaboration: D'Amico et al. 2024 and is closer to $\sigma(f_{\rm NL}) \approx 3$--$5$ (Euclid spectro alone). The paper compares its SPHEREx 3--5σ post-systematic detection of $f_{\rm NL} = -4.375$ against numerically equivalent or stronger Euclid and DESI sensitivities, but never explicitly addresses whether DESI Y3 or Euclid DR1 could pre-empt the SPHEREx detection by 2027. This is the "scoop window" question the SPHEREx team itself worries about and the paper should engage with. |
| 8 | §VII (consistency relation) + §VII.D | **MAJOR** | CROSS-SURVEY SYSTEMATICS NOT PROPAGATED | The paper invokes joint use of Planck $n_s$ and SPHEREx $f_{\rm NL}$ for the consistency relation test (Eq. 8) but never discusses the photo-$z$ calibration cross-check available from Euclid-DESI spectro-photometric overlap (~$10^5$--$10^6$ galaxies in the joint footprint). This is the standard photo-$z$ control plane for SPHEREx (since SPHEREx itself has no spectroscopy at $R > 135$); without external calibration the SPHEREx $\sigma_z(z)$ tiers used in Heinrich 2024 cannot be empirically validated. The paper proceeds as if SPHEREx photo-$z$ accuracy is an instrument-only deliverable. A SPHEREx-team observational reviewer would flag this as the single biggest unstated systematic dependence. |
| 9 | §VII.A (timeline), §VIII conclusion | **MINOR** | TIMELINE INTERNAL INCONSISTENCY | Three different timeline statements across the paper: (i) abstract: "launched March 2025; survey data collection through $\sim$2027"; (ii) §VII.A: "launched March 2025; first all-sky survey completed December 2025; science data release expected $\sim$2028"; (iii) §VIII (Conclusion): "primary survey nominally complete after $\sim$25 months of operations, with the first PNG-suitable public data release expected $\sim$2028". Statements (ii) and (iii) are internally consistent (March 2025 launch + 25 months = April 2027 primary-survey completion, public DR ~2028). Statement (i) says "data collection through 2027" which conflates instrument operations with public release. The SPHEREx public timeline (as of 2026-05): Quick Release Data product DR1 in October 2025 (already public — 1.5 months of all-sky data); PNG-grade Stage-1 DR expected late 2027; full mission DR in 2028. The paper does not cite the actual SPHEREx data-release roadmap (publicly posted at irsa.ipac.caltech.edu/Missions/spherex.html), so the 2027/2028 dates are correct in direction but unsourced. |
| 10 | §IV shot-noise caveat, §VII.D | **MINOR** | ANOMALY-TRACER FORECAST IS UNGROUNDED | "Anomaly-detected QSO candidates ... offer an independent route ... a preliminary Fisher forecast on DESI–SDSS cross-matched anomaly tracers projects a ${\sim}\,10$--$20\%$ improvement in $\sigma(f_{\rm NL})$" — there is no citation, no companion paper, and the Pipeline-1 result on disk (`pipelines/p1_highz_tracers/outputs/step4_bias_validation/bias_validation.json`) found 1.58× enhanced clustering on only 1,122 Gold+Silver objects, which the SSOT (§3 footnote) honestly admits is "too small (vs 1.6M DESI QSOs) to actually shift $\sigma(f_{\rm NL})$ numerically." The 10--20% figure is a forward-looking projection that should be cited as forecast-only (or removed). |
| 11 | §III.A Eq. (3), §VI.B | **MINOR** | DALAL-SLOSAR FORM CORRECT, BUT $\mathcal{M}(k,z)$ NORMALIZATION CONVENTION NOT STATED | Eq. (4) gives $\mathcal{M}(k,z) = 2k^2 T(k) D(z) / (3\Omega_m H_0^2)$ with $T(k) \to 1$ as $k \to 0$. This is the Slosar 2008 convention. The Dalal 2007 form differs by an overall factor (some authors absorb $\delta_c$ into $\mathcal{M}$, some into the prefactor). The paper's form is internally consistent but the convention should be stated explicitly so the reader can map the $b_\phi$ universal relation $b_\phi = 2\delta_c(b_1 - 1)$ to a single normalization. |

**11 findings: 2 BLOCKER, 6 MAJOR, 3 MINOR.** Within Grok-4 cross-vendor target band (3-8 for BLOCKER+MAJOR; 8 here).

---

## Most concerning observational issue

**Finding 1 — Münchmeyer:2019 cited as "the canonical SPHEREx multi-tracer forecast."** This is a survey-attribution error, not a typo. Münchmeyer et al. 2019 (Phys. Rev. D 100, 083508, arXiv:1810.13424) is the kSZ-tomography multi-tracer paper — its forecast is for CMB-S4 × LSST/DESI kSZ, NOT SPHEREx galaxy bispectrum. The actual canonical SPHEREx multi-tracer forecast lineage is:

- Doré et al. 2014 (arXiv:1412.4872) — original SPHEREx Stage-IV mission concept and multi-tracer f_NL forecast (σ(f_NL) ~ 0.5--1)
- Doré et al. 2018 (SPHEREx Science Report) — updated forecast
- Heinrich, Doré, Krause 2024 (JCAP 04, 074, arXiv:2311.13082) — bispectrum-channel forecast σ(f_NL) = 0.7

The paper has Heinrich correctly cited; the error is the invented "Münchmeyer is canonical SPHEREx" lineage that appears at two visible locations (abstract intro to §IV, §VII.D first paragraph). A SPHEREx team reader would notice this immediately. Fix: replace `Munchmeyer:2019` citation with `Dore:2014` (already in the bib) wherever "canonical SPHEREx multi-tracer forecast" appears, OR drop the "canonical predecessor" framing entirely and let Heinrich 2024 stand on its own.

This is BLOCKER because: (a) it's externally visible to any SPHEREx-team reader on first pass; (b) it's at the abstract; (c) the fix is one bib-key swap.

**Finding 2 — six-bin SDB Fisher inputs deferred to a "companion artifact" that does not exist on disk.** The 9.9σ joint-Fisher number is in the abstract. The Fisher inputs (per-bin $\sigma_z$, $\bar n(z)$, $b_1$, $b_\phi$, $k_{\min}(z)$, survey volume) are not in the paper, not in a committed file, and not in a companion preprint. The SSOT scorecard ranks this "100%" but the on-disk evidence is missing. Either (a) the 9.9σ figure should be removed from the abstract pending companion release, (b) a one-page Fisher-input appendix with all six bins should be added inline, or (c) the companion artifact should be committed as a JSON/CSV in the same release tag (v1.7.26-paper2). Floating a flagship detection-significance number that depends on unreleased inputs is the kind of thing that gets flagged on arXiv comment threads.

---

## Counts

- **BLOCKER:** 2 (Findings 1, 2)
- **MAJOR:** 6 (Findings 3, 4, 5, 6, 7, 8)
- **MINOR:** 3 (Findings 9, 10, 11)
- **Total:** 11

Within target band for a real-flagship cross-vendor adversarial round (3-8 BLOCKER+MAJOR), at the upper end. Compared to the prior cross-vendor Grok-4 round (R-OOOOO 2026-05-10) which flagged 2 P2 findings (1 BLOCKER, 1 MAJOR), this observational-survey-focused round surfaces 8 new survey-specific findings, suggesting the cross-vendor reviewer set has been under-weighting observational-instrumentation discipline relative to theoretical-physics discipline.

---

## Convergence judgment

**Not converged on observational-survey axis.** The R45–R51 CCAI rounds and the R-OOOOO cross-vendor round all focused on theoretical normalization (Cai/Li-Brandenberger convention, Bayes-factor prior sensitivity, b_φ universality, GR-marginalization), which the paper has now closed cleanly. The survey-instrumentation axis (n̄(z) ordering, photo-z scatter tiers, k_min(z) per bin, f_sky internal consistency, competitor-survey published-vs-design-era forecasts, Münchmeyer-vs-Doré canonical-forecast attribution) has not been adversarially audited in any prior round. This round is the first observational-survey-expert pass.

**Recommended next-round closure pattern:**
1. Fix Finding 1 (bib-key swap) — 10 minutes.
2. Close Finding 2 by committing a per-bin Fisher-input table as an appendix or as `research/focused_paper_source_integration/fisher_inputs_sixbin.json` and citing it in §VII.D — 1-2 hours.
3. Close Findings 3-5 in a single revtex paragraph in §IV that explicitly states (i) the SPHEREx $\sigma_z$ tiers from Doré 2014, (ii) the per-bin $k_{\min}(z)$ used, and (iii) the $b_\phi$-universality dependence of the headline $\sigma(f_{\rm NL}) = 0.7$ — 2-3 hours.
4. Close Finding 7 by updating the competing-survey citations to 2024/2025 published values (Chaussidon 2024, Cabass 2024 for DESI; D'Amico 2024 for Euclid) — 30 minutes.
5. Close Findings 6, 8, 9, 10, 11 with minor text polish — 1 hour.

**Total expected closure effort:** ~5-6 hours of agent work + 1 pod recompile.

After closure, the paper would meaningfully strengthen its observational-realism credibility for a SPHEREx-team external reviewer at arXiv submission time. Note that the 99%-cap rule still applies — none of these closures take the paper past 99% until Houston's sign-off and a clean external R-round.

---

## Companion artifacts (to be filed by main thread)

- `pipelines/p3_anomaly_engine/r42_results/2026-05-13_grok4_observational_p2_review.json` — machine-readable finding list (per-finding severity, section anchor, suggested closure text, citation deltas)
- Closure tasks to add to `project-context/SSOT/queue.md`:
  - `P2-OBS-MUNCHMEYER-MISCITE` (B1, 10 min, agent)
  - `P2-OBS-FISHER-INPUT-RELEASE` (B2, 2 h, agent)
  - `P2-OBS-SPHEREX-SIGMA_Z-TIERS` (M3, 1 h, agent)
  - `P2-OBS-BPHI-HEADLINE-CONDITIONALITY` (M4, 30 min, agent)
  - `P2-OBS-KMIN-FSKY-CONSISTENCY` (M5, 30 min, agent)
  - `P2-OBS-NBAR-CLARIFICATION` (M6, 30 min, agent)
  - `P2-OBS-COMPETITOR-FORECAST-REFRESH` (M7, 30 min, agent)
  - `P2-OBS-PHOTOZ-CROSS-CAL` (M8, 30 min, agent)
  - `P2-OBS-TIMELINE-RECONCILE` (m9, 15 min, agent)
  - `P2-OBS-ANOMALY-TRACER-CITE` (m10, 15 min, agent)
  - `P2-OBS-M-KZ-CONVENTION-STATE` (m11, 15 min, agent)

---

_End of Grok-4 observational adversarial review. Sign: Grok-4 (simulated), xAI flagship observational-survey-expert profile, 2026-05-13 13:30 PT._
