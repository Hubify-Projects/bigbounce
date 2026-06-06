# P5 auto-2026-06-06_0004pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (12065 chars)
**Wall time**: 70.8s

---

The manuscript cannot be properly vetted for citation forensics or quantitative consistency because what you provided is only the title, abstract, and selected chunks of the main text and references, not the full rendered PRD submission PDF (figures, full equations, all tables, full bibliography). Critical elements required by the instructions (full figure set, all tables, exact equation formatting, page numbers, and the full reference list) are missing.

Given that constraint, I can only audit what is actually present in your pasted text. All findings below should be read as applying to **the text you supplied**, not to the unseen full submission. Many required checks (axes, figure numbers, dimensions, full bibliography integrity) simply cannot be done.

---

### Global assessment

- The work leans heavily on a *companion paper “Paper IV”* that is “in preparation and not yet peer-reviewed” and uses it as a load‑bearing source for the chirality catalog, the quoted monopole offset, and some numerical expectations. That is a very serious issue for a PRD methods paper: the core dataset and key prior statistics are not traceable to a peer‑reviewed, citable reference.
- Several claims about statistical significance (σ, p‑values, ranges in percentage points) are internally consistent when recomputed from the reported \(n\) and \(f_{\mathrm{CW}}\), but I cannot verify them against any external source (no tables from earlier papers are shown).
- The reference list at the end appears plausible and the arXiv IDs and journal metadata for [1], [2], [5]–, – correspond to real papers with the correct topics; however, I cannot see the *full* bibliography or confirm there are no duplicates or mis‑ordered entries elsewhere.
- There is extensive “version‑history” and “companion paper” language throughout (e.g. “Paper II”, “Paper III”, “Paper IV”, “this campaign”, “Phase 2 sweep”, “P5 headline”). Some of this is acceptable context; some crosses into internal‑project bookkeeping that PRD generally expects to be cleaned up.

Because of these limitations, the findings below are necessarily incomplete. I will still follow your requested format and severity tagging.

---

## Findings

### 1. Dependence on non‑peer‑reviewed “Paper IV”

**ID:** P5‑E1  
**Location:** Abstract (p. 1), §II (p. 2), throughout text  
**Problem:** The paper’s core input—the 8.47M‑galaxy chirality catalog and its monopole offset \(\Delta f_{\mathrm{CW}}\approx -0.0026\)—comes from “Paper IV [3], … in preparation and not yet peer reviewed”. The present paper repeatedly treats this as a *load‑bearing* prior:  

- Abstract: “We cross-match the 8,474,531-galaxy chirality catalog of Paper IV [3] (companion work, not yet peer-reviewed)… The CW fraction shows no environment dependence above the sensitivity floor set by the Paper IV catalog-monopole offset…”  
- §II: “Paper IV [3]… establishes the global mixture… 0.4974 ± 0.000279, … establishes the catalog-wide CW-fraction monopole as a classifier-residual bias (∆fCW ≈ −0.0026)…”  

The PRD standard is that key data products and prior results used as calibration and systematics inputs come from citable, archived sources (peer‑reviewed or at least arXiv‑posted with stable identifiers). Here, the underlying chirality catalog and its quoted statistics are not independently verifiable in the literature.

**Required fix (ESSENTIAL):**

- At minimum, upload “Paper IV” to arXiv with a stable identifier and cite it by arXiv ID, **or** incorporate a self‑contained description of the catalog construction, classifier, training, validation, and the derivation of the monopole offset directly into this manuscript (including enough detail that a referee can reproduce or at least check internal consistency).
- Explicitly demote any claims that rely on non‑archived results to “assumptions” rather than “established results,” and quantify how conclusions change if the Paper‑IV monopole is shifted within plausible systematic bounds.
- Until the chirality catalog is traceable to an archived reference, PRD should not accept this paper.

---

### 2. Ambiguous use of “Paper IV monopole” value

**ID:** P5‑M1  
**Location:** Abstract (p. 1), §II (p. 2), §V, §VI C, §VIII F, elsewhere  
**Problem:** Two different numerical values for the catalog monopole appear, with no clear reconciliation:

- §II: “a ∆fCW ≈ −0.0026 offset from 0.5…”  
- Abstract and multiple sections use “Paper IV catalog-monopole offset of ∼ 0.2 pp”, i.e. 0.002.  
- §VIII F: “the P4 monopole … ∆fCW = −0.0026 … the observed −5.00σ corresponds to ∆fCW ≈ −0.0028, ∼8% larger than the P4 catalog-mean.”

In the abstract, you describe a “sensitivity floor set by … ∼ 0.2 pp,” which is significantly smaller than 0.26–0.28 pp actually used in the calculations. This is confusing and potentially misleading about the true systematic floor.

**Required fix (MAJOR):**

- Choose a single, clearly defined monopole value (or a small, justified range) and use it consistently throughout.  
- In the abstract, replace “∼0.2 pp” with the actual value used in analysis (e.g. 0.26 pp or 0.28 pp) and state that this comes from Paper IV (with a citation that can be checked).  
- Add a short paragraph in §II or §V explaining the numerical difference between −0.0026 and −0.0028 and its impact on the environment‑dependence limits.

---

### 3. Unverifiable internal references “Paper II” and “Paper III”

**ID:** P5‑M2  
**Location:** Abstract robustness paragraph (p. 1–2), §XII B (p. 18)  
**Problem:** The text references additional “companion” works:

- “Paper II [4], Paper III (both companion, not-yet-published works by the same author)…”, and [4] is listed as “companion paper (Paper II), in preparation; manuscript in preparation.”

These are non‑archived works relied upon for interpretive context (“fNL discrimination of bounce vs inflation”), yet cannot be checked. While not load‑bearing for the core environment‑dependence test, the repeated use of internal “Paper II/III” language is not appropriate for a self‑contained PRD article.

**Required fix (MINOR):**

- Remove or substantially downweight these references unless they are on arXiv with stable IDs. If kept, they must be described explicitly as “ongoing work” and non‑essential to the current paper.  
- Avoid internal project numbering (“Paper II”, “Paper III”) in the main text; refer instead to “a separate work on fNL” with clear bibliographic info if available.

---

### 4. Version‑history / internal bookkeeping language

**ID:** P5‑M3  
**Location:** Throughout (Abstract “Phase 2”, §V B “primary/secondary declaration”, “P5 headline”, “this campaign”, “Phase 2 sensitivity sweep”, etc.)  
**Problem:** The manuscript contains internal campaign labels and version‑style language that read like internal project documentation rather than a polished PRD submission, e.g.:

- “Phase 2 sensitivity sweep across nine cells…”  
- “primary vs. secondary analysis paths (pre-registration caveat)”  
- “This is the strongest single residual structure in the paper after the catalog-monopole subtraction; the DESIVAST-anchored primary analysis (§VIII) is constructed to be independent of this residual…”  
- “the primary cross-classifier validation remains the on-DESI DESIVAST re-projection at nDESIVAST_void = 56,981; see there…”  
- “This is a direct single-test demonstration…”  
- Frequent self‑referential “P5 headline,” “this campaign,” etc.

PRD papers must read as unified, final analyses, not as internal analysis logs.

**Required fix (MINOR):**

- Remove “Phase X”, “campaign”, “headline”, “primary/secondary” language or rephrase in standard scientific terms (e.g. “we perform a sensitivity analysis exploring nine values of {R_s, λ_th}…”).  
- Condense and streamline the “garden‑of‑forking‑paths” discussion; a brief, clear statement of choice of primary statistic and robustness checks is enough.

---

### 5. Use of label “P5” and ambiguous self‑identification

**ID:** P5‑N1  
**Location:** §VIII F (“P5 matched-spiral catalog monopole”), §XV title “CONCLUSIONS” mentions “P5 environment-independence claim” indirectly.  
**Problem:** The manuscript appears to refer to itself as “P5” (e.g. “P5 matched-spiral catalog”), but there is no explicit statement early in the paper that this work is “Paper V” in a series. It is easy to confuse “P5” with an internal review tag rather than an official series designation.

**Required fix (NIT):**

- If this is intended to be “Paper V” in a series, state that explicitly once in the introduction and then avoid shorthand “P5” labels elsewhere.  
- Otherwise, remove the “P5” tags entirely.

---

### 6. Non‑standard use of σ and p labels; mixing null procedures

**ID:** P5‑E2  
**Location:** Abstract (p. 1–2), §V, §VI, §VII, §VIII F, §XI  
**Problem:** The paper uses:

- “σfrom half” as a binomial z‑score,  
- “σpred” from the Paper‑IV monopole,  
- permutation p‑values from label shuffle,  
- Bonferroni thresholds,  
- empirical max‑stat nulls,

and often places different σ values side‑by‑side without explicit reminders each time that these σ’s are not directly comparable or not standard Gaussian significances. For example:

- Abstract: “Per‑class CW fractions … and σ values … The negative σ values in filament and cluster track the catalog‑wide ΔfCW … not an environmental signal.”  
- Also in the abstract: “label-shuffle p = 0.372 … |σ|max = 3.94 … below all Bonferroni thresholds … label-shuffle nulls p = 0.61/0.135/0.413.” These are juxtaposed with the “−5σ catalog-level signal”.

The instructions you gave explicitly require that sigma values from different null procedures not be juxtaposed without clear qualification. That condition is not satisfied here.

**Required fix (ESSENTIAL):**

- In every place where you juxtapose:  
  - catalog‑monopole σ (derived from Δf_CW),  
  - per‑bin σfrom half, and  
  - permutation p‑values converted to effective σ thresholds,

  you must explicitly state what each σ refers to and that they are not directly comparable as probabilities. For example: “σfrom half is a binomial z‑score relative to 0.5; σpred is the expected z‑score from the global monopole; neither is a permutation‑based p‑value.”

- In the abstract, add one explicit sentence clarifying that the quoted σ values refer to simple binomial deviations and are compared to permutation‑derived p‑values only as heuristic diagnostics.

---

### 7. EFT toy operator attribution

**ID:** P5‑M4  
**Location:** Appendix A (p. 19)  
**Problem:** The toy operator \( \mathcal{L}_{\text{parity}} \supset g_\phi (\nabla_i \phi)(\nabla_i \rho / \rho_{\text{bg}})(\hat{L}\cdot \hat{z}) \) is said to be “inspired by” Alexander & Yunes [1] and Lue, Wang & Kamionkowski [2], but the text is quite careful in noting that neither paper actually contains this operator. Given PRD’s standards, this is probably acceptable, but the current wording risks readers inferring that this form is standard in the parity‑violating gravity literature.

**Required fix (MINOR):**

- Make the disconnection stronger and shorter. For example: “This form is a purely illustrative parametrization introduced here; it does *not* occur in the specific models of Refs. [1,2]. Those works only motivate the idea that parity‑violating couplings can exist.”  
- Consider moving this to a very short note or deleting the operator entirely; the paper’s main conclusions do not depend on it.

---

### 8. Statistical numbers: internal consistency checks

I recomputed several of the quoted statistics against the numbers given in the text (using straightforward binomial approximations). They are generally internally consistent:

- **Table II filament:** \(n=408{,}187\), quoted \(f_{\rm CW}=0.4980\). Then \(n_{\rm CW}=f n \approx 203{,}261\) matches.  
  \(\sigma_{\text{from half}} = (n_{\rm CW}-0.5n)/\sqrt{0.25 n} \approx -2.6\), consistent with “−2.61σ”.
- **Cluster:** \(n=397{,}505\), \(f_{\rm CW}=0.4963\). Gives σ≈−4.7, consistent with “−4.66σ”.
- **Void:** \(n=428\), \(f_{\rm CW}=0.4836\). Gives σ≈−0.7, consistent with “−0.68σ”.
- **DESIVAST void:** \(n=56{,}981\), \(f_{\rm CW}=0.4964\). Gives σ≈−1.7, matches “−1.71”.

I did not see obvious arithmetic mistakes in the σ’s or ranges; however:

**ID:** P5‑N2  
**Location:** Abstract (p. 1) “counting statistics of ∼ 5 pp (statistical-dominated for V-Web void at n = 428, ∼2σ on the binomial null)”  
**Problem:** For \(n=428\), the 1σ binomial uncertainty on \(f\) is roughly \(\sqrt{0.25/n} \simeq 0.024\) (2.4 percentage points), not 5 pp. 5 pp corresponds to about 2σ, but the text phrases “counting statistics of ∼5 pp” as if it were a 1σ scale.

**Required fix (NIT):**

- Clarify: e.g. “the 1σ counting‑statistics uncertainty is ~2.4 pp, so a 2σ excursion corresponds to ~5 pp.”

---

### 9. Claims of novelty / superlatives

**ID:** P5‑M5  
**Location:** §VIII B, Abstract robustness paragraph  
**Problem:** The manuscript states:

- “This DESIVAST-anchored re-analysis is the largest matched-sample environmental-dependence test of spiral chirality in DESI DR1 to date…”  
- “the cleanest single chirality-in-voids measurement in this paper…”

These are plausible internally (no one else has used DESIVAST + this chirality catalog), but externally they are difficult to verify. Shamir‑type analyses and other catalog‑level chirality studies exist, but not with DESI DR1. The text is careful to add “in DESI DR1” in some places, but not everywhere.

**Required fix (MINOR):**

- Qualify all such claims with the relevant scope and evidence. For instance: “To our knowledge, this is the first DESI DR1 analysis of environment‑stratified spiral chirality and the largest void‑sample test within DESI DR1.”  
- Remove “cleanest single measurement” as a phrase; replace by something like “statistically most constraining among the DESIVAST tests.”

---

### 10. Bibliography: spot‑checked entries

Within the provided text, the following references appear and can be checked:

- [1] Alexander & Yunes, Phys. Rep. 480, 1 (2009), arXiv:0907.2562 – correct title and journal metadata.[5]  
- [2] Lue, Wang, Kamionkowski, Phys. Rev. Lett. 83, 1506 (1999), arXiv:astro-ph/9812088 – correct.[5]  
- [5] Hahn et al. 2007, MNRAS 375, 489, astro-ph/0610280 – correct.  
- [6] Hoffman et al. 2012, MNRAS 425, 2049, arXiv:1201.3367 – correct.  
- [7] Cautun et al. 2014, MNRAS 441, 2923, arXiv:1401.7866 – correct.  
-  Planck 2018 VI, A&A 641, A6 (2020), arXiv:1807.06209 – correct.  
-  Shamir 2022, MNRAS 516, 2281, arXiv:2208.13866 – correct.  
-  Tempel et al. 2014, A&A 566, A1 (2014), arXiv:1402.1350 – correct.  
-  Ullah et al. 2026, arXiv:2604.02463 – a new preprint; the title and authors match your description.  
-  Zapata‑Zuluaga et al. 2026, arXiv:2604.01456 – matches your description of ASTRA.  
-  Rincón et al. 2025, ApJ 982, 38, arXiv:2411.00148 – DESIVAST; matches.

**ID:** P5‑N3  
**Location:** Reference list, [3] and [4]  
**Problem:** [3] and [4] are “companion paper … in preparation; manuscript in preparation” without any arXiv IDs or journal submissions.

**Required fix (ESSENTIAL, as per P5‑E1/M2):**

- These must be replaced with arXiv IDs or removed as formal references and described only descriptively in text.

---

### 11. Length vs. contribution

**ID:** P5‑M6  
**Location:** Entire manuscript  
**Problem:** For a methods–null‑result paper, the text is very long and discursive, with repeated explanations of the same ideas (e.g. primary vs secondary paths, monopole subtraction, garden‑of‑forking‑paths caveats). The core empirical result is relatively simple (null environment‑dependence given a specific chirality catalog and DESI DR1), and could be presented more succinctly.

**Required fix (MAJOR):**

- Condense the manuscript. A reasonable target for PRD might be ~12–15 pages for the main text, with detailed robustness checks and toy EFT mapping moved to appendices or a supplementary document.  
- Focus the main text on: data, cross‑matching, V‑Web and DESIVAST methods, key null results, and one concise discussion section.

---

## Summary recommendation

**MAJOR REVISIONS**

The core numerical analysis appears internally consistent and the topic is potentially interesting, but the paper critically depends on a non‑archived “Paper IV” for its chirality catalog and monopole calibration, uses internal series labels and quasi‑version‑history language inappropriate for a final PRD publication, and mixes several σ and p‑value notions without consistently clarifying their comparability. The manuscript also needs significant tightening in length and style. At minimum, the chirality catalog and its monopole offset must be citable (arXiv) and the σ/p‑value presentation cleaned up before PRD can seriously consider acceptance.

---

## PASS 2 — self-critique findings (what initial review missed)

P5‑E3  
Location: Abstract, headline sentence; §II; §VIII F; throughout where the monopole is quantified  
Problem: The abstract still states that the sensitivity floor is “set by the Paper IV catalog‑monopole offset of ∼ 0.2 pp,” but the body consistently uses \(\Delta f_{\rm CW}=-0.0026\) (0.26 pp) and in §VIII F recomputes the matched‑sample monopole as \(\Delta f_{\rm CW}\approx -0.0028\) (0.28 pp). The σ‑reconciliations in §VIII F explicitly show that the operative monopole for this dataset is 0.26–0.28 pp, not 0.2 pp. The abstract therefore quantitatively understates the true systematic floor and is no longer numerically faithful to the body.  
Required fix (ESSENTIAL):  
- Replace “∼ 0.2 pp” in the abstract with the actual numerical range used in the analysis (e.g. “∼ 0.26–0.28 pp”), and explicitly tie it to the P4/P5 monopole values.  
- Add a brief parenthetical in §II or §VIII F that fixes a single adopted value (e.g. \(-0.0026\)) for quoting the “monopole floor,” noting that the P5 subsample monopole (−0.0028) is an 8% shift but does not qualitatively change any limit.  

---

P5‑E4  
Location: §VI C, projected‑density quintiles; Table III; Fig. 3 text  
Problem (arithmetic / conceptual): The text states that at \(N = 158{,}327\) per quintile the predicted monopole σ is \(|σ_{\rm pred}|=2·|−0.0026|·\sqrt{N}\approx 2.07\). The largest observed deviation is \(|σ_{\rm obs}|=3.94\), and you quote the residual as \(|σ_{\rm obs}-σ_{\rm pred}|\approx 1.87\).[Table III] Algebraically, this “residual” changes sign between quintiles (some bins have σ less negative than the prediction, some more negative), so a signed difference is defensible. But you then treat the absolute difference as if it were a “σ‑distance” between null and data, and compare it directly to the Bonferroni threshold |σ|=3.09 as though it were a standard Gaussian z, while ignoring that the underlying σ’s are binomial z‑scores and that the Paper‑IV monopole itself is uncertain. The result is a hybrid diagnostic that looks like a proper hypothesis test but is not clearly defined as such.  
Required fix (ESSENTIAL):  
- Explicitly define what statistical quantity \(|σ_{\rm obs}-σ_{\rm pred}|\) is intended to represent (e.g. a crude “distance from the monopole‑only prediction,” not itself a z‑score under a well‑specified null).  
- State clearly that you are *not* treating \(|σ_{\rm obs}-σ_{\rm pred}|\) as a Gaussian z with a known variance, and that the Bonferroni threshold is only used heuristically here.  
- Consider adding, at least once, a permutation‑based null for the *residuals* (e.g. label shuffle relative to a fixed monopole) so there is at least one place where the “residual significance” is defined by a genuine sampling distribution.  

---

P5‑M7  
Location: Table VIII vs §VIII D (catalog‑native V2 membership); §VIII C text  
Problem (internal consistency / stale numbers): Table VIII lists for V2‑REVOLVER \(n_{\rm void}=102{,}911\) with \(\sigma_{\rm void}=-0.88\).[Table VIII] In §VIII D you quote, for the catalog‑native GALZONE definition on *the same matched‑spiral subsample*, V2‑REVOLVER \(n_{\rm void}=86{,}276\) with \(\sigma_{\rm void}=-0.24\). The text then compares “catalog‑native vs sphere‑approximation analogues,” but nowhere do you explicitly restate the sphere‑based V2‑REVOLVER numbers (which differ in both n and σ from the catalog‑native ones) in equation or table form. As written, a reader must infer that the 102,911/−0.88 cell in Table VIII is the sphere‑approximation case and that 86,276/−0.24 is the catalog‑native case, but this is not said, and the difference (∼16k galaxies and a factor ∼3 in |σ|) is large enough that it looks like a potential bookkeeping error.  
Required fix (MAJOR):  
- Explicitly label Table VIII as using the *sphere* approximation for V2‑REVOLVER and V2‑VIDE, and make that label unambiguous in the table caption.  
- Add one sentence in §VIII D explicitly cross‑referencing Table VIII: e.g. “Compared to the sphere‑based counts in Table VIII (n=102,911, σ=−0.88), the catalog‑native V2‑REVOLVER void sample (n=86,276, σ=−0.24)…” so the reader understands that these are two different constructions.  
- Optionally, add a small 2×3 table contrasting sphere vs GALZONE for both V2 algorithms so that changes in n and σ do not look like silent inconsistencies.  

---

P5‑M8  
Location: §VIII E, HEALPix maximal‑void stratification; Table IX vs later P4‑monopole discussion  
Problem (stale / unquantified reuse): For the NSIDE=16 maximal‑void stratification you quote σ=−4.75 for the “0 maximal voids per pixel” bin and σ=−2.04 for the “6+” bin.[Table IX] Later you compare the −4.75 cluster‑free region to a P4‑monopole prediction σ_pred≈−3.20 at N=378,511. That is arithmetically fine, but you never recompute or quote a corresponding \(|σ_{\rm obs}-σ_{\rm pred}|\) for the 6+ bin (N=258,060, σ_obs=−2.04, σ_pred≈−2.64). You call the latter “fully null” but only give a ∆σ≈0.60 by eyeballing. This is an example of an unquantified hedge: the “fully null” wording sounds stronger than the actual residual.  
Required fix (MINOR):  
- Quote the explicit \(|σ_{\rm obs}-σ_{\rm pred}|\) for both 0‑void and 6+‑void bins, and rephrase “fully null” to a quantitative statement like “residual +0.60σ, well within 1σ of the monopole prediction.”  
- Avoid qualitative labels (“fully null”) without numerical qualifiers in places where σ values are already being used as precise diagnostics.  

---

P5‑M9  
Location: §VI B, redshift dependence; §XI “Systematics and null tests”  
Problem (equation/units and missing detail): The logistic regression in §VI B is summarized as “z‑coefficient 0.0059 with no significant intercept (0.000652), consistent with no redshift dependence,” but no units or scaling of z are provided (raw redshift? standardized?), and no standard error or z‑statistic for that coefficient is quoted. If z is in raw units, a coefficient of 0.0059 over the observed range 0–3.8 would correspond to a ∼2% shift in f_CW across the full sample, which is not negligible relative to the 0.26–0.28 pp monopole; if it is standardized, the interpretation is different. As written, “no significant intercept” is itself ambiguous (does it mean the intercept CI includes 0.5, or that it is small in magnitude?).  
Required fix (MAJOR):  
- Specify explicitly what scaling of redshift is used in the logistic regression (e.g. z as‑is, or (z−mean)/σ).  
- Report the estimated coefficient for z, its standard error, and the corresponding z‑ or p‑value, so that “no redshift dependence” is backed by a quantitative test.  
- Clarify what “no significant intercept (0.000652)” means. If you mean “intercept term is 0.000652 in log‑odds units,” say so and state whether its 95% CI includes 0 (and hence f_CW=0.5).  

---

P5‑M10  
Location: §VI A; Table II; Fig. 2 caption; §VIII F  
Problem (σ labelling and comparability): In multiple places you label σ values only as “σ” without repeating that they are *σ_from half* binomial z‑scores, and then you immediately discuss σ_pred from the monopole and permutation‑based nulls in the same paragraph. While §V defines σ_from half and σ_pred, later sections often talk about “the cluster signal is −4.7σ” or “−5σ catalog‑level signal” without reminding the reader that these are not permutation σ’s or Gaussian σ’s from a fully specified null. For example, §VIII F calls the monopole “∼9.5σ catalog‑level monopole reported in Paper IV,” then notes that the P5 subsample has −5.00σ; only a very careful reader will remember that these σ’s are computed under different Ns and with different nulls. This is exactly the comparability concern you had flagged in your own instructions.  
Required fix (ESSENTIAL):  
- In any section where σ_from half and σ_pred and permutation‑derived p‑values appear together (e.g. §VI A, §VI C, §VIII F, §X), insert a short clarifying clause such as “all σ values in this paragraph are simple binomial z‑scores relative to either 0.5 or the P4 monopole; permutation p‑values are quoted separately and not converted to σ.”  
- Whenever you call something “−5σ” or “−4.7σ” without a subscript, append “(binomial σ_from half)” at least once per section.  

---

P5‑N4  
Location: §VIII B, first sentence after Table VII  
Problem (stale phrasing vs updated numbers): The text calls the DESIVAST‑anchored re‑analysis “the largest matched‑sample environmental‑dependence test of spiral chirality in DESI DR1 to date,” which is now true essentially by construction, because you are the only group using this chirality catalog with DESI DR1. The immediately following parenthetical “(a null is not positive evidence…)” partially tempers this, but there is no explicit acknowledgment that no other DESI DR1 chirality‑environment analysis exists to compare against. Given you already toned down other novelty claims, this one still reads as a superlative without explicit scope.  
Required fix (NIT):  
- Change to “To our knowledge, this is the first matched‑sample environmental‑dependence test of spiral chirality in DESI DR1 and, within that scope, the largest void‑sample test.”  

---

P5‑N5  
Location: §XI “Systematics and null tests” vs earlier sections; confidence‑threshold sweep  
Problem (stale / unqualified summary): In §XI you summarize systematics tests and say “confidence‑threshold sweep p_max^cls_eq ∈ {0.4,…,0.8} with CW‑fraction flat to within ±0.001.” Earlier sections never show these numbers explicitly, and in the main text you adopt a stricter environment‑label uncertainty filter that adds 21,158 spirals to reach the 812,793 env‑labeled superset in §VIII F. The 0.001 claim is plausible but unsubstantiated in the text, and it implicitly suggests that the move from 791,635 to 812,793 has negligible effect on f_CW at all thresholds, which is stronger than what you actually demonstrate.  
Required fix (NIT):  
- Either (i) add a small table or one line with explicit f_CW values at two extreme thresholds (e.g. 0.4 and 0.8) to back up the “±0.001” statement, or (ii) weaken the language to “changes f_CW at the 10^−3 level” without quoting a specific ±0.001 band.  

---

P5‑N6  
Location: Appendix A, EFT mapping; units and dimensional analysis  
Problem (dimensional clarity): The toy coupling bound \(|g_\phi (\nabla \phi)/H_0| \lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\) mixes a gradient \(\nabla\phi\), a Hubble parameter \(H_0\), and a dimensionless density contrast \(\Delta\rho/\rho_{\rm bg}\), but does not state what dimensions are assigned to \(g_\phi\) or \(\phi\). If \(\phi\) is dimensionless and the Lagrangian term has mass dimension 4, then \(g_\phi\) must carry dimensions of mass squared; if \(\phi\) has mass dimension 1 (canonical scalar), \(g_\phi\) has different units. Without specifying the normalization, the numerical bound is only a scaling relation and the symbol “\(\lesssim\ 10^{-2}\)” risks being misread as a physical limit on a dimensionless coupling.  
Required fix (MINOR):  
- Add one sentence specifying: “Here we treat \(\phi\) as dimensionless and \(g_\phi\) as having dimensions of [X], so the combination \(g_\phi \nabla\phi\) has units of [Y], making the ratio with H₀ dimensionless; this is purely schematic.”  
- Alternatively, explicitly rephrase the bound as a dimensionless scaling: “schematically \(g_\phi \nabla\phi/H_0 \lesssim 10^{-2} / \langle|\Delta\rho/\rho|\rangle\), up to order‑unity EFT normalization factors we do not track here.”  

---

Overall explanation for no further categories:

- I could not systematically check *all* cross‑references, figure axes/units, or every equation’s units because the excerpt lacks the figure images and some equation contexts.  
- Within the provided text, the arithmetic of binomial σ’s, percentage ranges, and sample sizes appears internally consistent (as already partially documented in your own Section 8); apart from the σ_pred and residual interpretive issues flagged above, I did not find clear miscomputations of σ, p, or percentages in the tables or abstract.