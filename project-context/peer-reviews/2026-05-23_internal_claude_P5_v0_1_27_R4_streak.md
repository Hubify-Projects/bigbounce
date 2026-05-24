# P5 v0.1.27 — R4 internal Claude peer review (adversarial 3rd-streak verification)

**Date:** 2026-05-23
**Reviewer:** internal claude (adversarial methodology + physics, 4th-pass)
**Paper:** `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` v0.1.27-2026-05-23 (29 pp, 1492 lines)
**Prior rounds:** R1 (v0.1.22) → fixes → R2 (v0.1.25) 0B/0M → R3 (v0.1.26) 0B/0M → **R4 (v0.1.27) target: 3rd consecutive clean round per AGENT_RULES §4.4.1**

---

## Part A — Verification of v0.1.26 → v0.1.27 corrections

### Correction 1 — Pearson-r robustness-grid claim (fire-#57 honest-correction)
**v0.1.27 claim (L1245–1251):** "across the full 3×3 grid of NSIDE ∈ {16,32,64} and spiral-count cuts ∈ {100,200,500}, all cells return |r|<0.11 with p>0.10, none statistically significant; the headline NSIDE=32 cut=200 result r=+0.006 is consistent with this range. Companion artifact: voids_vs_chirality_robustness_grid.json."

**Audit against `voids_vs_chirality_robustness_grid.json`:** the artifact contains **7 cells, not 9**: `NSIDE=16,cut={100,200,500}` + `NSIDE=32,cut={100,200,500}` + `NSIDE=64,cut=100`. The `NSIDE=64,cut=200` and `NSIDE=64,cut=500` cells are absent.

For the 7 present cells:
| cell | r | p | n_pix | |
|---|---|---|---|---|
| NSIDE=16,cut=100 | −0.0916 | 0.119 | 291 | |r|<0.11 ✓, p>0.10 ✓ |
| NSIDE=16,cut=200 | −0.0747 | 0.213 | 280 | ✓ ✓ |
| NSIDE=16,cut=500 | −0.1011 | 0.107 | 255 | ✓ ✓ (max |r|, min p) |
| NSIDE=32,cut=100 | −0.0142 | 0.683 | 834 | ✓ ✓ |
| NSIDE=32,cut=200 | +0.0057 | 0.879 | 727 | ✓ ✓ (headline) |
| NSIDE=32,cut=500 | −0.0302 | 0.894 | 22  | ✓ ✓ (low n) |
| NSIDE=64,cut=100 | +0.0354 | 0.467 | 426 | ✓ ✓ |

The **numerical bound holds** for every cell present (max |r|=0.101, min p=0.107). But the **structural claim "full 3×3 grid"/"all cells" is false**: two cells are missing from the artifact. The headline NSIDE=32 r=+0.006 cross-check is artifact-correct. **PARTIAL PASS** — the headline is honest; the "3×3 / 9-cell" framing is not. See **Finding #N8 (MAJOR)** below.

### Correction 2 — R3 #N6 blank-line fix (§VI.A L451)
**v0.1.27 L451–456:** `\end{figure}` (L454) followed by blank line (L455) then `The negative $\sigma$ values...` (L456). **PASS.** Blank line is present; LaTeX paragraph break will render correctly.

### Correction 3 — R3 #N7 "fourth catalog-anchored cross-check" rewording (§VII.D L1141 → now L1143)
**v0.1.27 L1143:** "This is **an additional catalog-anchored cross-check on the sky-position axis, complementary to the abstract's (i)--(iv) enumeration**, showing that the catalog-level −5σ headline tracks survey-mask geometry rather than environment density..."

Verified against abstract (i)–(iv) enumeration at L114–135. The reworded text correctly frames this §VII.D analysis as additional to (not the same as) the four enumerated cross-checks. **PASS.** No double-counting; no contradiction with abstract.

---

## Part B — Findings introduced in v0.1.26 → v0.1.27 surface (R4 new)

### Finding #N8 — Robustness grid is 7 cells, paper claims 9 (MAJOR)

**Severity:** MAJOR
**Location:** §VII.D L1245–1251 (cosmic-web cross-check paragraph)
**Class:** numerical-claim / artifact-mismatch (same class as the fire-#57 issue the v0.1.27 edit was meant to close)

**The claim:** "across the **full 3×3 grid** of NSIDE ∈ {16,32,64} and spiral-count cuts ∈ {100,200,500}, **all cells** return |r|<0.11 with p>0.10"

**The artifact:** `pipelines/p5_desi_chirality/results/analysis_cosmic_web/voids_vs_chirality_robustness_grid.json` contains 7 cells. `NSIDE=64,cut=200` and `NSIDE=64,cut=500` are absent. Confirmed via `python3 -c 'import json; print(len(json.load(open("...json"))["cells"]))'` → `7`.

**Why MAJOR, not MINOR:** the same reviewer (Houston, via fire-#57) just caught the previous version's "|r|<0.05 at all 9 cells" claim being wrong because the artifact didn't support it. The v0.1.27 correction tightened the |r|/p bounds but kept the "3×3 / full grid" structural framing — which is also unsupported. This is the exact failure mode AGENT_RULES §4.4.1 is supposed to gate against: a numerical claim that doesn't match the on-disk JSON. The acceptable fixes are:

1. **Regenerate the missing two cells** in the JSON (add NSIDE=64,cut=200 and cut=500; both likely have very low n_pix_both — note NSIDE=32,cut=500 already has only n=22 — but include them with whatever |r|/p they yield, even if "insufficient overlap" is the honest result).
2. **OR honestly rewrite** the claim to: "across the **7 of 9 grid cells** where pixel overlap was sufficient to compute Pearson r (the NSIDE=64 / cut≥200 cells were excluded for n_pix_both < threshold), all return |r|<0.11 with p>0.10..." plus a brief note in the JSON `method` field explaining the exclusion.

Either fix removes the artifact-mismatch. Option 1 is preferred (fully populated 9-cell grid) and is the option AGENT_RULES §4.4.1 implicitly favors.

**Pass criterion:** paper claim must match artifact exactly. Currently it does not.

---

## Part C — Findings on 4th-pass careful re-read (not v0.1.27-introduced)

None new at BLOCKER or MAJOR severity that were not surfaced in R1–R3. The (i)–(iv) enumeration, abstract numbers, Phase-2 sweep table, three-algorithm DESIVAST robustness, within-class decompositions, Tempel cross-validation, and global LSS-anchored interpretation all hold up.

---

## Part D — Summary

**Findings count:**
- BLOCKER: 0
- **MAJOR: 1** (#N8 — robustness grid 7/9 vs claimed "full 3×3 / all cells")
- MINOR: 0

**3-consecutive-clean-rounds streak status per AGENT_RULES §4.4.1:**

R2 (v0.1.25) clean ✓ + R3 (v0.1.26) clean ✓ + **R4 (v0.1.27) NOT CLEAN (1 MAJOR)** → **streak BROKEN at R4**.

Cascaded-loop-exit per §4.4.1 is **NOT** met. P5 requires one more revision round (v0.1.28) to address #N8, then a fresh 3-consecutive-clean-rounds streak must be restarted (R-prime-1, R-prime-2, R-prime-3 all clean).

**Recommended fix for v0.1.28:** option 1 above (populate the 2 missing cells in `voids_vs_chirality_robustness_grid.json` from the existing matched-spiral + DESIVAST data; the script that generated the 7 cells lives at `pipelines/p5_desi_chirality/scripts/` and should accept NSIDE=64,cut∈{200,500} as input). Re-verify the |r|<0.11 / p>0.10 bound holds (or update it honestly if it doesn't), then bump version to v0.1.28-2026-05-23 with a comment block citing this R4 finding.

---

**Reviewer signature:** internal claude, R4 adversarial methodology + physics, 2026-05-23.
