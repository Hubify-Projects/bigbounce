# P3 2026-06-04_R5clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 42.3s

---

I cannot perform the requested citation-forensics audit without access to the paper’s bibliography and to the full manuscript beyond what you pasted.

What you provided is a very large excerpt of the body text plus an abbreviated references block ([1]–) with only partial metadata, but not:

- the full reference list with titles, arXiv IDs, DOIs, and author lists, nor  
- the complete paper (all sections, all tables, all reference callouts) in a way that lets me map every in-text citation to a specific reference entry.

Because of that, I cannot reliably:

- check that each in-text “[n]” matches the correct title/authors/venue/arXiv ID,  
- verify that specific quoted numbers/statements truly appear in the cited paper, or  
- detect fused metadata, incorrect “in preparation” statuses, or incorrect DOIs.

To do what you asked (full, per-citation forensic audit) I would need:

1. A complete PDF or LaTeX of the paper, including:
   - the full reference list with titles, arXiv IDs, DOIs, and journal info;
   - page/section numbers; and
   - all figures/tables and their captions.

2. The ability to cross-check every reference via arXiv and NASA ADS.

Given the constraints, I can only comment on limited aspects that are visible in the excerpt and partially check a few references where the paper already gives enough metadata.

Below I list concrete issues I can identify from the excerpt itself, but this is **not** a complete citation audit; it is only what can be seen and checked from the supplied text.

---

## Findings

### P3-E1 (ESSENTIAL) – No evidence you have normalized σ-values across null procedures

**Location**: Multiple places in abstract / Section V where σ(fNL) forecasts are compared:  
- initial multi-tracer forecast vs “Heinrich+2024 σ(fNL) ≈ 0.7”  
- your internal Fisher σ(fNL) ≈ 0.07–0.12  
- literature consensus “Münchmeyer et al.  σ(fNL) ≈ 0.4–0.9”  
- NANOGrav-related σ/Δχ²/Bayes factor comparisons.

**Problem**:  
The instructions you gave me require:

> If any σ values from different null procedures are presented as if they’re on the same scale without qualification, flag this as ESSENTIAL.

The manuscript repeatedly places different σ(fNL) forecasts and constraints, obtained under different assumptions, data sets, or Fisher setups, side by side as if directly comparable, without consistently and clearly stating the different systematics, priors, and modeling assumptions that go into each:

- Your “internal Fisher diagnostic” giving σ(fNL) ≈ 0.07–0.12 is treated as a numerical object and only partially caveated as “not used as the headline forecast”, but it appears adjacent to literature consensus values without a clear, explicit warning that it uses a different, more optimistic kernel and systematics treatment than e.g. Münchmeyer et al. .  
- The Heinrich et al.  σ(fNL) ≈ 0.7 baseline is cited and used as a benchmark, but it is not made clear whether noiserealization assumptions, redshift-bin choices, k-cuts, and nuisance-parameter priors are aligned with your Fisher engine.  
- In the PTA section, your Δχ² interpretation and Savage–Dickey Bayes-factor statements compare a bounce template and an SMBHB template using a free-spectrum KDE likelihood; that is a different “null procedure” than the Fisher forecasts above. Yet, in the narrative, all these σ, z, and Bayes-factor numbers appear in one continuous “cosmology applications” story.  

Even where individual caveats do appear later in §VI D, an expert reader would have to stitch them together manually. The paper does not clearly label, *each time a σ is quoted*, which null-hypothesis/likelihood structure/parameter space is being used and that these σ’s are **not directly commensurate**.

**Required fix**:

- Add, near the first appearance of each σ(fNL) or σ(γ) value, an explicit label of the procedure and assumptions (e.g. “single-tracer DESI Fisher, idealized systematics-free;” “multi-tracer Fisher with fixed α and no GR correction;” “internal Fisher with δs, δb, δσz priors;” “NANOGrav free-spectrum KDE likelihood, power-law-only GWB model”).  
- For every comparison in the text where two σ’s from different procedures are put side by side, explicitly state that they are not strictly on the same scale and why (different datasets, different nuisance blocks, different cosmological parameter spaces).  
- Make sure the abstract does **not** summarize any cross-procedure σ comparison as if it were a single axis of improvement. If necessary, drop σ comparisons from the abstract and keep them in a well-labeled cosmology methods section.

Until this is fixed, the paper risks misleading readers about the relative constraining power of different approaches and violating the rule you gave me about σ comparisons.

---

### P3-E2 (ESSENTIAL) – Version-history / audit language appears throughout main text

**Location**: Many places, including the first page and throughout §II and §VI D, e.g.:

- “ROUND: 2026-06-04_R5clean” (in your prompt, and similar style phrases in the paper)  
- “Path-C rebuild”, “Path-C native retrains”, “Path-B re-measurement”, “Pipeline-1”, “wave14 ii fisher systematics”  
- “artifact: fw6 stability/fw6 stability results.json”, “companion artifact: pipelines/p3 anomaly engine/...”, “r42 outputs/B11 shot noise fisher.json”

**Problem**:  
The paper reads like an internal technical changelog in many places. There is extensive “pipeline wave” terminology (“wave 14”, “Path-C rebuild”), explicit references to internal filenames, JSON artifacts, and prior draft logic (“earlier versions quoted X; here Y supersedes it”). These clearly constitute version-history and internal review artifacts, which you told me must be flagged.

This language is not appropriate for a PRD methods paper and will seriously impede readability and long-term clarity. It also makes it harder for a reader to see the *final* procedure as a clean, reusable method.

**Required fix**:

- Remove all explicit references to internal pipeline names (“Path-B”, “Path-C”, “wave14 ii”, etc.), JSON file paths, and changelog-style comments from the main body.  
- Replace them with a clean, linear description of the *final* analysis pipeline, possibly with one short subsection (or Appendix) describing “earlier pipeline variants and why they were abandoned,” but without internal filenames or version codes.  
- If you want to share detailed artifacts, move all paths, JSON filenames, “artifact:” tags, etc. to a data-release README or a GitHub companion, not to the PRD manuscript.  
- Ensure that the main text is free of “R5”, “wave”, or similar round labels; the only “dated” entities should be publication dates and data releases.

---

### P3-M1 (MAJOR) – Abstract overstates and conflates multiple main claims

**Location**: Abstract (opening block).

**Problem**:

1. The abstract narrates several distinct contributions:  
   - largest-scale multi-survey anomaly catalog;  
   - novelty fraction measurement;  
   - LAMOST training-bias “lesson”;  
   - multi-tracer fNL forecast;  
   - PTA spectral-index consistency.  

   These are intertwined in one very long paragraph and it is not clear *what the main proven contribution is*, especially from the perspective of PRD (cosmology methods) versus catalog construction.

2. Several statements are phrased in a way that suggests stronger cosmological impact than is actually supported later:
   - You emphasize a “canonical σ(fNL) = 8.14” and a “9.6×” bias enhancement ratio for a Gold+Silver subset, but only much later do you stress that these are consistent with no improvement at <1σ.  
   - The abstract says “Cosmological applications of the anomaly-selected tracers … are summarized inline using primary-source methodology” which reads overly strong given that all cosmology results are forecasts with large error bars and multiple caveats.

3. The abstract gives very detailed internal numbers (e.g. 378,080 vs 378,280 split, 73%, 21.5×, etc.) that are better suited to the body; yet, it does not succinctly state the key *safe* cosmology result: namely that your current empirical α is consistent with zero and the catalog’s cosmological role is **prospective**.

**Required fix**:

- Rewrite the abstract in 2–3 short paragraphs that clearly separate:
  - (i) the catalog construction and anomaly-detection methodology;  
  - (ii) the training-bias and null-result lessons (LAMOST, CMB, Planck×ACT);  
  - (iii) the *exploratory* cosmology forecasts, clearly labeled as non-detections with large uncertainties.  
- Make sure the abstract never implies an fNL detection or a strong PTA model-preference claim; it should say explicitly that the empirical α measurement is consistent with zero and that the σ(fNL) improvements are forecasts pending higher S/N.  
- Reduce numerical clutter in the abstract: keep one or two key scale numbers (total anomalies; novelty fraction) and a brief high-level sentence about possible cosmology applications.

---

### P3-M2 (MAJOR) – “Heinrich et al. ” citation and description need tightening

**Location**: Introduction, around:

> “the multi-tracer methodology of Heinrich et al.  (anchored to the Heinrich+2024 σ(fNL) ≈ 0.7 bispectrum-only forecast as the headline external benchmark; an internal Fisher diagnostic computation gives σ(fNL ) ≈ 0.07–0.12 … and is held aside as an internal-consistency check …).”

**Checking against the literature**:

-  is given as “C. Heinrich, O. Doré, and E. Krause … JCAP 2024, 074 (2024)” in your references. That matches arXiv:2311.13082 / JCAP 01 (2024) 074, “Measuring fNL with the SPHEREx Multi-tracer Redshift Space Bispectrum.”[1][2]  
- That paper presents Fisher forecasts for SPHEREx multi-tracer *bispectrum* constraints and finds σ(fNL) ∼ 0.7 (exact numbers depend on tracer combinations and k-cuts).[1][2]

Your description that Heinrich et al. provide a σ(fNL) ≈ 0.7 “bispectrum-only” forecast is broadly accurate, but:

- You then mention an “internal Fisher diagnostic” giving σ(fNL) ≈ 0.07–0.12 which is *much* tighter than any published SPHEREx forecast. You call this an “internal-consistency check,” but it is not clear how that check is constructed relative to Heinrich+24 (which is a different observable and different covariance structure).  

**Required fix**:

- Explicitly state that Heinrich et al.  is a **bispectrum** forecast and that your internal Fisher engine is not replicating their calculation; it is a separate, optimistic test with different assumptions.  
- Add a one-sentence disclaimer each time you mention σ(fNL) ≈ 0.07–0.12 that it is “an internal, optimistic Fisher exercise not directly comparable to the σ(fNL) ≈ 0.7 bispectrum forecast of Heinrich et al. ” and is not used as any headline cosmology figure.  
- Verify that the exact σ(fNL) ≈ 0.7 number you quote matches Heinrich+24’s fiducial scenario (you may need to specify whether this is their full multi-tracer, their most optimistic configuration, etc.).

---

### P3-M3 (MAJOR) – PTA section overstates evidence for matter-bounce versus SMBHB

**Location**: Section V.A (NANOGrav bounce consistency).

**Problem**:

- You fit a two-parameter power-law model to the NG15 HD-correlated free-spectrum KDE, and you find γ = 2.567 ± 0.382, log10 A ≈ −14.0.  
- You compute that γ = 3.0 (matter-bounce prediction) is at +1.13σ, γ = 4.33 (SMBHB) is at +4.61σ.  
- You then quote Bayes factors like B_matter-bounce/SMBHB ≈ 7×10³ (“decisive”), and at least in some sentences the narrative is close to implying that NANOGrav *favors* matter-bounce over SMBHB strongly.

Given NANOGrav’s own multi-model analyses, the current data do **not** decisively rule out SMBHB backgrounds; they find correlated stochastic backgrounds consistent with SMBHBs and leave room for other physics.[3][4] Their “new physics” companion paper (Afzal et al. 2023) explores multiple spectral shapes but does *not* claim bounce cosmology is favored at such strong Bayes factors over SMBHB.[4]

Your Savage–Dickey calculation is being done in a *restricted, two-parameter power-law* space using a particular prior on γ and logA, and using the free-spectrum KDE as a pseudo-likelihood. This is an internal modeling choice; presenting the resulting Bayes factor as though it reflects broad “SMBHB ruled out” evidence is easily misread.

**Required fix**:

- Tone down all language in this section:  
  - Emphasize that your Bayes factors apply **only** within a restricted power-law model class and specific priors, not as global evidence against astrophysical SMBHB backgrounds.  
  - Add a clear statement that NANOGrav’s own model-comparison analyses do *not* claim such a strong disfavouring of SMBHBs and that your result should be treated as a toy example of how the catalog could connect to PTA cosmology, not as a robust physical conclusion.  
- Make sure the abstract does **not** mention PTA Bayes factors at all; keep this as a technical appendix-level result or a short subsection with strong caveats.

---

### P3-M4 (MAJOR) – Length and scope creep

**Location**: Whole manuscript (49 pages).

**Problem**:

- For PRD, 49 pages is long even for a complex methods/catalog paper, and a large fraction of the length is taken up by internal pipeline discussions, multiple re-derivations, and extensive appendices whose level of detail (e.g., JSON path names, internal stability metrics) goes beyond what is needed for the scientific argument.  
- The cosmology sections in particular read like a partial second paper (on Fisher matrices and PTA model selection), which distracts from the main, well-posed catalog/methods contribution.

**Required fix**:

- Target a maximum of ≈ 30–35 pages including appendices for PRD. Concretely:
  - Move almost all JSON path references, internal filenames, and “artifact bundles” to an external data-release note or GitHub; in the paper, keep only a short “Reproducibility and data access” subsection.  
  - Consider splitting the PTA and the more speculative Fisher-systematics exploration into a separate cosmology-focused paper; in this catalog paper, you can keep a 1–2 page “Outlook: potential cosmology use-cases” section with no detailed Bayes-factor calculations.  
  - Compress the DEsi/SDSS/LAMOST individual survey sections: many pages repeat the same architecture description and validation logic; you can factor those into a single Method section plus a concise per-survey table.

---

### P3-m1 (MINOR) – Reference /[1] (Challinor & Lewis) metadata

**Location**: References  and [1] at end.

You list:

>  A. Challinor and A. Lewis, “Linear power spectrum of observed source number counts,” Phys. Rev. D 84, 043516 (2011).

Cross-check:

- The correct title is “The linear power spectrum of observed source number counts.”[1][2]  
- DOI 10.1103/PhysRevD.84.043516; arXiv:1105.5292.[2]

**Required fix**:

- Ensure the title capitalization and wording match the journal version (leading “The”), and add the arXiv ID in the reference list.  

This is minor but easy to fix; it also demonstrates that at least one reference matches the correct paper.

---

### P3-m2 (MINOR) – Potential duplicate / inconsistent reference labeling

**Location**: Ref.  / Heinrich et al.; also  Münchmeyer et al.

- In the text you refer to “Heinrich+2024” and mention that the bibkey is kept as “Heinrich2023” in some comment. Check that the actual reference label in your bibliography matches the in-text usage.  
- For Münchmeyer et al. , check that the journal and year match the final accepted version (2019, Phys. Rev. D 100, 083508; arXiv:1810.13424).[5]

**Required fix**:

- Make sure all in-text references use the same year and label as the bibliography entries; remove comments like “bibkey label retained as Heinrich2023” from the reference text—the reader does not see your .bib file.

---

### P3-n1 (NIT) – Several very long sentences and parenthetical asides

**Location**: Throughout; notable in the abstract and in §V and §VI D.

**Problem**:  
Many sentences exceed 5–6 nested clauses, with multiple parentheticals. This substantially reduces readability and increases the risk of logical ambiguity (e.g., where exactly a caveat applies).

**Required fix**:

- Split the longest sentences into two or three shorter, declarative sentences.  
- Move long parenthetical caveats into footnotes or a short “Caveats” paragraph following key results.

---

### P3-n2 (NIT) – Miscellaneous stylistic / formatting nits

- Use consistent notation for fNL (no mix between fNL and fNL ).  
- Ensure Greek letters and subscripts in equations are rendered with LaTeX and not inline prose typos.  
- Remove quotes around terms like “before / after” unless absolutely necessary.

These are cosmetic but will improve clarity.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The catalog and anomaly-detection methodology are promising and potentially impactful; however, the manuscript in its current form is far too long and carries substantial internal-pipeline and cosmology-extrapolation baggage. The mixing of different σ and likelihood procedures without very explicit separation is problematic under your own stated standard, and the PTA section in particular overinterprets a restricted power-law toy model. A thorough rewrite focusing on (i) a clean, survey-agnostic methods description, (ii) the catalog itself and the training-bias lessons, and (iii) only modest, clearly labeled cosmology “use cases” is necessary before the paper can be acceptable for PRD.