# P5 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v2_P5_v0_1_32
**Wall time**: 167.5s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=27876, completion=8440, reasoning=8184, total=36316

---

# Adversarial Peer Review: Provenance Audit

No BLOCKER or MAJOR finding; only a minor rounding inconsistency flagged. All other load‑bearing scalars in the abstract and conclusions trace to named JSON/CSV artifacts or to simple arithmetic from those artifacts.

## PAPER-DEE-1 (minor)
- **Location:** Conclusions, paragraph 1.
- **Issue:** The conclusion lists the four V‑Web CW fractions as `{0.484, 0.503, 0.498, 0.496}` and then states “a range of 1.98 percentage points”. The displayed fractions are rounded to three decimal places; computing the range from those rounded values gives `0.503 − 0.484 = 0.019 = 1.9` pp, not 1.98 pp. The reader cannot reproduce the 1.98 pp figure from the numbers shown in the conclusion.
- **Fix:** Either report the fractions with the same precision used in the abstract (four decimal places, e.g. `0.4836, 0.5034, …`) or round the range to `1.9 pp` to match the displayed rounding.
