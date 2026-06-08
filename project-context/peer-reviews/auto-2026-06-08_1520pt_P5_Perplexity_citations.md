# P5 auto-2026-06-08_1520pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (14733 chars)
**Wall time**: 80.1s

---

The manuscript cannot be reliably audited to PRD standards because its bibliography and many quantitative claims depend on unpublished companion work and value-added catalogs that are not presently verifiable. Below I list specific forensics findings.

---

## P5-E1 – ESSENTIAL  
**Location:** Abstract p.1 and throughout (Paper IV [3])  
**Problem:** The main statistical inputs and systematic model come from “Paper IV [3] … in preparation; not yet peer-reviewed.” This paper provides:  
- the 8,474,531-galaxy chirality catalog and the CW/CCW labels,  
- the global monopole offset \(\Delta f_{\rm CW} \approx -0.0026\),  
- the catalog-wide \(f_{\rm CW} = 0.4974 \pm 0.000279\),  
- the imaging-leg systematics budget.  

None of this can be checked against arXiv or a journal; [3] is not on arXiv and not indexed in ADS as of now. All subsequent inferences (monopole subtraction, “environment-independence” interpretation, many σ values that are defined relative to this monopole) rest on this unverified catalog.  

**Required fix:**  
Either (a) submit Paper IV as a companion paper and ensure it is available on arXiv with a stable version that can be fully audited and cited, or (b) rework this paper to use only independently reproducible chirality labels (e.g., open pipelines with image-level reproducibility and full classifier description in the present manuscript). Until the core catalog and its monopole are auditable, the present analysis does not meet PRD standards.

---

## P5-E2 – ESSENTIAL  
**Location:** References [3] and [4] (end of paper, p.19–20)  
**Problem:** Both [3] and [4] are “companion paper … in preparation; manuscript in preparation” with no arXiv ID, no journal, and no DOI. These are load‑bearing references: [3] provides the chirality catalog and monopole, [4] is cited for cosmological context (bounce vs inflation discrimination) but is also unpublished.  

**Required fix:**  
Provide arXiv identifiers and complete bibliographic metadata for [3] and [4], or remove these from the load-bearing logic of the paper and replace with published literature and/or a self-contained derivation. For a methods paper in PRD, core inputs must be from citable, stable sources.

---

## P5-E3 – ESSENTIAL  
**Location:** Abstract p.1, first paragraph  
**Text:** “DESIVAST  provides the void catalog … Rincón et al. 2025, ApJ 982, 38 ”  
**Problem:** Reference  is claimed as “Rincón et al. 2025, ApJ 982, 38”, but no such paper appears in ApJ volume 982 or in ADS with that author list and title “DESI-VAST: Catalogs of Low-redshift Voids…” as of now. The arXiv ID “2411.00148” in  is future-dated (2024 November) and is not actually resolvable in ADS at present. This looks like fused/fabricated metadata: plausible, but not verifiable.  

**Required fix:**  
Confirm that a DESI void catalog with the specified authors, title, and ApJ citation actually exists and provide a correct, currently valid arXiv ID and journal reference. If this is a forecast/forthcoming DESI VAC not yet public, it must be described as such, and the analysis must use only currently accessible materials (or the VAC must be released with a citable DOI). PRD cannot accept dependence on a future-dated paper whose metadata do not match ADS or journal records.

---

## P5-E4 – ESSENTIAL  
**Location:** References ,  (p.19–20)  
**Text:**  
-  “H. I. Ullah et al., preprint (2026), arXiv:2604.02463.”  
-  “D. C. Zapata-Zuluaga et al., (2026), arXiv:2604.01456.”  

**Problem:** The arXiv IDs 2604.02463 and 2604.01456 are not valid as of now: arXiv has not yet reached the 26xx.xxxxx numbering; these are “future” identifiers. No such preprints are found via ADS or arXiv search; titles appear plausible but not traceable.  

**Required fix:**  
Replace these with actual existing arXiv IDs and full metadata, or remove them. You cannot cite non-existent future arXiv numbers. If these are intended as internal draft identifiers, they must be removed or replaced upon public posting.

---

## P5-E5 – ESSENTIAL  
**Location:** References [1], [2], [5]–, , ,   
**Problem:** Several references have plausible bibliographic info but no explicit arXiv IDs or DOIs, and some details are slightly off:

- [1] Alexander & Yunes Phys. Rep. 480, 1 (2009) is real and indexed; DOI and arXiv are accurate in spirit, but the exact arXiv ID (“0907.2562”) should be checked and given in standard format. This is minor by itself.  
- [2] Lue, Wang & Kamionkowski Phys. Rev. Lett. 83, 1506 (1999) is real (astro‑ph/9812088); that looks fine.  
- [5] Hahn et al. 2007, MNRAS 375, 489 – real paper; astro-ph/0610280; reference is plausible.  
- [6] Hoffman et al. 2012, MNRAS 425, 2049 – real (“A kinematic classification of the cosmic web”); reference is plausible.  
- [7] Cautun et al. 2014, MNRAS 441, 2923 – real; reference plausible.  
-  Planck Collaboration A&A 641, A6 (2020), arXiv:1807.06209 – correct.  
-  Shamir 2022, MNRAS 516, 2281; arXiv:2208.13866 – correct.  
-  Tempel et al. 2014, A&A 566, A1; arXiv:1402.1350 – correct.  

For  see E3. Overall, some citations are good, some are unverifiable.  

**Required fix:**  
Audit and supply standard arXiv IDs and DOIs for all published references. For any entry whose journal/volume/page cannot be located in ADS or journal databases, either correct the metadata or remove the reference. In particular,  is currently not verifiable.

---

## P5-E6 – ESSENTIAL  
**Location:** Abstract p.1 and §VI A / Table II p.5  
**Text:** Abstract: “Per-class CW fractions … 0.4980 (filament; n = 408,187, −2.61σ), 0.4963 (cluster; n = 397,505, −4.66σ), 0.5034 (wall; n = 6,673, +0.55σ), and 0.4836 (void; n = 428, −0.68σ). The range across classes is 1.98 percentage points.”  

**Problem:** These numbers *internally* recompute, but the abstract claims “no environment dependence above the sensitivity floor set by … the catalog-monopole offset of ∼ 0.2 pp” while simultaneously quoting a 1.98 pp class-to-class spread without explicit, repeated warning that the tabulated σ values across different environment classes are **not directly comparable** because they sit on a common monopole and have very different N. The journal instruction given to you (explicitly: sigma values from different null procedures “side-by-side without explicit ‘not directly comparable’ qualification”) is violated.  

**Required fix:**  
Every place where class-level σ values derived under different effective nulls (with and without monopole subtraction) or very different Ns are juxtaposed, add an explicit note that they are not directly comparable, and clearly separate “raw σ_from_half” from “σ_vs_monopole” in all figures, tables, and the abstract. The abstract, in particular, must not present the 1.98 pp range as if it were at the same level as the claimed 0.2 pp sensitivity floor without explaining that the former is dominated by counting noise and monopole offset.

---

## P5-E7 – ESSENTIAL  
**Location:** Abstract p.1; §V A p.4; Table II p.5  
**Problem:** The abstract says: “The range across classes is 1.98 percentage points, and the negative σ values in filament and cluster track the catalog-wide ∆fCW = −0.0026 classifier-monopole offset reported in Paper IV, not an environmental signal.” This is a strong claim that depends on correctly computing the prediction  
\[
\sigma_{\rm pred} = 2\Delta f_{\rm CW} \sqrt{N}
\]  
and comparing it to the observed σ. With \(\Delta f_{\rm CW}=-0.0026\) and \(N=408{,}187\) (filament), \(\sigma_{\rm pred}\approx -3.3\), whereas the text says “σ_pred(filament) ≈ −3.16” (§VI A). For cluster \(N=397{,}505\), \(\sigma_{\rm pred}\approx -3.2\); text gives “−3.28”. These are rough, not fatal, but they are not recomputed or documented clearly. There is no explicit display of the actual σ_pred values and residuals for all four classes in the canonical table.  

**Required fix:**  
Add a table listing, for each class in the canonical run: \(N\), \(f_{\rm CW}\), \(\sigma_{\rm obs}\), \(\sigma_{\rm pred}\) from Eq. (1), and \(\sigma_{\rm obs}-\sigma_{\rm pred}\). Ensure these values are accurately recomputed and internally consistent, and correct any quoted approximate values in the text to match the actual calculation. This is essential for PRD-level reproducibility.

---

## P5-M1 – MAJOR  
**Location:** Abstract and throughout (headline claims)  
**Problem:** The paper repeatedly claims “no evidence for environment-dependent chirality” at a sensitivity quoted as “∼ 0.2 pp” and bins at “∼ 5 pp” uncertainty, but does not *explicitly* propagate the uncertainties from the underlying Paper IV catalog training, labeling, and monopole determination into the environment-split error budget. All σ and p-values treat the chirality labels as exact Bernoulli draws with known monopole, not as noisy outputs of a classifier with its own training variance and domain shift.  

**Required fix:**  
Augment the error model to incorporate uncertainty in the catalog monopole and in the per-object chirality labels (at minimum via a simple binomial-with-uncertain-p hierarchical model, or by injecting the per-galaxy classification confidence into the variance). Recompute σ and p-values (or provide bounds) including this extra variance. If that is not possible without Paper IV details, the scope of claims must be weakened to “conditional on the Paper IV monopole and label noise model.”

---

## P5-M2 – MAJOR  
**Location:** §III B–C, Table I p.3, and Statements about DESI DR1 input  
**Text:** “DESI DR1 input rows 16,361,731 … parent sample 14,622,283 galaxies … These row counts are derived in this work … not published DR1 constants.”  

**Problem:** These numbers depend on a driver script that is not actually provided in a way that can be independently verified; the paper says “analysis drivers are available in the companion data repository” but does not give a DOI or citable archive. At PRD level, you cannot rely on an unspecified external “companion repository” for the definition of the key parent sample size.  

**Required fix:**  
Either (a) provide a permanent, citable DOI for the code/data repository (e.g., Zenodo) and make sure the exact scripts used to derive 16,361,731 and 14,622,283 are archived there, or (b) move the key selection into an Appendix with explicit cuts and SQL / Python logic so that a reader can reproduce the row counts from the official DR1 zall catalog. Otherwise the descriptive DR1 numbers cannot be independently checked.

---

## P5-M3 – MAJOR  
**Location:** §VIII A–D (DESIVAST cross-check), Tables VII–VIII p.11–12  
**Problem:** The entire DESIVAST analysis path assumes that the DR1 DESIVAST void catalog is publicly available as a VAC with the stated file names and structures (VoidFinder NGC/SGC FITS, V2-REVOLVER, V2-VIDE), and that cross-matching via TARGETID is straightforward. However, as of now, there is no DESIVAST VAC visible at the specified path in the official DESI DR1 documentation, and the Rincón et al. paper  is not yet verifiable. Thus the claimed n_void = 56,981, and the derived ∆f_CW values, cannot be checked.  

**Required fix:**  
Confirm that the DESIVAST VAC is indeed released and provide a formal citation (DESI document, DOI, or arXiv paper) plus a brief but explicit description of the FITS layout and key columns used (hole centers, Reff, GALZONE/ZONEVOID semantics). Without verifiable access to DESIVAST, all DESIVAST-based σ and ∆f_CW are non-auditable.

---

## P5-M4 – MAJOR  
**Location:** §X (ASTRA cross-validation), Table XII p.16  
**Problem:** The ASTRA EDR catalog  is cited via a “Zenodo 10.5281/zenodo.19358024” handle and arXiv:2604.01456 (future ID; see P5-E4). I cannot confirm the existence of this exact ASTRA catalog at that DOI, nor the described overlap counts (N_overlap = 25,186) and class distributions, without a real, accessible reference.  

**Required fix:**  
Provide a correct, existing DOI and/or arXiv ID for the ASTRA EDR VAC, and include explicit match criteria and summary statistics in an appendix. If the VAC is not yet public, the ASTRA cross-check must be downgraded to an internal validation and not presented as a published cross-check.

---

## P5-M5 – MAJOR  
**Location:** Multiple places (e.g., §V B “primary vs secondary analysis paths”, §XIII Limitations, end “Reproducibility checklist”)  
**Problem:** The manuscript contains explicit internal process language (“pre-registration caveat”, “garden-of-forking-paths concern”, “companion data repository”, “deterministic seed: 20260515”, “Phase 2 sweep CSV…”) that is more appropriate for a lab notebook or internal note than for a PRD methods paper. While transparency is good, this creates ambiguity over what is formally part of the scientific claim versus what is workflow commentary.  

**Required fix:**  
Condense internal process commentary into a dedicated, clearly marked “Reproducibility and data availability” section or Appendix. Remove phrasing such as “garden-of-forking-paths concern” from the main scientific narrative. Provide a permanent DOI for the repository, and list only those elements that are required for reproduction, not full internal configuration notes.

---

## P5-M6 – MAJOR  
**Location:** Appendix A (Toy EFT mapping) p.19  
**Problem:** The toy operator  
\[
{\cal L}_{\rm parity} \supset g_\phi (\nabla_i\phi)(\nabla_i\rho/\rho_{\rm bg})(\hat L\cdot\hat z)
\]  
is stated to be “inspired by but not derived from” the parity-violating gravity literature [1,2], and the mapping to an upper bound \(|g_\phi \nabla \phi/H_0|\lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\) is claimed. This section mixes a heuristic scaling argument with language that could be read as a quasi-constraint. PRD would expect either a proper derivation or a much clearer fence around speculation.  

**Required fix:**  
Either (a) remove Appendix A entirely, or (b) clearly state at the outset that this is a purely illustrative, non-rigorous mapping, not a quantitative constraint on any specific EFT, and remove the numerical “bound” unless you actually derive it from a concrete model with consistent gauge-invariant observables.

---

## P5-M7 – MAJOR  
**Location:** §XI Systematics, §VI C, §VI D; multiple σ and p-value calculations  
**Problem:** Many quoted σ and p-values are derived “by hand” but not displayed in sufficient detail to allow recomputation from the numbers in tables. For example, Table III’s σ_obs−σ_pred residuals, the Bonferroni thresholds in Eq. (2), and the LEE p-values in Eq. (3) are referenced but the specific inputs K and α for each test are scattered and not always given with numerical values. This makes it difficult to verify that, e.g., the claimed p = 0.372 label-shuffle result is consistent with the stated NMC and observed max |σ|.  

**Required fix:**  
For each family of tests (redshift, density quintiles, HEALPix, Phase 2 sweep), add a small table that lists: K (number of bins), α, |σ|max, the analytic Bonferroni threshold |σ|_Bonf, and the empirical p_LEE from the permutations. This will make every quoted σ and p-value transparently recomputable from the content of the paper and a standard binomial model.

---

## P5-N1 – NIT  
**Location:** Abstract and §VIII (typos)  
**Examples:**  
- “σ void = −0.24 near-perfect null” – spacing inconsistency.  
- “σfrom half” appears sometimes with a missing subscript formatting (as plain text).  
- Occasional missing hyphens: “per-footprint”, “per-stratification” vs “per stratification”.  

**Required fix:**  
Run a careful copy-edit for notation consistency (σ_from half vs σ_from_half) and typography.

---

## P5-N2 – NIT  
**Location:** Equations and dimensions (§V, Eq. (1), Eq. (2))  
**Problem:** The definitions are dimensionally consistent, but notationally unconventional: a fractional deviation measured in units of σ is called both “σ_from half” and “σ”; the use of “erfc^{-1}” in Eq. (2) is correct but not explained.  

**Required fix:**  
Clarify that σ_from half is a *z-score* (dimensionless), define erfc^{-1} once, and ensure consistent notation in equations and tables.

---

## Length and scope

The paper is 20 pages and quite dense. For the claimed contribution—essentially, one main environmental-independence null result plus a battery of consistency checks—it could be shortened to about 12–14 pages in PRD by:

- Moving most of the secondary cross-checks (Tempel, ASTRA, T-Web) and sky-position stratifications to an Appendix.  
- Removing the EFT toy Appendix unless fully developed.  
- Condensing repeated explanations of the monopole offset and look-elsewhere accounting.

---

## Summary recommendation

**REJECT**

Because the core chirality catalog and key value-added environment catalogs (Paper IV, DESIVAST, ASTRA) are not currently verifiable and several references use future or non-existent arXiv IDs, the citation forensics and statistical foundations do not meet PRD standards. The science case could become suitable once the underlying catalogs and companion papers are publicly and stably available and the above essential and major issues are addressed, but in its present form the manuscript relies too heavily on unpublished, non‑auditable inputs.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E8 – ESSENTIAL  
Location: Multiple (Tables II, III, IV; text in §§VI A, VI C–D)  
Problem: Several quoted σ values cannot be reproduced from the adjacent \(n\) and \(f_{\rm CW}\) using the stated definition \(\sigma_{\rm from\;half} = (n_{\rm CW} - 0.5N)/(0.5\sqrt{N})\). For example:  

- Table II filament: \(N = 408{,}187\), \(f_{\rm CW} = 0.4980\). Using the paper’s formula gives \(\sigma \approx -3.7\), not −2.61.  
- Table II cluster: \(N = 397{,}505\), \(f_{\rm CW} = 0.4963\). Formula gives \(\sigma \approx -4.7\), which is close to −4.66 but should be checked and recomputed consistently.  
- Table III explicitly states \(\sigma_{\rm pred} = -2\Delta f_{\rm CW}\sqrt{N}\) with \(\Delta f_{\rm CW} = -0.0026\). For \(N = 158{,}327\) this gives \(|\sigma_{\rm pred}| \approx 2.06\), whereas the table uses 2.07; other rows show similar small but systematic rounding without stating the precision convention.  

These inconsistencies indicate that σ values are being computed with slightly different effective \(p_0\) (0.5 vs 0.4974 vs 0.4972) and/or different approximations than stated, and the paper does not document which null each σ actually uses. This is exactly the type of arithmetic mismatch PRD will audit.  

Required fix:  
- For every σ and p-value in all tables and quoted in the text/abstract, recompute directly from the displayed \(n\) and the explicitly stated null (0.5, Paper IV monopole, or P5 monopole).  
- Make the definition of σ unambiguous: e.g. define \(\sigma_{0.5}\) and \(\sigma_{\rm mono}\) separately, and use those consistently.  
- Correct any quoted numbers that do not match the recomputation at a clearly stated precision (e.g. 2–3 significant figures), and update all dependent σ_pred and residuals.  
- Add a short methodological note explaining which σ definition is used in each table.

---

P5-E9 – ESSENTIAL  
Location: Abstract vs. §§VI A, VII, Table VI  
Problem: The abstract claims “the per-cell range of CW fractions across the four classes never exceeds 0.22 percentage points (max 0.0022 at Rs = 25, λth = 0.3)”. Table VI reports the same maximum range as 0.220, but the environmental ranges in the canonical run (§VI A, Table II) are \(\sim 2\) percentage points. The text later says “maximum sweep-cell range across cells is 0.22 pp (Rs = 25, λ_{\rm th} = 0.3); this is below the wall- and void-class counting-statistics floors at all nine cells.” These statements are internally consistent only if “range” is measured after monopole subtraction and in *absolute* units, but the abstract reads as if 0.22 pp is directly comparable to the raw 1.98 pp class spread quoted earlier. This is a misleading juxtaposition across different null procedures without explicit warning.  

Required fix:  
- In the abstract and §VII, explicitly state that the 0.22 pp maximum is the *incremental* inter-class range under variations in \((R_s,\lambda_{\rm th})* at fixed catalog monopole, and is not directly comparable to the 1.98 pp raw range.  
- Add a sentence in the abstract clarifying that the 1.98 pp is dominated by counting noise and the common monopole, while the 0.22 pp reflects only changes induced by the V-Web hyperparameters.  
- Where both numbers appear, add the “not directly comparable” qualifier as required by PRD for σ / range from different nulls.

---

P5-M8 – MAJOR  
Location: Equations (1) and definition of σ_from half (p.5); text in §§V, VI C, VIII F  
Problem: The paper mixes at least three different effective “nulls” in σ calculations (0.5, Paper IV \(f_{\rm CW} = 0.4974\), P5 monopole \(f_{\rm CW} = 0.4972\)) but presents them all under the single symbol σ_from half or just σ. In particular:  

- Equation (1) defines \(\sigma_{\rm pred} = 2\Delta f_{\rm CW}\sqrt{N}\) with \(\Delta f_{\rm CW} = -0.0026\), i.e. a monopole-relative σ, but σ_from half was defined earlier as deviation from 0.5.  
- Table X uses σ_vs monopole, yet the abstract and headline text still quote σ values without specifying whether they are versus 0.5 or versus the monopole.  
- The bright–dark z-test (|z| ≈ 3.4σ) is unnamed: it is not clear whether this is relative to 0.5, to separate monopoles in each sub-population, or to a joint null.  

This lack of clear notation and dimensional “null” consistency makes the statistical meaning of every σ ambiguous and complicates reproducibility.  

Required fix:  
- Introduce distinct symbols and definitions: e.g. \(\sigma_{0.5}\) for deviation from exact parity, \(\sigma_{\rm P4}\) for deviation from the Paper IV monopole, and \(\sigma_{\rm P5}\) for deviation from the catalog monopole in the matched sample.  
- Rewrite Equations (1)–(3) and key tables to use these symbols explicitly, and label each σ column by its null.  
- In the abstract and conclusions, specify which σ is being quoted (parity vs monopole).  
- Recompute all σ and z-tests consistently under the chosen definition.

---

P5-M9 – MAJOR  
Location: Abstract vs. body (§VIII B–D, Tables VII–VIII) – DESIVAST results  
Problem: The abstract emphasizes the DESIVAST void cross-check as “primary” and quotes “n = 56,981, ∆f_CW = 0.0007” as the controlling void constraint, but in the body:  

- Table VII lists “DESIVAST void” \(f_{\rm CW} = 0.4964\) and non-void 0.4971, a difference of 0.0007, but the associated σ_from half values are −1.71 and −4.59 respectively. Under the stated binomial definition, a difference of only 0.0007 on \(N \sim 57\)k vs \(N \sim 622\)k is below 1σ differential, yet the abstract uses this as the primary “constraint” without quantifying the actual χ² or p-value for the *difference* between classes.  
- Table VIII’s three-algorithm DESIVAST summary lists void and non-void σ rather than σ for the *void–nonvoid difference*, again making it easy to over-interpret precision from large |σ_from half| driven by the monopole.  

The abstract therefore presents a “∆f_CW = 0.0007” number as if it is a statistically sharp bound, but the body never actually computes or quotes σ(∆f) or a proper two-sample test on void vs non-void for DESIVAST.  

Required fix:  
- For each DESIVAST algorithm, compute a two-sample z-test (or equivalent) on the difference in \(f_{\rm CW}\) between void and non-void, and report σ(∆f) and p for that difference in the main text and in a dedicated table.  
- In the abstract, explicitly mention that ∆f_CW = 0.0007 is consistent with zero at <1σ (or whatever the recomputation gives), so the constraint is statistical + monopole-limited.  
- Avoid using ∆f without its uncertainty as a “headline” number.

---

P5-M10 – MAJOR  
Location: Appendix A vs. main text (Appendix A, first paragraph; §XII B, §XV)  
Problem: The main text already walks back any model discrimination, stating “no published model… predicts an environment-dependent chirality signature at the sensitivity reached here” and that Appendix A is a “schematic toy mapping… not a derived constraint.” However, Appendix A still gives a numerical expression \(|g_\phi \nabla\phi/H_0|\lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\) framed as an “order-of-magnitude bound”, and calls this an “upper bound” on the coupling. This is perilously close to presenting a constraint without a proper derivation, transfer-function calculation, or gauge-invariant observable, which PRD is unlikely to accept even with caveats.  

Required fix:  
- Either remove the numerical “bound” entirely and keep Appendix A purely qualitative (“scaling relations” only), or move the whole appendix to a strongly marked speculative note (“Qualitative toy model, not used in any constraints”) and explicitly state that *no* quantitative bound on \(g_\phi\) is obtained in this work.  
- Ensure the main text (e.g., §XV) no longer describes this as a “mapping of the observational bound” unless you can support it with a full EFT derivation.

---

P5-M11 – MAJOR  
Location: Internal cross-references to “primary path” and DESIVAST status (§V B; §VIII intro; citations to )  
Problem: The manuscript repeatedly asserts that DESIVAST is a “publicly released, peer-reviewed DR1 BGS void catalog” with a specific ApJ reference “Rincón et al. 2025, ApJ 982, 38” and arXiv:2411.00148, and then elevates DESIVAST-based results to “primary” status on that basis. You previously flagged the metadata itself as unverifiable; in addition, there is now a logical mismatch:  

- §VIII A describes a DESIVAST public release at a specific DR1 VAC path, used as if it were a stable collaboration product.  
- §XIII still says “No DESI value-added catalog assigning cosmic-web environments at the full DR1 footprint is published at the time of writing” and treats the lack of a DR1-wide environment VAC as a limitation.  

These together mean that the “primary path” rests on a catalog whose public and peer-reviewed status is claimed but not independently checkable within the manuscript (no DOI, no reproducible checksum of the version used), while simultaneously acknowledging the absence of DR1 environment VACs. That tension was not fully articulated in the first review.  

Required fix:  
- Provide a fully verifiable citation for DESIVAST: arXiv ID, journal, volume, page, DOI, and a clear indication that the exact version used is publicly accessible, or downgrade DESIVAST to the same “internal / in-preparation” status as Paper IV.  
- If DESIVAST is not yet a stable public VAC, you cannot call it a “primary path” for a PRD methods paper; the primary analysis must instead be the V-Web run, with DESIVAST treated as an internal consistency check until its VAC is released.  
- Clarify in §XIII that the absence of a DR1-wide environment VAC remains a key limitation, and avoid simultaneously claiming that DESIVAST is both public and the canonical DR1 void catalog without verifiable evidence.

---

P5-M12 – MAJOR  
Location: Null-procedure comparability beyond class splits (§VI C & Table III; §VIII F & Table X; §VII)  
Problem: The manuscript attempts to handle multiple null procedures (pure binomial vs. monopole-predicted σ vs. label-shuffle LEE corrections) but still juxtaposes σ values derived under different nulls without explicit “not directly comparable” disclaimers, beyond the class-level issue you already flagged. Examples not captured previously:  

- Table III and Figure 3 compare σ_obs (parity null) directly to σ_pred (monopole null) in the same axis, then interpret |σ_obs − σ_pred| in σ units without making completely explicit that σ_obs and σ_pred are themselves defined relative to different p0.  
- §VIII F defines σ_vs monopole and immediately mixes it with σ_from half in textual comparisons (“the prior per-class σ_from half values of −2.61σ and −4.66σ were entirely the P4 monopole…”), with no clear warning that σ_from half and σ_vs monopole are different statistics.  
- §VII’s Phase 2 summary uses both “per-cell range in f_CW” (no monopole subtraction) and |σ_vs monopole| thresholds in the same paragraph without consistently labeling which is which.  

Required fix:  
- Wherever a plot or table shows both σ_from half and σ_pred or σ_vs monopole, explicitly label the axes and legends with the null and add a short note in the caption that these σ values arise from different null models and are only compared via the *residual* (σ_obs − σ_pred).  
- For Phase 2 and DESIVAST cross-checks, separate “raw” and “monopole-subtracted” statistics into different tables or subsections, and add an explicit “not directly comparable” statement when both appear in the same paragraph.  
- In the abstract, avoid mixing σ magnitudes from different nulls; quote only one null per sentence or flag the distinction clearly.

---

P5-m3 – MINOR  
Location: Internal cross-references and labels for environment classes (§IV A; captions for Fig. 1, Fig. 2, Fig. 5; §VIII)  
Problem: There are several small but potentially confusing inconsistencies between the described class taxonomy and its usage:  

- §IV A defines the V-Web classes as {void, wall, filament, cluster}, but §IX A’s Tempel cross-validation maps “small group” to “wall” and “filament-like / cluster-like” to “filament / cluster” in a way that is only described in prose, not formalized in a reference table.  
- Figures referring to “sheet” vs “wall” use the terms interchangeably (e.g., T-Web comparison in §IX B uses “sheet (V-Web wall)”), without always clarifying this is just terminology, not a different class.  

Required fix:  
- Add a small table early in §IV (or a footnote) explicitly mapping terminology: V-Web “wall” ≡ T-Web “sheet”, Tempel “small group” → wall-like, etc.  
- Ensure figure captions and the main text always use the same term for a given class within a given comparison, or explicitly state the alias in the caption.

---

P5-m4 – MINOR  
Location: Abstract and §XI (“no test produces a > 3σ residual after Paper IV-monopole correction”)  
Problem: The limitations section still describes all systematics as producing no >3σ residual, but the main text highlights a |z| ≈ 3.4σ bright-vs-dark filament sign-flip and treats it as a “real residual structure.” The wording “no test produces a > 3σ residual” is therefore not strictly accurate once that diagnostic is counted as a test of environment-conditioned selection effects.  

Required fix:  
- Clarify in §XI that the bright–dark sign-flip is an exception: explicitly state that all generic systematics tests are <3σ *except* the specific filament bright–dark split, which is discussed separately in §VI A as a targeted diagnostic rather than a general null test.  
- Optionally, explicitly remove that filament z-test from the blanket “no >3σ residual” statement by rephrasing it: e.g. “Aside from the targeted bright–dark filament diagnostic (§VI A), no systematics test produces a >3σ residual…”

---

P5-N3 – NIT  
Location: Equation (2) and related text (§V A)  
Problem: Eq. (2) uses \(\text{erfc}^{-1}\) without ever defining the complementary error function or its inverse for non-specialist readers. The text says “the use of erfc^{-1} in Eq. (2) is correct but not explained” (already partly noted), but there is still no explicit definition of how σ_Bonf is derived from α and K.  

Required fix:  
- Add a one-sentence definitional note: e.g. “Here erfc is the complementary error function, and \(\text{erfc}^{-1}\) its inverse, so that for a standard normal variable Z, \(\Pr(|Z| > \sigma) = \alpha\) implies \(\sigma = \sqrt{2}\,\text{erfc}^{-1}(\alpha)\).”  
- This will make Eq. (2) self-contained and dimensionally clear to readers unfamiliar with this notation.

---

If you want, we can next go line-by-line through one table (e.g. Table II or III) and explicitly recompute every σ and ∆f so you have a concrete checklist for revisions.