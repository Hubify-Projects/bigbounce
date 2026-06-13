# P4 R37conf — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v182.pdf` md5=d3785514 pages=23
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (7708 chars)
**Wall time**: 331.1s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA …” (23 pp.)

Scope of review
I evaluated the statistical methodology, estimator definitions and hierarchy, null procedures, MC sizes, arithmetic consistency (counts, fractions, fsky, conversions between fCW and Ap), dimensional consistency, and the traceability of every scalar quoted in the abstract, tables, and conclusions to statements in the body. I also audited internal version/provenance language and reproducibility surfaces per PRD expectations.

Overall assessment
The manuscript contains substantial methodological work and an unusually detailed null-calibration program. However, there are several essential issues that must be corrected before this can meet PRD standards, including inconsistencies in the training set accounting, a mismatch between the canonical-mask pixel count and reported fsky, pervasive version-history/audit prose and file-path references in the main text, and a versioning mismatch between the title-page stamp and the Data Availability section. There is also confusion in the look-elsewhere treatment of the hemisphere scan, and several clarity issues around field conventions in the harmonic channel.

Findings

ESSENTIAL

P4-E1 (Sec. II.B, p. 2–3): Training-set augmentation arithmetic is inconsistent
- Offending text: “The combined training set contains 25,790 source images; after flip augmentation of the training split the combined pool is 26,616 (80/20 split: ntrain = 21,293, nval = 5,323). The 826-image difference … arises entirely from horizontal-flip augmentation applied to the training split only — the validation split is never augmented.”
- Problem: If horizontal-flip augmentation is applied to the training split, one expects either on-the-fly stochastic augmentation (no change to the pool size) or a deterministic duplication of the training set (+Ntrain images). Here only +826 images are added to the pool, which is not explained by a standard augmentation protocol, and the description conflicts with the usual semantics of “applied to the training split.” The numbers 21,293 (train) and 5,323 (val) sum to 26,616 and imply that only 826 training images were duplicated offline.
- Required fix: Provide a precise, reproducible description of the augmentation policy that explains +826. Explicitly list pre-augmentation ntrain0 and nval0, the fraction or rule by which a subset of training images was flipped and stored, and confirm that validation had no augmentation. If augmentation is stochastic per epoch, remove the “combined pool = 26,616” statement and clarify that counts refer to on-disk items without duplication.

P4-E2 (Title page and throughout; e.g., Abstract p. 1; Sec. IV.D p. 9–12; Appendix A.d p. 16–17; multiple “earlier text misprinted/misquoted” notes): Version-history and audit log language in the body
- Offending examples:
  - Title page: “(Dated: June 12, 2026 — v1.0.182)”
  - Abstract: “An earlier version of this paper reported … that result is withdrawn (Appendix A) …”
  - Appendix A.d: “An earlier version … a subsequent provenance audit found … the result is therefore withdrawn.”
  - Numerous “earlier text misprinted,” “mis-attributed,” “earlier rendering,” “superseded,” and file-path artifacts litter the body (e.g., pp. 10–12, 15–21).
- Problem: PRD manuscripts must not contain version stamps, internal revision log prose, or retracted-run narratives in the main text. Such content belongs, at most, in a brief erratum-style note or in Supplementary Material, not in the primary scientific narrative.
- Required fix: Remove the version number from the title page. Excise “earlier version/withdrawn” narratives from the abstract and body. Condense any necessary clarifications to a single short Methods note (e.g., “We discovered an error in an internal test mask; all reported results use the canonical masks defined in Appendix A”) and move all provenance/audit discussion and run logs to a Supplementary Material (SM) with a DOI. Replace every in-text file path with a numbered reference to the SM.

P4-E3 (Appendix D.g Table XI p. 20 vs. multiple places incl. Table I p. 5, Appendix A.c p. 15–16): Canonical-mask fsky vs. pixel-count inconsistency
- Offending text:
  - Many places (e.g., Table I caption, Appendix A.c): “Canonical (Nspiral(p) ≥ 10) fsky = 0.49005.”
  - Appendix D.g Table XI: “Pixel count (Nspiral ≥ 10) = 24,061; fsky = 0.49005; NSIDE = 64.”
- Problem: At NSIDE = 64 (Npix = 49,152), 24,061/49,152 = 0.48967, not 0.49005. The stated fsky and pixel count cannot both be correct under the binary-mask definition used elsewhere. This inconsistency undermines all downstream statements that rely on the precise mask fraction.
- Required fix: Recompute and report a single consistent pair: either correct the pixel count or the fsky. State explicitly how fsky is computed (binary fraction of all HEALPix pixels at NSIDE=64). Propagate any corrections that affect quantities (e.g., effective sky fraction tables, mask-equivalence audit, Table I entries).

P4-E4 (Throughout; e.g., pp. 2–4, 5–13, 15–22): Pervasive in-text file paths and internal artifact identifiers
- Offending text: Hundreds of occurrences like “artifact pipelines/p2_chirality/outputs/...json”, “artifact c9b”, etc.
- Problem: PRD manuscripts should not refer to local file paths or internal artifact nicknames in the main text. This impedes readability and is not an archival citation practice.
- Required fix: Move these references to a curated Supplementary Material (or data release) with a stable DOI. In the main text, replace file-path strings with numbered citations to SM sections/figures/tables (e.g., “see SM Sec. S3, Fig. S7”).

P4-E5 (Data Availability, p. 21 vs. Title page p. 1): Versioning/provenance mismatch and missing archival freeze
- Offending text: Title page stamp “v1.0.182,” while Data Availability states “Repository state for this version: commit 53b41d12 (v1.0.180, June 2026)” and indicates “a Zenodo DOI … has not yet been minted.”
- Problem: The manuscript must pin a single, immutable release (code, catalog, and analysis artifacts) with a DOI. The mismatch between v1.0.182 (title) and v1.0.180 (Data Availability) is unacceptable.
- Required fix: Freeze a single release (code + model + catalogs + SM artifacts) with a DOI (Zenodo or equivalent). Ensure the manuscript cites exactly that DOI and a single version string consistently (remove v1.0.182 from the title page per P4‑E2). The links to HuggingFace should also be paired with a frozen snapshot DOI (via Zenodo integration) rather than only a mutable tag.

P4-E6 (Abstract p. 1 and Sec. I–VII): Maintain strict non-comparability warnings whenever σ from different nulls are juxtaposed
- Issue: Although the body often notes non-comparability (e.g., Sec. III.A, Table I caption, Sec. IV.C–D), the abstract lists “+0.41σ … +3.64σ … +7.28σ” without explicitly reminding the reader that these come from different nulls/fields and are not directly comparable. PRD abstracts must not encourage cross-channel σ comparisons.
- Required fix: Add a one-sentence qualifier in the abstract explicitly stating that these σ values arise from distinct estimators and nulls and are not directly comparable.

MAJOR

P4-M1 (Appendix C, p. 18–19; Table I p. 5): Hemisphere look-elsewhere treatment is confusing and double-corrected
- Offending text: “maximum asymmetry 3.05σ … The direct-MC look-elsewhere test … gives pLEE ≤ 10−4 … The Bonferroni/BH pass … reduces the post-LEE significance to < 1σ.” Table I also lists “pLEE ≤ 10−4 (syst.-attr.).”
- Problem: Reporting both a proper max-statistic Monte Carlo pLEE and then applying an additional Bonferroni/BH correction to the same grid is conceptually a double-penalty and confuses the reader as to the operative family-wise p-value. PRD expects a single, principled LEE correction.
- Required fix: Report only the direct-MC max-statistic pLEE (state the exact grid and correlation structure), and drop the secondary Bonferroni/BH numbers from the main text. If you wish to compare heuristics, move them to SM and state clearly that the operative pLEE is from the max-statistic MC.

P4-M2 (Sec. IV.C–D, Table III p. 11, Appendix A.a–c p. 15–16): Field/normalization conventions in the harmonic channel are difficult to follow
- Issue: The manuscript alternates between Ap and (fCW−0.5)=Ap/2 conventions, with mask-mean subtractions using Wp=Nall or Nspiral, and with monopole-subtracted vs. un-subtracted pseudo-Cℓ. While many caveats are present, the mixing makes it hard to trace a clear, single definition of the field used for each quoted number in Table III and in the text.
- Required fix: Consolidate definitions in one place (end of Sec. IV.B or start of Appendix A) in a single table mapping every quoted harmonic number (data vector, weight, apodization, mean-subtraction rule, band binning, null type). In the main text, reference that table rather than re-defining ad hoc. Ensure each occurrence of a Cℓ or z in the harmonic channel unambiguously points to its field convention.

P4-M3 (Sec. VI.A & Table V, p. 12–13): Axis-draw convention in injection–recovery
- Issue: The baseline injection sweep uses θ-uniform axis draws (not area-uniform), and only afterwards a spot-check with area-uniform shows similar thresholds. For PRD, the default should be area-uniform sampling on S2.
- Required fix: Rerun the primary injection–recovery sweep with area-uniform axis draws (cos θ ∼ U[−1,1]) and update Table V accordingly, or elevate the existing area-uniform rerun to the main table, moving the θ-uniform results to SM.

P4-M4 (Appendix E.b, p. 21): “Monopole-preserving … +4.31σ” estimator description is obscure
- Issue: The text introduces yet another pseudo-Cℓ variant (“monopole-preserving, single-mode pseudo-Cℓ before subtraction and before MASTER deconvolution”) with a +4.31σ value used only for a high-confidence-collapse check. This was not defined earlier and risks confusion with the canonical +3.64σ and apodized +7.28σ diagnostics.
- Required fix: Either: (i) remove this additional estimator from the main text (move to SM), or (ii) add it to the consolidated harmonic definitions table (see P4‑M2) with explicit field/weight/mean-subtraction choices and a clear rationale for its use.

P4-M5 (Sec. E.a, p. 20–21): Edge-on contamination quantification lacks data source specification
- Offending text: “65.7% of visually identified edge-on systems (b/a<0.3) …”
- Problem: It is unclear how b/a is obtained (which DR8 column? which catalog?), what sample is used, and how the “visually identified” subset is constructed. This result underpins the stated 5–8% sensitivity penalty.
- Required fix: Specify the source of b/a (e.g., LS DR8 tractor shape parameters with exact column names), the selection used to define edge-on (cuts applied, e.g., fracdev, axis-ratio estimator), and the sample size used for the 65.7% figure. Otherwise, soften/remove the quantitative penalty estimate.

MINOR

P4-m1 (Abstract p. 1; Sec. VII.a p. 14): Novelty phrasing
- Offending text: “largest chirality-labeled galaxy catalog to date.”
- Comment: This appears to be accurate relative to CE-ResNet (1.95M vs. 3.2M spirals), but add a citation directly in the abstract or soften to “to our knowledge, the largest …” (the body already uses this).

P4-m2 (Sec. I, p. 2): “factor of ∼6–12 under the present pipeline” exclusion of the 3% class
- Suggestion: Clarify that this is an amplitude-level inconsistency, not a formal likelihood exclusion, and that matched-footprint re-analyses would be required for a σ-level exclusion (you mostly do this; ensure the abstract and conclusion both carry the caveat).

P4-m3 (Sec. III.A, p. 3–4; multiple): Nomenclature for “moment-z” and “rank-p”
- Suggestion: Define once and thereafter abbreviate consistently (e.g., zmom, prank). Avoid restating the non-Gaussian mapping caveat in-line more than once; point to Sec. III.A.

P4-m4 (Sec. VII.a, Table VI p. 14): Provide uncertainty bands on “median z” where relevant
- Suggestion: Report interquartile ranges for recovered z in the harmonic-channel injection table to characterize axis-dependence spread.

P4-m5 (Typos/formatting, multiple pages):
- Examples: “C 2 2◦” appears with inconsistent spacing/superscripts; ensure consistent typesetting “C2 apodization (2°)”. Fix various minor hyphenation and en-dash/em-dash usages.

NIT

P4-n1 (Acknowledgments p. 22): “AI tool usage” statement
- Comment: Acceptable, but consider moving to a footnote or SM per journal style.

P4-n2 (Redundancies): The phrase “systematics-attributed” is used very frequently; consider light editing for concision.

Length
The manuscript is dense but lengthy (23 pages). Given the large amount of provenance and run-log detail in the body, I recommend moving most file-path/“artifact” references, audit trail text, and secondary diagnostics to a Supplementary Material with a DOI. The main text could likely be reduced by 15–20% without loss of scientific content.

Abstract-last drift sweep (pattern-045)
- All headline scalars in the abstract trace to the body, but the abstract needs (i) an explicit reminder that σ from different channels are not comparable (P4‑E6), and (ii) removal of “withdrawn”/audit language (P4‑E2). The “A95 between 1.0% and 1.5% (A50 ≈ 0.75%)” claim matches Table V; ensure the axis-sampling convention is area-uniform for the main reported thresholds (P4‑M3).

Provenance surfaces (patterns 046/047)
- The code/data version mismatch (P4‑E5) and the absence of a frozen DOI for the catalog/model and SM are blocking issues for PRD.

Uncomputed quantitative claims (pattern-048)
- Most assertions are quantified. The edge-on fraction and penalty need clearer sourcing (P4‑M5).

Effect sizes
- For every σ you generally provide an amplitude (e.g., Adip = 4.4×10−3; C1 values). This is good; retain.

## Summary recommendation
MAJOR REVISIONS

The paper presents careful and potentially important methodology and a large public catalog, but it currently does not meet PRD standards due to (i) internal arithmetic/provenance inconsistencies (training augmentation counts; canonical-mask fsky vs pixel count), (ii) pervasive version-history/audit/file-path prose in the main text, (iii) a versioning mismatch and lack of a frozen DOI, and (iv) clarity issues in the look-elsewhere and harmonic-field presentations. These are fixable. Once the essential corrections are made, the narrative cleaned of audit logs, and a single frozen, citable release is provided, the work could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-E7 (Appendix D.g, footnote 3; bootstrap block counts vs fsky): NSIDE-dependent super-pixel counts are inconsistent with the stated fsky
- Offending text: “NSIDE = 8 … 440 super-pixels” (and at NSIDE = 4: “∼127 super-pixels”), all for the canonical Nspiral≥10 mask with fsky ≈ 0.49005.
- Problem: At NSIDE = 8, Npix = 768, so a binary mask with fsky = 0.49005 would contain ≈ 0.49005×768 ≈ 377 super-pixels if defined geometrically at that NSIDE. The reported 440 implies an effective NSIDE=8 sky fraction ≈ 0.573. Likewise, at NSIDE = 4, Npix = 192, 127/192 ≈ 0.661. This suggests the block set was defined as the union of NSIDE=8 (or 4) pixels containing any NSIDE=64 in-mask child, inflating area relative to the binary definition. That choice changes block geometry and the spatial-coherence scale entering the bootstrap variance.
- Required fix: Explicitly define how block membership is constructed across NSIDEs; report the NSIDE=8 and NSIDE=4 geometric fsky implied by the block lists; justify the use of union-coverage masks for resampling, or recompute block lists that preserve fsky (and reassess σboot and the −18 z).

P4-E8 (Table I, footnote a; cross-reference): Wrong appendix table reference
- Offending text: “fsky = 0.49005 … (Appendix A Table VI).”
- Problem: In Appendix A, the consolidated mask/weight/apodization table is Table VII, not VI. Table VI in the main text is unrelated (harmonic-channel completeness).
- Required fix: Correct “Appendix A Table VI” to “Appendix A Table VII” (and re-check all table cross-references).

P4-E9 (Figure 7 caption vs null-comparability): Missing “not directly comparable” qualifier in a figure caption
- Offending text (Fig. 7 caption): “2.31σ real-space dipole + +6.48σ pre-MASTER … collapses to 0.41σ.”
- Problem: Two σ values from different estimators/nulls are juxtaposed in a caption without the non-comparability warning that the body provides elsewhere. PRD expects the same rigor in figure captions.
- Required fix: Add an explicit note in the caption that these σ values come from different estimators and null procedures and are not directly comparable.

P4-M6 (Sec. IV.C; Table V; Table I row (i) vs (vii)): Null-mismatch between the primary real-space estimator and the injection–recovery floor
- Issue: The primary real-space dipole significance uses an isotropic pixel-permutation null, while the quoted A50/A95 floors (Table V; Table I row vii) are computed against a per-pixel (binomial) label-shuffle null that preserves per-pixel totals. These are different nulls for the same estimator, yet the floors are used as the operative sensitivity for the primary result.
- Required fix: Recompute the injection–recovery curve with the same isotropic-permutation null used by the primary estimator (and area-uniform axis draws; cf. P4-M3). Alternatively, keep both and clearly state which floor applies to which null, and which one is the operative falsification threshold for the primary estimator.

P4-M7 (Sec. B and throughout): Inconsistent terminology for null randomizations (“per-galaxy label-shuffle,” “per-pixel label-shuffle,” “pixel-permutation,” “isotropic-bootstrap”)
- Issue: The manuscript alternates between several names for its nulls, sometimes in adjacent sections (e.g., Table III caption: “per-galaxy label-shuffle”; Sec. IV.C: “per-pixel label-shuffle null”; Sec. IV.C primary: “isotropic realizations … permuting Ap across pixels”). It is not always explicit what is preserved: per-pixel counts, global monopole, depth-decile strata, or nothing.
- Required fix: Add a single glossary-style table that precisely defines each null used (algorithmic steps and invariants). Use those names consistently in all tables, figures, and text.

P4-M8 (Appendix A.a; Fig. 8 caption vs text): Pseudo-Cℓ vs MASTER-deconvolved Cℓ nomenclature is sometimes conflated near captions
- Issue: Fig. 8 caption describes “Pseudo-Cℓ on the canonical mask” with a 200-MC “multi-null battery,” but the paragraph immediately below in the body pivots to the post-MASTER “canonical-mask +3.64σ” diagnostic. Readers can misinterpret which spectrum the σ refers to in the panel.
- Required fix: Keep the figure’s discussion strictly to the estimator shown (pseudo-Cℓ). Move the post-MASTER σ to the body with an unambiguous pointer to the corresponding estimator and field convention (per P4‑M2).

P4-M9 (Appendix B.d; Sec. B, T1/T7): Equivariance/QC metrics partially rely on reconstructed flip-leg probabilities from mismatched inference passes
- Offending text: “the flip-pass probabilities are recovered from the stored raw and 2-fold-TTA columns via p_flip = 2 p_eq − p_raw … for 2.9% of rows a recovered flip probability falls outside [0,1] … those rows derive from a separate raw-catalog inference pass rather than the equivariant pass…”
- Problem: Several QC summaries (e.g., T7 calibration proxy) are computed using reconstructed flip legs that are known to be inconsistent for 2.9% of rows. Although a flag and sensitivity check are provided, the global T1/T7 metrics as reported implicitly mix exact and reconstructed legs.
- Required fix: Recompute all QC metrics from a single, consistent inference pass that logs both original and explicit flip legs for every galaxy. Alternatively, restrict QC metrics to the subset with exact legs and report both the restricted and full-sample results.

P4-m6 (Sec. VII.a, Table VI): Report axis-spread for injected harmonic-channel z
- Issue: Table VI lists “median z ≈ 68–218” for Ap = 1.7% without dispersion. The main text elsewhere emphasizes axis dependence.
- Suggested fix: Add interquartile ranges (or 16–84%) for recovered z per axis to quantify axis spread.

P4-m7 (Sec. IV.C, confidence-cut sweep): Non-monotonic z values are reported without uncertainty bands
- Offending text: “z = +4.3, +4.1, +4.0 at cuts 0, 0.4, 0.5; collapsing to +0.41, +1.14, +0.51 at 0.6, 0.7, 0.8…”
- Comment: It would help to report per-cut MC uncertainties (e.g., standard error on zmom or rank-p) to show the statistical indistinguishability of the small differences across adjacent cuts.

P4-m8 (Sec. IV.D/Table IV, hemisphere-statistic grids): Two different direction grids (648-point 10° grid; 768-point NSIDEdir=8) are used for hemisphere scans with different nulls, but this is easy to miss
- Suggestion: Add an explicit statement near first mention that hemisphere diagnostics use two distinct grids for two different purposes (label-shuffle LEE vs monopole generative-null test), so their z and p are not cross-comparable.

P4-n3 (Appendix A.c): “C2 2°” apodization formatting is inconsistent
- Comment: Standardize to “C2 apodization (2°)” throughout captions and appendix text (several instances show “C 2 2◦” or mixed spacing).

P4-n4 (Sec. II.B, novelty of “bias-hardening audit suite”): Clarify scope briefly
- Comment: Since much of T1–T8 are implementation/QA checks rather than astrophysical bias tests, a brief one-sentence delimitation (“these tests validate implementation stability and obvious leakage; they are necessary but not sufficient for sub-percent cosmology”) would prevent over-interpretation. You already say this in Appendix B; add a pointer in Sec. II.B.

Explanation
The additional findings arose from (i) recomputing counts and geometric expectations at alternate NSIDEs (exposing the block-bootstrap super-pixel/fsky inconsistency), (ii) scanning captions for null-comparability caveats, (iii) auditing cross-references and table numbering, and (iv) tracing null definitions line-by-line for consistency. The issues above are distinct from those in the initial report and focus on arithmetic/cross-ref correctness, null-algorithm clarity, and caption-level caveats.