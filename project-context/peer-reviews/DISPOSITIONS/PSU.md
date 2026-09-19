# PSU disposition ledger — `paper-su`

**Canonical source:** `arxiv/paper_su_criterion/main.tex`
**Current paper-local version:** `v1S.0.9` (2026-09-18) — ledger reconciled this bundle after
sitting stale at v1S.0.2 for six versions (2026-09-18 process observation: this staleness is
exactly the class of gap that let the v1S.0.8 A2 closing-amendment land in Appendix A only,
undetected in Sec. III, for 11 days — see round `R3VERIFY` below).
**Exact PDF:** `arxiv/paper_su_criterion/main.pdf` == `site/public/papers/paper_su_criterion_v1S.0.9.pdf`,
sha256 `2b225d0b3ceaa42d9223cc5b54fb50e1c9a06875c8d6d1292610d85e00d94fb7`, md5 `fcc3383a…`, 7 pp.
(R1 artifact was `cc0dfb84…c48e` = v1S.0.1; R2 artifact `812dbaf1…aca31` = v1S.0.2; R3VERIFY
artifact reviewed was `9f1fc41c…443d` = v1S.0.8.)
**Venue:** Physical Review D — Letter / short note (length now 7 pp.; see N19, open).
**Claim policy:** S3 (failure vs. change-of-variable) is RESOLVED — the note is framed as an
exact, invertible change of variable, not a failure; this framing survived R1, R2, and
R3VERIFY unchallenged on the physics.

## Round history

| Round | Exact PDF sha256 | Legs | Outcome |
|---|---|---|---|
| `ROUND_2026-09-04-PSU-v1S.0.1-EXACTPDF-cc0dfb84-R1` | `cc0dfb84…c48e` | Claude Fable 5.1 INT (**major-revisions**), Grok API (**REJECT**), Gemini API (**MAJOR REVISIONS**); OpenAI/ChatGPT **ABSENT** (directive N pause) | 38 raw findings → **28 canonical**: 21 GENUINELY-NEW REAL, 0 re-flag, 5 FALSIFIED, 1 OPINION/GENRE, 1 OUT-OF-SCOPE-DISCLOSED. Clean-wave count **0**. Board: `../PSU_v1S.0.1_R1_BOARD_2026-09-04.md`; audit: `../INT_v3/PSU_v1S.0.1_R1_TRUTH_AUDIT_2026-09-04.md` |
| `ROUND_2026-09-04-PSU-v1S.0.2-EXACTPDF-812dbaf1-R2VERIFY` | `812dbaf1…aca31` | Claude Fable 5.1 INT (**major-revisions**, 6M/13m/4Q), Grok API (**REJECT**), Gemini API (**MAJOR REVISIONS**); OpenAI/ChatGPT **ABSENT** (directive N pause) | 39 raw findings → **32 canonical**: 20 GENUINELY-NEW REAL, 6 re-flag (4 still OPEN), 1 OUT-OF-SCOPE-DISCLOSED, 2 FALSIFIED, 3 OPINION. Clean-wave count **0**. Board: `../INT_v3/PSU_v1S.0.2_R2_BOARD_2026-09-04.md`; audit: `../INT_v3/PSU_v1S.0.2_R2_TRUTH_AUDIT_2026-09-04.md` |
| `ROUND_2026-09-18-PSU-v1S.0.8-EXACTPDF-9f1fc41c-R3VERIFY` (campaign lane L2; the R2-permitted verification round, unlocked by the intervening S7/S9/S9b/S9c/A2-adjudication science decisions) | `9f1fc41c…443d` | Claude Opus 5 INT (**MAJOR REVISIONS**, 2 ESSENTIAL/6 MAJOR/19 minor/7 nit), Grok API (**REJECT**), Gemini API (**MAJOR REVISIONS**); OpenAI/ChatGPT **ABSENT** (directive N pause) | Genuinely-new-real (all CLOSED in v1S.0.9): **PSU-9 (ESSENTIAL)** Sec. III printed the pre-A2-adjudication value `f^ρ_NL=-5/2` while Appendix A5 printed the corrected `-55/16` for the same quantity — the v1S.0.8 closing amendment landed in the Appendix only, never propagated to the main text; **PSU-10 (ESSENTIAL)** a raw UTF-8 `ρ` at `main.tex:514` threw `! LaTeX Error: Unicode character ρ not set up` and was silently dropped from the served PDF; **PSU-11 (MAJOR)** Appendix A5's closing-amendment paragraph narrated internal review/adjudication history ("reconciled by an independent adjudication…", "the earlier initial-label figure … came from composing … correcting the weight closes the gap") and used `λ'`, `A_2` without definition — a directive-G leak-gate violation; **PSU-12 (MAJOR)** footnote 1 miscounted `f_map^fin`'s contributions (listed the initial-label translation as a 5th contribution to `f_map^fin`, when it is the difference that distinguishes `f_map^init`); **PSU-13 (MINOR)** Reproducibility Statement omitted the two newest scripts (`psu_gates_S9_S10…`, `a2_lapse_monopole_adjudication…`) and their manifests. Re-flags (no action): future-date/version-string/AI-disclosure-genre items (= PSU-17/28, C27, C31); self-containedness/DOI complaints (= PSU-5/S4, PSU-16/S11, still OPEN, unchanged). **One item NOT closed, genuinely new, requires a science decision**: Gemini's pass-2 finding that the translation term's zero monopole (Appendix A3, `T(\eps,\mu)` "monopole 0 (all $\eps$)") was derived assuming $n_s=1$, which is not exact for general constant-$\eps$ backgrounds — if the exact $n_s(\eps)$-dependent trace is included, the composed `-5` may pick up an $\eps$-dependent correction. Claude's independent check confirms the five A2 contributions sum exactly to the printed Eq. (4) (a strong but not dispositive internal-consistency check — it does not independently re-derive the trace term). **Tracked as new open science gate S12** (below); not fabricated closed, not dismissed. Board/audit: `../INT_v3/PSU_v1S.0.8_R3VERIFY_claude_opus_2026-09-18.md`, `../R3VERIFY_PSU_Grok_brutal.md`, `../R3VERIFY_PSU_Gemini_cosmology.md`. |

## Canonical items (R1 board)

| ID | Class | Issue | Status | Verdict citation / closure |
|---|---|---|---|---|
| PSU-1 | REAL | Eq. (3) composition returns the **final**-position-label value ($-25/4+\tfrac{15}{4}\mu^2$) while Table I prints the **initial**-label $-5$; label never defined | OPEN | `threading_map_second_order_2026_09_04.md` §3 Totals + §4 Eq. (4). Gemini's proposed $f^{\rm in\text{-}in}=\lambda^2f_{\delta N}+\lambda f_{\rm map}$ **FALSIFIED** (fits only at $\eps=3/2$). → **S1** |
| PSU-2 | REAL | Fig. 1 caption "Both vanish at $w=-1$" — $\lambda(-1)=1$ | OPEN | Body (l. 135–137) is correct; caption (l. 141–142) is wrong. → **E1** |
| PSU-3 | REAL | Headline $8/3$ untraceable in-paper; monopole $-15/8$ never printed | OPEN | Factor correct (`separate_universe_failure_criterion…md` l. 179). Grok's "$16/7$" **FALSIFIED** (divided by $-35/16$, not the monopole). → **E3** |
| PSU-4 | REAL | Cai, Xue, Brandenberger & Zhang 2009 ($-35/8$) uncited and unreconciled | OPEN | `fnl_matter_contraction_adjudication_2026_09_02.md` l. 26/32/101 — Cai's $\times2$ located in their Eqs. 38–40 amplitude step; $-35/16$ matches Li+2016 Eq. 5.1. Dependence: with $-35/8$ the gap is $-5/8$, factor $8/7$. → **E4** |
| PSU-5 | REAL | Load-bearing derivations only in unpublished GitHub `.md` self-citations [18], [19] | OPEN | PRD standalone-reader failure. → **S4** |
| PSU-6 | REAL | Script name (§III) and manifest path (reproducibility statement) rendered into the PDF | OPEN | → **E2** |
| PSU-7 | REAL | Table I header says "in-in monopole"; the dust entry carries $\mu^2$ | OPEN | → **E3** |
| PSU-8 | REAL | $\delta N_c$ = separate-universe $\delta N$ asserted in one sentence; "initial-position label" undefined | OPEN | Derived in `threading_map…` §3 (`lab_init` row) and `separate_universe…` l. 133, but not in the paper. → **S1** + **S4** |
| PSU-9 | REAL | "Exact for any history" drops $-(1/a^2H)\nabla^2\zeta$; $\langle X\rangle_\zeta$ is $0/0$ on the attractor and ekpyrosis rows | OPEN | No initial-slice definition in either source note (checked). → **S2** |
| PSU-10 | REAL | "Failure" framing contradicts the source note's own conclusion | OPEN | `threading_map…` §4 l. 120–122. Directive R6. → **S3** |
| PSU-11 | REAL | NLO gradient-expansion literature missing from §IV | OPEN | Candidate refs arXiv:1004.1870, arXiv:1210.6525 — **unverified**, from reviewer memory. → **S5** |
| PSU-12 | FALSIFIED | "The criterion restates the known initial-data requirement" | CLOSED | §III states (i) and (ii) as logically distinct; Refs [3,4] carry no $\langle\eps/c_s^2\rangle_\zeta$ criterion. Residual novelty concern tracked at PSU-11. |
| PSU-13 | OOS-DISCLOSED | "USR uses $\eps\propto a^{-6}$, violating constant-$\eps$" | CLOSED | §V Limits discloses exactly this; the USR second-order statement is labelled structural. |
| PSU-14 | REAL | Fig. 1 two ordinates, no units/normalization stated | OPEN | → **E5** |
| PSU-15 | OPINION | "No new observable prediction; three validations are known results" | CLOSED | Validation tables reproduce known results by design; significance judgment. Root shared with PSU-10. |
| PSU-16 | REAL | No frozen DOI / archival release for the cited scripts | OPEN | → **E9** |
| PSU-17 | FALSIFIED | "Future date"; "no institutional address"; "self-citations post-date submission" | CLOSED | `\paperTimestamp` = today; `\email`, ORCID `\altaffiliation`, and affiliation all present in `main.tex`. |
| PSU-18 | FALSIFIED | "'Exact threading identity' not exact once $\eps=O(1)$" | CLOSED | Abstract already separates the linear (any history) and second-order (constant $\eps$, $c_s=1$) exactness claims. Real residual is PSU-9. |
| PSU-19 | FALSIFIED | "In-in monopole vanishing at $w=1$ is unsupported" | CLOSED (editorial residual **E6**) | General-$\eps$ monopole $-5(\eps-3)(\eps-6)/18$ vanishes at $\eps=3$; formula not printed in-paper. |
| PSU-20 | REAL | $\lambda_{\rm USR}$ assumes $\zeta\propto a^3$ from $\zeta=0$ at $a_s$ | OPEN | → **E7** |
| PSU-21 | REAL | Ekpyrosis row tests the definition, not the criterion | OPEN | → **E7** |
| PSU-22 | REAL | "Five geometric contributions" never listed | OPEN | They are `zlap`, `psi2`, `grad`, `wl_fin`, `lab_init` (`threading_map…` §3). → **E7** |
| PSU-23 | REAL | Reference style; [18]/[19] presented as citable works | OPEN | → **E8** |
| PSU-24 | REAL | AI-usage disclosure overclaims what the scripts verify | OPEN | → **E8** |
| PSU-25 | REAL | $\langle\eps\rangle_\zeta$ vs $\langle\eps/c_s^2\rangle_\zeta$; $\Theta$ undefined | OPEN | → **E8** |
| PSU-26 | REAL | Eq. (2) claimed "for any $c_s$" without naming the matter class ($P(X)$) | OPEN | → **E10** |
| PSU-27 | REAL | "USR agree to $O(\eps)$" reads as an NFS-constrained test | OPEN | → **E7** |
| PSU-28 | FALSIFIED | "Future-dated filenames and commit hashes" | CLOSED | Same root cause as PSU-17. |

## Open science gates

**S1** label-resolved composition (Fable) · **S2** $\langle X\rangle_\zeta$ normalization and the
dropped gradient term (Fable) · **S3** failure vs change-of-variable adjudication (Fable +
Houston) · **S4** self-containedness appendix (sonnet, gated on S1) · **S5** NLO
gradient-expansion literature verification (opus). Full specifications in the R1 truth audit.

**Directive R2**: no further review round on `paper-su` until S1 and S3 have produced a science
or scope decision.

## R2 canonical items (v1S.0.2)

Full table with citations and closure actions: `../INT_v3/PSU_v1S.0.2_R2_TRUTH_AUDIT_2026-09-04.md` §2.

- **C1–C20 — GENUINELY-NEW REAL, all OPEN.** Headline three: **C2** Eq. (4)'s second equality carries
  the wrong sign (`main.tex` l. 144–145; contradicts `psu_gates_S1_S2_2026_09_04.md` Eq. (S1.1) and
  the auditor's sympy); **C1** the abstract calls the separate-universe value $-5$ "the in-in
  monopole" (the in-in monopole is $-15/8$); **C4** the "$8/7$" robustness sentence (l. 88–90) is
  wrong — a uniform $\times2$ of the from-scratch shape gives monopole $-15/4$, gap $-5/4$, **ratio
  $4/3$**, and $-35/8$ is Cai's *isoceles* amplitude, not a monopole. Also C5/C7/C8 (reference layer:
  Li–Quintin–Wang–Cai 2017 uncited; refs [6]/[11]/[12] wrong; DPS "On separate universes"
  unengaged) and C9–C20 statement-precision items.
- **C21–C26 — re-flags.** C21 (standalone-reader / PSU-5 / gate S4), C22 (DOI / PSU-16),
  C23 ($\Theta$ / PSU-25), C24 (path breaks / PSU-6) remain **OPEN** — C23/C24 are regressions not
  fixed in v1S.0.2. C25 = PSU-15 (OPINION, closed). C26 = PSU-17/28 ("future dates", FALSIFIED).
- **C27 — OUT-OF-SCOPE:** `v1S.0.2` in the `\preprint` header, stripped at arXiv packaging.
- **C28, C29 — FALSIFIED (Grok).** C28: the composition $f^{\rm in\text{-}in}/\lambda+f^{\rm init}_{\rm map}$
  is identically $-5$ in $\mu$ and $\eps$; Grok used $f^{\rm init}_{\rm map}(\mu=0)=-5/8$ instead of the
  monopole $-5\eps/6$. C29: Eq. (2)'s domain qualifier is printed at l. 122–125.
- **C30–C32 — OPINION / genre.**

**Process finding (new, R2):** C4 originated in R1's own PSU-4 *disposition*, whose number was
transcribed into the manuscript unverified. Any number a disposition hands to a manuscript now gets
the same independent re-derivation gate as a number in the manuscript.

## Open science gates after R2

S4 (self-containedness appendix — now judged **required**, spec in the R2 audit §5(i) Appendix A),
**S6** identity-vs-fit verification + printed-Eq. (4) sympy assertion, **S7** Cai-2009 factor-2
reconciliation incl. Li+2017, **S8** numerical USR validation, **S9** uniform-$\phi$ vs uniform-$\rho$
final slice, **S10** general-history $f^{\rm init}_{\rm map}$, **S11** Zenodo DOI. S1/S2/S3 RESOLVED
(`research/theory_audit/psu_gates_S1_S2_2026_09_04.md`), S5 carried.

**Directive R2 (updated):** R1 + R2 exhaust the two-round convergence budget. After `v1S.0.3` lands
the editorial closures (audit §5(i) E-1…E-11), **review rounds on `paper-su` STOP** until a science
or venue decision is taken on S6–S10.

## Status after v1S.0.3–v1S.0.8 (science-only bundles, no review round) + R3VERIFY (2026-09-18)

S6 (identity-vs-fit), S7 (Cai-2009, `psu_gate_S7_cai_factor_2026_09_05.md`), S9/S10 (general
admixture + uniform-density slice, `psu_gates_S9_S10_2026_09_05.md`, then S9b/S9c follow-ups),
and the A2 lapse-monopole coefficient dispute (`a2_lapse_monopole_adjudication_2026_09_07.md`)
are all RESOLVED — this is the intervening science decision that unlocked the R3VERIFY round
under directive R2. S4 (self-containedness) remains **partially open**: R3VERIFY confirms the
Appendix A2/A3/A5 kernel listing is internally consistent (sums exactly to Eq. (4)) but Gemini's
MAJOR still holds that the ADM constraint *solve* itself (not just its listed results) is not
reproduced in-paper — tracked, not blocking. S8 (numerical USR validation) and S11 (Zenodo DOI)
remain OPEN, unchanged since R2 — carried, not blocking (venue/effort items, per directive R2's
"stop rounds when remaining findings are genre/length/venue").

**S12 (NEW, 2026-09-18, R3VERIFY) — translation-term monopole generality.** Gemini's pass-2
finding: Appendix A3's derivation that the translation term $T(\eps,\mu)$ has monopole $0$ for
all $\eps$ implicitly assumes $n_s=1$ (scale invariance) to drop a trace-part contribution
proportional to $n_s-1$; for a general constant-$\eps$ background $n_s\neq1$ except at specific
points ($\eps=3/2$, $\eps\to0$), so the exact monopole may carry an $\eps$-dependent correction
that (if present) would break the exact, $\eps$-independent $f_{\delta N}^{\rm init}\equiv-5$
result. Claude's independent check (same round) confirms the five A2 contributions sum exactly
to Eq. (4) and to monopole $-5\eps/6$, which is a strong internal-consistency check but does
**not** independently re-derive the trace-part computation Gemini is questioning. **Not closed,
not dismissed** — requires a from-scratch derivation of the translation term's trace part at
general (non-scale-invariant) $\eps$ before this can be dispositioned either way. This is now the
gating item for any further review round on `paper-su`.

**S12 — DISPOSITION (2026-09-19, campaign lane `bb-LS3-psu-s12`): CLOSED-WITH-CORRECTION.**
From-scratch exact-sympy derivation:
`research/theory_audit/psu_gate_S12_translation_trace_2026_09_19.{py,md,json}`; manifest
`reproducibility/manifests/experiments/psu-gate-s12-translation-trace.json` (local CPU, 27 s, \$0).
The script **solves** the linearised ADM Hamiltonian + momentum constraints for
$(\alpha_1,\psi_1)$ rather than assuming Maldacena's solution, integrates
$\xi^i=\int N^i\,dt$ along the fluid worldline, and builds the label-change kernel from $\xi$
alone — that kernel reproduces the committed `lab_init + wl_initextra` exactly. The full $s=0$
validation battery (per-piece $f$'s, $f^{\rm fin}_{\rm map}$, $f^{\rm init}_{\rm map}$, both
monopoles $-5\eps/6$, $T$, the composed $-5$, dust $-15/8$ / $25/8$ / $8/3$ /
$-25/4+\tfrac{15}{4}\mu^2$, the $\eps\to0$ USR row) passes **before** any general-tilt claim is
made, and a finite-$k_L$ numeric re-evaluation at $k_L/k_S=10^{-2..-4}$ confirms the series
extraction (errors falling as $(k_L/k_S)^2$).

**Gemini's premise is CORRECT; the printed Appendix A3 clause is wrong as written.** The trace
never vanishes — $\partial_i\xi^i=\eps\,\zeta_L$ exactly — and at general tilt
$T(\eps,\mu,n_s)=\frac{5\eps}{4(3-\eps)}\big[1-3\mu^2+(n_s-1)\mu^2\big]$, monopole
$\frac{5\eps(n_s-1)}{12(3-\eps)}\neq0$. A constant-$\eps$ background is not scale-invariant: the
growing branch these kernels correlate carries $n_s-1=2(2\eps-3)/(\eps-1)$ (equal to the
late-time dominant-mode index $3-2|1/(\eps-1)-1/2|$ exactly for $1<\eps<3$), vanishing at
$\eps=3/2$. Also established: $f^{\rm fin}_{\rm map}$ is tilt-**independent** (its kernel carries
no $1/k_L$ pole), so the entire tilt-sensitivity of the map is the translation term Gemini named.

**But the paper's result SURVIVES, unconditionally — and is stronger than stated.** Re-running
the committed general-$\eps$ in-in assembly with $P(k)=k^{n_s-4}$ (legitimate without touching
the vertices: those second-order kernels are bilinear in two linear modes whose $k$-dependent
amplitudes factor out, so the tilt enters only through the external power-spectrum weights; the
$s=0$ re-derivation reproduces $\frac{5}{12}(\eps^2\mu^2-\eps^2+6\eps-12)$ exactly) gives
$\delta f^{\rm in\text{-}in}=-\frac{5\eps}{12}(n_s-1)\mu^2$, and
$\delta f^{\rm in\text{-}in}/\lambda=-\delta T$ **term by term in $\mu$**. Hence
$f^{\rm init}_{\delta N}=f^{\rm in\text{-}in}/\lambda+f^{\rm init}_{\rm map}=-5$ exactly, for
every constant $\eps$ **and every $n_s$** — the residual vanishes identically *before*
$n_s(\eps)$ is substituted, so the verdict does not depend on the mode-function calculation.
Physically, the initial-position label is precisely the label in which the long mode's
Lagrangian displacement is undone. Every headline number is untouched ($\eps=3/2$ has $n_s=1$).

**Independent blind adjudication (one `fable` sub-agent, run once, not shown this lane's script
or conclusion): SAME verdict, same mechanism.** All seven expressions it reported are re-checked
symbolically in script §S9 and agree exactly. It additionally caught **two printed statements
this lane had not flagged**, both confirmed: (i) Appendix A2's "both with monopole $-5\eps/6$"
is $n_s=1$-specific — the initial-label map monopole is $\frac{5\eps(2\eps-7+n_s)}{12(3-\eps)}$,
while the final-label one is $-5\eps/6$ for any $n_s$; (ii) the printed $f^{\rm in\text{-}in}$
shape is the $n_s=1$ shape. It also noted, correctly, that $f^{\rm fin}_{\delta N}$ *is*
$n_s$-dependent, $\frac{5[\eps(n_s-4)\mu^2-3\eps+12]}{4(\eps-3)}$ — the expected asymmetry.

**Required manuscript changes — APPLIED 2026-09-19 (campaign lane `bb-L2b-psu-s12-apply`,
v1S.0.10):** Appendix A3's clause "the trace part vanishes at $n_s=1$" and the label "monopole
$0$ (all $\eps$)" replaced with the general-$n_s$ $T(\eps,\mu,n_s)$ and its correct monopole;
Appendix A2's "both with monopole $-5\eps/6$" corrected to state the final-label monopole holds
for any $n_s$ while the initial-label one is $n_s=1$-specific; the Appendix A4 in-in shape
labelled as the $n_s=1$ shape with the general-$n_s$ shape added; the $-5$ claim **strengthened**
to "for every constant $\eps$ and every spectral index" with the cancellation mechanism stated
inline; one optional sentence (P4) added to "What is new"; the Reproducibility Statement (P5)
now cites this note's script/json with real SHA-256 prefixes. Directive-G hygiene done in the
same bundle: version v1S.0.9→v1S.0.10, 4-pass recompile (0 undef refs, 0 raw Unicode, checked
before compiling), `/latex-audit` visual pass on all 7 rendered pages (PASS, no overflow), PDF
md5 `c6457c37f51a8ba0a92f57f1aed5d650` mirrored byte-identical to all served paths. No science
number changed; every sentence traces to this note's §"Printable" or the boxed results above —
`/never-fabricate-derivation` clean. See `project-context/SSOT/paper-su/status.md`
`## v1S.0.10 — S12 presentation fix + R4` for the full diff description.

**Gate status: S12 CLOSED, manuscript corrections APPLIED.** It is no longer the blocker on a
further review round; remaining `paper-su` open items are S4, S8, S11 and the venue/length
decision, all non-blocking.

**Directive R2 (updated 2026-09-19):** R3VERIFY was the one round the intervening S7–A2 science
decisions unlocked; it found and closed 2 ESSENTIAL + 3 MAJOR genuinely-new-real defects in
v1S.0.9 and surfaced S12. S12's resolution (2026-09-19, `bb-LS3-psu-s12`) plus its manuscript
application (this entry, `bb-L2b-psu-s12-apply`, v1S.0.10) is the intervening science decision
that re-opens the round budget: **R4, the one permitted verification board, is IN PROGRESS on
the exact v1S.0.10 PDF** (SHA-256 prefix `1015f442`,
`project-context/peer-reviews/INT_v3/ROUND_2026-09-19-PSU-v1S.0.10-EXACTPDF-1015f442-R4/`) — a
Claude-opus verdict-blind referee leg was dispatched; the Grok API + Gemini API legs via
`tools/v3_native_pdf_review.py` are blocked pending `bigbounce_preflight.py`'s clean-tree check
on `site/src/data/{live-status,papers}.ts`, which are mid-edit by concurrent campaign lanes in
this shared checkout (not a `paper-su`-specific problem). Whichever lane completes R4 must
truth-audit every finding against this file's fingerprints before closing; S8/S11/venue-length
remain carried, non-blocking open items.
