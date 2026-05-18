# P3_v3151_R13 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1430pt
**Wall time**: 72.9s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=65859, completion=9946, reasoning=8874, total=75805

---

## PAPER-GEM-B1: Unphysical Linear Fisher Bounds Retained as Headlines (BLOCKER)
**Location:** Abstract and Section 5
**Issue:** The text continues to quote the unphysical linear-extrapolated Fisher bounds ($\sigfnl = 8.27 \pm 2.37$ and $\sigfnl^{\rm GS} = 2.28 \pm 7.43$) as the primary grammatical subjects of the forecast sentences, followed by parentheticals explaining that these bounds violate Fisher information positivity (e.g., implying a mathematically impossible lower bound of $-5.15$). Section 6.4(j) explicitly notes that replacing these with the corrected asymmetric envelopes was "queued for v3.1.48+ headline-replacement", but in v3.1.51 the unphysical numbers are still the primary quoted values. You cannot quote a headline error bar that you explicitly prove is mathematically impossible in the very next sentence.
**Fix:** Replace the linear-extrapolated $\pm$ values in the Abstract and Sec 5 directly with the positivity-respecting asymmetric envelopes (e.g., "yields a central $\sigfnl = 8.14$ with a $1\sigma$ positivity-respecting envelope of $[3.92, 8.98]$"). Remove the linear-propagation numbers entirely to prevent them from being cited.

## PAPER-GEM-M1: Table I Caption Contradicts Native Thresholds (MAJOR)
**Location:** Table I caption and footnotes
**Issue:** The Table I caption claims "a fixed canonical-S cut at S > 5.0 for the three spectroscopic surveys (DESI DR1, SDSS DR18, LAMOST DR10)". However, the actual counts reported in the table for SDSS (77,905) and LAMOST (113,342) use top-percentile continuity cuts ($S \geq 0.1060$ and $S \geq 0.4613$), as detailed in the footnotes. Applying the strict $S>5$ cut would yield only 12 and 2,054 anomalies, respectively. The caption is factually incorrect for the native SDSS/LAMOST slices that form the catalog.
**Fix:** Update the Table I caption to accurately state that SDSS and LAMOST counts use top-percentile continuity slices ($S \geq 0.1060$ and $S \geq 0.4613$), restricting the "fixed canonical-S cut at S > 5.0" claim to DESI alone.

## PAPER-GEM-m1: Stale Deferral List Items (minor)
**Location:** Section 6.4, "Real cross-vendor R-round deferrals" block, item (g)
**Issue:** Item (g) lists the 5-fold Jaccard internal inconsistency as an open "v3.1.46+ task to reconcile the narrative", but the narrative was already successfully reconciled in Sec 2.2 and Sec 6.4(i) (which now explicitly state the full 47k pool was scored). The deferral list was not cleaned up after the fix was implemented.
**Fix:** Remove item (g) from the active deferral list since the narrative fix is already implemented in the body text.

## PAPER-GEM-m2: Version Number Desync on Verification Table (minor)
**Location:** Table I footnote $\S$ vs. Section 6.4 caveat (f)
**Issue:** Table I footnote $\S$ states the BigAE/IsolationForest intersection count is "queued for the v3.1.45 verification table", while Sec 6.4 caveat (f) correctly notes that it missed v3.1.45 and is "queued for the v3.1.46+ verification table".
**Fix:** Update Table I footnote $\S$ to say "v3.1.46+" to match the updated deferral schedule in Sec 6.4(f).

## PAPER-GEM-n1: 95% CI vs 1$\sigma$ CI in Fisher Positivity Text (nit)
**Location:** Section 5
**Issue:** For the full sample, the text quotes the 95% CI envelope $[2.4, 8.98]$ derived from the $\alpha^2$ form, but compares it directly against the $1\sigma$ linear error bar $\pm 2.37$. To be mathematically parallel with the Gold+Silver subset (which uses the $1\sigma$ envelope $[0.94, 8.98]$), the full sample should also explicitly report its $1\sigma$ positivity-respecting envelope.
**Fix:** Add the $1\sigma$ positivity-respecting envelope $[3.92, 8.98]$ to the full-sample Fisher forecast text in Sec 5 to ensure consistent statistical reporting across subsets.
