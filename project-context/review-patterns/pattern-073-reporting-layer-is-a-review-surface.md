# Pattern 073 — The reporting layer is a first-class review surface

**Class:** trust-infrastructure
**First observed:** 2026-07-23 (Houston confidence crisis triggered by stale grid/banner/widget while the papers themselves were fine)

## Observation
The papers were converged and consistent, but the /reviews verdict grid, the
home banner date, and the ETA widget lagged days behind — and the stakeholder
read the STALE REPORTING as evidence the SCIENCE was untrustworthy. Reporting
drift is indistinguishable from content drift to the reader.

## Rule
Every review wave must land its data on EVERY rendering surface in the same
bundle: Convex rows AND grid data (externalVerdictRounds) AND banner strings
AND any Convex FUNCTION whose aggregation feeds a widget. A wave that reached
the database but not the grid "didn't happen" to the reader. Add each new
reporting surface to the freshness gate the day it ships.
