# EXT6 P1B — ChatGPT Pro Extended (in-thread delta round 6)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded
**PDF**: paper1b_mcmc_companion_v1B.0.62.pdf (e0066b42) · harvested 2026-06-12 19:52 PT

---

Referee report on Paper 1B v1B.0.62

Updated recommendation: MAJOR REVISIONS.
The manuscript has moved toward publishability since v1B.0.60: the ΔN
eff
	​

 one-sided limit is now chain-computed, the w0wa overlap caveat is front-loaded, the ALP spectator subset is explicitly tabulated, and the BBN/Y
He
	​

 treatment is documented. However, two publication-level reproducibility issues remain: the public v1B.0.62 release layer is not internally consistent, and the manuscript claims an explicit PArthENoPE YAML flag that is not present in the public YAML files I inspected.

1. Closure verification against original BLOCKERS / MAJORS
Original issue	Status	Verification
B1. Public reproducibility artifacts contradicted or failed to verify Table I MCMC values	PARTIAL / REGRESSION	Numerically, the Table I values are now much more coherent: v1B.0.62 reports 176,240+132,949=309,189 raw samples, ΔN
eff
	​

=−0.020±0.169 and +0.058±0.179, H
0
	​

=67.68±1.06 and 67.78±1.09, and min ESS 4744/4692. 

paper1b_mcmc_companion_v1B.0.62

 The paper also states that both frozen chain directories are committed and that the corrected summaries supersede the legacy column-permuted export. 

paper1b_mcmc_companion_v1B.0.62

 But closure is incomplete: the raw public parameter_summary_CORRECTED.json files for both frozen chains still appear to be invalid JSON because the _provenance string spans a raw newline; the root public changelog has no v1B.0.62 entry, and the public README currently identifies Paper I(b) as v1B.0.61 rather than v1B.0.62. 
GitHub
+3
GitHub
+3
GitHub
+3

B2. Spectator-ALP headline unsupported by the posterior	PARTIAL	The scientific framing is much improved. The abstract now says the scan-prior m∼H
0
	​

 region brackets the signal, but the fixed-C
aγ
	​

=8 posterior shifts to m≫H
0
	​

, with median m≃36H
0
	​

, and that only the Ω
a
	​

<0.01 subset is spectator-safe. 

paper1b_mcmc_companion_v1B.0.62

 Table IV now gives posterior masses for the full chain, Ω
a
	​

<0.1, Ω
a
	​

<0.01, and θ
i
	​

≤0.1. 

paper1b_mcmc_companion_v1B.0.62

 Remaining gap: the Ω
a
	​

<0.01 table row still reports qualitative placeholders such as “post.-supported” and “smaller-weighted” rather than actual m/H
0
	​

,θ
i
	​

,C
aγ
	​

 percentiles. The text also still uses “scan-prior midpoint values” in a way that overstates the naturalness of the benchmark.
B3. w0wa “quintom-B empirical anchor” introduced without justified SN likelihood stack	PARTIAL	The main §III interpretation now front-loads the key caveat: the w0wa posterior is provisional under an overlap-uncorrected DES-SN5YR × Pantheon+ product likelihood, and no model-selection statement is claimed pending SN-overlap controls. 

paper1b_mcmc_companion_v1B.0.62

 The conclusion now calls it an exploratory, overlap-uncorrected test. 

paper1b_mcmc_companion_v1B.0.62

 But the analysis still uses the overlap-uncorrected product likelihood, and §V still labels the result “the canonical quintom signature” after giving w
0
	​

=−0.812±0.044, w
a
	​

=−0.667±0.186, and w
0
	​

+w
a
	​

=−1.48±0.15. 

paper1b_mcmc_companion_v1B.0.62


M1. 309,189 samples should not be called independent posterior samples	CLOSED	The manuscript consistently treats this as a raw/frozen sample count across two frozen combinations and excludes the accumulating Planck-only chain from the headline. 

paper1b_mcmc_companion_v1B.0.62


M2. Negative ΔN
eff
	​

 prior makes “extra species” framing incomplete	CLOSED	The prior is explicitly two-sided, N
eff
	​

∈[2.046,5.046], and the one-sided ΔN
eff
	​

≥0 limits are reported as ΔN
eff
	​

<0.31 and <0.40, with the Planck+BAO+SN limit recomputed from the committed 30%-burn-in chain. 

paper1b_mcmc_companion_v1B.0.62


M3. “standard-ECH route to dark energy via additional relativistic species” too strong	CLOSED	The manuscript now states that the stock-CAMB ΔN
eff
	​

 proxy does not test the ECH spin-torsion sector directly and would require a bespoke modified Boltzmann code for that. 

paper1b_mcmc_companion_v1B.0.62


M4. Full-tension DES-Y3 S
8
	​

 treatment only a compressed Gaussian prior	CLOSED	The frozen-chain stack is now clearly separated from the iter2 w0wa stack: no DESI BAO enters the frozen ΛCDM+ΔN
eff
	​

 chains, and DES-Y3 enters the full-tension chain as an S
8
	​

 Gaussian. 

paper1b_mcmc_companion_v1B.0.62

 The current public README also reflects this corrected stack. 
GitHub

M5. NaMaster validation overstated as ACT-like observational pipeline	CLOSED	The paper repeatedly states that this is a synthetic CMB-only pseudo-C
ℓ
	​

 injection/recovery validation, not a sky detection or α/β separation measurement. 

paper1b_mcmc_companion_v1B.0.62


M6. Do not call 12% under-recovery “unbiased”	CLOSED	The estimator is now described as having ∼12% multiplicative under-recovery, with the 0.040
∘
 value carried as an empirical pipeline-recovery floor rather than an unbiased-estimator statement. 

paper1b_mcmc_companion_v1B.0.62


M7. SNR=20.32 should be demoted or renamed	CLOSED	The SNR is described as a template-fit recovery SNR for injected MC signals, not the significance of a recovered angle or a sky-detection significance. 

paper1b_mcmc_companion_v1B.0.62


M8. ALP MCMC is summary-likelihood, not independent data fit	CLOSED	Appendix C states that all ALP fits use a Gaussian summary likelihood on the published Eskilt–Komatsu β
obs
	​

=0.342
∘
±0.094
∘
, not a re-analysis of EB spectra; ACT DR6 is only an external cross-check. 

paper1b_mcmc_companion_v1B.0.62


M9. Public repo should be versioned/pruned for this paper	PARTIAL / REGRESSION	The manuscript now says the public tagged release is pending and lists the HuggingFace dataset URLs directly, which is more honest. 

paper1b_mcmc_companion_v1B.0.62

 But the paper also claims the URLs are recorded in the repository CHANGELOG under v1B.0.62; the public changelog I inspected has no v1B.0.62 entry and the public README still points to v1B.0.61. 
GitHub
+1
2. Fresh pass — new/current findings
BLOCKERS
FB1. The v1B.0.62 public artifact layer is still not machine-publication-safe

Location: Data and Code Availability, p. 13–14; Appendix A, p. 14–15; public CHANGELOG.md; public corrected JSON artifacts.

Problem: The paper states that the repository version is identified by the in-tex v1B.0.62 stamp and matching version-stamp commit, and that the dataset URLs are recorded in CHANGELOG.md under v1B.0.62. 

paper1b_mcmc_companion_v1B.0.62

 The public .tex file does contain \paperVersion{v1B.0.62}, but the public changelog currently starts Paper I(b) at v1B.0.61 and contains no v1B.0.62 entry that pins the commit, dataset URLs, or checksums. 
GitHub
+1

The two corrected JSON summaries also still appear not to be valid JSON because the _provenance string is split by a raw newline in the raw files. This is a direct reproducibility blocker because those files are the named corrected replacements for the legacy column-permuted exports. 
GitHub
+1

Proposed fix: Add the v1B.0.62 changelog entry with exact commit SHA, artifact URLs, and checksums. Update the public README’s Paper I(b) version to v1B.0.62. Regenerate both parameter_summary_CORRECTED.json files with escaped provenance or a list-valued provenance field, then run python -m json.tool or jq . in CI on every JSON artifact before submission.

FB2. The manuscript claims an explicit PArthENoPE YAML flag that is absent from the public YAMLs

Location: §III, p. 3; public Cobaya YAML files.

Problem: The manuscript says the BBN predictor is explicitly pinned as bbn_predictor: 'PArthENoPE' in theory.camb.extra_args of each Cobaya YAML. 

paper1b_mcmc_companion_v1B.0.62

 In the public YAMLs I inspected, the theory.camb.extra_args blocks include settings such as lens_potential_accuracy and num_massive_neutrinos, but not bbn_predictor or an equivalent explicit PArthENoPE flag. 
GitHub
+3
GitHub
+3
GitHub
+3

This does not necessarily invalidate the physics result if CAMB’s default BBN-consistency module was used, but it does invalidate the stronger reproducibility claim that the BBN predictor was explicitly pinned in the YAMLs.

Proposed fix: Either add the correct CAMB/Cobaya BBN-predictor option to all four YAMLs and rerun or verify that results are unchanged, or rewrite the paper to say: “CAMB’s default BBN-consistency setting was used; no explicit BBN-predictor override appears in the YAMLs.” If the intended flag name differs from bbn_predictor, quote the exact public YAML key and path.

MAJORS
FM1. §V still overstates the w0wa result relative to the overlap-uncorrected likelihood

Location: §III p. 4–5; §V.B p. 9; Table II p. 19; Conclusion p. 13.

Problem: The §III caveat is now appropriately front-loaded, but §V.B still presents the w0wa result as “the headline result” and calls w
0
	​

+w
a
	​

=−1.48±0.15 “the canonical quintom signature.” 

paper1b_mcmc_companion_v1B.0.62

 Table II itself reports the marginal-tail distances but also clearly states the DESI DR2 + Planck + DES-Y5 + Pantheon+ likelihood stack. 

paper1b_mcmc_companion_v1B.0.62

 The SN-overlap controls remain queued rather than complete, so the body should not present this as a headline result in the same section titled “Model Comparison.”

Proposed fix: Rename §V.B’s w0wa paragraph to “Exploratory overlap-uncorrected w0wa cross-check.” Replace “headline result” and “canonical quintom signature” with “provisional phantom-crossing posterior under the current overlap-uncorrected product likelihood.” Keep +4.3σ/−3.6σ only as marginal-tail distances.

FM2. The ALP “scan-prior midpoint” phrasing remains misleading

Location: Introduction p. 2; §VI p. 9–12; Conclusion p. 13.

Problem: The paper now correctly says the fixed-C
aγ
	​

=8 posterior prefers median m≃36H
0
	​

 and that the Ω
a
	​

<0.01 subset is tuned. 

paper1b_mcmc_companion_v1B.0.62

 However, §VI still says the same prediction arises in GR “at scan-prior midpoint values.” That is not what the detailed calculation shows: Eq. (3) obtains β≃0.28
∘
 for C
aγ
	​

=8,θ
i
	​

=1,m≃3.9H
0
	​

, outside the stated m/H
0
	​

∈[1,3] scan-prior box at fixed C
aγ
	​

=8, and the observed 0.342
∘
 at C
aγ
	​

=8 requires m≳4H
0
	​

 or larger coupling. The continuous-prior posterior also has C
aγ
	​

 median 20.7 and a fixed-coupling median mass near 36H
0
	​

.

Proposed fix: Replace “at scan-prior midpoint values” with: “within the broader scan-prior envelope, but near its upper-displacement/coupling region; the posterior-supported fixed-coupling fit shifts to m≫H
0
	​

.”

FM3. The new spectator-subset table is useful but not yet quantitative enough

Location: Table IV, p. 20; §VI p. 11–12.

Problem: Table IV is a major improvement, but the rows for Ω
a
	​

<0.1 and Ω
a
	​

<0.01 still contain qualitative entries such as “post.-supported,” “broad,” and “smaller-weighted,” rather than actual weighted percentiles. 

paper1b_mcmc_companion_v1B.0.62

 This makes the central ALP claim harder to audit: the reader learns that 13% of the posterior is spectator-safe and has β=0.28
∘
±0.10
∘
, but not what m/H
0
	​

, θ
i
	​

, and C
aγ
	​

 values define that safe subset.

Proposed fix: For each subset in Table IV, report weighted 16/50/84 percentiles for m/H
0
	​

, θ
i
	​

, and C
aγ
	​

, plus weighted/raw sample counts and subset ESS. If the subset ESS is too low for stable percentiles, say so explicitly in the table.

FM4. The public README still contradicts the manuscript on χ
eff
2
	​


Location: Data and Code Availability p. 13–14; public reproducibility README.

Problem: The manuscript says χ
eff
2
	​

, AIC, BIC, and lnB are not reported; only the Table II channel goodness-of-fit decomposition is reported. 

paper1b_mcmc_companion_v1B.0.62

 The public README still lists χ²_eff | YES, albeit with AIC/BIC/lnB marked not reported. 
GitHub
 This creates a reproducibility mismatch over exactly which model-comparison/goodness-of-fit quantities are part of the paper.

Proposed fix: Rename the README row to “Table II channel χ
2
 decomposition” and mark χ
eff
2
	​

, AIC, BIC, and lnB as not reported, matching the manuscript.

MINORS

Appendix A table-reference drift after adding the ALP subset table.
Location: Appendix A, p. 14.
The text says the frozen ΛCDM+ΔN
eff
	​

 chain directories back “Table I and the Table III/Table IV reproducibility and claim-classification entries,” but Table IV is now the ALP spectator-subset table, and the claims-classification table is Table V. 

paper1b_mcmc_companion_v1B.0.62


Fix: Change this to “Table I, Table III, and the relevant Table V claim-classification entries.” State separately that Table IV is backed by the ALP c5 continuous chain.

PACS numbers remain.
Location: p. 1.
Fix: Retain only for PRD; remove for MNRAS or JCAP.

“Systematic floor” remains easy to misread in the abstract.
Location: abstract p. 1; §IV p. 7–8; conclusion p. 13.
The body explains this is a pipeline-recovery bias floor, not an observational systematic. The abstract still says “pipeline systematic floor.”
Fix: Use “pipeline-recovery bias floor” everywhere.

Version language should be made fully self-contained.
Location: Data and Code Availability, p. 13–14.
Because the public tagged release is still pending, the exact commit SHA should appear directly in the paper once final, not only in the external changelog.
Fix: Add “commit: <SHA>” in Data Availability at submission.

3. Updated recommendation

Recommendation: MAJOR REVISIONS.
v1B.0.62 is scientifically and rhetorically closer to publishable than v1B.0.60, but acceptance should wait until the v1B.0.62 artifact layer is actually pinned and machine-valid, the PArthENoPE/YAML claim is corrected or implemented, and the remaining w0wa/ALP phrasing is brought into exact alignment with the paper’s own caveats.
