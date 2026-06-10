# EXT1 P1B — Gemini 3.5 Thinking referee report
**Provider**: gemini.google.com web app · model **3.5 Thinking**
**Chat**: https://gemini.google.com/app/2ba6d99c84794eb7
**PDF**: paper1b_mcmc_companion_v1B.0.54.pdf (md5 bd19ee37) · **Harvested**: 2026-06-10T17:05 PDT

---

Gemini said
Referee Report

Journal: Monthly Notices of the Royal Astronomical Society (MNRAS)

Manuscript Title: Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔN
eff
	​

 MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

Author: Houston Golden

1. Recommendation

MINOR REVISIONS

This manuscript serves as a technical verification and validation companion paper for an underlying Einstein-Cartan-Holst (ECH) spin-torsion cosmology program. It covers three main numerical analyses: a stock-CAMB Markov Chain Monte Carlo (MCMC) proxy run evaluating extra relativistic degrees of freedom, a pseudo-C
ℓ
	​

 pipeline validation using the NaMaster code on synthetic cosmic microwave background (CMB) polarization maps, and a parametric consistency check of an axion-like particle (ALP) model against public cosmic birefringence measurements.

The paper is exceptionally transparent, highly detailed, and addresses algorithmic and systematic limits with commendable rigor. It satisfies the journal's standard for reproducibility by fully documenting its workflows, statistical samples, and software configurations. However, a few minor physical interpretations, nomenclature consistency issues, and methodological choices require clarification before the paper can be formally accepted for publication.

2. Strengths

Exceptional Transparency and Reproducibility: The author provides detailed software versioning (Cobaya v3.6.1, CAMB v1.6.5, NaMaster), exact dataset combinations, initialization seeds, and explicit parameter priors. The inclusion of a claims classification index (Table IV) and public repository manifests represents an outstanding standard for reproducible computational cosmology.

Rigorous Systematic Deconstruction: In Section IV, the pipeline-recovery bias of the pseudo-C
ℓ
	​

 deconvolution framework is systematically isolated via a targeted robustness battery. Pinpointing the exact breakdown of the −0.032
∘
 bias (attributing 80% to the unweighted template fit and the remainder to lensed B-mode template mismatch) demonstrates a deep command of the data pipeline.

Honest Boundary and Scope Delineation: The manuscript carefully distinguishes between pipeline-validation metrics and physical sky-detection claims. It explicitly avoids overstating the cosmological significance of its high internal signal-to-noise ratio (SNR) recovery figures and clearly defines the limits of its phenomenological parameters.

3. Specific Scrutiny of Key Focus Areas
A. MCMC Sample Sizes and Convergence

The paper reports a total of 309,189 raw MCMC samples generated via Cobaya across two main converged dataset configurations: a "full-tension" combination (176,240 samples) and a "Planck+BAO+SN" combination (132,949 samples). With a 30% burn-in fraction removed, the remaining pool of 216,432 post-burn-in samples provides a remarkably dense statistical foundation. The convergence criteria are exceptionally strict: the Gelman-Rubin threshold satisfies 
R
^
−1<3×10
−3
 across all sampled parameters, with the worst-performing parameter (n
s
	​

 in the full-tension chain) peaking safely below this at 
R
^
−1=9.74×10
−4
. The minimum effective sample sizes (ESS=4,744 and 4,692) ensure that the posterior means and 1σ errors reported in Table I are stable and free from sampling noise.

B. ΔN
eff
	​

≈0 and H
0
	​

 Standard Cosmology Consistency

The MCMC analysis reveals ΔN
eff
	​

=−0.020±0.169 for the full-tension chain and +0.065±0.17 for the Planck+BAO+SN chain, both entirely consistent with the Standard Model value of zero. Consequently, the derived Hubble constant (H
0
	​

=67.68±1.06 km s
−1
 Mpc
−1
 full-tension; 67.79±1.09 km s
−1
 Mpc
−1
 Planck+BAO+SN) remains in deep tension with local distance-ladder measurements (e.g., SH0ES at 73.04±1.04 km s
−1
 Mpc
−1
). The author correctly and transparently notes that a standard radiation proxy extension (ΔN
eff
	​

) lacks the required degrees of freedom to shift the acoustic scale calibration enough to resolve the Hubble tension, as the inverse-variance weight of the high-precision Planck NPIPE likelihood dominates the posterior. The paper appropriately frames this as a bounding null test rather than a definitive refutation of the underlying ECH framework, acknowledging that a true physical test would require a bespoke, torsion-modified Boltzmann solver rather than stock CAMB.

C. NaMaster Pseudo-C
ℓ
	​

 Pipeline 500 MC Recovery

The pipeline validation uses 500 Monte Carlo realizations mapped onto an ACT-like footprint mask (f
sky
	​

=0.32, white noise level 10 μK arcmin). Injecting a baseline spectator-ALP rotation of β
inj
	​

=0.27
∘
 yields a recovered mean value of 
β
^
	​

=0.238
∘
, representing a systematic under-recovery of roughly 12% (pipeline-recovery bias of −0.032
∘
). The author explicitly clarifies that the associated template-fit validation significance (SNR=20.32σ) characterizes the mathematical recovery of an injected signal under idealized, foreground-free conditions. It is not an observational sky-detection claim, which remains bounded by the published literature at 2.7σ−2.9σ. Carrying forward the worst-case injection bias of −0.040
∘
 (at β
inj
	​

=0.342
∘
) as a conservative systematic floor is an appropriate data-modeling choice.

D. Spectator-ALP Carved-Out Regime and Fine-Tuning

The manuscript reviews an ultra-light ALP field (f
a
	​

∼M
Pl
	​

, m∼H
0
	​

) evolving under standard General Relativity. The author identifies a significant fine-tuning tension required to maintain the "spectator" classification: if the initial misalignment angle is of order unity (θ
i
	​

∼1), the late-time axion energy density ρ
a
	​

∼m
2
f
a
2
	​

θ
i
2
	​

 reaches the cosmic critical density scale (Ω
a
	​

∼1), converting the ALP from a spectator into the primary dark energy field. Retaining a true spectator status (Ω
a
	​

≪1, specifically Ω
a
	​

≤0.01) carves out a narrow parameter sliver where θ
i
	​

∼0.1. This imposes a ∼25× fine-tuning of the initial misalignment condition. Furthermore, suppressing θ
i
	​

 restricts the field displacement Δϕ/f
a
	​

, which forces the photon anomaly coupling coefficient C
aγ
	​

 to scale inversely to match the observed cosmic birefringence product C
aγ
	​

(Δϕ/f
a
	​

)≈10.3. This pushes the required coupling well beyond standard O(1) KSVZ/DFSZ benchmarks into non-minimal enhancement regimes (C
aγ
	​

∼36.8−55.6), highlighting an independent coupling burden that is clearly articulated in Section VI.

4. Blockers (Must Fix Before Publication)

None. The paper contains no structural flaws, algebraic errors, or unsubstantiated primary claims that block publication.

5. Major Revisions (Should Fix)
Sec. III, p. 3 — Unquantified Systematic Pairing Bias

Context: The author notes that the MCMC runs mix Planck PR4/NPIPE high-ℓ likelihoods with 2018-release low-ℓ and lensing likelihoods. The text states: "any pairing-induced bias on the headline ΔN
eff
	​

/H
0
	​

/S
8
	​

 at the quoted precision is therefore unquantified here."

Proposed Fix: For a dedicated technical verification paper, leaving a known systematic coupling unquantified is a notable gap. The author should utilize existing literature estimates (e.g., from the Planck Collaboration or CamSpec validation notes) to place an analytical upper bound on the potential pairing-induced shift, confirming it does not threaten the core null-consistency conclusions.

Sec. V.B, p. 3 & Sec. VII, p. 13 — Status of the Accumulating Planck-Only Chain

Context: The manuscript mentions a third, Planck-only MCMC combination that has accumulated 114,992 raw samples but remains un-converged at 
R
^
−1∼0.05. It is excluded from the frozen summaries and tables.

Proposed Fix: Including a live, un-converged chain in the descriptive narrative adds unnecessary ambiguity. The author should either remove references to this accumulating run entirely or explicitly clarify why it is meaningful to state its partial status when it plays no role in the paper's final scientific conclusions.

6. Minor Revisions (Cosmetic & Polish)
Sec. II, p. 2 / Table I, p. 4 — Unit Formatting Consistency

Context: In Section II, the Hubble constant units are written as kms
−1
Mpc
−1
 or km s
−1
Mpc
−1
. In Table I, the header reads H
0
	​

[km/s/Mpc].

Proposed Fix: Standardize all instances of the Hubble constant units to standard astrophysical notation compliant with MNRAS style guidelines: kms
−1
Mpc
−1
.

Sec. IV, p. 8 — Justification for the Unweighted Estimator Baseline

Context: The robustness battery reveals that replacing the unweighted χ
2
 template fit with an inverse-variance-weighted fit eliminates 80% of the pseudo-C
ℓ
	​

 pipeline recovery bias (reducing it from −0.032
∘
 to −0.006
∘
).

Proposed Fix: If the inverse-variance-weighted approach offers a vastly superior, nearly unbiased recovery by properly discounting noise-dominated high-ℓ bins, the author should add a brief, 1–2 sentence justification explaining why the unweighted estimator was originally selected as the canonical baseline pipeline configuration.

Sec. VI, p. 10 — Narrative Drafting Artifacts

Context: The text notes: "an earlier draft paired Δϕ/f
a
	​

≈1.0−1.07 with m≈1.8−2H
0
	​

; the committed EOM integration gives Δϕ/f
a
	​

=0.35−0.42 at those masses... and the mass pairings are corrected throughout..."

Proposed Fix: While the open disclosure of code corrections is highly commendable, documenting the internal history of the working draft text within the final paper can confuse readers. Streamline this passage to state the verified physical grid coordinates and mass-pairing trajectories directly, keeping the focus on the final validated physics.




Thinking

