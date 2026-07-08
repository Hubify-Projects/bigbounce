# P2 (v1.7.102) — Gemini Deep Research (Pro) — EXT DEEP round 2026-07-08

- Reviewer: Gemini (Pro model + Deep Research tool; deep multi-source pass, "Physical Review D Referee Report: Manuscript Review")
- Chat URL: https://gemini.google.com/app/3f934d409b094fe7
- Harvested: 2026-07-08 (full immersive report extracted; verified READ before recording)
- PDF: /tmp/deep_P2.pdf md5 cca2e95f45507d02bb3c76951f83d090, page 1 "(Dated: July 8, 2026)", v1.7.102
- Full report: _raw_P2_gemini.txt (30 KB, 14 issues)

## PROMPT
You are an expert referee for Physical Review D. Review the attached manuscript to the standard you would apply to a real submission. Respond with exactly: (1) VERDICT ... (2) ISSUES ... (3) One sentence on whether the central claim is supported. Be rigorous and specific; do not inflate or soften.

## VERDICT (verbatim)
**(1) VERDICT: MAJOR REVISIONS**

## ISSUES (14 — headers verbatim)
1. Sec II.A / App A — Cai-Li factor-of-two resolution: "the theoretical proof remains fundamentally incomplete because it relies entirely on a time-ordered operator-algebra identity rather than the full numerical execution of the in-in contour integrals across the bounce phase." (symbolic re-summation "commendable... identifies a clear algebraic anomaly" but wants full numerical in-in)
2. Sec II.C — faithful cubic transmission through the bounce / Quintin no-go evasion: "Relying on a dimensional scaling estimate derived from the gradient expansion to dismiss third-order bounce contamination is inappropriate for a study forecasting σ(f_NL)≈0.7."
3. Secs IV & VII — additive-quadrature systematic budget: not a joint-marginalized Fisher.
4. Sec III.A & VII.C — SDB / f_NL / GR-projection degeneracy.
5. Sec VI — Bayesian evidence prior-volume dependence (curvaton-natural [−5,5] prior drops BF to ≈4 = "positive" not "strong" on Kass-Raftery).
6. Sec III.B — template mismatch / estimator orthogonality / residual non-local tails.
7. Sec IV — RSD omission of Fingers-of-God damping.
8. Literature — missing PBH / PTA discussion.
9. Sec VIII.B — f_NL running.
10. Sec II.C — negligible fermion-sourced torsion in Einstein-Cartan-Holst.
11. Sec VII.D — photo-z outlier ~5% impact.
12. Sec V — MegaMapper framing/maturity.
13. Sec III.A — scale-dependent bias local approximation.
14. Conclusion — conformal-Fermi vs gauge frame observables.

## (3) CENTRAL CLAIM (verbatim)
"The central claim—that a specific matter-dominated bouncing cosmology unambiguously predicts a local non-Gaussianity amplitude of −35/16 which falls within the measurable sensitivity envelope of upcoming large-scale structure surveys like SPHEREx—is theoretically promising and identifies a crucial literature discrepancy, but it remains currently unsupported due to the lack of explicit numerical in-in integration across the bounce phase and the reliance on a mathematically invalid, unmarginalized additive-quadrature systematic error budget."

## TRUTH-AUDIT SUMMARY
- VERDICT: MAJOR REVISIONS (14 issues). Same tier as fast-baseline Gemini P2 (MINOR/MAJOR across rounds); no regression to REJECT (softer than ChatGPT-DR's REJECT this round).
- The TWO load-bearing objections are both KNOWN, DISCLOSED limitations, NOT new errors:
  - Issue #1 (wants full numerical in-in contour integration, not operator-algebra/vertex re-summation): the −35/16 value itself is NOT challenged as wrong ("identifies a clear algebraic anomaly"). The paper explicitly does NOT claim a full numerical in-in re-derivation and flags full cubic in-in as its #1 follow-up (source-verified: 02_full_draft.tex line 1370 + changelog v1.7.89). ALL THREE deep reviewers (Gemini + Grok-Heavy + ChatGPT-DR) converge on this same disclosed-scope demand — textbook pattern-066 referee convergence on a disclosed limitation, not a genuinely-new finding.
  - Issue #2 (cubic transmission = dimensional scaling estimate): the paper labels assumption (d) the "load-bearing caveat (★)" and states the full numerical Maldacena-integral evaluation at the bounce is future work (Sec II.C / conclusion). Disclosed.
  - Issue #3 (additive-quadrature budget): the paper explicitly labels this a "scoping sensitivity envelope under the additive-quadrature heuristic... not a joint-covariance forecasted measurement precision, with no full bispectrum joint Fisher over the systematic nuisances performed here" (source-verified line 1305). Disclosed.
- Issue #5 (Bayes prior volume → BF≈4): the paper ITSELF states the curvaton-natural [−5,+5] prior gives BF≈4 (source-verified line 995) — the reviewer is quoting the paper's own honest disclosure.
- Issues #4,6–14: refinement/rigor-enhancement/literature-context requests (FoG damping, PBH/PTA discussion, torsion, photo-z, MegaMapper framing) — all editable additions or already-disclosed approximations, none a demonstrated error.
- GENUINELY-NEW REAL FINDING: ZERO. The −35/16 amplitude is not shown wrong; every load-bearing objection is a source-cited re-flag of a limitation the paper discloses itself. Nothing dispositioned non-real without source; nothing fabricated.
