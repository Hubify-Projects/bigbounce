# INT API Review — P4 v1.0.242 — openai (gpt-5.5)
paper: P4  version: v1.0.242  model: gpt-5.5
provenance: commit=97b9cb7f  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=8c9df3dac29459f568619bcb53daa7b9acc54e0a80bb8cb776f1277aa35a76c4
modality: native-PDF (Files API input_file)
UTC: 2026-07-14T11:54:04.541480Z  |  latency: 92.6s  |  attempt: 1
usage: {"input_tokens": 44450, "input_tokens_details": {"cache_write_tokens": 0, "cached_tokens": 0}, "output_tokens": 4792, "output_tokens_details": {"reasoning_tokens": 2588}, "total_tokens": 49242}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) **VERDICT: MINOR REVISIONS**

The manuscript’s deliberately narrow primary claim—an **observed-classifier-label** real-space dipole null in the HC sample—is substantially supported, provided the authors make several clarity and reproducibility fixes. I find **no fresh verified MAJOR blocker** beyond the limitations/gates the paper already explicitly discloses: no complete spatially varying image/confusion transfer, no matched-footprint independent estimator, no joint covariance/likelihood, and no final frozen DOI/release/preregistration record.

I recomputed the arithmetic exposed in the PDF where possible from the printed numbers. The catalog fractions, global CW-fraction significances, GZ1 confusion-derived accuracy and dilution factor, Fisher floors, Table V harmonic z-values to rounding, Table VI monopole-leakage ratios/z-values, and WLS diagnostic z-values are internally consistent to the quoted precision. I cannot independently recompute the primary HC dipole statistic from the PDF alone because the data-vector amplitude, null mean/width, and rank count are not printed; the manuscript instead points to repository artifacts.

---

(2) **Numbered issues**

1. **[MINOR] Page 1 abstract; Sec. III A p.2; Sec. IV C p.9; Conclusions p.15 — primary rank p-value is described inconsistently as one-sided/two-sided.**  
   **Claim/evidence:** Sec. III A says empirical rank p-values are one-sided unless labeled two-sided, and the primary pair is “moment-z / rank-p” with \(z_{\rm mom}=+0.41\), rank \(p=0.31\). The abstract says “rank \(p=0.31\)” without “two-sided.” The conclusions state “two-sided \(p=0.31\).” For a positive-definite dipole-amplitude statistic, a one-sided upper-tail rank p near 0.31 is plausible for \(z=+0.41\); a two-sided rank p would normally require a different definition and would not simply equal the upper-tail rank.  
   **Required fix:** Define the primary rank p-value explicitly in one place and use identical wording everywhere. Print the exact formula, e.g. \(p=(k+1)/(N+1)\) for the fraction of null amplitudes exceeding the data amplitude, or state the two-sided construction if genuinely two-sided. If \(p=0.31\) is upper-tail, remove “two-sided” from the conclusions.

2. **[MINOR] Sec. IV C p.9 and Table II p.5 — the load-bearing primary dipole statistic is under-exposed in the PDF.**  
   **Claim/evidence:** The central result is \(N=949{,}584\), \(z=+0.41\), rank \(p=0.31\), but the paper does not print the fitted dipole amplitude, fitted direction, null mean, null standard deviation, number of null draws above the data, or exact mask-pixel count for the HC run in the main text/table. These are necessary to recompute the primary result from the manuscript rather than from a path in a live repository.  
   **Required fix:** Add a compact “primary estimator audit” table giving: HC sample count, mask pixel count/fsky, fitted monopole, fitted dipole vector or amplitude/direction, null mean, null width, \(z\), rank count \(k/N\), rank p convention, RNG seed or deterministic null specification, and artifact checksum. This is the only load-bearing cosmological row, so it should be fully exposed.

3. **[MINOR] Sec. III B/Table II p.3–5; Sec. VI B p.13–14; Conclusions p.16 — sensitivity language still intermittently implies a threshold despite later caveats.**  
   **Claim/evidence:** Table II row (vii) states “50%-rec-3σ, \(A=0.75\%\),” and Sec. III B says “50%-recovery-at-3σ threshold at \(A=0.75\%\).” Later Sec. VI B correctly downgrades this to finite-grid descriptive evidence and says no calibrated 50% or 95% recovery amplitude is defined. Table VIII gives \(P(\sigma>3)=0.55\) at \(A=0.75\%\) for one pilot convention; Stage B gives 16/20 axes at 0.75%.  
   **Required fix:** Replace all “threshold” language by “finite-grid score fraction” language. For example: “At \(A=0.75\%\), the pilot score-pass fraction is 0.55/0.59 in the 100-injection grids and 16/20 in the deterministic-axis surrogate.” Do not call this a recovery threshold or sensitivity floor unless calibrated coverage is supplied.

4. **[MINOR] Sec. IV C–D p.9–11; Table V p.10; Conclusions p.16 — harmonic diagnostic conventions remain too easy to misread.**  
   **Claim/evidence:** The manuscript repeatedly warns that harmonic z-values are diagnostic and noncommensurable, but it still presents several nearby \(\ell=1\) values: +3.64, +7.28, +7.31, +7.93, +5.14 post-MASTER-monopole residual, etc. The explanations are present but dispersed. Since the primary result is a real-space null, the harmonic diagnostics should not create an apparent contradiction for readers.  
   **Required fix:** Add one consolidated table with one row per harmonic diagnostic, including field definition, mask, weight, mean subtraction, null type, null size, data value, null mean/width, z, rank p if any, and a final column “diagnostic only.” Remove or soften phrases such as “confirms this channel” unless immediately followed by “as a systematics diagnostic only.”

5. **[MINOR] Fig. 7 p.10 — raw-map panel appears visually misleading or incorrectly rendered.**  
   **Claim/evidence:** The left “Raw ViT-Small Catalog A” panel appears almost blank/sparse compared with the right equivariant panel, despite the caption describing a full raw sky map and a raw dipole artifact. This may be a plotting/color-scale/rendering issue, but as printed it does not visually support the stated comparison.  
   **Required fix:** Regenerate Fig. 7 with identical pixel support and visibility for both panels, or explicitly state that the left panel is a sparse diagnostic subset if that is what was plotted. The visual should not suggest that Catalog A covers only a few scattered pixels.

6. **[MINOR] Appendix B p.18–20; Data Availability p.24 — flip-identity QC issue is disclosed, but downstream handling should be more operational.**  
   **Claim/evidence:** The paper reports 59,515 HC rows with reconstructed flip-pass probabilities outside \([0,1]\) by up to 0.09, due to a raw/equivariant pipeline-pass mismatch. The authors state that hard labels and primary dipoles are unchanged and that a QC flag is released. This is acceptable for the primary hard-label estimator, but it is a real catalog-product defect for users of raw/flip probability columns.  
   **Required fix:** In the catalog schema and Data Availability section, explicitly mark which probability columns are safe for hard-label analyses, which are unsafe for probability-level inference without filtering, and provide the exact one-line filter used in every primary/diagnostic rerun. If possible, ship a corrected probability-only patch or deprecate the affected reconstructed columns.

7. **[MINOR] Data Availability p.24 — frozen reproducibility archive is still prospective.**  
   **Claim/evidence:** The paper says the repository currently resolves against the live main branch and that a Zenodo DOI, immutable tag, commit hashes, and checksums “will be deposited” at submission. This is an explicitly disclosed standing release/DOI gate, not a new scientific defect, but PRD publication requires a frozen reproducible record.  
   **Required fix:** Before final acceptance, replace prospective language with an actual DOI, immutable git commit, catalog release checksum, model checkpoint checksum, and checksums for the primary HC dipole artifact and the catalog rows used to form \(N=949{,}584\).

8. **[MINOR] Sec. II–VI and Appendix B — pseudo-label independence is handled honestly, but the wording should avoid implying external validation stronger than supplied.**  
   **Claim/evidence:** The paper correctly states that 66.5% of source labels derive from CE-ResNet and that shuffle nulls cannot test inherited spatial structure. The GZ1-only dipole is a useful independent-label corroboration but much smaller and not a tighter bound. Some phrases such as “corroborates the null independently” are acceptable only if the limited power is restated nearby.  
   **Required fix:** Wherever the GZ1 cross-check is invoked, append “at lower statistical power and without tightening the HC amplitude constraint.” This is mostly already done; enforce consistency.

---

(3) **Whether the narrow central observed-label claim is supported**

**Yes, with the above minor clarifications.** The manuscript’s actual central claim is narrow: the **observed hard-label** HC real-space chirality dipole in \(N=949{,}584\) objects is consistent with its isotropic pixel-permutation null, with reported \(z=+0.41\) and rank \(p=0.31\). Nothing in the printed arithmetic contradicts that claim. The paper also properly avoids claiming a primordial parity bound, a calibrated physical-amplitude exclusion, or a completed spatially varying confusion transfer.

The surrounding diagnostics—global monopole, MASTER residuals, WLS template fits, injection grids, and image-pair surrogate—are explicitly demoted to diagnostic status. That hierarchy is scientifically appropriate given the pseudo-label dependence and the unresolved transfer/covariance gates.

---

(4) **Whether any fresh verified MAJOR blocker exists**

**No.** I find **no fresh verified MAJOR blocker** to the narrow observed-label null result. The remaining serious limitations are already disclosed by the authors as open gates: spatially resolved image/confusion transfer, matched-footprint independent estimator comparison, joint covariance/likelihood, and final frozen release/DOI/preregistration status. The required fixes above are mainly consistency, exposition, and reproducibility-hardening revisions rather than scientific blockers.