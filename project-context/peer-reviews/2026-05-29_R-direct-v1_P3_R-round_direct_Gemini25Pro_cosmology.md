# P3 R-round — DIRECT vendor — Gemini-2.5-Pro cosmology-physics reviewer

**Model**: `gemini-2.5-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-05-29_R-direct-v1
**Wall time**: 51.8s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=76637, completion=302, total=82414

---

## PAPER-GEM-B1
**Finding Class:** BLOCKER
**Section:** §5 Cosmological Applications

**Issue:** The empirical bias enhancement `α` is measured from the angular auto-correlation of a 5,384-object "QSO-candidate" sample whose redshift distribution is almost entirely unknown. This effective, redshift-averaged bias cannot be directly inserted into a 3D Fisher forecast for `fnl`, which is highly sensitive to tracer redshift.

**Fix:** The forecast must be restricted to the small subset of tracers with known redshifts, or the analysis must explicitly marginalize over a range of plausible redshift distributions for the candidate sample. The current approach overstates the robustness of the forecast.

## PAPER-GEM-B2
**Finding Class:** BLOCKER
**Section:** §5 Cosmological Applications

**Issue:** The multi-tracer bias enhancement factor `α` is defined and measured as an internal ratio between a QSO-candidate subset of anomalies and the full anomaly sample (`b_QSO_cand / b_full_anomaly - 1`). However, the Fisher forecast improvement is calculated relative to a baseline of standard DESI QSOs, which requires the bias of the anomaly sample relative to the standard QSOs, a quantity that is never measured.

**Fix:** Measure the bias of the anomaly tracer sample relative to the standard DESI QSO sample, for instance via cross-correlation. Use this externally-referenced bias ratio in the Fisher forecast.
