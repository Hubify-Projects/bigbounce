# INT Codex-subscription Review — P1B v1B.0.111 — gpt-5.6-sol (high)
paper: P1B  version: v1B.0.111  tex: arxiv/paper1b_mcmc_companion.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=f9d8399198538e6b22b51d52ce44b50b3e077b1f3f2343aeb4cb0ad905d19503  prompt_sha256=4df106aaf50ad2c1982e613bd14520d59a280eb0ed3124505e47449487b5b4d2
provenance: commit=59517e43ab185d3e185681fd61065f99a11d1616  source_sha256=7a80e81038a10ef169dee4b0ef6f27fedc2f6e1f7d4a0b0e11a7a53b4e999898
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/defc8cafd0f71688838fd9bae8ee7a5f9e9d11b94f01a58b2787007bb5139533.pdf  sha256=defc8cafd0f71688838fd9bae8ee7a5f9e9d11b94f01a58b2787007bb5139533  pages=20
venue: Journal of Cosmology and Astroparticle Physics  article_type: Research article / computational methods  profile: JCAP-COMPUTATIONAL
source_tree: clean detached sparse tree at 59517e43ab185d3e185681fd61065f99a11d1616 (scope=arxiv)
UTC: 2026-07-16T13:39:30Z
context-note: Residual confirmation of the corrected physical CAMB 1.6.6 500-MC NaMaster suite and v1B.0.111 release. Distinguish newly introduced or still-valid manuscript defects from standing venue/scope opinions and explicitly disclosed limitations. OpenAI API and Anthropic are forbidden.

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] BBN implementation provenance (`arxiv/paper1b_mcmc_companion.tex:1779`): the manuscript states that the chains used a PArthENoPE-derived CAMB predictor and that all four YAML files explicitly declared `bbn_predictor: 'PArthENoPE'`. The committed execution receipt and frozen configuration instead show CAMB 1.6.5 using its default PRIMAT table; the reproduction YAMLs explicitly pin `PRIMAT_Yp_DH_ErrorMC_2021.dat`, while the quoted `PArthENoPE` value is not a valid CAMB table name. The methods and reproducibility statements must describe the configuration actually executed.
2. [MINOR] NaMaster Monte Carlo estimator description (`arxiv/paper1b_mcmc_companion.tex:2229`): the reported “500-MC sample mean of \(\widehat\beta\)” is obtained by fitting the mean bandpowers, whereas the uncertainty is the dispersion of estimates fitted realization by realization. Recomputing the latter from the committed bandpowers gives a mean \(0.269914^\circ\) and signed bias \(-8.6\times10^{-5}\) degrees for the \(0.270^\circ\) injection, not an identically zero bias. The result remains fully consistent with zero, but the estimator and rounding must be stated accurately.
3. [MINOR] Mischaracterized angular prior (`arxiv/paper1b_mcmc_companion.tex:1499`): a prior uniform in \(\cos\theta_i\) has density proportional to \(\sin\theta_i\) and median \(\theta_i=\pi/2\), not a midpoint near \(0.5\). The table contradicts the correct discussion later in the manuscript and should be corrected.

(3) Yes—the central claim is supported by the committed artifacts and independent recomputation, although the BBN provenance error must be corrected.