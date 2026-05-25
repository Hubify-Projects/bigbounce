# P1A R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-25_R-ext_P1A_v1A_0_35
**Wall time**: 314.9s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=28512, completion=10778, reasoning=8899, total=39290

---

## Adversarial Peer Review — Provenance Audit

**Paper:** P1A v1A.0.35 (ECH no-go theorem)  
**Reviewer focus:** Load‑bearing scalars without traceable sources; arithmetic irreproducible from displayed values.

---

### PAPER‑DEE‑M1 (MAJOR) — Irreproducible cross‑check ratio in Route 2 closure
**Location:** §4.2 (Route 2), paragraph after Eq. (4.2)  
**Issue:** The text states a “complementary cross‑check” yields a dimensionless ratio “of order \(10^{-33}\)” using the expression \(\alpha_{\rm em}/(4\pi\cdot M_{\rm Pl}\cdot(\alpha/M)\cdot\beta_{\rm obs})\cdot H_0\).  
- The expression as written has mass dimension \(+1\) (not dimensionless).  
- No arithmetic is shown; plugging the displayed numbers (\(H_0\sim 10^{-33}\,\text{eV}\), \(M_{\rm Pl}\sim 10^{28}\,\text{eV}\), \(\alpha/M\sim 10^{-21}\,\text{GeV}^{-1}\), etc.) does **not** reproduce \(10^{-33}\) in any obvious dimensionless reduction.  
- The paper itself notes the two orderings “differ”, but the \(10^{-33}\) value is unverifiable and likely dimensionally inconsistent.  

**Fix:** Either remove the cross‑check entirely, or provide a dimensionally correct expression and explicit step‑by‑step arithmetic that yields the claimed number.

---

### PAPER‑DEE‑M2 (minor) — Provenance of \(N_{\rm tot}\approx 92\) is contradictory
**Location:** §12.1 (“The Inflationary Suppression Factor”) and Abstract  
**Issue:** The headline number \(N_{\rm tot}\approx 92\) is called “a fitted parameter, not predicted” in §12.1, yet no fitting procedure, dataset, or script is referenced anywhere in the paper or the companion. Appendix B derives \(N_{\rm tot}\approx 94\) from the Planck‑scale hierarchy, and the main text elsewhere treats 92 as a direct consequence of matching \(\rho_\Lambda\). The reader cannot tell whether this number comes from a fit or from the analytic matching, and no JSON/script on disk is cited to reproduce it.  

**Fix:** Remove the “fitted” label and state explicitly that 92 follows from Eq. (12.1) with the quoted parameter values (show the one‑line calculation), or provide a pointer to a companion script that performs the fit.

---

### PAPER‑DEE‑M3 (minor) — Missing inline citation for \(\beta\approx 0.27^\circ\) in Abstract
**Location:** Abstract, sentence beginning “spectator‑ALP birefringence \(\beta\approx 0.27^\circ\)”  
**Issue:** The number \(0.27^\circ\) appears without an immediate reference; the companion paper that hosts the ALP fitting is cited only at the end of the abstract. This makes the value appear unmoored from any traceable source.  

**Fix:** Add a parenthetical citation (e.g., “[Golden2026P1b]”) directly after “\(\beta\approx 0.27^\circ\)”.

---

### PAPER‑DEE‑N1 (nit) — “13 logically‑independent” count asserted without demonstration
**Location:** Abstract and Conclusions  
**Issue:** The paper repeatedly states “13 logically‑independent mechanism‑class constraints” (14 catalog entries minus B8). While the arithmetic is trivial, the claim of logical independence is not justified anywhere; it is simply a count. This is not a scalar that requires a dataset, but as a headline figure it invites scrutiny.  

**Fix:** Either add a one‑sentence justification (e.g., each barrier blocks a distinct mechanism class by construction) or rephrase to “13 constraints (14 catalog entries, with one redundancy)”.

---

### PAPER‑DEE‑N2 (nit) — Unclear status of the \(10^5\) residual fine‑tuning
**Location:** §12.1 and Appendix B  
**Issue:** The paper states that the fine‑tuning is “reparameterized … to \(\sim 10^5\) as sensitivity to \(\Delta N_{\rm tot}\approx 4\) e‑folds”. The number \(10^5\) is order‑of‑magnitude from \(e^{12}\approx 1.6\times 10^5\), but the text does not show this simple arithmetic. A reader unfamiliar with the argument may wonder where \(10^5\) comes from.  

**Fix:** Add a brief parenthetical note: “(\(e^{3\Delta N_{\rm tot}}\approx e^{12}\sim 10^5\))”.

---

**Overall:** No blocker‑grade provenance violation found. The main quantitative results are either derivable from displayed equations or traceable to cited companion papers. The issues above are correctable with minor clarifications.
