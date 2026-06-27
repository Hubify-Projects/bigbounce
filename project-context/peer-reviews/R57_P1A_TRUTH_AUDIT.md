# R57 P1A — Hardened De-biased Truth Audit

Paper: P1A (paper1a_ech_nogo.tex) — ECH no-go.
Round: R57 hardened de-biased re-review. PDF: 29 pp, 0 undef, 0 overfull.
Vendors returned: OpenAI o3 (methodology), Gemini 2.5 Pro, Grok 4, Perplexity.
(Claude native-PDF leg failed over gracefully per cost-conservation mode.)
Independent severity assignment, no defaulting. Patterns 061–064 + calibration filter applied.

## SPECIAL-TASK FINDING — f_NL detectability range "2.6–5σ" (R56 lone OPEN MINOR)

VERDICT: **CLOSED-BY-SOURCING (real action).**

Resolution path: read P2's actual Fisher forecast
(`research/focused_paper_source_integration/02_full_draft.tex`). P2 L644 states
verbatim: *"We adopt the bispectrum-only 5.2–5.5σ optimistic and 2.6–5σ realistic
ranges as the headline forecast"* — recasting the Heinrich+2023
σ(f_NL^local)≈0.7 baseline for the matter-bounce template mismatch (r≈0.83–0.876),
reducing to 2.6–5σ after the systematic budget (template mismatch, ε-correction,
polynomial null-space scatter, photo-z, b_φ marginalization, GR projection).

So P2 **genuinely supports** the 2.6–5σ range; it is not a free-floating number.
The honest fix is to SOURCE it, not invent or soften. Edit made at the footnote
fn:spherex_range (arxiv/paper1a_ech_nogo.tex L2125) — now explicitly cites
`Golden2026P2`, states P2 adopts exactly these ranges as its headline forecast,
and clarifies that the in-text σ(f_NL)≈1.0 GR-marginalized value gives only the
≈4.4σ lower midpoint (resolving the apparent internal inconsistency the R56
finding flagged). Footnote citation changed `\cite{Heinrich:2023}` →
`\cite{Heinrich:2023,Golden2026P2}`. No fabricated numbers — P1A's range now
matches P2's verbatim. OpenAI o3 independently confirms (R57_P1A_OpenAI L132):
"SPHEREx 2.6–5σ consistent with body statements and carries disclaimer. OK."

## Other vendor findings — calibration / truth-audit verdicts

1. **σ from different null procedures juxtaposed without "not directly comparable"**
   (OpenAI MAJOR P1A-M3; Grok). VERDICT: **STALE.** Disclaimer already present at
   every flagged site — in-text L788 and BOTH figure captions (fig:naturalness
   L2196, fig:detection_forecast L2776: "σ values across panels use different null
   procedures; see text"), plus the full LiteBIRD null-hypothesis treatment L2993.
   Per-curve repetition beyond a caption pointer is OPINION-tier polish, not a
   PRD-bar defect.

2. **"in preparation / companion" sourcing of load-bearing numbers** (Grok
   BLOCKER; OpenAI). VERDICT: **OPINION (reject-framing) / known structural.**
   P2 and P1(b) are genuine sibling drafts; every companion reference is
   extensively caveated (handled across R52–R56: honorifics dropped, Table IV
   daggers, consolidation note). Legitimate companion-dependent paper, fully
   disclosed. Not a new actionable DO-NOW.

3. **Eq.(1) T² "on-shell shorthand"** (OpenAI). VERDICT: **STALE** — long-documented
   design choice, explicitly stated "not varied independently."

4. **H0 69.2 / 67.68 / 67.36 "inconsistency"** (OpenAI P1A-M9). VERDICT: **OPINION** —
   intentionally distinct sources (SH0ES-like local curve / companion MCMC / Planck
   reference) in a Hubble-tension comparison figure; standard practice, each labeled.

## Convergence

R52–R56 fixes verified intact (sign-consistency L1457, abstract cross-ref,
dimensional-completeness ΔN_Y, companion caveats) — none re-opened.
P1A f_NL item: **CLOSED.** No new VERIFIED DO-NOW survives the hardened filter.
P1A is **fully converged** for R57: zero genuine open findings remain.
