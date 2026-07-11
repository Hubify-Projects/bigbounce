# INT Claude-subscription Review — P3 v3.1.155 — claude-opus-4-8
paper: P3  version: v3.1.155  tex: pipelines/p3_anomaly_engine/paper3_draft.tex
modality: full-repo Claude Code subscription subagent (claude -p)
UTC: 2026-07-11T16:22:23Z
context-note: rebuild wave 1/2 on v3.1.155: +1.13->+1.14 sigma precision fix at 7 sites (DP3-19); no other changes

======================================================================
RAW RESPONSE (verbatim):
======================================================================

All DP3-19 changes verify exactly against the committed artifact. Let me confirm my arithmetic manually (I've computed by hand) and note the one residual issue: the displayed 3-sig-fig posterior does not reproduce the stated σ-shifts.

Verified against `savage_dickey_2026-05-29.json` and `results.json` (γ mean = 2.56647, std = 0.38183):
- `matter_bounce_3p0 = 1.13543` → **+1.14σ** ✓ (all 7 sites updated, 0 stale +1.13σ)
- `smbhb_13_3 = 4.6274` → **+4.63σ** ✓ (from v3.1.154)
- `B_matter_bounce_vs_smbhb = 7137.6` → 7.14×10³ ✓; `B_MB/free = 3.228` → 3.23 ✓; `B_SMBHB/free = 4.522e-4` → 4.52×10⁻⁴ ✓
- F₀ = 1/8.98² = 0.0123993 → **0.01240** ✓; 1/σ² = 0.01240 + 0.0747·0.19² = 0.015097 → 0.01510 ✓; σ = 8.14 ✓; envelope lower edge 0.84 → 3.92 ✓

But note the display-precision gap: from the *printed* γ = 2.567 ± 0.382 a reader computes (3.0−2.567)/0.382 = **1.13σ** and (4.33−2.567)/0.382 = **4.62σ**, not the stated 1.14/4.63. The full-precision mean (2.5665) is never shown.

---

**(1) VERDICT: MINOR REVISIONS**

**(2) ISSUES:**

1. **[MINOR]** §nanograv `paper3_draft.tex:1562` (and abstract:1003, discussion:1627, contributions:1645, Table footnote:1866) — The +1.14σ / +4.63σ parameter shifts are correct against the committed chain (`matter_bounce_3p0 = 1.13543`, `smbhb_13_3 = 4.6274`), but they are *not reproducible from the printed numbers*: (3.0 − 2.567)/0.382 = 1.13 and (4.33 − 2.567)/0.382 = 4.62. The reconciling digit (mean = 2.5665) is never displayed. Fix cleanly by printing γ = 2.566 ± 0.382 (which reproduces both 1.14σ and 4.63σ) or add a one-clause footnote that the shifts use the unrounded posterior mean 2.5665. This is the exact class of display-vs-full-precision mismatch DP3-19 was meant to close, and it is now internally consistent but still not reader-reproducible.

2. **[MINOR]** §fnl `paper3_draft.tex:1529` — F₀ = 1/(8.98)² is now written 0.01240 (correct: 0.0123993), consistent downstream (0.01510, σ = 8.14, envelope [3.92, 8.98] all verify). No action needed beyond confirming the same 5-sig-fig convention is used everywhere F₀ appears; this item is resolved.

3. **[MINOR]** §fnl `paper3_draft.tex:1520–1529` — The multi-tracer f_NL "forecast" is a genuine null (de-biased α² = 0, σ(f_NL) returns the 8.98 baseline exactly; central 9.4% shift at 0.29σ). This is disclosed honestly and repeatedly, but for a PRD reader the section still leads with the convex central 8.14 before the envelope; consider stating the null (returns-baseline) result in the first sentence of the Fisher-forecast paragraph rather than after the convex central value.

4. **[MINOR]** §nanograv `paper3_draft.tex:1562–1565` — The Savage-Dickey B_MB/SMBHB = 7.14×10³ "decisive" claim is immediately (and correctly) caveated as decisive only against the idealized circular-orbit reference, since environmentally-flattened SMBHB models reach γ ~ 2.5–3. Given that caveat effectively neutralizes the discriminating power, the "decisive on Jeffreys' scale" phrasing risks over-reading; recommend softening the headline to match the caveat's actual scope.

**(3)** The central claim — a reproducible, validated catalog-grade subset of 268,519 anomaly sources — is supported and independently recomputable from committed artifacts; the DP3-19 precision fix is arithmetically correct and fully propagated, and the two cosmological applications are correctly presented as null secondary demonstrations, not detections.
