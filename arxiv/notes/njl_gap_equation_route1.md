# Route-1 vacuum-condensate closure — NJL gap equation (directive L)

**Paper:** `arxiv/paper1_unified.tex` (v1U.0.13)
**Open item (DP1U ledger, conceded at sec:r1_njl, lines ~2643–2653):**
"⟨J5⟩=0 does not imply ⟨J5 J5⟩=0; a genuine closure requires a regulated gap
equation, effective potential, and demonstration that no relevant vacuum
solution exists."

**Script:** `arxiv/scripts/njl_gap_equation_route1.py` (sympy + numeric, self-checking)
**JSON:** `arxiv/scripts/njl_gap_equation_route1_results.json`

This note records the standard NJL-type analysis that closes the vacuum case
with an explicit calculation instead of a scope concession. **Not integrated
into the paper — for the integration owner.**

---

## 1. The paper's own four-fermion coupling

From torsion elimination (Hehl–Datta; paper `eq:torsion`, `eq:4fermi`,
`eq:NJL_torsion`):

    L_int = −(3/16) κ (ψ̄ γ^a γ⁵ ψ)²  =  −(3/16) κ (J5·J5),   κ = 8πG = M_Pl⁻²

This is the minimal Einstein–Cartan (γ→∞) value. With the Holst term the paper
multiplies by the bounded prefactor γ²/(γ²+1) ∈ (0,1) (`eq:4fermi`), so the EC
value is the **maximal** coupling — using it is conservative (hardest to exclude).

## 2. Fierz projection to the scalar (condensate) channel

The paper's own Fierz lemma (`eq:AAdecomp`, App `app:fierz`, verified by
`arxiv/scripts/fierz_lemma_check.py`):

    (J5·J5)  →  +¼ SS + ½ VV − ½ AA − ¼ PP

The chiral condensate σ ~ ⟨ψ̄ψ⟩ lives in the **SS** channel. Projecting:

    G_scalar = (−3/16)·(+¼) κ = **−(3/64) κ = −(3/64) M_Pl⁻²**

## 3. Regulated gap equation and derived critical coupling

Standard mean-field NJL, hard 4-momentum cutoff Λ, N_f flavors, N_c colors, for
L = G_s (ψ̄ψ)² (Klevansky RMP 64 (1992) 649; Hatsuda–Kunihiro; Buballa):

    M = m0 + 2 G_s N_f N_c · (M/2π²)[ Λ² − M² ln(1+Λ²/M²) ]

Bifurcation of a nontrivial M≠0 solution (chiral limit, slope of RHS/M at M→0
set to 1) **derives** — not quotes — the critical coupling:

    G_crit = π² / (N_f N_c Λ²)   ✓ matches textbook (symbolic check in script)

## 4. Two independent exclusions

**(A) Sign — the decisive one.** The scalar-channel coupling is
G_scalar = −(3/64)κ < 0: **repulsive**. Standard NJL condensation *requires* an
attractive scalar channel (G_s > 0). A repulsive channel gives an effective
potential monotone-increasing from M=0, so M=0 is the only (trivial) minimum —
**no condensate at ANY coupling strength or cutoff.**

**(B) Magnitude — belt-and-suspenders.** Even taking |G_eff|, the coupling is
far sub-critical. At Λ = M_Pl the ratio is cutoff-**independent** (M_Pl cancels):

    |G_eff|/G_crit = (3/64) N_f N_c / π²
      = 4.75e-3  (N_f N_c = 1, single-species minimal ECH)
      = 1.42e-2  (N_f N_c = 3)
      = 4.27e-2  (N_f N_c = 9, QCD-like)

At the paper's stated EFT-validity scale Λ_strong ~ M_Pl/√γ_BI (γ_BI = 0.274,
footnote near line 5375) G_crit is ~1/γ larger, so the ratio is *smaller* — the
worst case across all cutoffs/flavors scanned is 0.156 (Λ_strong, N_f N_c = 9),
still comfortably sub-critical. The Holst-dressed values are ~30× smaller again.

## 5. Verdict

**CONDENSATE EXCLUDED**, for two independent reasons: (1) the scalar channel is
repulsive (no condensate at any coupling), and (2) |G_eff| is far sub-critical
(< 5×10⁻³ at Λ=M_Pl single-species; < 1 in every case scanned). The Route-1
vacuum case is closed by an explicit regulated gap-equation + effective-potential
analysis — the exact object the ledger asked for — not by scope concession.

## Suggested paper integration (for the owner)

Replace the sec:r1_njl concession ("we do NOT claim to exclude a fully regulated
NJL vacuum condensate … out-of-scope open item") with a short paragraph: the
Fierz-projected scalar-channel coupling is repulsive (G_scalar = −(3/64)κ) so no
condensate forms at any coupling, and the magnitude is sub-critical
(|G_eff|/G_crit = (3/64)N_f N_c/π² ≈ 5×10⁻³ at Λ=M_Pl) — cite this script.
Nothing fabricated: every coefficient is the paper's own (eq:NJL_torsion,
eq:AAdecomp), G_crit is derived symbolically, and the ratios are computed.
