# PSU disposition ledger — `paper-su`

**Canonical source:** `arxiv/paper_su_criterion/main.tex`
**Current paper-local version:** `v1S.0.12` (2026-09-19) — R4COMPLETE closure (campaign lane
`bb-L2c-psu-r4-complete`); see the `R4COMPLETE` entry below for the full diff.
**Exact PDF:** `arxiv/paper_su_criterion/main.pdf` == `site/public/papers/paper_su_criterion_v1S.0.12.pdf`,
sha256 `d400dec4a70d5167b8ddbc0f2acef4185d3cdb08077f550601f25add8a730ac5`, md5
`7bae5b35c4ee1456557a8c74f57a3692`, 8 pp.
(R1 artifact was `cc0dfb84…c48e` = v1S.0.1; R2 artifact `812dbaf1…aca31` = v1S.0.2; R3VERIFY
artifact reviewed was `9f1fc41c…443d` = v1S.0.8; R4's Claude-opus leg reviewed `1015f442…` =
v1S.0.10; R4's Grok/Gemini legs reviewed `0fc47bd5…291563` = v1S.0.11 — see R4COMPLETE.)
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
| `ROUND_2026-09-19-PSU-v1S.0.10-EXACTPDF-1015f442-R4` + `R4COMPLETE` (campaign lanes L2b then L2c; the one R2-permitted board unlocked by S12's resolution; Claude-opus leg on v1S.0.10, Grok/Gemini legs on v1S.0.11 — different exact PDFs, recorded separately) | opus: `1015f442…`; Grok/Gemini: `0fc47bd5…291563` | Claude Opus 5 INT (**MAJOR REVISIONS**, v1S.0.10), Grok API (**REJECT**, v1S.0.11), Gemini API (**MAJOR REVISIONS**, v1S.0.11); OpenAI/ChatGPT **ABSENT** (directive N pause) | Genuinely-new-real, all CLOSED: opus leg closed in v1S.0.11 (Sec. II/abstract/Fig. 1 internal-consistency gap from the S12 fix, 2 wording slips); Grok/Gemini legs closed in v1S.0.12 (S14's Cai citation, 3× App.~A2→A3 cross-refs, Fig. 1 caption dual-axis clarity, Table I USR citation) — full detail in the `R4COMPLETE` narrative entry below. New gates opened by the opus leg: S13, S15 (both require a real derivation, carried OPEN); S16 (cosmetic, carried). Re-flags: S4, S11, venue/length decision (all unchanged). Board/audit: `../INT_v3/ROUND_2026-09-19-PSU-v1S.0.10-EXACTPDF-1015f442-R4/claude_opus_referee.md`, `../R4COMPLETE_PSU_Grok_brutal.md`, `../R4COMPLETE_PSU_Gemini_cosmology.md`. **R2 budget spent — no further board without a new science/scope decision.** |

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

**R4 Claude-opus leg — RETURNED and TRUTH-AUDITED (2026-09-19): MAJOR REVISIONS.** Raw:
`INT_v3/ROUND_2026-09-19-PSU-v1S.0.10-EXACTPDF-1015f442-R4/claude_opus_referee.md`. The referee
independently re-derived and confirmed correct essentially all of Appendix A2's kernel totals,
Eq. (4)'s identity, the $-5$ composition, the general-$n_s$ $f_{\delta N}^{\rm fin}$ form, and
byte-verified all 10 cited SHA-256 prefixes — strong evidence the S12 fix introduced no
computational error. Findings:

- **MAJOR 2 — genuinely-new-real, CLOSED in v1S.0.11.** Sec. II's Eqs. (3)-(5), the
  "label-independent monopole $-5\eps/6$" claim, Fig. 1's caption, and the abstract's
  "translation term with zero monopole" print the $n_s=1$ special case as general-$\eps$, with
  no tilt caveat — a direct contradiction with the Appendix A2/A3 correction this lane had just
  applied. Root cause: the S12 manuscript fix touched only the Appendix, not the main text that
  restates the same formulas. Fixed: matching $n_s$ qualifiers, the general-$n_s$
  $f_{\rm map}^{\rm fin}$/$f_{\delta N}^{\rm fin}$ forms, and the corrected monopole-agreement
  statement now appear in Sec. II, the abstract, and Fig. 1's caption; the $-5$ statement
  strengthened to "for every constant $\eps$ and every spectral index $n_s$" in both places.
- **Two real wording slips in the S12 addition itself, CLOSED in v1S.0.11** (referee MINOR 4,
  MINOR 6): (i) App. A3/A4 stated the in-in shape's extra tilt term "is exactly $-\delta T$"
  without the required $\lambda^{-1}$ factor (the identity is
  $\lambda^{-1}[-\tfrac{5\eps}{12}(n_s-1)\mu^2]=-\delta T$) — both sentences now show the
  division explicitly. (ii) the Reproducibility Statement said the in-in tilt term is "derived
  from the linearised ADM constraints" (an in-in bispectrum term cannot come from linearised
  constraints alone) — corrected to name the actual route (re-running the committed in-in
  vertex assembly with general-tilt external spectra).
- **MAJOR 1, MAJOR 3, MAJOR 4 — real findings, NOT closed, NOT dismissed, OUT OF THIS LANE'S
  SCOPE.** Tracked as new gates **S13** (initial-slice/$\zeta_L(t_i)=0$ convention
  inconsistency across Eq. 1-2, $\lambda_{\rm USR}$, and the ekpyrosis Table I row), **S14**
  (Cai et al. 2009 factor-of-2 erratum rests on an unpublished note, not an in-paper
  derivation), and **S15** (Appendix A5's $\lambda_g=1-\eps g/3$ asserted rather than derived,
  conflicting with S13's flat-slice premise) — full detail in
  `project-context/SSOT/paper-su/status.md` and the raw report. None of the three concern S12
  or the headline $f_{\delta N}^{\rm init}=-5$; they concern pre-existing Sec. II/Appendix A5/
  Sec. I content this lane's S12-application brief did not scope in, and closing them properly
  is a real derivation task, not an edit — correctly left open per `/never-fabricate-derivation`
  rather than closed with an unsupported claim.
- MINOR items 1, 2, 3, 5, 7-16: real but cosmetic (undefined symbol $m$; a sign mismatch between
  Sec. II and App. A3's $\xi^i$ convention; undefined App. A5/A7 symbols; the $n_s(\eps)$
  validity range; an uncited blind-adjudication claim; etc.) — carried as **S16**, non-blocking.

Directive-G: v1S.0.10→v1S.0.11 (4-pass, 0 undef refs, one new 26.77pt overfull hbox from the
added bracket fixed by wrapping into a two-line `align`, 0 overfull >10pt after, `/latex-audit`
visual PASS all 7 pages, md5 `c5b0ea962c5b9f965c22bc6d08d93250`, three-way matched including
Convex). No science number changed.

**R4COMPLETE (2026-09-19, campaign lane `bb-L2c-psu-r4-complete`) — Grok API + Gemini API legs
run on the exact v1S.0.11 PDF (sha256 `0fc47bd5…291563`), completing R4.** Preflight cleared
after three rounds of cross-lane shared-checkout contention (site-data dirty, then AF draft
dirty, then a stale AF mirror-integrity defect fixed as an unrelated one-line hygiene commit,
`f2fb65f4`); the exact v1S.0.11 tree state was preserved via `git stash` across the wait so the
API legs reviewed byte-identical content to the Claude-opus leg's target. Raws:
`../R4COMPLETE_PSU_Grok_brutal.md` (grok-4.3, REJECT), `../R4COMPLETE_PSU_Gemini_cosmology.md`
(gemini-3.1-pro-preview, MAJOR REVISIONS). **Record keeping: the Claude-opus leg reviewed
v1S.0.10; the Grok/Gemini legs reviewed v1S.0.11 — different exact PDFs, not blended.**

Truth-audit of every finding (verdict-first, against this file's fingerprints and by
independent re-derivation where a physics claim was made):

**Genuinely-new-real, CLOSED in v1S.0.12:**
- **S14 (Gemini ESSENTIAL-1, the Cai-citation half)** — confirmed real: Sec. I's factor-of-2
  claim against Cai et al. (2009), a published PRD paper, was cited only to
  `Golden2026Monopole`, an unpublished note that (checked directly) does not even contain the
  Cai comparison. The actual equation-level derivation lives in
  `research/theory_audit/psu_gate_S7_cai_factor_2026_09_05.md` (fetches the real arXiv e-prints
  of both Cai 2009 and Li–Quintin–Wang–Cai 2017, tests four hypotheses against Cai's own
  printed Eqs. 38–41 and Fig. 5, LOCATED verdict) but was never cited in the paper at all.
  **Fixed:** new bibitem `Golden2026CaiFactor` (commit `7222c91f`), Sec. I's sentence now cites
  it, and a new Appendix~A6 ("The Cai et al. (2009) amplitude factor of two") transcribes the
  note's hypothesis table and verdict verbatim (transcription only, no new math —
  `/never-fabricate-derivation` clean). The self-containment concern for the *in-in shape*
  itself (the other half of Gemini's ESSENTIAL-1) remains part of already-tracked **S4**.
- **PSU-N2 (Gemini pass-2 finding "N2"), cross-reference error** — confirmed real by direct
  text check: three in-text `(App.~A2)` citations (main.tex, formerly lines 176, 201, 337) all
  cite formulas/statements that are actually in Appendix **A3** ("The two worldline labels and
  the translation" — the general-$n_s$ initial-position monopole formula and the "kernel
  carries no $1/k_L$ pole" statement), not Appendix A2 ("The five second-order kernel
  contributions"). **Fixed:** all three corrected to `(App.~A3)`.
- **Gemini pass-2 "m1", Fig. 1 caption/plot ambiguity** — confirmed real by rendering the
  actual figure: $\lambda(w)$ and $f_{\rm map}^{\rm mono}(w)$ are deliberately dual-axis-scaled
  to coincide exactly, so only one visible curve appears on the page — a genuine reader-facing
  clarity gap, not a rendering defect. **Fixed:** one sentence added to the Fig. 1 caption
  stating the axes are scaled so the two curves coincide by construction.
- **Grok "M1" + Gemini "MAJOR-3" (independently, both reviewers), Table I's USR row** —
  confirmed real: the row prints exact values ($5/2$, $5/2$, $5/2$) next to "(not computed
  here)" with no in-row citation, reading as an internally-derived validated number when it is
  Namjoo–Firouzjahi–Sasaki's (2013) literature value (the citation exists two paragraphs later
  in prose, not in the table). **Fixed:** table caption gains a footnote citing
  `\cite{Namjoo2013}` directly, explicit that the row tests only the structural order.

**Re-flagged, no new action (already tracked):**
- Grok "E3" + the self-containment half of Gemini "ESSENTIAL-1" (in-in shape/derivations live
  in companion notes) = **S4**, OPEN non-blocking, unchanged since R1.
- Gemini "ESSENTIAL-2" (need a persistent Zenodo DOI for the reproducibility scripts) = **S11**,
  OPEN non-blocking, unchanged since R1.
- Gemini "MAJOR-4" (7 pp. exceeds the ~4.5 pp. PRD-Letter limit) = the already-tracked
  Houston-gated venue/length decision (SSOT close-the-gap section), unchanged.
- Grok "E4"/"E5"/"N1" + Gemini "MINOR N1" (reproducibility-statement hashes, AI Usage
  Disclosure section, version-string header read as "internal bookkeeping") = genre re-flags of
  the same pattern dispositioned across R1–R4 (PSU-17/28, C27, C31) — directive R2's genre
  exception; these are deliberate lab-policy disclosures, not defects.
- Grok "N5"/"N3" ("not computed here" inside the abstract) + Gemini "N3" (2026 dates read as
  stale) = same genre pattern; the honest disclosure is directive Q1/R6-compliant by design,
  and 2026 is the correct current date (not an error).

**FALSIFIED (independently re-derived or checked against the source text; not real):**
- Grok "E1"/"E2" (abstract/title overstate generality) — the abstract already states "for
  every constant $\eps$" for the second-order claim; the linear-order "exact" claim is
  legitimately general per Eq. (2)'s own proof (any single-field history); Sec. V "Limits"
  explicitly bounds validity (constant $c_s$/$\eps$, no time-dependent-$\eps$ second-order
  calc). Mischaracterizes already-precise, already-scoped language; the quoted phrase "carries
  an $O(1)$ error … not in either variable separately" exists (Sec. III's boxed statement, not
  the abstract) and is a correct, generally-true statement about the linear criterion.
- Grok "E6" (claims an "immediately following clause" asserts $f^\rho_{\rm NL}=-5/16$,
  contradicting the printed $-55/16$) — no such clause exists anywhere in the source text
  (checked verbatim); apparent misread of an unrelated $15/16$ coefficient elsewhere on the
  same page.
- Grok "E7" (claims the general-$n_s$ expression "preceding Eq. (4)" gives $+25/4$ at
  $\eps=3/2,n_s=1$) — independently re-derived Eq. (3)/(4) and the full composition by hand at
  $\eps=3/2,n_s=1$: reproduces the paper's own claimed $f_{\delta N}^{\rm init}=-5$ exactly (via
  $f^{\rm in\text{-}in}_{\rm mono}=-15/8$, $\lambda=1/2$: $-15/8\div(1/2)+(-5/4)=-5$); no
  $+25/4$ appears in any term.
- Grok "M5" (Fig. 1 "identity at $w=-1$" over-claim; "quadrupole piece … remains finite") —
  the quoted quadrupole formula does not match $f_{\rm map}^{\rm fin}$'s actual form (it matches
  an unrelated translation-term expression); at $w=-1$ ($\eps=0$), $f_{\rm map}^{\rm fin}(\eps,
  \mu)=-\tfrac{5\eps}{4}(1-\mu^2)$ vanishes identically for *every* $\mu$ (overall $\eps$
  prefactor), confirming the paper's identity-map claim is correct.
- Grok "N2"/"N4" (footnote 1 "asserts five … enumerates a sixth") — footnote 1 already reads
  "Four geometric contributions to $f_{\rm map}^{\rm fin}$ … A fifth contribution, the
  initial-label translation, is the difference that distinguishes $f_{\rm map}^{\rm init}$ from
  $f_{\rm map}^{\rm fin}$" (verified in the rendered v1S.0.11 PDF) — this exact defect (PSU-12,
  R3VERIFY) was already fixed before this round.
- Grok "M2"/"M3" — genre/opinion (style preference for denser anchoring against Refs.
  [3,4,9,12]); Sec. IV "What is new" already individually distinguishes this note's
  contribution from Refs. [3,4,6,9,10,11,12,13,14].

**Genuinely-new-real count this round: 4** (S14's citation fix, the 3 App.~A2→A3
cross-references, the Fig. 1 caption clarity note, and the Table I USR citation — S14 counted
once; App.~A2/A3 + caption + table are 3 additional independent items). All 4 closed in
v1S.0.12 with real, source-cited edits (no new derivations beyond transcription of an existing
verified note for S14). S13/S15/S16/S4/S11/venue-length remain OPEN, unchanged, not re-raised
this round.

**Directive-G:** v1S.0.11→v1S.0.12. 4-pass pdflatex, 0 undef refs, 0 raw non-ASCII, leak-gate
clean. One transient 179pt table overfull hbox from an over-long USR-row parenthetical was
caught and fixed by moving the citation to a table-caption footnote instead (final table
overfull is 12.6pt, `/latex-audit` visually confirmed PASS — full-width `table*`, no column
crossing, matches the pre-existing ~8pt Table I alignment overflow class already tracked across
rounds). 8 pages (up from 7 — the new Appendix A6 pushes one paragraph to a new page, mostly
whitespace, cosmetic). PDF md5 `7bae5b35c4ee1456557a8c74f57a3692`, sha256
`d400dec4a70d5167b8ddbc0f2acef4185d3cdb08077f550601f25add8a730ac5`, three-way matched: fresh
compile == `site/public/papers/paper_su_criterion_v1S.0.12.pdf` ==
`public/papers/paper_su_criterion_v1S.0.12.pdf`. No science number changed (all four closures
are citation/cross-reference/caption fixes and one appendix transcription).

**R4 status: COMPLETE.** All three legs run and truth-audited: Claude-opus (v1S.0.10, MAJOR
REVISIONS, dispositioned in v1S.0.11), Grok API (v1S.0.11, REJECT, dispositioned above — mostly
FALSIFIED/genre, 1 genuinely-real item contributing), Gemini API (v1S.0.11, MAJOR REVISIONS,
dispositioned above — 1 genuinely-real ESSENTIAL half-closed as S14, 2 more genuinely-real
items, rest re-flags). **Per this lane's task directive and directive R2, the round budget for
paper-su is now spent — R4 is the one board the S12 science decision unlocked, and it is
closed. No further review round on paper-su without a new intervening science/scope decision.**
Open, unchanged, non-blocking: S13 (initial-slice convention, needs a real derivation), S15
(Appendix A5 $\lambda_g$ derivation, needs a real derivation, linked to S13), S16 (cosmetic
MINORs, carried), S4 (self-containedness), S11 (Zenodo DOI), the Letter-vs-Brief-Report
length/venue decision (Houston-gated).
