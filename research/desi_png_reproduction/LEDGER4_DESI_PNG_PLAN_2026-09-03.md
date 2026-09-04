# Ledger #4 — Independent reproduction of the DESI DR1 local-PNG constraint from scale-dependent bias

**Date opened:** 2026-09-03 · **Ledger row:** 4 · **Directives:** R1 (ledger-first), Q1 (pure-contribution framing), Q2 (per-experiment manifests)

**Status:** PLAN + first cheap step (in progress)

## 0. Why this item exists

Ledger #1 fixed the lab's flagship matter-contraction value at f_NL^loc = −35/16
= −2.1875 (vs Cai et al. 2009's −35/8 = −4.375). Ledger #3's survey-reach study
(`research/track_a3_multichannel/survey_reach_fnl.py`) established that the
**only** channel that separates those two numbers is the large-scale-structure
survey channel, and that **DESI DR1 reaches 0.16σ** on −35/16. So this item is
explicitly *not* a detection attempt. The deliverable is a **constraint with the
lab's own systematics budget**, an independent check of the published DESI DR1
result, and a posterior statement about −35/16 vs −35/8 overlap — or a reasoned
"not yet" recording the exact blocker.

(Sections 1–6 below: published target, inputs, method, compute, kill/success,
risks. Filled in this session.)
