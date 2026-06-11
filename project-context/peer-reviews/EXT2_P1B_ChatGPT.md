# EXT2 P1B — ChatGPT in-thread delta review
**Provider**: chatgpt.com Big Bounce Book project · Pro Extended (GPT-5.5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded
**PDF**: paper1b_mcmc_companion_v1B.0.56.pdf · **Harvested**: 2026-06-10 ~21:30 PDT
**Mode**: same-thread re-review (closure verification + fresh pass + updated verdict)

---

Show more
Thought for 8m 46s
Referee report on Paper 1B v1B.0.56

Updated recommendation: MAJOR REVISIONS.
The paper moved toward publishability since v1B.0.54: several scope/overclaim problems are materially improved, especially the NaMaster and ΔN
eff
	​

 presentation. However, the reproducibility release is still not publication-safe, the ALP headline remains stronger than the posterior supports, and the w0–wa/SN-overlap issue is disclosed rather than fixed. I read the revised PDF end-to-end. 

paper1b_mcmc_companion_v1B.0.56

1. Closure verification against my original BLOCKERS / MAJORS
Original BLOCKERS
Original item	Status	Verification
B1. Public reproducibility artifacts contradict/fail to verify Table I MCMC values	PARTIAL / REGRESSION	The off-by-one/column-permutation bug is now correctly identified for the full-tension artifact, and parameter_summary_CORRECTED.json gives physically sensible full-tension values matching Table I. The accompanying README explains the wrong-column bug and gives the verification command. 
GitHub
+1
 But this is not complete: the Planck+BAO+SN diagnostics directory still contains only convergence_report.txt, with no corrected summary/README, and that report still includes the shifted parameter-summary values. 
GitHub
+1
 There is also a new inconsistency: freeze_diagnostics_CORRECTED.json says total_accepted_samples: 176840, whereas the manifest and paper use 176,240. 
GitHub
+1
 Finally, the PDF now claims a v1B.0.56 tag and README-pinned HuggingFace DOIs, but the advertised tag/tree path did not resolve during review, and the main reproducibility README still shows stale v0.9.0-era values. 

paper1b_mcmc_companion_v1B.0.56

 
Website Name Not Available
+1

B2. Spectator-ALP headline unsupported by the posterior	PARTIAL	The revision is much more honest: it now states the posterior median m≃36H
0
	​

, reports C
aγ
	​

 burdens, gives Ω
a
	​

<0.1 and Ω
a
	​

<0.01 posterior fractions, and quantifies the θ
i
	​

≤0.1 sliver. 

paper1b_mcmc_companion_v1B.0.56

 But the abstract/conclusion still say an ALP with f
a
	​

∼M
Pl
	​

,m∼H
0
	​

 is consistent with the signal, and §VI still says the model accommodates the signal for “natural parameter values.” That remains too strong given the paper’s own posterior: m≃36H
0
	​

, non-minimal C
aγ
	​

, only 13% posterior mass at Ω
a
	​

<0.01, and only 0.33% at strict θ
i
	​

≤0.1.
B3. w0–wa “quintom-B empirical anchor” introduced without justified SN likelihood stack	PARTIAL	The DES-SN5YR/Pantheon+ overlap is now disclosed, including the approximate 20% shared-SN issue and the lack of joint covariance. 

paper1b_mcmc_companion_v1B.0.56

 But the analysis still uses a naive product likelihood and still presents the chain as a “quintom-B empirical anchor.” The claimed bias direction is asserted, not demonstrated by re-running mutually exclusive SN stacks. Also, the comparison-analysis citation is wrong: the relevant paper is the DES Collaboration/Vincenzi et al. comparison of DES-SN5YR and Pantheon+, not the DES-SN5YR cosmology-results paper currently cited as [14]. 
arXiv
Original MAJORS
Original item	Status	Verification
M1. 309,189 should not be called independent posterior samples	CLOSED	The revised text now calls these “raw samples” in §III and explicitly excludes the Planck-only run from the headline. The sample-count reconciliation footnote is much clearer.
M2. Negative ΔN
eff
	​

 prior makes “extra species” framing incomplete	CLOSED	The revised §III adds one-sided ΔN
eff
	​

≥0 95% upper limits and defines the renormalised posterior convention.
M3. “standard-ECH route to dark energy via additional relativistic species” too strong	PARTIAL	Fig. 2 is fixed: it now says no recombination-era ΔN
eff
	​

 shift appears and that this does not directly test the ECH spin-torsion sector. 

paper1b_mcmc_companion_v1B.0.56

 But §III/Conclusion still say current data “neither require nor exclude a spin-torsion ΔN
eff
	​

 contribution,” despite the paper also saying the surviving Hehl-Datta-Mercuri contact interaction does not produce recombination-era ΔN
eff
	​

. That residual language should be replaced with “neither require nor exclude a phenomenological radiation-like proxy.”
M4. “full-tension” DES-Y3 S
8
	​

 treatment only a compressed Gaussian prior	CLOSED	Table I now explicitly states that DES-Y3 enters as a Gaussian S
8
	​

 prior and even explains the resulting combined posterior.
M5. NaMaster validation overstated as ACT-like pipeline	CLOSED	The abstract and §IV now repeatedly state that this is a synthetic CMB-only pseudo-C
ℓ
	​

 validation, not a sky detection or α/β separation test.
M6. Do not call 12% under-recovery “unbiased”	CLOSED	The revised §IV explicitly says the estimator is not unbiased in the standard statistical sense and calls the 0.040
∘
 number an empirical multiplicative-bias floor. 

paper1b_mcmc_companion_v1B.0.56


M7. Demote/rename SNR=20.32	CLOSED	The SNR is now clearly defined as a template-fit injected-signal recovery quantity, not a sky-detection significance, and the per-realization angle ratio is separately reported. 

paper1b_mcmc_companion_v1B.0.56


M8. ALP MCMC is summary-likelihood, not independent data fit	CLOSED	The revised Appendix C and Fig. 4 caption repeatedly state that all ALP fits use the same Gaussian summary likelihood on the published β, not EB spectra.
M9. Public repo should be versioned/pruned for this paper	REGRESSION	The paper now claims a v1B.0.56 tag, exact SHA in CHANGELOG.md, and README-pinned HuggingFace DOIs, but I could not resolve the advertised tag path; the public main README is still stale and says v0.9.0 with obsolete results such as H
0
	​

=69.2, ΔN
eff
	​

≈0.3, and no CMB map analysis. 

paper1b_mcmc_companion_v1B.0.56

 
Website Name Not Available
+1
2. Fresh pass — new findings only
Fresh BLOCKERS
F-B1. The revised data-availability section now makes false or unverifiable release claims

Location: Data and Code Availability, p. 12–13; Appendix A, p. 13–14.
Problem: The PDF states that the repository version corresponding to the paper is tagged v1B.0.56, that the exact commit SHA is in CHANGELOG.md, and that HuggingFace dataset DOIs are listed in the README at that tag. During review, the advertised tag/tree path returned 404, the main CHANGELOG.md raw path also did not resolve, and the public main README remains the old v0.9.0 reproducibility README. 
Website Name Not Available
+2
+2
 This is a publication blocker because the paper’s reproducibility claims depend on immutable artifact identity.

Proposed fix: Before submission, create an immutable GitHub release/tag actually named in the paper, include the exact commit SHA in the paper itself, update the tagged README, and put the three dataset DOI URLs directly in the paper rather than only in a mutable README. If the tag is intended to be paper1b-v1B.0.56 rather than v1B.0.56, use that exact name everywhere.

F-B2. Corrected MCMC diagnostics are only partially propagated

Location: Data and Code Availability, p. 12–13; Appendix A, p. 13; Table I, p. 16.
Problem: The full-tension corrected summary exists, but the Planck+BAO+SN diagnostics directory still lists only convergence_report.txt; it has no parameter_summary_CORRECTED.json or equivalent README. 
GitHub
 The remaining Planck+BAO+SN convergence report still contains a shifted “Parameter summary” where H
0
	​

-like values appear under nuisance labels such as amp_217, exactly the class of problem identified in the original review. 
GitHub
 The full-tension corrected diagnostic also introduces a new count mismatch: total_accepted_samples is 176,840, while the manifest and manuscript use 176,240. 
GitHub
+1

Proposed fix: Add corrected diagnostics for both frozen chains, not just full tension. Include a single machine-readable table1_reproduction.json with the two Table I columns and all seven parameters, plus raw count, 30% post-burn count, ESS, and 
R
^
−1. Add a CI/check script that compares this file to the manuscript table and fails on any count or parameter mismatch.

Fresh MAJORS
F-M1. DES-SN5YR/Pantheon+ overlap caveat cites the wrong paper

Location: §III caveat (e), p. 4; References, p. 14–15.
Problem: The manuscript tells readers to “refer to the DES Collaboration comparison analysis [14],” but [14] is the DES-SN5YR cosmology-results paper, not the DES/Pantheon+ comparison paper. The actual comparison paper is Vincenzi et al., “Comparing the DES-SN5YR and Pantheon+ SN cosmology analyses,” which explicitly discusses the 20% overlap and Malmquist-bias correction differences. 

paper1b_mcmc_companion_v1B.0.56

 
arXiv

Proposed fix: Add the Vincenzi et al. comparison paper as a separate reference and cite it in the overlap caveat. Keep the DES-SN5YR cosmology paper cited only for the DES-SN5YR likelihood itself.

F-M2. The w0–wa result remains too prominent for a caveated, overlap-uncorrected likelihood

Location: §III “Physics interpretation,” p. 3–4; Table II, p. 17; Conclusion, p. 12.
Problem: The paper now admits DES-SN5YR and Pantheon+ are multiplied as independent likelihood factors without a joint covariance, but it still calls the result a “Quintom-B empirical anchor” and an “empirical test of the quintom-B scenario.” Disclosure is not enough here: the result is not just mildly caveated; the stated likelihood is knowingly non-independent.

Proposed fix: Demote this to “exploratory w0–wa cross-check” unless the paper adds at least two control chains: DESI+Planck+Pantheon+ only and DESI+Planck+DES-SN5YR only. The overlap-corrected joint run can remain deferred, but the current combined run should not be called an empirical anchor.

F-M3. Data Availability says the ΛCDM+ΔN
eff
	​

 chains are “not pre-computed,” but the paper also points to frozen chain files

Location: Data and Code Availability, p. 12–13; Appendix A, p. 13.
Problem: Appendix A says the ΛCDM+ΔN
eff
	​

 proxy chains are not pre-computed and must be regenerated, but the corrected full-tension README explicitly verifies values by loading chain files in the frozen directory, and the GitHub directory contains chains/chain_01 through chain_06. 

paper1b_mcmc_companion_v1B.0.56

 
GitHub
+1

Proposed fix: Replace “not pre-computed” with a precise statement: either “chains are committed in the frozen artifact directories” or “chains are not included in the tagged release; only diagnostics are included.” The current wording is contradictory.

F-M4. The ALP “natural parameters” phrasing still conflicts with the quantified tuning/coupling burden

Location: §I scope item 3, p. 2; §VI caveats, p. 12; Conclusion, p. 12.
Problem: The revision did add the needed numbers, but then retains the old headline phrase. The paper’s own ALP section says the fixed-C
aγ
	​

=8 posterior has θ
i
	​

=1.32±0.41 and median m≃36H
0
	​

, while the strict θ
i
	​

≤0.1 sliver is only 0.33% by MC weight and the Ω
a
	​

<0.01 subset is only 13% of the posterior mass. Calling this “natural parameter values” remains misleading.

Proposed fix: Use this wording consistently: “The ALP summary-likelihood fit can accommodate the observed β, but the spectator-safe interpretation requires a tuned misalignment subspace and non-minimal photon coupling.” Remove “natural parameter values” from the abstract, §I, §VI caveats, and conclusion.

Fresh MINORS

PR3/PR4/NPIPE wording still invites confusion. The abstract footnote explains that the published Eskilt & Komatsu paper is PR3+WMAP9 while the code-repository rerun uses PR4/NPIPE, but §VI still phrases the headline observational constraint as “published … joint WMAP9 + Planck PR4/NPIPE.” Make every occurrence either “published PR3+WMAP9” or “repository PR4/NPIPE rerun,” not both.

The CMB-S4 sentence should not say “spin-torsion ΔN
eff
	​

 contribution.” Use “phenomenological ΔN
eff
	​

 proxy” unless a concrete ECH Boltzmann prediction is supplied. 

paper1b_mcmc_companion_v1B.0.56

PACS numbers remain. Remove unless the target journal specifically requests them.

Table IV still says “Verified” for claims whose public release is not yet cleanly versioned. Change to “internally verified / pending tagged public artifact” until the tag, DOI links, and corrected diagnostics are actually in place.

Appendix C says the C
aγ
	​

∈[4,60] prior covers the “full EOM-required band [9,51],” while §VI also says the natural-box requirement can extend to ∼160. Clarify that [9,51] is the posterior-supported band, not the full natural-box kinematic requirement.

3. Updated recommendation

Recommendation: MAJOR REVISIONS.
The revised manuscript is substantially more careful than v1B.0.54, especially on NaMaster and ΔN
eff
	​

, but it still needs a clean, immutable reproducibility release and further demotion of the ALP and w0–wa claims before it is publishable.

Sources

Pro Extended

