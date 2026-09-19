# AF ROUND_2026-09-19-AF-vAF.0.3-EXACTPDF-d85487e9-R1 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` sha256=d85487e97f6856040d12ef78b78ab57ce4d74fc6420d6664013cdc9651c17b41 pages=15
**Review packet(s)**: `902a6e4fc128da95d4c81b565f6473fcf706204f178be2c111c321e0ee592f52, 8e855bb60a1ab2d24b0c45c3c914b53dacf484577401da314ab7809fa61680fd`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 self-critique (2373 chars)
**Wall time**: 143.2s

---

**Referee Report – ApJS-CATALOG (Round 1)**

**Paper:** AF | provenance-sealed DESI DR1 anomaly-score catalogue

**Finding AF-E1 (ESSENTIAL, Abstract + Sec. V.B, p.1 & p.6)**  
Abstract states: “the anomaly score is uncorrelated with exposure quality and source brightness (|ρ_s| < 0.1)”. Body (p.6) reports Spearman ρ_s = +0.058 (median coadd S/N), –0.076 (exposure time), –0.093 (TSNR2_LRG), all formally significant though small, plus the dominant driver ρ_s = +0.527 (p ~ 10^{-89}) with the blue-arm residual r_B. The abstract claim is therefore stronger than, and omits the dominant instrumental correlation present in, the calibrated body statement.  
**Required fix:** Rewrite abstract sentence to match the body’s final calibrated statement exactly, including the blue-arm result and sign of the small exposure-quality correlations.

**Finding AF-E2 (ESSENTIAL, Abstract + Sec. V.D, p.1 & p.6)**  
Abstract: “A known-object recovery benchmark against five reference classes recovers no class at the pre-declared bar”. Body states the 95 % upper limit on recovery of the rarest class (SLSN hosts, N_ref = 27) is 12.5 %. The abstract omits the quantitative power statement that the body itself calls “the honest summary”.  
**Required fix:** Insert the 12.5 % (or equivalent) power figure into the abstract sentence.

**Finding AF-E3 (ESSENTIAL, Title + Abstract + Sec. VIII, p.1 & p.11)**  
Title and abstract present the work as “a provenance-sealed anomaly-score candidate catalogue”. The body’s own Sec. VIII and conclusions state the catalogue “does not bear on cosmology”, “admits no abundance/rate/number-density statement”, “is not a discovery catalogue”, and that the score “is driven almost entirely by the blue spectrograph arm”. The title therefore does not carry the null/instrumental framing that the paper’s final calibrated claims require.

**Finding AF-E4 (ESSENTIAL, Sec. III.B + Fig. 1 + Table II, p.3)**  
The provenance gate itself removes >99.5 % sky/non-science fibres in every score bin; the released 1,244 objects are the residual science-target tail. Fig. 1 and Table II show the sky fraction still rises monotonically with S. The catalogue is therefore a high-S tail of the already-cleaned science-target population, not an astrophysical anomaly sample. No figure or table quantifies how many of the 1,244 would be selected by a pure blue-arm residual cut.

**Finding AF-E5 (ESSENTIAL, Sec. VI.C + Fig. 8, p.8–9)**  
The 8-family taxonomy has silhouette –0.0162 (negative) over the 128 latent dimensions; the paper states the families are “score-tier × survey/programme stratification”, not physical classes. The latent-space test (V12) is therefore reported as “STRUCTURED-BUT-WEAK”. The taxonomy adds no separable physical information.

**Finding AF-E6 (ESSENTIAL, Sec. VII.B + Table XI + Fig. 9, p.11–12)**  
All four FT-A (z ≥ 4) candidates fail the Lyman-break test on public Legacy Survey photometry; one object already removed by public data alone. The paper therefore supplies zero confirmed high-redshift anomalies. The “named follow-up set” contains no object that survives the cheapest test advertised in the abstract.

**Finding AF-M1 (MAJOR, Sec. V.D + Table VII, p.6)**  
Recovery benchmark uses only five reference classes with tiny N_ref for the rarest objects (27 SLSN hosts). The paper itself notes this yields “almost nothing”. No power calculation or simulation of expected recovery under an astrophysical tail is supplied.

**Finding AF-M2 (MAJOR, Sec. IV.C + p.4)**  
The released schema omits per-object flux inverse variances. The paper states this “prevents a reader from forming a detection significance for any photometric statement”. This is a direct usability defect for the primary data product.

**Finding AF-M3 (MAJOR, Sec. IX + p.13)**  
Reproducibility manifest lists only Stage A (GPU) cost; Stage B (laptop) is asserted “under 60 s” with no wall-clock numbers or checksums for the 10 hashed artifacts. The Zenodo DOI is still a placeholder. A reader cannot reproduce the exact released tables from the manifest alone.

**Finding AF-N1 (MINOR, p.13)**  
Red placeholder text remains in OT-1: “[PLACEHOLDER: run and report per-class injection recovery with the exact model and substrate named]”. Draft language must be removed.

**Finding AF-N2 (MINOR, throughout)**  
Multiple sentences repeat the same caveat (“not a discovery”, “instrumental”, “no population inference”) in nearly identical wording; tightening would reduce length by ~1 page.

**Finding AF-N3 (NIT)**  
Page count 15 for a 1,244-object catalogue whose principal result is a negative benchmark and an instrumental correlation exceeds typical ApJS-CATALOG compression for a methods-only data release.

**Summary recommendation**  
**REJECT**

The paper’s own calibrated results demonstrate that (1) the anomaly score is overwhelmingly an instrumental blue-arm residual diagnostic, (2) the recovery benchmark has negligible power and returns zero detections, and (3) the released catalogue of 1,244 objects carries no usable astrophysical or cosmological signal. The title, abstract, and framing present the work as a candidate-anomaly catalogue rather than as a documented negative/instrumental result. These mismatches are not cosmetic; they violate ApJS-CATALOG standards that a catalogue paper must deliver a data product whose scientific utility is demonstrated, not merely asserted as future infrastructure. The provenance machinery is technically impressive but does not compensate for the absence of a scientifically usable sample.

---

## PASS 2 — self-critique findings (what initial review missed)

**AF-E7 (ESSENTIAL, Table VII, p.6)**  
Table VII lists the BAL-quasar enrichment as 4.2×. Recomputed from the displayed inputs: catalogue base rate = 1,244 / 21,793,550 = 5.709 × 10^{-5}; recovery fraction = 1 / 5,285 = 1.892 × 10^{-4}; ratio = 3.31×. The tabulated 4.2× value is arithmetically inconsistent with the numbers shown in the same table and with the base-rate definition given in the caption.

**AF-E8 (ESSENTIAL, Sec. V.B + Fig. 5, p.6)**  
Body text states the three exposure-quality Spearman coefficients are “formally significant though small” and plots them in Fig. 5. The abstract’s blanket claim “uncorrelated … (|ρ_s| < 0.1)” therefore remains quantitatively unsupported even after the blue-arm correction required by AF-E1; the three small ρ_s values are the only numbers offered, and they contradict the abstract wording.

**AF-E9 (ESSENTIAL, Sec. VII.B + Table XI, p.11–12)**  
Table XI and the Lyman-break test description show that all four FT-A candidates have Legacy Survey g-band fluxes inconsistent with a z ≥ 4 break (one already refuted by public data alone). The abstract’s phrasing “four anomaly-selected DESI-pipeline z ≥ 4 quasar candidates” therefore presents four objects whose cheapest advertised test has already eliminated every member.

**AF-M4 (MAJOR, Sec. III.A + Eq. (1), p.2)**  
S is defined as a per-spectrum standardised residual. The calibration constants (μ_MSE, σ_MSE) = (0.8771, 1.3605) are stated to be “sealed before the scan,” yet no table or manifest entry records the exact 20 000 + 20 000 spectra used to derive them. A reader cannot recompute S from the released latent activations alone.

**AF-N4 (MINOR, throughout)**  
The repeated sentence “the score is driven almost entirely by the blue spectrograph arm” appears verbatim or nearly verbatim in the abstract, Sec. V.B, Sec. VI.C, and the conclusions; a single consolidated statement would suffice.

**NO ADDITIONAL FINDINGS** on figure-caption/body mismatches, dimensional consistency of displayed equations, internal cross-references, null-procedure comparability qualifiers, unsupported novelty language, unquantified hedges, appendix/main-text drift, or stale numbers beyond the arithmetic discrepancy already noted in AF-E7. All other numeric claims recompute correctly from the displayed inputs, and all section references point to the content asserted.