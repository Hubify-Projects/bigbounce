# P1B v2B.0.18 R2 — TRUTH AUDIT (skeptical, verdict-first)

**Exact artefact:** `arxiv/paper1b_namaster_proof.pdf` == `site/public/papers/paper1b_namaster_proof_v2B.0.18.pdf`
sha256 `354d63b2e672ba4084987d993e59b73fd457a020a6bb794895c6e1d5074f88d2`, md5 `89cbca0f…`, 12 pp.
**Round:** `ROUND_2026-09-04-P1B-v2B.0.18-EXACTPDF-354d63b2-R2VERIFY`
**Receipt:** `INT_v3/ROUND_2026-09-04-P1B-v2B.0.18-EXACTPDF-354d63b2-R2VERIFY/preflight_receipt.json`
(generic rule receipt: 9 rules, 0 findings). No `Reviewer call FAILED` strings in either raw.
**Board:** `P1B_v2B.0.18_R2_BOARD_2026-09-04.md`
**Prior ledger:** `DISPOSITIONS/P1B.md` (R1 canonical C1–C23)

## Plan (executed in the sections below)

1. Board built from raws (verdicts read from raw text, not labels).
2. Fingerprint every finding from all three legs; classify (a) genuinely-new REAL,
   (b) re-flag w/ disposition id, (c) FALSIFIED w/ source, (d) OPINION/genre/venue,
   (e) OUT-OF-SCOPE disclosed.
3. Verify the statistics claims directly against `pipelines/namaster_proof/blind_test/`
   (batch-2 scorecard, `RULES_v2_FROZEN.md`, `verify.py`, `variants2.py`, `windows` module).
4. Canonical list with class + citation + closure action; per-leg counts.
5. CLOSURE PLAN: (i) editorial edits for v2B.0.19, (ii) science items.
6. R2 statement + `DISPOSITIONS/P1B.md` update.

*(sections filled in below; committed section-by-section)*

---

## 1. Independent verification of the contested statistics claims

All checks below were run by this auditor against
`pipelines/namaster_proof/blind_test/` at the round HEAD, not taken from any leg.

**(a) Clopper–Pearson arithmetic — the quoted one-sided bounds are correct.**
`public2/scorecard.json`: `detection_structural_S1_S4.lower95_one_sided = 0.8609`,
`false_positive_rate_honest.upper95_one_sided = 0.4507`. Recomputed: \(0.05^{1/20}=0.8609\),
\(1-0.05^{1/5}=0.4507\). **Not falsified — the numbers are right.**

**(b) The "95% interval [0.501, 0.807]" is a 90% interval — CONFIRMED REAL.**
Recomputed with `scipy.stats.beta`: two-sided CP for \(k=20,n=30\) is
**[0.4719, 0.8271] at 95%** and **[0.5006, 0.8067] at 90%**. The paper's pair is
exactly the scorecard's `lower95_one_sided`/`upper95_one_sided` (0.5006/0.8067), i.e.
two one-sided 95% bounds intersected — a 90% two-sided interval. `arxiv/paper1b_namaster_proof.tex:461`
labels it "95\% interval". Gemini E2 and Opus M2 are both correct and agree numerically.

**(c) The Opus M1 independence objection is CORRECT and self-inflicted by the paper.**
`RULES_v2_FROZEN.md` (pre-registered, "Independence caveat") and
`scorecard.json::independence_caveat` both state: "R1–R5 compare seed-independent
quantities against a fixed contract … effective independent n = 1". The per-arm table
confirms the mechanism: S1/S2 fire on R3+R4 only, S3 on R2+R3+R4 — all contract
comparisons of seed-independent quantities. A Clopper–Pearson interval assumes 20 i.i.d.
Bernoulli trials; under the paper's own pre-registration there are **4 deterministic
class-level outcomes**, not 20 trials. The abstract nevertheless leads with
"20 of 20 … (one-sided 95% Clopper–Pearson lower bound 0.861)" with no caveat
(`arxiv/paper1b_namaster_proof.tex` abstract, lines 175–180). The bound is arithmetically
right and inferentially void. **The honest replacement** is the design-level statement:
*"every replicate of all four structural classes was flagged (20/20 runs, 4/4 classes);
because R1–R5 compare seed-independent quantities, the replicates measure firing
determinism rather than sampling variance, so no detection-probability interval is
claimed."* If an interval is wanted, the only i.i.d. unit is the **class** (n=4,
one-sided 95% CP lower bound **0.4729**) — which is weak enough that the no-interval
statement is the stronger and more honest presentation. Same for the honest arm:
0/5 is effectively 0/1 for R1–R5 (only R6 is seed-sensitive), so "upper bound 0.451"
must go or carry the caveat inline.

**(d) The pooled 20/30 is an artefact of arm design — CONFIRMED.** Its value is fixed by
the choice to run four caught classes and two escape classes at equal replication; adding
a seventh class moves it with no change in detector performance. It is not an estimator
of any population quantity. Correct presentation: delete it, or state per-class outcomes
only (4/4 structural classes detected, 2/2 out-of-scope classes escaped as designed).

**(e) M3 (spin-0 vs spin-2) — CONFIRMED REAL from the code.** The windows layer's
documented contract is a \([4,n_b,4,n_\ell]\) tensor returning a \([4,n_b]\) array
(`arxiv/paper1b_namaster_proof.tex:264-265`) — a **spin-2** (EE,EB,BE,BB) workspace; the
retained artifact is \([4,20,4,1025]\) (line 598). The **spin-0** MASTER implementation is
the *blind test's* instrumented estimator (`blind_test/pcl.py:3`, "the full spin-0 MASTER
estimator"), a different object. The abstract attaches "spin-0" to the package's headline
window capability — factually wrong. Second half also confirmed: the abstract's
"not run against NaMaster or PyMaster itself" is contradicted by §8 (retained PyMaster
artifact), §9 ("Real PyMaster integration", lines 630–634) and §12 ("the retained physical
validation used PyMaster 2.6", line 735). The defensible statement is scoped to the blind
test only. Verified separately: `import pymaster` fails in this environment (true), **but
`pip download pymaster` resolves wheels for this platform** — so the cross-check is
feasible, not blocked (see science item S2).

**(f) M4 — CONFIRMED from `scorecard.json`.** S4: `r6_reference_disjunct = 5`,
`r6_crossrun_disjunct = 0`. The cross-run disjunct — the realistic cache-substitution
signal — was never exercised. S1/S2/S3 share R3+R4 (one trace-mismatch mechanism);
S4 is the only second mechanism. "Four structural classes" ≠ four independent mechanisms.

**(g) M7 — CONFIRMED.** `grep -rn "1\.66"` across `pipelines/namaster_proof/` returns no
script or committed output producing the 1.66 / 0.17 fractional deviations quoted at
`arxiv/paper1b_namaster_proof.tex:228-229`. Every other headline number is traceable.

**(h) Grok M2 partially FALSIFIED.** The "precise Wigner-3j count" *is* published:
`public2/contract.json::n_wigner3j = 137345`, and R3 enforces it. The mask digest
(`mask_sha256`), `ell_grid` (65 entries), `coupling_support = 4225`, `nside`, `lmax`
and the environment are all in the same committed contract. Only the workspace-tensor
DOI request survives as an enhancement.

**(i) Pre-registration.** Not re-derived here; the Opus leg's independent re-derivation
(assignment digest `c96b5bf1…` reproduced from the revealed key; seal commit `28efa21c`
contains only `sealed_digest.json` + `frozen_rules_digest.json`; verifier sha256
`6a9acd70…`) is accepted as verified evidence, and `public2/sealed_digest.json.ots`
(875 B, 19:31) exists as claimed. **No fabricated number was found in this paper.**

---

## 2. Canonical findings (27) — class · citation · closure action

Classes: **NEW** genuinely-new real · **RF** re-flag (disposition id) · **FAL** falsified
with source · **OP** opinion/genre/venue · **OOS** out-of-scope, disclosed · **SCI** new science.

| # | Fingerprint | Legs | Class | Citation | Closure |
|---|---|---|---|---|---|
| D-R2-01 | Abstract's CP bounds contradict the paper's own pre-declared independence caveat | Grok E2, Opus M1 | **NEW** | tex abstract 175–180 vs 461–467; `RULES_v2_FROZEN.md` independence caveat | v2B.0.19 abstract rewrite (§3-E1) |
| D-R2-02 | "95% interval [0.501,0.807]" is the 90% two-sided CP interval; pooled 20/30 is an arm-design artefact | Gemini E2, Opus M2, Opus Q5 | **NEW** (verified §1b/1d) | tex:461; recomputed 95%=[0.4719,0.8271] | v2B.0.19 §6 rewrite (§3-E2) |
| D-R2-03 | Abstract calls the window capability spin-0 (module contracts a spin-2 workspace) and says "not run against PyMaster" while §§8/9/12 report PyMaster 2.6 | Opus M3 | **NEW** (verified §1e) | tex:163, 264–265, 598, 630–634, 735; `blind_test/pcl.py:3` | v2B.0.19 abstract split (§3-E3) |
| D-R2-04 | S1–S3 share one detection mechanism (R3+R4); S4's cross-run R6 disjunct never exercised | Opus M4, Q2 | **NEW** (verified §1f) | `public2/scorecard.json` per-arm | v2B.0.19 §6 sentence + batch-3 science item S1 |
| D-R2-05 | Pre-registration is verifiable but the paper gives no verification recipe; freeze commit holds only the spec; sealed digest is over canonical JSON, not file bytes | Opus M5 | **NEW** | `4451b135`, `28efa21c`, `seal2.py::digest` | v2B.0.19 "how to check this yourself" list |
| D-R2-06 | "(S3, open)" / "(S2, in progress)" are dangling internal tags that collide with shortcut-class names | Gemini E1, Opus M6 | **NEW** | tex:692, 694 | v2B.0.19 numbered L1/L2 limitation list |
| D-R2-07 | §2's 1.66 / 0.17 fractional deviations trace to no committed artefact | Opus M7, Q3 | **NEW** (verified §1g) | tex:228–229; grep of `pipelines/namaster_proof/` | v2B.0.19 cite script+output, or recompute and commit |
| D-R2-08 | "to our knowledge this is the first…" primacy claim with no prior-art survey | Grok E1, Opus m1 | **NEW** | tex:182–186 | v2B.0.19 delete the primacy flag, state the contribution |
| D-R2-09 | "negligible memory footprint" is an unquantified performance claim | Gemini M1 | **NEW** | tex:721 | v2B.0.19 measured MB number or delete |
| D-R2-10 | Self-referential "§6" cross-references from inside §6 | Opus m2 | **NEW** (trivial) | tex §6, Table 2 | v2B.0.19 named paragraph pointers |
| D-R2-11 | 34-second seal→reveal window; discard-and-retry residual gap unnamed (OTS does not close it) | Opus m3, Q1 | **NEW** | commit times 19:01:41→19:04:49 | v2B.0.19 one sentence + explicit "run once" statement |
| D-R2-12 | OTS anchor status not dated or made checkable | Opus m4 | **NEW** | `public2/sealed_digest.json.ots` (875 B, 19:31) | v2B.0.19 give `ots upgrade`/`verify` + what it proves |
| D-R2-13 | Pre-declared success criterion file/commit not cited | Opus m5 | **NEW** | `BATCH2_PREREGISTRATION.md` in seal commit `28efa21c` | v2B.0.19 cite file + commit |
| D-R2-14 | R6 *description* correction (a third post-hoc change, no code change) missing from the pilot-disclosure paragraph — material because S4's 5/5 rests on that disjunct | Opus m6 | **NEW** | `RULES_v2_FROZEN.md` §"R6 — description corrected" | v2B.0.19 add to disclosure |
| D-R2-15 | Related work omits remote-attestation (TPM/SGX/TDX) and verifiable-computation (SNARK) lines | Opus m9 | **NEW** (minor) | tex §7 | v2B.0.19 two sentences + citations |
| D-R2-16 | Coverage abstention (no coverage tool configured) left implicit | Opus m11 | **NEW** (trivial) | tex §8 "39/41 standalone-effective" | v2B.0.19 make explicit |
| D-R2-17 | Table 2 caption carries an implementation detail ("exactly as implemented in verify.py") | Grok N2 | **NEW** (trivial) | tex Table 2 caption | v2B.0.19 move to text |
| D-R2-18 | "pilot / rule-development round" — spaced slash | Gemini N1 | **NEW** (trivial) | tex:384, 471 | v2B.0.19 rephrase |
| D-R2-19 | Title-page date + internal version string `v2B.0.18(…PT)` | Grok N1 | **NEW**, deferred | tex:152 | Lab directive-G requires the stamp on review builds; **strip in the submission build only** — recorded, not actioned in v2B.0.19 |
| D-R2-20 | JORS scope/adoption/length: no usage metrics, dependent packages, or external users | Grok E3 | **OP** / **RF C11** | R1 ledger C11 (JORS length/scope opinion, recorded not actioned) | Venue-fit opinion; recorded. Venue decision is a science/strategy call, not an edit |
| D-R2-21 | No value-level rule; S6 evades R0–R6 by construction; "presented as a finding rather than a design limitation" | Grok M1 | **FAL** (framing half) + **RF C5** + **SCI** | Framing falsified: abstract states the primitive is "not… of value-level shortcuts taken downstream" (tex:182–184) and §11 lists S6 as a limitation (tex:685–690); C5 already dispositioned | Framing half closed by citation; the value-level rule is **batch-3 science item S1** |
| D-R2-22 | No frozen release hash of the workspace tensor or the precise Wigner-3j count | Grok M2 | **FAL** (3j half) + **OP** (DOI half) | `public2/contract.json::n_wigner3j = 137345`, `mask_sha256`, `ell_grid`, `coupling_support`; R3 enforces the count | 3j half closed by citation; separate-DOI request recorded as enhancement |
| D-R2-23 | Threat model incomplete: adversary who also edits the harness | Grok M3 | **OOS disclosed** | Abstract states the unmodified-instrumented-harness model explicitly (tex:170–172); §11 states metadata forgery cannot in principle be caught | No edit required; D-R2-15's attestation citation is the constructive remainder |
| D-R2-24 | Express the 1.66 deviation as a bias on \(r\) or \(\beta\) | Gemini M2 | **OP** (Gemini itself: "not strictly required") | tex:228–229 | Recorded as enhancement |
| D-R2-25 | No figures for a paper whose result is a confusion matrix | Opus m7 | **OP** / genre | tex (4 tables, 0 figures) | Optional; a per-arm detection figure is a v2B.0.19 nice-to-have |
| D-R2-26 | Regenerate the \(1.41\times10^{-18}\) scalar under a live PyMaster so the number is matchable | Opus m8 | **SCI** | tex:598–612; `rebuild_workspace_check.py` | Batch-3 science item S2 (PyMaster wheels resolve on this platform) |
| D-R2-27 | Is an upstream 3j counter feasible in NaMaster/PyMaster, or does the C layer make it unobservable without a fork? | Opus Q4 | **SCI** | tex §11 | Science item S3 — one sentence makes §11 actionable rather than terminal |

### Per-leg counts

| Leg | Raw findings | NEW | RF | FAL | OP | OOS | SCI |
|---|---|---|---|---|---|---|---|
| Grok API (REJECT) | 8 | 4 (E1,E2,N1,N2) | 1 (E3→C11) | 2 partial (M1,M2) | 1 (E3 venue) | 1 (M3) | 1 (M1 remainder) |
| Gemini API (MINOR REVISIONS) | 5 | 4 (E1,E2,M1,N1) | 0 | 0 | 1 (M2) | 0 | 0 |
| Claude INT Opus (major-revisions) | 23 (7M/11m/5q) | 15 | 0 | 0 | 1 (m7) | 0 | 2 (m8, Q4) |

**Canonical total 27 · genuinely-new REAL 19 · OPINION 3 · FALSIFIED-in-part 2 ·
OUT-OF-SCOPE-disclosed 1 · SCIENCE 2.** Zero fabricated numbers found; zero findings
dispositioned without a source citation.
