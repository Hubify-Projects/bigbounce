# P4_v1070_R R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_0735pt
**Wall time**: 115.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=63235, completion=6365, reasoning=5178, total=69600

---

## PAPER-GPT-B1 — BLOCKER — §Monopole+Mask Leakage Null; §Conclusions canonical-$N$ MASTER

**Issue:** The monopole+mask generative null does **not** support the leakage interpretation: Table `monopole_mask_null` reports data at `+5.88σ` pre-MASTER and hemisphere max at `+6.62σ` **against** the monopole-only null, i.e. the null is rejected, not reproduced. The residual `+1.85σ` canonical post-MASTER value is not cosmological evidence by itself, but the paper cannot claim the monopole-only null “formalizes” the leakage explanation.

**Fix:** Re-run with the monopole fitted/marginalized/deprojected explicitly, include/deproject the $\ell=0$ template in MASTER, and use a systematics-preserving null including depth/PSF/morphology; until then, call the canonical-mask excess an unresolved mask/systematics residual, not a demonstrated monopole-leakage floor.

## PAPER-GPT-B2 — BLOCKER — §Sensitivity Floor; Table `mc_injection`; Conclusions item 1

**Issue:** The empirical injection recovery does not establish a “$0.5\%$ at $3σ$” sensitivity floor: at injected $A=0.5\%$, the table gives median significance `0.68` and `P(σ>2)=0.18`, with no $P(σ>3)$ crossing and no 50% recovery at any tested amplitude. The run also uses a reduced HC subsample and synthetic Bernoulli relabeling, so it is not a systematic-inclusive full-catalog floor.

**Fix:** State only “empirical threshold is $>0.5\%$ and unmeasured by this sweep,” or extend injections until the 50% recovery criterion is crossed, preferably on the full catalog with observed classifier/systematics structure preserved; keep the Fisher full-amplitude floor consistently as $\sim0.29\%$ before mask/$N_{\rm eff}$ inflation.

## PAPER-GPT-M1 — MAJOR — §Edge-On Galaxy Contamination; Table `face_on`

**Issue:** The face-on/HC robustness comparison is not like-for-like. The “monopole-preserving” null is described as preserving full-catalog $p_{\rm CW}=0.4974$, while the HC subsamples have different monopoles (`0.49606`, `0.49602`), so the null is mis-centered for the subsamples; the claimed `+4.31σ → +0.62σ` collapse is also against a different null than the paper’s isotropic-$p=0.5$ headline.

**Fix:** For each subsample, either fit/marginalize its own monopole or report both nulls consistently; remove the collapse claim unless the same estimator/null/cut is used throughout, and disambiguate the conflicting HC sample definitions/numbers.

## PAPER-GPT-M2 — MAJOR — §Dipole Analysis; Table `multipole`; §NaMaster MASTER configuration

**Issue:** The load-bearing `-0.12σ` MASTER result is not cleanly comparable to the canonical `+1.85σ` result: masks, $f_{\rm sky}$, apodization, pixel counts, and effective galaxy counts differ, and the “subsample mask” count `5,547,858` is not reconciled with the canonical `3,201,160` spirals. The paper effectively privileges the mask/method configuration giving the null without a single canonical, consistently defined primary estimator.

**Fix:** Define one primary NaMaster analysis with fixed catalog, map normalization, mask, apodization, binning, and null; demote all alternate masks to robustness tests and give a normalization/units reconciliation for the factor-scale difference between the quoted $C_1$ values.

## PAPER-GPT-M3 — MAJOR — §Hemisphere Asymmetry; Fig. `hemisphere`; Table `monopole_mask_null`

**Issue:** Hemisphere statistics are internally inconsistent: the text quotes `0.17%`, the footnote/figure quote full amplitude `0.853%`, and Table `monopole_mask_null` gives `1.48×10^{-3}`. The Bonferroni/BH discussion says the signal is consistent with null, while the direct MC gives `p_LEE ≤ 10^{-4}`, which rejects the random-label null; the paper then incorrectly treats the monopole-only null as reproducing the effect despite `+6.62σ`.

**Fix:** Define one hemisphere statistic and unit, use it consistently, and state plainly that random-label and monopole-only nulls are rejected; only a systematics-preserving null can justify the systematic-artifact interpretation.

## PAPER-GPT-m1 — minor — Bibliography / float formatting

**Issue:** `Walmsley:2023GZDESI` and `Walmsley:2023` duplicate the same paper; `Shamir:2022DESI` lacks final journal metadata and the manuscript contradicts itself on the comparator sample size (“nearly $1.3\times10^6$ spirals” vs “~200,000 spirals out of ~1.3M total”). The promoted `table*` floats have very long captions/notes under REVTeX `[!htb]`, which is likely to create float-stack/page-break drift.

**Fix:** Merge duplicate Walmsley entries, complete Shamir metadata, use one Shamir sample-size statement, and compile-check the four wide tables in two-column mode; shorten captions or move long interpretive notes to text if floats stack.
