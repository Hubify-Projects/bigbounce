# INT Codex-subscription Review — P4 v1.0.258 — gpt-5.6-sol (high)
paper: P4  version: v1.0.258  tex: pipelines/p2_chirality/chirality_catalog_paper.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=46cd83716df36d7d8dfc372481ecf46ea31a274cd49c717706f13f9ea7b2e553  prompt_sha256=2bc0e765e76aa1f13f30025527583affc5c4377cdf6740204d79f557f84c01d8
provenance: commit=68d7e2541aa48de03c15133f7aa9f3b8e1cce5ac  source_sha256=97101d1c31465bbb1496823bd740fddde5c7056b8111b4e133f9e9a9c9fe603b
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/e9b69665efdf757de69f27a0474d30ac4bc48bc7559424e077f41c7bcacbe061.pdf  sha256=e9b69665efdf757de69f27a0474d30ac4bc48bc7559424e077f41c7bcacbe061  pages=25
venue: The Astrophysical Journal Supplement Series  article_type: Catalog + methods article  profile: APJS-CATALOG-METHODS
source_tree: clean detached sparse tree at 68d7e2541aa48de03c15133f7aa9f3b8e1cce5ac (scope=pipelines/p2_chirality)
UTC: 2026-07-16T08:28:58Z
context-note: Residual confirmation after strict-sample and exact-FSC-support computational closure. Identify only evidence-backed remaining defects; distinguish disclosed limitations and historical superseded statistics from current claims.

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] The “Primary HC estimator audit” table reports the superseded unsafe-inclusive sample, null-array hash, and statistics—949,584/947,326, \(z=0.705317\), \(p=0.224678\)—despite the manuscript declaring that result replaced by the strict 890,069/887,472 analysis. Independent recomputation of the strict array gives \(z=0.634651\), \(p=0.237676\), and SHA-256 `3a03ca4b...ce7d`, not the table’s `f6360f4b...152c0` (`pipelines/p2_chirality/chirality_catalog_paper.tex:1063`).
2. [MAJOR] The public release identified as authoritative does not reproduce the manuscript’s current primary result: its schema, dataset card, retained array, and reproducer still designate the unsafe-inclusive \(N=949{,}584\), \(z=0.705317\), \(p=0.224678\) analysis as primary. This contradicts the claim that the commit-pinned release contains the exact release-safe primary null; the strict array exists only in the later repository closure ledger (`pipelines/p2_chirality/chirality_catalog_paper.tex:1353`; `pipelines/p2_chirality/CATALOG_SCHEMA.md:69`; `pipelines/p2_chirality/HF_DATASET_README.md:30`).
3. [MINOR] The exact-support binomial-monopole table prints null moments inconsistent with both its reported \(z\) values and the committed null array. Recalculation gives \((0.60414\pm0.91749)\times10^{-6}\) for 500 draws and \((0.57796\pm0.89263)\times10^{-6}\) for 10,000 draws, not \((5.2420\pm0.9257)\times10^{-6}\) and \((5.1242\pm0.2618)\times10^{-6}\) (`pipelines/p2_chirality/chirality_catalog_paper.tex:1132`).
4. [MINOR] The primary-estimator-summary caption describes row (iv) as using the \(N_{\rm all}\ge1\) footprint and two null families, whereas the row and exact-support artifact use a single fixed-occupancy null on the apodized 24,087-pixel FSC base mask (`pipelines/p2_chirality/chirality_catalog_paper.tex:859`).

(3) Yes—the central, strictly quality-controlled observed-label null is supported by the committed strict-sample array, but its manuscript table and cited public release are not yet synchronized with it.