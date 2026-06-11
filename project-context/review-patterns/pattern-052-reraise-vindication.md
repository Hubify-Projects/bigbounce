---
pattern_id: 052
status: active
first_seen: EXT3 (2026-06-11 — P2 Addis citation, vindicated after two wrongful falsifications)
papers_observed: [P2, P5]
proposed_by: EXT3 gap-mine 2026-06-11
---

# pattern-052: re-raise vindication test

**Description**: When a reviewer re-raises a previously-FALSIFIED finding across rounds, the re-raise is ITSELF evidence. Two outcomes observed: P5 k=20 (re-raised twice, auto-falsified correctly — prior falsification was evidence-based: the rerun IS in the paper) vs P2 Addis citation (re-raised twice, VINDICATED on source fetch — prior falsifications were assumption-based, nobody had fetched the source).

**Rule**: a finding may only be auto-falsified on re-raise if the PRIOR falsification cites primary evidence (grep output, artifact content, fetched source). If the prior verdict rested on assumption or paper-internal consistency alone, a re-raise triggers MANDATORY primary-source verification (WebFetch the citation, open the artifact, run the computation) before any verdict. Track re-raise counts in the audit table; third raises get a named auditor note either way.
