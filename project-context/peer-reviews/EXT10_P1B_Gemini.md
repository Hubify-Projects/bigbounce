# EXT10 Harvest — P1B — Gemini
- Provider: Gemini
- Model/Effort: 3.5 Thinking (Solves complex problems)
- Chat URL: https://gemini.google.com/u/0/app/aacdf7af086eb273
- PDF md5: 06410d7c
- Harvested: 2026-06-13 15:16 PDT

---

## Referee Report

**Journal:** Physical Review D / JCAP / MNRAS
**Manuscript Title:** Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔN_eff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model
**Author:** Houston Golden

---

**1. Recommendation: MINOR REVISIONS**

This manuscript serves as a highly transparent technical verification companion layer to the core structural-closure work presented in Paper I(a). The author provides an exceptionally honest, well-scanned documentation of numerical code paths, reproducibility frameworks, and baseline consistency checks. Because the paper is explicitly framed as a technical companion and methodology cross-check rather than a primary discovery paper, it satisfies the rigorous standards required for publication once several minor clarifications, formatting inconsistencies, and pending repository actions are resolved.

---

**2. Blockers (Must Fix Before Publication)**

None. There are no foundational scientific errors or missing critical validation controls that invalidate the reported parameter posteriors or verification metrics.

---

**3. Majors (Should Fix Before Final Production)**

**Section III / Section V — Supernova Product Likelihood Overlap Treatment**
Issue: In Section III (Physics interpretation) and Section V(C), the author notes that the w0wa diagnostic chain treats DES-SN5YR and Pantheon+ as entirely independent product likelihood components. These catalogs share roughly 20% of their raw supernova events but apply separate Malmquist bias corrections. The naive multiplication of these likelihoods double-weights the overlapping sample and introduces an artificial inward statistical pull.
Proposed Fix: While the author clearly states this as an uncorrected diagnostic limitation, the main text must explicitly clarify in the abstract or conclusions that the precise 4.3σ departure in w0 and -3.6σ departure in wa are subject to shift once a joint covariance framework is implemented. Add a direct text statement noting that while the qualitative quintom-B direction is likely robust, the exact cross-survey significance metrics are upper bounds.

**Section III — Lack of Release-Pairing Swap Test for MCMC**
Issue: The ΔNeff proxy run couples the newer Planck PR4/NPIPE CamSpec high-ℓ TTTEEE likelihood with the legacy 2018 low-ℓ and lensing likelihood configurations. The text acknowledges that any cross-release pairing bias remains unquantified at the quoted precision.
Proposed Fix: Expand the caveat paragraph in Section VII to state explicitly that while the baseline model is adequate for a generic proxy analysis, future precision checks must utilize a self-consistent, single-release likelihood stack to rule out sub-significance systematic shifts in the cosmological parameter tail.

---

**4. Minors (Typographical & Polish Items)**

- **Typography / Text-Extraction Artifact Cleanup:** Throughout the text, the angular momentum variable ℓ is occasionally rendered or extracted as a standard English lowercase "l" (e.g., "high-l", "low-l"). Similarly, the pseudo-Cℓ power spectra notation occasionally displays as "Ct" or "CfBB". Ensure uniform LaTeX rendering across all page sets.

- **Appendix A & C — Administrative Target Actions:** In Section VI and Appendix A, placeholder statements exist indicating that the Zenodo or Hugging Face DOI assignments are currently pending submission. Mint the permanent DOIs for the finalized frozen data chains and pipeline scripts, then substitute the literal URLs with standard bibliographic DOI index tags in the final paper layout.

---

**5. Strengths**

- **Exemplary Transparency & Open Science Implementation:** The absolute disclosure of code paths, exact Cobaya YAML configurations, committed raw chains on Hugging Face, and explicit reproduction shell scripts sets a commendable standard for modern cosmological data analysis.

- **Rigorous Pipeline Validation Floors:** Rather than claiming a flawless setup, the author identifies and quantifies an empirical 12% multiplicative under-recovery bias in the unweighted NaMaster pseudo-Cℓ pipeline. Carrying the worst-case 0.040° bias forward as a conservative systematic floor demonstrates excellent methodological discipline.

- **Honest Fine-Tuning Disclosures:** The manuscript does not hide the theoretical tensions or fine-tuning requirements of the spectator Axion-Like Particle (ALP) setup. Disclosing the 25× misalignment angle tuning needed to avoid backreaction and preserve the spectator status provides valuable clarity for phenomenology tracking.

---

**6. Specific Scrutiny of Key Structural Metrics**

**MCMC Posterior Sample Size & Convergence**
The manuscript utilizes a total pool of 309,189 raw MCMC samples across two frozen dataset combinations: 176,240 samples for the full-tension combination and 132,949 samples for the Planck+BAO+SN combination. A uniform 30% burn-in cut was appropriately applied to both chains, resulting in a verified 216,432 post-burnin sample pool. All sampled parameters show superb convergence with a worst-case Gelman-Rubin threshold of R̂⁻¹<0.003 and a robust minimum Effective Sample Size (ESS) exceeding 4,600.

**ΔNeff≈0 Stability and Hubble Tension Null-Result**
The chains return two-sided marginalized means of −0.020±0.169 (full-tension) and +0.058±0.179 (Planck+BAO+SN), showing perfect consistency with the Standard Model. Imposing the physical restriction ΔNeff≥0 yields a truncated 95th-percentile upper limit of ΔNeff<0.31 for the full-tension configuration and ΔNeff<0.40 for the baseline configuration. The proxy parameter configuration fails to clear the residual 3.6σ Hubble tension.

**NaMaster Pseudo-Cℓ Pipeline 500 MC Recovery**
Injecting a fiducial spectator-ALP cosmic birefringence angle of βinj=0.27° returns a recovered sample mean of β̂=0.238°. This corresponds to a localized pipeline-recovery template-fit signal-to-noise ratio of SNR=20.32 against single-realization noise. The under-recovery yields a negative bias (β̂−βinj=−0.032° at βinj=0.27°; −0.040° at βinj=0.342°). Through a six-configuration robustness battery, the author correctly attributes 80% of this bias to the equal weighting of noise-dominated high-ℓ bins.

**Spectator-ALP Carved-Out Subspace Analysis**
To preserve the spectator status definition (Ωa<0.01), the initial condition must satisfy θi≪1 (specifically θi∼0.1), representing a 25× misalignment energy density fine-tuning constraint. The continuous uniform prior rerun (Caγ∈[4,60]) yields a broad posterior with median Caγ=20.7. When restricting the posterior mass to the spectator-safe Ωa≤0.01 subset (which contains 13% of the MCMC weight), the pipeline recovers a rotation angle of β=0.28°±0.10°, which cleanly satisfies the observational joint WMAP+Planck 3.6σ benchmark.

The manuscript is clear, accurate, and provides full reproducibility paths. It is highly suited for publication once these minor revisions are finalized.
