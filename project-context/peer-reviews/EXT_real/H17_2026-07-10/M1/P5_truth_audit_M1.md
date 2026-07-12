# P5 M1-wave truth audit (v0.1.124, 2026-07-12)

Reviewed version: v0.1.124 (directive-M presentation completion: 352→41-line
PRD abstract, reader's-guide + co-review-request removed, commit 06451a93).
Auditor stance: strict, skeptical, journal-referee-grade, verdict-first,
source-cited. Not told a convergence conclusion.

Raws: `M1/P5_grok_M1.md` (Grok = **MAJOR REVISIONS**), `M1/P5_chatgpt_M1.md`
(ChatGPT = **REJECT**). Ledger match: Grok 5/6, ChatGPT 10/12.

---

## HEADLINE — the Grok-slip diagnosis (LOAD-BEARING)

**Verdict: (a) REACTION TO THE DIRECTIVE-M OVERHAUL, NOT pattern-066 oscillation.**
Grok slipped ACCEPT (H17F-final, RS2) → **MAJOR REVISIONS** on M1 because the
v0.1.124 abstract rewrite **INTRODUCED a genuinely-new self-contradiction** that
Grok correctly caught as its MAJOR #1. This is a real overhaul-caused regression,
not a reviewer flipping severity on unchanged content.

**Grok M1 MAJOR #1 (verbatim, raw l.5):**
> "The abstract calls the DESIVAST void-vs-non-void contrast \"the primary,
> pre-declared estimand,\" yet §V.B explicitly states that the DESIVAST path was
> designated post-hoc as the \"exploratory primary\" because \"no timestamped
> analysis plan predates the data\" ... This direct contradiction on analysis
> status undermines the headline claim and requires immediate correction (remove
> \"pre-declared\" or supply timestamped plan evidence)."

**ChatGPT M1 independently caught the same defect (verbatim, raw l.5):**
> "The abstract calls the footprint-restricted contrast \"pre-declared,\" whereas
> §V B explicitly states that no timestamped plan preceded inspection of the data
> and that the primary path was selected post hoc."

**Git proof the "pre-declared" word is overhaul-introduced (not standing):**
- `git log -S"pre-declared estimand"` returns EXACTLY ONE commit: **06451a93
  (v0.1.124, the directive-M overhaul).** The phrase did not exist before.
- Pre-overhaul abstract (v0.1.123, `git show 5939c1c1`) read: **"the primary
  estimand is the footprint-restricted DESIVAST..."** — NO "pre-declared"
  qualifier.
- Current tex (v0.1.124) l.778: **"The primary, pre-declared estimand is the
  footprint-restricted..."** — the overhaul inserted "pre-declared".
- §V.B still says the opposite in multiple places: l.1377 "made post-hoc, and we
  declare it"; l.1392-1393 "\emph{designated primary for reporting} (equivalently
  the \emph{exploratory primary}, since no timestamped analysis plan predates";
  l.1508 "the primary estimand was designated post-hoc"; l.4444 "\emph{designated
  primary for reporting} (exploratory/post-hoc: no ...)".

So the abstract-shortening pass over-tightened "the primary estimand" into "the
primary, **pre-declared** estimand" — a one-word claim that flatly contradicts the
body's honest post-hoc disclosure. Both external referees flagged it in the SAME
wave. This is the diagnostic signature of an overhaul reaction, not oscillation:
the flagged token is new to v0.1.124, and it inverts a load-bearing honesty
statement.

Distinguish from the standing re-flag DP5-13: DP5-13 disclosures ("post-hoc,
exploratory, garden-of-forking-paths") remain correct in §V.B. The DEFECT is that
the new abstract word "pre-declared" now **conflicts** with DP5-13's disclosure —
that conflict is the genuinely-new part.

---

## GENUINELY-NEW REAL FINDING (count = 1)

### GN-M1-01: Abstract "pre-declared" contradicts §V.B "post-hoc/exploratory" — overhaul-introduced
- **verdict: GENUINELY-NEW-REAL (editable, one-word fix for v0.1.125).**
- Caught independently by Grok M1 MAJOR #1 and ChatGPT M1 MAJOR #1.
- **Abstract tex line: 778** — `The primary, pre-declared estimand is the
  footprint-restricted` → the word "pre-declared" is false.
- **§V.B tex lines that contradict it:** 1377, 1392-1393, 1508, 4444 (all say
  post-hoc / exploratory / "no timestamped analysis plan predates the data").
- **Provenance:** introduced by overhaul commit 06451a93 (v0.1.124); absent in
  v0.1.123 (5939c1c1). Confirmed by `git log -S` returning only 06451a93.
- **Fix (v0.1.125):** delete "pre-declared" (revert l.778 to "The primary
  estimand is the footprint-restricted") OR replace with "designated-primary
  (exploratory)" to match §V.B. One-word / few-word edit; no number changes; no
  new computation. This restores the abstract↔§V.B consistency and directly
  answers both referees' MAJOR #1.

---

## Overhaul-regression ref/label hunt — CLEAN
- `.log` scan: no `Reference ... undefined`, no `Citation ... undefined`, no
  "multiply defined" (only a benign `OMS/cmtt/m/n` font-shape warning).
- Every `\ref/\eqref/\autoref` target still has a `\label` in the current tex
  (0 orphans).
- No `\label` deleted by the overhaul is still referenced (441-deletion diff is
  ref-clean).
- Conclusion: the ONLY overhaul-introduced defect is the "pre-declared" wording
  (GN-M1-01); the abstract collapse did not orphan any cross-reference.

---

## Grok M1 findings — dispositions

| # | Sev | Verdict | Maps to |
|---|-----|---------|---------|
| 1 | MAJOR | **GENUINELY-NEW-REAL** | GN-M1-01 (abstract "pre-declared" vs §V.B post-hoc) |
| 2 | MAJOR | RE-FLAG-DISCLOSED | **DP5-21** — Paper-IV dependency (class_eq labels, monopole −0.0026, GZ1 69.91%/κ=0.40 not independently verifiable without companion). §I "Independence from Paper IV" + §XIII + App A + DAS disclose; OPEN-VENUE, Houston-gated. |
| 3 | MAJOR | RE-FLAG-DISCLOSED | **DP5-11 (+DP5-10)** — ≈0.9pp quadrature envelope not a unified end-to-end MC/covariance. §VIII term list + √0.898 disclosed; "informed estimate" is the paper's OWN framing; unified MC = statistical-philosophy OPINION / OPEN-COMPUTE (DP5-10). |
| 4 | MINOR | RE-FLAG-DISCLOSED | **DP5-14 (+DP5-10)** — T-Web n=428 void bin underpowered/shell-contaminated + 2.1σ bright/dark sign-flip lacks DR2 injection-recovery mock. T-Web explicitly secondary/diagnostic; the underpower + sign-flip are the paper's own §VI D demotion disclosures; injection mock = disclosed DR2 item. |
| 5 | MINOR | RE-FLAG-DISCLOSED | **DP5-22 (+DP5-21)** — "invokes unprovided artifacts [A1]-[A34], companion repo; needs self-contained methods supplement." Reproducibility/artifact-DOI presentation, DAS added v0.1.114 (DP5-18) + Paper-IV coordination (DP5-21); D-round/venue class. |

Grok ledger-match: 5/6. The 1 unmatched = MAJOR #1 (the genuinely-new
"pre-declared" contradiction), correctly NOT in the ledger because it is new to
v0.1.124. Grok's one-sentence (raw l.11) concedes the central claim "is supported
... once the post-hoc designation contradiction and systematic-envelope
validation are resolved" — i.e. the null itself stands; MAJOR #1 is the editable
blocker.

---

## ChatGPT M1 findings — dispositions

ChatGPT = REJECT (10 MAJOR + 2 MINOR) — the documented maximal-harsh structural
floor (patterns 061-066; REJECT on unchanged honestly-scoped content across
RS1b/W2/W3/H17H). All source-cited re-flags EXCEPT the shared "pre-declared"
half of MAJOR #1 (which corroborates GN-M1-01).

| # | Sev | Verdict | Maps to |
|---|-----|---------|---------|
| 1 | MAJOR | RE-FLAG (post-hoc half **corroborates GN-M1-01**); Bonferroni-family half → **DP5-04/-13** | "pre-declared vs post hoc" = GN-M1-01. "Bonferroni-5 uses k=20 approx not exact footprint-restricted row" → DP5-04: the consolidated `tab:bonferroni5_family` (l.3454) lists per-row parents incl. the exact footprint row; family-wise coverage disclosed as exploratory (DP5-13). |
| 2 | MAJOR | RE-FLAG-DISCLOSED | **DP5-06** — non-void control is geometric footprint union, not BGS completeness mask/randoms/IPW. §VIII B "Footprint ≠ selection function" (l.3033), residual folded into `tab:systematic_budget` (l.3160). |
| 3 | MAJOR | RE-FLAG-DISCLOSED | **DP5-10** — binomial-independence SEs ignore void-level spatial covariance; cluster/void bootstrap needed. CI labeled "counting-statistics-only" (§VIII); OPEN-COMPUTE. |
| 4 | MAJOR | RE-FLAG-DISCLOSED | **DP5-11** — ≈0.9pp envelope mixes correlated terms in quadrature; < 1.1pp simultaneous bound. Term list + √0.898 + "approximately independent / peak-excursion" disclosed §VIII; statistical-philosophy OPINION. |
| 5 | MAJOR | RE-FLAG-DISCLOSED | **DP5-08 + DP5-09** — 2a−1 → 2.26pp conversion assumes symmetric non-differential errors; void arm ±3.7pp. Void-stratified matrix computed (v0.1.118, artifact `gz1_stratified_confusion.json`); ±3.7pp under-powered → corroborates-but-cannot-exclude; de-attenuation caveat STAYS. |
| 6 | MAJOR | RE-FLAG-DISCLOSED | **DP5-04 + DP5-16** — five void definitions not a common parameter; sphere-PIS author-constructed vs GALZONE native; REVOLVER/VIDE pruning variants. `tab:desivast_three_algo` caption (l.3310) + DP5-15 already state this. |
| 7 | MAJOR | RE-FLAG-DISCLOSED | **DP5-12** — 0.024pp RSD bound: displacing galaxies+holes with fixed void topology ≠ re-running VoidFinder on reconstructed field. First-order Zel'dovich CLOSURE (v0.1.122/123, artifact `27_rsd_void_recon_bound.json`); the no-full-nonlinear-catalog-re-derivation is the paper's OWN disclosed residual (tex l.847-850). |
| 8 | MAJOR | RE-FLAG-DISCLOSED | **DP5-14** — T-Web dominated by selection (23× void-fraction, 26.6% same-class); use randoms-weighted baseline or remove. Paper's OWN randoms-weighted disclosure; T-Web secondary/diagnostic. |
| 9 | MAJOR | RE-FLAG-DISCLOSED | **DP5-20** — bounce/inflation implication not derived; App B noncovariant toy operator. Labeled "speculative ... not a derived constraint," relegated App B + Conclusions. |
| 10 | MAJOR | RE-FLAG-DISCLOSED | **DP5-21** — CW/CCW labels from concurrent unreviewed Paper IV, placeholder arXiv/DOI; conditional on co-review. OPEN-VENUE, Houston-gated. |
| 11 | MINOR | RE-FLAG-DISCLOSED | **DP5-15** — external checks (Tempel multiplicity, ASTRA) overstated as cosmic-web validation. Labeled descriptive/supporting, not load-bearing (`tab:analysis_tree`). |
| 12 | MINOR | RE-FLAG (**overhaul-ack**) | **DP5-22 (+ corroborates GN-M1-01 label-inconsistency)** — "excessively repetitive ... inconsistent labels 'primary,' 'headline,' 'pre-declared,' 'designated primary,' 'exploratory primary'." Editorial-length/label-consistency D-round; the SPECIFIC "pre-declared vs post-hoc" instance is the editable GN-M1-01 fix. |

ChatGPT ledger-match: 10/12. The 2 "unmatched" resolve to the GN-M1-01 shared
contradiction (MAJOR #1) and the DP5-22 label-consistency MINOR #12 — both point
at the same overhaul-introduced "pre-declared" defect.

---

## FINAL COUNT

**Genuinely-new real editable findings: 1** — GN-M1-01 (abstract l.778
"pre-declared" contradicts §V.B post-hoc, lines 1377/1392-1393/1508/4444).
Overhaul-introduced (commit 06451a93; git-`-S` confirms). One-word v0.1.125 fix.

All other Grok(4) + ChatGPT(11) substantive findings = source-cited re-flags of
disclosed/dispositioned content (DP5-04/-06/-08/-09/-10/-11/-12/-13/-14/-15/-16/
-20/-21/-22). No new ref/label breakage from the overhaul.

## Streak
DP5-22 (RS2b) held streak at 3. GN-M1-01 is a genuinely-new editable defect in
the new v0.1.124 content → **streak RESETS to 0** (directive-K). Re-tests after
the v0.1.125 one-word fix.

## Integrity
Both external verdicts read verbatim before any disposition (Grok MAJOR REVISIONS
raw l.1; ChatGPT REJECT raw l.1). No ACCEPT faked. Every disposition source-cites
a tex line / artifact / prior DP-id. No dismissal without a source-cited verdict.
No math fabricated. The Grok ACCEPT→MAJOR slip is diagnosed as an
overhaul-reaction (git-verified new token) and recorded honestly — NOT laundered
as oscillation.
