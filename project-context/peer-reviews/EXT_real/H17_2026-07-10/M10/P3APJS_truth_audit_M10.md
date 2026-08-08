# P3 (ApJS) M10-EXT truth-audit (v3.1.158-apjs) — verdict-first, source-cited, ledger-first

Raws (read verbatim): `P3APJS_grok_M10.md` (VERDICT: MAJOR REVISIONS, md5 c6e6746dd56d823c2705fa31feb9c2fd)
· `P3APJS_chatgpt_M10.md` (VERDICT: REJECT, md5 76c671b30ecf682101983c144f0ad7ea).
Ledger: `DISPOSITIONS/P3.md` (20 D-ids). Both raws substantively byte-identical to the M8 raws
(same finding set/wording/counts: 268,319 · 2,468 · 77,905 · 86.6% · ~1.3% · 17.8% · 637),
which were adjudicated 0-genuinely-new. Independently re-verified below against current apjs .tex.

## Grok M10 — MAJOR REVISIONS (4 MAJOR + 2 MINOR)

| # | sev | verdict | source-cited one-liner |
|---|-----|---------|------------------------|
| 1 | MAJOR | RE-FLAG DP3-07 (+DP3-01/-09) | Uniform "validated" label unsupported; NEOWISE-419 masking-geometry only. Abstract L1027 states "mixed-validation, not uniform … NEOWISE (419) clears only a masking-geometry QA gate … per-object validity flags carry the gate type throughout." |
| 2 | MAJOR | RE-FLAG DP3-08 + DP3-15 | eROSITA irreproducible axis + pod-lost artifacts break "immutable/recomputable." eROSITA excision L1027/L1687; pod-lost tid→spectrum join = paper's own DP3-15 §II.F L1112 (~1.3% re-pullable). Immutable-release bar = DP3-20 CLOSED. |
| 3 | MAJOR | RE-FLAG DP3-07 | 2,468 (≈0.92×) vs ~141×/~73× multipliers prominence. Abstract L1027 leads with 2,468 like-for-like + "process-volume … not confirmed physical detections." (ledger_match 1.00) |
| 4 | MAJOR | RE-FLAG DP3-01/-09 (+DP3-13) | 5σ gate certifies broad class only; narrow ≥15σ floor. Abstract L1031 + L1146 state the ≥15σ floor verbatim and reflect it in the catalog-grade claim. |
| 5 | MINOR | RE-FLAG DP3-10 | §V fNL+NANOGrav disclaimed non-detections. §V "Secondary Demonstrations," returns null; venue Houston-gated (DP3-16). |
| 6 | MINOR | RE-FLAG DP3-07/-14 | Three-tier fragmentation. Disclosed-by-design three-tier + footnote ♡ L1182; presentation-preference opinion. |

## ChatGPT M10 — REJECT (15 MAJOR + 3 MINOR)

| # | sev | verdict | source-cited one-liner |
|---|-----|---------|------------------------|
| 1 | MAJOR | RE-FLAG DP3-07 + DP3-11 | 268,319/98.7% non-primary/86% TARGET=0 — disclosed abstract L984 "process-volume … not confirmed physical detections … 2,468 like-for-like"; §I reader's-guide. |
| 2 | MAJOR | RE-FLAG DP3-05 + DP3-15 | 26,218 real-tid vs 169,611 hashed vs "100% ZCAT join" — 195,790 primary-coadd ZCAT_PRIMARY reconciliation = DP3-05; ~1.3% ceiling = DP3-15 §II.F. |
| 3 | MAJOR | RE-FLAG DP3-07 + DP3-11 | ~37,000 vs 2,468 recount — 2,468 = disclosed like-for-like benchmark (L992); heterogeneous denominators disclosed. |
| 4 | MAJOR | RE-FLAG DP3-01 + DP3-12 | 5 folds score full 47k / val_loss 1.91≫0.30 — abstract L988 "correlated stability probes, not independent confirmations"; heldout ρ=1.00 on 47k never-trained rows §II.F. |
| 5 | MAJOR | RE-FLAG DP3-12 | Injection into "cleanest 5%" measures sensitivity not FDR/purity — disclosed §II.F + tab:caveats(b). |
| 6 | MAJOR | RE-FLAG DP3-06 + DP3-12 | 0/200 visual → ≤1.5% bound not representative — top-200 score-selected extreme disclosed. |
| 7 | MAJOR | RE-FLAG DP3-13 | Unweighted MSE ignores per-pixel σ/masks — disclosed §VI + tab:caveats; PCA baseline disclosed future work. |
| 8 | MAJOR | RE-FLAG DP3-14 + DP3-09 | 77,905 continuity-slice — footnote ♡ L1182 tabulates all three thresholds + rationale. |
| 9 | MAJOR | RE-FLAG DP3-01 + DP3-08/-09 | NEOWISE mask-geometry pass by construction — abstract "mixed-validation … NEOWISE geometry-QA-by-construction"; train-only-scaler queued. |
| 10 | MAJOR | RE-FLAG DP3-06 | Planck 200 same overlapping 10° patch bank — §planck 152/200-in-training + overlapping-tile inflation disclosed. |
| 11 | MAJOR | RE-FLAG DP3-06 | 48-patch binomial assumes independence — §planck p≈5.5e-4 disclosed "naive binomial"/lower bound. |
| 12 | MAJOR | RE-FLAG DP3-04 + DP3-09 | Union of non-equivalent units — disclosed per-survey gated union, no single-FDR; 37.3M reconciled DP3-03/-04. |
| 13 | MAJOR | RE-FLAG DP3-07 + DP3-09/-11 | 17.8% novelty not footprint-conditioned — abstract L988 "single-sample point estimate, not a survey-wide rate"; §IV L1361 "not a discovery rate." |
| 14 | MAJOR | RE-FLAG DP3-07 | Liang like-for-like denominators — 2,468 = disclosed like-for-like benchmark. |
| 15 | MAJOR | RE-FLAG DP3-08 + DP3-20 | Release-integrity LAMOST/Gaia/eROSITA — DP3-20 CLOSED-BY-RELEASE (tag p3-v3.1.157, 25 files); §III.E-G + tab:provenance. |
| 16 | MAJOR | RE-FLAG DP3-08 + DP3-15 (process tail) | "end-to-end regeneration required" — every provenance failure = paper's own disclosure; end-to-end re-inference = DP3-15 OPEN-COMPUTE. Bar does NOT reset streak. |
| 17 | MAJOR | RE-FLAG DP3-11 + DP3-07/-09 | 637 cross-survey RA-shift 60× — RA-shift + 5″ caveats are the paper's own disclosures. |
| 18 | MAJOR | RE-FLAG DP3-10 | fNL angular-bias-as-3D-bias / 5,384≠40,192 — §V "Secondary Demonstrations," null, App C caveats. |
| 19 | MAJOR | RE-FLAG DP3-10 | NANOGrav uses no catalog output — §V.A secondary null; SCOPE critique not the +4.63σ/+1.14σ arithmetic (CLOSED DP3-18/-19). |
| 20 | MINOR | RE-FLAG DP3-14 + DP3-16 | Figs show obsolete cross-transfer/ACT — retained historical demos, honest disclosure; venue opinion. |
| 21 | MINOR | RE-FLAG DP3-09 + DP3-11 | Terminology non-cross-comparable — disclosed survey-specific (♡ L1182); presentation opinion. |
| 22 | MINOR | RE-FLAG DP3-16 | Re-litigation / column-spec ask — presentation/venue opinion (pattern-066). |

## COUNTS
- genuinely-new reader-visible = **0** (Grok 0 + ChatGPT 0)
- re-flags = **28** (Grok 6 + ChatGPT 22, all mapped to existing D-ids)
- process-nits (riding DP3-15/-16/-20; no standalone reset) = ChatGPT #16, #22 character

## New D-ids: **None.** Every finding maps to DP3-01/-04/-05/-06/-07/-08/-09/-10/-11/-12/-13/-14/-15/-16/-20 with closures verified intact in v3.1.158-apjs.

## VERDICT: CLEAN — 0 genuinely-new. Byte-unchanged maximally-harsh floor (DP3-17 backfire), consistent with M8.
No version bump; v3.1.158-apjs stands; directive_g.sh not warranted. No faked accept, no un-sourced dismissal, no fabrication.
P3 clean-wave streak 3→4; cap 56 HOLDS.
