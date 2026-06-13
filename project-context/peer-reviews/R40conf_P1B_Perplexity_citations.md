# P1B R40conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/paper1b_mcmc_companion.pdf` md5=62374add pages=21
**Input format**: TEXT + web search + pass-2 self-critique (9840 chars)
**Wall time**: 76.4s

---

I cannot perform the requested audit to PRD standards because I do not have access to the actual rendered PDF, its reference list in bib format, or the numerical chain artifacts; I only see the text you pasted. That prevents me from:

- Verifying arXiv IDs, DOIs, author lists, and venue metadata directly against arXiv and NASA ADS for each reference.
- Recomputing posteriors, σ’s, p‑values, or reproducing figures from the underlying chains and artifacts.
- Checking that figure axes, units, and table entries match the plots and numbers actually displayed in the PDF.
- Confirming that every quoted statistic from prior work appears in the cited paper’s abstract/tables.

Given that constraint, I will treat what you pasted as the (textual) content of the paper and do a *text‑level* referee and citation forensics pass on that, but you should understand that anything depending on the actual PDF layout, the reference list formatting, or the external code/data artifacts is necessarily incomplete.

Below I list findings keyed to the text as given, using the page/section indications embedded in your paste (when present). Where I would normally say “ESSENTIAL” because PRD requires it, I still mark it as such, but you or the editors should treat these as “provisional” until a full PDF/ADS/arXiv cross‑check is run.

---

### P1B‑E1 – ESSENTIAL  
**Location:** Abstract (page 1) and throughout Sec. III, Table I, Conclusions.  

**Issue:** Load‑bearing numerical claims (ΔNeff, H₀ values, 3.6σ Hubble tension, 2.7–2.9σ birefringence, 3.6σ Eskilt & Komatsu) are not re‑derived in the paper and cannot be checked from numbers shown in the text alone. You describe how the chains were run, but you do not show the basic one‑line calculations readers can verify directly (e.g., how 3.6σ is derived or the precise two‑sided vs one‑sided conversions for ΔNeff). At PRD level, every headline σ and “tension” needs to be transparently reconstructible from either displayed table entries or fully specified combinations.  

**Required fix:**  

- For each load‑bearing σ / “tension” / “significance” in the abstract and main text (especially: ΔNeff constraints, 3.6σ Hubble tension, 2.7–2.9σ Planck/ACT, 3.6σ Eskilt–Komatsu, “3.9σ upper bound”), add a short parenthetical explicit computation directly from displayed numbers (e.g., “3.6σ = (73.04 − 67.68)/√(1.06²+1.04²)”).  
- In Table I, explicitly show the one‑sided ΔNeff upper limits, not just describe them in the caption; specify clearly that the two‑sided quoted ±σ are not physical extra‑species bounds, and that the one‑sided limits are posterior truncations at ΔNeff ≥ 0.  
- In Sec. IV, when quoting 2.7–2.9σ for Planck/ACT and 3.6σ for Eskilt–Komatsu, show the simple β/σ computation from the cited values in the text and make it clear which uncertainties are statistical vs total.  

---

### P1B‑E2 – ESSENTIAL  
**Location:** Abstract and Sec. II–III (H₀ tension), Table I, Table II.  

**Issue:** σ significances from different procedures are juxtaposed without consistently marking them as not directly comparable. You do this correctly in a few places (e.g. noting MB‑axis vs H₀‑axis tensions are not directly comparable), but elsewhere the text aligns:  

- “residual ∼ 3.6σ tension with the SH0ES … H₀ = 73.04 ± 1.04”  
- S₈ tension levels (2.5σ, 2.6σ, 2.0σ, etc.)  

without always clarifying that these come from different estimators (posterior tail, simple Gaussian combination, posterior‑overlap measures), and that they are not directly comparable one to another. The journal’s standard requires that when two σ‑numbers live side‑by‑side and come from different null/test statistics, their non‑comparability be spelled out at each juxtaposition.  

**Required fix:**  

- Every time you quote multiple σ’s in the same sentence or paragraph that arise from different null/estimator conventions (e.g. 3.6σ H₀ tension vs 3.2σ MB offset; 2.6σ vs 2.0σ S₈ “tensions”), add an explicit qualifier like: “These σ values are not directly comparable: the former is a survey‑vs‑survey Gaussian difference on H₀, the latter is a within‑chain marginal σMB,” etc.  
- In the abstract, when you mention the 3.6σ H₀ tension and the 3.6σ birefringence result, state clearly that they are unrelated statistics with different definitions.  

---

### P1B‑E3 – ESSENTIAL  
**Location:** Introduction (page 2), first paragraph; “What is NOT in this paper” paragraph.  

Text:  
> “The SPHEREx multi‑tracer Fisher forecast (in preparation, [6]) is the subject of Paper II. The multi‑survey anomaly catalog (in preparation, [7]) is the subject of Paper III. The galaxy chirality catalog (in preparation, ) is the subject of Paper IV.”  

**Issue:** References [6]– are explicitly “in preparation,” yet are cited as numbered references in a PRD‑style bibliography and used as load‑bearing context for the program. This is not acceptable for PRD unless they are either (a) publicly available on arXiv with stable identifiers, or (b) explicitly marked as unpublished and used *only* for non‑essential context. As written, they appear as if they will be “posted concurrently,” but there are no arXiv identifiers in the references list; that is citation‑forensics‑wise a red flag.  

**Required fix:**  

- Either supply actual arXiv identifiers for [1], [6], [7],  (if they are indeed posted) with correct titles, and ensure the references list contains accurate arXiv IDs and metadata; or  
- Remove [6]– as numbered references and rewrite the text to describe these as “forthcoming, not used anywhere in this paper’s analysis,” without presenting them as citable literature. They must certainly not be used to support any quantitative or methodological claim.  
- Update the reference list to conform; if they remain, add “(to appear)” or similar and make clear they are not peer‑reviewed.  

---

### P1B‑E4 – ESSENTIAL  
**Location:** Throughout the text, especially Sections II–III (MCMC setup), V.A (“Datasets and configuration”), Appendix A (“Reproducibility Materials”), Appendix C (ALP MCMC).  

**Issue:** Very heavy reliance on repository paths and internal filenames (“reproducibility/p1_namaster_500mc/...”, “research/branch_R_alp_birefringence/...”, “spin_torsion.input.yaml”, etc.) that do *not* carry stable DOIs or versioned archives. PRD reproducibility standards require that key data/code artifacts used to support numerical results be frozen with stable identifiers (DOI, Zenodo, or similar) or at least tagged Git commits. Here you mention a git commit SHA and a few HuggingFace dataset names, but you also refer to a number of internal files with no persistence guarantee (e.g. “c10b_alp_envelope_scan.json”, “c9f_negative_beta.json”). For a methods paper whose entire content is “technical verification,” that is a reproducibility gap.  

**Required fix:**  

- For every artifact that is used to support a quoted scalar in the text (e.g. ∆ϕ/fa ranges, β̂ values, σβ from MC, Ωa posterior fractions), ensure that the underlying artifact is part of a frozen release with a version tag and DOI (or equivalent), and that this release is cited in the Data & Code Availability section.  
- Replace bare internal paths in the main text with references to those frozen releases (e.g. “see Dataset X, file Y”), and keep the detailed path‑level documentation in an online README instead of in the PRD paper body.  
- Clarify explicitly that the version‑stamp “v1B.0.69” corresponds to a frozen tagged release on a public repository, and give enough information that a reader can clone that exact version even if the main branch changes.  

---

### P1B‑E5 – ESSENTIAL  
**Location:** Sec. IV, equations and estimator description; NaMaster simulation section.  

**Issue:** Dimensional consistency and estimator definition are only partially explicit. You define:  

\[
\chi^2(\beta) = \sum_b\left(C_b^{EB,\text{dec}} - \tfrac12 \sin(4\beta) C_{b,EE}^{\text{tmpl}}\right)^2
\]

and state that *no* σ² term is used (unweighted fit). Later, “pipeline‑recovery SNR” is defined as  

\[
\mathrm{SNR}_\text{tmpl}^2 \equiv \sum_b (C_b^{EB,\text{th}}/\sigma_b^\text{MC})^2
\]

but this σ_b^MC is only briefly described in a footnote. Nowhere in the main text do you give a dimension‑consistent mapping from Cℓ to β that a reader could reproduce without reading your code. For a methods paper, PRD will expect a precise, self‑contained estimator definition.  

**Required fix:**  

- Move the full estimator definition (including the definition of σ_b^MC and the exact β grid and interpolation strategy) into the main text or an explicit “Methods” subsection, not just in a footnote.  
- State clearly the units of Cℓ and how the normalization (e.g. sin(4β)/2 factor) is chosen; ensure that the mapping from β to CℓEB is dimensionally consistent and traceable to the physical EB expectation CℓEB = ½ sin(4β)(CℓEE − CℓBB).  
- Where you refer to “no σ² divisor,” explicitly note that this is a deliberate choice to match previous NaMaster scripts, and quantify the effect (as you partly do in the robustness section) in a way that allows a reader to recompute the bias analytically or semi‑analytically.  

---

### P1B‑E6 – ESSENTIAL  
**Location:** Sec. VI (“Cosmic birefringence: spectator ALP consistency check”), especially the Ωa definition and the “spectator‑status caveat,” and Table IV.  

**Issue:** The “spectator‑safe” Ωa thresholds (0.1, 0.01) and the claim of “∼25× misalignment tuning” are load‑bearing for the conclusion that the ALP is fine‑tuned, but they are not derived numerically in the text in a way the reader can check. You provide the general scaling Ωa ∼ m² f_a² θ_i² / (H₀² M_Pl²) and sketch the (1+z_osc)⁻³ factor, but you never show an explicit numeric worked example with actual numbers (m/H₀, θ_i, f_a = M_Pl) giving Ωa ≈ 1 for θ_i ~ 1 and Ωa ~ 0.01 for θ_i ~ 0.1. For a methods/consistency paper, that needs to be transparent.  

**Required fix:**  

- Add a short explicit computation for Ωa in the text, e.g. “At m = H₀, f_a = M_Pl, θ_i = 1, and z_osc ≈ 0, Ωa ≈ 1; at θ_i = 0.1 the same parameters give Ωa ≈ 0.01. Thus the spectator condition requires θ_i ≲ 0.1, i.e. ∼25× tuning relative to the prior midpoint θ_i = 0.5.”  
- Explicitly connect these numerical examples to the prior choices in Appendix C and to the mass range in Table IV.  
- Make it clear that the Ωa fractions 44% and 13% are computed with H₀ *fixed* at 67.68 km/s/Mpc, and comment on how much these fractions would change if H₀ were allowed to vary within its 1σ posterior.  

---

### P1B‑M1 – MAJOR  
**Location:** Abstract, opening sentences; Sec. I (“Scope of this paper”) and VII (Conclusions).  

**Issue:** Abstract‑last drift. The abstract claims three main contributions (ΛCDM+ΔNeff proxy, NaMaster validation, ALP consistency check) but is written with a mix of *program‑level* language (“ECH spin‑torsion program,” “no‑go program of Paper I(a)”) and *companion‑paper* language. Some important caveats that are spelled out in the body (e.g. the SN‑overlap systematic for w₀wₐ, the fact that ALP birefringence is not distinctive to ECH, the Planck PR4/2018 pairing caveat) do not appear in the abstract, which makes the abstract a bit stronger than the properly caveated body statements.  

**Required fix:**  

- Add at least one sentence to the abstract explicitly noting:  
  - that the ΛCDM+ΔNeff run does *not* directly test the spin‑torsion model;  
  - that the NaMaster results are pipeline‑validation only and *not* competitive sky detections;  
  - that the ALP birefringence is a generic GR+ALP effect and requires fine‑tuned θ_i and enhanced C_{aγ}.  
- Ensure the ordering of claims in the abstract matches the ordering and emphasis in the conclusion section (currently the abstract leads with the ΔNeff proxy, which is fine, but does not mention the SN overlap caveat at all).  

---

### P1B‑M2 – MAJOR  
**Location:** Sec. III (“Stock‑CAMB ΛCDM+ΔNeff MCMC”) and Sec. V.A (“Datasets and configuration”), Table III.  

**Issue:** Mixed Planck release pairing is only flagged qualitatively. You use Planck PR4/NPIPE CamSpec high‑ℓ and Planck 2018 low‑ℓ and lensing, acknowledge that this is the “standard Cobaya pairing” and that you have not done a “release‑pairing swap test.” For a paper whose central technical result is a ΔNeff posterior at ~0.17 precision and H₀ at ~1 km/s/Mpc precision, that mixed pairing deserves at least a quantitative robustness check: e.g. a Planck‑2018‑only chain to see if ΔNeff and H₀ shift by more than ~0.3σ.  

**Required fix:**  

- Either run and report a Planck‑2018‑only ΛCDM+ΔNeff chain and give the differences in ΔNeff, H₀, S₈ relative to your mixed PR4/2018 pairing (show they are small compared to quoted errors), or  
- Explicitly weaken all statements that depend on ΔNeff and H₀ (e.g. “∆Neff = …” and “does not resolve the Hubble tension”) to say that they are conditional on the standard PR4/2018 pairing and will need to be revisited when a consistent PR4 low‑ℓ/lensing likelihood is available.  

PRD is unlikely to accept high‑precision parameter statements without at least this basic pairing sanity check.  

---

### P1B‑M3 – MAJOR  
**Location:** Sec. II & III; discussion of “minimal matter‑bounce class” predicting ΔNeff ≈ 0 and the interpretation of the ΔNeff result as a “bounce‑class compatibility check.”  

**Issue:** The connection between ΔNeff and “minimal matter‑bounce” is asserted qualitatively, but the minimal class is only defined loosely (“no light bounce‑internal species are thermalized at recombination”) with a single citation . There is no quantitative statement of the predicted ΔNeff distribution under that model, and no explicit comparison to your posteriors, beyond “consistent with ≈0.” As written, the reader cannot tell whether the ΔNeff posterior meaningfully constrains that class. The phrase “compatibility check” is vague for PRD standards.  

**Required fix:**  

- Tighten the definition of the “minimal matter‑bounce class” and state explicitly what ΔNeff it predicts at recombination (e.g. ΔNeff ≈ 0 with theoretical uncertainty ≲ 0.01, or similar), citing the underlying calculation.  
- Then compute the expected p‑value or posterior support for ΔNeff = 0 under your two chains and state whether the data provide any non‑trivial bound; otherwise, say explicitly that the constraint is too weak to be informative.  
- Replace “compatibility check” with a more quantitative statement (e.g. “current ΔNeff posteriors are fully consistent with the minimal matter‑bounce expectation and place no meaningful upper bound on additional bounce‑generated radiation beyond σ(ΔNeff) ≈ 0.17”).  

---

### P1B‑M4 – MAJOR  
**Location:** Sec. V.C (“w₀wₐ cross‑check”), Table II, footnote (a) and associated discussion.  

**Issue:** Use of “+4.3σ” and “−3.6σ” deviations for w₀ and wₐ when the ΛCDM point is unsampled. You do correctly note that these are “marginal‑tail posterior‑extrapolation distances” and not Bayes factors, but the σ language will be misread. PRD typically expects either proper likelihood ratio or evidence calculations if you quote large “σ” disfavours, or very careful contextualization.  

**Required fix:**  

- Move the warning that “ΛCDM is unsampled; these σ are extrapolations, not proper tensions” into the main paragraph, not only in a table footnote.  
- Consider reporting these as “Δw₀/σ(w₀) = +4.3” etc. explicitly as *posterior mean displacements*, not as “σ” in the frequentist sense, and avoid language like “4.3σ exclusion.”  
- Restate in the abstract and conclusions that no Bayes factor is computed and no model‑selection claim vs ΛCDM is being made. Right now that is said, but buried.  

---

### P1B‑M5 – MAJOR  
**Location:** References section, all numbered references.  

**Issue (citation forensics, partial):** From the text:

- [3] is Diego‑Palazuelos et al. (Planck NPIPE birefringence). You quote “Phys. Rev. Lett. 128, 091302 (2022), arXiv:2201.07682” and β = 0.30° ± 0.11°. This matches the known paper, but I cannot confirm the exact β value from ADS without external access; assuming it is correct.  
- [4] is listed as “arXiv:2509.13654 [astro‑ph.CO]” (ACT DR6 birefringence). The year “2025” and the arXiv ID “2509.13654” are *future‑dated* relative to the article’s nominal date (June 13, 2026) and may not exist yet. I cannot hit arXiv from here, but any ID starting with “25” implies September 2025, which is plausible, but PRD will require that (a) the preprint actually exists, (b) the title and authors match what you claim, and (c) you are quoting β = 0.215° ± 0.074° correctly from it.  
- , , ,  etc. have 2025 dates and arXiv identifiers you quote in the text but not always in the reference list.  

**Required fix:**  

- For each reference with a 2024/2025 date or arXiv ID (especially [3], [4], , , , , , ), verify against arXiv/ADS: titles, authors, year, journal, and the numerical values you quote. Correct any mismatches.  
- Explicitly check that [4]’s arXiv ID and quoted β value are accurate and that the paper is indeed in the status you claim (preprint or published). If not yet available, mark it as “in preparation” and do not use it as a numerical constraint.  
- Ensure that the reference list includes arXiv IDs for all preprints cited in the text.  

This is work that must be done by the authors or a referee with external access; I cannot complete it from the pasted text alone.  

---

### P1B‑M6 – MAJOR  
**Location:** Data & Code Availability; Appendix A.  

**Issue:** Mention of a column‑permutation bug in `parameter_summary.json` and use of `parameter_summary_CORRECTED.json`. While you are commendably transparent, the main text does not specify *which* numbers in the paper depended on the corrected file vs the buggy one. PRD readers must be able to trust that the reported chains in Table I and II are unaffected.  

**Required fix:**  

- In Appendix A or the main text, include a concise statement explicitly listing which tables and quoted values were recomputed from the corrected file, and confirming that the earlier bug did not affect any published scalar numbers (or, if it did, give corrected values).  
- Ideally include a short table showing the maximum fractional change of any parameter’s posterior mean/σ induced by the correction.  

---

### P1B‑M7 – MAJOR  
**Location:** Appendix B (“Claims classification”), Table V.  

**Issue:** Table V advertises “machine‑checkable index” but the paper itself does not include a machine‑readable representation. In PRD this is not mandatory, but if you claim this as part of the reproducibility infrastructure, it should either be backed by a real machine‑readable artifact (e.g. a JSON in the repository with a DOI) or described without implying that PRD readers can execute it.  

**Required fix:**  

- Either (a) point explicitly to a JSON or similar artifact in the public repository that encodes Table V (with a stable tag/DOI), or  
- (b) downgrade the language in Appendix B so that it is clearly descriptive, not claiming machine‑checkability as part of the journal article itself.  

---

### P1B‑m1 – MINOR  
**Location:** Body text; repeated phrases.  

Examples:  

- “canonical canonical mask” does not appear in the pasted text, but double adjectives like “canonical estimator choice” appear; I did not see literal duplicate tokens like “canonical canonical‑mask,” so this check passes. However, keep an eye on phrases like “Planck NPIPE (PR4) CamSpec high‑ℓ TTTEEE + Planck 2018 low‑ℓ TT/EE + Planck 2018 lensing” which are repeated verbatim many times, making the text harder to read.  

**Required fix:**  

- No strict change is required for PRD, but consider abbreviating recurring likelihood stacks with a concise symbol and defining it once.  

---

### P1B‑m2 – MINOR  
**Location:** Sec. IV, Fig. 3 caption and associated text.  

**Issue:** You mention “Panel (b): the βinj = 0.27° sky‑fraction sweep… per‑realization σβ was not recorded… a dedicated 500‑MC rerun measures σβ = 0.046° at this point.” In the caption, the f_sky = 0.32 point is plotted without error bars. For a methods paper in PRD, reviewers will expect either an error bar there or a footnote in the caption making clear that its uncertainty has been measured in a separate run and giving the value.  

**Required fix:**  

- Add to the caption: “At f_sky = 0.32, σβ = 0.046° from a dedicated rerun; error bars not shown for visual clarity.” Or simply show the error bars using that σβ.  

---

### P1B‑m3 – MINOR  
**Location:** Sec. VI, ALP section.  

**Issue:** You discuss convention choices for the coupling (α_EM/(4π) vs α_EM/(2π)) only briefly. While it is mostly pedagogical, for PRD it would be cleaner to state explicitly your Lagrangian convention once and give the mapping to the widely used g_{aγγ} notation.  

**Required fix:**  

- Add a one‑line equation: “We define L ⊃ −(g_{aγγ}/4) φ F_{\muν} \tilde F^{\muν} with g_{aγγ} = C_{aγ} α_EM/(2π f_a); our birefringence formula β = (g_{aγγ}/2) Δφ corresponds to this normalization.”  

---

### P1B‑n1 – NIT  
**Location:** Acknowledgments.  

**Issue:** “The author acknowledges the use of Claude (Anthropic) as an AI research assistant…” PRD has no policy forbidding this, but it is unusual and could be shortened.  

**Required fix:**  

- Optionally abbreviate to: “The author used AI‑assisted tools during analysis; all scientific claims and results were independently verified by the author.”  

---

### P1B‑n2 – NIT  
**Location:** Data & Code Availability.  

**Issue:** You include full GitHub URL paths in the body. PRD’s style typically prefers dropping explicit “https://” in the main text and possibly moving full URLs to a footnote or ancillary material.  

**Required fix:**  

- Adjust to journal style as per PRD’s instructions (often: “All code is available at a public Git repository; see ancillary material for the URL”).  

---

## Length and scope

At 21 pages packed with methodological detail, this is borderline long for what is essentially a “technical verification companion.” Given PRD’s standards and that the primary physics results are in Paper I(a), I would recommend you aim to keep this companion at ≲18 pages in print by:

- Moving most of Appendix A (pipeline internals and file paths) and Appendix B (claims classification table) to an online supplement.  
- Compressing the very long footnotes about chain sample counts and burn‑in into a short paragraph plus a reference to the repository.  
- Consolidating repeated descriptions of the Planck+BAO+SN+H₀+S₈ stack and Planck NPIPE likelihood.  

This would not change the substance but would make the paper more readable.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The paper tackles exactly the sort of technical verification and reproducibility work that PRD should encourage for non‑standard cosmological models, but at present it falls short of PRD standards on several fronts: reliance on “in preparation” companions without stable identifiers, incomplete quantitative derivations for key “σ” claims and ALP spectator tuning, lack of a concrete Planck release‑pairing robustness test, and incomplete citation forensics for several future‑dated references. The reproducibility story is strong in spirit but needs to be tied to actual frozen releases rather than raw internal paths. Once those issues are addressed and the abstract is brought into full alignment with the carefully caveated body text, the manuscript could be suitable as a technical companion to the main ECH paper.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B‑N1 – NEW  
**Location:** Sec. II (H₀ / S₈ tension paragraph), comparison to Liu et al.  

**Issue (Arithmetic / notation):** The σ‑difference formulas for the Liu et al. cross‑check are written with a “+” inside the square root instead of the correct “+” between squared errors. As typeset:  
> “…H₀ = 68.41 ± 0.32 km/s/Mpc and S₈ = 0.812 ± 0.006 agree with our Planck+BAO+SN chain at 0.5σ in H₀ (|67.78 − 68.41|/ 1.092 + 0.322 ) and 1.3σ in S₈ (|0.827 − 0.812|/ 0.0102 + 0.0062 )…”  

The intended Gaussian combination is clearly  
\(|ΔH₀| / \sqrt{1.09^2 + 0.32^2}\) and \(|ΔS₈| / \sqrt{0.010^2 + 0.006^2}\), which do give ≈0.5σ and ≈1.3σ, but as printed the denominators look like “1.09² + 0.32²” (exponent applied only to the first term) rather than “(1.09² + 0.32²)^{1/2}”. This is both arithmetic‑notation ambiguous and formally wrong if taken literally.  

**Required fix:**  
- Rewrite these two expressions explicitly as  
  \(|67.78 − 68.41| / \sqrt{1.09^2 + 0.32^2}\) and \(|0.827 − 0.812| / \sqrt{0.010^2 + 0.006^2}\).  
- Check the rendered PDF to ensure the square root covers the full sum in each case, not just the first term.

---

P1B‑N2 – NEW  
**Location:** Sec. III (MB–H₀ offset calculation: “This offset is ∼ 3.2σ relative to the chain’s σ_MB = 0.049 marginal width…”)  

**Issue (Arithmetic transparency):** The 3.2σ figure is quoted without showing the actual difference and division. From the numbers given, the MB–H₀ degeneracy‑axis constant shifts from −18.571 (Riess anchor) to −18.415 (chain mean), i.e. Δ = 0.156 mag, so 0.156/0.049 ≈ 3.18 ≈ 3.2σ. The arithmetic is correct, but nowhere is this spelled out, so the reader cannot immediately verify how 3.2σ arises from the quoted 0.156 and 0.049.  

**Required fix:**  
- Add the explicit computation: “0.156/0.049 ≈ 3.2” when you first state “∼ 3.2σ”, to keep this in line with the explicit derivations you now provide for H₀ and β significances.

---

P1B‑N3 – NEW  
**Location:** Table I caption (S₈ tension and combination math).  

**Issue (Arithmetic / comparability clarifications):**  
- You correctly compute the naive two‑Gaussian combination of S₈ = 0.827 ± 0.010 (Planck+BAO+SN) with the DES‑Y3 prior 0.776 ± 0.017 to get 0.814 ± 0.009, and then state that the full‑tension chain’s 0.814 ± 0.008 is consistent “at the 0.01σ level.” The agreement is fine, but “0.01σ level” is never shown explicitly.  
- You also quote 2.6σ and 2.0σ “tensions” using two different constructions: a two‑Gaussian survey‑vs‑survey comparison for Planck+BAO+SN vs DES‑Y3, and a within‑stack posterior shift for the full‑tension chain which already includes the DES‑Y3 prior. You do flag this distinction (“not a measurement‑vs‑measurement tension but a within‑stack posterior shift”), but these σ values sit side‑by‑side and will be read as comparable. This is exactly the null‑procedure comparability issue you were asked to clean up elsewhere.  

**Required fix:**  
- In the caption, add a parenthetical explicit computation for the 2.6σ and 2.0σ numbers (e.g. “2.6σ = 0.049/0.019” with 0.019 from \(\sqrt{0.010^2+0.017^2}\)).  
- Add a one‑sentence clarification that the 2.6σ value is a survey‑vs‑survey Gaussian difference, whereas the 2.0σ value is a within‑posterior shift in a chain where DES‑Y3 is already an active prior, and therefore the two σ’s are not directly comparable.

---

P1B‑N4 – NEW  
**Location:** Sec. VI, Eq. (4) and surrounding text (ALP birefringence computation).  

**Issue (Arithmetic precision / internal consistency):**  
- You write: “The product of the three factors is 5.81×10⁻⁴ × 8 × 1.06 = 4.93×10⁻³ rad… rounding to two significant figures on ∆ϕ/fa would give 4.65×10⁻³, so the third significant figure is sensitive…” There are two issues:  
  - The phrase “three factors” is inaccurate; there are effectively four multiplicative pieces (α_EM, 1/(4π), C_{aγ}, ∆ϕ/fa), even if you are grouping α_EM/(4π) as one constant.  
  - The “4.65×10⁻³” number is just the same product with ∆ϕ/fa truncated, but the text does not show that explicitly; this is subtle and easy to misread as a different computation.  

**Required fix:**  
- Rephrase to make the grouping explicit, e.g. “Using α_EM/(4π) = 5.81×10⁻⁴, C_{aγ} = 8, and ∆ϕ/fa = 1.0601, the product C_{aγ}[α_EM/(4π)](∆ϕ/fa) = 5.81×10⁻⁴×8×1.0601 ≈ 4.93×10⁻³ rad.”  
- Then separate the truncation comment, e.g. “If ∆ϕ/fa were rounded to 1.06, the product would instead be 5.81×10⁻⁴×8×1.06 ≈ 4.94×10⁻³ rad, illustrating that the third significant figure is sensitive to the EOM precision.”  

This keeps the arithmetic traceable and avoids the impression that there are inconsistent numbers.

---

P1B‑N5 – NEW  
**Location:** Sec. VI (“Headline observational constraint”), Eq. (5), and abstract’s “3.9σ upper bound”.  

**Issue (Arithmetic & null‑procedure comparability):**  
- The inverse‑variance combination of β_P = 0.30±0.11° and β_A = 0.215±0.074° does indeed give β_comb ≈ 0.241° and σ_comb ≈ 0.061°, so 0.241/0.061 ≈ 3.95 ≈ “3.9σ”. The arithmetic is sound, but the abstract and Sec. VI both describe this as an “upper bound” without showing the computation, and the phrase “3.9σ upper bound” will be read as quantitatively comparable to the 3.6σ Eskilt–Komatsu result, even though one is a correlated joint‑likelihood significance and the other is a deliberately‑optimistic naive combination that assumes zero correlation.  

**Required fix:**  
- Add the explicit numbers in the main text around Eq. (5): e.g. show the weights and the √(σ⁻²) combination explicitly so a reader can reproduce 0.241 and 0.061.  
- Strengthen the non‑comparability disclaimer wherever 3.9σ and 3.6σ appear near each other (including the abstract), explicitly stating that the 3.9σ value is a deliberately‑optimistic naive Gaussian cross‑check that assumes zero correlation, and is not directly comparable to the properly‑correlated 3.6σ headline.

---

P1B‑N6 – NEW  
**Location:** Sec. III, footnote on sample counts; Fig. 1 caption (119,617 vs 176,240, 123,129, 123,368; 216,432 total).  

**Issue (Stale / confusing numbers):**  
- You have four different sample‑count figures for the same full‑tension chain (raw 176,240; three slightly different post‑burn‑in counts 123,368, 123,129, 119,617; and the combined 216,432). The long footnote explains why they differ (different burn‑in fractions and GetDist thinning), but the text is hard to follow and uses two distinct Planck+BAO+SN post‑burn‑in values (93,064 vs 93,066) without clearly saying which one underlies which table.  
- This is exactly the kind of “stale number left from an earlier cut” that causes confusion, even if the differences are small.  

**Required fix:**  
- Decide on a single authoritative post‑burn‑in sample count per chain at the adopted burn‑in fraction, and use those same counts consistently in the main text, Fig. 1 caption, and footnote.  
- In the footnote, explicitly map: “Table I uses N_post = … for full‑tension and … for Planck+BAO+SN” and then note that other values quoted (e.g. 119,617 after thinning; 93,066 versus 93,064) are GetDist‑internals that do not affect any reported scalar. This removes the appearance of inconsistent bookkeeping.

---

P1B‑N7 – NEW  
**Location:** Sec. IV (NaMaster “pipeline‑recovery SNR” vs per‑realization β̂/σ_β), Fig. 3 and associated footnote 4.  

**Issue (σ / SNR comparability):**  
- You correctly distinguish the template SNR (SNR_tmpl ≈ 20–26) from the per‑realization angle SNR (β̂/σ_β ≈ 5–8), but in several places these numbers are quoted close together without reiterating that they refer to different estimators and nulls. In particular, the abstract calls out “pipeline template‑fit SNR figures (e.g., 20.32)” while elsewhere you quote per‑realization |β̂|/σ_β ≈ 5.2 as a measure of angle recovery. It is easy for readers (and even referees) to mentally compare “20σ pipeline” vs “3.6σ sky” despite your earlier cautions.  

**Required fix:**  
- Wherever SNR_tmpl and |β̂|/σ_β appear in the same paragraph or section, add a short qualifier that they are not directly comparable statistics (template‑space SNR for a matched filter vs angle‑space SNR per realization).  
- In the abstract, add a brief parenthetical like “(template‑space pipeline SNR, not directly comparable to sky‑measurement significances)” to prevent over‑interpretation.

---

P1B‑N8 – NEW  
**Location:** Sec. VI (“Spectator‑subset readout”), Ω_a fractions 44% and 13%.  

**Issue (Arithmetic / dependence on fixed H₀):**  
- You correctly note that Ω_a is computed at fixed H₀ = 67.68 km/s/Mpc and that Ω_a ∝ H₀⁻², then state that marginalizing over the Planck 1σ range shifts Ω_a by ≲1%. Given the quoted H₀ errors, this “≲1%” is plausible but not explicit. The fractions 44% and 13% are sensitive to the Ω_a thresholds 0.1 and 0.01; a 1–2% change in Ω_a can move some samples across those cuts. This is a subtle but load‑bearing arithmetic point because you use these fractions to support the claim that only a small subset of the posterior is spectator‑safe.  

**Required fix:**  
- Add a short explicit estimate: e.g. “A ±1.06 km/s/Mpc shift in H₀ corresponds to a fractional change ΔH₀/H₀ ≈ 1.6%, so Ω_a changes by ≈3.2%, which in the current chain moves the Ω_a < 0.01 fraction from 13% to [X,Y]% (checked in a quick rescaling test).” Even a simple rescaling of stored Ω_a values by (H₀_new/H₀_old)⁻² would suffice.  
- Clarify that the quoted 44% and 13% are at fixed H₀ and may shift at the few‑percent level if H₀ is marginalized, but that this does not change the qualitative conclusion that the spectator‑safe subset is a minority.

---

If you want, I can next walk systematically through A–I for the sections you care most about (Table I/II, Fig. 1–4, Sec. VI) and draft the exact LaTeX edits so you can drop them into the manuscript with minimal friction.