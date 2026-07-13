# P3-ApJS M39-EXT truth-audit (2026-07-13, vs byte-unchanged v3.1.159-apjs)

**Legs:** Grok EXT = MAJOR REVISIONS (1 MAJOR / 4 MINOR — labels bare on site);
ChatGPT EXT = REJECT (13 MAJOR / 1 MINOR). Both raws read verbatim before any
verdict; screenshots present (P3APJS_grok_M39.png, P3APJS_chatgpt_M39.png).

## Provenance — CONFIRMED (genuine P3-ApJS reads on both legs)
Signature-grep both raws for P3 anomaly signatures (268,519 / DESI / SPARCL /
NEOWISE / Planck-top-200 / LAMOST / eROSITA / NANOGrav / fNL / 77,905 / 195,829):
PRESENT throughout both. P5 void-chirality signatures (DESIVAST / VoidFinder /
chirality / T-Web / 2.26): 0. Both carry the `ext_P3APJS_M39` submission tag.
→ genuine P3-ApJS reviews, NOT the M32 (P1U-under-P3) / M34 (P5-under-P3)
wrong-paper misfile class.

## DP3-21 DAS self-contradiction — STAYS ABSENT (fix HELD)
The live DAS (paper3_apjs.tex L1710) matches the v3.1.159 DP3-21 fix EXACTLY:
"the released LAMOST DR10 block carries per-object canonical-S scores but is a
failed-exploratory tier … included in the inclusive 377,482 total but *excluded*
from the 268,519 validated catalog-grade headline" and "the synthetic Gaia DR3
tier (500 objects) is *excised* — removed from the released catalog product and
from every count (§sec:gaia), so no Gaia block is released." The DAS-vs-body
self-inconsistency that DEFINED DP3-21 is GONE.

ChatGPT M39 #2 DOES contain Gaia/LAMOST/pinned-commit wording, but it is a
DIFFERENT claim: it asserts the HuggingFace **release manifest/files** conflict
with the manuscript ("a Gaia file remains present," "manifest says no LAMOST
per-object table," "metadata inconsistent about the pinned commit"). That is the
release-integrity / end-to-end-reproducibility class — DP3-15 (bounded ~1.3%
re-pull ceiling, pod-lost linkage) + DP3-20 (immutable-release, CLOSED-BY-RELEASE
at pinned tag p3-v3.1.157) + DP3-08 (Gaia excised from every count) — NOT the
DP3-21 DAS-vs-body internal contradiction. The DAS itself now explicitly states
"the machine-readable RELEASE_MANIFEST.json enumerates exactly the files that are
released." Disclosed release class, no new editable defect. DP3-21 HELD.

## Ledger disposition — 0 genuinely-new (both legs)

### Grok EXT (ledger_match 5/7 auto; 2 UNMATCHED = header fragments, not findings)
- MAJOR #1 (§2.2/§6.4(i)): "full count directly recomputable" not supported for
  DESI tier / 86.6% hashed tids / ~1.3% re-pullable / raw parquets on exited pod
  → **DP3-15** (bounded re-pull ceiling, paper's OWN 13.4%/86.6%/1.3% numbers).
- MAJOR "catalog-grade" three-tier / non-uniform validation / 141×,73× overstate
  → **DP3-07** (process-volume disclosed abstract L984) + **DP3-09** (heterogeneous
  gates disclosed) + **DP3-01** (NEOWISE by-construction).
- MINOR #3 eROSITA 0.259 irreproducible / 16 rescalings / ρ=−0.10 / top-298
  → **DP3-08** (eROSITA excised, provenance disclosed) + **DP3-15**.
- MINOR #4 DESI 2,468/190,015 selection-function not quantified
  → **DP3-07** + **DP3-11** (98.7% non-primary disclosed §I reader's guide).
- MINOR #5 full-sample scalers / NEOWISE train-split-only "queued"
  → **DP3-13** (preprocessing disclosed) + **DP3-15** OPEN-COMPUTE (train-split
  refit is pod-gated, NOT an edit).
- UNMATCHED #1 "REVISIONS ISSUES:" and #7 "caveats." = parse fragments of the
  verdict/one-sentence lines, NOT findings.
- Grok's own closing sentence AFFIRMS the disclosed limitations are "scope
  conditions rather than minor caveats" — the disclosure stance, not a new defect.

### ChatGPT EXT (ledger_match 11/16 auto; 5 UNMATCHED = verbose §-restatements)
- #1 268,519 not "validated real" / no FDR / no negative control → **DP3-07/-11/-12**.
- #2 irreproducible provenance / manifest-vs-paper Gaia+LAMOST+pinned-commit
  → **DP3-15/-20/-08** (release class; DP3-21 DAS-contradiction ABSENT, see above).
- #3 77,905 SDSS arbitrary continuity-slice count → **DP3-06/-14** (footnote ♡
  discloses fixed-size continuity slice).
- #4 DESI like-for-like invalid / 98.7% no science-bit vs 98.8% Redrock
  → **DP3-07/-11** (both numbers disclosed §III.C honestly).
- #5 S has no calibrated statistical meaning / 0.87%>S5 not 5σ → **DP3-09/-12**.
- #6 held-out tests fail val-loss gate / not independent → **DP3-01/-13** (closed;
  one production gate + two correlated fold probes, disclosed).
- #7 injection tests not a common protocol / incompatible "5σ" (UNMATCHED-auto)
  → **DP3-09** (per-survey gate-type matrix disclosed Fig caption) + **DP3-12**.
- #8 Planck spatial leakage / top-200 not top-1% / 5″ dedup meaningless
  → **DP3-06** (200=0.10% clarified) + **DP3-11**.
- #9 NEOWISE mask test = by-construction (UNMATCHED-auto) → **DP3-01/-13**
  (§III.8 discloses "by construction, not a detector-sensitivity test").
- #10 17.8% novelty unsupported (UNMATCHED-auto) → **DP3-07/-09** (catalog-
  unmatched-fraction framing disclosed).
- #11 5″ dedup inconsistent across surveys (UNMATCHED-auto) → **DP3-11**.
- #12 cross-transfer vs native SDSS conflation → **DP3-14** (footnote ♡).
- #13 37.3M / 377,482 aggregate incompatible quantities → **DP3-03/-04**
  (footnote ⊗ reconciles; disclosed).
- #14 §5 fNL forecast not valid / σ(fNL)≈5.67 vs 7.15 vs 16.85 (UNMATCHED-auto)
  → **DP3-10/-19** (§V "Secondary Demonstrations" null, App-C caveats disclosed).
- #15 §5.1 NANOGrav unrelated to catalog → **DP3-18/-10/-19**.
- MINOR #16 abstract long / superseded figures / shorten → **DP3-14/-16**
  (venue/presentation OPINION, referee-variance).

Item set is IDENTICAL to the M24/M27/M36 ChatGPT REJECT set = directive-H
maximally-harsh ApJS floor (DP3-17, pattern-066 backfire). Every finding is a
source-cited re-flag of already-closed/disclosed content.

## Verdict
**0 genuinely-new findings, both legs.** DP3-21 DAS stays absent (fix HELD).
clean-wave streak P3 **4→5** (directive-K; M36 was 3→4). cap **HOLDS 56**
(Grok MAJOR 6 + ChatGPT REJECT 0 + Gemini REJECT 0 + 50; verdict words unchanged).
STRATEGIC: DP3-15 end-to-end re-inference already run to its structural ceiling
(commit 2c52a1d2) — P3's residual is 100% Houston-gated (venue word / archive
re-pull); NO compute lever remains. No bump (byte-unchanged); directive_g.sh not
run (no .tex edit). No faked accept, no un-sourced dismissal, no fabrication.
