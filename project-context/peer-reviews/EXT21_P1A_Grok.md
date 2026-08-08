# EXT21 P1A Grok — chat: https://grok.com/c/6aafd65d-f30a-4cbe-8628-7f8eb76aa318

Referee Report – MNRAS format
Paper: Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter
Author: Houston Golden
Date of report: 26 June 2026
Recommendation: MINOR REVISIONS

Summary

This is a carefully scoped theoretical cosmology paper that performs a channel-level (not operator-basis) amplitude and naturalness audit of four enumerated minimal Einstein–Cartan–Holst (ECH) routes that could source late-time dark energy. It introduces a perturbation-transparency theorem for canonical scalar matter (torsion vanishes identically at all classical orders around the torsion-free branch; the Holst sector therefore decouples from scalar/tensor perturbation equations of motion via the algebraic Bianchi identity on the Levi-Civita connection). The paper catalogues 14 mechanism-class structural barriers (13 logically independent after B8 is subsumed by B14), identifies a structural tension between the N_tot ≈ 92 e-fold requirement of the dark-energy dilution mechanism and the survival of matter-bounce f_NL = −35/8 at SPHEREx-accessible scales, and cleanly separates ECH-specific closure from two surviving ECH-independent class-level tests (matter-bounce f_NL and spectator-ALP birefringence benchmark). All claims are explicitly conditional on stated phenomenological scaling ansätze, scoping limitations, and "left to follow-up" items. Companion numerical work (MCMC, Fisher forecasts, galaxy-spin analysis) is referenced as in-preparation or internal and is not used in the core structural proofs.

The manuscript is written at MNRAS/PRD/JCAP standard. The central results are internally consistent under the stated assumptions and scoping. No load-bearing claim lacks supporting reasoning or critical control within the channel-level remit the author has chosen.

BLOCKERS
None.

MAJORS

Perturbation-transparency proof (Sec. X) – The five-step argument (zero spin density → algebraic T=0 → Levi-Civita connection → Bianchi vanishing of the Holst dual contraction → no contribution to EOM) is correct in outline and generalises Hehl et al. (1976) appropriately. However, the explicit verification that the Holst term remains identically zero at all orders in scalar + metric perturbations (Sec. X D) is only sketched. Because B14 is load-bearing (it subsumes the historical B8 and is used to close tensor-parity channels), please expand Sec. X D with the leading-order perturbed Holst term written out explicitly (or a compact reference to the relevant component of the Nieh–Yan density after torsion elimination) so a reader can verify the cancellation without reconstructing the full perturbed connection. This is a presentation/clarification request, not a conceptual gap; the result itself appears robust.

Status and interdependence of companion papers – The structural closure (Secs. IV and IX) is explicitly independent of the companion MCMC / Fisher / galaxy-spin results, which is correctly stated. Nevertheless, the abstract, Sec. I, and Sec. VII refer to SPHEREx forecasts (2.6–5σ), LiteBIRD sensitivity, and the galaxy-spin null as supporting or falsification channels. Please add a single clarifying sentence in Sec. I B (or a short "Companion papers" paragraph) that (a) lists the companion identifiers/status (e.g., "Paper I(b) [6] (in preparation)", "Paper II Fisher forecast [2] (in preparation)", "Paper IV galaxy-spin analysis [23]"), and (b) reiterates that none of the numerical posteriors or forecast significances enter the channel-level no-go or barrier catalogue. This removes any ambiguity for readers who encounter this paper before the companions appear.

These are the only two items that rise above MINOR under the calibration (unsupported load-bearing claim or missing critical control). Both are straightforward to address.

MINORS

Abstract and opening paragraph of Sec. I: The phrasing "the four enumerated routes … are not proven to be a complete diffeomorphism-invariant operator basis" is already present and excellent. Consider moving the explicit list of omitted operators (Jackiw–Pi R∧R̃ and the parity-odd four-fermion partner carrying the γ_BI/(γ_BI²+1)·8πG coefficient) into the abstract itself for immediate visibility.

Sec. II C 1 (Inflationary suppression and reheating thermal-reset argument): The thermal-washout / Γ_wash > H argument for erasure of coherent axial current is presented as a "conditional strengthening" of Barrier 14. It is clearly labelled as such and not used as a primary closure. A one-sentence footnote or parenthetical noting that a full Boltzmann calculation across the bounce-to-reheating window is left to follow-up would prevent any reader from over-interpreting it as a completed calculation.

Eq. (15) and surrounding text (Route 2 amplitude budget): The dimensionless ratio Δθ_one-loop / Δθ_obs is correctly reduced. The parenthetical remark that an alternative ordering yields a "deliberately loose ∼10^{-33} upper bound, not used in the closure" is good conservatism. For clarity, add a short clause confirming that the canonical contraction already includes the H_0/M_Pl factor restored in the numerator (as required for dimensional consistency).

Table II and Sec. IX classification: The distinction between "Novel results", "Known results", and "Structural/philosophical observations" is useful. A single-line footnote on Barrier 9 (Liouville conservation) reiterating the explicit assumptions under which it applies (closed Hamiltonian evolution, no particle production, no coarse-grained entropy injection) would be helpful, since the paper already notes that dissipative or particle-producing bounces evade it.

Minor typographic / extraction artefacts (PDF itself appears clean; these are flagged only because the provided text extraction shows them): occasional missing subscripts on γ_BI, occasional rendering of ε^{abcd} as text, and one instance of "NJL four-fermion contact" appearing as "NJL contact" in a heading. All are cosmetic and do not affect meaning.

References / citation style: arXiv-style citations for the in-preparation companions are acceptable for MNRAS. Ensure the final reference list distinguishes "in preparation" from "submitted" or "arXiv:26xx.xxxxx" consistently.

Future-work / scoping items: All labelled "left to follow-up", "queued", "ansatz", "phenomenological", and "conditional on scaling ansatz" are deliberate and correctly caveated. No action required beyond the two MAJORS above.

Strengths (≥3)

- Explicit scoping and intellectual honesty: The repeated, prominent statements that this is a channel-level amplitude audit under a phenomenological on-shell scaling ansatz (not a derivation), that it is not an operator-basis theorem, and that key operators are deferred to follow-up work set a high standard for theoretical cosmology papers. Readers know exactly what has and has not been claimed.

- Perturbation-transparency result (Sec. X): The clean demonstration that, for canonical scalar matter, torsion vanishes algebraically at all orders, the connection reduces to Levi-Civita, and the Holst dual contraction vanishes identically by the algebraic Bianchi identity is a useful structural result. It cleanly decouples the minimal ECH parity-odd sector from scalar/tensor observables and correctly shifts any parity-sensitive tests to non-perturbative channels (ALP birefringence, primordial GWs). The generalisation of Hehl et al. (1976) to the Holst sector and to all perturbative orders around the torsion-free branch is a genuine contribution.

- Systematic barrier catalogue and structural tension: The 14-barrier taxonomy (7 Foundations + 6 Branches + ECH perturbation gates) organises a large parameter space into mechanism-class constraints with transparent provenance (novel vs. known). The identification of the incompatibility between N_tot ≈ 92 (required for the dark-energy dilution ansatz) and survival of matter-bounce contraction-mode f_NL at SPHEREx wavenumbers is a sharp, observationally relevant observation that correctly reframes the two programmes as independent.

- Clean separation of ECH-specific closure from class-level tests: The paper is explicit that f_NL = −35/8 and the β ≈ 0.27° benchmark are properties of the broader matter-bounce and GR+ALP classes, respectively, not distinctive ECH predictions. This prevents over-claiming while still highlighting falsifiable signatures accessible to SPHEREx (∼2028) and LiteBIRD (early 2030s).

- Observational anchoring and falsifiability criteria (Secs. III, VII, XIII): The linkage to concrete upcoming data (SPHEREx bispectrum, LiteBIRD σ(β) ≈ 0.03°) with realistic systematic budgets (GR projection, b_ϕ uncertainty, photo-z) and the clear statement of what would falsify the relevant class-level benchmarks (rather than ECH itself) is a strength. The paper does not hide behind "more work needed"; it states what the community can actually test in the next 3–5 years.

Overall assessment

This is a solid, well-scoped theoretical contribution that performs the stated channel-level closure with appropriate conservatism and transparency. The two MAJOR items are straightforward clarifications that will strengthen an already careful manuscript. Once addressed, the paper will be suitable for MNRAS, PRD, or JCAP. I recommend MINOR REVISIONS.
