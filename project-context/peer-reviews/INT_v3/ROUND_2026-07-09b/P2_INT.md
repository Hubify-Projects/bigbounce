# INT full-source verification — P2 (research/focused_paper_source_integration/02_full_draft.tex) v1.7.105

**Reviewer:** Claude Code INT (Houston subscription, full-source, script RAN + per-vertex re-derived)
**Date:** 2026-07-09
**Scope:** NEW content — Table VII vertex-walk (`tab:vertexwalk`) + frames table (`tab:frames`).
**Stance:** skeptical referee; NEVER rubber-stamp.

---

## Item 1 — Table VII vertex-walk (`tab:vertexwalk`, L1403–1414)

**Script:** `research/focused_paper_source_integration/scripts/p2_vertex_check.py`
— **RAN, exit 0.** Prints total squeezed `-35/16` and equilateral `-255/128`, plus the
Li c_s=1 cross-check `-35/16`.

**Per-vertex check (independent):** the committed script only prints the *totals*, so I
re-used the script's OWN `build_A` vertex definitions (v1 field-redef, v2 `L_ζζ̇²`,
v3 mixed `L_ζ̇∂ζ∂χ`, v4 highest-order `L_ζ(∂∂χ)²`) and computed each vertex's squeezed
and equilateral local amplitude separately via `fNL=(10/3)A_v/Σk³`. Exact-fraction sympy
results vs the table:

| vertex | table squeezed | computed | table equil. | computed |
|---|---|---|---|---|
| field redef. (v1) | −25/16 | **−25/16 ✓** | −35/32 | **−35/32 ✓** |
| L_ζζ̇² (v2) | −5/32 | **−5/32 ✓** | −5/32 | **−5/32 ✓** |
| mixed L_ζ̇∂ζ∂χ (v3) | 0 | **0 ✓** | −5/8 | **−5/8 ✓** |
| highest L_ζ(∂∂χ)² (v4) | −15/32 | **−15/32 ✓** | −15/128 | **−15/128 ✓** |
| **sum** | **−35/16** | **−35/16 ✓** | **−255/128** | **−255/128 ✓** |

**Every per-vertex fraction in the table matches the script's own vertex functions
exactly.** Column sums reproduce the certified benchmarks (−35/16, −255/128) exactly.

**Order-grouped Eq. `order_grouped` (L1429–1435)** independently checked:
`−5/2 + 5/16 + 0 = −40/16 + 5/16 = −35/16` ✓ (arithmetic correct; matches the ε-order
grouping Cai et al. describe).

Values are transcribed verbatim from the committed exact-fraction sympy certification;
no value is fitted or rounded. No fabrication.

**VERDICT: VERIFIED. No MAJOR, no MINOR.**

---

## Item 2 — Frames table (`tab:frames`, L1025–1034)

| frame | fNL^bounce | fNL^inf | ratio |
|---|---|---|---|
| gauge (survey observable) | −2.1875 | +0.015 | ≈146 |
| physical (conformal-Fermi) | −2.1875 | →0⁺ | ≫146 |

Consistency with body usage:
- bounce value −2.1875 = **−35/16** — matches the certified headline everywhere in the
  body (L1023, L1047, abstract). ✓
- gauge inflation +0.015 = `(5/12)(1−n_s)` consistency-relation value (L1023). ✓
- ratio 2.1875/0.015 = **145.83 ≈ 146** — matches the "≈146" benchmark cited at L1023
  and used in P1U cross-references. ✓
- physical-frame row (inflation →0⁺ under the conformal-Fermi consistency relation,
  ratio ≫146) is logically consistent with the Pajer/Tanaka-Urakawa conformal-Fermi
  discussion cited in the caption; the bounce value is correctly stated as frame-robust
  (contracting-phase cubic-action prediction, not a squeezed consistency-relation
  artifact). No contradiction with body usage.

**VERDICT: VERIFIED. No MAJOR, no MINOR.**

---

## P2 OVERALL VERDICT: **VERIFIED / ACCEPT-track.**
Script ran (exit 0); every per-vertex squeezed AND equilateral fraction in Table VII
matches the script's own vertex functions exactly (re-derived independently, exact
fraction); both columns sum to the certified −35/16 / −255/128; order-grouped
decomposition arithmetic checks. Frames table is internally consistent and consistent
with body usage (−35/16 bounce, +0.015 gauge inflation, ≈146 ratio). No fabrication,
no MAJOR, no MINOR.
