chat: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=7190095b-20a6-4b2f-a642-a66d17acb84e
reviewer: Grok (Expert) | paper: P2 v1.7.106 (37pp) | date: 2026-07-09 W12
baseline W11: MAJOR | movement: CONVERTED MAJOR -> MINOR (Eq.11 budget + calibrated f_NL closed; remaining issues presentational)
verdict (from raw): VERDICT: MINOR REVISIONS
---RAW---
Referee Report (PRD, full journal standard — ruthless calibration)

Focus verification (prior-round requests)

f_NL = −35/16 = −2.1875 claim + factor-of-2 resolution: CLOSED. The central value is now stated unambiguously and consistently as the single headline number in the abstract, §I, Table I, §II A, §IV, Table V, Fig. 2, and all significance quotes. The Cai–Li discrepancy is explicitly resolved by (a) vertex-by-vertex re-summation of Cai et al.’s own four cubic operators at ϵ = 3/2 in the squeezed limit (yielding clean −35/16 with O(k₁²/k²) correction), (b) exact match to Cai’s own ϵ-ordered intermediate expressions (their Eq. A5), and (c) agreement with Li et al.’s independent general-c_s formula at c_s = 1. The printed −35/8 is traced to one spurious +(99/128)∑k_i³ term that appears only in the final polynomial collapse (their Eq. 37) and is absent from all intermediates; it is retained solely as “upper-bookkeeping reference” in Appendix A, never as a forecast input. The erroneous value’s doubled significances (5.2–5.5σ) are noted only for historical context. This meets the “single unambiguous calibrated value” requirement.

Explicit budget (Eq. 11) + sensitivity map: CLOSED / PARTIAL (minor scoping gap). Eq. (11) is now written explicitly:

text
S = |f_NL| r / σ_eff ,   σ_eff = (σ₀² + ∑_j σ_j²)^{1/2}

with r = 0.84 (noise-weighted central), σ₀ = 0.7 baseline, and additive-quadrature combination rule stated up front in §VII. Table V is the required consolidated sensitivity map: every source (template mismatch, ϵ-correction 0.6–8%, null-space r scatter, b_ϕ widening 20/30/50%, GR σ_GR ∈ {0,0.5,1.0}, joint-Fisher ρ = −0.868 proxy) is itemized with “acts on” column (numerator/denominator), combination rule, and cumulative σ_eff/significance at the corrected central value. The map cleanly separates optimistic (CMB-Fisher r ≈ 0.876, minimal systematics → 2.6–2.75σ), realistic post-budget (LSS-weighted r = 0.84 + quadrature → 1.3–2.75σ), and conservative all-combined floor (∼1.3σ).

Minor gap acknowledged in text: the construction is explicitly a “transparent scoping heuristic, not a joint multi-tracer marginalized Fisher” (correlations neglected except for the bounded ρ-proxy channel). b_ϕ and high-z GR components for MegaMapper remain transferred/scoping rather than fully recalibrated. The independent tree-level multi-tracer Fisher (§IV) validates the recast (reff ≈ 0.99) but is itself limited (Gaussian covariance, tree-level, b₂ held fixed). These caveats are already flagged; they do not invalidate the map but cap its interpretation as a sensitivity envelope rather than a definitive joint forecast.

The requested items from prior rounds are now substantively addressed.

Fresh pass — Blockers / Majors / Minors (full end-to-end read via direct PDF access + targeted page ranges 20–25)

BLOCKERS: None. No mathematical inconsistencies, unsubstantiated claims, or ethical issues survive after the f_NL calibration. The vertex re-summation and Li et al. cross-check are solid; assumption (d) cubic transmission is bounded (single-clock nonlinear adiabaticity + O((kη_bounce)²) gradient term ≲ 10^{-3}) rather than merely asserted. Current-data recast (Planck PR4 + DESI) is consistent and correctly weakens discrimination at present precision.

MAJORS (addressable with moderate rewriting; none fatal to science):

Length / scope creep (37 pp total): The core advance is an incremental literature correction + sensitivity recast. The manuscript carries extensive supporting apparatus (full 10k-sample null-space scan with SVD, three independent Monte-Carlo Bayes ensembles, independent tree-level + redshift-space Fisher pipelines, detailed vertex tables, multiple weighting-scheme scans). This is valuable but dilutes the headline result and exceeds typical PRD conciseness expectations for this class of paper. (§§II, IV–VII and App. A dominate the bulk.)

Proposed fix: Move the full vertex re-summation proof, 10k-sample histograms, phase3_.json coefficient maps, and independent Fisher code outputs (c13_, c14_*) to Supplemental Material or a dedicated Zenodo/arXiv ancillary release. Retain only the headline r = 0.84 ± 0.02 result, Table I benchmarks, and Eq. (11)/Table V in the main text. Shorten the assumption list in §I (already repeated in §II C) and condense the MegaMapper discussion (§V) to a single paragraph + illustrative envelope.

Tone on the Cai et al. correction: Repeated phrasing (“arithmetic error”, “spurious term that entered when Cai et al. collapsed…”, “the published −35/8 traces to…”) is factually correct but reads as adversarial in multiple locations (abstract, p. 1, p. 3, §II A, App. A). PRD expects neutral scholarly framing even when correcting the literature.

Proposed fix: Replace with: “We identify the origin of the printed −35/8 as a single +(99/128)∑_i k_i³ term that appears only upon collapse of the (correct) ϵ-ordered intermediates into the final polynomial (their Eq. 37). Direct vertex-level re-summation of Cai et al.’s own four operators and their ϵ-grouped expressions both recover the clean −35/16 that matches Li et al.’s general-c_s result at c_s = 1.” Keep the technical identification; remove the word “error” from the abstract and early sections.

MegaMapper scoping vs. headline presentation: The abstract and Fig. 2 quote a 1.5–3.5σ envelope that mixes the SPHEREx-calibrated systematic budget with an explicitly uncalibrated transfer of the same GR/b_ϕ numbers to MegaMapper (z = 2–5, where Addis et al. show relativistic biases are substantially larger). The text correctly labels it “illustrative” and “design-uncertainty envelope”, but the visual headline treatment risks overstating near-term reach.

Proposed fix: Remove the MegaMapper bar from the main Fig. 2 (or clearly shade it as “future scoping”). Headline only the SPHEREx 1.3–2.75σ realistic range in the abstract; move the full MegaMapper discussion to a short “Projected reach of a Stage-V facility” subsection or appendix, reiterating that the systematic floor is transferred rather than recalibrated.

MINORS (easy fixes):

Endpoint language drift: Abstract and early §IV sometimes blur which r-weighting and which systematic tier produce the quoted 2.6–2.75σ vs. 1.3–2.75σ numbers. Table V is excellent; the prose is not always tied to specific rows. (Fix: one-sentence mapping in abstract and §IV: “Optimistic (CMB-Fisher r = 0.876, σ_GR = 0): 2.6–2.75σ; realistic post-budget (noise-weighted r = 0.84 + quadrature): 1.3–2.75σ — see Table V.”)
Assumption (d) cubic transmission: The O((kη_bounce)²) ≲ 10^{-3} bound is physically well-motivated (single-clock nonlinear adiabaticity) but remains a scaling + conservation-theorem argument rather than an explicit cubic in-in evaluation with bounce-modified mode functions. Text is already transparent that this is the weakest link. (Fix: add one sentence roadmap: “A full numerical cubic verification with Wilson-Ewing bounce mode functions is in progress; the present gradient bound already places any correction well below the target σ(f_NL) ≈ 0.7.”)
Data/Code Availability statement: Scattered mentions of released scripts (c13_independent_…, phase3_…, c8_…, null_space_analysis.py) and json outputs exist, but no consolidated paragraph or DOI appears in the extracted text. Heinrich et al. per-triangle covariance is correctly noted as unavailable. (Fix: standard one-paragraph “Data and Code Availability” section before References listing the key committed files and noting the external status of the Heinrich covariance.)
Minor presentational: Some figure captions and Table V notes still carry parenthetical references to the erroneous −35/8 values for “historical comparison.” These are useful but should be minimized or moved to a single footnote to avoid visual clutter.

Overall assessment: The manuscript has moved toward publishability. The two prior-round requests (single calibrated f_NL value + explicit Eq. (11) budget + sensitivity map) are now closed or closed-with-minor-scoping-caveats that are already acknowledged in the text. Remaining issues are almost entirely presentational (length, tone, scoping clarity) rather than scientific substance. No technical blockers remain.

VERDICT: MINOR REVISIONS — the paper is now close to PRD standard; the three majors and listed minors are addressable with targeted rewriting and do not require new calculations.