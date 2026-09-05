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
