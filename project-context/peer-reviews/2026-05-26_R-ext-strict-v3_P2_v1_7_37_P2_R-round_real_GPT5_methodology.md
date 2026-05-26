# P2 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict-v3_P2_v1_7_37
**Wall time**: 145.3s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=33171, completion=8598, reasoning=7634, total=41769

---

No blocker-grade findings.

## PAPER-GPT-M1 — MAJOR

**Location:** Appendix A; Abstract; Sec. SPHEREx forecast  
**Issue:** The paper uses two incompatible local-bispectrum normalizations: the abstract/SPHEREx correctly quote \(B_\zeta^{\rm local}=(6f_{\rm NL}/5)[PP+\mathrm{perms}]\), while Appendix A defines Planck/Komatsu-Spergel as \(c=2\) for \(B_\zeta\). \(c=2\) is the potential-\(\Phi\) convention, not the \(\zeta\) convention; the appendix also incorrectly frames a pure convention change as halving detection significance, even though \(f_{\rm NL}\) and \(\sigma(f_{\rm NL})\) rescale together.  
**Fix:** Rewrite Appendix A in one variable convention only (\(\Phi\) or \(\zeta\)), with explicit conversion factors. Treat \(-35/16\) either as an alternative physical amplitude in the Planck \(f_{\rm NL}\) convention or as a pure reparameterization, but not both.

## PAPER-GPT-M2 — MAJOR

**Location:** Abstract; Secs. `systematics`, `spherex`, `conclusion`  
**Issue:** The advertised post-systematic \(3\)–\(5\sigma\) range is not derived from an explicit propagated budget. Combining listed degradations multiplicatively can push the conservative case below \(3\sigma\), and the claimed SPHEREx null exclusion \(>4\sigma\) is not guaranteed once \(b_\phi\), GR, photo-\(z\), \(\epsilon\), and template uncertainties are all applied.  
**Fix:** Add a systematic-budget table with the exact propagation rule and separate optimistic/central/conservative rows. Downgrade “\(>4\sigma\)” null-disfavoring language to the subset of assumptions where it actually holds.

## PAPER-GPT-M3 — MAJOR

**Location:** Sec. `bayesian`; Tables `tab:bayes` and `tab:gr`  
**Issue:** The Bayes-factor tables mix incompatible calculations. The closed-form delta-prior, narrow-competitor case at \(\sigma=0.7\) gives BF \(=7.00\), but Table `tab:bayes` also reports an \(8\)–\(11\) GR-variation row for the same narrow prior; this is not the same likelihood/prior setup. More generally, drawing GR shifts and reporting median/P(BF>3) is not a Bayes factor unless the nuisance parameters are marginalized inside the evidence before taking the ratio.  
**Fix:** Define one evidence integral \(p(d|M)=\int p(d|\theta,M)\pi(\theta|M)d\theta\) including GR, \(b_\phi\), and survey-performance nuisances, then recompute every BF table from that same setup. Label posterior-predictive BF distributions separately from actual model evidences.

## PAPER-GPT-M4 — MAJOR

**Location:** Sec. `spherex`  
**Issue:** The text says applying the Heinrich Fisher matrix from fiducial \(f_{\rm NL}=0\) to \(f_{\rm NL}=-4.375\) is a shift “of order the parameter uncertainty.” It is not: \(|-4.375|/0.7\simeq6.25\sigma\). This is a nontrivial extrapolation of the Fisher derivatives/covariance.  
**Fix:** Either justify analytically that the bispectrum Fisher covariance and derivatives are effectively independent of \(f_{\rm NL}\) over \(|f_{\rm NL}|\sim4\), or rerun/reproduce the Fisher forecast at the bounce fiducial. Otherwise soften the quoted significance.

## PAPER-GPT-M5 — minor

**Location:** Secs. `benchmark`, `template`; Abstract systematic-budget sentence  
**Issue:** The “\(10^4\) valid coefficient sets” in the polynomial null space are not physically sampled models; they are arbitrary completions of an underdetermined reconstruction from three benchmark triangles. A uniform Euclidean ball of radius 50 in a chosen monomial basis is not an invariant or theory-motivated prior, so the quoted \(r=0.85\pm0.13\) is not a statistically meaningful systematic error bar.  
**Fix:** Present the null-space scan as a stress test only, or define a physically motivated coefficient prior/reconstruction before propagating its scatter into the significance budget.
