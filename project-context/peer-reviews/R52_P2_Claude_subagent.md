# R52 — P2 f_NL Forecast — Referee Report (Claude/Opus leg)

**Recommendation: MINOR REVISIONS**

Paper: "Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx
Sensitivity Recast with a MegaMapper Outlook" — P2 v1.7.70 (29 pp).
Referee read: full PDF end-to-end (pp. 1–29), with truth-audit of load-bearing
claims against `research/focused_paper_source_integration/` source + committed
artifacts.

This is explicitly a sensitivity recast / forecast paper, not an independent
Fisher forecast, and is judged as such. The science is sound, internally
consistent, and reproducible; the document is unusually transparent about its
scoping. No scientific rework is required. The findings below are a Data-
Availability completeness issue plus presentation/scoping polish.

---

## 1. BLOCKERS

None. The headline arithmetic, conventions, and Bayesian machinery all check
out (see Strengths for the independent verifications performed).

---

## 2. MAJORS

**M1 — Data & Code Availability bundle does not fully resolve; the headline
null-space overlap artifact is absent from the committed repo.**
*Where:* "Data and Code Availability" (p. 24–25); §III B; §II.
The paper names ~10 artifacts as "released with the paper's code" / "archived in
the same repository." Audit against the repo:
- `phase3_bispectrum_shape_overlap.json` — named as the archive of the full
  bispectrum-shape coefficient map and per-configuration overlap values for all
  six coefficient sets (this backs the central r = 0.84 / r = 0.85 ± 0.13
  null-space scan, the paper's most load-bearing computational result). **Not
  present anywhere in the repository.**
- `phase3_fisher_overlap.json` — named as the ℓ-space Fisher-overlap output
  backing r = 0.878 ± 0.012. **Present, but only under
  `research/matter_bounce_parameters/`, not co-located with the paper code and
  not in `arxiv_package/`.** (Content verified: `r_mean`/`k_space_r` ≈ 0.878,
  consistent with the text.)

Mitigating fact: the *generating* script `null_space_analysis.py` IS committed
and runnable, so the result is recoverable — this is a broken/incomplete
released-artifact bundle rather than true non-reproducibility. But a referee
checking the Data Availability statement currently hits a dead reference for the
headline overlap map, which for a paper whose credibility model is "everything
is released and reproducible" warrants a fix before acceptance.
*Proposed fix:* regenerate/commit `phase3_bispectrum_shape_overlap.json` and
relocate (or copy) `phase3_fisher_overlap.json` into the paper's code directory
and the Zenodo bundle; verify every named artifact in the Data Availability
paragraph resolves on the committed main branch (run `/artifact-link-verify`).

---

## 3. MINORS

**m1 — Abstract length and significance-number density.** Abstract spans >1 full
column-page and quotes many distinct significance figures (6.25σ uncorrected,
5.2–5.5σ optimistic, 2.6–5σ realistic, 2.6–2.8σ post-budget, 3–7σ MegaMapper,
BF ≈ 4–17). A reader cannot retain the hierarchy. *Fix:* lead with one headline
(5.2–5.5σ optimistic) and one realistic number (2.6–5σ); defer the rest to the
body. The −2Im / single-ordering convention material in the abstract could move
to §II/App A.

**m2 — Additive-quadrature combination of systematics underlies the realistic
2.6–5σ headline.** §VII / Table IV combine b_φ and GR-projection budgets in
quadrature (σ_eff = √(σ_base² + σ_syst²)) rather than a joint marginalized
Fisher. The paper honestly flags this as "a transparent scoping choice whose
conservatism a full joint Fisher would need to confirm." Since the *realistic*
headline (an abstract claim) rests on this rule, at least one joint-Fisher
cross-check on the all-combined endpoint would materially strengthen it. Labeled
scoping, hence MINOR, but worth a single confirming calculation.

**m3 — Cubic-order ε-transfer (assumption d).** The paper calls this "the
weakest link," supported at cubic order only by an order-of-magnitude
superhorizon scaling estimate "not a derived bound," while κ_ε ∈ [5.6, 80] with
the upper end an admitted "schematic scaling bound." This κ_ε range propagates
into the f_NL–n_s consistency coefficient c' ∈ [0.7, 10] (Eq. 12). *Fix:* state
explicitly at the headline that the forecast uses the *central* κ_ε, not the
schematic upper endpoint, so the reader does not read [0.7,10] as a forecast
uncertainty band.

**m4 — Submission-source date.** `arxiv_package/main.tex` uses `\date{\today}`;
the released arXiv source will stamp the compile date, not the manuscript date
(June 18, 2026). *Fix:* set a fixed `\date{}` for submission.

**m5 — Significance ladder.** The 6.25σ → 5.2–5.5σ → 2.6–5σ → 3.0σ chain is
spread across abstract, §IV, §VII, Table IV, and Fig. 2. A single consolidated
"from naive to all-combined" sentence pointing to Table IV would reduce the
apparent (but real, on audit) consistency of the numbers being hard to track.

---

## 4. Strengths

- **Independently verified internal numerical consistency.** I reproduced the
  significance arithmetic by hand: headline 4.375 × 0.84 / 0.7 = 5.25σ; every
  Table IV row (b_φ-30% → 4.1σ, b_φ-50% → 3.7σ, GR 0.5 → 4.3σ, GR 1.0 → 3.0σ,
  all-combined 30%+GR → 2.7σ, 50%+GR → 2.6σ); and the Bayes-factor
  self-consistency checks (delta-broad 17.10 vs 30/√(2π)/0.7 = 17.07;
  δ-rebooked 14.36 vs 14.34; Gaussian σ_θ=1 → 9.80; f_NL–n_s range [−4.35,−4.02]
  from c'∈[0.7,10]). All hold.
- **Rigorous resolution of the Cai/Li factor-of-two.** Appendix A separates a
  genuine Komatsu–Spergel normalization convention (c=2 vs c=1) from the
  in-in commutator time-ordering via a Hermiticity / −2Im operator-algebra
  identity, with the −35/16 single-ordering value explicitly labeled a
  non-physical stress test, not an alternative bispectrum. This is the correct
  and honest treatment of a subtlety that trips up most of the literature.
- **Exceptional, MECE scoping transparency.** Every systematic, convention, and
  assumption (a)–(f) is labeled with its status, combination rule, and effect;
  Table IV consolidates the full budget; the recast (not-independent) nature of
  both the σ=0.7 baseline and the −35/8 prediction is stated plainly rather than
  hidden.
- **Reproducibility of the computation.** A generating script for every
  quantitative claim is committed and runnable (`null_space_analysis.py`,
  `c9g/c9k/c9l_*` marginalization scripts, `c8_fnl_running_fisher.py`,
  `appendix_A1_wick_doubling.py`), with JSON outputs present (modulo M1).
- **Honest negative-space discussion.** The κ_min cliff, photo-z outlier,
  shot-noise, and b_φ fragilities are quantified and shown to bound but not
  overturn the conclusion, and the consistency-relation n_{f_NL}=0 discriminator
  is correctly framed as the sharper future test.

---

*Referee: Claude/Opus leg, internal round R52, 2026-06-26. Verdict calibrated to
MNRAS/PRD: substantial scientific rework not required; one Data-Availability
completeness MAJOR + five presentation/scoping MINORs.*
