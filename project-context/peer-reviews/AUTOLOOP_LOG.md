
## 2026-06-05_1418pt — round=auto-2026-06-05_1418pt


## Cross-round diff: `R10v3` → `R10v3p1`

- **P1A**: 147 findings, 7 consensus | appeared=8, disappeared=2, new ESSENTIAL=0
    - CLOSED [duplicate_phrase] (was caught by 1 prev)
    - CLOSED [shamir_citation,companion,future_date] (was caught by 1 prev)
- **P1B**: 131 findings, 5 consensus | appeared=2, disappeared=5, new ESSENTIAL=0
    - CLOSED [audit_artifact] (was caught by 2 prev)
    - CLOSED [audit_artifact,duplicate_phrase] (was caught by 1 prev)
    - CLOSED [companion,duplicate_phrase] (was caught by 1 prev)
    - CLOSED [table_ii,audit_artifact] (was caught by 1 prev)
    - CLOSED [table_ii,companion,length,audit_artifact] (was caught by 1 prev)
- **P2**: 122 findings, 3 consensus | appeared=1, disappeared=3, new ESSENTIAL=0
    - CLOSED [audit_artifact] (was caught by 1 prev)
    - CLOSED [cosmic_variance] (was caught by 1 prev)
    - CLOSED [duplicate_phrase] (was caught by 1 prev)
- **P3**: 112 findings, 4 consensus | appeared=3, disappeared=4, new ESSENTIAL=0
    - CLOSED [companion] (was caught by 1 prev)
    - CLOSED [companion,duplicate_phrase] (was caught by 1 prev)
    - CLOSED [table_ii,table_iv,future_date,dedup_audit] (was caught by 1 prev)
    - CLOSED [table_iv,length] (was caught by 1 prev)
- **P4**: 181 findings, 13 consensus | appeared=10, disappeared=5, new ESSENTIAL=0
    - CLOSED [duplicate_phrase] (was caught by 1 prev)
    - CLOSED [length] (was caught by 1 prev)
    - CLOSED [n_mc_500,sigma_mixing] (was caught by 1 prev)
    - CLOSED [sigma_mixing,table_ii,table_ii_sigma_arithmetic] (was caught by 1 prev)
    - CLOSED [table_ii,table_iv] (was caught by 1 prev)
- **P5**: 116 findings, 4 consensus | appeared=3, disappeared=4, new ESSENTIAL=1
    + NEW ESS [sigma_mixing,table_ii,table_iv] caught by 1 reviewer(s)
    - CLOSED [companion,future_date,tweb_vweb] (was caught by 1 prev)
    - CLOSED [companion,length,tweb_vweb] (was caught by 1 prev)
    - CLOSED [sigma_mixing,table_ii] (was caught by 1 prev)
    - CLOSED [sigma_mixing,table_ii,length,future_date,tweb_vweb] (was caught by 1 prev)

### Cross-paper pattern candidates (consensus key appearing in 2+ papers)

- `audit_artifact` → in 3 papers: ['P1A', 'P3', 'P4']
- `companion` → in 4 papers: ['P1A', 'P1B', 'P2', 'P5']
- `companion,audit_artifact` → in 2 papers: ['P1A', 'P3']
- `companion,length` → in 2 papers: ['P1A', 'P1B']
- `future_date` → in 6 papers: ['P1A', 'P1B', 'P2', 'P3', 'P4', 'P5']
- `length` → in 2 papers: ['P2', 'P3']
- `shamir_citation` → in 2 papers: ['P1A', 'P4']
- `sigma_mixing` → in 6 papers: ['P1A', 'P1B', 'P2', 'P3', 'P4', 'P5']
- `sigma_mixing,table_ii` → in 2 papers: ['P1B', 'P4']
- `table_ii` → in 5 papers: ['P1A', 'P1B', 'P3', 'P4', 'P5']
- `table_ii,companion` → in 2 papers: ['P1A', 'P1B']
- `table_ii,length` → in 2 papers: ['P1A', 'P3']
- `table_iv` → in 3 papers: ['P1A', 'P3', 'P4']
- `table_iv,companion` → in 2 papers: ['P1A', 'P3']

**Total NEW ESSENTIAL across all 6 papers this round: 1**

**Self-terminate condition**: 3 consecutive rounds with 0 new ESSENTIAL.

---
## Cross-round diff: `R10v3p1` → `auto-2026-06-05_1418pt`

- **P1A**: 142 findings, 6 consensus | appeared=3, disappeared=4, new ESSENTIAL=0
    - CLOSED [shamir_citation] (was caught by 1 prev)
    - CLOSED [sigma_mixing,table_ii,table_iv,companion] (was caught by 1 prev)
    - CLOSED [table_ii,length] (was caught by 1 prev)
    - CLOSED [table_iv,shamir_citation] (was caught by 1 prev)
- **P1B**: 111 findings, 3 consensus | appeared=2, disappeared=4, new ESSENTIAL=0
    - CLOSED [companion,future_date] (was caught by 1 prev)
    - CLOSED [companion,length] (was caught by 1 prev)
    - CLOSED [sigma_mixing] (was caught by 2 prev)
    - CLOSED [table_ii,companion] (was caught by 2 prev)
- **P2**: 138 findings, 1 consensus | appeared=0, disappeared=0, new ESSENTIAL=0
- **P3**: 127 findings, 5 consensus | appeared=5, disappeared=4, new ESSENTIAL=2
    + NEW ESS [companion] caught by 1 reviewer(s)
    + NEW ESS [sigma_mixing,table_ii,dedup_audit] caught by 1 reviewer(s)
    - CLOSED [audit_artifact] (was caught by 1 prev)
    - CLOSED [companion,audit_artifact] (was caught by 1 prev)
    - CLOSED [table_ii,length] (was caught by 1 prev)
    - CLOSED [table_iv,companion] (was caught by 1 prev)
- **P4**: 108 findings, 5 consensus | appeared=10, disappeared=10, new ESSENTIAL=0
    - CLOSED [audit_artifact] (was caught by 1 prev)
    - CLOSED [fisher_floor] (was caught by 2 prev)
    - CLOSED [fisher_floor,dilution_factor] (was caught by 1 prev)
    - CLOSED [gz1_stale_n] (was caught by 3 prev)
    - CLOSED [iye_citation] (was caught by 1 prev)
    - CLOSED [shamir_citation,fisher_floor] (was caught by 1 prev)
    - CLOSED [table_ii,table_ii_sigma_arithmetic] (was caught by 2 prev)
    - CLOSED [table_ii,table_iv,shamir_citation,length] (was caught by 1 prev)
    - CLOSED [table_ii,table_iv,table_iv_z] (was caught by 1 prev)
    - CLOSED [weighting,fsky_effective] (was caught by 1 prev)
- **P5**: 92 findings, 6 consensus | appeared=8, disappeared=5, new ESSENTIAL=2
    + NEW ESS [sigma_mixing,table_ii] caught by 1 reviewer(s)
    + NEW ESS [sigma_mixing,table_ii,tweb_vweb] caught by 2 reviewer(s)
    - CLOSED [companion,tweb_vweb] (was caught by 1 prev)
    - CLOSED [duplicate_phrase,tweb_vweb] (was caught by 2 prev)
    - CLOSED [sigma_mixing,companion,tweb_vweb] (was caught by 1 prev)
    - CLOSED [sigma_mixing,table_ii,table_iv] (was caught by 1 prev)
    - CLOSED [table_ii,companion,length] (was caught by 1 prev)

### Cross-paper pattern candidates (consensus key appearing in 2+ papers)

- `audit_artifact` → in 2 papers: ['P1A', 'P1B']
- `companion` → in 5 papers: ['P1A', 'P1B', 'P2', 'P3', 'P5']
- `companion,duplicate_phrase` → in 2 papers: ['P3', 'P5']
- `companion,length` → in 2 papers: ['P1A', 'P5']
- `future_date` → in 6 papers: ['P1A', 'P1B', 'P2', 'P3', 'P4', 'P5']
- `length` → in 3 papers: ['P2', 'P3', 'P4']
- `shamir_citation` → in 2 papers: ['P4', 'P5']
- `sigma_mixing` → in 5 papers: ['P1A', 'P2', 'P3', 'P4', 'P5']
- `sigma_mixing,table_ii` → in 3 papers: ['P1B', 'P4', 'P5']
- `table_ii` → in 5 papers: ['P1A', 'P1B', 'P3', 'P4', 'P5']
- `table_iv` → in 3 papers: ['P1A', 'P3', 'P4']

**Total NEW ESSENTIAL across all 6 papers this round: 4**

**Self-terminate condition**: 3 consecutive rounds with 0 new ESSENTIAL.

---
### Meta-reviewer (v3.2) findings on fire 1

| Paper | ESS | MAJ | Notable |
|---|---|---|---|
| P1A | 9 | 0 | (still landing) |
| P1B | 3 | 7 | CMB E-B analysis deep gaps |
| P2 | (landed) | | (still indexing) |
| P3 | (running) | | — |
| P4 | 4 | 5 | META-E1 Ap denominator factor-of-2 ambiguity (fCW-0.5 vs Ap), META-E2 W_p=N_all includes NS (persists), META-E3 monopole-leakage explanation for POST-MASTER residual unproven, META-E4 double LEE correction (max-stat MC + Bonferroni is wrong) |
| P5 | 2 | 6 | T-Web vs V-Web mislabeling persists |

### Loop status
- Fire 1 complete (v3.1 reviews + most meta-reviews landed)
- P3 meta-review still running
- 4 NEW ESSENTIAL findings this round (loop continues; need 3 zero-new-ESS rounds to self-terminate)
- Next fire: cron at :17 next hour

### v3 tool improvements seeded into AUTOLOOP_IMPROVEMENTS.md
- bash 3.2 compatibility for v3_review_autoloop.sh (fixed)
- gpt-5 reasoning_effort vs max_output_tokens (fixed)
- Claude streaming + adaptive thinking (fixed)
- Synthesis parser for markdown header IDs (fixed)
- gap_audit excludes synthesis/meta files (fixed)
