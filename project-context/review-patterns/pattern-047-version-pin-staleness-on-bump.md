---
pattern_id: 047
status: active
first_seen: EXT1 (2026-06-10, first automated browser-tier external round)
papers_observed: [P1A, P1B, P2, P3, P4, P5]
proposed_by: EXT1 gap-mine 2026-06-10
---

# pattern-047: version-pin-staleness-on-bump

**Description**: Data Availability commit hashes, bundle metadata, and DOI placeholders go stale across version bumps

**Evidence (EXT1)**: P4 F1 (2a2939b2=v1.0.166 cited in v1.0.171), P1A F6 (bundle README v0.9.0), P2 F18 + P3 F5 (no frozen DOI/hashes prepared)

**Prevention**: Bump pipeline stamps the .tex version but not the provenance surfaces. Gate added to /bigbounce-version-bump — every bump must update Data Availability hash, bundle metadata labels, and release manifests in the same commit.
