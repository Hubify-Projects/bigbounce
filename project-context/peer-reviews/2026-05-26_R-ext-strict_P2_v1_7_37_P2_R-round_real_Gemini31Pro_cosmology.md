# P2 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-strict_P2_v1_7_37
**Wall time**: 45.0s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=33588, completion=6028, reasoning=5205, total=39616

---

## PAPER-GEM-B1: BLOCKER - Audit-Trail and AI-Vendor Prose Contamination
**Location:** Abstract, Section VI.C, Table II caption, Section X.
**Issue:** The manuscript body is littered with raw internal AI-review audit trails and version-control metadata (e.g., "corrected v1.7.35 R-next-c-MAJ-1 from earlier ~6 via scipy.stats.norm", "corrected v1.7.36 R-next-d-MAJ-2", "corrected v1.7.36 R-next-d-MIN-2"). 
**Fix:** Purge all internal version-history, AI-prompting artifacts, and audit-trail prose from the compiled manuscript body prior to journal submission.

## PAPER-GEM-B2: BLOCKER - Missing Data Vector Definitions Table
**Location:** Section IX.D.
**Issue:** The paper claims a $9.9\sigma$ detection significance from a 6-bin joint Fisher forecast, but explicitly defers the actual Fisher inputs ($k_{\min}(z)$, $\bar n(z)$, $b_1$, $b_\phi$, $\sigma_z$, volume) to an unpublished "companion artifact". A headline quantitative claim cannot rest on withheld data vectors.
**Fix:** Provide the full 6-bin Fisher input table in the manuscript, or completely remove the $9.9\sigma$ quantitative claim.

## PAPER-GEM-M1: MAJOR - Gauge-Frame vs. Physical-Frame Observable Confusion
**Location:** Abstract and Section X.
**Issue:** The text claims SPHEREx measures the "gauge frame" $\fnl$ and that the physical-frame (CFC) value is "not the on-sky observable." This is theoretically backwards: surveys measure the physical gauge-invariant galaxy density, from which the gauge-frame primordial parameter is inferred by marginalizing over relativistic projection effects.
**Fix:** Correct the theoretical framing to state that surveys measure the physical observable, requiring explicit GR projection modeling to extract the gauge-frame $\fnl$.

## PAPER-GEM-M2: MAJOR - Stale Release Tag Mismatch
**Location:** Title page date vs. Data and Code Availability section.
**Issue:** The title page declares the manuscript as version "v1.7.37", but the Data and Code Availability section points to a stale, mismatched release tag "v1.7.26-paper2".
**Fix:** Update the GitHub release tag in the Data Availability section to match the submitted manuscript version.

## PAPER-GEM-M3: MAJOR - Unsubstantiated "Bounce Prediction" for ALP Birefringence
**Location:** Section IX.E.
**Issue:** The paper claims $\beta \approx 0.27^\circ$ is a "bounce prediction" for cosmic birefringence, but immediately admits it depends on free parameters (ALP coupling $g_{\phi\gamma}$ and mass $m_a$). This conflates the parameter-free scalar $\fnl$ mechanism with a highly model-dependent axion accommodation.
**Fix:** Remove the claim that $\beta \approx 0.27^\circ$ is a bounce prediction, and reclassify it strictly as a model-dependent accommodation.

## PAPER-GEM-m1: minor - Insufficient MC Size for Injection/Recovery
**Location:** Section II.A.
**Issue:** The injection/recovery test used to validate the template overlap $r_{\rm measured} = 0.90 \pm 0.01$ uses only 200 Monte Carlo realizations, which is statistically insufficient to robustly quote a $\pm 0.01$ error bar.
**Fix:** Increase the injection/recovery MC ensemble to $\geq 10^4$ realizations, or widen the reported error bar to reflect the small-sample variance.
