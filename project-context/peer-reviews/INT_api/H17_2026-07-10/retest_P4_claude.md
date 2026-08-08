I have completed the referee pass. The corrections landed coherently across the abstract, body, primary-callout table row, WLS section, appendix, conclusions, and the regenerated figure — with **one straggler** and a couple of minor consistency items.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES:**

1. **[MINOR] Straggler — Primary Results callout caption still cites the pre-correction value.** `chirality_catalog_paper.tex:816` (Table `tab:primary_callout` caption) reads *"all σ/z values in rows D1–D2 (including +0.41σ, +3.64/+7.28σ, and $z\approx-18$)…"*. The table **body** row P2 (line 824) correctly shows `z≈−7.6`, and the abstract, intro, Sec. IV, Appendix D (lines 802/822) and the figure all read −7.6. This is the only surviving `−18` in live body text (all other `−18`/`0.034` hits are in the `%` change-log). It must become `z≈−7.6` — as written the caption contradicts the very table it captions.

2. **[MINOR] −7.6 vs −7.8 at NSIDE=8, unreconciled.** Main text/table quote the primary block-bootstrap `z≈−7.6` (N_boot=1000). The robustness footnote at line 802 reports the NSIDE=8 sensitivity-check value as `z=−7.8` (N_boot=500, seed 42). The gap is explained by the different bootstrap sample size (σ_boot 1.63e−3 → z=−7.64 vs 1.60e−3 → z=−7.8), but a reader sees two "NSIDE=8" z-values differing by 0.2. Add a half-sentence noting the check used N_boot=500 vs the primary N_boot=1000.

3. **[MINOR] Figure has literal LaTeX-escape artifacts baked into the PNG.** `fig_bootstrap_null.png` (rendered) is otherwise correct — red dashed reference at `A_ref=0.017`, best-fit `4.55×10⁻³`, `z≃−7.6` arrow, all matching the corrected numbers (directive-I6 check: **passes** on values). But the title shows literal `vs.\ ` and the legend shows `interp.\,(i)` — mathtext escape sequences leaking as visible backslashes. Cosmetic; fix in `scripts/gen_fig_bootstrap_null.py` and re-mirror.

4. **[MINOR, disclosed] Sub-percent pseudo-label independence still rests on CE-ResNet labels.** The fully model-independent GZ1-human-only null (`z=−0.54`, N=46,017) is honest but sits at ~4.5× coarser sensitivity (A₅₀≈3.4%), so it only bounds an *inherited* dipole above ~3.4% — the headline sub-percent null still depends on the 66.5%-CE-ResNet-derived labels. This is explicitly and correctly disclosed (Sec. `pseudolabel_independence`); noting it as an acknowledged residual limitation, not a defect requiring new computation.

**Math check (passes):** The factor-of-2 correction is sound — `A_p = 2(f_CW−½) = (N_CW−N_CCW)/(N_CW+N_CCW)` is *identically* Shamir's reported asymmetry, so 1.7% → A_ref=0.017 with no rescaling; z=(0.00455−0.017)/0.00163=−7.64 ✓; tension 1.7/0.455=3.7× to 4.0/0.455=8.8× ✓. The old A_ref=0.034 / z=−18.1 was genuinely a double-count.

**(3)** The central claim — the large-scale morphological chirality dipole is consistent with null (two primary estimators: +0.41σ real-space HC dipole and z≈−7.6 clean-1.7%-template disfavor), placing Shamir's 2–4% class in ~3.7–8.8× *amplitude-level* tension without claiming a frequentist exclusion of his Ganalyzer estimator — **is supported and now internally coherent**, contingent only on fixing the single stale caption value (#1) so the headline table is self-consistent.
