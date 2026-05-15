# P4_v1070_R R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_0735pt
**Wall time**: 62.5s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=56960, completion=3557, reasoning=2651, total=60517

---

**PAPER-GRO-B1**  
**BLOCKER** — Sec. IX (Conclusions) + Sec. VI.B (monopole+mask leakage) + Table VII (monopole_mask_null)  
The canonical-mask +1.85σ at ℓ=1 is framed as “irreducible leakage floor” from the 9.5σ monopole, but the generative null only shows consistency with pure-monopole leakage; it does not quantitatively subtract the leakage or exclude a small primordial contribution at that level. The subsample-mask –0.12σ is presented as load-bearing while the full canonical sample (the actual production catalog) shows the excess.  

Fix: Either apply an explicit leakage model/subtraction to the canonical mask or report the primary result as a marginal +1.85σ excess on the full sample rather than a clean null.

**PAPER-GRO-B2**  
**MAJOR** — Sec. IX.J (face_on robustness) + Table VIII + Sec. VI (prereg hierarchy)  
The face-on HC-spiral rerun collapses from +4.31σ to +0.62σ only under a monopole-preserving null, while the paper’s headline dipole (0.43σ, p=0.30) and all other results use an isotropic p=0.5 null. This switch makes the robustness appear stronger than it is under the declared primary null.  

Fix: Recompute and report the HC-spiral dipole under the isotropic p=0.5 null used everywhere else, or explicitly justify the null change and label it a secondary diagnostic.

**PAPER-GRO-B3**  
**MAJOR** — Abstract + Sec. IX (sensitivity) + Table IX (mc_injection)  
The empirical floor is stated as |A_dipole| > 0.5% at 3σ, yet the injection-recovery table shows only P(σ>2) = 0.18 at A = 0.5% (and lower for 3σ). The quoted floor therefore overstates the actual detection threshold under the per-pixel-shuffle null the paper itself employs.  

Fix: State the floor as the amplitude at which P(detection) exceeds 50% under the chosen null, or report the result as a non-detection below ~0.7–0.8% with the current MC evidence.

**PAPER-GRO-B4**  
**MAJOR** — Sec. I (intro) + Sec. IX (comparison) + abstract  
The claim that the 3.2 M spiral sample “strongly disfavors” Shamir’s ~3% asymmetry by a factor of ~6–12 is presented as a direct amplitude comparison, but the classifiers, selection functions, and bias audits differ substantially; no matched-footprint reanalysis under Shamir’s pipeline is performed. This is an apples-to-oranges amplitude ratio, not a statistical exclusion.  

Fix: Replace “strongly disfavors … by a factor of ~6–12” with “the measured regional asymmetry is a factor of ~6–12 smaller than Shamir’s reported values under an independent classifier and pipeline; a like-for-like reanalysis would be required for a formal exclusion.”

**PAPER-GRO-B5**  
**minor** — Sec. II (labels) + Sec. IX (GZ1 cross-match)  
The independent GZ1 validation accuracy is only 69.91% (κ = 0.40) on 117 k spirals, yet the headline sensitivity and null claims treat the catalog as having near-Poisson-limited power. Classification noise at this level dilutes any true dipole and should be folded into the effective sensitivity.  

Fix: Add a short paragraph quantifying the dilution factor from the measured GZ1 agreement and adjust the quoted Fisher/empirical floors downward by that factor (or restrict the primary result to the HC-spiral subset).

**PAPER-GRO-B6**  
**nit** — Throughout (multiple tables, Sec. VI prereg, Sec. IX conclusions)  
Several load-bearing numbers (canonical N_spiral = 3 201 160, f_sky values, MC counts) are redefined or superseded across sections without a single consolidated table; readers must cross-reference footnotes and artifacts to reconstruct the exact analysis sample.  

Fix: Add one summary table in Sec. VI or IX listing the exact N, f_sky, mask, and null type for every headline statistic.
