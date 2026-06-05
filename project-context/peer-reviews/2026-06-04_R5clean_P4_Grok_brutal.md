# P4 2026-06-04_R5clean — Brutal-honesty journal referee (treating this as a real PRD submission)

**Model**: `grok-4.3`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 17.3s

---

**Referee Report for P4 (Physical Review D)**

**Paper length**: 56 pages. PRD methods/catalog papers are typically 15–30 pages. The manuscript is bloated with repetitive diagnostics, exhaustive null-model variants, multi-page artifact citations, and narrative hedging that does not advance the central claim. Recommended maximum length after revision: 25 pages. All non-essential appendices, exhaustive per-null tables, and “companion artifact” citations must be removed or condensed to a single reproducibility statement.

**ESSENTIAL findings** (paper cannot be accepted without these fixes)

- **P4-E1, Abstract + Sec. I (p. 1–3)**: The abstract states a headline “−0.12σ null” while the body reports a +3.64σ canonical-mask residual that is then re-interpreted as a systematic. The abstract does not honestly summarize what the paper proves (a null on one mask after MASTER, plus an unexplained residual on the canonical mask). Required fix: rewrite the abstract to state the two primary estimators, the canonical-mask residual amplitude and its systematic attribution, and the explicit statement that σ values are not comparable across nulls.

- **P4-E2, throughout (e.g., Sec. IV C, IV D, VI G, Table II, Table VI, Table VII, Table VIII)**: Multiple σ values derived from qualitatively different null procedures (per-pixel shuffle, label shuffle, binomial monopole-only, bootstrap) are presented with numerical comparisons or joint interpretations without consistent qualification. The single sentence in the abstract is insufficient. Required fix: every numerical result must carry an explicit parenthetical identifying its null model; any cross-comparison must be removed or replaced by rank-order statements only.

- **P4-E3, throughout (hundreds of instances)**: The manuscript contains pervasive internal audit/review-log language: “companion artifact pipelines/…”, “reproducibility artifact”, “legacy pre-correction baseline”, “SHA-256 stamped”, “v1.0.76”, “retracted”, “queued”, “on-disk MC log is the canonical record”, etc. These are not journal-clean. Required fix: delete every such phrase. Replace with a single Data Availability statement listing the public repository and the exact commit/tag used for the final results.

- **P4-E4, Sec. III A (p. 6)**: The analysis hierarchy is declared “after the first round of catalogue results” and fixed at v1.0.76. This is post-hoc and version-history language. Required fix: remove all language about when the hierarchy was fixed; present the hierarchy as the analysis choice without temporal qualifiers.

- **P4-E5, Sec. IV B, IV C, VI A, Table V**: The 9.5σ residual monopole is repeatedly described as “not interpreted cosmologically” while the paper simultaneously uses its existence to explain the canonical-mask residual. This is internally inconsistent. Required fix: either (a) demonstrate that the monopole has zero dipole projection on the survey footprint (via explicit cross-power with the dipole template) or (b) state that the monopole is an unaccounted systematic that limits the dipole interpretation.

- **P4-E6, Sec. VI C and Table IX**: The statistical-only Fisher floor (~0.29 % full-amplitude) is presented alongside the empirical 50 %-recovery threshold (0.75 %) without clear separation of what each number bounds. The abstract adopts the empirical number but the text mixes the two. Required fix: state once, unambiguously, that the headline sensitivity is the empirical, systematics-inclusive value and that the Fisher number is an ideal-statistical asymptote only.

**MAJOR findings** (significant revision required)

- **P4-M1, Sec. I and V A**: Claims of amplitude inconsistency with Shamir (2012, 2020, 2022) are presented without a matched-footprint Ganalyzer reanalysis. The paper correctly notes this limitation but then repeatedly uses the amplitude difference as evidence against prior claims. Required fix: either perform the matched reanalysis or remove all language implying statistical exclusion of Shamir’s estimator.

- **P4-M2, Sec. IV D and VI G**: The multi-null battery and cross-spectrum arguments used to attribute the +3.64σ canonical residual to systematics are suggestive but not a formal model comparison. The bootstrap injection test is acknowledged as “tautological” for the cosmological-dipole hypothesis yet is still cited. Required fix: replace the narrative multi-discriminator argument with a single, pre-specified model-comparison statistic (e.g., Bayesian evidence ratio between pure-dipole and dipole+systematic-template models) or downgrade the claim to “qualitatively consistent with systematics.”

- **P4-M3, entire manuscript**: The 56-page length and exhaustive enumeration of every possible null variant, hold-out, and cross-check constitute narrative inflation. The central claim (null dipole on the subsample mask after MASTER) can be stated and defended in far fewer pages. Required fix: condense to ≤25 pages; move all secondary diagnostics to a compact supplementary table or delete.

**MINOR findings** (should be addressed)

- **P4-m1, Sec. II B**: The GZ1 agreement (69.91 %, κ=0.40) is correctly reported as moderate, but the text still cites the 93.7 % training-set accuracy as the headline figure in multiple places. Required fix: move the training-set accuracy to a methods paragraph and foreground the independent GZ1 number.

- **P4-m2, Sec. VI D**: The edge-on contamination discussion is qualitative. A quantitative dilution factor derived from the b/a < 0.3 subsample should be stated once and used to adjust the sensitivity floor.

**NIT findings** (very minor)

- **P4-n1**: Occasional typographic inconsistencies (e.g., “peq” vs. “p_eq”, mixed use of “canonical-N” and “canonical mask”).
- **P4-n2**: Several figure captions contain parenthetical cross-references to companion artifacts that must be removed.

**Summary recommendation**  
**REJECT**

The manuscript is not journal-clean. It is 56 pages (more than double the typical PRD length for this class of paper), saturated with internal review artifacts (“companion artifact”, version tags, retracted claims, on-disk logs), and presents multiple σ values derived from incommensurate null procedures while claiming a clean null result. The central scientific claim—a null ℓ=1 dipole after MASTER on one mask—is defensible but is buried under narrative inflation and post-hoc reinterpretation of a +3.64σ residual. A drastically shortened (≤25 pp), artifact-free revision that (i) removes all internal tags, (ii) enforces uniform σ qualification, (iii) performs or explicitly disclaims a matched-pipeline comparison with prior work, and (iv) replaces the multi-null narrative with a single pre-specified model comparison could be reconsidered. In its current form the paper is not acceptable for Physical Review D.