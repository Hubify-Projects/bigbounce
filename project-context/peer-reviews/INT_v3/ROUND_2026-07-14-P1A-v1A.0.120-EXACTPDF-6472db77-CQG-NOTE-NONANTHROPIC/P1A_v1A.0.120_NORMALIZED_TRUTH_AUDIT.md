# P1A v1A.0.120 exact-PDF CQG Note and PRD confirmation panels — truth audit

## Immutable review target

- Source commit: `438ce8ec79cb13d7cfa5233671966a30f5b5e45c`
- PDF: `arxiv/paper1a_ech_nogo.pdf`
- PDF SHA-256: `6472db7741deebd4100fe3191d5ef23a9b0b7960c4284cf53e9e4761f62f535b`
- Version/page count: `v1A.0.120`, 8 pages
- Primary venue/article type: *Classical and Quantum Gravity*, Note
- Confirmation venue/article type: *Physical Review D*, regular article
- CQG raw verdicts: OpenAI **MAJOR REVISIONS**; Gemini **MINOR REVISIONS** (with one internally MAJOR-tagged item); Grok **ACCEPT**.
- PRD raw verdicts: OpenAI **MAJOR REVISIONS**; Gemini **MINOR REVISIONS** (with one internally MAJOR-tagged item); Grok **ACCEPT**.
- Declared panel gap: independent Codex subscription `gpt-5.6-sol` high was **NOT RUN** because the local weekly allowance was exhausted. No API fallback, alternate model, or synthesized verdict was substituted. The leg remains required before the final board.

The two venue boards reviewed the identical native PDF concurrently and are
kept separate rather than averaged. Verdict labels do not change readiness by
themselves. The dispositions below come from direct inspection of the exact PDF
and source, including the rendered equations and appendices.

## Confirmed work

1. **CQG Note focus and novelty — confirmed, structural major.** The exact PDF
   presents two consequences of the same algebraic Cartan elimination: the
   spin-sourced axial contact channel and the zero-spin scalar branch. That
   unifying structure is real, but the Note still reads as two adjacent results
   plus an NJL appendix, running-literature section, companion discussion, and
   code material. Refocus the title, abstract, introduction, and conclusion on
   one clarification: what the algebraic connection equation does on the
   spin-sourced and zero-spin branches, with a finite-density scale example as
   an illustration rather than a dark-energy result. State explicitly that the
   identities are standard and that the contribution is their convention-audited
   consolidation and sharply bounded observational consequence. The PRD board's
   novelty concern is an editorial venue barrier; it reinforces CQG Note as the
   primary route rather than proving the algebra false.

2. **Self-contained Cartan kernel step — confirmed, bounded major.** The PDF
   defines `Q_gamma`, gives its inverse for real finite nonzero gamma, excludes
   `gamma=0` and `gamma=+/-i`, and states that
   `Q_gamma(e^[I wedge T^J])=0` implies `T^I=0` for an invertible tetrad. It does
   not display the connection equation with its source or prove the last kernel
   implication. Add the explicit zero-source Holst-modified connection equation
   and a short invertible-tetrad algebra showing
   `e^[I wedge T^J]=0 => T^I=0`. This is a self-containment gap, not evidence
   that the stated nonsingular real-gamma conclusion is wrong.

3. **Above-Planck NJL stress test — confirmed, major and removable.** Appendix B
   explicitly evaluates `Lambda=M_Pl/sqrt(0.274)` and labels it formal and
   above-Planck. That point is outside the contact EFT's controlled domain and
   the exact pseudo-critical ratios have no physical interpretation there.
   Delete the three above-Planck rows and all abstract/body/conclusion claims
   built on them. Retain only sub-Planckian diagnostics, with the sign result
   clearly limited to the declared direct-channel, hard-cutoff, standard
   mean-field convention. No central theorem requires the stress rows.

4. **Observable and all-orders claim boundary — confirmed, major.** The exact
   paper later excludes quantum, fermionic, non-minimal, propagating-torsion,
   boundary, and nontrivial-global sectors, and the tensor discussion conditions
   parity on symmetric initial data. The implications bullet nevertheless says
   all listed perturbation observables are identical to GR with no ECH
   modifications at any order. Replace that with a local statement explicitly
   conditioned on the classical reduced action, canonical scalar matter,
   invertible tetrad, real nonsingular constant gamma, standard initial and
   boundary data, and absence of global/topological and loop/anomaly sectors.
   Distinguish equality after solving the algebraic Cartan equation from an
   off-shell equality of the original first-order actions.

5. **Finite-density benchmark framing — confirmed, bounded.** The PDF repeatedly
   and correctly says `kappa n_psi^2` is a dimensional homogeneous scale, not an
   expectation-value bound, stress tensor, or equation of state. The remaining
   problem is the unexplained choice `n_psi=100 cm^-3` and five-digit display.
   Give the scaling formula in `n_psi`, identify 100 cm^-3 only as a deliberately
   elevated illustrative normalization, and round outputs to physically honest
   precision. Do not infer dark-energy relevance from this example.

6. **Fierz derivation — mostly present; bounded clarity edit, not an open
   derivation major.** Appendix A already displays the full 5x5 `F_c` matrix,
   states `F_op=-F_c` from one Grassmann exchange, identifies the axial row,
   writes the exchange-channel operator identity, and multiplies the scalar
   coefficient by `-3 kappa/16`. Add one intermediate line in conventional
   bilinear notation that visibly carries the matrix element, Grassmann sign,
   and trace normalization into `G_s`. Keep the explicit Fierz-ambiguity and
   truncation caveats. OpenAI's stronger claim that no transparent derivation is
   present is stale against the exact appendix, but the requested one-line bridge
   will make the convention easier to referee.

7. **Four-fermion coefficient derivation — partially confirmed.** Section II
   now centralizes metric, epsilon, gamma-five, antisymmetrization, torsion, and
   bilinear-ordering conventions and cites the finite-gamma result. The exact PDF
   does not derive every contorsion component and substitution step. For a short
   Note, add the explicit sourced Cartan equation and enough algebra to fix the
   axial-contact sign and normalization in the displayed convention; relegate
   nonessential finite-gamma detail to a concise appendix or a precise source
   equation citation. Do not expand this back into a long general review.

8. **Peripheral material and typesetting — confirmed.** Remove undefined
   `Route-2/3` from the abstract; reduce Paper I(b), stock-CAMB, NaMaster, and
   spectator-ALP references to at most one non-load-bearing availability note;
   shorten the running and Nieh--Yan/Pontryagin discussion; repair the rendered
   `R R e`/`R R,e` artifacts; and round Table I. The Grok Nieh--Yan footnote
   concern is typesetting/notation, not a failure of the pointwise Bianchi step.

9. **Realistic fermions versus the scalar theorem — already scoped, optional
   bridge.** The exact statement is explicitly for canonical scalar matter and
   separately lists nonzero fermion spin density as a condition that breaks
   transparency. Add one cross-reference between the finite-density example and
   theorem domain so readers do not conflate the two sectors. Do not weaken the
   exact scalar-branch theorem or claim a realistic fermion cosmology is exactly
   torsion free.

10. **Literature coverage and tone — bounded editorial closure.** The paper
    already cites Hehl et al., Hehl--Datta, Freidel--Minic--Takeuchi, Mercuri,
    Shapiro--Teixeira, and Benedetti--Speziale. Verify that the final coefficient
    convention is pinned to an exact source equation and add only genuinely
    necessary standard references. Consolidate repeated negative disclaimers
    into one scope paragraph and concise claim-boundary sentences.

## Supported statements and rejected over-escalations

- All six raw reports support the narrow central content in essence: the
  Planck-suppressed minimal axial contact channel and classical Holst
  transparency on the torsion-free canonical-scalar branch.
- The exact paper already states that the finite-density number is not a bound,
  stress tensor, or equation of state; reviewer language suggesting that this
  boundary is absent is stale. Motivation and precision still need correction.
- The exact appendix already contains a convention-explicit Fierz matrix and
  operator ordering. A clearer intermediate line is warranted, but a new
  unconstrained Fierz-complete condensate proof must not be invented.
- The exact source already excludes quantum-loop/anomaly, fermionic,
  non-minimal, propagating-torsion, boundary, and global sectors. The defect is
  that the broad implications bullet does not carry those conditions locally.
- Grok's ACCEPT labels are preserved as real verdicts, but do not erase the
  confirmed structural and EFT-domain issues above.

## Accelerated closure and confirmation gate

Use CQG Note as the primary route. Make one surgical v1A.0.121 closure wave:
remove the above-Planck scan and companion-pipeline material; unify the Note
around the two branches of algebraic Cartan elimination; add the explicit
connection/kernel step and one-line Fierz bridge; localize every all-orders
condition; parameterize/round the density illustration; and repair notation.
Then compile, run the full PDF audit, and obtain a fresh blind exact-PDF CQG
panel. Run the PRD profile only as a venue-control board, not as an equal gate.
This round is **not** ACCEPT/minor-only evidence because OpenAI remains MAJOR in
both venues and several findings survive truth audit.
