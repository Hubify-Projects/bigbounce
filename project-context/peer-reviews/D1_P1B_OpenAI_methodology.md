# P1B D1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=a29137f5 pages=21
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (6825 chars)
**Wall time**: 352.2s

---

Referee report (methodology/statistics; Physical Review D)

I read the entire 21-page manuscript, including all figures, tables, captions, equations, footnotes, and appendices. Below I list all issues found, with severity classification and precise location, and I recompute/verify all load‑bearing numbers.

ESSENTIAL findings

P1B-E1
- Location: Appendix A, page 15 (“Data and Code Availability”), also Appendix A “HuggingFace datasets”
- Problem: Non-archival, unstable links and “DOI assignment is pending.” PRD requires stable, citable archival records. The section includes moving targets (GitHub main branch, non-versioned HF datasets), version-stamp prose (“in-tex v1B.0.74 stamp,” “current snapshot commit: b22f8cc9”) rather than a specific immutable release. The text also promises DOI insertion “at submission,” but no DOI is given in the manuscript version under review.
- Required fix: Before acceptance, register and cite permanent DOIs (e.g., Zenodo archival snapshots) for: (1) the exact GitHub repository state corresponding to the paper; (2) each HuggingFace dataset; (3) frozen chains and analysis artifacts referenced in the main text. Replace “pending” placeholders with the final DOIs and tag the exact code release. Remove promises to add later.

P1B-E2
- Location: Figures 2a–b, page 6
- Problem: Axis/label rendering errors. Panel (b) y-axis and panel annotations show truncated parameter symbols: “8” (should be σ8) and “m” (should be Ωm). This impairs interpretability and risks mislabeling of plotted quantities.
- Required fix: Regenerate Figure 2 with complete, unambiguous axis labels and parameter symbols (σ8, Ωm, ns, Neff, H0). Verify vector fonts embed correctly; avoid glyph clipping.

MAJOR findings

P1B-M1
- Location: Sec. IV, pp. 7–9; Fig. 3; robustness battery paragraph
- Problem: Primary estimator (unweighted χ2 template fit) is declared and used to define the “pipeline bias” that is then “carried forward” (−0.032° to −0.040°). The authors show this bias is largely an artifact of the equal weighting of high-ℓ noise-dominated bins and drops by ~80% (to −0.006°) under inverse-variance weighting. However, the manuscript still elevates the unweighted-estimator bias as the method’s “systematic floor” without stating that downstream applications will also use the same unweighted estimator. As written, the choice of canonical estimator and the bias that is “carried forward” are mismatched.
- Required fix: Either (a) adopt the inverse-variance-weighted estimator as the canonical choice and report its corresponding bias as the pipeline bias floor; or (b) state unambiguously that all downstream pipeline uses (and any bias corrections) will use the unweighted estimator, and document the exact corrective formula. In either case, present a small table summarizing bias and multiplicative under-recovery for both estimators at βinj ∈ {0, 0.27°, 0.342°} so the “carried-forward” choice is explicit and justified.

P1B-M2
- Location: Sec. III “Physics interpretation (Table II)”, p. 4; Table II caption p. 20; throughout Sec. III
- Problem: Tail-distance “+4.3σ” (w0) and “−3.6σ” (wa) are quoted from a product-likelihood chain that double-counts 20% overlapping SNe from DES-SN5YR and Pantheon+ (explicitly acknowledged). Although some caveats are present, not every instance of the σ-distances in the prose is immediately tagged as diagnostic-only and overlap-biased. For PRD readers, these can be misread as model-discrimination evidence.
- Required fix: Every occurrence of these σ-distances in the main text must carry an in-line qualifier (e.g., “diagnostic-only under overlap-uncorrected SN product likelihood; not a model-selection result”). Alternatively, move the numerical tail distances to an appendix and keep the main text qualitative.

P1B-M3
- Location: Sec. V.A datasets, p. 9; Sec. III scope/limitations p. 3; Table I caption p. 19
- Problem: Mixed Planck release pairing. The frozen chains pair PR4/NPIPE CamSpec high-ℓ with 2018 low-ℓ TT/EE and 2018 lensing.clik. A PR4-consistent re-run (c15) is shown only for the Planck+BAO+SN configuration, not for the full-tension combination. While you state 0.04σ agreement for Planck+BAO+SN, the full-tension chain—your headline H0/∆Neff numbers—is not explicitly validated under PR4-consistent low-ℓ/lensing.
- Required fix: Provide a PR4-consistent re-run for the full-tension chain (swap to planck 2020 lollipop.lowlE and planckpr4lensing) and report the resulting ∆Neff and H0 shifts. If computationally infeasible, demote the full-tension numbers to “preliminary under mixed-release pairing” and elevate the PR4-consistent Planck+BAO+SN chain as the headline. Either way, quantify a numeric bound on any pairing-induced bias for the full-tension case.

P1B-M4
- Location: Appendix A “Data and Code Availability,” p. 15; Sec. IV reproducibility notes, pp. 7–9
- Problem: Extensive internal bookkeeping (commit hashes, run directory paths, “pod” job labels, server brand names) appears in the body and appendix. PRD typically discourages ephemeral machine-specific filesystem paths and cloud vendor references in the archival paper body.
- Required fix: Move machine/path-specific details (e.g., pipelines/h200..., “RunPod H200 instances”) to a short “Computational environment” note in the Supplemental Material or replace with a generic description. Keep only persistent identifiers (release tags/DOIs) in the paper.

P1B-M5
- Location: Sec. IV footnote 4, p. 8
- Problem: The “template-fit SNR” uses σb estimated from the same 500-MC ensemble used to demonstrate recovery, which can be mildly optimistic (double use of data to set weights and evaluate significance).
- Required fix: State explicitly whether σb are estimated from an independent MC ensemble. If not, add a sentence noting potential slight optimism and, if possible, report SNR from an independent σb estimate (or a k-fold jackknife) to confirm robustness.

MINOR findings

P1B-n1
- Location: Table I caption, page 19
- Problem: Typography artifacts in numbers (e.g., “0 . 1 σ”, “132 ,949”). These likely stem from spacing macros but are visually distracting and ambiguous.
- Required fix: Clean numeric typography (remove stray spaces around decimals and thousands separators) and ensure consistent formatting.

P1B-n2
- Location: Sec. III MB–H0 joint-posterior offset, p. 5
- Problem: The constant-combination arithmetic gives a 0.156 mag offset normalized to σMB only (3.2σ). You note this is not a proper tension metric; good. For completeness, also report the offset along the Pantheon+ degeneracy including its own uncertainty if readily available, or add a sentence noting that a fully conditioned tension statistic is not provided here.
- Required fix: Add an explicit reminder that the correct cross-survey tension remains the canonical H0-axis 3.6σ and that the MB-axis figure is diagnostic-only.

P1B-n3
- Location: Sec. III one-sided bounds, pp. 3–4
- Problem: One-sided 95% bounds (∆Neff < 0.31 and < 0.40) are buried in the prose. These are useful and should be easy to find.
- Required fix: Add a row to Table I listing the one-sided 95% upper limits (with the truncation/renormalization definition in a footnote) for each dataset combination.

P1B-n4
- Location: Sec. IV, p. 7 (noise and mask)
- Problem: Pixel area value Ωpix = 47.21 arcmin^2 is correct for Nside=512; good. To help readers, add the explicit formula Npix=12Nside^2 and Ωpix=4π/Npix with units conversion in a footnote.
- Required fix: Add a short clarifying footnote/equation.

P1B-n5
- Location: References [4], p. 17
- Problem: “arXiv preprint (2025)” with no journal info for ACT DR6 birefringence. This is acceptable but please ensure the citation has full and current bibliographic details (title, authors, arXiv ID); and if a journal version exists by acceptance, update accordingly.
- Required fix: Verify/refine citation details.

P1B-n6
- Location: Sec. VI (ALP), pp. 10–14; Appendix C p. 16–17
- Problem: Coupling normalization. You note gaγ = Caγ αEM/(2πfa) and β = (gaγ/2)Δϕ, but readers will appreciate a one-line mapping to the common “E/N − 1.92” benchmarks (KSVZ/DFSZ) and a sentence on why |Caγ| ≳ O(10) is beyond minimal models.
- Required fix: Add a brief note connecting Caγ to standard ALP benchmark couplings and reiterate that the required coupling is non-minimal.

P1B-n7
- Location: Sec. VI and Fig. 4, p. 14
- Problem: The envelope Δϕ/fa vs (m/H0, θi) is referenced in prose. A small panel figure showing this envelope (e.g., contours of Δϕ/fa over m/H0 × θi) would make the parameter-space discussion clearer.
- Required fix: Add a 2D heatmap/contour panel (or move to appendix) illustrating Δϕ/fa across the prior box.

P1B-n8
- Location: Sec. V.A datasets, p. 9
- Problem: Neutrino sector: “one massive eigenstate (Σmν=0.06 eV).” This is default CAMB, but since τ and ns are sensitive to neutrino modeling, please state explicitly that the mass splitting choice follows the Planck baseline and does not materially impact ∆Neff constraints at this precision.
- Required fix: Add a one-sentence justification.

P1B-n9
- Location: Acknowledgments, p. 15
- Problem: “RunPod H200 instances” and “Claude (Anthropic) as an AI research assistant.” PRD allows acknowledgments, but brand names and AI-usage notes should be kept neutral and brief.
- Required fix: Consider rephrasing to “cloud GPUs” and “an AI assistant was used for drafting support; all scientific results were verified by the author.”

NITs (cosmetic)

P1B-N1
- Location: Throughout
- Problem: Occasional double hyphens and overuse of en/em dashes.
- Required fix: Normalize dash usage to PRD style.

P1B-N2
- Location: Sec. IV, multiple pages
- Problem: Many in-line file paths (reproducibility/...) in the main text clutter readability.
- Required fix: Move all file-path details to Appendix A and replace in text with a short pointer, e.g., “see Appendix A for artifact paths.”

Arithmetic/statistical audits (spot checks)

- Abstract ∆Neff and H0 values match Table I exactly. Verified.
- “3.6σ H0 tension”: (73.04−67.68)/sqrt(1.06^2+1.04^2)=3.61σ. Correct.
- NaMaster recovery bias: βinj=0.27° → β̂=0.238° (−0.032°), multiplicative recovery 0.238/0.27=0.881; βinj=0.342° → β̂=0.302° (−0.040°), ratio 0.883. “~12% under-recovery” correct.
- Template SNR scaling with fsky: 20.32×sqrt(0.85/0.32)=33.16, consistent with 32.98 reported; good.
- MB–H0 combination constant: −19.253−5log10(0.7304)=−18.570; chain mean −19.263−5log10(0.6768)=−18.416; offset 0.154 mag ≈ 3.1σ(σMB=0.049). Reported ~0.156 mag, ~3.2σ; fine.
- One-sided ∆Neff 95% bounds computed with truncation/renormalization: full-tension ~0.318; Planck+BAO+SN ~0.387. The latter is slightly below the reported 0.401 from weighted-sample evaluation; acceptable given non-Gaussian tails; adding them to Table I (P1B-n3) would settle this.
- CPL crossing redshift: z× ≈ 0.39; wpivot = −0.952±0.019; deviation 0.048/0.019 ≈ 2.53σ. Correct.
- H(z=0.5) fractional difference ≈ +1.7% computed from ρDE(a) formula. Correct.
- Eskilt–Komatsu β significance: 0.342°/0.094° = 3.64σ; correct rounding to 3.6σ and flagged as single-measurement Gaussian summary; good.
- Planck+ACT naive inverse-variance combine: 0.241±0.061°, 3.93σ under zero-correlation assumption; correctly labeled as optimistic upper bound.

## Summary recommendation
MAJOR REVISIONS

The analysis is careful and the numerical consistency checks are solid, but several issues must be addressed for PRD: (1) provide permanent DOIs for all code/data artifacts (essential); (2) fix figure labeling/typography issues (essential for Fig. 2); (3) resolve the estimator/bias “carried-forward” inconsistency in the NaMaster section; (4) either rerun (or explicitly bound) the full-tension chain under PR4-consistent low-ℓ/lensing; and (5) tighten presentation by moving machine-specific details to the appendix and flagging all overlap-biased σ-distances as diagnostic only. With these corrections the paper will meet PRD’s methodological and presentation standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second-pass audit)

P1B-M6
- Location: Eq. (1), Sec. IV p. 7; surrounding estimator text
- Problem: Dimensional inconsistency and mislabeling. The “χ2(β)” defined as a sum of squared bandpower residuals without a variance divisor is not dimensionless and is not a true χ2. Using a dimensionful sum-of-squares as the minimization objective is fine algorithmically, but labeling it χ2 is misleading.
- Required fix: Either (a) include an explicit σb−2 weighting to make χ2 dimensionless; or (b) relabel the objective as a “sum-of-squares” S(β) and state explicitly that it is minimized unweighted. Also state the units of the terms (power) and that the scale is arbitrary.

P1B-M7
- Location: Sec. V.B “Independent re-run cross-check (this version)”, p. 10
- Problem: Reported “effective weight” exceeds the raw sample count: “40,349 raw rows ... 107,853 effective weight.” By standard definitions, an effective sample size (ESS) cannot exceed N. It is unclear whether this “effective weight” is a GetDist-internal sum-of-weights (not an ESS) or a misreported ESS.
- Required fix: Report a properly defined ESS (e.g., via integrated autocorrelation time) that satisfies ESS ≤ N, and clarify the metric used. If quoting a GetDist “effective weight,” explain that it is not an ESS and provide the true ESS alongside it.

P1B-M8
- Location: Sec. IV “Canonical estimator choice,” p. 9
- Problem: Unsubstantiated comparability claim. The text asserts the unweighted estimator is adopted “to match the estimator configuration used in the public NaMaster driver scripts released by the published birefringence analyses (e.g., [5]).” The manuscript does not cite a specific public script/line from [5] (or another published analysis) that demonstrates the same unweighted objective.
- Required fix: Provide a precise citation (repository, commit, file path and line) in the referenced public analysis showing the same unweighted estimator, or soften/remove the comparability claim and justify the unweighted choice on its own merits.

P1B-M9
- Location: Sec. V.B independent re-run; Sec. III τ discussion and dataset pairing; Table I/II τ rows
- Problem: Mixed-release pairing and τ sensitivity not quantified. The low-ℓ EE likelihood choice materially affects τ. While pairing-induced Neff shifts are checked for Planck+BAO+SN (0.04σ), no analogous check is provided for τ (or for the full-tension stack), even though τ is directly constrained by low-ℓ EE and could be biased by 2018 vs PR4 low-ℓ choices.
- Required fix: For both Planck+BAO+SN and full-tension, report τ shifts under the PR4-consistent low-ℓ/lensing swap (planck 2020 lollipop.lowlE + planckpr4lensing). If not feasible, explicitly caveat τ as “preliminary under mixed-release pairing” and bound the potential bias.

P1B-m10
- Location: Eq. (1), Sec. IV p. 7; “Noise model and injections”
- Problem: Angle units are not stated at the point of use. The pipeline applies e2iβ to Q+iU and evaluates sin(4β) in the template, but the text does not explicitly state whether β is in radians in these trigonometric functions (the code likely uses radians; the manuscript also reports β in degrees elsewhere).
- Required fix: Add a one-sentence clarification that all trigonometric functions (e.g., sin(4β)) and Q/U rotations use β in radians; degrees are used only for reporting.

P1B-m11
- Location: Fig. 3b caption, Sec. IV p. 7
- Problem: Ambiguity in error-bar semantics. The panel overlays per-realization scatter σβ (outer bars) and the SE of the mean (inner bars) on the same points. Readers may misread σβ as an uncertainty on the mean.
- Required fix: Add a legend/annotation in the panel (or explicit caption sentence) stating that outer bars are the per-realization scatter (not an error on the mean) and inner bars are the SE on the 500-MC mean.

P1B-m12
- Location: Sec. VI (ALP), p. 12 (“At fixed β, Δϕ/fa ∝ θi along the underdamped trajectory”)
- Problem: Proportionality is regime-dependent. The ∝ θi scaling is valid in the small-angle harmonic regime; for θi ≳ O(1) anharmonicities alter the scaling.
- Required fix: Qualify the statement with its regime of validity (small-misalignment/underdamped) and note that anharmonic corrections enter for θi ≳ 1; cite a standard reference or show a brief numerical check.

P1B-m13
- Location: Sec. VI “Spectator-ALP consistency check” and “ALP dark-energy fraction Ωa”
- Problem: No explicit scaling guidance with fa. Since fa is fixed to MPl, readers cannot easily assess how β and Ωa would rescale if fa were different.
- Required fix: Add a one- or two-sentence scaling note: β ∝ Caγ (Δϕ/fa) with Δϕ set by dynamics (roughly ∝ fa for fixed θi in the harmonic regime), and Ωa ∝ (ma/H0)2 (fa/MPl)2 θi2/(1+zosc)3, so changing fa rescales both β and Ωa; give the dominant scalings and a sentence on the induced tension between matching β and keeping Ωa in the spectator regime.

P1B-m14
- Location: Sec. IV “Bins above the band limit ... carry zero template weight,” p. 8
- Problem: While including bins with zero template weight does not bias the minimizer, it changes the scale of the unweighted objective and any reported “χ2-like” goodness metrics.
- Required fix: Add a sentence clarifying that including noise-only bins above ℓmax does not affect the best-fit β (template weight zero) but does add a β-independent constant to the objective and is ignored in any fit-quality interpretation.

P1B-m15
- Location: Sec. VI “Onset of oscillations” and “Energy density today,” p. 13
- Problem: The onset criterion 3H=ma and the potential-dominated onset energy ρa(zosc) ≈ V(θi) neglect standard anharmonic and finite-temperature/onset-averaging corrections that can shift zosc and ρa by O(10%) for θi ~ O(1).
- Required fix: Add a brief sentence acknowledging these known corrections and that they are subdominant to current posterior/prior widths; optionally cite a standard treatment.

P1B-m16
- Location: Sec. IV “Robustness battery,” p. 9
- Problem: The σβ at fsky=0.32 is obtained from a separate negative-β injection rerun. While sign-symmetric in expectation, this indirection could confuse readers.
- Required fix: Add a parenthetical “we verified sign symmetry (±β give identical σβ within MC noise)” or provide σβ from a matching +0.27° rerun to avoid confusion.

Explanation of scope
- I focused only on NEW issues that were not mentioned in the initial report. Items like archival DOIs, figure label truncation, estimator/bias choice, mixed-release pairing for the headline chains, path verbosity, SNR double-use, typography, one-sided bounds in a table, pixel-area formula footnote, ACT-DR6 citation details, ALP coupling normalization note, Δϕ/fa envelope plot, neutrino-mass prior justification, acknowledgment style, and file-path clutter were already raised and are not repeated here.