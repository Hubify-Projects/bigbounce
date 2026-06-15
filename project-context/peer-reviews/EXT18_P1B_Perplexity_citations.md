# P1B EXT18 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/arxiv/paper1b_mcmc_companion.pdf` md5=5a3c98e9 pages=21
**Input format**: TEXT + web search + pass-2 self-critique (12724 chars)
**Wall time**: 100.6s

---

The manuscript cannot be reliably audited to Physical Review D standards because the rendered PDF is not actually available to inspect; only a text dump is provided, and I cannot see the figures, table layouts, actual equation rendering, or the bibliography formatting. That means I cannot fulfill core parts of your instructions (dimensional checks on equations, axis-label inspection, recomputing numbers directly from plots, verifying that every quoted statistic matches the cited paper’s tables, etc.). I will instead treat the provided text as a proxy and audit as far as the text allows, focusing on citation correctness, internal numerical consistency, and stated claims.

Below I list findings, grouped and tagged as requested. Page numbers are approximate, based on where the text appears in the dump.

---

### P1B-E1 – “In preparation” companion papers as references

- **Section + page**: Introduction, p.2  
- **Problem**: The manuscript cites multiple “in preparation” companion papers as numbered references:  
  - “[6] H. Golden, fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, (2026), companion paper, posted concurrently on arXiv.”  
  - “[7] H. Golden, Spectrally Unusual Sources at Scale … (2026), companion paper, posted concurrently on arXiv.”  
  - “[8] H. Golden, Galaxy Chirality at Scale … (2026), companion paper, posted concurrently on arXiv.”  
  In the main text they are called “in preparation” in the Introduction (“SPHEREx multi-tracer Fisher forecast (in preparation, [6])”, “multi-survey anomaly catalog (in preparation, [7])”, “galaxy chirality catalog (in preparation, [8])”). At the end, the reference list assigns them explicit 2026 dates and describes them as “companion paper, posted concurrently on arXiv.” This is contradictory provenance: the body claims “in preparation”, the references claim public arXiv status. For PRD, “in preparation” references are disfavoured and must not be load‑bearing; concurrently posted arXiv preprints need actual arXiv identifiers. No arXiv IDs are given anywhere for [1], [6]–[8].  
- **Required fix**:  
  - Decide the true status of [1], [6], [7], [8]. If they are on arXiv, provide correct arXiv IDs, titles, and (if applicable) journal info in the references, and change all “in preparation” wording in the body to “companion paper” (or similar) consistently.  
  - If any are genuinely not yet on arXiv, remove them as numbered references or clearly mark them as “unpublished, internal note; not used for any load-bearing claim,” and ensure no quantitative or methodological claim in this paper *depends* on them.  
  - For PRD, any load-bearing external result must be in a public, citable form; if Paper I(a) [1] is essential for the “no-go” interpretation, this paper is not stand-alone and must either (i) be merged with I(a) or (ii) cite I(a) as an actual arXiv/J/PRD paper with an identifier.

**Severity**: ESSENTIAL.

---

### P1B-E2 – Paper I(a) [1] and this paper are not stand‑alone (standalone-reader test)

- **Section + page**: Introduction, p.2; Conclusions, p.14–15.  
- **Problem**: The Introduction explicitly states: “This companion paper provides the technical verification layer for the ECH structural-closure no-go result reported in Paper I(a) [1]. Paper I(a) establishes … and motivates the numerical cross-checks of this companion.” Many of the conceptual claims (“13 barriers,” “perturbation-transparency theorem,” “14-barrier table,” “minimal-ECH parameter space is closed”) are only defined in Paper I(a). This manuscript repeatedly frames its results as “technical verification” and relies on the structural conclusions of [1] to motivate the calculations. As written, a reader who has not read [1] cannot understand the full scientific argument or how the numerical checks actually test the no-go result. That fails your own standalone-reader requirement and also PRD’s norm that each paper should be scientifically self-contained.  
- **Required fix**:  
  - Either (a) merge the conceptual content of Paper I(a) into this manuscript so that all assumptions, definitions (ECH model, Holst sector, “minimal bounce” class, etc.), and the meaning of the “no-go” claim are fully defined here; or (b) explicitly narrow the scope of this paper to “technical validation of generic pipelines (ΛCDM+ΔNeff MCMC, NaMaster pseudo‑Cℓ, ALP birefringence consistency)” and remove all language that suggests it confirms the ECH structural-closure program, postponing that interpretation to Paper I(a) once it is published.  
  - If you want PRD to publish this paper as a standalone methods piece, the abstract and conclusions must be rewritten to describe only *what is proved in this document*, without claiming to support the closure of ECH dark energy.

**Severity**: ESSENTIAL.

---

### P1B-E3 – Use of “in preparation” work in scope statements / forecasts

- **Section + page**: Introduction, p.2; Conclusions, p.14; Appendix A.  
- **Problem**: The text repeatedly refers to future work or “Paper II–IV” as if they are concrete deliverables (“SPHEREx multi-tracer Fisher forecast … is the subject of Paper II,” “multi-survey anomaly catalog … is the subject of Paper III,” “galaxy chirality catalog … is the subject of Paper IV”). These are not yet public and have no arXiv IDs; yet they are used to contextualize the importance of this work and to define program scope. PRD generally discourages embedding internal roadmap / version-history language and “promissory” references in the body; it also makes it difficult to interpret the current paper on its own merits.  
- **Required fix**:  
  - Remove or drastically shorten all roadmap language (“Paper II,” “Paper III,” “Paper IV”) from the body and conclusions, or move it to a short Outlook paragraph that is clearly speculative and does not affect the interpretation of any result here.  
  - Ensure that no key claim in this paper requires definitions, numerical results, or methods from those future papers.

**Severity**: MAJOR (could be ESSENTIAL if any of those future papers are actually needed for the logic; see E2).

---

### P1B-E4 – Abstract contains structural ECH claims not demonstrated in this paper (pattern‑045)

- **Section + page**: Abstract, p.1; Introduction, p.2; Conclusions, p.14.  
- **Problem**: The abstract starts “We report the technical verification material for the Einstein-Cartan-Holst (ECH) spin-torsion cosmology no-go program of Paper I(a) [1].” It then lists three analyses, each explicitly framed as *not* directly testing torsion (ΔNeff proxy uses stock CAMB; NaMaster is method validation on ΛCDM; spectator ALP is the same in GR and ECH). This paper does not derive the ECH spin-torsion model, does not implement a torsion Boltzmann code, and repeatedly says the key “no-go” result and “13 structural barriers” reside in Paper I(a). The abstract’s first sentence therefore overstates what is *proved here*: this paper verifies general-methods proxies, not the ECH spin‑torsion program per se.  
- **Required fix**:  
  - Rewrite the abstract so that every sentence describes *only* what is demonstrated within this manuscript. For example:  
    - Clearly say that ΔNeff is a ΛCDM extension used as a **proxy**, not a direct torsion test.  
    - State that NaMaster validation is a pure pipeline check on synthetic ΛCDM skies.  
    - State that the spectator-ALP calculation is a GR+ALP consistency check with fine-tuning and is not an ECH-specific prediction.  
  - Remove or qualify any wording that implies this paper itself establishes a “no-go” for ECH dark energy. If you wish to mention Paper I(a), it must be framed as “see [1] for conceptual arguments; here we only provide technical checks of generic ΛCDM/ALP pipelines.”

**Severity**: ESSENTIAL.

---

### P1B-E5 – Σ/σ “significance” statements without effect-size interpretation (pattern‑19)

- **Section + page**: Multiple, e.g. Abstract p.1; Sec. II–III, p.2–5; Sec. VI, p.10–13; Table II p.20.  
- **Problem**: Many tail-distance numbers are quoted (e.g. “∼ 3.6σ tension,” “+4.3σ,” “−3.6σ,” “3.2σ,” “9σ forecast” for LiteBIRD) with essentially no effect-size discussion beyond a sentence or two. In some places you do compute a fractional change (e.g. H(z = 0.5) differs by ≈ +1.7%), but this is not systematically attached to each headline σ value. For PRD—and for your own stated standard—every χ²/σ headline should carry a quantitative effect-size (fractional change, parameter shift relative to prior width, etc.).  
- **Required fix**:  
  - For each prominent σ / “tension” / “significance” number in the abstract, main body, and tables, add an explicit statement of the corresponding *effect size* (e.g., “4.3σ in w0 corresponds to a 0.19 shift from −1,” “9σ LiteBIRD forecast corresponds to β/σ ≈ 9 for β ≈ 0.27°”).  
  - Where two σ-values are being qualitatively compared but refer to different null procedures or error models (e.g. 3.6σ from WMAP+Planck vs 3.9σ naive inverse-variance Planck+ACT), explicitly label them “not directly comparable” at each juxtaposition. You do this once in Sec. IV–VI, but the abstract and conclusions still present multiple σ’s near each other without that reminder.

**Severity**: MAJOR.

---

### P1B-E6 – Sigma from different null procedures juxtaposed without repeated “not directly comparable” warnings (pattern‑07)

- **Section + page**: Abstract, p.1; Sec. II–III, p.2–5; Sec. VI, p.10–13; Conclusions, p.14.  
- **Problem**: The text juxtaposes:  
  - “residual ∼ 3.6σ tension with the SH0ES local‑distance‑ladder H0” in the abstract;  
  - 3.2σ when projecting onto MB;  
  - 2.5σ S8 tension;  
  - 3.6σ WMAP+Planck birefringence;  
  - 3.9σ naive Planck+ACT combination;  
  - 9σ LiteBIRD forecast;  
  sometimes in the same paragraph. While in some locations you explicitly state that, e.g., 3.6σ is from the published analysis and 3.9σ is an optimistic upper bound, the reader could still interpret them as directly comparable “σ” significance measures. Your own instructions require that “if sigma values from different null procedures appear side-by-side without explicit ‘not directly comparable’ qualification at every juxtaposition, flag ESSENTIAL.”  
- **Required fix**:  
  - In every place where two independent σ-values are mentioned within one paragraph or sentence, explicitly state that they are computed under different likelihoods / datasets / error models and *not directly comparable* as statistical tests.  
  - Consider moving some of these supporting σ-values to footnotes to avoid a “σ salad” that invites misinterpretation.

**Severity**: ESSENTIAL.

---

### P1B-E7 – “3.2σ” MB shift is not clearly supported by a proper tension definition (pattern‑048)

- **Section + page**: Sec. III, “MB–H0 joint-posterior offset check,” p.5.  
- **Problem**: The manuscript quotes “This offset is ∼ 3.2σ relative to the chain’s σMB = 0.049 marginal width.” That “σ” is defined only using the *chain’s* MB dispersion, not combining all relevant uncertainties (Pantheon+ covariance, SH0ES MB prior, correlation with H0). You do partially acknowledge this later (“this 3.2σ figure is a descriptive offset … not a properly conditioned tension statistic”), but the standalone “3.2σ” number still appears as a headline within that paragraph.  
- **Required fix**:  
  - Either remove the 3.2σ label entirely here or rewrite the sentence to avoid σ language: e.g. “the offset is 0.156 mag, about 3.2 times the chain’s marginal σMB, but this is not a proper tension statistic because it ignores covariance.”  
  - Make sure the abstract does not rely on this figure at all.

**Severity**: MAJOR.

---

### P1B-E8 – Use of internal file names / branch labels / version strings in the main text (patterns 8 and 16)

- **Section + page**: Sec. III–VI, Appendix A–C, multiple pages.  
- **Problem**: The main text is full of internal pipeline names, file names, branch labels, and version IDs (e.g. “spin_torsion.input.yaml,” “iter2 w0 wa,” “c15_converged,” “reproducibility/p1_namaster_500mc/results/c10_robustness_battery.json,” “branch_R_alp_birefringence,” v1B.0.72, etc.). While very useful for an internal reproducibility note, this is not standard PRD practice and makes the paper read like a repository README rather than a journal article. It also introduces effectively version-history language into the body.  
- **Required fix**:  
  - Move the detailed path and filename references to an online supplementary material or a short “Reproducibility Note” section, and compress the main text to high-level descriptions (“we performed 500 Monte Carlo realizations using NaMaster; configuration details are available in the online supplement”).  
  - Remove internal branch names and version tags (v1B.0.72, “iter2,” etc.) from the main narrative; keep only a minimal code-version statement in the Data Availability section if essential.

**Severity**: MAJOR.

---

### P1B-E9 – “Column-permutation warning” and audit-log style text in body (pattern‑046/047)

- **Section + page**: Data and Code Availability, p.15; Appendix A.  
- **Problem**: There is a long paragraph about a “column-permutation bug” in `parameter_summary.json`, advice on using `_CORRECTED.json`, and references to `CHANGELOG.md` and `parameter_summary_units_README.md`. This is essentially audit-log prose that belongs in a software release note, not in a PRD article. It distracts from the scientific content and clutters the Data Availability section.  
- **Required fix**:  
  - Condense this into a single sentence in an appendix or supplement: e.g. “An early diagnostic export had a column-order bug; all results in this paper are based on the corrected files described in the repository changelog.”  
  - Remove file-specific instructions from the main text.

**Severity**: MINOR.

---

### P1B-E10 – Data availability / reproducibility surfaces incomplete

- **Section + page**: Data and Code Availability, p.15; Appendix A.  
- **Problem**: The manuscript claims that “All materials are at: https://github.com/Hubify-Projects/bigbounce/tree/main/reproducibility” and references multiple HuggingFace datasets, but:  
  - No DOI is provided for any dataset.  
  - There is no explicit frozen-release tag (e.g. git tag, Zenodo DOI) corresponding to the exact version used for this paper—only a commit hash b22f8cc9 and an internal “v1B.0.72” string.  
  - For the core cosmology chains, you say “Fresh ΛCDM+ΔNeff proxy chains … are NOT bundled and must be regenerated locally,” which contradicts the earlier statement that the chains backing Tables I–II are committed. The description is confusing and not at the “download-and-run” clarity expected for reproducibility.  
- **Required fix**:  
  - Register a frozen data/software release (e.g. via Zenodo) tied to a specific git tag and provide that DOI in the Data Availability section.  
  - Carefully distinguish which artifacts are bundled (chains, masks, ALP chains) and which are to be regenerated, and ensure a competent reader could reproduce your figures by following a short, clear set of steps.  
  - For PRD, the HuggingFace URLs are fine as *additional* pointers, but there should be a citable DOI or similar persistent identifier.

**Severity**: MAJOR.

---

### P1B-M1 – Claim that this paper “confirms” or “supports” ECH no‑go is not adequately supported

- **Section + page**: Introduction p.2, Conclusions p.14–15.  
- **Problem**: The narrative implies that the three checks “support” the ECH structural no‑go program. But:  
  - The ΛCDM+ΔNeff run is a completely generic ΛCDM extension and is interpreted in terms of a *minimal matter-bounce class* that happens to predict ΔNeff ≈ 0—but there is no actual ECH torsion computation of Neff, and the paper itself notes that minimal ECH does not produce a recombination-era ΔNeff.  
  - The NaMaster validation is explicitly independent of ECH and is just a pseudo-Cℓ pipeline check on ΛCDM skies.  
  - The spectator-ALP birefringence is explicitly non‑distinctive: the same signal arises in GR+ALP.  
  Thus, none of the calculations directly test the ECH framework or its “13 barriers.” The only sense in which they “support” ECH is via compatibility with generic cosmology and a motivated ALP scenario, which is a weaker statement than implied.  
- **Required fix**:  
  - Tone down all claims that these analyses “support” or “verify” the ECH no-go result; instead, describe them as “methodological consistency checks” and “generic cosmological constraints consistent with, but not uniquely supporting, the ECH scenario.”  
  - Make it unambiguous that no observable computed here distinguishes ECH from standard ΛCDM+ALP.

**Severity**: MAJOR.

---

### P1B-M2 – Use of “fine-tuning” and “25× tuning” needs explicit numeric demonstration in main text

- **Section + page**: Abstract p.1; Sec. VI pp.10–13; fn. 6; Table IV.  
- **Problem**: The paper repeatedly states that spectator status “requires a ∼25× misalignment tuning” and that the θi ~ 0.1 sliver is tuned. You sketch the scaling (Ωa ∝ θi²) and mention Ωa(0.1)/Ωa(0.5) ∼ 1/25 in a footnote, but there is no explicit numerical worked example in the main text for “typical” parameters, nor any table row showing Ωa values at θi = 0.5 vs 0.1. For PRD’s standards and for clear communication, a central claim about “fine‑tuning” should be quantitatively demonstrated in the main body.  
- **Required fix**:  
  - Add a short numerical example in Sec. VI showing Ωa for two or three representative parameter points (e.g. m ≈ H0, fa ≈ MPl, θi = 0.5 vs 0.1), explicitly computing the ρa and Ωa values to illustrate the “25×” statement.  
  - Tie that example directly to the Ωa < 0.01 threshold used in Table IV so the reader can see why θi ≪ 1 is required.

**Severity**: MAJOR.

---

### P1B-M3 – ALP prior choices and posterior truncations under‑explained for a PRD audience

- **Section + page**: Sec. VI pp.10–13; Appendix C.  
- **Problem**: The ALP MCMC setup is intricate (different Caγ priors [1,30] vs [4,60]; flat θi vs flat cosθi; log10 ma ranges; multiple configurations run1, run2, c5). While you do explain many of these in detail, the reader has to piece together how the prior boxes relate to the “natural” region (m/H0 ∈ [1,3], θi ∈ [0.5,2]) and to the posterior-dominated regime (m ~ 36 H0, Caγ ~ 10–50). The discussion of the posterior mass truncated above Caγ = 30 and the subsequent rerun is scattered across paragraphs. This is close to adequate but still confusing for a non-expert.  
- **Required fix**:  
  - Add one concise table or paragraph summarizing the ALP runs: for each configuration (fixed Caγ, Caγ-free [1,30], Caγ-free [4,60]), list priors and the fraction of posterior mass touching or being truncated by the prior edges.  
  - Explicitly state in Sec. VI that the [1,30] run truncates ~28% of the posterior at the upper edge and that the [4,60] run is used for all final coupling statements.

**Severity**: MINOR.

---

### P1B-M4 – Use of “quintom-B” label without a minimal self-contained definition

- **Section + page**: Sec. III, Sec. V.C, p.4–5, 10.  
- **Problem**: The paper references “quintom-B” repeatedly and cites [27] as a general quintom cosmology review, but the specific “quintom-B” subclass is not defined in this paper. You give the CPL w0, wa values and argue for phantom crossing, but a reader unfamiliar with your Paper I(a) will not understand what precisely “quintom-B” means.  
- **Required fix**:  
  - Add a brief definition of “quintom-B” in Sec. V.C (e.g. specify the behavior of w(a), whether it crosses −1 once, etc.), independent of Paper I(a).  
  - Clarify that the observed w0, wa posterior sits in that region but that this is a purely phenomenological label, not a claim about an underlying field model in this paper.

**Severity**: MINOR.

---

### P1B-M5 – Length and density relative to contribution

- **Section + page**: Whole paper (21 pages including long appendices).  
- **Problem**: For what is claimed—three primarily methodological checks with no new detections and no new model-exclusion evidence—21 pages is excessive. A substantial fraction of the pages is devoted to internal path names, chain IDs, detailed robustness batteries, and claim‑classification tables. Much of this is valuable as supplementary information but not necessary in the main PRD article.  
- **Required fix**:  
  - Target a main-text length of ~12 pages for PRD: compress robustness details into short summaries, push file-path specifics and claim‑classification tables into online supplemental material, and retain only the crucial numerical results and conceptual caveats in the body.  
  - Keep Appendix C if needed for ALP details, but streamline Appendix A/B.

**Severity**: MAJOR.

---

### P1B-N1 – Minor duplicate / near-duplicate phrasing

- **Section + page**: Sec. IV–VI and Conclusions, multiple instances.  
- **Problem**: Certain phrases are repeated nearly verbatim in many sections, e.g. “pipeline-recovery figure, not a sky-detection significance claim,” “not a competitive sky measurement,” “the same prediction arises in GR.” While this is not a mechanical duplicate like “canonical canonical-mask,” it does make reading more tedious and could be tightened.  
- **Required fix**:  
  - Slightly vary or compress repeated explanatory phrases across sections, or refer back to the first detailed statement instead of restating in full.  

**Severity**: NIT.

---

### P1B-N2 – Reference formatting and missing identifiers

- **Section + page**: References, p.17–18.  
- **Problem**: Some references are partially specified:  
  - [3], [4] include arXiv IDs and journal names, which is good.  
  - [1], [6], [7], [8] lack arXiv IDs or journal info; they are only described as “(2026), companion paper, posted concurrently on arXiv.”  
  - For a methods-heavy paper, DOI information for key observational references ([21] Planck; [15] Pantheon+; [19] DESI DR2) should ideally be included, though that is a style issue more than a hard requirement.  
- **Required fix**:  
  - Once you have the actual arXiv numbers for [1], [6], [7], [8], add them. Until then, do not call them “posted concurrently on arXiv.”  
  - Ensure the reference formatting matches PRD style (journal name, volume, page, year, arXiv ID).  

**Severity**: MINOR.

---

### P1B-N3 – Occasional overuse of footnotes for load-bearing content

- **Section + page**: Sec. III and VI, multiple footnotes (e.g. fn. 1, fn. 2, fn. 6).  
- **Problem**: Some crucial clarifications (e.g. burn-in definition reconciliation, EFT validity of torsion four-fermion operator, spectator-status backreaction scaling) are placed in long footnotes rather than in the main text. For clarity and PRD readability, load-bearing physics and statistical caveats should be in the main narrative.  
- **Required fix**:  
  - Promote key portions of footnotes (especially fn. 2 and fn. 6) into the main text, leaving only implementation minutiae in footnotes.

**Severity**: MINOR.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The manuscript presents careful and unusually transparent methodological work, but in its current form it does not meet PRD standards for a standalone, well-focused physics paper. The core scientific results are conservative (ΔNeff consistent with zero, pseudo‑Cℓ pipeline bias quantified, ALP birefringence consistent but fine‑tuned and non‑distinctive), yet the paper is positioned as a “technical verification companion” to a broader ECH spin-torsion program that is not fully available or citable. Several aspects need substantial revision: clarifying the relationship to Paper I(a) and removing overstatements of what is proved here; cleaning up “in preparation” and companion references and providing proper arXiv IDs; tightening and partly relocating internal-audit and repo-specific text; and systematically qualifying σ-level comparisons and fine-tuning claims with clear effect sizes. With these corrections and a significant condensation of the main text, the work could become a solid methods/consistency-check article suitable for PRD, but it is not yet ready for acceptance.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E11 – Abstract σ‐language for H0 tension inconsistent with body’s more careful treatment (A, E, F, H, J)  

- **Section + page**: Abstract p.1; Sec. II p.2; MB–H0 paragraph p.5.  
- **Problem**: The abstract says “the ∆Neff extension does not reduce the residual ∼ 3.6σ tension with the SH0ES… H0 = 73.04 ± 1.04,” implying that *this* run yields and quantifies the 3.6σ distance-ladder tension.[p.1] In the body, the only 3.6σ figure is explicitly labelled “canonical Hubble tension” from the published comparison, not recomputed from the chain plus SH0ES; the chain’s contribution is to show Planck‑like H0 (67.68 ± 1.06) and ∆Neff ≈ 0, not to *measure* the 3.6σ again.[p.5] The abstract therefore overstates what is numerically established here: it mixes a literature σ (3.6σ) with the new chain’s Planck‑like posterior, without stating that the σ is imported, not recomputed.  
- **Required fix**:  
  - Rephrase the abstract to say explicitly that the “∼3.6σ” is the *published* SH0ES‑vs‑Planck tension and that this run leaves H0 Planck‑like and does not alleviate that published tension.  
  - Optionally include the actual chain‑based offset |67.68 − 73.04| and combined error to show that, at the level of this analysis, the tension is consistent with the canonical 3.6σ value but is not independently re‑estimated here.  

**Severity**: MAJOR.  

---

P1B-E12 – Abstract “∆Neff consistent with zero” lacks the one‑sided limit that is load‑bearing in body (A, F, H)  

- **Section + page**: Abstract p.1; Sec. III p.3; Table I p.19.  
- **Problem**: The abstract quotes two two‑sided posterior means for ∆Neff (−0.020 ± 0.169 and +0.058 ± 0.179) and calls them “consistent with zero,” but omits the one‑sided 95% limits that the body explicitly frames as necessary for any “extra species” interpretation (∆Neff < 0.31, 0.40).[p.3][p.19] In the physics discussion, the one‑sided limits are the actual load‑bearing constraints; omitting them in the abstract weakens the quantitative content and makes “consistent with zero” purely qualitative.  
- **Required fix**:  
  - Add the one‑sided 95% upper bounds (∆Neff < 0.31, 0.40 for ∆Neff ≥ 0) to the abstract, or at least state that the constraints correspond to “no evidence for ∆Neff > 0, with 95% upper limits < 0.3–0.4.”  
  - Make explicit that the two‑sided means quoted in the abstract are not the relevant constraints for “extra radiation” and that a one‑sided interpretation is used in the body.  

**Severity**: MINOR.  

---

P1B-E13 – Abstract LiteBIRD “∼9σ forecast” not tied to explicit arithmetic in body (A, F, H)  

- **Section + page**: Abstract p.1; Sec. VI, “LiteBIRD forecast” paragraph pp.13–14.  
- **Problem**: The abstract calls out a “9σ forecast for LiteBIRD” without showing the arithmetic, inviting readers to treat it as a headline forecast.[p.1] In the body, the LiteBIRD section states σ(β) ≈ 0.03° and β ≈ 0.27°, gives the ratio ∼9σ versus β = 0, and then correctly notes that LiteBIRD will not separate β = 0.27° from 0.342° because that difference is only ≈0.7σ once current errors are included.[pp.13–14] The abstract never mentions this limitation, so the forecast is numerically under‑contextualized at the point where it is most visible.  
- **Required fix**:  
  - In the abstract, either (i) briefly include the arithmetic (β ≈ 0.27°, σ(β) ≈ 0.03° ⇒ ~9σ relative to β = 0) and the caveat that this does not distinguish β = 0.27° from the present 0.342° central value, or (ii) move the 9σ language entirely to the body and replace it in the abstract with a more qualitative statement (“LiteBIRD could measure such a rotation to high SNR”).  

**Severity**: MAJOR.  

---

P1B-E14 – S8 tension numbers internally inconsistent across sections and partially mis‑labelled (A, H, J)  

- **Section + page**: Sec. III caveats p.5; Table I p.19.  
- **Problem**:  
  - The S8 “2.5σ above DES‑Y3” statement uses S8 = 0.8245 ± 0.0089 vs 0.776 ± 0.017, saying Δ = 0.049 against combined σ = 0.019.[p.5] From Table II, Δ = 0.8245 − 0.776 = 0.0485; quadrature gives √(0.00892 + 0.0172) ≈ 0.0191, consistent with 2.5σ but the Δ quoted (0.049) rounds up; not an error, but it would be better to explicitly state 2.5σ derives from 0.0485/0.0191.  
  - For the ΛCDM+∆Neff full‑tension chain, Table I gives S8 = 0.814 ± 0.008 and states the DES‑Y3 Gaussian prior is 0.776 ± 0.017 and that the combined posterior is consistent with the naive two‑Gaussian combination 0.814 ± 0.009 “at the 0.01σ level.”[p.19] Arithmetic check: combining 0.827 ± 0.010 with 0.776 ± 0.017 gives mean 0.8145, σ ≈ 0.0088; the table’s 0.814 ± 0.008 is very close but the claim of “0.01σ level” agreement is slightly overstated: the posterior mean differs by ~0.06σ and the width by ~0.09σ, both fine but not literally 0.01σ.  
- **Required fix**:  
  - In the S8 tension paragraph, explicitly quote Δ = 0.0485 and σcomb = 0.0191 to show the 2.5σ figure is computed, not heuristic.  
  - Relax the “0.01σ level” language to something accurate given the numbers (e.g. “better than 0.1σ in both mean and width”).  

**Severity**: MINOR.  

---

P1B-E15 – NaMaster pipeline “SNR = 20.32, 25.71” juxtaposed with σβ and sky significances without explicit local comparability warnings (A, E, H)  

- **Section + page**: Abstract p.1; Sec. IV (Scope note and production run paragraphs) pp.6–8; footnote 4 p.8; Fig. 3 caption p.7.  
- **Problem**: The paper correctly explains that template‑fit SNRtmpl values (20.32, 25.71) are *pipeline* significances on synthetic skies and not directly comparable to Planck/ACT sky σ’s.[pp.6–8, fn.4] However:  
  - The abstract has “pipeline-recovery bias β̂ − βinj = −0.032°, … carried forward as the observed pipeline bias floor — both are MC pipeline-recovery figures, not sky-measurement systematics, and are not directly comparable to each other’s published sky significances,” which only mentions “sky significances” generically, not the ACT/Planck σ’s that appear later in the same sentence cluster.[p.1]  
  - In Sec. IV, the sentence “The primary sky detection significance is the published Planck/ACT DR6 2.7–2.9σ…; the pipeline SNR figures refer to recovery of injected MC signals and are not competitive sky measurements” appears once,[p.6] but later the text and caption list β̂, σβ, and SNRtemplate numerically together (e.g. β̂ = 0.237°, σβ = 0.029°, SNRtmpl = 20.32; SNRtmpl scaling with fsky) without a repeated “not directly comparable” qualifier at each such juxtaposition.[pp.7–8] Given your own rule that σ‑like numbers from different null procedures must be explicitly labelled non‑comparable when juxtaposed, these later mentions are under‑qualified.  
- **Required fix**:  
  - In any paragraph or caption where SNRtmpl appears numerically alongside σβ, βobs/σobs, or 2.7–2.9σ, explicitly repeat that SNRtmpl is a different statistic and “not directly comparable” to the sky σ’s.  
  - Consider adding a short parenthetical wherever 20.32 or 25.71 appears: “(pipeline template SNR on synthetic skies; not comparable to Planck/ACT sky σ).”  

**Severity**: ESSENTIAL (by the manuscript’s own σ‑comparability rule).  

---

P1B-E16 – Birefringence ALP coupling product Caγ∆ϕ/fa arithmetic only shown once; later inferences not explicitly recomputed (A, H, J)  

- **Section + page**: Sec. VI, “Birefringence value” and “MCMC parameter estimation” pp.11–12; Fig. 4 caption p.14; Table IV p.21.  
- **Problem**: The key numerical relation Caγ∆ϕ/fa ≈ 10.3 is correctly derived once from βobs, αEM/(4π) and the β formula.[pp.11–12] Subsequent statements about required Caγ ranges (≈8.6–160 over ∆ϕ/fa ∈ [0.064, 1.19]) and the posterior‑preferred Caγ band (∼8–10 at saturated ∆ϕ/fa ≈ 1.2–1.3) are qualitatively right but not backed with explicit example arithmetic in the main text; readers must mentally do 10.3/(0.064) ≈ 160, 10.3/(1.19) ≈ 8.7, etc. The lack of even a single explicit pair of numeric checks in these ranges makes it easier for arithmetic slips to go unnoticed and reduces transparency, especially as you later build “outside KSVZ/DFSZ O(1)” and “needs ≳25× misalignment tuning” conclusions on these ranges.[pp.12–13, Table IV p.21]  
- **Required fix**:  
  - Add one short worked example in Sec. VI explicitly computing Caγ for the smallest and largest ∆ϕ/fa used (e.g. 10.3/1.19 ≈ 8.7, 10.3/0.064 ≈ 161), so that the 8.6–160 claim is transparently checked in text.  
  - Similarly, give a concrete example in the spectator‑safe corner: e.g. for θi = 0.1 and a typical ∆ϕ/fa from your EOM grid, show the resulting Caγ and compare to the posterior Caγ distribution in Table IV.  

**Severity**: MINOR (arithmetic is correct but under‑demonstrated; easy to fix by adding explicit calculation).  

---

P1B-E17 – Claims-classification Table V omits several load‑bearing quantitative statements (A, H, J)  

- **Section + page**: Appendix B, Table V p.19; main text multiple pages.  
- **Problem**: Table V purports to “classify every quantitative claim made in this companion,” but only lists a small subset: key headline numbers like H0 = 67.78 ± 1.09 (Planck+BAO+SN), S8 = 0.814 ± 0.008, the 0.31 and 0.40 ∆Neff one‑sided limits, 2.5σ, 3.6σ, 4.3σ, 3.2σ offsets, 0.032°/0.040° biases, 9σ LiteBIRD, the 25× misalignment tuning, and the Ωa posterior mass fractions (44%, 13%, 0.33%) are not listed.[pp.3–5, 7–8, 10–14, 20–21] The table therefore gives a false sense of completeness: many of the most consequential numerical claims are not indexed.  
- **Required fix**:  
  - Expand Table V to include all headline quantitative claims (especially all σ’s, percentages, count‑based fractions, and one‑sided limits) or explicitly relabel it as a *partial* index of selected claims.  
  - At minimum, include entries for: H0 values, both ∆Neff one‑sided limits, the σ values for H0, S8, w0/wa, the NaMaster bias (0.032°, 0.040°), LiteBIRD 9σ, the 25× tuning factor, and the Ωa posterior mass fractions used to define “spectator” status.  

**Severity**: MAJOR.  

---

P1B-E18 – MB–H0 constant‑offset arithmetic correct but “same tension” language under‑qualified (A, H)  

- **Section + page**: “MB–H0 joint-posterior offset check” p.5.  
- **Problem**: The MB–H0 paragraph correctly computes  
  - constSH0ES = −19.253 − 5 log10(0.7304) = −18.571,  
  - constchain = −19.263 − 5 log10(0.6768) = −18.415,  
  - offset = 0.156 mag,  
  and notes that this is ~3.2 times the chain’s σMB.[p.5] That arithmetic is sound. However, the text repeatedly frames this as “the same Hubble tension manifesting in the MB axis (3.2σ in chain-σ units, versus the canonical 3.6σ when the tension is expressed in distance-ladder terms in H0 axis; the two figures are derived from different estimators…).”[p.5] Even though you say they are “not directly comparable,” you still implicitly equate the MB offset with “the same tension” without quantifying how 3.2 vs 3.6 differ beyond that qualitative statement.  
- **Required fix**:  
  - Add a brief explicit comparison: e.g. “3.2σ (MB) vs 3.6σ (H0) differ by ~0.4σ, which is well within the uncertainty of this descriptive mapping; we therefore treat them as qualitatively the same tension but do not use 3.2σ as an independent tension statistic.”  
  - Consider replacing “the same Hubble tension” with “a manifestation of the SH0ES–Planck H0 tension along the MB axis” to avoid implying numerical identity.  

**Severity**: MINOR.  

---

P1B-E19 – “Stock CAMB ∆Neff bound consistent with minimal matter bounce” under‑quantified (H, G)  

- **Section + page**: Sec. III, “Physics interpretation (Table II)” p.4.  
- **Problem**: The text states that minimal matter‑bounce constructions “predict ∆Neff ≈ 0” and that the proxy run “confirming ∆Neff = −0.020 ± 0.169… is therefore consistent with the minimal matter-bounce prediction,” but gives no quantitative statement of how tight that consistency is relative to plausible nonzero ∆Neff values.[p.4] For example, a small but not negligible ∆Neff ≃ 0.2 would still be within ~1.2σ; the reader is left to infer this. While not strictly an arithmetic error, this is a place where σ and effect size could be tied together more concretely.  
- **Required fix**:  
  - Add a short numerical note: e.g. “the 95% one‑sided limit ∆Neff < 0.31 corresponds to Neff < 3.41, so any bounce scenario predicting |∆Neff| ≳ 0.3 at recombination would be disfavored at ≥95% C.L.; minimal matter‑bounce, which predicts ∆Neff ≈ 0, remains well inside the allowed range.”  

**Severity**: MINOR.  

---

If you want, I can now go through the paper line‑by‑line to assemble an explicit arithmetic‑check table (A‑class) for every σ, percentage, and ratio, but the additional issues above are the ones that stood out on a fresh, PRD‑style pass.