# INT Codex-subscription Review — P1B v1B.0.109 — gpt-5.6-sol (high)
paper: P1B  version: v1B.0.109  tex: arxiv/paper1b_mcmc_companion.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
binding: packet_key=0e7d0155d3c6adb314d837e10bc7e343a5e7c7bda225603abbedd040006372ef  prompt_sha256=3c369b40c7fd7738b549bf3e17aeefa3929f4041111960023a1b5c0b66e7c8b2
provenance: commit=54aeaae34614e24ee9d106416b46b7bbb5718128  source_sha256=1867608307746979f30fecaa247af2006394ba18b01784b09a8a1699451e17b2
pdf: snapshot=/Users/houstongolden/.cache/bigbounce/review-packets/pdf/36b8fc984b5be164f5ece1e2f0c3f661dfb49c9f99faa76e2b050e2bd0674a78.pdf  sha256=36b8fc984b5be164f5ece1e2f0c3f661dfb49c9f99faa76e2b050e2bd0674a78  pages=20
venue: Journal of Cosmology and Astroparticle Physics  article_type: Research article / computational methods  profile: JCAP-COMPUTATIONAL
source_tree: clean detached sparse tree at 54aeaae34614e24ee9d106416b46b7bbb5718128 (scope=arxiv)
UTC: 2026-07-15T10:13:18Z
context-note: Exact v1B.0.109 confirmation after spectator-conditioned closure. Verify the conditioned and unrestricted ALP estimands, executed NaMaster/S8 grids, weighted posterior summaries, and full-EB limitation. Immutable tag/DOI and standalone-JCAP venue disposition remain open.

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:
1. [MAJOR] NaMaster synthetic-sky normalization, arxiv/paper1b_mcmc_companion.tex:2105-2112. The generator labels its Gaussian template a Planck-2018 \(C_\ell^{EE}\) fit but passes amplitudes of \(15\)–\(40\,\mu{\rm K}^2\) directly to `healpy.synfast` as raw \(C_\ell\) (`reproducibility/p1_namaster_500mc/scripts/namaster_500mc.py:116-133,209`). Direct CAMB recomputation gives \(C_{140}^{EE}=3.58\times10^{-4}\,\mu{\rm K}^2\), versus the executed \(39.90\,\mu{\rm K}^2\), a factor \(1.1\times10^5\); analogous discrepancies occur at higher multipoles. Consequently the stated \(10\,\mu{\rm K}\)-arcmin noise is not ACT-like relative to the simulated signal, and the reported scatter, standard error, and template scores require rerunning with correctly normalized raw CAMB spectra. The committed 2,001-point recovery grid itself recomputes exactly to \(0.269^\circ\), \(0.341^\circ\), and \(-0.001^\circ\), so the algebraic window-operator closure is confirmed but its physical validation setting is not.

2. [MAJOR] Full-\(EB\) likelihood limitation, arxiv/paper1b_mcmc_companion.tex:2402-2426,3276-3299. The ALP calculation uses only the Gaussian scalar summary \(0.342^\circ\pm0.094^\circ\), omitting band-power covariance, calibration, foreground, and non-Gaussian likelihood structure. The manuscript discloses this correctly, and the committed arithmetic is verified: \(11{,}597/100{,}000=11.597\%\), \(6{,}137/100{,}000=6.137\%\), \(863/34{,}947=2.46945\%\), conditioned MC error \(0.0830\) percentage points, and the zero-count Wilson upper bound \(0.010991\%\). Raw-chain recomputation also exactly confirms the \(13.3818\%\) controlled selection fraction and \(\beta=0.27595^\circ\pm0.09880^\circ\). Nevertheless, the reported \(m\), \(C_{a\gamma}\), and spectator-subset inferences remain one-amplitude surrogate results; a full-\(EB\) analysis is required for them to constitute robust JCAP parameter inference.

3. [MAJOR] Standalone JCAP scope and novelty, arxiv/paper1b_mcmc_companion.tex:1317-1358,1515-1535. The manuscript explicitly describes three logically independent studies linked only bibliographically and programmatically: a standard stock-CAMB extension, an internal synthetic NaMaster closure test, and a one-datum ALP accommodation. It does not yet establish a unified scientific question or sufficient methodological novelty for a standalone JCAP Research Article. The revision must articulate and demonstrate a coherent methods contribution beyond collecting reproducibility checks, particularly after correcting the NaMaster simulation and completing the likelihood treatment.

4. [MINOR] \(S_8\) grid burn-in inconsistency, arxiv/paper1b_mcmc_companion.tex:1896-1908. The stated 4,001-point grid over \([0.70,0.92]\) was executed, and the inverse-variance arithmetic is correct, but its generator loads every raw chain row with `ignore_rows: 0` (`reproducibility/cosmology/c13_s8_desy3_overlay.py:25-40,81-95`), whereas the manuscript’s posterior summaries consistently discard 30% burn-in. Recompute the KDE overlaps and tensions after the same per-chain burn-in cut; the present values are numerically close but methodologically inconsistent.

5. [MINOR] Unsupported upper-prior-edge description, arxiv/paper1b_mcmc_companion.tex:2839-2870. Direct weighted recomputation of the \(c5\) chain gives \(m/H_0=1.71/13.17/196.65\) at 16/50/84%, against a prior extending to approximately \(700H_0\), with only \(4.94\%\) of weight in the uppermost 0.2 dex. This supports a shift above the \(m\sim H_0\) benchmark but not the caption’s claim that the marginal “piles toward” the upper prior edge.

6. [MINOR] Immutable release provenance, arxiv/paper1b_mcmc_companion.tex:2996-3013,3133-3149. Version v1B.0.109 still cites a pre-release v1B.0.108 manifest, while the paper-freezing commit/tag and dataset DOI remain pending. Before acceptance, the exact source, bound PDF, manifest, LFS payload OIDs, and supporting artifacts must be frozen under one immutable public version and persistent identifier.

(3) Yes—the narrowly stated proxy, exact-window algebraic closure, and conditional ALP-accommodation claims are supported by the committed artifacts, but their physical and standalone-JCAP interpretation requires the major revisions above.