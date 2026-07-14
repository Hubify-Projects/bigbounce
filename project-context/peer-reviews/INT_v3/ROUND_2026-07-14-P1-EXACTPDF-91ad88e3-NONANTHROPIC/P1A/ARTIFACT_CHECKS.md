# P1A exact-commit algebra and artifact checks

All source/artifact checks use commit `91ad88e36121da128175415f55be44d5e458f9f1`.

## Parts that survive

- The minimal-coupling contact coefficient `-(3κ/16) γ²/(1+γ²) J5·J5` agrees with the cited convention and reduces to the Einstein–Cartan value at real `γ -> infinity`.
- The displayed Fierz matrix squares to the identity. Its axial column is `(1/4, 1/2, 0, -1/2, -1/4)`, so the declared direct-channel scalar coefficient is `(-3/16)(+1/4)κ = -3κ/64`. Gemini's positive-sign objection omitted the leading minus.
- `1 cm^-3=(1.973e-5 eV)^3=7.68e-15 eV^3`; hence `100 cm^-3=7.68e-13 eV^3`. Dividing its square by the unreduced Planck mass squared gives `3.96e-81 eV^4`, or `1.42e-70 rho_Lambda` before restoring the contact prefactor. The qualitative late-density suppression remains about 69–70 orders even after the 8π repair.
- For canonical scalar matter, zero spin current, the algebraic Cartan equation, and the torsion-free Bianchi identity establish classical Holst transparency within the stated local domain.

## Planck-mass inconsistency

The source defines `κ=8πG` at line 1630, then writes `κ=1/M_Pl²` while explicitly choosing the unreduced `M_Pl=1.22e19 GeV` at lines 2466–2481. Correct identities are

`M_P=G^-1/2`, `Mbar_P=(8πG)^-1/2`, and `κ=8π/M_P²=1/Mbar_P²`.

Therefore every substitution `κ -> 1/M_P²` using the stated unreduced mass misses `8π`.

## Gap-equation normalization

For the source's explicit interaction `G_s (ψbar ψ)²`, mean field gives

`M = -2 G_s <ψbar ψ>`

and the Euclidean four-momentum-cutoff condensate is

`<ψbar ψ> = -(N_f N_c M / 4π²)[Λ² - M² ln(1+Λ²/M²)]`.

Thus

`M = (G_s N_f N_c M / 2π²)[Λ² - M² ln(1+Λ²/M²)]`

and the bifurcation threshold is

`G_crit = 2π²/(N_f N_c Λ²)`.

The paper and script use twice the right-hand side and half this threshold. No compensating factor-of-two definition is stated.

## Corrected worst-case ratio

The script's reported 0.156 maximum uses `N_fN_c=9`, `γ=0.274`, and `Λ=M_P/sqrt(γ)`. Correcting both independent normalizations gives

`R_scalar = (3 N_f N_c / 16π)(Λ²/M_P²) = 1.9608...`

at that formal point, with the axial magnitude twice as large, about 3.92. The scalar sign remains repulsive in the declared channel convention, but the separate claim that magnitudes remain subcritical is false.

## Nieh–Yan sign

With `NY=d(e^I wedge T_I)`, the standard identity in the paper's convention is

`NY = T^I wedge T_I - e^I wedge e^J wedge R_IJ`,

so `eeR=-NY+T²`. The OpenAI opposite-sign finding is a convention misread; at `T=0`, both the pointwise Bianchi proof and form identity give zero.
