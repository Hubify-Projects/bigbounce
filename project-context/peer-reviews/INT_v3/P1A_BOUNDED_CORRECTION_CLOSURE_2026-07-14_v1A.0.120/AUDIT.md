# P1A v1A.0.120 bounded-correction audit

## Frozen result

- Version: v1A.0.120
- Source SHA-256:
  bd60f9e22bd6490eea1625a8a3c0267dd506b8fe69c51d85d6dfb5848384c09e
- PDF SHA-256:
  6472db7741deebd4100fe3191d5ef23a9b0b7960c4284cf53e9e4761f62f535b
- PDF: 8 letter-size pages, 162,171 bytes.
- Build: Tectonic/XeTeX pipeline completed with BibTeX and no fatal error.

## Truth-audited correction

1. Every active claim that kappa*n_psi^2 is a rigorous finite-density bound
   was removed.  It is now a coefficient-one dimensional homogeneous
   benchmark.  The abstract and body state that number density supplies no
   inequality for the renormalized coincident composite <J5 J5> without a
   specified state, polarization, relativistic normalization, species
   contractions, and contact-renormalization prescription.
2. The active manuscript now centralizes the mostly-plus Lorentzian metric,
   epsilon_0123=+1, gamma-five, full-weight torsion, coincident-composite,
   and Grassmann/operator-ordering conventions.  Appendix A explicitly maps
   its scalar row to +G_s (bar psi psi)^2 and G_s=-3*kappa/16.
3. The Holst Cartan bivector operator and inverse are displayed.  Direct
   multiplication gives the gamma^2/(1+gamma^2) inverse confirmed by
   Freidel--Minic--Takeuchi Eq. (6).  The theorem is restricted to an
   invertible tetrad and real finite nonzero gamma; complex self-dual
   gamma=+/-i is excluded.
4. The tensor wave equation is labeled an illustrative source-free linear-FRW
   specialization.  The all-order statement is equality of the classical
   action/EOM to GR on the torsion-free branch.  Equal helicity evolution
   operators are no longer misreported as equal amplitudes without equal
   initial data.
5. The total-derivative item was removed from the proof.  The pointwise
   torsion-free algebraic Bianchi identity is explicitly the operative step;
   Nieh--Yan remains a non-load-bearing explanatory decomposition.

## Algebraic and manuscript checks

- python3 arxiv/scripts/fierz_lemma_check.py: PASS.
- python3 arxiv/scripts/njl_gap_equation_route1.py: PASS; six-row values
  unchanged, G_scalar/kappa=-3/16, scalar sign remains repulsive in the
  declared convention.
- TeX log: 0 LaTeX errors, 0 undefined controls/citations/references,
  0 overfull hboxes/vboxes.  Underfull paragraph warnings only.
- Extracted PDF text contains the new title, version, benchmark boundary,
  self-dual exclusion, illustrative-linear label, and all-order action/EOM
  statement.
- Active raw texttt path scan: 0.
- Date/version line is contained on page 1.

## Visual and link audit

- All 8 pages rendered at 150 dpi and were inspected.
- No clipping, column overlap, off-page equations, broken tables, malformed
  glyphs, or date/title overflow.
- 35 link annotations; 21 unique targets including one mailto target and 20
  HTTP URLs.
- HTTP audit: 15 targets returned 200.  Five publisher DOI resolvers returned
  403 to automated curl (AIP/APS); their DOI syntax and bibliography targets
  are intact.  All arXiv and repository-artifact targets returned 200.

## Honest status

The two merged technical majors and three bounded technical minors normalized
in the v1A.0.119 truth audit are corrected in this exact PDF.  No fresh review
panel has evaluated v1A.0.120, so no reviewer verdict is upgraded here.
Gemini's v1A.0.119 REJECT was a novelty/venue judgment and remains unresolved;
these correctness edits do not establish originality or PRD acceptance.
