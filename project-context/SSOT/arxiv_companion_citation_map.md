# arXiv Companion Citation Map — v2 Back-Patch Reference
## Generated: 2026-06-13 (preflight) | Purpose: Step 3 of ARXIV_SUBMISSION_RUNBOOK §4

Every line below must be sed-substituted from `arXiv:XXXX.XXXXX` (or from the cite-key alone, if the .tex uses `\cite{Golden2026PX}` against a `\bibitem{Golden2026PX}` entry that itself contains `arXiv:XXXX.XXXXX`) to the real arXiv ID once IDs are assigned.

**Two-axis patching:**
1. Body `\preprint{arXiv:XXXX.XXXXX}` markers (commented out — uncomment + fill at v2).
2. Bibliography `\bibitem{Golden2026P*}` entries that carry placeholder arXiv IDs — those are auto-resolved by replacing `arXiv:XXXX.XXXXX` strings inside each .tex's embedded bibliography.

---

## Cross-citation table (\cite-keys used in each paper)

| Paper (source) | cite-key | Target paper | .tex line(s) | Notes |
|---|---|---|---|---|
| P1A `arxiv/paper1a_ech_nogo.tex` | `Golden2026P1b` | P1B | 764, 767, 873, 943, 946, 949, 1470, 1490, 1987, 2037, 2080, 2461, 2498, 2500, 2616, 2732, 2872, 2894, 2930 | 19 \cite calls — `\bibitem{Golden2026P1b}` lives in same .tex; patch arXiv id inside that bibitem |
| P1A | `Golden2026P2` | P2 | 742, 764, 869, 871, 2629, 2661, 2675, 2790, 2875 | 9 \cite calls |
| P1A | `Golden2026P3` | P3 | 2470, 2475 | 2 \cite calls (NANOGrav-context) |
| P1A | `Golden2026P4` | P4 | 1436, 1476, 1481, 2014, 2019, 2728, 2738, 2879 | 8 \cite calls |
| P1A | `\preprint{arXiv:XXXX.XXXXX}` self | self | 663 (commented) | uncomment + fill with P1A's own arXiv id |
| P1B `arxiv/paper1b_mcmc_companion.tex` | `Golden2026P1a` | P1A | 1078, 1147, 1194, 2622 | 4 \cite calls |
| P1B | `Golden2026P2` | P2 | 1195 | 1 \cite call |
| P1B | `Golden2026P3` | P3 | 1197 | 1 \cite call |
| P1B | `Golden2026P4` | P4 | 1198, 2692 | 2 \cite calls |
| P1B | `\preprint{arXiv:XXXX.XXXXX}` self | self | 1064 (commented) | self-marker |
| P2 `research/focused_paper_source_integration/02_full_draft.tex` | NONE — `\cite{Golden2026P*}` | — | — | **No companion cite-keys.** Runbook claims "Insert P1A/P1B arXiv IDs at 'DOI inserted at submission' placeholders" — but the only placeholder is **L1047 "DOI inserted at submission" for Zenodo DOI**, not arXiv IDs. **GAP**: signoff says P2 needs P1A/P1B insertion; the source has no such markers. |
| P2 | `\preprint{arXiv:XXXX.XXXXX}` self | self | 17 (commented) | self-marker |
| P3 `pipelines/p3_anomaly_engine/paper3_draft.tex` | NONE — `\cite{Golden2026P*}` | — | — | **No companion cite-keys.** L1145 "DOI inserted at submission" is Zenodo, not arXiv. **GAP**: signoff says "Insert P1A/P1B arXiv IDs into P3 source" but no markers present. |
| P3 | `\preprint{arXiv:XXXX.XXXXX}` self | self | 45 (commented) | self-marker |
| P4 `pipelines/p2_chirality/chirality_catalog_paper.tex` | NONE | — | — | P4 is the most independent paper. No companion cross-cites. No `XXXX.XXXXX` markers. No `\preprint` line. |
| P5 `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` | `golden_chirality_2026` | P4 | 402, 620, 659, 2493 | 4 \cite calls; bibitem at L3630 |
| P5 | inline "companion paper (Paper IV/II)" | P4, P2 | 3634, 3639 | bibitem free-text — patch arXiv id inline |
| P5 | `\preprint{arXiv:XXXX.XXXXX}` | self | NONE present | **GAP**: P5 has no self-preprint marker — verify runbook expects one or not |

---

## Patch commands (Step 3 — after IDs assigned)

After arXiv assigns 6 IDs, fill the table at the top of the runbook then run **per-paper sed**. Example template (replace `2506.NNNNN` with real IDs):

```bash
P1A_ID="2506.NNNNN"
P1B_ID="2506.NNNNN"
P2_ID="2506.NNNNN"
P3_ID="2506.NNNNN"
P4_ID="2506.NNNNN"
P5_ID="2506.NNNNN"

# P1A: patch self-preprint, then any Golden2026P* bibitems
sed -i.bak "s|%\\\\preprint{arXiv:XXXX\\.XXXXX}|\\\\preprint{arXiv:${P1A_ID}}|" arxiv/paper1a_ech_nogo.tex
sed -i.bak "/\\\\bibitem{Golden2026P1b}/,/^$/ s|arXiv:XXXX\\.XXXXX|arXiv:${P1B_ID}|" arxiv/paper1a_ech_nogo.tex
sed -i.bak "/\\\\bibitem{Golden2026P2}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P2_ID}|"  arxiv/paper1a_ech_nogo.tex
sed -i.bak "/\\\\bibitem{Golden2026P3}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P3_ID}|"  arxiv/paper1a_ech_nogo.tex
sed -i.bak "/\\\\bibitem{Golden2026P4}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P4_ID}|"  arxiv/paper1a_ech_nogo.tex

# P1B: parallel structure
sed -i.bak "s|%\\\\preprint{arXiv:XXXX\\.XXXXX}|\\\\preprint{arXiv:${P1B_ID}}|" arxiv/paper1b_mcmc_companion.tex
sed -i.bak "/\\\\bibitem{Golden2026P1a}/,/^$/ s|arXiv:XXXX\\.XXXXX|arXiv:${P1A_ID}|" arxiv/paper1b_mcmc_companion.tex
sed -i.bak "/\\\\bibitem{Golden2026P2}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P2_ID}|"  arxiv/paper1b_mcmc_companion.tex
sed -i.bak "/\\\\bibitem{Golden2026P3}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P3_ID}|"  arxiv/paper1b_mcmc_companion.tex
sed -i.bak "/\\\\bibitem{Golden2026P4}/,/^$/  s|arXiv:XXXX\\.XXXXX|arXiv:${P4_ID}|"  arxiv/paper1b_mcmc_companion.tex

# P2: only self-preprint
sed -i.bak "s|%\\\\preprint{arXiv:XXXX\\.XXXXX}|\\\\preprint{arXiv:${P2_ID}}|" research/focused_paper_source_integration/02_full_draft.tex

# P3: only self-preprint
sed -i.bak "s|%\\\\preprint{arXiv:XXXX\\.XXXXX}|\\\\preprint{arXiv:${P3_ID}}|" pipelines/p3_anomaly_engine/paper3_draft.tex

# P4: nothing to patch (no XXXX markers in tarball)

# P5: golden_chirality_2026 bibitem at L3630 carries P4 metadata
sed -i.bak "/\\\\bibitem{golden_chirality_2026}/,/^$/ s|in preparation|arXiv:${P4_ID}|" pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex
# Also free-text "companion paper" bibitems at L3634, L3639:
# (manual or targeted sed needed — companion paper Paper IV → arXiv:${P4_ID}; Paper II → arXiv:${P2_ID})
```

---

## Critical gaps surfaced by this map

1. **P2 + P3 lack `\cite{Golden2026P*}` cross-citations.** The runbook + signoff package both claim P2 and P3 need P1A/P1B arXiv IDs inserted, but the source .tex has no such markers. Either (a) the runbook is wrong and P2/P3 are fully independent (likely), or (b) Houston intended to add cross-citations and never did. **Action: confirm with Houston before v2 patch.**
2. **P5's `golden_chirality_2026` bibitem says "in preparation"** rather than `arXiv:XXXX.XXXXX`. Patching this needs explicit sed for the bibitem free-text rather than a placeholder substitution. Documented above.
3. **P5 has no `\preprint{arXiv:XXXX.XXXXX}` self-marker.** All other 5 papers have it (commented). Either P5 needs one added pre-submission or the v2 patch step skips P5's self-preprint.
4. **P4 has zero placeholders in the .tex** — confirmed clean independent paper, no v2 patch needed for P4.

Total v2-patch surface:
- P1A: 1 self-preprint uncomment + 4 bibitem arXiv ID inserts
- P1B: 1 self-preprint uncomment + 4 bibitem arXiv ID inserts
- P2:  1 self-preprint uncomment
- P3:  1 self-preprint uncomment
- P4:  0 patches
- P5:  1 bibitem free-text patch + (optional) self-preprint add

---

*Generated by ARXIV_PREFLIGHT_CHECKLIST_2026-06-13.md from grep over 6 source .tex.*
