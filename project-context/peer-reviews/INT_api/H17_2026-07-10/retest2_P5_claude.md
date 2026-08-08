All arithmetic reconciles; the labeling contradiction is confirmed (L4330 and L2886–87 still call the *demoted* +0.0007 the "primary" while the paper promoted +0.0018 as primary). I now have what I need for a complete referee report.

---

## REFEREE REPORT — Paper P5, "Redshift-Space Environmental Dependence of Spiral Chirality: A DESIVAST Three-Algorithm Void Null Test" (v0.1.116)

### (1) VERDICT: **MINOR REVISIONS**

The paper is a carefully-bounded null result. Every headline statistic I checked reconciles from the tabulated integer counts (primary Δf_CW=+0.0018 at z=+0.78; three-algorithm table; T-Web per-class σ; χ²=3.55→p=0.31; the ≈0.9 pp quadrature envelope; the 39% Clopper–Pearson bound). The systematics budgeting, RSD caveats, and post-hoc-primary disclosures are unusually thorough. The remaining items are consistency/clarification issues and the (disclosed) companion-paper dependency — none require new analysis that changes the null.

### (2) ISSUES

1. **[MAJOR] Stale "primary" label contradicts the promoted primary estimand.** The paper promotes the *footprint-restricted* contrast Δf_CW=**+0.0018** (n_nonvoid=253,276) to primary and demotes +0.0007 to a sensitivity check (§sec:desivast_anchored_void L3025–27; abstract L736; Conclusions L4680). But two locations still call the demoted number the primary: `p5_desi_chirality.tex:4330` ("the primary Δf_CW = +0.0007 is therefore insensitive to this residual") and `:2886–2887` ("the primary P5 environment-independence claim, anchored on the DESIVAST Δf_CW≈0.0007 null at n=56,981"). Not a science error (both are nulls agreeing to 0.11 pp), but a reader-facing contradiction on the headline estimand the paper's entire framing rests on. Fix the two residual labels.

2. **[MAJOR] Essential label input is from an unpublished companion (Paper IV).** The per-galaxy CW/CCW `class_eq` labels — the sole input the environmental conclusion depends on — come from a concurrently-posted, not-yet-refereed companion. The paper itself makes acceptance "strictly conditional" on Paper IV (`:4500–4506`). This is handled about as well as possible (public CC-BY labels, self-contained Appendix A methodology reproduction, algebraic monopole-invariance of the two-sample contrast, model-free GZ1-human-vote cross-check at z=−0.54σ), so it is an editorial/citation-timing gate rather than a scientific defect — but it must be resolved via coordinated co-review before acceptance, and I flag it as the genuine gating condition.

3. **[MINOR] The newly-integrated confusion matrix does not measure the stratum that matters.** The GZ1-overlap stratified confusion matrix (`gz1_stratified_confusion.json` [A31]) is verified and matches every cited number (asymmetry +0.0001 [−0.005,+0.006]; BASS+MzLS +0.0042; DECaLS −0.0020; hi-conf −0.0019; accuracy 0.912→0.961). But it demonstrates parity-symmetric errors only across *imaging-leg* and *confidence* strata — not the *void/non-void* axis, which is precisely the axis this paper constrains. The paper is honest about this (`app:paper4_methods` L4874–4885), but the "first direct empirical support for the 2a−1 de-attenuation" should be stated more explicitly as support on *adjacent* strata that does not close the environment-differential-relabeling concern; it is suggestive, not dispositive.

4. **[MINOR] Accuracy figure used for de-attenuation is not reconciled with the confusion matrix's own accuracy.** The de-attenuation factor 2a−1=0.398 uses a=0.6991 (`app:paper4_methods` L4842; Discussion L4425), yet the same appendix's confusion matrix measures accuracy **0.912** on the confident-spiral overlap (0.961 at confidence>0.6). Using the conservative 0.699 for the *magnitude* is fine (it yields a weaker, more conservative physical bound), but drawing the *symmetry* demonstration from a 0.912-accuracy sample while applying the attenuation at a=0.699 is a scope mismatch. Add one sentence reconciling the two accuracies (confident-spiral restriction vs. full floor) and stating why symmetry at 0.912 is taken to transfer to the 0.699 regime.

5. **[MINOR] Imprecise table cross-reference.** The Bonferroni-5 family headline "|z_Δ|≤1.25" is cited to `Table~\ref{tab:desivast_three_algo}` (abstract L724/745; §primary_path L1687), but the value 1.25 comes from the GALZONE V2-REVOLVER row, which lives in the catalog-native table, not `tab:desivast_three_algo` (whose max is correctly |z|=1.12). Repoint the citation to the Bonferroni-5 family / catalog-native section.

### (3) Central-claim assessment

The central claim — that spiral chirality shows no void/non-void environment dependence in DESI DR1, presented as a bounded upper limit (≈0.9 pp classifier-label, ≈2.26 pp de-attenuated physical) rather than a positive detection of independence — **is supported** by the data as analyzed, contingent on Paper IV's coordinated review and the minor consistency fixes above.

Best Next Steps
1. Fix the two stale "primary = +0.0007" labels (`:4330`, `:2886–2887`) to the promoted +0.0018 footprint-restricted estimand.
2. Add the accuracy-reconciliation sentence (0.912 vs 0.699) and sharpen the confusion-matrix framing to "symmetry on adjacent, not the void, stratum."
3. Repoint the |z_Δ|≤1.25 cross-reference to the catalog-native/Bonferroni-5 table.

Say `continue` and I will take the next best scoped step.
