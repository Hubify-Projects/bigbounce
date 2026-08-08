# P4 INT-X-P4 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/P4_int.pdf` md5=077eeee9 pages=24
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 71.2s

---

**Referee Report**

**Paper:** Survey-Scale Galaxy Chirality with Equivariant TTA… (P4)

**Recommendation:** REJECT

The manuscript is not in a state suitable for review at PRD. It is a raw internal working document containing dozens of code paths, artifact filenames, commit hashes, and unreleased JSON references that have no place in a journal submission. These alone constitute an ESSENTIAL barrier. In addition, the central statistical claim (a clean null real-space dipole) rests on training labels that are 66.5 % model-derived; the resulting shuffle and permutation nulls are therefore circular for the very survey systematics the paper claims to have controlled. The manuscript is also ~2× longer than warranted by a null result whose primary cosmological content is a single +0.41σ measurement. Multiple other ESSENTIAL and MAJOR problems are enumerated below.

**ESSENTIAL findings (paper cannot be accepted without fixes)**

- P4-E1 (throughout, e.g. pp. 2–3, 5, 9–12, 16–17, 20): The text is littered with internal artifact strings (“artifact c12_r24conf_local.batch.json”, “pipelines/p2_chirality/outputs/canonical_provenance/c11_meta_m4_slab_stats.json”, “c9e”, “c9b”, SHA256 prefixes, seed=42, etc.). These are not reproducibility metadata; they are working-directory breadcrumbs. A submitted manuscript must contain none of them.
- P4-E2 (p. 1, abstract paragraph; §II.B p. 3): 66.5 % of training labels are CE-ResNet predictions. The paper’s own shuffle and per-pixel permutation nulls therefore randomize the model’s own outputs. This circularity is fatal for any claim that the null tests have excluded survey-correlated label noise inherited from CE-ResNet. The text acknowledges the issue (“so they do not by themselves test independence”) yet still presents the +0.41σ result as the primary cosmological estimator. This is not acceptable.
- P4-E3 (p. 1 and Table I): Multiple σ values obtained from qualitatively different null procedures (pixel-permutation, label-shuffle, block-bootstrap, monopole-only generative) are placed in the same table and abstract without a standing, explicit qualifier that they are “not directly comparable as detection significances.” The single sentence on p. 1 is insufficient; every juxtaposition must carry the caveat.
- P4-E4 (p. 1, “Dated: June 28, 2026”): A future date appears in the author block. This is either a placeholder error or evidence that the file has not been prepared for external review.
- P4-E5 (abstract vs. body): The abstract states the dipole is “consistent with null” at +0.41σ (p = 0.31). The body later shows that the same data vector yields +3.64σ (canonical mask) and +7.28σ (apodized) in the MASTER channel, attributed to leakage. The abstract therefore presents only the most favorable of several estimators without disclosing the size of the leakage term that the analysis itself flags as the dominant systematic. This is a material mismatch.

**MAJOR findings**

- P4-M1 (p. 3, §II.B): GZ1 cross-match accuracy is quoted as 69.91 % (Cohen’s κ = 0.40). This is treated as “explicitly conservative,” yet the paper uses the resulting catalog for an 8.47-million-galaxy cosmological claim. No propagation of this label noise into the final dipole uncertainty is shown.
- P4-M2 (p. 1, 7; Table I row iv): The 10^4-permutation apodized MASTER result (+7.28σ) is presented as a “systematics diagnostic” while the real-space dipole is presented as the “primary cosmological estimator.” The distinction is asserted rather than demonstrated by a quantitative test that the two estimators respond differently to the same injected systematics.
- P4-M3 (p. 4, Fig. 1 caption; p. 5, Table I): The canonical mask definition (N_spiral(p) ≥ 10) is changed between figures and tables without a single consolidated statement of the exact threshold used for every quoted number. Readers cannot reproduce the exact sample from the text.
- P4-M4 (length): 24 pages for a null result whose headline measurement is one 0.41σ number plus an extensive systematics audit is disproportionate. A PRD methods or results letter on a null dipole should not exceed ~10–12 pages including figures.

**MINOR / NIT findings (representative sample)**

- P4-n1: Duplicate phrasing “canonical canonical-mask” appears in at least two figure captions.
- P4-n2: Several axis labels in Figs. 4–5 use inconsistent capitalization and missing units.
- P4-n3: The 50 %-recovery A_95 = 0.75 % threshold is stated as an empirical floor yet is never shown as a curve with injected-signal recovery fraction versus amplitude; only a single operating point is given.

**Summary recommendation**

REJECT

The manuscript as submitted is an unreviewed internal draft containing pervasive code artifacts, an inadequately controlled circular null-test strategy, and an abstract that selectively reports the most favorable estimator while the body demonstrates substantial leakage in the harmonic channel. These problems are not cosmetic; they undermine the central claim that a clean, survey-scale real-space chirality dipole has been shown to be consistent with null. A complete rewrite that (i) removes every internal filename, (ii) replaces the CE-ResNet-derived labels with an independent training set or quantifies the induced bias, (iii) collapses the manuscript to a concise null-result letter, and (iv) applies uniform, explicit “not directly comparable” language to every cross-null comparison would be required before the paper could be considered for review.