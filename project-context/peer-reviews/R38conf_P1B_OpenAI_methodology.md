# P1B R38conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.66.pdf` md5=065d0962 pages=20
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7339 chars)
**Wall time**: 278.5s

---

Referee report — Physical Review D methodology review

Scope and contribution
The manuscript presents three technical verification analyses supporting a companion theoretical “no-go” result for Einstein–Cartan–Holst spin–torsion dark energy. The analyses are: (i) a stock-CAMB ΛCDM+ΔNeff proxy MCMC using Cobaya, (ii) a NaMaster pseudo-Cℓ Monte Carlo validation for birefringence angle recovery on synthetic CMB polarization skies, and (iii) a consistency check for a spectator axion-like particle (ALP) interpretation of isotropic CMB birefringence using a Gaussian summary likelihood for β from Eskilt & Komatsu. The paper is positioned as methods verification rather than a claim of new cosmological detections.

Overall, the paper is careful in distinguishing null-consistency from claims of statistical preference, and generally keeps sky-measurement significances separate from MC pipeline-recovery SNRs. Nonetheless, for PRD standards several methodological and presentation issues must be addressed before the paper is publishable.

Findings and required actions

ESSENTIAL

P1B-E1
- Location: Sec. III (Caveats, item (e)), Sec. V.C, Table II; pp. 4–5, 10, 19
- Issue: The w0wa chain combines DES-SN5YR and Pantheon+ as a product-likelihood without a joint covariance to account for the ≈20% event overlap and differing Malmquist corrections. The manuscript highlights large marginalized-tail distances from ΛCDM (+4.3σ in w0, −3.6σ in wa), phantom crossing, and wpivot = −0.952 ± 0.019, but these numbers depend on a statistically invalid SN combination.
- Required fix: Either (a) supply a correct joint SN covariance for DES-SN5YR × Pantheon+ and rerun the chain, or (b) rerun two overlap-robust configurations (Planck+BAO+DES-SN5YR and Planck+BAO+Pantheon+) and report the w0wa posteriors separately, removing the product-likelihood results from the main text and tables. All quoted sigma distances and “phantom-crossing required” statements must be recalculated with an overlap-safe configuration and explicitly labeled as posterior-tail distances only (not evidence, not ln B). Without this, the current w0wa results must not appear as a primary analysis.

P1B-E2
- Location: Data and Code Availability; Appendix A; p. 14–15
- Issue: Persistent archival identifiers are “pending.” PRD requires stable, citable, public artifacts for reproducibility at acceptance.
- Required fix: Register DOIs (e.g., Zenodo) or equivalent immutable archival records for: (i) frozen MCMC chains used for Table I and Table II, (ii) NaMaster MC artifacts (masks, seeds, outputs), and (iii) ALP chains. Replace “pending” with live DOIs and verify all text and links match the archived version. Include a single version tag/badge in the paper that pins the precise code/data snapshot used to produce all numbers.

MAJOR

P1B-M1
- Location: Sec. III (Scope statement), throughout; pp. 3–6, 13
- Issue: Mixing Planck PR4/NPIPE high-ℓ with Planck 2018 low-ℓ and lensing. The paper acknowledges this is the “standard Cobaya pairing” and flags a missing pairing-swap control. However, ΔNeff and H0 inferences can be sensitive at the 0.1–0.2σ level to this choice.
- Required fix: Provide a release-consistency check: run at least one configuration with PR4-consistent low-ℓ and lensing (where available) or, alternatively, an “all-2018” control using PR3 high-ℓ with 2018 low-ℓ/lensing on the same likelihood stack. Report the shift in ΔNeff and H0 means with uncertainties. If not feasible, clearly quantify an upper bound on possible bias (e.g., via literature benchmarks) and move the PR4/2018 mixture to a labeled limitation in the abstract and conclusions.

P1B-M2
- Location: Sec. IV; Fig. 3; pp. 6–9
- Issue: The NaMaster birefringence estimator is an unweighted χ2 fit across bandpowers [Eq. (1)], which is deliberately suboptimal. The resulting ≈12% multiplicative under-recovery is ascribed mainly to equal weighting of noise-dominated high-ℓ bins. While the paper shows that inverse-variance weighting reduces the bias to −0.006°, the baseline kept throughout is the unweighted estimator and a “systematic floor” of 0.040° is carried forward.
- Required fix: Promote the inverse-variance–weighted estimator to the primary pipeline result in the main text and figure, reporting both the recovered β and the uncertainty of the mean over N = 500 realizations, alongside the unweighted baseline for comparison. Quantify the uncertainty on the stated “worst-case bias” (e.g., standard error on the 500-MC mean at βinj=0.342°) and state it explicitly wherever the 0.040° number is used. Clarify that the 0.040° is an MC-measured, estimator-specific bias on synthetic skies, not a sky-measurement systematic.

P1B-M3
- Location: Sec. VI; pp. 10–13
- Issue: ALP-inference relies on a single Gaussian summary likelihood for β from Eskilt & Komatsu. The coupling posterior and the “m ≫ H0 (median ≈36 H0)” statement are prior-sensitive. While the paper is transparent about priors, a minimal robustness check is missing.
- Required fix: Add a sensitivity test: rerun the fixed-Caγ = 8 configuration with σβ inflated by, e.g., 25% (to emulate modest non-Gaussianity/unknown correlations) and report the shift in the m/H0 median. Alternatively, add a run swapping in the ACT-only or Planck-only β constraints (with an explicit correlation caveat) to show the qualitative robustness of the “m greater than H0” tendency. Present these as robustness checks without claiming independent confirmation.

P1B-M4
- Location: Sec. VI and Table IV; pp. 10–13, 20
- Issue: The spectator-status energy-density criterion is discussed qualitatively. The posterior slice statistics for Ωa < 0.1 and < 0.01 are reported, but the exact Ωa(a) used for selection is not explicitly stated (e.g., whether θ is small-angle approximated, or the full potential is used; at which epoch; and with what normalization).
- Required fix: Provide the explicit expression and evaluation point used for Ωa (e.g., today), including normalization to ρcrit (which H0 value) and whether the full cosine potential or quadratic approximation is used. Confirm that the Ωa diagnostic is derived per-sample from the numerically integrated trajectory, not from a simple scaling ansatz. Add a line in Appendix C describing this calculation.

MINOR

P1B-m1
- Location: Abstract; p. 1
- Issue: “the ∆Neff extension does not reduce the residual ∼ 3.6σ tension …” The 3.6σ figure matches the full-tension chain. For the Planck+BAO+SN chain the tension is ≈3.5σ.
- Required fix: Qualify that 3.6σ refers to the full-tension stack; optionally add the ≈3.5σ value for Planck+BAO+SN.

P1B-m2
- Location: Sec. III (MB–H0 check), pp. 4–5
- Issue: Reported MB–H0 “3.2σ” offset is normalized by σMB only, not conditioning on joint covariance along the SN degeneracy. The caveat is present but could be clearer at first mention.
- Required fix: Add “normalized by the MB marginal only” at first mention, and provide the value of the correlation ρ(MB,H0) if available, or state it is not used.

P1B-m3
- Location: Sec. IV (Noise model); p. 7
- Issue: Pixel area quoted as Ωpix = 47.21 arcmin2. The exact HEALPix Nside=512 area is ≈47.3 arcmin2.
- Required fix: Either cite the exact computed value used by the code (with enough digits) or add “≈” to indicate rounding.

P1B-m4
- Location: Sec. III; pp. 4–6
- Issue: The SH0ES likelihood is labeled “H0.riess2020Mb” while Ref. [9] is 2022 (ApJL 934, L7).
- Required fix: Harmonize the label to the 2021/2022 SH0ES release the likelihood corresponds to, or clarify the provenance of the MB value used in the YAML with a precise citation.

P1B-m5
- Location: Sec. IV; pp. 6–9
- Issue: The EE template is described as “Planck-2018 semi-analytic” without specifying the exact parameter set/spectrum file.
- Required fix: Identify the exact EE template source (e.g., best-fit parameters table or file checksum) to ensure reproducibility without mining the codebase.

P1B-m6
- Location: Sec. IV; Fig. 3 caption; p. 7
- Issue: The standard error of the 500-MC mean is used in the fsky sweep but not reported for the canonical fsky=0.32 point in the main text.
- Required fix: Add the measured σβ/√N = 0.046°/√500 ≈ 0.002° for fsky=0.32 where you quote β̂=0.238° to put the bias estimate on the same statistical footing across points.

P1B-m7
- Location: Sec. VI; pp. 10–12
- Issue: Statements that required Caγ exceed standard KSVZ/DFSZ values “O(1)” are made without a concrete reference.
- Required fix: Cite a standard review or original references summarizing typical model expectations for Caγ (e.g., PDG axion review, or classic KSVZ/DFSZ coupling ranges).

P1B-m8
- Location: Table I; p. 18
- Issue: The naive two-Gaussian combo S8 = 0.814 ± 0.009 differs slightly from the exact quadrature (≈0.0086).
- Required fix: Either report 0.0086 (rounded to 0.009) with a note “from inverse-variance combination” or provide the exact calculation method used.

NIT

P1B-n1
- Location: Throughout
- Issue: Heavy use of path-like artifact names in main text (e.g., reproducibility/..., pod1_...) is distracting.
- Required fix: Move long path strings to a brief “Reproducibility map” appendix table and refer to them by short labels in the text.

P1B-n2
- Location: Abstract; p. 1
- Issue: Grammar/clarity: “are not directly comparable to each other’s published sky significances” reads awkwardly.
- Required fix: Change to “are not directly comparable to the published sky significances.”

P1B-n3
- Location: References [4], [18]; pp. 16–17
- Issue: Future-dated arXiv numbers (e.g., 2509.x) appear unusual; PRD prefers current, verified references.
- Required fix: Verify years and arXiv identifiers are correct and publicly accessible; if preprints are not yet public, update before acceptance.

Methodological audits of key scalars and internal arithmetic

- ΔNeff posteriors (Table I, Figs. 1–2): −0.020 ± 0.169 (full-tension) and +0.058 ± 0.179 (Planck+BAO+SN) — consistent and traceable to chains as described.
- H0 tensions with SH0ES 73.04 ± 1.04: full-tension 67.68 ± 1.06 gives Δ=5.36 km/s/Mpc with σcomb=1.49 → 3.60σ; Planck+BAO+SN 67.78 ± 1.09 gives 3.49σ. The abstract’s “∼3.6σ” is strictly accurate for full-tension; clarify as per P1B-m1.
- w0wa tail distances: |w0+1|/σw0 = 0.188/0.044 = 4.27σ; |wa|/σwa = 0.667/0.186 = 3.58σ. Matches “+4.3σ” and “−3.6σ”.
- Phantom-crossing redshift: w0 + (1 − a×)wa = −1 ⇒ 1 − a× = (−1 − w0)/wa = 0.282 → z× ≈ 0.39 as stated.
- H(z=0.5) fractional deviation: with Ωm=0.314 and (w0,wa)=(-0.812,-0.667), I compute ≈ +1.7% relative to ΛCDM, matching text.
- MB–H0 degeneracy constants: at (MB,h)=(−19.253,0.7304) gives −18.569; at (−19.263,0.6768) gives −18.415; Δ=0.156 mag; normalized by σMB=0.049 gives 3.18σ; matches “∼3.2σ”, with appropriate caveat included.
- NaMaster pipeline multiplicative bias: 0.238/0.27=0.881; 0.302/0.342=0.883 → ~12% under-recovery; fsky scaling of template SNR is consistent with numbers quoted.
- Pixel-noise RMS: Nside=512 → Ωpix ≈47.3 arcmin2 → σpix = 10/√Ω ≈ 1.455 μK; matches text.
- ALP birefringence: α/(4π) ≈ 5.81×10−4; times Caγ=8 and Δφ/fa=1.06 yields 4.93×10−3 rad = 0.283°; matches ~0.28°.
- Inverse-variance β combination: 0.241 ± 0.061 and 3.9σ naive significance correctly computed; manuscript clearly flags this as an upper bound and not the headline.
- Mass prior range vs H0 energy: log10(ma/eV) ∈ [−35, −30] corresponds to m/H0 ≈ 7×10−3 to 7×102 (H0 ≈1.44×10−33 eV), consistent with text.

Length and focus
For the limited novelty (proxy ΔNeff null, pipeline MC validation, ALP consistency), the manuscript is verbose (20 pages). The extensive chain bookkeeping and path-level artifact references can be shortened or relegated to an appendix without loss of scientific content. Recommended maximum length is 14–16 pages, moving code-path details and convergence minutiae to a concise “Reproducibility Appendix.”

Effect sizes and clarity
The paper commendably quantifies an expansion-rate effect size (+1.7% at z=0.5). For NaMaster, report the per-realization σβ and the standard error on the mean explicitly alongside β̂ at each fsky to complete the effect-size picture (P1B-m6).

Abstract-last drift sweep
Abstract claims are mostly consistent with the body and appropriately caveated. Add the clarifications from P1B-m1 (3.6σ applies to full-tension chain) and explicitly reiterate that the 0.040° “systematic floor” is an MC pipeline-recovery figure on synthetic skies, not a sky-measurement systematic.

## Summary recommendation
MAJOR REVISIONS

The manuscript is careful and technically competent, but PRD publication requires: (i) an overlap-safe w0wa analysis (or removal of product-likelihood results from the main text), (ii) stable DOIs for all artifacts, (iii) a release-consistency check for the Planck likelihood pairing, and (iv) promoting the inverse-variance–weighted NaMaster estimator to the primary result with explicit uncertainty on the MC-measured bias. Addressing these points will resolve the principal methodological concerns; the remaining issues are minor edits and clarifications.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B — ADDITIONAL FINDINGS AFTER SECOND-PASS AUDIT (new items only)

ESSENTIAL

P1B-E3
- Location: Table IV; Sec. VI (discussion of fixed-Caγ and continuous-prior runs)
- Issue: Ambiguity/inconsistency in the “m/H0 (Caγ = 8)” column. Table IV summarizes posterior slices from the continuous-prior c5 chain (Caγ sampled), yet reports an m/H0 statistic labeled “(Caγ = 8).” It is unclear whether this is (i) directly from the fixed-Caγ = 8 run (run1_full), (ii) re-evaluated per-sample at Caγ = 8 by some mapping, or (iii) simply mislabeled. As written, readers could misinterpret a derived quantity from the Caγ-free chain as a result from the Caγ = 8 chain.
- Required fix: Either (a) replace the Table IV m/H0 entries with those computed from the fixed-Caγ = 8 chain (and label the table rows accordingly), or (b) explicitly define how “m/H0 (Caγ = 8)” is constructed from the Caγ-free chain (algorithm and equations), or (c) remove the parenthetical “(Caγ = 8)” and present m/H0 only from the chain actually used. State clearly in the caption which chain each statistic comes from.

MAJOR

P1B-M5
- Location: Table I vs Table II; Sec. V.A; footnotes; pp. 9, 18–19
- Issue: Lensing likelihood heterogeneity across chains. The ΛCDM+ΔNeff chains use planck 2018 lensing.clik, while the w0wa chain uses planck 2018 lensing.native. Mixing .clik vs .native implementations can shift posteriors at the 0.1σ level and complicates cross-comparisons (e.g., S8).
- Required fix: Provide a control rerun to quantify any shift introduced by .clik vs .native for at least one configuration (same data otherwise), or harmonize the lensing likelihood across all headline chains and report the impact on H0, S8, and w0wa.

P1B-M6
- Location: Sec. VI; Appendix C; pp. 10–13, 15–16
- Issue: ALP ODE initial-condition and integrator reproducibility. The text mentions an independent RK4 re-integration at zinit = 3000 with θ̇ = 0 as a check, but it is not explicit what initial redshift, θ̇ initialization, stepper/tolerances, and background H(z) sampling are used in all production MCMC runs (for which ∆φ/fa is derived).
- Required fix: In Appendix C, specify for the production ALP runs: initial redshift ainit or zinit, θ̇init prescription, integration variable (e.g., ln a), ODE solver type and tolerances, step-size control, and background H(z) source. Add a small robustness test showing that ∆φ/fa is stable (≤1–2%) under reasonable variations of zinit and solver tolerances.

P1B-M7
- Location: Sec. IV (template definition); Fig. 3; pp. 6–9
- Issue: Pixel-window treatment of the EE template is asserted to “cancel,” but the exact operation is not documented. It’s only stated that the template is “evaluated at the same Nside,” which is ambiguous.
- Required fix: State explicitly whether the HEALPix Nside=512 pixel window is applied to CEE,tmpl (and how), and cite the exact code path or checksum of the spectrum used. If not applied, justify the cancellation logic more formally or provide a numeric check that applying vs not applying the pixel window to the template leaves β̂ unchanged within the quoted MC mean error.

P1B-M8
- Location: Eq. (1) and surrounding text; Sec. IV; pp. 7–9
- Issue: Potential angle-units ambiguity in the χ2(β) template fit: β is displayed and reported in degrees throughout, but sin(4β) in Eq. (1) expects radians in implementation.
- Required fix: Add an explicit statement that β is converted to radians before evaluating trigonometric functions and reference the exact code line or unit test that enforces this. This is a common, high-impact pitfall in rotation-angle pipelines.

P1B-M9
- Location: Sec. III (BBN consistency); pp. 3–5
- Issue: CAMB PArthENoPE BBN-consistency validity range is asserted but not referenced. The prior Neff ∈ [2.046, 5.046] pushes near the edge of typical calibration domains.
- Required fix: Cite CAMB/BBN documentation confirming validity over this Neff range, or add a brief free-YHe control run (or a literature benchmark) demonstrating that the ΔNeff posterior is stable to the YHe treatment at the quoted precision.

MINOR

P1B-m9
- Location: Sec. IV; robustness battery; pp. 8–9
- Issue: High-ℓ bins above the map bandlimit. The text states “restricting the fit to ℓ ≤ 1024 changes nothing (0.238°),” but no quantitative uncertainty is given. Since mask-induced mode coupling can introduce a small β-dependence above ℓmax (maps computed to 1024, workspace to 1536), a numerical confirmation should be shown on equal statistical footing.
- Required fix: Report the recovered β̂ and the standard error of the 500-MC mean for the ℓ ≤ 1024 restriction, and compare it to the canonical result to document statistical equivalence.

P1B-m10
- Location: Sec. III (MB–H0 check); pp. 4–5
- Issue: SN degeneracy constant written as “MB − 5 log10(h) ≈ const” and “MB − 5 log10(H0/[km s−1 Mpc−1]) + 10 = const.” The +10 is nonstandard and may confuse readers.
- Required fix: Provide a one-line derivation or a standard reference for the chosen normalization of the degeneracy line to avoid ambiguity about constants and units.

P1B-m11
- Location: Sec. IV (Noise model); p. 7
- Issue: ΔP convention and the “no √2 factor” for Q and U. While consistent with some CMB conventions, others define ΔP per Stokes differently.
- Required fix: Add a citation (e.g., Planck Blue Book or a NaMaster/ACT convention note) stating that ΔP refers to the per-Stokes Q/U depth used here, and that σpix = ΔP/√Ωpix is applied identically to Q and U.

P1B-m12
- Location: Throughout Sec. IV; figures
- Issue: Trigonometric template equivalence. The text alternates between ½ sin(4β) CEE and sin(2β)cos(2β) CEE. While equivalent, this may cause reader confusion when matching to code.
- Required fix: Pick one form for the main text and note the equivalence once, or show the exact code expression to avoid misinterpretation.

P1B-m13
- Location: Table I; Sec. V.A; p. 18
- Issue: CamSpec/Planck likelihood versions are described descriptively (“NPIPE high-ℓ CamSpec”), but no exact version/hash is given.
- Required fix: Add the precise CamSpec and Planck likelihood versions (or git hashes/checksums) used, for strict reproducibility.

NIT

P1B-n4
- Location: Acknowledgments; p. 14
- Issue: “Claude (Anthropic) as an AI research assistant” acknowledgment. Some journals discourage or require specific wording regarding AI assistance.
- Required fix: Check PRD policy and adjust wording accordingly (e.g., clarify that AI tools were not used to generate scientific content, code, or analysis decisions, or remove if necessary).

P1B-n5
- Location: Sec. IV; Fig. 3 caption and panel labels
- Issue: Ensure axis labels explicitly include units “deg” for both injected β and recovered β̂ in Fig. 3 panels to match the main-text usage. The main text consistently uses degrees; the figure should be explicit.

Explanation
These issues focus on cross-configuration comparability (lensing pipeline difference), unambiguous provenance/labeling of ALP-derived quantities in Table IV, reproducibility-critical details for the ALP ODE integration, and implementation specifics that commonly cause subtle biases in birefringence pipelines (pixel window on the template; rad/deg handling). They were not covered in the initial review and, if addressed, will further solidify methodological rigor to PRD standards.