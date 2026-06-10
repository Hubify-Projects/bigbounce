# P1B auto-2026-06-08_1144pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 598.3s

---

Below are issues I found that none of the five prior reviewers raised. I focus on subtle but load‑bearing items: ΔNeff modeling assumptions (BBN/helium and neutrino mass), hidden data correlations in the “full‑tension” combo, estimator conventions and sign/units for birefringence injection, goodness‑of‑fit interpretability, and other chain‑composition pitfalls.

P1B-META-E1
- Severity: ESSENTIAL
- Section + page: Sec. III (pp. 2–4), Table I (p. 3), Sec. V A (p. 6)
- Why others missed it: Everyone scrutinized dataset naming but not the ΔNeff modeling knobs that change the posterior materially.
- Problem: The ΔNeff run never specifies the helium treatment (BBN consistency vs fixed Yp). The constraint on ΔNeff depends strongly on whether Yp is tied to ΔNeff via BBN or held fixed, and CAMB/Cobaya offer both modes.
  - Quote: “stock CAMB with ∆Neff as a free parameter… no torsion modifications.” (p. 1) and no mention anywhere of Yp or BBN consistency.
- Required fix: State explicitly whether BBN consistency is enforced (and which BBN relation/code used), or list the fixed Yp value. Report the prior on Yp if sampled. Provide a sensitivity check: ΔNeff posterior with/without BBN consistency.

P1B-META-E2
- Severity: ESSENTIAL
- Section + page: Sec. III (pp. 2–4), Table I (p. 3), Sec. V A (p. 6)
- Why others missed it: Focus stayed on CamSpec/PR3 vs PR4 labels; the neutrino‑mass setting was not queried.
- Problem: The sum of neutrino masses Σmν (and mass ordering) is not specified. Planck+BAO in ΛCDM+ΔNeff is sensitive to Σmν; fixing at 0.06 eV vs allowing Σmν to vary shifts H0, σ8, S8 and can correlate with ΔNeff.
  - Quote: No occurrence of “neutrino,” “Σmν,” or “mν” in the manuscript.
- Required fix: Declare Σmν (value, prior, hierarchy), and whether BBN consistency uses Neff‑dependent ηb. Add a short sensitivity test (fixed 0.06 eV vs free Σmν) or cite a standard that justifies the chosen setting.

P1B-META-E3
- Severity: ESSENTIAL
- Section + page: Sec. III/Table I (p. 3), Sec. V (p. 6)
- Why others missed it: Prior reviewers checked numbers but not ΔNeff priors.
- Problem: The prior range for ΔNeff is not given (and negative values are used). The posterior mean near zero can be prior‑dependent; truncation at ΔNeff ≥ 0 vs allowing ΔNeff < 0 gives different credible intervals and means.
  - Quote: No statement of the ΔNeff prior bounds or measure.
- Required fix: Report the ΔNeff prior (type and bounds). If ΔNeff < 0 is allowed, justify physically or as a pure proxy choice; otherwise re‑run with ΔNeff ≥ 0 and report both to show prior sensitivity.

P1B-META-E4
- Severity: ESSENTIAL
- Section + page: Sec. III “full‑tension chain” and MB–H0 paragraph (pp. 3–4)
- Why others missed it: Attention went to the MB–H0 algebra, not data‑independence.
- Problem: Double counting of SN information. The “full‑tension” combo uses both Pantheon+ (SN distances) and the SH0ES MB prior built from calibrating the same SNe, treating them as independent. This breaks likelihood independence and biases the joint posterior.
  - Quote: “the SH0ES H0 prior is active… sn.pantheonplus enforces a soft constraint… Mb is a single nuisance parameter sampled jointly by both sn.pantheonplus and H0.riess2020Mb.” (pp. 3–4)
- Required fix: Use a joint SN likelihood that properly incorporates the SH0ES calibration (no double counting), or remove the separate MB prior when Pantheon+ is included. Explicitly document the dependence structure.

P1B-META-M1
- Severity: MAJOR
- Section + page: Sec. IV “β injection” (pp. 5–6)
- Why others missed it: SNR/estimator issues were flagged, but not the angle convention at the map level.
- Problem: The rotation operator e2iβ is described with β in degrees elsewhere, but it is not stated that β is converted to radians in code for Q+iU rotation. Given previous unit slippage (Eq. 3), this is a real ambiguity for reproducibility.
  - Quote: “The β=0.27°, β=0.342°, and β=0 injections rotate Q+iU via e2iβ(Q+iU) before adding noise.” (p. 5) No units stated for β inside the exponent.
- Required fix: State explicitly that β is converted to radians before applying e2iβ, and confirm the sign convention (clockwise/counterclockwise) and polarization‑angle convention used (IAU vs COSMO).

P1B-META-M2
- Severity: MAJOR
- Section + page: Sec. VI, footnote 4 and main text (pp. 6–7)
- Why others missed it: Several flagged “fine‑tuning,” but not the misuse of small‑angle scaling across large θi.
- Problem: The backreaction scaling ρa ∼ m2 f2 a θ2 i is used while scanning θi up to 2 radians (beyond the small‑angle regime). The “∼25×” spectator tuning narrative relies on small‑angle scaling outside its validity.
  - Quote: “θi ∈ [0.5, 2] … ρa ∼ m2 f2 a θ2 i … the spectator label is only consistent under θi ≪ 1.” (pp. 6–7)
- Required fix: Either restrict the scaling relations to θi ≲ 0.5 and recompute backreaction consistently for larger θi using 1−cos(θ), or present separate small‑angle and full‑potential results. Re‑quantify the “25×” statement with the correct potential.

P1B-META-M3
- Severity: MAJOR
- Section + page: Table II (p. 4) and text (pp. 4–5)
- Why others missed it: Chi‑square rounding was noted; degrees‑of‑freedom and absolute fit quality were not.
- Problem: χ2 components are given without degrees of freedom, number of data points, or nuisance‑parameter penalties. Readers cannot assess absolute goodness‑of‑fit or whether the model is over/under‑fitting each block.
  - Quote: Table II “χ2 total 14037.4 ± 5.6; χ2 BAO 10.6 ± 1.8; χ2 CMB 10983.9 ± 5.3; χ2 SN 3043.0 ± 1.6.” Dof not stated anywhere.
- Required fix: Provide dof per block and total (or effective dof for Gaussian priors), and the reduced χ2. If priors contribute to χ2, specify how they are counted.

P1B-META-M4
- Severity: MAJOR
- Section + page: Sec. IV “Beam and pixel window” (p. 5)
- Why others missed it: One reviewer flagged beam provenance; none checked beam‑commutation with rotation and downgrade order.
- Problem: The sequence “degrade to Nside=512 and apply pixel window” vs rotating Q+iU is ambiguous. Rotation in pixel space and beam/pixel operations do not strictly commute on a cut sky; ordering can change EB leakage and β̂ bias at O(10−2 deg).
  - Quote: “we degrade to Nside=512 and apply the corresponding pixel window… The β injections rotate Q+iU via e2iβ before adding noise.” (p. 5)
- Required fix: Specify the exact ordering of smoothing/downgrading/rotation/masking/noise addition and verify that β̂ bias is invariant (within quoted 0.032–0.040°) under the two natural orderings. If not, adopt and document the order that minimizes bias.

P1B-META-M5
- Severity: MAJOR
- Section + page: Sec. III, Table I (p. 3), Fig. 1 caption (p. 5)
- Why others missed it: They focused on sample counts; not on parameter identifiability under the “full‑tension” stack.
- Problem: The “full‑tension” stack simultaneously includes Planck+lensing, BAO, SN, SH0ES MB prior, and a DES Y3 S8 prior while sampling ΔNeff. This combination risks over‑constraining the amplitude‑calibration/shape sector and confusing identifiability, yet there is no statement on parameter redundancy or resulting effective constraints (e.g., whether S8 prior dominates S8).
  - Quote: Table I shows S8 with tiny σ=0.008 in “full‑tension”; Sec. V A lists the S8 prior but no identifiability check.
- Required fix: Quantify parameter‑level Fisher information contributions or show posterior‑without‑prior tests (e.g., remove DES S8 prior and show S8 shift/σ). State explicitly whether adding the S8 prior is only used as a diagnostic or load‑bearing in conclusions.

P1B-META-m1
- Severity: MINOR
- Section + page: Sec. IV (pp. 5–6)
- Why others missed it: They asked for estimator definition but not its parity conventions.
- Problem: No parity/sign convention is given for EB (e.g., HEALPix/NaMaster conventions). EB can flip sign under different Q/U conventions; β̂ recovery must state the convention to be reproducible.
  - Quote: Estimator not defined; no EB sign convention stated.
- Required fix: Declare the Q/U and EB conventions (IAU vs COSMO, HEALPix sign) and confirm that the injected and recovered β follow the same convention.

P1B-META-m2
- Severity: MINOR
- Section + page: Sec. VI (p. 7)
- Why others missed it: They checked units; not the missing path‑length integral assumption.
- Problem: The birefringence formula implicitly assumes a uniform scalar evolution from recombination to today, but no line‑of‑sight integral or redshift weighting is shown. The claim that β depends only on Δϕ/fa (endpoint difference) needs a one‑line justification (it is true for uniform rotation but should be stated).
  - Quote: “Birefringence value.—For Caγ=8, θi=1, m≈2H0: β≈…×1.07≈0.29°.” No proof that only Δϕ matters.
- Required fix: Add a sentence that for a uniform rotation field, β = (α/4π) Caγ [ϕ(t0)−ϕ(t⋆)]/fa, independent of the detailed path, with a reference. If spatial fluctuations are neglected, state that explicitly.

P1B-META-m3
- Severity: MINOR
- Section + page: Sec. V A (p. 6) vs Abstract (p. 1)
- Why others missed it: They flagged PR3/PR4 naming; not the count mismatch.
- Problem: Sec. V A says “We analyze four dataset combinations,” but Table I and the text present results for only two, and no results for the other two are shown or archived.
  - Quote: “We analyze four dataset combinations…” (p. 6) while Table I has two columns; no table/figure for the other two.
- Required fix: Either include the other two combinations with full summaries or revise the text to reflect exactly the combinations reported.

P1B-META-N1
- Severity: NIT
- Section + page: Footnote a on p. 1
- Why others missed it: Focused on dataset confusion, not the process implication.
- Problem: “The repository README is the authoritative source for the dataset attribution…” A PRD paper should be self‑contained and not defer core provenance to a mutable README.
  - Quote: Footnote a, p. 1.
- Required fix: Move all dataset provenance into the manuscript (or a DOI‑archived supplement) and remove the claim that the README is authoritative.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, there are multiple essential blockers: dataset/attribution errors, missing ΔNeff modeling details (BBN/helium; neutrino mass), likelihood‑independence violations (Pantheon+ with SH0ES MB), undefined β estimator and conventions, incomplete MC variance modeling, and structural inconsistencies. My confidence that the paper would survive independent external peer review after addressing all essential/major items is moderate: the technical work seems sound in spirit, but reproducibility and modeling‑assumption transparency must be substantially improved, and some dataset citations must be corrected or withdrawn.