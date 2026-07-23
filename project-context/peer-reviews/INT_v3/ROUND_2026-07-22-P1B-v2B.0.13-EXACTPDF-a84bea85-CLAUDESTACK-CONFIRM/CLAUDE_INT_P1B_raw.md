# Claude INT Referee Report — P1B (namaster-proof software metapaper)

- Paper: `arxiv/paper1b_namaster_proof.pdf`
- Version stamp: v2B.0.13 (title page: "July 21, 2026 — v2B.0.13")
- Target venue: Journal of Open Research Software (software metapaper)
- Referee leg: Claude INT
- Round: ROUND_2026-07-22-P1B-v2B.0.13-EXACTPDF-a84bea85-CLAUDESTACK-CONFIRM

## EXACT-PDF BINDING

- Recorded sha256 (P1B, intwave_bindings.json): `a84bea85ad993f02230d439825e9a220be894e390e0d1f172d046e50c687cbee`
- Computed `shasum -a 256 arxiv/paper1b_namaster_proof.pdf`: `a84bea85ad993f02230d439825e9a220be894e390e0d1f172d046e50c687cbee`
- **MATCH — binding confirmed.** Review proceeds on the exact PDF. Page count = 6 (matches ~6 pp brief).

## Verification performed

All six pages read via pdftotext -layout; page 1 rendered via pdftoppm and inspected visually. Repository cross-checks in `packages/namaster-proof/`; archive DOIs verified via curl.

### External archive / availability checks (all PASS)
- `https://doi.org/10.5281/zenodo.21481753` (software 0.1.7 archive) → 200, resolves to `zenodo.org/records/21481753`; record page also 200. §11 claim verified.
- `https://doi.org/10.5281/zenodo.21481842` (paper deposit) → 200, resolves to `zenodo.org/records/21481842`; record page also 200. §11 claim verified.

### Repository claim checks (all PASS)
- **41-test claim (§7, Abstract):** VERIFIED. `tests/` has 28 `def test_` functions; five `@pytest.mark.parametrize` decorators expand them (+2, +3, +3, +2, +3 = +13 cases) → 28 + 13 = **41** collected. The 2 replay-equivalence tests (`test_legacy_equivalence.py`) are exactly the standalone-skip pair described in §7 ("39 run, 2 skip cleanly"). Fully self-consistent.
  - Note: a live `pytest --collect-only` in this sandbox errored on import because the package is not installed in the ambient Python 3.9; this is an environment condition, not a paper defect. Static parametrization arithmetic reproduces the claimed 41 exactly.
- **MIT License (§11):** VERIFIED — `LICENSE` = "MIT License, Copyright (c) 2026 Houston Golden"; `codemeta.json` license = SPDX MIT; `CITATION.cff` license: MIT.
- **codemeta / CITATION (§11):** VERIFIED — both `codemeta.json` and `CITATION.cff` present.
- **Version 0.1.7 (§7, §11):** VERIFIED and consistent across `pyproject.toml` (0.1.7), `codemeta.json` (0.1.7), `CITATION.cff` (0.1.7).
- **Python 3.10+ / NumPy 1.24+ floors (§11):** VERIFIED — codemeta runtimePlatform ">=3.10" and NumPy ">=1.24" match prose.
- **Archive commit pin (§11):** VERIFIED — `0a587b583f8e86c4ce1ee4a20526fcdcd8035fe6` (40-hex SHA-1) exists as a commit object in the repo (`git cat-file -t` → commit).
- **Cited example scripts (§7, §8):** VERIFIED — `examples/rebuild_workspace_check.py` and `examples/pymaster_integration.py` both present.
- **Validation-artifact SHA-256 digests (§11):** TRACEABLE — both cited digests (`745b0a2f…f39914` summary artifact, `b00f850e…325f331` bandpower artifact) appear in in-repo reproducibility manifests under `reproducibility/p1b_analysis_artifact_manifest_v1B.0.11x.json`.

### Internal-consistency checks
- Grid: §5 default 2001 points over [-1°, +1°] ⇒ 0.001° step; §8 recoveries 0.270°→0.270°, 0.342°→0.342° representable on that grid. Consistent.
- Workspace shape [4,20,4,1025] (§7) ⇔ Nside=512, ℓmax=1024 ⇒ nℓ=1025=ℓmax+1, nb=20 bins (§8). Consistent.
- Wall time §11: ~7×10² s on 8 workers ⇒ ~1.5–2 h single-worker ("a couple of hours"). Order-consistent.
- Scope honesty: EXEMPLARY. Repeated, precise disclaimers (Abstract, §8, §10) — "software-recovery checks … not measurements, detection significances, or evidence for a physical birefringence model"; the retained 1.41×10⁻¹⁸ scalar is explicitly qualified as "not a self-contained reproducibility claim or a universal error bound." Limitations (§10) are thorough and honest.

## Findings

### BLOCKER
None.

### MAJOR
None.

### MINOR

**MINOR-1 — "Overview" (§1) is an empty stub (presentation/structure defect).** [page 1, rendered]
Section "1 Overview" contains no prose body whatsoever — only the single line "Keywords. Python; cosmology; pseudo-Cℓ; NaMaster; reproducibility; provenance." A section titled "Overview" that holds nothing but a keyword list reads as a stub and is the one visible structural blemish in an otherwise clean layout. Either fold the keywords under the abstract and drop the empty heading, or give §1 a one-paragraph overview body.

**MINOR-2 — realization-count wording between §8 and §11 is slightly ambiguous.** [pages 3–4]
§8 ("Synthetic CMB recovery campaign") states "For each of two nonzero injected angles, a 500-realization … run" and separately notes "The null injection recovered 0.000°" without stating the null's realization count. §11 ("Additional system requirements") asserts "500 realizations at each of three injected angles." Not contradictory, but §8 should state explicitly that the null run also used 500 realizations so the "three injected angles" wording in §11 is unambiguously anchored.

## Assessment

A tightly-scoped, honestly-framed JORS software metapaper. Every load-bearing quantitative and availability claim I could check is accurate: exact 41-test count reconstructs from source, both Zenodo DOIs resolve (200), MIT/codemeta/CITATION present, version stamps consistent, commit pin real, validation-artifact digests traceable in-repo. Scope discipline and limitations disclosure are exemplary for this venue. The only issues are cosmetic/editorial: an empty "Overview" section and one wording gap on realization counts. These do not affect correctness or reproducibility but a JORS referee/copyeditor would flag the stub section, so I withhold outright ACCEPT pending those two edits.

VERDICT: MINOR-REVISIONS
