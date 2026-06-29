# RBEXT P1B ChatGPT — chat: https://chatgpt.com/c/6a42c73d-e2dc-83e8-b134-15c9836d3e20
VERDICT: MAJOR REVISIONS

Provider: ChatGPT (default/Instant tier)
PDF: RBEXT_P1B.pdf | md5: c85f8c7a9fac08711b6b57de0fcf6efa
Harvested: 2026-06-29

---

1. Recommendation: MAJOR REVISIONS

Technically substantial and unusually self-critical, but not yet publication-ready for MNRAS/PRD/JCAP. The core issue is not one fatal numerical error; it is that the paper is a companion/verification paper whose headline is diffuse, mixing a stock-CAMB null proxy, synthetic NaMaster validation, a caveated w0wa diagnostic, and an ALP consistency exercise without a single sharply controlled inference target.

2. BLOCKERS

None requiring rejection outright. The paper repeatedly states key limitations: ΔNeff is not an ECH theory module, NaMaster is not a sky detection, ALP birefringence is not distinctive ECH, and w0wa has an overlap-uncorrected SN product-likelihood caveat. These disclosures prevent the main claims from being misleading enough to reject, but they also weaken the paper's publishable contribution.

3. MAJORS

- The w0wa section should be demoted or moved to appendix unless overlap-controlled chains are included. The DES-Y5 × Pantheon+ overlap double-counts shared SNe and artificially narrows the posterior, so no σ-distance or model-selection claim is valid. Yet the text still spends substantial space on the phantom/quintom-B direction and unsampled ΛCDM point. Include Pantheon+-only and DES-Y5-only controls, or demote.
- The paper's main contribution is not sufficiently unified. The three/four analyses are individually scoped as "compatibility checks," but the companion's scientific claim becomes: several things do not contradict the program. For a top journal the authors need a clearer central question and a compact answer.
- The ALP result is accommodation, not explanation. The abstract and conclusions should make plainer that this is not evidence for ECH or bounce cosmology.
- NaMaster validation is useful but limited. Synthetic skies omit foregrounds and cannot test the β–α degeneracy that dominates real birefringence inference. Frame more narrowly as an algebraic pseudo-Cℓ recovery test, not as "CMB E-B analysis."
- Reproducibility claims depend heavily on repository artifacts. Frozen artifacts need stable DOI/versioned release, not just repository paths.

4. MINORS

- The abstract is too dense and overlong; reads like a compressed audit log.
- Several caveats are repeated many times; consolidate into one "Scope and limitations" table.
- The distinction between PR3/PR4/NPIPE provenance in the Eskilt-Komatsu value is confusing; simplify.
- The paper should avoid phrases like "headline" inside scientific claims.
- Table IV is visually overloaded; split full-chain and spectator-subset readouts.
- The "not directly comparable" warnings are correct but repetitive.
- The title may overpromise; "MCMC Proxy, Pipeline Recovery, and ALP Consistency Checks" would be more accurate.

5. Strengths

- Unusually transparent scope control. The paper explicitly prevents overinterpretation of ΔNeff, NaMaster, ALP, and w0wa results.
- Good numerical hygiene. Chain counts, convergence, ESS, burn-in choices, likelihood blocks, and corrected artifact warnings are documented in detail.
- The ΔNeff result is clean and publishable as a null proxy: stock CAMB gives ΔNeff consistent with zero and does not resolve H0 tension.
- The NaMaster bias attribution is valuable: the robustness battery identifies estimator weighting and BB-template assumptions rather than mask/apodization as the main under-recovery source.
- The ALP section is honest about non-distinctiveness and tuning, which makes it scientifically safer than many comparable phenomenology claims.
