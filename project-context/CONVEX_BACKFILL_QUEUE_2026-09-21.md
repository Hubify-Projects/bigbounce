# Convex backfill queue — 2026-09-21 Convex outage

Convex is DISABLED (deployment suspended for exceeding its spending limit; Houston-only
fix on the Convex dashboard). Every lane that would normally write live state via the
public HTTP API / ConvexHttpClient instead appends its exact intended mutation(s) here —
function name + exact args — so they can be replayed once Convex is re-enabled. Append
only; do not edit another lane's entries.

---

## LAF2 (bb-LAF2-af-todos), 2026-09-21

Paper AF, vAF.0.4 → vAF.0.5. Non-review directive-G bundle: DAF-16 fully closed
(released-column schema 183/192 → 192/192), full bibliography ADS-verification
completed (26 remaining entries, all match). No review board run (directive R2 stays at
round 1 of 2). See `project-context/SSOT/paper-af/status.md` §"LAF2 non-review TODO
closure" and `project-context/peer-reviews/DISPOSITIONS/AF.md` (DAF-16) for full detail.

```
paperVersions:bump({
  paperId: "AF" (slug "paper-af"),
  version: "vAF.0.5",
  pages: 18,
  date: "2026-09-21",
  sha256: "ea81ef413503d25291853a2be714226d3b47fe680ead2f01727aaabe961140ca",
  md5: "60de7e9dbfbcc77336b3050ee788e68e",
})

papers:setReadinessCap({
  slug: "paper-af",
  readinessCap: 77,   // was 75
})

activityFeed:add({
  type: "research",
  tags: ["paper-af", "vAF.0.5", "campaign-2026-09-18"],
  summary: "AF vAF.0.4->vAF.0.5 (lane LAF2, non-review): DAF-16 fully closed (schema table now documents all 192/192 released columns, was 183/192); full bibliography ADS-verified (26 remaining entries, all match, no text changed); OT-1 selection function and Zenodo DOI reconfirmed genuinely not agent-closable (GPU compute / Houston-only respectively), left unchanged. Directive-G bundle: 4-pass compile clean, 0 undef refs, 18pp, 5-way md5-verified mirrors, artifact-link-verify 6/6 pass, mirror-integrity 0 findings, arXiv tarball rebuilt+smoke-tested. Readiness 75->77 COMPUTED. Directive R2: round 1 of 2 still spent (no board run).",
})
```

---

## L4d (bb-L4d-p4p-row16-propagate), 2026-09-21

Paper P4P (P4′), v4P.0.9 → v4P.0.10. Science-content propagation (row-16(ii-b)
PA-parity-transfer result), not a review-round closure — no board run,
readiness stays 95 COMPUTED. See `project-context/SSOT/paper-4p/status.md`
§"Row-16(ii-b) PA-parity-transfer propagation" and
`project-context/peer-reviews/DISPOSITIONS/P4P.md` §"v4P.0.9 → v4P.0.10" for
full detail.

```
paperVersions:bump({
  paperId: "P4P" (slug "paper-4p"),
  version: "v4P.0.10",
  pages: 15,
  date: "2026-09-21",
  sha256: "054b63f8a73902000a0e703da62229ee887f2fc77b0cc027533c2309985f9310",
  md5: "d2d017145530e641ea491c4f5f0909de",
})

activityFeed:add({
  type: "research",
  tags: ["paper-4p", "v4P.0.10", "campaign-2026-09-18"],
  summary: "P4P v4P.0.9->v4P.0.10 (lane L4d, science propagation, not a review round): applied lane bb-LS-ledger16/bb-LS5-row16-finalize's exact PROPAGATION_NOTE.md sentences (P-1..P-5d) verbatim to main.tex -- withdrew the invalid pixel-injection naive-identity tension claim (+0.434/47sigma, 0.038 ratio, ~26% floor, all comparisons between incompatible statistics) and adopted the measured direct dilution bound instead: PA-restoring-reversal epsbar=0.754+/-0.005, D<=0.717+/-0.005, A95^phys>=1.37%, consistent with (not in tension with) the illustrative g=0.398 bridge. Propagated consistently to the three other in-paper mentions (S2.3 forward-ref, Discussion, Conclusions) using only already-cited numbers, no new derivation. Directive-G bundle: paperVersion/date bumped, 4-pass compile 0 undef refs (inline thebibliography, no .bbl dependency), 14->15pp, 1 pre-existing 5.88pt hbox unchanged, 3-way byte-identical PDF mirror (source/site-public/public), 19/19 hyperlink URIs resolved (15 GitHub incl. 2 new row16iib links + 2 Zenodo + 1 HF + 1 site link), arXiv tarball rebuilt and standalone-compile-verified. Readiness unchanged at 95 COMPUTED; directive R2 round budget refreshed by this science decision but no board run in this lane. LS6's second propagation note (row16_tta_2026_09_21/) did not exist at run time -- not included, flagged for a future lane.",
})
```
