# P4 R-round — DIRECT vendor — Gemini-2.5-Pro cosmology-physics reviewer

**Model**: `gemini-2.5-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round7
**Wall time**: 54.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=99429, completion=1155, total=105321

---

## PAPER-GEM-B1

*   **Classification:** BLOCKER
*   **Location:** Abstract (L107-111), Sec. IX.D (L2541-2550), Sec. IX.J (L2608-2668)
*   **Issue:** The paper's falsification criterion and headline sensitivity are based on a small, high-confidence (HC) subsample ($A \gtrsim 0.75\%$), while a full-catalog injection test reported in the discussion shows much better sensitivity ($A < 0.50\%$). This is inconsistent and misrepresents the constraining power of the full dataset by quoting a weaker limit from a subsample.
*   **Fix:** The falsification criterion and all headline sensitivity statements must be based on the full-catalog injection-recovery analysis. Update the abstract and conclusion to reflect the stronger, consistently-derived, full-catalog sensitivity floor.

## PAPER-GEM-B2

*   **Classification:** BLOCKER
*   **Location:** Sec. III.E (L946-976), Sec. IX.F (Table IX), Sec. IX.H (Table XI)
*   **Issue:** The paper reveals that the hard-label argmax-based CW-fraction is a "fragile statistic" dominated by noise on $N \sim 2000$ holdouts. This demonstrated fragility undermines the robustness of all other hard-label-based diagnostics on small-to-intermediate subsamples, a weakness not sufficiently propagated to the interpretation of results like the confidence-stratified or per-leg dipoles.
*   **Fix:** Add a quantitative caveat to all hard-label-based subsample analyses about the potential for noise-driven fluctuations due to this demonstrated statistical fragility. The lengthy retraction narrative in Sec. III.E should be moved to an appendix.

## PAPER-GEM-M1

*   **Classification:** MAJOR
*   **Location:** Abstract (L57-60), Sec. IV.B (L1101-1153), Sec. IX.K (L2816-2840)
*   **Issue:** The paper measures a $9.5\sigma$ parity-odd monopole but dismisses it as a systematic based on a working hypothesis. The abstract misleadingly states parity-odd observables are "outside this paper's scope," when in fact the monopole is a key measured quantity and the driver for the central systematic leakage channel.
*   **Fix:** Reframe the abstract and discussion to state that a significant parity-odd monopole *is* detected but attributed to systematics. The dismissal of the monopole must be presented as a plausible but unproven hypothesis pending a scaled, independent, non-human-labeled reference.

## PAPER-GEM-M2

*   **Classification:** MAJOR
*   **Location:** Abstract (L50-53), Sec. III.A (L641-650), Sec. X (L3213-3219)
*   **Issue:** The headline null result ($-0.12\sigma$) relies on a "subsample mask," while the "canonical mask" shows a $+3.64\sigma$ excess. Without a pre-registered analysis plan, the choice of which mask provides the "load-bearing scientific result" appears post-hoc, undermining the strength and objectivity of the null claim.
*   **Fix:** The abstract and conclusions must give equal weight to both the subsample-mask null and the canonical-mask residual. State explicitly that the null result is mask-dependent and a residual exists on the canonical footprint that is attributed to, but not definitively proven to be, a systematic.

## PAPER-GEM-m1

*   **Classification:** minor
*   **Location:** Sec. III.E (L912-923)
*   **Issue:** The text describes the smaller, adopted variance widening factor of $1.21\times$ as "more conservative" than the upper bound of $1.29\times$, which is incorrect usage. The origin of the $1.21\times$ factor from "leading-order linear propagation" is also opaque.
*   **Fix:** Correct the language to state the $1.21\times$ factor is a less strict estimate than the upper bound. Provide a clear, one-sentence derivation for the $1.21\times$ factor or simply use the well-derived upper bound of $1.29\times$.

## PAPER-GEM-m2

*   **Classification:** minor
*   **Location:** Sec. IX.K (L2816-2840)
*   **Issue:** The discussion of the parity-odd nature of the monopole ($\ell=0$) and even-$\ell$ multipoles is correct but subtle, and appears very late in the paper (Sec. IX.K). This crucial theoretical distinction should be introduced earlier, as it reframes the interpretation of the entire power spectrum analysis and the nature of the monopole systematic.
*   **Fix:** Move the core of the symmetry classification paragraph (Sec. IX.K, L2816-2840) to the introduction or methods section. This ensures the reader understands from the outset which observables test isotropy (odd $\ell$) versus parity (even $\ell$).
