# P1A_v1A027_R7 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1100pt
**Wall time**: 598.7s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=26542, completion=17359, reasoning=16001, total=43901

---

## PAPER-DEE-B1 — Blocking Reproducibility Gap for $N_{\text{tot}} \approx 92$
**Section(s):** §2.3 (around Eq. 2.10), Abstract, §14, Appendix B  
**Issue:**  
$N_{\text{tot}} \approx 92$ (and the derived 120‑OOM hierarchy, the $\Delta N_{\text{tot}}\approx 4$ sensitivity, and the structural‑tension erasure argument) is a **load‑bearing scalar that appears nowhere from a traceable source**. There is no JSON/script/dataset on disk that produces this number. It is reported as a “fitted” parameter but the fitting procedure is neither described nor referenced to a companion script. Without a traceable provenance, the central no‑go and structural‑tension claims collapse.  
**Fix:** Either (a) provide the exact computation script (e.g., a `compute_Ntot.py` with the bracketing of $\rho_\Lambda$, $T_{\text{reh}}$, $M_{\text{GUT}}$, and the exponent inversion) and cite its repository hash, or (b) retract the numerical claim and state the bound qualitatively from first‑principles inequalities.

## PAPER-DEE-B2 — Blocking: $(T_{\text{reh}}/M_{\text{GUT}})^{3/2} \approx 0.03$ Has No On‑Disk Derivation
**Section(s):** §2.3 (“Order‑of‑magnitude matching”), §14  
**Issue:**  
The half‑integer exponent and the numerical match $\approx 0.03$ are described as “dimensional‑analysis‑aesthetic” and “matched at the order‑of‑magnitude level”. No derivation script, thermal partition‑function integral, or phase‑space factor is supplied. This prefactor enters the $N_{\text{tot}}\approx 92$ extraction; without it the sensitivity to $\Delta N_{\text{tot}}\approx 4$ cannot be reproduced.  
**Fix:** Either supply a self‑contained computation notebook that evaluates the prefactor from first principles for the stated $T_{\text{reh}}$, $M_{\text{GUT}}$, or replace the prefactor with a bracketed interval propagated through the $N_{\text{tot}}$ inversion.

## PAPER-DEE-m1 — Major: $H_0 = 67.68 \pm 1.06$ is a MCMC‑dependent Claim with No Supporting Artifact
**Section(s):** Table I, §1, Abstract  
**Issue:**  
The Hubble‑constant value is attributed to companion Paper I(b) but no MCMC chain, `.yaml` configuration, or chain‑diagnostic summary is present in this manuscript’s file tree. The reader cannot verify whether this number comes from the Planck prior alone or from a data combination.  
**Fix:** (a) Append the chain diagnostic table (mean, $\pm 1\sigma$, $\hat R$, $n_{\text{eff}}$) directly to this paper, or (b) remove the numerical posterior and state the qualitative result in words.

## PAPER-DEE-m2 — Major: LiteBIRD $0.73\sigma$ Model‑Discrimination Claim is Inconsistently Stated
**Section(s):** §15, item 2; §7  
**Issue:**  
The conclusion states LiteBIRD will separate the spectator‑ALP $0.27^\circ$ from the Planck/ACT central $0.342^\circ$ at only $0.73\sigma$. However §7 still asserts LiteBIRD “will either confirm a non‑zero $\beta$ at high significance or rule out the spectator‑ALP class”. These two statements are in tension: $0.73\sigma$ cannot rule out the class. The arithmetic appears correct ($0.072/\sqrt{0.03^2+0.094^2}=0.73$), but the interpretation is inconsistent across the paper.  
**Fix:** Reconcile §7 and §15. If the $0.73\sigma$ figure is the official model‑discrimination forecast, remove all language implying a high‑significance exclusion.

## PAPER-DEE-m3 — Minor: $\alpha/M = 10^{-21} \, \text{GeV}^{-1}$ is Traced Only to a Self‑Citation
**Section(s):** §2.2, §4(R4), §13, §A  
**Issue:**  
The critical coupling is “one‑loop motivated” (Eq. 2.7, Ref. [Freidel2005, ShapiroTeixeira2014]) but no numeric script or explicit plug‑in from those references is provided. The birefringence‑bound derivation in §4(R4) and the “22‑36 OOM overshoot” range all depend on this scalar; it should be reproducible with a back‑of‑the‑envelope computation from the cited one‑loop integrals.  
**Fix:** Provide a short supplementary script (or an appendix arithmetic box) showing the conversion from the one‑loop integrals of Freidel/Shapiro to $\alpha/M = 10^{-21} \, \text{GeV}^{-1}$.

## PAPER-DEE-n1 — Nit: Appendix B $M_{\text{Pl}}^5$ vs. $M_{\text{Pl}}^3$ Ambiguity is Documented but Suggests a Non‑Robust Derivation
**Section(s):** Appendix B, Eq. B.3  
**Issue:**  
The text acknowledges that the operator has mass dimension $+1$ and that a factor of $M_{\text{Pl}}^3$ must be inserted by hand to reach dimension $+4$. It then offers both $(\alpha/M) M_{\text{Pl}}^5 \sim 10^{-2} M_{\text{Pl}}^4$ and the “equivalent” $(\alpha/M) M_{\text{Pl}}^3$ rewriting. These two expressions differ by a factor of $M_{\text{Pl}}^2 \sim 10^{38} \, \text{GeV}^2$; they cannot both be correct as a single numerical ansatz.  
**Fix:** Pick one ansatz and propagate it consistently, or state explicitly that the $M_{\text{Pl}}^5$ form is the only one used and delete the conflicting line.
