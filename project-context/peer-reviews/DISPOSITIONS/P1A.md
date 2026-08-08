# P1A disposition ledger

**Canonical source:** `arxiv/paper1a_ech_nogo.tex`  
**Current paper-local version:** `v1A.0.116` (2026-07-14 split revival)  
**Claim policy:** specific minimal-action results only; no operator-complete or unrestricted no-go.

| ID | Issue | Status | Evidence / residual scope |
|---|---|---|---|
| DP1A-01 | Off-shell action displayed an on-shell `T^2` shorthand, inviting double counting. | **CLOSED-BY-EDIT v1A.0.116** | The reader-visible action is now first order in tetrad and Lorentz connection with no independent `T^2`; the algebraic connection is solved before the four-fermion operator is written. |
| DP1A-02 | R1 vacuum-condensate rhetoric exceeded the standard mean-field NJL calculation. | **CLOSED-BY-SCOPE v1A.0.116** | Main text and Appendix B limit the result to the declared single-species, hard-cutoff, direct-channel mean-field convention. Fierz ambiguity, beyond-mean-field dynamics, exchange/flavor structure, and non-minimal completions remain explicitly outside the result. |
| DP1A-03 | Fierz closure was presented as completeness of the gravitational EFT. | **CLOSED-BY-EDIT v1A.0.116** | Appendix A now states only the Dirac-algebra rearrangement of the axial contact operator. The cited script no longer reports an operator-complete no-go. |
| DP1A-04 | Route 2 one-loop Holst/Nieh--Yan operator, absolute normalization, and cosmological observable map were not derived. | **REMOVED FROM CLAIM SET; OPEN RESEARCH** | R2 is absent as a closure. Section IV records Shapiro--Teixeira only as unresolved literature context. |
| DP1A-05 | Route 3 Immirzi running was not matched from its fermionic scheme into a Lorentzian cosmological stress tensor or observable. | **REMOVED FROM CLAIM SET; OPEN RESEARCH** | R3 is absent as a closure. Section IV records Benedetti--Speziale only as unresolved literature context. |
| DP1A-06 | Generic ALP, NaMaster, stock-CAMB, MCMC, galaxy, and forecast material obscured the theory claim. | **CLOSED-BY-SPLIT v1A.0.116** | Those analyses are not reader-visible in P1A and remain separately scoped in P1B. |
| DP1A-07 | Classical scalar transparency was overread as a theorem about all matter/quantum sectors. | **CLOSED-BY-SCOPE v1A.0.116** | The result is explicitly limited to minimally coupled canonical scalar matter, constant Immirzi parameter, classical algebraic torsion, and the torsion-free branch. |
| DP1A-08 | Journal novelty and adequate manuscript depth after claim surgery. | **OPEN-VENUE / FRESH-REVIEW REQUIRED** | The honest focused artifact is six two-column pages, not the aspirational 30--35 pages. Length was not padded with retired claims. Venue fit and novelty require fresh non-Anthropic review. |

## Reproducibility checks

- `python3 arxiv/scripts/fierz_lemma_check.py` — PASS; contact-operator scope only.
- `python3 arxiv/scripts/njl_gap_equation_route1.py` — PASS; largest scalar ratio `0.156`, axial magnitude ratio `0.31`; formal above-Planck cutoff labeled as sensitivity-only.
- The script's former reversed cutoff-scaling prose was corrected in the same split closure.

