# 00: Live Signal Lock

## Flagship Quantity

f_NL^local = -35/8 = -4.375 (matter-bounce bispectrum in the squeezed limit)

## Shape Function Source

AT(k₁,k₂,k₃) = (3/(256·k₁²k₂²k₃²)) × P(k₁,k₂,k₃)

where P is a homogeneous polynomial of degree 9 in k₁,k₂,k₃. Multiple equivalent coefficient representations exist; all produce identical |B|_NL values. Verified at three special cases:
- Squeezed (k₁→0): |B|_NL = -35/8 = -4.375
- Equilateral (k₁=k₂=k₃): |B|_NL = -255/64 = -3.984
- Folded (k₁=2k₂=2k₃): |B|_NL = -9/4 = -2.250

Working coefficient set: (c₁,c₂,c₃,c₄,c₅,c₆) = (4, 5, -9, 0, -68, 19) with prefactor 3/(256·Πk²).

## Benchmark Parameters

| Parameter | Value | Status |
|-----------|-------|--------|
| ε (background) | 3/2 | Fixed (matter contraction) |
| ε_correction | 0.003 | Fitted to n_s (does not affect f_NL) |
| f_NL^local | -4.375 | Fixed, parameter-free |
| cos(θ) with local template | ~0.95 (prior estimate) | TO BE REFINED in this phase |
| f_NL^eff | ~-4.16 (prior estimate) | TO BE REFINED |

## Fixed vs Model-Dependent

| Quantity | Fixed/Adjustable |
|----------|-----------------|
| f_NL amplitude (-35/8) | FIXED |
| f_NL sign (negative) | FIXED |
| Shape function AT | FIXED |
| Template projection cos(θ) | COMPUTABLE (this phase) |
| n_s | Adjustable (1 param) |
| r | LQC-dependent |

## Canonical Live Model for Forecast

Wilson-Ewing LCDM quasi-dust: w = -0.003, LQC bounce, BD vacuum.
For forecast purposes: use f_NL = -4.375 with the full shape function, projected onto the local template.
