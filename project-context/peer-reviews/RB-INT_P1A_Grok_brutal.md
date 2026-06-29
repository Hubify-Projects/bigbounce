# P1A RB-INT — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=5223958f pages=32
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 193.2s

---

**Referee Report — Physical Review D**

**Manuscript:** Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes and Perturbation Transparency for Scalar Matter (Houston Golden)

**Date on manuscript:** June 29, 2026 (future date appearing in the rendered PDF)

**Finding P1A-E1 (ESSENTIAL)**  
Section: Title page (p. 1)  
Problem: The manuscript date is “(Dated: June 29, 2026)”. This date lies in the future relative to any possible submission or review cycle.  
Required fix: Remove or correct the date. A future date is an internal artifact that cannot appear in a submitted manuscript.

**Finding P1A-E2 (ESSENTIAL)**  
Section: Abstract + Sec. I (pp. 1–4) and repeated throughout  
Problem: The central claims (“channel-level closure”, “perturbation-transparency result”, “14 historical catalog entries”, “13 distinct barriers”) rest on results imported from “Paper I(b)”, “Paper II”, “Paper III”, “Paper IV”, and multiple works “in preparation”. The argument is not self-contained. Undefined symbols, MCMC posteriors, Fisher forecasts, and NaMaster pipeline validation are cited by companion label only.  
Required fix: All load-bearing numerical results and derivations must be reproduced in the present manuscript or the paper must be withdrawn. Standalone-reader test fails.

**Finding P1A-E3 (ESSENTIAL)**  
Section: Abstract (p. 1) vs. Sec. IV, IX, and Appendix B (pp. 11–19, 25)  
Problem: Abstract states that the four routes are “closed” and that the Holst sector “decouples”. Body repeatedly qualifies every closure as (a) channel-level only, (b) under an explicitly labeled phenomenological on-shell scaling ansatz (not a derivation), and (c) with the leading parity-odd operator having off-shell mass dimension +1 rather than the required +4. The abstract claim is materially stronger than the calibrated body statement.  
Required fix: Abstract must be rewritten to match the body’s final, caveat-laden conclusion exactly.

**Finding P1A-E4 (ESSENTIAL)**  
Section: Sec. X (pp. 19–20) and footnote a (p. 2)  
Problem: The “perturbation-transparency” theorem is derived by showing that the Holst dual contraction vanishes identically on the Levi-Civita connection (T = 0) via the algebraic Bianchi identity. The paper itself notes this is distinct from the Pontryagin density argument. No demonstration is given that the same vanishing holds order-by-order once the full set of omitted operators (Jackiw–Pi term, parity-odd four-fermion partner) is restored. The theorem is therefore conditional on the very truncation the paper elsewhere acknowledges is incomplete.  
Required fix: Either prove the result for the most general diffeomorphism-invariant parity-odd sector or retract the claim of a general transparency result.

**Finding P1A-M1 (MAJOR)**  
Section: Table I (p. 5) and Sec. XIII (p. 22)  
Problem: The “surviving testable prediction” f_NL = −35/8 is labeled a class-level matter-bounce result, not an ECH-specific prediction. The abstract nevertheless presents it as a central output of the ECH analysis.  
Required fix: Remove f_NL = −35/8 from any ECH-specific claim list or provide an explicit ECH-only derivation.

**Finding P1A-M2 (MAJOR)**  
Section: Sec. IV D (pp. 13–15) and Sec. IX (pp. 16–19)  
Problem: Route 4 is closed by a “naturalness/explanatory-deficit objection” rather than an amplitude mismatch. This is an aesthetic criterion, not a dynamical no-go. The paper simultaneously states that the same spectator-ALP coupling reproduces the observed β_obs inside the 1σ band once m_θ ∼ H_0 is allowed. The closure is therefore not amplitude-based and is not on equal footing with Routes 1–3.  
Required fix: Reclassify Route 4 or remove it from the enumerated “no-go” list.

**Finding P1A-M3 (MAJOR)**  
Section: Sec. II C and Appendix B (pp. 8, 25)  
Problem: The parity-odd operator (Eq. 6) is assigned off-shell mass dimension +1 by hand via a scaling ansatz. The paper acknowledges this is “not a derivation”. All subsequent amplitude-budget arguments rest on this ansatz. No power-counting or matching calculation to a UV completion is supplied.  
Required fix: Either promote the ansatz to a controlled EFT result or label every numerical bound that follows from it as conditional on the ansatz.

**Finding P1A-N1 (MINOR)**  
Section: Multiple figure captions and text (e.g., Fig. 1, p. 6)  
Problem: Several internal cross-references use labels (“Barrier 14”, “B14”, “Foundation A”) that are defined only inside the present manuscript but are presented as if they belong to a pre-existing catalog.  
Required fix: Ensure every label is introduced before use.

**Finding P1A-N2 (NIT)**  
Section: Throughout  
Problem: Repeated use of the phrase “channel-level closure” without a concise, one-sentence definition in the abstract or introduction.  
Required fix: Add a single-sentence definition on first use.

**Additional observations**  
- The manuscript is 32 pages long. The actual novel technical content (the Bianchi-identity argument in Sec. X and the 14-barrier catalog) occupies roughly 6–7 pages once all companion citations and repeated qualifications are removed. The length-to-substance ratio is excessive for PRD.  
- No effect-size or practical-significance statement accompanies any σ or “orders of magnitude” claim (e.g., “∼70 orders”, “∼60 orders”).  
- Several σ values (0.342° ± 0.094°, 0.215° ± 0.074°) are juxtaposed without an explicit statement that they are not directly comparable because they arise from different null hypotheses and masks.  
- The bibliography contains multiple “in preparation” and “(in preparation)” entries used as load-bearing evidence; these are not citable.

**Summary recommendation**  
**REJECT**

The manuscript fails the standalone-reader test at multiple critical junctures, presents an abstract whose claims are materially stronger than the body’s calibrated statements, relies on a future date and an extensive set of unpublished companion works, and advances a “closure” result whose central technical step is conditional on an explicitly labeled ansatz rather than a derivation. These defects are structural and cannot be repaired by ordinary revision.