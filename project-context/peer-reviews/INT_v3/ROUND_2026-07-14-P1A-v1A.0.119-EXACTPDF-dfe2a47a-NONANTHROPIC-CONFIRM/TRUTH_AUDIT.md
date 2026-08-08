# P1A v1A.0.119 exact-PDF truth audit

## Frozen object and panel

- Reviewed commit: `142d9d54`
- Reviewed PDF: `arxiv/paper1a_ech_nogo.pdf`
- SHA-256: `dfe2a47a3221888477dfa47adb9cddf7ebbe25acc96185c3af9e58a1e7c065d0`
- Native-PDF verdicts: OpenAI `MAJOR REVISIONS`; Gemini `REJECT`; Grok
  `MINOR REVISIONS`.
- This audit records finding dispositions only.  It does not change a verdict
  and does not claim that any later edit changes Gemini's novelty/venue
  judgment.

## Primary-source anchors used in the audit

1. Freidel, Minic, and Takeuchi, *Phys. Rev. D* **72**, 104002 (2005),
   [arXiv:hep-th/0507253](https://arxiv.org/abs/hep-th/0507253), especially
   Eqs. (5)--(6), define the Holst bivector operator and its inverse with the
   factor `gamma^2/(gamma^2+1)`; the same paper states that the effective
   interaction is singular at `gamma=+/-i` and gives the minimal axial--axial
   interaction in Eq. (49).
2. Hehl, von der Heyde, Kerlick, and Nester, *Rev. Mod. Phys.* **48**, 393
   (1976), [doi:10.1103/RevModPhys.48.393](https://doi.org/10.1103/RevModPhys.48.393),
   is the cited primary review for the algebraic Cartan equation and
   spin--torsion contact interaction.
3. Nieves and Pal, *Am. J. Phys.* **72**, 1100 (2004),
   [arXiv:hep-ph/0306087](https://arxiv.org/abs/hep-ph/0306087), fixes the
   c-number Fierz matrix convention used in Appendix A.  Turning that identity
   into the displayed anticommuting field-operator ordering requires the
   separately stated Grassmann exchange sign.

## Normalized dispositions

| ID | Raw finding | Truth-audit disposition | Required action |
|---|---|---|---|
| OAI-1/OAI-2 | `kappa n_psi^2` is called a finite-density/late-time bound although number density alone does not bound the renormalized composite `<J5 J5>` | **REAL MAJOR (merged).** The arithmetic is correct, but no inequality follows without a specified state, polarization, species content, normalization, and contact-renormalization prescription. | Recast everywhere as a coefficient-one dimensional homogeneous benchmark; explicitly deny a rigorous bound or cosmological stress inference. |
| OAI-3 | The repulsive scalar conclusion is not independently auditable because conventions and Fierz ordering are dispersed | **REAL MAJOR.** The v1A.0.119 code and Appendix A repair the row/column error, but the active manuscript still lacks one convention block connecting the operator row to `G_s(bar psi psi)^2`. | State metric, epsilon, gamma-five, torsion normalization, bilinear/operator ordering, and the Appendix-A-to-`G_s` bridge in one active location. |
| OAI-4 | The scalar-branch proof uses a schematic Cartan equation rather than the invertible Holst-modified operator | **REAL BOUNDED MINOR.** The conclusion is correct for real finite nonzero Immirzi parameter, but the proof omits the algebra that excludes the complex self-dual singular cases. Freidel--Minic--Takeuchi Eq. (6) confirms the `1+gamma^2` denominator. | Display the bivector operator inverse, state its real-`gamma` domain, exclude `gamma=+/-i`, and then infer `S=0 => T=0`. |
| OAI-5 | The displayed tensor wave equation is linear although the surrounding claim is all-order | **REAL BOUNDED MINOR.** | Label the equation an illustrative source-free linear-FRW specialization; locate the all-order claim in equality of the classical action/EOM on the torsion-free branch. |
| OAI-7 | Step 5's total-derivative argument obscures the stronger pointwise Bianchi identity | **REAL BOUNDED MINOR.** | Remove it as a load-bearing proof step; retain Nieh--Yan only as a non-load-bearing explanatory note. |
| OAI-6 | Parity-sensitive extensions could be misread as signals of the minimal constant-Immirzi theory | **ALREADY CLOSED / REFLAG.** The abstract and scope already exclude dynamical-Immirzi, axionlike, fermionic, non-minimal, and propagating-torsion sectors; no new correctness defect. | Preserve the explicit boundary. |
| OAI-8 | Do not imply that the cited RG papers attempted a dark-energy observable map | **ALREADY CLOSED / REFLAG.** v1A.0.119 says only that the cited calculations do not themselves supply such a map. | No change required. |
| OAI-9 | Analytic factors should not depend on repository scripts | **ALREADY CLOSED / REFLAG.** The action, contact coefficient, Fierz row, gap equation, and threshold are displayed in the paper; scripts are reproducibility checks. | No change required. |
| GROK-1 | Explain the physical status/range of the `100 cm^-3` benchmark | **MERGED INTO OAI-1/OAI-2.** | Same benchmark-only correction. |
| GROK-2 | Clarify Fierz ambiguity / standard threshold | **ALREADY DISCLOSED / REFLAG.** The paper gives the normalized threshold and explicitly preserves mean-field Fierz ambiguity; the new convention block will improve auditability. | No independent new claim. |
| GROK-3 | Clarify that the second-order display is not the basis of the all-order result | **MERGED INTO OAI-5.** | Same illustrative-linear/all-order-action correction. |
| GEMINI-1..4 | The correct results are standard and insufficiently novel for PRD | **UNRESOLVED NOVELTY/VENUE JUDGMENT.** Gemini explicitly says the mathematics is technically correct. This is not a correctness defect and cannot be closed by algebraic clarification. | Record honestly; later venue/framing or a stronger novel result is an author-level decision. |

## Closure boundary

The bounded v1A.0.120 correction may close the two merged technical majors and
three technical minors above.  It must **not** be described as converting the
Gemini `REJECT` into acceptance, establishing novelty, or satisfying PRD's
editorial threshold.  A fresh independent review panel would be required to
change the external readiness state.
