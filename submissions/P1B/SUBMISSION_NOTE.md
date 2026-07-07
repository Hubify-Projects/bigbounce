# SUBMISSION_NOTE — P1B ↔ P1A coordinated cross-reference

**Paper:** P1B — `arxiv/paper1b_mcmc_companion.tex`, v1B.0.101 (22 pp)
**Bundle:** `submissions/P1B/arxiv_p1b_v1B.0.101.tar.gz`
**Status:** publication-ready. Content error-clean per internal full-source
review (2026-07-05); the one concrete external quantitative item (reduced-M_Pl
ΔN_eff convention) is fixed (v1B.0.100). Remaining external objections are
venue/scope (standalone-vs-appendix), Houston-gated, not content errors.

## Coordinated two-paper posting

P1B and P1A (`arxiv/paper1a_ech_nogo.tex`) post together. **P1B goes up in the
first wave** so P1A can cite P1B's assigned arXiv identifier the same day, and
reciprocally P1A's identifier is inserted back into P1B.

### The placeholder marker

Every reference from P1B to P1A that should carry the live arXiv ID uses the
literal clearly-marked placeholder:

```
[arXiv:XXXX.XXXXX]
```

It appears in exactly two places in the P1B source:

1. **`arxiv/references.bib`**, bib key `Golden2026P1a`, `note =` field:
   `"Companion paper, posted concurrently on arXiv [arXiv:XXXX.XXXXX --- ID inserted at coordinated submission]"`
   — renders in the bibliography wherever `\cite{Golden2026P1a}` is used.
2. **`arxiv/paper1b_mcmc_companion.tex`**, Introduction, coordinated-submission
   paragraph (the sentence beginning "Because the two papers are posted
   together…"), inline `\mbox{\texttt{[arXiv:XXXX.XXXXX]}}`.

### Insertion procedure at submission

1. Submit the P1B bundle (`arxiv_p1b_v1B.0.101.tar.gz`) → obtain P1B's arXiv ID.
2. Insert P1B's ID into P1A wherever P1A references P1B (P1A carries the mirror
   placeholder in its own `Golden2026P1b` bib entry / cross-ref).
3. When P1A's ID is assigned, replace BOTH `[arXiv:XXXX.XXXXX]` occurrences in
   P1B above with P1A's real `arXiv:NNNN.NNNNN`.
4. Recompile P1B (`pdflatex ×4 + bibtex`), re-verify 0 undefined refs, re-mirror
   the PDF to all served paths, bump Convex `paperVersions`, rebuild the bundle,
   and commit — i.e. run standing Directive-G one final time on the ID insertion.

Do NOT hand-edit the compiled PDF; always recompile from source after inserting
the ID so the bundle, served copies, and Convex md5 stay in three-way agreement.
