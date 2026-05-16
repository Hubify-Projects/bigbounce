# P4_v1098 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-16_0230pt_P4_v1098_R16_R-round_real
**Wall time**: 50.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=83564, completion=5332, reasoning=4018, total=88896

---

### Truth-Audit of v1.0.98 Closures
| Prompt Check | Status | Location of Failure / Regression |
| :--- | :--- | :--- |
| (a) Verify all 11 closures | **FAIL** | Multiple regressions found (see below). |
| (b) Convergent regressions | **FAIL** | Sec VI.C reinstates the 2.5× gap factor explicitly deleted in the abstract. |
| (c) Parity-violating overclaim | **FAIL** | Abstract and Sec IV.C still call the dipole the "parity-violation observable". |
| (d) Data Availability tag | **FAIL** | Footnote 2 and Sec VIII point to `paper4-v1.0.97`, not `v1.0.98`. |
| (e) Iye:2026P6 in-body text | **FAIL** | Sec V.A still says "remains in preparation at the time of this version freeze". |
| (f) $f_{\rm sky}$ drift | **FAIL** | 0.494 and 0.4938 persist in Tables I, III, VIII, and Sec IV.C, VII. |
| (g) 0.75% vs 0.29% gap | **FAIL** | Sec VI.C calls the 2.5× cross-sample ratio a "standard Fisher-vs-empirical factor". |
| (h) HC-broad-0.6 rename | **FAIL** | Sec IV.J and VI.D use `HC-spiral_p>0.6` and `HC-spiral-0.6` for the 949,584 cut. |

***

## PAPER-GEM-B1: BLOCKER - Contradiction on Parity vs Isotropy (Prompt item c)
**Section:** Abstract & Section IV.C
**Issue:** The abstract correctly caveats that the $\ell=1$ dipole is parity-EVEN (an isotropy test, not a parity test), but later in the same abstract explicitly contradicts this by stating "the parity-violation observable is the dipole, not the monopole." Section IV.C repeats this error: "The parity-violation signature of interest is the large-scale dipole". This violates the rigorous symmetry derivation in Section VI.E.
**Fix:** Globally replace "parity-violation observable is the dipole" with "isotropy-violation observable is the dipole", and scrub all remaining instances of "parity-violating dipole" in favor of "isotropy-breaking dipole".

## PAPER-GEM-M1: MAJOR - Stale Data Availability Tags (Prompt item d)
**Section:** Footnote 2 & Section VIII (Data Availability)
**Issue:** The closure required updating the reproducibility release tags to `paper4-v1.0.98`. Both Footnote 2 and the Data Availability section still point to the stale `paper4-v1.0.97` tag.
**Fix:** Update the GitHub release tag URLs and text in Footnote 2 and Section VIII from `paper4-v1.0.97` to `paper4-v1.0.98`.

## PAPER-GEM-M2: MAJOR - Iye:2026P6 "In Preparation" Regression (Prompt item e)
**Section:** Section V.A
**Issue:** The bibliography correctly lists Iye & Yagi (2026) as public (arXiv:2605.05570), but the in-body prose in Section V.A still contains the stale text: "...but the paper remains in preparation at the time of this version freeze...".
**Fix:** Delete the "remains in preparation at the time of this version freeze" clause in Section V.A and update the prose to reflect its published/public status.

## PAPER-GEM-M3: MAJOR - 2.5x Gap Factor Confabulation Regression (Prompt item g)
**Section:** Section VI.C
**Issue:** The abstract correctly deletes the 2.5× gap factor as a cross-sample arithmetic confabulation (comparing HC empirical $N=471k$ to full-catalog Fisher $N=3.2M$). However, Section VI.C regresses by explicitly reinstating it: "the ~2.5x gap between the analytic Fisher floor and the empirical MC threshold is the standard Fisher-vs-empirical factor reported in the dipole-recovery literature."
**Fix:** Delete the sentence in Section VI.C claiming the ~2.5× gap is a "standard Fisher-vs-empirical factor".

## PAPER-GEM-m1: minor - Inconsistent $f_{\rm sky}$ Drift (Prompt item f)
**Section:** Tables I, III, VIII, Section IV.C, Section VII
**Issue:** The closure anchored the canonical mask sky fraction to $f_{\rm sky} = 0.49005$ (which appears correctly in Table IV). However, Table I, Table III, Section IV.C, Section VII, and Table VIII still use the stale $0.494$ or $0.4938$ values.
**Fix:** Globally synchronize the canonical mask sky fraction to `0.49005` to match the Table IV anchor.

## PAPER-GEM-m2: minor - Inconsistent 'HC-broad-0.6' Nomenclature (Prompt item h)
**Section:** Section IV.J & Section VI.D
**Issue:** Table VI correctly uses the renamed `HC-broad-0.6` nomenclature for the $N=949,584$ cut. However, Section VI.D refers to this exact same cut as `HC-spiral-0.6`, and Section IV.J refers to it as `HC-spiral_p>0.6`.
**Fix:** Standardize the $N=949,584$ cut nomenclature to `HC-broad-0.6` globally across Section IV.J and Section VI.D.
