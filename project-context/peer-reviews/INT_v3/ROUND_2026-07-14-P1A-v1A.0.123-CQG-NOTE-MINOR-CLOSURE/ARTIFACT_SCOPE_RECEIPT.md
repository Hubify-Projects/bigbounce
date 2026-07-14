# P1A v1A.0.123 bounded NJL artifact-scope correction

This receipt records the first, provenance-safe unit of the v1A.0.123 closure.
It changes no derivation, coefficient, regulator, paper claim, readiness value,
SSOT record, or site state.

## Truth-audited defect

The v1A.0.122 paper evaluates only three multiplicity rows at the bookkeeping
ceiling `Lambda=M_Pl` and explicitly states that no cutoff above `M_Pl` is
evaluated.  The pinned script and JSON nevertheless retained three legacy rows
at `M_Pl/sqrt(gamma_BI)=1.9104017997521754 M_Pl`.  That made the active
reproducibility artifact broader than the manuscript's declared computation.

## Bounded correction

- `arxiv/scripts/njl_gap_equation_route1.py` now emits only the three declared
  `N_f*N_c = 1, 3, 9` rows at `Lambda=M_Pl`.
- The symbolic gap-equation derivation, contact/Fierz coefficients, finite-Holst
  diagnostics, density benchmark, and sign conclusion are unchanged.
- The legacy six-row result remains preserved in Git history and in the frozen
  v1A.0.122 exact-artifact review bundle.  No historical evidence is deleted or
  overwritten.
- The regenerated JSON is deterministic and must byte-match a second run.

The immutable commit produced from this unit is the only honest target for the
v1A.0.123 reader-facing artifact links.  The manuscript pin is intentionally
deferred to the second logical commit so it cannot refer to a commit that does
not yet contain the corrected artifact.

## Verification

- Python bytecode compilation: **PASS**.
- Symbolic gap-equation assertions: **PASS**.
- Declared cutoff list: exactly `M_Pl`.
- Output row count: exactly 3.
- Above-`M_Pl` row count: 0.
- Retained scalar ratios: `0.238732414637843`, `0.716197243913529`,
  `2.148591731740587`.
- Retained supercritical magnitude rows: 1 (`N_f*N_c=9`), matching the paper.
- Scalar sign coefficient: `-3/16`, unchanged.
- Two consecutive regenerations were byte-identical.
- Corrected script SHA-256:
  `69681ea3a420d562b28faaa534d1e729269a6cfa9c966f44b89a9326d5d8843c`.
- Corrected JSON SHA-256:
  `a53d19e1db2cf0de7102b4e864ca5dbf4924794469f848652b447ef7d4c31d3f`.
