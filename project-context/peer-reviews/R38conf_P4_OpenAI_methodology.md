# P4 R38conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v183.pdf` md5=34b06870 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7309 chars)
**Wall time**: 557.0s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A Null Real-Space Chirality Dipole, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review
- Focus: statistical-method validity, estimator declaration, null procedures, internal arithmetic consistency, effect sizes, look-elsewhere handling, reproducibility surfaces (versions, commits, releases), and consistency of abstract and conclusions with the body.
- I audited every scalar and table entry I could recompute from the text. Where exact recomputation is not possible (e.g., MC-derived curves), I checked logical coherence and consistency across sections.

Overall assessment
The paper presents a very large chirality-labeled catalog (8.47M galaxies; 3.20M spirals), a carefully bias-hardened analysis pipeline, and a null real-space dipole result with extensive systematics diagnostics. The methodological care is well above average for this topic and many usual pitfalls are explicitly addressed. However, there are several essential issues that must be fixed before PRD publication, chiefly around reproducibility/versioning, the presentation of two discordant canonical ℓ=1 MASTER significances for the same field, and a few unsubstantiated numerical claims that need derivations. I also flag numerous instances of internal version-history prose that PRD will not accept as-is. Finally, the data/code release needs a stable DOI or an exact frozen release that matches the paper’s version.

Findings

ESSENTIAL

P4-E1 (Data availability/version mismatch)
- Location: Data Availability (page 22), Title header (page 1), footers throughout
- Problem: The paper header states “v1.0.183 (Dated: June 13, 2026)”, but the Data Availability section pins “commit 53b41d12 (v1.0.180, June 2026).” This is a direct mismatch between the paper’s stated version and the frozen repository state, undermining reproducibility.
- Required fix: Update the Data Availability to pin the exact commit hash that corresponds to v1.0.183 (the version in the PDF header) and ensure all referenced artifacts (scripts, outputs, null arrays) exist at that commit. Provide a stable archival identifier (Zenodo DOI or equivalent) for the catalog and code corresponding to v1.0.183.

P4-E2 (Canonical MASTER ℓ=1 significance inconsistency)
- Location: Sec. IV D (pp. 9–11), Table III (p. 11), Sec. VII c (p. 15)
- Problem: Two different canonical-mask, unapodized MASTER ℓ=1 significances are quoted for the same dataset: +3.64σ (500-MC direct run; one-sided pMC=0.030) and +7.93σ (10^4-permutation recompute; Table III). The text attributes this to “different null-run sizes and mask/weight conventions,” but both are described as canonical unapodized, and a factor-of-two jump in z cannot be due to MC sample size alone. This confuses the reader about the magnitude of the canonical residual.
- Required fix: Choose and present a single, definitive canonical MASTER ℓ=1 pipeline (field definition, monopole subtraction convention, mask/weight, and decoupling method) with one null specification and one quoted significance, and relegate all legacy variants to Supplementary Material. Explicitly reconcile why +3.64σ and +7.93σ differ so strongly, with a side-by-side table of the exact estimator inputs (field normalization, mean subtraction recipe, binning/decoupling) and null construction. If the estimator was changed, state so clearly and drop the superseded value from the main text.

P4-E3 (Archival release/DOI)
- Location: Data Availability (p. 22)
- Problem: “A persistent archival DOI has not yet been minted; until it is, the versioned release tag above is the citable artifact.” PRD requires a stable archival record for data/code underpinning the main claims.
- Required fix: Mint and include a DOI (Zenodo or similar) for the exact code and catalog release matching the paper’s version and commit. Verify that all artifact paths cited in the paper are present at that release.

P4-E4 (Unsubstantiated “65.7% edge-on labeled CW/CCW” statistic)
- Location: Appendix E a (p. 21)
- Problem: The statement “65.7% of b/a<0.3 objects receive CW/CCW labels” is a precise figure with no derivation, sample size, or artifact pointer. Given its interpretive impact on effective sensitivity, it must be supported.
- Required fix: Provide the derivation: sample definition, cross-match procedure, counts, and uncertainty. Add a pointer to a committed artifact (table or script output). If unavailable, either remove the precise percentage or clearly label it as an illustrative estimate without use in any quantitative conclusion.

P4-E5 (Residual internal version-history/log prose in the body)
- Locations (non-exhaustive):
  - Sec. IV C footnote 1 (p. 7): “An earlier run reported 0.43σ … after repair and regeneration…”
  - Fig. 8 caption (p. 10): “an earlier rendering of this figure…”
  - Appendix D g footnote (p. 20): “post-R29…”
  - Multiple places: “superseded by …,” “earlier version… overstated,” etc.
- Problem: PRD articles must present a clean, final narrative. Internal revision history and audit logs are not suitable in the main text and confuse the reader.
- Required fix: Remove all version-history/edit-log language from the main text and figures. If necessary, move such notes to a brief “Version history” paragraph in Supplemental Material and keep the main text focused on the final pipeline and results.

MAJOR

P4-M1 (Terminology “isotropic-bootstrap null”)
- Location: Sec. IV C (pp. 7–8), Table I (p. 5)
- Problem: The “isotropic-bootstrap null” is implemented as a per-pixel permutation of Ap across in-mask pixels. This is a valid empirical null, but it is not “isotropic” in the sense of drawing realizations from an isotropic random field on a cut sky; it preserves the in-mask 1-point distribution and mask geometry exactly. The label “isotropic” risks overclaiming.
- Required fix: Rename consistently to “pixel-permutation null” throughout (or define “isotropic-bootstrap” precisely once and use that term consistently) and add one sentence clarifying its properties and limitations (preserves the one-point distribution and mask geometry; breaks spatial coherence).

P4-M2 (Primary-estimator pre-declaration claim needs tightening)
- Location: Sec. III B (pp. 3–4)
- Problem: The paper states the primary estimator hierarchy “was declared in early versions … and predates the provenance audit,” but this is equivalent to an internal log entry and does not demonstrate a pre-registered analysis plan.
- Required fix: Remove the claim of pre-declaration or restate neutrally: “We designate the real-space dipole as the primary estimator and treat the harmonic channel as a diagnostic.” Do not imply time-stamped pre-registration unless a dated, accessible record exists (link to it if so).

P4-M3 (Abstract-to-body cross-check: harmonic-channel residual presentation)
- Location: Abstract (pp. 1–2), Sec. IV C–D, Table III
- Problem: The abstract lists +3.64σ (canonical unapodized) and +7.28σ (apodized footprint) residuals. Given the inconsistency identified in P4-E2, the abstract should reflect the final, unified canonical number and avoid implying the two values are commensurate. It also uses “≈1.9σ Gaussian-equivalent” without explicitly stating that this refers to the +3.64σ with p=0.03, not the +7.93σ canonical recompute.
- Required fix: After resolving P4-E2, revise the abstract to include only the final canonical value and its null convention. Keep the caution that it is a systematics diagnostic, not a cosmological detection.

P4-M4 (Overuse of path-like artifact references in main text)
- Location: throughout (e.g., pp. 3, 5–9, 14–22)
- Problem: The prose is littered with repository path strings and JSON artifact filenames. While commendable for reproducibility, this level of inline detail renders the article difficult to read.
- Required fix: Move artifact-path specifics to a Reproducibility Appendix or a separate README in the archived repository. In the main text, retain only short identifiers (e.g., “Artifact A1”) and a concise mapping table in an appendix.

P4-M5 (Harmonic-channel completeness reporting)
- Location: Sec. VII a (p. 14), Fig. 9, Table VI
- Problem: The completeness curve uses a specific null (“MASTER ℓ=1 label-shuffle null”) and the axis-averaged P(≥3σ) at Ap values. While this is stated, the “≥0.999 at 0.75%” could be misread as a general pipeline completeness unless the null and estimator dependence are reiterated prominently.
- Required fix: Add one explicit sentence near Fig. 9/Table VI: “This completeness applies only to the MASTER ℓ=1 diagnostic channel under the label-shuffle null and cannot be used to set real-space falsification thresholds.”

P4-M6 (Effect-size clarity for headline ℓ=1 residuals)
- Location: Sec. IV C–D (pp. 8–11), Table III
- Problem: You report σ values and Cℓ amplitudes in different normalizations across footprints/fields. Although many caveats are provided, readers would benefit from a compact effect-size comparison in a single normalization (e.g., Ap units) across footprints for the ℓ=1 mode.
- Required fix: Add a small table or paragraph that reports the ℓ=1 effect-size in a single normalization (e.g., the square root of C1 in Ap units, or an equivalent fractional amplitude) for each footprint/weight choice, alongside the null convention used, to anchor the interpretation of the σ values.

P4-M7 (Edge-on contamination: impact on sensitivity)
- Location: Appendix E a–b (p. 21)
- Problem: The ~5–8% sensitivity penalty derivation assumes a particular dilution of Neff but does not show the counts or the exact mapping from inclination proxy to sample fraction for the HC cuts.
- Required fix: Provide the counts and effective sample-size estimates used to derive the 5–8% penalty, or explicitly mark it as an approximate scaling argument not used in any quantitative conclusion.

MINOR

P4-m1 (Arithmetic and internal consistency checks passed but should be stated compactly)
- Locations:
  - Table II (p. 5): binomial σ for fCW matches recomputation; dev values consistent.
  - Fisher floor (Sec. VI A, p. 12): σ(A) ≈ 9.7e−4 at N=3.2M; 3σ≈0.29% recomputes; for N=949,584, 3σ≈0.53% recomputes.
  - Table IX (p. 18): three-class accuracy 58.7% and class-wise precision/recall consistent with the matrix.
- Recommendation: No change required; consider a short “Sanity checks” paragraph collating these cross-checks so a reader does not have to hunt for them.

P4-m2 (Terminology consistency: Ap vs fCW)
- Location: multiple figures and captions (e.g., Figs. 4, 7; pp. 8–10)
- Problem: Units alternate between Ap and fCW with conversions explained in text. This is correct but can be missed.
- Fix: Add a one-line reminder in each figure caption that uses fCW instead of Ap: “Ap = 2(fCW − 0.5).”

P4-m3 (Axis labeling and notation for NaMaster apodization)
- Location: Appendix A (p. 15), Table VII (p. 16)
- Problem: “C 2 2◦ apodization” spacing/notation is irregular.
- Fix: Standardize to “C2 apodization with 2° apodization length.”

P4-m4 (Library versions)
- Location: Acknowledgments/Software (p. 22)
- Problem: “pymaster 2.6” is stated; consider pinning exact versions for healpy, numpy, pytorch, timm, and providing a requirements file in the repository.
- Fix: Add a requirements.txt (or environment.yml) at the archived commit and refer to it.

P4-m5 (HuggingFace dataset path formatting)
- Location: Data Availability (p. 22)
- Problem: The dataset path in text shows line-break artifacts: “galaxy- chirality- catalog”.
- Fix: Provide the exact URL without line-break artifacts.

P4-m6 (Look-elsewhere description)
- Location: Appendix C c (p. 18)
- Problem: Good to have both direct-MC max-statistic and BH/Bonferroni; please add the note that BH assumptions are not strictly met due to strong correlations (you already hint at this) and emphasize that the direct-MC max-statistic is the authoritative LEE control.

NITS

P4-N1 (Minor typos/hyphenation)
- Locations: scattered hyphenation artifacts due to line breaks (“cata­log”, “apod­ized”, etc.).
- Fix: Clean typographical artifacts in the final typeset version.

P4-N2 (Repeated qualifiers)
- Location: e.g., “systematics-attributed diagnostics” appears very frequently.
- Fix: Consider slight condensation to improve readability while keeping the key caveats.

P4-N3 (Footnote style)
- Location: Footnotes 3–5 (pp. 20–21)
- Fix: Convert multi-sentence footnotes with methodological content into main-text parentheticals or appendices for clarity.

Abstract-last drift sweep (pattern-045)
- I verified each abstract claim against the body. All major numbers (8.4745M/3.20116M counts; +0.41σ with p=0.31; 99.32% pre-MASTER leakage reproduction; +3.64σ canonical/+7.28σ apodized; A50≈0.75%, A95∈(1.0%,1.5%]) are traceable. After fixing P4-E2, update the abstract’s harmonic-residual sentence to reflect the final canonical value and null convention. All caveats about non-interchangeability of σ across channels are present in the body; consider mirroring one short “not directly comparable” caveat in the abstract sentence that lists both harmonic σ values.

Provenance surfaces (patterns 046/047)
- The paper provides unusually rich artifact pointers, but the version/commit mismatch (P4-E1) must be fixed. Also, move path-level details to a reproducibility appendix to meet PRD style.

Uncomputed quantitative claims (pattern-048)
- “65.7% of b/a<0.3” (P4-E4) requires support or softening.
- “~5–8% sensitivity penalty” (P4-M7) needs a compact derivation or a clear “approximate” label.

Standalone-reader test
- The article is self-contained; no reliance on a companion paper. Good.

Effect sizes
- Generally well reported (dipole amplitude in Ap units; fCW deviations; Cℓ amplitudes). Add the requested unified ℓ=1 effect-size snapshot (P4-M6).

Length
- At 23 pages including extensive appendices, this is long for a null result. Given the community relevance and the catalog resource, it is acceptable, but many artifact-path sentences can be moved to an online supplement to tighten the main text by ~2–3 pages without losing scientific content.

## Summary recommendation
MAJOR REVISIONS

The science appears careful and the main conclusions (null real-space dipole; monopole–mask leakage dominates pre-MASTER ℓ=1; remaining harmonic residuals are systematics-dominated) are supported by the analyses. However, the paper must fix the reproducibility/versioning mismatch, present a single, consistent canonical MASTER ℓ=1 result (and demote conflicting legacy numbers), provide a derivation or soften the precise edge-on statistic, and streamline internal version-history prose. With these addressed, along with minor presentation improvements and an archival DOI, the work would meet PRD’s methodological and reproducibility standards.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eyes pass)

ESSENTIAL

P4-E6 (Observed harmonic z mismatch between figure and text)
- Location: Sec. VII a, Fig. 9 (caption/annotation) vs. Sec. IV C b and Table VI
- Problem: The figure annotation shows “obs. z = 7.21” for the apodized MASTER ℓ=1 channel, while the body quotes +7.28σ (Sec. IV C b; Table VI) and +7.31σ (Table III, 10^4-permutation recompute). This is a stale-number inconsistency for the same channel.
- Required fix: Harmonize the observed z across Fig. 9, Sec. IV C b, and Table VI. State the null convention and MC size once and use a single number (preferably the highest-statistics value).

P4-E7 (Broken cross-reference to Appendix table)
- Location: Table I footnote a and Sec. IV B (both refer to “Appendix A Table VI”)
- Problem: The mask/sky-fraction consolidation table in Appendix A is labeled Table VII (not VI). The cited “Table VI” in Appendix A is actually the harmonic completeness table in Sec. VII.
- Required fix: Correct all “Appendix A Table VI” references to “Appendix A Table VII” (or the appropriate label after renumbering). Audit other appendix/table refs for similar drift.

MAJOR

P4-M12 (Arithmetic: Table II “Catalog B (calibrated)” deviation inconsistent with rounded fraction)
- Location: Table II
- Problem: The row reports fCW = 0.504 ± 0.0003 with “Dev. +14.6σ.” Using the displayed numbers, (0.504 − 0.5)/0.0003 ≈ 13.3σ, not 14.6σ. The 14.6σ would require more trailing digits in the fraction (e.g., ~0.50438).
- Required fix: Either provide the unrounded fCW (enough digits to support 14.6σ) or update the Dev. value to match the displayed fCW and σ.

P4-M13 (Fisher-floor formula lacks an explicit estimator derivation)
- Location: Sec. VI A a (Eq. 4 and surrounding text)
- Problem: The paper asserts σ(A) = √(3/N) with a one-line Fisher argument but does not specify the actual dipole estimator and weighting for which this holds on a cut sky. Since this benchmark is used to contextualize the empirical floor, it needs a short, explicit derivation or a standard reference linking the estimator to the stated Fisher result.
- Required fix: Add a brief derivation (or cite a standard reference) showing the estimator and assumptions that lead to σ(A) = √(3/N) and clarify how cut-sky geometry enters (or is ignored) in that ideal limit.

P4-M14 (Injection-recovery axis sampling is not area-uniform in the primary table)
- Location: Sec. VI A b, Table V
- Problem: The primary injection-recovery sweep uses θ-uniform axis draws (non–area-uniform on the sphere). Although an area-uniform spot check and a full rerun are mentioned and appear consistent, the headline table (which underpins A50/A95 statements) still reflects the θ-uniform convention.
- Required fix: Standardize the primary completeness table to area-uniform axis draws (cosθ ∼ U[−1,1]) and keep the θ-uniform results as a cross-check, or state clearly in the table header that the reported P(σ > 3) is for θ-uniform draws and provide the area-uniform companion values side-by-side.

P4-M15 (Table I row (vi) statistic label ambiguous)
- Location: Table I, row (vi) “monopole+mask null”
- Problem: The “Reported statistic” cell lists “+1.69” without specifying this is a moment-z (or other) significance relative to the binomial-monopole generative null.
- Required fix: Explicitly label this as “+1.69σ (vs. monopole-only generative null)” to avoid confusion.

MINOR

P4-m7 (Figure/body unit drift in completeness panel)
- Location: Fig. 9 vs. Table VI and Sec. IV C b
- Problem: Beyond P4-E6’s z-value mismatch, the figure and text do not explicitly restate the null convention next to the observed z in the figure. A reader could mistake the plotted completeness (under the label-shuffle null) as directly tied to a different null used elsewhere.
- Fix: Add “Null: label-shuffle (MASTER ℓ=1)” in the Fig. 9 panel/legend next to “obs. z = …” to bind the observed point to the correct null.

P4-m8 (Effective-sky-fraction definition is non-standard without a reference)
- Location: Appendix A c, Table VII
- Problem: f_eff_sky is defined as ⟨W⟩^2/⟨W^2⟩. This is a valid descriptive choice but differs from alternative “effective f_sky” definitions sometimes used for pseudo-Cℓ variance (e.g., involving ⟨W^2⟩^2/⟨W^4⟩).
- Fix: Add a brief note that this f_eff_sky is for descriptive bookkeeping only (as you partly state) and cite a standard reference for other common choices to preempt confusion.

P4-m9 (Hemisphere max-statistic p-value description)
- Location: Appendix C c, Table I row (v)
- Problem: The main table lists pLEE ≤ 10−4 without immediately reminding that a subsequent BH/Bonferroni heuristic yields < 1σ. Although the caption discusses this, the row can still be misread in isolation.
- Fix: Append “(direct-MC max-statistic; BH/Bonferroni yields < 1σ)” to the row or add a superscript linking to this clarification.

P4-m10 (Hemisphere p-value one-sided vs. |A|)
- Location: Appendix C c
- Problem: The per-direction p-values are described as one-sided exceedances of |A|. That is effectively a two-sided test in A but could be confusing as written.
- Fix: Clarify that using |A| with a one-sided exceedance is equivalent to a two-sided test for signed A, and that the direct-MC max-statistic distribution already encodes the absolute-value choice.

P4-m11 (Leg-proxy cross-power reporting is incomplete)
- Location: Appendix D d
- Problem: Only two imaging-leg cross-correlation coefficients are reported (BASS+MzLS and DES). DECaLS is omitted explicitly, even if it is the baseline.
- Fix: Report rℓ=1 for DECaLS×Ap as well (or state explicitly that DECaLS is the reference and r is not quoted by construction).

P4-m12 (Terminology consistency for nulls)
- Location: scattered
- Problem: “pixel-permutation,” “per-pixel random-label permutation,” “label-shuffle,” and “isotropic-bootstrap null” appear in different places. P4-M1 already requests renaming “isotropic-bootstrap”; an additional clean-up is helpful.
- Fix: After adopting a canonical label for each null type, ensure the same term is used consistently in figure captions, tables, and text.

P4-m13 (Caption-level unit reminder)
- Location: Figs. that use fCW units (e.g., Figs. 4, 7)
- Problem: Some captions do include the conversion to Ap; others rely on text.
- Fix: Add “Ap = 2(fCW − 0.5)” as a one-line reminder in captions using fCW.

NITS

P4-N4 (Typographical/notation polish)
- Locations: Fig./text instances of “C 2 2◦” and “axis x, ˆ y, ˆ zˆ”
- Fix: Standardize to “C2 apodization with 2° length” and clean stray diacritics in axis labels.

P4-N5 (Table/figure self-containment)
- Locations: Tables I, III, VI; Fig. 9
- Fix: Where space allows, repeat the null type and MC size in the table/figure headers so they can be read standalone without hunting in the text.

Explanation
I focused on fresh classes of issues per A–J. Most arithmetic in the body checks out; however, I found a clear σ mismatch in Fig. 9 vs. the text/tables (P4-E6) and a rounding-driven inconsistency in Table II’s “Dev.” for the calibrated catalog (P4-M12). Cross-reference drift (P4-E7) and methodological presentation points (P4-M13–M15, P4-m8–m12) are common misses on first pass and should be straightforward to address. The rest of the initial report’s essential items still stand.