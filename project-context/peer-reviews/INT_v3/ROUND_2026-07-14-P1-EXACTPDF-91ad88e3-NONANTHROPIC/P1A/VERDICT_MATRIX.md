# P1A exact-PDF truth-audit matrix

Frozen target: P1A v1A.0.116 at commit `91ad88e36121da128175415f55be44d5e458f9f1`.

This matrix adjudicates every labeled finding in the OpenAI, Gemini, Grok, and Codex GPT-5.6-sol/high raw reports. Severity is assigned from the frozen source and commit-pinned artifacts, not copied from a reviewer's recommendation.

## Publication-blocking findings

| Finding | Raw IDs | Truth-audit verdict | Exact evidence |
|---|---|---|---|
| Inconsistent Planck convention changes the NJL ratios | OpenAI E6; Codex E01 | **VERIFIED — GENUINELY NEW BLOCKER** | Source defines `κ=8πG` at line 1630, then `κ=1/M_Pl^2` while using unreduced `M_Pl=1.22e19 GeV` at lines 2466–2481 and again substitutes `κ=M_Pl^-2` at lines 4558–4596. Correctly, `κ=8π/M_P^2`; the paper's 0.156/0.31 become 3.92/7.84 under its gap formula. |
| Gap equation is high by two for the explicitly declared `G_s(ψ̄ψ)^2` normalization | Codex M01 | **VERIFIED — GENUINELY NEW BLOCKER** | Lines 4579–4589 declare the interaction and threshold. Direct mean-field linearization gives `G_crit=2π²/(N_f N_c Λ²)`, not `π²/(...)`. Combined with the 8π repair, the reported maximizing point remains supercritical: about 1.96 scalar and 3.92 axial. |
| Inputs behind 0.156/0.31 are absent and conflict with “single species” | OpenAI E1, M3; Grok E2; Codex M02 | **VERIFIED — GENUINELY NEW BLOCKER** | Lines 4598–4604 never give `N_f`, `N_c`, or numerical `γ`. Commit-pinned `arxiv/scripts/njl_gap_equation_route1.py` uses `γ=0.274` and scans `N_fN_c=1,3,9`; 0.156 is the QCD-like 9, above-Planck point, not the declared single-species case. |
| Vanishing one-point axial current is used to assign the composite equation of state | Codex M04 | **VERIFIED — REAL MAJOR** | Lines 2487–2497 infer no coherent `w=-1` component from `<J5>≈0` while admitting `<J5J5>≠0`. A composite stress tensor/equation of state is state-dependent; the independent amplitude bound survives, but this “second leg” is not derived. |

## Reproducibility, derivation, and scope findings

| Finding | Raw IDs | Truth-audit verdict | Exact evidence |
|---|---|---|---|
| Mutable/generic code links | OpenAI E2; Grok E4; Codex m08 | **VERIFIED — REAL MINOR** | Artifact macro line 51 targets mutable `blob/main/#1` and renders generic “repository artifact”; lines 3840–3848 do not pin a release/hash. This is a provenance/presentation defect, not an essential physics defect by itself. |
| Promised torsion-convention footnote is missing | OpenAI E4 | **VERIFIED — REAL MINOR** | Lines 2446–2452 point to a convention footnote at Eq. (2), but no rendered footnote exists; the fuller convention text is inside an inactive comment block. |
| Contact coefficient lacks an in-paper convention-locked derivation | OpenAI E5; Codex m05 | **VERIFIED — REAL MINOR** | Lines 1622–1650 cite Freidel/Mercuri and state the standard coefficient, but omit signature, epsilon, Dirac normalization, contorsion solution, and substitution. The coefficient itself agrees with the cited minimal-coupling convention. |
| Internal/spacetime epsilon bridge and signature are not declared | OpenAI M4, m4, m10; Codex m05 | **VERIFIED — REAL MINOR** | Active source uses internal and spacetime epsilon tensors at lines 1624–1649 and 3683–3698 without giving signature, epsilon normalization, or tetrad identity. This weakens self-containment but does not falsify the theorem. |
| Fierz ordering/convention deserves clearer documentation | OpenAI M2; Gemini M1 | **VERIFIED — REAL MINOR** | Lines 4543–4568 give the standard matrix, citations, `F²=1`, and the axial column, so the algebra is reproducible; a precise exchange ordering/equation citation would remove convention ambiguity. Gemini's requested positive scalar sign is false. |
| “v_R=v_L” follows only with equal initial data | OpenAI m6; Codex m06 | **VERIFIED — REAL MINOR** | Lines 3721–3727 infer equality from parity-identical equations. Equal equations imply equal propagation/transfer, not equal mode amplitudes for arbitrary chiral initial conditions. |
| Formal transparency statement omits elementary hypotheses | OpenAI m7; Codex m07 | **VERIFIED — REAL MINOR** | Lines 3646–3669 should make explicit an invertible tetrad and real nonsingular constant Immirzi parameter. Ordinary boundary assumptions are relevant only to the redundant boundary-language step, not the pointwise Bianchi identity. |
| `100 cm^-3` called a high-density upper bound | Codex m09 | **VERIFIED — REAL MINOR** | Lines 2471–2475 are conservative relative to the cosmic mean but not an upper bound on all astrophysical environments. This is wording only; the dark-energy-scale conclusion is unaffected. |
| Step 5 mixes pointwise vanishing with boundary-term language | Codex n10 | **VERIFIED — REAL MINOR** | Lines 3700–3705 are redundant after pointwise Bianchi vanishing and can confuse the nonzero-torsion case, where a torsion-square term remains. |
| Undefined/loose notation and forward references | OpenAI m1–m3, m6, m8, m9; Codex m05–m07 | **VERIFIED — REAL MINOR** | Active source has a forward reference to Eq. (5), undefined/loose `v_R,v_L` and `ζ`, and no explicit `J5·J5` contraction. `γ` itself is defined at line 1623; “γBI undefined” is overstated. |
| Cosmic-mean numerical value requested | OpenAI m5 | **OPINION/VENUE** | Lines 2471–2500 already state the cosmic mean and explain it strengthens the bound; an additional computed number is optional, not a defect. |
| Alternative regulator scan and loop/nonminimal corrections requested | Grok M1, M2 | **OUT-OF-SCOPE/DISCLOSED** | Lines 2518–2522 and 4606–4612 expressly restrict the gap check to one hard-cutoff mean-field convention; lines 3776–3788 and 3814–3821 exclude quantum/nonminimal/propagating-torsion sectors. |
| Paper is too narrow/not novel enough for PRD | Grok M3; Codex M03 | **OPINION/VENUE** | The title, abstract, and Secs. IV–VI accurately frame a narrow constraint/transparency note. Venue novelty cannot be truth-adjudicated as a technical error. |

## Falsified, stale, or misread findings

| Finding | Raw IDs | Truth-audit verdict | Exact evidence |
|---|---|---|---|
| Scalar Fierz sign should be positive | Gemini E1 | **STALE/MISREAD** | Frozen Eq. (B1), lines 4575–4577, explicitly has `(-3/16)(+1/4)=-3/64`; Gemini silently dropped the leading minus. Matrix multiplication independently reproduces the `+1/4` projection. |
| Date July 14, 2026 is in the future | Gemini N1; Grok E1 | **STALE/MISREAD** | Review date is 2026-07-14; the dateline is current, not future. |
| Density arithmetic is off by four orders | Grok E5 | **STALE/MISREAD** | Lines 2471–2481 use `100 cm^-3`, hence `7.66e-13 eV^3`; Grok recomputed with the line's `1 cm^-3` intermediate. The stated `4e-81 eV^4` is correct before the separate 8π normalization repair. |
| Abstract claims regulator-independent exclusion | Grok E3, E6 | **STALE/MISREAD** | Abstract lines 1081–1111 and body lines 2518–2522/4606–4612 explicitly call the result conditional and exclude regulator/basis-independent reach. |
| Nieh–Yan sign is wrong | OpenAI M1 | **STALE/MISREAD** | With the paper's definition, `d(e^I∧T_I)=T^I∧T_I-e^I∧e^J∧R_IJ`; therefore `eeR=-NY+T²`, exactly as lines 3740–3754 state. |
| Holst/Bianchi vanishing is not pointwise algebraic | Grok M4 | **STALE/MISREAD** | Lines 3683–3698 prove pointwise vanishing directly from `R_{μ[νρσ]}=0`; the later differential-form identity is an independent cross-check, not a premise. |
| Action prefactor fails the Einstein–Hilbert normalization | Grok N3 | **STALE/MISREAD** | The `1/(4κ) ε e e R` form at lines 1624–1628 is the conventional first-order normalization once wedge/dual factors are included; no contrary arithmetic was supplied. |
| Critical-coupling equation is visually ambiguous | OpenAI E3 | **STALE/MISREAD** | Frozen source lines 4586–4589 is unambiguous `π²/(N_fN_cΛ²)`, and the rendered PDF fraction is visually clear. The formula is nevertheless technically wrong by two for the declared interaction, captured separately above. |
| Fierz citation is absent | Grok N2 | **STALE/MISREAD** | Lines 4543–4547 cite Itzykson–Zuber and Nieves–Pal at first use. |
| Late-density scalar result needs companion paper | Grok E2 | **STALE/MISREAD** | The complete active derivation is in lines 2436–2522 and Appendices A–B. The actual reproducibility gap is the missing scan inputs, already verified above. |
| Contact result generates a vector–axial term under minimal coupling | Implied in some scope criticism | **STALE/MISREAD** | Lines 1651–1654 correctly state that the cited minimal coupling produces only axial–axial; nonminimal coupling is required for vector–axial parity violation. |
| Minor visual/spacing defects in bilinears/equations | OpenAI N1, N2; Codex n12 | **OPINION/VENUE** | Six rendered pages show no clipping, overlap, malformed equation, or missing glyph. TOC density, reference wrapping, and notation layout are editorial preferences. |

## Submission and editorial items

| Finding | Raw IDs | Truth-audit verdict | Exact evidence |
|---|---|---|---|
| Companion arXiv identifier absent | Grok NIT1, NIT2; Codex n11 | **KNOWN SUBMISSION BLOCKER** | Reference 6 describes concurrent posting without an assigned identifier. This must be filled at coordinated submission, but is not a new scientific defect. |
| PACS is obsolete | Grok N1 | **OPINION/VENUE** | `showpacs` is active; final taxonomy/style follows target-journal submission policy. |
| Author email looks nonacademic | Gemini N2 | **OPINION/VENUE** | A working domain email is not a placeholder merely because it is not a university address. |
| Bibliography/style harmonization | OpenAI N3 | **OPINION/VENUE** | No citation was shown to be false or unresolvable; formatting is a copyediting issue. |

## Honest disposition

The frozen P1A is **not publication-ready**. The contact coefficient, natural-unit conversion, late-density suppression, Fierz matrix, and classical scalar-transparency theorem survive. The advertised independent NJL magnitude closure does not: the Planck convention and gap normalization are inconsistent, the maximizing inputs are hidden, and the correctly combined worst-case magnitude remains above threshold. These are genuine technical blockers, not reviewer taste.
