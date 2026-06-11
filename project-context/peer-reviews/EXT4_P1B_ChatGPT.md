# EXT4 P1B — ChatGPT Pro Extended (in-thread delta round 4)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded
**PDF**: paper1b_mcmc_companion_v1B.0.58.pdf (74e0cc28) · harvested 2026-06-11 15:53 PT
---
Referee report on Paper 1B v1B.0.58

Updated recommendation: MAJOR REVISIONS.
The manuscript moved toward publishability since v1B.0.57: the scientific prose is now substantially better scoped, especially for PR3/PR4, ΔN
eff
	​

, NaMaster, and the w0wa result. However, the paper still has publication-blocking reproducibility-release defects, and the ALP spectator-safe interpretation remains only partially closed.

1. Closure verification
A. Closure against my original v1B.0.54 BLOCKERS / MAJORS
Original issue	Status	Verification
B1. Public reproducibility artifacts contradicted or failed to verify Table I MCMC values	PARTIAL / REGRESSION	Numerically, the correction is much improved: both corrected summaries now contain all seven Table I parameters, including S
8
	​

, and the reported means match Table I to rounding. The PDF also states that the corrected summaries supersede the legacy column-permuted exports. 

paper1b_mcmc_companion_v1B.0.58

 However, both public parameter_summary_CORRECTED.json files still appear to be invalid JSON: the _provenance string contains a raw newline between line 0 and line 1. That will break standard json.load/jq reproducibility checks. 
GitHub
+1
 There is also a release-pinning regression: the PDF says the v1B.0.58 URLs are recorded in the root CHANGELOG.md, but the public CHANGELOG.md contains entries through v1B.0.57 and v1B.0.56, not v1B.0.58. 

paper1b_mcmc_companion_v1B.0.58

 
GitHub

B2. Spectator-ALP headline unsupported by the posterior	PARTIAL	The revision is much more candid. It now states the m≃36H
0
	​

 posterior median, the C
aγ
	​

 coupling burden, the Ω
a
	​

<0.1 and Ω
a
	​

<0.01 posterior fractions, the θ
i
	​

≤0.1 sliver, and the fact that the same birefringence is not an ECH-specific prediction. The remaining gap is that the conclusion still summarizes the spectator-consistent regime as “θ
i
	​

∼0.1,” but θ
i
	​

∼0.1 is not spectator-safe over the posterior mass range when m/H
0
	​

 can be tens. The load-bearing restriction should be Ω
a
	​

<ϵ, not a fixed θ
i
	​

 shorthand.
B3. w0wa “quintom-B empirical anchor” used without justified SN likelihood stack	PARTIAL	The conclusion is now correctly demoted to “Exploratory w0wa cross-check,” explicitly called overlap-uncorrected and provisional pending SN-overlap control chains. 

paper1b_mcmc_companion_v1B.0.58

 The body also now cites Vincenzi et al. for the ∼20% DES-SN5YR/Pantheon+ overlap and Malmquist-correction differences. 

paper1b_mcmc_companion_v1B.0.58

 But the actual likelihood is still the naive product of overlapping SN samples; the Pantheon+-only and DES-SN5YR-only controls are still queued rather than complete.
M1. 309,189 samples should not be called independent posterior samples	CLOSED	The manuscript consistently describes these as raw/frozen samples and excludes the Planck-only accumulating run from the headline.
M2. Negative ΔN
eff
	​

 prior makes “extra species” framing incomplete	CLOSED	The paper now states that the prior is two-sided and reports one-sided ΔN
eff
	​

≥0 95% upper limits with a clear renormalised-posterior definition.
M3. “Standard-ECH route to dark energy via relativistic species” too strong	CLOSED	The proxy is now framed as a stock-CAMB phenomenological radiation-like test, not a direct ECH spin-torsion Boltzmann-module test. 

paper1b_mcmc_companion_v1B.0.58


M4. Full-tension DES-Y3 S
8
	​

 treatment only a compressed Gaussian prior	CLOSED	Table I explicitly states the DES-Y3 Gaussian S
8
	​

 prior, the naive Gaussian-combination check, and the within-stack interpretation of the residual. 

paper1b_mcmc_companion_v1B.0.58


M5. NaMaster validation overstated as ACT-like observational pipeline	CLOSED	The paper repeatedly states that the NaMaster run is a synthetic CMB-only pseudo-C
ℓ
	​

 recovery test, not a sky detection or α/β separation measurement. 

paper1b_mcmc_companion_v1B.0.57


M6. Do not call 12% under-recovery “unbiased”	CLOSED	The text now uses calibrated-bias / multiplicative-under-recovery language and explicitly says the estimator is not unbiased in the standard statistical sense.
M7. SNR=20.32 should be demoted or renamed	CLOSED	The SNR is defined as a template-fit injected-signal recovery SNR, not a sky-detection significance.
M8. ALP MCMC is summary-likelihood, not independent data fit	CLOSED	The abstract footnote, §VI, and Appendix C now state that the ALP chains use only the scalar Gaussian summary likelihood β=0.342
∘
±0.094
∘
, not EB spectra.
M9. Public repository should be versioned/pruned for this paper	PARTIAL / REGRESSION	The root README is much better and now has Paper I(b) quick links. 
GitHub
 But v1B.0.58 is not present in the public CHANGELOG.md despite the PDF claiming it is, the corrected JSON artifacts still appear machine-invalid, and no immutable public tag/release pins v1B.0.58. 
GitHub
+2
GitHub
+2
B. Closure of the fresh blockers/majors from my v1B.0.57 report
v1B.0.57 issue	Status	Verification
F-B1. Planck+BAO+SN corrected diagnostic invalid JSON	NOT CLOSED / REGRESSION	The Planck+BAO+SN file still appears to contain an unescaped raw newline inside _provenance; the regenerated full-tension corrected file now appears to have the same problem. 
GitHub
+1

F-B2. HuggingFace DOI/URL wording not actually backed	PARTIAL / REGRESSION	The PDF now correctly says DOI assignment is pending and lists the three HuggingFace URLs directly in Appendix A. 

paper1b_mcmc_companion_v1B.0.58

 But it also says the URLs are recorded under a v1B.0.58 CHANGELOG.md entry; the public root changelog has no v1B.0.58 entry. 
GitHub

F-M1. Corrected summary did not reproduce all seven Table I parameters	PARTIAL	The full-tension corrected summary now includes S
8
	​

, closing the numerical omission. 
GitHub
 The file still appears not to be parseable JSON, so the machine-checkable closure is incomplete.
F-M2. w0wa result too prominent for overlap-uncorrected likelihood	PARTIAL	The conclusion now calls it an exploratory, overlap-uncorrected, provisional cross-check, which is a real improvement. 

paper1b_mcmc_companion_v1B.0.58

 The body still presents the w
0
	​

,w
a
	​

 posterior in strong “canonical quintom signature” language before the caveat, and the controls are still pending.
F-M3. PR3/PR4/NPIPE wording conflicted with summary likelihood	CLOSED	The abstract footnote now says the ALP MCMC uses only the scalar Gaussian summary likelihood and does not depend on the PR3/PR4 map-level distinction except through the summary value’s provenance. 

paper1b_mcmc_companion_v1B.0.58

2. Fresh pass — new or still-current findings only
BLOCKERS
FB1. The v1B.0.58 public release layer is still not publication-safe

Location: Data and Code Availability, p. 13; Appendix A, p. 14; public CHANGELOG.md; public corrected JSON artifacts.

Problem: The paper now says v1B.0.58 is identified by the in-tex stamp and the matching version-stamp commit in the repository log, with URLs recorded in the root CHANGELOG.md under v1B.0.58. The public source file does have \newcommand{\paperVersion}{v1B.0.58}, but the public root CHANGELOG.md has no v1B.0.58 entry; it stops at v1B.0.57 for Paper I(b). 
GitHub
+1
 The two corrected JSON files also appear not to be valid JSON due to raw newlines inside _provenance, even though these are now the named authority for Table I reproducibility. 
GitHub
+1

Proposed fix: Add the v1B.0.58 entry to root CHANGELOG.md with the exact commit SHA and dataset URLs. Regenerate every parameter_summary_CORRECTED.json with escaped provenance or a provenance list, then verify with python -m json.tool or jq . in CI. Do not submit until the PDF, .tex, root changelog, and public corrected JSON artifacts agree.

MAJORS
FM1. The root reproducibility README still contradicts the manuscript in its “What This Bundle Reproduces” table

Location: Data and Code Availability, p. 13; public reproducibility/README.md.

Problem: The README is improved because it now has Paper I(b) quick links and explicitly points to corrected summaries with all seven Table I parameters. 
GitHub
 But lower down it still describes the “full-tension configuration” as “Planck NPIPE + BAO + Pantheon+ + DES-SN5YR + DESI DR2,” while the manuscript says DESI DR2 enters only the separate w0wa chain and the frozen ΛCDM+ΔN
eff
	​

 chains use SDSS BAO, not DESI DR2. 

paper1b_mcmc_companion_v1B.0.58

 The README also says χ
eff
2
	​

, AIC, and BIC are reproducible “YES,” whereas the paper explicitly omits AIC/BIC/lnB and defers controlled evidence/model-comparison statistics to nested sampling. 
GitHub

Proposed fix: Split the README’s Paper I(a) and Paper I(b) sections cleanly. For Paper I(b), list exactly: frozen ΛCDM+ΔN
eff
	​

 Table I chains, NaMaster artifacts, ALP summary-likelihood chains, and the exploratory iter2 w0wa chain. Remove “AIC/BIC YES” unless those exact values are actually reported in the paper.

FM2. The spectator-safe ALP condition is still summarized by an unsafe shorthand

Location: Abstract, p. 1; §VI, p. 9–11; Conclusion, p. 12.

Problem: The text now provides the important numbers: m≃36H
0
	​

, C
aγ
	​

 burden, Ω
a
	​

<0.1 and Ω
a
	​

<0.01 posterior fractions, and the θ
i
	​

≤0.1 sliver. But the conclusion still says the “spectator-consistent regime” is θ
i
	​

∼0.1. That shorthand is only meaningful near m∼H
0
	​

; for the posterior-preferred m/H
0
	​

≫1, spectator safety requires a much smaller θ
i
	​

 unless the energy-density calculation is defined differently. The paper’s own Ω
a
	​

<0.01 subset is the correct restriction, not θ
i
	​

∼0.1.

Proposed fix: Replace every “spectator-consistent regime θ
i
	​

∼0.1” summary with “the Ω
a
	​

<0.01 spectator-safe subset.” Add a tiny table for that subset with posterior mass, β, m/H
0
	​

, θ
i
	​

, and C
aγ
	​

 percentiles. This would close the ALP issue.

FM3. The w0wa result is still too emphatic in §III relative to its provisional status

Location: §III, p. 3–5; Table II, p. 18; Conclusion, p. 12.

Problem: The conclusion correctly demotes the result to an “exploratory, overlap-uncorrected test” pending queued SN-overlap control chains. 

paper1b_mcmc_companion_v1B.0.58

 But the first body presentation still says the posterior is a “canonical quintom signature,” “centered well into quintom-B territory,” and “consistent with the bounce / pre-Big-Bang scenario” before the reader reaches the overlap caveat. 

paper1b_mcmc_companion_v1B.0.58

 That ordering still gives the result more evidentiary weight than an uncorrected product likelihood with overlapping SN samples should carry.

Proposed fix: Move the w0wa discussion to a clearly labelled “Exploratory w0wa cross-check” subsection or appendix. At first mention, state that the SN-overlap controls are pending and that the quoted +4.3σ/−3.6σ marginal-tail distances are provisional.

FM4. The “quintom-B scenario” citation in the conclusion points to the DESI DR2 paper, not a quintom reference

Location: Conclusion, p. 12; References, p. 15–16.

Problem: The conclusion says the exploratory w0wa chain is a test of the quintom-B scenario “[19].” In this bibliography, [19] is the DESI DR2 BAO/cosmological-constraints paper, while the quintom theory review is [27]. 

paper1b_mcmc_companion_v1B.0.58

Proposed fix: Change the citation after “quintom-B scenario” to the quintom review, or cite both DESI DR2 for the BAO data and the quintom reference for the model interpretation.

MINORS

Data Availability still has one ambiguous chain sentence.
Location: Data and Code Availability, p. 13.
“MCMC chains: regenerate via reproduce_cosmology.sh” reads as if no chains are included, while Appendix A says the two frozen chain directories are committed. Replace with: “Frozen chains are committed; fresh re-verification chains can be regenerated via reproduce_cosmology.sh.”

The public README’s birefringence row still uses confusing PR4 wording.
Location: public reproducibility/README.md.
It calls β≃0.27
∘
 a “literature value (WMAP+Planck PR4),” while the paper now correctly says the headline β=0.342
∘
±0.094
∘
 is PR3+WMAP9 and the ALP 0.27
∘
 is a model/fiducial consistency value. Fix the README to match the manuscript. 

paper1b_mcmc_companion_v1B.0.58

 
GitHub

PACS numbers remain.
Location: p. 1.
Retain only if PRD is the target; remove for MNRAS or JCAP.

3. Recommendation

Recommendation: MAJOR REVISIONS.
v1B.0.58 is scientifically clearer and closer to publishable than v1B.0.57, but I would not accept it until the v1B.0.58 public reproducibility layer is machine-valid and actually pinned, and until the ALP and w0wa summaries are made fully consistent with their own caveats.
