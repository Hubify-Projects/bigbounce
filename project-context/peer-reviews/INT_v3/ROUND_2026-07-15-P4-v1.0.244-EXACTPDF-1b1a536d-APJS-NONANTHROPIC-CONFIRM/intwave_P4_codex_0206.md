# INT Codex-subscription Review — P4 v1.0.244 — gpt-5.6-sol (high)
paper: P4  version: v1.0.244  tex: pipelines/p2_chirality/chirality_catalog_paper.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=22e2c48e2e6b295766d3d70786b0bac7132abccc0af24f1fe507e5c53346b829  prompt_sha256=6cb86b57e680d5f534f82e078e533425eb83aa6460dd83c818ff247d104a3fe4
provenance: commit=6534a6e8fc57419f1674df4ee5dd13adad19854b  source_sha256=2ceb563b354ff2c4547381ce337fc566c713b18107d60a99150f206c4eafd4a0
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/1b1a536dfbd7d07ea4958304d6694582ce3b5ec7d6ce16b08b5d17fdefc15669.pdf  sha256=1b1a536dfbd7d07ea4958304d6694582ce3b5ec7d6ce16b08b5d17fdefc15669  pages=26
venue: The Astrophysical Journal Supplement Series  article_type: Catalog + methods article  profile: APJS-CATALOG-METHODS
source_tree: clean detached sparse tree at 6534a6e8fc57419f1674df4ee5dd13adad19854b (scope=pipelines/p2_chirality)
UTC: 2026-07-15T09:06:44Z
context-note: Exact v1.0.244 bounded ApJS catalog-and-methods confirmation. Judge this exact artifact only; do not inherit v1.0.243 verdicts. The narrow claim is the observed-label HC real-space null, not a physical parity bound.

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] Primary-null calibration (pipelines/p2_chirality/chirality_catalog_paper.tex:773, pipelines/p2_chirality/chirality_catalog_paper.tex:1003; pipelines/p2_chirality/run_dipole_catalog_c.py:213): the primary permutation shuffles heteroscedastic pixel asymmetries among sky positions even though their variance depends strongly on spatially varying pixel occupancy. Exchangeability is therefore not established. Promote an occupancy-preserving galaxy-label randomization to the primary null, retain its exact draw array and generator, and recompute the reported significance.
2. [MAJOR] Training-set provenance (pipelines/p2_chirality/chirality_catalog_paper.tex:760, pipelines/p2_chirality/chirality_catalog_paper.tex:1402; pipelines/p2_chirality/train_v2_fast.py:119): the stated sources sum to 25,790 objects, yet the manuscript attributes the additional 826 objects in the 26,616-object pool to flip augmentation. The production code instead adds CE-ResNet-selected non-spirals before splitting; flips are generated on-the-fly for the consistency loss and do not add dataset rows (pipelines/p2_chirality/train_v2_fast.py:207). The source counts, CE-derived fraction, split description, and Table training provenance must be corrected; the unseeded split/training operations also prevent exact training reproduction.
3. [MAJOR] Catalog-release availability (pipelines/p2_chirality/chirality_catalog_paper.tex:698, pipelines/p2_chirality/chirality_catalog_paper.tex:1614): the exact v1.0.244 science-facing catalog, quarantine Parquet, manifest, and validation receipt are absent from the bound repository and, as acknowledged at pipelines/p2_chirality/chirality_catalog_paper.tex:1619, remain local rather than content-addressed and public. An ApJS catalog article requires the exact reviewed products, immutable checksums, and archival identifier to be available for independent inspection.
4. [MINOR] Calibration lower bounds (pipelines/p2_chirality/chirality_catalog_paper.tex:1473): the claimed ECE lower bounds combine the catalog-wide mean confidence with accuracies measured on a GZ1-selected subset. Jensen’s inequality requires confidence and correctness averages over the same objects; recompute the mean confidence and ECE on the exact GZ1 evaluation sample.
5. [MINOR] “Disjoint” GZ1 validation (pipelines/p2_chirality/chirality_catalog_paper.tex:760, pipelines/p2_chirality/chirality_catalog_paper.tex:1457): the committed artifact reports 69.9108% on 117,205 chirality-evaluable pairs within the full 240,919-object match, not a recomputed metric after excluding the 6,637 training objects. Subtracting counts to obtain 234,282 does not establish a disjoint evaluation; provide the object-level exclusion and recomputed confusion matrix or remove the independence claim.

(3) Yes—the central claim is supported narrowly as an observed-label null, with the retained 10,000-draw array reproducing \(z=0.5491202\) and \(p=0.2651735\), but it supports no physical parity bound.