# P3 INT-EXTDB2check — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=5bf37274 pages=30
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 74.7s

---

**Referee Report – Physical Review D**

**Paper:** Spectrally Unusual Sources at Scale… (Golden 2026)

**Recommendation:** REJECT

The manuscript presents an ambitious multi-survey anomaly catalog but fails to meet PRD standards for reproducibility, internal consistency, and honest framing of results. The core methodological contribution is obscured by an extremely long (≈30-page) manuscript whose headline numbers rest on fragile, partially irreproducible pipelines and on post-hoc choices that are not fully disclosed in the abstract. Several load-bearing quantitative claims in the abstract are either stronger than, or lack the explicit caveats present in, the body. The paper cannot be accepted without major surgery; the current form is not salvageable by minor revision.

### ESSENTIAL findings (paper cannot be accepted without these fixes)

**P3-E1 (Abstract + §I, p. 1; §III E, p. 11)**  
Abstract states “largest application of autoencoder anomaly detection by total sources processed in a single multi-archive framework.” Body never supplies a systematic literature comparison establishing this claim against Liang et al. (2023), Baron & Poznanski (2017), or other published single-survey or multi-survey searches. The claim is therefore unsupported.  
*Required fix:* Remove or replace with a properly bounded statement that cites and quantitatively compares against all prior works.

**P3-E2 (Abstract + Table I footnote ¶, p. 9; §III E, p. 11)**  
Abstract headline “269,317 Recommended-Tier (378,280 Total)” is presented without the body’s explicit qualification that the eROSITA tier is a non-reproducible membership list only (score axis irreproducible from any committed artifact) and that the Gaia + eROSITA exploratory components are retained only as “per-object validity flags.” The abstract therefore overstates the size of the validated catalog-grade subset.  
*Required fix:* Abstract must state the exact size of the reproducible, catalog-grade subset (≥268,519 point sources) and flag the irreproducible components.

**P3-E3 (Table I + §III E, p. 11; §VI D)**  
The eROSITA 298-source tier and the Planck 200-patch tier rest on axes that the text itself labels “irreproducible from the committed aggregate artifact.” No frozen release hash or exact production script is supplied that would allow a reader to regenerate these numbers. This violates PRD reproducibility requirements for any result that appears in the headline catalog.

**P3-E4 (§V, p. 17–18; Appendix C)**  
The Fisher forecast under the empirical \(\alpha_{jk}=0.19\pm0.65\) bias returns a central value \(\sigma(f_{NL})=8.14\) whose 9.4 % improvement over the single-tracer baseline is stated without the explicit qualifier that appears only later: “no multi-tracer improvement at current S/N.” The abstract and §V therefore present a stronger claim than the calibrated body statement supports.  
*Required fix:* Every appearance of the 9.4 % figure must be accompanied by the explicit statement that it is a noise-driven forecast pending higher-S/N data and does not constitute a detection.

**P3-E5 (multiple locations, e.g. Table I footnotes, §III D, §VI A)**  
The manuscript repeatedly juxtaposes cross-transfer and native-retrain anomaly rates (e.g., LAMOST 0.39 % → 0.018 %) while stating only in footnotes that the scores “are not directly comparable across surveys.” This violates the explicit instruction in the review criteria: any side-by-side use of differently normalized scores without the qualifier at every juxtaposition is ESSENTIAL.

### MAJOR findings (significant revision required)

**P3-M1** The 30-page length far exceeds the actual incremental methodological advance once the reproducibility caveats are acknowledged. Recommended maximum: 12–14 pages.

**P3-M2 (§II D, Path-C protocol)** The six-step native-retrain + injection-recovery + 7-way deduplication pipeline is so survey-specific and gate-laden that the headline catalog cannot be regarded as a single, uniformly validated product. The paper should be reframed as a methods demonstration plus an exploratory catalog, not as a definitive 378 k source catalog.

**P3-M3 (Fig. 3, right panel; §III C)** The SDSS cross-transfer score distribution is shown on a log scale that compresses the extreme tail; the body never quantifies how many of the \(S>10^{10}\) objects are simply the known M7–T2 dwarf locus that lies outside the DESI training distribution. This is a domain-shift artifact, not a discovery.

**P3-M4 (§IV A)** The 17.8 % “genuine novelty fraction” is computed against an 18-catalog CDS X-Match on only the top-1,000 DESI objects. The paper never demonstrates that this fraction is stable when the matching radius or the depth of the comparison catalog is varied; the Wilson interval quoted therefore overstates precision.

**P3-M5 (NANOGRAV analysis, §V A)** The recovered \(\gamma=2.567\pm0.382\) is presented as “marginally consistent” with the matter-bounce prediction \(\gamma=3.0\). The Savage-Dickey Bayes factor against the SMBBH reference is given only under a flat prior; no prior-sensitivity test is shown. This is insufficient for a cosmological claim in PRD.

### MINOR / NIT findings (selected)

- Multiple instances of “superseded,” “cross-transfer baseline,” and “Path-C unique” language that read as internal version-control notes rather than archival prose.
- Table I contains 11 footnotes; several are mutually contradictory on whether a given threshold is “fixed-size continuity slice” or “top-1 %.”
- Fig. 7 (spatial map) has no scale bar or HEALPix \(N_\mathrm{side}\) label.
- Equation (2) normalizes by survey-specific \(\mu_\mathrm{val},\sigma_\mathrm{val}\); the text never states that this choice precludes any absolute ranking across surveys, yet the abstract treats the combined catalog as a single ranked list.

### Summary recommendation

**REJECT**

The manuscript attempts a genuinely large-scale, multi-survey anomaly search but buries essential reproducibility failures, irreproducible score axes, and post-hoc threshold choices inside an excessively long text whose abstract overstates both the size and the robustness of the delivered catalog. Until the authors (1) restrict the headline numbers to the fully reproducible, catalog-grade subset, (2) remove or properly caveat every unsupported “largest/first” claim, (3) shorten the paper by at least half, and (4) bring every cross-survey comparison under a single, explicitly qualified normalization, the work does not meet Physical Review D standards.