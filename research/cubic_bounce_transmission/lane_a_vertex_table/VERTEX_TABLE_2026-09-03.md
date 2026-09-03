# Lane (a) — cubic-vertex table for ζ through a nonsingular bounce

**Ledger row:** `project-context/NEXT_SCIENCE_LEDGER.md` item #2, second half (intrinsic bounce
contribution to f_NL). Lane (a) of three; lanes (b) numerical in-in and (c) are separate.
**Date:** 2026-09-03 · **Venue:** local CPU (sympy) · **Cost:** $0.
**Artifacts (this directory):** `cubic_vertex_table.py` → `cubic_vertex_table.log`, `vertex_table.json`;
`REGULARISATION_ASSUMPTION.md`; manifest
`reproducibility/manifests/experiments/p2-a2-lane-a-cubic-vertex-table.json`.

Status: **IN PROGRESS** (header + plan committed first per hard rule; sections appended as computed).

## Plan

1. Write the cubic action for ζ (comoving gauge) in the Seery–Lidsey / Chen–Huang–Kachru–Shiu form
   with c_s, including the field-redefinition boundary term. Every literature coefficient is cited
   (paper + equation) and labelled literature.
2. Evaluate every coefficient on (i) the Quintin+2015 bounce phase H=Υ(t−t_B), a=a_B e^{Υ(t−t_B)²/2}
   and (ii) the LQC effective background H² = (ρ/3)(1−ρ/ρ_c), and record its behaviour as H→0
   (ε→−∞). Sympy does the limits; nothing is transcribed by hand.
3. Regularisation: which coefficients carry 1/H or 1/ε poles, which are finite in the z-form, and
   the explicit scheme assumption (`REGULARISATION_ASSUMPTION.md`). Build on the prior lab result
   (effective-fluid z² has an H=0 pole; dressed-metric a''/a bounded) — not redone.
4. Table (markdown + JSON): operator × {coefficient, |ε|→∞ behaviour, removable?, expected sign of
   its squeezed-f_NL contribution}; the boundary-term / field-redefinition piece generalised to η≠small.
5. State the integrals lane (b) must evaluate and the leading super-Hubble (kη_B≪1) analytic
   estimate of Δf_NL^{bounce}, compared with the contraction value −35/16 (ledger #1, closed).
