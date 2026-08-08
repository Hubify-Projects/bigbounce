# EXT21 P1B ChatGPT — chat: https://chatgpt.com/c/6a3e4f3d-9854-83e8-98b2-c99099471034

Referee Report — Paper P1B, "Bounce MCMC companion"

1. Recommendation: MINOR REVISIONS

This companion paper is technically careful, unusually transparent about scope, and appropriately conservative in its interpretation. The manuscript makes clear that the ΛCDM+∆Neff run is a stock-CAMB phenomenological proxy rather than a torsion Boltzmann-code test; that the NaMaster analysis is a synthetic-sky pipeline validation rather than a competitive sky measurement; and that the ALP birefringence calculation is an accommodation/consistency check rather than a distinctive ECH prediction. Those distinctions are central, and they are stated repeatedly enough that I do not find a load-bearing overclaim.

I find no blockers and no major scientific revisions required. The remaining issues are mainly clarity, internal wording consistency, and submission-polish items. The paper would be suitable for publication after minor revisions.

2. BLOCKERS
None.

No issue found that requires substantial scientific rework, invalidates a load-bearing inference, or prevents reproducibility from the committed-artifact description as presented in the PDF.

3. MAJORS
None.

The manuscript's key scientific claims are scoped conservatively enough to avoid the usual major objections: the ∆Neff analysis is explicitly not a spin-torsion theory module; the CMB E/B pipeline exercise is explicitly not a sky-detection claim; the ALP result is explicitly not a unique ECH prediction; and the w0wa result is framed as a diagnostic cross-check with the SN-overlap caveat rather than a model-selection result.

4. MINORS

Sec. VI, pp. 11–13; Table IV, p. 21 — clarify the "spectator-safe" versus "strict θi ≤ 0.1" language.
The text sometimes equates the spectator-safe interpretation with θi ∼ 0.1, while Table IV reports the Ωa < 0.01 subset with θi percentiles 0.15/0.21/0.27 and reserves θi ≤ 0.1 as a much smaller strict sliver.
Fix: Add one explicit sentence near the first spectator-status caveat: "We distinguish the derived Ωa < 0.01 spectator-safe subset, whose posterior θi median is ≃0.21, from the stricter illustrative θi ≤ 0.1 misalignment sliver used to quantify the ∼25× tuning relative to θi = 0.5." Also adjust the conclusion sentence on p. 15 so it does not imply that the entire Ωa < 0.01 subset has θi ∼ 0.1.

Sec. VI, p. 11 — correct the phrase "spectator-consistent posterior" attached to the [0.01, 0.48]° ALP envelope.
The preceding sentence defines this span over the scan-prior box Caγ ∈ [4, 12], m/H0 ∈ [1, 3], θi ∈ [0.5, 2], which is not generally spectator-safe by the paper's own Ωa criterion.
Fix: Replace "across the spectator-consistent posterior" with "across the physical scan-prior envelope" or "across the benchmark EOM grid."

Sec. IV, pp. 7–9 — state explicitly whether the quoted NaMaster bias is ever applied as a correction or only carried as a floor.
The manuscript says the bias is "carried forward as the observed NaMaster pipeline bias" and later refers to a multiplicative under-recovery, but the reader could wonder whether any reported β values are bias-corrected.
Fix: Add one sentence after the robustness battery: "No published sky β value is corrected using this MC bias; the 0.040° figure is carried only as a pipeline-validation systematic floor."

Sec. V.C and Table II, pp. 10 and 20 — keep the w0wa result visibly diagnostic.
The SN-overlap caveat is strong and well stated, and no ln B/∆AIC claim is made. However, the table headline still presents +4.3σ and −3.6σ numbers prominently.
Fix: In the Table II caption or first row note, add "diagnostic only; overlap-uncorrected product likelihood; not a model-selection or exclusion statistic."

Conclusion, p. 15 — tighten the ALP conclusion wording.
The paragraph states "Within the Ωa < 0.01 spectator-safe subset … an ALP with fa ∼ MPl and posterior median m ≃ 40.5 H0…" and repeats the subset description in a slightly tangled way.
Fix: Rewrite as two sentences: first give the subset readout; second give the interpretation. For example: "In the Ωa < 0.01 subset, representing 13% of the posterior mass, the median mass is m ≃ 40.5 H0 and β remains consistent with the published signal. This is a tuned spectator accommodation, not a natural or distinctive ECH prediction."

Appendix B/Table V, p. 21 — either expand the claims-classification table or narrow its description.
The text says Table V classifies "every quantitative claim," but the table does not list several quantitative claims that appear important: c15 rerun values, w0wa posterior distances, Ωa subset fractions, coupling posterior ranges, θi ≤ 0.1 sliver fraction, and LiteBIRD forecast numbers.
Fix: Either add rows for these claims or retitle the table as "selected load-bearing quantitative claims."

Data and Code Availability / Appendix A, pp. 15–16 — finalize archival identifiers before journal submission.
DOI assignment is marked pending, and the repository/versioning description is otherwise detailed.
Fix: Insert the final DOI or immutable release tag before publication, and ensure the v1B.0.74 stamp, commit hash, HuggingFace dataset versions, and corrected summary artifact names all point to the same frozen state.

Figures 1–2, p. 6 — improve print readability and axis labeling.
The rendered corner plot and ∆Neff comparison are legible but small. In Fig. 2, the axis label appears visually close to "Neff" rather than clearly "∆Neff," which matters because the text repeatedly emphasizes the negative-∆Neff prior convention.
Fix: Enlarge figure fonts and explicitly label the marginal axis as "∆Neff" in the rendered graphic.

Sec. III, pp. 3–5 — consider moving part of the long burn-in/sample-count reconciliation into Appendix A.
The reconciliation is useful and transparent, but it interrupts the flow of the physical interpretation.
Fix: Keep the one-sentence reconciliation in the main text and move the detailed 20%/30% GetDist/burn-in accounting to the reproducibility appendix.

References/cross-paper placeholders — no substantive objection, but maintain final consistency.
The companion-paper citations are deliberately scoped placeholders, and I do not regard them as a defect under the stated calibration.
Fix: Before submission, ensure the final titles/version labels match the companion manuscripts' submitted titles exactly.

5. Strengths

- Excellent scope discipline. The paper repeatedly distinguishes stock-CAMB ∆Neff phenomenology from a true ECH Boltzmann-module test, and distinguishes ALP accommodation from ECH prediction. This substantially reduces the risk of overclaiming.

- Strong transparency around null results and caveats. The ∆Neff posterior is presented as a null-consistency result, the Hubble tension is explicitly not claimed to be resolved, and the w0wa analysis is caveated for SN overlap and lack of nested-sampling evidence.

- Reproducibility is unusually detailed. The manuscript gives chain counts, convergence values, burn-in conventions, corrected artifact names, repository paths, script locations, dataset links, and a claims-classification appendix. This is above the norm for a companion verification paper.

- The NaMaster validation is carefully framed. The paper makes clear that the high SNR values are injected-signal pipeline-recovery SNRs, not sky-detection significances, and it includes a useful robustness battery identifying estimator weighting and BB-shape assumptions as the main bias sources.

- The ALP section is scientifically cautious. The analysis quantifies the coupling and misalignment burdens rather than hiding them, and it explicitly notes that the same birefringence mechanism exists in standard GR.

- The tables are useful for refereeing. Tables I–V collect the core numerical claims, likelihood stacks, convergence diagnostics, spectator subsets, and claim classifications in a way that makes the paper easier to audit than a typical long-form cosmology companion manuscript.

Final assessment

The manuscript is publishable after minor revisions. I do not see a blocker or a major scientific deficiency. The most important revision is to remove small internal wording ambiguities in the spectator-ALP section, especially the distinction between the Ωa < 0.01 subset and the stricter θi ≤ 0.1 sliver. The rest of the requested changes are clarity and presentation improvements rather than substantive scientific rework.
