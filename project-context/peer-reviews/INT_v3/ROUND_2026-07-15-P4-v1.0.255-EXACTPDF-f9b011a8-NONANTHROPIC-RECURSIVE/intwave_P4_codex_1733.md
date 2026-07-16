# INT Codex-subscription Review — P4 v1.0.255 — gpt-5.6-sol (high)
paper: P4  version: v1.0.255  tex: pipelines/p2_chirality/chirality_catalog_paper.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=c1a6255635a80b23a057a7bfb832394682e118db5f20d9f60bc91250a6b1361f  prompt_sha256=b493fe732ca3b5d33860c91f60aa385b7d015415a7e024693721134678487ec8
provenance: commit=770121acc77f9f40b730863d2bfdbddfdf62c3f8  source_sha256=93ddf83c817c69e4d5eb89cb16b91b4e6456c6cb3cf1e6a1b86f16a5cd42b388
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/f9b011a84351781b0b0e48e02e811a60ba1666296fa1f80413c918fe131c7dce.pdf  sha256=f9b011a84351781b0b0e48e02e811a60ba1666296fa1f80413c918fe131c7dce  pages=29
venue: The Astrophysical Journal Supplement Series  article_type: Catalog + methods article  profile: APJS-CATALOG-METHODS
source_tree: clean detached sparse tree at 770121acc77f9f40b730863d2bfdbddfdf62c3f8 (scope=pipelines/p2_chirality)
UTC: 2026-07-16T00:34:03Z

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] The catalog-generation classifier lacks reproducible, independent validation (`pipelines/p2_chirality/chirality_catalog_paper.tex:794`, `:1457`, `:1508`). Training totals and validation accuracies conflict, object/split manifests and random states are missing, most labels are CE-ResNet-derived, and the GZ1 evaluation may include training objects; consequently, catalog purity, completeness, and the meaning of “high confidence” are not established to ApJS catalog standards.

2. [MAJOR] The bias-hardening results are not supported by one checkpoint-bound artifact (`pipelines/p2_chirality/chirality_catalog_paper.tex:1490`). Table values of 94.4% rotation stability, 91.2% perturbation robustness, and \(<0.4\%\) hemispheric difference conflict with committed results of 89.8%, 84%, and 3.6%, respectively, while the scripts also use different rotation grids and test definitions.

3. [MAJOR] No byte-complete, submission-frozen v1.0.255 reproducibility package exists (`pipelines/p2_chirality/chirality_catalog_paper.tex:1649`). Artifact links target mutable `main`, the DOI/tag/commit archive remains promised for later, the current submission tarball contains v1.0.252 source, and seven referenced figure files are absent from the clean source tree; the manuscript of record therefore cannot be rebuilt from the current committed submission package.

4. [MAJOR] Machine-readable records contradict the manuscript’s primary provenance (`pipelines/p2_chirality/chirality_catalog_paper.tex:1038`). The retained fixed-occupancy array independently reproduces \(z=0.705317\) and \(p=0.224678\), but `outputs/dipole/catalog_c_summary.json` still labels a pixel-permutation result \(z=0.549120,\ p=0.265173\) as the “single primary,” and `catalog_c_post_tta_dipole_summary.json` calls that stale record canonical.

5. [MAJOR] Essential catalog systematics metadata remain unavailable (`pipelines/p2_chirality/chirality_catalog_paper.tex:1344`, `:1655`). Full-catalog imaging leg, depth, seeing, PSF, and redshift fields—and their covariance propagation—are missing, preventing users from independently reproducing or testing the spatial-selection and classifier-systematics interpretation central to this catalog article.

6. [MAJOR] The claimed causal TTA demonstration is uncontrolled (`pipelines/p2_chirality/chirality_catalog_paper.tex:1090`, `:1215`, `:1411`). The raw and equivariant products have different spiral memberships, originate from different inference passes, and use different null conventions; 249,066 raw/equivariant pass mismatches are documented. The comparison illustrates a pipeline change but cannot isolate TTA as the cause of the \(2.31\sigma\rightarrow0.71\sigma\) reduction.

7. [MINOR] The \(D_4\) validation overstates its evidence (`pipelines/p2_chirality/chirality_catalog_paper.tex:913`, `:1487`). One sample is a rate-limit-truncated cached subset with different cutout preprocessing, and no overlap or uncertainty analysis shows that the \(-1.35\%\) versus \(+2.11\%\) sign reversal “confirms” sample noise.

8. [MINOR] The look-elsewhere probability is mischaracterized (`pipelines/p2_chirality/chirality_catalog_paper.tex:821`, `:1555`). Zero exceedances in 10,000 simulations gives the add-one estimate \(1/10001\), not an upper bound \(p_{\rm LEE}\le10^{-4}\); the 95% binomial upper limit is approximately \(3.0\times10^{-4}\).

9. [MINOR] The NGP/SGP null is described incorrectly (`pipelines/p2_chirality/chirality_catalog_paper.tex:1552`). Its generator uses independent binomial draws at \(p=0.5\), whereas the primary null preserves the global CW count through multivariate-hypergeometric allocation.

10. [MINOR] “Spatially uniform classifier artifact” is too strong (`pipelines/p2_chirality/chirality_catalog_paper.tex:1025`). Committed artifacts contain an RA slab at \(z=-3.20\), an equal-area extremum \(|z|=2.89\), and significant low-\(\ell\) structure; the supported statement is bounded sub-percent variation with no detected dipole under the declared primary estimator.

(3) Yes—the narrow claim that the selected observed hard-label field is consistent with the declared fixed-occupancy randomization null is supported, but it does not establish a physical-spin or primordial-parity null.