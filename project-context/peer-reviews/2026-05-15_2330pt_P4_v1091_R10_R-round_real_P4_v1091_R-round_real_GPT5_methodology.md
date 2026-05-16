# P4_v1091 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_2330pt_P4_v1091_R10_R-round_real
**Wall time**: 65.2s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=81213, completion=4364, reasoning=3106, total=85577

---

## PAPER-GPT-B1 — BLOCKER — Conflicting dipole significances on same catalog

**Section/Table:** §Edge-On Galaxy Contamination, Table `face_on`; §Dipole Analysis; Conclusions.  
**Issue:** Table `face_on` reports **Catalog C full** dipole significance **+4.31σ** under a monopole-preserving null, while the headline real-space dipole is **+0.43σ** on Catalog C. The “different estimator” explanation is not acceptable: two dipole estimators on the same data with nulls that both preserve the monopole cannot differ by a factor of 10 in σ without one estimator/null being invalid or measuring a different statistic.  
**Fix:** Either remove the +4.31σ table result until reconciled, or explicitly define it as non-dipole / mask-leakage statistic and show simulations proving why it is not a dipole detection. The headline null cannot stand while this contradiction remains.

## PAPER-GPT-B2 — MAJOR — 0.5% sensitivity-floor regression and inconsistent injection probabilities

**Section/Table:** §Motloch; §Sensitivity; Conclusions item 1.  
**Issue:** The paper still states an empirical systematic-inclusive threshold of “∼0.5%” in Conclusions and “≳0.5%” in §Motloch, contradicting the stated canonical **0.75% 50%-recovery-at-3σ threshold**. Conclusions also says at **A=0.5%**, `P(σ>3)=0.03`, while Table `mc_injection` gives **0.15**. It also says `P(σ>3)=0.50` at 0.75%, while the table gives **0.55**.  
**Fix:** Replace every threshold/floor claim with **0.75% full-amplitude empirical 50%-recovery-3σ threshold**. Keep **0.5% only as a tested non-detection point with P(σ>3)=0.15**. Correct all conclusion/table prose to match Table `mc_injection`.

## PAPER-GPT-B3 — MAJOR — ell_eff=4 bandpower is still conflated with the ell=1 dipole

**Section/Table:** §Dipole Analysis after Table III; Conclusions “Headline finding”; §Systematic Dipole.  
**Issue:** The text still says the lowest bandpower centered at **ell_eff=4**, spanning **ell=[2,6]**, is followed by `C_1^{meas}=1.494e-6`, and Conclusions says a raw pseudo-`C_l` at **ell=1** collapses to **−0.12σ** “once MASTER is applied on the same data.” That is false: the pre-MASTER **ell_eff=4 asymmetry-map bandpower**, the monopole-only **CW-fraction-map ell=1**, and the post-MASTER **subsample-mask ell=1** result differ in map, mask, monopole treatment, and estimator.  
**Fix:** Never label the ell_eff=4 `[2,6]` bandpower as `C_1` or as an ell=1 dipole estimator. Rewrite all collapse language as “different diagnostic stages,” not “same-data MASTER collapse.”

## PAPER-GPT-B4 — MAJOR — HC-spiral sample counts are internally inconsistent

**Section/Table:** §Confidence Stratification; Table `confidence_bins`; Table `face_on`; §Bin-flatness.  
**Issue:** The high-confidence spiral count is given as **949,584** for `max(p_CW,p_CCW)>0.6`, but Table `confidence_bins` sums the bins above 0.6 to **193,560 + 131,364 + 619,902 = 944,826**, a discrepancy of **4,758**. §Confidence also says the “broader HC-broad” cut is spiral-only but “counts confident-NS galaxies,” which is self-contradictory.  
**Fix:** Define exactly one `HC-spiral-0.6` selection and make every table/artifact use the same Boolean cut. If Table `confidence_bins` excludes objects below 0.4 or uses a different confidence variable, state that explicitly and add the missing bin/count.

## PAPER-GPT-B5 — MAJOR — Hemisphere LEE interpretation remains statistically incoherent

**Section/Table:** Abstract; §Hemisphere; Fig. `hemisphere`; §Hemisphere Discussion; Conclusions.  
**Issue:** The abstract says the hemisphere statistic rejects the random-label null at **p_LEE ≤ 10⁻⁴**, then says Bonferroni/BH drops it to **<1σ consistent with null**. These are not two comparable corrections to the same statistic; one is a direct max-statistic MC and the other is an analytic independent-bin bound under a different null. Presenting both as “post-LEE” verdicts is misleading.  
**Fix:** Make the direct-MC max-statistic result the sole primary LEE statement. Move Bonferroni/BH to a clearly labeled non-primary sanity bound, or remove it from the abstract.

## PAPER-GPT-B6 — MAJOR — TTA bias cancellation is overclaimed and mathematically false

**Section:** §Systematic Dipole.  
**Issue:** The paper says equivariant averaging “eliminates the real-space systematic by construction,” “cancels to machine precision,” and that the soft chirality score averages to zero per galaxy. Eq. (TTA) does not imply `p_CW^eq = p_CCW^eq` per galaxy, and the paper’s own residual **9.5σ monopole** proves hard-label bias is not canceled.  
**Fix:** Replace “by construction / machine precision / per-galaxy zero” with the empirical claim actually supported: TTA suppresses the measured real-space dipole from **2.31σ to 0.43σ** while leaving a nonzero uniform monopole.
