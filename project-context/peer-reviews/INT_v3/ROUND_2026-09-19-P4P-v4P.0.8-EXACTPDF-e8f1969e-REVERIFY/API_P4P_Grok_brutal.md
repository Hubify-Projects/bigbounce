# P4P ROUND_2026-09-19-P4P-v4P.0.8-EXACTPDF-e8f1969e-REVERIFY — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `pipelines/p4prime_chirality_test/paper/main.pdf` sha256=e8f1969e415777622561dde0f21a8ac7d6398c3b2ef55f69200ba50a89d91cd2 pages=14
**Review packet(s)**: `6c18f4c05b0f82b19cf243eabbd609ac13dc347185600ffb962a83abdcdb2c5b, 149dcf673111249df66adec37eb8f1c31d219f1b3e20ef776267e18c7b0dbea5`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 118.7s

---

**REFEREE REPORT — ApJS (Track C1 catalog + science)**

**Paper:** “The Largest Test of a Preferred Galaxy-Spin Axis: An 8.47-Million-Galaxy DESI Chirality Catalog…” (v4P.0.8, 14 pp.)

I have examined every page, table, figure, equation, caption, and the abstract against the rendered PDF. All quoted numbers were recomputed from displayed inputs where possible. The paper fails ApJS standards on multiple independent grounds.

### ESSENTIAL findings (paper cannot be accepted without fixes)

**P4P-E1 (Abstract, p. 1; §5.2, p. 8)**  
Abstract states the 887 472-galaxy primary null “disfavors a dipole above ~1 % at ≥95 % power, 2–20× below the ~2–33 % literature amplitudes.” The body (§5.2) shows this limit is obtained only after inserting an *illustrative, not-adopted-for-strengthening* bridge factor \(g=0.398\) that converts observed-label amplitude to a putative physical parity amplitude. No calibration of \(g\) exists in the archived release or cited literature. The abstract claim is therefore stronger than the calibrated statement in the body.  
**Required fix:** Remove the factor-of-2–20 claim from the abstract or replace it with the unbridged observed-label floor \(A_{95}^{\rm obs}\simeq0.98\%\) and an explicit statement that no physical-amplitude conversion has been validated.

**P4P-E2 (Abstract, p. 1; §5.1, p. 7)**  
Abstract and title frame the work as “a Sensitivity Confrontation with the Rotating-Black-Hole-Universe Prediction.” Poplawski (2010, 2012, 2016) papers supply only a qualitative tendency; no amplitude, alignment fraction, or relaxation timescale is predicted. Eq. 4 (\(A_{\rm pred}\approx\eta\)) is introduced by the authors. The confrontation is therefore against a literature amplitude range, not against the model itself.  
**Required fix:** Retitle and rewrite abstract/§5 to state that the paper tests literature-reported amplitudes, not a quantitative model prediction.

**P4P-E3 (§3, p. 4; §5.2, p. 8)**  
The primary real-space dipole null (\(A_{\rm dip}=0.467\%\), \(z_{\rm mom}=+0.635\), one-sided \(p=0.238\)) and the FSC harmonic diagnostic (\(z=+6.923\)) are presented side-by-side without the explicit qualifier “not directly comparable” at every juxtaposition. Instruction 7 is violated.  
**Required fix:** Insert the qualifier in both abstract and §3, or remove one diagnostic.

**P4P-E4 (Table 5, p. 8; §5.2)**  
Every literature amplitude “exceeds \(A_{95}^{\rm obs}\) by a factor of 2–20.” The ratio column is computed with the *illustrative* \(g=0.398\) bridge. The table therefore reports a derived quantity whose calibration is not established.  
**Required fix:** Delete the Ratio column or label every entry “illustrative, uncalibrated conversion.”

### MAJOR findings (significant revision required)

**P4P-M1 (Overall length, 14 pp.)**  
ApJS catalog papers are expected to be concise. This manuscript devotes >4 pages to post-hoc robustness tests, three secondary diagnostics, and an appendix whose sole purpose is to document that the primary null survives every check the authors could invent. Recommended maximum: 8–9 pages including all tables/figures.

**P4P-M2 (§4, p. 6; Fig. 3)**  
The DESIVAST void/non-void contrast is performed on a 145 766-galaxy subset after the primary analysis was complete; the hierarchy was “fixed after inspecting the data.” The result (\(\Delta f_{\rm CW}=+0.00145\), \(p=0.66\)) is reported as an independent probe. Post-hoc redefinition of the test after data inspection requires a registered-analysis statement or removal from the main text.

**P4P-M3 (Abstract, p. 1)**  
“the largest test of that claim to date.” The primary supported-pixel sample (\(N=887\,472\)) is smaller than Shamir (2022) DESI Legacy sample (\(N=1.3\) million). The claim is true only for the *full* 8.47 M catalog, not for the statistical test that actually constrains the dipole. The abstract is therefore misleading on its most prominent quantitative claim.

**P4P-M4 (§2.2, p. 3; Table 3)**  
The released classifier’s Cohen’s \(\kappa=0.40\) (69.91 % agreement) is validated only against a Galaxy Zoo overlap that is overlap-contaminated. The manifest-retrained \(\kappa=0.97\) figure is explicitly “neither comparable to, nor a replacement for” the released classifier. Readers cannot assess label reliability from the released product alone.

**P4P-M5 (Fig. 1, p. 4; §3)**  
The HEALPix map shows no coherent structure, yet the caption claims “no coherent large-scale structure is visually apparent in either support.” The figure is therefore decorative; it adds no information beyond the already-reported null.

### MINOR findings

**P4P-m1 (p. 2, Table 1)** Column “score_eq_max” description is truncated (“max eq. class score (\(p_{\rm eq}\))”).  
**P4P-m2 (p. 5, Eq. 2)** The Neyman 95 % CL interval is reported as bracketed values without the explicit statement that it is the *complementary* amplitude whose recovered distribution stays above the 5th percentile of the null.  
**P4P-m3** Multiple instances of “this research program’s own bounce papers” (pp. 1, 7) read as self-promotional rather than scientific.

### NITs (cosmetic)

- Future date “September 18, 2026” on draft line.  
- Inconsistent use of “one-sided” vs “two-sided” \(p\)-values without always stating which tail is used.  
- Table 8 caption says “\(z\) is against the 1 000-realization label-shuffle null” but the table header does not repeat the null definition.

### Summary recommendation

**REJECT**

The manuscript fails the ApJS acceptance bar on first read. Its central scientific claim—an exclusion of the rotating-black-hole-universe spin-axis prediction—rests on an uncalibrated conversion factor that the authors themselves label “not adopted for strengthening.” The abstract asserts both “largest test” and a quantitative factor-of-2–20 disfavoring that the body does not support without that factor. The paper is also overlength, contains a post-hoc environmental test, and juxtaposes non-comparable statistics without the required qualifier. These are not cosmetic issues; they are structural. A revised submission would need to (1) remove or clearly caveat the physical-amplitude bridge, (2) shorten by at least 5 pages, (3) register or remove the void analysis, and (4) rewrite the abstract so that every load-bearing scalar matches the final calibrated statement in the body. Until those changes are made, the paper does not meet the standards of ApJS.