# TRUTH AUDIT — P1B v2B.0.13 — ROUND 2026-07-22 (EXACTPDF a84bea85, CLAUDESTACK-CONFIRM)

- Paper: `arxiv/paper1b_namaster_proof.tex` / `arxiv/paper1b_namaster_proof.pdf`
- Exact-PDF binding: sha256 `a84bea85ad993f02230d439825e9a220be894e390e0d1f172d046e50c687cbee` — MATCH across all three legs (Claude INT, Grok, Gemini).
- Venue: Journal of Open Research Software (software metapaper).
- Legs audited: Claude INT (MINOR-REVISIONS, 2 minors), Grok grok-4.3 (MINOR-REVISIONS, 3 minors), Gemini 3.1-pro-preview (MINOR-REVISIONS, 3 minors).
- Verdict classes: ALREADY-TRACKED-GATE / DISCLOSED-RE-FLAG / SCOPE-VENUE-OPINION / FALSIFIED / GENUINELY-NEW-REAL (when in doubt → GENUINELY-NEW-REAL).

## Per-finding verdict matrix

| # | Reviewer | Finding gist | Verdict | Evidence |
|---|----------|-------------|---------|----------|
| 1 | Claude INT MINOR-1 | §1 "Overview" is an empty stub — only a `\paragraph{Keywords.}` line, no prose body | **GENUINELY-NEW-REAL** | tex L79–82: `\section{Overview}` immediately followed by `\paragraph{Keywords.}` and the keyword list only; no body sentence. Confirmed visually page 1. Real presentation defect. |
| 2 | Claude INT MINOR-2 | §8 vs §11 realization-count wording ambiguous (§8 "two nonzero angles, 500-realization"; null count unstated; §11 "500 at each of three") | **GENUINELY-NEW-REAL** | tex L262–265 (§8): "For each of two nonzero injected angles, a 500-realization … run … The null injection recovered 0.000°" (null count NOT stated). tex L316 (§11): "500 realizations at each of three injected angles." GROUND-TRUTH VERIFIED below — the true number is 500 at each of THREE (2 nonzero + null); §8 should state the null also used 500. Presentation-clarity fix, not a numeric error. |
| 3 | Grok MINOR-1 | Manuscript "v2B.0.13" (title) vs body "Version 0.1.7" = "irreproducible mismatch" between declared release and documented artifact | **FALSIFIED** | Two intentionally distinct namespaces: `\paperVersion{v2B.0.13}` is the MANUSCRIPT stamp (tex L53, L59 `\date`); "Version 0.1.7" is the SOFTWARE PACKAGE version, consistent across `pyproject.toml` (0.1.7), `codemeta.json` (0.1.7), `CITATION.cff` (0.1.7) — verified by Claude INT too. No mismatch exists; the premise that they must match is false. |
| 4 | Grok MINOR-2 | §11 gives GitHub/commit/Zenodo but no PyPI/conda name, sdist/wheel, or `pip install namaster-proof` command | **SCOPE-VENUE-OPINION** | Package is repo-embedded + Zenodo-archived, not PyPI-published by design. §11 (tex L335) already supplies an install command: `python -m pip install ./packages/namaster-proof`. JORS accepts repo + immutable archive (Zenodo DOI 10.5281/zenodo.21481753, tex L348–352); PyPI/conda is a reviewer distribution preference, not a JORS requirement or correctness defect. |
| 5 | Grok MINOR-3 | §8 exact recoveries reported without releasing 500-realization input spectra, seeds, or mask files — "cannot be independently re-run from the manuscript alone" | **DISCLOSED-RE-FLAG** | Reproducibility inputs ARE released in-repo and SHA-bound: `reproducibility/p1_namaster_500mc/scripts/` (namaster_500mc.py, physical_spectra.py) committed; `summary.json` records `seed_base: 42`, full CAMB 1.6.6 params, `f_sky: 0.3226`, `n_mc_realizations: 500`; §11 Validation-artifacts (tex L359–367) binds `summary.json` (745b0a2f…) + `bandpowers.npz` (b00f850e…) by SHA-256. Deterministic seeds make it reproducible from the committed repo; §10 discloses these are software-recovery checks, not measurements. |
| 6 | Gemini MINOR-1 | §11 sentence "This closes the previously disclosed persistent-identifier submission blocker." reads as an editor/review-response remnant; remove | **GENUINELY-NEW-REAL** | tex L353–354 contains that exact sentence inside the Archive paragraph. It is meta-commentary on prior review state (DP1B-15 blocker), not text for a final published manuscript. Real editorial defect; safe to delete. |
| 7 | Gemini MINOR-2 | Abstract lists full "EE, EB, BE, BB" but Eqs (1)–(3) assume vanishing EB; §10 clarifies — add a clarifying sentence in §5 too | **DISCLOSED-RE-FLAG** | Already disclosed in §10 (tex L289–291): "Uniform rotation and initially vanishing EB are assumptions of the optimized three-component response; the general algebraic rotation helper accepts all four input spectra." Gemini itself acknowledges the §10 disclosure and requests duplication into §5. Not genuinely-new. (Optional 1-line clarity add noted in fix list.) |
| 8 | Gemini MINOR-3 | JORS template conformance — nest §5,§6 under §4; fold §8,§10 into §12 | **SCOPE-VENUE-OPINION** | Section nesting is an editorial/template preference; current top-level sections are coherent and complete. No correctness or reproducibility impact; a JORS copyeditor may restructure at production. Venue-structure opinion. |

## Ground-truth verification of the two Claude minors (verified against tex + campaign scripts + artifacts)

**Realization count (finding #2 / #3):** The campaign used **500 realizations at each of THREE injected angles** (two nonzero + one null). Proof:
- `reproducibility/p1_namaster_500mc/results/physical_spectrum_v2/summary.json`: `n_mc_realizations: 500` (single global setting), `results` block holds all three injections — `beta_paper1` (0.27°→0.27°), `beta_observed` (0.342°→0.342°), `beta_null` (0.0°→0.0°). `runtime_seconds: 701.5` ≈ 7×10² s; `realization_workers: 8` — both match §11.
- `scripts/namaster_500mc.py`: L25 "Aggregate across 500 Monte Carlo realizations per β"; L282 "Running {N_REAL} MC realizations per β value"; L249–250 each realization measures ALL betas (the null 0.0 is one of `betas`). So the null shares the same 500 realizations as the nonzero angles.
- Therefore §11's "500 realizations at each of three injected angles" is TRUE. §8 is the under-specified side (states 500 only for the two nonzero, leaves the null's count implicit). Fix = make §8 state the null run also used 500 realizations. **Do NOT change §11's "three."**

**Overview stub (finding #1):** tex L79–82 confirmed — `\section{Overview}` body is only the Keywords paragraph. Real.

## GENUINELY-NEW-REAL FIX LIST

1. **§1 Overview stub (Claude MINOR-1).** Either (preferred) delete `\section{Overview}` (tex L79) and move `\paragraph{Keywords.}` + keyword list (L81–82) to immediately follow the `\end{abstract}` (L77), so keywords sit under the abstract with no empty heading; OR add a one-paragraph overview body under §1 summarizing what `namaster-proof` is and the two error classes it eliminates. Prefer the delete-and-relocate to avoid inventing prose.

2. **§8 null realization count (Claude MINOR-2).** In §8 (tex L262–266), change the null sentence so it states the count. Replace "The null injection recovered 0.000°." with: "The null injection, also run with 500 realizations, recovered 0.000°." This anchors §11's "500 realizations at each of three injected angles" (L316) unambiguously. Verified true number = 500 at each of 3 (2 nonzero + null); §11 stays as-is.

3. **§11 review-response remnant (Gemini MINOR-1).** In §11 Archive paragraph (tex L353–354), delete the sentence "This closes the previously disclosed persistent-identifier submission blocker." (remnant of DP1B-15 review state; not manuscript-appropriate). Leave the surrounding Zenodo DOI sentences intact.

### Optional (non-blocking, DISCLOSED-RE-FLAG — apply only if cheap)
- §5 EB-clarity (Gemini MINOR-2): optionally add one sentence in §5 noting the optimized three-component response assumes initially vanishing EB (already in §10 L289–291), for upfront reader clarity. Not required; content already disclosed.

## Summary counts
- GENUINELY-NEW-REAL: 3 (Claude MINOR-1, Claude MINOR-2, Gemini MINOR-1)
- DISCLOSED-RE-FLAG: 2 (Grok MINOR-3, Gemini MINOR-2)
- SCOPE-VENUE-OPINION: 2 (Grok MINOR-2, Gemini MINOR-3)
- FALSIFIED: 1 (Grok MINOR-1)
- ALREADY-TRACKED-GATE: 0
- BLOCKER/MAJOR across all legs: 0
