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
