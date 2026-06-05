# Persistent Meta-Findings Tracker

Tracking META findings across 2 autoloop fires.
Rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1517pt']

## Findings that persist ≥2 rounds (escalation candidates for Houston decision)

Persistent META findings indicate scientific issues that the v3.2 meta-reviewer
consistently surfaces. They are NOT mechanical bugs — they require Houston's
judgment on which fix to apply (mechanical text edit vs analysis rerun vs
text relabel).

### 🟡 RECURRING P1B — `lee` (2/2 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1517pt']

Example (round auto-2026-06-05_1418pt, finding P1B-META-E1):

> “17 sampled parameters (7 cosmological + 10 Planck likelihood nuisance: Aplanck, amp143, amp217, amp143×217, n143, n217, n143×217, calTE, calEE, Mb for the SNIa absolute magnitude).”

### 🟡 RECURRING P3 — `dedup|deduplication` (2/2 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1517pt']

Example (round auto-2026-06-05_1418pt, finding P3-META-M8):

> “For the 7-way 5″ deduplication, the expected random coincidence contribution is ≲ 10 across all survey pairs against 637 observed multi-survey clusters (<2% contamination).” Given the large numbers of anomalies and heterogeneous footprints, ≲10 total random overlaps is implausibly low without a det

### 🟡 RECURRING P4 — `binomial` (2/2 rounds)

Seen in rounds: ['auto-2026-06-05_1418pt', 'auto-2026-06-05_1517pt']

Example (round auto-2026-06-05_1418pt, finding P4-META-m11):

> The pixel-space dipole fit (NSIDE=64, pixels with >10 spirals) does not state whether pixels are inverse-variance weighted (∝ Nspiral) or equally weighted. For a binomial-derived asymmetry per pixel, equal weighting is suboptimal and can bias the amplitude uncertainty.
