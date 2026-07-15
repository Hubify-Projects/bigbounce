# Proactive Six-Paper Portfolio Sweep — 2026-07-15

## Outcome

This was the first enforced portfolio sweep under the new rule that no review
packet may be created without a content-addressed six-paper preflight receipt.
It found two real release-contract defects before another review round, repaired
four prevention-tool false positives, and converted both real defects into
regression gates. No reviewer verdict was generated and no readiness score was
raised.

| Paper | Proactive result | Disposition | Readiness |
|---|---|---|---:|
| P1A | Einstein--Cartan coefficient warning was a detector false positive: `-3πG/2 = -3κ/16` for `κ=8πG`, and the manuscript states the limit explicitly | Pattern-040 detector corrected and regression-tested | 62 hold |
| P1B | The 195-artifact manifest named base `75477aa4…`, but one script matched `97ceca7f…`; all 171 Git blobs and 24 LFS pointers match the corrected base | Manifest provenance repaired; exact verifier added to portfolio gate | 56 hold |
| P2 | Eight artifact failures were resolver false positives for contextual paths | Resolver corrected; artifact gate passes | 80 hold |
| P3 | Catalog validator passes; current log retains a small formatting-evidence discrepancy and the current exact tarball must be rebuilt | Open release task; no review dispatch yet | 56 hold |
| P4 | Claim/catalog validators pass; exact v1.0.255 review and a current tarball remain open | Eligible only after clean portfolio receipt | 80 hold |
| P5 | Manuscript falsely claimed a frozen historical full DESIVAST join that does not exist in the worktree or reachable Git history | Closed in v0.1.134; A39/A40 bounded to the GALZONE/VoidFinder control | 74 hold |

## P5 v0.1.134 exact release evidence

- Canonical PDF: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf`
- Version: `v0.1.134-2026-07-15`
- Pages: 39
- SHA-256: `c2ecb845b28ef890a1b1b4105723f52faf41dca8307e3322aaae9f676763afc6`
- MD5: `ca62080dfbbc1c173418d123f72fc145`
- Retention manifest:
  `project-context/pdf-archive/manifests/2026/07/20260715T233910Z-21dea42f4654.json`
- Convex row: `k572q7n4t8gcaztkd0pnz5e2898ajrrh`
- Every canonical and legacy P5 served alias is byte-identical.

### LaTeX/PDF audit

```text
LATEX AUDIT — p5_desi_chirality.pdf
──────────────────────────────────
Compile errors:        0
Undefined refs/cites:  0
Overfull hboxes:       0
Broken local URLs:     0 / 40 GitHub-main links
External endpoints:    8 / 8 resolved (APS DOI endpoint returns an automated-client 403, not 404)
Page-1 version/date:   PASS
Visual review:         PASS, all 39 pages
Final-render equality: 39 / 39 pages pixel-identical to inspected render

Verdict: PASS
```

The first compile produced an otherwise blank 40th page because two lines landed
before a forced `\clearpage`. The visual gate caught it; removing that unnecessary
break restored a clean 39-page layout. A clean LaTeX exit alone would not have
found this regression.

## Learning-loop accelerations implemented

1. **Review dispatch now fails closed on portfolio artifacts.** A missing claimed
   artifact prevents receipt creation and therefore prevents Codex, Grok, Gemini,
   or external-browser dispatch.
2. **Known findings became executable regressions.** P1B manifest provenance and
   P5 artifact availability are now covered by focused tests and the portfolio
   gate rather than remembered instructions.
3. **False-positive detectors were repaired, not waived.** Contextual path
   resolution, caption parsing, the P1A Einstein--Cartan limit, and P5 artifact
   scope now have explicit regression coverage.
4. **PDF retention precedes mutation.** The exact P5 PDF was retained before
   mirror and Convex updates; historical versions remain append-only.
5. **Alias inference was replaced by an explicit registry contract.** The old
   release helper hashed every PDF in each served directory and could miss an
   alias after it had already drifted. `paper_registry.json` now owns legacy
   aliases; the helper updates them directly in O(owned aliases), with tests.
6. **OpenAI routing remains subscription-only.** No OpenAI API call was made.
   No Anthropic/Claude leg was used. Direct-provider review is still allowed only
   for Grok and Gemini with raw receipts, after preflight passes.

## Remaining critical path

1. Create and verify a clean six-paper receipt at the committed P5 v0.1.134 release.
2. Build and standalone-verify the exact P5 and P4 current-version source bundles.
3. Run exact P4 v1.0.255 and P5 v0.1.134 non-Anthropic reviews; truth-audit before
   any closure or readiness change.
4. Execute P1B corrected production when compute funding is available; do not
   substitute prose for the missing result.
5. Complete public archive/DOI and human editorial/referee gates. Automated
   review cannot prove journal acceptance.
