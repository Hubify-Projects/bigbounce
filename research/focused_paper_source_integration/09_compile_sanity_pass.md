# 09: Compile / Source Sanity Pass

## LaTeX Compiler: NOT AVAILABLE
pdflatex/xelatex not installed on this machine. Static source review performed instead.

## Static Source Sanity Check

### Structure
- ✅ \documentclass, \begin{document}, \end{document} present
- ✅ All sections numbered and labeled
- ✅ Abstract within \begin{abstract}...\end{abstract}
- ✅ Bibliography via \bibliography{focused_paper_refs}

### Citations
- ✅ All \citep{} keys have corresponding .bib entries
- ✅ 16 bibliography entries covering all referenced works
- ⚠️ \bibliographystyle{JHEP} — need to ensure JHEP.bst is available or switch to a standard style (e.g., unsrtnat)

### Figures
- ✅ fig3_kmin_cliff.png referenced and present in directory
- ⚠️ Fig 1 (shape function), Fig 2 (survey comparison), Fig 4 (thresholds), Fig 5 (inflation comparison) are GENERATED but not yet \includegraphics'd in the tex. Only Fig 3 is inserted.
- FIX NEEDED: Add \includegraphics for Figs 1, 2, 4, 5 at appropriate locations

### Tables
- ✅ Table 1 (benchmarks) — present and correct
- ✅ Table 2 (Bayes factors) — present and correct
- ✅ Table 3 (GR scenarios) — present and correct

### Equations
- ✅ 3 numbered equations (shape function, |B|_NL, scale-dependent bias)
- ✅ All use standard LaTeX math formatting
- ✅ Custom macros (\fnl, \BNL, \Pzeta) defined

### Potential Issues
1. \bibliographystyle{JHEP} may not compile without JHEP.bst → change to `unsrtnat` for portability
2. Only 1 of 5 figures is actually inserted → add remaining 4
3. No \usepackage{cite} or similar — may need for citation sorting
4. Author affiliations and ORCID not included (standard for submission)

## Recommended Fixes Before Submission
1. Switch bibliographystyle to `unsrtnat` (universally available)
2. Insert remaining 4 figures with \includegraphics at marked locations
3. Add proper author affiliation
4. Install LaTeX compiler for actual compilation test
