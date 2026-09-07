# Adjudication: the L×S second-order lapse monopole A₂(ε) on the uniform-density slice (2026-09-07)

**Status:** IN PROGRESS (plan header committed first, anti-stall). Independent adjudicator; reads only S9 (`psu_gates_S9_S10_2026_09_05.md`) and S9c (`psu_gate_S9c_evolution_residual_2026_09_05.md`).

## Dispute
- S9: from the exact comoving-gauge density surface ρ = φ̇²/(2N²)+V with lapse N = 1+α₁+α₂, α₂ = A₂ ζ_L ζ_S, the constraint solve gives the squeezed super-Hubble monopole A₂ = ε(3−ε)²/3 (= 9/8 at dust) and hence f^ρ = 5(2ε−15)/24 = −5/2 at dust.
- S9c: an exact separate-universe solution (closed form + DOP853) gives f^ρ = 5(ε−7)/8 = −55/16 on the uniform-density slice (all ε), −5 comoving, and shows the whole gap 5(6−ε)/24 sits in A₂: it requires A₂ = 2(3−ε)² = 2α_Lα_S/(ζ_Lζ_S) (= 9/2 at dust).

## Plan (one commit per step, explicit paths, no paper .tex edits)
1. Set up the ADM constraints in comoving gauge (δφ=0) for a constant-ε background, second order in ζ, long×short product, super-Hubble (gradient-free) limit; solve the Hamiltonian constraint for N₂ exactly (it is algebraic in the separate-universe limit).
2. Identify the L×S monopole; obtain A₂(ε) in closed form; compare with ε(3−ε)²/3 and 2(3−ε)².
3. Feed A₂ into S9's (S9.4) chain → f^ρ; compare with −5/2 and −55/16 at dust.
4. Validations: attractor ε→0; USR (ε→0 with growing mode m=3/ε−1 → the Namjoo 5/2 check through the same lapse formula); comoving-slice analogue → −5.
5. VERDICT + printable sentences; script `a2_lapse_monopole_adjudication_2026_09_07.py` + json; manifest; ledger rows 1 + 17.
