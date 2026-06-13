# P1B R37conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar` [FALLBACK from sonar-pro]
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.65.pdf` md5=bac8d620 pages=20
**Input format**: TEXT + web search + pass-2 self-critique (13338 chars)
**Wall time**: 52.3s

---

I cannot complete the requested **citation-forensics audit** to PRD-standard from the material provided, because the prompt contains only the paper text and no live arXiv/ADS search results for the cited references. I can still flag internal consistency problems in the manuscript text itself, but I cannot सत्यापित titles/authors/venues/arXiv IDs against external databases as requested without search access to those sources in the response context.

The paper is **not publication-ready** as written: it contains numerous internal self-qualifying caveats, load-bearing numerical claims, and provenance statements that are either not sufficiently self-contained or are weakened by unresolved reproducibility and comparison issues. The most serious issues are the uncorrected DES-SN5YR × Pantheon+ overlap, the use of non-comparable significance statements side-by-side, and multiple places where “verification” claims are explicitly not direct tests of the underlying theory.

## Findings

### P1B-E1 — Section III, pp. 3–5
**Problem:** The paper repeatedly presents the ΛCDM+∆Neff run as a “null-consistency test” but also uses it as if it were a proxy for the spin-torsion sector, while explicitly stating that “no torsion-modified Boltzmann equations are solved” and that a bespoke modified Boltzmann code would be required for a direct test.  
**Offending text:** “No custom CAMB modifications are used; no torsion-modified Boltzmann equations are solved.” / “It does not verify the spin-torsion theory module itself.”  
**Required fix:** Separate the proxy analysis from any theory-level inference much more aggressively in the abstract, conclusions, and claims table; remove any wording that implies verification of the ECH sector by this MCMC run.

### P1B-E2 — Section III, pp. 4–5
**Problem:** The manuscript uses multiple significance conventions side-by-side without a clean, repeated “not directly comparable” qualifier at every juxtaposition, violating the paper’s own stated rule and your review instruction.  
**Offending text:** “3.2σ in chain-σ units, versus the canonical 3.6σ when the tension is expressed in distance-ladder terms…” and similar comparisons between 3.6σ, 3.2σ, 2.5σ, and 0.5σ.  
**Required fix:** For every juxtaposition of sigma values derived from different null procedures, explicitly mark them as non-comparable and state the exact estimator used.

### P1B-E3 — Section III / Table I, pp. 3, 18
**Problem:** The DES-SN5YR and Pantheon+ overlap is acknowledged as approximately 20%, but the paper nevertheless uses their product likelihood as a load-bearing result and repeatedly states only that a control chain is “queued.” This is not an acceptable substitute for a corrected joint-covariance treatment.  
**Offending text:** “The present analysis combines them via a product likelihood without a joint covariance…”  
**Required fix:** Either provide the joint-covariance corrected chain and make it the quoted headline result, or demote all overlap-uncorrected results to clearly labeled exploratory status and stop using them as support for major conclusions.

### P1B-E4 — Section III, pp. 4–5
**Problem:** The paper claims the chain is “the correct compromise of three inputs,” but the SN overlap caveat means the compromise is not statistically correct as stated.  
**Offending text:** “The chain posterior is therefore the correct compromise of three inputs…”  
**Required fix:** Replace with “a provisional overlap-uncorrected compromise” and remove any claim of correctness until the control chain exists.

### P1B-E5 — Section III, pp. 3–4
**Problem:** The manuscript relies on a posterior-truncated one-sided upper limit for ∆Neff and treats it as a meaningful physical bound, but the prior allows negative ∆Neff and the model is explicitly a generic proxy. The inference is prior-sensitive and not framed with sufficient caution in the abstract.  
**Offending text:** “Under the physically motivated restriction ∆Neff ≥ 0…”  
**Required fix:** Make clear in the abstract and Table I caption that the one-sided limit is a post-processing convention, not a direct measurement, and is prior-dependent.

### P1B-E6 — Section IV, Eq. (1), p. 7
**Problem:** The estimator equation is internally inconsistent with the surrounding prose unless the omitted \(\sigma_b^2\) divisor is intentionally absent; the reviewer metadata says Eq. (1) must match the released script form. In the body text, this is indeed written as an unweighted \(\chi^2\), but the manuscript still needs to state explicitly that the estimator is unweighted and that the script version intentionally drops the divisor.  
**Offending text:** Eq. (1): “\(\chi^2(\beta)=\sum_b [C_b^{EB,decoupled} - \frac12 \sin(4\beta) C_b^{EE,tmpl}]^2\)”  
**Required fix:** Add an explicit sentence immediately after Eq. (1) stating that this is the intended script-matching unweighted form, with no per-bin variance normalization.

### P1B-E7 — Section IV, p. 7–9
**Problem:** The manuscript states that the unweighted estimator is the canonical choice because it matches public scripts, but then uses an inverse-variance-weighted fit as a cross-check to explain the bias. This is acceptable only if the paper clearly states which estimator underlies every quoted headline figure. That is not done consistently enough.  
**Offending text:** “The unweighted χ2 template fit is adopted as the canonical baseline…”  
**Required fix:** Add a table or explicit sentence listing which \(\hat\beta\) values come from the unweighted baseline versus which come from weighted or modified-template robustness tests.

### P1B-E8 — Section IV, pp. 7–9
**Problem:** The paper quotes pipeline-recovery SNR values such as 20.32 and 25.71, but these are not the sky-measurement significances and are repeatedly discussed in proximity to the published 3.6σ result. The distinction is made, but not strongly enough in figure captions and the abstract.  
**Offending text:** “The high pipeline template-fit SNR figures … refer to recovery of injected MC signals.”  
**Required fix:** Add a figure-caption warning that these SNRs are not observables and cannot be compared to the literature’s detection significances.

### P1B-M1 — Section II, pp. 2–5
**Problem:** The paper quotes specific tensions and derived values for \(H_0\), \(S_8\), \(\sigma_8\), and \(\Omega_m\), but the derivations are spread across prose, Table I, and footnotes. For PRD standards, the load-bearing scalars in the abstract need direct body traceability in a single location.  
**Offending text:** “\(-0.020 \pm 0.169\) full-tension; \(67.68 \pm 1.06\)” etc.  
**Required fix:** Add a compact derivation/check paragraph or a reproducibility table showing exactly how each quoted scalar is obtained from the frozen chains.

### P1B-M2 — Section II, p. 4
**Problem:** The manuscript computes \(H(z=0.5)\) from the CPL form and reports a \(\approx +1.7\%\) difference, but the computation is not shown with enough intermediate numerical detail to audit.  
**Offending text:** “the CPL Hubble rate \(H(z=0.5)\) differs … by ≈ +1.7%”  
**Required fix:** Show the numerical substitution explicitly or provide the checked artifact pointer in the body, not only in reproducibility prose.

### P1B-M3 — Section III, p. 3
**Problem:** The paper states “the data are consistent with \(\Delta N_{\rm eff}=0\) in stock CAMB” while also emphasizing that the PR4/2018 likelihood pairing has not been systematically tested. That means the quoted null result is not fully provenance-robust.  
**Offending text:** “we have not run a release-pairing swap test…”  
**Required fix:** Downgrade the conclusion to “within the chosen likelihood pairing” and state that the result is conditional on the untested pairing choice.

### P1B-M4 — Section III, p. 5
**Problem:** The S8 tension discussion mixes a within-stack posterior shift with an external measurement-vs-measurement tension, then gives a numerical “2.0σ residual” in a context where the DES-Y3 prior is already part of the chain.  
**Offending text:** “this 2.0σ residual is a within-stack readout…”  
**Required fix:** Remove the residual as a headline number or isolate it in a clearly labeled internal-consistency subsection.

### P1B-M5 — Section V, pp. 9–10
**Problem:** The w0–wa chain is explicitly overlap-uncorrected, yet the manuscript still presents \(w_0=-0.812\pm0.044\), \(w_a=-0.667\pm0.186\), and phantom crossing as if these are robust physical inferences.  
**Offending text:** “provisional under the overlap-uncorrected likelihood”  
**Required fix:** Demote the entire w0–wa result set to exploratory status in the abstract, conclusions, and Table II caption unless the control chains are completed.

### P1B-E9 — Section V, pp. 9–10
**Problem:** The manuscript invokes Bayesian evidence and model preference repeatedly while explicitly not computing \(\ln B\), AIC, or BIC. This is acceptable only if all such claims are removed from any persuasive context.  
**Offending text:** “robust ln B is left to a follow-up nested-sampling analysis.”  
**Required fix:** Ensure no conclusion, abstract sentence, or section heading implies model-selection support.

### P1B-M6 — Section VI, pp. 10–13
**Problem:** The birefringence section mixes three different observational summaries: PR3+WMAP9, PR4/NPIPE, and ACT DR6, then uses one as the primary constraint and others as auxiliary checks. The paper’s repeated language makes these appear more interchangeable than they are.  
**Offending text:** “The primary observational reference adopted in this analysis is …” / “ACT DR6 enters only as an auxiliary inverse-variance cross-check.”  
**Required fix:** Add a compact provenance table that states exactly which measurement drives which fit.

### P1B-E10 — Section VI, pp. 10–13
**Problem:** The paper claims the same \(\beta\approx0.27^\circ\) arises in standard GR with an identical ALP, which is physically plausible, but this also means the result is *not* an ECH prediction. The manuscript says this, but the abstract still risks overstating the ECH relevance by tying the ALP discussion to the companion-paper consistency check.  
**Offending text:** “The same birefringence arises in standard GR with an identical ALP; it is not a distinctive ECH prediction.”  
**Required fix:** Remove any implication that the birefringence analysis supports ECH itself rather than merely showing compatibility with an external ALP model.

### P1B-M7 — Section VI, pp. 11–12
**Problem:** Several significance statements are presented with optimistic or approximate combinations that are explicitly said to be “upper bounds” or “auxiliary cross-checks,” but they still occupy central argumentative space.  
**Offending text:** “This 3.9σ figure is an upper bound…” / “This 9σ figure is not a model-discrimination forecast…”  
**Required fix:** Move these to a clearly secondary subsection and ensure the abstract does not echo them.

### P1B-M8 — Section VI, pp. 10–12
**Problem:** The manuscript claims a ∼25× fine-tuning of \(\theta_i\), but this is partly a prior-volume statement and partly a physical backreaction statement. The text conflates the two.  
**Offending text:** “\(\theta_i \sim 0.1\) versus the natural-prior midpoint \(\theta_i \sim 0.5\)”  
**Required fix:** Distinguish parameter-space fine-tuning from dynamical spectator/backreaction tuning.

### P1B-M9 — Section VI, p. 12
**Problem:** The coupling range is quoted as extending to \(\sim 160\), but the prior used in the continuous-prior rerun only covers \([4,60]\), and the paper itself says values above 60 lie outside that scan. This is presented in a way that can be misread as supported by the fit.  
**Offending text:** “required Caγ spans ≈8.6 up to ≈160 …”  
**Required fix:** State clearly that \(\sim160\) is an extrapolated requirement, not a sampled posterior result.

### P1B-M10 — Table I, p. 18
**Problem:** The table’s “2.0σ residual” and “2.6σ two-Gaussian tension” language mixes within-stack and between-experiment quantities in a way that is not publication-grade unless the distinction is highlighted at point of use.  
**Offending text:** “this 2.0σ residual is a within-stack readout…”  
**Required fix:** Add a strong note in the caption defining which tension measures are valid comparisons and which are not.

### P1B-M11 — Table II, p. 19
**Problem:** The “marg.-tail, +4.3σ” label is not a frequentist exclusion and is explicitly not a Bayes-factor result. The table could easily be misread as a robust detection of departure from \(\Lambda\)CDM.  
**Offending text:** “\(+4.3\sigma\)”  
**Required fix:** Rename this column to make clear it is a tail-extrapolation distance only, not a hypothesis test.

### P1B-M12 — Table III, p. 19
**Problem:** The table describes “Planck block” and “SDSS BAO block” as likelihood stacks, but the exact realization of the Planck block changes across chains, and the paper notes a PR4-vs-2018 pairing mismatch elsewhere.  
**Offending text:** “The exact Cobaya likelihood blocks of all five chains are listed in Table III.”  
**Required fix:** Add release/version granularity for each block and mark any mixed-release stacks as provisional.

### P1B-M13 — Table IV, p. 20
**Problem:** The table reports medians and percentiles for multiple subsets, but the “strict \(\theta_i \le 0.1\)” subset is explicitly “indicative only,” making the accompanying percentile readouts potentially unstable and not fit for load-bearing claims.  
**Offending text:** “indicative only”  
**Required fix:** Move this subset out of the main results table or label it as non-quantitative exploratory output.

### P1B-M14 — Table V, p. 20
**Problem:** The claims classification table marks many results as “Internally verified,” but this is not the same as external reproducibility or journal-grade verification.  
**Offending text:** “Internally verified”  
**Required fix:** Replace with a more precise status taxonomy that distinguishes internal recomputation from externally reproducible, frozen-release verification.

### P1B-M15 — Appendix A, pp. 14–15
**Problem:** The repository and dataset provenance are not frozen to an immutable public snapshot at the time of submission; DOI assignment is “pending,” and the paper relies on version-stamp commits plus mutable repository paths.  
**Offending text:** “DOI assignment is pending” / “a public tagged release pinning all of these artifacts to a single immutable snapshot is pending”  
**Required fix:** Provide a frozen release tag or DOI before acceptance.

### P1B-M16 — Appendix A, p. 14
**Problem:** The repository contains program-wide code from other papers, including galaxy-spin pipeline code “used by Paper IV but not by any analysis of this paper.” That raises provenance ambiguity.  
**Offending text:** “program-wide content used by Paper IV, not by this paper’s analyses.”  
**Required fix:** Separate the paper-specific artifact bundle from unrelated program-wide code.

### P1B-M17 — Appendix A, p. 14
**Problem:** The paper explicitly warns about a “column-permutation bug” in earlier JSON exports. That is a serious provenance issue and should be front-loaded more prominently because it affects trust in all reported chain readouts.  
**Offending text:** “earlier parameter_summary.json export carried an off-by-one column-index bug.”  
**Required fix:** State exactly which derived numbers were potentially affected and prove they were all recomputed from the corrected files.

### P1B-M18 — Appendix C, pp. 15–16
**Problem:** The ALP-MCMC chain is described as using a Gaussian summary likelihood on the published birefringence result rather than the EB spectra themselves. This is acceptable for a consistency check, but it must not be described as an MCMC fit to the observation in a stronger sense.  
**Offending text:** “anchored to the Gaussian summary likelihood … not to the EB spectra themselves”  
**Required fix:** Make the abstract and conclusions reflect that this is a summary-likelihood consistency exercise only.

### P1B-M19 — Abstract, p. 1
**Problem:** The abstract is overloaded with load-bearing numbers from three distinct analyses, but some of the key statements are conditional or exploratory in the body. The abstract therefore overstates certainty relative to the final calibrated statements.  
**Offending text:** “We report the technical verification material…” plus the ensuing numerical claims.  
**Required fix:** Add caveats in the abstract matching the body’s strongest limits: proxy-only MCMC, overlap-uncorrected w0–wa chain, and consistency-check-only ALP analysis.

### P1B-M20 — Abstract / Conclusion, pp. 1, 13
**Problem:** The abstract and conclusions imply the paper is a verification companion, but several numerical claims remain tied to uncorrected systematics or deferred analyses. The paper’s final statements are stronger than the body-supported calibrated ones.  
**Offending text:** “confirms” / “verifies” in contexts where the body says “queued,” “provisional,” or “auxiliary.”  
**Required fix:** Replace confirmatory language with conditional language wherever the result depends on unresolved overlap, pairing, or model-selection issues.

## Summary recommendation
**MAJOR REVISIONS**

The manuscript contains enough internal numerical work to be potentially salvageable, but it is not acceptable in its current form for PRD. The main blockers are unresolved overlap-covariance in the SN analysis, repeated mixing of non-comparable significance metrics, and several places where exploratory or proxy analyses are narrated too strongly relative to what they actually establish. The bibliography and external citation verification cannot be completed from the provided materials alone, and the paper should not proceed until the provenance bundle is frozen, the ambiguous comparisons are cleaned up, and the abstract/conclusion are rewritten to match the most conservative body-supported statements.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-A1 — **Table I arithmetic mismatch**
- The table’s “with the chain-recomputed marginal, the full-tension posterior \(S_8 = 0.814 \pm 0.008\) is consistent with the naive two-Gaussian combination of the Planck+BAO+SN marginal and the DES-Y3 prior \((0.827 \pm 0.010 \otimes 0.776 \pm 0.017 = 0.814 \pm 0.009; agreement at the 0.01σ level)\)” contains an arithmetic inconsistency in the quoted uncertainty.
- Recomputing the inverse-variance combination gives \( \sigma = \left(1/0.010^2 + 1/0.017^2\right)^{-1/2} \approx 0.0086\), which rounds to \(0.009\), so the quoted mean is fine but the uncertainty should be checked against the actual chain-recomputed marginal rather than presented as an exact equality from the naive combination.
- This is minor numerically, but it is a load-bearing derived quantity in the table caption and should be made internally explicit.

P1B-A2 — **Table I min-ESS vs sample-count arithmetic needs clarification**
- The caption says the full-tension chain has “6 chains” and “176,240” total samples, with “Min ESS 4,744.”
- Because the effective sample size is a derived quantity from autocorrelation, the paper should show how the quoted ESS maps to the chain lengths or at least specify whether it is the minimum across all sampled parameters or across all subchains.
- As written, the reader cannot verify whether “4,744” is the minimum over the 17 parameters, the 6 chains, or a post-thinning diagnostic.

P1B-A3 — **Figure 3 caption vs body: bias-floor arithmetic is not transparently recomputed**
- The body says the canonical injection \(\beta_{\rm inj}=0.27^\circ\) recovers \(\hat\beta=0.238^\circ\), giving bias \(-0.032^\circ\), and the worst-case injection \(\beta_{\rm inj}=0.342^\circ\) gives \(-0.040^\circ\).
- The figure caption then states the “inner bars” use the standard error of the 500-MC mean and that the dedicated rerun at \(f_{\rm sky}=0.32\) measures \(\sigma_\beta=0.046^\circ\).
- The relation between the displayed SNR values, the mean-recovery values, and the quoted \(\sigma_\beta\) is not fully auditable from the caption alone; the paper should state the exact formula used for each displayed number.

P1B-B1 — **Figure 1 caption and Table I use different H0/S8 summary language**
- Figure 1 says the full-tension corner plot “confirms no additional relativistic species at recombination.”
- Table I, however, frames the same \(\Delta N_{\rm eff}\) result as a null-consistency cross-check and gives \(H_0\), \(S_8\), \(\sigma_8\), and \(\Omega_m\) summaries.
- This is a body-claim mismatch: the figure caption turns a posterior consistency statement into a stronger physical confirmation claim than the table supports.

P1B-B2 — **Figure 4 caption vs body: parameter-range numbers are inconsistent**
- Figure 4 caption says the continuous-prior configuration has \(\theta_i \in [0.01,\pi]\) and \(\log_{10}(m_a/{\rm eV}) \in [-35,-30]\), while also stating that the “dropped [1,4) interval lies entirely below the minimum coupling \(\approx 8.6\).”
- The body discussion elsewhere emphasizes the earlier \([1,30]\) chain truncates \(\sim 28\%\) of posterior mass above 30 and that the new \([4,60]\) run is the primary coupling-inference result.
- The caption should distinguish more clearly between the old truncated chain and the new continuous-prior chain; otherwise the plotted parameter support can be misread as directly comparable to the earlier run.

P1B-C1 — **Equation (1) dimensional normalization is incomplete**
- Eq. (1) defines
  \[
  \chi^2(\beta)=\sum_b \left[C_b^{EB,{\rm decoupled}}-\frac12 \sin(4\beta) C_b^{EE,{\rm tmpl}}\right]^2
  \]
  with no explicit variance normalization.
- As written, this is not a true \(\chi^2\) in the statistical sense unless all bandpowers have identical units and identical implicit weights; it is an unweighted least-squares objective.
- The paper later says this is intentional, but the equation itself should be relabeled or explicitly annotated to avoid dimensional and statistical ambiguity.

P1B-C2 — **Eq. (3) is dimensionally fine, but the surrounding text misstates the scope**
- Eq. (3), \(\Delta\phi/f_a \approx 0.42\), is dimensionless and consistent.
- However, the text presents it as if it were a broadly representative result over the model space, while it is explicitly one point \((m=2H_0,\theta_i=1)\).
- This is an equation-to-text mismatch in scope, not algebra, and it should be localized more clearly as a single benchmark trajectory.

P1B-D1 — **Table II footnote b contains an internal consistency check that is not actually shown in the main text**
- Footnote b defines \(w_{\rm pivot}\) via the covariance relation and states that the direct readout gives \(1-a_p=0.210\), \(a_p=0.790\), \(z_p=0.27\).
- The main text refers to \(z_p=0.27\) as the decorrelation pivot, but it does not show the covariance calculation.
- This is a cross-reference gap: the body relies on an internal derivation that only appears in the table note.

P1B-D2 — **Appendix C and Table IV disagree on the meaning of the continuous-prior chain**
- Appendix C says the continuous-prior configuration is the “primary coupling-inference result.”
- Table IV presents the same chain as a “restricted-posterior readout” and emphasizes the \(\theta_i \le 0.1\) subset as “indicative only.”
- The paper should clearly distinguish the full continuous-prior posterior from the subset readout, because the same chain is being used both as a main result and as a restricted diagnostic.

P1B-E1 — **Distinct null procedures are juxtaposed without explicit non-comparability language**
- The abstract and body place side by side:
  - the \(3.6\sigma\) Hubble tension in \(H_0\),
  - the \(2.5\sigma\) \(S_8\) shift,
  - the \(3.2\sigma\) MB-axis offset,
  - and the \(2.7\text{–}2.9\sigma\) birefringence measurement,
  all of which come from different null procedures.
- Although the manuscript sometimes warns that some are not directly comparable, it does not do so consistently at every juxtaposition.
- This remains a presentation flaw: the paper should not list these values in a single argumentative sequence without a repeated comparability qualifier.

P1B-E2 — **The “0.01σ level” agreement claim in Table I is not actually supported by the displayed numbers**
- The caption states that \(0.814 \pm 0.008\) agrees with \(0.814 \pm 0.009\) at the \(0.01\sigma\) level.
- But the difference between the central values is exactly zero to the displayed precision, so the quoted \(0.01\sigma\) is not a meaningful independently checkable statistic from the printed numbers.
- This should be described as agreement within rounding, not as a computed significance level.

P1B-E3 — **The “2.6σ two-Gaussian tension” in Table I depends on the stated overlap integral but is not reproducible from the displayed summary alone**
- Table I says the Planck+BAO+SN \(S_8\) marginal is \(0.827 \pm 0.010\) and the DES-Y3 prior is \(0.776 \pm 0.017\), with overlap integral 0.05 and “2.6σ two-Gaussian tension.”
- Using the printed means and standard deviations, the naive difference is \(0.051/\sqrt{0.010^2+0.017^2}\approx 2.6\), so the arithmetic is fine.
- The issue is that the “overlap integral” is introduced as a separate statistic but not operationally connected to the 2.6σ number in the caption, leaving the reader unable to tell whether the 2.6σ is a Gaussian-distance estimate or an overlap-derived tension.

P1B-F1 — **Abstract sentence about the NaMaster result overstates the body-supported claim**
- The abstract says the pipeline recovery “confirms the algebraic pseudo-\(C_\ell\) \(E \to B\) deconvolution under MASTER mode coupling.”
- The body later says the test is a validation of a synthetic-sky pipeline and is not a sky-measurement significance.
- The word “confirms” is stronger than what the body establishes; the body supports “validates on synthetic skies,” not a general confirmation of the physical measurement pipeline.

P1B-F2 — **Abstract sentence about the ALP result overstates model specificity**
- The abstract says the same birefringence “arises in standard GR with an identical ALP” and is “not distinctive ECH prediction.”
- The body later says the ECH framework provides only heuristic motivation and no derived photon-torsion coupling.
- The abstract should therefore avoid framing the ALP section as part of an ECH verification story at all; the body does not support that connection.

P1B-G1 — **“Primary observational reference” is not the same as a single authoritative measurement**
- In Sec. VI, the paper names the Eskilt–Komatsu joint WMAP+Planck value as the “primary observational reference” and then uses Planck NPIPE and ACT DR6 only as context.
- But the paper also says the 3.9σ inverse-variance combination is a separate cross-check and not the headline value.
- This creates a novelty-like hierarchy without a formal justification for why the WMAP+Planck summary, rather than the later Planck/ACT measurements, should anchor the model discussion.

P1B-G2 — **“the full-tension chain samples 17 parameters” is novel-sounding but unsupported by comparison**
- Table I states the full-tension chain samples 17 parameters and lists the breakdown.
- This is presented like a careful bookkeeping detail, but the paper does not compare it against the 16-parameter Planck+BAO+SN chain in a way that explains why that difference matters for the reported posterior shifts.
- If parameter-count novelty is being implied, the paper does not substantiate it.

P1B-H1 — **“consistent with zero” hides a stronger numerical statement that should be foregrounded**
- The paper repeatedly says \(\Delta N_{\rm eff}\) is “consistent with zero.”
- But the actual quoted values are \(-0.020 \pm 0.169\) and \(+0.058 \pm 0.179\), which imply the posterior means are only \(\sim 0.1\text{–}0.3\sigma\) from zero.
- That delta should be stated explicitly wherever “consistent with zero” is used, otherwise the claim is too vague for PRD standards.

P1B-H2 — **“no model-selection statement is claimed” still leaves model-preference language too prominent**
- Sec. V says no \(\ln B\), AIC, or BIC is reported, but the surrounding prose still repeatedly invokes “quintom-B,” “phantom crossing,” and “posterior distance from \(\Lambda\)CDM.”
- Those phrases are not model-selection results.
- The body should separate descriptive posterior geometry from interpretive model preference much more sharply.

P1B-I1 — **Appendix C priors do not fully match the main-text interpretation of the spectator-safe subset**
- Appendix C gives the continuous-prior chain priors as \(\theta_i \in [0.01,\pi]\), \(\log_{10}(m_a/{\rm eV}) \in [-35,-30]\), and \(C_{a\gamma}\in [4,60]\).
- The main text, however, repeatedly interprets the spectator-safe corner as \(\theta_i \sim 0.1\), \(C_{a\gamma}\sim 8\), and \(\Omega_a<0.01\).
- The paper should state explicitly that the spectator-safe subset is an emergent posterior slice, not an imposed prior region.

P1B-I2 — **Appendix A says the repository is “program-wide” while the paper claims paper-specific reproducibility**
- The main text says “A reproducibility manifest is included in Appendix A.”
- Appendix A then says the repository includes code from other papers and program-wide components not used by this paper.
- This is a mismatch in reproducibility framing: the manifest is not paper-specific unless the relevant subdirectory is isolated from the broader repository contents.

P1B-J1 — **The sample-count arithmetic in Appendix A and Appendix C is not self-consistent**
- Appendix A says the two frozen \(\Lambda\)CDM+\(\Delta N_{\rm eff}\) chain directories contain the chains backing Table I, while the third Planck-only run is “not aggregated.”
- Appendix C separately says the ALP-MCMC results quoted in Sec. VI come from 9,720 total accepted samples across the three committed configurations.
- The paper does not provide a single consolidated sample-count map across the cosmology and ALP sections, so the reader cannot verify whether totals and subset counts are mutually exclusive or overlapping across the archived artifacts.

P1B-J2 — **Figure 3 and the body use slightly different best-recovery values**
- The body reports \(\hat\beta=0.238^\circ\) at \(\beta_{\rm inj}=0.27^\circ\) and \(\hat\beta=0.302^\circ\) at \(\beta_{\rm inj}=0.342^\circ\).
- Figure 3 caption also mentions a negative injection rerun giving \(-0.238^\circ\), but the caption and body do not present the positive and negative cases in an exactly parallel way.
- This is small, but it is a stale-style inconsistency that can confuse a careful reader about whether the 0.238 value is specific to the positive injection or sign-symmetric.

P1B-J3 — **The main text and Table II differ slightly in the \(w_0\), \(w_a\), and \(w_0+w_a\) rounding**
- The body rounds to \(w_0=-0.812\), \(w_a=-0.667\), \(w_0+w_a=-1.48\pm0.15\).
- Table II prints \(w_0=-0.8122\pm0.0436\), \(w_a=-0.6666\pm0.1864\), \(w_0+w_a=-1.4788\pm0.1485\).
- The values are consistent, but the manuscript should standardize the precision or explain why some sections use four decimals and others use three.

If you want, I can next turn this into a **PRD-style referee report** with severity labels, or produce a **single consolidated red-flag list** sorted by likelihood of blocking acceptance.