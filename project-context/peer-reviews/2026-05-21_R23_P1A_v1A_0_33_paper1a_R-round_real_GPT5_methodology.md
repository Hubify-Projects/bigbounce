# paper1a R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R23_P1A_v1A_0_33
**Wall time**: 168.0s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=28767, completion=8887, reasoning=7768, total=37654

---

# Review

No blocker-grade findings.

## PAPER-GPT-M1 — MAJOR — §II.C.1 Eq. (Dinf), App. B, §XIV.C

**Issue:** The load-bearing \(e^{-3N_{\rm tot}}\) dilution is not derived for a vacuum-energy contribution. In EC, \(K\propto J^5\propto a^{-3}\), but the standard torsion-induced energy/four-fermion term scales as \((J^5)^2\propto a^{-6}\); changing the exponent from 3 to 6 moves \(N_{\rm tot}\sim92\) to \(\sim46\), undermining the claimed \(N_{\rm tot}\gtrsim60\) erasure tension. The text also says “surplus \(\sim14\) e-folds,” inconsistent with \(92-60\simeq32\).

**Fix:** Derive the dilution exponent from the explicit dimension-4 operator being mapped to \(\rho_\Lambda\), and quote \(N_{\rm tot}\) with an exponent/systematic uncertainty. Remove “definitively erased” unless the \(e^{-3N}\) scaling is proven.

## PAPER-GPT-M2 — MAJOR — §IV Route 2, Eq. after \(\Gamma_{\rm one-loop}^{\rm parity-odd}\)

**Issue:** The R2 one-loop closure is still dimensionally uncontrolled. The manuscript gives two “dimensionless” orderings yielding \(\sim10^{-58}\)–\(10^{-60}\) and \(\sim10^{-33}\), a 25+ order-of-magnitude discrepancy, while \(\theta\)’s normalization and the map to a photon Chern-Simons birefringence angle are not derived.

**Fix:** Canonically normalize \(\theta\), derive the effective photon/ALP Chern-Simons coupling, and compute \(\beta\) from a single dimensionally consistent line-of-sight expression. Otherwise demote R2 to a qualitative Planck-suppression argument.

## PAPER-GPT-M3 — MAJOR — §IV “Scope,” §IV.E Closure summary, §XV Conclusions

**Issue:** The paper admits the four routes are not a complete operator basis and explicitly omits Jackiw–Pi \(R\wedge\tilde R\) and the parity-odd four-fermion partner, but later says R1–R4 “exhaust” the available channels and “close every minimal-ECH dark-energy route.” That is an overclaim relative to the proven scope.

**Fix:** Replace “exhaust/close every” with “close the four enumerated channel-level routes,” or add a complete diffeomorphism-invariant parity-odd/torsion operator basis and close the omitted operators.

## PAPER-GPT-M4 — MAJOR — §IV Route 4, §XII, §XIII, §XV

**Issue:** The ALP birefringence value \(\beta\simeq0.27^\circ\) is a fitted benchmark/consistency point, not a prediction. The claim that \(f_a\sim M_{\rm Pl},\,m\sim H_0\) works “without fine-tuning” contradicts R4’s own statement that \(m_\theta\sim H_0\) relabels the CC tuning; LiteBIRD’s \(0.27/0.03\sim9\sigma\) is only a detection-vs-zero number, not model support against Eskilt \(0.342^\circ\pm0.094^\circ\).

**Fix:** Consistently call \(\beta=0.27^\circ\) a benchmark consistency check, propagate the current \(\beta\) uncertainty and calibration systematics, and remove “without fine-tuning” unless technical naturalness is separated from the dimensionful \(H_0\) tuning.

## PAPER-GPT-M5 — MAJOR — §II.C.1 “Reheating thermal-reset barrier”

**Issue:** The reset argument uses total fermion number density \(n_\psi\sim T^3\) as the torsion source. Minimal EC torsion is sourced by axial spin density \(J^{5\mu}\), and an unpolarized thermal bath has \(\langle J^{5\mu}\rangle=0\) despite large \(n_\psi\).

**Fix:** Recompute the post-reheating source using \(\langle J^{5\mu}\rangle\) and spin-spin correlators. Reframe the barrier as algebraic no-memory/zero mean torsion after reheating, not overwrite by a large \(T^3\) torsion.

## PAPER-GPT-m1 — minor — Abstract, §I, §VI Systematics

**Issue:** The supplied §VI contains no NaMaster methods paragraph; NaMaster validation is only deferred to Paper I(b) while still advertised in this paper. If no P1A result depends on it, this is just scope clutter; if it does, reproducibility is missing.

**Fix:** Either remove NaMaster validation claims from P1A or add a minimal methods pointer: masks/apodization, binning, \(E/B\) purification, mode-coupling correction, covariance/MC count, null tests, and exact companion section/commit.
