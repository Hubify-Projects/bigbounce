# P2 INT-M2 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/research/focused_paper_source_integration/02_full_draft.pdf` md5=79edd4cc pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7158 chars)
**Wall time**: 280.7s

---

Referee report on “Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook” (29 pp)

Scope of review
I audited the paper for methodological rigor, numerical and algebraic consistency, estimator specification, error propagation, dimensional consistency, and internal coherence between abstract/conclusions and body. I recomputed all headline ratios and significances from the numbers given, and checked that sigma numbers from incomparable null procedures are not conflated.

Overall assessment
The paper presents a sensitivity recast (not an independent forecast) for testing the matter-bounce prediction fNL = −35/8 with SPHEREx and (illustratively) MegaMapper. The work carefully distinguishes gauge-frame vs. CFC-theory statements, quantifies a template-mismatch factor r, propagates a systematic budget, and provides a closed-form Bayes-factor comparison. Many caveats are clearly labeled. Arithmetic and order-of-magnitude checks are, in most cases, correct.

That said, several essential items require revision to reach PRD standards. The most important are: (i) missing persistent archival DOI in the Data/Code section; (ii) incomplete, non-self-contained specification of the “SPHEREx-like” and other weighting kernels used to compute r (readers should not be required to infer definitions from external code); (iii) an indexing inconsistency for the squeezed-limit labels; and (iv) a few places where language and bookkeeping should be tightened to prevent misinterpretation.

Findings

ESSENTIAL

P2-E1
- Location: Data and Code Availability (page 25)
- Issue: “archived at Zenodo (DOI inserted at submission)” – missing persistent DOI. PRD requires a citable, immutable archival record matching the version used in the paper.
- Required fix: Provide the final Zenodo (or equivalent) DOI and/or Git commit hash for the exact code/data release used to generate all results. Freeze a versioned archive and cite it in the manuscript. Remove “inserted at submission”.

P2-E2
- Location: Sec. III.B, pages 8–9 (Template Projection and Amplitude Recovery)
- Issue: Inconsistent squeezed-limit indexing. Earlier (Sec. II.A, page 3) the squeezed long mode is k1 (“k ≡ k2 ≈ k3, k1/k → 0”). Later you define x3 ≡ k3/k1 with “x3 → 0 for squeezed limit k3 ≪ k1 ≈ k2,” which makes k3 the long mode. This is a notational contradiction.
- Required fix: Choose a single long-mode label consistently throughout (either k1 or k3) and correct all sentences, symbols, and cutoff definitions (xmin) accordingly. Explicitly state which index is the long mode in all places where squeezed configurations are referenced, including figure captions and weighting scans.

P2-E3
- Location: Sec. III.B, pages 8–9; Table IV caption (page 20); Fig. 2 caption (page 11)
- Issue: The computation of the amplitude-recovery factor r relies on “SPHEREx-like”/“LSS noise-weighted” weighting and “five region-masked variants,” but these weight functions are not defined in the text. The reader must not be forced to mine code to reproduce a load-bearing number (r = 0.84 ± 0.02).
- Required fix: Provide explicit analytic definitions of every weighting used to form r (including masks, k- or triangle-shape ranges, measure, and any survey window approximations). If they correspond to Fisher kernels, write them down (or give the exact discrete quadrature used). State the integration domain and binning (including any kmin/kmax or triangle-grid limits) for each weighting. Summarize the 10 weights in a small appendix or table with enough detail to reproduce r without running your repository. Keep the repository as a complement.

P2-E4
- Location: Abstract and throughout (e.g., pages 9, 10, 20)
- Issue: Multiple sigma values from different null procedures are juxtaposed (e.g., “naive uncorrected 6.25σ” next to template-corrected 5.2–5.5σ). In most places you do flag non-comparability, but at a few juxtapositions the caveat is absent or easy to miss (e.g., Abstract sentence listing “5.2–5.5σ … reducing to a realistic ∼2.6–5.5σ …” without restating the different null procedures in that specific sentence).
- Required fix: At every juxtaposition of sigma numbers from different null procedures, explicitly state “not directly comparable: different null procedure” in-line or in the immediate footnote. Ensure the Abstract and Conclusions contain these qualifiers wherever two different σ-lines appear together.

MAJOR

P2-M1
- Location: Sec. II.A, pages 3–4, footnote 1; Sec. II, Table I
- Issue: The degree-9 polynomial P is reconstructed in your symmetrized monomial basis with coefficient set (2, 7, 3, −12, −69, 19). While you do specify the six orbit-sum monomials and provide the coefficients, the explicit linear combination for P(k1,k2,k3) is not written in one place; readers must piece it from prose and a footnote.
- Required fix: Write the explicit closed-form expression for P(k1,k2,k3) in the main text or an appendix (one line with the six orbit sums and your six coefficients). This removes any ambiguity about permutation conventions and makes the shape fully reconstructible from the PDF alone.

P2-M2
- Location: Sec. III.B, page 8–9; Appendix A.2/Table V (page 28)
- Issue: The ℓ-space Fisher “consistency check” for r (CMB-like) and the bispectrum 3D LSS weighting are of different dimensionalities and noise structures. Though you say “limited commensurability,” the text could be read as validating LSS r with a 2D CMB estimator.
- Required fix: Add one clarifying sentence immediately after reporting the ℓ-space Fisher result that it is a separate 2D test not directly validating the 3D LSS r; it only serves as a sanity check that the overlap is large under a different metric. Point to the LSS-defined weights as the numbers used in SPHEREx significance.

P2-M3
- Location: Sec. IV, page 10 (Heinrich recast); Sec. VII/Table IV, page 20
- Issue: The “SPHEREx bispectrum σ(fNL) = 0.7” baseline is treated correctly as imported, but the paper’s length and repeated “headline” references can obscure that no new bispectrum-Fisher matrix is constructed in this work. PRD readers should have this plainly stated once at the start of Sec. IV and in Conclusions.
- Required fix: Add an explicit, one-line disclaimer at the start of Sec. IV and in Conclusions that every SPHEREx σ(fNL) number is a recast of Heinrich et al. (no independent bispectrum-Fisher recomputation), and that all “headline significances” are sensitivity envelopes, not forecasted measurement precisions.

P2-M4
- Location: Sec. VII.C/Table III (pages 18–19)
- Issue: The GR-projection “σGR” quadrature model is a heuristic stress test (you note this), yet Bayes factors and significance windows are computed from it. The connection to Addis et al. is qualitative only.
- Required fix: Place a short boxed note or footnote at Table III explicitly stating: “σGR is a heuristic additive-variance stress parameter, not derived from a survey Fisher matrix; the resulting BF and σeff are for scoping only.” Include one quantitative sentence bounding how sensitive BF vs. tuned is to σGR over [0,1] (you do for P(BF>3); mirror that in the prose).

P2-M5
- Location: Sec. III.B, page 8–9
- Issue: The statement “squeezed-limit cutoff x3,min from 0.001 to 0.200 changes r by < 0.0002” depends on the definition of the squeezed ratio and on the sampling measure. With the indexing inconsistency (P2-E2), this could confuse readers.
- Required fix: After fixing the index convention, restate this result with the correct ratio definition and explicitly name the triangle-shape measure and grid (uniform in log k, 50/100/200 bins) used to establish the < 2×10−4 variation.

P2-M6
- Location: Sec. VII.E/Table IV (page 20)
- Issue: The “All combined” rows stack bϕ-widened σ with σGR in quadrature. While clearly labeled as heuristic, readers could conflate these with a marginalized joint Fisher. You do warn earlier, but the table is standalone.
- Required fix: Add a boldface sentence in the Table IV caption: “All σeff combinations are additive-in-quadrature scoping budgets, not results of a joint multi-parameter Fisher marginalization.”

MINOR

P2-m1
- Location: Sec. II.A, Eq. (2), page 3
- Issue: BNL definition could benefit from a single explicit normalization sentence (“dimensionless by construction: degree-9/degree-6/degree-3” is given but terse).
- Required fix: Add one clarifying phrase: “so BNL is homogeneous of degree zero in k.”

P2-m2
- Location: Sec. II.C, pages 6–7
- Issue: κϵ range [5.6, 80] is described as a “schematic bound.” Good, but provide a 1–2-line numeric illustration (e.g., translate to ΔfNL ≈ 0.03–0.36 at Planck ns).
- Required fix: Add that translation (you partly do later; bring it up front here).

P2-m3
- Location: Sec. VIII.A, page 20
- Issue: Recast of Planck PR4 to bounce template uses r = 0.876; confirm in-line that this is the CMB-Fisher-only r (signal-dominated) to avoid ambiguity with r = 0.84 (LSS).
- Required fix: Insert “(CMB-Fisher overlap r = 0.876)” in that sentence.

P2-m4
- Location: Sec. VI.C, pages 12–15; Table II caption (page 16)
- Issue: The distinction between r → 1 bookkeeping and noise-weighted rebooking is correct but could be made more prominent in the table’s header.
- Required fix: Add a column header note “All entries r → 1; rebooked r = 0.84 values in parentheses.”

P2-m5
- Location: Figures 2, 4, 5 (pages 11, 17–18)
- Issue: Axes/legends appear correct in text, but add units where applicable (e.g., kmin [h/Mpc]).
- Required fix: Ensure units are printed on every axis that admits them.

NITS

P2-n1
- Location: Throughout
- Issue: Heavy use of internal meta terms (“headline,” “bookkeeping”). Not wrong, but non-standard academic tone.
- Required fix: Consider reducing frequency or move some of this wording to parentheses.

P2-n2
- Location: Appendix A, page 25
- Issue: “the Komatsu-Spergel constant c” – stylistically, cite Komatsu & Spergel (2001/2005) once to anchor the term.
- Required fix: Add citation in the first mention.

P2-n3
- Location: Typos/formatting
- Issue: Sporadic hyphenation artifacts (e.g., “con￾tains”) due to PDF linebreaks.
- Required fix: Clean during proofing.

Arithmetic and consistency checks (selected)
- Slow-roll fNL ≈ (5/12)(1 − ns) with ns = 0.9649: 0.0146 ≈ 0.015 (correct).
- Bounce-to-inflation contrast: 4.375/0.015 ≈ 292 (quoted ≈ 290; fine).
- Naive SPHEREx significance: 4.375/0.7 = 6.25 (correct).
- Template-corrected: r = 0.84 → 4.375×0.84/0.7 ≈ 5.25 (in 5.2–5.5 band; correct); r = 0.876 → 5.48 (~5.5; correct).
- GR-only σeff (σGR = 1): sqrt(0.7^2+1^2) = 1.221 → 3.675/1.221 ≈ 3.01σ (quoted ~3.0; correct).
- All-combined example: sqrt(0.9^2+1.0^2) = 1.345 → 3.675/1.345 ≈ 2.73σ (quoted ~2.7; correct).
- 16th-percentile r = 0.70 → 4.375×0.70/0.7 = 4.375σ (~4.4σ; correct).
- Bayes factor delta, broad prior: 30/(√(2π)×0.7) = 17.1 (correct).
- Delta, narrow prior exact: ~7.0 (approximation + CDF-tail correction as described; consistent).
- Table V single-ordering stress test: 2.1875×0.84/0.7 = 2.63σ (correct).

Stand-alone reader test
- The SPHEREx-like/LSS weighting definitions for r and the masked variants are not self-contained (ESSENTIAL/MAJOR items above).
- Otherwise, the paper largely passes the stand-alone test: equations are dimensioned; priors and likelihoods are defined; Bayes-factor integrations are explicit; and the template polynomial structure with coefficients is mostly reconstructible (once P2-M1 is implemented).

Length
- At 29 pages for a sensitivity recast with extensive caveats, the paper is on the long side for the net new content. Consider shortening by ~4–6 pages by moving some repetition (e.g., repeated “headline range” explanations) and secondary stress-test prose to an appendix. This is a recommendation, not a condition.

## Summary recommendation
MAJOR REVISIONS

The numerical and methodological core is solid, careful, and mostly well qualified. However, PRD requires a self-contained specification of the weighting kernels used to produce the load-bearing r = 0.84 ± 0.02 number; the current manuscript defers too much to the repository. Additionally, the squeezed-limit index inconsistency must be corrected, and the archival DOI must be provided. With these changes (and the minor clarifications requested), the paper would meet PRD’s methodological standards for a sensitivity recast.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (FRESH-EYES PASS)

ESSENTIAL

P2-E5
- Location: Sec. VIII.A (Planck PR4 recast), page 20
- Issue: Tiny but real stale-number inconsistency in the “distance from bounce” line. You first rescale the Planck PR4 constraint by the CMB-Fisher r = 0.876, which moves the central value from −0.10 to −0.11, but then compute the tension as |−4.375 + 0.1|/5.71 = 0.75σ (uses 0.10, not 0.11).
- Required fix: Use the consistently rebooked central value −0.11 in the numerator: |−4.375 + 0.11|/5.71 = 0.745σ. State the rounded result (0.75σ) after the consistent substitution to avoid “two centrals” in one paragraph.

MAJOR

P2-M7
- Location: Sec. II.A, “triangle grid” paragraph (page 4)
- Issue: Triangle-count scaling across grid resolutions looks internally inconsistent and is not algorithmically specified. You quote ≈23,098 triangles for 50 bins/side, ≈190,000 at 100 bins (≈8.2×), and ≈1.5M at 200 bins (≈65×). For a fixed-shape-ratio grid with ordering (k1 ≤ k2 ≤ k3), counts normally scale ~N^2 (not ~N^3), so 50→100→200 would naively give ~4× and ~16×, not ~8× and ~65×. Without the exact de-duplication, ordering, and triangle-inequality handling, readers cannot validate rcos convergence via counts alone.
- Required fix: Add a one-paragraph algorithmic specification (ordering, how degeneracies are removed, exact index loops, any bin-edge exclusions). Optionally tabulate counts for a few N with the algorithm fixed. If the higher-than-N^2 scaling is expected (e.g., because you keep near-degenerate cells), state why.

P2-M8
- Location: Sec. III.A–B, Eqs. (3)–(4) and surrounding text (pages 7–9)
- Issue: Dimensional conventions for M(k, z) are not explicit. You say “wavenumbers k are quoted in h Mpc−1 throughout,” but H0 in Eq. (4) is not unit-cast to the same system (H0 is usually km s−1 Mpc−1). Without stating c = 1 and the implied conversion of H0 to h Mpc−1, M(k, z) is not manifestly dimensionless, and Δb(k, z) in Eq. (3) would carry residual units.
- Required fix: Add an explicit units sentence: “We work with c = 1 and express H0 in h Mpc−1 so that M(k, z) is dimensionless for k in h Mpc−1,” or give the exact numerical prefactor used if you work in mixed SI/astrophysical units. This also clarifies the intended normalization for reproducing SDB plots.

P2-M9
- Location: Figs. 4 and 5 captions; corresponding body text in Sec. VII (pages 17–18)
- Issue: Curves depend on specific parameter choices (e.g., r value for the horizontal “SPHEREx bispectrum” line; assumed bϕ priors; survey fsky; redshift-bin set). The captions do not state which r (0.84 vs 0.876) and which σ(fNL) baseline (0.7 vs widened) are used. The body text provides some of this context but not all in one place.
- Required fix: Add in-caption qualifiers, for example: “SPHEREx bispectrum (σ = 0.7; r = 0.84)” in Fig. 4 right and “SPHEREx bispectrum (5.2σ line uses r = 0.84, σ = 0.7)” in Fig. 5 right. This prevents readers from inferring CMB-Fisher r = 0.876 or a widened σ by mistake.

P2-M10
- Location: Sec. VII.D, “Photometric redshift outliers” paragraph (page 18)
- Issue: Mixed quantitative story: you compute a dilution ≈ fcat^2/(1 + fcat)^2 ≈ 0.008 (0.8%) and then assert an overall ≈5% σ degradation “from smearing.” The 5% figure is not tied to a calculation or citation and may be misread as derived from the 0.8% term.
- Required fix: Separate the two channels explicitly and quantify/cite the “smearing” contribution (or show a quick back-of-envelope scaling to 5%). If 5% is an adopted bound from ref. [26], state it as such and remove any impression it follows from the 0.8% dilution.

MINOR

P2-m6
- Location: Sec. III.B, Eq. (1) and surrounding sentence (page 3)
- Issue: Slight ambiguity in typography: “3/(256 k1^2 k2^2 k3^2)” could be read as 3/256 · (k1 k2 k3)−2 or as 3/(256 k1^2) · k2^2 k3^2. The text clarifies later, but the equation as written can be parsed ambiguously.
- Required fix: Add parentheses around the k-product in the denominator, e.g., AT = 3/[256 (k1 k2 k3)^2] P(…).

P2-m7
- Location: Sec. VII.B–D, general (pages 17–19)
- Issue: Several hedged phrases (“O(10–30%)”, “highly robust”, “dominant effect”) appear without a single compact quantitative summary right where they are introduced, even though supporting numbers are later given. This invites cherry-picking of the optimistic end.
- Required fix: Where you first introduce each hedge, add one parenthetical numerical anchor, e.g., “we adopt 5% as a working bound for photo-z in the bispectrum channel (Sec. VII.D),” with the forward reference.

P2-m8
- Location: Appendix A.2/Table V (page 28)
- Issue: The header says “σ(fNL) = 0.7” and r = 0.84 is used in the body of the table, but the caption does not explicitly say that r = 0.84 is assumed for both rows.
- Required fix: Add “both rows use r = 0.84 and σ(fNL) = 0.7” in the first sentence of the caption.

P2-m9
- Location: Sec. III.B, “squeezed-limit cutoff” sentence (page 9)
- Issue: After you fix the long-mode index (P2-E2 in your first report), this one-liner should restate the exact squeeze ratio definition and the grid measure used for the < 2×10−4 variation result, otherwise readers cannot verify it without digging into code.
- Required fix: Append “using xlong ≡ klong/khard with uniform log-binning in (k1, k2, k3) and the 50/100/200-bin triangle grids defined above” to that sentence.

P2-m10
- Location: Table/figure rounding throughout
- Issue: Occasional mixed rounding (e.g., 0.860/0.700 = 1.23 but sometimes shown as 1.20–1.21 elsewhere; 7.35→7.4 vs 7.48→7.5). Not wrong, but can look inconsistent to a careful reader trying to back-calculate inputs from labels.
- Required fix: Add a one-line rounding policy early (e.g., “two significant digits for intermediate factors; one decimal for σ”) and apply it to figure legends where space allows.

NITS

P2-n4
- Location: Sec. II.D (page 7)
- Issue: You introduce rt for tensor-to-scalar ratio to avoid clash with the overlap r. Good, but later uses of “r” (template overlap) are frequent and come near “rt” once or twice; a stray “r” near “tensor” could be misread.
- Required fix: Add “we always denote tensor-to-scalar as rt and the template-overlap factor as rovl in figure labels” or similar; consider using a distinct symbol in figures/axes.

P2-n5
- Location: Sec. VI.C (pages 12–15)
- Issue: The careful Eq. (9)/(10) discussion is long; two times you restate that Eq. (10) applies to the delta-prior broad-competitor corner only. It’s correct but repetitive.
- Suggested tweak: Move the “applicability map” into a short displayed box or footnote to tighten the main flow.

WHY THESE WERE MISSED BEFORE
- They are small but real consistency or reproducibility frictions (units in M(k,z); triangle-grid scaling; caption parameterization) that do not change any headline arithmetic but can obstruct faithful reproduction from the PDF alone or allow misreadings.
- The stale 0.10 vs 0.11 Planck central in the same paragraph, and the 0.8% vs 5% juxtaposition in photo-z, are easy to overlook on a first pass because the resulting numbers barely move — but PRD will expect these to be internally tidy.

End of new findings.