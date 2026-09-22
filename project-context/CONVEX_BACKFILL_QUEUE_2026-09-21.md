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

---

## L1c (bb-L1c-a3m-row9-r11), 2026-09-21

Paper A3M, v3M.0.26 → v3M.0.27. Science-decision propagation (ledger row 9 /
D-A3-9, Bardeen-potential scheme selection) + gate-S12 correction, not a
review-round closure — no board run yet at this bundle, readiness stays 75
COMPUTED. See `project-context/SSOT/paper-a3m/status.md` §"v3M.0.27
(2026-09-21)" for full detail.

```
paperVersions:bump({
  paperId: "A3M" (slug "paper-a3m"),
  version: "v3M.0.27",
  pages: 21,
  date: "2026-09-21",
  sha256: "3e49f29bdc4bb21ea293db6a2174c4289f1308db2da9b3d96fa1e5192fbbdcef",
  md5: "ea6ebd918399650702ee5a9c81182ab2",
})

activityFeed:add({
  type: "research",
  tags: ["paper-a3m", "v3M.0.27", "campaign-2026-09-18"],
  summary: "A3M v3M.0.26->v3M.0.27 (lane L1c, science propagation, not a review round): applied research/cubic_bounce_transmission/row9_scheme_independence_2026_09_19/PROPAGATION_NOTE.md sentences verbatim -- the Bardeen potential Phi (z-free, 1/H-free, regular at H=0 and at rho+p=0) selects scheme S2 on the Quintin-type background (|lambda_zeta|=0.9699, independently blind-confirmed by a different (Psi,D)/Israel-matching construction); f_NL^after collapses from the two-scheme band [-1.25,-0.50] to the single value -1.25 there, while r_after takes the S2 value ~9.4e2 (was S1's 24.0) -- tensor no-go strengthens from 670x to 2.6e4x BICEP/Keck, both directions propagated together per directive F. Same bundle: gate-S12 general-tilt (n_s=1) correction to Appendix A's monopole and in-in bispectrum formulas (research/theory_audit/psu_gate_S12_translation_trace_2026_09_19.md) -- no headline number changes, since this paper's construction is exactly at eps=3/2 dust where the correction vanishes. Directive I6: both figures checked, neither carries the affected values, no regeneration needed. Directive-G bundle: 4-pass compile 0 undef refs, 20->21pp, one intermediate 116pt table-row overflow from an over-long multicolumn label caught by /latex-audit and fixed (final residual 2.16pt), 3-way byte-identical PDF mirror (source/site-public/public), pages 1/6/13/18/19 visually checked. Readiness unchanged at 75 COMPUTED. This is the intervening science decision directive R2 required after the R9+R10 rounds-stop; R11 INT board dispatched on this exact PDF in the same lane.",
})
```

## Lane `bb-LS7-row23-fate-de` (2026-09-22) — Convex DISABLED, queued not sent

Research/ledger lane only: no paper version changed, so **no `paperVersions:bump`,
no `papers:setReadinessCap`, no `rRounds:create`, no `externalReviews:upsertByLabelDate`.**
One activity event:

```
activityFeed:add({
  type: "research",
  tags: ["open-questions", "ledger-row-23", "cosmic-fate", "dark-energy", "campaign-2026-09-18"],
  summary: "Ledger row 23 answered as a BOUNDARY result (lane bb-LS7-row23-fate-de, research/cosmic_fate_de_2026_09_22/). Pre-registration committed alone before any statistic. Cross-table: the 11 Branch I bounce-compatible DE rows (Classes 1-7 plus Phase-1 subclasses A-F) evaluated against the row-20 turnaround criterion (COSMIC_FATE_MEMO.md Eqs. 2.3-2.5), each decided by a sympy lemma. Intersection = 3 classes: zero-crossing quintessence, zero-crossing k-essence, interacting dark sector with a sustained drain. Lambda, viable f(R) and vacuum sequestering FAIL by the positive-floor lemma; braiding, DHOST and massive gravity stay UNDETERMINED on the bounce axis per Branch I's own verdict and are not promoted. Step 2, at fixed Omega_m = 0.2975 and h*r_d = 101.54 Mpc against DESI DR2 per-bin uncertainties and correlations derived in code from published covariance blocks: a >1 sigma present-day separation from LambdaCDM DOES exist, but only above a threshold in the PRESENT-DAY equation of state -- linear-potential quintessence crosses 1 sigma at w0 = -0.951 / t_c = 53.8 Gyr and the quadratic-top family at w0 = -0.934 / t_c = 13.7 Gyr, i.e. a 0.017 spread in w0 but a factor 3.93 in the turnaround epoch. DESI DR2 therefore constrains how fast dark energy is evolving now; the fate epoch is inferred, not measured, and the inference is potential-family dependent. Row 23 stays an OPEN QUESTION at the row-20 memo's evidence layer: no manuscript claim, no SSOT row, no null changed. Three named gaps recorded and never filled with an invented number (frame-dependence for non-minimally coupled scalars; no citable DR2-era f*sigma8; no citable DR2 central values). Also re-verified symbolically that CPL's rho_DE(a) is positive for every a, so no CPL fit implies a Crunch.",
})
```
