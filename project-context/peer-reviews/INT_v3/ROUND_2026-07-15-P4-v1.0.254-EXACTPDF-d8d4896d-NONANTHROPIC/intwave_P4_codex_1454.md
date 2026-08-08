# INT Codex-subscription Review — P4 v1.0.254 — gpt-5.6-sol (high)
paper: P4  version: v1.0.254  tex: pipelines/p2_chirality/chirality_catalog_paper.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=5f80e793f0257a6a7e7bd5cb2935ab7fb453eccec7102d7897c0186a78b6d4c6  prompt_sha256=8b3dbc050cca280078cf2414947d19010f60c6d98c85c69a15b6b302306096a4
provenance: commit=96c3a97eaa33a543420c2e26702fb9e279b87461  source_sha256=3b5d8a6fa1deec96c85c744a7bc2091c3d897e312d8b20c12ed02bcb118f62db
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/d8d4896d651f172a9fa407951cea12d96ac79e796ff0a88dad2dc2c7fd6533dd.pdf  sha256=d8d4896d651f172a9fa407951cea12d96ac79e796ff0a88dad2dc2c7fd6533dd  pages=29
venue: The Astrophysical Journal Supplement Series  article_type: Catalog + methods article  profile: APJS-CATALOG-METHODS
source_tree: clean detached sparse tree at 96c3a97eaa33a543420c2e26702fb9e279b87461 (scope=pipelines/p2_chirality)
UTC: 2026-07-15T21:54:52Z
context-note: Exact v1.0.254 post-publication confirmation. Assess the sole released Catalog C scope, semantic validator, corrected source-count disclosure, and immutable dataset/model cards. Do not treat standing disclosed training-realization, spatial-transfer/joint-covariance, metadata, DOI, or human-review gates as already closed.

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] The claimed independently runnable semantic validator is not portable as published (`pipelines/p2_chirality/chirality_catalog_paper.tex:1650`): the bootstrap downloads only the validator and schema into the pinned-source tree (`pipelines/p2_chirality/apjs_release_v1.0.253_semantic_contract/validate_p4_catalog_c_semantics_v1_0_253.py:84`), but the pinned validator imports `reproduce_p4_primary_null_v1_0_244` at module load (`pipelines/p2_chirality/build_apjs_release_v1_0_244.py:29`), while that dependency is downloaded into a separate release directory; a clean execution therefore fails before validation.
2. [MAJOR] The semantic validator does not prove the claim that the quarantine contains every unsafe row (`pipelines/p2_chirality/chirality_catalog_paper.tex:948`): it checks only quarantine row totals, reason codes, and `do_not_use_for_science` aggregates (`pipelines/p2_chirality/build_apjs_release_v1_0_244.py:302`), without verifying that quarantine object IDs uniquely and exactly equal the safe catalog’s `raw_flip_qc_unsafe=True` IDs or that per-row HC flags agree.
3. [MAJOR] The immutable “current” model card cited in Data Availability (`pipelines/p2_chirality/chirality_catalog_paper.tex:1651`) remains scientifically inconsistent with the release: it claims per-class Platt calibration and calibrated residuals (`pipelines/p2_chirality/HF_MODEL_README.md:49`) although the manuscript declares Catalog B historical and Catalog C scores uncalibrated (`pipelines/p2_chirality/chirality_catalog_paper.tex:913`), while production code applies raw softmax followed directly by flip averaging (`pipelines/p2_chirality/run_eq_dataloader.py:145`).
4. [MAJOR] Classifier provenance remains insufficient for an ApJS methods product (`pipelines/p2_chirality/chirality_catalog_paper.tex:789`): the 26,616/26,626-row conflict, 93.6878%/92.10% validation conflict, missing object/split manifest, missing random states, and unknown GZ1 training overlap prevent independent reconstruction or validation of the model that generated all released labels.
5. [MAJOR] The manuscript overstates bias control as “definitive” (`pipelines/p2_chirality/chirality_catalog_paper.tex:1485`) despite explicitly lacking a spatially resolved confusion model and uncertainty propagation (`pipelines/p2_chirality/chirality_catalog_paper.tex:1338`) and a joint real-space/harmonic/nuisance covariance (`pipelines/p2_chirality/chirality_catalog_paper.tex:1368`); claims must remain limited to structural flip-equivariance and the observed-label statistic.
6. [MAJOR] The released catalog lacks full-catalog redshift, imaging-leg, depth, seeing, and PSF metadata (`pipelines/p2_chirality/chirality_catalog_paper.tex:1650`), preventing users from reproducing the survey-selection and spatial-systematics analyses central to the methods article; an executable metadata sidecar or substantially narrower catalog-utility claim is required.
7. [MINOR] The corrected source-count disclosure says the 35 absent rows have unknown identities and reasons (`pipelines/p2_chirality/chirality_catalog_paper.tex:944`), but Figure 3 still describes the 8,474,531 rows as retained “after image-quality QA” (`pipelines/p2_chirality/chirality_catalog_paper.tex:953`), reintroducing an unsupported exclusion explanation.
8. [MINOR] The manuscript/source/figure archive and DOI remain prospective placeholders rather than an immutable published-version record (`pipelines/p2_chirality/chirality_catalog_paper.tex:1644`); these identifiers must be supplied before final acceptance.

(3) Yes—the narrowly defined Catalog C observed-label null is supported by the retained array and independently recomputes to \(z=0.705317\) and \(p=0.224678\), but no physical chirality or primordial-parity bound is supported.