# EXT1 P4 — External Referee Truth Audit
**Paper:** P4 — Survey-Scale Galaxy Chirality (v1.0.171, 21 pp)  
**Source file:** `pipelines/p2_chirality/chirality_catalog_paper.tex`  
**Reviewers audited:** ChatGPT Pro Extended (MAJOR), Grok Heavy (MINOR), Gemini 3.5 Thinking (MINOR)  
**Auditor:** Claude Sonnet 4.6 (bigbounce truth-audit protocol)  
**Audit date:** 2026-06-10  

**Key SAMPLE+ESTIMATOR+NULL rule:** all verifications identify sample (HC p>0.6, N=949,584 vs full 3.2M), estimator (real-space dipole vs MASTER vs WLS), and null (iso-boot vs label-shuffle vs block-boot) before concluding discrepancy.

---

## Verdict Table

| # | Reviewer | Severity | Finding | Verdict | Evidence |
|---|----------|----------|---------|---------|----------|
| F1 | ChatGPT | BLOCKER (B1) | Commit 2a2939b2 in Data Availability = v1.0.166, but PDF is v1.0.171; headline values differ (+0.43σ/p=0.30/N=471,049 in .tex vs +0.41σ/p=0.31/N=949,584 in PDF). Source-to-PDF chain not auditable. | VERIFIED | `git show 2a2939b2` confirms that commit is the v1.0.166 SEV-1 retraction commit. Current `\paperVersion{v1.0.171}` but `\Data Availability: commit 2a2939b2` never updated. The v1.0.166 .tex does contain +0.43σ, p=0.30, N=471,049 (HC-strict p>0.9 sample). v1.0.171 updated to HC-broad p>0.6, N=949,584, +0.41σ, p=0.31. Stale commit hash is a real artifact versioning gap. |
| F2 | ChatGPT | BLOCKER (B2) | Artifact `monopole_mask_null_results.json` says both observables are mask-coupled and neither is MASTER-deconvolved; pure monopole explains only ~12% of post-MASTER C₁, not ~100%. Claims "88% unexplained" by monopole-only leakage post-MASTER. | VERIFIED | `master_decoupled_monopole_null.json` (N=500): data_C1=6.554e-6, null_mean=8.01e-7, σ=4.84; `master_decoupled_monopole_null_10k.json` (N=10,000): σ=5.14. Ratio null_mean/data_C1 = 12.2%. `monopole_mask_null_results.json` config string explicitly states "neither is MASTER-deconvolved." The paper text in Sec. IV.D says monopole null is "consistent with monopole-mask leakage" for the +3.64σ value but does NOT use the post-MASTER decoupled artifact to support this claim — it uses only the pre-MASTER 99.32% reproduction. **The 99.32% claim is for pre-MASTER pseudo-C₁ only and is correctly stated in the paper.** The post-MASTER +3.64σ is attributed to systematic residuals via the 8-anchor battery (App. D), not to monopole-only leakage. ChatGPT's reading that the paper claims monopole-only explains the post-MASTER +3.64σ is incorrect — the paper explicitly calls the post-MASTER residuals "systematics-attributed." However, the leakage discussion in Sec. IV.D is genuinely ambiguous: "the +3.64σ canonical value is consistent with monopole-mask leakage" appears in the estimator hierarchy (item vi) in a way that could mislead readers. The prose needs one clarifying sentence distinguishing pre-MASTER (99.32% explained) from post-MASTER (residual requires depth/morphology systematics). The MASTER-decoupled monopole-only artifacts exist in the repo but are not cited in the paper text. |
| F3 | ChatGPT | BLOCKER (B3) | +3.64σ in abstract/conclusions is superseded by +7.93σ in Table III canonical row. Abstract foregrounds the superseded number. | PARTIAL | The paper's Table III caption explicitly states "+3.64σ is superseded as a table entry by the canonical rows above but retained in the text for continuity with the leakage analysis." The abstract and conclusions correctly label this as a non-headline diagnostic value: abstract says "MASTER pseudo-C_ℓ channel...is a systematics diagnostic, not an independent cosmological null." However, the abstract foregrounds "+3.64σ moment-z, ≈1.9σ Gaussian-equivalent, canonical mask" without clearly stating it is superseded. A reader could reasonably mistake this as the current best canonical MASTER value rather than a historical continuity value. The +7.93σ 10⁴-permutation canonical row (Table III) is not mentioned in the abstract. The two values are from different estimator conventions (500-MC direct vs 10⁴-perm coupled matrix), but this is insufficiently clear in the abstract. The warning "These two channels are not on the same statistical footing" is buried. Real confusability issue, though the scientific conclusions do not rest on either. |
| F4 | ChatGPT | BLOCKER (B4) | Training-set accounting inconsistent: Sec. II says 6637+17153+2000=25,790 images but App B says n_val=5,323 of 26,616 (total mismatch of 826). | PARTIAL | Confirmed discrepancy: 6637+17153+2000=25,790 raw sources; 80/20 split yields 5,158 expected val but App B gives n_val=5,323 of 26,616. The artifact `c17_item13_training_semantics.json` confirms n_train=21,293, n_val=5,323, total=26,616. The 826-count gap (26,616 − 25,790) is not explained in the paper text. This is not a harmless rounding error — it represents a real count difference between the stated source manifest (25,790 labeled images from 3 sources) and the actual training/validation pool (26,616). Likely explanation: augmented duplicates, but the paper does not state this. ChatGPT's diagnosis is correct: the paper needs an accounting reconciliation table explaining the 826 extra entries. |
| F5 | ChatGPT | BLOCKER (B5) | WLS/template-fit artifact `joint_nuisance_model_fit.json` reports f_sky_canonical=0.740926 and n_pix=36,418, while paper claims f_sky=0.49005. Bootstrap artifact uses galactic latitude cut mask (|b_gal|>15° & n_total>0), not canonical N_spiral≥10 mask. | PARTIAL | Confirmed: `joint_nuisance_model_fit.json` has `f_sky_canonical=0.740926` with `n_pix_in_mask=36418`. This is a mislabeled field — 36,418/49,152=0.741, which matches the mask-restricted normalization factor defined in App. A (the paper explicitly warns "the mask-restricted normalization is a weight-uniformity factor rather than a sky fraction"). The `joint_nuisance_bootstrap_sigma.json` uses mask `(|b_gal|>15°) & (n_total>0)` with 24,187 pixels — not the canonical N_spiral≥10 mask (24,087–24,297 pixels). Both artifacts yield A_dipole≈4.55×10⁻³ and z≈−18.1 consistently, so the headline result is robust across mask definitions. But the artifact `f_sky_canonical` field is numerically misleading, and the bootstrap mask description does not match the paper's stated "canonical mask." This is a real documentation/reproducibility gap but does not invalidate the headline z≈−18 exclusion. |
| F6 | ChatGPT | MAJOR (M1) | HC null depends on confidence cut that removes non-null full-sample signal; headline should be "HC-selected real-space null." | OPINION (with valid nit) | The paper fully acknowledges this: Sec. IV.B explicitly discusses the full-sample 0.57% dipole at z≈4.2–4.4 attributed to low-confidence systematic, the confidence-cut sweep, and states the HC threshold is pre-declared. The paper's abstract says "equivariant-catalog high-confidence dipole fit (confidence>0.6; N≈9.5×10⁵ spirals) gives +0.41σ" — the HC qualification IS in the abstract. The framing criticism has merit in that a casual reader might miss this, but the paper already uses "HC-broad" and "HC-selected" language throughout. OPINION as a blocker; a nit at most: the paper could more prominently label the headline as "HC-selected" in its first mention. |
| F7 | ChatGPT | MAJOR (M2) | "Three-interpretation closure" language is stronger than evidence; anchors are correlated. | OPINION | The paper already hedges appropriately: App. D says evidence "favors" interpretation (ii); the operational conclusion says "most likely explanation." The word "closure" appears in the section title (Sec. III.A heading "Generative Monopole-Only Null") and in the abstract (three-interpretation closure language). The paper is technically correct that it uses "consistent with" and "favored" rather than "confirmed." OPINION: tightening "closure" wording to "favors" throughout is a valid minor polish request but not a blocker. |
| F8 | ChatGPT | MAJOR (M3) | ℓ=2 cross-spectrum (r=−0.65, z=−2.89) underpowered with only 200 realizations and pixel-density proxy only; not strong enough to carry "confirmed" language. | PARTIAL | Cross-spectrum uses 200-realization permutation null (confirmed in App. D.h text and paper). 200 is the minimum cited. The paper does not use "confirmed" for this specific test; the App. D operational conclusion says "most likely explanation is...supported by: (a) ℓ=2 cross-spectrum anti-alignment." The 200-MC floor is an acknowledged limitation. The request for N_MC=5,000–10,000 and physical depth/PSF templates is valid. |
| F9 | ChatGPT | MAJOR (M4) | WLS block-bootstrap z≈−18 correctly downscoped, but "Shamir excluded" implication should be removed; this only excludes a clean template at A_ref=1.7%. | OPINION | The paper already contains exactly this caveat (Sec. V.A and App. D.g): "a matched-footprint Ganalyzer reanalysis is required for a likelihood-level exclusion" appears multiple times. The text explicitly says "we do not claim a frequentist exclusion of Shamir's Ganalyzer estimator." OPINION: ChatGPT's diagnosis was pre-empted. |
| F10 | ChatGPT | MAJOR (M5) | Classifier calibration (max-p 0.951 vs GZ1 accuracy 58.7%) should be elevated to abstract/conclusions limitation. | OPINION | The paper explicitly states in Sec. IV.A: "these max-class probabilities are not probabilistically calibrated" and "the catalog-wide mean confidence (0.951) far exceeds the independent GZ1 three-class accuracy (58.7%)." This caveat is in the Data Availability section and prominently in the catalog description. It is a design choice to put this in body text rather than abstract, but it is fully disclosed. OPINION as a blocker; Gemini F21 also flags this as a MINOR with the same "add to abstract/conclusions" request — reasonable polish. |
| F11 | ChatGPT | MAJOR (M6) | 21.4% argmax-label flip rate on borderline galaxies (Z₂ vs D₄); need spatially-stratified Z₂-vs-D₄ comparison in low-confidence tail. | OPINION | The paper reports this 21.4% rate and attributes it to "sample-noise on a fragile argmax statistic rather than a real D₄-TTA systematic" with sign-flip analysis. The paper correctly distinguishes mean p_CW stability (<0.0016) from argmax flip rate. The request for spatially-stratified Z₂-vs-D₄ in low-confidence tail is a valid future analysis but does not affect the headline HC null. OPINION as a blocker. |
| F12 | ChatGPT | MAJOR (M7) | "Largest chirality-labeled catalogue" claim: 8.47M total but only 3.20M spirals; should say "3.20M spiral chirality sub-catalogue." | OPINION | The paper text in Sec. IV.A already says "N_spiral=3,201,160 spirals, publicly released." The abstract says "8,474,531 DESI Legacy DR8 galaxies...with N_spiral=3,201,160 spirals." The distinction is clearly present. The "largest chirality-labeled catalogue" claim refers to the full catalog with chirality probabilities (which is 8.47M), not just confirmed spirals. The paper explicitly states all three classes. OPINION: a minor wording nit at most. |
| F13 | ChatGPT | MINOR | Add arXiv ID for Shamir 2022a (PASJ). ChatGPT suggests arXiv:2101.04068. | PARTIAL | Confirmed: `\bibitem{Shamir:2022}` has DOI:10.1093/pasj/psac058 but no arXiv ID. The suggested arXiv:2101.04068 cannot be verified without external search, but the missing arXiv ID is real. Note: the paper does correctly label this as Shamir (2022a) and separates it from Shamir (2022b/DESI). Fix is straightforward: add arXiv ID. |
| F14 | ChatGPT | MINOR | Title is too long. | OPINION | Editorial preference; journal decision. |
| F15 | ChatGPT | MINOR | Add line numbers for review. | OPINION | Standard format request for journal submission. Not a content issue. |
| F16 | ChatGPT | MINOR | Figure 3/NS gallery caption: "non-spiral / face-on / morphologically indeterminate" should be "non-spiral / edge-on / morphologically indeterminate." | VERIFIED | `fig_class_pie` caption (line 233) says "N_NS=5,273,371 (non-spiral / face-on / morphologically indeterminate)." However, the paper's Appendix E (line 660) correctly identifies the edge-on problem: "edge-on disk galaxies, whose spiral structure is obscured by projection." Face-on spirals are NOT classified as NS — they are the target chirality class. The caption is factually wrong: it should be "edge-on / morphologically indeterminate," as face-on objects are precisely what the classifier aims to label as CW/CCW. This is a genuine content error in the Fig. 3 / NS-class description. |
| F17 | ChatGPT | MINOR | Move long provenance/correction notes out of main flow into reproducibility appendix. | OPINION | Houston's transparency policy; HOUSTON-DECISION. |
| F18 | ChatGPT | MINOR | Unify confidence notation (p_eq, p_CW^eq, per-spiral confidence). | PARTIAL | Notation does vary. App. B defines p_eq as max-class equivariant probability. Adding a notation table in the front matter would help readers. |
| F19 | ChatGPT | MINOR | Add single p-value convention table. | PARTIAL | The paper mixes moment-z, rank-p, and Gaussian-equivalent σ. A compact cross-reference table would add clarity. |
| F20 | ChatGPT | MINOR | Local artifact paths should be stable DOI-backed links. Zenodo DOI not yet minted. | VERIFIED | `\Data Availability` says "a Zenodo DOI snapshot will accompany the journal submission" — DOI not yet minted, confirmed. This is a HOUSTON-DECISION (deliberate "mint at submission" policy). |
| F21 | ChatGPT | MINOR | PACS/bibliography format; coordinate conventions. | OPINION | Journal formatting; minor. |
| F22 | Grok | MAJOR (G-M1) | Monopole-only generative null description has internal inconsistency: prose near 99.32% could imply post-MASTER, but artifact confirms pre-MASTER only. Clarify 0.68% residual consistent with +1.69σ. | PARTIAL | Grok correctly identifies that the prose is ambiguous but does NOT claim the "88% unexplained" language appears in the paper (it explicitly says "the prompt's '88% unexplained' phrasing does not appear in the manuscript"). The paper's Table IV (monopole null) caption distinguishes pre-MASTER, and the body text says "MASTER deconvolution substantially reduces, but does not remove, this leakage." Grok's request to add one explicit sentence clarifying the 0.68% pre-MASTER residual consistency is a valid minor clarification. |
| F23 | Grok | MAJOR (G-M2) | NSIDE=8 block size for bootstrap not justified in text; request sensitivity to NSIDE=4 and NSIDE=16. | VERIFIED | Confirmed: Appendix D.g describes the block-bootstrap at "NSIDE=8 (N_boot=1000, 440 super-pixels)" but gives no justification for choosing NSIDE=8 over alternatives. The paper acknowledges the inflation factor (14.7×) but does not test other block sizes. Both Grok and Gemini flag this independently. The request for a block-size sensitivity footnote is valid and not currently in the paper. |
| F24 | Grok | MAJOR (G-M3) | Falsification criterion is estimator-specific; clarify that harmonic-channel completeness does not define primary falsification boundary. | PARTIAL | The paper's Sec. VII (Conclusions) explicitly says "These thresholds are estimator-specific: A50 and A95 are floors of the real-space dipole estimator...whereas the harmonic-channel completeness...is a property of the MASTER ℓ=1 diagnostic channel...The two are computed against different fields, weights, and null procedures and are not interchangeable." This is already handled in the conclusions paragraph. Grok requests one additional sentence in the abstract — a reasonable polish nit. |
| F25 | Grok | MINOR (G-mn1) | Fig 4 & 7 captions: add unit reminder A_p = 2(f_CW − 0.5). | PARTIAL | The sky map caption (Fig. 4) shows "color scale [−0.08,+0.08]" but does not include the A_p = 2(f_CW − 0.5) reminder inline. The equivariance demo caption (Fig. 7) mentions the convention once. Adding explicit unit reminders is a valid minor. |
| F26 | Grok | MINOR (G-mn2) | Table I & III: add "Null procedure" column header summary row. | PARTIAL | Tables I and III have footnotes explaining null non-comparability. An additional column header would improve quick-scan readability. |
| F27 | Grok | MINOR (G-mn3) | Move withdrawn subsample-mask audit artifacts into Data Availability. | PARTIAL | Artifacts listed in App. A text (c3_, c6_) are not listed in the Data Availability section. |
| F28 | Grok | MINOR (G-mn4) | Shamir 2022 DOIs: ensure [2] and [3] are complete. | PARTIAL | Confirmed: Shamir:2022 has DOI:10.1093/pasj/psac058 (complete). Shamir:2022DESI has arXiv:2208.13866 and DOI:10.1093/mnras/stac2372 (complete). No action required for DOIs; the missing arXiv for Shamir:2022 PASJ is F13 above. |
| F29 | Grok | MINOR (G-mn5) | Typography: extraction artifacts, missing superscripts on σ values. | PARTIAL | Pre-submission proofread item. |
| F30 | Gemini | MAJOR (Ge-M1) | NSIDE=8 block-bootstrap scale not justified (same as F23). | VERIFIED | Independent corroboration of F23. Two of three reviewers flag this. |
| F31 | Gemini | MINOR (Ge-mn1) | T7 calibration proxy inversion in equivariant-class spirals: add physical/architectural intuition. | PARTIAL | The paper notes: "restricted to equivariant-class spirals only the mean ordering inverts (0.698 vs 0.464), driven by the raw/equivariant class-disagreement subpopulation." The text attributes the inversion to the QC edge-case flag. Adding one sentence of architectural intuition is a valid minor. |
| F32 | Gemini | MINOR (Ge-mn2) | Sec. IV.A: add explicit recommendation to calibrate soft probabilities (temperature scaling) before downstream use. | PARTIAL | The paper warns probabilities are not calibrated; the catalog Data Availability section says "should not be used for precision parity tests below 0.75% threshold without local re-normalization." Adding explicit calibration method suggestions (temperature/Platt scaling) is a valid community service minor. |

---

## Consensus Findings (2+ independent reviewers)

1. **NSIDE=8 block-bootstrap not justified** (F23/F30 — Grok + Gemini). The block size choice is stated but not defended in the text.
2. **Clarify pre-MASTER vs post-MASTER leakage framing** (F2/F22 — ChatGPT + Grok). The 99.32% figure is pre-MASTER only; post-MASTER residual requires depth/morphology systematics beyond monopole-only. This is correct in the paper but the prose in Sec. IV.D can be read as claiming monopole explains the post-MASTER +3.64σ.
3. **Falsification criterion estimator-specificity** (F24/Grok + abstract). Grok + Gemini both confirm this is handled in Conclusions but request one abstract sentence.

---

## Action Plan (Hardest First, VERIFIED/PARTIAL findings)

### P0 — Must fix before submission

**F1 (VERIFIED): Update Data Availability commit hash to current HEAD or v1.0.171 tag.**
- File: `pipelines/p2_chirality/chirality_catalog_paper.tex` line 674
- Change: `commit \texttt{2a2939b2}` → current HEAD commit or mint a Zenodo release tag first, then cite it
- The v1.0.166 and v1.0.171 differ in: headline σ (0.43→0.41), p-value (0.30→0.31), sample (N=471,049 HC-strict→N=949,584 HC-broad), and nearly 5 more version increments of analysis. A reader who pulls the cited commit gets materially different numbers.

**F2 (VERIFIED, partial): Add one clarifying paragraph distinguishing pre-MASTER vs post-MASTER monopole leakage.**
- File: `pipelines/p2_chirality/chirality_catalog_paper.tex`, Sec. IV.D / App. D preamble
- Add: "The 99.32% pre-MASTER reproduction figure is specific to the un-deconvolved pseudo-C₁; the post-MASTER MASTER-decoupled monopole-only null (N=500 realizations, artifact `master_decoupled_monopole_null.json`) gives σ=4.84, with monopole-only reproducing only ~12% of post-MASTER C₁. The post-MASTER residual therefore requires coherent depth/PSF/morphology systematics beyond the monopole-only channel." Cite the existing artifact.

**F16 (VERIFIED): Fix NS gallery caption wording from "face-on" to "edge-on".**
- File: `pipelines/p2_chirality/chirality_catalog_paper.tex` line 233
- Change: `non-spiral / face-on / morphologically indeterminate` → `non-spiral / edge-on / morphologically indeterminate`
- Face-on spirals are the desired chirality target; edge-on spirals are the contamination source.

### P1 — Should fix (VERIFIED/PARTIAL, reproducibility-relevant)

**F4 (PARTIAL): Reconcile training-set count (25,790 sources → 26,616 train+val pool).**
- File: Sec. II Training Labels, Appendix B
- Add one sentence: "After augmentation/deduplication the combined pool is 26,616 images (80/20 split: n_train=21,293, n_val=5,323); the 826-entry difference from the 25,790-source manifest reflects [augmentation/dedup policy]." The `c17_item13_training_semantics.json` artifact confirms n_train=21,293, n_val=5,323.

**F5 (PARTIAL): Fix `joint_nuisance_model_fit.json` mislabeled field `f_sky_canonical=0.740926`.**
- File: `pipelines/p2_chirality/outputs/canonical_provenance/joint_nuisance_model_fit.json`
- Change: rename `f_sky_canonical` to `mask_restricted_normalization_factor` or add a comment field explaining it is the weight-uniformity factor (n_pix/N_total), not a sky fraction. The paper text is correct; the artifact field name misleads external reproducers.
- Also: add a comment in the bootstrap artifact `joint_nuisance_bootstrap_sigma.json` noting that the `(|b_gal|>15°) & (n_total>0)` mask produces equivalent results to the canonical N_spiral≥10 mask (A_dipole consistent to 4 significant figures).

**F23/F30 (VERIFIED — consensus): Add block-bootstrap NSIDE=8 justification footnote.**
- File: `pipelines/p2_chirality/chirality_catalog_paper.tex`, App. D.g, block-bootstrap paragraph
- Add after "block-bootstrap at NSIDE=8 (N_boot=1000, 440 super-pixels)": "The NSIDE=8 block scale (~7° pixels) was chosen to preserve spatial coherence on angular scales ≳5° characteristic of the imaging-leg systematic structures while maintaining sufficient super-pixel statistics (440 blocks); sensitivity of z≈−18.1 to block size is given by [run NSIDE=4 and NSIDE=16 checks and add footnote or supplemental table]."

**F3 (PARTIAL): Clarify abstract treatment of +3.64σ vs +7.93σ.**
- File: `pipelines/p2_chirality/chirality_catalog_paper.tex`, abstract
- The abstract foregrounds "+3.64σ moment-z...canonical mask" without noting it is from a 500-MC direct run superseded in Table III by the 10⁴-permutation canonical row at +7.93σ. Add one parenthetical: "(500-MC direct-MC run; the 10⁴-permutation coupled-matrix canonical row is +7.93σ, both systematics-attributed)." The distinction is estimator-convention, not result quality, but must be clear.

### P2 — Polish minors (PARTIAL/OPINION with clear text fix)

- **F13**: Add arXiv ID for Shamir 2022a (PASJ). Locate via DOI:10.1093/pasj/psac058 search.
- **F18**: Add notation table defining p_eq, p_CW^eq, and max-class confidence in a dedicated "Notation" paragraph.
- **F19**: Add compact p-value convention table mapping each result to its convention.
- **F22**: Explicit sentence: "0.68% residual is +1.69σ consistent with the monopole-only null; this is the pre-MASTER diagnostic. The post-MASTER MASTER-decoupled null (artifact `master_decoupled_monopole_null.json`) shows the data remain σ=4.84 above the monopole-only null — the post-MASTER residual is not explained by monopole-only leakage."
- **F24**: Add one abstract sentence: "The falsification criterion [A≥A95, ≥5σ] is estimator-specific to the real-space dipole; the harmonic-channel completeness (P(≥3σ)≥0.999 at A_p=0.75%) is a separate diagnostic property."
- **F25**: Add A_p = 2(f_CW − 0.5) unit reminder to Fig. 4 and Fig. 7 captions.
- **F32**: Add to Data Availability or catalog description: "Users requiring calibrated probabilities for downstream probabilistic models should apply temperature scaling or Platt scaling; raw p_eq values are ranking scores, not frequentist probabilities."

### P3 — HOUSTON-DECISION items

- **F20**: Zenodo DOI minting timeline. Paper explicitly defers to journal submission. No change needed before submission trigger.
- **F17**: Long provenance notes in main text. This is Houston's deliberate transparency policy. Keep as-is unless journal requires restructuring.

---

## Gap Analysis — What Internal Rounds Missed

1. **Stale commit hash (F1)**: 5 version increments passed (v1.0.166→v1.0.171) without updating the Data Availability commit reference. Internal rounds audited headline numbers but not the Data Availability section for version consistency. Add to internal checklist: "After every version bump, verify Data Availability commit hash = HEAD."

2. **Post-MASTER monopole-only null not cited in text (F2)**: The `master_decoupled_monopole_null.json` and `master_decoupled_monopole_null_10k.json` artifacts were created (versions v1.0.121 and later) but never cited in the paper text. Internal rounds verified the 99.32% pre-MASTER claim but did not catch the missing post-MASTER artifact citation.

3. **NS gallery caption "face-on" error (F16)**: A content/semantic error in a figure caption that passed all internal math/stat reviews unnoticed. Suggests figure caption text is under-reviewed in internal rounds.

4. **Bootstrap artifact mask description mismatch (F5)**: The `joint_nuisance_bootstrap_sigma.json` uses a galactic-latitude-cut mask definition that differs from the paper's "canonical mask" description. The headline z≈−18 result is robust, so internal reviews passed the number — but the mask provenance would confuse an independent reproducer.

5. **Training set count discrepancy (F4)**: 25,790 (Sec. II) vs 26,616 (App. B) went uncaught because Sec. II and App. B are distant in the paper and the discrepancy is small relative to the total sample size.

---

## Verdict Summary

| Category | Count |
|----------|-------|
| VERIFIED | 5 (F1, F2-core artifact, F16, F23/F30-consensus, B1 commit) |
| PARTIAL | 10 (F3, F4, F5, F8, F18, F19, F22, F24, F25, F27) |
| OPINION | 9 (F6, F7, F9, F10, F11, F12, F14, F15, F17) |
| FALSIFIED | 0 |
| STALE | 0 |
| HOUSTON-DECISION | 2 (F17, F20) |

**Recommendation: CONDITIONAL ACCEPT after P0+P1 fixes.**

The paper's core scientific claims are solid and internally consistent. The headline +0.41σ real-space null and z≈−18 template exclusion are verified against multiple committed artifacts and are robust to mask/estimator variation. The transparency on the SEV-1 retraction, provenance audit, and systematic attribution is exemplary. 

Three genuine issues require pre-submission fixes: (1) update the stale commit hash in Data Availability — the cited v1.0.166 commit contains materially different headline numbers than the PDF; (2) add one explicit sentence distinguishing pre-MASTER (99.32%) from post-MASTER monopole-only reproduction (~12%) to prevent the main leakage conclusion from being misread; (3) fix the NS gallery caption "face-on" factual error. The block-bootstrap NSIDE=8 justification (consensus finding) and training-set reconciliation (826-count gap) should be added for reproducibility. None of the OPINION findings represent genuine scientific errors.

ChatGPT's 5-blocker assessment is partially justified for B1 (real, critical) and B4/B5 (real reproducibility gaps) but B2 and B3 overstate the severity — the paper already handles the post-MASTER interpretation correctly via the 8-anchor battery and the "superseded" notation, just not with sufficient clarity. Grok and Gemini's MINOR assessments correctly match the residual issue density after verifying the core science is sound.
