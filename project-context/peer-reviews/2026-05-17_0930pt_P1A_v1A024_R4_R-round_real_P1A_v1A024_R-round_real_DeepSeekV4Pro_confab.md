# P1A_v1A024 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0930pt_P1A_v1A024_R4_R-round_real
**Wall time**: 253.2s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=26016, completion=13139, reasoning=11737, total=39155

---

## Adversarial Peer Review — Paper 1A v1A.0.24 (R4)

### Finding 1 — BLOCKER: Dimensional inconsistency in birefringence coupling (Route 4) conflates dimensionless and dimension‑1 pseudoscalar fields
**ID:** PAPER-DEE-B1  
**Section:** §4.4 (Route 4), also affects §3.1 and the abstract’s β≈0.27° statement.  
**Issue:** The parity‑odd operator in §2.2 carries coupling α/M with mass dimension –1 and the Nieh–Yan pseudoscalar is dimensionless. In Route 4 the same coupling is used to compute a rotation angle via β = (α/M)Δθ, but the standard axion‑photon birefringence formula requires a dimension‑1 field (Δθ must have dimension +1 to yield a dimensionless β). The paper silently switches θ from a dimensionless Nieh–Yan scalar to a canonical ALP field of dimension +1 without any conversion factor or clarification. This makes the Route 4 amplitude‑closure argument dimensionally inconsistent and undermines the claim that the same coupling cannot simultaneously deliver dark energy and birefringence.  
**Fix:** Either (i) explicitly introduce a separate ALP field φ with dimension +1 and a new coupling g_{aγ} unrelated to α/M, or (ii) derive the mapping from the dimensionless Nieh–Yan pseudoscalar to a canonically normalised field, showing how the effective coupling acquires the correct dimension. Without this, the Route 4 closure is not trustworthy.

---

### Finding 2 — MAJOR: Headline cosmological numbers are not reproducible from the provided repository
**ID:** PAPER-DEE-B2  
**Section:** §15 (Conclusions), Appendix A, and the Data Availability statement.  
**Issue:** The paper states that “All materials necessary to reproduce the cosmological … results are publicly available at [GitHub]” and lists H₀=67.68±1.06, σ₈=0.803±0.008, Ωₘ=0.308±0.005, ΔN_eff≈0, etc. The repository contains only Cobaya YAML configurations and pipeline code; the actual MCMC chains and post‑processing scripts that produce those numbers are not present (they are deferred to companion Paper I(b)). A reader cannot reproduce the headline values from the supplied repository alone. This violates the paper’s own reproducibility claim.  
**Fix:** Either (i) upload the full chains and a script that regenerates the quoted values to the repository, or (ii) remove the claim that the repository alone enables reproduction and clearly state that the numbers are verified only in the companion paper.

---

### Finding 3 — minor: Thermal‑reset argument incorrectly equates fermion number density with spin density
**ID:** PAPER-DEE-B3  
**Section:** §2.3 (Reheating thermal‑reset barrier, supporting B14).  
**Issue:** The argument states that post‑reheating torsion is set by the instantaneous thermal bath because n_ψ(T_reh) ~ T_reh³ is “enormously larger” than the diluted bounce‑era spin density. However, torsion couples to the axial spin density S^λ_{μν}, not the number density. In an unpolarised thermal bath the expectation value of the spin density is zero, so the thermal bath does not generate a large torsion; it resets torsion to zero. The qualitative conclusion (memory erased) survives, but the quantitative comparison is physically incorrect and could mislead readers into thinking a large thermal torsion is produced.  
**Fix:** Replace the number‑density comparison with a statement that the thermal bath is unpolarised, hence the net spin density vanishes, erasing any bounce‑era torsion memory.

---

### Finding 4 — minor: Unexplained 25‑order discrepancy in Route 2 cross‑check
**ID:** PAPER-DEE-B4  
**Section:** §4.2 (Route 2).  
**Issue:** The main dimensionless ratio gives Δθ_one‑loop/Δθ_obs ~ 10⁻⁵⁸–10⁻⁶⁰. A “complementary cross‑check” is mentioned that yields ~10⁻³³, a difference of ~25 orders of magnitude, with no derivation or explanation of why the two orderings differ so drastically. The text merely states both land on qualitative closure, but such a large spread suggests an unresolved dimensional or algebraic ambiguity that could hide a factor that changes the conclusion.  
**Fix:** Either remove the unreproduced cross‑check or provide its full derivation and show explicitly why the 25‑order spread does not affect the closure.

---

### Finding 5 — nit: Abstract rounding of e‑fold factor inconsistent with main text
**ID:** PAPER-DEE-B5  
**Section:** Abstract (line “k_bounce ~ e^{30} times the observable horizon”) vs. §14.4 (uses e^{32} from N_tot−N_exit=32).  
**Issue:** The abstract states the SPHEREx wavenumbers are pushed to “e^{30} times the observable horizon”, but the detailed calculation in §14.4 gives e^{32} (≈7.9×10¹³ vs. ≈1.1×10¹³). The rounding from 32 to 30 is not explained and changes the scale by a factor of ~7. While not fatal, it introduces a small numerical inconsistency.  
**Fix:** Use e^{32} in the abstract or explicitly note that 30 is a round‑number approximation.

---

### Finding 6 — minor: Claim of “13 logically‑independent” barriers is debatable for several pairs
**ID:** PAPER-DEE-B6  
**Section:** §9 (Barrier table) and throughout.  
**Issue:** The paper merges B8 and B14 as non‑independent, but other barriers also show significant overlap. For example, Barrier 5 (Scale Separation) and Barrier 10 (UV→IR Specificity Dilemma) both address the impossibility of bridging Planck‑scale bounce physics to late‑time H₀ without fine‑tuning; Barrier 4 (Planck Suppression) and Barrier 11 (Decoupling Universality) both rely on Planck‑mass suppression of torsion couplings. Counting them as fully independent overstates the logical disjointness of the constraint catalog.  
**Fix:** Either acknowledge the partial overlap explicitly or re‑group the barriers into a smaller set of independent mechanism‑closure arguments.
