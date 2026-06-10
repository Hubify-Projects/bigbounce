# P5 R28conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/p5_desi_chirality_v0.1.59.pdf` md5=3a80c50b pages=28
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique
---

## Pass 1 — 26-series priority additions (verified against `26_r27conf_ess_recomputes.json`)

### Per-cell dilation clarification (Methods bullet 5, p4 / `.tex` L501–507)

Bullet states: `\lceil R_s/cell\rceil + 1 = 2` iterations at canonical $R_s=25$, recomputed per sweep cell, 3 at $R_s=50$.

JSON cross-check:
- `q1_per_rs_dilation.method.dilation_rule_scaled` = `"iterations = ceil(R_s/cell) + 1 (10->2, 25->2, 50->3)"` — matches.
- `cell_size_mpc_h = 25.91`; `ceil(10/25.91)+1 = 0+1+1 = 2`; `ceil(25/25.91)+1 = 1+1 = 2`; `ceil(50/25.91)+1 = 2+1 = 3`. Arithmetic correct.
- Canonical (R25) `n_mask_cells` rebuild = 3,150,089 vs published 3,150,086 (Δ=3 cells, volfrac diff < 5.5×10⁻⁷); paper quotes 3,150,086 → exactly consistent within rebuild jitter. **Verified.**

### Mask-dilation scaling paragraph (p11, `.tex` L1297–1308)

Claim 1: "local rebuild reproduces the published $R_s=50$ mask to within 4 of 3,416,329 in-mask cells (volume fractions agree to $<10^{-6}$)."
- JSON `published_sweep_check.R50.published_n_mask_cells = 3,416,329`; `rebuilt_scaled_n_mask_cells = 3,416,333`; diff = 4. ✓
- `max_abs_volfrac_diff = 5.51×10⁻⁷` < 10⁻⁶. ✓

Claim 2: counterfactual ($R_s=50$ fixed-2 mask) "shifts class volumes by $\le 0.82$ pp."
- JSON `deltas_R50_scaled3_minus_fixed2.max_abs_volume_fraction_shift_pp = 0.8196`. Rounds to 0.82. ✓

Claim 3: "retains 99.75% of matched-spiral class assignments."
- JSON `spiral_class_assignment_agreement = 0.99751` → 99.75%. ✓

Claim 4: "moves per-class $f_{\rm CW}$ by at most 0.27 pp (the $n=406$ void bin)."
- JSON `max_abs_f_cw_shift_pp = 0.2727`; located in `f_cw_by_class.void.delta_f_cw_pp = -0.2727`. ✓
- $n$ for the void bin in `R50_scaled.spiral_f_cw_by_class.void.n = 406` (and `R50_fixed2.void.n = 410`). The paper says "n=406 void bin" referring to the scaled-3 build, which is the canonical baseline. ✓

### FoG-MC sentence (RSD paragraph, p14, `.tex` L1536–1548)

Claim A: "$\sigma = 5$ Mpc/$h$ Gaussian (200 realizations…)."
- JSON `q2_fog_membership.method.fog_model`: "eps ~ N(0, 5 Mpc/h), 200 realizations." ✓

Claim B: "reassigns $\sim 4.4\times 10^{4}$ hole-union memberships per realization."
- JSON `fog_mc.n_flip_in.mean = 31,876`; `n_flip_out.mean = 12,466`; sum = 44,342 ≈ 4.43×10⁴ → "$\sim 4.4\times 10^4$." ✓
  (Aggregate reassignment = inflows + outflows is the right operational count for the sentence.)

Claim C: "void count rises from 57,081 to 76,490 ± 161 as boundary spirals scatter inward."
- Baseline `uncompressed_baseline.void.n = 57,081`. ✓
- `fog_mc.n_void.mean = 76,490.36`, `std = 160.77` → 76,490 ± 161. ✓

Claim D: "$\Delta f_{\rm CW}$ stays within $[-0.34, +0.37]$ pp."
- `fog_mc.delta_fcw_pp.min = -0.3371`, `max = +0.3696` → $[-0.34, +0.37]$ pp. ✓

Claim E: "coherent $\pm 5$ Mpc/$h$ shifts: $-0.16$/$+0.03$ pp."
- `coherent_shifts.plus_5.delta_fcw_pp = -0.1601` → $-0.16$. ✓
- `coherent_shifts.minus_5.delta_fcw_pp = +0.0326` → $+0.03$. ✓
- (Paper convention: "$+5$ Mpc/$h$" listed first, mapping to $-0.16$, matches `plus_5` → $-0.16$. Sign/ordering convention is internally consistent.)

Claim F: "no realization's void/non-void two-sample $|z|$ exceeds 1.9."
- `fog_mc.two_sample_z.max = 1.924`; `min = -1.755`. Max absolute = 1.924. Paper says "exceeds 1.9" — the max IS 1.924, which marginally exceeds 1.9.
  → see **P5-m1** below.

---

## P5-m1 (minor — wording precision, FoG-MC z bound)

`.tex` L1546–1547 reads: "no realization's void/non-void two-sample $|z|$ exceeds 1.9."

JSON `fog_mc.two_sample_z.max = 1.92429` (and the realization-wise `|z|` therefore reached at least 1.924). The literal statement "$|z|$ does not exceed 1.9" is falsified by the worst realization's $|z| = 1.924$. The intended scientific content is preserved — 1.924 is well below the Bonferroni / "$3\sigma$" thresholds used throughout the paper, and the null verdict is robust — but the **inequality as written is wrong by 0.024**.

**Fix (either)**:
- Replace "1.9" with "1.93" (matches max value, still well below 2 / Bonferroni).
- Replace with "no realization's two-sample $|z|$ reaches $2\sigma$ (max $|z| = 1.92$ across 200 draws)."

Severity: minor — does not move any verdict; pure numerical-quote tightness. Caught only because the JSON max is 1.9243.

---

## P5-N1 (nit — "n=406 void bin" anchoring)

The mask-dilation paragraph cites "the $n=406$ void bin" as the worst-case 0.27 pp shift. In the JSON, `R50_scaled.void.n = 406` and `R50_fixed2.void.n = 410`; the 0.27 pp delta is the *difference* between two builds whose void $n$ values are 406 and 410. Citing "$n=406$" anchors to the scaled (3-iter) build, which is the canonical/published one — defensible and conventional, but a vigilant referee may ask why not "$n \in \{406, 410\}$." A parenthetical "($n=406$ scaled / $n=410$ fixed-2)" would be airtight; current phrasing is acceptable. No action required if pressed for space.

---

## P5-N2 (nit — methods bullet 5 vs JSON `n_mask_cells`)

`.tex` L506 quotes "2,417,697 occupied $\to$ 3,150,086 in-mask" at canonical. JSON `R25_scaled.n_mask_cells = 3,150,089` (Δ=3 cells from the published 3,150,086 quoted in the bullet and Table). Within rebuild jitter (volfrac diff < 5.5×10⁻⁷); paper number is the production-pipeline value, JSON is the local rebuild. Both stand; no action.

---

## Explicit all-clears (with arithmetic)

1. **Per-cell dilation iteration formula** — `ceil(10/25.91)+1=2`, `ceil(25/25.91)+1=2`, `ceil(50/25.91)+1=3`. Matches JSON `dilation_rule_scaled` and Methods bullet 5 / Mask-dilation paragraph. CLEAR.
2. **R50 mask rebuild closeness** — published 3,416,329 cells vs rebuilt 3,416,333, |Δ|=4 < quoted "within 4 of"; volfrac diff 5.51×10⁻⁷ < 10⁻⁶. CLEAR.
3. **Counterfactual 0.82 pp** — JSON `max_abs_volume_fraction_shift_pp = 0.8196 → 0.82`. CLEAR.
4. **Counterfactual 99.75% class-assignment retention** — JSON `spiral_class_assignment_agreement = 0.99751`. CLEAR.
5. **Counterfactual 0.27 pp $f_{\rm CW}$ shift** — JSON `max_abs_f_cw_shift_pp = 0.2727 → 0.27` pp, void bin. CLEAR.
6. **FoG-MC $\sigma=5$ Mpc/$h$, 200 realizations** — JSON `fog_model`. CLEAR.
7. **FoG-MC $\sim 4.4\times 10^4$ reassignments** — 31,876 (in) + 12,466 (out) = 44,342 ≈ 4.43×10⁴. CLEAR.
8. **Void count 57,081 → 76,490 ± 161** — baseline `void.n = 57,081`; MC `mean = 76,490.36`, `std = 160.77`. CLEAR.
9. **$\Delta f_{\rm CW} \in [-0.34, +0.37]$ pp** — `delta_fcw_pp.min = -0.337`, `max = +0.370`. CLEAR.
10. **Coherent $\pm 5$ Mpc/$h$: $-0.16/+0.03$ pp** — `plus_5.delta_fcw_pp = -0.160`, `minus_5.delta_fcw_pp = +0.033`. CLEAR.
11. **Hole-union vs maximal-sphere flip 36,181 of 57,081** — earlier R-round sentence retained, JSON also shows the same void.n=57,081 anchor. CLEAR (no change in this round).
12. **R10 grid-resolution caveat (cell=25.9 Mpc/$h$ > $R_s=10$)** — paper carries the under-resolved caveat; JSON `note` for R10 confirms `dilation_iterations` collapses to the same value as fixed-2, consistent with degenerate near-unsmoothed limit. CLEAR.

---

## Pass-2 self-critique (vs `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`)

Re-read of the .tex source against pass-1:

- **Did I overstate P5-m1?** The .tex L1546–1547 sentence is "no realization's void/non-void two-sample $|z|$ exceeds 1.9." JSON max is 1.9243. This *is* a literal-false statement (1.9243 > 1.9), but it is a single-decimal rounding ambiguity. A defender could argue "1.9" is shorthand for "approximately 1.9" / "below $2\sigma$." I retain it as a minor because the *verbatim* numeric inequality is wrong, and the paper elsewhere is precise to 2–4 decimals (0.0007, 0.0026, etc.), so the looser-than-house-style "1.9" stands out. Not load-bearing on any verdict.

- **Did I miss anything in the FoG sentence?** Checked: the "2-sample $|z|$ exceeds 1.9" is the only number where pass-1 found a mismatch; everything else in the sentence is exact. The phrase "used in place of a deterministic per-galaxy compression, which would require a group catalog" is properly hedged and matches the JSON `DISCLOSED CHOICE` note. No fabrication; the rationale is transparently disclosed.

- **Did the per-cell-dilation clarification break consistency anywhere?** Searched `.tex` for "2 iterations" and "3 iterations" and `\lceil R_s/{\rm cell}\rceil`. Only two anchors — Methods bullet 5 (L501–507) and Mask-dilation paragraph (L1297–1308). Both agree on the rule. The earlier "cube-connected 3-iteration dilation variant" mention in §VIIIA (L2080–2084) is a different (cube-connected) structuring element variant, not in tension with the face-connected default.

- **Did I miss any silent contradiction?** Spot-checked the abstract's "$|\Delta f_{\rm CW}| \lesssim 0.002$" three-algorithm bound (Table VIII): VoidFinder $\Delta f_{\rm CW} = +0.0007$, V2-REVOLVER $-0.0019$, V2-VIDE $-0.0001$. Largest $|0.0019|$ rounds to 0.002 → bound holds. CLEAR.

- **Pass-2 verdict:** pass-1 P5-m1 stands; no additional findings surfaced.

---

## Summary recommendation + counts line

The 26-series additions (per-cell dilation clarification, mask-dilation scaling paragraph, FoG-MC sentence) are quantitatively faithful to `26_r27conf_ess_recomputes.json` in all twelve checked claims except a single 0.024-unit looseness in the "$|z|$ exceeds 1.9" phrasing (P5-m1, minor wording fix). No errata, no methodology issues, no architecture concerns. The paper is publication-ready modulo this one cosmetic numeric tightening.

**Recommendation:** ACCEPT with one minor wording fix (P5-m1).

**Counts:** E=0, M=0, m=1, N=2.
