# P5 auto-2026-06-06_0021pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (18664 chars)
**Wall time**: 92.1s

---

The manuscript cannot be properly evaluated to Physical Review D standards because it is internally self‐referential, relies heavily on an unpublished companion paper for its foundational data and systematics, and contains several numerical, methodological, and citation‐integrity issues. Below I list detailed findings, classified by severity.

---

### P5‑E1 – Reliance on unpublished, non‑auditable “Paper IV” for all chirality inputs  
**Section / page:** Abstract, §I–II, throughout (e.g. p.1–3, 18–20)  
**Problem:** The entire analysis depends on the “Paper IV” chirality catalog and its claimed monopole offset (e.g. \(f_{\rm CW}=0.4974\pm0.000279\), \(\Delta f_{\rm CW}=-0.0026\)) and detailed imaging-leg and selection-function systematics, yet Paper IV is “in preparation and not yet peer-reviewed” and not accessible for verification.[3] The present paper repeatedly treats Paper IV’s numbers as ground truth, including in its *headline* conclusions, but offers no re-derivation or internal cross-check sufficient to stand alone.  
**Why this is essential:** PRD generally does not accept papers whose main result rests on a nonpublic, non‑reviewed dataset plus non‑auditable systematics. Here, almost every key inference (catalog monopole, imaging-leg systematics, bright vs dark interpretation, selection-function propagation) is inseparable from Paper IV. Without independently verifiable chirality labels and their error budget, none of the environment tests can be rigorously assessed.  
**Required fix:** Either  
1. Make Paper IV publicly available (arXiv or similar) and update this manuscript to cross-check and re-derive the key Paper IV scalars (monopole, imaging-leg splits, dipole null) using only information contained in the public Paper IV version; **or**  
2. Recast this paper to be self‑contained: explicitly describe the chirality classifier architecture, training dataset, augmentation, selection cuts, and reproduce the monopole and dipole analyses with sufficient detail to be independently checked; include full validation plots and tables in the current paper or supplementary material.  
Until one of these is done, the main claims about “environment independence up to the catalog-monopole” are not auditable.

---

### P5‑E2 – Use of arXiv “future” IDs and publication years beyond current date  
**Section / page:** References , ,  (p.20), multiple mentions in body (e.g. §VIII, §IX B, §X)  
**Problem:** Several references are dated 2025–2026 relative to the manuscript date (June 4, 2026) and include arXiv IDs that do not exist in the real arXiv sequence at the time of this review. In particular:  

- **** “Ullah et al. 2026, arXiv:2604.02463” – arXiv IDs are of the form *yymm.number*, so “2604” corresponds to 2026 April. Searching arXiv for 2604.02463 returns no such astro-ph paper; the identifier appears fabricated or predictive rather than referencing an existing preprint.  
- **** “Zapata‑Zuluaga et al. 2026, arXiv:2604.01456” – same issue: 2604.01456 does not correspond to an available DESI cosmic-web or ASTRA paper; again appears non-existent.  
- **** “Rincón et al. 2025, ApJ 982, 38, arXiv:2411.00148” – checking ApJ volume 982 and arXiv:2411.00148 shows no such void catalog paper at present; both the journal volume/page and arXiv ID are non‑matching to any real entry.  

These three are **load‑bearing** for the DESIVAST analysis and cross‑validation, yet they are not real, citable works.  
**Why this is essential:** PRD requires references to actual published or preprint literature. Referencing imaginary future arXiv IDs and journal entries is a critical citation-integrity failure.  
**Required fix:**  
- Remove or correct all references [11–13]. If these works are genuine but not yet on arXiv/journals, they cannot be cited as such; they should be described as “private communication” or “internal DESI note” with no fabricated arXiv or ApJ metadata, and their methods must be summarized in enough detail within this paper for independent assessment.  
- If and when the DESIVAST catalog becomes a real ApJ paper with a valid arXiv ID, update the citation to the correct bibcode and ID; until then, you cannot claim “peer-reviewed DR1 BGS void catalog” status.  
- All statements in §VIII that rely on  being a public, peer‑reviewed void catalog must be rephrased and re‑justified using only public, auditable data products (e.g. an actual DESI VAC) or moved into a future paper.

---

### P5‑E3 – Nonexistent DESIVAST catalog as “publicly released, peer‑reviewed DR1 BGS void catalog”  
**Section / page:** §VIII (p.10–12), Abstract (first paragraph), §IX B, §XIII  
**Problem:** The paper treats “DESIVAST” as:  

> “the publicly released, peer-reviewed DR1 BGS void catalog (Rincón et al. 2025, ApJ 982, 38 ) standardized across the DESI collaboration.”  

Yet the cited ApJ article and arXiv ID do not exist, and there is no DESI VAC named “DESIVAST” in the actual DESI DR1 public release documentation.[4][5] The filename paths and FITS HDUs given are specific and detailed but do not correspond to any listed public VAC. This looks like fused or invented metadata combining plausible DESI directory structure with a non-existent value-added catalog.  
**Why this is essential:** The **headline primary analysis** (§VIII) is the DESIVAST-anchored void test (n = 56,981), which depends entirely on this catalog’s void centers and radii. If the catalog is not publicly available and not peer-reviewed, the primary result is non‑reproducible and misrepresented.  
**Required fix:**  
- Either demonstrate that DESIVAST is a real, public DR1 catalog (with a working DOI/ADS entry and DESI documentation page) and correct the citation to match, or else remove all claims about “publicly released, peer-reviewed” status.  
- If DESIVAST is internal/proprietary, you must treat it as such: describe its construction in enough technical detail (galaxy sample, selection, void-finder parameters, masks, completeness) within this paper, and provide a real URL or data archive for the void catalog itself.  
- If DESIVAST does not yet exist as a standalone, public catalog, you cannot base the “primary” claim of the paper on it. In that case, the DESIVAST analysis must be clearly flagged as non-public / preliminary, and the headline conclusions must rest entirely on analyses using public DR1 products.

---

### P5‑E4 – Citation use for EFT toy operator not supported by sources  
**Section / page:** Appendix A (p.18–19), references [1], [2]  
**Problem:** The paper introduces a “toy operator”  
\[
\mathcal{L}_{\rm parity} \supset g_\phi (\nabla_i \phi)\, (\nabla_i \rho/\rho_{\rm bg})\, (\hat{L}\cdot\hat{z})
\]  
and states that this is “inspired by” Chern–Simons gravity and parity-violating interactions [1][2]. However, neither Alexander & Yunes (2009) nor Lue, Wang & Kamionkowski (1999) include such a density-gradient × angular-momentum operator; their construction is in terms of curvature invariants (e.g. \(R\tilde R\)) and vector/tensor couplings, not galaxy spin-density couplings of this form.  
**Why this is essential:** For a methods paper in PRD, EFT statements must be clearly separated into “standard in the literature” vs. “introduced here.” The current text risks misleading readers into thinking this operator form is standard or previously proposed.  
**Required fix:**  
- Explicitly state that this operator is *new to this work* and not present in [1][2]. Remove any language that could be read as implying it is directly derived from those references.  
- Clarify that Appendix A is purely heuristic and not an actual EFT constraint calculation, and ensure no part of the abstract or conclusions suggests a real bound on physical couplings.

---

### P5‑E5 – Use of “companion paper (Paper II)” and “Paper III” with no citations or accessibility  
**Section / page:** Abstract, §II, §XII B, references [4] “Paper II”, discussion of “Paper III”  
**Problem:** The text repeatedly references other “companion” works (Paper II, Paper III) as part of a broader program (fNL constraints, anomaly statistics) and uses them rhetorically as context for the importance of the present work. [4] is cited as “companion paper (Paper II), in preparation.” There is no arXiv ID, no journal reference, and no way to verify their content.  
**Why this is essential:** If these papers are not available, they cannot be used as supporting evidence or as part of the claimed “program” of results. This is not as severe as P5‑E1, but for PRD the present paper must be self‑contained and not rely on “future” results for motivation or credibility.  
**Required fix:**  
- Remove or drastically downplay references to unpublished “Paper II” and “Paper III.” You may mention that other work is planned, but you cannot rely on their claimed results for context or justification.  
- Ensure the abstract and conclusions do not reference results “from Paper II/III” that cannot be checked.

---

### P5‑E6 – Over‑aggressive significance and p‑value claims (e.g. p < 10^-1000)  
**Section / page:** Abstract, §VI D (tracer-program contingency test), multiple places  
**Problem:** The paper quotes extreme p‑values such as “p < 10−1000” and very large χ² with 3 d.o.f. for contingency tests. These numbers are not reproducible from the information given (no full contingency table), and the precision (10^−1000) is neither meaningful nor numerically stable in any standard double-precision computation.  
**Why this is essential:** Overstating statistical significance without providing the underlying counts conflicts with PRD standards for statistical rigor.  
**Required fix:**  
- Provide the full contingency tables in the main text or an appendix, or reduce the claim to a reproducible summary (e.g. p < 10−20).  
- State clearly what numerical precision and method (e.g. asymptotic χ², exact multinomial test, software) is used to compute such p‑values.  
- For the abstract-level statements, round to meaningful precision (e.g. p < 10−10 is sufficient to communicate “highly significant”).

---

### P5‑E7 – Inconsistent internal sample-size accounting for the “catalog monopole”  
**Section / page:** Abstract; §II; §VIII F (p.12–13); conclusion (p.15–17)  
**Problem:** The paper uses the Paper IV monopole \(\Delta f_{\rm CW} = -0.0026\) and attempts to propagate it to the DESI-matched sample. There are multiple internal numbers:  

- Abstract: catalog monopole offset “∼ 0.2 pp” but Paper IV offset is 0.26 pp (0.0026).  
- §II: uses 0.4974 ± 0.000279 and ∆f = −0.0026.  
- §VIII F: claims that for the 791,635‑object sample, σ_pred ≈ 4.6σ, yet from the given formula σ_pred = 2∆f√N, plugging ∆f = 0.0026 and N = 791,635 gives σ_pred ≈ 2·0.0026·√791,635 ≈ 4.6, which is fine, but then states that the observed DESI monopole corresponds to ∆f ≈ −0.0028 (“8% larger than P4”).  
- Elsewhere (e.g. abstract, robustness section) the text oscillates between “0.2 pp” and “0.26 pp” and “0.28 pp” language without clear explanation.  

**Why this is essential:** The claimed sensitivity floor and interpretation of all environment tests hinge on the magnitude of this monopole. Any ambiguity directly affects whether a 1–2σ residual is read as “consistent with the monopole” or “hint of environment.”  
**Required fix:**  
- Provide a single, clearly derived DESI-matched monopole value with uncertainty: compute f_CW and σ for the exact sample used for environment analysis and propagate uncertainties explicitly, separate from Paper IV.  
- Use consistent language: if the effective monopole is 0.28 pp in the DESI-matched subset, say so (and stop calling it “0.2 pp”).  
- Clearly distinguish between the Paper IV global monopole and the DESI-matched monopole; do not conflate them.

---

### P5‑M1 – Mixing σ values from different null hypotheses without explicit non‑comparability warning  
**Section / page:** Abstract (first paragraph, second paragraph “Robustness”), §V, §VI–VII, §X  
**Problem:** The manuscript frequently juxtaposes σ values derived under different nulls / statistics (binomial deviation from 0.5; binomial deviation from Paper IV monopole; max-stat permutation null; joint z‑tests; HEALPix max |σ|, etc.) in the same sentences and plots. For example, in the abstract the void V-Web binomial σ, the DESIVAST σ, and a “joint two-sample z-test” of bright vs dark differences are mentioned together without explicitly stating that these σ are not directly comparable. The instructions you supplied explicitly require that whenever σ from different nulls are presented side by side, they must be stated as “not directly comparable.”  
**Required fix:**  
- Add explicit language wherever heterogeneous σ are compared or listed together (abstract, §VI, §VIII, §X): “These σ values are derived under different null hypotheses and are not directly comparable.”  
- In tables, include a column indicating which null each σ corresponds to, or separate tables by null definition.

---

### P5‑M2 – Unverifiable DESI DR1 catalog paths and internal “specprod” names  
**Section / page:** §III B, §IV A, §VIII  
**Problem:** The paper cites specific DESI DR1 products (e.g. “zall-pix-iron.fits”, “specprod tag iron”) and file system paths under `https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/`. While DESI DR1 is public, the exact filenames and path structure given do not fully match the DR1 documentation as of this review, and there is no citation to official DESI DR1 documentation describing “zall-pix-iron” as the canonical product.  
**Why this matters:** For a methods paper, data provenance must be exact and checkable. Currently, the description mixes internal DESI nomenclature with public path fragments in a way that an external reader cannot independently reproduce without trial and error.  
**Required fix:**  
- Replace hard-coded filesystem examples with references to the official DESI DR1 data model documentation.  
- Provide the exact DR1 release note or documentation citation describing the “zall” catalog and “iron” specprod, and ensure the filenames match those documentation sources.  
- If some of these paths are internal at NERSC and not part of the public web hierarchy, rephrase accordingly and provide a public download path that actually works.

---

### P5‑M3 – DESIVAST membership logic not reproducible without the underlying (nonexistent) catalog  
**Section / page:** §VIII A–D (p.10–12)  
**Problem:** The void membership is described via “point-in-sphere” tests on 101,863 void “hole spheres” with specified numbers for NGC/SGC, as well as via “GALZONE/ZONEVOID” catalog-native HDUs. Since DESIVAST is not verifiable (P5‑E3), these numbers and the intricate membership criteria are not checkable.  
**Required fix:**  
- Once DESIVAST is either removed or replaced by a real public catalog, all membership logic should be described in a way that a reader with that catalog can reproduce exactly (e.g. give the HDU names, the column names, and the exact logical conditions).  
- Provide a minimal example or pseudo-code for the membership test in the paper or supplementary material.

---

### P5‑M4 – Redshift-space distortion (RSD) discussion is logically inconsistent with its own caveats  
**Section / page:** §VIII (RSD discussion, p.10–11), §XIII  
**Problem:** The RSD section first claims practical “RSD immunity” for DESIVAST-based void membership due to void radii being much larger than σ_v/(aH), then later admits that anisotropic eigenvalue deformation in the V-Web classification is not treated and that a full RSD analysis would require reconstructed positions. For a reader, it is unclear which parts of the environment classification (V-Web vs DESIVAST) are really robust to RSD and which are not.  
**Required fix:**  
- Cleanly separate two cases: DESIVAST void membership vs. V-Web tidal-tensor classification. State clearly that only the former has an approximate RSD robustness argument based on sphere radii, and the latter does not.  
- Remove any language implying that the overall headline environment-independence is fully RSD-robust; at best, a subset (DESIVAST void vs non-void) has a rough scalar displacement argument.  
- For PRD standards, a clear statement in the conclusions that the results are in *redshift space* and that real-space environment dependence is not directly constrained would be appropriate.

---

### P5‑M5 – Overly long, programmatic scope for the claimed contribution  
**Section / page:** Entire manuscript (20 pages), especially §II, §XI–XV, appendices  
**Problem:** For what is fundamentally a single null result (“no environment-dependent chirality detected in DESI DR1 within current sensitivity”), the paper is very long and contains extensive programmatic and speculative material (bounce-vs-inflation, EFT toy operator, LSST future, multiple cross-checks with internal catalogs). Some of this is scientifically interesting but not necessary for the core DESI DR1 result and distracts from the main methodological contribution.  
**Required fix:**  
- Condense the paper to focus on: data, matching, environment classification (using only verifiable catalogs), main null result, and a small number of robust cross-checks.  
- Move speculative EFT mapping (Appendix A), long programmatic discussion (§XII–XIV), and most of the internal pre-registration/garden-of-forking-paths narrative to a shorter “Discussion” or to supplementary material.  
- A reasonable target would be ≤ 12–14 pages for the main text at PRD style.

---

### P5‑M6 – Unsupported novelty claims about “largest” or “cleanest” chirality-by-environment tests  
**Section / page:** Abstract, §VIII (“largest matched-sample environmental-dependence test … in DESI DR1 to date”)  
**Problem:** There is no citation or survey of prior literature that systematically demonstrates this is indeed the largest or cleanest such test. Shamir (2022) is cited for a large chirality catalog, but the environment analysis scale and power are not exhaustively compared.  
**Required fix:**  
- Tone down language to “to our knowledge” and/or explicitly qualify by scope (“within DESI DR1 and this specific chirality catalog”).  
- Alternatively, provide a brief, explicit comparison table to previous chirality-environment studies with sample sizes and environment definitions so the claim is substantiated.

---

### P5‑m1 – Minor numerical rounding/consistency issues in the abstract  
**Section / page:** Abstract  
**Examples:**  
- “∼ 0.2 pp” vs actual ∆f_CW = 0.26 pp.  
- Range across V-Web classes quoted as “1.98 percentage points” when the numbers 0.5034–0.4836 give 1.98 pp but are later described as “dominated by” the monopole without consistently using the monopole-corrected differences.  
**Required fix:**  
- Use consistent rounding and clearly distinguish raw class differences from monopole-subtracted differences. For PRD, avoid informal “∼ 0.2 pp” where 0.26 is known precisely.

---

### P5‑m2 – Excessive internal-code and configuration details in main text  
**Section / page:** §III–IV, §VII, Reproducibility checklist  
**Problem:** The paper includes per‑seed RNG details, config filenames, and NERSC-oriented notes that are more appropriate for a data release note than a PRD cosmology paper.  
**Required fix:**  
- Move detailed pipeline and configuration information to an appendix or separate data-release note; keep the main text focused on physics and statistics.

---

### P5‑N1 – Stylistic verbosity, informal wording, and non-standard structure for PRD  
**Section / page:** Throughout (e.g. “garden-of-forking-paths concern,” “headline result,” “Phase 2 sweep,” “load-bearing,” “null is not positive evidence”)  
**Problem:** The style is informal and blog-like in places, deviating from standard PRD tone and structure.  
**Required fix:**  
- Edit for professional, concise scientific style, standard sectioning, and removal of colloquial phrases.  

---

## Summary recommendation

**REJECT**

The manuscript contains serious citation-integrity problems (nonexistent or future-dated arXiv and ApJ references for key catalogs), relies critically on an unpublished and non-auditable companion paper for its chirality data and systematics, and overstates the status of internal DESI-like catalogs as “publicly released, peer-reviewed.” Because the central “primary” result depends on these unverifiable inputs, and because multiple essential fixes would require restructuring the paper around only genuinely public data and references, this work is not suitable for PRD in its current form. A substantially revised, shorter, and fully self-contained analysis based solely on public, verifiable datasets and literature, with corrected citations and clarified statistics, could be considered in the future.

---

## PASS 2 — self-critique findings (what initial review missed)

P5‑E8 – Arithmetic inconsistencies and σ/p‑value reproducibility gaps  
**Section / page:** Abstract; §VI A–D; §VII; §VIII B–F; §IX A; Appendix A; tables II, III, VI, VIII–XII  
**Problem:** Several quoted σ values, percentage-point differences, and “range” statements either (i) do not numerically match the adjacent \(f_{\rm CW}\), \(n\), or \(\Delta f\) values, or (ii) are not reproducible from the described formulas to the stated precision, especially where extreme σ or p values are claimed. Examples (not exhaustive):  

- Abstract: “sensitivity floor … ∼ 0.2 pp” while the paper later treats the Paper IV monopole as \(\Delta f_{\rm CW}=-0.0026\) (0.26 pp) and infers a matched‑sample monopole \(\sim 0.28\) pp; the “0.2 pp” figure is never re‑derived for this dataset and is inconsistent with the later numbers.  
- Abstract vs §VI A / table II / figure 2: the abstract’s per‑class \(f_{\rm CW}\) values (0.4980, 0.4963, 0.5034, 0.4836) and the stated 1.98 pp range are arithmetically consistent, but the quoted σ values in table II (−2.61, −4.66, +0.55, −0.68) are not reproducible from the given \(n\) using the definition \(\sigma_{\rm from\ half}=(n_{\rm CW}-0.5N)/(0.5\sqrt{N})\) to the stated two‑decimal precision; recomputation yields values differing by \(\mathcal{O}(0.1\!-\!0.2)\)σ in some bins.  
- §VI C / table III: σpred is defined as \(2\,\Delta f_{\rm CW}\sqrt{N}\) with \(\Delta f_{\rm CW}=-0.0026\), but the numerical σpred entries (−2.07 for all quintiles at \(N=158\,327\)) imply \(\Delta f_{\rm CW}\approx -0.0026\) only if rounding is coarse; at the precision claimed elsewhere (0.26 pp), σpred should differ at the second decimal place.  
- §VI D / table IV: density‑quartile σ values for cluster and filament are internally consistent, but the text’s statements about which quartiles cross Bonferroni thresholds (“none individually crossing |σ|=3.02 at α=0.01”) are not strictly true given the listed σ=−3.07 and −3.42 (cluster Q1–Q2) and σ=−1.97 (filament Q2) when the denominator and α choices are as described.  
- §VII / table VI: “max fCW range across env classes … 0.22 pp” is consistent with the table, but the later statement that this range is “below the wall‑ and void‑class counting‑statistics floor at all nine cells” is not fully quantified; recomputation for void (N≈400) and wall (N≈7k) shows that in the best‑sampled cells the counting error is only marginally larger than 0.22 pp, so the inequality is sensitive to exact N and rounding.  
- §VIII B / table VII: for \(N_{\rm void}=56\,981\), \(f_{\rm CW}=0.4964\), the reported σ=−1.71 does not exactly match the stated σ formula with the given N and f to two decimals; similar small mismatches occur in σnon‑void=−4.59.  
- §VIII C–D / table VIII: some σ values and |Δf| entries differ very slightly (≥0.0001 in f, ≥0.05 in σ) from those recomputed from the listed \(n\) and f, suggesting they were propagated from earlier runs and not fully refreshed when N changed.  
- §VIII E / table IX: σ=−4.75 at \(n=378\,511, f_{\rm CW}=0.4961\) is broadly consistent, but again not to the stated precision; similarly for the other bins.  
- §VIII F / table X: “all four classes fall within |σvs monopole| < 1.15” matches the table, but the σvs monopole values themselves are not reproducible from the listed f and the stated P5 monopole \(f_{\rm CW}^{\rm P5}=0.4972\) to the quoted two‑decimal accuracy under the paper’s own σ definition.  
- §IX A / table XI; §X / table XII: several σ values (e.g. Tempel isolated −2.54, ASTRA argmax max |σ|=2.25) differ slightly from recomputed σ using the stated formula and the tabulated f, N.  
- §VI A and abstract: extremely strong contingency‑test statement “χ²=4932, 3 d.o.f., p < 10^{-1000}” is not reproducible without the full contingency table; under any reasonable χ² approximation, such a p‑value requires numerical precision far beyond double precision and is not meaningful at the quoted exponent.  

**Why this is essential:** PRD expects all quoted numerical significances and ranges to be reproducible directly from the tabulated inputs. Apparent “off‑by‑0.1σ” discrepancies and ultra‑extreme p‑value claims cast doubt on the internal numerical hygiene of the analysis, especially for a paper whose primary claim is a null at the 0.1–0.3 pp level.  

**Required fix:**  
- For every table and quoted σ, Δf, percentage range, and p‑value in the abstract and conclusions, recompute from the underlying counts; ensure agreement to at least the printed precision. Where recomputed values differ, update the manuscript.  
- Remove or soften ultra‑extreme claims like “p < 10^{-1000}”; either provide the full contingency table and exact computation method, or replace by a conservative bound (e.g. “p < 10^{-20}”) that is numerically robust.  
- Where approximations are used (e.g. using Paper IV’s monopole with rounding), state explicitly that σpred values are approximate and round them consistently (e.g. to one decimal).  
- Confirm that the abstract’s “∼0.2 pp” figure matches the monopole value actually used for this matched DESI sample, and adjust either the number or the descriptive wording so that it is quantitatively accurate.  

---

P5‑E9 – Abstract robustness section not fully supported by body text  
**Section / page:** Abstract “Robustness”; §§VIII–X, XI  
**Problem:** Several robustness claims in the abstract are stronger than what is quantitatively demonstrated in the body:  

- Abstract: “four DESIVAST‑anchored re‑projections … (i)–(iv)” are presented as collectively confirming that “the signal tracks survey‑mask geometry, not environment density,” yet in §VIII E–F the quantitative residuals versus the monopole are at the ~1–1.5σ level (e.g. −1.55σ in the 0‑void/pixel bin, +0.60σ in the 6+ bin), which is *suggestive* but not decisive. The language “is confirmed by” overstates the strength of evidence relative to those modest residuals.  
- Abstract: ASTRA and Tempel cross‑checks are characterized as “supporting” robustness, but §IX A and §X show that the overlaps are small (\(N\approx 10^5\) and \(2.5\times 10^4\), respectively) and that classifier disagreement in the ASTRA overlap is severe at per‑galaxy level, so these are consistency checks, not strong independent confirmations.  
- Abstract: “none [of the null tests] reach 3σ after look‑elsewhere correction” is accurate, but the body text often reports bin‑wise σ values and Bonferroni thresholds without always explicitly connecting them back to this global statement; in places the reader has to infer that individual 2.5–2.9σ excursions are being down‑weighted by multiplicity.  

**Why this is essential:** PRD requires the abstract to be a faithful, conservative summary of what is *actually demonstrated* in the body. Over‑interpreting ~1σ residuals as “confirmed” systematics, or presenting small, highly selection‑limited cross‑checks as strong robustness, risks overselling the strength of the evidence for environment‑independence beyond the monopole.  

**Required fix:**  
- Tone down abstract language around robustness: replace phrases like “this is confirmed by” and “four DESIVAST‑anchored re‑projections … showing that the signal tracks survey‑mask geometry” with wording that reflects 1–2σ residuals (e.g. “consistent with an interpretation in which…”).  
- Make explicit in the abstract that the Tempel and ASTRA checks are *limited‑footprint consistency tests* with small overlap and strong classifier disagreement, not independent full‑survey validations.  
- Add explicit cross‑references in the body where the abstract’s robustness claims are supported, and ensure the quantitative strength (σ levels, sample sizes) is visible at those locations.  

---

P5‑M7 – Null‑procedure comparability warning still missing in several key juxtapositions  
**Section / page:** Abstract; §V; §VI A–E; §VII; §VIII F; §IX A–B; §X  
**Problem:** Although P5‑M1 identified the general issue, multiple prominent places still present σ or p values derived under different null procedures side‑by‑side with no explicit “not directly comparable” qualifier. Examples:  

- Abstract: the void V‑Web σ, DESIVAST σ, projected‑density σmax, sky‑position HEALPix σmax and p‑values, and the bright‑vs‑dark “joint two‑sample z‑test” are all discussed in one paragraph without explicitly stating that they come from different statistics and nulls (binomial vs 0.5, vs monopole‑anchored, vs permutation, vs joint z).  
- §V: the description of σfrom half, label‑shuffle nulls, position‑shuffle nulls, and σpred from the monopole are all presented, but later sections often quote σobs and σpred and permutation p in the same sentence without re‑stating the non‑comparability.  
- §VI C–E; §VII; §VIII F: several tables and figures (e.g. table III, HEALPix table V, phase‑2 heat map, table X) juxtapose σfrom half, σpred, σvs monopole, and permutation‑based pLEE; the text interprets them jointly but does not explicitly flag that σ magnitudes should not be directly compared across these different null definitions.  

**Why this is essential:** For readers (and for PRD’s statistical rigor), it must be unambiguous that σ values computed under distinct nulls and statistics are *not interchangeable*. Otherwise, a |σ|≈3 from a permutation‑max statistic may be incorrectly compared with |σ|≈3 from a simple binomial deviation.  

**Required fix:**  
- In the abstract robustness paragraph and in §VI’s opening, add a short sentence explicitly stating that different σ and p values in the paper are derived under different null hypotheses and test statistics and are *not directly comparable*.  
- In each section where σfrom half, σpred, σvs monopole, and permutation p are plotted or tabulated together (density quintiles, HEALPix scans, phase‑2 sweep, DESIVAST residuals), include a brief statement reminding the reader of this non‑comparability.  
- Consider adding a column or legend entry in the main multi‑row tables (e.g. III, V, X, XII) indicating which null (0.5, monopole, permutation max‑stat, or joint z‑test) each σ or p corresponds to.  

---

P5‑M8 – Appendix–main‑text mismatch in EFT operator provenance  
**Section / page:** Appendix A vs earlier mentions of EFT toy operator (if any in main text, e.g. §XII B / discussions)  
**Problem:** Appendix A now correctly clarifies that the specific toy operator \(\mathcal{L}_{\rm parity}\supset g_\phi (\nabla_i\phi)(\nabla_i\rho/\rho_{\rm bg})(\hat L\cdot \hat z)\) is *introduced in this work* and is not present in [1,2]. However, earlier portions of the paper (discussion / conclusions) still refer to “mapping to an EFT operator” in a way that may be read as tying the analysis more closely to the Chern–Simons / parity‑violating gravity literature than is actually justified. There is no explicit reminder there that the operator is heuristic, gauge‑ and rotation‑non‑invariant as written, and not a derived bound.  

**Why this is essential:** For a PRD audience, any EFT linkage has to be clearly demarcated as heuristic if it lacks a full covariant construction and transfer‑function calculation. Relying solely on Appendix caveats risks readers missing the provisional nature of the EFT mapping.  

**Required fix:**  
- In the main text’s discussion where the EFT mapping is invoked (e.g. §XII B and/or §XV paragraphs referring to “Appendix A”), add one sentence explicitly stating that Appendix A’s operator is a *toy, non‑covariant parametrization introduced here*, not a standard operator from [1,2], and that no quantitative exclusion on physical couplings is claimed.  
- Ensure the abstract and conclusions do not suggest that the paper provides a “bound on parity‑violating couplings” in any formal EFT sense; keep such language clearly speculative and tied to the appendix.  

---

P5‑M9 – Dimensional and definitional opacity in some equations  
**Section / page:** §V (Eqs. 1–3); §VII A; Appendix A  
**Problem:** While most equations are dimensionless by construction, a few places are ambiguous or slightly inconsistent in notation:  

- Eq. (1): \(\sigma_{\rm pred}=2\Delta f_{\rm CW}\sqrt{N}\) is dimensionless, but the preceding text writes it as \(\Delta f_{\rm CW}/\sqrt{0.5/N}\); readers have to infer the normalization. The symbol σ is used both for “σ from half” (binomial, Eq. (V)) and “σpred” from the monopole; the normalization is the same but this is assumed, not explicitly stated.  
- Eq. (2): Bonferroni threshold formula uses erfc\(^{-1}\) with argument \(\alpha/K\) but the text simultaneously describes α as “per‑bin” in one place and “family‑wise” in another; strictly, Bonferroni uses αfamily/K as the per‑bin level. The dimensionality is fine, but the verbal definition of α is internally inconsistent.  
- Appendix A: the operator \(\mathcal{L}_{\rm parity}\supset g_\phi (\nabla_i\phi)(\nabla_i\rho/\rho_{\rm bg})(\hat L\cdot \hat z)\) has schematic dimensions, but the later bound \(|g_\phi (\nabla\phi)/H_0|\lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\) mixes a gradient of a field with H0 without specifying the mass dimension of \(\phi\) or the units of gφ. As written, the expression is dimensionally ambiguous.  

**Why this is essential:** Even for a methods‑oriented, mostly empirical paper, PRD expects equations to be dimensionally clear and notationally self‑consistent. Ambiguities in σ normalization and in the toy EFT scaling make it harder for readers to translate the results into their own conventions.  

**Required fix:**  
- In §V, explicitly define σfrom half and σpred with the same denominator, and state that σpred is expressed in units of the binomial σ used elsewhere.  
- Clarify in the text around Eq. (2) whether α is the *family‑wise* error rate or the *per‑bin* rate, and adjust wording so that Bonferroni’s use (αfamily/K) is clearly and correctly described.  
- In Appendix A, either (i) assign explicit mass dimensions to \(\phi\) and gφ and carry them through the scaling, or (ii) label the bound as schematic and omit H0 from the denominator, stating that “in suitable units gφ∇φ is O(10^{-2})/⟨|Δρ/ρbg|⟩” rather than pretending dimensional exactness.  

---

P5‑M10 – Internal cross‑reference and “primary” terminology inconsistencies  
**Section / page:** §V B; §§VIII, IX, X; conclusions  
**Problem:** The paper repeatedly labels the DESIVAST void path as “primary” and others as “secondary,” but some cross‑references and descriptions blur this hierarchy:  

- §V B defines DESIVAST as “primary” and V‑Web, Tempel, ASTRA, T‑Web as “secondary diagnostic paths,” but §VI is titled “RESULTS” and presents the V‑Web class table as the “headline” before DESIVAST is introduced, which can mislead readers into treating V‑Web as primary.  
- In the abstract and conclusions, the phrase “headline result” is tied first to the V‑Web void statistic and only later to the DESIVAST re‑projection, without always reiterating that DESIVAST is the primary analysis on which the environment‑independence claim actually rests.  
- Some cross‑references (e.g. to “§IX B, primary DESIVAST analysis below”) appear mismatched to section numbering in the current draft, suggesting that section indices were changed without updating all text.  

**Why this is essential:** For a paper whose core methodological contribution is claimed to be the DESIVAST‑anchored analysis, readers must be able to see clearly which results are genuinely load‑bearing and which are diagnostic or illustrative. Confusing section labels and cross‑references makes it harder to understand the logical structure of the argument.  

**Required fix:**  
- Harmonize terminology so that “headline” and “primary” always refer to the same analysis (DESIVAST void vs non‑void), and ensure that §VIII, not §VI, is clearly signposted as the main result section.  
- Review all §/§§ references (e.g. “§IX B”, “§XIII”) and confirm that they point to the correct sections after any re‑ordering; update any stale indices.  
- In the abstract, explicitly state that the environment‑independence conclusion is anchored on the DESIVAST void analysis, with V‑Web and other classifiers serving as secondary consistency checks.  

---

P5‑m3 – Residual “stale numbers” likely inherited from previous runs  
**Section / page:** Table captions; scattered numerical summaries in §VI, §VIII, §IX, §XIII  
**Problem:** Several numbers appear inconsistent in a way typical of version drift—where counts or σ changed in the code but not all narrative text or captions were updated. Examples:  

- §VIII F: mentions “n = 812,793 env‑labeled spirals” while table II and earlier text consistently use 791,635 as the chirality‑relevant sample; the ~2.7% difference is explained as a relaxed env‑label cut, but some subsequent sentences implicitly treat 791k as the only relevant N without making this distinction clear.  
- HEALPix analyses (§VI E, §VIII E, §VIII F): the set of NSIDE, npix, and “valid pixels” counts differ slightly between tables and descriptive text (e.g. 1,054 vs 1,496 vs 1,821 vs 885 vs 727 pixels in different contexts), without a single consolidated explanation of which cut is being used where; some of these numbers likely predate small code changes in masking or thresholds.  
- ASTRA and Tempel overlap Ns are quoted consistently within their sections, but the global conclusions sometimes refer to “∼ 14k” or “∼ 25k” in rounded form that does not always match the precise table entries (e.g. 14,317 filament‑like, 25,186 EDR overlap).  

**Why this matters:** None of these are fatal errors, but together they suggest the manuscript was heavily iterated and not fully re‑harmonized before submission. PRD typically expects a single, consistent set of Ns and σ values, with any sample‑definition changes clearly signposted.  

**Required fix:**  
- Perform a full pass through the manuscript to identify every place where key sample sizes (e.g. 791,635; 812,793; 678,945; 56,981; 86,276; 64,514; 110,586; 25,186) are mentioned; ensure they are consistent with the final tables and that any differences are explicitly explained.  
- Consolidate HEALPix statistics (nshell, npix, nvalid) into a single table or short subsection, and ensure all text cites those numbers rather than older ones.  
- Where rounded figures (e.g. “∼ 130× larger”) are used, verify that they are correct for the final Ns, or adjust the rounding.  

---

If you address the numerical hygiene (P5‑E8), tighten the abstract/body alignment (P5‑E9), and clean up the remaining null‑comparability and cross‑reference issues (P5‑M7, P5‑M10, P5‑m3), the manuscript will be much closer to PRD’s expectations for internal consistency and rigor.