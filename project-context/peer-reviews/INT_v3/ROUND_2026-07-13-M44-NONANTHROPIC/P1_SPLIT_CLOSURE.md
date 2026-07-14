# P1 M44 split-revival closure report

**Date:** 2026-07-14  
**Inputs:** M44 P1U non-Anthropic INT/EXT truth audits and the preserved separate sources  
**Outputs:** P1A `v1A.0.116`; P1B `v1B.0.105`  
**Historical unified source:** `arxiv/paper1_unified.tex` was not edited.

## Decision

The six-paper topology is restored at the paper-local level by treating P1A and P1B as distinct submissions. The M44 P1U reviews were most persuasive where they identified a mismatch between the manuscript's broad four-route rhetoric and its actually derived results. The closure therefore removes the unsupported claim surface rather than relabeling it.

## P1A closure

P1A now retains only:

1. the first-order minimal ECH action and algebraic elimination of torsion;
2. the resulting Planck-suppressed axial contact operator, late-density bound, and explicitly standard-mean-field NJL check; and
3. the classical constant-Immirzi transparency identity on the minimally coupled canonical-scalar torsion-free branch.

Reader-visible R2/R3 dark-energy closures, operator-basis-complete rhetoric, single-scale dark-energy ansatz, ALP/NaMaster/MCMC material, barrier catalog, galaxy payload, and forecast claims were retired. Shapiro--Teixeira and Benedetti--Speziale appear only as literature context whose cosmological matching remains unresolved.

The retained NJL computation is conditional. The scalar direct-channel coefficient is repulsive (`-3 kappa / 64`), the largest scanned scalar magnitude ratio is `0.156`, and the axial magnitude ratio is `0.31`. These do not remove mean-field Fierz ambiguity or exclude non-minimal/beyond-mean-field completions. The formal `M_Pl/sqrt(gamma)` cutoff point is above `M_Pl` and is labeled a sensitivity stress test, not a controlled EFT regime.

## P1B closure

P1B remains a standalone computational paper. Its live title/abstract/scope now classify:

- the Cobaya/CAMB result as a stock-CAMB generic extra-radiation proxy;
- the NaMaster result as a foreground-free synthetic injection/recovery validation; and
- the spectator-ALP result as a generic GR+ALP accommodation/prior-volume study.

None is ECH evidence, a bounce test, or support for P1A. The numerical payload was preserved; submission metadata, Bayes factors, full real-sky foreground/calibration treatment, and final archive IDs remain open and disclosed.

## Verification performed

- Both papers compiled successfully with two explicit Tectonic invocations after the edits.
- P1A: 6 pages; 0 TeX errors; 0 undefined references/citations; 0 overfull boxes.
- P1B: 21 pages; 0 TeX errors; 0 undefined references/citations; 0 overfull boxes.
- Both BibTeX runs have 0 errors; the sole remaining `.blg` warning is the APS style's `jnrlst` control message.
- Every page of both PDFs was rendered at 110 DPI and visually inspected; no margin escape, column overlap, figure clipping, or title/date overflow was found.
- P1A Fierz and NJL scripts ran successfully. The NJL script's historical reversed cutoff-scaling explanation was corrected and re-run.
- Every active P1A/P1B `\\includegraphics` file and every reader-visible repository artifact path checked locally exists.
- The final PDFs contain 72 HTTP(S) links. All 10 links into this repository map to existing local paths; the 62 external targets returned 46 successful HTTP 200 responses and 16 publisher anti-bot HTTP 403 responses, with no 404 or transport failure. This audit exposed and corrected a mistyped Br\"uggen DOI (`10.1023/A:1026747107994`).

Final SHA-256 checksums:

- P1A PDF: `69bf8e8980ac67801347ce520d19556804e53a5138a33f8139bfa6d182450d2f`
- P1B PDF: `2d35148497808b619500aca39d3be67d074b07647c3f68b5ce7c4b4d7db24d35`
- NJL result JSON: `30d612c5ccedb3bea00c8dcce68cc38e7a56e73b05831ab66daefe805985cc4f`

## Honest residual blockers

1. P1A is a six-page focused note after the unsupported material is removed, not the aspirational 30--35-page theory paper. Padding it with retired claims would be scientifically worse. Venue/novelty fit needs a fresh review.
2. P1A does not derive R2/R3 cosmological matching and therefore cannot claim a complete dark-energy no-go.
3. P1B remains limited by stock CAMB, synthetic foreground-free maps, a summary-likelihood ALP fit, omitted Bayesian model comparison, and pending immutable submission identifiers.
4. Neither v1A.0.116 nor v1B.0.105 has yet received a fresh independent non-Anthropic review. No readiness score or verdict word is upgraded by this closure report.
5. No site, SSOT, Convex, root `version.json`, shared PDF mirror, tarball, or external archive was changed.
