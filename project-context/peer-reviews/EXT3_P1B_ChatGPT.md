# EXT3 P1B — ChatGPT in-thread delta review (round 3)
**Provider**: chatgpt.com Big Bounce Book project · Pro Extended
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded
**PDF**: paper1b_mcmc_companion_v1B.0.57.pdf · **Harvested**: 2026-06-11 ~02:50 PT

---

Show more
Thought for 9m 1s
Referee report on Paper 1B v1B.0.57

Updated recommendation: MAJOR REVISIONS.
The manuscript has moved toward publishability since v1B.0.56: the MCMC sample-count correction, Planck+BAO+SN corrected diagnostics, PR3/PR4 attribution, Vincenzi citation, and ALP-scope wording are all real improvements. It is not yet publication-safe because the reproducibility layer still has machine-readable artifact problems and the w0–wa result remains too prominent for an overlap-uncorrected SN product likelihood. 

paper1b_mcmc_companion_v1B.0.57

1. Closure verification
Original issue	Status	Verification
B1. Public reproducibility artifacts contradicted / failed to verify Table I MCMC values	PARTIAL / REGRESSION	The headline raw-count regression is fixed: freeze_diagnostics_CORRECTED.json now reports total_accepted_samples: 176240, matching the paper. The Planck+BAO+SN corrected diagnostic now exists and its numerical values match v1B.0.57 Table I: H
0
	​

=67.7845, ΔN
eff
	​

=0.0578, S
8
	​

=0.8273. However, the new Planck+BAO+SN parameter_summary_CORRECTED.json appears not to be valid JSON because the _provenance string spans a raw newline, and the full-tension parameter_summary_CORRECTED.json still omits S
8
	​

, which is one of the seven Table I parameters. The release is also not immutable; the paper now honestly says a tagged release is pending, but that means the final publication artifact is still not pinned. 
GitHub
+2
GitHub
+2

B2. Spectator-ALP headline unsupported by the posterior	PARTIAL	The revision is much better: it states the posterior median m≃36H
0
	​

, the C
aγ
	​

 burden, the Ω
a
	​

<0.1 and Ω
a
	​

<0.01 posterior fractions, and the small θ
i
	​

≤0.1 sliver. But the abstract/conclusion still lead with “f
a
	​

∼M
Pl
	​

,m∼H
0
	​

 is consistent,” while the actual posterior-preferred fixed-coupling mass is far outside the nominal m/H
0
	​

∈[1,3] box and the Ω
a
	​

<0.01 subset is not summarized with its own m/H
0
	​

,θ
i
	​

,C
aγ
	​

 percentiles. The result is now fairly described as accommodation, not natural prediction, but the spectator-safe parameter restriction is still not fully tabulated.
B3. w0–wa “quintom-B empirical anchor” introduced without justified SN likelihood stack	PARTIAL	The overlap caveat is much improved and now cites the correct Vincenzi et al. comparison paper in the references. However, the first sentence asserting the ∼20% shared-SN overlap still cites DES-SN5YR [14] rather than Vincenzi [16], and the conclusion still calls the combined chain a “Quintom-B empirical anchor” / “empirical test” despite using an uncorrected product likelihood for overlapping SN samples. The Vincenzi paper specifically discusses the 20% overlap and Malmquist/selection-correction issue, so it should be the citation attached to the overlap claim. 
arXiv
+1

M1. 309,189 samples should not be called independent posterior samples	CLOSED	The manuscript consistently says raw/frozen samples and excludes the Planck-only run from the headline count.
M2. Negative ΔN
eff
	​

 prior makes “extra species” framing incomplete	CLOSED	The paper now reports the two-sided posterior and one-sided ΔN
eff
	​

≥0 upper limits.
M3. “standard-ECH route to dark energy via additional relativistic species” too strong	CLOSED	Fig. 2 and the conclusion now frame this as a stock-CAMB phenomenological proxy, not a direct ECH spin-torsion test.
M4. Full-tension DES-Y3 S
8
	​

 treatment only a compressed Gaussian prior	CLOSED	Table I now explicitly states the DES-Y3 S
8
	​

 Gaussian-prior treatment and the within-stack interpretation.
M5. NaMaster validation overstated as ACT-like observational pipeline	CLOSED	The paper now repeatedly states that this is a synthetic CMB-only pseudo-C
ℓ
	​

 recovery test, not a sky detection or α/β separation measurement.
M6. Do not call 12% under-recovery “unbiased”	CLOSED	The revised text calls it multiplicative under-recovery / calibrated-bias language, not an unbiased estimator.
M7. SNR=20.32 should be demoted or renamed	CLOSED	It is now defined as a template-fit injected-signal recovery SNR, not a sky-detection significance.
M8. ALP MCMC is summary-likelihood, not independent data fit	CLOSED	Appendix C and Fig. 4 caption explicitly say the ALP fits use a Gaussian summary likelihood on the published β, not EB spectra.
M9. Public repo should be versioned/pruned for this paper	PARTIAL	The root CHANGELOG.md now exists and records v1B.0.57 with commit 63931207, which is a real improvement. But the public-facing reproducibility README is still a program-wide / Paper I(a) README, the paper still lacks a single immutable tagged release, and the advertised HuggingFace “DOIs” are not actually listed in Appendix A; the CHANGELOG says DOI assignment is pending and gives live URLs instead. 
GitHub
+1
2. Fresh pass — new findings and regressions in v1B.0.57
BLOCKERS
F-B1. The new Planck+BAO+SN corrected diagnostic appears to be invalid JSON

Location: Data and Code Availability, p. 13; Appendix A, p. 13; public artifact planck_bao_sn_20260312_1954/diagnostics/parameter_summary_CORRECTED.json.

Problem: The file exists and has the right numerical values, but its _provenance string spans two raw lines. As displayed from the raw GitHub file, line 0 opens the string and line 1 closes it after a literal newline. Standard JSON does not allow unescaped newlines inside strings, so json.load, jq, CI checks, and downstream scripts may fail on the very file introduced to repair the earlier column-permutation bug. 
GitHub

Proposed fix: Regenerate parameter_summary_CORRECTED.json as valid JSON. Put provenance in either a one-line string with escaped \n, a list of strings, or a separate Markdown README. Add a CI check equivalent to python -m json.tool parameter_summary_CORRECTED.json for every .json artifact.

F-B2. Data Availability still claims HuggingFace “DOI links” that are not actually present

Location: Data and Code Availability, p. 13; Appendix A “HuggingFace datasets,” p. 13–14; root CHANGELOG.md.

Problem: The PDF says the HuggingFace dataset DOIs are listed below in Appendix A and in the CHANGELOG. Appendix A lists only three dataset descriptions, not URLs or DOIs. The CHANGELOG says DOI assignment is pending and gives live HuggingFace URLs instead. That is now an honest repository state, but the paper still uses DOI language that is not true at the time of review. 
GitHub

Proposed fix: Either insert the actual DOI URLs in the paper or replace “DOI links” with “dataset URLs; DOI assignment pending.” For publication, the cleanest fix is to put the three live URLs and the final DOI/Zenodo identifiers directly in Appendix A, not only in a mutable external file.

MAJORS
F-M1. The “authoritative corrected summary” does not yet reproduce all seven Table I parameters in one place

Location: Table I, p. 15; Data and Code Availability, p. 13; Appendix A, p. 13.

Problem: The paper says the corrected summaries and committed chains back Table I. The Planck+BAO+SN corrected artifact includes S
8
	​

, but the full-tension parameter_summary_CORRECTED.json includes only H
0
	​

,ΔN
eff
	​

,τ,σ
8
	​

,Ω
m
	​

,n
s
	​

; it omits S
8
	​

, even though S
8
	​

 is a Table I headline parameter. The separate freeze_diagnostics_CORRECTED.json does contain S
8
	​

, but that is not the file named in the Data Availability correction paragraph. 
GitHub
+1

Proposed fix: Add a single table1_reproduction.json containing both dataset columns and all seven Table I parameters, plus raw sample count, burn fraction, post-burn count, worst 
R
^
−1, and minimum ESS. The manuscript should cite that file as the authoritative Table I artifact.

F-M2. The w0–wa SN-overlap caveat is improved but still not reflected in the conclusion

Location: §III caveat (e), p. 4; Conclusion, p. 12; Table II, p. 16.

Problem: The paper now discloses the DES-SN5YR/Pantheon+ overlap and queues control chains, which is good. But the conclusion still labels the overlap-uncorrected product-likelihood result as a “Quintom-B empirical anchor” and “empirical test.” That is still too strong until the Pantheon+-only and DES-SN5YR-only control chains converge, or a proper joint covariance is built.

Proposed fix: Replace “Quintom-B empirical anchor” with “exploratory w0–wa cross-check.” State that the combined-SN significance is provisional pending the queued overlap-control chains.

F-M3. PR3/PR4/NPIPE wording is almost fixed, but one sentence still conflicts with the likelihood description

Location: abstract footnote, p. 1; §VI, p. 9; Appendix C, p. 14.

Problem: The footnote says PR4/NPIPE labels refer to the code-repository dataset “which is what the ALP-MCMC re-runs actually use.” Appendix C says all ALP fits use only a Gaussian summary likelihood with beta_obs: 0.342, sigma_beta: 0.094, not a re-analysis of EB spectra. The paper also says the 0.342° headline is from the published PR3+WMAP9 joint analysis. These statements can be reconciled only if the authors explain exactly which β summary was fed to the ALP MCMC.

Proposed fix: Replace “which is what the ALP-MCMC re-runs actually use” with: “the ALP MCMC uses only the scalar Gaussian summary β=0.342
∘
±0.094
∘
; it does not depend on the PR3/PR4 map-level distinction except through the provenance of that summary value.”

MINORS

Post-burn sample counts remain slightly inconsistent.
Location: §III footnote 1, p. 3; full-tension README; Planck+BAO+SN README.
The manuscript has 123,129, 123,368, 216,432, and 93,064/93,066 variants. These are all small rounding/thinning differences, but the paper should define one exact convention and use it everywhere.

The first overlap sentence still cites [14] instead of [16].
Location: §III caveat (e), p. 4.
The sentence “These two catalogs share approximately 20%...” should cite Vincenzi et al. [16], not DES-SN5YR [14], or cite both with [16] first.

The root reproducibility README is still Paper I(a)-oriented.
Location: Data and Code Availability, p. 13; public repository README.
Since the paper points readers to the program-wide reproducibility root, add a short Paper1B_README.md or put a “Paper I(b) quick links” block at the top of the root reproducibility README. The current visible README is still primarily a Paper I(a) bundle and says “No CMB map analysis,” which is misleading for this companion even if the CHANGELOG is now correct. 
GitHub

PACS numbers remain.
Location: p. 1.
Keep them only if PRD is the target; remove for MNRAS/JCAP.

3. Recommendation

Recommendation: MAJOR REVISIONS.
v1B.0.57 is materially closer to publication than v1B.0.56, but the paper still needs a valid machine-readable corrected diagnostic release, direct dataset URLs/DOIs or corrected DOI wording, and demotion of the overlap-uncorrected w0–wa result before acceptance.

Sources

Pro Extended

