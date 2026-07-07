# MERGE PROPOSAL — Unified Paper 1 (P1A + P1B → one PRD article)

**Status:** PROPOSAL for Houston's approval. Built in isolated worktree
`worktree-agent-ae5e7eab3fb9e3fda` on branch `worktree-agent-ae5e7eab3fb9e3fda`.
Committed there only — **NOT pushed, NOT on `main`.** The two-paper layout on
`main` is untouched and remains the fallback.

**Why:** All three EXT reviewers + both API vendors consistently reject P1B as
"not a standalone article — fold into P1A" (Gemini + Grok explicitly recommend
merging). This merge makes every P1B number in-paper, which simultaneously kills
the P1B standalone-rejection class AND the P1A companion-reliance rejection class.

**NO NUMBER WAS CHANGED.** Verified: P1B's MCMC values (309,189 samples;
`H_0 = 67.68 ± 1.06`; `ΔN_eff^(ECH) ~ 10^-44`; NaMaster `β̂ = 0.238°`, bias
`-0.032°`/`-0.040°`; ALP prior-predictive `11.6%`/`23.9%`, `C_{aγ}=8`, `36 H_0`)
and P1A's `f_NL = -35/16` all carried through byte-identically. The single live
`-35/8` in the unified file is P1A's own (correct) sentence citing the *superseded*
Cai value that P2 traced to a spurious term — unchanged from P1A.

---

## Output

| Artifact | Value |
|---|---|
| Source | `arxiv/paper1_unified.tex` |
| PDF | `arxiv/paper1_unified.pdf` |
| Pages | **56** (P1A 37 + P1B 22 = 59, minus 3 via dedup) |
| Bytes | 2,518,462 |
| md5 (PDF) | `6f6921ebfb208c0227f51e6933e64d06` (recompiles cleanly; not pinned) |
| Undefined refs | **0** |
| Undefined citations | **0** |
| Overfull hbox > 50pt | **0** (only 2 overfull total: 2.88pt, 0.67pt) |
| Bibliography | shared `references.bib` (102 entries; every P1B cite key already present) |

---

## Structure map (section / appendix)

**Body — P1A verbatim, unchanged** (§I–§XV: Introduction, Theoretical Framework,
Observational Signatures, Four-Route No-Go, Data Methods, Systematics,
Falsifiability, Related Work, Structural Constraints / 14 Barriers,
Perturbation-Transparency Result, Hybrid Loophole, Discussion, Surviving Tests,
Limitations, Conclusions). Title, author, abstract, and every theorem/closure
kept exactly as in P1A v1A.0.113.

**Appendices:**

| App | Title | Origin |
|---|---|---|
| A | Complete Parameter Summary | P1A (unchanged) |
| B | Dimensional Status of the Parity-Odd Operator | P1A (unchanged) |
| C | Line-of-Sight Birefringence from Maxwell–Chern–Simons | P1A (unchanged) |
| **D** | **Cosmological Constraint Methodology** — ΛCDM+ΔN_eff MCMC proxy, bespoke ECH-sector ΔN_eff bound (derivation intact), cosmological fits & model comparison | **P1B §tensions + §verification (incl. §torsion_neff) + §cosmo_fits** |
| **E** | **NaMaster Pseudo-C_ℓ E→B Pipeline Validation** | **P1B §data_cmb** |
| **F** | **Spectator-ALP Cosmic-Birefringence Consistency Check** (incl. prior-predictive accommodation-cost MC) | **P1B §birefringence_check** |
| **G** | **Data Availability, Reproducibility Materials, and Sampled-Parameter Priors** | **P1B App: reproducibility + claims classification + ALP priors** |

The **ΔN_eff bound** (`~10^-44` at BBN, from integrating out algebraic torsion)
is merged into App D with its first-principles derivation intact (`eq:neff_bound`,
`eq:torsion_ratio`, `eq:fourfermion` all preserved and internally referenced).
The **reproducibility manifest** becomes the unified data-availability appendix G.

---

## What was deduplicated

- **P1B abstract** — dropped (paper keeps P1A's single abstract).
- **P1B Introduction + "Imported theory results (restated for standalone
  readability)"** — dropped. This restatement block was P1B's summary of P1A's
  own results (13 barriers, transparency theorem, surviving `f_NL`), now redundant
  because P1A's body states them directly. *Bonus:* this block carried a **stale
  `f_NL = -35/8`** (P1B was never swept to `-35/16`); dropping it means no stale
  number is imported — a deletion, not a number change.
- **P1B Conclusions** — dropped (paper keeps P1A's conclusions).
- **Shared preamble / packages / macros** — collapsed into one preamble.
  P1B-only additions imported: `\usepackage{array}`, `\sigmaunit`, `\repoBase`,
  `\artifact`.
- **P1B `\tableofcontents`** — dropped (P1A has none).
- **Shared bibliography** — one `\bibliography{references}`.

## Cross-reference conversion (the core of the merge)

- Every live **`\cite{Golden2026P1b}` / "Paper I(b)" / "companion" MCMC pointer in
  P1A's body → internal `\ref{app:cosmo_methodology}`** (or the specific folded
  appendix). Every imported number is now in-paper.
- P1B's self-cites **`\cite{Golden2026P1a}` / "Paper I(a)" → "the main text"**
  (they now point at this same paper).
- P1B section labels namespaced `sec:X → sec:p1b_X` to avoid collision with P1A's
  `sec:intro` / `sec:conclusions`; all internal refs updated consistently
  (0 undefined).
- The SPHEREx f_NL Fisher forecast pointer stays an **external** companion cite
  `\cite{Golden2026P2}` — P2 is a separate paper and is **not** merged.

---

## What the merge FIXES (rejection classes eliminated)

1. **P1B standalone-rejection** ("not a standalone article — fold into P1A";
   Gemini + Grok explicit) — eliminated: P1B no longer exists as a standalone
   item; its content is appendix material to a substantial no-go paper.
2. **P1A companion-reliance** ("numbers imported by citation cannot be refereed
   until the companion posts"; recurring MAJOR from all 3 EXT reviewers) —
   eliminated: every former companion-imported number now resolves to an internal
   `\ref`, refereeable in-document.

All honest caveats from BOTH papers are kept verbatim: the "not a spin-torsion
theory module" MCMC scope statement, the NaMaster "pipeline-recovery not
sky-detection" caveat, the spectator-ALP `θ_i ≪ 1` fine-tuning disclosure and
"not a distinctive ECH prediction" note, and the "no model-preference inference"
deferral.

## What Houston LOSES by merging

- **The separate P1B arXiv item** — there is no longer an independent
  "Technical Reproducibility Companion" paper on arXiv (one arXiv submission
  instead of two in wave 1). If the two-item coordinated submission has value
  (e.g. a citable standalone reproducibility note), that is the reason to keep
  two papers.

## Alternative (stays intact on `main`)

The two-paper layout — `paper1a_ech_nogo.tex` (v1A.0.113) +
`paper1b_mcmc_companion.tex` (v1B.0.103) — is **unchanged on `main`** and remains
the fallback if Houston prefers the separate coordinated submission. This proposal
adds `paper1_unified.tex`/`.pdf` in the worktree only; it does not modify or delete
either source paper.

---

## Verification performed

- 4-pass pdflatex + bibtex: **0 undefined refs, 0 undefined citations**.
- `/latex-audit` basics: **0 overfull hbox > 50pt** on any page (2 trivial
  overfulls total, 2.88pt & 0.67pt).
- Single `\begin{document}` / `\end{document}` / `\title` / `\begin{abstract}` /
  `\appendix` / `\bibliography`; no duplicate labels.
- Visual render (pdftoppm) of page 1, App-D start (p.33), and the folded NaMaster
  figure (p.55, Fig. 10) — clean two-column layout, cross-refs resolve to
  appendix subsections ("Sec. E 1"), figure values intact.
- Number-preservation grep on all headline P1A + P1B values — all present,
  none altered.
