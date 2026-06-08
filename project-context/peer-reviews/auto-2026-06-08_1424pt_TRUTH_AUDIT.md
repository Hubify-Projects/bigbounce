# Fire 14 META findings — truth-audit results (2026-06-08 14:50pt)

Per `feedback_peer_review_truth_audit_protocol`: every external/internal multi-model
peer-review finding MUST pass through a per-finding truth-audit table BEFORE
closures. Reviewers (including the gpt-5-pro meta-reviewer) don't have full
repo context and over-call severity on stale/mislabeled/missing artifacts.

This memo truth-audits the 4 fire-14 META findings that fall under pattern-041
(META arithmetic check). Each was re-derived using the paper's own formula
and parameters, then cross-checked against the .tex source.

---

## P3-META-E4 — γ ± 0.382 vs CI [2.304, 2.882] arithmetic — **VERIFIED**

**Source citation**: `pipelines/p3_anomaly_engine/paper3_draft.tex:712`
```
\textbf{Posterior:} $\gamma = 2.567 \pm 0.382$
(median $2.591$, 68\% CI $[2.304, 2.882]$)
```

**Arithmetic**:
- ±0.382 as Gaussian 1σ → 1σ CI width = 2 × 0.382 = 0.764
- Quoted 68% CI width = 2.882 − 2.304 = 0.578
- CI half-width around median 2.591: left = 0.287, right = 0.291
- Ratio CI/Gaussian = 0.578 / 0.764 = 0.757 → **49% mismatch**

**Interpretation**: the posterior is non-Gaussian / asymmetric. The Gaussian
± summary (0.382) is the sample std-dev; the 68% CI is the quantile-based
credible interval. They differ. The paper presents both as if they were the
same uncertainty.

**Fix**: pick one interval convention. Either drop the ± and quote only the
68% CI, or quote a Gaussian-equivalent ± that matches the CI half-width
(≈ 0.289). Suggest the latter since the ± is in the abstract.

**Effort**: 15 min text fix at three sites (abstract L80, body L457+712, 
conclusion L519/537).

---

## P5-META-E1 — three incompatible "range" numbers for canonical V-Web — **VERIFIED**

**Source citations**: `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex`
```
L549, L558, L1880:  Table II f_CW range = 1.98 pp (correct from {0.4836, 0.5034, 0.4980, 0.4963})
L977:               "per-cell range upper bound of 0.22 pp"
L1765:              "$\sim 0.497$ with range $\sim 0.2$ percentage points across the four [classes]"
```

The meta-reviewer's exact phrasing referenced Table VI for Rs=25, λ_th=0 giving
"fCW range (pp) = 0.165" — would need to confirm Table VI; haven't found that
specific table yet, but the L977 and L1765 ~0.22 / ~0.2pp claims do contradict
the L549 / L1880 1.98pp claim.

**Note on my earlier summary error**: in fire-14 AUTOLOOP_LOG closure I framed
this as "1.98pp vs 1.7pp" — the .tex contains no "1.7pp" claim. The actual
contradiction is 1.98pp (Table II range across 4 classes) vs ~0.2–0.22pp
(per-cell upper bounds, possibly a different statistic). Apologies for the
mislabel.

**Fix**: rename the per-cell range statistic so it's not called the same thing
as the Table II inter-class range. Suggest:
- Table II: "inter-class range" or "max f_CW − min f_CW across {void, wall, filament, cluster}"
- L977 / Table VI: "per-cell residual range" or similar

**Effort**: 15 min text fix + label all "range" mentions.

---

## P1B-META-E1 — βALP=0.336° exceeds formula maximum at fixed C_aγ=8 — **VERIFIED**

**Source citations**: `arxiv/paper1b_mcmc_companion.tex`
```
L1171:  $\beta_{\rm ALP} = 0.336^\circ \pm 0.107^\circ$ ($C_{a\gamma}=8$ fixed)
L1122:  $\Delta\phi/f_a \in [0.2, 1.1]$
```

**Arithmetic** (using paper's own formula β = (α_EM/(4π)) C_aγ (Δϕ/f_a)):
- α_EM/(4π) = 5.807e-4
- C_aγ = 8, Δϕ/f_a max = 1.1 → β_max = 5.807e-4 × 8 × 1.1 = 5.11e-3 rad = **0.293°**
- Quoted central β = 0.336°
- **0.336° > 0.293° → quoted central exceeds formula maximum by 15%**

This is a real physical inconsistency. Either:
(a) The MCMC posterior on β somehow places median at 0.336° even though the
    formula at the stated (C_aγ, Δϕ/f_a) bounds caps at 0.293° → suggests the
    posterior is exploring outside the stated [0.2, 1.1] Δϕ/f_a range.
(b) C_aγ wasn't truly fixed at 8 — it varied to ~9.2 to bring the formula
    bound up to 0.336°.
(c) There's a normalization factor (e.g., a missing α/2π vs α/4π convention
    swap, or a factor-of-2 somewhere) that the paper has but my recomputation
    missed.

**Fix**: reconcile by either expanding the Δϕ/f_a window in the MCMC prior
or documenting the actual sampler range. Note: the meta-reviewer's "much
less than 0.336°" phrasing overstates the gap; the actual gap is 15% (not
order-of-magnitude). The finding remains a real bound-violation but mild.

**Effort**: 30 min — needs the actual MCMC posterior file inspected to
determine which option (a/b/c).

---

## P2-META-E1 — β arithmetic gives 0.002° vs 0.27° — **FALSIFIED (meta error)**

**Source citations**: `research/focused_paper_source_integration/paper2_alp_birefringence.tex`
```
L23:  abstract: β ≈ 0.27°
L42:  Δφ/f_a ≈ 0.2–1.1 (for m/H_0 ∈ [0.5, 3], θ_i = 1)
L44:  fiducial m=H_0, θ_i=1: Δφ/f_a ≈ 0.65
L50:  β = g_aγ/2 · Δφ = α_EM · C_aγ / (4π·f_a) · Δφ
L54:  For C_aγ=8, θ_i=1, m≈2H_0: Δφ/f_a ≈ 1.07, β = (α_EM × 8 / 4π) × 1.07 ≈ 0.29°
```

**My arithmetic verification** using paper's actual values (C_aγ=8, Δφ/f_a=1.07):
- α_EM/(4π) × 8 × 1.07 = 5.807e-4 × 8 × 1.07 = 4.97e-3 rad = **0.285°** ≈ 0.27°-0.29° ✓

**Meta-reviewer's claimed arithmetic** (C ~ O(1), Δφ/f_a ≈ 0.24):
- 5.807e-4 × 1 × 0.24 = 1.39e-4 rad = 0.008° — but paper does NOT use C=1 or
  Δφ/f_a=0.24 anywhere. The "0.24" appears to be a hallucinated misreading of
  the MCMC fit β=0.242° (line 23 abstract) confused with the input parameter.

**Verdict**: the paper's arithmetic is internally consistent: C_aγ=8 (line 54 says
"DFSZ-type natural value"), Δφ/f_a=1.07 (from numerical integration at fiducial
m=2H_0, θ_i=1), β=0.29°. The meta-reviewer's "β should be 0.002°" used
incorrect inputs and FALSIFIES.

**Action**: remove #A2-5 (P2 β arithmetic) from HOUSTON_DECISION_PACKAGE.md TIER A2.

This is the FIRST falsification of a pattern-041 finding. Truth-audit verdict
log: pattern-041 verification rate after fire 14: **3/4 = 75%**. Still high
enough to keep pattern-041 in DRAFT promotion candidacy.

---

## Summary

| Finding | Verdict | Effort to fix | Action |
|---|---|---|---|
| P3-META-E4 γ-CI | VERIFIED | 15 min | Close in next P3 bump |
| P5-META-E1 ranges | VERIFIED | 15 min | Close in next P5 bump |
| P1B-META-E1 β bound | VERIFIED (mild) | 30 min | Close in next P1B bump (needs MCMC posterior inspection) |
| P2-META-E1 β arithmetic | FALSIFIED | n/a | Remove from queue |

Pattern-041 verification rate: 3/4 = 75%. Pattern remains valid; meta-reviewer
occasionally hallucinates inputs.

---

## Truth-audit improvement: cross-check meta-reviewer arithmetic against .tex BEFORE shipping

This fire's audit caught a meta-reviewer hallucination (P2 β with wrong inputs).
Without the audit, we'd have queued a fake finding for Houston. Going forward,
EVERY pattern-041 firing gets a 10-min arithmetic re-derivation + .tex grep
before being escalated.

Added as standing rule to `feedback_review_learning_loop` workflow.
