# EXT7 P1B — ChatGPT Pro Extended (in-thread delta round 7; Gemini = fresh thread)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded
**PDF**: paper1b_mcmc_companion_v1B.0.64.pdf (0f28d3489d369eb9) · harvested 2026-06-13 ~03:16 PT
---

Updated recommendation: MAJOR REVISIONS.
The manuscript has moved toward publishability since v1B.0.62: the ΔN
eff
	​

 limits, ALP spectator-subset table, w0wa caveat front-loading, NaMaster scope language, and BBN/Y
He
	​

 documentation are all substantially improved. I would still not accept it in the present form because the public release layer is not yet internally consistent, and the newly explicit NaMaster estimator equation contradicts the canonical unweighted estimator implemented in the released scripts.

1. Closure verification against original BLOCKERS / MAJORS
Original issue	Status	Verification
B1. Public reproducibility artifacts contradicted / failed to verify Table I MCMC values	PARTIAL / REGRESSION	The scientific numbers now look internally coherent: Table I reports all seven parameters, raw counts 176,240+132,949=309,189, min ESS 4744/4692, and one-sided ΔN
eff
	​

≥0 limits <0.31 and <0.40. The BBN/Y
He
	​

 claim is also now supported in the public YAMLs: the four Cobaya YAMLs I inspected include bbn_predictor: PArthENoPE. 
GitHub
+3
GitHub
+3
GitHub
+3
 But the public release layer still fails a publication-grade audit: the PDF says v1B.0.64 is recorded in root CHANGELOG.md, while the public changelog top entry is v1B.0.63; the public reproducibility README still identifies Paper I(b) as v1B.0.62; and both parameter_summary_CORRECTED.json files still appear, as served raw, to contain an unescaped newline inside _provenance, making them non-parseable by strict JSON tooling. 
GitHub
+3
GitHub
+3
GitHub
+3

B2. Spectator-ALP headline unsupported by the posterior	PARTIAL	This is greatly improved. The abstract and §VI now acknowledge that the fixed-C
aγ
	​

=8 posterior shifts to m≫H
0
	​

, with median m≃36H
0
	​

, and Table IV now gives restricted-posterior readouts for Ω
a
	​

<0.1, Ω
a
	​

<0.01, and θ
i
	​

≤0.1. The remaining problem is phrasing: the conclusion still says “f
a
	​

∼M
Pl
	​

,m∼H
0
	​

 is consistent” before the reader reaches the fact that the spectator-safe Ω
a
	​

<0.01 subset has m/H
0
	​

=6.0/40.5/238, θ
i
	​

=0.15/0.21/0.27, and C
aγ
	​

=29.9/43.3/54.1. That is now an accommodation in a tuned, high-coupling subset, not a clean m∼H
0
	​

 spectator result.
B3. w0wa “quintom-B empirical anchor” introduced without justified SN likelihood stack	PARTIAL	The paper now front-loads the DES-SN5YR/Pantheon+ overlap caveat and relabels the result as an exploratory, overlap-uncorrected cross-check pending control chains. This is a real improvement. It remains partial because the likelihood is still the uncorrected product of overlapping SN samples and the Pantheon+-only / DES-SN5YR-only control chains remain queued rather than reported.
M1. 309,189 samples should not be called independent posterior samples	CLOSED	The text consistently says raw/frozen samples and excludes the non-converged Planck-only run from the headline count. 

paper1b_mcmc_companion_v1B.0.64


M2. Negative ΔN
eff
	​

 prior makes “extra species” framing incomplete	CLOSED	The prior is explicitly two-sided, N
eff
	​

∈[2.046,5.046], and the one-sided non-negative limits are now stated in §III and Table I.
M3. “standard-ECH route to dark energy via additional relativistic species” too strong	CLOSED	The stock-CAMB run is now clearly framed as a phenomenological radiation-proxy null test, not a direct ECH spin-torsion Boltzmann-module test.
M4. DES-Y3 S
8
	​

 treatment only a compressed Gaussian prior	CLOSED	Table I and Table III now state that DES-Y3 enters the full-tension chain as an S
8
	​

 Gaussian prior, while DESI DR2 and DES-SN5YR belong only to the separate iter2 w0wa chain.
M5. NaMaster validation overstated as ACT-like observational pipeline	CLOSED	The manuscript repeatedly states that the run is a synthetic CMB-only pseudo-C
ℓ
	​

 injection/recovery validation, not a sky detection or α/β separation measurement.
M6. Do not call 12% under-recovery “unbiased”	CLOSED, with a new regression below	The prose no longer calls the estimator unbiased and treats 0.040
∘
 as a pipeline-recovery bias floor. However, a new equation-level inconsistency has appeared in §IV; see fresh Blocker FB2.
M7. SNR=20.32 should be demoted / renamed	CLOSED	The paper now defines the SNR as a template-fit injected-signal recovery quantity, not a recovered-angle or sky-detection significance. 

paper1b_mcmc_companion_v1B.0.64


M8. ALP MCMC is summary-likelihood, not independent EB spectra	CLOSED	Appendix C states that all ALP chains use only the Gaussian summary likelihood β
obs
	​

=0.342
∘
±0.094
∘
, not a direct EB-spectrum reanalysis. 

paper1b_mcmc_companion_v1B.0.64


M9. Public repo should be versioned/pruned for this paper	PARTIAL / REGRESSION	The README content is much cleaner than earlier versions, and the manuscript now admits that a public tagged release is pending. But the public README/changelog are not synchronized to v1B.0.64, and the corrected JSON artifacts still appear machine-fragile. 
GitHub
+1
2. Fresh pass — new/current findings only
BLOCKERS
FB1. v1B.0.64 public artifact layer is still not publication-safe

Location: Data and Code Availability, p. 14; Appendix A, p. 15; Table V, p. 20; public CHANGELOG.md, public reproducibility/README.md, and corrected JSON artifacts.

Problem: The manuscript says the paper version is identified by the in-tex v1B.0.64 stamp and matching version-stamp commit, with dataset URLs recorded in root CHANGELOG.md under v1B.0.64. The source file does contain \paperVersion{v1B.0.64}, but the public changelog I inspected has no v1B.0.64 entry; its top Paper I(b)-relevant entry is v1B.0.63. The public reproducibility README still announces v1B.0.62. 
GitHub
+2
GitHub
+2

The corrected JSON files also still appear invalid as raw public JSON because the _provenance string is split by a literal newline. This is especially problematic because the paper names these corrected files as the authority for Table I after the old column-permutation bug. 
GitHub
+1

Proposed fix: Before submission, create a v1B.0.64 changelog entry with exact commit SHA, artifact URLs, and checksums; update the public README version to v1B.0.64; create or explicitly defer an immutable public tag/release; and regenerate both parameter_summary_CORRECTED.json files with a JSON-valid provenance field. Add CI checks equivalent to python -m json.tool or jq . on every committed JSON artifact.

FB2. The new NaMaster χ
2
(β) equation contradicts the released canonical estimator

Location: §IV, p. 7–8, Eq. (1); public namaster_500mc.py; public c10_robustness_battery.py.

Problem: The manuscript says the canonical estimator is an unweighted χ
2
 template fit and explicitly states that all bins carry equal weight. But Eq. (1) includes a division by σ
b
2
	​

, which is inverse-variance weighting. The public canonical driver implements an unweighted grid fit:

χ
2
=
b
∑
	​

(C
b
EB,meas
	​

−C
b
EB,th
	​

)
2
,

with no σ
b
−2
	​

 factor. The robustness-battery script separately implements the inverse-variance case as a different configuration. 
GitHub
+1

This is not a cosmetic typo: the paper attributes the ∼12% under-recovery partly to using the unweighted estimator and shows that inverse-variance weighting recovers 0.264
∘
, removing most of the bias. Therefore the equation currently describes the cross-check estimator, not the canonical estimator.

Proposed fix: Replace Eq. (1) with the actual canonical unweighted objective:

χ
unw
2
	​

(β)=
b
∑
	​

[C
b
EB,decoupled
	​

−
2
1
	​

sin(4β)C
b
EE,tmpl
	​

]
2
.

Then define σ
b
	​

 only in the template-SNR and inverse-variance robustness contexts. If the authors instead intend Eq. (1) to be the production estimator, rerun the NaMaster suite and update all bias, SNR, and robustness numbers.

MAJORS
FM1. The ALP conclusion still over-compresses the tuned spectator-safe result into “m∼H
0
	​

” language

Location: Abstract, p. 1; §VI, p. 10–12; Conclusion, p. 13–14; Table IV, p. 20.

Problem: The technical content is now much stronger: the paper reports the continuous-prior ALP posterior, prior sensitivity, ESS, and the Ω
a
	​

<0.01 spectator-safe subset. But the conclusion still states that an ALP with f
a
	​

∼M
Pl
	​

,m∼H
0
	​

 is consistent with the published signal. 

paper1b_mcmc_companion_v1B.0.64

 Table IV shows that the spectator-safe subset has median m/H
0
	​

≃40.5, median θ
i
	​

≃0.21, and median C
aγ
	​

≃43.3, with only 13% posterior mass. That is a tuned, high-coupling accommodation, not a simple m∼H
0
	​

 spectator benchmark.

Proposed fix: Change the abstract and conclusion to: “The broader scan-prior envelope brackets the published signal, but the posterior-supported spectator-safe accommodation lies in a tuned Ω
a
	​

<0.01, low-θ
i
	​

, high-C
aγ
	​

 subset and shifts away from the simple fixed-coupling m∼H
0
	​

 benchmark.” Keep the Table IV numbers as the controlling statement.

FM2. The w0wa chain remains too evidentially prominent for an overlap-uncorrected product likelihood

Location: §III, p. 4–5; §V.C, p. 10; Table II, p. 18–19; Conclusion, p. 14.

Problem: The revision has demoted the result to “exploratory” and front-loaded the SN-overlap caveat, which is correct. The remaining issue is not wording alone: the Pantheon+ and DES-SN5YR overlap controls are still queued, not reported, and no joint covariance has been built. The quoted +4.3σ/−3.6σ marginal-tail distances therefore remain provisional.

Proposed fix: Either move the w0wa result to an appendix or add the two control chains already described: DESI DR2+Planck+Pantheon+ only and DESI DR2+Planck+DES-SN5YR only. Until then, replace any “quintom-B match” language with “candidate phantom-crossing geometry under the current overlap-uncorrected likelihood.”

MINORS

“NaMaster systematic floor” remains in several places.
Location: Fig. 3 caption and §IV, p. 7–9.
The abstract now correctly uses “pipeline-recovery bias floor,” but body/caption text still says “systematic floor.” Use “pipeline-recovery bias floor” everywhere to avoid implying a sky-measurement systematic.

PACS numbers remain.
Location: p. 1.
Retain only for PRD; remove for MNRAS or JCAP.

Public YAML comments still appear to reference stale table numbering.
Location: public cobaya_full_tension.yaml; Appendix A / Table III.
The YAML comment refers to “Table III, Table IV row 4,” but in v1B.0.64 Table IV is the ALP restricted-posterior table. Update comments to “Table III row 4 / Table I full-tension column” to prevent future audit confusion. 
GitHub

Version self-containment.
Location: Data and Code Availability, p. 14.
Once final, put the exact commit SHA directly in the paper, not only in the changelog. This will avoid another version-stamp/changelog mismatch.

3. Recommendation

Recommendation: MAJOR REVISIONS.
v1B.0.64 is scientifically closer to publishable than v1B.0.62, but acceptance should wait until the v1B.0.64 artifact layer is actually synchronized and machine-valid, and until the NaMaster estimator equation matches the released unweighted canonical implementation.
