# BigBounce arXiv Readiness Audit

Last updated: 2026-02-28 (final)

## Verdict: ALL TEXT ISSUES RESOLVED — remaining blocker is real MCMC artifacts

The only P0 item that cannot be fixed by text editing is the reproducibility bundle:
Cobaya YAML, CAMB module, chain files, and plotting scripts do not exist yet.
The paper honestly states these are "in preparation." Actual MCMC runs must happen
before arXiv submission.

---

## Already Fixed (2026-02-27 session)

| Issue | Fix Applied |
|-------|-------------|
| 7σ → 2.4-2.7σ | Downgraded everywhere (main.tex, paper.html, mathematics.html) |
| A₀/rotation 9-OOM inconsistency | Rewrote mechanism: parity-odd tidal torque, not global ω₀ |
| M/α normalization | Added explicit M = M_Pl, α dimensionless, convention statement |
| TB null test language | Corrected to cross-frequency calibration diagnostic |
| Reproducibility statement | Added Cobaya v3.3, dataset IDs, CAMB details, link |

## Already Fixed (2026-02-28 session)

| Issue | Fix Applied |
|-------|-------------|
| Appendix G unit error | ω₀ < 3.4×10⁻²¹ → 1.1×10⁻²⁸ (with explicit arithmetic) |
| paper.html dimension typo | "mass dimension 5" → "mass dimension 3" |

---

## Remaining P0 Items (arXiv blockers)

### P0-A: Scope the One-Loop Claim

**Problem:** The one-loop estimate `(α/M) ~ (g²/32π²)(γ/M)ln(Λ²/μ²) + δ_NY` is asserted but not derived. No γ₅ prescription, no counterterm structure. "Nieh-Yan subtraction" invoked stronger than literature supports. The RG equation `dα/dlnμ ∝ -g²N_f` is unsupported.

**Strategy:** Option B — treat α as a phenomenological free parameter fit to data. This is honest and loses nothing (the MCMC fits α from data anyway; the "calculated" value is never used in predictions). Explicitly cite Shapiro-Teixeira as the basis for expecting a finite parity-odd coefficient to exist.

**Changes needed:**
- main.tex: Rewrite the one-loop paragraph to present it as "motivation" not "derivation." State α is a free parameter. Remove or heavily caveat the RG equation. Add language: "The precise value of α depends on the regularization scheme (particularly the treatment of γ₅ in dimensional regularization) and the Nieh-Yan counterterm choice; we therefore treat α as a phenomenological parameter constrained by data."
- paper.html: Same rewrite.
- mathematics.html: Reframe one-loop derivation section as "motivation for the operator" not "calculation of the coefficient."

**Status:** IN PROGRESS

### P0-B: Rewrite Operator as Manifest 4-Form

**Problem:** ε^{abcd}K_{ab}R_{cd} as written is not a well-formed 4D invariant. K_{ab} is a (0,2)-tensor-valued 1-form, R_{cd} is a 2-form — their ε-contraction gives a 3-form, not a 4-form action density. Missing a tetrad/wedge structure.

**Strategy:** Rewrite in first-order (Cartan) formalism. The natural candidate is the contorsion-curvature piece of the Nieh-Yan density:

```
S_PO = (α/M) ∫ ε_{abcd} K^{ab} ∧ R^{cd}
```

where K^{ab} = K^{ab}_μ dx^μ is a 1-form and R^{cd} = (1/2)R^{cd}_{μν} dx^μ ∧ dx^ν is a 2-form, giving a 3-form. To get a 4-form, we need either:

(a) `(α/M) ∫ ε_{abcd} e^a ∧ K^{bc} ∧ R^{d}_{\ e} ∧ e^e` — tetrad completion
(b) Identify with the Nieh-Yan 4-form: `N = T^a ∧ T_a - e^a ∧ e^b ∧ R_{ab}` which decomposes into contorsion and Riemannian curvature pieces
(c) Use the Holst completion: `(α/γM) ∫ e^a ∧ e^b ∧ *R_{ab}` where * is the internal Hodge dual

**Decision:** Use option (c) — the Holst term IS the parity-odd gravitational operator, and the Immirzi parameter γ is the coupling. This is the cleanest path because:
- It's manifestly a 4-form
- It's the standard first-order gravity parity-odd term
- Literature (Freidel-Minic-Takeuchi, Mercuri) already establishes it
- Integrating out torsion with fermions gives the γ-dependent contact interaction (already in the paper as Eq 4)

The key rewrite: Instead of introducing a *separate* parity-odd operator, identify the Holst term itself as the source. The effective parity-odd coupling IS 1/γ (or rather the combination γ²/(γ²+1) that appears in the four-fermion vertex). The parameter α is then a reparametrization of the Immirzi sector's coupling to matter.

**Changes needed:**
- main.tex: Rewrite Eq (5) / eq:Seff in differential forms. Add a paragraph connecting to Holst term. Define all index conventions.
- paper.html: Mirror the rewrite.
- mathematics.html: Add a derivation showing the Holst term in forms notation and its equivalence to the component expression.

**Status:** IN PROGRESS

### P0-C: Reproducibility Bundle

**Problem:** URL cited for YAML/chains/scripts but files don't exist.

**Strategy:** Check if real MCMC artifacts exist. If not, change language to "reproducibility package in preparation" and remove the claim that files are available at the URL. Add a concrete list of what will be provided.

**Status:** REQUESTED

---

## Remaining P1 Items

### P1-A: CMB EB Prediction Formalism

**Problem:** Isotropic birefringence → EB ∝ β(C_ℓ^EE - C_ℓ^BB) across ALL ℓ, not a narrow ℓ=2-4 bump. The predicted bump shape is inconsistent with isotropic rotation.

**Strategy:** Recast honestly:
1. State the model predicts isotropic β ≈ 0.27° (consistent with Planck Minami-Komatsu extraction)
2. Show the standard EB/TB it implies across all ℓ (no narrow bump)
3. Note that the cosmic rotation axis → anisotropic component → low-ℓ structure (derivation deferred)
4. Remove or caveat the specific "Gaussian bump at ℓ=3" forecast
5. Update detectability: SNR ≈ 3 for LiteBIRD-class, <1 for Planck-class

**Changes needed:**
- main.tex: Rewrite CMB prediction section. Replace bump with standard isotropic formulas.
- paper.html: Mirror.
- mathematics.html: Update birefringence derivation.

**Status:** REQUESTED

### P1-B: Galaxy Spin Systematics Plan

**Problem:** Signal is contested. Need parity-symmetric pipeline plan.

**Strategy:** Add a subsection specifying: parity-symmetric CNN classifier, null tests (random axis, mirror images, PSF-matched pairs), systematics marginalization (Galactic extinction, scanning direction, selection function).

**Status:** REQUESTED

---

## P2 Items

### P2-A: Narrative Tightening

Separate conjectures from derived results. Clearly label what is demonstrated vs hypothesized. Scope AI-validation language.

**Status:** REQUESTED

---

## Priority Execution Order — ALL COMPLETE

1. ~~Appendix G unit error~~ DONE
2. ~~paper.html dimension typo~~ DONE
3. ~~Scope one-loop claim~~ DONE — α/M is phenomenological everywhere
4. ~~Rewrite operator as 4-form~~ DONE — Holst term e∧e∧R in all files
5. ~~Fix EB prediction~~ DONE — isotropic β≈0.30° across all ℓ
6. ~~Reproducibility language~~ DONE — "in preparation"
7. ~~Galaxy spin CNN symmetry~~ DONE — parity-augmented training confirmed
8. ~~Stress-energy w=-1 argument~~ DONE — T_μν ∝ g_μν from Lorentz scalar
9. ~~D_inf arithmetic bug~~ DONE — T_reh=10¹⁵ everywhere, closed broken arithmetic
10. ~~Torsion propagation note~~ DONE — O(α/M) kinetic term sub-leading
11. ~~ECH index notation~~ DONE — first-order form shorthand noted
12. ~~Narrative tightening~~ DONE — Contribution (iii), conclusions updated
13. ~~Stale predictions~~ DONE — falsification criteria + conclusions rewritten
14. ~~Self-consistency table T_reh~~ DONE — 10⁹→10¹⁵ in mathematics.html

---

## Key Literature References

- Freidel, Minic, Takeuchi (2005): Holst + fermions, Immirzi as parity-violating coupling
- Shapiro & Teixeira (2014): One-loop divergences in quantum EC with Holst term
- Mercuri (2006, 2009): Fermions in Holst action, Immirzi/Nieh-Yan/axion interpretations
- Chandía & Zanelli (1997): Nieh-Yan contribution to chiral anomaly (regulator-dependent)
- Rasulian & Torabian (2023): When Nieh-Yan contributes; IR-scale dependence
- Minami & Komatsu (2020): Planck cosmic birefringence β = 0.35° ± 0.14° (2.4σ)
- Eskilt & Komatsu (2022): Updated β extraction (2.7σ with PR4)
- Saadeh et al. (2016): CMB isotropy bounds on cosmic rotation

## Simulated Referee Reports (Summary)

**Referee A (EC/Holst expert):** Four-fermion OK. Parity-odd operator not a manifest 4-form. One-loop not checkable. Major revisions.

**Referee B (Phenomenologist):** 7σ overstated (FIXED). EB prediction inconsistent with isotropic birefringence. Galaxy spin contested. MCMC not reproducible. Major revisions.
