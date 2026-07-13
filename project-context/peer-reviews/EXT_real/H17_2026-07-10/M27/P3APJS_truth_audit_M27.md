# P3 (ApJS variant) — M27-EXT truth-audit

**Date:** 2026-07-13
**Paper:** P3 ApJS variant `pipelines/p3_anomaly_engine/paper3_apjs.tex`
**Reviewed version:** v3.1.159-apjs — **byte-unchanged since M24** (no `.tex` edit since commit `e24b42a9`; this is a fresh Grok re-read of the same content the DP3-21 DAS fix landed in).
**Raw (read verbatim before any verdict):**
- `EXT_real/H17_2026-07-10/M27/P3APJS_grok_M27.md` — **VERDICT: MAJOR REVISIONS** (4 MAJOR + 3 MINOR)

Only the Grok leg ran this round. ChatGPT M26 P4/P1U legs were DEFERRED-ratelimit
(daily cap ~16 legs M20–M26); no ChatGPT/Gemini P3APJS leg placed for M27. Grok
verdict recorded to Convex (`major-revisions`, cap recomputed 56 = Grok MAJOR 6 +
ChatGPT REJECT 0 + Gemini REJECT 0 + 50). No faked accept.

## CRITICAL CHECK — did the DP3-21 DAS fix stay held? → **HELD**
Signature-grep of the M27 raw for the DP3-21 contradiction (`feature-space score` on
the Gaia block / `excluded from every count` for LAMOST / internal DAS contradiction):
**NONE.** Grok does not re-raise the self-consistency defect the fix closed. Fix HELD.

## Verdict matrix (EXT, from raw VERDICT line)
| Reviewer | Verdict | MAJOR | MINOR |
|----------|---------|-------|-------|
| Grok EXT | MAJOR REVISIONS | 4 | 3 |
| ChatGPT EXT | (no M27 leg — daily rate-limit; carry M24 REJECT) | — | — |
| Gemini EXT | (no M27 leg — browser hard-throttled; carry REJECT) | — | — |

## Per-finding adjudication — Grok (4 MAJOR + 3 MINOR; all source-cited re-flags, 0 genuinely-new)

- **G1 [MAJOR]** Abstract/§1/§3 "validated catalog-grade 268,519" vs process-volume
  candidates, ~98.7% DESI on non-science-target spectra, only 2,468 on validated
  science targets → **DP3-07** (process-volume vs validated framing disclosed abstract
  first sentence + §I reader's guide) + **DP3-09** (heterogeneous per-survey gates).
  The 98.7% / 2,468 figures are the paper's OWN disclosed numbers.
- **G2 [MAJOR]** §3.5 eROSITA irreproducible axis (fails all 16 monotone rescalings +
  IsolationForest retrains) + §3.7 Gaia synthetic-placeholder tier; "remove entirely"
  → **DP3-08** (both excised from every count, §erosita/§gaia + `tab:provenance`) +
  **DP3-15/-16** (disclosed reproducibility ceiling). The "separately released" member
  lists are already outside every headline count; disclosure ≠ inflation.
- **G3 [MAJOR]** §2.2/§2.4/§6.4(i) full per-object re-inference of the 22.5 M DESI
  catalog blocked — raw native-score parquets on an exited pod, absent from committed
  tree/HF → **DP3-15 OPEN-COMPUTE** (the disclosed ~1.3% structural reproducibility
  ceiling). This is the compute-gated item in `SSOT/compute-to-accept-queue.md`
  (held-out end-to-end re-inference = a real RunPod run, Houston-gated). **NOT editable;
  not faked.** Disclosed honestly at its structural bound.
- **G4 [MAJOR]** §2.4/Table 2 validation not uniform — DESI/SDSS/Planck pass
  injection-recovery, NEOWISE passes geometry-QA mask only, aggregated into one
  headline → **DP3-07/-14** (four-tier structure + per-survey gate heterogeneity
  disclosed; NEOWISE geometry-only gate stated explicitly in §II/`tab:provenance`).
- **G5 [MINOR]** §3.1/Table 3 Liang "≈0.92×" like-for-like without explicit
  sample-size/selection-function comparison → **DP3-13/-10** (Liang benchmark
  disposition; the 2,468 science-target subset is the like-for-like comparator).
- **G6 [MINOR]** §5 multi-tracer fNL + NANOGrav null "secondary demonstrations" add
  length; move to appendix/remove → **OPINION** (editorial placement preference; the
  sections are already labeled secondary and return honest null results). Not a defect.
- **G7 [MINOR]** Reads as internal technical report (pipeline paths, committed JSON,
  pod-provenance notes) not self-contained ApJS submission → **DP3-20-adjacent**
  (provenance-transparency disclosure; the self-contained core statistics are in-text).
  Presentation nit; recurring across M17→M24.

## Disposition
**0 genuinely-new real findings.** Every Grok M27 finding fingerprint-matches a standing
DP3 disposition (DP3-07/-08/-09/-10/-13/-14/-15/-16/-20) or is an editorial OPINION.
The single true barrier (G3 = DP3-15 full re-inference) is **compute-gated**, not
editable — it needs a real held-out end-to-end re-inference pod run, which stays
Houston-gated per directive-L / `compute-to-accept-queue.md`. **No paper edit is due**
(content byte-unchanged; nothing new to fix). DP3-21 DAS fix stays HELD.

**Clean-wave streak: P3 1 → 2** (M24 was 0→1; M27 is a second 0-genuinely-new P3 read
on the same v3.1.159-apjs). Cap HOLDS **56**. No bump, no directive_g.sh (no `.tex`
change). No faked accept, no un-sourced dismissal, no fabrication.
