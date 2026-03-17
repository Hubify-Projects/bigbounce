# Closest Prior Work Map

**Date:** 2026-03-17

---

## Top 5 Closest Papers to Our Branch R Result

---

### #1. Fujita, Murai, Nakatsuka & Tsujikawa (2021)
**arXiv:** 2011.11894 | **Published:** PRD 103, 043509

**OVERLAP: VERY HIGH — this is the most dangerous prior.**

| Dimension | Fujita+ 2021 | Ours |
|-----------|-------------|------|
| Field content | Single ALP, cosine + quadratic | Single ALP, cosine |
| f_a | M_Pl considered as explicit case | M_Pl fixed |
| Coupling | g_{aγ} free (parametric) | C = 8 (SM) fixed → g derived |
| Mass regime | Full range: spectator, DE, EDE | Spectator only (m >> H_0) |
| Spectator case? | YES — one of several cases studied | YES — the only case |
| MCMC? | YES | YES |
| Free params | g, m (with f derived) | θ_i, log10(m) |
| β ~ 0.3° fit? | YES | YES |
| Free-β baseline? | NO | YES |
| ALP ≡ free-β? | NOT STATED | EXPLICITLY DEMONSTRATED |
| ECH motivation? | NO | YES |

**What they did that we also do:**
- Considered f_a = M_Pl
- Ran MCMC on ALP parameters
- Obtained mass constraints in spectator regime
- Fit β ~ 0.3° from Planck data

**What we do that they don't:**
- Fix C = 8 (SM anomaly coefficient) and f_a = M_Pl simultaneously → 2-parameter model
- Compare against free-β baseline explicitly
- Demonstrate ALP is statistically equivalent to free β (the "honest assessment")
- Frame within ECH/torsion UV completion
- Present the ALP as the sole surviving prediction of a broader program

**What they do that we don't:**
- Consider DE and EDE regimes (not just spectator)
- Constrain coupling g directly (we fix it via C)
- Use Planck likelihood (we use the summary statistic β_obs ± σ)
- More sophisticated data treatment

**Honest assessment:** Fujita+ 2021 is our closest competitor. They already showed that a Planck-scale ALP in the spectator regime fits the birefringence data. Our value-add is: (a) the specific 2-parameter reduction with SM coupling, (b) the free-β comparison, and (c) the broader framework context. These are incremental, not revolutionary.

---

### #2. Nakagawa, Nakai, Qiu & Yamada (2025)
**arXiv:** 2503.18924

| Dimension | Nakagawa+ 2025 | Ours |
|-----------|---------------|------|
| Field content | Single axion + Λ | Single ALP (spectator) + Λ |
| f_a | ~10^{17} GeV (string scale) | M_Pl = 2.4 × 10^{18} GeV |
| Coupling | c_γ fit to match β = 0.3° | C = 8 fixed |
| Mass regime | 2H_0 ≲ m ≲ 7H_0 | Few × H_0 (from posterior) |
| MCMC? | NO (parameter scan) | YES |
| Free-β baseline? | NO | YES |
| Key innovation | aΛCDM: axion modifies w(z) slightly | Pure spectator, no w(z) effect |

**What makes us different:** They keep f_a sub-Planckian and find c_γ ~ O(1). We fix f_a = M_Pl and C = 8 and find θ_i ~ O(1). These are complementary parameterizations of the same physics. Their mass window (2–7 H_0) overlaps with our posterior. Key difference: they connect to DESI w(z) through subdominant DE contribution. We treat the ALP as pure spectator.

**Honest assessment:** Conceptually very similar. Different parameterization, different f_a choice, no MCMC. Not a direct overlap but shows the same physical story is being told by multiple groups.

---

### #3. Namikawa, Murai & Naokawa (2025)
**arXiv:** 2506.20824 | **Published:** PRD (2025)

| Dimension | Namikawa+ 2025 | Ours |
|-----------|---------------|------|
| Data treatment | Full Planck EB power spectrum (multi-ℓ, multi-frequency) | Summary statistic (β_obs ± σ) |
| Model | General ALP (g, m free) | Fixed f_a = M_Pl, C = 8 |
| MCMC? | YES (sophisticated) | YES (simple) |
| Mass constraints | Specific mass exclusions at > 2σ | Weakly constrained mass posterior |
| Key innovation | Uses EB spectrum SHAPE for mass discrimination | Uses single number β_obs |

**What makes us different:** They use the full EB power spectrum — this is fundamentally more informative than our single Gaussian likelihood. Their mass constraints are much stronger than ours. We cannot compete on data analysis sophistication.

**What we have that they don't:** The specific 2-parameter model with physical interpretation (θ_i naturalness), the free-β comparison, the ECH context.

**Honest assessment:** This paper is the state-of-the-art for ALP birefringence constraints. It supersedes our data analysis. Our value is in interpretation, not in constraint quality.

---

### #4. Lin & Yanagida (2023)
**arXiv:** 2208.06843 | **Published:** PRD 107, L021302

| Dimension | Lin & Yanagida 2023 | Ours |
|-----------|---------------------|------|
| f_a | 10^{16} GeV (string-inspired EW axion) | M_Pl |
| Model | Electroweak axion | General ALP with SM coupling |
| β natural? | YES — "naturally explained" | YES — θ_i ~ O(1) |
| MCMC? | NO | YES |

**What makes us different:** Different f_a choice, different UV motivation. They argue f_a ~ 10^{16} GeV is natural from string theory; we argue f_a = M_Pl is natural from ECH. Both claim the birefringence is "naturally explained" by their respective frameworks. Our MCMC adds quantitative posterior; their analytic argument is simpler.

**Honest assessment:** This paper makes a "naturalness" argument very similar to ours, just with a different f_a. The claim "our model naturally gives β ~ 0.3°" is not unique to us.

---

### #5. Eskilt, Herold, Komatsu, Murai, Namikawa & Naokawa (2023)
**arXiv:** 2303.15369 | **Published:** PRL 131, 121001

| Dimension | Eskilt+ 2023 | Ours |
|-----------|-------------|------|
| Model | EDE axion with photon coupling | Spectator ALP |
| MCMC? | YES — full Planck likelihood | YES — single Gaussian |
| Mass constraints? | YES — from EB shape | WEAK — from β amplitude only |
| Key innovation | First EB spectrum shape analysis | None comparable |

**What makes us different:** They study EDE, not spectator. Different mass range, different physics. Our models are complementary, not competing.

**Honest assessment:** Lower direct overlap but shows that MCMC + ALP + birefringence is a well-established methodology. Our MCMC adds nothing methodologically new.

---

## Overlap Summary

| Novelty Dimension | Already in Literature? | Our Version |
|-------------------|----------------------|-------------|
| f_a = M_Pl + birefringence | YES (Fujita+ 2021) | Same |
| MCMC on ALP params from β | YES (Fujita+ 2021, Namikawa+ 2025) | Simpler version |
| β ~ 0.3° naturally explained | YES (multiple papers) | Same conclusion |
| c_γ ~ O(1) or C = 8 natural | YES (Nakagawa+ 2025, Choi+ 2021) | Similar |
| Spectator regime identified | YES (Fujita+ 2021) | Same |
| EB spectrum shape analysis | YES (Eskilt+ 2023, Namikawa+ 2025) | We DON'T do this |
| Free-β baseline comparison | NO | **OURS** |
| ALP ≡ free-β demonstration | NO | **OURS** |
| ECH/torsion UV motivation | NO (for birefringence) | **OURS** |
| Broader closure framework | NO | **OURS** |
| 13 barriers + sole survivor | NO | **OURS** |

---

## The Brutal Truth

The ALP birefringence result itself — "a Planck-scale spectator ALP with O(1) parameters naturally gives β ~ 0.3°" — is **not new**. Fujita+ 2021 already demonstrated this. Multiple subsequent papers have explored the same parameter space with more sophisticated data treatments.

What is potentially new is:
1. The specific 2-parameter reduction (f_a = M_Pl, C = 8 fixed) with MCMC posteriors
2. The explicit demonstration that ALP = free β statistically
3. The framing as the sole survivor of a systematic 15-branch investigation
4. The ECH torsion connection (though this is motivational, not predictive)

Whether these constitute sufficient novelty for a publication depends on how the paper is framed.
