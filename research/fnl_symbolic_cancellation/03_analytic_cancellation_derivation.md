# 03: Analytic Cancellation Derivation

## The Central Theorem

**Claim:** Im[ext × I_superhorizon] = 0 for ALL Maldacena cubic action terms, including Term 6 with its k₁⁻² divergence.

**Therefore:** The physical bispectrum B = 2·Im[ext × I_total] = 2·Im[ext × I_crossing], where I_crossing is the contribution from the horizon-crossing region only.

## Proof

### Step 1: Phase structure of superhorizon mode functions

On superhorizon scales (|kη| ≪ 1), the Bunch-Davies mode functions have definite phases:

ζ_k(η) → -i · R_k(η)     [purely imaginary, R_k real and positive]
ζ'_k(η) → +i · S_k(η)    [purely imaginary, S_k real and positive]

where R_k = 1/(√(2k³)·A·|η|³) and S_k = 3/(√(2k³)·A·|η|⁴).

(Sign conventions: η < 0, so η³ < 0 and η⁴ > 0.)

More precisely: for η < 0, |kη| → 0:
- g_k(η) = e^{-ikη}/(√(2k)η²)(1-i/(kη)) → -i/(√(2k³)|η|³)·(−1)³ = +i/(√(2k³)·η³)

Hmm wait, let me be more careful. η < 0, so η³ < 0.
g_k(η → 0⁻) ≈ -i/(kη)/(√(2k)η²) = -i/(√(2k³)η³)

Since η < 0: η³ < 0, so -i/η³ = -i/(negative) = positive imaginary.
g_k → +i|η|⁻³/(√(2k³)) — purely imaginary, POSITIVE imaginary coefficient.

Similarly: g'_k → d/dη[-i/(√(2k³)η³)] = 3i/(√(2k³)η⁴)
Since η⁴ > 0: g'_k → 3i/(√(2k³)|η|⁴) — purely imaginary, POSITIVE imaginary coefficient.

**Conjugates (for external legs):**
g*_k → -i|η_f|⁻³/(√(2k³)) — purely NEGATIVE imaginary
g*_k² = (-i)²|η_f|⁻⁶/(2k³) = -|η_f|⁻⁶/(2k³) — purely REAL, negative

### Step 2: Phase of external product

ext = g*_{k₁}(η_f) · [g*_k(η_f)]²
= [-i·R₁] · [-R_k²]    (where R₁, R_k² are real positive)
= +i·R₁·R_k²

**ext is purely POSITIVE imaginary on superhorizon.**

### Step 3: Phase of the time integral (superhorizon regime)

For the generic integrand F(η') = η'⁴ · (product of mode functions at η'):

**Term 1:** η'⁴ · g_{k₁} · (g'_k)²
= η'⁴ · (+i·R₁') · (+i·S_k')² = η'⁴ · (+i)·(-1) · R₁'·S_k'²
= -i · η'⁴ · R₁' · S_k'²
→ purely NEGATIVE imaginary

**Terms 3,5 (after χ sub):** η'⁸ · (products of ζ and ζ')
The η'⁸ is real positive. Each ζ or ζ' contributes a factor of ±i.
For 3 mode functions (each ±i): i³ = -i or i·i·(-i) etc.
The product of THREE imaginary factors is imaginary: (±i)³ = ±i.
So integrand → purely imaginary.

**Term 6:** Same structure — 3 mode functions, each imaginary on superhorizon.
η'⁸ · ζ_k · ζ'_{k₁} · ζ'_k → η'⁸ · (+i)(+i)(+i) · (reals) = -i · (reals)
→ purely NEGATIVE imaginary

### Step 4: Product ext × integrand on superhorizon

ext × integrand = (+i·real) × (-i·real) = +1·(real²) = REAL POSITIVE

For ALL terms, ext × (superhorizon integrand) is **purely REAL**.

### Step 5: Conclusion

Im[ext × I_superhorizon] = Im[∫ (real function) dη'] = 0 ∎

**The k₁⁻² divergence from T6 lives entirely in Re[ext × I], not Im[ext × I].**

The physical bispectrum B = 2·Im[...] receives NO contribution from the divergent superhorizon regime.

## What Determines the Physical f_NL

The physical bispectrum comes from the **horizon-crossing region** (|kη| ~ 1), where:
- The mode functions deviate from their superhorizon asymptotic forms
- The phase relationship (all imaginary) breaks down
- The integrand develops a REAL component
- This real component, multiplied by the imaginary ext, gives Im ≠ 0

The horizon-crossing integral is:
1. Finite (no growing-mode divergence)
2. Independent of η_f (for sufficiently late η_f)
3. Well-defined numerically (moderate values, O(1))

## The Remaining Numerical Challenge

Even though the superhorizon contribution to Im[ext×I] is exactly zero IN THE LIMIT |kη_f| → 0, at FINITE η_f there are corrections of order (kη_f)² that leak the real divergence into the imaginary part.

For Term 1: the leakage is at order (kη_f)² × η_f⁻¹⁵ ~ η_f⁻¹³, while the physical signal is at η_f⁻¹². The signal-to-leakage ratio improves as η_f → 0, so float64 eventually resolves it.

For Term 6: the leakage involves the k₁⁻² factor, making it:
leakage ~ k₁⁻² × (kη_f)² × η_f⁻¹¹
signal ~ η_f⁻¹²
Ratio: k₁⁻² × η_f³ — DIVERGES as k₁ → 0 for any fixed η_f.

**This means: for T6, no matter how small η_f is, the leakage always dominates for small enough k₁.** The numerical computation fails because the real divergence always overwhelms the physical signal in the squeezed limit.

## Resolution: Two Approaches

### Approach A: Subtracted Integration
Compute I_subtracted = ∫ [exact_integrand - superhorizon_integrand] dη'.
This removes the divergent real part analytically. The subtracted integrand is O(kη)² smaller and numerically tractable. But forming the full f_NL from the subtracted integral requires careful treatment of the boundary matching.

### Approach B: Arbitrary Precision at Moderate η_f
Use mpmath with 50+ digits at η_f where the leakage is manageable. For xf = -0.5 (just inside horizon), the values are moderate and the leakage is O(1).

### Approach C: Follow Cai's Formalism
Use Cai et al.'s A_T definition, which is constructed to be manifestly time-independent and automatically handles the growing-mode cancellation.

## Key Result

**The k₁⁻² divergence from T6 does NOT affect the physical bispectrum.** It is a gauge artifact of the standard in-in formalism for growing modes, confined to the real part of ext×I. The physical observable (Im[ext×I]) is finite and comes from horizon crossing.

The remaining question is purely technical: how to extract the finite coefficient numerically given the precision challenges.
