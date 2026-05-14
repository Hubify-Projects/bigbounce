# P2_v17_28 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Round**: 2026-05-14_2310pt
**Wall time**: 91.6s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=30256, completion=4843, total=35099

---

## PAPER-GPT-B1 — BLOCKER — Appendix A / Abstract convention caveat

**Issue:** The convention discussion is internally inconsistent. Appendix A defines \(B_\zeta=c f_{\rm NL}PP\), so changing \(c=2\to1\) for the same physical bispectrum doubles \(f_{\rm NL}\), while the text also says the Li/Cai-Brandenberger value \(-35/16\) is “equivalently” a full-ordering \(c=1\) result and that detection significance both is convention-independent and halves. Those statements cannot all be true.

**Fix:** Separate “normalization convention” from “missing time-ordering/physical amplitude.” If the physical bispectrum is the same, S/N cannot halve; if the amplitude is actually half, stop calling it a convention and revise the abstract, Appendix A, and Table A.2 accordingly.

## PAPER-GPT-M1 — MAJOR — Sec. Current Data, \(f_{\rm NL}\)–\(n_s\) consistency relation

**Issue:** The sign arithmetic is wrong. With the written equation
\[
f_{\rm NL}=-35/8+\kappa_1(\epsilon-3/2),\quad \kappa_1>0,\quad \epsilon-3/2=(n_s-1)/8<0,
\]
the correction makes \(f_{\rm NL}\) more negative, roughly \([-4.73,-4.40]\), not the quoted \([-4.35,-4.02]\).

**Fix:** Change the sign to \(f_{\rm NL}=-35/8-\kappa_1(\epsilon-3/2)\) or define \(\kappa_1<0\). Then recompute the quoted \(1\)–\(8\%\) interval and propagate it through the significance/Bayes-factor tables.

## PAPER-GPT-M2 — MAJOR — Abstract / Sec. Discussion, joint \((f_{\rm NL},n_{f_{\rm NL}})\) Fisher

**Issue:** The \(9.9\sigma\) SDB joint-Fisher number remains quantitatively unverifiable: the six-bin Fisher inputs are deferred, not on disk, and the implied unmarginalized \(\sigma(f_{\rm NL})\simeq0.114\) is \(6\times\) sharper than the published SPHEREx bispectrum baseline. Hedging it as “illustrative” is not enough while it is still quoted in the abstract.

**Fix:** Remove the \(9.9\sigma\), \(\sigma(n_{f_{\rm NL}})=0.086\), and \(\sigma(f_{\rm NL})=0.44\) numerical claims from the abstract/main forecast until the Fisher matrix and bin inputs are released. Otherwise include the full Fisher table and reproducibility artifact in this paper.

## PAPER-GPT-M3 — MAJOR — Secs. Benchmark/Template/Systematics, error propagation

**Issue:** The significance ranges do not consistently propagate the stated nuisance budget. The “\(5.2\)–\(5.5\sigma\)” optimistic range uses \(r\simeq0.83\)–0.876 but effectively ignores the quoted \(\epsilon\)-shift lower amplitude \(-4.02\), which would push the lower end to \(\sim4.8\sigma\), and it ignores the null-space scatter \(r=0.85\pm0.13\) / range \(0.55\)–1.14.

**Fix:** Provide one multiplicative error-budget table with \(f_{\rm NL}\), \(r\), \(\epsilon\)-shift, photo-\(z\), \(b_\phi\), and GR factors, including correlations where claimed. Quote headline significance only from that table, or explicitly condition the \(5.2\)–\(5.5\sigma\) number on the reference polynomial and no null-space marginalization.

## PAPER-GPT-M4 — MAJOR — Abstract / Introduction / Conclusion, physical-frame inflation comparison

**Issue:** The physical-frame narrative overclaims. “Single-field slow-roll predicts exactly zero” is only the leading squeezed-limit conformal-Fermi statement up to gradient, projection, and finite-squeezed corrections, while the actual SPHEREx forecasts use the standard Planck/local-template \(f_{\rm NL}\) convention. The paper mixes the CFC physical-frame discriminator with a global-template LSS forecast without a clean mapping.

**Fix:** State that the CFC squeezed-limit primordial bispectrum vanishes at leading order, not that any measured local \(f_{\rm NL}\neq0\) “rules out” single-field slow-roll without qualifications. Keep survey forecasts in the Planck/local convention and add a short paragraph explaining how the CFC statement maps, or does not map, onto the LSS estimator.

## PAPER-GPT-M5 — MAJOR — Introduction / Mechanism Independence, ECH fermion caveat

**Issue:** The Hehl-Datta-Mercuri caveat does not close the ECH decoupling gap. The text admits fermions reactivate \(\gamma_{\rm BI}\) through a dim-6 four-fermion operator, then asserts robustness because “contracting-phase mode functions are scalar-dominated,” but gives no bound showing the axial four-fermion density is negligible during the bounce/transfer epoch.

**Fix:** Add an explicit assumption excluding fermion/torsion energy density during contraction and bounce, or quantify a bound on \(\langle\bar\psi\gamma^5\gamma^a\psi\rangle^2\) showing its cubic-action and transfer corrections are below the stated \(f_{\rm NL}\) error budget. Otherwise narrow the claim to scalar-only ECH models and remove “ECH-compatible” robustness language.
