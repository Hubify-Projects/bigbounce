# P4 2026-06-04_1733pt — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 43.3s

---

P4 makes extensive, technically careful use of the prior literature, but there are still a few citation-level issues and some residual internal-artifact text. I did not find any egregious “this paper says X” claims that contradict the cited works, but there are places where metadata/titles are slightly off, status of “in prep.” work is not correctly synchronized, and a few internal-version artifacts remain. I also think the paper is too long for PRD’s usual methods papers.

Below I list all concrete findings I can identify from the supplied text, organized by severity.

---

## ESSENTIAL findings

### P4-E1 — Outdated / incorrect handling of “in prep.” work  
**Section:** V.A, around “anticipated Iye & Yagi forthcoming … (in prep.)”  
**Issue:** The text mentions “An anticipated Iye & Yagi forthcoming HSC-WIDE Survey spin-parity analysis (Iye & Yagi, in prep.)” as if no public version exists. Iye & Yagi have in fact posted arXiv results on spin parity with HSC-SSP since 2022–2023; treating them as “in prep.” is outdated and misleads the reader about the current literature status.[5][6]  
**Required fix:**  
- Replace the “in prep.” mention with an accurate citation to the relevant HSC-based spin-parity paper(s), including arXiv ID and journal if available.  
- If the exact paper you had in mind is different, either (i) update to the actual arXiv identifier, or (ii) explicitly delete the “in prep.” clause and rephrase so you are not implying there is specific unpublished work.  

---

### P4-E2 — Internal version-history / review-log language in body text  
**Section:** III.A, III.E, IV.D, VI.G, VI.I, VII; multiple instances  
**Issue:** The manuscript still contains explicit references to earlier drafts, external reviews, and internal audit narratives, e.g.:  

- “This test was added after the an earlier external review…”  
- “Honesty note: the binomial per-pixel-shuffle null does NOT preserve depth…”  
- “( scope restoration …)”  
- “earlier drafts additionally reported… as a third rotational-systematic metric; the partial-harvest … sign-flips this … we therefore retract this auxiliary metric…”  
- “Cross-model peer review (cross-confirmed by Gemini 3.1-Pro and GPT-5) flagged that earlier earlier drafts had used…”  
- “the earlier-snapshot one-tailed p = 0.33 … is superseded.”  
- “earlier placeholder citation identifier … has been removed…”  
- “The original historical reference … has been retracted as a methodological artifact.”  

PRD will not want this internal review history and “AI peer review” commentary in the main body of a science paper; it reads as lab notebook text.  
**Required fix:**  
- Systematically scrub all version-history and external-review references from the prose and tables.  
- Rewrite such passages into timeless, impersonal statements: e.g. “We initially used Ntot in the shot-noise denominator; this was incorrect and has been corrected here to Nspiral = …” without referencing Gemini/GPT, earlier drafts, or “retractions.”  
- Ensure Tables and captions likewise avoid language like “legacy baseline”, “smoke estimate,” “retracted,” etc. These details can go into a brief “errata from earlier preprints” note at the end if you insist, but not sprinkled throughout.

---

### P4-E3 — Residual internal tags / malformed prose fragments  
**Section:** III.E (D4-TTA discussion), VI.G, footnotes in Tables II/VII/VIII  
**Issue:** There are obvious internal markers and broken parentheses in the prose that look like editing artifacts rather than polished text, e.g.:

- “( scope restoration the mean-probability invariance … is the load-bearing population diagnostic …)”  
- “The extended joint fit with leg × confidence-bin interaction amplitudes show large z-scores…” followed by an unmatched closing parenthesis.  
- Several footnotes include half-sentences such as “the earlier the earlier-draft auxiliary claim … is retracted here (§III E closure note)” and “historical predecessor tags” etc.

This is not acceptable as final journal prose.  
**Required fix:**  
- Carefully re-edit the D4-TTA subsection and the canonical-mask multi-null subsection to remove parenthetical fragments and ensure every sentence is grammatically complete.  
- Remove or rewrite any “closure note” language to straight, declarative exposition.  

---

### P4-E4 — Length / scope vs PRD norms  
**Section:** whole paper; 57 pages  
**Issue:** For PRD, a 57-page methods/catalog paper is unusually long; most comparable works are ~15–30 pages. The current draft includes extensive narrative on internal null-battery design, multiple alternative masks, long digressions on bootstrap vs label-shuffle nulls, AI-tool acknowledgments and GPU-throughput benchmarking, etc., that go substantially beyond what is needed to support the core science claim (a null ℓ=1 dipole plus a quantified canonical-mask systematic).  
**Required fix:**  
- Substantially reduce length. A realistic target for PRD is ≤30 pages, with truly essential technical details (e.g. full multi-null battery, D4-holdout diagnostics, GPU benchmarking) moved to a separate, clearly referenced online supplement or data release note.  
- In the main paper, keep: data description, classifier architecture + key validation, catalog statistics, primary dipole/Master analysis, canonical-mask leakage demonstration, and the main comparison to Shamir / CE-ResNet / Iye et al.  
- Eliminate internal-audit narratives, repeated recounting of the same σ values under many slightly different nulls, and most of the GPU-throughput and edge-case engineering commentary.

Given how tightly the argument is already constructed, you should be able to present the essential science convincingly in ~25–30 pages.

---

## MAJOR findings

### P4-M1 — Abstract over-claims detailed canonical-mask interpretation  
**Section:** Abstract (first 3 paragraphs)  
**Issue:** The abstract spends significant space on the canonical-mask +3.64σ residual and the three-way interpretation (dipole vs depth/morphology vs NaMaster artifacts), and states “Interpretation (ii) is therefore the favoured verdict at the diagnostic level…” The full body makes clear this is *not* a rigorous, likelihood-level decomposition (no full spatial likelihood, limited template basis), and repeatedly emphasizes caveats.  
**Required fix:**  
- In the abstract, reduce this to: “We find a +3.6σ ℓ=1 excess on the patchy canonical mask, which we attribute to a depth/morphology-correlated systematic based on cross-spectra with pixel density and imaging-leg splits. This residual is not used as a cosmological detection.”  
- Remove any wording in the abstract that sounds like a firm model-selection result between dipole and systematics; reserve that nuanced discussion for the main text, with explicit caveats.  

---

### P4-M2 — Over-use of σ-language from heterogeneous nulls  
**Section:** Throughout Results/Discussion, especially Tables II, VI, VII, VIII, XVI; Figures 8–12  
**Issue:** You are careful, but there are still many places where different “σ” values (Gaussian-equivalent from MC, analytic σ, χ²-derived σ) are juxtaposed in ways that a typical PRD reader will read as directly comparable, even though the underlying nulls differ (label-shuffle vs bootstrap vs monopole-only generative vs density-stratified). This brushes up against instruction (7): no mixing of σ scales without explicit qualification.  
**Required fix:**  
- For every table that lists multiple σ values, add an explicit column or a one-line caption indicating **which null is used** (e.g. “MC label-shuffle,” “monopole-only binomial,” “bootstrap over pixels”).  
- Where you compare σ’s in the text (e.g. “+3.64σ vs −0.22σ vs +3.57σ”), always immediately qualify the null, or replace σ with a statement like “pMC≈0.03 under a binomial-shuffle null; under a bootstrap null the statistic is consistent with zero.”  
- If you keep σ notation, add a one-paragraph “Conventions for significance throughout” early in Methods stating that σ’s from different nulls are not directly comparable and are only used as shorthand for rank-based p-values.

---

### P4-M3 — Some reference metadata incomplete or slightly imprecise  
These are not catastrophic but should be cleaned for publication.

#### (a) Shamir 2022 PASJ vs MNRAS  
**Section:** Introduction, V.A; ref. [2]/[3]  
**Issue:** You clearly distinguish Shamir (2012, PASJ) and Shamir (2022, MNRAS 516, 2281; arXiv:2208.13866). However in the text there is at least one mixed phrase: “Shamir’s earlier work [1] reported ∼3% asymmetries… Shamir (2022) [3] reported DESI Legacy Survey results…” where [2] is PASJ and [3] is MNRAS. That’s fine, but the parenthetical “(Methodology / Ganalyzer-pipeline reference paper. The DESI Legacy spin-direction paper is cited separately below as Shamir:2022DESI.)” in the references suggests an internal shorthand that doesn’t appear in the main text.  
**Required fix:**  
- Ensure the main text always refers to the actual journal names: “Shamir (2012, PASJ 74, 1114)” and “Shamir (2022, MNRAS 516, 2281)”.  
- Remove any internal labels like “Shamir:2022DESI” that are not used consistently; just cite the standard ref.  

#### (b) DESI white paper citation  
**Section:** VIII / references   
**Issue:** You cite the DESI Collaboration white paper as “arXiv:1611.00036 (white-paper only, no journal publication).” According to ADS, this is accurate (no PRD/ApJ version), but PRD usually prefers a standard arXiv citation style.  
**Required fix:**  
- Standardize to APS style: “DESI Collaboration, A. Aghamousa et al., arXiv:1611.00036.” Optionally drop the parenthetical commentary “white-paper-only” or move it to a brief footnote if you think it’s important that there is no peer-reviewed version.

---

### P4-M4 — Abstract aims vs what is actually demonstrated  
**Section:** Abstract, last paragraph (“Falsification criterion” and “Scope”)  
**Issue:** The falsification criterion currently mixes statistical and systematic floors, e.g. prose like “falsify the present null at σ>5 at amplitude ≳0.75% (the demonstrated 50%-recovery-at-3σ threshold…) … the floor tightens under LSST sample-size scaling.” The body text clarifies that 0.75% is an empirical, pipeline-specific threshold for the HC subsample under a particular null, not a fundamental limit.  
**Required fix:**  
- Rewrite the falsification criterion to: “A future survey that, after comparable systematics control, detects a chirality dipole with full amplitude ≥0.75% at ≥5σ significance would be in tension with our null result.”  
- Remove the specific LSST extrapolated “∼0.08%” type numbers from the abstract and keep them in the Discussion where the assumptions are clearly laid out.

---

## MINOR findings

### P4-m1 — Slight mismatch in wording of Jia et al. (CE-ResNet) abstract claim  
**Section:** Introduction, paragraph on CE-ResNet; V.B; ref.   
**Issue:** You state that CE-ResNet “yields cw/ccw = 0.998, consistent with parity.” This matches the Jia et al. reported result (they state their catalog-level CW fraction is within ~0.2% of 0.5). I did not find a contradiction. However, you might want to quote explicitly the CE-ResNet number as “fCW≈0.499” or “0.998 cw/ccw ratio” to match their notation.  
**Required fix:**  
- Optionally tighten the phrasing to “Jia et al. report cw/ccw≈0.998, i.e. fCW≈0.499, consistent with parity.” This keeps your summary visibly traceable to their abstract rather than looking like a rounded reinterpretation.

---

### P4-m2 — SpArcFiRe DR9 overlap description could be more precise  
**Section:** V.C; refs.   
**Issue:** You say “the SpArcFiRe DR9-overlap catalog reports CW/CCW counts consistent with 50/50 to within ∼0.3% at its ∼1.4×105-galaxy footprint (, Table 3 plus the public Hayes-Davis DR9 update).” Davis & Hayes (2014) ApJ 790, 87 indeed describe SpArcFiRe; the 0.3% figure comes from their SDSS/DR7+DR8 overlap analysis and Hayes’ subsequent online table. I can’t fully verify the 0.3% number from  alone; it depends on the external “DR9 update” you reference but don’t formally cite.  
**Required fix:**  
- Either (i) cite explicitly the DR9 update source (arXiv or a data release page), or (ii) soften this to: “SpArcFiRe DR9 overlap results (Hayes & Davis 2014 plus later online DR9 updates) are reported to have CW/CCW consistent with 50/50 at the ≲1% level on ~1.4×105 galaxies.”  

---

### P4-m3 — “Tadaki et al. (2020)” metadata  
**Section:** V.A; ref. [6]  
**Issue:** You refer to Tadaki et al. as “Tadaki et al. (2020) HSC-SSP imaging,” which matches their MNRAS 496, 4276 paper. From ADS this is correct: year 2020, MNRAS 496, 4276.[6]  
**Required fix:**  
- None strictly required; if you want to be maximal precise, you could add the journal “MNRAS 496, 4276 (2020)” inline once when first mentioned.

---

### P4-m4 — Some reference titles truncated or paraphrased  
**Section:** References , , ,  (parity-odd 4PCF / g* papers)  
**Issue:** You paraphrase several theory-paper titles slightly (e.g. “Colliders and ghosts: Constraining inflation with the parity-odd galaxy four-point function” for Cabass–Ivanov–Philcox, which is accurate, and the Cahn–Slepian–Hou test). I do not see mismatches that would mislead the reader; these are minor.  
**Required fix:**  
- Check your reference-list titles against ADS to ensure they match the published titles exactly; adjust if needed for APS style, but this is mostly cosmetic.

---

### P4-m5 — A few remaining colloquial phrases  
**Section:** Various, especially Discussion and conclusions  
**Issue:** Phrases like “honesty note,” “we urge…,” “this is the canonical follow-up,” “smoke estimate,” “stress-test vs sanity-check” are better suited for an internal methods memo than for PRD.  
**Required fix:**  
- Replace with neutral, journal-style phrasing: “Note that…,” “A natural follow-up is…,” “we performed a preliminary test (N=25)…” etc.

---

## NIT-level findings

### P4-n1 — Minor duplication/near-duplication phrases  
I did not find egregious literal duplicates like “canonical canonical-mask,” but there are a few near-duplicated constructions that could be cleaned for style:

- “earlier earlier drafts” (typo duplication).  
- “historical predecessor patch tags historical predecessor tags” (in one footnote-style sentence there is a repetition).

**Required fix:**  
- Correct typos and remove duplicated words wherever they occur.

---

### P4-n2 — Clarify which σ is “Gaussian Z” vs “rank-based”  
You are already doing this most of the time, but there are a few short phrases like “a 3.64σ family-corrected residual” where it is not immediately obvious whether that σ is from Gaussian Z or from Φ^{-1}(1−pMC/2).  
**Required fix:**  
- Add a parenthetical when such numbers are first introduced in a section: “3.64σ (Gaussian-equivalent, from (C1−⟨C1,null⟩)/σnull).”

---

### P4-n3 — AI usage paragraph  
**Section:** Acknowledgments  
**Issue:** The AI-usage disclosure is detailed; APS hasn’t imposed strict rules yet, but this volume of operational detail about “cross-confirmed by Gemini 3.1-Pro and GPT-5” is unusual. It also directly mentions specific models.  
**Required fix:**  
- Condense to a single neutral sentence: “Large-language-model tools were used for code review and LaTeX editing; all scientific results are from the authors’ own analysis.” Remove specific model names and version-history commentary.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The core cosmological and methodological result looks sound and carefully caveated, and I did not find any outright misrepresentations of what the cited arXiv/journal papers claim. However, the manuscript is significantly over length for PRD, contains pervasive internal-review and version-history artifacts, uses σ values from multiple null procedures in a way that will confuse many readers, and treats at least one “in preparation” work as unpublished despite existing arXiv results. A substantial editorial clean-up, explicit standardization of significance conventions, correction of the “in prep.” status, and aggressive shortening (to ≲30 pages) are required before I would consider it ready for publication.