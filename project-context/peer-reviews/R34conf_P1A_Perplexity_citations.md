# P1A R34conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.62.pdf` md5=9a1a725b pages=28
**Input format**: TEXT + web search + pass-2 self-critique (18537 chars)
**Wall time**: 110.7s

---

I cannot perform the requested audit to PRD standards because I do not actually have access to the rendered PDF (with real page numbers, figure rendering, equation layout, and the full reference list in its final typeset form). The text you provided is a continuous manuscript dump without page boundaries or the complete bibliography formatting, and my web search access does not let me open “this submission” as a PRD PDF.

Given those constraints, I must be explicit:

- I cannot see page numbers to localize issues.
- I cannot see figures/tables as rendered graphics (axis labels, units, etc.).
- I cannot see the full reference list as formatted in the PDF; I only see the reference stubs embedded in the text.
- I cannot re-run the companion analysis code or inspect the GitHub repo contents.
- I cannot recompute all quoted numerical results that depend on external chains or data files.

Under PRD’s bar and under your instructions, that means I cannot certify the paper’s citation forensics as clean. What I can do is:

- Check the cited external papers that *are* visible in the text (title/author/year/arXiv-ID/venue consistency).
- Flag internal-provenance, “companion in preparation”, and version-history issues that are already evident in the body text you supplied.
- Flag any obviously problematic numerical claims that I can recompute directly from what is printed.
- Identify structural issues that are clear without needing the figures.

Below is a conservative report based only on what I can actually verify. Where I cannot complete a check, I mark the finding as “uncertain but high‑risk” rather than pretending it is clean.

---

## ESSENTIAL findings

### P1A‑E1 – Multiple “companion paper in preparation” as load‑bearing sources  
**Location:** Numerous (Introduction, Paper Organization, Sec. III B, V, VI, VII, X G, XI, XII, XIII, Data & Code Availability); last page explicitly cites [2], [6], ,  as “companion paper, posted concurrently on arXiv” but also repeatedly labels them “in preparation”.  
**Problem:**  
The manuscript repeatedly imports *load‑bearing* numerical results and forecasts from companion works that are:

- described as “in preparation” and not yet on arXiv (e.g. Paper I(b) [6], Paper II [2], Paper IV , Paper III ),
- yet simultaneously claimed to be “posted concurrently on arXiv” in the reference list.  

Examples:

- “a detailed multi-tracer SPHEREx Fisher forecast is presented in a companion work in preparation [2]”; later: “[2] H. Golden, fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, (2026), companion paper, posted concurrently on arXiv.”  
- “ΛCDM+∆Neff MCMC verification, NaMaster pipeline validation, and ALP parameter fitting are documented separately in companion work in preparation [6].”  
- References ,  in the list are also described as “companion paper, posted concurrently on arXiv.”

I cannot verify via search whether those specific arXiv entries actually exist because only very generic placeholder descriptions are given (no arXiv IDs, and the titles are not uniquely identifying). That combination—“in preparation” in body + “posted concurrently” in refs + no arXiv ID—is not acceptable as a citable, reproducible basis in PRD.

**Required fix:**  
- Either (a) post all companion papers and give concrete arXiv IDs in the references, or (b) remove all *load‑bearing* dependence on those works from the PRD submission.  
- Any numerical result that is central to the argument (e.g. Cobaya chain sizes, σ(fNL) forecast, γPTA from “real‑KDE GPU MCMC”, galaxy‑spin null significance) must either be:
  - fully documented and reproducible *within this paper*, or
  - supported by a published, independent source with a proper citation.  
- All occurrences of “in preparation” attached to load‑bearing results must be eliminated. If the result is needed, the companion must already be publicly available (preferably peer‑reviewed, at minimum arXiv) with a stable identifier.

---

### P1A‑E2 – Version‑history and internal‑audit language in the body  
**Location:**  
- Title page: “(Dated: June 11, 2026 PDT — v1A.0.62)”  
- Footnote a under the abstract: “Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion…”  
- Sec. II A 1, footnote 2: “earlier Hehl–Datta-era literature (Sec. IV A)…”  
- Sec. X G: “This figure supersedes the earlier synthetic-Gaussian-likelihood value … used in pre-real-KDE drafts…”  
- Data & Code Availability: “bundle is labelled v1A.0.59-bundle … the bump from v1A.0.58-bundle covers the EXT2 external-round textual-closure edits … present manuscript version v1A.0.61 uses the v1A.0.59-bundle unchanged (text-only restamp).”  

**Problem:**  
PRD manuscripts must not contain internal version‑tracking jargon or peer‑review‑round bookkeeping (“v1A.0.62”, “EXT2 external‑round textual‑closure edits”, “pre‑real‑KDE drafts”). These are internal development artifacts and not scientifically relevant to the reader. Your own instructions explicitly require such language to be flagged.

**Required fix:**  
- Remove *all* version‑history / internal review tags from the scientific narrative and footnotes.  
  - Replace the date line with a simple “(Dated: …)” if PRD style allows.  
  - Rephrase footnotes to avoid “earlier versions of this manuscript” and similar. At most, say “We previously mis‑identified X as Y; here we correct this point” without referring to drafts.  
  - In the Data & Code section, remove bundle internal version numbers that reflect review rounds (“v1A.0.59‑bundle”, “EXT2”, “text‑only restamp”) and state instead a single release tag or DOI that the authors commit to.  

---

### P1A‑E3 – Mixed use of different numerical values for the same external measurements  
**Location:**  
- Abstract: βobs = 0.342° ± 0.094° and β = 0.215° ± 0.074°  
- Sec. III A: repeats the WMAP+Planck and ACT DR6 values with ∼3.6σ and ∼2.9σ  
- Sec. XIII: again β ≈ 0.27° and βobs = 0.342° ± 0.094°, etc.  

**Problem:**  
The quoted birefringence measurements are attributed to Minami & Komatsu and Eskilt & Komatsu and ACT DR6 follow‑up. I can partially verify the first:

- Minami & Komatsu 2020 report β = 0.342° ± 0.070° (stat.) ± 0.037° (syst.), often combined as ≈ 0.34° ± 0.09° in quadrature, which is reasonably consistent with 0.342° ± 0.094°.[3]  

However, the paper attributes **both** WMAP+Planck and a separate “improved” constraint to Eskilt & Komatsu and then quotes a single number 0.342° ± 0.094°. There has been at least one later analysis (Eskilt & Komatsu 2022) with a different central value and uncertainty. Without explicit arXiv identifiers or journal references, I cannot confirm that the specific number and σ you use match the exact paper and data combination you claim. The ACT DR6 number β = 0.215° ± 0.074° is also not traceable without a verifiable citation; the cited author line “Diego‑Palazuelos & Komatsu [5]” must correspond to an actual arXiv entry.

**Required fix:**  
- Provide full, precise citations for each birefringence number: authors, year, journal, arXiv ID, and the exact dataset combination used.  
- Confirm from the cited papers’ abstracts or tables that the central value and σ you quote correspond *exactly* to those works. If you are combining statistical and systematic errors, state the combination method explicitly.  
- If multiple papers by the same authors exist, disambiguate which one you are using (e.g. Minami & Komatsu 2020 PRL vs later analyses).  
- Ensure each β and σ used in your own numerical arguments can be traced to a specific equation or table in the cited work. If not, recalculate or remove.

---

### P1A‑E4 – Use of unpublished DESI DR2 cosmology results as if finalized  
**Location:**  
- Introduction: “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset‑dependent) [9, 10].”  
- Sec. VIII and Sec. XIV D: more discussion of DESI DR2 “evidence for equation‑of‑state crossing at 3.1–4.2σ ”  

**Problem:**  
You cite DESI “DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025)” and claim a 3.1–4.2σ dynamical‑DE signal. I cannot verify the exact quoted significance numbers without being able to open and read that specific DESI DR2 paper. Under PRD standards, any quoted σ must be clearly traceable to a published table or figure in the DESI paper.

**Required fix:**  
- Give the exact DESI paper identifiers (collaboration lead author, year, arXiv ID) and specify which table or figure yields the 3.1–4.2σ range.  
- Make sure “3.1–4.2σ” is not an internal reinterpretation or a combination of multiple lines that is not actually stated in the DESI papers. If it is your own combination, label it explicitly as your derived quantity and show the computation.  
- If DESI DR2 is still under revision or only in preprint, clearly state that status.

---

### P1A‑E5 – Dependence on unverified real‑KDE PTA analysis and “Paper III”  
**Location:**  
- Caption of Fig. 1: “PTA annotation reflects the current real‑KDE reanalysis γPTA = 2.567 ± 0.382 (Sec. X G); γPTA denotes the GWB power‑law spectral index…”  
- Sec. X G and Table IV: quote γPTA = 2.567 ± 0.382 from “real‑KDE GPU MCMC, companion Paper III ”.  
- Reference : “Spectrally Unusual Sources at Scale: A Multi‑Survey Catalog of 378,280 Anomalies and Native‑Trained Novelty Rates from 37.3 Million Sources, (2026), companion paper, posted concurrently on arXiv.”

**Problem:**  
The claimed PTA spectral index result is central to your “bounce discrimination” discussion, but the only source is your own “Paper III”, which is *not* described as a PTA paper in the reference list title, and no arXiv ID is given. I cannot confirm that:

- such an analysis exists on arXiv,
- the value 2.567 ± 0.382 is actually obtained there, or
- the method is sound or even relevant to PTAs.

PRD does not accept critical quantitative claims supported only by unpublished internal analysis.

**Required fix:**  
- Either remove γPTA from this paper’s argument entirely, or  
- Publish the PTA analysis with a clear, relevant title and arXiv ID, and then strictly summarize the result here with a proper citation, without adding new un‑reviewed inferences.  
- Until that is done, all references to “real‑KDE GPU MCMC” and “γPTA = …” must be treated as speculative and should not appear as if they were established literature.

---

### P1A‑E6 – Abstract and body rely on un‑derived phenomenological ansätze without consistently labeling them as such  
**Location:**  
- Abstract: “dark‑energy mapping rests on a phenomenological on‑shell scaling ansatz whose off‑shell mass dimension is +1 rather than +4 (Appendix B); we treat this scaling explicitly as an ansatz, not a derivation.”  
- Sec. II A 2, Eq. (6) and Appendix B: parity‑odd operator with incorrect mass dimension +1; identification ρΛ = Ξ MPl⁴ introduced phenomenologically.  
- Sec. XII A and Appendix B: Ntot ≈ 92 derived from this ansatz.

**Problem:**  
To the authors’ credit, they explicitly acknowledge that their core parity‑odd operator does not have the correct mass dimension for a local EFT term and that the ρΛ mapping is purely phenomenological. However:

- These phenomenological constructions are repeatedly used in the abstract and conclusions as if they were robust structural results (e.g. Ntot ≈ 92, “fine‑tuning reduction from 10^120 to 10^5”).  
- The abstract claims “channel‑level closure” based on 13 barriers, but several key quantitative barriers (notably the Ntot ≈ 92 structural tension argument) rest on this ad‑hoc dimensional fix.

For PRD, any non‑EFT operator must either be replaced by a consistent EFT description or strictly confined to a clearly labeled toy‑model section. Here, the phenomenological operator underlies multiple headline claims.

**Required fix:**  
- In the abstract and all summary sections, *downgrade* any claim that depends on the phenomenological operator to clearly say it is conditional on a toy ansatz that is not an EFT derivation.  
- Alternatively, replace the operator with a truly dimension‑4 operator constructed within a consistent EFT and redo all dimensional and Ntot bookkeeping from that starting point.  
- Remove the “fine‑tuning score comparison” plot and discussion unless it is carefully qualified as schematic and based on an explicitly non‑EFT ansatz.

Given the PRD bar, I would require either a genuine EFT treatment or a much more modest, toy‑model presentation.

---

### P1A‑E7 – Standalone‑reader test failure: key “Foundations” and “Branches” are not self‑contained  
**Location:**  
- Sec. IX: “Through 7 foundation studies (Foundations A–G) and 6 observational research branches (Branches H, J, L, M, N, O)…”.  
- Table II: lists Barriers 1–14 with sources “Found. A, Found. B, … Branch M, Branch N/O, ECH Gates” but gives minimal derivations.  

**Problem:**  
The barrier catalogue is the central structural contribution of the paper, but many of the so‑called foundations (A–G) and branches (H, J, L, M, N, O) are *not actually developed from first principles in this manuscript*. Instead, the text:

- asserts heuristics like “Mass‑coupling lock”, “Topological‑shift duality”, “Liouville conservation”, “Vacuum amplification ceiling” with only partial sketches,  
- frequently points to companion papers for full derivations, or  
- simply states “this is a heuristic closure under explicit assumptions”.

Under your own instruction (standalone‑reader test), a PRD reader must be able to follow the logical chain for each barrier without opening any companion. That is not satisfied here.

**Required fix:**  
- For every barrier that is claimed as “novel” or “ECH‑specific”, provide a self‑contained derivation or at least a clean theorem‑proof style argument in this paper.  
- Where only heuristic reasoning is available, explicitly demote the barrier to “tentative” and do not count it in the claimed “13 logically independent constraints”.  
- Remove references to “Foundations A–G” and “Branches” as if they were separate studies unless all their content is either (a) in this paper, or (b) backed by already published external literature.

---

### P1A‑E8 – Use of σ, p‑values, and “>100 orders of magnitude” without explicit recomputable backing  
**Location:**  
Throughout:  
- “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ”  
- “Galaxy spin asymmetry: confirmed null … Shamir’s 3% claim is disfavored by factor of ∼ 6–12”  
- “Hehl–Datta term underpredicts A₀ by >100 orders of magnitude”  
- “suppressed by at least 10⁻⁵⁸ or 10⁻⁶⁰ relative to βobs”  
- Multiple claims of “∼ 2.6–5σ realistic significance” for SPHEREx etc.

**Problem:**  
Your instructions demand recomputation of every σ and percentage from displayed numbers. In the text I have, many of these σ levels are asserted but:

- the underlying raw numbers (e.g. exact sample sizes and dipole amplitudes for the galaxy spin test; exact Fisher matrix eigenvalues for fNL forecasts) are *not* shown;  
- some are taken from companion works;  
- the order‑of‑magnitude factors (e.g. 10⁻⁶⁹ ρΛ, 10⁻²² overshoot) assume particular unit conversions that are not carefully demonstrated.

I cannot recompute these claims from what is printed. Under PRD standards, such σ‑claims must either be fully reproducible from tables/equations in this paper or explicitly labeled as imported from another published work.

**Required fix:**  
- For each σ, p‑value, “factor of X”, “>Y orders of magnitude” that is used as a *load‑bearing* argument, include the necessary intermediate numbers (e.g. densities, coupling sizes, sample counts) and show the calculation explicitly.  
- If the numbers are borrowed from another published paper, cite that paper and quote their exact result instead of recomputing loosely.  
- Remove or soften any “>100 orders of magnitude” claims that you cannot demonstrate with explicit numbers in this manuscript.

---

### P1A‑E9 – Data & Code Availability section references a GitHub repo but no frozen DOI or hash  
**Location:**  
- Data and Code Availability: “Supplementary materials are at https://github.com/Hubify‑Projects/bigbounce.” and later “bundle is labelled v1A.0.59‑bundle … present manuscript version v1A.0.61 uses the v1A.0.59‑bundle unchanged …”.

**Problem:**  
For reproducibility, PRD increasingly expects a frozen release (DOI or at least a commit hash) corresponding *exactly* to the version used in the paper. Here:

- No specific tag or commit hash is given;  
- The bundle version numbers mix with internal review labels;  
- The text explicitly notes that some bundles are “text-only restamp”, which is confusing for reproducibility.

**Required fix:**  
- Provide a specific Git commit hash or Zenodo DOI for the exact code/data snapshot used for the results in this submission.  
- State explicitly which analyses in the paper can be reproduced from that snapshot.  
- Remove internal labels (v1A.0.59‑bundle, v1A.0.58‑bundle, EXT2) from the main text; retain only a minimal, stable identifier.

---

## MAJOR findings

### P1A‑M1 – Ambiguous / fused citations in the references  
**Location:** Reference list, several entries.  

**Problem:**  
Many references as given in your text are generic or composite and lack essential metadata:

- [1] Cai et al. JCAP 0905, 011, arXiv:0903.0631 – this matches “Non‑Gaussianity in a matter bounce” and is credible.  
- [3] Minami & Komatsu 2020 PRL 125, 221301 – OK.  
- [4] “Improved constraints on cosmic birefringence from the WMAP and Planck cosmic microwave background polarization data, Phys. Rev. D 106, 063503 (2022), arXiv:2205.13962” – likely correct, but I cannot confirm that your βobs matches the exact dataset combination they call their main result.  
- [5] Diego‑Palazuelos & Komatsu (ACT DR6) – an ACT DR6 birefringence analysis is plausible, but I cannot confirm title, year, or arXiv ID; your reference text calls it “arXiv preprint (2025), arXiv:2509.13654” which looks like a *future‑dated* arXiv ID (2509.*), impossible as of mid‑2026. That is a red flag: arXiv:2509.13654 will not exist until 2025‑09 and is not checkable now.  

Using future‑dated arXiv IDs or invented IDs to represent “expected” submissions is not acceptable.

**Required fix:**  
- Replace all future‑dated or placeholder arXiv IDs with real ones. If the paper is not yet on arXiv, do not assign an arXiv ID.  
- For each reference, verify via arXiv or NASA ADS that:
  - the author list and year are correct,  
  - the title matches,  
  - the journal volume/page are correct.  
- If any cited work does not yet exist (e.g., ACT DR6 birefringence might not yet be public), remove or clearly label it as a private communication, and do not use its numbers as firm inputs.

---

### P1A‑M2 – Mixed notation and potential dimensional inconsistencies  
**Location:**  
- Eq. (7), Eq. (10), Eq. (11), Appendix B, Appendix C  

**Problem:**  
The paper acknowledges in Appendix B that the main parity‑odd operator has mass dimension +1. But even within that context, various estimates mix GeV and eV, H0 /MPl, etc., with loosely described “order‑of‑magnitude” reasoning. For example:

- Eq. (15) uses H0 /MPl ∼ 10⁻⁶¹, αem/(4π) ≈ 5 × 10⁻⁴, and (α/M)MPl ∼ 10⁻², and concludes ∆θ_one‑loop/∆θ_obs ∼ 10⁻⁶⁰. That can be more carefully recomputed, but it is not shown step‑by‑step.  
- In Sec. IV D, the scaling ρθ = 2 mθ² β² / (α/M)² is used with mθ = H0, β ≈ 6 × 10⁻³ rad, α/M = 10⁻²¹ GeV⁻¹ to claim ρθ ≈ 1.6 × 10⁻¹⁰ eV⁴ ≈ 6ρΛ. This is plausible, but not explicitly derived in the text and leaves room for mistakes.

Given the centrality of these numbers and PRD standards, dimensional bookkeeping needs to be fully explicit.

**Required fix:**  
- For each “headline” suppression factor (10⁻⁶⁰, 10⁻⁶³, >10²² overshoot, etc.), add a short explicit line showing the numerical substitution and units.  
- Make sure all operator dimensions are consistent across the main text and appendices. The current combination of an off‑shell +1‑dimensional operator plus on‑shell MPl insertions is conceptually muddled; if you keep it, clearly distinguish EFT‑consistent operators from purely phenomenological scalings.

---

### P1A‑M3 – Abstract‑last drift: strength and ordering vs. body  
**Location:** Abstract vs. Secs. IV, IX, XIV.  

**Problem:**  
The abstract states:

- “we report 13 logically‑independent mechanism‑class constraints that collectively constrain the enumerated channels of the minimal‑ECH route…”  
- “The central result is a perturbation‑transparency result… Holst sector therefore decouples from all scalar/tensor perturbation equations of motion (Sec. X).”  
- “The minimal‑ECH four‑route channel set is therefore tightly constrained as both a dark‑energy generator and a matter‑bounce host.”

In the body, however:

- Several barriers are explicitly called “heuristic” or dependent on unproven assumptions (e.g. Barrier 9 Liouville, Barrier 12 vacuum amplification ceiling).  
- The “tightly constrained” matter‑bounce host statement is conditional on a phenomenological Ntot ansatz and on SPHEREx sensitivity that is not yet realized and is imported from a companion forecast.  

This is a classic abstract‑last drift: the abstract reads more definitive (“channel‑level closure… central result… structural tension”) than what is rigorously supported in the body once all caveats are counted.

**Required fix:**  
- In the abstract, explicitly state that several barriers are heuristic, and that the closure is conditional on specific phenomenological ansätze and assumptions (e.g. canonical scalar matter only, no propagating torsion, no non‑minimal couplings).  
- Remove or soften “tightly constrained as a matter‑bounce host” unless you present a fully quantitative transfer function showing erasure of fNL at SPHEREx scales.  
- Clearly separate “proven” results (like the scalar‑sector perturbation‑transparency theorem under minimal assumptions) from “programmatic” or conjectural ones.

---

## MINOR and NIT findings (partial list)

Because I do not see the actual figures, equations, and page layout, I cannot give page‑specific IDs. Below I nonetheless list issues that should be fixed.

### P1A‑N1 – Repeated long phrases and verbosity  
There are multiple very long paragraphs and repeated phrases (“channel‑level amplitude closure”, “phenomenological scaling ansatz”, etc.). This is stylistic, but for PRD a more concise exposition is desirable.

**Fix:** Edit down repetitive wording; consider moving long phenomenological discussions to an appendix.

### P1A‑N2 – Acknowledgment of using “Claude”  
The Acknowledgments explicitly name “Claude (Anthropic)” as an AI assistant.

**Fix (journal‑policy dependent):** Many journals now ask that AI assistance be acknowledged only in a specific, controlled way and not as a co‑analyst. Check PRD policy; if necessary, rephrase to a neutral statement like “We used large‑language models to help with copyediting; all scientific content is the authors’ responsibility.”

---

## Summary recommendation

**Recommendation: REJECT**

This manuscript is ambitious and contains some interesting structural and perturbative arguments, but it falls short of PRD standards on multiple fronts that are fundamental, not cosmetic:

- Core closure claims depend on phenomenological, non‑EFT operators with acknowledged dimensional inconsistencies.  
- Many key numerical results and forecasts are imported from companion papers that are not yet publicly available or are referenced with future‑dated arXiv IDs.  
- Several barriers in the “13 logically independent constraints” catalogue are heuristic and not derived in a self‑contained way.  
- Version‑history language and internal review artifacts are embedded throughout.  
- I cannot, from the text provided, fully verify the accuracy of σ‑levels, p‑values, and external measurement quotes, nor can I recompute many of them from the displayed numbers.

Given the strength of the claims and the complexity of the framework, I see no realistic path to a “minor” revision: a substantial re‑write, a genuine EFT treatment of the parity‑odd sector, and a clean separation between this paper and its companions would be required. I therefore recommend rejection in its present form, with the above issues addressed before resubmission to PRD or another venue.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A‑E10 – Arithmetic inconsistencies and non‑recomputable σ / “orders‑of‑magnitude” claims  
**Scope:** Multiple locations (Abstract, Sec. II C 1, III A–B, IV A–D, VI, XII A, XIV D, Table IV, Appendix B–C).  

**New problems (beyond P1A‑E8):**  

1. **Orders‑of‑magnitude claims not reproducible from printed inputs**  
   - Example: “> 100 orders of magnitude” underprediction for galaxy‑spin asymmetry and “> 100 orders of magnitude” cosmological‑constant mis‑match in several places.  
   - In Sec. IV A, the NJL density estimate gives \(ρ_{\text{NJL}} ≈ 4 × 10^{-80}\,\text{eV}^4 ∼ 10^{-69} ρ_Λ\). This is ~69, not “>100”, orders of magnitude below \(ρ_Λ\), and nothing in the paper shows how this becomes “>100” elsewhere.  
   - Appendix B states the true \(M_{\rm Pl}^4/ρ_Λ\) hierarchy is \(\sim10^{122}\) but other parts of the text speak of “reduction from 10^{120} to 10^5” (Fig. 5 caption, Sec. XII A). There is no explicit demonstration of how “10^5 residual” is obtained from the printed \(N_{\rm tot}\) and scaling factors; it is only qualitatively described.  
   - The ALP overshoot arguments in Sec. IV D claim ∼22–36 orders of magnitude overshoot across the “natural” mass range; the factors \((m_θ/H_0)^2\) are plausible, but the underlying numerical values (H0 in eV, mθ endpoints) are never explicitly tabulated and the order‑of‑magnitude factors are therefore not recomputable from nearby text.  

   **Required fix:** Wherever you use “>X orders of magnitude”, provide explicit intermediate numbers (with units) in the same section so a reader can reproduce the exponent difference directly. Reconcile the 10^120 vs 10^122 vs “>100 OOM” language and adjust the text to the quantitatively correct hierarchy.

2. **Significance ranges “2.6–5σ” for SPHEREx not arithmetically reproducible from given numbers**  
   - Several places (Table I note b, Sec. VII, Fig. 4, Fig. 6, Sec. XIII) quote that SPHEREx will test \(f_{\rm NL}=-35/8\) at “2.6–5σ realistic” or “≳5σ on Stage III/IV timescales”. The only explicit numbers given locally are \(f_{\rm NL} = -4.375\) and “σ(fNL) ≈ 0.7 Fisher‑ideal” and “σ(fNL) ≈ 1.0 after GR‑projection and photo‑z marginalization”. From those:  
     - |fNL|/0.7 ≈ 6.25σ (not “5–5.5σ” as claimed in the footnote),  
     - |fNL|/1.0 = 4.375σ (not “2.6σ” at the low end).  
   - You invoke a “template‑overlap correction r ≈ 0.84” and “further GR‑projection and bϕ degradation,” but no explicit multiplicative factors are given near the σ range; a reader cannot reconstruct how 6.25σ turns into “5–5.5σ optimistic” and further into “2.6–5σ realistic.”  

   **Required fix:** In the main text (not only in the companion Paper II), show the actual chain of degradations as multiplicative factors or effective σ values so that 2.6–5σ can be reproduced numerically from the displayed inputs. Alternatively, remove the numeric range and refer to the companion forecast as the sole source.

3. **DESI “3.1–4.2σ” tension: no explicit arithmetic or reference to a specific table/fit**  
   - The introduction and Sec. XIV D repeatedly state “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset‑dependent).” You never show which combination of DESI DR2 analyses, priors, and models yield the endpoints 3.1 and 4.2.  
   - Since you do not present any of the DESI numbers, covariances, or likelihood ratios in this paper, a reader cannot recompute the quoted σ range from anything printed.  

   **Required fix:** Either (a) explicitly quote, for a specific DESI DR2 paper and model (e.g., their Table number and Δχ² or σ), the numbers that correspond to 3.1 and 4.2σ, or (b) remove the explicit σ range and simply paraphrase DESI’s own stated significance.

4. **Galaxy‑spin “factor of ∼6–12” tension not recomputable**  
   - Sec. III B and Sec. V mention that Shamir’s claimed ∼3% asymmetry is “disfavored by a factor of ∼6–12.” No explicit numbers are given for your ViT‑based dipole amplitude and its uncertainty, nor for the precise Shamir amplitude used as reference. Consequently the “6–12×” factor cannot be checked arithmetically from the text.  

   **Required fix:** Give your measured asymmetry (or upper limit) and uncertainty, and the specific Shamir amplitude (with error bar) you compare to, so that a reader can verify the 6–12 factor from ratios of displayed numbers.

5. **PTA γPTA and “+1.13σ” arithmetic are not reproducible**  
   - Table IV lists γPTA = 2.567 ± 0.382 and states “Bounce γ = 3.0 at +1.13σ.” A reader would naturally compute (3.0 − 2.567)/0.382 ≈ 1.13; however, the actual computation is not shown, and the PTA analysis that produced both γPTA and its σ is entirely in the unpublished Paper III.  
   - Under PRD standards, this is effectively an imported σ from an unpublished analysis; the paper does not expose any of the numbers needed to recompute either γPTA or its uncertainty.  

   **Required fix:** If you retain this statement, either (a) move it to a citation to an arXiv‑posted companion PTA paper where the underlying chain is fully tabulated, or (b) drop the +1.13σ phrasing and simply say that the fiducial γ = 3.0 lies within the 1σ interval of the reanalysis.

---

P1A‑E11 – Figure‑caption vs body‑text mismatches and non‑traceable “forecast panels”  
**Scope:** Fig. 1, Fig. 3, Fig. 4, Fig. 5, Fig. 6.  

1. **Fig. 3 (H(z) panel) vs Sec. II C: no explicit parameters to reproduce the plotted curves**  
   - The caption states that the orange curve corresponds to an “ECH dark‑energy model” with a ΞMPl² term and a negligible rotation term, and the lower panel shows percent deviations ∆H/HΛCDM. However:  
     - The paper never spells out a numerical value for Ξ beyond “Ξ ∼ 10−123” or gives the exact ΩΛ, Ωm, and H0 used to generate that particular curve.  
     - Without these, the percent deviation in the bottom panel cannot be reconstructed to check whether the plotted deviations are consistent with the claimed mechanism.  

   **Required fix:** Specify in the caption or nearby text the concrete parameter choices used in the figure (Ξ, H0, Ωm, possible w(z) assumptions) so a reader can recompute H(z) and ∆H/HΛCDM.

2. **Fig. 5 (“fine‑tuning score comparison”) vs Sec. XII A/B text**  
   - The figure caption asserts “ΛCDM (10^120), quintessence (10^60), f(R) (10^40), spin‑torsion Ntot parameterization (10^5).” The body text later says this “10^5 residual annotation is the score under the Ntot reparameterization; per Sec. XII A this is a reparameterization of the cosmological‑constant problem as sensitivity to Ntot, not a resolution.”  
   - Nowhere do you provide a transparent step‑by‑step computation of “10^5 residual” from Ntot ≈ 92 and the other dimensional factors. As a result, a reader cannot check whether the plotted bar labelled 10^5 is consistent with the quantitative numbers in Appendix B.  

   **Required fix:** Either (a) add an explicit calculation for the “fine‑tuning score” in Sec. XII A and reference it in the figure caption, or (b) remove the numeric labels from Fig. 5 and frame it qualitatively.

3. **Fig. 4 & Fig. 6 vs text on LiteBIRD discrimination**  
   - Fig. 4 shows LiteBIRD detecting β with σ(β) ≈ 0.03° and plots the current βobs points. Sec. XIII and Sec. XV, however, emphasize that LiteBIRD will *not* strongly distinguish β ≈ 0.27° from the current central value 0.342°.  
   - The figure visually suggests a strong “forecast vs measurement” discriminant, but the text rightly notes that the relevant comparison is |βfuture − βobs| normalized by both uncertainties, giving only ~0.7σ. This tension between the graphic’s suggestive layout and the quantitative caveat in the body is easy to miss and can mislead a reader.  

   **Required fix:** Make the discriminant nature explicit in the caption: state that LiteBIRD’s main role is to distinguish β≠0 at high significance, *not* to separate β=0.27° from 0.342°, and that the differential tension is ~0.7σ given current uncertainties.

4. **Fig. 1 GWB PTA annotation vs Sec. X G text**  
   - Fig. 1 annotates “γPTA = 2.567 ± 0.382 (Sec. X G)” as “real‑KDE reanalysis.” Sec. X G describes this as coming from “companion Paper III.” In the present paper, no PTA spectra, noise model parameters, or even the frequency band used are given, so there is no way to verify visually that the figure annotation faithfully reflects the analysis described in the body.  

   **Required fix:** Either (a) remove the γPTA numerical annotation from Fig. 1 and just refer to “a current PTA preferred slope” with a citation, or (b) include enough PTA spectral information in Sec. X G to allow an independent reader to check that the numeric annotation is correct.

---

P1A‑E12 – Dimensional consistency and normalization gaps beyond those already acknowledged  
**Scope:** Sec. II A 2–3, II C 1, IV B–D, VIII, IX A, XIV A, Appendix B–C.  

Beyond your own explicit admission in Appendix B that the main parity‑odd operator has mass dimension +1 off shell, there are additional consistency issues:

1. **Use of \(M_{\rm Pl}\) vs \(M_{\rm Pl}/\sqrt{8π}\) is treated as negligible but sometimes matters at the level you claim**  
   - Sec. II C notes that the reduced vs unreduced Planck mass distinction is “below the order‑of‑magnitude resolution of every estimate in this paper.” For raw “> 60 OOM” arguments this is true; but in places where you claim ∼2% offsets (e.g., Ntot ≈ 92 vs 94, “∼2% reparameterization offset”), a factor of \((8π)^2 ≈ 630\) in MPl^4 is no longer negligible.  
   - You never show explicitly whether the “genuine” 10^122 hierarchy uses reduced or unreduced MPl; the ambiguity is then inherited by all more precise statements (e.g. Ntot ≈ 94 from “genuine MPl^4 to ρΛ”).  

   **Required fix:** Choose one Planck‑mass convention for all quantitative hierarchy statements and demonstrate explicitly how the 10^122 ratio and Ntot ≈ 94 follow under that choice.

2. **Mixing GeV and eV without always carrying the conversion factor**  
   - In Sec. IV B and IV D you move between α/M in GeV−1 and densities in eV^4. For example, in Eq. (15) you treat \(M_{\rm Pl} · (α/M) ∼ 10^{19}\,\text{GeV} × 10^{-21}\,\text{GeV}^{-1} = 10^{-2}\) and then combine this with H0 in “eV” without explicitly converting H0 to GeV.  
   - While the final order‑of‑magnitude (10−60) is likely correct, the intermediate steps omit the 10^9 factor between GeV and eV. Since you are already making O(1–10) statements about “2% offsets” and “10× basis‑conversion gaps,” the reader needs to see the unit conversions written out to verify that no power‑of‑10 mistakes creep in.  

   **Required fix:** Whenever both GeV and eV appear in the same chain of reasoning, carry the 10^9 conversion explicitly at least once and check that the final exponents are unchanged.

3. **Eq. (11) “inflationary suppression” factor and (Treh/MGUT)3/2 prefactor**  
   - Sec. II C 1 explains that the (Treh/MGUT)3/2 factor is obtained from dimensional/phase‑space arguments, not a full Boltzmann integration, and even calls it “aesthetic.” However, in Sec. XII A you then use precisely this factor as part of the argument that the residual fine‑tuning can be “reparameterized” down to 10^5.  
   - Since the exponent “3/2” is not derived, the dimensional consistency of Eq. (11) is arguable: you start from nψ ∼ T³, but then compound “density of states” effects to get a non‑integer power; the text acknowledges that this is an ansatz, but later treats the numerical Ntot ~ 92 as more precise than the ansatz justifies.  

   **Required fix:** Clearly label any use of (Treh/MGUT)3/2 in quantitative claims (especially Ntot and the 10^5 residual) as relying on an un‑derived ansatz, and do not present Ntot ≈ 92 as a 2%‑level structural result.  

4. **Eq. (18) “geff ∼ H0/MPl ∼ 10−61” and t3-scaling**  
   - You define geff ∼ (1/√|t3|) ∼ H0/MPl with t3 ∼ mT−1, and then assert this is a “scaling ansatz.” As written, [t3] and the powers of mass do not resolve cleanly: if t3 ∼ mT−1, then \(√{|t3|} ∼ mT^{-1/2}\), so \(geff ∼ m_T^{1/2}/M_{\rm Pl}\), which is not dimensionless unless you insert an additional mass scale. You note this is only a “scaling ansatz,” but the dimensional mismatch is not addressed explicitly.  

   **Required fix:** Either correct the mass‑dimension bookkeeping for t3 and geff, or remove this equation and describe the argument qualitatively.

---

P1A‑E13 – Internal cross‑references and structural claims that cannot be verified locally  
**Scope:** Sec. I, II A 2–3, IV Scope, IX–XI, XIV D, Table II.  

1. **“13 logically‑independent barriers” vs Table II and text**  
   - You claim “13 logically‑independent constraints (14 historical catalogue entries, with B8 subsumed by B14).” Table II lists exactly that, and the text notes that B8 is an observational consequence of B14.  
   - However, other potential interdependencies are never examined. For example, B1 (mass‑coupling lock), B4 (Planck suppression), B11 (decoupling universality), and B12 (vacuum amplification ceiling) all rely on the same Planck‑suppressed nature of torsion couplings and energy densities. You never provide a crisp “independence” argument that shows why these are not variations of the same suppression mechanism.  

   **Required fix:** Either (a) soften the claim to “13 catalogued constraints, at least some of which are mutually independent,” or (b) give a short independence argument (e.g., a table indicating which barriers rely on distinct physical assumptions) so that the “logically independent” label is justified.

2. **Abstract and Sec. I “7 foundations and 6 branches” vs actual self‑contained development**  
   - The abstract says “Through 7 foundation studies (Foundations A–G) and 6 observational research branches (Branches H, J, L, M, N, O) we report 13 logically‑independent mechanism‑class constraints.” Many of these “foundations/branches” are only sketched heuristically (as you already note in P1A‑E7), but the cross‑reference language (“Found. A,” “Branch M,” etc.) gives the impression of fully developed sub‑studies.  
   - The new point here is that several of these cross‑references circle back to the same underlying arguments in Secs. II–IV. For example, B4 (“Planck suppression”) and the R1 closure both rely on the same nψ²/MPl² estimate; B6 (“attractor‑sensitivity dilemma”) is not used quantitatively anywhere in the closure proofs; B9 (“Liouville conservation”) is explicitly acknowledged as heuristic.  

   **Required fix:** In Sec. IX and the abstract, distinguish barriers that are truly independent, quantitatively used in your closure (B1, B4, B10–12, B14) from those that are philosophical/heuristic, and avoid presenting the latter as equal “studies” without derivations.

---

P1A‑E14 – Abstract and conclusion over‑state the level of quantitative support in the body (abstract faithfulness)  
**Scope:** Abstract, Sec. I, Sec. XV.  

New issues beyond earlier findings:

1. **“Channel‑level closure … at amplitude‑budget granularity” vs what is actually computed**  
   - The abstract, Sec. I, and Sec. XV claim “channel‑level amplitude closure … at amplitude‑budget granularity” for each of the four routes. For several routes (R2, R3, R4), the “amplitude budget” in this paper consists only of order‑of‑magnitude estimates and qualitative suppression arguments, sometimes explicitly labeled as ansätze (e.g., Eq. (16), (Treh/MGUT)3/2).  
   - There are no explicit numerical “budgets” tabulating observational upper limits vs computed contributions per route. In other words, the paper convincingly argues “parametrically far below observable” but does not provide an audit‑style table of amplitudes vs data.  

   **Required fix:** Rephrase “amplitude‑budget granularity” in the abstract/conclusions to something like “order‑of‑magnitude amplitude estimates” unless you add explicit quantitative budgets (e.g., tables listing ρroute/ρΛ or βroute/βobs for each route with all numerical inputs shown).

2. **“We report 13 logically‑independent mechanism‑class constraints that collectively constrain the enumerated channels …”**  
   - In the body, you already admit that some barriers (e.g. B9, B12) are heuristic or ceiling‑type and are not used as primary closure arguments. The abstract, however, presents the “13 logically‑independent” set as if each is on an equal quantitative footing.  

   **Required fix:** Make explicit in the abstract that some barriers are heuristic or schematic, and that the strict closure of R1–R4 relies on a subset of these plus the perturbation‑transparency theorem.

---

P1A‑M3 – Additional stale / inconsistent numbers and wording  
**Scope:** Sec. II A 3, II B, Sec. I, Appendix B, references.  

1. **γSU(2) ≈ 0.274 “scheme range ∼ 0.020” vs statements about not propagating this as statistical error**  
   - Appendix B and Table IV call the ±0.020 spread an “effective range only and not propagated as a statistical error.” Elsewhere, you refer to this as a “scheme range ∼0.020.” This is internally consistent qualitatively, but the way γ is carried into the “area gap” and ρcrit estimates suggests you are using one fixed value (0.274) while also talking about a “0.27–0.41 ρPl” range for ρcrit.  
   - Without explicit propagation, it is impossible for a reader to see which of your quantitative statements (e.g. ΩGW ceiling in B12) are evaluated at ρcrit = 0.27 ρPl vs 0.41 ρPl, and whether the “0.07–0.17” range in Eq. (20) really follows from the γ range quoted.  

   **Required fix:** Where you quote ranges (e.g. ρcrit/ρPl ≃ 0.27–0.41 leading to ΩGW ≲ 0.07–0.17), show one explicit mapping from γ→ρcrit→ΩGW so a reader can see that the endpoints are consistent with the quoted γ values.

2. **“DESI 2024–2025 BAO results” phrasing vs reference years**  
   - The intro repeatedly refers to “DESI 2024–2025 BAO results,” but the reference  is “Physical Review D 112, 083515 (2025)” with arXiv:2503.14738. This is not strictly wrong, but the phrasing could mislead about whether you are citing a finalized DR2 paper or an evolving set of internal results.  

   **Required fix:** Make clear in the introduction that your 3.1–4.2σ statements refer to the *published* PRD DR2 paper, and avoid “2024–2025” phrasing that suggests a moving target unless you explicitly separate 2024 preprint and 2025 journal versions.

---

If you want, I can next walk through a specific subset—e.g. every σ in the abstract and conclusions—and give suggested replacement numbers/text that are numerically consistent with the printed inputs.