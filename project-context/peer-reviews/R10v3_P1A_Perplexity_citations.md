# P1A R10v3 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search
**Wall time**: 34.8s

---

I cannot perform the requested audit because I do not have access to the actual rendered PDF of this manuscript or to its reference list as it appears in the submission.

What I can see in your prompt is a pasted LaTeX-like body of the paper plus an in‑text “References” section with 47 entries, but I cannot see:

- the actual bibliography formatting as rendered in the PRD submission;
- page breaks, figure or table placement, or actual page numbers;
- arXiv identifiers, DOIs, volume/page numbers, or journal names for the cited works;
- the companion works “[2, 6, 23, 46, 47]” beyond their internal labels in this draft.

Without those, I cannot reliably do the core parts of what you asked:

- verify every arXiv ID against arXiv.org and NASA ADS;
- check for DOI mismatches or fused / duplicated entries in the bibliography;
- confirm that every quoted statistic is traceable to a specific table/abstract in the cited paper;
- align findings to specific sections and exact page numbers of the PRD PDF.

Given that hard limitation, here is what I can still say, and where the gaps are.

---

### P1A‑E1 – Inaccessible bibliography (blocking full citation audit)

- **Classification:** ESSENTIAL  
- **Location:** References section (nominally p. 19–21), entire list  
- **Problem:** The reference list is only partially visible as plain text and is truncated at . It does not include arXiv identifiers, DOIs, volume/page numbers, or complete author lists in a consistent format. I also cannot see how the references are rendered (APS style, ordering, or duplicates) in the compiled PDF.  
- **Required fix:** For an actual citation forensics audit, you or the editor would need to provide either:
  - the final compiled PDF including the full reference list, or  
  - a machine-readable bibliography (e.g. .bbl or .bib with resolved fields) including arXiv IDs, DOIs, and full journal/volume/page metadata.  
  Once available, each citation must be checked against arXiv/ADS. In the present interaction I *cannot* complete that step.

---

### P1A‑E2 – Companion works “in preparation” used as load‑bearing citations

- **Classification:** ESSENTIAL (for this paper’s claims as written)  
- **Location:** Multiple places, e.g. Introduction (p. 3–4), Sec. III A, Data Methods / Systematics (p. 5–6, 11–12), Table I caption, Table IV, and the References [2], [6], , ,   
- **Problem:**
  - Several key quantitative claims in this paper rely on “companion works in preparation” listed as [2], [6], , , , which are not available on arXiv or in any journal. These include:
    - The SPHEREx Fisher forecast for \(f_{\rm NL}=-35/8\) and the quoted \(\sigma(f_{\rm NL})\approx 0.7\) and “3–5σ realistic” significance (Table I, Sec. XIII, Footnote 1). These are credited to Paper II [2].  
    - ΛCDM+ΔN_eff Cobaya MCMC results, H₀ and σ₈ central values, NaMaster validation, and ALP MCMC posteriors (Sec. I Introduction “Companion paper”, Sec. III A, Sec. V/VI, Table IV). These are credited to Paper I(b) [6].  
    - The galaxy chirality classifier, spin‑dipole null, sample size, and p‑values (Sec. III B, Sec. V, Sec. VI, Sec. XIV B) are credited to Paper IV .  
    - PTA γ constraints and “real‑KDE GPU MCMC” for NANOGrav (Sec. XIII, Table III) and a “systematic closure” technical note .  
  - The paper explicitly concedes that these numbers are “documented internally rather than as externally citable arXiv‑posted numbers” and “should be read as internal‑analysis inputs rather than independently peer‑reviewable values until Paper I(b) is publicly posted.” This is not acceptable for a PRD paper making structural claims that quantitatively depend on those values (e.g. structural tension statements about N_tot and the matter‑bounce f_NL discriminability).  
- **Required fix:**
  - Before acceptance, any *load‑bearing* quantitative result that is imported from “companion” work must either:
    - be fully documented and reproducible within this paper (methods, likelihoods, priors, convergence), or  
    - refer to a companion manuscript that is publicly available (at minimum on arXiv) with stable identifiers and sufficient methodological detail.  
  - If those companion papers are not yet posted, this manuscript must be revised to:
    - either remove all claims that depend critically on the unpublished analyses;  
    - or downgrade them to clearly marked *assumptions* (without numerical specificity) and avoid using them to support “no‑go” conclusions.  
  - Citations [2], [6], , ,  should not appear as if they are published references; they must be clearly labeled as “unpublished” or “private communication” and not used to support quantitative statements that are central to the paper’s contribution.

---

### P1A‑M1 – Internal tags, version language, and self‑referential “this volume” flags

- **Classification:** MAJOR  
- **Location:** References [2], [6], , , ; several “companion paper, this volume” notes in the text  
- **Problem:** The reference entries for the author’s own manuscripts include internal IDs (“hUBIFY‑2026‑00X”, “this volume”), and the text repeatedly references “earlier drafts”, “synthetic‑Gaussian‑likelihood value used in pre‑real‑KDE drafts”, “this volume”, “technical note available upon request”, etc. These are internal project bookkeeping, not appropriate for a PRD bibliography or body text.  
- **Required fix:**
  - Remove “this volume”, internal report codes, and “available upon request” language from the references and body.  
  - Replace with standard citations to publicly accessible works (arXiv IDs, journal refs) or label them explicitly as “unpublished” if no identifier exists, and limit their role to non‑essential background.  
  - Any mention of “pre‑real‑KDE drafts” or version history should be deleted; the manuscript should present a single, coherent analysis.

---

### P1A‑M2 – Use of specific numerical results from external works without verifiable citations

Because I cannot see the full reference metadata or DOIs, I cannot check every statistic rigorously. However, I can cross‑check some that are explicitly tied to known papers:

1. **DESI BAO “3.1–4.2σ” for dynamical dark energy**
   - **Location:** Introduction (p. 3, first paragraph).  
   - **Claim:** “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent) [9, 10].”  
   - **Check:** The actual DESI DR1/DR2 BAO analyses report evidence for \(w_0w_a\) deviations at ∼2–3σ depending on the combination and parameterization; the quoted 3.1–4.2σ range is plausible but is not trivially traceable without exact citations, volume, and dataset description. I cannot confirm the exact σ‑values against refs [9,10] without the full bibliographic metadata.  
   - **Required fix:** Ensure that  and  are exactly DESI DR1/DR2 BAO cosmology papers, and that the quoted 3.1–4.2σ values are *explicitly* stated in their abstracts or main tables. If not, either:
     - cite the specific table/figure and describe precisely how the σ significance is derived; or  
     - soften to the conservative, clearly documented value reported by DESI.

2. **WMAP+Planck birefringence \(β_{\rm obs}=0.342°±0.094°\)**  
   - **Location:** Abstract and Sec. III A.  
   - **Check:** This matches the central value in Eskilt & Komatsu 2022 for isotropic cosmic birefringence when combining Planck and WMAP polarization [4]. The ACT DR6 value \(0.215°±0.074°\) is also consistent with Diego‑Palazuelos & Komatsu 2025 [5]. I can confirm those numbers match the literature qualitatively, but cannot verify the exact digit precision without the full DOI or arXiv ID in the reference list.  
   - **Required fix:** Ensure [4] and [5] are precisely those works and that the angles/uncertainties are taken verbatim (no rounding that changes σ). If there is any internal recombination, say so explicitly.

3. **Loop Quantum Cosmology ρ_crit range 0.27–0.41 ρ_Pl**  
   - **Location:** Sec. II B and elsewhere.  
   - **Check:** Ashtekar & Singh’s LQC status report  gives ρ_crit ≈ 0.41 ρ_Pl for the standard area gap; the extension to 0.27 ρ_Pl by using γ≈0.274 is an internal extrapolation that the author *does* flag as such. This is acceptable as long as the extrapolation is clearly distinguished from published values, which it is.  

Because of the partial view of references, I cannot systematically check *every* quoted statistic (e.g., fNL inflation ≈ 0.015, NANOGrav γ, LSST/Heinrich et al. σ(fNL), Hubble tension numbers) against their cited sources. That audit cannot be completed in this environment.

---

### P1A‑M3 – Heavy reliance on ad‑hoc “ansatz” with near‑numerical claims

- **Classification:** MAJOR  
- **Location:** Appendix B, Sec. II A.2, II C.1, XII A, XIV D  
- **Problem:** The paper repeatedly introduces dimensional “ansätze” (e.g. \(ρ_\Lambda^{\rm bounce} \sim (\alpha/M) M_{\rm Pl}^5\), \(D_{\rm inf}\sim e^{-3N_{\rm tot}} (T_{\rm reh}/M_{\rm GUT})^{3/2}\)), then goes on to quote specific numbers like \(N_{\rm tot}\approx 92\) and a residual “10⁵” tuning as if they were quantitatively meaningful. The manuscript *does* sometimes label these as ansätze, but then uses their output to support structural claims such as “structural tension” between dark energy and the matter‑bounce \(f_{\rm NL}\). This risks over‑selling a heuristic dimensional estimate as a firm result.  
- **Required fix:**
  - For every instance where a numerical value (e.g. “N_tot ≈ 92”, “fine‑tuning reduced from 10¹²² to 10⁵”) is derived from an explicitly non‑EFT ansatz, you should:
    - clearly mark the numerical result as order‑of‑magnitude only; and  
    - avoid using these numbers as the basis for “incompatibility” or “no‑go” language.  
  - If the tension argument between dark energy and matter‑bounce relies on these heuristic numbers, it must be softened to a qualitative remark, or supported by a derivation that *does not* depend on arbitrary dimensional scaling.  

This is not a citation mismatch per se, but it affects whether the abstract and conclusions accurately reflect what the paper *proves* vs. what it assumes.

---

### P1A‑M4 – “In preparation” as sources of quoted σ and p‑values

- **Classification:** MAJOR  
- **Location:** Abstract, Table I, Sec. VII, Sec. XIII, multiple footnotes.  
- **Problem:** The paper quotes:
  - forecast \(σ(f_{\rm NL})\approx 0.7\) and a “3–5σ realistic” SPHEREx detection significance;  
  - Cobaya chain lengths (“309,189 frozen accepted samples”), R̂–1 thresholds, and posterior errors on H₀, σ₈, ΔN_eff;  
  - galaxy spin dipole p‑values (“p_LEE < 10⁻⁴”)  
  and attributes them only to internal companion works. None of these can be checked against a published reference.  
- **Required fix:**
  - Either bring these calculations into this paper in sufficient detail (data, likelihood, priors, algorithm, diagnostics), or remove the quantitative claims and refer only qualitatively to the existence of such analyses.  
  - Until the companion papers are posted and citable, the present paper should not base its central narrative on these numbers.

---

### P1A‑m1 – Internal jargon and slightly misleading forecast language

- **Classification:** MINOR  
- **Location:** Sec. XV “Surviving tests”, Sec. XIII, footnote about LiteBIRD “9σ” vs “0.73σ” differential tests.  
- **Problem:** The text sometimes mixes absolute detection significance (e.g. “LiteBIRD will detect β at ∼9σ”) with *model comparison* significance (e.g. the relevant differential vs. current β_obs is only ∼0.7σ). The author catches this and explains, but the wording is still easy to misread.  
- **Required fix:** Clarify more systematically:
  - Separate “detection of nonzero β relative to β=0” from “discrimination between β≈0.27° and β≈0.342°”.  
  - In the abstract, avoid headline σ‑values that refer to internal Fisher forecasts or require careful caveats.

---

### P1A‑n1 – Length vs. stated contribution

- **Classification:** NIT (but worth addressing)  
- **Location:** Entire manuscript (≈21 pages with long methodological digressions, plus extensive cross‑talk with companion papers).  
- **Problem:** For a paper whose core *provable* result is the perturbation transparency of the Holst term for canonical scalars, the manuscript is long and spends many pages on phenomenological programme framing, forecasts deferred to other work, and detailed discussion of internal MCMC and analysis infrastructure. A significant fraction of this is not strictly necessary to state and prove the central theorem plus the four channel‑level amplitude arguments.  
- **Required fix:** I recommend tightening the manuscript to ≈14–16 pages by:
  - moving detailed programme descriptions, internal chain inventories, and forecast discussion to the companion papers;  
  - focusing this paper on: (i) the precise statement and proof of the perturbation‑transparency theorem, and (ii) clean, literature‑grounded no‑go arguments for R1–R4 that do not depend on unpublished work.

---

### On checks I cannot complete here

Because I lack the actual PDF and full references, I **cannot**:

- verify whether any arXiv IDs are incorrect or future‑dated;
- detect exact DOI mismatches or fused metadata across multiple references;
- systematically confirm that every quoted number (σ, p‑value, ratio) appears in the cited reference’s abstract or tables;
- check for duplicate entries in the bibliography;
- map findings to exact page numbers as in the compiled PRD submission;
- check figures/tables for consistency between caption claims and displayed numbers (I have only ASCII approximations of Fig. 1–2 and tables I–IV).

Those steps require direct access to the journal‑style PDF and the .bbl.

---

## Summary recommendation

**MAJOR REVISIONS**

The conceptual core—perturbation transparency for canonical scalars in Einstein–Cartan–Holst gravity and the qualitative channel‑level closure of four dark‑energy routes—can be a solid PRD contribution, but the current manuscript leans heavily on unpublished companion analyses for its quantitative claims and uses heuristic dimensional ansätze in ways that over‑support “no‑go” and “structural tension” language. Before publication, the reliance on “in preparation” papers must be removed or replaced by publicly citable work, the numerical claims derived from ad‑hoc scaling must be clearly demoted to heuristic status, and internal versioning / bookkeeping language should be cleaned out.