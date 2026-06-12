# P2 R35conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.56.pdf` md5=bd702ba5 pages=27
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (10594 chars)
**Wall time**: 465.2s

---

Referee report on “Testing the Matter Bounce with Primordial Non‑Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook”

Scope and contribution
The manuscript presents a sensitivity recast for testing the “quasi‑dust” matter‑bounce prediction fNL = −35/8 with upcoming LSS surveys, focusing on the SPHEREx multi‑tracer bispectrum forecast of Heinrich et al. (σ(fNL) ≈ 0.7, local template). The authors quantify template mismatch (overlap r ≈ 0.84–0.88), propagate this into expected SPHEREx/MegaMapper detection significances, and perform Bayesian model comparison against inflationary competitors. They also audit the factor‑of‑two discrepancy between Cai et al. (−35/8) and Li et al. (−35/16), attributing it to the −2 Im in‑in commutator doubling, and provide an extensive systematics discussion.

The paper is careful in many methodological respects: it distinguishes the on‑sky gauge‑frame estimator from the conformal‑Fermi consistency relation, repeatedly labels the work as a recast rather than an independent survey forecast, and quantifies the impact of several systematic effects. However, a number of issues must be addressed before the work can meet PRD standards. I list all findings, with severity and required actions.

Findings

P2‑E1 (ESSENTIAL)
Section: Multiple locations (pp. 11, 16, 20); also Table III caption
Problem: Version-history “Correction note” prose appears in the body of the paper, e.g.:
- p. 11: “[Correction note: an earlier version of this paragraph placed the local‑degenerate endpoint at μ/H = 3/2; … corrected here.]”
- p. 16, Table III caption: “[Correction note: an earlier version of this table quoted BF values … they are replaced here …]”
- p. 20: “[Correction note: an earlier version of this analysis quoted substantially tighter joint constraints … withdrawn.]”
PRD does not allow internal version‑history notes in the published text.
Required fix: Remove all “Correction note” and version‑history language from the manuscript body and captions. If needed, place a concise erratum‑style remark in a footnote or in a brief “Note added” (but PRD generally discourages this in the main text). Present only the final, supported results.

P2‑E2 (ESSENTIAL)
Section: Data and Code Availability (p. 22–23)
Problem: Placeholder “DOI inserted at submission” is present; no frozen release/DOI provided. PRD requires reproducibility with a citable, immutable archive (e.g., Zenodo DOI) matching the exact version used for the paper’s results.
Required fix: Provide a working DOI (Zenodo or equivalent) that freezes the exact commit used for all figures, tables, and numbers. Ensure that the DOI landing page includes instructions to reproduce the main results and that file names in the text match the archive. Remove placeholders.

P2‑E3 (ESSENTIAL)
Section: VI.C (pp. 11–14), Table II (p. 15), Table III (p. 18)
Problem: Bayes factor claims rely on a “closed‑form” integration but only Eq. (8) is given (integral definition). The numerical BF values are highly prior‑ and bookkeeping‑dependent. For PRD reproducibility standards, all inputs to the closed‑form evaluation at the reported benchmark (f̂NL = −35/8, σ = 0.7) must be explicitly stated.
Required fix:
- State explicitly the analytic expressions evaluated (e.g., likelihoods, normalizations) for each model class used in Tables II–III, including the precise priors: bounce prior (delta vs. Gaussian with σtheory), multifield competitor priors (uniform bounds), and SSFSR treated as a point hypothesis at fNL ≈ 0.
- Provide the exact numerical inputs used in each tabulated BF cell (fobs, σeff, prior widths) and the resulting BF from the closed‑form formula, so a reader can recompute them without running the authors’ code.
- For the SSFSR rows, show the likelihood ratio formula for two point hypotheses and plug in numbers (this can be a two‑line derivation in the text/appendix).

P2‑E4 (ESSENTIAL)
Section: IV (p. 9–10), V (p. 10), VII (pp. 15–17), Fig. 5 caption (p. 16)
Problem: The manuscript juxtaposes σ(fNL) or “detection significance” from different observables/estimators (SPHEREx bispectrum vs. SDB power‑spectrum, and also CMB‑like flat‑sky injection tests) in common figures and text without an explicit “not directly comparable” disclaimer at every juxtaposition as required by the review instructions. Example: Fig. 5 overlays MegaMapper SDB and SPHEREx bispectrum curves; the caption notes differing sensitivity but not that the estimators and covariances are different, hence σ values are not directly comparable.
Required fix: At every instance where σ or “significance” from distinct estimators/channels are shown side‑by‑side (text and figure captions), add a clear statement that these are not directly comparable because they use different summary statistics and covariance structures. Clarify precisely which estimator underlies each curve/bar. Do the same for the KSW‑type flat‑sky injection test vs. 3D galaxy bispectrum forecasts.

P2‑E5 (ESSENTIAL)
Section: II.C and Appendix A (pp. 6–7, 23–25)
Problem: In the main text (p. 7), the factor‑of‑two difference between Cai et al. and Li et al. is at one point described as a “convention difference,” while elsewhere (Appendix A) it is correctly framed as missing time‑ordering (−2 Im in‑in commutator) plus a separate normalization convention c. This inconsistency could mislead readers.
Required fix: Harmonize the narrative so that throughout the paper it is unambiguously stated:
- One factor‑of‑two is a normalization convention (c in BΦ).
- The other is the in‑in commutator doubling (−2 Im), i.e., Li et al. reported the single time‑ordering intermediate (−35/16) and the physical bispectrum is −35/8 in the Planck/Komatsu–Spergel convention.
Remove any phrasing in the main text that suggests the missing time‑ordering factor is a mere “convention difference.”

P2‑E6 (ESSENTIAL)
Section: IX.B (p. 21), “Auxiliary consistency check: cosmic birefringence”
Problem: The manuscript states: “bounce‑motivated physics allows for a spectator ALP coupling that predicts cosmic birefringence β ≈ 0.27° …” with no derivation or citation that yields the numerical prediction 0.27°. This is a load‑bearing number (used to assert 0.77σ consistency) introduced without provenance.
Required fix: Either (a) provide a citation to a peer‑reviewed calculation deriving β ≈ 0.27° from a specified bounce + ALP model with parameters, or (b) remove the birefringence paragraph entirely. It is not central to the paper’s contribution and, as written, is unsupported.

P2‑M1 (MAJOR)
Section: II–III.B (pp. 4–8) and IV (p. 9–10), Abstract
Problem: The injection/recovery test uses a 2D KSW‑type CMB estimator with isotropic Gaussian noise “with the published SPHEREx photometric‑z power spectra as the diagonal noise covariance,” yet the target analysis is a 3D multi‑tracer galaxy bispectrum. Even though the authors flag it as a Fisher‑space test, this hybrid noise model is methodologically mismatched and could confuse readers about its relevance to LSS estimators; it is used to corroborate r ≈ 0.90.
Required fix: Move the KSW injection/recovery test to an appendix or explicitly label it as a CMB‑style internal consistency check with no direct bearing on the 3D LSS estimator performance. Make clear that the r values used for SPHEREx forecasts come exclusively from the LSS‑appropriate weightings (Sec. III.B). Consider removing the KSW test altogether unless a minimal 3D mock with LSS‑consistent window/shot noise is added.

P2‑M2 (MAJOR)
Section: IV (pp. 9–10), VII.B (p. 16)
Problem: The quadrature combination of systematics (template mismatch, ε‑correction, bϕ prior widening, GR projections, photo‑z degradation) is described as a “transparent scoping choice” and is used to form headline “realistic” detection ranges. While the authors explicitly acknowledge that a full joint Fisher/marginalization could shift results, PRD readers need an at‑a‑glance quantitative accounting.
Required fix: Provide a table that lists each systematic, the adopted σ contribution (or fractional degradation), and the resulting σeff or significance when added in quadrature, for at least two representative scenarios (e.g., “optimistic” and “conservative”). Mark clearly that correlations are neglected. Ensure the abstract’s 2.6–5σ “realistic” envelope matches the table entries.

P2‑M3 (MAJOR)
Section: VI.C (pp. 11–14), Table II (p. 15), Table III (p. 18)
Problem: Prior dependence in Bayes factors is well discussed, but the manuscript mixes the “r → 1 bookkeeping” and “bounce‑amplitude bookkeeping with r ≈ 0.84” in prose and in the abstract. Although both are reported, it is easy for a reader to lose track of which BF applies to which bookkeeping.
Required fix: Consolidate Bayes‑factor reporting into a single canonical bookkeeping (recommended: measured‑space with the survey’s local‑template estimator, i.e., including the r factor as it affects σeff). Present the alternative bookkeeping only in an appendix, with a single sentence in the body referencing it.

P2‑M4 (MAJOR)
Section: Figures 2, 4, 5 (pp. 10, 15, 16)
Problem: Figure axis labeling and units must be explicitly visible and unambiguous. From the provided rendering, it is not fully clear that all axes include units (“kmin [h Mpc−1]”, “σ(fNL)”, “Detection significance [σ]”, “bϕ prior uncertainty [%]”), nor that the plotted values correspond to the exact numbers used in the text.
Required fix: Ensure all figure axes are labeled with quantity and units where applicable. In the captions, state the main fixed inputs used (e.g., σ(fNL) baseline, r used, fsky assumptions, k‑ranges) so a reader can reproduce the plotted points.

P2‑M5 (MAJOR)
Section: VIII.A (p. 17–18)
Problem: Planck PR4/NPIPE recast: “fNL = −0.1 ± 5.0” is recast via r = 0.876 to “−0.1 ± 5.7”. The text also states “0.75σ from the bounce prediction.” This is arithmetically consistent (Δ/σ ≈ 4.275/5.71 ≈ 0.75). However, the central value should also be consistently “rebooked” (−0.11) in the likelihood comparison; the text mentions recasting the central value in a parenthetical but could be clearer.
Required fix: State the recast pair explicitly as (−0.11 ± 5.71) and then compute the 0.75σ distance using those numbers. Keep one consistent recasting convention throughout that subsection.

P2‑M6 (MAJOR)
Section: Throughout; contribution vs. length
Problem: For a paper that is an explicit sensitivity recast (not a full end‑to‑end forecast), the manuscript is long (27 pages) and includes extensive ancillary discussions (e.g., S3 orbit basis construction, long null‑space scanning details, multiple bookkeeping paths for Bayes factors, auxiliary birefringence). PRD expects concision proportional to the contribution.
Required fix: Reduce the main text by removing/moving to appendices: (i) S3‑orbit basis and permutation‑count details; (ii) the long null‑space sampling discussion (retain only the high‑level results r and rcos in the main text); (iii) the entire auxiliary cosmic‑birefringence paragraph (or, if retained, move to appendix with a proper citation per P2‑E6). A target of ~18–20 pages for the main text is reasonable.

P2‑m1 (MINOR)
Section: III.A (p. 7)
Problem: M(k, z) definition varies by convention (presence/absence of a factor of a or g(z)); authors use M(k,z) = 2 k^2 T(k) D(z) / (3 Ωm H0^2). This is fine, but please cite a standard reference or state the convention explicitly (e.g., normalization D(0)=1, T→1 as k→0).
Required fix: Add a sentence citing Dalal et al. (2008) or Desjacques et al. (2018) to anchor the adopted convention.

P2‑m2 (MINOR)
Section: VI.A (p. 11)
Problem: The “natural curvaton prior” claim (“|fNL| ≲ a few”) is qualitative. A citation would help (e.g., curvaton prior ranges from recent reviews).
Required fix: Add an appropriate reference or rephrase as “commonly adopted in the literature.”

P2‑m3 (MINOR)
Section: References [28], [34]
Problem: [28] lacks complete bibliographic details (journal/volume/pages) and [34] has inconsistent capitalization (“dESI”). Ensure all references conform to PRD style and that quoted numbers match the cited source.
Required fix: Update references to full journal citation (or “in press”) and fix typographical issues.

P2‑m4 (MINOR)
Section: II.D (p. 7–8)
Problem: Use of “rt” for tensor‑to‑scalar ratio is unusual (standard is r). Although explained to avoid collision with r (overlap), it can confuse readers.
Required fix: Consider using a different symbol for the overlap factor (e.g., ρshape) and keep r for tensor‑to‑scalar ratio, or define a consistent notation table early on.

P2‑m5 (MINOR)
Section: Throughout (e.g., p. 6, p. 12)
Problem: Occasional typography/notation issues: “γ¯5γa”, “perms”, mid‑sentence capitalization (“GR‑marginalization”), etc.
Required fix: Clean up notation and minor typos for professional polish.

P2‑n1 (NIT)
Section: Abstract and Conclusions
Problem: “launched March 2025” and detailed timelines are not necessary for PRD scientific content and can become dated.
Required fix: Consider removing specific launch dates and keep to “in operation”/“forthcoming.”

P2‑n2 (NIT)
Section: Footnote 1 (p. 3–4)
Problem: Very detailed discussion of permutation‑count ratios, with file names in parentheses, in the main text.
Required fix: Move to an appendix; retain only the essential conclusion in the main text.

Arithmetic and dimensional cross‑checks (spot‑audit)

- |fNL|/σ naive = 4.375/0.70 = 6.25σ (p. 9–10, Fig. 2): correct.
- Template‑corrected significance with r = 0.83: 4.375×0.83/0.70 ≈ 5.19σ; with r = 0.876: ≈ 5.47σ. “5.2–5.5σ” is consistent.
- GR quadrature floor: σeff = √(0.7^2 + 1.0^2) ≈ 1.2207. Significance with r = 0.83: 3.631/1.2207 ≈ 2.98σ. Text’s “≈ 3.0σ” is consistent.
- With bϕ widened to raise per‑bin σ to 0.9–1.0 and GR σGR = 1.0: σeff ≈ 1.35–1.41. Significance with r = 0.83: 3.631/1.35–1.41 ≈ 2.6–2.7σ. “2.6–2.8σ” consistent.
- Planck PR4 recast: −0.1 ± 5.0 → divided by rCMB = 0.876 gives −0.11 ± 5.71; distance to −4.375 ≈ 0.75σ: correct.
- Ratio |−4.375|/0.015 ≈ 291.7 (“≈ 290”): correct.
- Table IV: with r = 0.84, σ = 0.7, |fNL| = 4.375 gives 5.25σ; with 2.1875 gives 2.63σ: correct.
- SSFSR BF (point vs point) with f̂ = −4.375, σ = 0.7: likelihood ratio ∝ exp((0 − (−4.375)^2)/(2×0.49)) ≈ exp(+19.53) ≈ 3.0×10^8; Table III reports 3.5×10^8: plausible given rounding. OK.

Methodological notes

- The use of Heinrich et al. (2024) σ(fNL) = 0.7 as the baseline and treating this work as a recast is acceptable provided all caveats remain and the quadrature combination is clearly labeled as heuristic.
- The operator‑algebra resolution of the Cai/Li discrepancy is clearly explained in Appendix A; ensure consistency in the main text (P2‑E5).
- The explicit separation of gauge‑frame estimator predictions and conformal‑Fermi theoretical statements is appreciated; please keep this careful separation throughout.

## Summary recommendation
MAJOR REVISIONS

The manuscript is careful in many places and the core quantitative claims (template overlap r, significance recast, rough Bayes‑factor ranges under explicit priors) are largely consistent. However, it cannot be accepted in its current form due to (i) residual version‑history text embedded in the paper, (ii) missing DOI and reproducibility pointers, (iii) the need to consolidate and clarify Bayes‑factor bookkeeping and provide explicit closed‑form inputs, (iv) explicit “not directly comparable” caveats wherever different estimators’ σ are juxtaposed, (v) removal or proper support for the birefringence “auxiliary check,” and (vi) trimming/moving non‑essential material to appendices for length. Addressing the ESSENTIAL and MAJOR items above should bring the paper to PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS AFTER SECOND PASS

P2-E7 (ESSENTIAL)
Location: Abstract (first paragraph), Sec. II A (p. 1–2), Appendix A vs A.1 (pp. 23–25)
Issue: In-in identity uses L vs H inconsistently. The abstract and main text repeatedly state/verify i⟨[ζ^3, L]⟩ = −2 Im⟨ζ^3 L⟩, but Appendix A.1 correctly derives the identity for the interaction Hamiltonian Hint: i⟨[ζ^3, Hint]⟩ = −2 Im⟨ζ^3 Hint⟩. Swapping L ↔ H is not a mere notational choice; it requires the explicit assumption (and sign) that Hint = −Lint after integrations by parts and solving constraints. That mapping is not stated or shown in the body.
Required fix: Use one operator consistently. If you intend to present the identity for Hint, change all occurrences of “L” to “Hint” in the identity, including in the abstract and Sec. II; then add a one‑sentence remark (with citation) where you use Lagrangian language that the standard single‑field cubic interaction obeys Hint = −Lint (up to total derivatives), so the commutator identity is applied with Hint. Alternatively, keep L but provide the derivation that the in‑in commutator can be written directly with L and reconcile the sign conventions.

P2-M7 (MAJOR)
Location: Sec. III B (p. 8), multiple places
Issue: Over-strong claim on template mismatch irreducibility. The text states “The mismatch is intrinsic to the shape … and cannot be removed by survey design or estimator optimization.” This is only true if one insists on a local-template estimator. A matched estimator built on the bounce template would, by construction, recover the full amplitude (r → 1).
Required fix: Rephrase to “cannot be removed if one uses a local-template estimator; a dedicated bounce‑template estimator would recover the full amplitude.” Make this explicit anywhere the irreducibility is asserted.

P2-M8 (MAJOR)
Location: Sec. II A–B (pp. 3–5), Sec. III B (pp. 7–8)
Issue: Basis-dependent “null-space” systematic treated as survey-level uncertainty. You acknowledge that the ±0.13 scatter in r depends on the choice of monomial basis and uniform Euclidean sampling in that basis. Despite this, the full ±0.13 is propagated as a systematic in headline ranges. PRD readers may interpret this as a physical modeling error bar rather than a basis/measure artifact.
Required fix: Move full technical details of the null‑space scan to an appendix and in the main text either (i) present a basis‑invariant bound/diagnostic (e.g., extremize r under an L2 norm in bispectrum shape space directly), or (ii) clearly label ±0.13 as a measure‑dependent diagnostic rather than a physical systematic and refrain from including it in the quadrature budget that underpins the 2.6–5σ headline unless you justify that inclusion.

P2-M9 (MAJOR)
Location: Sec. V (MegaMapper forecast, p. 10), Sec. VII C (pp. 16–17), Table III usage language
Issue: GR-projection degradation applied identically to SPHEREx and MegaMapper. The text explicitly notes MegaMapper is more vulnerable to relativistic projection effects at z > 2, yet the significance ranges quoted for MegaMapper appear to reuse the same σGR ∈ [0.5, 1.0] stress‑test adopted for SPHEREx. This likely underestimates MegaMapper’s true degradation if carried over numerically.
Required fix: Provide a separate GR‑contamination scenario for MegaMapper (with citation/argument) or explicitly state that the MegaMapper “2.6–5σ” is a schematic illustration reusing the SPHEREx GR budget and is not a calibrated MegaMapper result. Ideally, add a second row for MegaMapper in the GR table with appropriately larger σGR, or remove the post‑GR MegaMapper numbers.

P2-M10 (MAJOR)
Location: Fig. 2 caption and body text describing the “illustrative 3–7σ design‑uncertainty envelope” (pp. 10–11)
Issue: The 3–7σ “design‑uncertainty envelope” lacks quantitative support (no inputs or ranges are shown). This looks like an editorial band rather than a plotted, computed result.
Required fix: Either (a) provide the explicit assumptions that define the 3σ and 7σ endpoints (σ(fNL), r used, σGR, bϕ prior) and show the computation, or (b) remove this band from the figure and text.

P2-M11 (MAJOR)
Location: Sec. III B (p. 8, “projection noise” paragraph)
Issue: Quantifying “projection noise” via 1 − rcos^2 under an unweighted shape cosine is not a bound for the SPHEREx estimator, whose Fisher metric differs. Presenting < 6% as a variance fraction can be misleading.
Required fix: Downgrade this to a qualitative similarity statement and remove the quantitative “< 6%” claim unless you provide a derivation in the SPHEREx Fisher metric or a dedicated Monte Carlo showing the additional variance term under the actual 3D bispectrum covariance.

P2-M12 (MAJOR)
Location: Sec. IV (p. 10) and “Shot-noise caveat” sub‑section
Issue: Unsupported performance claim for anomaly‑selected tracers. You state a “preliminary Fisher forecast” suggests a ∼10–20% improvement, but no setup, inputs, or results are shown.
Required fix: Either provide a short appendix with the number densities, redshift distributions, bias parameters, and the Fisher setup that yields the 10–20% figure (even as an upper bound), or remove that claim.

P2-E8 (ESSENTIAL)
Location: Appendix A.2, Table III caption row “Corrected (10% residual; = Ideal, verification only)”
Issue: Ambiguous labeling vs. content. The row title reads “10% residual; = Ideal,” but only footnote text explains that the printed value is exactly equal to “Ideal” by construction (strict zero‑residual limit), while an actual 10% residual of σGR = 0.5 would give a tiny but nonzero change. As labeled, it is confusing and internally contradictory.
Required fix: Rename the row to “Corrected (residual neglected; equals Ideal by construction)” and, if you wish to keep a 10% example, add a separate numeric line (e.g., “Corrected (10% of σGR = 0.5 residual): σeff = 0.702, BF = …”) or remove the row.

P2-M13 (MAJOR)
Location: Data and Code Availability (pp. 22–23); Sec. III B and Sec. III A
Issue: Reproducibility omissions beyond DOI. The ℓ‑space Fisher overlap and the SDB kernel usage require explicit survey/noise inputs to be reproducible (e.g., the exact Planck‑like noise parameters used in the CMB Fisher overlap; transfer‑function and growth‑factor conventions; k‑range and binning for the SDB plots).
Required fix: In Data and Code Availability (or a reproducibility appendix), list: (i) the Planck noise model numbers used in the ℓ‑space Fisher overlap; (ii) the k‑ranges, bin widths, and fiducial cosmology parameters used in Eqs. (3)–(4) for all SDB‑based plots; (iii) the triangle grids used for r and rcos calculations. Ensure these match the archived code defaults.

P2-m6 (MINOR)
Location: Sec. IV (abstract and body), Sec. VII intro lines
Issue: Wording “combined additively in quadrature” is internally contradictory (addition in quadrature is not additive in the ordinary sense).
Required fix: Replace with “added in quadrature” or “combined heuristically in quadrature.”

P2-m7 (MINOR)
Location: Sec. III B (p. 8): “Squeezed-limit cutoff is completely insensitive … changes r by < 0.0002.”
Issue: Over‑precise claim without reproducible specification (grid size, seed, numerical tolerances). This could be a numerical artifact given finite sampling.
Required fix: Add the grid resolution and numerical tolerance used for this test, and qualify the statement (e.g., “at our default triangle grid resolution, the change is < 2×10−4”). Otherwise, soften to “negligible.”

P2-m8 (MINOR)
Location: Sec. II A (p. 3), novelty claim
Issue: “No prior quantification of this overlap exists (2009–2024)” is a novelty assertion without a supporting survey comparison.
Required fix: Either add a literature scan citation (or short footnote listing searched works) or soften to “we are not aware of a prior quantification of this specific overlap.”

P2-m9 (MINOR)
Location: Appendix A (p. 23): BΦ/Bζ mapping prose
Issue: The mapping is correct, but the derivation uses both Φ and ζ normalizations in one sentence. Readers may appreciate an explicit line: PΦ = (3/5)^2 Pζ ⇒ PΦ^2 = (3/5)^4 Pζ^2; (5/3)^3 × (3/5)^4 × 2 = 6/5.
Required fix: Add one explicit algebraic line (as above) or a citation to Komatsu-Spergel normalization for clarity.

P2-m10 (MINOR)
Location: Sec. V (p. 10)
Issue: The phrase “under the same GR marginalization and bϕ uncertainty budget applied to SPHEREx above” is easy to read as numerically reusing SPHEREx’s σGR and bϕ priors for MegaMapper, despite the earlier caveat that MegaMapper is more sensitive to both.
Required fix: Add a parenthetical “(for illustration only; not calibrated to MegaMapper’s higher‑z sensitivities)” or provide distinct priors.

P2-m11 (MINOR)
Location: Sec. III B (p. 8), ℓ-space Fisher overlap
Issue: “Stable across ℓref = 50–950” — ℓref is not defined. Readers cannot tell what this pivot/limit means.
Required fix: Define ℓref (e.g., a pivot multipole used to set a weighting scale) or remove the parenthetical if not essential.

P2-m12 (MINOR)
Location: Table III “BF vs. SSFSR”
Issue: Mix of exact values and orders of magnitude (“> 10^2” vs “3.5 × 10^8”) within the same column can be confusing.
Required fix: Adopt a consistent significant-figure policy (e.g., scientific notation with two significant figures everywhere), and if using inequalities, explain why exact numbers are not shown.

P2-m13 (MINOR)
Location: Sec. III A (p. 7), Eq. (3)–(4)
Issue: Although a convention citation is requested in P2-m1 of the first report, an additional clarity sentence would help: confirm units/c = 1 and that M(k,z) is dimensionless in the ζ-normalization used.
Required fix: Add “We adopt c = 1 units; M(k, z) is dimensionless in our ζ normalization (Dalal et al. 2008; Desjacques et al. 2018).”

P2-m14 (MINOR)
Location: Throughout
Issue: Occasional inconsistent capitalization and symbols (e.g., “GR‑marginalization,” “perms,” “γ¯5γa,” “rt” vs “r,” etc.) beyond those already flagged.
Required fix: Global copyedit for notation and typography consistency.

Explanation
These items are new relative to the first report. They focus on: (1) a fundamental operator‑level inconsistency between L and H in the in‑in identity statements; (2) an over‑strong “irreducibility” claim for the template mismatch; (3) basis‑dependent diagnostics being propagated as systematic error bars; (4) inconsistent treatment of GR systematics between SPHEREx and MegaMapper; (5) a few unsupported or over‑precise performance and novelty claims; and (6) clarity/reproducibility gaps not previously called out. Addressing these will materially improve rigor and clarity to PRD standards.