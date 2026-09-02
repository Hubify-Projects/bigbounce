# Final author/visual review recommendations — 2026-09-02 (orchestrator, Fable 5.1)

Directive P composition: science closure 25 + evidence/reproducibility 25 +
automated review convergence 25 + packaging/PDF hygiene 20 = 95 when all four
agent gates hold; 100 only with Houston's per-paper sign-off (quote in SSOT).
Publishing mechanics (endorsement, venue submission, journal review) are a
separate phase and never subtract from the score.

## P4′ — `pipelines/p4prime_chirality_test/paper/` v4P.0.4 (ApJS) — **APPROVE** (agent gates), readiness → 95
- Boards: R1 (Claude major / Grok reject / Gemini reject) → 20 items closed;
  R2 (Claude major / Grok reject / Gemini major) → 21 closed incl. the
  primary-support monopole resolved from committed artifacts and a real
  Neyman-inversion 95% CL limit (0.75%); R3 verification (Claude minor /
  Grok reject / Gemini minor) → 7 editorial items closed. Truth-audits found
  no arithmetic or measurement-layer error in any round. Rounds stop (R2).
- Visual pass (pages 1, 2, 7, 11 at 55 dpi + full render): two-column
  AASTeX clean, no overflow, tables legible, Fig. 3 error bars readable,
  references resolve to DOIs/URLs; the P5 source is cited at its served URL
  with an honest "no DOI" note.
- Framing check: abstract names the detection-power floor (0.98%) and the
  CL limit (0.75%) with their exact meanings, concedes Shamir 2022's larger
  primary sample, and states that Popławski's papers give no quantitative
  amplitude. No bounce claim. Directive Q1 clean.
- Packaging: arXiv tarball `SSOT/arxiv_tarballs/paper4prime_chirality_test_arxiv_v4P.0.4.tar.gz`
  sha256 db108413…, standalone recompile PASS; PDF md5 ed6b8f66… mirrored;
  Convex k576j98m….
- Residual (not blocking, for Houston's read): (i) P5 has no Zenodo DOI —
  mint one as a new version under the P4 concept or as its own record before
  ApJS submission (click-list); (ii) the "Draft version" AASTeX header is
  standard and disappears at submission.
- Next phase: astro-ph.GA endorsement (CLVMAQ) → arXiv → ApJS portal
  (fields in `SSOT/PORTAL_KITS_2026-09-02.md`).

