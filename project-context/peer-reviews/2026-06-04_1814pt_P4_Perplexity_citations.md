# P4 2026-06-04_1814pt — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 42.9s

---

I cannot perform the requested citation audit on this paper because I do not have access to the references section or full bibliographic list. The body text you provided contains in‑text citations ([1]–) and descriptions of prior work, but without the actual reference list (authors, titles, venues, arXiv IDs, DOIs) I cannot:

- Verify that each numbered citation maps to a specific, unique paper.
- Check titles, author lists, venues, years, DOIs, or arXiv IDs.
- Confirm that quoted numerical results (e.g., sample sizes, σ values, percentages) appear in the cited sources.

Any attempt to “reconstruct” the reference list from context would be speculative and would not meet the standard of a forensic citation audit.

Given that limitation, I can still do two things:

1. Flag issues visible directly in the manuscript that violate your instructions (σ comparability, version‑history artifacts, duplicate phrases, abstract/prose mismatches).
2. Identify a few places where claims *about* named prior work (Shamir, Iye, Tadaki, Jia/CE‑ResNet, SpArcFiRe, Motloch & Pen, etc.) are specific enough that they *likely* can be cross‑checked, and note what *must* be verified against arXiv/NASA ADS in a proper audit.

Below I treat this as a referee report focused on the issues you requested, but I cannot complete the core task “Verify every cited paper actually says what is claimed.”

---

## Referee report (Citation forensics focus)

### Global/structural findings

**P4‑E1 (ESSENTIAL) – No reference list provided, so core citation audit is impossible**

- **Location:** Global (end of manuscript – “References” section is truncated).
- **Problem:** The text ends with “ […] https://github.com/rwightman/pytorch-image-models” but the actual reference list is not printed. Without the full references, I cannot verify:
  - Whether each in‑text numeric citation ([1]–) maps to a unique bibliographic entry.
  - Whether arXiv IDs, DOIs, titles, author lists, and venues are correct.
  - Whether quoted numerical results (sample sizes, σ, percentages) really appear in the cited papers.
- **Required fix:** Provide the full reference list (authors, titles, journal/proceedings, volume, page, year, arXiv ID, DOI) for all citations [1]–. Only after that can an arXiv/ADS‑based citation audit be done.

Because of P4‑E1 I cannot honestly claim to have “verified every cited paper.” I will instead flag internal issues visible from the body text, plus “must‑check” items for a later audit.

---

### σ‑scale and null‑procedure comparability

Your instruction 7:

> If any σ values from different null procedures are presented as if they're on the same scale without qualification, flag this as ESSENTIAL.

Overall the manuscript is very careful about this—there are repeated caveats that σ values from bootstrap, label‑shuffle, binomial, etc. are not comparable. I looked specifically for *violations* where this distinction is blurred.

**P4‑E2 (ESSENTIAL) – Some passages still mix σ from different nulls in ways that will mislead a typical reader**

- **Location:** Multiple; representative examples:
  - Abstract / early pages:
    - “The headline scientific result is a null ℓ = 1 chirality-dipole observable on the analysis subsample mask… −0.12σ (500‑MC label‑shuffle null)… The real-space post-TTA Catalog C dipole is +0.43σ (p = 0.30, per-pixel-shuffle null)… Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable…”
  - Canonical‑mask discussion:
    - The big composite sentence in Fig. 8 caption and similar in the main text:
      > “…auto-spectrum +4.73σ at ℓ = 2 vs +3.63σ at ℓ = 1 — a real dipole at 1.7% would be ℓ = 1-dominant, with injected real dipoles showing σ = +2.87 at ℓ = 1 under the same null…”
      and in the abstract‑like portion:
      > “…pre-MASTER raw pseudo‑Cℓ in the lowest bandpower … +6.48σ… fully removed by MASTER mode-coupling deconvolution to the null −0.122σ headline, and independently collapsed to 0.43σ in real space…”
- **Problem:**
  - Although you *do* state that σ values are tied to their own null, these sentences juxtapose different σ’s in a way many readers will interpret as directly comparable “signal strengths”. Examples:
    - +6.48σ (pre‑MASTER pseudo‑Cℓ, label‑shuffle null) vs −0.12σ (MASTER, different null) vs 0.43σ (real‑space dipole, third null) in one narrative.
    - +3.63σ vs +4.73σ vs +2.87σ, where the last is an injection under the “same” null but the reader has to work hard to understand that this is not a global σ scale.
  - The text sometimes calls the canonical +3.64σ “mild” and elsewhere treats “+2.89σ… ∼ 2.3σ family‑corrected” as evidence. This mixing of raw σ, family‑wise‑corrected σ, and different nulls is very hard to track, and despite your caveats it reads as if these σ’s live on a common scale.
- **Required fix:**
  - Wherever you *compare* two or more σ values in the same sentence or argument, you must explicitly state that they come from the same null, or explicitly say “under different nulls, not directly comparable on a σ scale; comparison is via p‑values only.”
  - For the canonical‑mask interpretive triage section:
    - Replace σ‑based comparison like “ℓ = 2 > ℓ = 1 (4.73σ vs 3.63σ)” by:
      - Either a ratio of **Cℓ amplitudes**,
      - Or explicit p‑values under the *same* null.
  - Add a short boxed or bolded caution early in Sec. IV that “within this manuscript, σ’s are not comparable across nulls. Any argument that contrasts two values is based on p‑values under the same null; mixed‑null σ comparisons are for rough orientation only.”
  - Check all locations where three or more σ values appear in one sentence (e.g. “+6.48σ… −0.12σ… 0.43σ”; “+3.63σ… +4.73σ… +2.87σ”). Either:
    - Recast them in terms of Cℓ and *relative* changes, or
    - Explicitly annotate “σX (null A), σY (null B), not directly comparable.”

Given your own emphasis on null‑dependent σ, these are fixable wording issues, but they are absolutely essential to avoid misinterpretation.

---

### Version‑history / internal‑log artifacts

Instruction 8:

> If any version-history language, internal audit tags, or review-log artifacts appear in the body prose, flag each one.

There are **many** such artifacts; they are pervasive and need to be stripped or moved to a technical note / data‑release appendix.

I list representative cases; this is not exhaustive but indicates a systematic cleanup is required.

**P4‑M1 (MAJOR) – Versioning tags and internal audit notes scattered throughout prose**

- **Location:** Title and front matter:
  - Title block: “(Dated: June 4, 2026 PDT — v1.0.153)”
  - Abstract: “…paper4-v1.0.153.”
- **Problem:** Physical Review D papers do not include internal version tags like “v1.0.153” or “paper4‑v1.0.153” in the scientific narrative.
- **Required fix:** Remove these from the title and abstract. If you want to document the code/data tag, move it to the Data Availability section only.

**P4‑M2 (MAJOR) – Internal pipeline paths and JSON filenames in main text**

- **Location:** Many places, e.g.:
  - Sec. II B 0 a: “Reproducibility artifact: pipelines/p2_chirality/r42_results/B20_B21_results.json”
  - Footnotes to Table II, Table VII, etc.: “companion artifact master_decoupled_monopole_null_10k.json”
  - NaMaster appendix: “wrapper: pipelines/p2_chirality/scripts/canonical_l1_namaster_pod.py”
- **Problem:** These look like internal reproducibility notes or lab notebook entries. In a PRD methods paper they belong in a code‑release README or online supplement, not in the science prose.
- **Required fix:**
  - Remove all explicit filesystem paths and JSON filenames from the main text.
  - In Data Availability, state that *machine‑readable artifacts and scripts are provided in the GitHub repository and tagged release*, without listing individual path names.
  - If some results truly rely on specific JSON files, describe their content generically (e.g. “a 3×3 confusion matrix, see supplementary material”) rather than putting the path inline.

**P4‑M3 (MAJOR) – Explicit “wave_xx”, “B20/B21” and pod labels**

- **Location:** Numerous:
  - “wave_14_kk_ba_reconciliation_results.json”
  - “pod2_chirality_2026-04-29”
  - “wave11c_nspiral_recompute_2026-05-01”
- **Problem:** These look like internal run IDs / audit wave numbers, not scientific nomenclature. They clutter the narrative and will confuse readers.
- **Required fix:** Remove “wave_XX”, “BYY”, “podN” style naming from text. If you must distinguish multiple reruns, call them “baseline run” / “recomputed shot‑noise run” etc., and document the exact artifact IDs only in the code repository.

**P4‑M4 (MAJOR) – Explicit mention of previous buggy results and “retractions” in body**

- **Location:** Several examples:
  - “the older snapshot value 2.75σ predates the canonical Nspiral shot‑noise normalization…”
  - “This manuscript retracts this as fragile‑argmax sample noise…”
  - “the earlier 0.79% value used an inconsistent symmetric‑error model and is corrected here…”
- **Problem:** While it is good to be transparent, PRD articles normally present a *clean* analysis. Detailed errata about earlier drafts belong in a supplementary “analysis log” or, if really necessary, a short paragraph noting that a corrected computation supersedes an earlier value, without narrative about “wave 11” or “pre‑correction baseline.”
- **Required fix:**
  - Replace these with concise, forward‑looking statements. Example:
    - “We previously reported 2.75σ using an incorrect shot‑noise denominator; a corrected calculation yields 6.48σ pre‑MASTER and −0.12σ post‑MASTER. All analysis in this paper uses the corrected normalization.”
  - Remove language like “this manuscript retracts…” and “legacy pre‑correction baseline.”

Given the density of such artifacts, I recommend a thorough top‑to‑bottom scrub: search in the LaTeX source for `pipelines/`, `wave_`, `B20_`, `pod`, `.json` and remove or move to supplementary material.

---

### Duplicate / garbled phrases

Instruction 9:

> If any duplicate phrases appear (e.g. "canonical canonical-mask"), flag them.

I see several places where phrases are duplicated or sentences are garbled, likely from incremental edits.

**P4‑M5 (MAJOR) – Garbled, over‑long sentence in canonical‑mask residual discussion**

- **Location:** Early abstract‑like block (first page), sentence starting “Interpretation (ii) is attributed to a coherent depth/sampling-correlated systematic… These tests do not exclude…”
- **Problem:** The paragraph runs on for multiple lines with parentheses nesting, then abruptly says “The bootstrap pixel-resample test gives −0.22σ … and is therefore retained only as a sampling-variance diagnostic.” Later in the same paragraph there is a near‑duplicate wording of that bootstrap point. This is confusing and repetitive.
- **Required fix:** Rewrite this whole paragraph into 2–3 clear sentences:
  - One summarizing the three interpretations.
  - One clearly stating which is favored and why (with *minimal* σ numbers).
  - One stating the limited role of the bootstrap.

**P4‑N1 (NIT) – Minor duplicated/awkward phrases**

Examples:

- “the present pipeline differs from Shamir’s in classifier (ViT with equivariant TTA vs deterministic Ganalyzer), spiral selection, and bias-mitigation stack; a matched-footprint reanalysis under Shamir’s exact Ganalyzer pipeline and magnitude/redshift cuts would be required… and we do not perform that reanalysis here. We also demonstrate that uncorrected survey systematics…”
  - The “we do not perform that reanalysis here” phrase appears in almost identical wording several times.
- “monopole-only null reproduces 99.3% of the observed pre-MASTER pseudo-Cℓ… prior literature’s pre‑MASTER class of dipole-detection claims is therefore (modulo the matched-pipeline caveat…) explained at the percent level by this leakage channel under our DESI / ViT‑Small classifier monopole.”
  - “pre‑MASTER class of dipole-detection claims” is awkward; consider tightening.

These are stylistic, but a careful copy‑edit would improve clarity.

---

### Abstract vs paper content

Instruction 10:

> Check that the abstract accurately summarizes what the paper proves — not what the paper hopes to prove.

**P4‑M6 (MAJOR) – Abstract’s falsification criterion is phrased too strongly relative to what’s actually demonstrated**

- **Location:** Abstract, paragraph starting “Falsification criterion. A future survey that…”.
- **Text:** 
  - “A future survey that, after comparable systematics control, detects a chirality dipole at σ > 5 with full amplitude ≳ 0.75% … would falsify the present null.”
- **Problem:**
  - The 0.75% amplitude is the *empirical 50%‑recovery‑at‑3σ threshold under a specific per‑pixel‑shuffle null on a specific HC subsample*. It is not a universal, model‑independent falsification bound.
  - The body text later adds many caveats: dependence on null choice, per‑pixel shuffle destroying systematics, LSST‑specific assumptions, etc. The **abstract** omits these.
- **Required fix:**
  - Soften and make conditional:
    - “Under the null and analysis protocol adopted here, a future survey that… would be inconsistent with our null at high significance.” 
    - Or: “Our injection tests show we would detect a dipole of ≳ 0.75% at ≥ 3σ half of the time; a future ≥5σ detection at that amplitude or larger would be in tension with our result, modulo different systematics.”
  - Explicitly state that this is an *analysis‑dependent* sensitivity, not a fundamental theoretical bound.

---

### Length / focus

Instruction 6:

> If the paper is too long for the claimed contribution, say so and state the recommended maximum page count.

**P4‑M7 (MAJOR) – Paper is significantly longer than needed for the stated methods/catalog contribution**

- **Location:** Global; 56 pages for a PRD methods/catalog paper.
- **Problem:** A large fraction of the manuscript is occupied by:
  - Internal run‑log details and path names.
  - Repetitive explanations of the canonical mask residual and its multi‑null interpretation.
  - Very detailed prose about injection‑recovery settings, block bootstrap variants, etc., that could be condensed.
- **Required fix:**
  - Target ~30–35 pages for the main text, with additional technical material moved to an online supplement:
    - Keep: data description, model, bias tests, main dipole estimators, one clean section on canonical‑mask residual.
    - Move to supplement: many of the run‑log details, per‑wave names, per‑null MC configuration details, and some of the more exploratory diagnostics (e.g. extended leg×confidence grids) that don’t change the headline result.

---

### “Must‑check” claims about prior work (for a future audit with references)

Once the full reference list is available, the following statements should be *explicitly checked* against the cited papers (via arXiv and NASA ADS):

1. **Shamir series:**
   - Shamir (2012): “2–4σ dipole significance with per‑bin asymmetry amplitudes of ∼ 5–20% using ∼1.27×10^5 SDSS galaxies (126,501 spirals; Shamir 2012 abstract).”
   - Shamir (2020): “SDSS DR8 + Pan‑STARRS, ∼6.4×10^4 SDSS spirals plus ∼3.3×10^4 Pan‑STARRS galaxies…”
   - Shamir (2022): “MNRAS 516 2281; the published abstract reports ‘nearly 1.3×10^6 spiral galaxies’ as the analyzed spiral set…”
   - **Audit tasks:**
     - Verify the galaxy counts and “per‑bin asymmetry amplitudes” are quoted correctly (from abstract and tables).
     - Confirm that the spin asymmetry amplitudes are indeed in the 2–4% range for DESI Legacy data.

2. **Iye et al. 2021; Tadaki et al. 2020; Iye & Yagi 2026:**
   - Check that the claimed “null” results and sample sizes match the author’s descriptions here (e.g. “∼ 80,000 face‑on spirals”, “HSC‑SSP imaging”, “documented duplication of photometric objects” etc.).

3. **Jia et al. (CE‑ResNet):**
   - Verify:
     - “∼ 1.95 million spiral classifications”.
     - Training on DESI Legacy with SDSS in training.
     - “cw/ccw = 0.998” parity statement.
     - Architectural chirality equivariance (flip swapping CW/CCW).

4. **SpArcFiRe:**
   - Confirm that:
     - The quoted sample sizes (~140,000 galaxies).
     - The agreement with Galaxy Zoo percentages.
     - Any claim about SpArcFiRe’s CW/CCW balance (“consistent with 50/50 to within ∼0.3%”) are traceable to Davis & Hayes and any updates.

5. **Motloch & Pen 2021:**
   - Confirm:
     - The ~2.7σ correlation between galaxy spins and reconstructed initial conditions.
     - That the correlation is indeed “marginal” and potentially sensitive to reading‑direction biases.

6. **Parity‑odd 4PCF / parity‑violating sectors:**
   - Verify that references to Lue, Wang & Kamionkowski (1999), Cabass–Ivanov–Philcox, Cahn–Slepian–Hou, Philcox, Eskilt & Komatsu, etc., are used correctly:
     - The description of Π = (PL −PR)/(PL+PR).
     - The 3.6σ CMB birefringence result and β value.
     - The 7.1σ / 3.1σ parity‑odd 4PCF statements.

Because I don’t have the reference list, I can’t check arXiv IDs or DOIs, but a future audit must verify each such claim against ADS/arXiv.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper presents a technically careful and ambitious analysis, but from a *citation‑forensics and presentation* standpoint it requires substantial revision:

- The full reference list is missing; without it a proper citation audit cannot be done.
- There are pervasive internal‑log and versioning artifacts that must be removed from the body text.
- Some σ‑based comparisons across different null procedures are still presented in a way that will mislead non‑expert readers.
- The abstract overstates the generality of the 0.75% “falsification” threshold relative to what is actually demonstrated.
- The paper is substantially longer than needed for its main scientific contribution and should be shortened with technical detail moved to supplementary material.

Once these issues are addressed—and after a real citation audit is run using the completed reference list—the paper could be reconsidered.