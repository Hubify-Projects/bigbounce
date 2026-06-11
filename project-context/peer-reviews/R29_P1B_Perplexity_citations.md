# P1B R29 — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.55.pdf` md5=b776a111 pages=17
**Input format**: TEXT + web search + pass-2 self-critique (12256 chars)
**Wall time**: 59.0s

---

I cannot produce a defensible referee report from the material provided because I do **not** have the paper PDF itself, only extracted text. I can still give a limited citation-forensics audit of the bibliography and the internal consistency of the rendered text you pasted.

**Bibliography / citation-forensics findings**

- **P1B-M1** — **Ref. [4] arXiv ID is future-dated and therefore invalid in a June 10, 2026 paper.** The reference lists “arXiv preprint (2025), arXiv:2509.13654,” which is dated September 2025, later than the paper’s stated date and must not be cited as if already published at that point.[4] **Required fix:** replace with a citation to the actual published/posted version available on the manuscript date, or state clearly that it is a future-appearing placeholder if this is a draft artifact.

- **P1B-M2** — **Ref. [1] is bibliographically incomplete.** It is listed as “(2026), companion paper, posted concurrently on arXiv” with no title, journal venue, or arXiv ID.[1] **Required fix:** provide full bibliographic metadata and arXiv identifier.

- **P1B-M3** — **Ref. [4] is internally inconsistent with its own description in the body.** The body says the cited published result is “PRD 106:063503, arXiv:2205.13962,” while the bibliography instead cites a 2025 arXiv preprint with a different ID.[5][4] **Required fix:** align the bibliography entry with the publication actually used in the text.

- **P1B-M4** — **Ref.  appears future-dated relative to the manuscript.** The bibliography gives “(2025), arXiv:2507.04265,” which is July 2025 and may or may not have existed by the manuscript date; the paper treats it as an established citation without noting preprint status. **Required fix:** verify existence and availability on the manuscript date, and label as preprint if appropriate.

- **P1B-M5** — **Ref.  future-dated / publication year mismatch risk.** The entry says “Physical Review D 112, 083515 (2025), arXiv:2503.14738,” which may be plausible but must be verified against arXiv and PRD metadata; the manuscript also uses it as an already-published reference. **Required fix:** confirm venue/year/volume/page against the final published record.

- **P1B-M6** — **Ref. [3] citation metadata is likely fused/abbreviated and needs verification.** The entry says “reports beta = 0.30 +/- 0.11 deg from Planck NPIPE (PR4)” and gives arXiv:2201.07682, but the body elsewhere cites PR4/NPIPE as a published Planck result with that same value.[3] **Required fix:** ensure title, author list, journal, and the specific quoted statistic exactly match the source.

- **P1B-M7** — **Ref. [5] is cited for a statistic that is repeated inconsistently in the body.** The abstract says 3.6σ for β = 0.342° ± 0.094°, and later the body uses the same value; that is self-consistent numerically, but the bibliography should be checked against the original paper’s abstract/tables for exactness.[5] **Required fix:** confirm the citation metadata and whether the quoted significance is directly reported or computed.

- **P1B-M8** — **Several references are “companion paper, posted concurrently on arXiv” placeholders rather than complete bibliographic entries.** This applies to [1], [6], [7], and .[1][6][7] **Required fix:** replace placeholders with complete metadata or explicitly mark them as unpublished preprints with arXiv IDs.

**Internal-consistency findings in the rendered text**

- **P1B-E1** — **The paper is not self-contained about the “Paper I(a)” results it depends on.** It repeatedly imports claims such as “14 independent structural constraints,” “perturbation-transparency theorem,” and the “13 logically-independent structural barriers” from another paper, but those results are not stated here beyond summaries.[1] **Required fix:** either include enough detail for a standalone reader or clearly bracket these as external assumptions, not load-bearing evidence in this companion.

- **P1B-M9** — **The manuscript uses several sigma comparisons side-by-side that are explicitly said to be “not directly comparable,” but the qualification is not always carried through every juxtaposition.** This appears in the abstract and later in the NaMaster and ALP sections when MC recovery significances are compared with sky-detection significances.[3][4][5] **Required fix:** attach an explicit “not directly comparable” note at each juxtaposition of pipeline-recovery SNR and sky-measurement significance.

- **P1B-M10** — **The paper mixes multiple null procedures and tail significances without always restating the statistical basis.** Examples include “marginal-tail +4.3σ,” “3.9σ” inverse-variance β combination, and “9σ statistical significance against β = 0,” which are not comparable quantities.[3][4][5] **Required fix:** state the null procedure and effect size every time a sigma headline appears.

- **P1B-M11** — **The body contains an explicit version-history / draft-language artifact in a footnote.** Footnote 3 says “quoted in an earlier draft,” and footnote 1 says “the 119,617 figure in Fig. 1 reflects additional getdist effective-sample weight-based thinning,” while the footnote also compares against a “prior draft.” These are draft-history markers in the manuscript body and should be removed or quarantined.[1] **Required fix:** delete version-history language from the paper text.

- **P1B-M12** — **The body contains a direct self-contradiction in the sample-count accounting.** The text says the full-tension chain has 176,240 raw samples, then footnote 1 gives 30% burn-in and several conflicting post-burn-in counts, including 123,368, 123,129, and 119,617, while also stating a combined total of 216,432 after burn-in from two chains.[1] **Required fix:** provide one consistent chain-accounting table and use it everywhere.

- **P1B-M13** — **The abstract’s “309,189 frozen samples across two converged dataset combinations” is not backed cleanly by the table labels.** Table I lists 176,240 and 132,949 samples, which do sum to 309,189, but the manuscript also discusses a third Planck-only chain with 114,992 raw samples and R̂−1∼0.05 that is excluded from all tables yet mentioned in the abstract-adjacent prose.[1] **Required fix:** explicitly state in the abstract that the headline count excludes the third chain and that it is not part of any reported summary.

- **P1B-M14** — **The NaMaster “systematic floor” is an empirical pipeline-recovery bias, but the paper later phrases it in ways that could be mistaken for an observational uncertainty.** The text correctly says it is not a sky-measurement systematic, but the prose still uses “systematic floor” without repeating the scope limitation at every use.[3] **Required fix:** keep the “pipeline-only” qualifier whenever the 0.040° floor appears.

- **P1B-M15** — **The claim “The primary sky detection significance is the published Planck/ACT DR6 2.7–2.9σ” is not a single clearly traceable statistic.** It merges multiple published values without specifying exactly which cited paper gives 2.7σ and which gives 2.9σ.[3][4] **Required fix:** attribute each number to a specific paper and measurement.

- **P1B-M16** — **The inverse-variance combination in Eq. (4) is numerically checkable, but the manuscript omits the exact effect-size framing needed for a sigma headline.** The combined value is 0.241° ± 0.061°, but the paper should state the fractional amplitude and note that this ignores correlated systematics.[3][4][5] **Required fix:** add a practical-significance statement and keep the correlation caveat adjacent to the headline.

- **P1B-M17** — **The ALP section uses multiple inconsistent parameterizations of the same quantity without a clean mapping in one place.** It alternates among \(m \sim H_0\), \(m = 2H_0\), \(m \approx 3.9H_0\), and \(m \sim 10\)–\(10^2 H_0\) while also saying the “natural parameter range” is \(m/H_0 \in [1,3]\).[5] **Required fix:** separate the benchmark point, the scan prior, and the posterior-preferred region in one table.

- **P1B-M18** — **The manuscript quotes “\(\beta\) is periodic, \(\beta \equiv \beta + n \times 90^\circ\)” but does not explain the convention sufficiently for a standalone reader.** This matters because the paper uses both signed degrees and wrapped-angle periodicity in different places.[5] **Required fix:** define the convention once, clearly, where first used.

- **P1B-M19** — **The paper asserts “no DESI BAO likelihood enters the frozen ΛCDM+∆Neff chains” while elsewhere discussing DES-Y5 and Pantheon+ in ways that can blur which chain is which.** Table III helps, but the narrative still risks conflating the frozen chains with the iter2 \(w_0w_a\) chain. **Required fix:** add a one-line chain map before Section V.

- **P1B-M20** — **The claim that “CMB-S4 will provide the first precision test (σ(Neff) ∼ 0.03)” is unsupported by a specific citation in the immediate context.** It may be true, but the paper does not trace the forecast to a particular source in the body.[1] **Required fix:** cite the forecast source and state whether the quoted precision is forecasted marginalized uncertainty or instrument sensitivity.

- **P1B-M21** — **The paper claims the ALP result is “not a distinctive ECH prediction,” but then repeatedly motivates it with ECH-specific phrasing.** That is a scope inconsistency: the result is framed as a generic GR+ALP computation, not as a consequence of ECH.[1] **Required fix:** tighten the scope language so the ECH motivation is clearly secondary.

- **P1B-M22** — **The manuscript says the ALP MCMC uses “9,720 total accepted samples across the three committed configurations,” but Appendix C gives 2,160 + 6,840 + 720 = 9,720 only if the three chains are exactly those listed.** The continuous-prior chain of 8,955 accepted samples is separate, and the prose sometimes treats it as part of the same tally.[5] **Required fix:** distinguish the three baseline chains from the additional continuous-prior rerun.

- **P1B-M23** — **The quoted 3.2σ offset in \(M_B\) is not fully conditioned and is correctly acknowledged as such, but the paper still uses it rhetorically as if it were a tension statistic.** The paper itself says it is not properly conditioned, yet the surrounding prose still leans on it. **Required fix:** remove any tension-style wording and keep it purely descriptive.

**Summary recommendation**

## Summary recommendation
**MAJOR REVISIONS**

The manuscript has several serious citation-forensics and internal-consistency problems: incomplete bibliographic metadata, at least one future-dated arXiv citation, multiple draft-history artifacts in the body, inconsistent chain-count bookkeeping, and repeated use of sigma claims without fully maintaining the stated non-comparability caveats. The core scientific narrative may be salvageable, but it is not yet PRD-ready as written because the reference list and quantitative provenance are not clean enough for a rigorous, standalone audit.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B new findings only (building on, not repeating, the earlier report):

---

**A. ARITHMETIC / NUMERICS**

- **P1B-A1** — *Naive two-Gaussian S8 combination mis-quoted and mis‑used as an independent check.*  
  Table I states that combining 0.827 ± 0.010 and 0.776 ± 0.017 gives “0.814 ± 0.009” and that the full‑tension chain value 0.814 ± 0.008 is “consistent … agreement at the 0.01σ level.” But the chain value is partly driven by the DES‑Y3 Gaussian prior itself, so its closeness to the algebraic product is not an independent validation and should not be presented as such.[Table I] **Required fix:** Make clear that the “naive two‑Gaussian” and the chain value are not statistically independent checks; at most, quote the arithmetic and drop the “0.01σ‑agreement” rhetoric.

- **P1B-A2** — *H0–MB “3.2σ” chain-space offset is unconditioned and presented without the relevant correlated σ.*  
  The text computes a 0.156 mag offset in MB−5 log10 h between the Riess anchor and chain mean and divides only by σMB = 0.049 to quote “∼ 3.2σ,” while explicitly admitting it “does not condition on the MB–H0 covariance … nor on the uncertainty of the Pantheon+ constraint itself” and “is therefore not a properly conditioned tension statistic.”[III, MB–H0 joint-posterior offset check] **Required fix:** Either (a) remove the “3.2σ” label altogether, or (b) provide the correctly conditioned significance using the full 2D error ellipse and Pantheon+ uncertainty, clearly separated from the canonical 3.6σ H0-tension figure.

- **P1B-A3** — *wpivot “+2.5σ from −1” is only tail distance; this is not clearly separated from evidential statements.*  
  Table II gives wpivot = −0.952 ± 0.019 and annotates “+2.5σ from −1.”[Table II] While fn. a explains that w0, wa departures are marginal-tail distances not Bayes factors, the table’s “phantom-crossing required” and “+2.5σ” phrasing can be read as a formal exclusion. **Required fix:** In Table II, explicitly tag the “+2.5σ from −1” as *marginal-tail distance only, not a tension or model-preference statistic*, in the same way you did for w0, wa.

- **P1B-A4** — *LiteBIRD “∼9σ statistical significance” for β is not a detection significance in the usual sense and mixes notions of σ.*  
  The text computes 0.27°/0.03° ≈ 9 and labels this “∼9σ statistical significance against the β = 0 null,” but then immediately notes that LiteBIRD alone cannot distinguish 0.27° from the observed 0.342° due to the larger current error bar.[VI, LiteBIRD forecast] This can be misread as a 9σ *future detection claim* rather than a simple SNR scaling. **Required fix:** Rephrase as “would correspond to SNR ≈ 9 for β (under the forecasted σ(β))” and explicitly state this is *not* a full forecast of detection or model discrimination, nor does it include systematics.

- **P1B-A5** — *S8 tension numbers are quoted without symmetric treatment of the “2.5σ” value.*  
  The iter2 chain S8 = 0.8245 ± 0.0089 differs from DES‑Y3 0.776 ± 0.017 by Δ = 0.0485; the combined σ is ≈ 0.019, giving ≈ 2.6σ, not “2.5σ.”[Table II, Caveats (d)] The difference is small but you present 2.6σ elsewhere (for Planck+BAO+SN vs DES‑Y3 in Table I notes) and “2.5σ” here; this looks like a leftover from an earlier iteration. **Required fix:** Recompute once from the final numbers and use a single rounded value (e.g. “2.6σ”) consistently.

---

**B. FIGURE‑CAPTION VS BODY‑CLAIM**

- **P1B-B1** — *Fig. 3 caption vs text: σβ at fsky=0.32 and the “quoted in an earlier draft” language.*  
  The caption states that “a dedicated 500‑MC rerun (fn. 3) measures σβ = 0.046° at this point” (fsky = 0.32).[Fig. 3] Footnote 3, however, still contains “quoted in an earlier draft” and mixes numbers (≈ 0.047°, ≈ 5) that were superseded by the rerun.[fn. 3] **Required fix:** Remove the draft-history phrase from fn. 3 and align all σβ and SNR values for fsky=0.32 with the final rerun numbers used in Fig. 3.

---

**C. EQUATION / DIMENSIONAL CONSISTENCY**

- **P1B-C1** — *Definition of S8 is textual only; the paper never explicitly spells out the dimensionless combination it relies on.*  
  Table I says “S8 ≡ σ8(Ωm/0.3)1/2, computed as a Cobaya derived parameter with exactly this definition,” but the equation is never displayed with units explained.[Table I] For a verification companion that leans heavily on S8, this is under-documented. **Required fix:** Add a displayed equation explicitly noting that σ8 and Ωm are dimensionless so S8 is dimensionless, and tie that to the DES‑Y3 definition you compare against.

- **P1B-C2** — *CaγΔϕ/fa ≈ 10.3 derivation is not made dimensionally explicit in-text.*  
  The paper uses β = (αEM/4π)Caγ(Δϕ/fa) and then states “β = 0.342° (5.97×10−3 rad)… αEM/(4π)=5.8×10−4, giving Caγ Δϕ/fa ≈ 10.3,” but never explicitly writes this intermediate equation.[VI, MCMC parameter estimation] A reader has to reconstruct the step. **Required fix:** Insert the displayed relation  
  \[
  C_{a\gamma}\frac{\Delta\phi}{f_a} = \frac{\beta}{\alpha_{\rm EM}/(4\pi)}
  \]  
  once, explicitly noting that Δϕ/fa is dimensionless and that β is in radians.

---

**D. INTERNAL CROSS‑REFERENCES**

- **P1B-D1** — *Chain mapping between Abstract, Sec. III, Sec. V A, Table III and Conclusions is still easy to mis-follow.*  
  The abstract, Sec. III, Sec. V A, Table III, and Conclusions all refer to “two frozen dataset combinations”, the Planck‑only accumulating chain, and the DESI DR2 iter2 chain in slightly different words.[Abstract][III][V A][Table III][VII] Your earlier caveat that DESI does not enter the frozen ΛCDM+ΔNeff chains is correct, but the reader has to chase multiple sections to realize that (i) DESI only appears in the w0wa iter2 chain, and (ii) the Planck‑only and Planck+BAO chains in Table III contribute to no headline number. **Required fix:** Insert a one‑paragraph “chain map” near the start of Sec. III or V A that explicitly lists which chains feed which tables and which are *never* used in any abstract or conclusion headline.

- **P1B-D2** — *Appendix C chain labels vs text labels could be misaligned for non-experts.*  
  The main text refers to “run1 full”, “run2 extended”, and “c5 continuous” without a direct pointer to the exact filenames/paths in Appendix C; Appendix C uses these names but the mapping relies on the reader understanding the local directory structure.[VI][App. C] **Required fix:** Add a one‑line mapping table in Appendix C linking the textual labels (“fixed‑Caγ fit”, “extended Caγ prior”, “continuous prior”) to the exact on‑disk chain names/paths.

---

**E. NULL PROCEDURE COMPARABILITY**

(Many such issues were already captured; only *new* juxtapositions are listed.)

- **P1B-E2** — *Abstract and Sec. IV jointly juxtapose three incompatible σ notions without carrying all caveats forward.*  
  Across the abstract and Sec. IV you place side‑by‑side:  
  – the published 3.6σ Eskilt–Komatsu sky detection,[Abstract][IV]  
  – the “pipeline-recovery SNR figures (e.g. 20.32, 25.71)” which are matched‑template SNR, not sky significances,[fn. 3]  
  – and the LiteBIRD “∼9σ” forecast for β.[VI]  
  Although each is locally explained, the abstract’s compressed structure risks readers treating them as comparable “σ” metrics. **Required fix:** In the abstract and in the one place in Sec. VI where the 9σ number appears, add an explicit phrase such as “these σ values are defined on different null procedures and are not directly comparable to each other.”

---

**F. ABSTRACT FAITHFULNESS**

- **P1B-F1** — *“Natural parameter” phrasing in the abstract overstates how generic the ALP region is.*  
  The abstract and Sec. I say “a field with fa ∼ MPl, m ∼ H0 is consistent with … β = 0.342°±0.094° (3.6σ)” and call these “natural parameter” values.[Abstract][I][VI] The body then makes clear that (i) the posterior prefers m ≫ H0 (∼10–10² H0), (ii) θi must be tuned down to ∼0.1 for true spectator status, and (iii) Caγ must be enhanced beyond KSVZ/DFSZ by factors ≳ 9–O(10²).[VI] **Required fix:** In the abstract, temper “natural parameters” to something like “parameters within a broad phenomenological prior range (but requiring both misalignment and coupling tuning as detailed in Sec. VI).”

---

**G. UNSUPPORTED NOVELTY CLAIMS**

- **P1B-G1** — *“CMB-S4 will provide the first precision test (σ(Neff) ∼ 0.03)” lacks a local forecast citation.*  
  The line “CMB-S4 (σ(Neff) ∼ 0.03) will provide the first precision test” is not tied to any specific CMB‑S4 forecast reference in the ΛCDM+ΔNeff section itself.[III, key finding] Only LiteBIRD is later cited for σ(β). **Required fix:** Add an explicit citation to a CMB‑S4 Neff forecast paper and specify whether the 0.03 figure is a marginalized posterior forecast or an instrumental sensitivity estimate.

- **P1B-G2** — *“First precision test” is ambiguous relative to existing Planck-level Neff constraints.*  
  Current Planck constraints already provide σ(Neff) ≈ 0.19–0.20; your text suggests CMB‑S4 provides the “first precision test,” which undercuts the existing Planck precision.[Table I][III] **Required fix:** Rephrase to “a substantially more precise test (forecast σ(Neff) ∼ 0.03), improving by about a factor of six over current Planck constraints,” with citation.

---

**H. UNQUANTIFIED HEDGES**

- **P1B-H1** — *“Quintom signature is unlikely to be reversed” is not quantified.*  
  In discussing the double-counting of overlapping DES‑SN5YR/Pantheon+ supernovae, you state that the bias is “unlikely to be reversed by a rigorous joint-covariance treatment” and that the quintom‑B finding is “therefore unlikely to be reversed,” but you supply no quantitative bound on how much w0, wa might shift under a correct covariance.[II, caveats (e)] **Required fix:** Either add a rough Fisher-level estimate of how much w0, wa would move under a plausible joint covariance, or soften the wording to a purely qualitative caution without implying stability.

---

**I. APPENDIX VS MAIN‑TEXT MISMATCH**

- **P1B-I1** — *Spectator-slice posterior fractions (0.33%, 0.068%, etc.) are stated without uncertainties or cross‑reference to Appendix C.*  
  Sec. VI quotes very small posterior fractions for θi≤0.1 and Ωa≤0.01 subsets, based on 8 955 samples, but the statistical sampling error on such small fractions is not given, and the reader is not pointed to the underlying chain diagnostics in Appendix C.[VI][App. C] **Required fix:** Add either (a) binomial error bars (e.g. 0.33% ± …%) or (b) a pointer to Appendix C noting that these slices are indicative only due to limited sample counts.

---

**J. STALE / VERSION‑DRIFT NUMBERS**

- **P1B-J1** — *Multiple places still carry “earlier draft” language around numeric ranges.*  
  You note that earlier drafts quoted Δϕ/fa ranges “[0.2,1.1]” and “[0.17,0.43]°” which are now superseded by “[0.064,1.19]” and “[0.01,0.48]°,” but the main text still spends space describing the old values and stating “those values do not reproduce from the committed integration and are corrected here.”[V, ALP field evolution][VI, β envelope] For a final PRD submission this reads like internal version-control commentary. **Required fix:** Delete the obsolete numeric ranges from the prose and keep only the final values, perhaps with a single note in Appendix A or C that earlier internal drafts used different ranges that were later corrected.

- **P1B-J2** — *S8 tension narrative mixes 2.6σ and 2.0σ language in a way that looks like leftover wording.*  
  Table I notes that Planck+BAO+SN vs DES‑Y3 is at 2.6σ tension and full‑tension vs DES‑Y3 is at 2.0σ; later text about the iter2 chain’s S8 tension uses 2.5σ.[Table I][II(d)] The uneven rounding suggests these numbers have been updated piecemeal rather than globally recomputed. **Required fix:** Recompute all S8 tension levels from the final quoted means and σ’s and enforce a single rounding convention (e.g. one decimal place) throughout.

---

If you want, I can next go parameter-by-parameter through the key tables (I & II) and the NaMaster / ALP sections with explicit recomputation of every σ, SNR, and ratio, but that will be quite long; I focused here on issues that materially affect how a PRD referee will interpret the robustness and honesty of the quantitative claims.