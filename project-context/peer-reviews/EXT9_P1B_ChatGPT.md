# EXT9 P1B — ChatGPT (in-thread delta round 9; recalibrated prompt)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded
**PDF**: paper1b_mcmc_companion_v1B.0.66.pdf · harvested 2026-06-13 13:27 PT
---
Referee report on Paper 1B v1B.0.66

Updated recommendation: MINOR REVISIONS.
The paper has moved toward publishability since v1B.0.65. The scientific core is now mostly publication-ready: the ΛCDM+ΔN
eff
	​

 proxy is properly scoped, the NaMaster estimator equation matches the unweighted implementation, the ALP spectator regime is quantitatively tabulated, and the w0wa result is no longer presented as a model-selection result. The remaining issues are mainly reproducibility-release synchronization and a small amount of interpretive wording.

1. Closure verification
A. Prior report’s fresh BLOCKER / MAJOR items
Prior item	Status	Verification
FB1. Public IMPLEMENTATION_MAP.md and KNOWN_GAPS.md stale and contradicting the manuscript	NOT ADDRESSED / still publication-condition	The PDF still points readers to IMPLEMENTATION_MAP.md and KNOWN_GAPS.md as part of the reproducibility package. 

paper1b_mcmc_companion_v1B.0.66

 Public IMPLEMENTATION_MAP.md still contains obsolete values such as H
0
	​

=69.2, ΔN
eff
	​

=0.3, χ
eff
2
	​

=1148.3, and lnB entries, all inconsistent with v1B.0.66. 
GitHub
 Public KNOWN_GAPS.md still says the paper reports/handles a “modified CAMB” spin-torsion Λ
eff
	​

(z) module and that Bayes factors are reported with caveats, both inconsistent with the current stock-CAMB/no-Bayes-factor paper. 
GitHub

FM1. v1B.0.65 changelog entry lacked the promised commit SHA	PARTIAL / REGRESSION	The public changelog has entries through v1B.0.65, but the v1B.0.65 entry still uses Commit: (this wave) rather than an actual SHA, and I did not find a public v1B.0.66 entry despite the PDF saying the v1B.0.66 URLs are recorded under that entry. 

paper1b_mcmc_companion_v1B.0.66

 The public changelog’s top Paper I(b) entry is v1B.0.65. 
GitHub

FM2. Public NaMaster summary.json still used old SNR/detection wording	NOT ADDRESSED	The PDF’s NaMaster wording is now acceptable, but public summary.json still says “NaMaster analysis confirms SNR=20.32 for beta=0.27 at ACT sensitivity” and still labels fields as paper1_prediction_deg and observed_value_deg. That remains weaker than the paper’s current “template-fit recovery, not sky-detection” caveat. 

paper1b_mcmc_companion_v1B.0.66

 
GitHub

FM3. ALP conclusion over-compressed the spectator-safe subset into m∼H
0
	​

 language	PARTIAL	The abstract and Table IV are much improved: the paper now states that the fixed-coupling posterior shifts to m≫H
0
	​

, and Table IV gives the Ω
a
	​

<0.01 spectator-safe subset with median m/H
0
	​

≃40.5, median C
aγ
	​

≃43.3, and 13% posterior mass. 

paper1b_mcmc_companion_v1B.0.66

 

paper1b_mcmc_companion_v1B.0.66

 The conclusion still begins the ALP summary with “f
a
	​

∼M
Pl
	​

,m∼H
0
	​

 is consistent,” which is technically true only as a scan-envelope statement and still too easy to misquote. 

paper1b_mcmc_companion_v1B.0.66

B. Original v1B.0.54 BLOCKERS / MAJORS, rechecked in v1B.0.66
Original issue	Status	Current assessment
B1. MCMC reproducibility artifacts contradicted Table I	PARTIAL	Table I values and counts now look scientifically consistent, and both frozen chains are described as committed and recomputed from raw chains. 

paper1b_mcmc_companion_v1B.0.66

 But the public release layer is still not fully synchronized: stale implementation/gaps docs, missing v1B.0.66 changelog entry, and raw corrected JSON files that still appear split across invalid raw-string newlines. 
GitHub
+3
GitHub
+3
GitHub
+3

B2. Spectator-ALP headline unsupported by posterior	PARTIAL, near closed	The quantitative issue is now mostly fixed by Table IV and the explicit m≫H
0
	​

, high-C
aγ
	​

, Ω
a
	​

<0.01 caveats. Remaining gap is wording in the conclusion, not missing analysis.
B3. w0wa empirical-anchor issue with overlapping SN samples	PARTIAL, acceptable if non-load-bearing	The overlap systematic is disclosed and no lnB, AIC, BIC, or model-selection claim is made. But the DES-SN5YR × Pantheon+ product likelihood remains overlap-uncorrected and the control chains are deferred, so the result should stay framed as a caveated cross-check, not a robust empirical anchor. 

paper1b_mcmc_companion_v1B.0.66


M1. 309,189 samples not independent posterior samples	CLOSED	The paper now consistently calls them raw/frozen samples and excludes the accumulating Planck-only run.
M2. Negative ΔN
eff
	​

 prior	CLOSED	The two-sided prior is stated, and one-sided ΔN
eff
	​

≥0 limits are now reported, including <0.40 from the Planck+BAO+SN chain. 

paper1b_mcmc_companion_v1B.0.66


M3. “ECH route via relativistic species” too strong	CLOSED	The proxy is now explicitly stock CAMB and not a spin-torsion Boltzmann-module test.
M4. DES-Y3 S
8
	​

 only a Gaussian prior	CLOSED	The likelihood stack now separates frozen ΔN
eff
	​

 chains from the iter2 w0wa chain and labels DES-Y3 as an S
8
	​

 Gaussian.
M5. NaMaster overstated as ACT-like observational pipeline	CLOSED	The paper repeatedly says this is synthetic CMB-only pseudo-C
ℓ
	​

 injection/recovery, not a sky detection or α/β separation.
M6. 12% under-recovery called unbiased	CLOSED	The paper now uses multiplicative-under-recovery and pipeline-recovery bias language, and Eq. (1) matches the unweighted estimator. 

paper1b_mcmc_companion_v1B.0.66


M7. SNR=20.32 needed demotion	CLOSED in PDF; artifact wording remains	The manuscript demotes it correctly; public summary.json still needs wording cleanup.
M8. ALP MCMC summary-likelihood scope	CLOSED	Appendix C and the body state that the ALP fits use the published Gaussian β summary, not EB spectra.
M9. Public repo versioning/pruning	PARTIAL	The paper-facing README is much better than earlier versions, but public docs and changelog are still not fully aligned to v1B.0.66.
2. Fresh pass — new findings only
Fresh BLOCKERS

None on the scientific content of the PDF.
I do not see a new load-bearing physics or methods blocker in v1B.0.66. The remaining publication-condition item is the already-open reproducibility-release synchronization problem: the PDF names a v1B.0.66 changelog entry and paper-facing docs that, in the public repository I inspected, are not yet synchronized.

Fresh MAJORS
F-M1. w0wa framing regressed slightly from “exploratory/provisional” to “published cross-check,” while the control chains remain deferred

Location: §III p. 4–5; §V.C p. 10; Conclusion p. 13–14.

The text now says the w0wa chain is a “published cross-check” of quintom-B under an overlap-uncorrected SN product likelihood, while also saying the DES-SN5YR/Pantheon+ overlap has not been tested by completed control chains and no model-selection statement is claimed. This is not fatal, because the caveat is explicit and the result is no longer advertised as a Bayes-factor or AIC/BIC preference. But “published cross-check of the quintom-B scenario” is still stronger than the evidence supports from a known double-counted SN likelihood. 

paper1b_mcmc_companion_v1B.0.66

Proposed fix: Use “caveated w0wa diagnostic” or “overlap-uncorrected cross-check of phantom-crossing geometry” in the conclusion. Keep the tail-distance numbers, but keep “quintom-B” as an interpretation contingent on the follow-up SN-overlap controls.

Fresh MINORS

Data-release synchronization must be completed before submission.
Location: Data and Code Availability p. 14; Appendix A p. 14–15.
Add the actual v1B.0.66 changelog entry, real commit SHA, and final DOI/tag references before arXiv/journal submission. This is a submission-condition item rather than scientific rework.

Corrected JSON files should be valid strict JSON.
The raw public corrected summaries still appear with _provenance split across two raw lines, which strict JSON parsers reject. Regenerate with escaped \n or a list-valued provenance field. 
GitHub
+1

Public docs need a stale-value grep before release.
Delete or update all obsolete H
0
	​

=69.2, ΔN
eff
	​

=0.3, modified-CAMB, χ
eff
2
	​

, lnB, and old w0wa-retraction language in the public paper-facing docs. 
GitHub
+1

NaMaster artifact labels should match the manuscript.
In summary.json, replace snr_namaster and “confirms SNR=20.32” with template_fit_recovery_snr and “not a sky-detection significance.” 
GitHub

PACS numbers remain.
Keep for PRD; remove for MNRAS/JCAP.

3. Recommendation

Recommendation: MINOR REVISIONS.
v1B.0.66 is substantially closer to publication than v1B.0.65: I would not require major scientific rework, but I would require the repository/changelog/docs/JSON synchronization and one w0wa/ALP wording pass before acceptance.
