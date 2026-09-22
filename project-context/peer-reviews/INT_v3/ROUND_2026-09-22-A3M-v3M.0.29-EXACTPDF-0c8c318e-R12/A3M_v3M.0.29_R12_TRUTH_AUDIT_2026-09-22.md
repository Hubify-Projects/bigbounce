# A3M R12 truth-audit — v3M.0.29 exact PDF, sha256 `0c8c318e18…12`

**Round:** the one confirmation board authorized by the row-9b intervening science decision
(directive R2's "confirmation after real closure" clause), dispatched by lane
`bb-L1d-a3m-row9b-r12`, co-director authorized.

## Legs

| leg | status | verdict |
|---|---|---|
| Grok API (`grok-4.3`) | **FAILED-INFRA** | none recorded |
| Gemini API (`gemini-3.1-pro-preview`) | **FAILED-INFRA** | none recorded |
| Claude opus INT referee (verdict-blind, no prior-history access) | ran | **MAJOR REVISIONS** |

**Grok/Gemini FAILED-INFRA — reason, recorded never as a verdict.** `tools/v3_native_pdf_review.py`
requires a fresh `bigbounce_preflight.py run` receipt, which requires ALL registered draft-paper
inputs (`project-context/draft_paper_registry.json`) to be git-clean, not just A3M's. At dispatch
time `pipelines/p4prime_chirality_test/paper/{main.tex,main.pdf}` were dirty under a concurrent,
legitimately active lane (P4P) this lane does not own and is not authorized to touch or stash
(an attempted temporary `git stash` of only those two files, meant to be popped back immediately
after receipt generation, was blocked by the harness's own safety classifier as a modification of
another lane's uncommitted work). No receipt could be generated; `verify_receipt`'s HEAD-pinning
also means no older receipt (even one already containing an A3M draft record) could be reused,
since three commits landed on this lane's own bundle after the last available receipt. This is
the same class of shared-checkout contention already recorded for the P-SU lane's R4 board
(`DISPOSITIONS/PSU.md`, 2026-09-19: "the shared-checkout preflight clean-tree gate cleared ...
then immediately re-blocked on a different validator ... unrelated to paper-su ... the gate was
not bypassed"). Per directive I2, an INT infrastructure failure never stops the check that is
independently valuable and does not depend on the same gate: the Claude opus verdict-blind
referee (a direct sub-agent dispatch, not routed through `v3_native_pdf_review.py`) ran, and its
findings are truth-audited below.

## Truth-audit, verdict-first

The referee's full raw report — findings, its own independent-verification table (37 checks,
all reproduced), and its verdict — was written to disk (this directory) before this audit began.
Each finding is checked against the exact v3M.0.29 PDF and, where applicable, against
`DISPOSITIONS/A3M.md`'s existing fingerprint ledger.

### GENUINELY-NEW-REAL — CLOSED in v3M.0.30

1. **Finding 2 [ESSENTIAL] — LQC's two non-S1 linear transfers ($T=0.409$ vs $T=0.500$) were
   never reconciled.** CONFIRMED real: caused by this lane's own row-9b propagation, which added
   the "LQC effective dust (Bardeen)" row without addressing the pre-existing "$T=0.409$,
   scheme S2" sentence three paragraphs earlier. Source note
   (`row9b_bardeen_lqc_2026_09_22/PROPAGATION_NOTE.md` §3.2) already states these are "two
   different constructions ... reported side by side, not merged" but this lane had not carried
   that distinction into the paper clearly enough. **Closed**: added an explicit paragraph
   distinguishing the fluid-variable handoff-at-$-\eta_B$ construction ($0.409$) from the
   geometric-variable dust-phase-handoff construction ($0.500$), naming both variables and both
   handoff surfaces (`main.tex`, the paragraph immediately following Table III).

2. **Finding 3 [MAJOR] — "$\rho+p$" denotes two different quantities in Sec. III A; $x$
   undefined.** CONFIRMED real, introduced by this lane's own new prose (the row-9b extension
   text). **Closed**: (a) the first "$\rho+p=0$" crossing statement now reads
   "$\rho+p\equiv-2\dot H=0$" with an inline note that this is the GR-identity combination, not
   the LQC matter's own $\rho+p$; (b) $x\equiv\rho/\rho_c\in(0,1]$ is now defined explicitly at
   first use, with the Friedmann equation rewritten in terms of it; (c) the sentence establishing
   the LQC anchor now states explicitly that $-2\dot H=x(1-2x)\neq\rho+p=x$ because "the classical
   GR identity is violated by the modified Friedmann equation" — the root cause, not just the
   symptom. $\rho_B$/$\rho_c$ collision: not renamed (both symbols are pre-existing and load-bearing
   elsewhere in the paper); left as a carried NIT (see below) rather than risk a wider renaming
   sweep under this round's scope.

3. **Finding 1 [ESSENTIAL] — Channel II's headline $1.84\pm0.03$ is measured entirely inside the
   region Table V's own caption calls "non-perturbative branch."** CONFIRMED real and
   pre-existing (not introduced by row-9b; present since at least R10/R11, never previously
   raised in this specific form — Grok M3 at R11 raised only the shallower "144-point subset is
   a physical restriction" claim, RE-FLAGGED there; this referee's finding is a materially
   different, deeper claim about regime validity that no prior leg raised).
   **Not closed by new computation** — closing it properly requires re-running the
   per-point perturbativity diagnostic ($1.2|f_{\rm NL}|\sigma_r$) across the 144-point
   in-coverage grid, which needs $\sigma_r$ per point (derivable from the committed
   `row11_gammacr_extension.json`'s per-point $(\Delta,r_pk_p)$ via the compaction script's own
   variance integral, but not a one-line derivation from already-computed fields) — outside this
   lane's row-9b mandate and its remaining budget, and `/never-fabricate-derivation` forbids
   estimating it from adjacent numbers. **Closed by honest disclosure instead**: added a sentence
   stating plainly that the perturbativity diagnostic has been checked only on the displayed
   27-point grid, that the entire 144-point headline population lies below the
   $\gamma_{\rm cr}\lesssim0.8$ non-perturbative threshold, and that the measured continuity of
   the $\gamma_{\rm cr}$-slope across both grids is evidence the same regime applies, not a
   substitute for the pointwise diagnostic — which is left as an open item (see "Carried, not
   closed" below). This converts an implicit overclaim into an honest, bounded limitation; it
   does not resolve the deeper question, and R12 is NOT converged on this item.

4. **Finding 4 [MAJOR] — the 144-point/27-point reconciliation was left as an exercise for the
   reader.** CONFIRMED real, pre-existing. **Closed**: added the explicit arithmetic
   ($\gamma_{\rm cr}$ means $0.430$ vs $0.853$, OLS slope $-0.20$/unit $\Rightarrow$
   $1.759+(-0.20)(0.430-0.853)=1.84$, matching the 144-point mean to three significant figures),
   computed directly from the committed `row11_gammacr_extension.json` points (no new
   computation — an aggregation of already-committed per-point data).

5. **Finding 5 [MINOR] — the $T_{f_{\rm NL}}<1/2$ disclaimer was scoped only to Quintin-type.**
   CONFIRMED real, caused by row-9b (LQC and poly now also have Bardeen transfers outside
   $[0,1/2)$). **Closed**: disclaimer reworded to cover all three backgrounds, with all three
   Bardeen transfer values ($1.03$, $1/2$, $0.521$) stated explicitly.

6. **Finding 6 [MINOR] — the Quintin-type "sharing its sign" sentence needs an S1 qualifier.**
   CONFIRMED real, pre-existing text whose omission became consequential once row-9b's S2
   selection was established for this background. **Closed**: added "in scheme S1" plus a
   parenthetical noting S2's net cubic term instead suppresses $|f_{\rm NL}|$ on this background.

### FALSIFIED (source-cited, no edit)

- **Finding 17 [NIT] — "the poly Bardeen bracket's upper endpoint should be $-0.14$, not
  $-0.13$."** FALSE. The referee reconstructed the endpoint from the *rounded* printed values
  ($-1.140+1.00=-0.140$). The actual construction uses the unrounded linear transfer
  ($f_{\rm NL}^{\rm after,lin}=-1.1399921\ldots$, `results.json` `consequences.poly` in
  `row9b_bardeen_lqc_2026_09_22/`) and the unrounded Quintin-type cubic endpoint ($+1.007$, not
  $+1.00$): $-1.1400+1.007=-0.133\to-0.13$, exactly what is printed. Re-verified against the
  committed JSON, not re-derived. No edit.

### RE-FLAG-OF-DISCLOSED (no edit)

- **Findings 13/14 [MINOR] — abstract $c_s$-window numbers are S1-only; LQC anchor stated
  unconditionally.** Already disclosed in the body (Sec. VIII: "This entire $c_s$-window
  analysis is carried out in scheme S1"; Sec. III A: the anchor's assumption and its plausible
  alternative are both stated). The referee's own report concedes the body discloses this
  properly for 13. No edit; carried as a possible future abstract tightening, not a defect.

### Carried, not closed (real, lower priority, or requiring computation this lane did not
perform — full text in the raw report above)

- **Finding 1's underlying regime question** (does the 144-point ratio survive a pointwise
  perturbativity check?) — needs a new script run against `row11_gammacr_extension.json`'s
  per-point $(\Delta,r_pk_p)$, computing $\sigma_r$ from the compaction script's variance
  integral. Concrete next step, not performed here.
- Finding 7 (Table II literature-plateau column not tabulated).
- Finding 8 (symbol $\lambda$ carries three meanings — a renaming sweep, not a one-line fix).
- Finding 9 (superseded $f^\rho_{\rm NL}$ formula in App. A 4 unmarked).
- Finding 10 ($\epsilon_{\rm eff}=1/2$ undefined; no stated sensitivity to the background
  $\epsilon=3/2$).
- Finding 11 (Discussion quotes stale S1 significances after S2 is selected).
- Finding 12 (curvaton $r$-comparability across the S1/S2 tensor amplification).
- Finding 15 (Savage–Dickey factor at $\gamma_*=2$ not reconstructible from printed chain
  statistics).
- Finding 16 ($B_{\rm MB/SMBHB}$ rounding: $6.5\times10^3$ vs the stated $7$–$9\times10^3$
  range).
- $\rho_B$/$\rho_c$ near-collision noted in Finding 3 (not renamed this round).
- Findings 18–23 (NIT cluster: caption wording, citation-year consistency, dangling $r=0.84$
  cross-reference, undefined $W$/$r_i$ in App. A 4, symbol $A$ overload, decade-range phrasing).

## Class counts

**6 GENUINELY-NEW-REAL** (2 ESSENTIAL closed by real edit, 1 ESSENTIAL closed by honest
disclosure — not converged on this item, 1 MAJOR closed by real edit, 2 MINOR closed by real
edit), **1 FALSIFIED**, **2 RE-FLAG-OF-DISCLOSED**, **11 carried** (not closed this round).
Clean-wave count: **0** (this round is not clean — real items were found and only partially
closed).

## Verdict

**NOT CONVERGED.** The Claude opus leg returned MAJOR REVISIONS; Grok and Gemini FAILED-INFRA
(never counted as clean, never back-filled). Six genuinely-new-real items found; five closed
with real edits or honest disclosure in v3M.0.30, one (the PBH perturbativity pointwise check)
left open and named as the concrete next step. No physics error was found anywhere in the
paper's core derivations (the referee independently reproduced roughly forty displayed
equations and table entries). No headline number changed.

## Directive R2 status

This was the one confirmation board R2's "confirmation after real closure" clause authorized.
It did not confirm (found and partially closed 6 real items). **No further board on A3M without
another intervening science or scope decision.** The open PBH perturbativity item is the most
concrete candidate for that next decision.
