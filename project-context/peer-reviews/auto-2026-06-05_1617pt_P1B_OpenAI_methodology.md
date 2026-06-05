# P1B auto-2026-06-05_1617pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9322 chars)
**Wall time**: 362.1s

---

Referee report on “Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model”

Overall scope and positioning
- The manuscript explicitly frames itself as a verification companion paper, not a stand‑alone spin‑torsion theory result. The three technical tracks are: a stock‑CAMB ΛCDM+ΔNeff MCMC proxy; a NaMaster pseudo‑Cl pipeline validation via MC injection; and a spectator‑ALP birefringence consistency check.
- The paper is careful in many places to separate “pipeline-recovery SNR” from sky-detection significance and to avoid overclaiming. That is good.
- However, there are several methodological inconsistencies and internal-reference artifacts that must be corrected for Physical Review D standards. The most serious issues are: (i) an internal inconsistency about the Planck dataset versions used (PR3/2018 vs PR4/NPIPE), (ii) a Table/footnote contradiction regarding a third “Planck-only” chain that is said to be “reported in Table I” but is not in the table, and (iii) references that contain internal commentary (“used at L256/L416 of P1B…”) which is not acceptable in a PRD bibliography. There are also missing or underspecified likelihood/nuisance details for the Planck CamSpec configuration and for the separate w0wa run.

Findings

ESSENTIAL

- P1B-E1
  - Location: Sec. III, p. 3–4, Table I (p. 3), footnote 1 (p. 3)
  - Problem: Contradiction about the “third (Planck-only) dataset combination.” Footnote 1 states it is “reported separately in Table I,” yet Table I contains only two columns (Full-tension and Planck+BAO+SN) and no Planck-only column or entries.
  - Required fix: Either (a) add the Planck-only column (with its current status, samples, R̂−1, and parameter means/uncertainties) to Table I, or (b) remove the statement that it is “reported separately in Table I” and clearly state that the third run is ongoing and not tabulated.

- P1B-E2
  - Location: Throughout Sec. III and Table II captions/notes (pp. 3–4, 6); dataset naming; also Sec. V (p. 6)
  - Problem: Inconsistent naming and likely mixing of Planck PR3 (2018) vs PR4/NPIPE (2020/2022) low-ℓ likelihoods. Text alternates between “Planck NPIPE CamSpec TTTEEE + lowl TT/EE + lensing” (Sec. III, p. 3) and explicitly “planck 2018 lowl.EE + planck 2018 lowl.TT” (footnote b on p. 4). Table II further lists “Planck 2018 NPIPE lowl.EE+TT + highl.CamSpec.TTTEEE + lensing.native,” which is internally contradictory (2018 is PR3; NPIPE is PR4). Using PR3 low-ℓ with PR4 high-ℓ and lensing can be done, but it must be unambiguously stated and justified; otherwise, this is a versioning error.
  - Required fix: State precisely for each dataset combination: which Planck high-ℓ likelihood (CamSpec PR3 or PR4), which low-ℓ TT/EE likelihood (PR3 or PR4/NPIPE), and which lensing likelihood (PR3 or PR4) were used. If mixing PR3 low-ℓ with PR4 high-ℓ, justify the choice (and any calibration/consistency considerations). Update all corresponding references to the correct Planck papers.

- P1B-E3
  - Location: References [15] and [22] (pp. 10)
  - Problem: References include internal commentary/version-history notes inappropriate for a PRD bibliography (e.g., [15] “the value used at L256/L416 of P1B,” [22] “Used in P1A Sec. VI to point readers to…”). This violates PRD style and introduces internal cross-document version chatter into the ref list.
  - Required fix: Replace these references with standard, clean bibliographic entries (authors, title, journal, volume, page, year, arXiv). Remove all internal notes referring to P1A/P1B/pagination/review-process context.

- P1B-E4
  - Location: Sec. V and Table II (pp. 6–7)
  - Problem: The paper reports a substantial w0–wa posterior (Table II) and uses it for interpretive statements (e.g., “phantom crossing required,” distances in σ from ΛCDM), but the w0–wa dataset/likelihood configuration is not enumerated alongside the four dataset combinations listed earlier in Sec. V.A. The likelihood stack shown in Table II (DESI DR2 BAO + Planck low-ℓ + high-ℓ CamSpec + lensing + DES-Y5 + Pantheon+) is different from the four earlier dataset combinations and lacks a complete methodological description in the main text (nuisance set, priors, etc.). Moreover, the table caption claims 16 chains, 8 cosmological + 9 nuisance parameters, which is unusually small for a Planck CamSpec high-ℓ fit.
  - Required fix: Add a dedicated subsection describing the w0–wa run: full likelihood list (with versions), the complete nuisance-parameter set per likelihood, priors for w0, wa, and other parameters, sampler settings, and convergence diagnostics. Alternatively, remove this result from the main text and relegate it to a dedicated appendix with full details. As presented, it is not reproducible to PRD standards.

MAJOR

- P1B-M1
  - Location: Table I footnote a (p. 3)
  - Problem: The footnote states “all 17 sampled parameters (7 cosmological + 10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb…)”. This is internally inconsistent: Mb is not a Planck nuisance; and the listed set seems incomplete for CamSpec TTTEEE, which typically has many more nuisance parameters (foregrounds, calibrations, beam terms). With only 10 nuisances listed, readers cannot verify what was actually varied. This undermines reproducibility.
  - Required fix: Provide the full, exact nuisance-parameter list (by name) used for each Planck likelihood in each dataset combination, categorized by likelihood (high-ℓ TT/TE/EE, low-ℓ TT/EE, lensing). Clarify which are fixed vs free. Correct the mislabeling of Mb. If a reduced-nuisance “lite” configuration is used, document and justify it.

- P1B-M2
  - Location: Sec. IV, Foreground and noise model (p. 5–6)
  - Problem: The pipeline validation injects birefringence in a cleaned Planck Commander CMB map, but draws Monte Carlo noise realizations at ACT noise level (ΔP = 10 μK·arcmin). This is acceptable as a stress test, but the implication for the reported “pipeline-recovery SNR” is not clearly quantified: i.e., this SNR (20–26) is conditional on an ACT-like noise level and specific binning choices, not Planck-like noise. The paper states this is not a sky measurement, but the reported SNR numbers may still be misread without a quantitative dependence statement.
  - Required fix: Add a one- or two-sentence quantitative statement explaining the dependence of the “pipeline-recovery SNR” on the assumed noise level and binning, and clarify that at Planck‑like noise levels the recovery SNR would differ (optionally provide an estimate or a scaled value). This avoids misinterpretation.

- P1B-M3
  - Location: Sec. IV, bias characterization (p. 6)
  - Problem: The text asserts the recovered bias 0.032–0.040° is “consistent with the apodized-mask bias expected from a 2° apodization scale,” but no reference or derivation is provided.
  - Required fix: Provide a citation (e.g., to NaMaster methodology or a mask‑induced EB leakage bias study) or a brief derivation/argument justifying the magnitude and sign of the expected bias for the stated mask/apodization. Alternatively, rephrase to “empirically observed” without claiming consistency with a theoretical expectation.

- P1B-M4
  - Location: Sec. III, “Independent cross-validation.” (p. 5)
  - Problem: The claim “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8” with Liu et al. [11] is not substantiated by explicit comparative numbers.
  - Required fix: Provide the H0 and σ8 numbers (mean ± σ) from Liu et al. [11] and from your chains for the matched dataset configuration to demonstrate the stated 0.5σ and 0.4σ agreements. Otherwise, remove the sentence.

- P1B-M5
  - Location: Sec. III and VII (pp. 3, 8)
  - Problem: The text forecasts “CMB-S4 (σ(Neff) ∼ 0.03)” without a citation.
  - Required fix: Add a standard CMB-S4 forecast reference supporting σ(Neff) ≈ 0.03 (e.g., the CMB-S4 Science Book or a more recent forecast).

MINOR

- P1B-m1
  - Location: Abstract (p. 1), Sec. IV (pp. 5–6), Conclusions (p. 8)
  - Problem: The paper juxtaposes pipeline-recovery SNR values (20–26) with sky-detection significances (2.4–2.9σ) in proximity. While multiple caveats are present, make it impossible to miss that these numbers are not directly comparable.
  - Required fix: Add the explicit phrase “not directly comparable” at each of the two places where both figures appear on the same page (Abstract; Sec. IV opening paragraph).

- P1B-m2
  - Location: Sec. VI, Eq. (3) (p. 7)
  - Problem: The equation for β mixes radians and degrees implicitly. Although the subsequent text and numerics are consistent, the equation as written will be clearer if β is explicitly stated to be in radians before conversion to degrees.
  - Required fix: Append “(β in radians)” to Eq. (3) or write β(rad) = (αEM C_{aγ}/4π) × Δφ/fa, followed by β(deg) = β(rad) × 180/π.

- P1B-m3
  - Location: Sec. III, “MB–H0 joint-posterior offset check” (p. 4–5)
  - Problem: The algebra yielding −28.571 and −28.416 is correct; the σ-level mapping uses σ_MB for a 2D compromise involving H0 and MB. This is a nuanced diagnostic; a sentence acknowledging that this is a projection along the Pantheon+ degeneracy (and hence not a 1D p-value for either parameter alone) would improve clarity.
  - Required fix: Add a sentence clarifying that the quoted “∼3.2σ” is along the MB–H0 degeneracy axis enforced by the SN likelihood and not a direct 1D discrepancy in MB or H0 alone.

- P1B-m4
  - Location: Sec. VI (pp. 6–7)
  - Problem: The “spectator” caveat is well disclosed, but because the paper is a methods companion, it would help to state explicitly that Ωa ∝ θi^2 when m ~ H0 and fa ~ MPl in the adopted units (natural units) to make the scaling argument fully explicit.
  - Required fix: Add a brief note “in natural units, ρa ~ m^2 f_a^2 θ_i^2 ⇒ Ωa ∝ θ_i^2 for fixed m ~ H0 and f_a ~ MPl.”

- P1B-m5
  - Location: Sec. V.A (p. 6)
  - Problem: You list four dataset combinations but later analyze a different fifth combination (Table II, DESI DR2 BAO + Planck low‑ℓ/high‑ℓ + lensing + DES‑Y5 + Pantheon+). This mismatch can confuse readers.
  - Required fix: Append the w0–wa combination to the bullet list in Sec. V.A, or defer the w0–wa run to an appendix with an upfront pointer.

- P1B-m6
  - Location: Fig. 1 caption (p. 5)
  - Problem: Axes lack units where appropriate (H0). Common in field, but PRD prefers clarity.
  - Required fix: Add “km s−1 Mpc−1” to the H0 axis label in the figure (or in caption) to avoid ambiguity.

- P1B-m7
  - Location: Acknowledgments (p. 8)
  - Problem: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant…” PRD has no explicit prohibition, but this is unconventional and distracts from scientific content.
  - Required fix: Consider removing or moving this to a data/code availability note. If retained, state explicitly that all scientific claims and computations were verified by the author (already present).

NITS

- P1B-n1
  - Location: Footnote a in Abstract (p. 1)
  - Problem: The repository/README details embedded in a footnote in the abstract are overly specific for an abstract.
  - Required fix: Condense footnote a and move extended dataset-version commentary to a methods section or appendix.

- P1B-n2
  - Location: Sec. IV, “Reproducibility—Full driver script…” (p. 5)
  - Problem: Pathnames with dates and local folder names read like lab notes.
  - Required fix: Move the specific pathnames to the reproducibility appendix and keep the main text higher level.

- P1B-n3
  - Location: References [3], [11]
  - Problem: “arXiv preprint (2025/2024/2025)” phrasing; stylistic consistency.
  - Required fix: Standardize reference formatting to PRD style (Authors, Title, Journal/Archive, Volume, Page, Year, arXiv).

Arithmetic/consistency spot checks

- ΔNeff and H0 values in the abstract match Table I (p. 3). OK.
- Difference H0(FT) vs SH0ES: (73.04 − 67.69)/sqrt(1.04^2+1.06^2) ≈ 3.60σ. Matches text.
- w0 and wa σ-distances in Table II: (−0.8122 − (−1))/0.0436 ≈ +4.31σ; (−0.6666 − 0)/0.1864 ≈ −3.58σ. Matches text.
- wpivot offset: (−1.0344 + 1)/0.0301 ≈ −1.14σ. Matches text.
- β-combination (Planck 0.30±0.11, ACT 0.215±0.074): β = 0.2415±0.0614 deg; significance ≈3.93σ. Matches Eq. (4) (3.9σ).
- ALP coupling-displacement product from βobs=0.342°: 0.342° = 5.966×10−3 rad; (αEM/4π) ≈ 5.8×10−4 ⇒ CaγΔφ/fa ≈ 10.3. Matches text.
- Caγ range implied by Δφ/fa ∈ [0.2,1.1]: ≈ [51.5, 9.4]. Matches stated “∼ 9 to ∼ 51.”

Length and focus
- The paper is dense but largely focused. With the corrections above, the current 10 pages are acceptable for a PRD Methods Companion. No page reduction is necessary provided the added clarifications fit within a similar length.

## Summary recommendation
MAJOR REVISIONS

The manuscript’s caution about claims and careful separation of methods vs. sky results are strengths. However, before publication in PRD, the authors must resolve the Planck dataset version inconsistencies (PR3 vs PR4/NPIPE), correct the Table I/footnote contradiction about the third chain, clean the bibliography of internal process notes, and provide a minimally complete methodological description of the w0–wa run (or move it to an appendix). Clarification of the Planck nuisance set and small additions to avoid misinterpretation of pipeline SNRs are also required. With these addressed, the paper could meet PRD methodology standards.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B — ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

- P1B-E5
  - Location: Sec. V.A (p. 6) vs Table II (pp. 4, 6–7)
  - Problem: DESI BAO dataset version mismatch. Sec. V.A states “DESI 2024 DR1 BAO [18]” among the analyzed combinations, while Table II and accompanying text use DESI DR2 BAO (and even cite [12] for DR2 elsewhere). This is a versioning inconsistency that affects reproducibility and comparisons.
  - Required fix: Unambiguously state which DESI BAO release is used in each run (DR1 vs DR2). Align the main-text list in Sec. V.A with Table II and update references accordingly.

- P1B-E6
  - Location: Sec. VI (pp. 6–7) and Appendix C (p. 9)
  - Problem: Inconsistent description of the ALP “βfree” MCMC and sample accounting. The text reports βfree = 0.344° ± 0.096° from “our internal model-independent MCMC fit … with β as a free parameter, 9,720 accepted samples across the 3 ALP-MCMC configurations described in Sec. VI (configurations Caγ = 4, 8, 12…)”. But Appendix C defines those three configurations as having Caγ fixed (4, 8, 12), and lists separate “model-independent βfree fit”. As written, it reads as if the βfree result is pooled across the three Caγ-fixed configurations, which would be inappropriate and confusing.
  - Required fix: Cleanly separate and document:
    1) the three ALP runs with Caγ fixed = {4,8,12} (report per-config sample counts and results), and
    2) the single model-independent βfree run (report its own sample count and result).
    Do not conflate their sample totals. Provide a minimal likelihood/parameter list for βfree (since it is a distinct analysis).

- P1B-E7
  - Location: Table II (pp. 4, 6–7) and Sec. V text
  - Problem: SN-likelihood combination clarity and potential double-counting. Table II’s “Likelihood stack” and “Goodness-of-fit decomposition” indicate using “DES-Y5 + Pantheon+” under the SN contribution. That appears to mean DES-SN5YR (Ref. [14]) together with Pantheon+ (Ref. [13]). This joint use requires handling overlap and cross-covariance (or explicitly asserting independence) to avoid double-counting common calibrators/low-z anchors.
  - Required fix: State explicitly whether DES-SN5YR and Pantheon+ are combined with a shared-covariance treatment (and cite the cross-covariance), or affirm that they are treated as independent with justification. List the exact SN likelihoods used, their nuisance sets, and any de-duplication or covariance blocks.

- P1B-E8
  - Location: Sec. IV scope note (p. 5) vs Sec. VI (pp. 6–7) and Appendix C (p. 9)
  - Problem: Scope contradiction around “not a competitive sky measurement.” The paper positions the birefringence content as a methods companion, yet it also presents an “internal model-independent MCMC fit” to Planck PR4 + ACT DR6 EB-spectrum likelihoods with a quoted βfree = 0.344° ± 0.096° and convergence claims. That is a sky-likelihood result. Moreover, Appendix A states “No CMB polarization map analysis code is provided beyond the NaMaster driver script; all published birefringence values are literature citations,” which conflicts with reporting a new internal βfree result.
  - Required fix: Either remove the internal βfree result entirely (and strictly cite literature values only), or provide a proper methods subsection (likelihood versions, nuisance, priors, sampler settings, convergence) and reconcile Appendix A’s statement. Also reinforce the non-competitiveness claim if retained (e.g., by showing it reproduces the literature likelihoods within errors and is used only as a cross-check).

MAJOR

- P1B-M6
  - Location: Sec. V / Table II captions and text
  - Problem: Ambiguous “lensing.native” label. The lensing likelihood is referred to as “lensing.native” without specifying whether this is Planck PR3 or PR4 (NPIPE) and which exact code/branch/version is used. This is separate from the broader PR3/PR4 low-ℓ/high-ℓ inconsistency (P1B-E2), and specifically concerns the lensing likelihood used in Table II.
  - Required fix: Name the exact Planck lensing likelihood (PR3 vs PR4/NPIPE), code version, and any non-default options. Update references accordingly.

- P1B-M7
  - Location: Sec. IV, Foreground and noise model (pp. 5–6)
  - Problem: “Conservative worst-case bias check” phrasing vs ACT-like noise. The MC realizations use ΔP = 10 μK·arcmin (ACT-like, i.e., lower noise than Planck), which inflates SNR. Calling this “a conservative worst-case bias check” is misleading if SNR is reported. It is conservative for detecting small residual biases, but optimistic for SNR. Since SNR numbers are quoted (20–26), the language should be precise.
  - Required fix: Rephrase to make clear that the noise choice is optimistic for SNR but was intended to stress-test bias; or provide paired SNR/bias numbers at Planck-like noise. This complements, but is distinct from, the quantitative dependence clarification requested in P1B-M2.

- P1B-M8
  - Location: Sec. VII, final paragraph (p. 8)
  - Problem: Misapplied citation. “GetDist posteriors … are available as an empirical test of the quintom-B scenario [12].” Ref. [12] is the DESI DR2 BAO results paper; it does not define “quintom-B.” The citation does not support the claim being made in that sentence.
  - Required fix: Replace [12] with an appropriate theory/phenomenology reference for “quintom-B” (e.g., Ref. [22] already cited) and keep [12] only for the BAO data/likelihood.

- P1B-M9
  - Location: Sec. IV, Beam and pixel window (p. 5)
  - Problem: Commander beam specification may be inappropriate. The text assumes a 5′ Gaussian beam “at 143 GHz” for the Commander CMB Q/U map. Commander is a component-separated CMB map, not a single-frequency 143 GHz map. Its effective beam for polarization should be cited and used (it may be close to 5′, but it is not “at 143 GHz”).
  - Required fix: Specify the exact Commander polarization product used (PR3 vs PR4/NPIPE, file name/version) and its effective beam window, with citation, and confirm that this is the beam passed to NaMaster (rather than a band-specific 143 GHz beam).

MINOR

- P1B-m8
  - Location: Sec. IV (pp. 5–6)
  - Problem: Wording: “The deconvolution is therefore unbiased at the 0.04° level in the worst-case injection,” immediately after reporting a 0.040° bias. That phrasing is self-contradictory.
  - Required fix: Replace with “The bias is below 0.04° in the worst-case injection.”

- P1B-m9
  - Location: Conclusions (p. 8), final NaMaster paragraph; also Abstract and Sec. IV already covered by P1B-m1
  - Problem: Another juxtaposition of pipeline SNR/bias statements with published 2.4–2.9σ sky-detection figures without the explicit “not directly comparable” qualifier in this section.
  - Required fix: Add “not directly comparable” to the Conclusions paragraph where both appear.

- P1B-m10
  - Location: Sec. VI, Eq. (3) and surrounding text (p. 7)
  - Problem: The factor “1.07” in Eq. (3) is an unstated shorthand for Δφ/fa at m ≈ 2H0.
  - Required fix: State explicitly that 1.07 = Δφ/fa for the chosen parameters (or write Eq. (3) as β(rad) = (αEM Caγ/4π) × (Δφ/fa) and then supply Δφ/fa = 1.07 for the fiducial point).

- P1B-m11
  - Location: Units across the manuscript (Table I vs elsewhere)
  - Problem: Mixed unit styles (“km/s/Mpc” in Table I vs “km s−1 Mpc−1” elsewhere).
  - Required fix: Standardize unit formatting throughout (PRD prefers km s−1 Mpc−1).

- P1B-m12
  - Location: Sec. V (p. 6), Caveats paragraph
  - Problem: Informal phrasing “the KDE estimator fails catastrophically.”
  - Required fix: Replace with neutral, technical language (e.g., “the KDE estimator is unreliable at an unsampled point in the joint tail”).

- P1B-m13
  - Location: Sec. III, “Physics interpretation (Table II)” (p. 3–4)
  - Problem: Editorial artifact “An earlier count erroneously quoted ‘98.6% quintom-B’ weight…” This reads like version‑history commentary.
  - Required fix: Remove or move to a footnote/appendix; keep the main text focused on final, verified results.

- P1B-m14
  - Location: Sec. IV, “Reproducibility—Full driver script …” (p. 5)
  - Problem: The Commander map version/file-level specificity is missing (PR3 vs PR4 product, exact filename/checksum).
  - Required fix: Add a brief identifier of the specific Commander polarization map used (release, product name), ideally in Appendix A.

- P1B-m15
  - Location: Sec. IV, “Independent verification (production 500-realization run, April 2026).” (p. 5)
  - Problem: Dated process notes in the main text.
  - Required fix: Move the date/process phrasing to Appendix A and keep the main text timeless.

NITS

- P1B-n4
  - Location: Fig. 1 (p. 5)
  - Problem: Axis label “Neff” in the triangle plot likely refers to ΔNeff but is ambiguous.
  - Required fix: Label explicitly as “ΔNeff”.

- P1B-n5
  - Location: Throughout
  - Problem: Occasional stylistic inconsistencies (e.g., “CamSpec TTTEEE + lowl TT/EE” vs likelihood package names; minor hyphenation artifacts).
  - Required fix: Standardize likelihood names to the exact package labels used in YAMLs and clean hyphenation.

Notes on arithmetic checks (Class A)
- No new arithmetic inconsistencies identified beyond those already cross‑checked in the initial report. All recomputable σ-distances, unit conversions, and combinations still match the provided inputs within rounding.