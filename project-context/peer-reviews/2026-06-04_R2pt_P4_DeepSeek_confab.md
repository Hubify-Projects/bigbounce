# P4 2026-06-04_R2pt — Confabulation-hunter referee (reasoning mode)

**Model**: `deepseek/deepseek-r1-0528`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 162.0s

---

### Referee Report for P4 (Confabulation-Hunter Mode)

**PAPER:** P4  
**ROUND:** 2026-06-04_R2pt  
**REFEREE MODE:** Confabulation-hunter (strict provenance enforcement)  

---

#### I. General Assessment  
The paper presents a sophisticated analysis of galaxy chirality using DESI Legacy data, reporting a null dipole result with sub-percent sensitivity. While the technical rigor is commendable, the manuscript suffers from critical flaws in numerical provenance, internal consistency, and adherence to PRD length guidelines. Key scalars in high-impact positions (abstract, conclusions) lack traceable sources, and the narrative contains unresolved contradictions. The paper requires major revisions to establish full reproducibility and eliminate confabulation risks.  

---

#### II. Detailed Findings  

**ESSENTIAL REVISIONS**  
1. **P4-E1: Abstract scalar without provenance**  
   - **§ Abstract**: "MASTER-deconvolved single-mode pseudo-C1 ... yields −0.12σ (500-MC label-shuffle null)"  
   - **Problem**: The scalar `n = 5,547,858` (used in the headline −0.12σ result) lacks traceable provenance. No JSON/script in the reproducibility package outputs this value. Table II cites `pipelines/p2_chirality/master_results/master_power_spectrum.json`, but this artifact does not exist in the described repository structure.  
   - **Fix**: Provide a machine-readable artifact (JSON/script) that outputs `n = 5,547,858` and links it unambiguously in Table II.  

2. **P4-E2: Decomposition arithmetic inconsistency**  
   - **§ Abstract & §IV D**: Claims a "99.3%" reproduction of pre-MASTER power by monopole leakage, then attributes "12%" of post-MASTER residual to the same leakage (Table VIII).  
   - **Problem**: The decomposition 99.3% (pre-MASTER) + 12% (post-MASTER) ≠ 100%, violating conservation. The narrative implies these are additive components of the same signal, but 99.3% + 12% = 111.3% is impossible.  
   - **Fix**: Reconcile the decomposition logic. Explicitly state that 99.3% refers to raw pseudo-Cℓ amplitude, while 12% refers to decoupled Cℓ power. Clarify that 88% residual is *not* additive with 99.3%.  

3. **P4-E3: Incomparable σ values presented without qualification**  
   - **§ Abstract**: Reports −0.12σ (label-shuffle null), +0.43σ (per-pixel-shuffle null), +3.64σ (binomial null) without emphasizing incomparability.  
   - **Problem**: Though a footnote notes σ values are null-dependent, the abstract presents them in sequence, implying comparability. This risks misinterpretation (e.g., comparing −0.12σ subsample result to +3.64σ canonical residual).  
   - **Fix**: Add bold disclaimer: "**σ values are not comparable across null procedures**" adjacent to the first σ in the abstract. Reiterate in Conclusions.  

4. **P4-E4: Conclusions claim unsupported by abstract**  
   - **§ Conclusions**: States the paper proves "a quantifiable monopole-mask leakage channel" reproduces 99.3% of pre-MASTER signal.  
   - **Problem**: The abstract omits this leakage quantification, instead emphasizing the −0.12σ null. The leakage channel is central to the paper's contribution but buried.  
   - **Fix**: Restructure abstract to highlight: "We identify a monopole-mask leakage channel reproducing 99.3% of raw pseudo-Cℓ power (generative null), eliminated by MASTER deconvolution."  

**MAJOR REVISIONS**  
5. **P4-M1: Paper length exceeds PRD norms**  
   - **§ Entire paper**: 56 pages (PRD methods papers typically 15–30pp).  
   - **Problem**: Excessive length dilutes impact. Diagnostic detours (e.g., hemisphere asymmetry, wCW(θ)) belong in supplements.  
   - **Fix**: Reduce to 30pp by moving §§IV E–K, V, VI H–I to Supplementary Material. Retain only load-bearing results (dipole null, leakage channel) in main text.  

6. **P4-M2: Version-history artifacts in prose**  
   - **§III A**: "fixed at v1.0.76 of this manuscript", "v1.0.153" in date.  
   - **Problem**: Internal version tags break peer review immersion.  
   - **Fix**: Remove all versioning tags. Use "analysis version finalized prior to [stage]" if temporal context is essential.  

7. **P4-M3: Duplicate phrases**  
   - **§ Title, §IV D**: "canonical canonical-mask" (title), "canonical-mask residual" (§IV D).  
   - **Problem**: "canonical" duplicated in title.  
   - **Fix**: Shorten title to "Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.12σ ℓ=1 Null and Monopole-Mask Leakage Channel".  

**MINOR REVISIONS**  
8. **P4-m1: Undefined scalar in conclusions**  
   - **§ Conclusions**: "falsify the present null" if future survey detects dipole "at σ > 5 with full amplitude ≳ 0.75%".  
   - **Problem**: 0.75% amplitude lacks direct trace to a table (Table XVI lists it but calls it "empirical 50%-recovery-at-3σ threshold", not falsification threshold).  
   - **Fix**: Add "falsification threshold" column to Table XVI and cite it in conclusions.  

9. **P4-m2: Ambiguous spiral count**  
   - **§ Abstract**: "3.2 Million Spirals" vs. **§IV A**: 3,201,160.  
   - **Problem**: Inconsistent rounding. 3,201,160 = 3.20 million, not 3.2 million.  
   - **Fix**: Standardize to "3.20 million spirals" throughout.  

**NITS**  
10. **P4-n1: Confusing "canonical" usage**  
    - **§IV C**: "canonical-N" vs. "subsample-mask" vs. "strict-superset" masks.  
    - **Problem**: Overloaded terminology distracts.  
    - **Fix**: Rename "canonical-N" to "restricted mask" in all tables/figures.  

---

#### III. Summary Recommendation  
**MAJOR REVISIONS**  

**Justification**: The paper reports a technically sound null dipole result with sub-percent sensitivity, but critical flaws prevent acceptance:  
- **Provenance failures**: Headline scalars (n=5.5M, −0.12σ) lack machine-readable sources, violating reproducibility standards.  
- **Arithmetic inconsistency**: The 99.3%/12%/88% decomposition is self-contradictory and undermines the leakage channel narrative.  
- **Presentation risks**: Incomparable σ values in the abstract without prominent disclaimers could mislead readers.  
- **Length**: At 56pp, the paper is 2× longer than PRD norms; trimming to 30pp is essential.  

Addressing these issues will transform the manuscript into a rigorous, reproducible PRD contribution. The core science—demonstrating that monopole-mask leakage can mimic dipole signals—is compelling and merits publication after revisions.