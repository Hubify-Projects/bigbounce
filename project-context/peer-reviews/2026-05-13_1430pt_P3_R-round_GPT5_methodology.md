# P3 R-round — Adversarial Statistical-Methodology Review (Simulated OpenAI GPT-5, Gelman/Vehtari profile)

**Reviewer profile:** GPT-5 adversarial, statistical methodology (Gelman/Vehtari lens).
**Target:** `pipelines/p3_anomaly_engine/paper3_draft.tex` — Paper 3 v3.1.37 (May 10, 2026), 1,134 lines, title "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches."
**SSOT cross-check:** `project-context/SSOT/paper-3/status.md` read for R41–R43 closure history and R42 Wave 14-RR / Wave 14-X / Wave 14-II / Wave 14-NNN / Wave 14-VVV / Wave 14-KKKK context.
**Round number:** This is the next external R-round after R44 (the R45 self-review + cross-vendor non-Anthropic round + Houston sign-off all listed as pending in SSOT line 49).
**Date:** 2026-05-13 14:30 PT.

---

## Total counts

| Severity | Count |
|---|---|
| **B** (Blocker — must resolve before arXiv) | **1** |
| **M** (Major — methodology defect, fix before submission) | **5** |
| **m** (Minor — precision/framing, fix on next pass) | **6** |
| **n** (Nit — wording/cross-ref/typo) | **4** |

---

## Most concerning finding (one-line)

> **B1 (Blocker, §VI NANOGrav, L557 & App A L949).** The "Bayes factor BF(bounce/SMBHB) ≈ 2.2×10⁴" claim is a Δχ² likelihood ratio computed under a Gaussian approximation around the posterior mean, **not** a Bayes factor. The prior-volume integral over (γ, log10A) is required for a real Bayes factor and is not performed; the quoted ">4σ-equivalent" headline is methodology-misstated and will not survive PRD referee scrutiny.

---

## B — Blockers (1 finding)

### B1. The "Bayes factor 2.2×10⁴ / >4σ-equivalent" headline in §VI is not a Bayes factor (L557, App A L949)

**Quote (L557):** *"Bayes factor BF(bounce/SMBHB) = exp[-(Δχ²_bounce − Δχ²_SMBHB)/2] = exp(20.03/2) = exp(10.0) ≈ 2.2×10⁴. The matter-bounce hypothesis is therefore favored over the softened-SMBHB hypothesis at >4σ-equivalent strength on the present 15-yr KDE-likelihood data set, with the caveat that this Bayes factor is computed under the Gaussian-posterior approximation around γ_obs and assumes equal model priors."*

**Defect.** What is written is a *profile-likelihood ratio* at the two point hypotheses γ=3.0 and γ=4.33 under a Gaussian approximation centered on γ_obs=2.567. A Bayes factor in the model-comparison sense requires marginalizing the marginal likelihoods of two competing models over their parameter spaces (here at minimum γ AND log10A AND any noise/pulsar-model nuisance parameters), each with its declared prior. Both candidate templates are *power-law GWBs with fixed γ but free log10A* — so the marginalization over log10A is non-trivial and the prior-volume penalties for the two models are not identical even though the flat prior is the same. The "assumes equal model priors" disclaimer does not patch this; the issue is that the *parameter*-level marginal likelihoods, not the prior probabilities of the models, have not been computed.

A defensible statement is one of:
- (a) "The likelihood ratio at the maximum-likelihood points is exp(10.0) ≈ 2.2×10⁴, equivalent to a Δχ² = 20.03 frequentist test," OR
- (b) Compute a real BF via thermodynamic integration / nested sampling / Savage-Dickey on the existing emcee chain (the chain at `chain_real_freespec.npy` 5.1 MB has both γ and log10A; Savage-Dickey at a fixed γ-slice plus a 1D integral over log10A is ~10 lines of numpy).

**The ">4σ-equivalent strength" claim** rests on the Bayes-factor framing. If the statement is downgraded to "likelihood ratio at the MLE points," the ">4σ" should be reworded to "Δχ² = 20.03 between SMBHB and bounce templates at fixed γ; the matter-bounce template is favored by a likelihood-ratio of 2.2×10⁴ at the MLE points pending a full marginal-likelihood model comparison."

This finding also affects §VI conclusion item 5 at L633, where the same Bayes-factor framing is implied by "matter-bounce favored by the smaller deviation," and the Implications paragraph at L614.

**Severity:** Blocker, because PRD statisticians (and any referee with a Gelman/Vehtari lens) will reject the BF claim outright; the fix is either a one-paragraph re-wording (option a) or a 1-hour script (option b). Both are cheap.

---

## M — Majors (5 findings)

### M1. The Δσ/Δα linearity used to translate the α-CI into a σ(f_NL) envelope is unstated and unverified (§V L550, §V.B and Abstract)

**Quote (L550):** *"mapping the 95% confidence interval α ∈ [-1.08, +1.46] through the linear-in-α Fisher scaling gives σ(f_NL) ∈ [~5.91, ~12.92]."*

**Defect.** The Fisher information for f_NL scales with the *square* of the high-bias-tracer bias (through b_φ ∝ (b−1) for the standard scale-dependent bias), not linearly in α. A "linear-in-α scaling" is at best a tangent-line approximation around α=0.15, and even that requires explicit specification. The headline σ(f_NL) = 8.27 ± 2.37 carries a symmetric error that is then *also* propagated through the same linearity to produce the asymmetric [5.91, 12.92] 95% envelope — but the asymmetry is inherited from the α-CI asymmetry, not from any Jacobian computation. At α = −1.08 (lower CI) the bias-enhancement factor (1+α) = −0.08 is **negative**, which is unphysical (it implies the QSO-candidate population has a *negative* bias, i.e., anti-clustered with respect to the field). The Fisher pipeline should explicitly truncate α ≥ −1 (the physical floor) and recompute the lower-tail σ(f_NL).

**Fix.** State the b_φ functional form used, give the Jacobian ∂σ(f_NL)/∂α explicitly at α=0.19, truncate at α ≥ −1, and re-report the asymmetric 95% envelope. A 1-page methods appendix would close this.

### M2. The internal-Fisher σ(f_NL) ≈ 0.07–0.12 number is reported alongside Heinrich+2024 σ(f_NL) ≈ 0.7 with insufficient guardrails for a casual reader (§V L550, Abstract L54, §I L71)

**Quote (L71):** *"…at 3–5σ realistic significance under the multi-tracer methodology of Heinrich et al. [Heinrich2023] (anchored to the Heinrich+2024 σ(f_NL) ≈ 0.7 bispectrum-only forecast as the headline external benchmark; an internal Fisher diagnostic computation gives σ(f_NL) ≈ 0.07–0.12 under specific cross-tracer correlation kernel assumptions, 3–10× tighter than the Münchmeyer et al. [Munchmeyer2019] consensus σ(f_NL) ≈ 0.4–0.9 for SPHEREx-class surveys, and is held aside as an internal-consistency check pending an auditable cross-tracer covariance release — it is not used as the headline forecast)."*

**Defect.** A factor-of-10 gap between the internal Fisher and the Münchmeyer consensus is too large to be characterized as "an internal-consistency check." A consistency check is something that *agrees* with the consensus; this disagrees by 3–10×, and the paper's own framing concedes this is because cross-tracer correlations are not damped by realistic photo-z kernels and magnification-bias coupling is treated at linear order. That is not "internal consistency" — it is a known systematic under-estimate of the Fisher uncertainty. A reader who scans the abstract or §I quickly will see "0.07–0.12" and forget the parenthetical caveat.

**Fix.** Either (a) drop the 0.07–0.12 numerical range from the abstract and §I entirely (keep it in §V only as a methodology comparison), or (b) prefix it with "uncorrected Fisher information" rather than "internal Fisher diagnostic." The current framing reads as if the 0.07–0.12 is a real forecast that just happens to be too optimistic; the truth is the Fisher is over-determined.

### M3. The bibliography on Heinrich is cited variously as "Heinrich2023" and "Heinrich+2024" in the same paragraph (§I L71, §V L550, §VI L614)

**Quote (L71):** *"…the multi-tracer methodology of Heinrich et al. [Heinrich2023]…anchored to the Heinrich+2024 σ(f_NL) ≈ 0.7 bispectrum-only forecast…"*

**Defect.** The citation key is `Heinrich2023` (consistent with the bibliography), but the prose alternates between "Heinrich et al. (2023)" and "Heinrich+2024" — apparently the same paper in two different years. Either the paper is Heinrich 2023 (in which case all "+2024" mentions are typos) or there is a separate Heinrich 2024 reference that is not in the bibliography. Pulling the bibitem and checking the year is a 30-second fix; failing to do so will be the first thing a PRD copy-editor flags.

**Fix.** Pick one year, propagate.

### M4. The σ(f_NL)^{GS} = 2.28 ± 7.43 "central 74% improvement" framing in the abstract is misleading because the central improvement is consistent with no improvement *and* with much larger improvement (Abstract L54, §V.B L550, §VII L633)

**Quote (Abstract L54):** *"A high-confidence-restricted Path-B re-measurement on the 1,122-object Gold+Silver subset (Wave 14-KKKK) yields α_{GS,jk} = +1.83 ± 2.03 (σfnl^{GS} = 2.28 ± 7.43, consistent with zero at 0.90σ); the central value is 9.6× higher as an α-ratio…"*

**Defect.** A measurement with ±326% fractional uncertainty cannot honestly anchor a "central 74% improvement" narrative. The 1σ envelope on the GS forecast σ(f_NL) ∈ [−5.15, +9.71] **straddles σ(f_NL) = 0** (i.e., zero variance, perfect measurement, which is unphysical) on the lower side and exceeds the baseline σ(f_NL)=8.98 on the upper side. The asymmetric envelope hides the fact that the negative-α branch of the CI is at α=−1.83−2σ ≈ −5.9, which would predict the Gold+Silver tracers are *strongly anti-correlated* with the bulk anomaly population — clearly nonsensical. The paper acknowledges this at §V "consistent with no improvement at <1σ" but the abstract leads with "9.6× higher" as if the *ratio* is the headline result, which it isn't (the ratio is dominated by the small α_full ≈ 0.19 denominator, not by genuine Gold+Silver clustering).

**Fix.** Lead the abstract sentence with the *uncertainty* — e.g., "the Gold+Silver high-confidence subset yields α_{GS,jk} = +1.83 ± 2.03 (1σ jackknife), with the σ(f_NL) forecast consistent with no improvement over the standard DESI QSO baseline at <1σ." Move the "9.6× α-ratio" framing to §V where the per-bin context is available.

### M5. The "17.8% novelty rate" Wave 14-EEEEE forward-closure reframe is consistent across abstract, §VII.6 limitations, and conclusion item 2, but the framing is still confused about which sample stratum the 17.8% applies to (Abstract L54, §VII.6 L583, §VIII item 2 L627)

**Quote (Abstract L54):** *"Extended archival cross-matching of the top-1,000 DESI anomalies against NED, VizieR, and 20 all-sky catalogs yields a genuine novelty fraction of ~17.8% (objects absent from all major catalogs). This is a single-sample point estimate measured at the top-1,000 score stratum; the full-catalog rate is empirically untested in the present analysis (the converse hypothesis -- that highest-scored objects are bright cataloged outliers more easily matched to existing catalogs, in which case the full-catalog novelty would be higher than 17.8% -- is at least equally plausible a priori). A score-stratified novelty measurement on quintiles of the top-1,000 DESI anomalies is the natural follow-up."*

**Quote (§VII.6 L583):** *"…approximately 17.8% for the DESI top-1,000 measured directly, far below the 58.8% SIMBAD-unmatched headline. We report 17.8% as a single-sample point estimate measured at the top-1,000 score stratum and explicitly do not claim it as an upper bound, lower bound, or floor on the full-catalog novelty fraction."*

**Quote (§VIII item 2 L627):** *"a genuine novelty fraction of approximately 17.8% as a single-sample point estimate at the top-1,000 DESI score stratum (no upper- or lower-bound status assigned; §VII.6)."*

**Defect.** The reframing is *consistent across the three locations* (good — the Wave 14-EEEEE close worked) but the framing itself is statistically self-undermining. Reporting a point estimate with the disclaimer "the true value could be higher OR lower, we have no evidence" is not a useful scientific claim. The right response is either:
- (a) Stratify the top-1,000 into quintiles (200 each) and report novelty(q1)…novelty(q5) with binomial error bars, which would resolve whether the rate is monotonic in score; this is ~30 minutes of CDS X-Match work given the cross-match has already been done, OR
- (b) Demote 17.8% from the abstract entirely; report only "the top-1,000 DESI anomalies have 178 objects absent from 20 major catalogs (17.8%); the full-catalog rate is not measured here." The current phrasing of "primary catalog novelty figure" in the abstract is in tension with "single-sample point estimate, no bound status."

The natural follow-up (a) is one paragraph and one figure in §V.A. This should land before submission.

---

## m — Minors (6 findings)

### m1. PTA sample size discrepancy: paper says emcee 32×10,000 = 320,000 samples (App A L939), SSOT line 17 says "134k post-burn samples," prompt asks "what sample size?" (App A L939, L951)

**Quote (App A L939):** *"emcee.EnsembleSampler [Foreman-Mackey2013] with 32 walkers, 10,000 production iterations, 2,500 burn-in."*
**Quote (App A L951):** *"Chain (chain_real_freespec.npy, 5.1 MB, 320,000 × 2 float64)…"*

**Defect.** 32 × 10,000 = 320,000 post-burn samples (consistent with the 5.1 MB chain size for 2 float64 columns = 5,120,000 bytes ≈ 5.1 MB ✓). The arithmetic is right. But the SSOT Wave 14-RR entry (line 17) describes a *different run* — `nanograv_improved_analysis.py` on 6 signal-dominated free-spectrum bins, 32×6000 steps, 30% burn-in, 134k post-burn samples, headline γ = 3.201 ± 0.420. That is the historical "γ = 3.20 ± 0.42" lineage referenced in the prompt and in CLAUDE.md, not the run reported in the paper.

The paper's current §VI / App A reports a *third* run: 30 Fourier-frequency bins (the full Zenodo 8060824 KDE), 32×10,000, γ = 2.567 ± 0.382. This is fine on its own merits, but the SSOT must be updated to reflect that γ = 3.20 ± 0.42 is now a *superseded internal-draft synthetic-power-law fit*, and γ = 2.567 ± 0.382 is the paper headline. The prompt-stated and CLAUDE.md-stated headline γ = 3.20 ± 0.42 / 0.48σ-from-bounce is **stale** — the paper now reports γ = 2.567 ± 0.382 and bounce at **+1.13σ** above the posterior mean.

**Fix.** The paper itself acknowledges this in §VI L557 ("This real-likelihood result supersedes the synthetic-from-power-law summary-statistic fit (γ = 3.20 ± 0.42)…"). The remaining work is: (i) SSOT/index.md headline and CLAUDE.md project-level highlights both still quote γ = 3.20 ± 0.42 as the canonical figure; both should be flipped to γ = 2.567 ± 0.382 / bounce at +1.13σ. The prompt's question "verify the Fisher recompute v2b math: σ(γ) = 0.42 on what sample size? what likelihood?" is therefore answered by **the paper no longer uses σ(γ) = 0.42 as the headline**; the v2b Fisher lineage is preserved only as a "what we used to report" caveat at L557 and L949.

### m2. The Fisher v2b recompute (Wave 14-II) is described as Path A "FULL HARD FIX" of P3-CM-M1, but the §V text in the paper still presents *both* paths (Wave 14-R cheap-fast caveat AND Wave 14-II quantitative recompute) (§V L550)

**Quote (§V L550):** *"…We have also computed a multi-tracer Fisher matrix including a 4n+1-dimensional nuisance-parameter block…After full marginalization, σ(f_NL) floors to 0.067–0.116…This internal-Fisher floor is held aside as an internal-consistency check pending an auditable cross-tracer covariance release and is NOT used as the headline forecast for this paper."*

**Defect.** Stacking the cheap-fast caveat AND the FULL HARD FIX in §V is defensible as an audit-trail mechanism (per SSOT Wave 14-II commentary at line 19), but the §V opener reads as if there are *three* sequential reframes (Wave 14-O α-dependence, Wave 14-R zero-systematic caveat, Wave 14-II quantitative recompute) without a unifying single statement of "here is what we now claim." A reader trying to extract the methodological state has to integrate three italic blocks plus a fourth one (Wave 14-VVV empirical α) plus the legacy fixed-α=0.15 retention. This is hard to follow.

**Fix.** Add a one-sentence "Bottom line" anchor at the start of §V that states: "We measure α = 0.19 ± 0.65 directly (Wave 14-VVV) and propagate this through the multi-tracer Fisher with full systematics marginalization (Wave 14-II); the resulting σ(f_NL) = 8.27 ± 2.37 is the headline forecast, with σ(f_NL) ≈ 0.07–0.12 from the unmarginalized Fisher and the σ(f_NL) ≈ 0.7 Heinrich+2024 bispectrum-only anchor reported alongside for comparison." Then let the four italic blocks function as detail. Right now the four blocks land before the headline forecast and the reader has to back-compute it.

### m3. The "Path-C unique" rate column in Table I (1.01%) is computed against 37,272,042 (ACT-excluded scored total), not against 37,292,042 (the cross-transfer baseline) — but the rate label is just "Rate (%)" with no denominator stated (Table I row "Path-C unique (primary)" L206)

**Quote (Table I L206):** *"Path-C unique (primary) … 37,272,042 … 378,280 … 1.01 … --- … 7-way dedup at 5″, ACT excluded; 378,080 pt-src + 200 Planck."*

**Defect.** 378,280 / 37,272,042 = 1.015% (rounds to 1.01% ✓). But the denominator switched from the cross-transfer baseline 37,292,042 to the ACT-excluded 37,272,042 inside the same table without an inline note. The other column ("Total (cross-transfer baseline, ACT-incl. archival)") uses 37,292,042 / 319,443 = 0.857% (rounds to 0.86%). Both arithmetic checks pass, but a reader scanning the table sees two different denominators in adjacent rows without explanation.

**Fix.** Add an inline parenthetical to the Path-C row: "Rate computed against ACT-excluded scored total 37,272,042."

### m4. The "internal-Fisher floor σ(f_NL) ≈ 0.07–0.12 is 3–10× tighter than Münchmeyer+2019 consensus 0.4–0.9" claim has a factor inconsistency (§I L71, §V L550)

**Quote (§I L71):** *"3–10× tighter than the Münchmeyer et al. [Munchmeyer2019] consensus σ(f_NL) ≈ 0.4–0.9."*

**Defect.** Tightest internal Fisher 0.067 vs. tightest Münchmeyer 0.4 → 5.97× tighter (≈6×). Loosest internal Fisher 0.116 vs. loosest Münchmeyer 0.9 → 7.76× tighter (≈8×). Tightest internal Fisher 0.067 vs. loosest Münchmeyer 0.9 → 13× tighter. Loosest internal Fisher 0.116 vs. tightest Münchmeyer 0.4 → 3.45× tighter (≈3.5×). The "3–10× tighter" range is therefore a hand-wave over an actual 3.5–13× span; the lower bound rounds down to 3 (defensible) but the upper bound should be 13, not 10.

**Fix.** Use "~3.5–13× tighter" or "of order 10× tighter."

### m5. The "0.06σ" agreement claim between empirical α=0.19 and fiducial α=0.15 in the abstract is mathematically correct but rhetorically over-stated (Abstract L54, §VII.4 L583)

**Quote (Abstract L54):** *"The empirical α is statistically consistent with zero at 0.29σ from null and consistent with the prior fiducial α = 0.15 at only 0.06σ (the empirical-to-fiducial gap is ~1/16 of the jackknife dispersion, so the agreement is far tighter than 'within 1σ' would suggest)."*

**Defect.** |0.19 − 0.15| / 0.65 = 0.0615 ✓. But this is a "two numbers within 1/16 of the noise" coincidence, not a measurement that constrains α — the fiducial 0.15 was a *guess*, and the empirical 0.19 ± 0.65 *does not constrain α at all* (it is consistent with zero at 0.29σ). Bragging about "0.06σ agreement with the fiducial" is the wrong rhetorical move — it makes the measurement sound much more precise than it is. The correct framing is "the prior fiducial 0.15 was a guess; the measurement at 0.19 ± 0.65 is consistent with the guess but cannot rule out α=0 or α=1; tighter measurements are needed."

**Fix.** Drop the "0.06σ" framing from the abstract; keep "consistent with zero at 0.29σ" and "95% CI [−1.08, +1.46]" as the load-bearing numbers.

### m6. The Pipeline-1 1.58× clustering bias claim in the abstract and §V refers to a "random-baseline" comparison that the paper does not define (Abstract L54, §V L550)

**Quote (Abstract L54):** *"The shift direction (toward the bounce prediction) is consistent with the Pipeline-1 1.58× clustering-bias enhancement observed independently on the same Gold+Silver subset against a random-baseline benchmark."*

**Defect.** "Random-baseline benchmark" is undefined in the paper. The on-disk artifact `pipelines/p1_highz_tracers/outputs/step4_bias_validation/bias_validation.json` confirms the 1.58× figure (`relative_bias_vs_baseline = 1.5819`) but the JSON metadata explicitly flags itself as **"Preliminary — uses uniform randoms, not DESI survey window function"**. The paper does not pass this caveat through; the abstract makes 1.58× sound like a validated cross-survey measurement when it is actually a uniform-randoms benchmark that the JSON itself disclaims as preliminary.

Note also that the Wave 14-KKKK Path-B re-measurement on the same Gold+Silver subset gives b_GS/b_full = 2.83 ± 2.03 (jackknife) or 3.17 (per-bin geomean) — these are 1.79× to 2.0× larger than the 1.58× Pipeline-1 number. The paper at §V L550 acknowledges this internally ("Gold+Silver tracers are more strongly biased than the full QSO-candidate pool, consistent with the 1.58× random-baseline comparison originally reported") but does not reconcile the 1.58× → 2.83× shift.

**Fix.** Either (a) note that 1.58× is a uniform-randoms preliminary number whose successor at Wave 14-KKKK is 2.83 ± 2.03 with proper jackknife, OR (b) drop the 1.58× from the abstract; keep it in §V with the appropriate caveat.

---

## n — Nits (4 findings)

### n1. Title length

The title is 24 words across three lines: *"Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches."* This is at the upper end of revtex4-2 title length and will be hard to fit on submission-system landing pages. Consider trimming to "A Multi-Survey Catalog of 378,280 Anomalies from 37.3 Million Sources" + subtitle.

### n2. Abstract length

The abstract is ~1,400 words / one solid paragraph; PRD typical is ~250 words. The Path-C strata, the α calibration, the high-confidence re-measurement, and the systematics-marginalization story all belong in the abstract, but the current density makes it unreadable in the abstract preview surfaces. Consider a 4-sentence headline + 4-sentence detail split.

### n3. Stale "ACT~DR6 is documented only in Appendix" cross-reference

L73 (Introduction) cites `\ref{sec:act_appendix}` but the canonical paper structure puts ACT under §III ("ACT DR6 (formally quarantined…)" subsection, L411) labelled `\label{sec:act}`, not under an `\label{sec:act_appendix}`. Verify that `sec:act_appendix` resolves; if not, fix the cross-reference.

### n4. The §VI conclusion item 4 ("Cross-survey validation") states "637-cluster multi-survey 5″-coincidence manifest" but the §IV.3 Cross-Survey Matches text states "All 637 are pairwise; no triple coincidences appear at 5″" — consistent, but item 4 doesn't make the "all pairwise, no triples" point and a reader of the conclusions alone won't know (L631)

A one-clause addition to item 4 would close this.

---

## Item-by-item response to prompt focus questions

| # | Focus question | Verdict |
|---|---|---|
| 1 | 17.8% novelty rate framing consistent across abstract / §limitations / Conclusions item 6 | **PASS** (covered in M5 — framing is consistent but rhetorically incomplete; quintile stratification recommended) |
| 2 | γ_PTA = 3.20 ± 0.42 Fisher recompute v2b math | **STALE PROMPT** (covered in m1 — paper now uses γ = 2.567 ± 0.382 from the 30-bin Zenodo KDE-likelihood; γ = 3.20 ± 0.42 is explicitly superseded at L557. SSOT/CLAUDE.md highlights need a downstream sync.) |
| 3 | Tier arithmetic 37,292,042 / 319,443; per-survey breakdown | **PASS** — verified independently: 195,829+77,905+298+44,075+200+200+436+500 = 319,443 ✓; scored total 37,292,042 = sum of all 8 per-survey scored counts ✓; Path-C 388,493 - 10,213 dedup = 378,280 ✓; pt-src 378,280 - 200 Planck = 378,080 ✓; ACT-excluded scored 37,292,042 - 20,000 ACT = 37,272,042 ✓ |
| 4 | AUC values DESI DR1 AE/IF/IF-cal stages | **NOT IN PAPER** — `grep -c "AUC"` on paper3_draft.tex returns 0. The AUC values referenced in CLAUDE.md (FRB CHIME AUC=0.997, GW echo LIGO AUC=0.975, ZTF light curve AUC) belong to *other* sub-pipelines, not Paper 3. Paper 3 uses Jaccard stability (J̄=0.862 for 5-fold DESI; J̄=0.7320 prod-vs-control 100K Jaccard) and injection-recovery fractions, not AUC. Prompt focus item is misframed for this paper. |
| 5 | eROSITA top-cut policy 298 (BigAE top-cut) vs 9,303 (top-1% IF placeholder) | **PASS** — disclosed in §III.4 (L383, "the published anomaly set as the 298 sources with S > 0.259 … score threshold is data-driven rather than a manually chosen round number"), Table I footnote § (L214, "the 9,303-object reference set is the top-1% IF cross-validation pool, distinct from the 298-source published catalog headline"), §VII.5 caveat (v) (L598). Consistently disclosed across abstract / §III / Table I / §VII. |
| 6 | ACT-quarantine policy 378,280 (no ACT) vs 378,480 (with ACT); R47-M2 fix verification | **PASS** — Table I row "Path-C unique (primary)" reports 378,280 (ACT excluded), the §III.6 ACT subsection explicitly flags ACT as "formally quarantined" with both gate criteria failed (L412), the §II.4 Step 6 description distinguishes "canonical 7-way" from "8-way-with-ACT sensitivity check producing 378,480 unique objects" (L164), the §Acknowledgments Data availability paragraph (L651) names both `pathc_unique_objects_no_act.parquet` (378,280, canonical) and `pathc_unique_objects.parquet` (378,480, sensitivity-only). The 8-way-with-ACT variant produces +200 by construction because ACT contributed zero positional overlaps at 5″ — arithmetically and provenance-consistently stated. |
| 7 | Pipeline-1 cross-survey holdout validation methodology | **PARTIAL** — the paper describes a 5-fold *cross-fold* validation on the DESI 47K training pool (J̄=0.862; §II.B paragraph "In-sample scoring and held-out validation" L119, §VII.5 caveat (i) L590) AND a 103K-spectrum SPARCL holdout production-vs-control ensemble (J̄_prod×ctrl=0.7320 vs J̄_ctrl×ctrl=0.8738; §VII.5 (i) L590). There is no separate *cross-survey* holdout — the Pipeline-1 Gold+Silver clustering analysis is reported separately as the Wave 14-VVV / Wave 14-KKKK empirical α measurement (§V L550), but the question "was the Pipeline-1 cross-survey holdout described" — there is no such holdout in the paper, only the in-DESI k-fold and SPARCL holdout. If the prompt intended "cross-survey holdout," the answer is "not applicable; the paper validates on within-survey holdouts only." |
| 8 | bias_validation.json 1.58× — does it match on-disk artifact? | **PASS but stale wording** — artifact at `pipelines/p1_highz_tracers/outputs/step4_bias_validation/bias_validation.json` line 220 reads `"relative_bias_vs_baseline": 1.5819284884179885`, which rounds to 1.58 ✓. **However**, the JSON metadata explicitly flags the run as "Preliminary — uses uniform randoms, not DESI survey window function." The Abstract L54 sentence does NOT propagate this caveat. See m6 above. Also note the paper's primary headline is now the Wave 14-VVV / Wave 14-KKKK Landy-Szalay measurement (α_jk = 0.19 ± 0.65 full sample; b_GS/b_full = 2.83 ± 2.03 jackknife on Gold+Silver), which *supersedes* the 1.58× number; the paper retains 1.58× only as a side-cross-check at §V L550. |
| 9 | Independent vs dependent anomaly counts; multi-survey overlap discussion | **PASS** — the §IV.3 Cross-Survey Matches subsection (L509) explicitly enumerates 637 multi-survey coincidences at 5″ across 388,493 detections (the dedup compression rate is 2.6%, which the paper interprets as "different survey pipelines are flagging fundamentally distinct anomaly populations… with minimal redundancy at matched sky positions"). The 378,280 unique-object headline accounts for the overlap; the 388,493 sum-over-surveys is preserved as the pre-dedup detection count. The §IV.1 "Expected false-match rates" paragraph (L477) bounds random-coincidence contamination to <2% of the 637 multi-survey clusters. The treatment is methodologically correct. |
| 10 | 17.8% claim — specifically tied to top-1,000 DESI score stratum? | **PASS** — abstract L54 says "Extended archival cross-matching of the top-1,000 DESI anomalies"; §V.A "Archival cross-match and genuine novelty fraction" L471 says "a cross-match of the DESI DR1 top-1,000 anomalies (ranked by score) against 20 curated all-sky catalogs via CDS X-Match … yields an archival-ID rate of 82.2% (822/1,000). The residual 17.8% (178/1,000) constitutes the candidate genuinely novel population"; §VII.6 limitations L583 says "approximately 17.8% for the DESI top-1,000 measured directly"; §VIII Conclusions item 2 L627 says "a genuine novelty fraction of approximately 17.8% as a single-sample point estimate at the top-1,000 DESI score stratum." All four locations are consistently scoped to DESI top-1,000. **The 17.8% is NOT a cross-survey claim; it is DESI-only.** Good. |

---

## Overall verdict

**Recommendation:** **Major revisions before submission.** 1 Blocker + 5 Majors + 6 Minors + 4 Nits = 16 findings total. The Blocker (B1, Bayes-factor framing) is a 1-paragraph fix or a 1-hour script. The Majors are about precision of statistical claims, not about the underlying science, which is sound. The 17.8% reframe (M5) and the σ(f_NL)^{GS} framing (M4) are the highest-priority Major fixes for honest reporting.

The headline science (378,280 unique anomalies, Path-C native-retrain methodology, multi-survey 5″ dedup, native vs cross-transfer before/after, 17.8% genuine novelty at top-1,000 with explicit no-bound-status disclaimer) is methodologically defensible and matches the on-disk artifacts. The arithmetic chain (319,443 cross-transfer baseline → 388,493 Path-C raw → 378,280 7-way dedup → 378,080 point-source + 200 CMB-patch stratification → 378,480 8-way-with-ACT sensitivity check) is internally consistent and independently verifiable.

The PTA spectral-index lineage (synthetic γ=3.20±0.42 → KDE γ=2.567±0.382, bounce at +1.13σ) is correctly stated in the paper but is **stale in SSOT/CLAUDE.md/prompt headline language**; this is a sync-downstream issue, not a paper-content issue.

**Cap-lifting eligibility:** Under the 99% cap rule (Houston sign-off + clean external R-round with zero MAJOR/MINOR), this round does NOT close the cap — 5 Majors are open and at least 2 of those (B1 Bayes factor; M5 17.8% framing follow-up) require substantive work, not text-only edits. P3 readiness should hold at 88–95% until B1 is fixed and at least M4+M5 land. The 6 Minors and 4 Nits can ride a subsequent text-only sweep.

---

## Companion artifact pointer

This review file: `project-context/peer-reviews/2026-05-13_1430pt_P3_R-round_GPT5_methodology.md`.
Suggested SSOT/queue.md row: `P3-GPT5-R45-B1 Bayes factor methodology B; P3-GPT5-R45-M1..M5 Majors; P3-GPT5-R45-m1..m6 Minors; P3-GPT5-R45-n1..n4 Nits.`
Suggested companion JSON: `pipelines/p3_anomaly_engine/r45_results/gpt5_methodology_findings.json` (to be created on close-out).
