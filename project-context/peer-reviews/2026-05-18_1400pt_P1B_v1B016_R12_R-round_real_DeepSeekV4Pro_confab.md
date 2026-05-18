# P1B_v1B016_R12 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1400pt
**Wall time**: 308.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=17432, completion=8746, reasoning=7857, total=26178

---

## PAPER-DEE-C1: MAJOR – Conclusions misstate NaMaster systematic bias bound relative to detailed analysis

**Location:** Section 8 (Conclusions), line `“the deconvolution pipeline recovers injected birefringence angles with bias \(\leq 0.032^\circ\) at SNR consistent with the ACT-noise floor.”`

**Issue:** Section 4 explicitly splits the measured pipeline‑recovery bias into \(0.032^\circ\) (for the \(0.27^\circ\) injection) and \(0.040^\circ\) (for the \(0.342^\circ\) injection) and states “we carry forward the \(0.04^\circ\) level in the worst‑case injection as the NaMaster systematic floor.” The Conclusions erroneously quote the bias as \(\leq 0.032^\circ\), contradicting the body text and under‑reporting the validated systematic floor.

**Fix:** Amend the Conclusions to reflect the amplitude‑dependent bias, e.g., *“bias up to \(0.040^\circ\) in the worst‑case injection.”* or at minimum *“bias consistent with the \(0.032^\circ\)–\(0.040^\circ\) injection‑dependent range reported in Section 4.”*

## PAPER-DEE-C2: MAJOR – Broken cross‑reference `\ref{sec:results}`

**Location:** Section 8 (Conclusions), line *“per the 3‑vendor convergent R2 BLOCKER (Sec.~\ref{sec:results}, \emph{Model‑comparison statistics} paragraph).”*

**Issue:** The manuscript contains no section labelled `sec:results`; the referenced paragraph lies within Section 5 (“Cosmological Fits and Model Comparison”) but that section has no `\label{sec:results}`. Therefore the LaTeX will generate an undefined reference, leaving the reader with no hyperlink and a broken citation. This introduces a direct regression of the broken‑section‑reference fixes claimed in the R7 inventory.

**Fix:** Insert a `\label{sec:results}` at the appropriate point in Section 5 (e.g., near the “Model‑comparison statistics” paragraph) or change the reference to `\ref{sec:cosmo_fits}` and adjust the phrasing to point to the relevant paragraph.

## PAPER-DEE-C3: minor – Numerical inconsistency in full‑tension \(H_0\) inside the iter2‑caveat (c) vs. Table 1

**Location:** Section 5, caveat (c) of Table 1B: *“The full‑tension chain returns \(H_0 = 67.69 \pm 1.06\) km/s/Mpc …”*

**Issue:** Table 1 (and all other occurrences in the abstract, Sec. 3, and Conclusions) uniformly lists the full‑tension \(H_0\) as \(67.68 \pm 1.06\,\text{km}\,\text{s}^{-1}\,\text{Mpc}^{-1}\). The caveat therefore introduces a spurious \(0.01\) deviation with no accompanying explanation or archival provenance.

**Fix:** Correct the caveat to read \(67.68 \pm 1.06\) to match the verified Table 1 value and avoid confusion about which figure is the authoritative posterior.

## PAPER-DEE-C4: minor – Stale version entry in cross‑paper status table for P1(b)

**Location:** Table 2 (Cross‑Paper Verification Status), row for P1(b): `v1B.0.13` while the paper’s own `\paperVersion` is `v1B.0.16`.

**Issue:** The table claims the companion paper’s last formal version is `v1B.0.13`, but the document itself declares version `v1B.0.16`. This inconsistency persists from an earlier iteration and misrepresents the current state of P1(b) for any reader referencing the cross‑paper summary.

**Fix:** Update the version string in Table 2 to `v1B.0.16` (and adjust the readiness percentage if it has changed since v1B.0.13).
