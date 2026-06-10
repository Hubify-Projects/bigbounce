# P4 2026-06-04_R6clean — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 187.0s

---

## Referee Report: Paper P4

### ESSENTIAL Revisions

**P4-E1: Abstract and Sec. VII (Conclusions) – Misleading decomposition presentation**  
- **Problem**: The abstract claims a "decomposition 99.3%/12%/88%/25%" as if these percentages are additive components of a single whole. However, these values reference distinct systematic contributions at different analysis stages (pre-MASTER leakage: 99.3%, post-MASTER monopole leakage: 12%, residual systematics: 88%, leg-proxy contribution: 25% of residual). Presenting them as a unified decomposition implies arithmetic consistency that does not exist.  
- **Required Fix**: Restructure the abstract to clarify that these are independent diagnostics (e.g., "99.3% of pre-MASTER power is explained by monopole leakage; 12% of post-MASTER residual is from monopole leakage, with 88% from other systematics; 25% of the latter is attributed to a leg-proxy").  

**P4-E2: Sec. IV C (Results) and Sec. VII (Conclusions) – Inadequate qualification of σ values**  
- **Problem**: While Table II and the abstract note that σ values are not comparable across null procedures, the conclusions (Sec. VII) present the subsample-mask null (−0.12σ) and canonical-mask residual (+3.64σ) without reiterating this critical caveat. This risks readers misinterpreting the +3.64σ as contradicting the −0.12σ null.  
- **Required Fix**: In Sec. VII, explicitly state: "The +3.64σ canonical-mask residual and −0.12σ subsample-mask null are defined under different null procedures (Table II) and cannot be directly compared."  

---

### MAJOR Revisions

**P4-M1: Abstract and Sec. VI C – Untraced 0.75% sensitivity threshold**  
- **Problem**: The falsification criterion (abstract and Sec. VII) claims a "demonstrated empirical 50%-recovery-at-3σ threshold" of 0.75% but does not cite the specific table (Table XVI) or section (Sec. VI C) where this is derived. The value is load-bearing for the paper's claim of sub-percent sensitivity.  
- **Required Fix**: Add inline citations to Table XVI/Sec. VI C when stating 0.75% in the abstract and conclusions. Ensure the injection-recovery script is included in the public repository with a documented path.  

**P4-M2: Sec. IV D (Results) – Ambiguous residual decomposition**  
- **Problem**: The 25% "leg-proxy" contribution (Table VIII) is ambiguously presented as part of the 88% residual systematics but lacks a clear basis. The text states it is a "partial closure lower bound," but no calculation shows how 25% relates to the 88% (e.g., 25% of what?).  
- **Required Fix**: Quantify the 25% explicitly (e.g., "accounts for 25% of the canonical-mask ℓ=1 amplitude") and clarify its independence from the 88% residual. Provide a cross-reference to the leg-stratification results in Table XI.  

**P4-M3: Sec. VI G (Discussion) – Unvalidated monopole origin**  
- **Problem**: The 9.5σ global CW-fraction monopole (0.4974 ± 0.0003) is attributed to Galaxy Zoo 1 (GZ1) training bias without conclusive evidence. The SpArcFiRe cross-check (Sec. V C) is only "consistent" with this hypothesis but does not rule out physical or PSF-driven effects.  
- **Required Fix**: Either: (a) conduct a matched-pipeline test with a non-GZ1 label source (e.g., SpArcFiRe on the full catalog), or (b) weaken claims to "likely reflects GZ1 bias" and discuss alternative explanations in Sec. VI G.  

---

### MINOR Revisions

**P4-m1: Abstract – Redundant "all file extensions removed"**  
- **Problem**: The phrase "all file extensions removed" in the abstract appears unrelated to scientific content (likely a metadata artifact).  
- **Required Fix**: Remove the phrase.  

**P4-m2: Sec. III E (Methods) – Inconsistent D4-TTA reporting**  
- **Problem**: The per-galaxy argmax flip rate (21.4%) is emphasized in Table II but downplayed in Sec. III E as "not primary," creating confusion about its impact on hard-label diagnostics.  
- **Required Fix**: Clarify in Sec. III E that the 21.4% flip rate directly affects hard-label-based uncertainties (Table X, XVI) and justify the 1.21× error widening factor.  

**P4-m3: Sec. IV B (Results) – Unresolved tier discrepancies**  
- **Problem**: Catalog A (raw), B (Platt-scaled), and C (equivariant) report different global CW fractions (Table V), but the narrative does not explain why Catalog B (+0.4% excess) fails to correct the bias fully.  
- **Required Fix**: Briefly note in Sec. IV B that Platt scaling inherits CE-ResNet biases and is insufficient for parity tests, justifying the focus on Catalog C.  

---

### NIT Revisions

**P4-n1: Throughout – "canonical" overuse**  
- **Problem**: The term "canonical" appears 127 times (e.g., "canonical mask," "canonical residual"), occasionally redundant (e.g., "canonical canonical-mask" in Sec. IV D).  
- **Required Fix**: Replace non-essential instances (e.g., "the canonical analysis" → "this analysis") and fix the duplicate phrase in Sec. IV D.  

**P4-n2: Sec. VI C (Discussion) – Undefined "pCW (n̂)" convention**  
- **Problem**: The amplitude convention \(p_{\text{CW}}(\hat{n}) = \frac{1}{2}(1 + A \cos \theta)\) is introduced in Sec. VI C without derivation, making the Fisher floor discussion hard to follow.  
- **Required Fix**: Define the convention when first used in Sec. IV C.  

---

## Summary Recommendation  
**MAJOR REVISIONS**  

Justification: The paper reports a significant null result with a rigorously produced catalog but has major issues in presentation clarity. The decomposition in the abstract (99.3%/12%/88%/25%) is misleadingly framed, and key numbers (0.75% sensitivity threshold) lack immediate traceability. The σ-comparability caveat is underemphasized in conclusions, risking misinterpretation. While the core science is robust (null dipole at ≥0.75% sensitivity), revisions are essential to:  
- Clarify the disjoint nature of the systematic contributions.  
- Explicitly tie all headline numbers to tables/methods.  
- Resolve ambiguity in the monopole-attribution narrative.  
The 54-page length is acceptable given the catalog scale and multi-null diagnostics, but redundant phrasing (e.g., "canonical") should be reduced.