# INT Codex-subscription Review — P4 v1.0.256 — gpt-5.6-sol (high)
paper: P4  version: v1.0.256  tex: pipelines/p2_chirality/chirality_catalog_paper.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=cbb8b476655dce3a449a8d24a484b95b3f3db3c0e8bd2c7a934d1a3da72de4a9  prompt_sha256=b577a1c92d37284b62581735bada101e7217e06466e6c2bbfd1facfbc5422ce2
provenance: commit=0197358b17570309ba217070e43b56b55e840e23  source_sha256=687adcb37fff45febc0e6ddc4a53d61840732a3e095b931411ea36169f4944d8
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/6dfccf7c26d698599c3512bd91f0f73f714f967604f42f73aeaf4e9a59573110.pdf  sha256=6dfccf7c26d698599c3512bd91f0f73f714f967604f42f73aeaf4e9a59573110  pages=29
venue: The Astrophysical Journal Supplement Series  article_type: Catalog + methods article  profile: APJS-CATALOG-METHODS
source_tree: clean detached sparse tree at 0197358b17570309ba217070e43b56b55e840e23 (scope=pipelines/p2_chirality)
UTC: 2026-07-16T06:27:21Z
context-note: Exact-PDF confirmation after truth-audited v1.0.255 closure

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] Classifier validation and training provenance — pipelines/p2_chirality/chirality_catalog_paper.tex:797, pipelines/p2_chirality/chirality_catalog_paper.tex:1460, pipelines/p2_chirality/chirality_catalog_paper.tex:1511. The training membership, split, random state, and exact realization are unrecoverable; committed records conflict, and the only human-label validation may contain training objects. Consequently, the reported 58.7% three-class and 69.91% chirality agreement do not provide an independent estimate of catalog purity, completeness, or transfer performance. An ApJS catalog requires an object-disjoint labeled validation set or a reproducibly retrained model with an immutable split manifest.
2. [MAJOR] Inadequate released selection-function metadata — pipelines/p2_chirality/chirality_catalog_paper.tex:954, pipelines/p2_chirality/chirality_catalog_paper.tex:1340, pipelines/p2_chirality/chirality_catalog_paper.tex:1658. The release omits full-catalog imaging leg, depth, seeing, PSF, and redshift despite documented spatially varying confusion, a 9.5-sigma label monopole, and significant harmonic structure. Without these columns and their propagation into the primary estimator, users cannot reproduce the relevant systematic conditioning or determine where the catalog is reliable.
3. [MAJOR] Inconsistent imaging-leg validation — pipelines/p2_chirality/chirality_catalog_paper.tex:762, pipelines/p2_chirality/chirality_catalog_paper.tex:1320, pipelines/p2_chirality/chirality_catalog_paper.tex:1527. DR8 is described as three campaigns, but the GZ1 spatial-confusion analysis uses only declination-defined BASS+MzLS and DECaLS strata, folding the DES region into the latter while claiming consistency “in every leg.” The confusion analysis must use actual three-leg membership and report DES separately before it can support that statement.
4. [MINOR] Causal overstatement of the raw-versus-equivariant comparison — pipelines/p2_chirality/chirality_catalog_paper.tex:1092. The caption says the comparison demonstrates that equivariant post-processing prevents spurious dipoles, although the manuscript acknowledges that Catalogs A and C came from different inference passes and memberships and that their quoted dipoles use different null conventions; the comparison does not isolate TTA causally.
5. [MINOR] Archival reproducibility remains provisional — pipelines/p2_chirality/chirality_catalog_paper.tex:1652. Analysis links target mutable `main`, while the exact code commit, immutable manuscript tag, and Zenodo DOI are deferred until submission; these identifiers should be supplied before acceptance.

(3) Yes—the narrowly stated claim that the selected observed-label sample is null-consistent under the specified fixed-occupancy randomization is supported, but it is not yet a validated true-chirality or physical-isotropy result.