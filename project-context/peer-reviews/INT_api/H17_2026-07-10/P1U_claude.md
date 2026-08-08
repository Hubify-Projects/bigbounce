I have completed the verification. Let me record my referee assessment.

---

## Referee Report — P1U (`arxiv/paper1_unified.tex`, v1U.0.9)

**(1) VERDICT: MINOR REVISIONS**

The manuscript is honest, carefully scoped, and its quantitative claims verify against the committed artifacts. One dimensional-bookkeeping error sits in the very table built to demonstrate dimensional consistency, and two claims are mildly overstated relative to the paper's own scope caveats. None require new physics.

**(2) ISSUES**

1. **[MAJOR] Table `tab:dim4_parityodd` (line 4784), O4 "Fate" is dimensionally inconsistent.** The table's stated contract is `[O_n^[4]] = +4 throughout` (line 4763), and `eq:dim4_defs` (line 1899) fixes `O_4^[4] = M_Pl²·ε_IJKL T^IJ T^KL`. Reducing via the Cartan constraint `T = κS` (κ=M_Pl⁻²) and Check D (`SₐᵦᵨSᵃᵇᶜ = 6 J⁵·J⁵`): `O_4^[4] = M_Pl²·κ²·S² = M_Pl⁻²·S² = κ(J⁵·J⁵)`, dimension **+4**. The table writes `→ κ²(J⁵·J⁵)`, which is dimension **+2**. This contradicts (a) the "+4 throughout" setup, (b) the body text at line 1916 ("the M_Pl⁻²-suppressed Fierz-closed four-fermion sector (O4, O5)" — i.e. one power of κ), and (c) the sibling row O5, which correctly reads `→ κ(J⁵·J⁵)`. Both genuine dim-4 densities must carry the same κ¹. Fix: `κ² → κ` for O4. The physics conclusion (four-fermion sector is M_Pl⁻²-suppressed) is unaffected, but a referee running exactly the requested operator-dimension check will trip on it. Checked: `eq:dim4_defs`:1899, table:4784, body:1916, script Check D:141–169.

2. **[MINOR] Over-broad "every admissible" verdict vs. the Fierz scope caveat.** The App-B verdict (line 4827) — "Every admissible local dimension-4 parity-odd density in minimal ECH is [topological / Fierz-reducible / Bianchi-vanishing]" — is stronger than the Fierz-lemma scope disclaimer (lines 4897–4910), which explicitly lists *non-enumerated* classes (derivative four-fermion terms, higher-order curvature–torsion mixed invariants, multi-species chiral structures, dynamical-Immirzi coefficients, non-minimal torsion irreps). Qualify "every admissible" to the enumerated set at the stated power-counting order, consistent with the caveat.

3. **[MINOR] "Symbolic verification" oversells the script.** `dim4_parityodd_enumeration.py` verifies only two standard identities (`ε^{μνρσ}R_{μνρσ}=0` under the first Bianchi; `ε_{abcd}ε^{abce}=6δ^e_d`), both correct analytically, and its own docstring concedes it "does not manufacture the physics conclusion" (i.e. it does not establish basis completeness). The abstract phrasing "enumerated explicitly (…with symbolic verification)" (line 1227) should read as verifying the two load-bearing identities, not the completeness. (I could not execute the scripts in-session due to a sandbox restriction; the identities and the Fierz matrix with `F²=1` at `eq:fierzmatrix`:4864 are textbook-correct, so the PASS is not in doubt.)

4. **[MINOR] "No-go" framing vs. its NDA/naturalness content.** Case II is explicitly "a heuristic dimensional argument … not a full field-theoretic formalization" (4635–4643) and the bound assumes single-scale EFT with no cancellation (4668–4681). This is disclosed well, but "single-scale NDA dimensional no-go" in the abstract reads stronger than the hedged content warrants; consider foregrounding that the dark-energy exclusion is an NDA power-counting + naturalness estimate, as the (excellent) title already does.

**Verified as correct — no action needed:**
- Perturbation-transparency result: `ε^{μνρσ}R_{μνρσ}=0` on the T=0 branch by the first (algebraic) Bianchi identity is correct and is the solid positive core.
- `m_θ∼H₀` Route-4 arithmetic: `ρ_θ = 2m_θ²β²/(α/M)²` with `m_θ=H₀=1.5×10⁻³³ eV`, `β=6×10⁻³`, `α/M=10⁻²¹ GeV⁻¹` gives `1.6×10⁻¹⁰ eV⁴ ≈ 6ρ_Λ` (line 3155) — reproduced independently; the "relocation, not solution" framing is honest, and the free-coupling degeneracy is disclosed.
- MCMC-envelope claims match the committed chains: `176,240 + 132,949 = 309,189`; post-burn-in `93,066` (planck_bao_sn) and `123,369` (full_tension) match `parameter_summary_CORRECTED.json`; ΔNeff means (−0.020, +0.058) are consistent with the one-sided `<0.31 / <0.40` bounds and the "consistent with 0" statement. Correctly labeled as a stock-CAMB proxy, *not* an ECH test.
- Cross-refs: all spot-checked labels are defined; the log's only "undefined" is a benign `OMS/cmtt` font-shape warning (no undefined references/citations). `f_NL=-35/16` is used consistently; the six `-35/8` hits are comment lines plus one deliberate citation of the historical Cai value it corrects (4267–4269).

**(3)** The central claim — channel-level closure of the four enumerated minimal-ECH dark-energy routes *under the stated single-scale/minimal-field assumptions*, plus scalar-sector perturbation transparency — **is supported as narrowly stated**, contingent on fixing the O4 dimensional entry and softening the "every admissible / no-go" wording to match the paper's own (already explicit) scope caveats.

---

**Best Next Steps**
1. Patch `tab:dim4_parityodd` O4 fate `κ² → κ` and recompile (directive-G PDF hygiene: bump + re-mirror + Convex md5).
2. Soften the App-B verdict (4827) and abstract "symbolic verification" wording to match the Fierz scope caveat.
3. Log this round on `reviewTimeline.ts` in the same commit bundle.

Say `continue` and I will take the next best scoped step.
