# INT Codex-subscription Review — P5 v0.1.135-2026-07-15 — gpt-5.6-sol (high)
paper: P5  version: v0.1.135-2026-07-15  tex: pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=10e64fe0576144c6e827bbde5c57c3a117751ee446ad7748055a23213d399aad  prompt_sha256=be8880d6fea78865f47d74311914f7e95a67b19e0489340ba8604eb7101e4631
provenance: commit=0197358b17570309ba217070e43b56b55e840e23  source_sha256=f38ead4ba602cafcd9a08a8d3865d98a1c7f533138c85754b3f109d8034b1d89
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/7223afcce95bd735ddbd0efc05745738ba699949aa8f6536271a97aca394bdc8.pdf  sha256=7223afcce95bd735ddbd0efc05745738ba699949aa8f6536271a97aca394bdc8  pages=39
venue: The Astronomical Journal  article_type: Observational research article  profile: AJ-OBSERVATIONAL
source_tree: clean detached sparse tree at 0197358b17570309ba217070e43b56b55e840e23 (scope=pipelines/p5_desi_chirality/paper)
UTC: 2026-07-16T06:27:16Z
context-note: Exact-PDF confirmation after truth-audited v0.1.134 closure

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] The focal inference is not validated under its stated specification (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:1736-1754`). It uses CR1-normal inference with only \(G=50\) clusters and \(K=78>G\); an independent refit reproduced the point estimate but found a numerically rank-77, extremely ill-conditioned bread matrix. The wild-cluster calculation instead uses a different \(K=13\) model, so it cannot validate the focal interval. Apply finite-sample inference to the unchanged focal estimator or promote a defensible low-rank specification.
2. [MAJOR] The self-contained classifier provenance is materially inconsistent with the canonical companion manuscript (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:4767-4798`; `pipelines/p2_chirality/chirality_catalog_paper.tex:797`). P5 attributes the increase from 25,790 to 26,616 training rows to flip augmentation; Paper IV identifies the additional 826 as CE-selected non-spirals and states that flips do not add rows. Paper IV also reports conflicting training records and no retained split manifest, seed, or run receipt. Because these labels define the outcome, P5 must reproduce the honest provenance limitations and complete its acknowledged final-label re-verification gate.
3. [MAJOR] The reproducibility identifiers are incorrect (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:4941-4945,5043-5059`). The claimed Hugging Face tag `v2026.04` conflicts with the committed acquisition configuration, which pins revision `1ba76bc7` and records that only `main` existed. Commit `e2e842d…` also cannot regenerate all reported results because A41/A42 were added later in `0a46753d…`; the text additionally calls v0.1.132 the current candidate although this is v0.1.135. Freeze and cite one complete immutable release.
4. [MINOR] Figure 5 contains a sign error (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:2017`): its embedded legend prints \(\sigma_{\rm pred}=-2\Delta f_{\rm CW}\sqrt N\), contradicting Eq. 2 and the plotted negative predictions.
5. [MINOR] Figure 9 mislabels its T-Web population (`pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex:4038`): the image says \(n=791{,}635\), while its displayed class counts sum to the 812,793-row environment-labeled parent.

(3) Yes—the narrowly stated catalog-specific classifier-label non-detection is supported by independent recomputation, but its focal uncertainty, label provenance, and immutable release record require correction before publication.