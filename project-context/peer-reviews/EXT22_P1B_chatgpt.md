# EXT22 P1B chatgpt — chat: https://chatgpt.com/c/6a3e66e2-02b4-83e8-bc72-549ccf3663c4

Referee Report — Paper P1B (revised), "Bounce MCMC companion"

1. Recommendation: ACCEPT
This revised companion paper is publishable in its present scientific form. It is unusually explicit about scope: the ΛCDM+ΔNeff chains are correctly framed as a stock-CAMB radiation-proxy null test rather than a torsion Boltzmann-module test; the NaMaster work is clearly labelled as synthetic-sky pipeline validation rather than a sky detection; and the ALP section is repeatedly scoped as a standard GR+ALP consistency check, not a distinctive ECH prediction.
The paper is dense and occasionally over-caveated, but I do not find a blocker, unsupported load-bearing claim, missing critical control, or reproducibility gap requiring substantial scientific rework. Remaining issues are presentation/clarification items.

2. BLOCKERS — must fix before publication
None.
I find no publication-blocking scientific issue in the revised manuscript.

3. MAJORS — should fix if possible, but not acceptance-blocking

Major 1 — Secs. III/V C/Table II, w0wa diagnostic: reduce prominence of marginal-tail "σ" language.
Location: Sec. III "Physics interpretation," Sec. V C, Table II.
Issue: The manuscript correctly states that the w0wa departures are marginal-tail posterior-distance diagnostics, not detection significances or model-selection evidence. However, the repeated "+4.3σ" and "−3.6σ" phrasing remains visually stronger than the caveat, especially because the DES-SN5YR × Pantheon+ overlap-covariance issue is not corrected in this paper.
Fix: Keep the numbers, but relabel them everywhere as "posterior-distance diagnostic" or "marginal-tail distance," and avoid standalone wording that could be read as a detection/exclusion claim. A compact statement such as "diagnostic only; not a model-comparison result" should appear in the first sentence where the values are introduced.

Major 2 — Sec. IV, NaMaster estimator choice: document the exact public-script comparability more tightly.
Location: Sec. IV, "Canonical estimator choice" and robustness-battery discussion.
Issue: The unweighted χ² estimator is retained to match public NaMaster birefringence driver scripts. The robustness battery shows that inverse-variance weighting removes most of the observed under-recovery, so the estimator choice is scientifically acceptable for a comparability test. Still, the claim of matching public scripts should be pinned more explicitly.
Fix: Add the exact public script/version/commit or URL anchor used for the estimator comparison, and state whether the production public analysis uses the same binning, template, and weighting convention or only the same broad estimator family.

Major 3 — Sec. VI/Table IV, spectator-ALP subset: clarify whether Ωa < 0.01 is a physical prior or a posterior diagnostic cut.
Location: Sec. VI "Spectator-subset readout," "ALP dark-energy fraction Ωa," Table IV.
Issue: The text says the spectator-safe subset is 13% of posterior mass and is the only subset safely sub-dominant. This is well disclosed, but the paper should make absolutely clear that the headline ALP posterior is not sampled under Ωa < 0.01 as a prior; rather, Ωa < 0.01 is a posterior restriction/readout.
Fix: Add one sentence before Table IV: "The Ωa cuts are posterior diagnostic restrictions, not priors imposed during sampling; the spectator-safe posterior is therefore a restricted-subset readout rather than a separately normalized spectator-prior fit."

4. MINORS — polish / clarity

Minor 1 — Abstract/page 1: shorten the abstract.
The abstract is scientifically transparent but too long and internally repetitive. It could be reduced by 25–35% without losing any load-bearing caveats. In particular, several caveats about the NaMaster MC not being a sky detection and the ALP not being distinctive ECH are repeated in nearly identical form.

Minor 2 — Sec. III/Table I: define "full-tension" once in a compact boxed or parenthetical form.
The full-tension stack is clear after careful reading, but readers would benefit from a single early definition: Planck NPIPE high-ℓ + Planck low-ℓ/lensing + SDSS BAO + Pantheon+ + SH0ES MB-anchor + DES-Y3 S8.

Minor 3 — Sec. III footnote 1: compress sample-count reconciliation.
The reconciliation is useful, but the footnote is long enough to interrupt the main narrative. Move the most detailed burn-in/GetDist accounting to Appendix A and retain only the essential numbers in the footnote.

Minor 4 — Table II: make "overlap-uncorrected" visually unavoidable.
The caption already states this, but because Table II contains prominent σ-distance entries, add "diagnostic, overlap-uncorrected" directly in the table title or first column header.

Minor 5 — Sec. IV/Fig. 3: explicitly state that the MC bias is not a real-sky systematic budget.
This is already said in the text. It should also be included in the Fig. 3 caption's first or final sentence, because readers may inspect the figure independently.

Minor 6 — Sec. IV: clarify the role of bins above ℓ = 1024 earlier.
The explanation that bins above the map band limit carry zero template weight appears later and is reassuring. Move a short version immediately after the formal binning definition to prevent confusion about fitting to ℓ = 1536 with Nside = 512 maps.

Minor 7 — Sec. VI Eq. (4): distinguish convention from physics in one sentence.
The αEM/(4π) convention is explained, but readers may wonder whether a different convention changes β. Add one sentence saying that changing convention only shifts the definition of Caγ, not the observable product CaγΔϕ/fa.

Minor 8 — Sec. VI/Table IV: avoid saying "median m ≃ 40.5H0" as though it is universal.
The conclusion correctly distinguishes full-chain median m ≃ 36H0 from Ωa < 0.01 median m ≃ 40.5H0. Keep the subset label attached every time this number appears.

Minor 9 — Data and Code Availability: add a tagged-release placeholder.
The commit hash and version stamp are good. A DOI/tag placeholder is fine, but the final submission should include either a Zenodo DOI or an immutable GitHub release tag.

Minor 10 — Appendix C: flag the βfree ESS caveat near the first βfree mention in Sec. VI.
Appendix C notes ESS ≈ 265 for βfree. Add a short parenthetical in Sec. VI when βfree is first reported, so readers do not need to wait until the appendix.

5. Strengths

Excellent scope discipline. The paper repeatedly prevents over-interpretation: stock-CAMB ΔNeff is not presented as a torsion Boltzmann solution, NaMaster MC is not presented as a sky detection, and ALP birefringence is not presented as an ECH-specific prediction.

Reproducibility is unusually strong. The manuscript names chain counts, burn-in conventions, YAML likelihood blocks, corrected artifacts, code paths, HuggingFace datasets, and known gaps. This is substantially above typical companion-paper transparency.

The revised NaMaster section is scientifically honest. The paper not only reports the ∼12% under-recovery but performs a useful attribution battery showing that estimator weighting and BB-template assumptions dominate over apodization/mask geometry.

The ALP section now contains the necessary spectator-status caveat. The Ωa definition, posterior-subset table, coupling burden, and misalignment tuning are all explicit. This prevents the paper from overstating "naturalness."

Model-comparison restraint is appropriate. The manuscript correctly avoids claiming Bayes factors, AIC/BIC, or Savage-Dickey evidence from a Metropolis-Hastings chain where the ΛCDM point is unsampled.

The paper is internally consistent with its companion role. It supplies verification and compatibility checks for the broader ECH program without trying to make those checks carry the full theoretical burden of Paper I(a).

Final assessment
The revised P1B companion is technically acceptable. Its main results are null/compatibility checks, and the manuscript now says that clearly. I recommend ACCEPT, with the above changes treated as optional final polish rather than grounds for another substantive revision round.
