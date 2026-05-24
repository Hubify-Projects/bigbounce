# P2 v1.7.35 — R-next-d theoretical-physics-Gemini verdict

**Date:** 2026-05-24
**Reviewer:** Claude (Opus 4.7) acting as theoretical-cosmologist + Gemini-cosmology-rotation reviewer
**Round:** 3-of-3 in the §4.4.1 cross-model streak on v1.7.35 (post v1.7.35 BF four-corner sweep)
**Perspective:** Theoretical-physics rigor + scope-creep audit; verifies the consistency of the v1.7.35 BF sweep across all ≥12 sites and rechecks load-bearing physics claims (Wilson-Ewing class flagging, Heinrich+2023 anchoring, Li & Brandenberger c=1/c=2 resolution, CFC-frame framing).
**Artifacts read:**
- `/Users/houstongolden/Desktop/CODE_2025/bigbounce/research/focused_paper_source_integration/02_full_draft.tex` (563 lines, v1.7.35)
- R-next-a theoretical-physics (1 MAJ closed in v1.7.34 + 1 MAJ falsified)
- R-next-b Perplexity-citation (0 MAJ / 2 min — clean)
- R-next-c brutal-honesty-Grok (1 MAJ + 1 MIN — closed in v1.7.35 sweep)

---

## One-line summary

The v1.7.35 BF sweep is **NOT internally consistent** — three residual sites still carry the pre-correction `BF~8 / BF~6` / `BF~6-17` numbers despite the rest of the paper updating to `BF~10 / BF~4 / BF~10-17`. The σ_th=0.5 and σ_th=2.0 rows are also inconsistent with the same scipy.stats.norm formula that produced the σ_th=1.0 sweep. The conclusion section's `>6×10^5 MC` figure contradicts the abstract's `3×10^5 aggregate` correction. One MAJOR + two MINOR + one nit on physics-framing.

---

## Per-finding blocks

### MAJOR-1 — `tab:bayes` row 1 (PRIMARY headline) still reports BF~$\mathbf{8}$, not BF~$\sim 10$, contradicting the v1.7.35 sweep

**Location:** L295 in `02_full_draft.tex`:
```latex
\textbf{Gaussian, $\sigma_{\rm theory}=1.0$ (recommended headline)} & $\sim \mathbf{8}$ & $\gg 1$ \\
```

**Issue:** This is the PRIMARY headline cell — the same row whose caption (L303) explicitly says "BF~$\sim 10$ at broad multifield $[-15,+15]$", whose pre-table prose (L286) says "BF~$\sim 10$ vs.\ tuned multifield, broad $[-15,+15]$ column", and whose abstract (L58) says `BF~$\approx 10$ at the recommended physically motivated baseline`. The bullet list at L255 also says `$\sim 10$ (corrected v1.7.35 R-next-c-MAJ-1 from $\sim 8$ via scipy.stats.norm)`. **Every other instance updated 8→10; this one cell did not.** scipy recompute confirms BF=9.80 at σ_th=1.0 / broad-$[-15,+15]$. A reviewer reading Table~\ref{tab:bayes} top-to-bottom will see a `$\sim 8$` headline cell directly contradicting the caption two lines below, the abstract, and the prose.

**Hard-fix (v1.7.36):** change L295 `& $\sim \mathbf{8}$ &` → `& $\sim \mathbf{10}$ &`. One-character edit. The row is bolded as the recommended headline; the mismatch with the bolded caption value is the most visible v1.7.35 sweep miss.

**Severity:** MAJOR — load-bearing arithmetic mismatch on the PRIMARY headline row, in the same column whose caption asserts a different value. An external referee running visual consistency on the table will catch this within one page-flip.

---

### MAJOR-2 — Abstract envelope at L309 still reads `BF~$\mathbf{6}$–$17$`, not `BF~$\sim 4$–$17$` or `BF~$\sim 10$-$17$`

**Location:** L309, final sentence of the QSFI-closure paragraph:
> "the abstract $\mathrm{BF}\,{\sim}\,\mathbf{6}$--$17$ envelope should be read as bracketing the curvaton-class discrimination only…"

**Issue:** The abstract (L58) now reads `the full $\mathrm{BF}\,{\sim}\,4$--$17$ envelope` (lower bound corrected to the narrow-multifield σ_th=1.0 = BF=4.01) AND the recommended headline framing `$\mathrm{BF}\,{\sim}\,10$–$17$`. The L309 paragraph still anchors to a stale "$\sim 6$–$17$" interval that has been retired in both directions: the lower bound is now 4 (curvaton-natural narrow column σ_th=1.0) and the recommended-baseline envelope is `10–17`. The `~6–17` range corresponds to neither the corrected curvaton-natural envelope NOR the recommended-baseline envelope and is a pure v1.7.35-sweep miss.

**Hard-fix (v1.7.36):** L309: change `$\mathrm{BF}\,{\sim}\,6$--$17$` → `$\mathrm{BF}\,{\sim}\,4$--$17$` (matching the curvaton-natural lower-bound to delta-prior upper-bound bracket that the rest of the abstract now uses), or alternately `$\mathrm{BF}\,{\sim}\,10$–$17$` (matching the recommended-baseline-headline envelope). Either is internally consistent; what is NOT consistent is the current `~6–17`. Recommend the `~4–17` version since the abstract already uses that lower-bound corner.

**Severity:** MAJOR — same arithmetic-mismatch class as MAJ-1; this is the QSFI-closure paragraph that the abstract envelope explicitly bookends, and the stale `~6` lower bound is the corner that R-next-c found and the v1.7.35 sweep was supposed to retire everywhere.

---

### MINOR-1 — σ_th=0.5 and σ_th=2.0 rows of `tab:bayes` (L296/L297) and bullet list (L254/L256) are inconsistent with the same scipy formula that produced the σ_th=1.0 row

**Location:** L254–L256 prose bullet list, L296–L297 Table~\ref{tab:bayes} rows 2 and 3.

**Issue:** The v1.7.35 sweep updated the σ_th=1.0 row to scipy.stats.norm exact values (BF=9.80 → `$\sim 10$` broad; BF=4.01 → `$\sim 4$` narrow). But the σ_th=0.5 and σ_th=2.0 rows were NOT swept. Direct scipy recompute (same formula, identical inputs):

| Row | Width | Paper says | scipy.stats.norm | Discrepancy |
|---|---|---|---|---|
| σ_th=0.5 / broad [-15,+15] | 30 | `~12` (L254, L296) | **13.91** | paper UNDERSTATES by ~14% |
| σ_th=1.0 / broad [-15,+15] | 30 | `~10` (L255 prose, L303 caption — but L295 cell still says `~8`) | **9.80** | matches prose, mismatch with L295 cell (MAJ-1) |
| σ_th=2.0 / broad [-15,+15] | 30 | `~4` (L256, L297) | **5.65** | paper UNDERSTATES by ~30% |

The σ_th=2.0 row is the worst offender: paper reports BF~4, scipy gives 5.65 — a 41% underreport. The σ_th=0.5 row is also off by 16%. After the σ_th=1.0 closure these two adjacent rows are the only Gaussian-row entries inconsistent with the same arithmetic; an external referee running a one-line scipy check on any of these corners will hit a discrepancy. R-next-c brutal-honesty MAJ-1 + MIN-1 both flagged that the delta-prior rows are exact to four-digit precision — the σ_th=0.5 and σ_th=2.0 rows should also reconcile with that same formula and currently do not.

**Hard-fix (v1.7.36):** Either (a) update L254 12→14, L256 4→6, L296 12→14, L297 4→6 to match scipy, OR (b) add one sentence to the §sec:bayesian prose explaining the deviation (e.g., "the σ_th=0.5 and σ_th=2.0 entries include a residual MC-validation penalty not present in the σ_th=1.0 baseline"). Path (a) is preferred (one-character edits, full consistency); path (b) is acceptable only if the paper plans to keep the MC-validation framing.

**Severity:** MINOR — these are NOT headline rows (PRIMARY = σ_th=1.0); but they sit immediately adjacent to the recommended-baseline row in both the bullet list and the table, and the inconsistency is mechanical. A reviewer who runs the BF=9.80/4.01 scipy check at σ_th=1.0 will run the σ_th=0.5/2.0 check at the same time and see the deviation.

---

### MINOR-2 — Conclusion section L450 still reads `>$6\times 10^5$ Monte Carlo realizations`, contradicting abstract correction at L58

**Location:** L450 `\subsection{Conclusion}` block:
> "Our Bayesian model comparison, validated over $>\!6\!\times\!10^5$ Monte Carlo realizations that confirm the closed-form analytic Bayes factor…"

**Issue:** The abstract (L58) explicitly corrects this: "the aggregate $3\times 10^5$ count is not a single Monte Carlo but three framework-specific cross-checks…". L245 §sec:bayesian also corrects to "$3\times 10^5$ aggregate (a rhetorical ``${>}6\times 10^5$'' figure appeared in an older draft conclusion paragraph; the canonical realization count is $3\times 10^5$ across the 3 framework ensembles, and any larger number was an aggregation error)". The conclusion section was not updated. An external referee reading the conclusion alone will get the retired figure.

**Hard-fix (v1.7.36):** L450: change `$>\!6\!\times\!10^5$ Monte Carlo realizations` → `$3\times 10^5$ Monte Carlo realizations across three framework-specific cross-checks`. One-line edit; preserves the meaning while aligning with the explicit correction made in two other sections.

**Severity:** MINOR — does not affect a numerical result; the BF claims hold either way. But the §sec:bayesian explicitly flags the >6×10^5 figure as an "aggregation error" that should no longer appear in the paper — and it still appears in the conclusion. This is exactly the kind of cross-section consistency miss that the R-round protocol exists to catch.

---

### NIT-1 — Wilson-Ewing class restriction flagging is solid but Zhu-Cai 2026 citation is the only counter-example named

**Location:** L71 intro, L147 §sec:assumptions assumption (e).

**Observation:** The paper correctly flags that assumption (e) restricts to the Wilson-Ewing class without prolonged post-bounce inflation, and names Zhu-Cai 2026 (`Zhu:2026echoes`) as the prolonged-inflation counter-example. This is honest disclosure. But the prompt mentions "many cited bounce papers (Cai, Brandenberger, etc.) DO have prolonged post-bounce inflation and would NOT make the f_NL=-35/8 prediction". The paper's own L71 framing — "bounce models that invoke prolonged post-bounce inflation (e.g., as required by some dark-energy-from-bounce constructions) erase the $\fnl$ signal" — is correct but cites only the dark-energy-from-bounce class as the counter-example. **Cai et al. 2009 itself is the source of the -35/8 prediction and is in the Wilson-Ewing class (no prolonged inflation needed for the cubic-action result); Cai & Brandenberger 2014 likewise. The Cuscuton-bounce class is also in-class.** So the paper's framing is actually correct: the counter-examples are dark-energy-bounce-with-prolonged-inflation constructions, not the Cai/Brandenberger originals. No fix needed — the Wilson-Ewing class flagging at L71, L147, and L448 conclusion is sufficient and consistent.

**Severity:** NIT — observational, not actionable. The reviewer-prompt assumption that Cai/Brandenberger themselves would not predict -35/8 is incorrect; they are the source of -35/8 and are in the Wilson-Ewing class.

---

## Cross-check survives cleanly on the following vectors

| Vector | Audit | Verdict |
|---|---|---|
| **(b) Closed-form Gaussian-prior BF derivation** | The formula at L246–L247 ($B = (\fnl^{\rm max}-\fnl^{\rm min})\cdot\mathcal{L}(\fnl^{\rm obs}\mid -35/8)/\int\mathcal{L}\,d\fnl$) is the correct delta-bounce / uniform-competitor BF. For the Gaussian-bounce case (σ_th≠0), the marginal likelihood is $m_b = N(\fnl^{\rm obs};\,-35/8,\,\sqrt{\sigma_{\rm obs}^2+\sigma_{\rm th}^2})$ — i.e., Gaussian-on-Gaussian convolution; scipy.stats.norm direct evaluation confirms this at σ_th=1.0 gives 9.80 (broad) and 4.01 (narrow), matching the v1.7.35-corrected σ_th=1.0 row of the prose and caption (though NOT the L295 cell — see MAJ-1). | ✅ Formula correct; v1.7.35 σ_th=1.0 numbers correct; σ_th=0.5/2.0 numbers off (MIN-1) |
| **(c) Abstract envelope `BF~10-17` internal consistency** | Abstract L58 says `$\mathrm{BF}\approx 4$ ... up to $\mathrm{BF}\approx 17$` with headline `$\approx 10$` at the recommended baseline. Mini-table (L268–L277) consistent (10/17 broad column, 4/7 narrow column). Caption L303 consistent. Prose L286 + L307 consistent. **Inconsistent at L295 (tab:bayes cell) and L309 (`~6–17` stale).** | ⚠ MAJ-1 + MAJ-2 |
| **(d) Wilson-Ewing class restriction** | Flagged at L71 intro, L147 assumption (e), L448 conclusion. Zhu-Cai 2026 cited as the prolonged-inflation counter-example. Framework correctly restricts to scalar-only Wilson-Ewing class. | ✅ Clean (NIT-1 confirms reviewer-prompt's "Cai/Brandenberger excluded" assumption is itself incorrect) |
| **(e) Heinrich+2023 σ(f_NL)=0.7 anchoring** | L185 cites `Heinrich:2023` correctly; L199 anchors to Heinrich+2024 = PRD 109 123511; three caveats flagged (b_φ universality, local-template assumption, full-SPHEREx-depth assumption). Noise-weighted shape mismatch r=0.84±0.02 propagated consistently through L189, L307, L334, L448. | ✅ Clean |
| **(f) Li & Brandenberger c=1 vs Cai c=2 resolution** | Appendix App.~A (L462–L477) gives the explicit Wick-doubling derivation: Cai includes both time-orderings via $i\langle[\zeta^3,L]\rangle = -2\,\text{Im}\,\langle\zeta^3 L\rangle$; Li includes only single ordering; Planck-convention value is f_NL=-35/8. Convention sensitivity reported at abstract (L58, halving to 1.5–2.5σ post-systematic), §sec:conclusion (L448), App.~A.2 dual-normalization Fisher table (L538). | ✅ Clean — three-level reconciliation maintained |
| **(g) Table cross-references (tab:bayes vs tab:gr vs tab:dualnorm)** | tab:bayes caption footnote $^a$ explicitly reconciles "Table~\ref{tab:bayes} row 4 = 9.4 = Table~\ref{tab:gr} row 2 BF-vs-Tuned" at σ_GR=0.5. tab:dualnorm is the convention-sensitivity Fisher table, independent of the BF grid. **The internal `tab:bayes_minimal` reference in caption L303 ("prior versions of this caption + Table~\ref{tab:bayes_minimal}") is a dangling reference** — there is no `\label{tab:bayes_minimal}` anywhere in the paper. The mini-table at L268–L277 does not carry a label. This is a latent `\ref{??}` that will emit an undefined-reference warning at pdflatex compile time (or simply render as "Table??" if the label is missing). Minor citation-hygiene flag, not a numerical issue. | ⚠ Latent `\ref{tab:bayes_minimal}` undefined reference at L303 — should be removed or the mini-table should be labeled `tab:bayes_minimal` |
| **(h) Mukhanov-Sasaki / Maldacena cubic action / CFC frame** | L71 intro: scalar perturbations reduce exactly to the standard Mukhanov-Sasaki sector under the Holst topological-invariance argument for scalar-only matter; Barbero-Immirzi parameter is invisible. CFC frame: L58 abstract `→ 0 at leading order` with `gradient / projection / finite-squeezed-corrections caveats` framing is consistent with L228 §sec:bayesian, L448 conclusion ("vanishes at leading order in slow-roll with O(slow-roll) residuals"). The v1.7.34 closure of R-next-a MAJ-2 (softening "strictly 0" → "vanishes at leading order with O(slow-roll) residuals") holds. | ✅ Clean — the MS/Maldacena/CFC framing is dimensionally and conceptually consistent |

I record the `tab:bayes_minimal` dangling reference as an **additional MINOR** below (MIN-3) because the v1.7.35 caption explicitly invokes that label and an external compiler will emit an undefined-reference warning.

---

### MINOR-3 — `Table~\ref{tab:bayes_minimal}` at caption L303 is a dangling LaTeX reference

**Location:** L303 inside the tab:bayes caption:
> "prior versions of this caption + Table~\ref{tab:bayes_minimal} reported BF~$\sim 8$…"

**Issue:** There is no `\label{tab:bayes_minimal}` anywhere in `02_full_draft.tex` (grep returns only this `\ref{}` invocation and a v1.7.35 % comment). The mini-table at L268–L277 has `\begin{table*}` but no label. pdflatex will emit `LaTeX Warning: Reference 'tab:bayes_minimal' on page X undefined` at compile time, and the rendered PDF will read "Table~??" at L303. This is the same class of issue as the R-next-b Perplexity-citation findings (citation hygiene) and is closable in one line.

**Hard-fix (v1.7.36):** Either (a) add `\label{tab:bayes_minimal}` immediately before `\end{table*}` at L277 in the mini-table block (so the caption-reference resolves), OR (b) replace `Table~\ref{tab:bayes_minimal}` at L303 with `the mini-table above` (so the ref is removed). Option (a) is the more rigorous fix because Table~\ref{tab:bayes_minimal} also appears in the v1.7.35 audit-trail comment at L31 as the intended cross-reference target.

**Severity:** MINOR — does not affect any number; emits a compile-time warning and a rendered "Table??". An external referee or arxiv compile QA will flag this.

---

## Verdict

**Status:** NOT clean. R-next-d returns **0 BLOCKER / 2 MAJOR / 3 MINOR / 1 NIT** on v1.7.35.

Per §4.4.1 cascaded-loop-exit, a clean round requires `≤ 0 MAJOR + ≤ 2 MINOR`. R-next-d does NOT satisfy that bar: MAJ-1 (L295 cell `~8` not updated to `~10`) and MAJ-2 (L309 envelope `~6–17` not updated to `~4–17` or `~10–17`) are direct v1.7.35-sweep misses that re-open the same arithmetic-consistency class that R-next-c (brutal-honesty) closed for the abstract+caption+prose but missed for these two locations.

**The streak is BROKEN at round 3-of-3** by two residual BF-sweep-miss sites. A v1.7.36 closure of MAJ-1 + MAJ-2 + the three MINOR (σ_th=0.5/2.0 row consistency, conclusion MC count, tab:bayes_minimal dangling ref) is required before a fresh three-round streak can commence.

The fixes are surgical:
- **MAJ-1:** L295 cell `$\sim \mathbf{8}$` → `$\sim \mathbf{10}$` (1 char)
- **MAJ-2:** L309 `~6--17` → `~4--17` (1 digit)
- **MIN-1:** L254 12→14, L256 4→6, L296 12→14, L297 4→6 (4 digits)
- **MIN-2:** L450 `>6×10^5` → `3×10^5 across three framework cross-checks` (one phrase)
- **MIN-3:** add `\label{tab:bayes_minimal}` to the mini-table at L268–L277, OR replace L303 `Table~\ref{tab:bayes_minimal}` with `the mini-table above`

PDF impact <1 KB. No re-derivation of physics, no new figures, no new MCMC.

**Recommended next action for Houston:**
1. v1.7.36 closure of MAJ-1 + MAJ-2 + MIN-1/2/3 (surgical edits only).
2. Re-fire R-next-d on v1.7.36 (theoretical-physics rotation) to verify a clean round.
3. If clean, re-fire R-next-a + R-next-b + R-next-c on v1.7.36 to lock in the fresh 3-round §4.4.1 cascaded-loop-exit streak.

**Readiness impact:** 95% cap holds. Mid-streak rollback to ~92% is appropriate while two MAJORs are open at the abstract-envelope + headline-row level. Forward step to 95% only after v1.7.36 closure + clean re-fired R-rounds. The 95% ceiling remains gated on the still-blocked external 5-vendor wave + Houston sign-off.
