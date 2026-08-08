# P5 v0.1.128 exact-PDF verdict matrix

Frozen input: `p5_desi_chirality.pdf`, SHA-256 `f1ba53bf236cbaecbd7b8d3b76b46411d43bd90fb7907650a742a5b4739dcc22`, 41 pages. All raw verdict words below are preserved exactly; no cross-vendor fallback was used.

| Leg | Model / route | Modality | Raw verdict | Raw issue structure | Central-claim position |
|---|---|---|---|---|---|
| OpenAI API | `gpt-5.5` | native PDF, Files API `input_file` | **MAJOR REVISIONS** | 4 major, 7 minor | Narrow exploratory classifier-labelled fixed-redshift-space null is broadly supported; selection/control, interval terminology, and provenance prevent acceptance. |
| xAI API | `grok-4.3` | native PDF, xAI file input | **MINOR REVISIONS** | 0 major, 3 minor | Central claim supported within the stated limitations. First request failed because xAI attempted to store an oversized response; the same model succeeded on attempt 2. |
| Google API | `gemini-3.1-pro-preview` | native PDF, inline PDF | **MINOR REVISIONS** | 2 items under `MAJOR ISSUES`, 3 minor, despite the overall MINOR verdict | Central null described as rigorously supported; companion-paper tracking and T-Web disclosure requested. |
| Codex subscription | `gpt-5.6-sol`, reasoning `high` | authenticated subscription CLI, read-only, all 41 rendered pages | **MAJOR REVISIONS** | 2 major, 7 minor | Displayed primary null is supported; unmatched selection function and row-level bootstrap provenance prevent acceptance. |

## Objective synthesis

- Verdict board: **2 MAJOR / 2 MINOR / 0 REJECT / 0 ACCEPT**.
- All four legs reproduce or affirm the load-bearing descriptive null. No leg demonstrates a nonzero void/non-void chirality contrast.
- The two MAJOR verdicts converge on genuine publication gates: the primary control is not selection-function matched, and the highlighted cluster bootstrap is not yet backed by an immutable archived row-level input snapshot.
- Several remaining reader-visible defects are smaller but real: endpoint values are mislabeled as interval half-widths, the quadrature uses the older 0.44 pp counting term, the membership-reassignment extrapolation is unsupported, the dark-program residual is under-described, Fig. 8 retains extraneous axes, and null/family terminology is inconsistent.
- No readiness, acceptance, SSOT, site, Convex, version, or ledger state is changed by this matrix.

