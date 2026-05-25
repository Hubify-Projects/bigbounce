# P4 R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P4_v1_0_128
**Wall time**: 25.5s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=87541, completion=1923, reasoning=967, total=89464

---

**PAPER-GRO-B1 (BLOCKER)**  
**Section: Abstract + §4.4.1 / dipole_symmetry_caveat**  
The canonical-mask +3.64σ residual is interpreted as depth-correlated systematics on the basis of ℓ=2 > ℓ=1 structure, quartile washout, and cross-spectrum r_ℓ=2 = −0.65 (σ = −2.89), yet the ℓ=1 cross-spectrum is only −1.53σ and the bootstrap is explicitly tautological. The three-interpretation “closure” therefore rests on suggestive patterns rather than decisive evidence; a clean primordial dipole at ~1.7% is disfavored but not excluded at high .

**Fix:** Replace “favoured by direct cross-spectrum” and “three-interpretation closure” with “consistent with a depth-correlated systematic at the ~2–3σ level; a sub-dominant primordial component is not excluded.” Move the +3.64σ result to a dedicated systematics subsection rather than the abstract.

**PAPER-GRO-B2 (BLOCKER)**  
**Section: Abstract + §1 + §9 (Shamir comparison)**  
The claim that the result is “inconsistent in amplitude with Shamir’s ~3% asymmetry by a factor of ~6–12” is presented as a direct refutation, yet the paper repeatedly states that a matched-footprint Ganalyzer reanalysis under Shamir’s exact cuts and classifier is required for a likelihood-level comparison and is not performed. The amplitude comparison therefore mixes different selection functions, classifiers, and masks.

**Fix:** Change the abstract and introduction to “our pipeline yields a maximum regional asymmetry of 0.32% on a 2.5× larger spiral sample; a matched Ganalyzer reanalysis on the same footprint is required to quantify tension with Shamir (2012, 2020, 2022).”

**PAPER-GRO-M1 (MAJOR)**  
**Section: §4.4.1 + Table I + monopole_mask_null**  
The headline −0.12σ subsample-mask null is load-bearing, but the canonical-mask direct-MC remains +3.64σ after MASTER, with only ~12% explained by the monopole-only null. The paper’s own multi-null battery shows the residual is robust to apodization and pixel-count threshold, yet is still attributed to systematics without a systematics-preserving null model.

**Fix:** State explicitly that the canonical-mask residual is unresolved at the present null-model level and that the load-bearing result is the subsample-mask null; do not describe the canonical result as “resolved by the v1.0.108 multi-null battery.”

**PAPER-GRO-M2 (MAJOR)**  
**Section: Abstract + §1 + title**  
The framing “Survey-Scale Galaxy Chirality… A −0.12σ Subsample-Mask ℓ=1 Null” and repeated emphasis on 8.47 M galaxies / 3.2 M spirals presents the catalog size as the primary advance, yet the effective sensitivity gain over CE-ResNet (Jia et al. 2023) is only ~1.3× in spiral count and the null result is consistent with prior nulls (Iye 2021, Tadaki 2020). The “largest” claim is numerically true but does not establish a qualitatively new constraint once classifier and mask differences are acknowledged.

**Fix:** Lead the abstract and introduction with the methodological advance (equivariant TTA + explicit monopole-mask leakage quantification) rather than raw sample size; qualify the size comparison as “larger spiral count under a different classifier and selection.”

**PAPER-GRO-m1 (minor)**  
**Section: §4.4.1 + sensitivity floor**  
The empirical 50%-recovery-at-3σ threshold is quoted as 0.75% while the Fisher floor is ~0.29% full-amplitude; the text correctly notes the empirical value is the relevant one, but the abstract still leads with the statistical Fisher number in the falsification criterion.

**Fix:** Make the falsification criterion use the empirical 0.75% threshold throughout; remove the parenthetical Fisher value from the abstract falsification sentence.

**PAPER-GRO-n1 (nit)**  
**Section: Throughout (version notes and artifact macros)**  
The LaTeX source contains extensive internal review scaffolding, cron-fire notes, and retracted claims that were already cleaned in v1.0.123; residual phrases such as “truth-audit falsifies this” and long artifact URLs remain in footnotes and captions.

**Fix:** Perform a final pass to remove all internal-review language and shorten artifact paths to the minimal reproducible form.
