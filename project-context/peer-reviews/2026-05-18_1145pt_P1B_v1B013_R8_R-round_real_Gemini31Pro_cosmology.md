# P1B_v1B013_R8 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1145pt
**Wall time**: 69.2s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=17917, completion=8608, reasoning=7927, total=26525

---

## Finding 1: MAJOR
**ID:** PAPER-GEM-B1
**Location:** Table 1B caption vs. Section 3 "Caveats" paragraph
**Issue:** There is a direct contradiction regarding the $\tau$ constraint methodology. The Table 1B caption explicitly lists `lowl.EE` in the likelihood stack, which actively constrains $\tau$. However, Caveat (b) states the chain uses a Gaussian prior on $\tau$ "rather than a free $\tau$ from a low-$\ell$ likelihood". Using both simultaneously constitutes invalid double-counting of the Planck $\tau$ constraint; if only one is used, the manuscript is contradictory.
**Fix:** Remove `lowl.EE` from the caption's likelihood stack if a prior was used, or delete Caveat (b) if the low-$\ell$ likelihood was used instead of the prior.

## Finding 2: MAJOR
**ID:** PAPER-GEM-B2
**Location:** Section 1, "What is NOT in this paper" paragraph
**Issue:** The text claims $f_{\rm NL}=-35/8$ is a "mechanism-independent test prediction," which severely overstates its UV-completion independence. This specific value is an exact prediction strictly for a matter-dominated contracting phase (the minimal matter bounce) and does not apply generically to all bounce mechanisms (e.g., ekpyrotic or string-gas bounces yield entirely different $f_{\rm NL}$ signatures).
**Fix:** Replace "mechanism-independent test predictions" with "matter-bounce specific test predictions" or explicitly scope the $f_{\rm NL}$ value to the matter-dominated contraction phase.

## Finding 3: minor
**ID:** PAPER-GEM-B3
**Location:** Table 1B, Goodness-of-fit decomposition
**Issue:** The reported $\chi^2$ components ($10.6 + 10983.9 + 3043.0$) sum to $14037.5$, but the total is reported as $14037.4$. While this is a standard GetDist rounding artifact (mean of the total $\chi^2$ vs. sum of the means of the individual $\chi^2$s), it presents as an unforced arithmetic error in a technical verification table.
**Fix:** Adjust the least-significant decimal of one component to match the total, or add a brief footnote attributing the $0.1$ discrepancy to GetDist marginalization rounding.

## Finding 4: minor
**ID:** PAPER-GEM-B4
**Location:** Table 1B caption
**Issue:** The parameter nomenclature in the caption's list is ambiguous and inconsistent with the table body. The caption lists "$\log A$" and "$w$", whereas standard Cobaya/GetDist notation requires $\ln(10^{10}A_s)$, and the table body correctly uses $w_0$. "$\log A$" is mathematically ambiguous regarding base and scaling.
**Fix:** Change "$\log A$" to "$\ln(10^{10}A_s)$" and "$w$" to "$w_0$" in the caption's sampled parameter list.
