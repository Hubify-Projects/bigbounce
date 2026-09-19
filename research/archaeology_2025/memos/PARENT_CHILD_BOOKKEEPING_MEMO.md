# Parent–child mass / energy / entropy bookkeeping, and an independent reproduction of Popławski's Einstein–Cartan "universe in a black hole" matter-amplification claim

**Worker:** W5 (2025 legacy-archaeology campaign) · **Date:** 2026-09-18 · **Model:** Fable 5.1
**Status:** COMPLETE — numerical reproduction run; results quoted verbatim from the JSON outputs.

**Artifacts (all under `research/archaeology_2025/outputs/`):**
- `poplawski_reproduction_2026_09_18.py` → `poplawski_reproduction_2026_09_18.json` (ApJ 832:96 system, four parent masses, β scan, Table-I check, Desai–Popławski calibration)
- `poplawski_stiff_mass_2026_09_18.py` → `poplawski_stiff_mass_2026_09_18.json` (arXiv:1103.4192 closed form)

**Sources read in full this session (PDF → text):** arXiv:1410.3881v2 (ApJ 832, 96, 2016; the arXiv stamp reads "v2 26 May 2026" — version pinned), arXiv:1007.0587 (PLB 694, 181), arXiv:1105.6127 (GRG 44, 1007), arXiv:1510.08834 (Desai & Popławski, PLB 755, 183), arXiv:1305.6977 (CQG 31, 065005), arXiv:1103.4192 (arXiv only), gr-qc/9408002 (Hayward, PRD 53, 1938). Abstract verified this session: arXiv:1407.4103 (Hashemi, Jalalzadeh & Ziaie, EPJC 75, 53). BibTeX keys refer to `research/archaeology_2025/bibliography/archaeology_2025.bib` (W2).

**Standing constraints honoured:** no active manuscript touched; Popławski's spin-axis dipole (excluded 2026-09-02) not reopened; Houston's preference for cosmic reproduction is not a prior; no divergence is claimed anywhere below; every growth factor quoted is finite and derived.

---

## 0. Executive summary

1. **"Does the child contain more mass than the parent?" is ill-posed until a mass functional and a slice are named.** The parent has ADM = Bondi = Misner–Sharp-at-the-horizon = M. The child (closed FLRW, compact slices, no spatial or null infinity) has **no** ADM or Bondi mass; its total Misner–Sharp mass over the whole 3-sphere is **exactly zero**; and its naive matter integral E = ∫ρ dV is slice-dependent and not conserved unless p = 0 (§2).
2. **Two non-dynamical geometric facts already produce "amplification" before any physics is added.** With Popławski's own initial condition (closed universe at rest with a_i = r_s), the child's Misner–Sharp mass at its equator is exactly M (so the identification is honest, §3.1), but the naive integral over the full 3-sphere is (3π/2) M c² = 4.71 M c² (§3.2), and after the collapse to the torsion bounce the naive thermal energy is T_max/T_i ≈ 10²⁰–10²⁵ times larger still, with **zero** particle production (§3.3). Neither number is "created energy"; both are the ordinary non-conservation of ∫ρ dV for p ≠ 0 in a non-stationary geometry.
3. **Popławski's ApJ 2016 mechanism reproduces at the equation level.** T_max, τ, |H|_max, T_i, a_min, β_cr, the bounce density (15.4 ρ_Planck) all reproduce to ≤0.3 % (§4.5, JSON `paper_comparison`). The particle-production ansatz K = β(κε̃)² with β slightly below β_cr = 1/929.09 does produce a finite plateau of nearly constant T and nearly constant H = 7.40×10⁴³ s⁻¹ — an inflation-like phase — as claimed.
4. **But the amount of matter is not predicted; it is dialled.** The production e-fold count is a one-parameter family, N_e ≈ 1.11 (1 − β/β_cr)^(−0.52) (JSON `efolds_vs_b_powerlaw`), diverging as β → β_cr. The "enormous amount of matter" (factor ≥ 10³⁰ in particle number for a stellar parent) is a *requirement* read off from our universe's Λ and T_eq (his eqs. 33–37), and β is then chosen to be within 0.3 % of β_cr to deliver it. Nothing in the theory fixes β.
5. **Three of his quantitative statements do not reproduce as printed:** (i) the ApJ text's "t_infl depends on τ(β_cr − β)^(−1)" — we find exponent −0.52 ± 0.02, and his own numerical paper's Table I is consistent with −1/2, not −1; (ii) Desai & Popławski's "about 60 e-folds" for β = 1/929.25 — with their exact parameters we reproduce the end-of-acceleration time 1.33×10⁻⁴² s to 0.1 % but obtain **97.9** e-folds, which is also what their own H ≈ 7.4×10⁴³ s⁻¹ × 1.33×10⁻⁴² s implies; (iii) their Table I bounce counts require a one-bounce escape threshold of ≈19 e-folds, whereas the ApJ paper's own eqs. 36–37 give 23.0 for the stellar initial condition it states (we get 2, 3, 4, 7, 13 bounces where they print 1, 2, 3, 5, 10). Full list in §7.
6. **Is there an invariant amplification ratio? Not one that compares parent to child.** The only slicing-independent child-side quantity is the comoving particle number / entropy, N ∝ (aT)³; its growth factor A_N = e^(3 N_e) is a genuine invariant of the child's history *but it is a function of the free parameter β*, and it never involves the parent mass. The parent mass enters only through the *initial* particle number ∝ M^(3/2). The ratio (child rest mass in the dust era)/(parent M) is well defined in exact FLRW but is fixed by β and by the assumed conversion of relativistic particles into rest mass — a model choice, not an invariant of the geometry (§4.7). In the older stiff-EOS paper (arXiv:1103.4192) the analogous ratio is m_max/M = (128/27)^(1/2) m_n M/m_Pl² ∝ M — a *different* dependence on M for the *same* parent, which is itself the proof that the "amplification factor" is model-dependent (§5).
7. **One-line answer to "can the daughter contain vastly more proper matter than the parent's mass?":** Yes in the sense that the child's comoving particle number and dust-era rest mass can exceed M by any factor one likes, because (a) the child's total gravitational mass is zero regardless, and (b) the excess is set by a free production coefficient (or by an assumed energy→rest-mass conversion), not by the parent. It is **not** a prediction of Einstein–Cartan theory, and it does **not** violate ∇_μT^{μν} = 0 (§4.9, §6).
8. **New falsifiable prediction for BigBounce: none** (§6.5).

---

## 1. Which "mass" on the parent side

All four standard notions are defined for a collapsing spherical star in an asymptotically flat spacetime; they coincide in the cases relevant here.

| Quantity | Where defined | Definition (G = c = 1) | Value for Schwarzschild / Oppenheimer–Snyder |
|---|---|---|---|
| ADM mass M_ADM | spatial infinity i⁰ | surface integral of the metric's 1/r fall-off at i⁰ (standard: Arnowitt–Deser–Misner; textbook Wald 1984 ch. 11, MTW §20.2 [section numbers from memory — W2 to confirm]) | M (conserved for all time; the collapse does not change it) |
| Bondi mass M_B(u) | null infinity ℐ⁺ | limit of the Misner–Sharp/Hawking mass along outgoing null cones; non-increasing in retarded time u | M for a spherically symmetric collapse (no gravitational radiation in spherical symmetry; Birkhoff) |
| Misner–Sharp mass m(r) | quasi-local, any sphere | m = (r/2)(1 − ∇r·∇r), r the areal radius (Misner & Sharp 1964, `MisnerSharp1964`; Hayward 1996 eq. 1, `Hayward1996`, verified) | M for every sphere in the exterior vacuum; m = (4π/3)ρ r³ inside a uniform-density (OS) interior; m(r_star) = M at the surface |
| Horizon / irreducible mass | at the apparent/event horizon | m = r_h/2, equivalently M_irr = (A/16π)^(1/2) for non-rotating holes | M |

Facts used below (all from Hayward 1996, verified this session): m reduces to the ADM energy at i⁰ and to the Bondi–Sachs energy at ℐ⁺ (abstract); a sphere is **trapped iff m > r/2 and marginal iff m = r/2** (abstract); in the small-sphere limit m → (4π/3)ρ r³ (abstract); the Kodama current is conserved with charge m (abstract; Appendix B), which is what makes m the right quasi-local quantity to track through a spherical collapse even without a timelike Killing vector.

**Dimensional check.** m = (r/2)(1 − ∇r·∇r): ∇r·∇r is dimensionless, so [m] = [length] = [G M/c²] ✓; restoring units, m_phys = (c² r/2G)(1 − ∇r·∇r).

**Bottom line for the parent:** a non-rotating parent has one unambiguous number, M, and it is simultaneously its ADM mass, its Bondi mass, its horizon mass, and the Misner–Sharp mass of its horizon sphere.

## 2. Which "energy" on the child side

Take a closed (k = +1) FLRW child, ds² = −dt² + a(t)²[dχ² + sin²χ dΩ²], 0 ≤ χ ≤ π, with a perfect fluid (ρ, p).

### 2.1 The naive matter integral and its scaling

On a constant-t slice the proper volume is V = 2π² a³ (standard; e.g. Popławski ApJ eq. 30 text, and any GR textbook), so

E_matter(t) ≡ ∫_Σ ρ dV = 2π² ρ(t) a(t)³.

The continuity equation ∇_μT^{μ0} = 0 for FLRW is ρ̇ + 3H(ρ + p) = 0 (standard; MTW §27.4 / Wald §5.2 [from memory]). For p = wρ it integrates to ρ ∝ a^(−3(1+w)), hence

- dust (w = 0): E_matter ∝ a⁰ — constant;
- radiation (w = 1/3): E_matter ∝ a⁻¹ — *decreases* on expansion, *increases* on contraction;
- vacuum (w = −1): E_matter ∝ a³;
- stiff (w = 1): E_matter ∝ a⁻³.

Only for dust is ∫ρ dV a constant of motion. For everything else the change is exactly the p dV work: d(ρV) = −p dV. That is not creation or destruction of energy; it is the statement that "energy of the matter alone" is not the conserved quantity when the geometry does work on the matter.

### 2.2 The Misner–Sharp mass inside comoving radius χ, and its value for the full 3-sphere

Areal radius r = a sin χ. With ∇r·∇r = −ṙ² + (∂_χ r)²/a² = −ȧ² sin²χ + cos²χ,

m(χ) = (r/2)(1 − cos²χ + ȧ² sin²χ) = (a sin χ/2)(sin²χ + ȧ² sin²χ) = (a sin³χ/2)(1 + ȧ²).

The Friedmann equation for k = +1 is (ȧ² + 1)/a² = (8π/3)ρ, so 1 + ȧ² = (8π/3)ρ a² and

**m(χ) = (4π/3) ρ (a sin χ)³ = (4π/3) ρ r³.**   (dimensional check: [ρ r³] = mass ✓)

Two consequences:
- **m(π) = 0.** The Misner–Sharp mass of the *entire* closed universe vanishes identically (the antipodal point has r = 0). This is the quasi-local form of the standard statement that a closed universe has zero total (matter + gravitational) energy; Popławski himself proves the same thing with the Einstein pseudotensor in CQG 31, 065005 (arXiv:1305.6977, verified this session: "the energy and momentum of the closed Universe are equal to zero").
- **m over the full sphere ≠ ∫ρ dV.** The naive integral 2π²ρa³ is positive and finite; the gravitational mass is zero. The difference is the (negative, non-localizable) gravitational binding energy. No additive decomposition "matter + gravity" is unique (MTW §20.4, "Why the energy of the gravitational field cannot be localized" [from memory]).

### 2.3 Why there is no conserved total energy in FLRW

A conserved energy requires a timelike Killing vector ξ so that J^μ = T^{μν}ξ_ν is conserved; FLRW with ȧ ≠ 0 has none (its isometry group is purely spatial). ∇_μT^{μν} = 0 holds (four equations, one of which is the continuity equation above), but a covariantly conserved *tensor* does not integrate to a conserved *scalar* without a Killing field. This is textbook (Wald 1984 §4.3 / §11.2; MTW §19–20 [from memory — W2 to confirm]). The dump's Galaxies-journal citation [8] (Elizalde 2026, resolved by W2) is on-topic but is not needed; the statement is standard.

## 3. The only comparisons that are meaningful

State plainly: **the question "does the child contain more mass than the parent" is well-posed only after choosing (a) or (b) below.** Popławski's papers, and the 2025 notes, silently use (b).

### 3.1 (a) Misner–Sharp mass on both sides at the same 2-sphere

The parent's horizon is a marginally trapped sphere with m = r/2 = M. In the Oppenheimer–Snyder construction (MTW §32.4 [from memory]) the interior is a *cap* χ ≤ χ₀ of closed FLRW dust matched to Schwarzschild at the star's surface, and the matching condition is precisely m(χ₀) = (4π/3)ρ(a sin χ₀)³ = M. So on the only sphere both sides share, the two masses agree by construction.

Popławski's initial condition (ApJ eq. 16 text) is: the closed universe is momentarily at rest, ȧ = 0, at a = a_i = r_s = 2GM/c². Evaluate m at the equator χ = π/2 with ȧ = 0: from §2.2, m(π/2) = a_i/2 = GM/c² → **m_equator = M exactly** (JSON `parent_masses.*.misner_sharp_mass_equator_over_M` = 1.0 for all four parents). Also, with ȧ = 0 the equator satisfies m = r/2, i.e. it is a marginal (minimal) surface — the throat. So his identification of "the universe's radius at turnaround" with "the Schwarzschild radius" is exactly the statement that the child's equatorial sphere carries the parent's Misner–Sharp mass. This is the honest, invariant parent–child link. It is also the only place M enters his model.

### 3.2 (b) The naive integral ∫ρ dV over the child's whole slice

With κε a_i²/3 = 1 at turnaround (his eq. 16), ε_i = 3c⁴/(8πG a_i²), and

E_i = ε_i · 2π² a_i³ = (3π/4) c⁴ a_i/G = (3π/2) M c².

**The child's naive energy is already 4.71 M c² at the instant of "formation," with nothing having happened** (JSON `E_thermal_formation_over_Mc2` = 4.712388980384690). The factor 3π/2 = (2π²a³)/((4π/3)a³) is just the ratio of the 3-sphere's volume to the volume of the flat ball whose surface is the equator. Anyone quoting a "child/parent mass ratio" without saying which of (a) or (b) they mean is already off by this factor before any dynamics.

### 3.3 The blueshift factor during collapse

Between formation (a_i, T_i) and the torsion bounce (a_min, T_max), with no particle production (aT = const, his eq. 14), the naive thermal energy scales as E ∝ a⁻¹, so

E_thermal(bounce)/E_thermal(formation) = a_i/a_min = T_max/T_i.

JSON `parent_masses.*.E_thermal_bounce_over_formation`: **1.44×10²⁰ (10 M_☉), 1.44×10²¹ (10³ M_☉), 4.55×10²² (10⁶ M_☉), 4.55×10²⁴ (10¹⁰ M_☉).** Meanwhile the *effective* source that gravitates, ε̃ = ε − αn_f², is by definition **zero** at the bounce (`E_effective_at_bounce` = 0.0), and the total Misner–Sharp mass is zero throughout. This is the cleanest demonstration in the lane that "energy in the child" is not a bookkeeping quantity one can compare to M: a factor 10²⁰ appears with no source term at all.

### 3.4 (c) Genuine sources show up in the continuity equation

Any real production process modifies ρ̇ + 3H(ρ + p) = 0 to ρ̇ + 3H(ρ + p) = Γ-term, equivalently changes the comoving particle number N = n a³ V_comoving. That is what Popławski does (his eq. 41–42) and it is the *only* thing in his model that is not slice bookkeeping. Whether it "creates energy" is answered in §4.9: in his construction it does not, because the source is the gravitational sector and the total is zero before and after.

---

## 4. Reproduction of Popławski, ApJ 832:96 (2016), arXiv:1410.3881v2

### 4.1 The Einstein–Cartan Friedmann equation and the bounce density

His eqs. (9)–(10): a spin fluid of unpolarized fermions is equivalent (after averaging the last term of his eq. 6) to a perfect fluid with

ε̃ = ε − α n_f²,  p̃ = p − α n_f²,  α = κ(ħc)²/32,  κ = 8πG/c⁴,

and the closed-FLRW constraint is

**(ȧ/c)² + 1 = (κ/3)(ε − α n_f²) a².**   (his eq. 10; identical in form to 1007.0587 eq. 10 and 1105.6127 eq. 1 with ε_S = −κs²/4, s² = (ħc n)²/8)

Dimensional check: [κ] = m J⁻¹; [ε] = J m⁻³; [κ ε a²] = 1 ✓. [α] = m J⁻¹ · J² m² = J m³; [α n_f²] = J m³ · m⁻⁶ = J m⁻³ ✓ (an energy density). Coupling constant: α = κ(ħc)²/32 = 6.4864×10⁻⁹⁶ J m³ (JSON `derived.alpha_J_m3`).

Thermal content (his §4, standard Bose/Fermi kinetic equilibrium): ε = h_* T⁴, n_f = h_nf T³, with h_* = (π²/30) g_* k_B⁴/(ħc)³, h_nf = (ζ(3)/π²)(3/4)g_f k_B³/(ħc)³, g_* = g_b + (7/8)g_f. Standard-model content g_b = 28, g_f = 90 (his choice, from his ref. [18], Rich 2001 — not fetched; flagged as PAPER input).

Bounce (H = 0, k negligible): ε = α n_f² ⇒ **T_max² = h_*/(α h_nf²)**. Substituting the coefficients gives his eq. (20), T_max = (2π⁵/15)^(1/2) g_*^(1/2)/(ζ(3)(3/4)g_f) · T_P; the script checks the two forms agree to 10⁻¹².

Numbers (JSON `derived`): **T_max = 1.1524×10³² K = 0.813 T_Planck** (paper 1.15×10³²; ratio 1.0021). Bounce density: ρ_max = h_* T_max⁴/c² = **7.92×10⁹⁷ kg m⁻³ = 15.37 ρ_Planck** (1105.6127 eq. 14 states 15.4 ε_Pl; reproduced). This is the *thermal* density; the effective gravitating density ε̃ is zero there. Note the bounce is above the Planck density, which Popławski acknowledges (1105.6127 §2; ApJ §8 argues classical spacetime may persist). Characteristic time τ = (α h_nf²/c)(3/κh_*³)^(1/2) = **4.7507×10⁻⁴⁵ s = 0.0881 t_P** (paper 4.75×10⁻⁴⁵); **|H|_max = (4/27)^(1/2)/τ = 8.10×10⁴³ s⁻¹** (paper 8.1×10⁴³).

Stellar check with his a_i = 10⁴ m (JSON `stellar_check`, `paper_comparison`): T_i = (3/(κ h_* a_i²))^(1/4) = **1.375×10¹² K** (paper 1.38×10¹²); a_min = a_i T_i/T_max = **1.193×10⁻¹⁶ m** (paper 1.19×10⁻¹⁶); ã_i/a_i required by eq. (37): **9.99×10⁹** (paper "> 10¹⁰"). Everything in his §5 reproduces to ≤ 0.3 %.

### 4.2 The particle-production ansatz

- **Starting point (his eq. 39, attributed to his ref. [34], Beilin et al., Sov. Phys. JETP 51, 1045 (1980)):** for a strong field in GR the local production rate of massive spin-1 particles is (1/√−g) d(√−g n₁)/dt = (c/288π) P², P the Ricci scalar. [UNVERIFIED — not fetched this session; W2 did not resolve Beilin et al.; the deeper formalism is Parker 1969 (`Parker1969`, verified by W2) and Zel'dovich–Starobinsky 1972 (`ZeldovichStarobinsky1972`, W2 lower-confidence; cited here only via Popławski's own citation).] Dimensional check of the form: [c P²] = m s⁻¹ · m⁻⁴ = m⁻³ s⁻¹ ✓ (a number-density rate). The coefficient 1/288π is never used; it is absorbed into β.
- **Generalization (his eq. 40–41):** (1/a³) d(a³n₁)/dt = cK with K a curvature/torsion scalar of dimension m⁻⁴.
- **Problem he notices (text after eq. 44):** for FLRW, P = −κ(ε̃ − 3p̃) = −2κα n_f² does **not** vanish at the bounce, so the Beilin-type rate ∝ P² would keep producing particles at T = T_max and push T above T_max, making ȧ² < 0. Rather than derive K from QFT in Riemann–Cartan spacetime (which he says "ultimately" should be done), he **posits the simplest scalar that vanishes at the bounce**:
- **Ansatz (his eq. 45): K = β (κ ε̃)²**, β > 0 a dimensionless free constant. [κε̃] = m⁻² so [K] = m⁻⁴ ✓.
- **Modified continuity equation (his eq. 42):** writing n₁ = h_n1 T³ (h_n1 with g_b1 = 9: W±, Z) and substituting,

  **ȧ/a + Ṫ/T = cK/(3 h_n1 T³) = cβ(κε̃)²/(3 h_n1 T³).**

  This replaces d(aT)/dt = 0. Implicit assumption: the produced W/Z bosons thermalize instantly at the common T so that every species keeps n ∝ T³ (he writes n₁(T) = h_n1T³ without comment). He then **keeps the Friedmann constraint (17) with thermal ε(T)** and states that his eq. (11) "must be modified" — i.e. the acceleration equation, not the constraint, absorbs the production (see §4.9).
- **Dynamics (his eq. 47):** near the bounce with k negligible, (ȧ/a)[1 − x] = −Ṫ/T with x ≡ 3β(ȧ/a)³/(c³ h_n1 T³). In an expanding phase x < 1 is required (else T would grow forever: eternal inflation). x(T) has its maximum at T = T_max/√2, giving **β < β_cr = (√6/32) h_n1 h_nf³ (ħc)³/h_*³ = 1/929.09** (his eq. 49–50, "≈ 1/929"; Desai–Popławski print 1/929.0915; JSON `derived.one_over_beta_cr` = 929.0916). I re-derived β_cr independently from the stall condition in my own dimensionless variables (below) and the two agree to 10⁻¹⁰ (`beta_cr_rederived_from_stall`).
- **The inflation claim (his §7):** for β slightly below β_cr, when T reaches T_max/√2, x ≈ 1 ⇒ Ṫ ≈ 0 ⇒ ȧ/a ≈ c(κε̃/3)^(1/2) = const at ε̃ ≈ h_*³/(8α²h_nf⁴): exponential expansion at constant T. Its duration "depends on τ(β_cr − β)^(−1)"; in a one-bounce scenario eqs. (37) and (54) *require* H t_infl ≳ 23.

### 4.3 What exactly he claims about the daughter's matter content, and what it depends on

Verbatim structure of the argument (his §6, eqs. 31–38):
1. A closed universe with matter mass M_univ = ρV and Λ expands forever iff **D > 2/(3√Λ)**, D ≡ 4GM_univ/(3πc²) (his eq. 33, attributed to Lord 1976 [UNVERIFIED — textbook not fetched]; **derived independently in §4.6 below**).
2. Using T_eq = 8820 K and Λ/κ = 5.24×10⁻¹⁰ Pa (his ref. [18]; PAPER inputs), and a_eq T_eq = ã_i T_i, this becomes a condition on the invariant aT after production: **ã_i/a_i > 10¹⁰** for the stellar a_i = 10⁴ m (his eq. 37; ours 9.99×10⁹, JSON `required_ratio_eq37`). Equivalently the particle number and entropy must grow by (ã_i/a_i)³ > 10³⁰.
3. If β is too small the child recollapses, bounces again with more particles, and so on; "after a finite number of cycles" D satisfies (33) and the last bounce is "the big bang." Desai–Popławski Table I gives the cycle count vs β/β_cr.
4. If β ≲ β_cr the whole 10¹⁰ is delivered in one inflationary plateau with H t_infl ≳ 23.

So the claim is: *for a suitable β the child acquires enough matter (≥ 2×10⁵³ kg, §4.6) to become a Λ-dominated, ever-expanding universe like ours.* **What it depends on:** (i) the free coefficient β (everything), (ii) the initial aT set by the parent via a_i = r_s (weakly: only the *required* N_e depends on it, §4.5), (iii) the number of cycles if β is not near-critical, (iv) the instant-thermalization and single-temperature assumptions, (v) the ansatz K ∝ ε̃² itself.

### 4.4 Numerical setup (script) and how the parent mass enters — assumptions stated

Dimensionless variables: θ = T/T_max, N = ln(a/ℓ), ℓ = cτ = 1.4242×10⁻³⁶ m, time in units of τ, b = β/β_cr. Then his eqs. (17) and (42) become exactly

- **h ≡ τ ȧ/a = ± [F(θ) − e^(−2N)]^(1/2),  F(θ) = θ⁴(1 − θ²)**  (the e^(−2N) is the k = +1 term);
- **d ln θ/dN = −1 + G(θ)/h,  G(θ) = 8 b θ⁵(1 − θ²)².**

Derivation: κε̃/3 = (κh_*T_max⁴/3)θ⁴(1−θ²) and (c²κ/3)h_*T_max⁴ = 1/τ² (since |H|_max² = (4/27)/τ² at θ² = 2/3 — this is how his eq. 25 fixes τ); the production rate becomes cβκ²ε̃²/(3h_n1T³) = (3β/(c³τ³h_n1T_max³)) θ⁵(1−θ²)²/τ and the bracket 3β/(c³τ³h_n1T_max³) equals 8b because max_θ θ³(1−θ²)^(3/2) = 1/8 at θ² = 1/2. The stall variable is x = 8bθ³(1−θ²)^(3/2), so x_max = b — his eq. (48) in our units.

Invariants tracked: aT ∝ (particle number)^(1/3) ∝ (entropy)^(1/3); production e-folds N_e ≡ ln[(aT)_after/(aT)_before] = ∫x dN.

**How the parent mass enters (ASSUMPTION A1):** exactly as in his §5 — the closed universe starts contracting from rest at a_i = 2GM/c², so T_i = (3/(κh_*a_i²))^(1/4) and the initial invariant is (aT)_0 = a_iT_i ∝ M^(1/2). §3.1 shows this is equivalent to "the child's equatorial Misner–Sharp mass equals M." Nothing else about the parent (its spin, its formation history, the collapse being a cap rather than a full sphere) enters. Assumptions A2–A6 are listed in the JSON `provenance.assumptions`: standard-model g's; production active in contraction and expansion (his §7 says so); instant thermalization; constraint kept with thermal ε; contraction started at θ = 10⁻³ where x ≈ 8×10⁻⁹.

Integration: `scipy.integrate.solve_ivp` (DOP853, rtol 10⁻⁹) in N through contraction to θ = 1 − 10⁻⁷, then expansion from the same a; acceleration bookkeeping via ä/a = H²(1 + d ln H/dN); end of acceleration = last sign change. Escape test per cycle against (aT)_esc from §4.6.

### 4.5 Results (quoted from `poplawski_reproduction_2026_09_18.json`)

**Closed-form comparison (`paper_comparison`):**
```
T_max: paper 1.15e32   ours 1.1524e32   ratio 1.0021
tau:   paper 4.75e-45  ours 4.7507e-45  ratio 1.00015
H_max: paper 8.1e43    ours 8.1020e43   ratio 1.00024
T_i (a_i=1e4 m): paper 1.38e12  ours 1.3753e12  ratio 0.9966
a_min (a_i=1e4 m): paper 1.19e-16  ours 1.1934e-16  ratio 1.0029
1/beta_cr: paper ~929 (DP: 929.0915)  ours 929.0916
eq.37 ratio: paper 1e10  ours 9.988e9  -> required one-bounce e-folds 23.02
rho_bounce/rho_Planck: GRG-2012 15.4  ours 15.37
```

**Production e-folds per cycle vs b = β/β_cr (`efolds_vs_b`, stellar a_i; N_e is independent of a_i to 6 digits — confirmed across the four parents):**
```
b=0      Ne=0.000   A_N=1
b=0.5    Ne=0.919   A_N=1.6e1
b=0.757  Ne=1.888   A_N=2.9e2
b=0.9    Ne=3.462   A_N=3.2e4    no T-plateau
b=0.965  Ne=6.340   A_N=1.8e8    plateau 2.6 e-folds, H=7.42e43 s^-1
b=0.984  Ne=9.658   A_N=3.8e12
b=0.99   Ne=12.36   A_N=1.3e16   plateau 9.2 e-folds
b=0.996  Ne=19.83   A_N=6.9e25   plateau 16.7 e-folds, t_end_accel=2.81e-43 s
b=0.999  Ne=40.13   A_N=1.9e52
b=0.9998 Ne=90.27   A_N=4.1e117
b=0.99995 Ne=181.0  A_N=6.0e235
b=1.0, 1.05: expansion never leaves the plateau within 400 e-folds (eternal inflation)
```
Of each N_e, 0.45–0.49 e-folds come from production during the *contraction*; the rest from the expansion plateau. Power-law fit on b ∈ [0.9, 0.99995]: **N_e ≈ 1.107 (1 − b)^(−0.517)** (`efolds_vs_b_powerlaw`). The plateau Hubble rate is **7.40×10⁴³ s⁻¹** for every b (it is fixed by θ = 1/√2, not by β), so t_infl = N_e/H ∝ (1 − b)^(−1/2), **not** (β_cr − β)^(−1) as the ApJ text states after eq. (54).

**Desai–Popławski calibration (`desai_poplawski_calibration`; their β = 1/929.25, a₀ = 10⁻²⁷ m, T₀ = 0.99 T_max, expansion only):**
```
beta/beta_cr = 0.99983
e-folds bounce -> end of acceleration: 97.95     (paper: "about 60")
t at end of acceleration: 1.3286e-42 s           (paper: 1.33e-42 s)
```
The time reproduces to 0.1 %; the e-fold count does not. Their own figures (H roughly constant, Fig. 2) with H = 7.4×10⁴³ s⁻¹ × 1.33×10⁻⁴² s = 98 e-folds are consistent with our number, not with 60. Either their "60" counts from a later starting point they do not define, or it is an error; we cannot tell from the text.

**Table I (`table_I_reproduction`, bounces before Λ-escape, stellar a_i = 10⁴ m):**
```
b=0.996: paper 1  ours 2
b=0.984: paper 2  ours 3
b=0.965: paper 3  ours 4
b=0.914: paper 5  ours 7
b=0.757: paper 10 ours 13
```
Their counts are what one gets if the one-bounce escape threshold is ≈ 18.9–19.0 e-folds; the ApJ paper's own eqs. (36)–(37) give 23.0 for the stated a_i = 10⁴ m. Their Table I does not state its initial condition. The *relative* pattern (1 : 2 : 3 : 5 : 10 ≈ N_e(0.996)/N_e(b)) is reproduced and is itself evidence for the (1 − b)^(−1/2) law: under a (1 − b)^(−1) law b = 0.757 would need ≈ 60 bounces, not 10.

**Parent-mass sweep (`parent_masses`; all densities identical because T_max is content-only):**
```
M/M_sun  a_i [m]    T_i [K]    a_bounce [m]  E_bounce/E_form  N_form     S_BH [k_B]  S_child,form/S_BH  req.Ne  b_req
10       2.954e4    8.00e11    2.05e-16      1.44e20          2.5e59     1.05e79     9.7e-20            22.48   0.99687
1e3      2.954e6    8.00e10    2.05e-15      1.44e21          2.5e62     1.05e83     9.7e-21            20.18   0.99613
1e6      2.954e9    2.53e9     6.49e-14      4.55e22          8.0e66     1.05e89     3.1e-22            16.73   0.99443
1e10     2.954e13   2.53e7     6.49e-12      4.55e24          8.0e72     1.05e97     3.1e-24            12.12   0.98962
bounce density (all): 7.924e97 kg m^-3 = 15.37 rho_Planck; Misner-Sharp equator/M = 1.0; full 3-sphere = 0; E_form/(Mc^2) = 4.712; E_eff(bounce) = 0
```
Per-mass runs at b = 0.9, 0.99, 0.996 and at b_req (the b that delivers exactly the required N_e in one cycle; the `bounces_to_escape` field flips between 1 and 2 at b_req because it sits on the threshold by construction — e.g. 10 M_☉: Ne 22.4826 vs required 22.4831). Sample, 10 M_☉ at b_req = 0.99687: N_e = 22.48, A_N = 1.96×10²⁹, e-folds bounce→end of acceleration 22.64, t_end = 3.17×10⁻⁴³ s, H_plateau = 7.41×10⁴³ s⁻¹, E_thermal(θ = 0.1)/E_thermal(bounce) = 4.6×10²⁷, N_particles after = 4.95×10⁸⁸, S_child after = 1.99×10⁸⁹ k_B = 1.9×10¹⁰ S_BH(parent).

**Does the run reproduce his numbers?** Section 5 (no production): yes, all of them. Section 6–7 (production): the *qualitative* mechanism (finite plateau of constant T and H for b just below 1, eternal for b ≥ 1, cyclic for small b) reproduces; the *quantitative* statements about e-fold counts and scaling do not (see §7).

### 4.6 The escape condition, derived (so eq. 33 need not rest on an unfetched textbook)

Matter era with Λ (his eq. 32): (ȧ/c)² + 1 = D/a + Λa²/3. No recollapse iff f(a) = D/a + Λa²/3 − 1 > 0 for all a > 0. f is minimized at a³ = 3D/(2Λ), where D/a + Λa²/3 = (3/2)D/a = (3/2) D (2Λ/3D)^(1/3). Requiring this > 1 gives D² > 4/(9Λ), i.e. **D > 2/(3√Λ)** ✓ (his eq. 33). With D = 4GM_univ/(3πc²): **M_univ > πc²/(2G√Λ) = 2.03×10⁵³ kg = 1.02×10²³ M_☉** (JSON `derived.M_univ_escape_kg`) — the mass of an observable-universe-sized closed universe, as it must be, since Λ and T_eq were taken from ours. Translating to the invariant aT via his eqs. (34)–(35): (aT)_esc = [2/(κh_*T_eq√Λ)]^(1/3) = **1.374×10²⁶ m K**; the child at escape therefore always has N_particles ≈ 5×10⁸⁸ and S ≈ 2×10⁸⁹ k_B *regardless of parent mass* (visible in the b_req rows above). (Caveat inherited from the paper: it uses g_* = 106.75 at T_eq, which is not physical; it affects the threshold at the O(1) level.)

### 4.7 Is there an invariant amplification ratio? (Part B item 5)

- Growth of ∫ρ dV under the production term **is** physical: it changes ρa³ (equivalently N = n a³). Growth of ∫ρ dV from expansion or contraction alone is the ordinary a-scaling of §2.1 (radiation: 10²⁰–10²⁴ during the collapse, §3.3; then back down by the same law after the bounce). Any ratio built from E_thermal is therefore slice-dependent: E_thermal(θ)/E_thermal(bounce) = A_N · θ, so quoting it "at the end of production" requires naming θ_end (we used θ = 0.1, a choice).
- The least arbitrary child-side invariant is the **comoving particle number (equivalently entropy) amplification A_N = (aT)³_after/(aT)³_before = e^(3N_e)**: slicing-independent in exact FLRW, geometric (a ratio of scale factors at equal temperature, his ã_i/a_i), and measured between two states where production is negligible. **We computed it: A_N = exp[3 × 1.107 (1 − β/β_cr)^(−0.517)]** per cycle, from 1 (β = 0) through 6.9×10²⁵ (β = 0.996 β_cr) to unbounded as β → β_cr.
- **It is invariant under slicing but not under the model:** it is a function of the free β only, and it does not contain the parent mass at all. The parent enters only through the initial N ∝ (a_iT_i)³ ∝ M^(3/2). So "child matter / parent mass" = [N_after × (mass per particle in the dust era)]/M = A_N(β) × (const) × M^(1/2) — every factor except M^(1/2) is a modelling choice (β, and which particles end up nonrelativistic). **There is no parent-to-child amplification ratio that is an invariant of the geometry.** The invariant statement is weaker and exact: the parent fixes the Misner–Sharp mass of the child's throat (= M) and nothing else.

### 4.8 Entropy (Part B item 6)

Parent: S_BH = 4πGM²k_B/(ħc) = A/(4ℓ_P²) k_B (Bekenstein–Hawking, standard): **1.05×10⁷⁹, 1.05×10⁸³, 1.05×10⁸⁹, 1.05×10⁹⁷ k_B** for 10, 10³, 10⁶, 10¹⁰ M_☉ (JSON `S_BH_parent_kB`). Child at formation (thermal, s = (2π²/45)g_*k_B(k_BT/ħc)³, times 2π²a³): **1.0×10⁶⁰, 1.0×10⁶³, 3.2×10⁶⁷, 3.2×10⁷³ k_B**, i.e. 10⁻¹⁹–10⁻²⁴ of S_BH. Without production S_child is constant through the bounce (his eq. 14 + 30: aT = const). With production it grows by A_N; at the Λ-escape threshold it is **≈ 2.0×10⁸⁹ k_B for every parent** (§4.6) — larger than S_BH for parents below ≈ 10⁶ M_☉, smaller above.

What can be compared: two coarse-grained entropies of two different systems in two causally separated regions. What cannot be claimed: any second-law statement across the horizon. S_BH counts the exterior observer's ignorance of the interior; the interior's thermal entropy is not accessible to that observer, and the generalized second law constrains the exterior. There is no "reset": in his model the child's entropy is conserved through a bounce and only ever increases (his eq. 43, dS/dt ∝ K ≥ 0); the *dilution* of the child at its own late times is the ordinary a-scaling, not a reset. His remark that a black hole is "a state of maximum entropy" for outside observers while the interior keeps producing entropy is consistent and is exactly why no comparison across the horizon is meaningful.

### 4.9 Conservation (Part B item 7)

In FLRW the Bianchi identity applied to the Friedmann constraint (10) and acceleration equation (11) gives the continuity law (12) for the *effective* fluid (ε̃, p̃). Popławski keeps (10) with thermal ε(T) and replaces the continuity law by (42); therefore (11) must change. Write the required modification as an extra effective pressure p_c (a "creation pressure" in the sense of Prigogine-type open-system cosmology — standard construction; not cited here as no primary was fetched). Then ∇_μT̂^{μν} = 0 holds for T̂ = thermal fluid + torsion term + creation pressure, and the equations are consistent. **∇_μT^{μν} = 0 for the thermal fluid alone is violated by construction** — that is what "particle production" means. The source is the gravitational/torsion sector, and Popławski's statement (ApJ §1, §6; CQG 31, 065005) that "particle production does not change the total energy and momentum of the matter and gravitational field" is *true and empty at the same time*: the total (pseudotensor or Misner–Sharp) energy of the closed child is zero before and after, so any amount of matter energy can appear as long as the (non-localizable) gravitational contribution goes equally negative.

**What the conserved current is / is not:** there *is* a conserved Kodama current with charge m (Hayward 1996, App. B) — its total charge for the closed child is 0 = 0 throughout. There is *no* conserved particle-number current (∇_μ(n u^μ) = cK ≠ 0) and *no* conserved matter-energy current. Nothing in this is a violation of general covariance or of local conservation; it is the ordinary situation of an open subsystem in a dynamical geometry.

---

## 5. The closed-form "amplification" of arXiv:1103.4192, the counter-result, and what the 2025 intuition traces to

### 5.1 What the formula is (quoted from `poplawski_stiff_mass_2026_09_18.json`)

Popławski (2011, arXiv only) takes **stiff** matter (p = ε ⇒ ε ∝ a⁻⁶) and defines the child's "mass" as m = εV/c² ∝ a⁻³ — the naive integral of §2.1 with w = 1. He **assumes the fermion number density tracks ε/(m_nc²)** (n ∝ a⁻⁶; his footnote 1 admits that with N conserved one would have n ∝ a⁻³ instead), so the entire blue-shifted energy is booked as neutrons. The torsion bounce then occurs at (a_min/a₀)⁶ = κ(ħcn₀)²/(32ε₀), and

**m_max/M = (a₀/a_min)³ = (128/27)^(1/2) m_n M/m_Pl² = 2.177 M_*/M,  M_* ≡ M² m_n/m_Pl².**

Dimensional check: [M² m_n/m_Pl²] = mass ✓. **Reproduction:** with n₀ = 3M/(m_n V) as printed in his eq. (6), our direct evaluation gives prefactor 2.17732 = (128/27)^(1/2) exactly, a_min = 5.52×10⁻³ m and m_max = 3.05×10⁵¹ kg for M = 10 M_☉ (paper: 6×10⁻³ m, 3.1×10⁵¹ kg) ✓. **The unstated assumption:** the factor 3 in n₀ = 3M/(m_nV) — three spin-½ fermions (valence quarks) per neutron mass. Nowhere in the text. With one fermion per neutron the prefactor would be (128/3)^(1/2) = 6.53 (`prefactor_check`).

Values: m_max/M = **1.53×10²⁰ (10 M_☉), 1.53×10²² (10³), 1.53×10²⁵ (10⁶), 1.53×10²⁹ (10¹⁰)**; m_max = 3.05×10⁵¹, 3.05×10⁵⁵, 3.05×10⁶¹, 3.05×10⁶⁹ kg. His eq. (20) critical parent mass for Λ-escape evaluates to 82 M_☉ with the same Λ (`M_c_escape_Msun`; he does not print the number).

### 5.2 What it means

This is §3.3 in a different equation of state: E ∝ a⁻³ between r_s and a_min is the p dV work of the collapse, no production required; the "mass" is then obtained by *declaring* that energy to be rest mass. Torsion's only role is to set a_min, hence the blueshift factor (a₀/a_min)³ ∝ M. **Compare with §4.7:** the same parent (10 M_☉) gets "amplification" 1.5×10²⁰ in this model and A_N ≈ 2×10²⁹ (× a conversion efficiency) in the ApJ model, with opposite dependence on M (∝ M here; ∝ β only, independent of M, there). Two papers by the same author, same theory, same parent, ratios differing by nine orders of magnitude and in their M-scaling: **the "amplification factor" is a property of the production assumption, not of Einstein–Cartan gravity or of the parent.**

### 5.3 Where the 2025 "daughter much larger than parent" intuition traces to

The Notion-era intuition matches 1103.4192 (a closed form, M_* ∝ M²) more closely than 1410.3881 (a tunable plateau). Both rest on comparison (b) of §3 — a naive ∫ρ dV — against the parent's M, and both silently pass through the 4.71 factor of §3.2 and the blueshift factor of §3.3. The legitimate kernel is only: *a closed FLRW region behind a horizon has zero total gravitational mass, so its matter content is not bounded by the parent's M.* That kernel is standard GR, not new physics, and it says nothing about how much matter there actually is.

### 5.4 The counter-result (W4 handoff item 1)

Hashemi, Jalalzadeh & Ziaie, EPJC 75, 53 (2015), arXiv:1407.4103 (abstract verified this session): homogeneous Weyssenhoff spin fluid, Oppenheimer–Snyder-type collapse in Einstein–Cartan theory; "the spacetime singularity that occurs in the OS model is replaced by a non-singular bounce beyond which the collapsing cloud **re-expands to infinity**"; for some parameters a mass threshold prevents horizon formation altogether. Same theory, same matter model as Popławski's §5, but the matter is a *cap* (χ ≤ χ₀) matched to an exterior, and it comes back out. Popławski's closed daughter is the *full* 3-sphere with the horizon "asymptotically" the throat — he labels this a conjecture (ApJ §1: "we conjecture that eventually the wormholes will merge…"). **The closed-daughter topology is therefore an additional assumption, not a consequence of torsion**, and his bookkeeping (§4) is bookkeeping *inside that assumption*. Our reproduction cannot adjudicate between the two because it starts, as he does, from an already-closed homogeneous 3-sphere at rest; the difference lies in the matching problem neither paper solves.

---

## 6. Part C — synthesis questions 7–10 (§18 of the dump) and falsifiability

**Q7. Can the daughter contain vastly more proper matter than the parent's mass?** Yes, in every published EC daughter model, and the excess is unbounded in principle: the child's total gravitational mass is zero (§2.2), so its matter content is not constrained by M, and the actual amount is set by a free production coefficient (ApJ 2016: β within 0.3 % of β_cr gives ≥ 10³⁰ in particle number) or by an assumed energy→rest-mass conversion (arXiv:1103.4192: m_max/M = 2.18 m_nM/m_Pl² ≈ 10²⁰ for 10 M_☉). The parent's M fixes only the Misner–Sharp mass of the child's throat (§3.1). None of this is a prediction of the theory.

**Q8. Where does the additional matter come from mathematically?** From a source term in the particle-number equation, ∇_μ(n u^μ) = cK with K = β(κε̃)² posited by hand (§4.2), which forces an effective creation pressure into the acceleration equation while the Friedmann constraint is kept with the thermal density. The energy for it is booked to the gravitational/torsion sector, whose contribution is non-localizable and whose total for a closed universe is zero. In the stiff-EOS version it comes from p dV work during collapse plus the assumption that blue-shifted energy is rest mass.

**Q9. Does that violate local conservation?** No. ∇_μT̂^{μν} = 0 holds for the total effective stress tensor (thermal fluid + spin–torsion term + creation pressure), and the Bianchi identity is respected. It *does* violate conservation of the thermal fluid's energy and of particle number taken alone — which is the definition of particle production. There is no conserved global energy in FLRW to violate (§2.3).

**Q10. Is there a meaningful invariant amplification ratio?** For the child alone, yes: the comoving particle-number/entropy growth A_N = e^(3N_e), slicing-independent and computed here as exp[3 × 1.107(1 − β/β_cr)^(−0.517)] per cycle. For parent-versus-child, no: every candidate ratio is either slice-dependent (any E_thermal ratio: extra factor θ), geometric and trivial (m_equator/M = 1; m_total/M = 0; E_formation/Mc² = 3π/2), or a function of the free production parameter and of which particles become nonrelativistic. The correct replacement for "amplification ratio" is the pair (m_throat = M; A_N(β) as a child-internal invariant).

**6.5 Does this lane yield any NEW falsifiable prediction not already tested by BigBounce?** No. The daughter's interior is causally disconnected from the parent, so nothing computed here is observable from outside — the sole exterior-observable consequence Popławski has proposed (a preferred spin axis inherited from the parent's rotation) was confronted with the DESI A95 limit on 2026-09-02 and is excluded; this memo does not touch it. Viewed from inside a daughter, the model predicts an inflation-like phase whose n_s and r depend on β (Desai–Popławski), but that is a claim about our own early universe already in the literature, it has a free parameter tuned to 0.02 % of criticality to work, and it is not a parent–child bookkeeping observable. The bookkeeping itself produced two *retirements*: "energy is created in the child" (it is booked against a zero total) and "there is an amplification factor" (there is a free parameter); the 2025 notes' unbounded-energy phrasing has no derived divergence behind it and is retired with them. The one genuinely open technical question this lane surfaced is the matching problem of §5.4 — whether a torsion bounce inside a trapped region closes off or re-expands into the parent — and that is a question for the daughter-universe lane (W4), not for BigBounce's data.

---

## 7. Part D — step-by-step reproduction ledger (the most important deliverable)

Legend: **(a)** reproduces; **(b)** reproduces only with an assumption the paper does not state; **(c)** does not reproduce.

**ApJ 832:96 (arXiv:1410.3881v2)**
1. (a) Spin-fluid → effective perfect fluid, ε̃ = ε − αn_f², α = κ(ħc)²/32 (eqs. 6–9): dimensionally consistent; identical to PLB 694 and GRG 44 forms.
2. (a) Closed-FLRW Friedmann constraint with torsion (eq. 10) and the no-production continuity law d(aT)/dt = 0 (eqs. 12–14).
3. (a) T_max (eq. 20): 1.1524×10³² K vs 1.15×10³²; depends only on g_b, g_f.
4. (a) Bounce density 15.37 ρ_Planck (GRG 44 eq. 14: 15.4).
5. (a) τ (eq. 25) 4.7507×10⁻⁴⁵ s vs 4.75×10⁻⁴⁵; |H|_max (eq. 26 text) 8.10×10⁴³ vs 8.1×10⁴³ s⁻¹.
6. (a) Stellar initial condition (eqs. 16, 21, 29): T_i = 1.375×10¹² K vs 1.38×10¹²; a_min = 1.193×10⁻¹⁶ m vs 1.19×10⁻¹⁶.
7. (b) Identification a_i = r_s of the parent (text below eq. 16): reproduces as an *equatorial Misner–Sharp* matching (§3.1), but the paper does not state that this is the sense in which the parent mass is being matched, nor that the naive ∫ρ dV is already (3π/2)Mc² at that instant (§3.2).
8. (b) Closed daughter topology (full 3-sphere, §1 of the paper): reproduces *given* the conjecture that all trapped regions merge and the horizon becomes the throat; the published EC collapse with a matched exterior (Hashemi et al. 2015) re-expands into the parent instead (§5.4). Assumption, not derivation.
9. (a) Escape condition D > 2/(3√Λ) (eq. 33): derived independently (§4.6); attribution to Lord 1976 unverified but unnecessary.
10. (a) Required ã_i/a_i > 10¹⁰ for a_i = 10⁴ m (eq. 37): ours 9.99×10⁹, i.e. 23.0 e-folds; M_univ > 2.03×10⁵³ kg.
11. (b) Production law (eqs. 39–42): the Beilin et al. rate is unverified and unused; K = β(κε̃)² (eq. 45) is stated as "the simplest form that vanishes at a bounce," i.e. an ansatz chosen for consistency, not derived — the paper says so. The *unstated* assumptions are instant thermalization of produced W/Z into the common T (n₁ = h_n1T³) and retaining the constraint (10) while abandoning (11) without writing the replacement.
12. (a) β_cr = 1/929.09 (eqs. 48–50): reproduced two ways (closed form and stall condition), to 10⁻¹⁰.
13. (a) Existence of a finite exponential plateau at T = T_max/√2, constant H = 7.40×10⁴³ s⁻¹, for β slightly below β_cr; eternal for β ≥ β_cr; cyclic with finite cycles for 0 < β < β_cr (§7 of the paper).
14. (c) "This interval depends on τ(β_cr − β)^(−1)" (text after eq. 54): the e-fold count and t_infl scale as (1 − β/β_cr)^(−0.52±0.02); Table I of the companion paper is consistent with −1/2 and inconsistent with −1.
15. (b) "H t_infl ≳ 23" is a *requirement* (from item 10), not a prediction; the paper's wording ("relations (37) and (54) constrain the time interval") is correct, but the abstract's "can create enormous amounts of matter" omits that the amount is whatever β is set to produce, with β needing to be within 0.3 % of β_cr for one bounce to suffice.
16. (a) "Particle production does not change the total energy and momentum of the matter and gravitational field" (§1, §6; CQG 31, 065005): reproduced in the Misner–Sharp form m_total = 0 (§2.2) — true, and see §4.9 for why it carries no constraint.
17. (a) Entropy: constant through a bounce without production; dS/dt ∝ K ≥ 0 with it (eqs. 30, 43).
18. (a) "Dynamics insensitive to a_i, depends on β only" (§8): N_e per cycle identical to 6 digits across a_i spanning 9 orders of magnitude; only the *required* N_e depends on a_i (23.0 → 12.1 from 3 M_☉ to 10¹⁰ M_☉).

**Desai & Popławski, PLB 755:183 (arXiv:1510.08834)** — used because the ApJ paper delegates all numerics to it
19. (a) End of acceleration at t = 1.33×10⁻⁴² s for β = 1/929.25, a₀ = 10⁻²⁷ m, T₀ = 0.99 T_max: ours 1.3286×10⁻⁴² s.
20. (c) "About 60 e-folds" for the same run: ours 97.9 from the bounce to the end of acceleration, and 97.3 of production; consistent with their own H × t. Their definition of the start of the count is not given.
21. (b) Table I bounce counts (1, 2, 3, 5, 10 at β/β_cr = 0.996, 0.984, 0.965, 0.914, 0.757): ours 2, 3, 4, 7, 13 for the ApJ paper's stated stellar initial condition; theirs correspond to an escape threshold of ≈ 19 e-folds whose initial condition is not stated. Relative pattern reproduces.

**arXiv:1103.4192 (stiff EOS)**
22. (a) a_min = (27/128)^(1/6) 2GM̃/c² and m_max = (128/27)^(1/2) M²m_n/m_Pl² (eqs. 7–10) and the M = 10 M_☉ numbers (eq. 11): 5.52×10⁻³ m and 3.05×10⁵¹ kg vs 6×10⁻³ m and 3.1×10⁵¹ kg.
23. (b) The prefactor requires n₀ = 3M/(m_nV), three fermions per neutron mass — printed in eq. (6) but never explained; with one fermion per neutron the prefactor is (128/3)^(1/2).
24. (b) "Mass of the universe ∝ a⁻³" requires N ∝ a⁻³ (n ∝ a⁻⁶), i.e. total conversion of blue-shifted stiff-matter energy into neutrons; the paper's footnote 1 acknowledges that conserved N would give n ∝ a⁻³ — the amplification is *assumed in*, not derived.
25. (c) "Gravitational time dilation thus makes it possible for the mass of the Universe to be much bigger than the mass of the parent black hole as measured by external observers" (§1 of that paper): time dilation plays no role in eqs. (4)–(10); the factor comes from p dV work plus item 24. The sentence does not reproduce as a mechanism.

**Counts: (a) 15 · (b) 8 · (c) 3.**

---

## 8. References (verification status)

Verified by full-text fetch this session: Popławski, ApJ 832, 96 (2016), arXiv:1410.3881v2 [`Poplawski2016`]; Popławski, PLB 694, 181 (2010), arXiv:1007.0587 [`Poplawski2010torsion`]; Popławski, GRG 44, 1007 (2012), arXiv:1105.6127 [`Poplawski2012`]; Desai & Popławski, PLB 755, 183 (2016), arXiv:1510.08834 [not in W2 bib; verified by web search + full text]; Popławski, CQG 31, 065005 (2014), arXiv:1305.6977 [not in W2 bib; verified by web search + full text]; Popławski, arXiv:1103.4192 (2011, arXiv only) [W4-verified; full text fetched here]; Hayward, PRD 53, 1938 (1996), gr-qc/9408002 [`Hayward1996`].
Verified by abstract/record this session: Hashemi, Jalalzadeh & Ziaie, EPJC 75, 53 (2015), arXiv:1407.4103; Misner & Sharp, Phys. Rev. 136, B571 (1964) [`MisnerSharp1964`, APS record].
From W2's verified bibliography, not re-fetched: Parker, Phys. Rev. 183, 1057 (1969) [`Parker1969`]; Zel'dovich & Starobinsky, Sov. Phys. JETP 34, 1159 (1972) [`ZeldovichStarobinsky1972`, W2 lower-confidence — cited only via Popławski's citation].
Standard textbook results cited without fetch (section numbers from memory; W2 to confirm if load-bearing): Wald, *General Relativity* (1984) ch. 4, 5, 11; Misner, Thorne & Wheeler, *Gravitation* (1973) §20.2, §20.4, §27.4, §32.4.
[UNVERIFIED]: Beilin et al., Sov. Phys. JETP 51, 1045 (1980) (Popławski's ref. [34]); Lord, *Tensors, Relativity and Cosmology* (1976) (his ref. [5]); Rich, *Fundamentals of Cosmology* (2001) (his ref. [18], source of g_b, g_f, T_eq, Λ/κ). None is load-bearing here: the rate coefficient is absorbed into β, the escape condition is derived in §4.6, and the thermal inputs are flagged as PAPER inputs in the script.
