# Retired: main.tex monolith

**Retired:** 2026-09-02

`main.tex` / `main.pdf` / `main.bbl` / `main_arxiv_submission.tar.gz` in this
directory are the June-2026 v2.3.18 unified monolith paper. It was superseded
by the split-paper architecture and was still carrying the stale
`f_NL = -35/8` matter-bounce value that the rest of the repo moved off of in
the v110 text sweep (see directive I6 in `CLAUDE.md` for the propagation
lesson).

`README-SUBMISSION.txt`, `make_overleaf_zip.sh`, and `compile_on_pod.sh` are
this monolith's own submission tooling (the README's title/abstract text is
the monolith's "Geometric Dark Energy from Spin-Torsion Cosmology" framing,
not any currently registered paper) — retired alongside it rather than
repointed, since each active paper now has its own submission-tarball
workflow (see e.g. `arxiv/submission_tarballs/` for P1A).

The registered, actively maintained P1A source is
**`arxiv/paper1a_ech_nogo.tex`** (see `project-context/paper_registry.json`).

Do not compile, cite, or submit anything from this directory. It is kept for
historical/lineage reference only.

See `project-context/PORTFOLIO_DECISION_2026-09-02.md` §1 for the portfolio
architecture decision that formalized the split away from this monolith.
