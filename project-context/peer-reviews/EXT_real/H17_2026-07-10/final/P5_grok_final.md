Peer Review Report

Paper Summary
This manuscript presents a null test for environment dependence of spiral-galaxy chirality (CW/CCW fraction) in DESI DR1, anchored on the public DESIVAST void catalog (three algorithms + two catalog-native zone definitions). The primary estimand is the footprint-restricted void vs. non-void contrast on 57,081 DESIVAST-matched spirals (plus sensitivity checks at ~57k). Secondary paths include a full T-Web tidal-tensor classification on 14.6 M galaxies (yielding a small void bin of n=428 that is flagged as survey-shell contaminated) and various stratifications (redshift, projected density, HEALPix sky position, tracer program, within-class density). All tests are null after proper multiplicity correction (Bonferroni-5 on the primary family; label-shuffle permutation p-values). The headline result is a bounded null: |Δf_CW| ≲ 0.004 (observed classifier-label fraction) with an honest ~0.9 pp systematic envelope (quadrature of counting, membership, geometry, footprint, match-radius, and confidence terms). A de-attenuated physical-chirality bound of ~2.26 pp is quoted for model-builders, with explicit caveats on the GZ1 accuracy floor (~70 %, κ≈0.40) and the lack of an environment-stratified confusion matrix. The paper is transparent about the post-hoc primary-path designation, the garden-of-forking-paths exposure (few-dozen trials), redshift-space nature of all metrics, and the fact that the T-Web void bin is not load-bearing.

Strengths

Large, well-defined primary sample (57k void spirals) from a public, peer-reviewed DR1 VAC.
Built-in robustness via five correlated but distinct void definitions (sphere-growing + two watershed variants + two catalog-native).
Thorough multiplicity control, permutation nulls, Jeffreys intervals, and explicit disclosure of exploratory/post-hoc status.
Careful treatment of the classifier monopole (subtracted where relevant; algebraically cancels in the two-sample contrast).
Multiple orthogonal cross-checks (density quintiles, redshift, sky position, tracer-program splits, Phase-2 (R_s, λ_th) sweep) all return nulls consistent with the primary.
Honest systematic envelope and de-attenuation discussion; limitations (RSD, no real-space reconstruction, attenuated proxy) are stated clearly and not overstated.
Reproducibility artifacts and pipeline tag are referenced.

Minor Comments / Suggestions

De-attenuation section (around §I / Appendix A): The factor 2a−1 ≈ 0.40 is used to convert the ~0.9 pp observed-label bound into a ~2.26 pp physical bound. This is the correct conservative approach for model-builders, but the text could briefly note that any environment-dependent variation in the confusion matrix (not available) would add a small extra uncertainty term. A one-sentence parenthetical would suffice.
T-Web void bin emphasis: The n=428 T-Web void bin is correctly labeled “not load-bearing” and dominated by survey-shell artifacts. A short sentence reiterating that the primary result does not rely on it (and why the DESIVAST re-projection is used instead) would help readers who skim §VI.
Figure/Table captions: Some multi-panel figures (e.g., the density-quintile and HEALPix maps) are information-dense. Adding a one-line “key takeaway” sentence at the end of the caption would improve accessibility without lengthening the paper.
Minor wording: In a few places the phrase “the null holds” could be softened to “the data are consistent with the null at the quoted sensitivity” to emphasize that this is an upper bound, not a proof of exact independence. (The paper already does this in most places; a global search-replace would finish the job.)

No major methodological, statistical, or interpretive flaws were identified. The analysis is conservative, the multiplicity and post-hoc issues are properly bounded, the primary result is robust across void definitions, and the quoted bounds are honest. The manuscript is ready for publication after the minor clarifications above.

VERDICT: ACCEPT
