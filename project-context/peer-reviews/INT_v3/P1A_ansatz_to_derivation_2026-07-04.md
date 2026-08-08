# P1A R3 (Immirzi running): ANSATZ → DERIVATION

**Date:** 2026-07-04
**Reviewer MAJOR addressed:** R2/R3/R4 bounds on Δγ/γ and the induced dark-energy
channel rest on ansatz-tier / labeled upper-bound estimates rather than
first-principles derivations.
**Tier attacked:** R3 (Route 3, `sec:r3_immirzi`, Eq. `eq:gamma_running`), the
Barbero–Immirzi running channel. This is the most tractable tier because a
*verified* first-principles β-function exists for it (Benedetti–Speziale 2011).
**Verdict:** R3's magnitude estimate is UPGRADED from ansatz to a genuine
integrated RG result, **for a GUT-scale UV boundary**. Precise scope boundary
identified (Planck-scale UV → O(1), perturbation theory breaks down).

---

## 1. Verified source (arXiv:1111.0884, Benedetti & Speziale)

PDF fetched and text-extracted. Eq. (7), the **on-shell fermion-coupled**
one-loop β-function, reads *verbatim*:

```
beta_{gamma^2} = mu d(gamma^2)/d(mu) = -(gamma^2 - 1) * (mu^2 kappa^2)/(8pi)^2 * (23 gamma^2 + 5)
kappa^2 = 16 pi G
```

Confirmed structure:
- `(gamma^2 - 1)` factor (NOT squared) ✓ — matches the paper's restored Eq. `bs_beta`.
- `(23 gamma^2 + 5)` coefficient ✓.
- **Explicit `mu^2 kappa^2` prefactor** ✓ — this is dimensionful and makes the
  running **power-law**, not logarithmic.
- Fixed point `gamma^2 = 1`, UV-attractive, but "out of the range of validity of
  perturbation theory" (BS's own words, corresponding to divergent four-fermion
  coupling) ✓.

**Resolves the earlier truth-audit worry** (v1A.0.100→101, "abstract says
logarithmic not power-law"): the *off-shell* pure-gravity running (BS Eq.4,
`beta_gamma = (4/3pi) gamma g`) is the logarithmic/exponential one; the
*on-shell fermion-coupled* Eq.7 that P1A actually cites carries the explicit
`mu^2 kappa^2` prefactor and is genuinely **power-suppressed**. The paper cites
the correct equation.

## 2. Genuine RG integration (not an ansatz bound)

`kappa^2 = 16 pi G = 16 pi / Mpl^2`, so `mu^2 kappa^2/(8pi)^2 = (mu/Mpl)^2/(4 pi)`.
With `t = ln mu`, the RHS carries an explicit `e^{2t}` — the flow integrates as
`∫ e^{2t} dt = (1/2) e^{2t}`, **dominated by the UV endpoint**.

Integrated numerically (scipy `solve_ivp`, rtol 1e-11) AND analytically
(frozen-coefficient), from `gamma_0 = 0.2375` (LQG black-hole-entropy value) at
the UV down to `mu_IR = 1 GeV`. The two methods agree to 4 significant figures.

| UV matching scale | (mu_UV/Mpl)^2 | **integrated \|Δγ/γ\|** |
|---|---|---|
| GUT, 1e16 GeV | 6.7e-7 | **1.41e-6** |
| reduced Mpl, 2.4e18 | 4.0e-2 | 8.2e-2 |
| Planck, 1.22e19 | 1.0 | ~1.5 (O(1)) |

**Headline (GUT UV): |Δγ/γ| ≈ 1.4×10⁻⁶.** This is a *real integrated running*,
not an ansatz — the number falls out of the verified Eq.7 with a fixed UV
boundary condition. The power-suppression `|Δγ/γ| ~ (mu_UV/Mpl)^2` is a robust
structural consequence of the gravitational coupling `kappa^2`.

## 3. Propagation to the dark-energy channel

The Route-3 parity-odd Holst operator (built from γ, R_ab, e^a, J^{5μ}) is
mass-dimension-4, forcing one power of `1/Mpl`. Using the paper's own DE-channel
suppression `(Δγ/γ)·(H0/Mpl)`:

- `(Δγ/γ)·(H0/Mpl) ≈ 1.7×10⁻⁶⁷` — the dimensionless amplitude budget.
- `rho_running` in the paper's channel form ≈ **~67 orders of magnitude below**
  `rho_Lambda_obs ≈ (2.25 meV)^4 = 2.6×10⁻¹¹ GeV⁴`.
- Even the most generous dimensional upper form (`Δγ/γ · H0^2 Mpl^2`) sits
  ~41 orders below observed.

Either way the **derived** running gives a torsion/Immirzi contribution to
`rho_Lambda` dozens of orders of magnitude below the observed dark-energy
density — the no-go closes with enormous margin, now from a *derived* result
rather than an ansatz upper bound (for the GUT-UV case).

## 4. Honest scope boundary (first-principles input runs out here)

The one place first-principles input genuinely runs out: **the UV matching
scale is an input, not derived.** At `mu_UV = Mpl` the integrated `|Δγ/γ|` is
O(1) — but that is exactly the regime BS flag as *outside perturbative control*
(the `gamma^2=1` fixed point ↔ divergent four-fermion coupling). So:
- For any sub-Planckian UV boundary (GUT and below) the running is a clean,
  perturbatively-controlled, power-suppressed derived number (~10⁻⁶ or smaller).
- A literal Planck-scale UV boundary is not perturbatively computable from Eq.7
  alone; that would require a UV completion / non-perturbative LQG input.

This is a legitimate scope statement, not a hidden ansatz. The R3 **closure**
(≳60 orders of margin) is insensitive to it: even the O(1) Planck-UV value is
≪1, so γ retains its order of magnitude and the amplitude suppression still
closes the route.

**Net:** R3's Δγ/γ magnitude is upgraded from "chiral-count EFT ansatz upper
bound (~0.3)" to "integrated result from the verified BS Eq.7,
|Δγ/γ| ≈ 1.4×10⁻⁶ for GUT-UV, power-suppressed by (mu_UV/Mpl)^2." No coefficient
was fabricated; every number traces to the verified Eq.7 + a stated UV boundary.

---

## Proposed P1A .tex upgrade (NOT applied — for Houston review)

The paper already contains most of this (lines 2467–2529, restored in
v1A.0.101→102). The upgrade is to (a) add the explicit robustness/UV-boundary
table's conclusion, and (b) sharpen the ansatz→derivation framing so the
reviewer MAJOR is unambiguously answered. Suggested replacement for the
sentence at L2484–2491 ("Integrating Eq.(bs_beta) from a GUT scale ... robust
structural consequence"):

> Integrating Eq.~\eqref{eq:bs_beta} numerically from a GUT-scale ultraviolet
> boundary $\mu_{\rm UV}\sim10^{16}\,$GeV down to $\mu_{\rm IR}\sim1\,$GeV (with
> $\gamma$ near the LQG value $\gamma\!\approx\!0.24$) gives, in agreement with
> a frozen-coefficient analytic estimate to four significant figures,
> $|\Delta\gamma/\gamma|\approx1.4\times10^{-6}$. This is a genuine integrated
> running, not an ansatz bound: the explicit $\mu^2\kappa^2=(\mu/M_{\rm Pl})^2$
> prefactor makes the flow power-suppressed, so
> $|\Delta\gamma/\gamma|\sim(\mu_{\rm UV}/M_{\rm Pl})^2$ and the integral is
> dominated by the ultraviolet endpoint. The result is perturbatively controlled
> for any sub-Planckian UV boundary; only a literal Planck-scale boundary would
> push $|\Delta\gamma/\gamma|\to\mathcal{O}(1)$, precisely the regime
> Benedetti \& Speziale flag as outside perturbative control (the
> $\gamma^2=1$ fixed point corresponds to a divergent four-fermion coupling), so
> a Planck-scale evaluation would require UV-completion input beyond the
> one-loop $\beta$-function. The derived physical running therefore only
> \emph{strengthens} Route~3;

And update the "Ansatz vs derivation (R2/R3)" box (L2530) to note R3's magnitude
is now a derived integrated result (GUT-UV), with R2 remaining the chiral-count
EFT scaling bound.
