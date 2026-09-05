# paper-su gate S7 — locating Cai et al. 2009's factor 2 (−35/8 vs −35/16)

**Date:** 2026-09-05 · **Status:** IN PROGRESS (plan header committed first; anti-stall) · **Owner:** S7 lane

## Plan
1. Fetch arXiv e-print sources of 0903.0631 (Cai, Xue, Brandenberger, Zhang) and 1612.02036 (Li, Quintin, Wang, Cai).
2. Transcribe verbatim: Cai's f_NL definition (bispectrum/power-spectrum convention), Eqs. 21, 34–37, and the step giving −35/8.
3. Transcribe Li+2016 Eqs. 3.18, 4.18, 4.19, 5.1 and the c_s = 1 limit.
4. sympy: reproduce each printed intermediate under each factor-2 hypothesis (isoceles 1/2, P vs 2P, symmetry factor, algebra); record which reproduces −35/8.
5. Verdict LOCATED / NOT LOCATED; correct sentence for paper-su and A3M; script + json + manifest; ledger row 17.

## Log
- step 0: plan header committed.
- step 1: sources fetched (0903.0631 → matterbounceng2.tex; 1612.02036 → general_matter_bounce_cosmology.tex); Cai f_NL = (10/3) A/Σk³, ⟨ζζζ⟩=(2π)^7 δ P_ζ² A/Πk³; Cai isoceles −35/8, squeezed A_T=−21/8 k³.
