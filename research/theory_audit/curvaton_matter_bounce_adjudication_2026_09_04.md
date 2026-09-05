# Adjudication: the curvaton-type matter bounce (ledger row 15) — 2026-09-04

**Role:** independent adjudicator of contested math (Fable, not the row-15 owner lane).
**Disputed artifact:** `research/track_a3_multichannel/row15_curvaton/` (report, `results.json`,
`row15_curvaton.py`). Does not touch `research/track_a3_multichannel/paper/main.tex`.
**Stance:** re-derive every item from stated assumptions; validate the machinery on the
de Sitter / inflationary-curvaton limit first; never steer toward viability or non-viability.

## Plan

| Item | Claim under adjudication | Method |
|---|---|---|
| A | CXB11 (arXiv:1101.0822) Eq. 18 is "the de Sitter coefficient", 4x too small for the contraction; Case 1 collapses to f_NL = -320/pi^4 | fetch source; re-derive massive-spectator tilt in a ~ eta^2; check Eq. 65 substitution |
| B | branch-W ALP-curvaton tilt sign (n_sigma - 1 ~ -m^2/H^2) is wrong | same derivation, both backgrounds |
| C | light spectator obeys the same MS operator as zeta; tilt 12w/(1+3w); n_s inherited | sympy: u''+(k^2-a''/a)u=0 vs v''+(k^2-z''/z)v=0 for constant w |
| D | r = 24/[1 + (4/3) r_dec^2 (M_pl/sigma_*)^2]; r<0.036 needs r_dec M_pl/sigma_* > 22.35 | two-channel P_zeta; check P_dsigma normalisation and P_zeta,ad = P_v/(2 eps M_pl^2) |
| E | f_NL = 5/(4 r_dec) - 5/3 - 5 r_dec/6; +9.30 -> -1.25 on [0.113,1]; zero at 0.5811 | LUW03 / SVW06 delta-N; evaluate |
| F | adiabatic -35/16 enters with weight (r/24)^2; SPHEREx-detectable only for r >= 22.95 | two-uncorrelated-channel bispectrum algebra |

Outputs: this file (verdicts + paper-ready sentences + open items),
`curvaton_matter_bounce_adjudication_2026_09_04.py` + `.json`,
`reproducibility/manifests/experiments/a3-row15-curvaton-adjudication.json`, ledger row 15 status line.

## Status

- [ ] literature fetched (1101.0822; Cai–Easson–Brandenberger 2012; LUW 2003; SVW 2006)
- [ ] sympy derivations + de Sitter validation
- [ ] verdicts A–F written
- [ ] manifest validated; ledger updated
