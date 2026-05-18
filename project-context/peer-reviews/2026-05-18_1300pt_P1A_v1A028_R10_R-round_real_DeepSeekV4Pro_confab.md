# P1A_v1A028_R10 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1300pt
**Wall time**: 431.1s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=27035, completion=12742, reasoning=11306, total=39777

---

# Adversarial Peer Review (Confabulation‑Hunter)

**Reviewer:** DeepSeek‑V4‑Pro (reasoning)  
**Manuscript:** P1A v1A.0.28  
**Task:** Hunt for unsourced load‑bearing scalars, irreproducible arithmetic, and new convergent regressions.  

**Verdict:** No BLOCKER‑grade errors detected. The numbers that are load‑bearing (the no‑go amplitude closures, the bounce‑class $\fnl$, the birefringence amplitude, the e‑fold counts) are either sourced to companions/literature or are simple arithmetic derivable from displayed constants. The previous vendor‑convergent dimensional issues are acknowledged as phenomenological and no longer mis‑framed as derivations. Below are the minor/nit findings, none of which threaten the structural conclusions.

---

## PAPER‑DEE‑M1 (MAJOR)
**Section:** 4.3 (Route 2), “complementary cross‑check” passage.  
**Issue:** The alternative expression claimed to give a “dimensionless ratio” is not dimensionless; it carries dimensions of energy.  
`α_em/(4π·M_Pl·(α/M)·β_obs)·H_0` with `M_Pl (α/M)` dimensionless leaves `H_0` in the numerator; the result has units of eV, not a pure number. The value “of order 10⁻³³” is therefore not a dimensionless ratio and cannot be compared to the primary ratio. The statement that “both land on the qualitative R2 closure” is not harmed, but the arithmetic as written is dimensionally inconsistent and would mislead a reader trying to reproduce the cross‑check.  
**Fix:** Either delete the cross‑check, or rewrite it as a consistently dimensionless combination (e.g. move the `H_0` into the denominator as `(H_0/M_Pl)`) and recompute the resulting numeric value, or state that the second ordering is not used. If retained, the magnitude must be recalculated and the text updated.

---

## PAPER‑DEE‑m1 (minor)
**Section:** 2.3, 2.5 (dilution), and elsewhere.  
**Issue:** The total e‑fold number `N_tot ≈ 92` is described as “a fitted parameter, not predicted”, but no fitting procedure is described anywhere in the paper. The value is essentially a back‑of‑envelope matching to the observed ρ_Λ using the phenomenological dilution ansatz. The Appendix later computes `N_tot ≈ 94` from the genuine hierarchy. Labelling 92 as “fitted” gives a false impression of statistical determination.  
**Fix:** Replace “fitted” with “chosen to match ρ_Λ” or “obtained from the dilution matching”. State explicitly that it is an order‑of‑magnitude estimate, not a result of a statistical fit. The slight offset between 92 and 94 is harmless but should be acknowledged.

---

## PAPER‑DEE‑m2 (minor)
**Section:** 2.5 and 12 (Discussion).  
**Issue:** The “residual 10⁵” fine‑tuning number is presented without the underlying arithmetic. The claim that it “tracks e^{–3 ΔN_tot} for ΔN_tot ≈ 4 e‑folds” implies 10⁵ ≈ e^{12} ≈ 1.6×10⁵, which is an order‑of‑magnitude match. However, the number 10⁵ is never derived from any displayed equation; it appears only as the product “10⁻² × D_inf” with D_inf ~ 10⁻¹²¹, yet the 10⁵ does not come from that product (which gives 10⁻¹²³). The logic of the “reparameterization from 10¹²² to 10⁵” is conceptually clear but the explicit factor is not computed.  
**Fix:** Add one sentence showing the arithmetic: e.g., “N_tot ≈ 92 absorbs the 10¹²² hierarchy, and the remaining sensitivity is ΔN_tot ≈ 4, so the residual fine‑tuning factor is e^{3·4} ~ 1.6×10⁵, which we approximate as 10⁵.” This makes the provenance self‑contained.

---

## PAPER‑DEE‑n1 (nit)
**Section:** Abstract, line “the Holst dual contraction … vanishes identically by the first Bianchi identity”.  
**Issue:** This statement is only true when torsion is zero (the Levi‑Civita connection). Without torsion, the first Bianchi identity with torsion does not force the dual contraction to vanish. The abstract does not qualify that torsion vanishes in the relevant case; the reader could misinterpret it as a general property of the Holst term. The main text (Sec. 10) makes the chain of reasoning clear, so the abstract’s isolated phrasing is slightly misleading.  
**Fix:** In the abstract, qualify: “for the torsion‑free connection that results in the scalar‑matter case, the Holst dual contraction … vanishes identically …”. Or simply say “the Holst sector decouples completely”.

---

## PAPER‑DEE‑n2 (nit)
**Section:** 4.2 (Route 1), Eq. (4.2) bounding `ρ_NJL`.  
**Issue:** The bound `ρ_NJL ∼ n_ψ² / M_Pl²` is stated to have correct mass‑dimension +4. The text notes a prior transcription error; the current expression is correct. However, no numerical estimate of `n_ψ` at recombination or today is given, so the quantitative suppression relative to ρ_Λ is not displayed. The conclusion “many orders of magnitude below” is qualitative. Given the paper’s emphasis on amplitude‑level closures, a concrete number (or at least an explicit bound on n_ψ from baryon number density) would strengthen the route closure.  
**Fix:** Optionally add a sentence: “Using the post‑recombination baryon number density n_B ∼ 10⁻⁷ cm⁻³ ∼ 10⁻⁴² GeV³, one finds ρ_NJL ≲ 10⁻⁸⁴ GeV⁴, which is 40 orders of magnitude below ρ_Λ.” Even if approximate, it anchors the claim.

---

**Summary:** No new convergent regressions, no load‑bearing arithmetic errors, no unsourced headline figures that are claimed as original results of this paper. The issues above are editorial or presentational and do not affect the structural no‑go. The manuscript remains ready for external review on the physics‑cosmology axis.
