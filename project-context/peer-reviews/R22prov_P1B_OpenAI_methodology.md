# P1B R22prov — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6961 chars)
**Wall time**: 362.2s

---

Referee report on: Technical Verification Companion to the ECH Spin-Torsion Program: ΛCDM+ΔNeff MCMC Proxy, NaMaster Pipeline Recovery, and a Birefringence Consistency Check with a Spectator-ALP Model

Overall scope and standards
- This submission is positioned as a technical verification companion, not a primary cosmological analysis. That is fine in principle for PRD, but the same standards of methodological clarity, dataset traceability, statistical correctness, and internal consistency apply.
- I audited all reported scalars in the abstract and conclusions against the body. Many core numbers are internally consistent. However, there are several essential issues that must be fixed before this can meet PRD standards, most notably dataset-version inconsistencies, a mislabeled figure axis for ΔNeff, a mismatch between figure title and dataset, a reference entry containing internal editorial notes, and ambiguous/uncited overlays in a key figure. I also flag several major issues that require clearer documentation and minor/nit fixes.

Findings

ESSENTIAL

P1B-E1
- Section V.A, p. 6, and elsewhere
- Problem: Dataset-version inconsistency between different parts of the paper. Examples:
  - Sec. II and Table II clearly use DESI DR2 BAO + DES-Y5 + Pantheon+ in the w0wa analysis.
  - Sec. V.A (the four ΔNeff dataset combinations) lists “+DESI 2024 DR1 BAO” and “+DES Y3 S8,” while Table I and Fig. 1/2 results are described as “Planck+BAO+SN(+H0+S8).”
  - The paper does not explicitly and unambiguously list the BAO release and DES S8 prior used in each of the ΔNeff chains (Planck+BAO+SN; full-tension).
- Required fix: Provide a clear, consolidated table listing, for each dataset combination actually used in the ΔNeff runs, the exact likelihood components, versions/releases (e.g., DESI DR1 vs DR2, DES Y3 vs Y5), and how they enter (priors vs full likelihoods). Ensure the text of Sec. V.A matches that table, and update captions (Table I, Fig. 1, Fig. 2) accordingly. If the w0wa chain is a separate analysis with DR2+DES-Y5 while the ΔNeff chains use DR1+DES-Y3, state that separation explicitly and consistently throughout.

P1B-E2
- Fig. 2(a) (p. 5)
- Problem: Axis labeling confusion and incorrect standard-model annotation.
  - The x-axis is labeled “Neff,” but the paper samples ΔNeff; the plotted distributions (centered near 0) are clearly for ΔNeff.
  - The vertical annotation reads “SM (Neff = 0)”; if read literally as Neff this is false (SM Neff ≈ 3.046). It is only correct for ΔNeff.
- Required fix: Relabel the x-axis to “ΔNeff” and correct the annotation to “SM (ΔNeff = 0).” Verify that any other panel labels referencing Neff/ΔNeff are consistent.

P1B-E3
- Fig. 3 + text in Sec. IV, p. 6
- Problem: Dataset mismatch in figure labeling vs text. The figure header text (visible in the plotted panel) says “NaMaster, Planck SMICA,” while the caption and the methods text say the analysis uses the Planck Commander CMB polarization map.
- Required fix: Ensure the figure panel and caption both refer to the same input map (Commander if that is what is used). If multiple maps were tested, present both clearly or restrict to one and correct the figure graphic.

P1B-E4
- Ref. [15], p. 12
- Problem: Reference contains internal editorial/log text: “the value used at L256/L416 of P1B.” This is not acceptable in a PRD bibliography.
- Required fix: Remove all internal-notes text. Supply the correct, citable bibliographic information for the specific result used (including the reported β = 0.30 ± 0.11 deg), with correct author list and journal.

P1B-E5
- Fig. 2(a) overlays, p. 5
- Problem: Several vertical overlays are uncited/unclear or potentially incorrect in value/context:
  - “WP4 reheating [0.05, 0.40]”, “WP4 decay [0.01, 0.25]”, “BBN 2 upper (0.41)”, “ACT DR6 central (0.40)”. It is unclear what these represent (forecasts? priors? external constraints?) and how they are derived. “ACT DR6 central (0.40)” for ΔNeff is not a standard published central value I am aware of; if it is an Neff–3.046 mapping from a specific ACT analysis it must be cited precisely.
- Required fix: Either (a) remove these overlays entirely, or (b) provide precise citations and one-sentence definitions in the caption explaining each band/line (including whether they refer to Neff or ΔNeff, and from which paper/dataset) and ensure numerical values match the cited source. As drawn, they are misleading.

P1B-E6
- Sec. IV, SNR reporting, p. 6
- Problem: The paper reports “SNRSE = 20.32” (and 25.71 for β = 0.342°), and later SNRreal ≈ 0.91 and ≈ 1.15, but does not state the actual per-realization σβ used in the canonical 500-MC fsky = 0.32 run. The sky-fraction sweep reports per-realization σβ values (0.029°, 0.033°) that would imply enormous SNRSE values, but those are for different masks. For reproducibility and to prevent misinterpretation, the canonical σβ value used to compute SNRSE and SNRreal must be stated numerically.
- Required fix: Add the per-realization σβ for the canonical fsky = 0.32, Nside = 512, N = 500 run. Provide the exact numeric SNRSE and SNRreal values with that σβ, so the reader can reproduce the 20.32 and 25.71 values from first principles.

P1B-E7
- Sec. VI, Eq. (3) and paragraph “Caγ(Δφ/fa) ≈ 10.3…”, p. 7–8
- Problem: While the β = (αEM/4π) Caγ (Δφ/fa) normalization is standard, the text toggles between radians and degrees without an explicit conversion statement at the point where numbers are quoted. The statement “β = 0.342° in radians is 5.97 × 10−3, the prefactor… 5.8 × 10−4, giving Caγ Δφ/fa ≈ 10.3” is correct only if β is in radians there; elsewhere β is given in degrees.
- Required fix: Add a one-sentence clarification that all intermediate products in the Caγ (Δφ/fa) calculation use β in radians, and restore the units explicitly in that derivation for clarity.

P1B-E8
- Sec. IV/Fig. 2(b), p. 5
- Problem: The x-axis label in panel (b) is garbled: “(x xfull_tension) / full_tension” appears nonsensical. It likely intends a standardized shift, e.g., (x − xfull_tension)/σfull_tension.
- Required fix: Correct the axis label to the intended standardized variable (e.g., Δ/σ) and define it in the caption.

MAJOR

P1B-M1
- Sec. VI (ALP posterior fractions), p. 8–9
- Problem: The statement “69% of the posterior mass falls inside the EOM-required band [9, 51]” for Caγ is made for a likelihood that is a single Gaussian on βobs and priors that strongly shape the degeneracy Caγ(Δφ/fa) ≈ const. This posterior fraction is significantly prior-dependent (e.g., the wide prior on θi and log10 ma). As written, the reader cannot assess the robustness of “69%” to the chosen priors.
- Required fix: Add a short sensitivity check: report how this posterior mass fraction changes under at least one alternative reasonable prior (e.g., a narrower θi range or a log-uniform Caγ prior), or explicitly state that the fraction is primarily prior-dominated given the single-constraint likelihood. At minimum, provide the exact prior choices used in the continuous-prior run (you do for Caγ and ma; also state θi prior bounds in the main text where the 69% number is discussed).

P1B-M2
- Sec. IV, pipeline configuration, p. 5–6
- Problem: The beam description for the Commander CMB Q/U map reads “Planck-2018 effective Gaussian beam (5 arcmin FWHM at 143 GHz), we degrade to Nside = 512.” Commander is a component-separated CMB map with an effective beam; tying this to “143 GHz” is potentially misleading (Commander is not simply the 143 GHz channel).
- Required fix: Rephrase to “effective 5 arcmin Gaussian beam (Commander CMB map, Planck 2018)” and remove the 143 GHz parenthetical unless you actually used a 143-GHz-channel map.

P1B-M3
- Sec. III, full-tension combination definition, p. 3–5 and Table I
- Problem: The “full-tension” stack composition is not explicitly enumerated in one place. The table caption lists nuisance parameters but not the dataset list; the text mentions SH0ES and S8 but not explicitly which S8 prior and BAO release.
- Required fix: Add to Table I caption (or a small table alongside) the precise list of likelihoods included in “full-tension” (with versions and whether they are priors or full likelihoods). This overlaps with P1B-E1 but is a specific table-level correction.

P1B-M4
- Sec. III, MB–H0 “exactly corresponds” language, p. 5
- Problem: The computed offset along the SN degeneracy is 0.155 mag, “∼3.2σ relative to σMB = 0.049,” and the text then says it “corresponds exactly to the canonical 3.6σ Hubble tension.” 3.2σ is not “exactly” 3.6σ.
- Required fix: Soften to “is consistent with the ∼3.6σ Hubble-tension level” or give the combined-tension calculation (which you do elsewhere: 5.35/1.49 ≈ 3.59σ) and avoid “exactly.”

P1B-M5
- Sec. III/IV, Planck likelihood mixing, p. 3–6
- Problem: You mix Planck PR4 CamSpec high-ℓ with Planck 2018 low-ℓ TT/EE and 2018 lensing. This is a legitimate but nonstandard combination.
- Required fix: Add one sentence justifying this choice (e.g., PR4 high-ℓ availability paired with stable 2018 low-ℓ/lensing likelihoods), and state the CamSpec version/hash if possible.

P1B-M6
- Sec. IV, “Artifact:” file-path lines in main text, p. 6
- Problem: The paper contains literal repository path callouts (“Artifact: reproducibility/…json”). These are useful for reproducibility but belong in a data-availability appendix or SI, not in the main narrative.
- Required fix: Move “Artifact:” lines to the Data and Code Availability section or an appendix, and refer to them from the main text generically.

P1B-M7
- Sec. VI, continuous-prior ALP run, p. 8–9 and Fig. 4
- Problem: The parameterization for this run uses log10(ma/eV) ∈ [−35, −30] rather than the earlier m/H0 ∈ [1, 3]. This change is material, yet not explicitly discussed when comparing results. Also, the implied m/H0 range for this prior (given H0 ≈ 1.5×10−33 eV) is ∼[0.03, 300].
- Required fix: Add a sentence quantifying the implied m/H0 range for the continuous prior, and note that it subsumes the earlier [1, 3] “natural” box. Clarify why the posterior piles to the heavier end (as you state qualitatively) and how that affects the comparison to fixed-Caγ runs.

P1B-M8
- Sec. III, “promised a Savage-Dickey ratio,” p. 4
- Problem: The wording “promised a Savage-Dickey ratio…” reads like internal process language and is inappropriate in the method exposition.
- Required fix: Rephrase neutrally to “A Savage–Dickey readout is not viable because …”

P1B-M9
- Sec. IV, ΔNeff panel annotations, p. 5
- Problem: “BBN 2 upper (0.41)” must be cited and defined (is this a 2σ upper bound on ΔNeff from BBN? From which analysis?).
- Required fix: If kept, add a proper citation and description; otherwise remove.

MINOR

P1B-n1
- Eq. (1)–(3), units, p. 6–7
- Suggest adding “β is reported in degrees unless stated otherwise; intermediate calculations use radians.”

P1B-n2
- Sec. III, footnote 1, p. 3
- Minor arithmetic language polish: You refer to both “post-burnin count … is 123,129 (within ±1% of 123,368)” and “the 119,617 figure in Fig. 1 reflects thinning.” Consider adding the exact thinning factor or GetDist setting for clarity.

P1B-n3
- Sec. IV, SNR notation, p. 6
- Typo: “SNRSE ≡ β/ˆ SE(βˆ)” should read “SNRSE ≡ β̂ √N / σβ̂” with no stray slash/hat. Please standardize β-hat formatting.

P1B-n4
- Repeated “quintom-B” terminology, p. 3–4
- Since this is a methods companion, either add a one-line definition of “quintom-B” in situ or remove jargon; do not rely on the main paper for basic definitions in this companion.

P1B-n5
- Acknowledgments, p. 10
- The explicit mention of a proprietary AI assistant (“Claude”) is unconventional for PRD; if kept, please ensure the journal permits such acknowledgments in this form. Otherwise omit.

P1B-n6
- Data availability, p. 10
- The inclusion of galaxy-spin code and datasets unrelated to this manuscript’s analyses is distracting. Consider trimming to only materials relevant to this paper (Cobaya YAMLs, NaMaster scripts, ALP chains) and move unrelated items to repositories of the other companions.

P1B-n7
- Bibliography consistency, multiple items
- Double-check [15] author list/year/journal to ensure it actually corresponds to the NPIPE β = 0.30 ± 0.11 deg result used; correct if necessary.

NIT

P1B-nt1
- Hyphenation and style: “high-ℓ TTTEEE,” “GetDist,” “NaMaster,” etc. Standardize typography throughout.

P1B-nt2
- Remove incidental colloquialisms like “canonical Hubble-tension result” or “fails catastrophically” for a more neutral tone.

P1B-nt3
- Ensure consistent use of symbols αEM for fine-structure constant vs α for instrument angle; you do this mostly, but add a brief notation line where both appear.

Arithmetic/consistency checks performed
- Abstract ΔNeff and H0 values match Table I.
- w0/wa departures: (−0.8122 + 1)/0.0436 = +4.31σ; (−0.6666 − 0)/0.1864 = −3.58σ; w0+wa = −1.4788 ± 0.1485; wpivot offset −0.0344/0.0301 ≈ −1.14σ. All consistent with text.
- MB−5 log10 H0 constants: −19.253 − 5 log10 73.04 ≈ −28.569; −19.263 − 5 log10 67.69 ≈ −28.417; difference ≈ 0.152 mag (~3.1σ for σMB = 0.049). The “exactly 3.6σ” wording should be softened (see P1B-M4).
- β normalization: αEM/(4π) ≈ 5.80×10−4; βobs = 0.342° = 5.97×10−3 rad; product ratio ≈ 10.3, matching text. With Caγ = 8 and Δφ/fa ≈ 1.07, β ≈ 0.284°; consistent with 0.29° quoted.
- MC bias values: 0.27°→0.238° bias 0.032°; 0.342°→0.302° bias 0.040° as stated.

Length
- For a technical companion, 12 pages is acceptable if the essential corrections above are made and the dataset/figure issues are resolved. No hard cap recommended, but the “Artifact:” file paths should be moved to appendices to streamline the main text.

## Summary recommendation
MAJOR REVISIONS

Justification: The manuscript is close to publishable as a well-scoped technical companion, but there are several essential problems that must be addressed for PRD acceptance: dataset-version inconsistencies (DR1 vs DR2; DES Y3 vs Y5) across sections; a mislabeled ΔNeff axis and misleading overlays in Fig. 2; a Commander vs SMICA mismatch in Fig. 3; and an internal note embedded in a reference. In addition, the ALP posterior-mass claim needs a clear statement of prior sensitivity; SNR values must be backed by explicit σβ for the canonical run; and several clarity/style fixes are needed. Addressing these will make the results reproducible and the statistical claims unambiguous.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P1B-E9
- Location: Sec. III fn. 1; Sec. VII, both referencing Table I
- Issue: The text states the “Planck-only” chain (114,992 raw samples; R̂−1 ~ 0.05) is “reported separately in Table I.” Table I contains only two columns (Full-tension and Planck+BAO+SN) and no Planck-only column or numbers.
- Required fix: Either add the Planck-only results as a third column in Table I (with sample count and diagnostics), or remove all statements that it is “reported in Table I.”

P1B-E10
- Location: Fig. 1 (corner plot)
- Issue: Mislabeled parameter axis. One axis is labeled “Neff” with tick range ~0.03–0.07, which numerically matches τ, not ΔNeff. This is a serious label error and risks confusing τ with ΔNeff. Also, if ΔNeff is shown anywhere in this corner, it should be labeled “ΔNeff” with a range centered near 0.
- Required fix: Correct the mislabeled axis to “τ” (with correct tick range) and, if ΔNeff is included, add a properly labeled “ΔNeff” axis with the correct range. Regenerate the figure to avoid any τ/ΔNeff mix-up.

P1B-E11
- Location: Table II footnote b (wpivot and ap)
- Issue: The pivot-redshift algebra is internally inconsistent. The text gives ap = 1 − Cov(w0,wa)/Var(wa) and then writes σ^2(wpivot) = σ^2(w0) + (1 − ap)^2 σ^2(wa). That second expression omits the 2(1 − ap) Cov term and is not the variance of a decorrelated linear combination. Using the provided ap = 0.668 and σ’s implies |Cov| ≈ 0.0115, which violates the Cauchy bound |Cov| ≤ σw0 σwa ≈ 0.00813, i.e., the numbers cannot be mutually consistent under the stated formula.
- Required fix: Use the correct decorrelation relation ap = 1 + Cov(w0,wa)/Var(wa) (note sign) and σ^2(wpivot) = Var(w0) + (1 − ap)^2 Var(wa) + 2(1 − ap) Cov(w0,wa), which reduces to Var(w0) − Cov^2/Var(wa) after substituting the decorrelation condition. Recompute ap, zp, and σ(wpivot) consistently from the actual posterior covariance; update Table II and the footnote.

P1B-E12
- Location: Sec. VII (Conclusions)
- Issue: Wrong cross-reference. The text cites “see §VI body text” for the 0.040° pipeline bias at injected β = 0.342°. The pipeline/injection analysis is in §IV, not §VI.
- Required fix: Change the section reference to §IV.

P1B-E13
- Location: Sec. VI, “Birefringence value” paragraph and subsequent “range” sentence
- Issue: The quoted model span “β ≈ 0.17–0.43° over Caγ ∈ [4, 12], m/H0 ∈ [1, 3], θi ∈ [0.5, 2]” is inconsistent with the paper’s own normalization and envelope. Using β(deg) ≈ 0.03325 × [Caγ (Δφ/fa)] and the stated envelope Δφ/fa ∈ [0.2, 1.1], Caγ ∈ [4, 12] gives βmin ≈ 0.03325 × (4 × 0.2) ≈ 0.027°, not 0.17°. The text itself later acknowledges the “independent-extremes product” yields [0.027, 0.44]°, underscoring the mismatch.
- Required fix: Either correct the stated lower bound to ~0.027° or justify explicitly why the joint-trajectory scan excludes the (Caγ, Δφ/fa) combinations that would produce β ≈ 0.027°, including the exact prior/trajectory restriction that raises the minimum to 0.17°.

MAJOR

P1B-M10
- Location: Sec. IV, “Pipeline configuration”
- Issue: Resolution downgrade without an explicit low-pass filter. The text says the map is degraded from Nside = 2048 to 512 and the pixel window is applied, but does not state any pre-smoothing/low-pass filter used to prevent aliasing when downgrading. With a 5′ beam to 512-pixel scale (~6.9′), omission of an explicit low-pass can bias pseudo-Cℓ (and therefore β) estimates.
- Required fix: Document the downgrade procedure, including any pre-smoothing kernel (or prove analytically why it is unnecessary here), and quantify its effect on β-bias with a MC test. If none was used, add a robustness check demonstrating negligible aliasing impact at the quoted systematic floor.

P1B-M11
- Location: Sec. III, “Independent cross-validation”
- Issue: Unquantified “0.5σ in H0 and 0.4σ in σ8” agreement with Liu et al. [11]. The manuscript does not provide the comparison numbers from [11] or the exact calculation of σ-differences.
- Required fix: Quote the H0 and σ8 values (and errors) from [11], compute the differences explicitly using a consistent σ definition (e.g., quadrature of uncertainties), and show the arithmetic yielding 0.5σ and 0.4σ. Otherwise, soften/remove the claim.

P1B-M12
- Location: Sec. VI and Appendix C (ALP-MCMC)
- Issue: “Spectator” labeling vs. priors actually sampled. The main ALP-MCMC priors θi ∈ [0.5, 2] lie in the regime where Ωa ~ O(1) (non-spectator), as the manuscript itself notes, yet the headline posterior numbers are presented under a “spectator-ALP” banner.
- Required fix: Either (a) provide a spectator-restricted posterior (e.g., θi ≲ 0.1) or (b) re-title these as “ALP consistency” results that include DE-ALP parameter space, with “spectator-consistent” results shown separately or caveated in the main text where the posteriors are quoted.

MINOR

P1B-m4
- Location: Fig. 2(a) legend vs. Table I
- Issue: Sample-count mismatch. Fig. 2 label lists “Full tension (175 545 samples), Planck+BAO+SN (132 949),” whereas Table I quotes 176,240 raw samples for the full-tension run. The small discrepancy is unexplained.
- Required fix: Clarify if the plotted counts are post-filtered/thinned subsets. State in the caption which count is being shown (raw accepted vs. post-burn-in vs. thinned) and align text/captions across figures/tables.

P1B-m5
- Location: Table I footnote (last sentence)
- Issue: Orphaned explanation: “References to ‘k = 7’ elsewhere in this paper…” No other locations in this manuscript use “k = 7”.
- Required fix: Remove or add the specific place where “k = 7” is used; otherwise the note is confusing.

P1B-m6
- Location: Sec. VI (end of paragraph discussing Caγ range)
- Issue: Stale phrasing “correcting the earlier Caγθi product,” which reads like an editing note referencing a prior draft.
- Required fix: Delete this editorial aside.

P1B-m7
- Location: Sec. VI, Fig. 4 caption, Appendix C
- Issue: Notation inconsistency for the axion mass: the main text uses m (e.g., m/H0), while Fig. 4 and Appendix C use ma. This can confuse readers.
- Required fix: Standardize to a single symbol (ma) throughout and state it once near the start of Sec. VI.

P1B-m8
- Location: Sec. III, SH0ES MB comparison
- Issue: The text says the chain MB agrees with SH0ES at “0.2σ” without stating whether this uses the joint uncertainty. Using Δ/σSH0ES alone would be ~0.37σ; using the quadrature joint uncertainty gives ~0.18σ.
- Required fix: Specify that the 0.2σ figure uses the quadrature of the two uncertainties (or adopt a consistent convention and state it).

NO DUPLICATES
- None of the items above duplicate issues from the initial report; they address new internal inconsistencies (e.g., Fig. 1 axis; Planck-only/Table I; pivot algebra), missing downgrade details, unquantified comparison claims, a mislabeled “spectator” posterior, stale editorial notes, and notation clarity.