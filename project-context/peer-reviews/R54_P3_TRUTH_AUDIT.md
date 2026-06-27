# R54 P3 Truth Audit — Convergence Confirmation

- **Date:** 2026-06-26
- **Paper:** P3 (Multi-Survey Spectral Anomaly Catalog), `pipelines/p3_anomaly_engine/paper3_draft.tex` (canonical, NOT arxiv stub)
- **Compiled PDF:** `/tmp/R54_P3/paper3_draft.pdf` (29pp pre-fix → 30pp post-fix); 0 undefined, 0 overfull hbox.
- **Legs:** native-PDF review returned Gemini (gpt/gemini), Grok, OpenAI (gpt-5, reasoning_effort=high); FAILED: Perplexity (fallback), Claude/Anthropic (no file emitted). Plus own Opus read + chain recompute.

## Net verdict: NOT-yet-converged — ONE genuine MAJOR found and closed (verified).

The headline science is sound and every headline number recomputes exactly
(141×/100×/73× scale; dedup histogram 9,553 clusters → 10,213 collapsed → 378,280;
α_jk 0.19/0.65=0.29σ; σ_fNL envelope [3.92,8.98]; Cramér V=0.0064; Wilson CIs;
γ shifts +1.13σ/+4.61σ; fiducial Savage-Dickey B_MB/SMBHB=7137.6→7.14e3). Wilson-CI
and Fig.3/Fig.6 caption fixes from R52/R53 verified present — not re-opened.

## VERIFIED DO-NOW closed (MAJOR, non-headline)

**Table IX (`tab:bf_robustness`) — fabricated non-fiducial prior-robustness rows.**

The 3 non-fiducial rows ([0,5],[1,6],[2,5]), added in EXT14–16 without a backing
computation, asserted B_SMBHB/free "varies ~40×" and the narrowest prior [2,5]
gives B_MB/SMBHB ≈ 200. Recomputing the genuine prior-reweighted 1-D Savage-Dickey
on the COMMITTED chain (`chain_real_freespec.npy`, 320k samples) — method validated
because the fiducial row reproduces the committed `savage_dickey_2026-05-29.json`
EXACTLY (3.2276 / 4.5219e-4 / 7137.6) — gives:

| γ prior | B_MB/free (paper→TRUE) | B_SMBHB/free (paper→TRUE) | B_MB/SMBHB (paper→TRUE) |
|---|---|---|---|
| [0,7] | 3.23 → 3.23 ✓ | 4.52e-4 → 4.52e-4 ✓ | 7.14e3 → 7.14e3 ✓ |
| [0,5] | 3.23 → **2.31** | 6.1e-3 → **3.23e-4** | 5.3e2 → **7.14e3** |
| [1,6] | 3.25 → **2.31** | 4.5e-4 → **3.20e-4** | 7.2e3 → **7.24e3** |
| [2,5] | 3.24 → **1.47** | 1.7e-2 → **1.69e-4** | 1.9e2 → **8.69e3** |

The paper's narrative was inverted: the **ratio** B_MB/SMBHB = p(3.0|data)/p(4.33|data)
is in fact the MOST prior-stable quantity (the 1/Δγ width factor cancels), staying
7.1e3–8.7e3 — always "decisive" — across every prior. The individual B_x/free entries
shrink with prior width through the 1/Δγ denominator, not via tail sensitivity.

**Closure:** corrected the 3 table rows; rewrote the §-opening clause, the lead
paragraph, and the table footnote narrative; provenance artifact
`pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/bf_prior_robustness_R54.json`.
Headline (fiducial 7.14e3, decisive only vs idealized circular-orbit SMBHB) unchanged.
Recompiled ×3 (0 undef, 0 overfull); table visually verified within-column.

## Vendor findings — all STALE / OUT-OF-SCOPE / TRULY-BLOCKED (no new genuine defect)

- **OpenAI** ESSENTIAL (Gaia/NEOWISE scaler-leakage): known disclosed limitation;
  the train-split refit needs pod-side feature tables (GPU-blocked, same class as the
  non-blocking DESI injection). Explicitly recomputed and ACCEPTED the PTA Savage-Dickey
  "as quoted" — i.e. MISSED the fabrication (native-PDF vendors cannot run the chain).
- **Gemini** "catalog-grade vs exploratory contradiction": already disclosed framing —
  269,317 is the 6-way-dedup catalog-grade tier carrying per-object exploratory validity
  flags for Gaia/eROSITA; LAMOST is a separate excluded exploratory tier (L724, L1165).
- **Grok** M1 length/scope (catalog-class, size not a defect), M2 LAMOST bias, M3 Fig.3
  axis, M4 novelty — all previously closed; STALE.

## Convergence statement

P3 is **converged after this R54 closure**: a single genuine MAJOR (the fabricated
BF-robustness rows) remained — invisible to all native-PDF vendors and catchable only
by recomputing on the committed chain — and is now corrected against ground truth.
No other genuine BLOCKER/MAJOR/MINOR survives; all remaining vendor items are STALE,
size-of-catalog, or GPU-blocked. Headline results unaffected.
