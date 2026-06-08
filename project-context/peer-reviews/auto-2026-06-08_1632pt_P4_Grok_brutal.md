# P4 auto-2026-06-08_1632pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 44.0s

---

**Referee Report**

**P4-E1 (ESSENTIAL, Abstract + Sec. IV C, p. 1 and p. 4)**  
The abstract juxtaposes “−0.122σ (500-MC label-shuffle null)” with “+0.43σ (p=0.30, isotropic-null bootstrap)” without the explicit qualifier “these σ values are not directly comparable across estimators” that the body itself requires. The same side-by-side presentation recurs in Table I and the opening paragraph of Sec. IV C. Required fix: insert the qualifier at every numerical juxtaposition or remove all cross-null σ comparisons from the abstract and headline tables.

**P4-E2 (ESSENTIAL, Sec. IV D + Table IV, p. 5)**  
The generative monopole-only null is stated to reproduce “99.3 % of the observed pre-MASTER pseudo-C_ℓ^(ℓ=1) power.” The binomial draws are performed on N_spiral(p) while the real map uses N_all(p) (weight W_p). The inflation factor N_all/N_spiral ≈ 1.49 is acknowledged only in a footnote; the quoted 99.3 % figure is therefore not reproducible from the displayed numbers. Required fix: recompute and quote the exact fraction under the N_all weighting used for the data vector, or retract the 99.3 % claim.

**P4-M1 (MAJOR, Sec. I + II B, p. 2)**  
67.6 % of training labels are taken from CE-ResNet predictions rather than independent visual classification. The quoted “conservative accuracy floor” of 69.91 % is therefore partly circular. The paper never quantifies how label noise propagates into the final dipole posterior. Required fix: either (a) repeat the full analysis on the 32.4 % GZ1-only subset or (b) supply a full end-to-end noise-injection simulation that maps GZ1/CE-ResNet label error into ΔC_ℓ.

**P4-M2 (MAJOR, Sec. VI A, p. 6)**  
The empirical 50 %-recovery-at-3σ threshold is given as A ≈ 0.75 % on the HC-spiral subsample. The Fisher Poisson floor calculated from the same numbers is ≈ 0.29 %. The factor-of-two discrepancy is attributed to “classification noise (GZ1-dilution factor g = 2a−1 ≈ 0.398)” but no explicit propagation of g into the dipole covariance is shown. Required fix: derive and publish the modified Fisher matrix that includes the dilution factor, or demonstrate that the quoted 0.75 % threshold is already the final survey sensitivity.

**P4-M3 (MAJOR, entire manuscript length)**  
The paper is 11 pages for a single null result plus an extensive systematics audit. PRD norms for a methods/null paper of this type are 4–6 pages. The exhaustive eight-test bias-hardening suite and five-anchor canonical-mask analysis could be condensed into a companion data-release note. Required fix: shorten to ≤ 6 pages or justify the length against the incremental scientific advance.

**P4-N1 (MINOR, title page)**  
“(Dated: June 2026)” is a future date and functions as an internal placeholder. Remove.

**P4-N2 (MINOR, Table I caption)**  
The sentence “N_map weighted exceeds N_catalog spiral because W_p includes non-spiral galaxies” is repeated almost verbatim in the text two paragraphs later. Delete the duplicate clause.

**P4-N3 (NIT, multiple locations)**  
Minor typographic inconsistencies: “canonical canonical-mask” phrasing does not appear, but “the canonical-mask residual is +3.64σ” is written both with and without the hyphen in consecutive paragraphs. Standardize.

**Summary recommendation**  
MAJOR REVISIONS

The manuscript presents a carefully documented null result and an extensive systematics audit. However, the non-comparability of σ values is not enforced at every numerical juxtaposition (E1), the headline 99.3 % null-reproduction claim cannot be reconstructed from the displayed counts (E2), and the dominant training-label contamination is not propagated into the final posterior (M1). These three items are essential for a PRD-level claim of “diagnostic evidence” for a systematics floor. In addition, the paper is substantially over-length for its incremental contribution. Until the essential items are corrected and the manuscript is shortened, it does not meet the acceptance threshold of Physical Review D.