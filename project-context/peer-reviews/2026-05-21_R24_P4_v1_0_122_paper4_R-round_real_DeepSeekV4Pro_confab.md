# paper4 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R24_P4_v1_0_122
**Wall time**: 212.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=89589, completion=8693, reasoning=8337, total=98282

---

# Adversarial Peer-Review: Provenance Audit of Scalars

## Finding 1: Per-Region CW Fractions Lack On-Disk Artifact (MAJOR)

**ID:** PAPER-DEE-M1  
**Location:** Table 5 (Sky Region Balance), supporting the claim “maximum regional asymmetry is 0.32%” (Conclusions bullet 2) and the abstract’s statement that the result is a factor ~6–12 smaller than Shamir’s ~3% asymmetry.  
**Issue:** The per-region CW fractions for the seven equatorial slabs (e.g., RA [0°,90°) = 0.4968, ∣Δ∣=0.32%) are used to derive the maximum regional asymmetry of 0.32%, which is the primary comparator against prior literature. The paper acknowledges in a footnote that the cited artifact (`global_cw_fraction.json`) contains only the global CW fraction and that “per-region values are manuscript-only at this version freeze.” No JSON, script output, or dataset partition is provided that produces these seven numbers, making it impossible for a reader or reviewer to independently verify the claimed 0.32% maximum asymmetry and the resulting factor-of-~9 discrepancy with Shamir’s results without re-implementing the RA/Dec splitting pipeline.  
**Fix:** Provide a dedicated per-region JSON (e.g., `per_region_cw_balance.json`) that records the CW/(CW+CCW) fractions and spiral counts for each of the seven regions, as committed under the `paper4-v1.0.122` release tag, or explicitly note that these numbers are unfinalized and will be backed by an artifact before journal submission.
