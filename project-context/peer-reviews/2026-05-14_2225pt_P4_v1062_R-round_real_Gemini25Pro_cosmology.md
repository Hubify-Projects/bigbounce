# P4_v1062 R-round — REAL cross-vendor — Gemini-2.5-Pro cosmology-physics reviewer

**Model**: `google/gemini-2.5-pro` (via OpenRouter)
**Round**: 2026-05-14_2225pt
**Wall time**: 53.7s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=59508, completion=4927, total=64435

---

No blocker-grade findings. The paper's theoretical framing and interpretation of its own systematic-floor artifacts are sophisticated and sound. The discussion of how the morphological dipole null constrains cosmological parity-violation models is appropriately cautious and well-referenced.

## PAPER-GEM-M1

*   **Section:** §IX.G, "Mapping the bound onto cosmological parity-violation observables"
*   **Issue:** The distinction between the morphology and 4-point function (4PCF) channels is correct but could be stated more precisely in effective field theory (EFT) terms. The text describes them as "different observational projections," which is true but vague.
*   **Fix:** Clarify that the morphology channel (via tidal-torque theory) probes parity-odd couplings involving the tensor mode $\gamma_{ij}$, while the 4PCF primarily probes couplings involving the scalar mode $\zeta$.
*   **Classification:** minor

## PAPER-GEM-M2

*   **Section:** §VII, "Conclusions", paragraph 'Canonical-$N$ MASTER ℓ=1 direct compute'
*   **Issue:** The argument for dismissing the $+1.85\sigma$ result as a systematic artifact rests on the claim that the other two estimators (real-space dipole, subsample-mask MASTER) are more robust against monopole leakage. This claim is presented without a physical justification.
*   **Fix:** Add a brief physical reason why the full-sky real-space and larger-mask MASTER estimators are less susceptible to this specific systematic, e.g., they average over larger, more contiguous regions, which suppresses the projection of monopole power from small-scale mask features.
*   **Classification:** minor

## PAPER-GEM-N1

*   **Section:** §IX.G, "Mapping the bound onto cosmological parity-violation observables"
*   **Issue:** The paper correctly states it does not compute the primordial-to-morphology transfer function. It could briefly cite existing work that has estimated parts of this link to better motivate why the sub-percent regime is a theoretically interesting target.
*   **Fix:** Add a sentence noting that while a full end-to-end calculation is absent, partial estimates (e.g., Yu et al. 2020) suggest a small transfer function, making sub-percent morphology dipoles a plausible target for primordial signals.
*   **Classification:** nit
