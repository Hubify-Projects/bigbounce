# INT Codex-subscription Review — P4 v1.0.257 — gpt-5.6-sol (high)
paper: P4  version: v1.0.257  tex: pipelines/p2_chirality/chirality_catalog_paper.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=631693ac6dd7cf3f0b4fdb43af0cbf97cc4f4307b1b960734c580160a4dcd19f  prompt_sha256=88cac9503bff12701bae4d05616b90944a0633a537dec8ab427b782a72bce780
provenance: commit=e97f0b7365267355d06e5a979738ea5d6675950f  source_sha256=34640a37bd41329c66c34b732e11ace75d23d2c5b417ce7464ea52e175a593c6
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/726acd8bacaddeec34f6180096107f1b247a3e6d5f279a3c3586afac4b0491a1.pdf  sha256=726acd8bacaddeec34f6180096107f1b247a3e6d5f279a3c3586afac4b0491a1  pages=29
venue: The Astrophysical Journal Supplement Series  article_type: Catalog + methods article  profile: APJS-CATALOG-METHODS
source_tree: clean detached sparse tree at e97f0b7365267355d06e5a979738ea5d6675950f (scope=pipelines/p2_chirality)
UTC: 2026-07-16T07:04:37Z
context-note: Exact-PDF confirmation after truth-audited v1.0.256 confirmation closure

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] The \FSC{} harmonic-support attribution is incorrect (`pipelines/p2_chirality/chirality_catalog_paper.tex:1153`). The manuscript assigns the $+3.64\sigma$, $+4.84\sigma$, apodization, and multipole diagnostics to the 24,087-pixel $N_{\rm spiral}\ge10$ support, but the linked generator uses `n_total > 0`, yielding 24,270 pixels and $f_{\rm sky}=0.493774$ (`pipelines/p2_chirality/scripts/master_decoupled_monopole_null.py:83`; `pipelines/p2_chirality/outputs/canonical_provenance/master_decoupled_monopole_null.json:10`). The committed threshold-10 calculation instead reports 24,087 pixels and $z=7.891$ under its 10,000-permutation convention (`pipelines/p2_chirality/outputs/canonical_provenance/c16_r24conf_pod_batch.json:251`). Consequently, the claimed support-audited \FSC{} synthesis and post-MASTER monopole-only conclusion at `chirality_catalog_paper.tex:1165-1180` require recomputation on the declared support.

2. [MAJOR] The primary analysis includes rows that the release labels unsafe and quarantines as `do_not_use_for_science` (`pipelines/p2_chirality/chirality_catalog_paper.tex:959`). These comprise 59,515 of 949,584 HC rows (`pipelines/p2_chirality/outputs/canonical_provenance/p4_catalog_c_semantic_validation_v1_0_255.json:46`), while the exact primary generator filters only `primary_hc` and does not exclude `raw_flip_qc_unsafe` (`pipelines/p2_chirality/generate_p4_primary_label_shuffle_v1_0_244.py:63`). The exclusion test used a different pixel-permutation null rather than the current fixed-occupancy primary null (`pipelines/p2_chirality/outputs/canonical_provenance/ext3_nfm1_hc_dipole_qc_rerun.json:1`). The release semantics and primary sample must be reconciled, with the exact primary null rerun on the 890,069-row strict sample if these rows are genuinely unsuitable for science.

3. [MAJOR] The catalog lacks an independent, reproducible validation of its classifier labels (`pipelines/p2_chirality/chirality_catalog_paper.tex:800`). The training realization, object/split membership, and random states are unrecoverable; committed records disagree on training counts and validation accuracy, and the GZ1 evaluation cannot exclude training overlap (`pipelines/p2_chirality/chirality_catalog_paper.tex:1457-1476`, `:1508`). For an ApJS catalog-and-methods article, an independently held-out, representative human-label audit—or a reproducible retraining and validation—is needed to establish catalog purity, completeness, and spatially dependent error rates.

4. [MAJOR] Data Availability is not submission-ready (`pipelines/p2_chirality/chirality_catalog_paper.tex:1650`). Supporting-artifact links target mutable `main`, while the immutable source/artifact snapshot, exact repository commit, and Zenodo DOI remain prospective placeholders; the manuscript of record must identify a frozen archive and immutable analysis-code revision.

5. [MINOR] Figure 2 states that the Catalog A-to-C asymmetry change is “dominated by” TTA (`pipelines/p2_chirality/chirality_catalog_paper.tex:898-903`), contradicting the later acknowledgment that different inference passes, memberships, and null conventions prevent causal isolation (`pipelines/p2_chirality/chirality_catalog_paper.tex:1031`, `:1099`).

6. [MINOR] The bibliography contains 23 uncited entries, beginning at `pipelines/p2_chirality/chirality_catalog_paper.tex:1726`, despite using a numbered citation scheme; these should be cited substantively or removed.

(3) Yes—the narrowly stated HC observed-label null is supported: recomputation of the retained 10,000-draw array gives mean 0.0034899420, standard deviation 0.0015696946, \(z=0.705317\), and upper-tail \(p=0.224678\), but it supports no physical chirality or primordial-parity inference.