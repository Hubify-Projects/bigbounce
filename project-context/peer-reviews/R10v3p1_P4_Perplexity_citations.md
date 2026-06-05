# P4 R10v3p1 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (24776 chars)
**Wall time**: 58.1s

---

**The paper is not citation-clean and does not meet PRD standards in its current form.** There are multiple hard failures: at least one reference entry is internally malformed, several load-bearing numerical claims are not traceable to the cited or displayed data, and the manuscript repeatedly blurs primary results with appendix-systematics in a way that is not publication-ready for a rigorous cosmology methods paper.

- **P4-E1 — Bibliography entry  is malformed / incomplete**  
  **Section:** References, p. 10  
  **Problem:** The entry ends mid-sentence: “` J. Hou, Z. Slepian, and R. N. Cahn, “Measurement of parity-odd modes in the large-scale 4-point correlation function of SDSS BOSS DR12 CMASS and LOWZ galaxies,” Mon. Not. R. Astron. Soc. 522, 5701 (2023),`” and then the next line abruptly continues with the search-result-style fragment “`arXiv:2206.03625.`” This is not a valid bibliography record as rendered.  
  **Required fix:** Restore the full citation formatting for  and verify author list, title, journal, year, volume, page, and arXiv identifier against ADS/arXiv.

- **P4-E2 — The paper states a “parity-odd analog” incorrectly in the abstract**  
  **Section:** Abstract, p. 1  
  **Problem:** “`the parity-odd analog requires 3D spin-vector or polarization-rotation cross-correlation observables outside this paper’s scope`” is presented as a general statement, but the paper later cites parity-odd 4PCF work and cosmic birefringence literature in the references, and the statement is not properly qualified. More importantly, the manuscript’s own framework is about projected morphology chirality, not a demonstrated theorem about all parity-odd observables.  
  **Required fix:** Rephrase as a scope statement tied specifically to this analysis, not a universal claim about parity-odd cosmological observables.

- **P4-M1 — The abstract quotes multiple σ values that are not consistently mapped to their nulls in the body**  
  **Section:** Abstract, p. 1  
  **Problem:** The abstract gives “`−0.122σ`,” “`+0.43σ`,” “`+3.64σ`,” and “`+3.57σ`” in close proximity, each under different null procedures, but the mapping is easy to lose and not always repeated at every juxtaposition in the body. The paper itself warns that these σ values are not directly comparable, but then repeatedly places them side-by-side in a way that can mislead.  
  **Required fix:** Add explicit null labels at every occurrence in the abstract and main text, or restructure to avoid adjacent incomparable σ values.

- **P4-E3 — Table I mixes estimators with incompatible definitions without sufficient formal separation**  
  **Section:** Table I, p. 4  
  **Problem:** The table reports “`real-space dipole`,” “`MASTER deconv`,” “`canonical MASTER`,” “`hemisphere LEE (MC)`,” “`monopole+mask null`,” and “`injection floor`” in one list, but these are not the same kind of quantity. Some are measured significances, some are p-value limits, and one is a sensitivity threshold.  
  **Required fix:** Split the table into separate tables by statistic class, or add a strict legend with units, null type, and interpretation constraints.

- **P4-E4 — Table II uncertainty formula is not transparently consistent with the reported numbers**  
  **Section:** Table II, p. 4  
  **Problem:** The table says uncertainties are binomial with \( \sigma=\sqrt{p(1-p)/N} \) and \(N=3{,}201{,}160\), but the printed values are internally inconsistent with the displayed significances if interpreted naively. For example, for \(p=0.4974\), the binomial deviation from 0.5 is about \(-0.0026\), which at this \(N\) does correspond to roughly \(-9.5\sigma\); however the table labels the “Dev. (σ)” column as 9.5 without clarifying sign convention, while the main text later calls this a “`9.5σ` CW-fraction monopole.”  
  **Required fix:** Define the sign convention explicitly and make the direction of the deviation unambiguous in the table header.

- **P4-M2 — Table III’s bandpower significance values are not reproducible from the displayed \(C_\ell\) and \(\sigma\) numbers as presented**  
  **Section:** Table III, p. 5  
  **Problem:** Example: for \(\ell=1\), \(C_\ell=1.494\times10^{-6}\) and \(\sigma_\ell=0.429\times10^{-6}\) gives \(1.494/0.429\approx3.48\), but the table reports “`−0.122`,” which only makes sense if a nonzero null mean is subtracted. The table does not show the null mean in the table itself, so the significance cannot be recomputed from the displayed row alone. Similar opacity affects the other rows.  
  **Required fix:** Include the null mean in the table or state explicitly that the significance is \((C_\ell-\langle C_\ell\rangle)/\sigma\) with numerical values shown.

- **P4-M3 — Table IV’s “99.3% reproduced” claim is not adequately documented in the displayed numbers**  
  **Section:** Table IV and Sec. IV D, pp. 5–6  
  **Problem:** The text states the monopole-only null reproduces “`99.3% of the observed pre-MASTER pseudo-Cℓ power`,” but the displayed data are \(1.696\times10^{-2}\) and \((1.685\pm0.007)\times10^{-2}\). This is close, but the paper never shows the exact formula used to obtain 99.3%, and the quoted percentage is a derived quantity that should be explicitly reproducible from the table.  
  **Required fix:** Add the exact computation, including whether the ratio is of means, medians, or an observed-minus-null residual percentage.

- **P4-E5 — The manuscript repeatedly labels canonical-mask residuals as “systematics” based on interpretation, not proof**  
  **Section:** Abstract, Sec. IV D, Sec. VI, pp. 1, 5–6  
  **Problem:** Phrases such as “`is not interpreted as a cosmological signal`,” “`systematics-attributed`,” and “`most likely explanation`” are conclusions, not established facts from the displayed analyses. The paper does not provide a definitive causal proof that the canonical-mask residual is systematic rather than cosmological.  
  **Required fix:** Downgrade these claims to evidence-based interpretation and separate them from demonstrated results.

- **P4-M4 — “Falsification criterion” is overstated relative to the evidence shown**  
  **Section:** Abstract and Discussion, pp. 1, 6  
  **Problem:** “`A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% ... would falsify the present null`” is too strong because the threshold is pipeline-dependent and tied to a specific null model and classifier architecture.  
  **Required fix:** State the criterion as conditional on the current pipeline, training regime, and mask treatment.

- **P4-M5 — The manuscript uses “null” and “detection” language inconsistently**  
  **Section:** Abstract, Results, Conclusions, pp. 1, 4–6  
  **Problem:** The paper calls the \(-0.122\sigma\) result the “headline scientific result,” while also emphasizing the \(+3.64\sigma\) canonical-mask residual and the \(+3.57\sigma\) apodized result. This creates ambiguity over which statistic is primary and which are diagnostics.  
  **Required fix:** Explicitly designate the primary estimator and relegate diagnostics to a separate subsection with clear status labels.

- **P4-M6 — Claims about “not directly comparable” σ values are not enforced consistently enough**  
  **Section:** Abstract, Results, Discussion, pp. 1, 4–6  
  **Problem:** The manuscript states, “`σ values throughout this paper ... are not directly comparable across estimators`,” but then compares them repeatedly, e.g. “`+3.64σ`” versus “`−0.122σ`” and “`+3.57σ`” versus “`+3.64σ`.” Without repeating the caveat at every juxtaposition, this remains easy to misread.  
  **Required fix:** Add per-claim qualifiers or avoid comparative language between heterogeneous σ metrics.

- **P4-M7 — The citation to Shamir (2012) is incomplete relative to the claim being made**  
  **Section:** Introduction and Reference [4], pp. 2, 10  
  **Problem:** The paper attributes “`2–4σ dipole with per-bin asymmetry amplitudes of ∼ 5–20%`” to Shamir (2012) and later uses “`∼ 3%`” as a benchmark. The cited title and venue are correct in spirit, but the manuscript does not show that the quoted range is extracted from the cited paper’s abstract/tables rather than a secondary interpretation.  
  **Required fix:** Quote the exact abstract/table values from the source paper or soften the numerical summary.

- **P4-M8 — The citation to Iye et al. (2021) is used for a claim that is stronger than the reference as presented**  
  **Section:** Introduction and Comparison, pp. 2, 5  
  **Problem:** The paper states that Iye et al. “`found no significant dipole after correcting for reading-direction bias and photometric-object duplication`.” The cited paper’s title is about dipole analysis with 3D random walk simulations; the manuscript’s paraphrase may be correct, but it is not directly traceable from the citation entry alone.  
  **Required fix:** Provide the specific result location in the cited paper or reduce the claim to what is explicitly documented.

- **P4-M9 — The “CE-ResNet” citation appears broadly correct, but the manuscript overstates comparability**  
  **Section:** Introduction, Comparison, p. 2 and p. 5  
  **Problem:** “`cw/ccw = 0.998 on ∼ 1.95 million galaxies`” is quoted for Jia et al. and then compared directly to this work’s 0.4974 fraction. That comparison is not apples-to-apples unless the same label convention and preprocessing are shown to match.  
  **Required fix:** Explain the matching conventions and preprocessing, or limit comparison to the scale of the datasets.

- **P4-M10 — Table/figure numbering is absent; the paper is difficult to audit**  
  **Section:** Throughout  
  **Problem:** The manuscript refers to “Table I/II/III/IV/V” but no figures are present in the provided text, and several key claims are said to be supported by appendices rather than primary figures. For a PRD submission, the evidentiary chain is too text-heavy and too diffuse.  
  **Required fix:** Add figures for the principal estimators, masks, and null distributions, and ensure all referenced diagnostics are visually checkable.

- **P4-M11 — Reference  is incomplete as rendered**  
  **Section:** References, p. 10  
  **Problem:** The DESI Collaboration entry reads “`arXiv:1611.00036 (2016)`” without a journal or final venue. That may be acceptable only if the paper is a preprint entry, but the bibliography format is inconsistent with other entries and should be standardized.  
  **Required fix:** Either cite the final journal version if available or explicitly format it as a preprint reference.

- **P4-M12 — Reference  is incomplete as rendered**  
  **Section:** References, p. 10  
  **Problem:** “`C. R. Harris, K. J. Millman, S. J. van der Walt et al., Nature 585, 357 (2020).`” omits the article title and DOI. While this is a software citation, the format is inconsistent with the rest of the bibliography.  
  **Required fix:** Standardize the software citations and verify the exact bibliographic metadata.

- **P4-M13 — Reference  is not in standard journal format**  
  **Section:** References, p. 10  
  **Problem:** “`R. Wightman, PyTorch Image Models (2019), https://github.com/...`” is a software repository citation, not a conventional paper reference. This is acceptable only if the journal style allows it, but it should be formatted consistently.  
  **Required fix:** Either provide the canonical citation for timm or format it uniformly as software.

- **P4-M14 — Several numerical claims are unsupported by visible calculations**
  **Section:** Results, Discussion, Appendices, pp. 4–9  
  **Problem:** Claims such as “`3.86× asymmetry-suppression factor`,” “`25% of the observed canonical-mask ℓ = 1 amplitude`,” “`14.7×` inflation,” and “`zboot ≈ −18`” are presented without enough intermediate arithmetic in the rendered text to verify them.  
  **Required fix:** Add explicit derivations or compact calculation lines for every quoted factor and \(z\)-score.

- **P4-M15 — The manuscript overclaims novelty with “largest galaxy chirality catalog to date”**  
  **Section:** Conclusions, p. 7  
  **Problem:** The statement “`We have constructed and analyzed the largest galaxy chirality catalog to date`” is a priority claim that is not substantiated against all relevant prior catalogs in the text. The paper mentions CE-ResNet and Galaxy Zoo DESI, but not a systematic comparison against all chirality catalogs.  
  **Required fix:** Either document the comparison basis or soften to a qualified statement.

- **P4-M16 — Duplicate / near-duplicate content across abstract, introduction, and conclusions**  
  **Section:** pp. 1–7  
  **Problem:** The same core claims about the \(-0.122\sigma\) result, the \(+3.64\sigma\) canonical residual, and the leakage interpretation are repeated multiple times with small wording changes. This is not a physics error, but it reduces clarity and makes the evidentiary hierarchy harder to audit.  
  **Required fix:** Consolidate repeated claims and reserve detailed interpretation for the Results and Discussion sections.

- **P4-M17 — Internal bookkeeping language appears in the body**  
  **Section:** Multiple locations, especially Abstract, Sec. IV D, Appendix D  
  **Problem:** Phrases such as “`headline scientific result`,” “`non-headline`,” “`previous paper versions`,” and “`operational conclusion`” are manuscript-management language, not standard scientific prose.  
  **Required fix:** Replace with neutral scientific phrasing.

- **P4-M18 — The paper is overly long relative to the stated contribution**  
  **Section:** Entire manuscript, 10 pages plus dense appendices  
  **Problem:** For a methods paper whose main contribution is a null chirality result with leakage diagnostics, the body is overloaded with systematic sub-analyses, appendix cross-checks, and multiple comparative narratives. The claimed contribution would be better served in a shorter, tighter paper.  
  **Required fix:** Recommended maximum length: about 7–8 pages of main text, with only essential diagnostics retained in appendices.

- **P4-M19 — Appendix B equation (B1) is notationally ambiguous**  
  **Section:** Appendix B, p. 7  
  **Problem:** In \(L = L_{\mathrm{CE}} + \lambda \cdot \frac{1}{N}\sum_i \|p(x_i)-S\,p(\tilde{x}_i)\|^2\), the text defines \(S\) as a swap of CW and CCW channels “leaving not spiral unchanged,” but the dimensionality and exact action of \(S\) on the 3-class output are not explicitly shown.  
  **Required fix:** Write \(S\) as an explicit 3×3 permutation matrix and verify channel ordering.

- **P4-M20 — Appendix A field definition has inconsistent monopole-subtraction language**  
  **Section:** Appendix A, p. 7  
  **Problem:** The appendix says the headline estimator uses the “`monopole-subtracted CW-deficit map`,” then later says the monopole-mask leakage channel uses an input field “`constructed WITHOUT monopole subtraction`.” That distinction is scientifically important but not cleanly separated in notation.  
  **Required fix:** Use distinct symbols for the two fields and define both explicitly at first use.

- **P4-M21 — The claimed “null dipole at sub-percent sensitivity” is too strong without a formal survey-selection model**  
  **Section:** Abstract, Discussion, Conclusions, pp. 1, 6–7  
  **Problem:** The paper infers a null isotropy-breaking dipole from two estimators, but the sensitivity floor is explicitly limited by classification noise, edge-on contamination, and mask leakage. A “sub-percent sensitivity” claim is only valid within this pipeline, not as an intrinsic property of the dataset.  
  **Required fix:** Qualify the sensitivity statement as pipeline-specific.

- **P4-M22 — Reference  is cited as supporting parity-related interpretation, but the paper’s own scope is narrower**  
  **Section:** References and Discussion, pp. 6, 10  
  **Problem:** The paper cites a cosmic birefringence review alongside galaxy chirality claims. The connection is conceptual, but the manuscript does not provide a rigorous mapping from those observables to the measured quantity.  
  **Required fix:** Limit the citation to contextual background unless a formal mapping is derived.

- **P4-M23 — The manuscript’s use of “proof” language is not justified**  
  **Section:** Abstract and Conclusions, pp. 1, 7  
  **Problem:** The paper “reports,” “demonstrates,” and “tests” numerous hypotheses, but it does not prove the residual is systematic, nor prove the absence of cosmological signal.  
  **Required fix:** Replace proof-language with evidence-language throughout.

- **P4-M24 — Citation  author formatting is incomplete**  
  **Section:** References, p. 10  
  **Problem:** The DESI collaboration entry lists “`DESI Collaboration, A. Aghamousa, J. Aguilar et al.`” which is a mixed collaboration-plus-author format and may not match the canonical citation style.  
  **Required fix:** Use the proper collaboration citation format consistent with ADS.

- **P4-M25 — Several “future work” items are too speculative for the conclusions section**  
  **Section:** Discussion C and Conclusions, pp. 6–7  
  **Problem:** Proposed regression against morphology fields, GP likelihoods, and spectroscopic upgrades are presented as if they are straightforward extensions, but the paper does not show feasibility or expected impact quantitatively.  
  **Required fix:** Mark these as speculative follow-up ideas rather than implied next steps.

## Summary recommendation
**REJECT**

This manuscript contains substantive bibliography problems, several numerically opaque or insufficiently reproducible claims, and repeated overstatement of what the analyses demonstrate versus what they merely suggest. For PRD, the paper needs a serious structural rewrite, bibliography cleanup, and a much tighter audit trail for every quoted statistic before it can be considered for publication.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-M29 — **Table I’s “monopole+mask null” significance is internally inconsistent with the stated null mean**
- **Section:** Table I, p. 4
- **Problem:** The row reports the monopole+mask null as **+1.68σ**, but Table IV gives the same null’s observed pre-MASTER pseudo-\(C_\ell\) as \(1.696\times10^{-2}\) versus null \( (1.685\pm0.007)\times10^{-2}\), which implies a deviation of \((1.696-1.685)/0.007 \approx 1.57\sigma\), not 1.68σ.
- **Required fix:** Recompute the quoted significance from the displayed mean and uncertainty, or explain what alternative normalization was used.

P4-M30 — **Table I’s hemisphere LEE p-value does not match the corresponding sigma language elsewhere**
- **Section:** Table I, p. 4; Appendix C, p. 8
- **Problem:** Table I gives **\(p_{\mathrm{LEE}} \le 10^{-4}\)** for the hemisphere maximum-asymmetry estimator, while the body text says the same statistic has a **3.05σ local maximum** and that Bonferroni/BH reduction leaves the post-LEE significance **below \(|\sigma|<1\)**. A \(p\)-value at or below \(10^{-4}\) is not obviously consistent with that narrative unless the \(p\)-value is for the uncorrected scan and the \(\sigma\) is for a different corrected metric.
- **Required fix:** Explicitly label which null the \(p\)-value refers to and separate raw-look-elsewhere and multiplicity-corrected results.

P4-M31 — **Table II’s “Dev. (σ)” values are numerically inconsistent with the stated binomial formula**
- **Section:** Table II, p. 4
- **Problem:** Using the printed formula \(\sigma=\sqrt{p(1-p)/N}\) with \(N=3{,}201{,}160\), the row values do not reproduce the reported deviations. For the equivariant tier, \(p=0.4974\) gives \(\sigma \approx 0.0002795\), so \((0.4974-0.5)/\sigma \approx -9.30\), not **9.5** if the table is using magnitude, and certainly not \(-9.5\) unless the rounded \(p\) is hiding additional digits.
- **Required fix:** Either print more digits for \(p\) or note that the deviation is computed from unrounded values and reported as an absolute value.

P4-M32 — **Table II’s raw-tier deviation is off by more than rounding alone would suggest**
- **Section:** Table II, p. 4
- **Problem:** For the raw tier, \(p=0.5079\) and \(N=3{,}201{,}160\) give \(\sigma\approx 0.0002795\), so the deviation from 0.5 is \(0.0079/0.0002795\approx 28.27\), not **28.8**.
- **Required fix:** Show the unrounded fraction or recompute the deviation using the exact internal value.

P4-M33 — **Table II’s calibrated-tier deviation is also numerically loose**
- **Section:** Table II, p. 4
- **Problem:** For \(p=0.504\), the same formula gives \(0.004/0.0002795\approx 14.3\), not **14.6**.
- **Required fix:** Provide the full-precision fraction or state that the value is approximate and not derived from the rounded table entry.

P4-M34 — **Table III’s significance column is inconsistent with the displayed \(C_\ell\) and \(\sigma_\ell\) values beyond the first row**
- **Section:** Table III, p. 5
- **Problem:** The first row is explainable only if a null mean is subtracted, but the remaining rows are not reproducible from the table alone. For example, \(\ell_{\mathrm{eff}}=4\) has \(C_\ell=3.210\times10^{-6}\) and \(\sigma_\ell=0.804\times10^{-6}\), which is \(3.99\) in naive \(z\)-units, not **6.097**. The same issue appears for the other bandpowers.
- **Required fix:** Display the null mean for each row or replace the significance column with an explicit formula-based quantity.

P4-M35 — **Table III’s “Joint \(\chi^2\)/dof” appears to misuse the dof count**
- **Section:** Table III, p. 5
- **Problem:** The table reports **161.2/38 = 4.24**. If this is a reduced \(\chi^2\), the conventional notation would be \(\chi^2_\nu = 4.24\), not “161.2/38 = 4.24” without clarifying whether 38 is the number of bandpowers, the degrees of freedom after parameter fitting, or the raw bin count.
- **Required fix:** State the exact number of fitted parameters and the resulting dof.

P4-M36 — **The paper’s 99.3% reproduction claim is not mathematically recoverable from the displayed Table IV numbers**
- **Section:** Table IV, p. 5; Conclusions, p. 7
- **Problem:** The table shows \(1.696\times10^{-2}\) observed and \((1.685\pm0.007)\times10^{-2}\) null. The ratio \(1.685/1.696\approx 0.9935\), i.e. **99.35%**, while the text says **99.3%**. That is close, but the manuscript never states whether the reported percentage is rounded from the mean ratio, from a median ratio, or from a residual-power metric.
- **Required fix:** Write the exact formula used for “reproduces 99.3%” and report the unrounded value.

P4-M37 — **The \(-0.122\sigma\) headline value is not derivable from the printed Table III row without the hidden null mean**
- **Section:** Table III, p. 5; Abstract, p. 1
- **Problem:** The row prints \(C_1=1.494\times10^{-6}\) and \(\sigma=0.429\times10^{-6}\), which would naively imply \(3.48\sigma\). The quoted **\(-0.122\sigma\)** is only recoverable if an unprinted null mean \( \langle C_1\rangle = 1.546\times10^{-6} \) is supplied elsewhere.
- **Required fix:** Include the null mean directly in Table III or change the table header to make the subtraction explicit.

P4-M38 — **The 3.86× “asymmetry-suppression factor” does not follow from the nearby numbers as printed**
- **Section:** Results B, p. 4
- **Problem:** The text says suppression is from raw **+2.05%** to equivariant **−0.53%**. The ratio of magnitudes is \(2.05/0.53 \approx 3.87\), so the quoted **3.86×** is close but not exact. If the sign is intended to matter, a suppression factor should be defined as a ratio of amplitudes, not signed percentages.
- **Required fix:** State whether the factor is \(|2.05|/|0.53|\), and retain full precision or the underlying unrounded inputs.

P4-M39 — **The “1.6× CE-ResNet’s scale” claim is only approximately supported by the stated counts**
- **Section:** Introduction, p. 2; Comparison, p. 5
- **Problem:** The paper compares **3,201,160** spirals to **1.95 million** CE-ResNet galaxies. The ratio is \(3.201160/1.95 \approx 1.64\), so “**1.6×**” is a rounding, but the manuscript uses it as a quasi-quantitative novelty claim.
- **Required fix:** Either report the exact ratio or phrase it as an approximate scale comparison.

P4-M40 — **The “30× extension” over Iye et al. is arithmetically unsupported by the numbers shown**
- **Section:** Results C, p. 5
- **Problem:** The text says the analysis extends Iye et al. with **3.2×10^6 spirals (30× extension)**. If the comparison target is the cited \(\sim 80{,}000\) face-on spirals in Tadaki et al. or the SDSS spiral sample in Iye et al., the ratio \(3.2\times10^6 / 80{,}000 = 40\), while \(3.2\times10^6 / 1.3\times10^6 \approx 2.5\). The “30×” factor is therefore ambiguous and not reproducible from the displayed context.
- **Required fix:** Identify the exact denominator for the extension factor.

P4-M41 — **The “0.75%” falsification threshold is not consistent with the stated \(\pm 0.75\%\) amplitude language elsewhere**
- **Section:** Abstract, Discussion, Conclusions, pp. 1, 6–7
- **Problem:** The paper alternates between **\(A \approx 0.75\%\)**, **\(\gtrsim 0.75\%\)**, and **\(\sim 0.75\%\)** as if they were interchangeable. Because the threshold is said to come from a 50%-recovery-at-3σ injection study, it should be stated as a measured threshold with uncertainty, not a single hard number.
- **Required fix:** Quote the threshold with its uncertainty and specify whether it is the median, mean, or interpolated crossing point.

P4-M42 — **The “Fisher Poisson floor at 3σ is \(\sim 0.29\%\)” and the injection threshold are not clearly derived from compatible assumptions**
- **Section:** Discussion A, p. 6
- **Problem:** The Fisher floor is quoted using \(N_{\mathrm{spiral}}=3{,}201{,}160\) and \(f_{\mathrm{sky}}=0.46\), while the empirical threshold comes from the HC subsample \(N=471{,}049\). The paper calls the larger threshold “above the Fisher floor due to classification noise,” but the two calculations are not directly comparable without an explicit normalization to the same effective sky fraction and selection function.
- **Required fix:** Show the effective \(N\) and sky coverage used in each estimate.

P4-M43 — **The “65.7% of \(b/a<0.3\) objects receive CW or CCW labels” claim is not backed by a denominator in the displayed text**
- **Section:** Appendix E, p. 9
- **Problem:** The percentage is presented without the underlying counts. Since this figure is used to justify the dilution argument, the missing denominator makes the claim impossible to independently verify from the paper text alone.
- **Required fix:** Provide the raw counts and selection criterion in the appendix text or table.

P4-M44 — **The “69.91%” GZ1 agreement figure changes denominator between the main text and Appendix E**
- **Section:** Introduction, p. 3; Appendix E, p. 9
- **Problem:** The main text says the independent GZ1 cross-match is on **234,282** disjoint matches, while Appendix E says **240,919**. The same **69.91%** agreement and \(\kappa=0.40\) are quoted in both places, so one of the denominators is stale or refers to a different filter.
- **Required fix:** Harmonize the sample size or explicitly label the two match sets as distinct.

P4-M45 — **The “9.5σ” global CW-fraction monopole is not consistently tied to the printed binomial calculation**
- **Section:** Abstract, Results B, Conclusions, p. 1, 4, 7
- **Problem:** Using Table II’s \(p=0.4974\) and \(N=3{,}201{,}160\) gives a deviation of about **\(-9.30\sigma\)**, not 9.5σ. The text repeatedly refers to a **9.5σ** monopole, so either the fraction is more precise than the printed value or the sigma claim is stale.
- **Required fix:** Update either the fraction or the sigma value so they match at the displayed precision.

P4-M46 — **The “\(p_{\mathrm{MC}}=15/500=0.030\)” statement is arithmetically fine, but the implied significance conversion is not**
- **Section:** Conclusions, p. 7
- **Problem:** The paper treats \(15/500=0.030\) as “\(\approx 1.9\sigma\) Gaussian-equivalent.” For a one-sided Gaussian tail, \(p=0.03\) corresponds to about **1.88σ**, so the approximation is acceptable, but the manuscript mixes empirical-rank and Gaussian-equivalent language without marking the conversion rule.
- **Required fix:** State whether the Gaussian-equivalent is one-sided or two-sided and keep the convention fixed throughout.

P4-M47 — **The “+\(6.48\sigma\) pre-MASTER pseudo-\(C_\ell\)” claim is not visibly traceable**
- **Section:** Results C, p. 4; Discussion, p. 6
- **Problem:** The body mentions a **+6.48σ** pre-MASTER pseudo-\(C_\ell\), but the displayed Table IV only gives the observed and null means for the pre-MASTER canonical-mask statistic, from which the significance is **+1.68σ** for the monopole-only null, not 6.48σ. The paper never shows the calculation that leads to 6.48σ.
- **Required fix:** Specify the null model and variance used for the 6.48σ claim, or remove the number.

P4-M48 — **The “+3.3σ signal in the 1.87M-galaxy [0.5, 0.6) confidence bin” is not derivable from the stated bin size alone**
- **Section:** Results E, p. 5; Appendix C, p. 8
- **Problem:** The text gives the bin size and significance but no underlying count asymmetry, null mean, or uncertainty. That makes the quoted **+3.3σ** impossible to audit from the displayed text.
- **Required fix:** Include the bin’s measured fraction or asymmetry and the null expectation.

P4-M49 — **The “\(-0.03\sigma\)” after cutting to \(p_{\mathrm{eq}}>0.6\) is unsupported by displayed numbers**
- **Section:** Results E, p. 5; Appendix E, p. 9
- **Problem:** The paper asserts that the confidence cut removes the signal and yields **\(-0.03\sigma\)**, but no accompanying count, asymmetry, or null variance is shown. The number cannot be checked from the text.
- **Required fix:** Report the corresponding statistic and null distribution in the appendix or a table.

P4-M50 — **The “\(+4.31\sigma\) monopole-preserving dipole” in Appendix E is not linked to a calculation**
- **Section:** Appendix E, p. 9
- **Problem:** The appendix says the HC-broad-0.6 cut gives a **+4.31σ** monopole-preserving dipole, but no estimate, uncertainty, or null mean is provided. It is therefore unclear whether this is a direct measurement, a fitted significance, or a bootstrap rank translated into σ.
- **Required fix:** Add the measured value and the null standard deviation used to obtain 4.31σ.

P4-M51 — **The “\(+0.62\sigma\)” and “\(+0.87\sigma\)” HC-cut collapse values do not specify the null procedure**
- **Section:** Appendix E, p. 9
- **Problem:** The appendix states the HC-broad and HC-strict results, but does not say whether the null is the same isotropic bootstrap used for the main dipole, a label-shuffle, or something else. These values are therefore not directly comparable to the headline \(-0.122\sigma\).
- **Required fix:** Attach the null label to each HC-cut result.

P4-M52 — **The “\(<0.5\sigma\) variation” under pixel-count threshold sweep is not quantified by endpoint values**
- **Section:** Appendix E, p. 9
- **Problem:** The paper says varying the per-pixel minimum spiral count threshold from 5 to 50 produces **<0.5σ variation**, but gives no endpoint statistics. Without the endpoints, one cannot tell whether the variation is monotonic, noisy, or driven by a single threshold.
- **Required fix:** Tabulate the threshold sweep results or plot them in a figure.

P4-M53 — **The “94.4% rotation stability” test in Table V is not described in units that make it comparable to the threshold**
- **Section:** Appendix B, p. 7
- **Problem:** The threshold is **>80%**, result is **94.4%**, but the test definition is not given as an accuracy, agreement rate, or correlation coefficient. Because other table entries use percentages and one uses \(r\), the statistic class is ambiguous.
- **Required fix:** State the exact metric used for T2 and its uncertainty.

P4-M54 — **The “100% artifact rejection” in Table V is likely a ceiling effect rather than a measured continuous statistic**
- **Section:** Appendix B, p. 7
- **Problem:** Reporting **100%** for blank/scrambled-image rejection suggests a binary pass/fail criterion rather than a calibrated test statistic, yet it is presented alongside continuous percentages. That makes the test suite harder to interpret as quantitative evidence.
- **Required fix:** Report the underlying rejection rate and sample size, not just a clipped percentage.

P4-M55 — **The “49.7%” CW/CCW balance in Table V is not obviously tied to the catalog-wide 49.74% fraction**
- **Section:** Appendix B, p. 7; Table II, p. 4
- **Problem:** Table V reports **49.7%**, while Table II implies **49.74%**. These are close, but because Table V is a bias-hardening test and Table II is the catalog statistic, the manuscript should clarify whether Table V is rounded from the same sample or from an independent validation subset.
- **Required fix:** Specify the sample underlying T8 and whether the quoted percentage is rounded from the catalog-wide value.

P4-M56 — **The 8-test bias-hardening suite is not integrated with the main systematic claim**
- **Section:** Appendix B and Discussion, pp. 7, 6
- **Problem:** The discussion uses the suite as evidence that the classifier is bias hardened, but the main text never states how passing the eight tests quantitatively constrains the residual CW bias. Without a mapping from each test to the reported 0.26% residual, the suite functions as qualitative reassurance rather than a calibrated bound.
- **Required fix:** Add a short table linking each bias test to the specific failure mode it bounds.

P4-M57 — **The “0.26% (9.5σ)” released-label residual is not explicitly derived from the stated fraction and sample size**
- **Section:** Data Availability, p. 9
- **Problem:** The paper says released catalog labels carry a **0.26% (9.5σ)** residual, but the visible numbers elsewhere are \(0.4974\) and \(N=3{,}201{,}160\). Those imply a deficit of \(0.26\%\) and a deviation near \(9.3\)σ, not 9.5σ.
- **Required fix:** Recompute the significance from the exact label fraction or update the printed sigma.

P4-M58 — **The “\(A = 0.75\%\) at \(N=471{,}049\)” injection threshold is not obviously consistent with the claimed “50%-recovery-at-3σ” criterion**
- **Section:** Discussion A, p. 6; Table I, p. 4
- **Problem:** With \(N=471{,}049\), a simple Poisson scaling would suggest a different \(3σ\) floor than the one implied by the threshold if the effective asymmetry estimator uses only one count per galaxy. Because the paper does not show the injected vs recovered statistics, the threshold’s derivation cannot be verified.
- **Required fix:** Provide the recovery curve or the injected amplitude grid and success counts.

P4-M59 — **The “\(C_1\) decoupled from 2.30×10\(^{-5}\) to 1.51×10\(^{-5}\)” reduction is not reconciled with the reported \(+3.64σ\) residual**
- **Section:** Appendix A, p. 7
- **Problem:** The appendix says monopole subtraction reduces decoupled \(C_1\) from \(2.30\times10^{-5}\) to \(1.51\times10^{-5}\) and increases \(\sigma\) from **+1.85** to **+3.64**. But if the variance shrinks or the mean shifts, the paper should explain which null distribution changed and why the same observed statistic becomes more significant after subtraction.
- **Required fix:** State the exact null mean and variance before and after monopole subtraction.

P4-M60 — **The “all 7 equatorial slabs within 0.5% of 50/50” statement is not supported by slab-by-slab numbers**
- **Section:** Results B, p. 4
- **Problem:** The paper uses the uniformity of 7 coordinate slabs to argue against a dipole, but no slab table is shown in the text. Since this claim underpins the interpretation of the monopole as non-dipolar, it needs the actual per-slab fractions.
- **Required fix:** Add a table of the 7 slab fractions and uncertainties.

P4-M61 — **The “direct cross-spectrum \(C(A_p \times n_{\text{total}})\) at \(\ell=2\) gives \(r=-0.65\) with \(\sigma=-2.89\)” is dimensionally incomplete**
- **Section:** Abstract, p. 1; Results D, p. 5; Appendix D, p. 9
- **Problem:** The paper reports both a correlation coefficient and a sigma for the same cross-spectrum result, but does not define the normalization of \(r\) or show how the \(\ell=2\) cross-spectrum maps to a scalar correlation coefficient. This makes the claim impossible to reproduce from the displayed text.
- **Required fix:** Provide the formula for \(r\) and the units/normalization of the cross-spectrum statistic.

P4-M62 — **The “\(-264.5\)” and “\(-250\)” \(z\)-scores in Appendix D are likely stale or placeholder artifacts**
- **Section:** Appendix D, p. 9
- **Problem:** The appendix says a naive WLS posterior gives \(z=-264.5\), and a larger template fit gives \(z\approx-250\). These extreme values are far outside the scale of all other reported statistics and appear inconsistent with the rest of the paper’s uncertainty budget. They may be machine-generated placeholders or carry-over numbers from earlier drafts.
- **Required fix:** Verify the raw fit outputs and explain the normalization that produces such enormous \(z\)-scores.

P4-M63 — **The “+2.49σ” quadrant maximum and “−0.82σ” minimum are not shown to come from the same estimator**
- **Section:** Appendix C, p. 8
- **Problem:** The sky-quadrant diagnostics list values ranging from \(-0.82σ\) to \(+2.49σ\), but the paper does not say whether these are dipole-fit significances, raw asymmetry significances, or bootstrap ranks. That matters because the adjacent text treats them as evidence against a primordial dipole projection.
- **Required fix:** Annotate each quadrant statistic with the estimator and null.

P4-M64 — **The “NGP \(b>0\) gives \(\sigma_{\text{iso}}=+0.47\)” and SGP gives \(+2.02\) asymmetry are not directly comparable**
- **Section:** Appendix C, p. 8
- **Problem:** The northern and southern galactic poles are reported under a common “\(\sigma_{\text{iso}}\)” label, but the sample sizes and mask coverage are not given. Without those, the numeric asymmetry values cannot be compared or combined.
- **Required fix:** Include the denominators and null definitions for the hemisphere split.

P4-M65 — **The “\(+3.29\sigma\)” confidence-bin signal decomposed into imaging legs does not sum transparently**
- **Section:** Appendix C, p. 8
- **Problem:** The text gives BASS+MzLS \(+0.30σ\), DECaLS \(+4.50σ\), and DES \(+2.46σ\), but these are not shown to combine into the stated overall **+3.29σ** signal because the bins are likely weighted differently. The weighting scheme is not given.
- **Required fix:** Show the weighted combination formula and the bin weights.

P4-M66 — **The “\(p_{\mathrm{eq}}>0.6\) gives \(-0.03σ\)” and “HC-broad-0.6 gives \(+0.62σ\)” results appear to use different subsets with no explicit overlap policy**
- **Section:** Results E, p. 5; Appendix E, p. 9
- **Problem:** One cut is on equivariant max-class probability in the main text, the other is on a high-confidence broad subsample in Appendix E. Because the exact subset definitions differ, the two values are not directly comparable, yet they are discussed as if they were successive refinements of the same signal.
- **Required fix:** Define the subset hierarchy and state which cut is nested inside which.

P4-M67 — **The “0.951 mean classification confidence” and “0.9997 median” are not supported by a distributional summary**
- **Section:** Catalog Statistics, p. 3
- **Problem:** The paper reports mean and median confidence but no percentile spread. Given the heavy skew implied by a median near 1.0 and a mean of 0.951, the absence of quartiles or a histogram makes the confidence distribution impossible to assess.
- **Required fix:** Add a summary table or figure with at least quartiles and low-confidence tails.

P4-M68 — **The paper’s use of “survey-scale” is not benchmarked against the cited DESI morphology catalog**
- **Section:** Title, Abstract, Conclusions, pp. 1, 7
- **Problem:** The paper calls the catalog “survey-scale” and “largest to date,” but the comparison against Galaxy Zoo DESI’s **8.7M** detailed morphology measurements is not a direct chirality comparison. The novelty claim depends on whether chirality labels, not general morphology labels, are the relevant comparator.
- **Required fix:** State the comparator class explicitly and distinguish chirality catalogs from morphology catalogs.

P4-M69 — **The “publicly available on HuggingFace” claim conflicts with the repository paths in Data Availability**
- **Section:** Abstract, Data Availability, pp. 1, 9
- **Problem:** The abstract says the catalog and scripts are publicly released at the project repository, while Data Availability splits catalog, model, and code across HuggingFace and GitHub. That is not necessarily wrong, but the wording is inconsistent and can mislead readers about what is actually hosted where.
- **Required fix:** Harmonize the release statement and name the hosting locations consistently.

P4-M70 — **The “monopole subtraction reduces decoupled \(C_1\) … and increases \(\sigma\)” claim needs a sign explanation**
- **Section:** Appendix A, p. 7
- **Problem:** The appendix simultaneously says the statistic drops from \(2.30\times10^{-5}\) to \(1.51\times10^{-5}\) and the significance rises from **+1.85** to **+3.64**. That only makes sense if the null mean moves closer to zero or the variance shrinks after subtraction, but the paper does not say which. The sign logic is not transparent.
- **Required fix:** State the null mean before and after subtraction and show the corresponding variances.

P4-M71 — **The “50%-recovery-at-3σ threshold at \(A=0.75\%\)” is not tied to a displayed recovery curve**
- **Section:** Abstract, Discussion, Conclusions, pp. 1, 6–7
- **Problem:** The paper repeatedly references the 50% recovery criterion, but no curve or table shows recovery probability versus amplitude. Without that, the threshold is not auditable.
- **Required fix:** Add the full injection-recovery curve or a small table of amplitudes and recovery fractions.

P4-M72 — **The “null dipole result at sub-percent sensitivity” is stronger than the visible selection-function evidence**
- **Section:** Abstract, Introduction, Discussion, pp. 1, 2, 6
- **Problem:** The paper uses the catalog’s large size to infer sub-percent sensitivity, but the actual selection function includes classifier dilution, edge-on contamination, and mask-dependent leakage. The text never quantifies the combined selection bias in a way that would justify the blanket “sub-percent sensitivity” statement across the full survey footprint.
- **Required fix:** Restrict the claim to the specific estimators and cuts that were tested.

