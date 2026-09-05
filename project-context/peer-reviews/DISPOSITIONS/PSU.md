# PSU disposition ledger — `paper-su`

**Canonical source:** `arxiv/paper_su_criterion/main.tex`
**Current paper-local version:** `v1S.0.2` (2026-09-04)
**Exact PDF:** `arxiv/paper_su_criterion/main.pdf` == `site/public/papers/paper_su_criterion_v1S.0.2.pdf`,
sha256 `812dbaf1af7e8eafa5769730fed55c81cfa8b429fbeab022d1125be1527aca31`, md5 `fcbecd03…`, 4 pp.
(R1 artifact was `cc0dfb84…c48e` = v1S.0.1.)
**Venue:** Physical Review D — Letter / short note.
**Claim policy (as of R1, pending S3):** the note currently asserts an $O(1)$ *failure* of the
isotropic separate universe. The committed source note it rests on concludes the opposite
framing ("there was never a discrepancy in the physics, only in the variable",
`research/theory_audit/threading_map_second_order_2026_09_04.md` §4). Until S3 is adjudicated,
do **not** restate the failure framing in SSOT, site copy, or abstracts as settled.

## Round history

| Round | Exact PDF sha256 | Legs | Outcome |
|---|---|---|---|
| `ROUND_2026-09-04-PSU-v1S.0.1-EXACTPDF-cc0dfb84-R1` | `cc0dfb84…c48e` | Claude Fable 5.1 INT (**major-revisions**), Grok API (**REJECT**), Gemini API (**MAJOR REVISIONS**); OpenAI/ChatGPT **ABSENT** (directive N pause) | 38 raw findings → **28 canonical**: 21 GENUINELY-NEW REAL, 0 re-flag, 5 FALSIFIED, 1 OPINION/GENRE, 1 OUT-OF-SCOPE-DISCLOSED. Clean-wave count **0**. Board: `../PSU_v1S.0.1_R1_BOARD_2026-09-04.md`; audit: `../INT_v3/PSU_v1S.0.1_R1_TRUTH_AUDIT_2026-09-04.md` |
| `ROUND_2026-09-04-PSU-v1S.0.2-EXACTPDF-812dbaf1-R2VERIFY` | `812dbaf1…aca31` | Claude Fable 5.1 INT (**major-revisions**, 6M/13m/4Q), Grok API (**REJECT**), Gemini API (**MAJOR REVISIONS**); OpenAI/ChatGPT **ABSENT** (directive N pause) | 39 raw findings → **32 canonical**: 20 GENUINELY-NEW REAL, 6 re-flag (4 still OPEN), 1 OUT-OF-SCOPE-DISCLOSED, 2 FALSIFIED, 3 OPINION. Clean-wave count **0**. Board: `../INT_v3/PSU_v1S.0.2_R2_BOARD_2026-09-04.md`; audit: `../INT_v3/PSU_v1S.0.2_R2_TRUTH_AUDIT_2026-09-04.md` |

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
