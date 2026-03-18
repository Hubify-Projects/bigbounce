# 03: Hybrid DE Literature Comparison

**Created:** 2026-03-17
**Status:** COMPLETE

---

## The Strategy in the Literature

"Early-universe mechanism + phenomenological late-time DE" is the DEFAULT approach in bouncing cosmology papers. The strategy is to use the bounce for singularity resolution and primordial perturbation generation, then add a separate dark energy sector for late-time acceleration. The two sectors do not interact or derive from the same mechanism.

---

## Key Papers

### 1. Bounce Inflation + CPL (The Direct Comparator)

**Reference:** arXiv:2601.03028, January 2026
**What it does:** Takes bounce inflation and bolts on CPL w(z) = w0 + wa(1-a). Fits to DESI DR2 + CMB + Pantheon+.
**Best-fit:** w0 = -0.919 +/- 0.038, wa = -0.37 +/- 0.12
**DE sector derived from bounce?** NO. CPL is a free parametrization. The bounce modifies the primordial spectrum; the DE is a separate sector.
**Is it more predictive than plain w0waCDM?** NO. The bounce affects primordial perturbations; the DE sector is identical to standard w0waCDM. Sum of two independent models, not a unified framework.

**This is exactly the loophole we rejected.** If we had done this with our ECH framework, we would have produced an equivalent paper.

### 2. Odintsov-Oikonomou Reconstruction Program

**References:** arXiv:2009.09947 (f(R), 2020), arXiv:2010.13580 (Gauss-Bonnet, 2020), arXiv:2109.00345 (Chern-Simons f(R), 2021), Physics of the Dark Universe 35 (2022) (ekpyrotic + GB)
**What they do:** Choose a desired a(t) with bounce + matter + radiation + DE eras, then solve for the f(R) or f(G,T) function that produces it.
**DE sector derived from bounce?** NO. The modified gravity Lagrangian is reverse-engineered from the desired cosmology. This is Lagrangian reconstruction, not first-principles derivation. The f(R) function has at least as many free degrees as the phenomena it explains.
**Community reception:** Understood to be reconstruction, not prediction. Not credited with theoretical unification despite "unification" language in titles.

### 3. Torsion Cosmology + DESI (Direct ECH Comparison)

**Reference:** arXiv:2507.04265, Liu et al., July 2025 (EPJC)
**What it does:** EC framework with torsion parameter alpha. Fits to DESI DR2 + CMB + SNe.
**Result:** alpha = -0.00066 +/- 0.00098 (consistent with zero at < 1 sigma)
**Key finding:** AIC improvement of -5.68 to -6.62 vs LCDM. Reduces S8 tension.
**DE sector derived from torsion?** PARTIALLY — the torsion modification IS the DE modification. But the parameter alpha is freely fit to data. The theory does not predict alpha.
**Critical point:** Torsion parameter is consistent with zero. This CONFIRMS our barriers: torsion effects are negligible at late times.

### 4. LQC + Phenomenological DE

**References:** arXiv:2205.15751 (interacting DE in LQC, 2022), MDPI Universe 8(10) 520 (k-essence DE in LQC, 2022)
**What they do:** LQC bounce + separately added quintessence/k-essence DE sector.
**DE derived from LQC?** NO. The DE field is added by hand. LQC effects diminish at late times.
**Standard approach:** This is the default in LQC cosmology. The bounce resolves the singularity; a separate mechanism handles DE.

### 5. Kaluza-Klein LQC (Most Principled Approach)

**Reference:** arXiv:2508.07962, 2025
**What it does:** Loop-quantizes a Kaluza-Klein cosmology where extra-dimension dynamics produce both inflation and late-time acceleration.
**DE derived from mechanism?** YES — from the extra-dimensional dynamics. More principled than adding DE by hand.
**Cost:** Requires extra dimensions. Not testable.

### 6. Quintom Cosmology After DESI

**References:** arXiv:2404.19437 (Cai, Saridakis, 2024), arXiv:2505.24732 (Cai et al., 2025), arXiv:2511.19994 (review, 2025)
**What they claim:** DESI w-crossing (from w < -1 to w > -1) is naturally explained by quintom models. The quintom bounce involves NEC violation (w-crossing at the bounce); the quintom DE involves w-crossing at late times.
**Connection between bounce and DE quintom?** CONCEPTUAL ONLY. Both involve w-crossing, but at vastly different energy scales (Planck vs meV). No causal mechanism connects them.
**Assessment:** The quintom "unification" is mathematical (same equation structure) not physical (same mechanism).

### 7. Nieh-Yan Teleparallel + Quintom DESI

**Reference:** arXiv:2602.00506, February 2026
**What it does:** Couples DE to the Nieh-Yan density in teleparallel gravity. This stabilizes DE perturbations around w = -1 crossing.
**Connection to our work:** We explored the Nieh-Yan term in Foundation B (topological-shift duality). Their approach differs: they use Nieh-Yan as a perturbation stabilizer, not a DE source.
**DE sector derived from geometry?** NO — the background DE evolution is unaffected by the Nieh-Yan coupling. Only perturbation stability is improved.

---

## Answers to Specific Questions

### What extra degrees of freedom are being added?
In all cases: 1-2 free functions or parameters (w0, wa, or a scalar field potential V(phi)) controlling late-time expansion. These are always independent of the bounce parameters.

### What problem do those extra freedoms solve?
The DESI tension: LCDM (w = -1) is disfavored at 2.8-4.2 sigma by DESI + CMB + SNe combined data. Adding w0wa absorbs this tension.

### Would these have rescued our Paper 1 fit-level claims?
**YES.** Adding w0 and wa to our MCMC would have improved Delta-AIC by ~6-8 points, matching the DESI-preferred dynamical DE. Paper 1 would have claimed "ECH cosmology with dynamical DE fits DESI better than LCDM."

### In what sense is the success real?
The fit improvement is real. Chi-squared decreases. AIC/BIC may improve. The model passes more stringent data combinations.

### In what sense is it no longer a first-principles bounce success?
The fit improvement comes entirely from the w0wa parameters, which are:
- Not derived from the bounce
- Not constrained by the bounce
- Available to any framework (LCDM, inflation, or nothing)
- Not falsifiable as bounce predictions

The bounce word in "bounce + w0wa" adds zero predictive content to the DE sector.

### Is this loophole framework-agnostic across ECH / LQC / generic bounce?
**YES.** The loophole works identically for ECH, LQC, or any bounce framework because the DE sector is completely decoupled from the bounce. Branch I confirmed this: "ships passing in the night, separated by 122 orders of magnitude."

---

## The Underdetermination Problem

Wolf & Ferreira (arXiv:2310.07482, PRD 2023) proved that multiple microphysical models produce the same (w0, wa). Even perfect w0wa measurements cannot identify the underlying DE theory. This means:
- Fitting w0wa tells you nothing about whether the DE is from a bounce, inflation, or vacuum fluctuations
- The phenomenological success is real but fundamentally uninformative about the early universe

Wolf & Read (arXiv:2501.13521, 2025) extended this to show "permanent underdetermination" in both DE and inflationary cosmology. Some model-selection problems are inherently unresolvable from data alone.

---

## The DESI Evidence Itself Is Contested

- **Frequentist:** 2.8-4.2 sigma preference for w0waCDM over LCDM (DESI DR2 + CMB + SNe)
- **Bayesian:** arXiv:2504.15222 and arXiv:2603.05472 find much weaker evidence; Bayesian model comparison modestly favors LCDM
- **Dataset sensitivity:** Results depend on which supernova sample is used (arXiv:2602.11936)
- **Pathological best-fit:** The DESI BAO-only best fit (w0 = 0.016, wa = -3.69) corresponds to physically unreasonable DE (arXiv:2502.08876)

The "dynamical DE" hint may not survive to 5-sigma discovery. Building a research program around fitting this signal carries significant risk of building on sand.

---

## Bottom Line

**Our rejection of the loophole is strongly supported by the literature landscape.** Every paper that combines bounce + DE either:
1. Adds DE by hand (standard approach, no theoretical content)
2. Reconstructs a Lagrangian from desired cosmology (Odintsov-Oikonomou, not predictive)
3. Invokes a conceptual connection that is not causal (quintom)

Nobody derives w(z) from a bounce mechanism. Our systematic A-G investigation confirms this is not an omission in the literature — it is a structural impossibility at current theoretical understanding.
