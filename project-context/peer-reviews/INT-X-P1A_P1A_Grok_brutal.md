# P1A INT-X-P1A — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/arxiv/paper1a_ech_nogo.pdf` md5=6fc7ac8c pages=31
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 74.8s

---

**Referee Report**

**Paper**: P1A — Channel-Level Closure of Four Minimal Einstein–Cartan–Holst Dark-Energy Routes… (Houston Golden)

**Journal bar**: Physical Review D (high). The paper is 31 pages long.

**Classification of findings** (only ESSENTIAL/MAJOR listed; MINOR/NIT omitted for brevity)

**P1A-E1 (ESSENTIAL)**  
Section I (pp. 3–4) and every subsequent section that imports numerical results.  
The manuscript is not standalone. All load-bearing numbers (H₀ = 67.68 ± 1.06 km s⁻¹ Mpc⁻¹, ΔN_eff = −0.020 ± 0.169, σ₈, β_obs = 0.342° ± 0.094°, the 2.6–5σ Fisher forecasts, NaMaster pipeline validation, ALP MCMC posteriors) are imported from “Paper I(b) (in preparation) [6]” or “Paper II [2]”. No self-contained derivation or table of these quantities exists. Standalone-reader test fails.

**P1A-E2 (ESSENTIAL)**  
Abstract (p. 1) and Sec. IV (pp. 10–13).  
Abstract states the four routes “are closed”. Body repeatedly qualifies that (a) the parity-odd operator is a phenomenological on-shell scaling ansatz with off-shell mass dimension +1 (Appendix B, p. 24), not a controlled EFT operator; (b) R4 is closed only by a naturalness/explanatory-deficit objection, not amplitude mismatch; (c) the Jackiw–Pi term and the four-fermion partner of R1 are omitted from the enumerated set. The abstract claim is therefore stronger than the calibrated body statement.

**P1A-E3 (ESSENTIAL)**  
Sec. X (pp. 18–19) and footnote a (p. 2).  
The “perturbation-transparency” theorem is presented as the central result. It rests on the algebraic Bianchi identity R_μ[νρσ] = 0 on the torsion-free Levi-Civita connection. The paper itself notes this is “distinct from the Pontryagin density” and does not follow from a total-derivative argument. No explicit check is supplied that the same vanishing holds once the omitted operators (R∧R̃, four-fermion) are restored at the same order. The claim therefore exceeds what is demonstrated.

**P1A-E4 (ESSENTIAL)**  
Table I (p. 5) and Sec. XIV D (p. 22).  
f_NL = −35/8 is advertised as a “surviving testable prediction”. The text immediately states it is a property of the scalar-only w = 0 matter-bounce class under Assumption (f) of Paper II and is erased once N_tot − N_exit ≳ N_coh. It is therefore not an ECH-specific signature. Advertising it as such in the abstract and Table I is misleading.

**P1A-E5 (ESSENTIAL)**  
Sec. IX and Table II (pp. 16–17).  
Fourteen “mechanism-class constraints” are enumerated, yet B8 is “subsumed by B14” and the set is explicitly described as “not a complete diffeomorphism-invariant operator basis”. The counting therefore mixes logically distinct physical failure modes with re-labeling. The headline “13 distinct barriers” is not supported by the actual logical structure.

**P1A-M1 (MAJOR)**  
Abstract and Sec. III A (p. 9).  
Three independent β measurements (WMAP+Planck 0.342° ± 0.094°, ACT DR6 0.215° ± 0.074°) are placed side-by-side and compared to the same 0.27° benchmark without an explicit statement that the pipelines are not directly comparable (different masks, foreground treatments, multipole ranges). Violates the “not directly comparable” rule for juxtaposed null results.

**P1A-M2 (MAJOR)**  
Appendix B (p. 24) and Eq. (6).  
The parity-odd operator is written with off-shell dimension +1. All amplitude-budget closures (Routes 1–3) rely on this operator being Planck-suppressed or mass-dimension-locked. Because the dimension is admitted to be an ansatz, the quantitative suppression factors (10⁻⁶⁰, 10⁻⁶³, 10⁻⁷⁰ …) are not derived and cannot be used to close channels at the stated significance.

**P1A-M3 (MAJOR)**  
Page count vs. contribution.  
A 31-page manuscript whose core claim is a channel-level no-go resting on a scaling ansatz plus 14 re-labeled barriers exceeds PRD norms for a methods/limits paper. Recommended maximum: 12–15 pages once companions are removed and the ansatz status is foregrounded.

**P1A-M4 (MAJOR)**  
Fig. 1 (p. 6) and Sec. IV.  
The figure and text present four “minimal ECH routes” while simultaneously stating that the Jackiw–Pi term and the leading four-fermion partner of R1 lie outside the enumerated set. The figure caption does not flag this truncation, rendering the diagram incomplete for the claimed scope.

**P1A-M5 (MAJOR)**  
Sec. II C 1 and Eq. (11).  
The inflationary suppression factor D_inf ∝ exp(−3 N_tot) is derived under an order-of-magnitude matching to GUT-scale quantities whose numerical values are taken from the companion. No independent derivation or error budget is supplied.

**Summary recommendation**  
**REJECT**

The manuscript is not self-contained, its central “closure” statements rest on an explicitly non-derivative scaling ansatz, the abstract overstates the strength of the no-go relative to the body caveats, and the 14-barrier catalog mixes distinct physics with re-labeling. These are not cosmetic deficiencies; they are structural. A substantially shortened, fully standalone version that foregrounds the ansatz status and removes all companion-dependent numerics could be reconsidered, but the present submission does not meet PRD standards.