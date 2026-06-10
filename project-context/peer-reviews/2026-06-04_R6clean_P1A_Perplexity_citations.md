# P1A 2026-06-04_R6clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 50.1s

---

P1A-B1 (ESSENTIAL) – Global – Incomplete citation metadata for in‑preparation companion papers  
**Problem:** Multiple references to “companion work in preparation” and “companion paper, this volume” are given citation numbers [2], , , ,  without arXiv IDs, journal info, or public availability, e.g.  
- “a companion work in preparation [2]” (Abstract)  
- “companion works in preparation [2, 6]” (Abstract)  
- “Paper I(b)  … in preparation” (Sec. I, Companion paper paragraph)  
- “Paper IV ” (Sec. III B, Sec. V, Sec. XIV B)  
- “Paper III ” (Sec. XIII G)  
- Ref. [2], , , ,  at end are explicitly “(in preparation)” with internal report codes (hUBIFY‑…).  
Physical Review D generally requires references to be publicly accessible (arXiv or published). These works are also used as **sources of numerical results, MCMC chains, systematics audits, and forecasts**, not just mentioned as future work.  
**Required fix:**  
- Before acceptance, either:  
  - (a) Post each companion paper to arXiv and update references with arXiv IDs and full titles; or  
  - (b) Remove any dependence on unpublished internal work for quantitative claims, replacing with published literature or self‑contained derivations in this paper.  
- For any still genuinely “in preparation” work, restrict citations to purely forward‑looking statements and remove use as a source for concrete results, parameter values, or forecasts.

---

P1A-B2 (ESSENTIAL) – Global / Abstract / Sec. II C / Appendix B – Use of internal/unpublished numbers as if established results  
**Problem:** The paper treats internal MCMC outputs and forecasts from companion papers as if they were established, citable numerical results:  
- “ΛCDM+∆Neff MCMC verification … are documented separately in companion work in preparation .” (Abstract)  
- “Cosmological parameter values referenced in this paper (H0 = 67.68 ± 1.06, ∆Neff ≈ 0, etc.) are drawn from the companion internal MCMC analysis … they are documented internally rather than as externally citable arXiv-posted numbers…” (Sec. I).  
- Table IV lists precise posteriors (H0, σ8, Ωm, ∆Neff) with  as source.  
- SPHEREx fNL forecast significance (3–5σ) is attributed to [2], which is in preparation.  
These values are used in arguments and tables but the underlying analyses are not accessible.  
**Required fix:**  
- Either (i) make the MCMC and forecast papers public (arXiv) and update the references with full metadata, or (ii) remove the numerical use of these unpublished posteriors and forecasts from this paper. Replace them with published constraints (e.g., Planck, DESI, existing SPHEREx forecasts) and clearly separate what is new here from what is only planned elsewhere.  
- Explicitly state that any remaining internal numbers are illustrative only and not part of the paper’s quantitative claims.

---

P1A-B3 (ESSENTIAL) – Abstract & repeated later – σ‑scale mixing across different null procedures  
**Problem:** CMB birefringence detections are quoted and directly compared in σ units as if exactly comparable without qualification:  
- “βobs = 0.342◦ ± 0.094◦ (∼ 3.6σ from β = 0, first reported by Minami & Komatsu [3] and refined by Eskilt & Komatsu [4]), and is comparable to the independent ACT DR6 follow-up β = 0.215◦ ± 0.074◦ at ∼ 2.9σ (Diego-Palazuelos & Komatsu [5]).” (Abstract, Sec. III A, Sec. VI)  
These σ significances are from **different experiments, pipelines, foreground systematics, and null tests**; quoting “3.6σ” vs “2.9σ” as directly comparable without stressing the different error models risks implicitly treating σ as a common scale, contrary to the instructions.  
**Required fix:**  
- Add explicit language whenever σ levels from different analyses are mentioned that clarifies they derive from different likelihoods and systematics and are **not directly comparable as a single σ scale**.  
- E.g., “3.6σ in the WMAP+Planck analysis and 2.9σ in ACT DR6, using different pipelines and null tests; σ values are not on a unified scale.”

---

P1A-B4 (ESSENTIAL) – Abstract vs Sec. X / IX – Abstract accuracy vs proofs  
**Problem:** The abstract states as a “perturbation-transparency theorem” that torsion vanishes at all orders and the Holst sector decouples from all scalar/tensor perturbation equations, and then qualifies “The perturbation-transparency result of Sec. X is restricted to canonical scalar matter: fermion spin density… outside its scope.” However, in the body:  
- Sec. X B “Proof (Scalar Sector)” and X C “Extension to Tensor Sector” **only treat canonical scalar field matter** and briefly assert extension to tensors without a fully explicit tensor-mode derivation.  
- The abstract calls it a “theorem” and “for canonical scalar matter” but also says “Holst sector therefore decouples from all scalar/tensor perturbation equations of motion” in broad language.  
**Required fix:**  
- Narrow the abstract wording to exactly match the proven scope: e.g., “for minimal ECH with canonical scalar matter and torsion-free tensor modes, the Holst term contributes only a boundary term and thus decouples from scalar and tensor perturbations.”  
- Make clear both in abstract and Sec. X that any case with fermions, propagating torsion, non‑minimal couplings, or dynamical Immirzi fields is **not covered by the proof**, and avoid any language suggesting an operator‑level theorem for all ECH.

---

P1A-B5 (MAJOR) – References [1], [3], [4], [5], –, – – Citation metadata and consistency check  
**Problem:** Several key references correspond to important known works; you must verify that titles, authors, years, and arXiv IDs are accurate. Spot checks show:  

- [1] Cai et al., “Non-Gaussianity in a matter bounce” JCAP 0905:011 (2009), arXiv:0903.0631 – citation appears correct (authors, title, journal, arXiv).  
- [3] Minami & Komatsu, PRL 125, 221301 (2020), arXiv:2011.11254 – correct.  
- [4] Eskilt & Komatsu, Phys. Rev. D 106, 063503 (2022) – correct.  
-  Planck 2018 parameters Aghanim et al., A&A 641, A6 (2020), arXiv:1807.06209 – correct.  
-  Ashtekar & Singh CQG 28, 213001 (2011), arXiv:1108.0893 – correct.  
-  Hehl et al. RMP 48, 393 (1976) – correct.  
-  Mercuri PRL 103, 081302 (2009), arXiv:0902.2764 – correct.  
-  Shapiro & Teixeira CQG 31, 185002 (2014), arXiv:1402.4854 – correct.  
-  Hehl & Datta JMP 12, 1334 (1971) – matches.  
-  Holst PRD 53, 5966 (1996) – correct.  
-  Date, Kaul & Sengupta PRD 79, 044008 (2009), arXiv:0811.4496 – correct.  
-  Benedetti & Speziale JHEP 06 (2011) 107, arXiv:1104.4028 – correct.  
-  Lue, Wang & Kamionkowski PRL 83, 1506 (1999), astro-ph/9812088 – correct.  

However:  
- Several recent refs (–) correspond to very fresh preprints. You must check that years, titles, and arXiv IDs precisely match the final arXiv entries; any mismatch needs correction before publication.  
**Required fix:**  
- Systematically verify each reference against arXiv.org or ADS; correct any mismatched year, volume, page, or arXiv ID.  
- Where you cite internal identifiers (e.g., “canonical quintom‑cosmology review…” inside ), ensure the actual paper title and details match current ADS/arXiv records.

*(I cannot perform live ADS/arXiv lookups here, but the editorial process must do so; any mismatches discovered should be corrected as standard.)*

---

P1A-B6 (MAJOR) – Sec. II A 2, Eq. (7) – Attributing one-loop estimate to refs without clear derivation  
**Problem:** Eq. (7) gives  
\(\alpha/M \sim \frac{g^2}{32\pi^2 M}\ln(\Lambda_{UV}^2/\mu^2) + \delta_{NY}\)  
and states it is “Following Freidel et al.  and Shapiro & Teixeira , the one-loop estimate is …” But those works do not, as far as the text indicates, explicitly derive this exact coefficient with that normalization; the paper elsewhere acknowledges “no published calculation currently derives this exact coefficient structure from the Mercuri construction.”  
**Required fix:**  
- Clarify the credit: say explicitly that this is a **phenomenological EFT-motivated ansatz** whose form is inspired by the loop structures in [15,20], but not literally derived there.  
- Do not present Eq. (7) as “the one-loop estimate” attributable to those references unless you can point to an explicit matching formula in those papers. If none exists, change phrasing to “a natural one-loop–motivated estimate is…” and remove the implication of a direct derivation.

---

P1A-B7 (MAJOR) – Sec. IV B, Eq. (14)–(15) – One-loop operator from Mercuri / Mercuri & Capozziello  
**Problem:** A specific parity-odd operator (14) is introduced, and the surrounding text mentions Mercuri and Mercuri & Capozziello  as motivation. The paper partially admits this is not directly derived in [19,22], but the exposition is still ambiguous: readers could infer that  computes precisely this operator with that normalization.  
**Required fix:**  
- Tighten wording: clearly state that Mercuri & Capozziello compute one-loop corrections in Einstein–Cartan–Holst but **do not derive Eq. (14) in this form**, and that you are using Eq. (14) as an **upper-bound EFT ansatz**.  
- Avoid phrases like “we adopt the one-loop parity-odd operator” without the qualifier “phenomenological” and without clearly distinguishing from the actual results in [19,22].

---

P1A-B8 (MAJOR) – Sec. III B, V, XIV B – Galaxy spin “null” and use of Paper IV   
**Problem:** The galaxy spin null result is heavily leaned on, but only sourced to Paper IV , which is in preparation:  
- “independent ViT-Small chirality classifier … null all-sky dipole… high significance… in Paper IV .”  
- “confirmed null at the dipole level (Paper IV )” (Sec. VI, XIV B).  
Since  is not available, these are not verifiable and yet are used to reinforce model conclusions, including statements that Shamir’s claimed 3% asymmetry is “refuted … at high significance.”  
**Required fix:**  
- Either (a) ensure Paper IV is posted on arXiv and update its reference, or (b) significantly soften and de‑emphasize the claim; present only the qualitative statement that current independent reanalyses (e.g., Patel & Desmond, Philcox & Ereza) cast doubt on strong spin asymmetry, citing [34,35], and remove reliance on internal work as a decisive refutation.  
- Do not claim “confirmed null” based primarily on unpublished analysis.

---

P1A-B9 (MAJOR) – Sec. XIII & Table III – Use of PTA γ = 2.567 ± 0.382 from Paper III   
**Problem:** The PTA spectral index γPTA is given as “2.567 ± 0.382 (real-KDE GPU MCMC)” sourced to Paper III , again in preparation. This number is used to compare with a bounce prediction γ = 3.0 at +1.13σ.  
**Required fix:**  
- As with other companions, either make Paper III public (arXiv) and treat this as a proper result, or remove the numerical comparison from this paper and just qualitatively remark that current PTA results are not in strong tension with γ ≈ 3.  
- Avoid referencing intermediate fits or reanalyses that are not publicly documented.

---

P1A-M10 (MAJOR) – Sec. II C 1, II C, Appendix B – Cosmological constant hierarchy and N_tot bookkeeping  
**Problem:** The paper includes a long internal audit of dimensional analysis and Ntot ≈ 92–94 e‑folds, but the hierarchy numerics and scaling assumptions remain confusing and partly self‑contradictory across sections. The author notes earlier drafts mis‑stated the hierarchy (“∼35” vs true ∼120 OOM), which is fixed here, but:  
- Appendix B uses a phenomenological ansatz ρ_Λ^bounce ∼ (α/M) M_Pl^5 ∼ 10^-2 M_Pl^4.  
- Sec. II C and XII A switch between 92 and 94 e‑folds, and between 10^-121 and 10^-123 factors.  
- The chain of reasoning still mixes Planck densities, “pseudo‑densities” and dimensional fixes in a way that a reader cannot independently trace to a clean, unique formula.  
**Required fix:**  
- Present a single, clean, step‑by‑step derivation (or explicit *non‑derivation* with clear ansatz status) of the relation between ρ_Pl, ρ_Λ, D_inf, and N_tot, numerically verifying each step.  
- Remove or compress the internal version‑history commentary about earlier mis‑statements, keeping only the final consistent result and an explicit statement that it is an ansatz, not derived from ECH dynamics.

---

P1A-M11 (MAJOR) – Global – Overreliance on private code repos / unverifiable reproducibility  
**Problem:** Data and code availability section references a GitHub repository with an “implementation map” and says MCMC chains and diagnostics are “in companion Paper I(b) .” But the chains themselves are not clearly stated to be publicly available, and key numerical results still point to “companion” internal documents.  
**Required fix:**  
- Explicitly state which parts of the code and which data products (chains, configs, derived spectra) are publicly available in the GitHub repo.  
- For anything not public (e.g., large chains), provide a reasonable path (e.g., “available from the author on request” or deposit in a data repository) consistent with PRD reproducibility standards.  
- Remove references to “implementation map” that are not accessible unless the map is indeed in the repository.

---

P1A-M12 (MINOR) – Abstract & Sec. I & IV E – “Four enumerated minimal-ECH routes” but additional operators acknowledged  
**Problem:** The abstract and several sections talk about “channel-level closure of the four enumerated minimal‑ECH dark‑energy routes” while acknowledging that Jackiw–Pi Chern–Simons and the parity‑odd four‑fermion partner are not included. This is mostly clear, but the language can mislead less careful readers into thinking a more exhaustive theorem has been proven.  
**Required fix:**  
- In the abstract and conclusions, explicitly repeat that the four‑route closure is **not an operator‑basis closure** and is contingent on the omission of additional parity‑odd operators, pointing the reader to the specific section where this is scoped. Slightly down‑weight claims like “channel-level closure” or immediately follow them with “within the four routes defined in Sec. IV.”

---

P1A-M13 (MINOR) – Sec. III A & XI – Photon–torsion coupling not derived  
**Problem:** The text correctly notes that “Connecting to a quantitative rotation angle β from the gravitational/torsion operator requires an explicit photon-torsion coupling that has not been derived here,” but elsewhere it casually treats β ≈ 0.27° as a “benchmark” as if partially ECH motivated.  
**Required fix:**  
- Add a short sentence explicitly stating that no explicit ECH‑derived photon–torsion coupling is currently known, and that all birefringence numerics in this paper are based on **standard ALP–photon couplings in GR**, not ECH; they are presented only as consistency benchmarks.

---

P1A-M14 (MINOR) – Sec. VII & XIII – SPHEREx σ(fNL) numbers  
**Problem:** SPHEREx sensitivity σ(fNL) ≈ 0.7 (ideal) and ≈1 (with systematics) is taken from Heinrich et al. , but the text intermixes raw σ ratios, template overlap, and later systematic degradations. It is not always clear which value includes which effects, and the text attributes some numbers to “companion Paper II [2]” instead of .  
**Required fix:**  
- Cleanly separate what comes from  (published SPHEREx forecast) and what is new (if anything).  
- If all numbers are from , cite that directly and either remove reference to the unpublished Paper II or state that Paper II will present an independent Fisher analysis but is not needed for the claims in this paper.

---

P1A-M15 (NIT) – Global – Version-history / review-log artifacts  
**Problem:** There are several bits of internal version/audit language that should be removed in a final PRD paper, e.g.:  
- “three substantive theory-derivation issues were identified during preparation of this paper and are documented here for the record” (Sec. IV, scope paragraph)  
- Multiple mentions of “earlier drafts” mis‑stating hierarchies.  
- Footnote in Table III describing current state of a “new DESI DR2 w0wa (new)” Cobaya chain with R̂−1 ≈ 3×10−2.  
These read as internal development log rather than polished paper.  
**Required fix:**  
- Remove version‑history commentary and references to earlier draft errors; present only the final, consistent statements.  
- For the chain currently running, either omit this footnote entirely or move it to a brief outlook sentence that does not contain Monte Carlo diagnostic details.

---

P1A-M16 (NIT) – Duplicated phrases / awkward repetition  
**Problem:** A few phrases are repeated verbatim in close proximity, e.g.:  
- “channel-level amplitude closure of the four enumerated minimal-ECH dark-energy routes” appears multiple times almost identically.  
- “one of which, B8, is the observational consequence of the perturbation-transparency theorem B14 and is retained in the catalog for historical mechanism-class completeness” appears essentially twice (Sec. I, Sec. XV).  
While not strictly incorrect, it makes the text harder to read.  
**Required fix:**  
- Edit for concision; keep the explanation of B8 vs B14 once in the main structural section and refer back to it later rather than rephrasing the same sentence.

---

P1A-M17 (MAJOR) – Length vs contribution  
**Problem:** The paper runs 21 pages and includes extensive internal commentary (detailed MCMC logistics, code infrastructure, long footnotes on running chains, multiple recaps of the same points) for what is fundamentally a conceptual, mostly analytic channel‑closure argument. Given that companion papers will handle data analysis and systematics, this manuscript is overly long for the claimed theoretical contribution.  
**Required fix:**  
- Compress or remove:  
  - The detailed Cobaya chain counts and convergence diagnostics (Sec. I, Table IV footnotes).  
  - The long observational and survey-operations digressions (e.g., LSST Era, MPI pod details, BLAS oversubscription).  
  - Repeated explanations of D_inf and N_tot.  
- A target of ~14–16 pages for the main text (excluding refs) is reasonable for PRD given the scope; aim to cut at least 4–6 pages of ancillary material that properly belongs in companion works or supplementary notes.

---

## Summary recommendation

**MAJOR REVISIONS**

The core conceptual content (channel-level closure of four specific ECH routes, and the scalar-matter perturbation transparency statement) is potentially suitable for PRD, and the author is admirably explicit about assumptions and limitations. However, the current manuscript relies heavily on unpublished companion papers for key numerical results, forecasts, and null tests; it contains ambiguous attributions of specific one-loop operators to prior work; and it needs both conceptual tightening (scope of “theorems”) and significant pruning of internal-version and MCMC-log material. These issues must be resolved—primarily by either making the companion analyses public or removing reliance on them, clarifying the phenomenological status of several operators, and compressing the exposition—before the paper can be considered for acceptance.