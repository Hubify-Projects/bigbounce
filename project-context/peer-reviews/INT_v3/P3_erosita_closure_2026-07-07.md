# P3 — eROSITA reproducibility MAJOR: REAL-SCIENCE closure (2026-07-07)

**Paper:** `pipelines/p3_anomaly_engine/paper3_draft.tex`
**Version:** v3.1.141 → **v3.1.142**
**Standing finding (all 3 EXT reviewers + OpenAI, every round):** *"the eROSITA
anomaly-score axis is disclosed as irreproducible/non-monotone yet its objects
remain in the headline totals."*

---

## STEP 1 — Root cause

The eROSITA production scoring run applied an **undocumented post-hoc rescaling**
that placed the top-298 knee at `0.259` on an axis whose code was never committed.
The committed audit (`r24conf_erosita_axis_sweep.py` → `.json`) established:

- `0.259` reproduces on **none** of 16 monotone rescalings of the committed raw
  reconstruction score, nor on 3 retrained IsolationForest axes.
- The production Table-IV `S_BigAE` values are **non-monotone** in the committed
  raw score (Spearman ρ = −0.10).

⇒ The **score axis is irreproducible as a matter of provenance** (lost production
rescaling code), not merely unidentified. **Path A (regenerate the axis) is not
achievable.**

The prior fix (v3.1.133) committed `erosita_membership_reproduce.py`, which proves
the *selection* (top-298 by committed raw score, `S_raw ≥ 3.4119`) is **rank-scale-
invariant** and therefore reproducible. Verified here: the script runs
deterministically, `min_released_raw_score == rank-298 threshold == 3.4119`, and the
298-member SET + rank order are invariant across all 8 monotone transforms.

**But the reviewers' MAJOR was never about the selection** — it was that the 298
eROSITA objects were **still folded into the inclusive headline total (377,780)**
via the per-survey sum (387,993) and the Table-I "Path-C unique (primary)" row. An
irreproducible-axis tier still touched a headline number. The rank-invariance
recipe is a correct but subtle defense reviewers kept re-flagging.

## STEP 2 — Path taken: **B (clean excision from all headline totals)**

eROSITA is now **excised from EVERY count in the paper**, exactly as the synthetic
Gaia tier already was, and released **separately** only as the reproducible top-298
membership-list addendum. Mechanism: eROSITA formed **exactly 298 isolated
singleton clusters** in the 5″ dedup (zero cross-matches with any survey, verified
in `outputs/sixway_dedup_artifact.json`), so excision subtracts **exactly 298**
with zero dedup recomputation — identical to the Gaia-500 excision. This is the
stronger paper: every remaining headline object is now on a fully reproducible axis.

### Every number that changed (old → new)

| Quantity | Old | New |
|---|---|---|
| Per-survey detection sum | 387,993 | **387,695** |
| Inclusive Path-C unique headline | 377,780 | **377,482** |
| Point-source tier | 377,580 | **377,282** |
| ACT-with variant | 377,980 | **377,682** (input 388,193→387,895) |
| Radius sweep {3″,5″,7″} | 378,104 / 377,780 / 377,645 | **377,806 / 377,482 / 377,347** |
| Compression % | 2.629% | **2.634%** |
| Collapse counts (637 / 9,576 / 10,213) | — | **UNCHANGED** (eROSITA all singletons) |
| Validated catalog-grade headline | 268,519 | **268,519 (UNCHANGED — eROSITA was never in it)** |
| ~141× / ~73× multipliers | (on 377,780) | (on 377,482 = 140.6× — unchanged) |

Excision chain now stated explicitly in footnote ‖: **378,280 → 377,780 → 377,482**
(Gaia −500, eROSITA −298).

### Sites edited (all live, non-comment)

Abstract (858, 862, 864), Intro (885), three-tier block (972 tier-2 rewritten to
"separately-released, excluded from all counts"; 973 tier-3), per-survey summary
(975, 981), Table I Path-C row (1005), footnotes ‖/¶ (1025, 1028) with the exact
298-singleton arithmetic, LAMOST-lesson footnote ♠ (1033), Gaia section (1198),
spatial-uniformity χ² (1268), 6-way dedup (1289), radius sweep (1291), Conclusions
"Scale" (1463), data availability (1491), ACT appendix (1722), and the **§erosita
opening** now leads with the excision decision.

### χ² — honest handling (NOT fabricated)

The spatial-uniformity χ² = 376,713 was computed (pod-side,
`r24conf_pod_session_batch.json`) on the **full inclusive object set that still
included the 500 Gaia + 298 eROSITA** (it derives from the `7way_headline`
n_objects = 378,280 block — it was **already stale** vs the shipped 377,780). The
pod-side LAMOST positions (~113k) are **not committed locally**, so an exact
recompute of χ² for the 377,482 set is **not possible here without fabricating**.
Handled honestly: the χ² sentence is reframed to state it was computed on the full
inclusive set incl. the now-excised 798 objects (0.21%, incl. one LMC-concentrated
eROSITA pixel), that this does not change the qualitative footprint-dominated
conclusion, and that it is reported only as a raw order-of-magnitude diagnostic —
**no new χ² value invented.** (eROSITA does spike one N_side=64 pixel at 57 objects;
Gaia is spatially diffuse.) A full recompute is a follow-up when pod-side positions
are restaged.

## STEP 3 — directive-G PDF hygiene: **PARTIAL — recompile BLOCKED in this env**

- ✅ `.tex` version bumped v3.1.141 → **v3.1.142**; date/timestamp = July 7, 2026.
- ✅ Full changelog block added to the `.tex` header.
- ✅ Arithmetic audit: all counts internally consistent (script-verified).
- ✅ LaTeX brace / math-delimiter balance verified; all new `\artifact{}` targets exist.
- ✅ Figure inventory checked — **no figure PNG/PDF embeds 377,780 / 377,580**
  (generator scripts grepped clean); no figure regeneration required (directive I6).
- ⛔ **`pdflatex` / any LaTeX engine is NOT installed on this machine** (no MacTeX,
  no texlive, no tlmgr, no tectonic). **The recompile, PDF re-mirror to all served
  paths, Convex `paperVersions:bump` with real md5/pages, and the three-way md5
  check CANNOT be completed in this environment.**

### Remaining (must run where LaTeX exists)

1. `pdflatex → bibtex → pdflatex → pdflatex` on `paper3_draft.tex` (expect 0 undef-refs).
2. `/latex-audit` (overflow / column-escape check).
3. Mirror new PDF byte-identical to all served paths (site/public/papers/ versioned
   + aliases, public/papers/, source dir).
4. Convex `paperVersions:bump` paper-3 with new md5/pages; three-way md5 check
   (compile == served == Convex); page-1 visual spot-check shows v3.1.142 + date.
5. Rebuild standalone-verified arXiv tarball + metadata + checklist.
6. reviewTimeline.ts entry + commit/push.

## Integrity

NEVER fabricated. Every changed count is the exact arithmetic consequence of
removing 298 verified-singleton objects. The score axis was **not** faked
reproducible — it is honestly excised because it genuinely cannot be regenerated.
The χ² was **not** given an invented new value.
