# P1B R36conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.63.pdf` md5=e00d5028 pages=20
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7297 chars)
**Wall time**: 343.7s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model” (20 pp)

General assessment
The manuscript presents three distinct technical exercises: (i) a stock-CAMB ΛCDM+ΔNeff MCMC “proxy” run; (ii) a NaMaster pseudo-Cℓ Monte Carlo validation for an EB-based birefringence estimator; and (iii) a consistency-level spectator-ALP scan confronting a Gaussian summary likelihood for β from the literature. The authors are careful to delineate scope and repeatedly avoid over-claiming. Many numerical statements are internally cross-referenced to artifacts, with arithmetic that is largely correct when recomputed from the numbers supplied. However, several methodological and presentation issues preclude publication in PRD in current form:

- The DES-SN5YR × Pantheon+ product likelihood is used without an overlap covariance, yet large “σ” tail distances in w0, wa and “phantom crossing required” appear in the main text. Although multiple caveats are given, PRD requires either (a) a corrected joint-covariance treatment or (b) that such provisional results be quarantined to Supplementary Material and refrained from numerical tail-distance claims in the body.

- The Planck PR4/NPIPE high-ℓ likelihood is paired with 2018 low-ℓ/lensing without a release-consistency swap check; ΔNeff results are quoted to two decimals without quantifying the possible mixing bias. This needs a concrete cross-check, or precision toned down.

- The paper includes extensive repository-path details, version stamps, and change-log process notes in the main text; PRD style requires moving these to a short Data Availability, Supplemental Material, or external repository. Most critically, all datasets are “pending DOI.” An immutable DOI snapshot is required at submission.

- Minor but real method clarifications are needed in the NaMaster section (treatment of the pixel window and of template CEE beyond the map band limit; a compact, explicit definition of χ2(β) with the weighting actually used).

- Small presentation issues (axis labeling for ΔNeff, a few “few-percent”/“≲ few-percent” assertions that should be numerically backed, etc.) should be fixed.

Detailed findings
ESSENTIAL (paper cannot be accepted without this fix)

P1B-E1 (Sec. Data and Code Availability, p. 13–14): “DOI assignment is pending” for HuggingFace datasets; version stamps (v1B.0.63) are referenced, but there is no immutable archival snapshot.
Required fix: Deposit all frozen chains, NaMaster artifacts, and ALP chains in an immutable repository (Zenodo or similar) and provide DOIs. Replace “pending” with final DOIs in the manuscript. Retain Git/paths only in the repository; in-paper provide short, stable links.

P1B-E2 (Sec. V, Table II discussion, pp. 9–10, 18–19): Product likelihood combining DES-SN5YR and Pantheon+ without a joint overlap covariance is used to quote large marginalized tail distances (+4.3σ in w0, −3.6σ in wa) and “phantom crossing required,” albeit with caveats.
Required fix: Either (a) provide a joint-covariance treatment quantifying the impact of the ≈20% SN overlap and report updated posteriors; or (b) move all quantitative w0–wa posterior-distance claims (including “phantom crossing required,” zp, wpivot, σ-wpivot) to an appendix or supplement, explicitly labeled provisional, and remove them from the main narrative and conclusions. In the main text, restrict to a short qualitative statement that the DESI+Planck+SN stack may prefer non-ΛCDM, pending overlap controls. Do not present σ distances until the overlap is treated.

MAJOR (significant revision required)

P1B-M1 (Sec. IV, pp. 6–9): Treatment of the HEALPix pixel window and template band limit. The text asserts “bins above the map band limit ℓ=1024 carry noise only” and “restricting the fit to ℓ≤1024 changes nothing (0.238°),” but the estimator is described as an unweighted χ2 fit to CEE templates up to ℓ=1536. This is only consistent if the template CEE is explicitly zeroed above ℓmax or multiplied by the same pixel window as the maps.
Required fix: State explicitly whether the template CEEb entering χ2(β) was (i) truncated to ℓ≤1024 or (ii) multiplied by the same pixel window as the spectra. If neither, quantify the induced bias (repeat the fit with template truncated or smoothed) and update the bias attribution accordingly.

P1B-M2 (Sec. IV, p. 8–9): Estimator definition. The “unweighted χ2 template fit” is described, but the paper never writes χ2(β) explicitly nor specifies the β-grid spacing except once in passing (“10−3-degree fit-grid resolution”).
Required fix: Add a compact equation defining χ2(β) and sample weighting (unweighted by σb or inverse-variance). Specify the β-grid bounds and step explicitly in the methods subsection.

P1B-M3 (Sec. III, pp. 2–5; Sec. V, pp. 9–10): PR4/NPIPE high-ℓ paired with 2018 low-ℓ/lensing. The paper acknowledges no pairing-swap control was performed, yet ΔNeff and H0 are quoted to ~0.17–0.18 precision.
Required fix: Run a pairing-consistency cross-check (PR4-consistent low-ℓ EE/TT and lensing) and report any shift in ΔNeff and H0 at the quoted precision, or qualify the reported central values as preliminary and reduce the stated precision to reflect potential pairing systematics.

P1B-M4 (Sec. VI, p. 10): “few-percent” impact statement. The ALP ODE is integrated on a ΛCDM H(z) and stated to differ by ≲ few percent from a quintom w0wa background.
Required fix: Provide a numerical check (e.g., one (m, θi, Caγ) point) that compares Δφ/fa on the two backgrounds, quantifying the fractional change.

P1B-M5 (Fig. 2, p. 6): Axis labeling inconsistency. The caption calls it “ΔNeff marginal posterior,” but the horizontal axis label reads “Neff,” with ticks roughly ±1 around zero. This could confuse Neff vs ΔNeff.
Required fix: Relabel the axis to “ΔNeff” and ensure the zero-tick is ΔNeff=0.

P1B-M6 (Sec. IV, pp. 6–9): Noise convention. The driver uses σpix = ΔP/√Ωpix with “no √2 factor;” this assumes ΔP is per-component (Q or U), which is not universal.
Required fix: Add a one-sentence justification/citation that the adopted ΔP convention (per Q/U component) matches the ACT-DR6 convention and thus needs no √2.

P1B-M7 (Sec. IV, p. 8): Bias attribution completeness. Pixel-window and beam are argued to cancel “by construction,” but this hinges on exact spectrum/template symmetry and is not explicitly demonstrated.
Required fix: Add a one-line robustness entry (or clarify existing runs) documenting that applying/removing the pixel window to the template (and, if relevant, a common beam) shifts β̂ by <10% of the −0.032° bias. If not true, include that component in the bias attribution.

P1B-M8 (Sec. V, Tables I–III, pp. 18–19): One-sided ΔNeff limits only in text.
Required fix: Add a line in Table I or the caption reporting the one-sided 95% CL bound for ΔNeff≥0 for each dataset (0.31 and 0.40 as quoted), with the truncation/renormalization definition.

P1B-M9 (Data/Code Availability, pp. 13–14): Extensive repository paths and change-log commentary in the body of the paper (e.g., “parameter_summary_CORRECTED.json,” “COUNT EXPLANATION.md,” “closure wave”).
Required fix: Move all file-path and change-log process notes to a short Data Availability paragraph plus Supplementary Material or the repository README. Keep the main text free of pathnames and internal bookkeeping.

MINOR (address but paper can proceed)

P1B-n1 (Abstract and throughout): The claim “worst-case bias across injections, −0.040° … carried forward as the pipeline-recovery bias floor” is fine, but state once that this “floor” is not added to any observational error budget (since the pipeline is a synthetic validation only).
Required fix: Add one sentence in Sec. IV explicitly saying the −0.040° floor is not propagated into any sky measurement or ALP likelihood.

P1B-n2 (Sec. III, pp. 4–5): H0–MB degeneracy check uses a constant MB−5 log10 h = −18.571; the reported chain point is −18.415 (offset 0.156 mag), normalized to σMB=0.049 to get “3.2σ.” This is fine, but the comparison mixes a 1D marginal σ with a 2D degeneracy.
Required fix: Add a clause that this 3.2σ normalization is descriptive only and not a properly conditioned tension statistic; refer the reader to the canonical H0-axis tension as the conditioned comparison (you already say this later; bring it forward).

P1B-n3 (Sec. IV, p. 8): The phrase “the estimator is not unbiased in the standard statistical sense” could be misconstrued.
Required fix: Clarify that the observed bias is largely multiplicative due to high-ℓ noise-domination under equal weighting and small residual template-shape mismatch.

P1B-n4 (Sec. VI, p. 10–12): ALP normalization. You correctly state the convention L ⊃ −(gaγ/4) φ F μν F~ μν with β=(gaγ/2)Δφ. Consider adding this 2-line derivation as an equation so readers can reconcile α/(4π) vs α/(2π) conventions at a glance.

P1B-n5 (Sec. IV, captions pp. 6–8): Ensure all axes carry units (deg for β, μK^2 for bandpowers if ever shown). If only template-fit SNR and β are displayed, annotate units there.

P1B-n6 (Sec. V, p. 9): The S8 two-Gaussian combination quoted as 0.814±0.009 is actually 0.814±0.0086 by strict quadrature; round consistently to 0.0086 or state that it’s rounded to 0.009.

P1B-n7 (Acknowledgments, p. 14): Brand-name tooling (“Claude (Anthropic)”) is unusual for PRD acknowledgments.
Required fix: Consider rephrasing to a neutral “the author used AI-powered assistants during analysis; all scientific claims were independently verified,” or consult PRD guidance.

NIT (cosmetic)

P1B-N1 (Throughout): Hyphenation artifacts from PDF parsing (e.g., “en￾ters”). Ensure final typeset copy is free of line-break artifacts.

P1B-N2 (Sec. III footnote 1, p. 3): The long burn-in/sample-accounting paragraph reads like repository notes.
Required fix: Move footnote details to Supplementary Material or repository; in-paper keep a single authoritative total post-burn-in count and R̂.

P1B-N3 (Sec. IV, pp. 6–9): Several occurrences of repository filenames in the prose and captions (e.g., c10_robustness_battery.json).
Required fix: Retain only high-level artifact identifiers in the paper; keep specific filenames in the repository index.

Internal arithmetic and dimensional checks (selected)
- H0 tension: |73.04−67.68|/sqrt(1.04^2+1.06^2)=5.36/1.485=3.61σ (matches ~3.6σ stated).
- S8 tension Planck+BAO+SN vs DES-Y3: Δ=0.051; σcomb=0.0197; Δ/σ=2.58σ (reported 2.6σ).
- Inverse-variance βcomb: 0.241°±0.061°; 0.241/0.061=3.95σ (reported “naive 3.9σ,” correct).
- EB estimator multiplicative bias: 0.238/0.27=0.881; 0.302/0.342=0.883 (≈12% under-recovery, correct).
- LiteBIRD forecast: 0.27°/0.03°=9.0σ (correct).
- ALP rotation normalization: α/(4π)=5.81×10−4; CaγΔφ/fa≈8×1.06=8.48; product=4.93×10−3 rad=0.283° (≈0.28°, correct).
- Pivot quantities: Using provided covariances gives wpivot≈−0.952, σwpivot≈0.0193, zp≈0.26–0.27 (matches text).

Scope and claims consistency
- Abstract and Conclusions are appropriately cautious for the ΔNeff proxy and pipeline validation. The ALP portion is clearly framed as a consistency check, not an ECH-specific prediction. Good.
- The only scope overreach is the presentation of numerical w0–wa tail distances in the main text under an acknowledged provisional SN-overlap setup; see P1B-E2.

Length
The paper is lengthy relative to the modest methodological claims (20 pages) because much space is devoted to artifact provenance and process notes. With the repository DOI and a concise Data Availability section, the main text could be reduced to ~12–14 pages without loss of scientific content.

## Summary recommendation
MAJOR REVISIONS

The core analyses appear technically sound and carefully caveated; most numbers check out. However, PRD publication requires (i) immutable DOI-backed data release, (ii) removal or quarantine of provisional w0–wa σ claims until the DES-SN5YR × Pantheon+ overlap is treated with a joint covariance, (iii) a brief but explicit clarification of the NaMaster template/pixel-window treatment, and (iv) a release-pairing cross-check (or precision softening) for the ΔNeff proxy run. Once these are addressed, along with the listed minor/presentation fixes, the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B — ADDITIONAL FINDINGS AFTER SECOND-PASS (fresh-eyes audit)

ESSENTIAL/MAJOR

P1B-M10 (Sec. IV/V, p. 4, “CPL Hubble-rate shift is ≈ +1.7% at z=0.5”): Arithmetic inconsistency
- The text claims that for (w0, wa) = (−0.812, −0.667), at fixed Ωm = 0.314 and the chain’s H0, the CPL Hubble rate H(z = 0.5) differs from ΛCDM by ≈ +1.7%.
- Recomputing with the stated CPL energy-density evolution ρDE(a)/ρDE,0 = a^−3(1+w0+wa) exp[3 wa (a−1)], at a = 2/3:
  • 1 + w0 + wa = 1 − 0.812 − 0.667 = −0.479 → a^−3(1+w0+wa) = (2/3)^+1.437 ≈ 1.79
  • exp[3 wa (a−1)] = exp[3 (−0.667)(−1/3)] = exp(+0.667) ≈ 1.95
  • ρDE(a)/ρDE,0 ≈ 1.79 × 1.95 ≈ 3.49
  • E^2_CPL = Ωm a^−3 + ΩDE,0 × 3.49 = 0.314 × 3.375 + 0.686 × 3.49 ≈ 1.059 + 2.394 = 3.453
  • E^2_LCDM = Ωm a^−3 + ΩDE,0 = 1.059 + 0.686 = 1.745
  • H_CPL/H_LCDM = √(3.453/1.745) ≈ 1.41 → ≈ +41%, not +1.7%.
- Required fix: Correct the stated percent difference (or precisely state a different comparison procedure if parameters are re-optimized when toggling to ΛCDM). As written, the 1.7% figure is off by more than an order of magnitude.

P1B-M11 (Sec. IV, pixel window/template treatment — internal inconsistency and likely bias channel)
- In multiple places the manuscript asserts “decoupled spectra are not pixel-window-deconvolved, and no pixel-window mismatch enters the β estimate,” because “the synthetic skies and the recovery template share the same spectra.”
- However, maps at Nside=512 inevitably include the HEALPix pixel window Wpix(ℓ), while the stated template CEE entering χ2(β) appears to be the theory input Cℓ (no explicit convolution) unless otherwise noted. If the fit compares decoupled CEB,b (convolved) to sin(2β) cos(2β) CEE,b (unconvolved), a mismatch exists and biases β̂.
- Later, the text also says “bins above the band limit carry zero template weight” and “restricting the fit to ℓ ≤ 1024 changes nothing,” implicitly suggesting the template was indeed truncated/convolved — but this is never stated cleanly.
- Required fix: Unambiguously state and implement that the template is either (i) truncated at ℓmax=1024 and/or (ii) convolved with the identical pixel window (and beam, if any) as the maps before binning. Provide a one-line quantitative check that applying/removing Wpix(ℓ) to the template shifts β̂ by <10% of the quoted −0.032° bias. If not, include this source in the bias attribution and update the bias values accordingly.

P1B-M12 (Sec. IV, inclusion of bins above the map band limit in an unweighted χ2 fit)
- The methods say bandpowers are binned to ℓ = 1536, while the maps have harmonic content to ℓmax = 1024. If the unweighted χ2 includes bins above ℓmax with nonzero template CEE but zero-signal EB, this will systematically pull β̂ toward zero (a known bias when high-ℓ, noise-only bins are equally weighted).
- The manuscript later claims “restricting the fit to ℓ ≤ 1024 changes nothing (0.238°)” and that “bins above the band limit carry zero template weight,” which would be fine, but is not explicitly documented in the estimator definition.
- Required fix: Make explicit in methods that the fit excludes bins above ℓmax (or sets the template to zero there). If this was not the case, re-run with truncation and report the change in β̂. This is distinct from P1B-M11: it concerns template/band-limit truncation and unweighted-bin bias, not the Wpix convolution per se.

P1B-M13 (Sec. IV, “Planck-like” fsky = 0.85 mask description)
- The text attributes fsky = 0.85 to a “Planck-like” Galactic-cut mask but does not specify the actual latitude cut producing 0.85. A canonical |b| > 20° cut yields fsky ≈ 0.66–0.70, not 0.85.
- Required fix: Specify the exact mask definition(s) used for fsky = 0.85 and 0.65 (e.g., |b| > bcut with bcut values), and confirm the reported fsky numerically. If additional cuts (e.g., declination) are removed for the 0.85 case, say so.

MINOR

P1B-m8 (Sec. IV, estimator/SNR weighting inconsistency)
- The β fit is explicitly unweighted in χ2, while the quoted “template-fit SNR” uses per-bin σb (inverse-variance implicitly). This is fine, but the mismatch can confuse readers.
- Required fix: Add a sentence clarifying that the β estimator is unweighted, whereas SNRtmpl is computed with inverse-variance weighting to measure detectability of the injected template against MC noise.

P1B-m9 (Sec. VI, “natural prior midpoint” for θi)
- The text uses “natural-prior midpoint θi ∼ 0.5” in some places, but Appendix C adopts θi ∈ [0.01, π] (flat in θi) and elsewhere the “natural box” for grid scans is θi ∈ [0.5, 2]. This mixing of “midpoint” notions is confusing.
- Required fix: Define “natural prior” and “natural box” precisely and use them consistently (e.g., “our grid-envelope box θi ∈ [0.5, 2] has midpoint 1.25; the spectator-safe corner is θi ≲ 0.1; the MCMC prior is flat in θi on [0.01, π]”).

P1B-m10 (Sec. VI, coupling-mass fraction accounting)
- The coupling posterior mass fractions quoted (e.g., “69% inside [9, 51], 22% below 9, 5% above 55”) sum to 96%. Clarify the remaining ~4% (presumably Caγ ∈ (51,55]).
- Required fix: Either give a full partition that sums to 100% or state that the remainder lies in a narrow intermediate bin.

P1B-m11 (Sec. IV, bin edges and NaMaster band-limit)
- Binning is described as integer edges from ℓ=30 to 1536. For Nside=512, the formal maximum useful ℓ is 3Nside−1=1535. If the final bin includes 1536, confirm NaMaster’s internal handling (truncate to 1535 or accept 1536) and that this off-by-one does not affect results.
- Required fix: Add a brief note or adjust the upper bin edge to 1535 for formal correctness.

P1B-m12 (Sec. V/Table I caption, “overlap integral 0.05” vs “2.6σ” presentation)
- The caption reports a two-Gaussian σ-distance (2.6σ) and also an overlap integral (0.05) for S8. Readers might infer a direct mapping. Since these are distinct summary metrics, add an explicit disclaimer that the 0.05 overlap is not a direct restatement of 2.6σ but a complementary measure.
- Required fix: Add one clause noting the two metrics are not interchangeable.

NO FURTHER ISSUES FOUND in classes B, C, D, E, F, G, I, J beyond those already in the initial report or the new items above
- Figure captions vs body claims: Numbers and units otherwise agree where checkable; ΔNeff axis mislabeling was already flagged (P1B-M5).
- Dimensional consistency: Equations (ALP EOM, β normalization) are dimensionally consistent.
- Cross-references: Equation/section references that can be checked are correct; no new broken refs found.
- Null-procedure comparability: The manuscript generally marks non-comparable σ’s; remaining juxtaposition issues were already covered in the first review.
- Abstract faithfulness: The abstract’s statements align with the body given their caveats (aside from the new H(z) % error flagged as P1B-M10).

Summary
The most significant new issue is the ≈1.7% claim for H(z=0.5) under the quoted CPL parameters; a straightforward recomputation gives ≈+41%. The NaMaster pixel-window/template handling remains internally inconsistent as written; please explicitly convolve/truncate the template and document the effect. Smaller clarifications on mask definitions, estimator/SNR weighting, θi prior language, bin edges, and metric presentation will further tighten the manuscript.