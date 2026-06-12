# EXT5 P1B — ChatGPT Pro Extended (in-thread delta round 5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded
**PDF**: paper1b_mcmc_companion_v1B.0.60.pdf · harvested 2026-06-12 00:47 PT · state done
---
Referee report on Paper 1B v1B.0.60

Updated recommendation: MAJOR REVISIONS.
The paper has moved toward publishability since v1B.0.58: the scientific scoping is now much clearer, especially for BBN/Y
He
	​

, PR3/PR4 birefringence provenance, ALP-chain ESS, and the w0wa conclusion. I would still not accept it because the public reproducibility layer remains internally inconsistent and machine-fragile, and the w0wa/ALP interpretations still need final tightening.

1. Closure verification against my original BLOCKERS / MAJORS
Original issue	Status	Verification
B1. Public reproducibility artifacts contradicted or failed to verify Table I MCMC values	PARTIAL / REGRESSION	The numerical side is much improved: v1B.0.60 reports Table I with all seven parameters, including S
8
	​

, raw counts 176,240+132,949, and min ESS 4744/4692. The manuscript also states that frozen MCMC chains are committed and that corrected summaries supersede the legacy column-permuted exports. However, the named corrected JSON files still appear to be invalid JSON because the _provenance string is split by a raw newline in both the full-tension and Planck+BAO+SN files; standard json.load/jq will fail. 
GitHub
+1
 The PDF also says URLs are recorded in the root CHANGELOG.md under v1B.0.60, but the public changelog I inspected has v1B.0.59 and v1B.0.58 entries, not v1B.0.60. 

paper1b_mcmc_companion_v1B.0.60

 
GitHub

B2. Spectator-ALP headline unsupported by the posterior	PARTIAL	The paper now discloses the key burden: fixed-C
aγ
	​

=8 prefers θ
i
	​

=1.32±0.41 and median m≃36H
0
	​

; the required coupling lies outside minimal KSVZ/DFSZ benchmarks; only 13% of posterior mass satisfies Ω
a
	​

<0.01; and the θ
i
	​

≤0.1 sliver has very small posterior mass. The conclusion is much better because it now says only the Ω
a
	​

<0.01 subset is spectator-safe. But the abstract still leads with “f
a
	​

∼M
Pl
	​

,m∼H
0
	​

 is consistent,” while the posterior-preferred fixed-coupling mass is far from m∼H
0
	​

. The closure would be complete if the Ω
a
	​

<0.01 subset were tabulated with its own m/H
0
	​

,θ
i
	​

,C
aγ
	​

,β percentiles.
B3. w0wa “quintom-B empirical anchor” introduced without justified SN likelihood stack	PARTIAL	The conclusion now correctly calls this an “exploratory, overlap-uncorrected test” that remains provisional pending SN-overlap control chains. 

paper1b_mcmc_companion_v1B.0.60

 The body also discloses the DES-SN5YR/Pantheon+ overlap, product-likelihood treatment, and queued Pantheon+-only / DES-SN5YR-only control chains. 

paper1b_mcmc_companion_v1B.0.60

 But the main §III interpretation still says “canonical quintom signature,” “consistent with the bounce / pre-Big-Bang scenario,” and “centered well into quintom-B territory” before the reader reaches the caveat. 

paper1b_mcmc_companion_v1B.0.60

 The control chains remain queued rather than reported.
M1. 309,189 samples should not be called independent posterior samples	CLOSED	The text now consistently treats 309,189 as raw/frozen samples across two frozen combinations, with the Planck-only run excluded from the headline.
M2. Negative ΔN
eff
	​

 prior makes “extra species” framing incomplete	CLOSED	The prior is explicitly two-sided, N
eff
	​

∈[2.046,5.046], and the one-sided ΔN
eff
	​

≥0 upper limits are reported: <0.31 and <0.39.
M3. “Standard-ECH route to dark energy via relativistic species” too strong	CLOSED	Fig. 2 and §III now frame the run as a stock-CAMB phenomenological proxy, not a direct spin-torsion Boltzmann-module test.
M4. Full-tension DES-Y3 S
8
	​

 treatment only a compressed Gaussian prior	CLOSED in the manuscript	Table I and Table III now make clear that DES-Y3 enters the full-tension chain as a Gaussian S
8
	​

 prior, not a full weak-lensing likelihood. A public-README contradiction remains, but I treat that as a fresh reproducibility finding below.
M5. NaMaster validation overstated as ACT-like observational pipeline	CLOSED	The paper now repeatedly says the NaMaster run is a synthetic CMB-only pseudo-C
ℓ
	​

 recovery test, not a sky detection or α/β separation measurement.
M6. Do not call 12% under-recovery “unbiased”	CLOSED	The text now states that the estimator has ∼12% multiplicative under-recovery and is not unbiased in the standard statistical sense. 

paper1b_mcmc_companion_v1B.0.60


M7. SNR=20.32 should be demoted or renamed	CLOSED	The 20.32 value is now explicitly a template-fit injected-signal recovery SNR, not an angle-detection or sky-detection significance.
M8. ALP MCMC is summary-likelihood, not independent data fit	CLOSED	Appendix C states that all ALP fits use a Gaussian summary likelihood on β
obs
	​

=0.342
∘
±0.094
∘
, not a re-analysis of EB spectra; ACT DR6 is only an external cross-check. 

paper1b_mcmc_companion_v1B.0.60


M9. Public repo should be versioned/pruned for this paper	PARTIAL / REGRESSION	The manuscript now says a public tagged release is pending, which is more honest, and Appendix A lists the HuggingFace dataset URLs directly. But the public changelog lacks the claimed v1B.0.60 entry, the corrected JSON artifacts are not machine-valid, and the public README still misstates the full-tension dataset stack. 
GitHub
+3
GitHub
+3
GitHub
+3
2. Fresh pass — new/current findings only
BLOCKERS
FB1. v1B.0.60 public reproducibility layer is still not machine-publication-safe

Location: Data and Code Availability, p. 13; Appendix A, p. 14; public CHANGELOG.md; public parameter_summary_CORRECTED.json files.

Problem: The PDF says v1B.0.60 is identified by the in-tex version stamp and a matching version-stamp commit, and that the dataset URLs are recorded in root CHANGELOG.md under v1B.0.60. The public source does contain \paperVersion{v1B.0.60}, but the public changelog I inspected does not contain a v1B.0.60 entry; its top relevant entry is v1B.0.59, followed by v1B.0.58. 
GitHub
+1
 More seriously, both corrected JSON summaries appear invalid because their _provenance string contains a literal raw newline. That defeats the purpose of making them the machine-readable replacement for the old column-permuted exports. 
GitHub
+1

Proposed fix: Regenerate every corrected JSON file with escaped provenance or a list-valued provenance field, and require python -m json.tool or jq . to pass in CI. Add a v1B.0.60 changelog entry with exact commit SHA, dataset URLs, and checksums. Either create the immutable public tag/release before submission or change the paper to say the current artifact is internally verified but not yet externally pinned.

FB2. Public README still contradicts the manuscript on the full-tension likelihood stack

Location: Public reproducibility/README.md; manuscript §V/Table III, p. 8 and p. 19.

Problem: The manuscript is clear that the frozen ΛCDM+ΔN
eff
	​

 full-tension chain is Planck + SDSS BAO + Pantheon+ + SH0ES M
B
	​

-anchor + DES-Y3 S
8
	​

 Gaussian, and that DESI DR2 and DES-SN5YR belong to the separate iter2 w0wa chain. 

paper1b_mcmc_companion_v1B.0.60

 The public README, however, still describes the “full-tension configuration” as “Planck NPIPE + SDSS BAO + Pantheon+ + DES-SN5YR,” omitting SH0ES and DES-Y3 and incorrectly adding DES-SN5YR to the frozen Table I stack. 
GitHub
 This is not cosmetic: it is a wrong recipe for the headline chain.

Proposed fix: Replace that README row with the exact Table III stack: Planck block + SDSS BAO + Pantheon+ + H0.riess2020Mb + DES-Y3 S
8
	​

 Gaussian. Put DESI DR2 + DES-Y5 + Pantheon+ + Planck only under the iter2 w0wa row. Also change the README’s χ
eff
2
	​

 row to distinguish “Table II channel χ
2
 decomposition reported” from “χ
eff
2
	​

/AIC/BIC/lnB not reported,” matching the manuscript’s model-comparison paragraph. 

paper1b_mcmc_companion_v1B.0.60

MAJORS
FM1. The w0wa body text remains too emphatic for an overlap-uncorrected exploratory chain

Location: §III “Physics interpretation,” p. 4; §III caveat (e), p. 4–5; Conclusion, p. 12.

Problem: The conclusion is now appropriately cautious, but §III still opens with strong interpretation: “canonical quintom signature,” “consistent with the bounce / pre-Big-Bang scenario,” and “centered well into quintom-B territory.” 

paper1b_mcmc_companion_v1B.0.60

 The caveat later admits DES-SN5YR and Pantheon+ are multiplied as independent likelihood factors despite ∼20% shared SNe, no joint covariance, and no completed control chains. 

paper1b_mcmc_companion_v1B.0.60

 This ordering still gives the w0wa result more evidentiary weight than the actual likelihood stack justifies.

Proposed fix: Rename the §III paragraph itself to “Exploratory w0wa cross-check” and start it with the SN-overlap caveat. Replace “canonical quintom signature” and “consistent with the bounce / pre-Big-Bang scenario” with “a provisional w0wa posterior lying in the phantom-crossing region under an overlap-uncorrected product likelihood.” Keep the +4.3σ/−3.6σ numbers only as marginal-tail distances, not as an empirical anchor.

FM2. The ALP spectator-safe result still needs a compact restricted-posterior table

Location: Abstract, p. 1; §VI, p. 9–11; Conclusion, p. 12; Appendix C, p. 14–15.

Problem: The paper now discloses the tuning burden well, including non-minimal C
aγ
	​

, the m≃36H
0
	​

 fixed-coupling posterior median, Ω
a
	​

<0.1 and Ω
a
	​

<0.01 fractions, and the very small θ
i
	​

≤0.1 sliver. But the abstract still uses the broad phrase “f
a
	​

∼M
Pl
	​

,m∼H
0
	​

 is consistent,” while the posterior-preferred fixed-coupling mass is not m∼H
0
	​

. The conclusion improves this by saying only the Ω
a
	​

<0.01 subset is spectator-safe, but it still leaves readers without the actual restricted-posterior parameter values. 

paper1b_mcmc_companion_v1B.0.60

Proposed fix: Add a small table for the continuous-prior chain with rows: full posterior, Ω
a
	​

<0.1, Ω
a
	​

<0.01, and θ
i
	​

≤0.1. Columns should include posterior mass, β, m/H
0
	​

, θ
i
	​

, C
aγ
	​

, and ESS/raw count in the subset. In the abstract, replace “m∼H
0
	​

” with “the scan-prior m∼H
0
	​

 region can bracket the signal, but the posterior-supported fixed-coupling accommodation shifts toward m≫H
0
	​

 and the spectator-safe subset is tuned.”

FM3. Appendix A still has a table-reference ambiguity around what the frozen chains back

Location: Appendix A “What is included vs. regenerable,” p. 13–14.

Problem: Appendix A says the two frozen ΛCDM+ΔN
eff
	​

 chain directories “back Tables III–IV.” The same paragraph later says Table I–II numerical entries were recomputed from committed raw chains, but the first statement omits Table I, which is the main table those frozen chains actually back. 

paper1b_mcmc_companion_v1B.0.60

Proposed fix: Change the sentence to: “The two frozen ΛCDM+ΔN
eff
	​

 chain directories back Table I and the Table III/Table IV reproducibility and claim-classification entries.”

MINORS

Post-burn count should be standardized across JSON and prose. The manuscript gives several compatible but different values for the full-tension post-burn count: 123,368, 123,129, and Fig. 1’s 119,617 thinned count; the corrected full-tension JSON reports post_burnin_samples: 123369. Pick one exact convention per artifact and label all others as thinned/rounded/legacy. 

paper1b_mcmc_companion_v1B.0.60

 
GitHub

README front matter remains Paper I(a)-weighted. The public README now has useful Paper I(b) quick links, but its title still reads like a Paper I(a) reproducibility bundle. Add “Paper I(b) MCMC technical companion” to the top-level title or split Paper I(a)/I(b) into separate top-level sections. 
GitHub

PACS numbers remain. Keep them if PRD is the target; remove for MNRAS or JCAP.

The phrase “systematic floor” is now mostly safe but still easy to misread. In the abstract and conclusion, consider “NaMaster pipeline-recovery bias floor” rather than “systematic floor,” even though the text correctly says it is not a sky-measurement systematic. 

paper1b_mcmc_companion_v1B.0.60

3. Recommendation

Recommendation: MAJOR REVISIONS.
v1B.0.60 is scientifically closer to publishable than v1B.0.58, but acceptance should wait until the v1B.0.60 public artifact layer is actually pinned and machine-valid, the public README matches Table III, and the w0wa/ALP summaries are fully aligned with their own caveats.
