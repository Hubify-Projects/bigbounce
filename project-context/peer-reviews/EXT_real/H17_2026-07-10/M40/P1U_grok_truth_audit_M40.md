# P1U — M40 EXT Grok truth-audit (2026-07-13)

**Raw:** `EXT_real/H17_2026-07-10/M40/P1U_grok_M40.md` (read verbatim).
**Reviewer:** EXT Grok (headed browser).
**Verdict (raw L1):** MAJOR REVISIONS.
**Target:** P1U v1U.0.20, byte-unchanged (served md5 `c295beef`; no .tex edit since v1U.0.20).
**Provenance verified:** the raw reviews P1U's Four-Route No-Go content — Sec IV A–D (Routes 1–3 closures), App B/D regulated NJL gap-equation, Sec X Holst perturbation-transparency, Fierz-by-Fierz projection lemma (App C), F1–F2 symmetry-counting, N_tot≈92 vs matter-bounce f_NL=−35/16 tension. This is unambiguously P1U. (The M40 raw initially tripped the signature gate as a FALSE POSITIVE; corrected by the count-based dominance fix, commit b35f43c4 — the misfile detector now agrees this is P1U.)
**Band context:** Grok MINOR (M35, 0M/4m) → **MAJOR (M40, 3M/3m)** on IDENTICAL byte-unchanged content = pattern-066 verdict-word variance (the documented Grok MINOR↔MAJOR band swing: M18→M21, M16, M30, M35→M40). NOT new findings.

## ledger_match DRAFT
`tools/ledger_match.py` → 4/7 auto-MATCHED, 3 UNMATCHED (Opus-adjudicated below). Finding #1 is a `REVISIONS (2) ISSUES:` scaffold header — non-finding, not counted.

## Per-finding disposition (all source-cited standing DP1U D-ids)

| # | sev | finding | disposition |
|---|-----|---------|-------------|
| 1 | — | `REVISIONS (2) ISSUES:` | scaffold header, non-finding |
| 2 | MAJOR | Sec I/IV/IX excessively long (~62pp), repetitive defensive scope language; streamline / move scope paragraphs + completeness lemmas + MCMC to appendices | **DP1U-22** (length / repetitiveness / "should be a Letter", BACKFIRE-PATTERN-066). Pure venue/style OPINION; multiple prior reviewers echo. Not an editable error. |
| 3 | MAJOR | R1–R3 amplitude-suppression rest on OOM estimates / phenomenological ansätze (D_inf (T_reh/M_GUT)^{3/2}) / one-loop coefficients not derived from minimal ECH action; NJL gap-equation exclusion must be reproduced in main text with full algebra | **DP1U-10** (Route-3 β-function / amplitude-budget conditional, SCOPE) + **DP1U-09** (Route-2 ansatz-vs-derivation) + **DP1U-05/-19** (NJL regulated gap-eq = CLOSED-BY-COMPUTE v1U.0.14, App `app:njl_gap` + `njl_gap_equation_route1.py`; the derivation the reviewer asks for already exists in-appendix). Placement-in-main-text = presentation nit, not new. |
| 4 | MAJOR | Sec X perturbation-transparency proof only sketched; full scalar-decoupling + tensor + perturbed-tetrad term-by-term EoM must be supplied | **DP1U-12** (transparency / B8-subsumption; standard on-shell scalar equivalence, narrow "solid positive core" for canonical scalar matter, explicitly excluding fermions/torsion/dynamical-γ, Claude verified-correct). "Only sketched" = referee-preference depth, disclosed scope. Not new. |
| 5 | MINOR | N_tot≈92 dark-energy route vs matter-bounce f_NL tension = bookkeeping that relocates CC; state quantitatively/conditionally | **DP1U-17** (f_NL=−35/16 self-containedness, P2-companion resolved) + **DP1U-14** (N_tot≈92 ansatz / matter-bounce erasure, disclosed bookkeeping). Grok itself concedes the tension is "correctly identified as mutually exclusive." Not new. |
| 6 | MINOR | "basis-complete at M_Pl-power-counting level" central to novelty; Fierz-by-Fierz projection lemma (App C) + F1–F2 symmetry-counting must be summarized quantitatively in intro/early Sec IV | **DP1U-07** (O1–O6 basis completeness / F1 / F2 / Fierz projection) + **DP1U-20** (operator-vs-channel completeness OPEN-VENUE). F1–F2 + the completeness lemma are already in-body (added v107, L295/L306-adjacent; the fully-explicit Fierz-by-Fierz lemma disclosed "left to follow-up"). Summarize-in-intro = placement nit, not new. |
| 7 | MINOR | Observational elements (galaxy-spin null, NaMaster EB, spectator-ALP MCMC) + companion-sibling numbers included while claiming theoretical self-containment; remove/reduce to citations, stand alone as theory paper | **DP1U-06** (channel-vs-operator + self-containment framing) + **DP1U-15** (App E–H don't test ECH, disclosed) + **DP1U-16** (companion-reliance / self-containedness, disclosed reproducible-now via `\cite{BigBounceRepro}`). Not new. |

## Verdict
**0 genuinely-new findings.** Every finding fingerprint-matches a standing DP1U disposition. This is the documented Grok MINOR→MAJOR band swing (pattern-066) on byte-unchanged v1U.0.20 — a maximal-harsh-referee re-flag wave, not a content regression.

## Integrity
No faked accept. No un-sourced dismissal. No fabrication. Raw read verbatim before any verdict. No .tex edit due (byte-unchanged, all re-flags / presentation nits / disclosed-scope); no bump; `directive_g.sh` NOT run.

## Bookkeeping
- **clean-wave streak:** 15 → **16** (directive-K; M37 completed the M35 wave at 15; this M40 Grok read is P1U's next clean wave).
- **cap:** Grok leg MINOR (M35, 12) → **MAJOR (M40, 6)** — contribution drops 12→6; `post_verdict.sh` recomputes cap = 50 + latest-per-reviewer {Grok MAJOR 6 + ChatGPT REJECT 0 + Gemini MAJOR 6} = **62**. Honest per the EXT formula.
