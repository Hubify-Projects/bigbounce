# P1C R13 board — truth audit (PARTIAL closure; not a convergence claim)

**Exact PDF reviewed:** v1C.0.15, sha256 `f3e29c45df35f7ac358d8f4e6a854d1b9f79fa20c71a725922732db82bd967d4` (25 pp).
**Closure version:** v1C.0.16 (commit `2d445855`, 2026-08-10; 25 pp, 4-pass 0 err / 0 undef / 0 overfull; `tools/p1c_consistency_check.py` 4/4 PASS; mirrors byte-identical).
**Audit written:** 2026-08-28 (session close-out). This document records what was closed and what is explicitly still OPEN. The R-phase is **not** converged.

## Verdict matrix

| Leg | Model | Verdict | Raw |
|---|---|---|---|
| Claude INT | Opus | MAJOR REVISIONS — 4 MAJOR (3 correctness, 1 provenance) / 8 MINOR; 20 relations re-derived correct; 5 candidates self-withdrawn after ≥300-DPI re-render | `P1C_claude_r13_leg.md` |
| Gemini API | gemini-3.1-pro-preview | MAJOR REVISIONS | `../../ROUND_2026-08-08-P1C-v1C.0.15-EXACTPDF-f3e29c45-R13CONV_P1C_Gemini_cosmology.md` |
| Grok API | grok-4.3 | leg captured; verdict token not machine-extractable from the raw (read the raw before citing a verdict) | `..._P1C_Grok_brutal.md` |
| Perplexity | — | FAILED (optional leg; never a verdict) | `..._P1C_Perplexity_citations.md` |

## Claude MAJORs — dispositions

| # | Finding | Verdict | Closure |
|---|---|---|---|
| M1 | Sec. IV A (tex ~1155): "reduces to the Nieh–Yan density on shell" — a surviving pre-erratum claim contradicting Eqs. (12)/(13) | GENUINELY-NEW-REAL [correctness] | CLOSED v1C.0.16: reduction now stated as Nieh–Yan density **plus** the ε-contracted torsion-square of Eq. `o4_onshell`, vanishing only as γ→∞ (`2d445855`) |
| M2 | Sec. VI (tex ~2205): trace/tensor irreps called "a genuine escape" — App. C was corrected at R12 but Sec. VI was missed; under the solved connection equation the trace-vector irrep is present under **minimal** coupling | GENUINELY-NEW-REAL [correctness] | CLOSED v1C.0.16: excluded set narrowed to the tensor irrep + non-minimal couplings; trace-vector irrep stated as Holst-generated under minimal coupling and carried through O4, the O1=O6 remainder, and Eq. `vj5_onshell` (`2d445855`) |
| M3 | Construction rule equates "one ε" with parity-odd; O5 is P-even off-shell (App. B); the genuinely P-odd ε-free density T^a_{ab}J^{5b} = 3β(J⁵·J⁵) ≠ 0 was unenumerated | GENUINELY-NEW-REAL [correctness] | CLOSED v1C.0.16 by **scoping** (option b): new Eq. `vj5_onshell` exhibits the density with its fate computed from the artifact's trace vector V_c = T^a_{ac} = 3β J⁵_c (`ech_torsion_onshell_2026_08_08.json`, `onshell_torsion/trace_vector_V_c`); it lands in the same κ-suppressed Fierz-closed (J⁵·J⁵) class as O4/O5, and the enumeration claim is restated for the ε-contracted densities the rule generates with this companion carried explicitly. No new enumeration algorithm was written (a mechanized enumeration remains the pre-submission checklist item). |
| M4 | Frozen released script `arxiv/scripts/dim4_parityodd_enumeration.py` still prints pre-erratum statements ("T = kappa S", "O1,O6 vanish by Bianchi", "basis") with no erratum | GENUINELY-NEW-REAL [provenance/presentation] | CLOSED 2026-08-28: dated ERRATUM ADDENDUM inserted at the top of the script's docstring; original text and output preserved verbatim; supersession pointed at the two adjudication artifacts. |

## Explicitly OPEN — carried to R14

- Claude's **8 MINORs** (see raw for anchors) are **not yet dispositioned**.
- The **Gemini** and **Grok** R13 ledgers are **not yet dispositioned** (prior-round re-flags vs genuinely-new to be determined against the R1–R12 audit docs).
- Pre-submission checklist unchanged: mechanized operator enumeration (or keep the scoped framing); ST Eq. 58 quote verification; venue-length condensation (25 pp vs ≤15 pp target); version DOI / archival deposit for the P1C script set (now eight files) at P-round; refereed-companion gate for cited-only companion results.

## Integrity notes

- No mistake-narration entered the paper (directive Q1); the process record lives here and in the artifacts' dated erratum addenda.
- v1C.0.16's tex changes were compiled, audited, and mirrored under directive G at commit `2d445855`; the site pointer (`site/src/data/papers.ts`) lagged at v1C.0.15 until this close-out and is corrected in the same bundle as this document.
- Next board: **R14 on the exact v1C.0.16 PDF** (sha `285948c6248e7995…` — see SSOT), preceded by the linter gate.
