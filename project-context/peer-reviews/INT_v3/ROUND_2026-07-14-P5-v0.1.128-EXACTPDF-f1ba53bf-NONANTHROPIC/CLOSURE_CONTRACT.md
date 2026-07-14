# P5 v0.1.128 bounded closure contract

This contract is evidence-driven and intentionally unimplemented in this review lane. The paper must not be called publication-ready until the P0 gates close and a fresh exact-PDF review returns only minor revisions or better across the required board.

## P0 — publication gates

1. **Selection-function control:** construct the primary control with the official DESIVAST/BGS mask and DESI randoms, or fit a pre-specified matched/IPW/logistic control spanning redshift, angular position/imaging leg, magnitude/size/morphology, and classifier confidence. Report the adjusted void coefficient/contrast with angular/redshift block- or void-cluster-robust uncertainty. If this compute is not performed, narrow every “controlled” / “same-selection-function” claim to the exact hole-union-support descriptive estimand.
2. **Row-level covariance provenance:** archive the exact bootstrap input table with stable object ID, position/redshift, chirality label, void/control flag, and maximal-void region ID; record its SHA-256; pin driver, table, and result to an immutable repository tag and DOI. Re-run the 20,000-draw bootstrap from that archive. If exact row-level provenance cannot be frozen, remove the precise cluster-SE claim from the abstract.
3. **Companion and immutable release:** replace the Paper-IV placeholder arXiv ID, create and verify the claimed `v0.1.128-2026-07-14`-equivalent immutable release/tag, and replace the pending Zenodo language with the actual archived DOI or an explicitly submission-time-valid alternative. The current tag does not exist locally or on `origin` as audited.

## P1 — exact reader-visible corrections

4. Define one coherent inferential hierarchy: distinguish the exact 57,081/253,276 designated contrast from the 56,981/621,964 `k=20` family member, and make Tables IV, X, XIII, XIV, abstract, and conclusions use unambiguous names. The counts are not contradictory; the family/primary naming is.
5. Replace the Table XI 0.44 pp counting entry with the exact primary counting uncertainty (`2SE = 0.4633` pp; normal 95% half-width `0.4540` pp), recompute the heterogeneous quadrature (`≈0.96` pp), and retain the explicit statement that it is not a CI or calibrated coverage bound.
6. Rename 0.77/0.63/0.50/1.12/0.86 pp as maximum absolute interval endpoints, not half-widths. Print the true Bonferroni half-widths separately; preserve the valid ≈1.1 pp maximum-absolute-endpoint statement.
7. Remove the claim that a 0.5 pp estimator shift “would require” >1.3× the observed membership reassignment, or support it with targeted injection/adversarial simulations demonstrating the assumed scaling.
8. Report the dark-program void/non-void residual explicitly (`Δ≈−4.71` pp, `|z|≈1.97`, nominal two-sided `p≈0.049`) and state that it is suggestive but not significant after the declared multiplicity treatment.
9. Re-render Fig. 8 without the outer 0–1 Cartesian axes and with separated labels/colorbars; reconcile the Fig. 6 top-panel caption. Re-run the 41-page visual audit.
10. Correct the conclusion’s Table XIII→Table XIV family reference; use “consistent with zero void/non-void contrast,” not “consistent with parity”; replace remaining “three independent algorithms” wording with “three definitions spanning two algorithmic families.”

## Acceptance verification

- Recompile and pass the full LaTeX/PDF audit: zero errors, zero unresolved references, zero overfull boxes, all pages inspected, links and immutable artifacts checked.
- Independently recompute the primary count null, conditional exact test, likelihood-ratio test, Bonferroni family, adjusted-control result, and archived cluster bootstrap.
- Freeze the new PDF hash before review. Run non-fallback native-PDF reviews plus an independent subscription referee. Do not advance readiness unless every finding is truth-audited and the board is ACCEPT/MINOR only.

