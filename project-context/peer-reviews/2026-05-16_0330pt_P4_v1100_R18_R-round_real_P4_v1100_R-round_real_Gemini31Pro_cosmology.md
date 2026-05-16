# P4_v1100 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0330pt_P4_v1100_R18_R-round_real
**Wall time**: 52.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=83733, completion=6066, reasoning=4971, total=89799

---

## Truth-Audit & Convergence Table

| Category | Status | Classification | Notes |
| :--- | :--- | :--- | :--- |
| **Abstract Parity Language** | FAILED CLOSURE | BLOCKER | "parity-violation observable is the dipole" remains in Abstract. |
| **Table I $f_{\rm sky}$** | FAILED CLOSURE | BLOCKER | Row (iv) missed in global 0.494 $\to$ 0.49005 sweep. |
| **Redundant Phrasing** | NEW REGRESSION | MAJOR | Botched sed replacements created mangled, stuttering sentences in Sec V.F and VI. |
| **Body Parity Language** | DIMINISHING-RETURNS | minor | "parity-preference test" / "parity-dipole" persist in Sec III.G, IV.C, Table III. |
| **Stale Tags** | DIMINISHING-RETURNS | nit | `v1.0.99` remains in bibliography LaTeX comment. |
| **MASTER-not-same-data** | DEFERRED | PERSISTENT-RESIDUAL | Explicitly acknowledged in Table I footnote b. |
| **face_on +4.31σ vs +0.43σ** | DEFERRED | PERSISTENT-RESIDUAL | Explicitly acknowledged in Table VIII reconciliation. |
| **0.75% HC-only threshold** | DEFERRED | PERSISTENT-RESIDUAL | Explicitly scoped to HC-subsample in Sec V.F. |

## PAPER-GEM-B1: Failed Closure on Abstract Parity Language (BLOCKER)
**Location:** Abstract, 5th paragraph (`the parity-violation observable is the dipole, not the monopole.`)
**Issue:** Closure (2) mandated replacing "parity-violation observable/hypothesis is the dipole" with "isotropy-breaking observable/hypothesis". The Conclusions section was updated, but the Abstract instance was missed, directly contradicting the strict symmetry classification established in Sec V.H.
**Fix:** Change to `the isotropy-breaking observable is the dipole, not the monopole.`

## PAPER-GEM-B2: Failed Closure on Table I $f_{\rm sky}$ (BLOCKER)
**Location:** Table I, Row (iv)
**Issue:** Closure (3) mandated a global sweep of Table I rows (iii, iv, v) to update $f_{\rm sky}=0.494 \to 0.49005$. Row (iv) "hemisphere LEE" was missed and still reads `0.494`.
**Fix:** Update Table I, row (iv) $f_{\rm sky}$ column to `0.49005`.

## PAPER-GEM-M1: Mangled Sed Replacements / Redundant Phrasing (MAJOR)
**Location:** Sec V.F (Paragraph 6) and Sec VI (Item 1)
**Issue:** A botched search-and-replace operation created severely mangled, stuttering sentences. Sec V.F reads: `the empirical $|A_{\rm dipole}| \geq 0.75\%$ empirical $50\%$-rec-$3\sigma$ amplitude threshold`. Sec VI reads: `we achieve a conservative empirical $50\%$-recovery-$3\sigma$ threshold of $\geq 0.75\%$ at the empirical $50\%$-recovery-$3\sigmaunit$ amplitude threshold`.
**Fix:** De-duplicate the phrasing. In Sec VI, use `we achieve a conservative empirical $50\%$-recovery-$3\sigma$ threshold of $|A_{\rm dipole}| \geq 0.75\%$`. In Sec V.F, use `the empirical $50\%$-recovery-$3\sigma$ amplitude threshold of $|A_{\rm dipole}| \geq 0.75\%$`.

## PAPER-GEM-m1: Residual Parity-Dipole Language in Body (minor)
**Location:** Sec III.G, Sec IV.C, Table III Caption
**Issue:** Despite the V.H symmetry classification correctly identifying the dipole as an isotropy-breaking (parity-even axial-vector) test, residual text still conflates the two. Sec III.G: `The parity-preference test of this paper is the \emph{dipole}`. Sec IV.C: `the load-bearing parity-dipole observable`. Table III: `the dipole-parity observable`.
**Fix:** Change "parity-preference test" to "isotropy-breaking test" and "parity-dipole observable" to "isotropy-breaking dipole observable" globally.

## PAPER-GEM-n1: Stale v1.0.99 Tag in Bibliography (nit)
**Location:** Bibliography, `\bibitem{Ivezic:2019}`
**Issue:** A stale tag remains in a LaTeX comment: `%% (cleaned v1.0.99 - removed stale NOTE commentary; canonical citation above)`.
**Fix:** Delete the comment line or update the tag to `v1.0.100`.
