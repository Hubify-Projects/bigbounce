# P1A v1A.0.121 — normalized truth audit of the exact-PDF CQG Note panel

## Provenance and verdicts

- Manuscript commit: `b587cb7bb8e075aa9d0245ba8257fcef7ff196b8`
- Review-dispatch commit: `15f2e6af98daec7f9634e50961c7c1f7375c87fe`
- TeX SHA-256: `4bf3a979fa214a06c29c474fe7a49f3d032150769d505de16647b0854701a650`
- PDF SHA-256: `adfaf5e9fec12dc89857ea947b06d2923d49a8a0b3e45880b278b79bd22dab77`
- Length: 7 pages
- Profile: `CQG-NOTE`
- OpenAI GPT-5.5: **MINOR REVISIONS**
- Gemini 3.1 Pro Preview: **MINOR REVISIONS**
- Grok 4.3: **MINOR REVISIONS**
- Independent Codex subscription leg: typed `NOT_RUN`; see `DECLARED_GAPS.json`
- Anthropic/Claude: not dispatched

The three native-PDF legs ran concurrently against immutable packets for the
same PDF. Critical-path latency was 63.5 seconds versus 103.4 seconds summed, a
38.6% wall-clock reduction.

## Adjudication

All three reviewers support the narrow central result. No report contains a
hidden `[MAJOR]` issue. The remaining findings are bounded clarifications or
presentation changes; no new derivation, numerical result, or scientific claim
is required. This is the first exact three-vendor minor-only board in the
current publication campaign.

It is not yet the full campaign terminator. The independent Codex leg was not
run, and this internal/API panel is not an external human or governed-browser
confirmation. The verified public readiness cap therefore remains 62 pending a
bounded v1A.0.122 closure and fresh external confirmation.

## Finding ledger

| ID | Finding | Disposition | Closure |
|---|---|---|---|
| P1A-121-01 | "Sharply bounded observational consequence" overstates the density illustration. | **CONFIRMED MINOR** | Replace with "dimensional coefficient benchmark" in abstract/introduction/conclusion; state explicitly that the 100 cm^-3 normalization is illustrative and not a constraint. |
| P1A-121-02 | The 100 cm^-3 reference lacks a physical scale anchor. | **BOUNDED/OPTIONAL MINOR** | If an anchor is added, identify it only as an order-of-magnitude number-density comparison and state that number density does not determine the axial-current composite. Do not imply a relic-neutrino state calculation. |
| P1A-121-03 | Cartan-source normalization or the bridge to the Freidel--Minic--Takeuchi coefficient should be more explicit. | **CONFIRMED CLARITY MINOR** | Add one convention-pinned intermediate line/cross-reference between the displayed source equation, contorsion, and back-substituted contact coefficient. Preserve the source-derived coefficient. |
| P1A-121-04 | Separate coefficient-one `kappa n^2`, actual contact coefficient, Holst factor, and state-dependent composite. | **MOSTLY PRESENT; BOUNDED MINOR** | The body already distinguishes all four. Tighten the abstract/first benchmark paragraph so no foregrounded ratio can be read as a bound on `J5.J5`. |
| P1A-121-05 | `Lambda=M_Pl` and `R_A` need stronger caveats. | **MOSTLY STALE; PRESENTATION MINOR** | Appendix B already calls the cutoff a bookkeeping ceiling and `R_A` a coefficient-magnitude benchmark, not an axial threshold. Repeat that in the table caption. |
| P1A-121-06 | "Standard boundary data" should be concrete. | **CONFIRMED CLARITY MINOR** | Define the local theorem as matched background, initial, and boundary data with the standard falloff/vanishing boundary contribution assumed; keep nonstandard boundaries and global/topological sectors excluded. |
| P1A-121-07 | Fierz operator ordering should be cross-referenced wherever `G_s=-3 kappa/16` is invoked. | **CONFIRMED PRESENTATION MINOR** | Add a compact Appendix-A convention cross-reference at the first main-text scalar-coupling use. No sign or coefficient change. |
| P1A-121-08 | Running-based critique should name the precise barrier. | **BOUNDED MINOR** | State the evidenced barrier narrowly: a physical Lorentzian cosmological stress tensor/observable has not been derived from the Euclidean running calculation. Do not invent a specific Wick-rotation failure mechanism. |
| P1A-121-09 | `TB/EB` is informal. | **CONFIRMED COPYEDIT** | Expand to `TB and EB CMB cross-power spectra`. |
| P1A-121-10 | Other NJL regulators could change convention-dependent details. | **ALREADY DISCLOSED; BOUNDED MINOR** | Retain the statement that the gap check is not regulator- or basis-independent. Mention alternate regulators only without claiming whether they flip the stability condition; no such calculation was performed. |
| P1A-121-11 | PACS is obsolete and repository provenance should be immutable. | **CONFIRMED WORKFLOW/COPYEDIT** | Remove `showpacs`/PACS for the CQG Note and cite an immutable repository commit/tag in the submission package. |

## Closure gate

Apply the bounded edits in one v1A.0.122 wave, compile and run the full PDF
audit, freeze an immutable packet, then seek external confirmation. Do not add
new phenomenology, density claims, regulator calculations, or broad all-orders
language.
