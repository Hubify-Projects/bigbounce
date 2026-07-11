# INT Claude-subscription Review — P4 v1.0.236 — claude-opus-4-8
paper: P4  version: v1.0.236  tex: pipelines/p2_chirality/chirality_catalog_paper.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T15:03:00Z
context-note: FR1 fresh round on the July-11 restamped version (no content change since exit)

======================================================================
RAW RESPONSE (verbatim):
======================================================================

I've read the complete manuscript and verified its core numbers against the committed artifacts. Summary of my independent checks (all recomputed, not just read):

- **Catalog counts/percentages** (CW 1,592,107 / CCW 1,609,053 / NS 5,273,371 / spiral 3,201,160 / total 8,474,531; 18.787/18.987/62.226/37.774%) — arithmetic exact.
- **CW fractions & deviations** (Cat A 0.507879, +28.72σ; Cat C 0.497353, −9.47σ; binomial σ) — exact.
- **Headline dipole** — `catalog_c_summary.json`: amp 0.004423, dir (292.95°,12.02°), 0.408σ→0.41, p=0.308→0.31, shuffle-null 0.579→0.58/rank-p 0.26 — all match.
- **GZ1-human-only null** — `gz1only_fullN_dipole_result.json`: z=−0.539/−0.551, N=46,017, CW frac 0.4836, amp 0.0546 — match.
- **Monopole-mask leakage** — `monopole_mask_null_results.json`: 99.322%, z=+1.69, hemisphere z=+4.42, all sub-values — match.
- **GZ1 confusion matrix** → 3-class acc 0.5871, chirality 0.6991, CW 67.4%/CCW 72.4% — all derive exactly from the table.
- **WLS/block-bootstrap P2**: (0.00455−0.017)/0.00163 = −7.64 → −7.6 — match; tension factor 1.7/0.455=3.7 to 4.0/0.455=8.8 — match.

The PDF is freshly recompiled (Jul 11 07:52, after the .tex). Below is my referee report.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES**

1. **[MINOR] Presentation density in Sec. IV.D (`chirality_catalog_paper.tex:1026`).** The "Quantitative forward model of the residual amplitude" is a single ~700-word paragraph that restates the *same* a-fortiori bound (unmodelled ~47% residual ⇒ A_p=0.32% < A_50=0.75% < A_95, so it cannot affect the exclusion) at least three times ("Bottom line, stated first…", "Statistical upper limit…", "In summary…"). Combined with the abstract (`:629`), the decision tree (`:724`), Table I callout (`:825`), and Table V reader's note (`:984`) all re-litigating "these σ are not inter-comparable," the manuscript over-hedges. A PRD referee would ask to consolidate each caveat to one authoritative statement. Readability revision, not a science error.

2. **[MINOR] The headline falsification threshold A_95 is only coarsely bracketed (`:631`, `:1091`).** The paper leads with A_95∈(1.0%,1.5%] as *the* real-space falsification boundary, but this rests on a 0.5%-spaced injection grid with only N_MC,inj=100 per amplitude, and tightening is deferred "to future work" (`:1091`). Because this bracketed number is the quantitative falsification criterion the abstract advertises, and the computation is cheap (observed-label-field MC, no GPU/retrain), a real referee would reasonably request a finer grid + larger ensemble to pin A_95 rather than leave a factor-1.5 uncertainty on the load-bearing threshold. This is a genuine do-now, not a truly-blocked item.

3. **[MINOR] The z≈−7.6 magnitude depends entirely on interpreting Shamir's 1.7% as an asymmetry, without a citation-to-equation (`:625`, `:1412`).** The primary exclusion statistic P2 hinges on A_ref=0.017 in A_p units, justified by the assertion that Shamir quotes (N_CW−N_CCW)/(N_CW+N_CCW). The paper adopts the *conservative* (smaller-|z|) reading and states the convention, which is defensible — but the whole exclusion magnitude flips (to ≈−18) under the alternative f_CW-deviation reading, so a referee would want the specific Shamir equation/quantity cited to nail the convention rather than an inline assertion.

4. **[MINOR] Co-labeling P2 as "primary" while its selection function is unpropagated (`:716`, `:931`).** The block-bootstrap WLS (P2) runs on the full unthresholded Catalog C (N=3,201,160), and its p_eq>0.6 science-sample selection is explicitly *not* carried into the block-bootstrap covariance, whereas P1 (the real-space dipole) is on the HC subsample. Presenting the two as co-equal "primary" estimators is slightly awkward given they act on different samples; honestly disclosed, but a referee would ask for one sentence reconciling why the clean-dipole disfavor is meaningful on a sample whose selection isn't in its error model.

5. **[MINOR] Archival DOI still pending (`:1486`, `:1491`).** Zenodo DOI + frozen commit hash are "to be inserted at submission." Standard, but must be minted before publication; the current citable handle is only the HuggingFace release tag `v2026.04`.

*(Housekeeping note, outside the science: the highest served PDF mirror under `site/public/papers/` is ~v1.0.190–200, while source is v1.0.236. Since the context note states this is a no-content-change restamp, the served content is scientifically identical — this is a directive-G mirroring lag, not a manuscript defect.)*

**(3)** Yes — the central claim (a null chirality dipole at sub-percent sensitivity in an 8.5M-galaxy catalog, with prior "detections" attributable to a quantified monopole-mask leakage channel plus classifier bias) is well-supported: every headline number reproduces against the committed artifacts, the null survives a fully model-independent GZ1-human-label cross-check, and the two primary estimators plus the eight-anchor systematic battery consistently disfavor a clean ≥1.7% dipole while honestly bounding the one unresolved (~47%) residual below the recovery threshold.
