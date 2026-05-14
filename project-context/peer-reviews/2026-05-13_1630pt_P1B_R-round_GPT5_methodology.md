# P1B v1B.0.3 — GPT-5 Adversarial Review (Methodology)

**Date:** 2026-05-13 (16:30 PT)
**Reviewer persona:** OpenAI GPT-5, statistical-methodology lens (Gelman/Vehtari-flavored adversarial)
**Paper:** `arxiv/paper1b_mcmc_companion.tex` v1B.0.3 (header L46 says `v1B.0.3`, abstract L61 dated "May 8, 2026, 21:30 PDT") / 658 lines / depends on shared `arxiv/references.bib`
**Headline under review:** $\Lambda$CDM$+\Delta N_{\rm eff}$ stock-CAMB proxy MCMC (424,781 total / 309,789 frozen samples across 3 dataset combinations), NaMaster 500-MC pipeline validation ($\hat\beta=0.238^\circ$ for $\beta_{\rm inj}=0.27^\circ$, pipeline SNR=20.32), and spectator-ALP consistency with Eskilt+2022b joint Planck+ACT $\beta=0.342^\circ\pm 0.094^\circ$ ($3.6\sigma$).
**Live-state cross-check pulled this session:**
- `reproducibility/cosmology/frozen/full_tension_20260311_1728/chains/` = 176,246 total raw lines (incl. header); matches abstract "176,840" to within ~0.3 % (header rows + minor accounting).
- `reproducibility/cosmology/frozen/planck_bao_sn_20260312_1954/chains/` = 132,955 total raw lines; matches "132,949".
- `reproducibility/cosmology/frozen/` contains **only** these two combos. **No `planck_only_*` or `planck_bao_*` directory exists under `frozen/`.** The only Planck-only artifacts on disk are `reproducibility/cosmology/planck_only_live_sync/chain_{01..06}/spin_torsion.1.txt` totaling **4,264 raw lines across 6 chains** (~700 lines each, ~400 KB each). The "Planck-only ~114,992 raw samples" row of Table V (paper L480) has **no frozen artifact backing it on this filesystem**; it is two orders of magnitude smaller on disk than what the paper reports.
- `reproducibility/cosmology/convergence_latest.csv` lists 14 rows (7 parameters × 2 datasets = `full_tension` + `planck_bao_sn`); **no `planck_only` row exists**, and only **7** parameters per dataset are diagnosed, not the "all 14 sampled parameters" claimed in footnote `fn:rhat_csv`.

## Summary counts: B/M/m/n

| Severity | Count |
|---|---:|
| BLOCKER | 3 |
| MAJOR | 7 |
| MINOR | 6 |
| NIT | 4 |
| **TOTAL** | **20** |

**Most concerning finding (one sentence):** The paper's three-combo Planck-only row (Table V row 3, abstract L68, and Conclusions L532) reports "114,992 raw samples" as part of an "ongoing" frozen-corpus headline of **424,781** — yet the only on-disk Planck-only artifact is `planck_only_live_sync/` with **4,264 sample lines** total (a ~27× shortfall), and the abstract still calls the sum "424,781 samples across three dataset combinations" in a sentence that places it on equal footing with the two genuinely frozen combos; this is the same on-disk-vs-paper category-error that DeepSeek flagged in P1A tick 3 and it remains uncorrected in P1B v1B.0.3 despite §VII subsection 'Free-w0wa chain status' being the explicit anchor footnote for exactly this kind of disclosure.

---

## BLOCKERs

### B1: Planck-only "114,992 raw samples" is not present on disk; abstract/conclusion 424,781 headline is therefore unsupported (abstract L68; Table V row 3 L480; Conclusions L531)

**Quote (abstract, L67-69):** "Stock-CAMB $\Lambda$CDM$+\Delta\Neff$ MCMC proxy (Cobaya~v3.6.1, 424{,}781 samples across three dataset combinations)"

**Quote (Table V row 3, L480):** "Planck-only & 114{,}992 & $\sim$0.05 & Ongoing"

**Quote (Conclusions L531-533):** "The stock-CAMB Cobaya~v3.6.1 run (424{,}781 samples) finds $\Delta\Neff$ consistent with zero in both frozen dataset combinations"

**Quote (footnote `fn:sample_stratification` L186-193):** "\textbf{424{,}781} (abstract) is the total raw-accepted count across all three combinations. \textbf{309{,}789} is the sum of the two frozen combinations only ($176{,}840 + 132{,}949$). [...] All four numbers correspond to the same underlying chains."

**Issue:** I cannot find 114,992 Planck-only raw samples on disk. The only candidate is `reproducibility/cosmology/planck_only_live_sync/chain_{01..06}/spin_torsion.1.txt` with the following per-chain line counts: 709, 680, 679, 700, 728, 768 — **4,264 lines total**, of which ~6 are headers, so ~4,258 raw-accepted samples across all 6 Planck-only chains. The shortfall vs the paper's quoted 114,992 is **~27×**. The `paper1_clean_restart_sync/chains/dneff/planck_only/` mirror contains 458 lines total, even smaller. There is no `frozen/planck_only_*` directory under `reproducibility/cosmology/frozen/`.

Three things flow from this:

1. The abstract headline "424,781 samples across three dataset combinations" is mathematically $176{,}840 + 132{,}949 + 114{,}992$, but the third term in that sum is not real — it does not correspond to a chain on disk that has accepted that many samples. The honest current Planck-only figure is ~4,300, not 114,992. Even allowing for the chain being "ongoing", an ongoing chain at ~4,300 samples after multiple months is not what readers will infer from "114,992 raw samples" — they will infer a corpus 27× larger than what exists.

2. The footnote `fn:sample_stratification` claim "**All four numbers correspond to the same underlying chains**" is false in the Planck-only case: there is no chain on disk corresponding to the 114,992 sample number.

3. The Conclusions sentence "The stock-CAMB Cobaya~v3.6.1 run (424{,}781 samples) finds $\Delta\Neff$ consistent with zero **in both frozen dataset combinations**" is internally inconsistent: it concatenates a 3-combo total with a 2-combo verdict. The verdict applies to 309,789 samples, not to 424,781.

This is the same category of error that P1A tick 3 closed (the "‡ footnote" stale R̂−1=0.076 + ETA "1-3 days" language was rewritten outcome-agnostic per the brief). **P1B is the explicit cross-paper anchor for that footnote** (paper §VII.A subsection, L487-519). The anchor must be honest or the P1A footnote loses its backing.

**Fix:** EITHER (a) demote the abstract+Conclusions headline to **309,789 samples across two frozen dataset combinations**, mark Planck-only as "supplementary live chain, ~4,300 raw samples to date, not used in the §III $\Delta\Neff$ verdict", and update Table V row 3 status to "Live, ~4,300 raw samples, not frozen, not used in verdict"; OR (b) if the 114,992-sample Planck-only chain genuinely exists on a pod and just hasn't been mirrored to the repo, mirror it before submission and add the pod path + sha256 of the mirrored chain to the manifest. Status-quo is unacceptable: the paper is quoting a sample count that the public repository does not contain.

### B2: Footnote `fn:rhat_csv` claims "all 14 sampled parameters" satisfy $\hat R-1 < 3\times 10^{-3}$, but `convergence_latest.csv` only diagnoses 7 parameters per dataset (footnote L214-220)

**Quote (footnote `fn:rhat_csv`, L214-220):** "Sourced from \texttt{convergence\_latest.csv}: worst row is $n_s$ in the full-tension combination at $\hat{R}-1 = 9.74\times 10^{-4}$; **all 14 sampled parameters across both frozen combinations** satisfy $\hat{R}-1 < 3\times 10^{-3}$."

**Issue:** `reproducibility/cosmology/convergence_latest.csv` contains 14 rows total — but this is **7 parameters × 2 datasets**, not "14 sampled parameters." The parameters diagnosed are H0, delta_neff, omegam, ombh2, ns, tau, sigma8. Missing from the diagnostic CSV are: $A_s$ (or $\ln(10^{10}A_s)$), $\omega_c$, nuisance parameters (Planck NPIPE CamSpec calibration $A_{\rm planck}$, foreground amplitudes if marginalized internally), and any derived parameters (S_8, $\Omega_\Lambda$, $\theta_{\rm MC}$) that getdist typically diagnoses. The current footnote both (a) miscounts (says "14 sampled parameters" but the CSV has 14 *rows* = 7 params × 2 datasets), and (b) under-discloses (the actual Gelman-Rubin diagnostic only covers 7 cosmological parameters; the user has no way to confirm whether nuisance parameters or $A_s$ converged).

A reviewer at PRD or JCAP will run `getdist` on the released chains, see additional sampled parameters absent from the convergence summary, and ask why. The honest framing is "we report $\hat R-1$ for the 7 cosmological parameters $\{H_0, \Delta\Neff, \Omega_m, \omega_b h^2, n_s, \tau, \sigma_8\}$; the worst is $n_s$ in full-tension at $9.74\times 10^{-4}$." If $A_s$ or nuisance parameters are sampled, their $\hat R-1$ should be added.

**Fix:** Rewrite footnote `fn:rhat_csv` to say "all 7 cosmological parameters diagnosed in `convergence_latest.csv`" or extend the CSV to cover the actual sampled-parameter list (including $\ln(10^{10}A_s)$, $\omega_c$, and any nuisance amplitudes). Do not claim "14 sampled parameters" — that number is not in the CSV.

### B3: DESI DR2 $w_0 w_a$ row in Table V (L481) carries stale "$\sim$109 accepted" + "$>0.1$" status; the SSOT trajectory shows 9,127 samples and $\hat R-1\approx 0.0315$ at 2026-05-13 20:35 UTC

**Quote (Table V row 4, L481):** "DESI DR2 w0wa (new) & $\sim$109 accepted & $>0.1$ & Running"

**Quote (Table V caption, L470-473):** "The cobaya DESI DR2 w0wa chains (4 chains, Pod~3 H200) are in progress; convergence expected in $\sim$3 days from 2026-05-05."

**Quote (paper L487-519 §VII subsection 'Free-w0wa chain status' point (ii)):** "with $\sim 109$ samples accepted as of 2026-05-08 18:27 PT and $\hat R - 1 \approx 0.076$. Publication-quality convergence ($\hat R - 1 < 0.01$) is still 1--3 days out."

**Issue:** Per the brief, the current cobaya iter2-OMP6 state pulled at the start of this review session is $\hat R-1=0.0315$ at 2026-05-13 20:35 UTC, with ~41k samples and last progress write 8h ago. The SSOT (`project-context/SSOT/paper-1/status.md` line 66) records the trajectory more honestly: "**Honest R-1 trajectory (pulled fresh 5/11 17:33 PT)**: 0.55 → 0.20 → 0.16 → 0.12 → 0.115 → 0.079 → 0.095 ... 9,127 accepted across 4 chains, 28% acceptance ... **Honest ETA for R-1 < 0.01: 5-15 more days**." The P1A ‡ footnote was just rewritten at tick 3 (per the brief) to be **outcome-agnostic**, dropping the stale "$\hat R-1 \approx 0.076$ ... 1-3 days" language. **P1B v1B.0.3 still carries that exact stale language at L504-506 and a roughly compatible-but-also-stale "$\sim$109 accepted, $>0.1$" status in Table V row 4.**

Three load-bearing points (i)-(iii) at L491-519 (§VII anchor for the P1A ‡ footnote) depend on this status being current. As of v1B.0.3 they are not.

**Fix:** Replace L502-506 (point (ii)) with outcome-agnostic prose matching P1A tick 3: "The DESI~DR2 $w_0 w_a$-extended chain (Table~\ref{tab:mcmc_inventory} row~4) is currently running on Pod~3 H200; the chain has not yet reached publication-quality Gelman-Rubin convergence ($\hat R - 1 < 0.01$). Until that chain converges, this program has no $w_0 w_a$ posterior. The cross-paper update committed at convergence is the only place a verdict will appear." Replace Table V row 4 columns 2-3 with "in progress (not yet converged)" and remove the column-4 "Running" + caption "expected in $\sim$3 days from 2026-05-05" (the 2026-05-05 ETA is 8 days stale). Do not commit P1B to arXiv with any chain-progress number that can age out between submission and acceptance.

---

## MAJORs

### M1: NaMaster pipeline-SNR of 20.32 / 25.71 is computed without disclosing how the noise covariance was estimated (§4 L296-311)

**Quote (L296-302):** "We performed a NaMaster pseudo-$C_\ell$ analysis on the Planck Commander map with 500 MC noise realizations. Injecting the spectator-ALP fiducial $\beta=0.27^\circ$ (consistent with, but not derived from, the ECH action) recovers: $\hat\beta_{\rm NaMaster} = 0.238^\circ$ (pipeline-recovery SNR=20.32)."

**Issue:** A pipeline-recovery SNR of 20.32 = (0.238° − bias)/$\sigma_{\hat\beta,\rm MC}$ requires $\sigma_{\hat\beta,\rm MC}\sim 0.012^\circ$ — about 7.5× smaller than the published Planck/ACT $\sigma_\beta\sim 0.09^\circ$ that the paper itself adopts as the headline observational uncertainty. The paper is careful to say (L82-84, L124-127, L264-266) that this is *pipeline* SNR, not sky SNR. Good. But the methodology paragraph (L267-294) never specifies *how* $\sigma_{\hat\beta,\rm MC}$ is computed from 500 realizations. Options:
- (a) $\sigma_{\hat\beta,\rm MC}$ = std-dev of $\hat\beta$ across the 500 MC realizations — this is the legitimate sample standard deviation of the MC recovery distribution. SNR=20.32 then means the noise floor at ACT-noise level $\Delta_P=10\mu$K·arcmin gives a recovery scatter of ~$0.012^\circ$.
- (b) $\sigma_{\hat\beta,\rm MC}$ = standard error of the mean across 500 realizations (i.e., the std-dev / $\sqrt{500}$). This would give a $\sqrt{500}\approx 22.4\times$ inflated SNR purely from MC averaging and is not what a reviewer would call a meaningful detection-significance number.
- (c) An EE/EB band-power-level Fisher-information aggregation across $\ell$-bins, treating each band-power as independent.

A 20.32σ pipeline SNR is a *factor-of-7* tighter than the ACT-alone sky measurement $0.215°\pm 0.074°$ (i.e., 2.9σ at the published value). If interpretation (b) is the operative one, the SNR figures are meaningless for the reader: $\sqrt{500}$ MC averaging cannot reduce the sky-level constraining power. If interpretation (a) is operative, the noise floor at $\Delta_P=10\mu$K·arcmin and $f_{\rm sky}=0.32$ implies a single-realization sensitivity of $\sigma_\beta\approx 0.012^\circ$ on a noise-only patch — which is **5× sharper than ACT DR6** ($\sigma_\beta=0.074°$), even though the sky configuration and noise floor are explicitly chosen to be "conservative." That is a red flag: either the MC injection is on noise-only realizations (which would not yield $\hat\beta = 0.238^\circ$ near the injected value), or the band-power binning is over-counting independent modes.

**Fix:** State explicitly in the §IV methods paragraph: "We define $\sigma_{\hat\beta,\rm MC}\equiv\text{std}(\{\hat\beta_i\}_{i=1}^{500})$, the sample standard deviation of the 500 MC recoveries. The pipeline SNR is $|\hat\beta - \beta_{\rm inj}|/\sigma_{\hat\beta,\rm MC}$ — wait, that's the bias-to-scatter ratio, not a detection significance. The reader needs a one-sentence formula and a one-sentence sanity check: 'This pipeline scatter $0.012^\circ$ is smaller than the ACT DR6 sky $\sigma=0.074^\circ$ because [reason: e.g., we use the cosmic-variance-limited noise budget at $\ell\le 1024$, not the realistic ACT inverse-noise weights]'." Without this disclosure, the 20.32 number reads as either a methodological misstatement or a misleading flagship for the casual reader.

### M2: Spectator-ALP "natural parameters" claim is conditional on $C_{a\gamma}\in[4,12]$ and $m/H_0\in[1,3]$ but never justifies why those windows are "natural" (§6 L406-413)

**Quote (L406-413):** "For $C_{a\gamma}=8$, $\theta_i=1$, $m\approx 2H_0$: $\beta \approx \frac{\alpha_{\rm EM}\times 8}{4\pi}\times 1.07 \approx 0.29^\circ$. [...] The prediction spans $\beta\approx 0.17$--$0.43^\circ$ over $C_{a\gamma}\in[4,12]$, $m/H_0\in[1,3]$, $\theta_i\in[0.5,2]$, comfortably bracketing the observed value without fine-tuning."

**Issue:** The "without fine-tuning" claim is not quantified. A factor-of-3 window in $C_{a\gamma}$, a factor-of-3 window in $m/H_0$, and a factor-of-4 window in $\theta_i$ together span a ~36× volume in 3-parameter space; mapping this onto $\beta\in[0.17°, 0.43°]$ (a factor of 2.5 in $\beta$) means the predictive prior is broad. The question for a Bayesian reviewer is: what is the prior volume on $(C_{a\gamma}, m, \theta_i)$ that makes $\beta\in[0.27°-2\sigma, 0.27°+2\sigma] = [0.082°, 0.458°]$? If the model accommodates the signal over 80%+ of the prior volume, the predictive value is weak and "no fine-tuning" is essentially "any reasonable prior fits." If only 5% of the prior accommodates, the model has predictive power.

The paper does not compute this. Without it, the consistency check is asymmetric — it celebrates that the prior accommodates the data, without quantifying whether it would have *predicted* it. This is the same Bayesian-evidence-vs-fit-quality distinction that the paper is careful about elsewhere (§5 explicitly demotes Savage-Dickey to "indicative" because of $r=-0.89$ correlation, L362-365). The same rigor should apply here.

**Fix:** Either (a) compute a one-sentence prior-volume estimate: "The fraction of $(C_{a\gamma}, m, \theta_i)$ prior volume yielding $\beta$ within 2σ of the Eskilt+2022b value is $\sim X\%$"; or (b) drop "without fine-tuning" and replace with "consistent with"; or (c) add a one-sentence caveat: "we do not claim predictive power; the ALP class accommodates the signal for a range of natural parameters." Currently the abstract (L86-88) and §VI conclusion (L548-552) both use "without fine-tuning" as if it were quantitative.

### M3: Quintom-B "theoretical accommodation" is asserted but never substantiated against the actual frozen MCMC posteriors (§VII point (iii) L509-519)

**Quote (L513-518):** "the asymmetry between the Quintom-B accommodation row (which carries an unmarked ``consistent$^\dagger$'' on theoretical grounds because Quintom-B is the only class admitted to span the dynamical-equation-of-state window the DESI signal populates~\cite{DESI2025DR2}) and the rest of the rows is intentionally one of \emph{theoretical accommodation, not of fit quality measured in this program}."

**Issue:** "Quintom-B is the only class admitted to span the dynamical-equation-of-state window" is a definitional claim, not a falsifiable one. The asymmetric privileged-row treatment in P1A Table~II is therefore based on an assertion: "the model that is allowed to cross $w=-1$ is the model that accommodates a $w$-crossing signal." This is a tautology unless paired with (a) a quantitative comparison of which Quintom-B parameter region maps onto the DESI 95 % CL $(w_0, w_a)$ contour, and (b) some demonstration that the *competing* bounce classes (matter bounce, Cuscuton, ekpyrotic) cannot reproduce the DESI signal under any equation-of-state mapping.

The "rest of the rows" are labeled "not tested" — fine and honest — but the privileged row should be subject to the same evidentiary standard. Currently the asymmetry rests on a theory-vs-data argument without showing the data. CLAUDE.md (project file, lines 73-77) explicitly flags this: "earlier 'quintom-B at 98.6%' bookkeeping was fire-#21 confabulation, corrected fire #25." The current P1B language has retreated from "98.6%" to "theoretical accommodation" — good — but the retreat leaves an unjustified asymmetric checkmark in the table.

**Fix:** Add one of: (a) a footnote in P1B §VII (and matching footnote in P1A Table II) citing the specific Quintom-B parameter window that maps onto the DESI 95 % CL, OR (b) demote the Quintom-B row to "not tested" pending the DR2 chain converging, matching the rest of the table; the current "consistent$^\dagger$ on theoretical grounds" is neither tested nor falsifiable as written.

### M4: ALP MCMC "9,720 total accepted samples" reported with $\hat R-1<0.01$ but acceptance fraction, autocorrelation time, and sampler are not disclosed (§VI L426-433)

**Quote (L426-433):** "Dedicated MCMC sampling of the ALP parameter space (3 configurations, 9{,}720 total accepted samples) yields: $\beta_{\rm ALP} = 0.336^\circ\pm 0.107^\circ$ ($C_{a\gamma}=8$ fixed), [...] Convergence: $\hat{R}-1 < 0.01$ for all runs."

**Issue:** 9,720 samples across 3 configurations = ~3,240 samples per configuration. For Cobaya/emcee with default settings, an autocorrelation time of $\tau_{\rm ac}\sim 100$ steps would imply effective sample sizes of ~30 per parameter per config — below the standard ESS > 400 threshold that Gelman/Vehtari recommend for 1σ posterior moment quotes. The reported uncertainty $\sigma(\beta_{\rm ALP})=0.107^\circ$ is computed from these ~30 effective samples per chain unless the autocorrelation is much shorter. Without disclosing $\tau_{\rm ac}$, the reader cannot assess whether $0.107^\circ$ is the true posterior 1σ or MC noise on the posterior 1σ.

Additionally, the paper does not specify which sampler is used (emcee? Cobaya MH? PolyChord/MultiNest?). Cobaya v3.6.1 supports all three; their convergence behaviors differ. For a 2D parameter space $(C_{a\gamma}, \theta_i)$ this is a minor issue — but the paper is *also* quoting $C_{a\gamma}\times\theta_i = 3.4\pm 1.1$ (line 432) as a moment, which is only well-defined if the joint chain is well-mixed.

**Fix:** Add one sentence: "ALP MCMC was run with Cobaya's [sampler], 3 chains × 3,240 samples, with acceptance fraction $f_{\rm acc}=X$ and autocorrelation time $\tau_{\rm ac}=Y$ giving effective sample size $N_{\rm eff}=Z$ per configuration." This is a standard disclosure for any MCMC-derived 1σ quote.

### M5: Bayesian evidence vs parameter-shift framing is inconsistent between abstract, §5, and Conclusions (abstract L73-76, §V L348-374, Conclusions L538)

**Quote (abstract L73-76):** "this run uses stock CAMB with $\Delta\Neff$ as a free parameter and carries \emph{no torsion modifications to the Boltzmann equations}; it is reported as a null-consistency test"

**Quote (§5 L348-357):** "$\Delta\text{AIC}=-5.9$ favors $\Lambda$CDM$+\Delta\Neff$ on Akaike grounds, while the $\Delta$BIC of $-0.7$ is below the Kass-Raftery threshold of $|\Delta\text{BIC}|<2$. Together these metrics are mildly favorable but not decisive."

**Quote (Conclusions L537-539):** "the AIC/BIC differences ($\Delta$AIC$=-5.9$, $\Delta$BIC$=-0.7$) are the primary cross-references."

**Issue:** The paper is a "null-consistency test" (abstract), but Table III (L341-345) bolds $\Lambda$CDM$+\Delta\Neff$ as the best-fitting model with $\Delta\chi^2_{\rm eff}=-7.9$ and Conclusions calls $\Delta$AIC/$\Delta$BIC the "primary cross-references" as if they were evidentiary outputs. If the inferential frame is "null-consistency" (i.e., is $\Delta\Neff$ consistent with zero?), the relevant statistic is the marginal posterior $P(\Delta\Neff = 0 | \text{data})$, not $\Delta$AIC across nested models. AIC/BIC test whether the *extension* improves fit — they answer a different question. Quoting both styles together without unifying them creates the kind of "spaghetti inference" Gelman warns against: the reader is left choosing which framework wins (Bayesian posterior, frequentist AIC, Bayes factor).

The Savage-Dickey $\ln B=+4.8$ is correctly demoted to "indicative" (footnote `fn:bayes_caveat` L361-365) because of the $r=-0.89$ correlation between $\Delta\Neff$ and $H_0$. Good. But the AIC/BIC numbers face an analogous concern: $\Delta\chi^2_{\rm eff}=-7.9$ for one extra parameter on a tension dataset is the standard signature of a parameter absorbing SH0ES tension, *not* of a real physical degree of freedom. The §V text acknowledges this ("emerges only when SH0ES-driven tension data are included") — but then Conclusions promotes AIC/BIC back to "primary cross-references." Pick one frame: either the paper makes a posterior consistency statement ($\Delta\Neff=-0.020\pm 0.169$, consistent with zero), or it makes a model-comparison statement (AIC favors the extension on tension data only). Doing both blurs the inference.

**Fix:** In Conclusions, state explicitly: "The primary inferential output of this proxy MCMC is the posterior on $\Delta\Neff$, which is consistent with zero in both frozen datasets. The AIC/BIC differences are reported as standard diagnostics but are not the headline; the $\Delta$AIC $=-5.9$ on the SH0ES-included dataset reflects the well-known degeneracy between $\Delta\Neff$ and $H_0$ in tension data, not a physical preference for the extension."

### M6: NaMaster mask product / apodization scale is specified but the underlying mask file is not version-pinned (§4 L267-295)

**Quote (L277-279):** "The mask uses $C_2$ apodization at $2^\circ$ scale."

**Quote (L292-294):** "Full driver script, mask, MC seeds, and binning specification are in \texttt{pipelines/h200\_results/pod1\_namaster\_umap\_2026-04-29/}."

**Issue:** The methods paragraph specifies the apodization scale and $f_{\rm sky}=0.32$ but does not say which mask product (Planck SMICA, GAL080, GAL060, common-mask, lensing-mask, etc.) is being apodized. $f_{\rm sky}=0.32$ is unusually low for a CMB B-mode analysis (Planck typically uses $f_{\rm sky}=0.6$–$0.7$ for E/B; ACT DR6 uses $f_{\rm sky}=0.4$). A factor-of-2 smaller sky area should give $\sqrt{2}\times$ larger statistical error, which is part of why the pipeline SNR question (M1) matters. Specifying the underlying mask + apodization recipe completely is needed for the reproducibility manifest. Pointing to a pipeline directory is necessary but not sufficient — the abstract reader needs the mask name.

**Fix:** Add to L277-279: "We use the Planck [SMICA/Commander/GAL080] $f_{\rm sky}=0.32$ Galactic + point-source mask, apodized with $C_2$ at $2^\circ$." If the mask is custom, name the procedure ("the union of GAL060 with a 1° apodized point-source mask at >100 mJy").

### M7: ALP equation-of-motion integration result $\Delta\phi/f_a \approx 0.65$ is reported without specifying the integration range, the initial-velocity choice, or convergence tolerance (§6 L397-404)

**Quote (L398-404):** "Numerical integration of the ALP equation of motion $\ddot\phi + 3H\dot\phi + m^2 f_a\sin(\phi/f_a) = 0$ in a $\Lambda$CDM background yields the field displacement from recombination to today: $\Delta\phi/f_a \approx 0.65 \quad (m = H_0,\; \theta_i = 1)$."

**Issue:** The numerical integration uses an unspecified ODE solver, unspecified tolerance, unspecified initial velocity $\dot\phi(z_{\rm rec})$, and unspecified background $H(z)$ source (Planck 2018? Same as the MCMC posterior?). For an under-damped oscillator with $m\sim H_0$, the integration is sensitive to the initial-velocity choice and to whether the ALP is frozen or oscillating at recombination. The "natural" choice $\dot\phi(z_{\rm rec}) = 0$ is fine but should be stated. Otherwise the $\beta\approx 0.29°$ derivation (L406-409) cannot be reproduced.

**Fix:** One sentence: "We solve the ALP equation of motion with initial conditions $\theta_i = \phi(z_{\rm rec})/f_a = 1, \dot\phi(z_{\rm rec}) = 0$ in the Planck 2018 $\Lambda$CDM background, using [scipy.solve_ivp / RK45, rtol=1e-8]." Cross-reference to the reproducibility appendix.

---

## MINORs

### m1: Abstract sample-count phrasing "424,781 samples across three dataset combinations" reads as if all three are frozen (L67-69)

The abstract says "424,781 samples across three dataset combinations" without qualifying that only two are frozen. The §III text (L181-184) corrects this — "plus an ongoing Planck-only run (114,992 raw samples)" — but the abstract reader will infer three frozen combos. Add "(two frozen, one ongoing)" parenthetical.

### m2: Inconsistent "424,781" vs "424,181" historical artifact

CLAUDE.md line 51 records: "Paper 1 abstract canonical figure: 176,840 + 132,949 + 114,992 = 424,781; supersedes earlier 424,181 arithmetic mismatch corrected fire #25". The current paper does use 424,781 consistently — but only if the Planck-only 114,992 stands (see B1). If B1 is closed by demoting Planck-only, the headline becomes 309,789 and the 424,781 mention vanishes.

### m3: Footnote `fn:bayes_caveat` (L361-365) is excellent — but the same caveat should apply to the "$+4.8$" appearing in Table III (L343) and in the abstract `\ln B = +4.8` if it were quoted there. Currently Table III bolds the $\ln B = +4.8$ row without inline caveat.

Add a daggered footnote on Table III's $\ln B$ column header: "Savage-Dickey estimate, biased at $r=-0.89$ between $\Delta\Neff$ and $H_0$; see footnote `fn:bayes_caveat`."

### m4: "$\Omega_k$ is fixed to zero (mandated by 92 $e$-folds of post-bounce inflation)" (L156-158)

This claim is true in the matter-bounce scenario but is paper-internal-circular: $\Omega_k = 0$ is then *not* a data-driven constraint of this proxy MCMC, it is a prior. The verification cannot test $\Omega_k$ because $\Omega_k$ is fixed by the bounce model. State explicitly: "We impose $\Omega_k = 0$ as a prior in all runs; this is not a posterior result."

### m5: §III "$\sigma_8 = 0.785 \pm 0.016$" historical claim (L160) is reported but the cited "original MCMC analysis" is not bibliographically anchored

The L160 sentence references an unidentified "original MCMC analysis (which included the SH0ES $H_0$ prior)." Was this Cobaya v3.5 from `arxiv/main.tex` v2.x? Add a cite or "(Paper~I(a) v2.2.0, superseded by the v3.6.1 verification chains in this companion; see Sec.~\ref{sec:verification})."

### m6: Cobaya version inconsistency — abstract says "Cobaya v3.6.1", §V.A says "Cobaya v3.5 original; v3.6.1 verification" (L324)

L324: "Parameter estimation uses Cobaya~\cite{Cobaya2021} (v3.5 original; v3.6.1 verification) with stock CAMB."

This is honest — but the abstract and Conclusions only quote v3.6.1. Either drop the "v3.5 original" reference (since the v3.6.1 run is the operative one), or add "v3.5 chains superseded; v3.6.1 is the headline." Otherwise the reader wonders whether some of Table III is v3.5 and some is v3.6.1.

---

## NITs

### n1: "$N_{\rm side}=512$, $\ell_{\rm max}=1024$" (abstract L78) vs §IV "$\ell_{\min}=30$ to $\ell_{\max}=1024$" (L283)

The abstract gives $\ell_{\max}=1024$ for $N_{\rm side}=512$, which is the standard $2\,N_{\rm side}$ Nyquist limit. Good. Add a sentence that the choice is Nyquist-limited (so the reader knows there's no $\ell_{\max}$ tuning).

### n2: $C_{a\gamma}\times\theta_i = 3.4 \pm 1.1$ (§VI L432) — units missing

State that $C_{a\gamma}$ is the dimensionless chiral anomaly coefficient and $\theta_i$ is dimensionless. The product is dimensionless. As written a non-cosmology reader might infer mismatched units.

### n3: "the published Planck/ACT DR6 $2.4$--$2.9\sigma$" (L82, L127, L265-266, L546)

This range appears four times. Consider citing the source range once and cross-referencing. Currently the reader sees the range repeatedly without seeing which paper gives 2.4 and which gives 2.9.

### n4: `paperTimestamp` macro (L47) is "2026-05-09 17:00 PDT" but `\date` (L61) is "May 8, 2026, 21:30 PDT"

Two timestamps that disagree by ~20 hours. Pick one and rebuild. This is the same `\paperTimestamp` staleness issue the P1A scorecard flagged (P1A SSOT L175: "set 2026-04-13 — refresh to compile date on next build").

---

## Cross-paper coordination check

**P1A ‡ footnote anchor (brief item 7):** The brief asks whether "three load-bearing points (i)-(iii) anchoring P1A ‡ footnote — are these still in P1B §VII subsection 'Free-w0wa chain status'?" — YES, they are at L491-519. **However**, point (ii) at L502-506 still carries the stale "$\sim 109$ samples accepted as of 2026-05-08 18:27 PT and $\hat R - 1 \approx 0.076$. Publication-quality convergence ... is still 1--3 days out." This is the same stale language that P1A tick 3 just rewrote outcome-agnostic. If P1A footnote ‡ now reads outcome-agnostic but P1B §VII still carries stale numbers, the cross-paper anchor is broken — P1A ‡ would cite P1B for a number P1B no longer agrees with. **B3 must close before P1A and P1B can be submitted together.**

**P3 / P4 cross-refs (L141-143):** P1B cites `Golden2026P2` (Paper 2 SPHEREx Fisher), `Golden2026P3` (anomaly catalog), `Golden2026P4` (chirality catalog). Per P1A SSOT line 18-19, these cross-paper bibitems were added Wave 14-JJJJ to `arxiv/references.bib`. P1B inherits these via the shared `.bib`. Confirm at recompile that all four cross-paper cites resolve cleanly (no `[?]`).

**Bibliography:** P1B uses the shared `arxiv/references.bib` (no separate `paper1b_mcmc_companionNotes.bib` is loaded). Per P1A SSOT, `Alonso2019` (NaMaster), `WilsonEwing2012`, `Agazie:2023ng15`, and the `Eskilt2022b` fix from P1A tick 3 are all in `references.bib`. P1B should compile cleanly against this. **Verify at next recompile** that `Eskilt2022b`, `Eskilt2022`, `DiegoPalazuelos2025`, `Fujita2021`, `LiteBIRD2023`, `ECTorsionDESI2025`, `DESI2025DR2`, `Cobaya2021`, `Planck2018params`, `DESI2024`, `Riess2022`, `DES2024`, `Walmsley2022` all resolve.

---

## Summary

P1B v1B.0.3 has the right scope discipline (proxy framing throughout, NaMaster as pipeline-validation not sky-detection, ALP as consistency not prediction). The three load-bearing scope statements at L116-135 ("Not a spin-torsion theory module / Not a competitive sky detection / Not a distinctive ECH prediction") are excellent and should not be touched. The text is much closer to publication-ready than the historic v2.x prose.

The three BLOCKERs are all in the same category: **the paper quotes numbers that don't match the on-disk live state**. B1 (114,992 Planck-only samples don't exist on disk) and B3 (DESI w0wa chain status is 8 days stale) are both **honesty-of-sample-count** issues and both need to close before submission. B2 (footnote `fn:rhat_csv` "14 sampled parameters" miscount) is smaller but in the same category — the convergence diagnostic does not cover what the footnote claims.

If those three close, the seven MAJORs are all defensible-with-one-sentence-fixes: most are missing methodological specifications (NaMaster $\sigma_{\hat\beta,\rm MC}$ definition, ALP MCMC sampler/autocorrelation, mask product name, ODE solver tolerance) that a reviewer will demand and that the paper has the information for, it just hasn't been written down.

The headline most-concerning finding is B1 (Planck-only sample-count category error) because it propagates into the abstract, Conclusions, and Table V row 3, *and* because it undermines the §VII subsection that anchors the P1A ‡ footnote at the cross-paper level. Close B1 + B3 together as a coordinated edit with P1A.

**Recommendation:** Do not submit P1B until the three BLOCKERs close and the abstract sample-count headline is honest. Once those close, MAJORs M1-M7 should land as a single text-edit wave (~2-3 hours combined). MINORs and NITs are cleanup-on-recompile.
