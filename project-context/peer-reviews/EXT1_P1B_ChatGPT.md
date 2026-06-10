# EXT1 P1B — ChatGPT Pro Extended referee report
**Provider**: chatgpt.com web app (Big Bounce Book project) · intelligence **Pro Extended** (GPT-5.5)
**Chat**: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a29e620-242c-83e8-80a6-225f2095aded
**PDF**: paper1b_mcmc_companion_v1B.0.54.pdf (md5 bd19ee37) · **Harvested**: 2026-06-10T17:05 PDT

---

Show more
Thought for 12m 19s
Referee report — Paper 1B v1B.0.54

Recommendation: MAJOR REVISIONS
I would not recommend acceptance in the present form. The core ΛCDM+ΔN
eff
	​

 null result may be publishable after cleanup, but the current paper has reproducibility-artifact contradictions, an over-stated spectator-ALP interpretation, and an out-of-scope/likely invalid w0–wa section that must be fixed before publication. I reviewed the attached PDF end-to-end; locators below use PDF section/page and extracted-text line numbers where useful. 

paper1b_mcmc_companion_v1B.0.54

BLOCKERS — must fix before publication
B1. Public reproducibility artifacts contradict or fail to verify the quoted MCMC parameter values

Location: §III/Table I, p. 3–4, lines 153–164, 177–197, 239–252; Appendix A/Data Availability, p. 13–14, lines 958–972 and 1032–1069.

Problem: The paper’s headline MCMC counts are plausible as raw accepted samples: 176,240+132,949=309,189. The frozen manifests in the linked public repository also give those same raw sample counts for the full-tension and Planck+BAO+SN packs. However, the current public artifacts are not internally reliable enough to verify Table I. The full-tension frozen parameter_summary.json labels H
0
	​

=0.8035, ΔN
eff
	​

=13.82, τ=1.0409, etc., which are clearly column/header misassignments rather than physical values. The Planck+BAO+SN convergence report likewise shows the cosmological values shifted into nuisance-parameter labels; for example the value 67.777 appears under amp_217, and 0.8273 appears under n_217, not under H
0
	​

 and S
8
	​

. 
GitHub
+3
GitHub
+3
GitHub
+3

There is also a burn-in inconsistency: the PDF footnote says both frozen chains use 30% burn-in, giving 216,432 post-burn samples, but the public Planck+BAO+SN report says 20% burn-in and 106,361 post-burn samples. The current public README at the paper’s reproducibility path is also stale: it describes an older v0.9.0 paper and lists old values such as H
0
	​

=69.2, ΔN
eff
	​

≈0.3, and “no CMB map analysis,” which conflicts with this manuscript. 
GitHub
+1

Proposed fix:
Freeze a versioned v1B.0.54 reproducibility release with DOI/Zenodo or immutable Git tag. Regenerate all MCMC summary tables directly from chain headers using a tested parser. Include a small machine-checkable table with, for each dataset: raw accepted samples, burn fraction, post-burn weighted sample count, minimum ESS, worst 
R
^
−1, and exact script/commit hash used to compute Table I. Add a unit test that fails if H
0
	​

, S
8
	​

, Ω
m
	​

, nuisance parameters, or derived columns are shifted. Until this is fixed, the Table I values may be correct but are not externally auditable from the cited artifacts.

B2. The spectator-ALP headline is not supported as stated by the paper’s own posterior

Location: Abstract, p. 1, lines 31–36; §VI, p. 10–12, lines 714–760, 847–860, 913–930; Conclusion, p. 13, lines 1003–1012; Appendix C, p. 14–15, lines 1047–1049 and 1111–1115.

Problem: The manuscript repeatedly says an ALP with f
a
	​

∼M
Pl
	​

, m∼H
0
	​

 and “natural parameter values” is consistent with the birefringence signal. But §VI later states that the fixed-C
aγ
	​

=8 posterior has θ
i
	​

=1.32±0.41 and median m≃36H
0
	​

, outside the declared “natural” m/H
0
	​

∈[1,3] box. It also states that C
aγ
	​

=8 reaches the observed central value only for m≳4H
0
	​

 or larger coupling, and that the strict θ
i
	​

≤0.1 sliver carries only 0.33% posterior mass under the flat-θ
i
	​

 prior and 0.068% under a cosθ
i
	​

-flat prior. That is not a natural spectator explanation; it is a tuned, non-minimal-coupling accommodation.

The explicit spectator condition is also under-specified. With reduced M
Pl
	​

 and small-angle potential,

Ω
ϕ
	​

≃
6
1
	​

(
H
0
	​

m
	​

)
2
(
M
Pl
	​

f
a
	​

	​

)
2
θ
i
2
	​

.

Thus Ω
ϕ
	​

<ϵ requires

θ
i
	​

<
6ϵ
	​

m
H
0
	​

	​

f
a
	​

M
Pl
	​

	​

.

For f
a
	​

=M
Pl
	​

, this gives θ
i
	​

<0.245 for m=H
0
	​

 and Ω
ϕ
	​

<0.01, but θ
i
	​

<0.063 for m=3.9H
0
	​

, and θ
i
	​

<0.0068 for the quoted posterior median m≃36H
0
	​

. Therefore the paper’s shorthand “θ
i
	​

∼0.1” is not a sufficient spectator restriction across the posterior mass range.

Proposed fix:
Recast the claim as: “A tuned, non-minimal-coupling ALP can accommodate the published β summary likelihood; it is not a natural m∼H
0
	​

 spectator explanation.” Then add a hard spectator analysis: impose Ω
ϕ
	​

<0.1 and Ω
ϕ
	​

<0.01 in the MCMC, report posterior mass, posterior β, m/H
0
	​

, θ
i
	​

, C
aγ
	​

, and prior sensitivity under both flat-θ
i
	​

 and flat-cosθ
i
	​

 priors. Remove “natural parameter values” from the abstract, conclusion, and figure captions unless the restricted posterior actually supports it.

B3. The w0–wa “quintom-B empirical anchor” is a fourth analysis, not advertised in the abstract, and its SN likelihood stack is not justified

Location: §III, p. 3, lines 157–176; Table II, p. 5, lines 291–304; Table III, p. 10, line 704; §V Results, p. 9, lines 632–655; Conclusion, p. 13, lines 945–955.

Problem: The paper advertises three analyses, but then introduces a large, separate DESI DR2 + Planck + DES-Y5 + Pantheon+ w0–wa analysis and concludes with it as a “Quintom-B empirical anchor.” This is not a minor aside; it becomes a headline result. More seriously, Table II combines DES-Y5 and Pantheon+ as if independent. A DES Collaboration comparison paper reports that Pantheon+ and DES-SN5YR have overlapping SN events, with about 20% SNe in common, and discusses nontrivial differences in Malmquist-bias corrections and selection functions. A naive product likelihood without joint covariance or overlap treatment can double-count data and distort w0–wa constraints. 
Illinois Experts

Proposed fix:
Either remove Table II and the “quintom-B empirical anchor” from this companion, or move it to a separate paper with a full likelihood/covariance justification. If retained, rerun w0–wa with mutually exclusive SN options: DESI+Planck+Pantheon+, DESI+Planck+DES-SN5YR, and a justified joint/overlap-corrected SN combination. Do not quote +4.3σ/−3.6σ departures as a program-level empirical anchor until the SN covariance/overlap issue is resolved.

MAJORS — should fix
M1. The 309,189 samples should not be described as “posterior samples” without qualification

Location: Abstract p. 1, lines 10–16; §III p. 3, lines 153–164 and footnote lines 177–197; Table I p. 4, lines 239–252.

The count is raw accepted samples, not independent posterior samples. The relevant posterior precision is governed by post-burn weighted samples and ESS, with minimum ESS ∼4.7×10
3
. The text is mostly careful, but the abstract/headline still risks inflation. Use: “309,189 raw accepted samples; min ESS 4,692; post-burn sample counts X/Y under stated burn-in.”

M2. The ΔN
eff
	​

 proxy prior allows negative “extra radiation”

Location: §III p. 3, lines 153–164; Fig. 2 caption p. 6, lines 421–455.

The paper frames the run as an “extra radiation-like degree of freedom,” but the prior is N
eff
	​

∈[2.046,5.046], i.e. ΔN
eff
	​

∈[−1,+2]. Negative ΔN
eff
	​

 is a useful phenomenological shift, not an extra species. Report a one-sided upper limit under ΔN
eff
	​

≥0, or state throughout that this is a two-sided N
eff
	​

 shift, not a physical extra-species prior.

M3. “Standard-ECH route to dark energy via additional relativistic species” is too strong

Location: Fig. 2 caption p. 6, lines 427–442; §III p. 3, lines 145–157.

The stock-CAMB N
eff
	​

 run does not test an ECH Boltzmann module and cannot rule out a generic “standard-ECH route” unless that route is precisely mapped to recombination-era N
eff
	​

. Replace with: “No evidence for a recombination-era N
eff
	​

 shift in this stock-CAMB proxy.”

M4. The “full-tension” DES-Y3 S
8
	​

 treatment is only a compressed Gaussian prior

Location: Table I caption p. 4, lines 220–237; §V p. 9, lines 652–663.

The manuscript acknowledges this, but the naming “full-tension” may imply a full DES 3×2pt likelihood. Rename the column “Planck+BAO+SN+compressed SH0ES/DES-Y3 priors” or similar. State explicitly that the DES-Y3 contribution is not a full weak-lensing likelihood and should not be interpreted as a DES likelihood analysis.

M5. The NaMaster validation is a toy synthetic-sky algebra test, not an ACT-like pipeline in the usual observational sense

Location: §IV p. 6–9, lines 501–543, 553–585, 593–641.

The paper is unusually careful about caveats, but the words “ACT-like,” “systematic floor,” and “SNR=20.32σ” still overstate the scope. The public script confirms a semi-analytic EE fit, C
ℓ
BB
	​

=0.05C
ℓ
EE
	​

, white isotropic noise, no beam, no foregrounds, no α/β separation, no bandpower covariance, and a diagonal template SNR. 
GitHub

Use “synthetic mask/noise pseudo-C
ℓ
	​

 recovery test” rather than “ACT-like pipeline validation” unless a more realistic ACT/Planck-like simulation suite is added.

M6. Do not call a 12% under-recovery “unbiased”

Location: §IV p. 8, lines 557–585 and 632–641.

The canonical estimator recovers 0.238
∘
 for 0.270
∘
, a ∼12% multiplicative bias. The robustness battery shows that inverse-variance weighting reduces the bias from −0.032
∘
 to −0.006
∘
. 
GitHub
 The sentence “The deconvolution is therefore unbiased at the ∣Δ
β
^
	​

∣≤0.040
∘
 level” should be replaced by “The pipeline is calibrated with an empirical bias of up to 0.040
∘
 for this intentionally simple estimator.” Better still, make the inverse-variance estimator the baseline.

M7. The “SNR=20.32σ” should be demoted or renamed

Location: §IV footnote 3, p. 8, lines 593–629; conclusion p. 13, lines 989–1001.

The manuscript defines this as a matched-template ratio using per-bin MC scatter, not a recovered-angle detection significance. The negative-β rerun gives a per-realization angle ratio ∣
β
^
	​

∣/σ
β
	​

≃5.2, while the template SNR is ∼20.3. 
GitHub
 The current public summary still says “NaMaster analysis confirms SNR=20.32,” which is exactly the wording likely to be misunderstood. 
GitHub
 Rename it S/N
template,diag
	​

 and keep it out of the abstract.

M8. The ALP MCMC is a reparameterized summary-likelihood fit, not an independent data fit

Location: §VI p. 11, lines 811–845; Appendix C p. 15, lines 1109–1119.

The text does say the chains use a Gaussian summary likelihood, but then gives several “MCMC” posterior comparisons that can look like independent confirmations. Keep the warning every time β
ALP
	​

, β
free
	​

, and β
obs
	​

 are compared: these are all constrained by the same single published β summary, not by independent EB spectra.

M9. The public repository should be versioned and pruned for this paper

Location: Data Availability p. 13, lines 958–972; Appendix A p. 13–14, lines 1001–1069.

The linked repository is program-wide and currently contains stale README values, unrelated PTA/galaxy-spin files, and outdated Paper 1 labels. 
GitHub
+1
 For a journal paper, provide a clean v1B.0.54 release directory with only the files needed for this paper, plus checksums and exact commands.

MINORS — polish

PACS numbers: remove for MNRAS/JCAP style unless the target journal requires them.

Bibliography cleanup: Ref. [25] contains an internal explanatory sentence about “Used in P1A Sec. VI”; remove program-management prose from the reference list.

PR3/PR4 wording: the abstract footnote says the published Eskilt & Komatsu result is PR3+WMAP9, while §VI line 680 calls it “joint WMAP9 + Planck PR4/NPIPE.” Make this consistent.

Use one naming convention: alternate labels “LCDM” and “ΛCDM” appear; use ΛCDM throughout.

Define M
Pl
	​

: specify reduced vs unreduced Planck mass in the ALP energy-density formula.

LiteBIRD statement: replace “LiteBIRD will settle this at ∼9σ” with “under forecast foreground/calibration assumptions, a β≃0.27
∘
 signal would be detected relative to β=0 at ∼9σ.”

Figures: Fig. 1 is too small for journal reproduction; enlarge labels or move it to supplementary material.

Claim-classification table: change “Verified” to “Verified by author / reproducibility artifact” until the artifact parser bug is fixed.

“Systematic floor” wording: use “internal MC recovery-bias floor” to avoid confusion with sky-measurement systematics.

HuggingFace links: Appendix A says links are in the repository README; the current README I inspected did not contain the v1B.0.54 HuggingFace dataset links. Add explicit URLs/DOIs in the paper or remove the claim.

Strengths

The manuscript is unusually transparent about scope: stock CAMB is not a torsion Boltzmann solver, the NaMaster analysis is not a sky detection, and the ALP is not a distinctive ECH prediction.

The ΔN
eff
	​

 null result is physically sensible and, if the corrected chains verify it, is a useful negative result: H
0
	​

 remains Planck-like and the extension does not solve the Hubble tension.

The NaMaster robustness battery is a real strength: the paper identifies estimator weighting as the dominant source of the ∼12% under-recovery and tests sign, sky fraction, apodization, mask, and purification.

The ALP section honestly discloses both coupling and misalignment burdens; the problem is not concealment but inconsistent headline framing.

The paper makes a serious attempt at reproducibility with manifests, checksums, script paths, and sample-count reconciliation, even though the current public artifacts need repair.

Specific scrutiny requested
1. 309,189 MCMC samples across two converged dataset combinations

The arithmetic 176,240+132,949=309,189 is correct, and the frozen manifests corroborate the raw sample counts. But the phrase must be “raw accepted samples,” not “posterior samples” or “independent samples.” The post-burn accounting is currently inconsistent between the PDF and public artifacts, and the public parameter-summary artifacts have a severe column-mapping bug. I would not allow the sample-count claim to stand without a corrected, immutable chain release.

2. ΔN
eff
	​

≈0 and H
0
	​

=67.68

The reported Table I values are plausible and internally consistent with a Planck-dominated stock-CAMB N
eff
	​

 extension. The interpretation should remain narrow: the run supports “no evidence for a two-sided N
eff
	​

 shift in stock CAMB,” not a direct ECH test. The negative-ΔN
eff
	​

 prior also means the physical extra-radiation result should be quoted as an upper limit under ΔN
eff
	​

≥0.

3. NaMaster 500-MC recovery at SNR =20.32σ

The recovery numbers are reproducible from the public summary: injected 0.270
∘
, recovered 0.238
∘
, bias 0.032
∘
, template SNR 20.3156. 
GitHub
 But this is not a sky detection and not even the per-realization angle significance. It is a diagonal matched-template signal-to-noise on synthetic CMB-only maps. The paper should stop using “20.32σ” in any headline context and report the more interpretable per-realization σ
β
	​

≃0.046
∘
, ∣
β
^
	​

∣/σ
β
	​

≃5.2, and MC-mean bias.

4. Spectator-ALP carved-out regime

The paper needs a hard, explicit parameter restriction, not just “θ
i
	​

≪1” or “θ
i
	​

∼0.1.” A publishable version should state something like:

Ω
ϕ
	​

≃
6
1
	​

(
H
0
	​

m
	​

)
2
(
M
Pl
	​

f
a
	​

	​

)
2
θ
i
2
	​

≪1,

then choose a numerical spectator threshold, e.g. Ω
ϕ
	​

<0.01, and impose it in the posterior. For the paper’s own posterior median m≃36H
0
	​

, θ
i
	​

∼0.1 is not spectator-safe; it gives Ω
ϕ
	​

 of order unity or larger under the standard reduced-M
Pl
	​

 normalization. The current ALP result should therefore be rewritten as “accommodation with tuning and enhanced coupling,” not “natural spectator ALP with m∼H
0
	​

.”

Sources

Pro Extended

