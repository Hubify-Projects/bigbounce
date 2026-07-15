# INT Codex-subscription Review — P1B v1B.0.108 — gpt-5.6-sol (high)
paper: P1B  version: v1B.0.108  tex: arxiv/paper1b_mcmc_companion.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=f547fa9e1f939a9f4d78f82da7ea48f5e04a20a5fa775e202cefea4bcfe141cc  prompt_sha256=7e4445b9e53799f821bb6085d69d73a2e9af3c3b296def0476e62c7e8499ceb4
provenance: commit=6534a6e8fc57419f1674df4ee5dd13adad19854b  source_sha256=d65b8150655881d852c440030fc65f1cf323152bc50a4a747412236c6767a9d4
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/a85f43f93ed7bb53e73304cd21fb0fe68ed0d6627103ccbcf970036d31d9a9fb.pdf  sha256=a85f43f93ed7bb53e73304cd21fb0fe68ed0d6627103ccbcf970036d31d9a9fb  pages=19
venue: Journal of Cosmology and Astroparticle Physics  article_type: Research article / computational methods  profile: JCAP-COMPUTATIONAL
source_tree: clean detached sparse tree at 6534a6e8fc57419f1674df4ee5dd13adad19854b (scope=arxiv)
UTC: 2026-07-15T09:06:44Z
context-note: Exact v1B.0.108 post-closure confirmation. Judge this exact artifact only. Separate scientific correctness from standalone JCAP venue fit; do not inherit v1B.0.107 verdicts.

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] Standalone JCAP venue fit is not established: the manuscript combines a standard stock-CAMB extension, a matched-model synthetic NaMaster closure test, and a single-datum ALP accommodation exercise, while explicitly conceding that they are disconnected proxy/validation studies rather than a new cosmological inference or general computational method (arxiv/paper1b_mcmc_companion.tex:1509, arxiv/paper1b_mcmc_companion.tex:1648, arxiv/paper1b_mcmc_companion.tex:2085, arxiv/paper1b_mcmc_companion.tex:2395, arxiv/paper1b_mcmc_companion.tex:2877). Scientific correctness is largely separate from this problem: a standalone JCAP Research article needs a coherent new scientific question or a demonstrably novel, broadly benchmarked method.
2. [MAJOR] The advertised spectator-ALP prior-predictive fractions are calculated over unrestricted ALP priors on a fixed ΛCDM background, without computing or imposing the manuscript’s own physical spectator condition $\Omega_a<0.01$ (arxiv/paper1b_mcmc_companion.tex:1341, arxiv/paper1b_mcmc_companion.tex:2421, arxiv/paper1b_mcmc_companion.tex:2439; reproducibility/cosmology/alp_prior_predictive.py:122). Although the caveat that 11.597% and 6.137% are unconditional fractions is accurate, these numbers are not a prior-predictive accommodation statistic for the spectator model because they include trajectories for which the assumed background may be inconsistent; a spectator-conditioned calculation or self-consistent background evolution is required.
3. [MINOR] The NaMaster recovery-grid specification is not exact: the manuscript states $\beta\in[-2^\circ,+2^\circ]$ at $0.001^\circ$ spacing, whereas the committed fitter defaults to $[-1^\circ,+1^\circ]$ with 2,001 points (arxiv/paper1b_mcmc_companion.tex:2173; reproducibility/p1_namaster_500mc/scripts/windowed_rotation.py:65). This does not change the reported injections, which I recomputed as $0.269^\circ$, $0.341^\circ$, and $-0.001^\circ$, but the reproducibility description must match the executed code.
4. [MINOR] The reported $S_8$ overlap-integration grid is misstated as $\Delta S_8=10^{-4}$ over $[0.70,0.90]$; the committed calculation uses 4,001 points over $[0.70,0.92]$, giving $\Delta S_8=5.5\times10^{-5}$ (arxiv/paper1b_mcmc_companion.tex:1897; reproducibility/cosmology/c13_s8_desy3_overlay.py:80). The quoted overlaps are unaffected at displayed precision, but the claimed recipe is not exact.
5. [MINOR] The fixed-coupling ALP posterior summary mixes conventions without labeling them: direct multiplicity-weighted recomputation gives $\theta_i$ mean$\pm$SD $=1.359\pm0.449$ and median/16–84% $=1.317^{+0.439}_{-0.369}$, whereas the paper reports $1.32\pm0.41$; the corresponding weighted mass median is $37.2H_0$, not approximately $36H_0$ under the stated $H_0=1.44\times10^{-33}$ eV conversion (arxiv/paper1b_mcmc_companion.tex:2593, arxiv/paper1b_mcmc_companion.tex:3177).
6. [MINOR] The exact artifact remains explicitly pre-release: the manuscript points to mutable `main`-branch URLs, states that the manifest does not freeze the paper, and leaves the final commit/tag and DOI pending (arxiv/paper1b_mcmc_companion.tex:2962, arxiv/paper1b_mcmc_companion.tex:3069). A stable archival release binding source, PDF, code, and scientific payload identifiers is required before acceptance.

(3) The central limited claim is supported for the stock-CAMB null result, synthetic NaMaster recovery, and explicitly fixed-background ALP surrogate, but not yet as a standalone physical spectator-ALP inference suitable for JCAP.