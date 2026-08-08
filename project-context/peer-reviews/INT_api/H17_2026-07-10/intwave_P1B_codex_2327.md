# INT Codex-subscription Review — P1B v1B.0.106 — gpt-5.6-sol (high)
paper: P1B  version: v1B.0.106  tex: arxiv/paper1b_mcmc_companion.tex
modality: full-repo Codex CLI ChatGPT-subscription referee (read-only, ephemeral)
UTC: 2026-07-15T06:27:45Z
context-note: Exact local candidate commit d4924987; 20-page PDF arxiv/paper1b_mcmc_companion.pdf SHA-256 7cb825572d6474e5d0fb88fa61157df31cf5b88730243f11cf39fc25e2512013. Verify this hash before reviewing. Review standalone P1B science; readiness remains 56 and no human acceptance is claimed.

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: MAJOR REVISIONS

(2) ISSUES:

1. [MAJOR] The advertised cosmology reproduction path is nonfunctional (`arxiv/paper1b_mcmc_companion.tex:3027`; `reproducibility/cosmology/reproduce_cosmology.sh:37`). From the documented directory, the script searches for nonexistent `cosmology/cosmology/*.yaml` paths and skips every chain; it also requests Cobaya 3.5.4 rather than the reported 3.6.1 and does not regenerate the corrected summaries, convergence tables, or figures.

2. [MAJOR] The claimed version-specific SHA-256 provenance is incomplete (`arxiv/paper1b_mcmc_companion.tex:3014`; `arxiv/paper1b_mcmc_companion.tex:3161`; `reproducibility/p1b_analysis_artifact_manifest_v1B.0.106.json:7`). Although all 46 listed hashes verify, the manifest omits the frozen cosmology chains and corrected summaries, the ALP forward-model code, fixed-coupling chains, and prior-predictive artifacts underlying several quoted claims; therefore “internally verified from files identified by the manifest” is not currently true.

3. [MAJOR] The declared NaMaster robustness masks do not match the executed masks (`arxiv/paper1b_mcmc_companion.tex:2249`; `reproducibility/p1_namaster_500mc/scripts/declared_fsky_sign_battery.py:45`). The paper specifies \(|b|>5^\circ\) and \(|b|>15^\circ\) plus a declination cut, whereas the driver uses pure Galactic cuts of \(8.6269^\circ\) and \(20.4873^\circ\), with no declination selection; the reported recoveries are numerically reproducible, but they do not establish robustness for the stated survey geometries.

4. [MAJOR] The ALP abundance calculation described in the manuscript is not the calculation used to construct Table IV (`arxiv/paper1b_mcmc_companion.tex:2700`; `arxiv/paper1b_mcmc_companion.tex:2762`; `research/branch_R_alp_birefringence/phase2_mcmc/alp_ode.py:148`). The text applies \(3H=m_a\) followed by onset-energy dilution, while the code integrates the nonlinear cosine equation through \(z=0\) and evaluates present kinetic plus potential energy; applying the printed approximation to the committed chain gives only 2.03% weight at \(\Omega_{a,0}<0.01\), not the reported 13.38%.

5. [MAJOR] The spectator-ALP interpretation conflates distinct conditional subsets (`arxiv/paper1b_mcmc_companion.tex:2410`; `arxiv/paper1b_mcmc_companion.tex:2841`; `arxiv/paper1b_mcmc_companion.tex:2982`). The reproducible \(\Omega_{a,0}<0.01\) subset has \(\theta_i=(0.149,0.211,0.267)\), whereas \(\theta_i\le0.1\) is a separate 0.3275%-weight sliver with \(\beta=0.117\pm0.047^\circ\); consequently the claimed \(\theta_i\sim0.1\), \(25\times\) tuning characterization is unsupported. Moreover, the quoted 11.6% and 6.1% prior-predictive hit fractions are not conditioned on \(\Omega_{a,0}<0.01\), so they cannot quantify the prior-volume cost of the controlled spectator model.

6. [MINOR] The torsion estimate identifies the bare scaling \((T/M_{\rm Pl})^2\) directly with \(\Delta N_{\rm eff}\) (`arxiv/paper1b_mcmc_companion.tex:1673`; `arxiv/paper1b_mcmc_companion.tex:1705`). The numerical ratios \(1.7\times10^{-43}\) and \(1.1\times10^{-56}\) are arithmetically correct, but a physical \(\Delta N_{\rm eff}\) bound requires the thermal axial-current correlator, species factors, sign, and normalization to one neutrino species; this should be presented as a parametric negligibility estimate.

7. [MINOR] The reported template “S/N” neglects inter-bin covariance (`arxiv/paper1b_mcmc_companion.tex:2223`). Summing \((C_b^{EB}/\sigma_b)^2\) using marginal per-bin dispersions is not a matched-template significance for correlated cut-sky bandpowers; either use the full Monte Carlo covariance or label this explicitly as a diagonal heuristic.

8. [MINOR] The c15 run cannot provide the claimed empirical bound on likelihood-pairing bias (`arxiv/paper1b_mcmc_companion.tex:2354`; `arxiv/paper1b_mcmc_companion.tex:2379`). It failed the manuscript’s convergence threshold and simultaneously changed the low-\(\ell\) and lensing likelihoods, so its \(0.04\sigma\) agreement is only a corroborative check, not a quantitative systematic bound.

9. [MINOR] Several reported diagnostics contain internal numerical inconsistencies: Table I gives Planck+BAO+SN worst \(\hat R-1=0.003\) although the cited current diagnostics give \(9.71\times10^{-4}\) (`arxiv/paper1b_mcmc_companion.tex:1914`); the same c14 result is quoted as both \(0.328\pm0.100^\circ\) and \(0.326\pm0.099^\circ\) (`arxiv/paper1b_mcmc_companion.tex:2692`); and rounding \(1.06\) to two significant figures cannot change \(4.93\times10^{-3}\) to \(4.65\times10^{-3}\) (`arxiv/paper1b_mcmc_companion.tex:2520`).

(3) No—the headline stock-CAMB null posterior and canonical exact-window recovery are numerically supported, but the manuscript’s broader computational-reproducibility and controlled spectator-ALP claims are not supported as presently documented.