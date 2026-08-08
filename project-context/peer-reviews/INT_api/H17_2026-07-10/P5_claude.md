I have verified the flagged claims against the committed artifacts and pipeline. Here is my referee report.

---

## REFEREE REPORT — P5 (`p5_desi_chirality.tex`, v0.1.113, July 10 2026)

### (1) VERDICT: **MINOR REVISIONS**

### (2) ISSUES

**[MINOR] Abstract / §XI.C — quadrature radicand is arithmetically wrong (headline survives).** Line 3063–3064 states the term-sum as `√(0.44² + 0.37² + 0.60² + 0.37² + 0.11² + 0.24² + 0.02²) = √0.885 = 0.94 pp`. The seven listed squares actually sum to **0.8975**, not 0.885, and √0.8975 = **0.947** (rounds to 0.95). No combination of the `tab:systematic_budget` values (line 3111–3117) reproduces 0.885. The final envelope ≈0.9 pp is robust to this either way, but the displayed intermediate and √ are internally inconsistent. Checked: `p5_desi_chirality.tex:3063` vs `tab:systematic_budget:3111–3117`.

**[MINOR] Abstract / §XI.C — de-attenuated physical bound uses the more-favorable numerator.** The 2.26 pp physical bound is `0.9/0.3982` (line 748–749, 4315–4316), which is arithmetically correct. But the *honest* classifier-label envelope this de-attenuates is the quadrature value **0.94 pp**, not the rounded 0.9; the consistent physical bound is `0.94/0.3982 ≈ 2.36 pp`. For an *upper* bound, quoting the tighter 2.26 rather than 2.36 is mildly self-favoring — the opposite of the "widen, never tighten" posture the paper otherwise adopts. Recommend quoting ≈2.3–2.4 pp or explicitly deriving from 0.94. The attenuation factor itself is sound: a = 0.6991 → 2a−1 = 0.3982, and κ = 2a−1 = 0.40 is consistent; **verified sourced**, not fabricated (`pipelines/p2_chirality/outputs/B20_B21_results.json:8` = 0.6991083…, `README_CANONICAL.md:21`).

**[MINOR] §XI.B / Table `tab:desivast_canonical` — primary +0.0018 is paired with a different void N than the headline table.** The primary contrast Δf_CW = +0.0018 (z = +0.78, p = 0.43) is computed on the **exact k-unbounded void, n = 57,081** (`29_ext3_desivast_footprint_retabulation.json:52–56`: delta 0.001809, se 0.002317, z 0.781, p 0.4349 — **verified exactly**). But the table headline void row (line 2959) is the k=20 sample, **n = 56,981**, and the abstract attaches "56,981" to the void count. The 0.18% (100-galaxy) difference is disclosed as immaterial, but the headline pairing is strictly inconsistent (253,276 non-void ↔ 57,081 void, not 56,981). Trivial to reconcile; flag only for exactness.

**[MINOR] Companion-paper (Paper IV) dependency — mitigated but still a live gate for publication.** The headline environmental null rests on Paper IV's per-galaxy `class_eq` classifier labels, and Paper IV is cited with an **unfilled arXiv placeholder** (`\paperIVarxiv = arXiv:XXXX.XXXXX`, line 24). The independence argument is genuinely strong — (i) labels are public/CC-BY on HuggingFace, (ii) the two-sample contrast is algebraically monopole-invariant, (iii) the GZ1-human-only null corroborates provenance (**verified**: `gz1only_fullN_dipole_result.json` → N = 46,017, z = −0.539σ). But (iii) is a *global* parity null on a 12× smaller sample, not an environmental test, so environmental independence still inherits the classifier labels. This resolves automatically once Paper IV posts, but a PRD editor will require the companion public at review time; the placeholder must clear before acceptance. Not fabricated, honestly framed — but a hard pre-publication gate, not a pure formatting note.

**[MINOR] Monopole-invariance claim — correct, one caveat worth stating.** The claim that Δf_CW cancels any "catalog-wide monopole shift" (line 788–791) is algebraically valid: a constant additive bias δ to f_CW in both subsamples cancels in f_nonvoid − f_void. **Verified** the per-class monopole-subtracted residuals independently: filament +0.0008·√408187/0.5 = +1.02 (paper +0.99), cluster −1.14 (paper −1.11), void −0.56, wall +1.01, all `|σ_vs_monopole| < 1.15` (`tab:p4_monopole_residual:3542–3545`). The unstated assumption is that δ is itself environment-independent — which is what a chirality-environment test partly probes — but for a true *global* monopole the cancellation is exact and the residual analysis backs it. Suggest one sentence making the "monopole assumed environment-independent" assumption explicit at line 789.

**[MINOR] Counting term 0.44 pp vs SE.** `tab:systematic_budget` lists Counting CI (2σ) = 0.44 pp, but 2·SE = 2·0.002317 = 0.463 pp (≈0.46) and 1.96·SE = 0.454 pp. 0.44 pp is slightly under the 2σ half-width. Immaterial to the envelope; reconcile for consistency (`tab:systematic_budget:3111` vs `29_ext3…json:54`).

### (3) Central-claim support

The central claim — **a bounded null on void/non-void spiral-chirality dependence** (primary Δf_CW = +0.0018, z = 0.78; family-wise Bonferroni-5 |Δ| ≤ 0.004) — **is supported**: the primary contrast reproduces the committed artifact exactly, the significant per-class σ values are correctly and verifiably attributed to a sample-size-scaled global classifier monopole rather than environment, and the claim is appropriately hedged as a post-hoc, redshift-space, classifier-attenuated *upper limit* (≈0.9 pp label / ≈2.3 pp physical), not a discovery. The remaining issues are minor arithmetic/consistency slips and the standard companion-paper timing gate — none touch the null verdict itself.

Best Next Steps:
1. Fix the quadrature display (0.885 → 0.8975, √ → 0.947≈0.9) and derive the physical bound from 0.94 pp (≈2.36 pp) for internal consistency.
2. Reconcile the headline void N (56,981 k=20 vs 57,081 exact) at the primary-contrast statement.
3. Treat the Paper IV arXiv-ID fill as a hard pre-submission gate; add the "monopole assumed environment-independent" caveat at §V.

Say `continue` and I will take the next best scoped step.
