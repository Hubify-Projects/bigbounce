# P5 2026-06-04_1814pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 73.8s

---

## Referee Report for Paper P5  

### ESSENTIAL Revisions  

- **P5-E1**: Abstract, page 1  
  **Problem**: Unresolved section reference "see §??" for survey-edge artifact explanation. This renders the provenance of the void-class constraint untraceable.  
  **Fix**: Replace "see §??" with the correct section number (e.g., §VIII) where the DESIVAST-anchored re-projection is detailed.  

- **P5-E2**: Title and multiple sections (e.g., §VIII, §XIII)  
  **Problem**: Version-control artifacts (e.g., "R-upgraded-round9 close: 7 do-now fixes", "v0.1.44 GEM-M1 closure", "R-ext-GRO-min1 reframing") appear in body prose. These are internal workflow tags, not scientific content.  
  **Fix**: Remove all version-history language, audit tags, and review-log artifacts (e.g., "R-upgraded-round9", "v0.1.44", "GEM-M1", "R-multi-round2").  

- **P5-E3**: Abstract, page 1  
  **Problem**: Sensitivity floors "∼ 0.2 pp" (systematic) and "∼ 5 pp" (statistical) lack provenance. No script/dataset/equation derives these values; they are asserted without evidence.  
  **Fix**: Add a citation to the specific analysis (e.g., §VI.A or §VII) or equation (e.g., Eq. 1) that quantifies these floors.  

### MAJOR Revisions  

- **P5-M1**: Abstract and §VI.A, page 1  
  **Problem**: Headline CW fractions (void: 0.4836, wall: 0.5034, filament: 0.4980, cluster: 0.4963) are presented without traceable source. Though §VI.A references a CSV artifact, the abstract does not link to any dataset/script, and the paper lacks a public repository for `pipelines/` scripts.  
  **Fix**: (1) Reference the exact dataset (e.g., Table II) in the abstract; (2) Provide a public URL or supplementary material for `pipelines/p5_desi_chirality/scripts/`; (3) Add SHA-256 hashes for data in Table I.  

- **P5-M2**: §VI.A, page 1  
  **Problem**: The filament σ value (-2.61σ) is irreproducible from displayed values. Given n=408,187 and f<sub>CW</sub>=0.4980, σ<sub>from half</sub> = (0.4980 - 0.5) / (0.5/√408187) ≈ -2.56σ, contradicting -2.61σ. Similar inconsistency exists for void σ (-0.68σ vs. calculated -0.67σ).  
  **Fix**: Correct the σ calculations or provide the exact formula (including binomial adjustments if used).  

- **P5-M3**: §II, §VI, §XII  
  **Problem**: Critical dependence on unpublished Paper IV for chirality labels and monopole offset (∆f<sub>CW</sub> = -0.0026). Paper IV is "not yet peer-reviewed," undermining reproducibility.  
  **Fix**: Include sufficient methodological details in this paper (e.g., classifier architecture, TTA procedure) or defer submission until Paper IV is accepted.  

- **P5-M4**: §V.B, §VIII  
  **Problem**: The "primary analysis path" (DESIVAST) is declared post-hoc without pre-registration, risking garden-of-forking-paths bias. The paper uses five DESIVAST estimators but does not correct for multiplicity in the headline claim.  
  **Fix**: (1) Justify the DESIVAST primary designation a priori; (2) Apply Bonferroni correction to the five DESIVAST estimators (α<sub>adj</sub> = 0.01) and report adjusted thresholds.  

### MINOR Revisions  

- **P5-M5**: §III.B, Table I  
  **Problem**: DESI DR1 input row count inconsistency: text states "16.4 × 10<sup>6</sup>" but Table I lists 16,361,731. The discrepancy (38,269 rows) is unexplained.  
  **Fix**: Align text with Table I (use 16,361,731) or clarify rounding.  

- **P5-M6**: §VI.D.a, page 7  
  **Problem**: Duplicate phrase "boundary-leakage interpretation" in consecutive sentences reduces clarity.  
  **Fix**: Rephrase (e.g., "This interpretation of boundary leakage" → "This leakage interpretation").  

- **P5-M7**: §IX.B, page 16  
  **Problem**: T-Web volume fractions from Ref. [11] are cited as "approximate concordance" but lack quantitative comparison to V-Web results (e.g., χ<sup>2</sup> test).  
  **Fix**: Add a quantitative concordance metric (e.g., |∆f<sub>void</sub>| = +0.084–0.184) and discuss implications.  

### NIT Revisions  

- **P5-N1**: §III.D, Table I  
  **Problem**: "NS (excluded)" count (1,440,577) does not sum with CW+CCW counts (393,592 + 398,043 = 791,635) to match "Chirality-relevant" total. Residual 1,440,577 + 791,635 = 2,232,212, but "Matched primary" is 2,232,212—this is correct but confusingly presented.  
  **Fix**: Relabel "NS (excluded)" as "Non-spiral/undetermined" and add a footnote clarifying the sum.  

- **P5-N2**: §V, Eq. 1  
  **Problem**: Equation for σ<sub>pred</sub> uses "N" without defining it as bin-specific sample size.  
  **Fix**: Clarify "N<sub>bin</sub>" in notation.  

- **P5-N3**: References  
  **Problem**: Ref. [11] (Ullah et al. 2026) and [12] (Zapata-Zuluaga et al. 2026) are preprints cited as "concurrent literature," but their status is undefined.  
  **Fix**: Label as "submitted" or "arXiv."  

---  
## Summary recommendation  
**MAJOR REVISIONS**  

The paper reports a rigorous null test of environment-dependent chirality using DESI DR1, with commendable cross-checks across multiple cosmic-web classifiers (V-Web, DESIVAST, Tempel FoF). However, essential issues undermine reproducibility: unresolved section references (§??), version-control artifacts in prose, and untraceable sensitivity floors. Major revisions are required to address provenance gaps in headline numbers (e.g., CW fractions, σ values) and dependence on unpublished work (Paper IV). The post-hoc designation of the primary analysis path (DESIVAST) risks confirmation bias and must be justified a priori. Methodological rigor is high, but these flaws prevent acceptance in current form.