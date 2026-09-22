# LS13 `bb-LS13-p1n-essentials` — run log

`LS13-p1n-essentials START 2026-09-22T10:17Z` — lane opened. Scope: real science
closure of DP1N-60 (contact-term equation of state / repulsion sign condition)
and DP1N-61 (Poplawski2012 dark-energy rebuttal scale) on P1N
(`arxiv/paper1bc_ech_note/main.tex`, v1N.0.7, readiness 95, SIGN-OFF HOLD).
Derive from scratch; do not adjudicate. Withdrawal is an acceptable outcome.

`LS13-p1n-essentials MILESTONE` — numerics closed
(`outputs/eos_and_scales.json`). Fluid machinery validated against four
known-answer cases (dust w=0, radiation w=1/3, vacuum w=-1, two-body contact
w=+1) plus the textbook Gross-Pitaevskii mean-field contact-gas equation of
state, and against the a^-6 scaling consistency of w=+1. Manuscript's own
Sec. II.A arithmetic independently reproduced to 4 s.f.
(kappa n_psi^2 = 9.954e-80 eV^4, ratio 3.884e-69) -- the manuscript's
benchmark number is CORRECT; the CONFIRM board's falsification of the
adversarial "57-order unit error" stands re-confirmed a fourth time.

`LS13-p1n-essentials BLOCKED->SUBSTITUTED` — blind adjudicator leg, `fable`
attempt 1: **FAILED-INFRA**, HTTP 429 "out of usage credits"
(request id req_011CfJL14ksKRvnaqNLPmeYv, model claude-fable-5-1). Recorded as
infrastructure failure, NOT as a verdict. Substituted with `opus` under the
changed label `blind-adjudicator-opus` per the lane's 429 rule.

`LS13-p1n-essentials MILESTONE` — derivation + propagation note committed
(`ea8f626b`) and pushed.

**FRESHNESS_SKIP record (correction).** `ea8f626b` was pushed with
`FRESHNESS_SKIP=1`. The gate's failure was verified afterwards to be **solely**
the six `versions ... Convex unreachable x2 - infra, not staleness` rows (the
only `STALE` rows; `skillslog` is `WARN`, and banner/skills/board/heartbeat/
papers are all `FRESH`) — so the bypass was legitimate under the lane rule, but
the required statement was omitted from that commit's body. Recorded here and
restated in the next commit body rather than rewriting pushed history.

`LS13-p1n-essentials MILESTONE` — independent blind-adjudication leg returned.
`blind-adjudicator-opus` (substituted for the 429'd `fable` leg, label changed)
was given both questions with **neither this lane's conclusions nor its method**,
and was explicitly permitted to answer "undecidable". It independently reached:
`w=+1` via the same on-shell cubic-Dirac mechanism; `ρ+3p = -4L_4ψ` and the
inverted sign condition; the ECSK `ε_spin=p_spin` cross-check; and every DP1N-61
finding (condensate mechanism, `(54 meV)^4` reproduced, ~74-order scale gap,
"direct quantitative rebuttal" UNSUPPORTED). Its arithmetic agrees with
`outputs/eos_and_scales.json` throughout.

**It also corrected this lane.** On the sign of `⟨J5·J5⟩` in the bounce
configuration it cited the Kerlick result that the ECSK spin-spin contact
interaction is *attractive* for the Dirac field's totally antisymmetric spin
density. It mis-attributed the title to Kerlick's PRD 12, 3004 (1975); the
correct reference for that title is **R. F. O'Connell, PRD 16, 1247 (1977)**,
verified independently here against the OSTI record — the substance stands with
both citations corrected.

Consequence: this note's first §1.7 ("two compensating sign errors, paper's
conclusion survives, title claim intact") is **WITHDRAWN**. §II loses a claim,
not merely a derivation. `DERIVATION.md` §1.7 rewritten with the correction
recorded in place rather than silently replaced; `PROPAGATION_NOTE.md` §0, §1a,
§1b, §1c, §1d, §4 and §5 updated. **Readiness recommendation moved 88 → 85.**

`LS13-p1n-essentials DONE 2026-09-22` — DP1N-60 and DP1N-61 both closed by
derivation with three independent agreeing legs. Two claim withdrawals handed to
the P1N lane as exact printable sentences. No `main.tex`, SSOT, site-data or
ledger edits made by this lane. Convex writes not attempted (disabled); the
`paperVersions:bump` for the eventual P1N edit is the P1N lane's to queue.
