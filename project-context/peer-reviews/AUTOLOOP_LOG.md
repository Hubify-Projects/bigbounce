
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