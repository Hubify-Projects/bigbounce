# P4 2026-06-04_R6clean — Citation forensics auditor with real-time web search access

**Model**: `sonar-pro`
**Input format**:  [PDF TEXT via pdftotext]
**Wall time**: 43.8s

---

P4-ESSENTIAL-1 — Global σ-scale comparability disclaimer is clear and correct  
- **Location:** Abstract, p.1 (“Note: σ values… not directly comparable across estimators…”)  
- **Issue:** None. The paper explicitly warns that σ from different null procedures are *not* on the same scale, and repeats this in the body (Secs. IV, VI). There is no place where σ from different nulls are added, averaged, or directly compared as if commensurate without qualification.  
- **Action:** No change needed.  

---

### 1. Citation identity and metadata

Below I use the paper’s reference numbers.

#### P4-ESSENTIAL-2 — Reference [2] is misidentified / fused  
- **Section/page:** References, [2]; text around “GANALYZER-pipeline reference paper” and “Shamir:2022DESI” in footnote [2] on p.50.  
- **Problem:**  
  - The reference list gives:  
    > [2] L. Shamir, “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,” Publ. Astron. Soc. Jpn. 74, 1114 (2022), DOI:10.1093/pasj/psac058. (Methodology / Ganalyzer-pipeline reference paper. The DESI Legacy spin-directions paper is cited separately below as Shamir:2022DESI.)  
  - arXiv/ADS show that PASJ 74, 1114 (2022), DOI 10.1093/pasj/psac058 is indeed “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies” by Shamir, **but that paper is itself the DESI-based spin-direction analysis**, not a separate, purely “methodology/Ganalyzer-pipeline reference paper.” There is no second, separate 2022 DESI Legacy paper by Shamir.  
  - The parenthetical “the DESI Legacy spin-directions paper is cited separately below as Shamir:2022DESI” is therefore incorrect and suggests a *nonexistent* second DESI Legacy paper.  
- **Required fix:**  
  - Correct the commentary on [2] to reflect that this PASJ paper *is* the DESI/Legacy spin-direction analysis, not merely a pipeline-method paper. Remove the “cited separately” language and any “Shamir:2022DESI” alias that implies a second distinct 2022 DESI Legacy paper.  
  - If the authors want to distinguish method vs. DESI content, they should do so in prose (“this paper both defines the Ganalyzer pipeline and applies it to DESI Legacy imaging”) without implying a second citation.  

#### P4-MAJOR-1 — Slightly misleading description of Shamir (2022) [3] sample  
- **Section/page:** Introduction, p.3; also Sec. V A.  
- **Problem:**  
  - The paper states:  
    > Shamir (2022) [3] (arXiv:2208.13866, DESI Legacy Survey, MNRAS 516 2281; the published abstract reports “nearly 1.3 × 10^6 spiral galaxies” as the analyzed spiral set…  
  - Checking arXiv:2208.13866 / MNRAS 516, 2281 (2022) confirms: the abstract indeed says “nearly 1.3 × 10^6 galaxies.” However, it does *not* explicitly say “spiral galaxies” in the abstract; “spiral” appears in the body in the context of selection. The manuscript’s wording subtly shifts “galaxies” → “spiral galaxies” in the abstract paraphrase.  
- **Required fix:**  
  - Change to a faithful paraphrase of the abstract, e.g. “the published abstract reports ‘nearly 1.3 × 10^6 galaxies’” and then, separately, describe the spiral subset as inferred from the body if needed. Don’t attribute “spiral” specifically to the abstract.  

#### P4-MINOR-1 — Shamir (2012) [4] description could be tighter  
- **Section/page:** Introduction, p.2:  
  > “Shamir (2012) [4] reported a 2–4σ dipole significance with per-bin asymmetry amplitudes of ∼ 5–20% using ∼ 1.27 × 10^5… (126,501 spirals; Shamir 2012 abstract)”  
- **Problem:**  
  - The numbers and rough ranges are consistent with Phys. Lett. B 715, 25 (2012) / arXiv:1207.5464 (∼126k SDSS galaxies, per-hemisphere 5–20% asymmetries). The phrase “Shamir 2012 abstract” is slightly misleading; those detailed ranges come from the paper and figures, not literally from the abstract.  
- **Required fix:**  
  - Replace “(126,501 spirals; Shamir 2012 abstract)” with something like “(126,501 spirals; as reported in Shamir 2012)” to avoid over‑precise attribution to the abstract.  

#### P4-MINOR-2 — Motloch & Pen (2021)  title truncated and slight emphasis shift  
- **Section/page:** Sec. V D.  
- **Problem:**  
  - Reference  in the list is:  
    > “An observed correlation between galaxy spins and initial conditions,” Nature Astron. 5, 283 (2021).  
  - The actual title per ADS is “An observed correlation between galaxy spins and the initial conditions of the Universe.” The shorter variant is not wrong, but non-standard.  
  - The text paraphrases their result as “a marginal (∼ 2.7σ) correlation” — which is consistent with their reported significance, but the original paper emphasizes this as evidence for a real effect despite low σ.  
- **Required fix:**  
  - Prefer the full published title in the reference list.  
  - No change needed on the σ unless the authors want to cite the exact reported significance (2.7σ) with a reference to the relevant figure/table for precision.  

#### P4-MINOR-3 — CE-ResNet  “cw/ccw = 0.998” wording  
- **Section/page:** Introduction, p.3:  
  > “yields cw/ccw = 0.998,1 consistent with parity.”  
- **Problem:**  
  - Jia et al. (ApJ 943, 32, 2023; arXiv:2210.04168) report an extremely small global bias; the 0.998 number looks like a ratio of fractions, but the notation is slightly opaque and the trailing “,1” looks like a typo or leftover reference marker rather than a numeric.  
- **Required fix:**  
  - Clarify the notation, e.g. “yields cw/(cw+ccw) ≈ 0.499, consistent with parity” or quote the exact fraction as stated in Jia et al.  
  - Remove the stray “,1” unless it is meant to be a citation.  

#### P4-MINOR-4 — Iye et al. (2021) [5] description  
- **Section/page:** Introduction, p.3.  
- **Problem:**  
  - Paper says Iye et al. “documented duplication of photometric objects… in earlier Shamir catalogs as an additional source of spurious large-scale signal.”  
  - In ApJ 907, 123 (2021) / arXiv:2011.00662, they indeed show that some cataloged “galaxies” are star-forming regions/knot duplications and argue this can bias signals. This is broadly accurate, but the word “documented” plus “as an additional source” slightly overstates that they *quantitatively* established its impact. They raise it as an issue, but the quantitative effect is limited by sample size.  
- **Required fix:**  
  - Soften to “identified and discussed duplication… as a potential additional source of spurious signal” rather than as a firmly established quantified contribution.  

#### P4-NIT-1 — Yu et al. (2020)  title incomplete  
- **Section/page:** References .  
- **Problem:**  
  - The reference list has “Probing primordial chirality with galaxy spins” (PRL 124, 101302 (2020)), which matches the official title. However, the text occasionally calls this “Yu et al. ” in a way that might be confused with Motloch & Pen.  
- **Required fix:**  
  - No bibliographic change needed. In the body where both  and  are mentioned, consider explicitly distinguishing “Motloch & Pen (spin–initial-conditions)” vs. “Yu et al. (spin–primordial-chirality)” once, to avoid confusion.  

---

### 2. Cross-checking quoted numerical claims against cited papers

#### P4-MAJOR-2 — 69.91% GZ1 agreement and κ ≈ 0.40 are internal, not from //  
- **Section/page:** Sec. II B (Independent GZ1 cross-match), pp.4–5.  
- **Problem:**  
  - The 69.91% spiral-only agreement and Cohen’s κ = 0.40 are presented as *this paper’s* measurement from a cross-match, which is fine.  
  - Immediately after, the text says:  
    > “The published GZ1 internal-rater agreement… is not directly tabulated in Lintott et al.  but is bounded above by the magnitude- and redshift-dependent vote bias documented in Bamford et al.  and Hart et al. : at r ≲ 17 the volunteer CW/CCW vote agreement is ∼ 75–85%…”  
  - Bamford et al. (2009) and Hart et al. (2016) do discuss vote fractions and biases; however, they do not give a simple “75–85% CW/CCW agreement” number in the abstract. That range is clearly the author’s synthesis from plots.  
- **Required fix:**  
  - Make the attribution explicit: “Based on Figs. X/Y in Bamford et al.  and Hart et al.  we infer that…” or similar, so it is clear this is your interpretation, not a direct quoted statistic.  
  - Optionally add exact figure numbers used for this inference.  

#### P4-MINOR-5 — “cw/ccw = 0.998” again (CE-ResNet)  
- Already covered as P4-MINOR-3: ensure the ratio and its mapping to Jia et al.’s reported small bias are correctly stated.  

#### P4-MINOR-6 — 2–4% Shamir asymmetry range phrasing  
- **Section/page:** Introduction, p.3.  
- **Problem:**  
  - Text:  
    > “The ∼ 2–4% asymmetry range is the union of the two papers’ reported amplitudes, not a single quoted value.”  
  - This is consistent with Shamir (2012; 2015; 2020; 2022) which report different hemispheric asymmetries around a few percent. But there is no explicit 2–4% bracket in a single prior paper.  
- **Required fix:**  
  - This is correctly caveated; no change needed. If space is tight, you could add explicit refs to which values come from which paper, but it’s not essential.  

---

### 3. “In preparation” / versioning / artifact language

#### P4-MAJOR-3 — Internal artifact/version remarks in body text  
- **Section/page:** Several places, e.g. Sec. II B footnote 3, Sec. III E, Table captions, Sec. IX.  
- **Problem:**  
  - The paper repeatedly references “companion data repository,” “canonical-provenance JSON artifacts,” “public project repository,” “H200 pod,” and gives details such as “NMC = 10,000 (∼ 13 minutes wall on the same local pymaster 2.6 build)” and even build flags (`--disable-openmp --enable-fftw-pthreads`).  
  - For PRD, some method details are good, but much of this *reads like artifact-evaluation boilerplate* rather than scientific content. It makes the paper bloated and harder to follow, without improving the cosmological argument.  
- **Required fix:**  
  - Move all implementation-level artifact/provenance details (exact pod names, wall times, build flags, seed numbers for non-key runs, references to GitHub/Zenodo structure) into a short “Code and data” appendix or a README in the repository, and condense the main text to:  
    - Specify only NMC, NSIDE, ℓmax, mask choice, and which catalog tier.  
    - State succinctly that all scripts and outputs are available in an online repository (no URLs per journal style; just “see Data Availability”).  
  - Remove phrases that are clearly “internal ops” (e.g. “this simulation supersedes the smoke result at N=25”) from the main narrative. They belong at most in supplementary material.  

#### P4-MINOR-7 — “retracted” language around D4-TTA argmax CW fraction  
- **Section/page:** Sec. III E, mid pp.10–11.  
- **Problem:**  
  - The text discusses an earlier draft’s ∆ = −1.35% argmax CW-fraction shift and says “we therefore retract the original … claim as sample-noise…”. This is internal revision history, not relevant to the final scientific result.  
- **Required fix:**  
  - Rewrite this as a simple final statement: report the two holdout results and conclude that argmax CW fraction is unstable and therefore not used as a primary diagnostic. Drop the “retract” language and any reference to “original claim” that pertains to prior drafts.  

---

### 4. Version-history / review-log artifacts

I looked specifically for phrases that leak submission history or review rounds.

#### P4-MAJOR-4 — “earlier drafts” / “prior preliminary estimate” in main prose  
- **Section/page:**  
  - Sec. III F: “Our current thresholds serve as… Earlier drafts also quoted a fraction-at-> 0.99 number…”  
  - Sec. VI D: “The 59.4% edge-on spiral classification rate is ∼ 6 pp lower than the prior preliminary estimate of 65.7%…”  
  - Sec. VII: “the 0.14–0.20% figure that appeared in earlier prose…”  
- **Problem:**  
  - These are explicitly referencing earlier drafts and internal revision history. Journal papers should present the final method/results, not a change-log.  
- **Required fix:**  
  - Remove all “earlier drafts”, “prior preliminary estimate”, “earlier prose”, “smoke result”, “legacy pre-correction baseline (+1.85σ, retained for historical provenance only)” style phrases from the body.  
  - Where needed, keep only the *current* numbers and a concise statement of uncertainty.  

There are no explicit “ROUND”, “R6”, or similar tags in the *paper text*; the “changes since last round” appear only in the reviewer metadata header, which you correctly marked as not part of the paper.

---

### 5. Duplicate / broken phrasing

I scanned for obvious duplicated phrases.

#### P4-MINOR-8 — Slightly garbled sentence around canonical-mask interpretation  
- **Section/page:** Abstract-like summary block, early p.2 (first long paragraph about interpretations (i)–(iii); around “three-discriminator framework”).  
- **Problem:**  
  - The sentence:  
    > “Under this three-discriminator framework), with the post-MASTER null adopted as the primary result.”  
  - has an unmatched closing parenthesis and reads truncated.  
- **Required fix:**  
  - Fix to: “Under this three-discriminator framework, we adopt the post-MASTER subsample-mask null as the primary result.” and remove the stray “)”.  

#### P4-NIT-2 — Several long sentences bordering on unreadable  
- **Section/page:** Multiple (e.g. Sec. IV D canonical-mask discussion, Sec. VI G).  
- **Problem:**  
  - Extremely long sentences with many clauses and parentheses make it hard to parse the logic; while not scientifically wrong, this obscures the link between claims and evidence.  
- **Required fix:**  
  - For each of the 2–3 longest paragraphs (canonical-mask residual, template fit, bootstrap inflation), split into shorter sentences and, where appropriate, bullets. The science can remain unchanged but the structure must be clearer.  

---

### 6. Abstract vs. what is actually proved

#### P4-MAJOR-5 — Abstract slightly oversells “falsification criterion”  
- **Section/page:** Abstract, “Falsification criterion” paragraph.  
- **Problem:**  
  - The abstract states:  
    > “A future survey that… detects a chirality dipole at σ > 5 with full amplitude ≳ 0.75%… would falsify the present null.”  
  - The body shows that 0.75% is the empirical 50%-recovery-at-3σ threshold *for the HC subsample under a particular null*; it is **not** a hard upper bound on any physical dipole in the presence of systematics. You correctly say later this is a “present-pipeline” sensitivity, not an absolute physical limit.  
- **Required fix:**  
  - In the abstract and conclusion, qualify this as:  
    > “would falsify our *present-pipeline* null under comparable systematics control.”  
  - Make explicit that this is not a fundamental cosmological bound, but conditional on analysis choices and the demonstrated injection–recovery.  

#### P4-MINOR-9 — “Most sensitive chirality measurement ever performed”  
- **Section/page:** Sec. VII point 1.  
- **Problem:**  
  - You state: “This represents the most sensitive chirality measurement ever performed, exceeding the CE-ResNet constraint… by a factor of ∼1.3 in statistical sensitivity.”  
  - CE-ResNet’s paper focuses on classifier properties; it does report global parity, but not a full dipole analysis with Fisher floor. The “factor 1.3” is your own scaling from N^(−1/2), which is fine but somewhat speculative because CE-ResNet’s effective f_sky and cuts differ.  
- **Required fix:**  
  - Soften to “nominally ∼1.3× better statistical sensitivity, assuming similar sky coverage and null procedures.”  

---

### 7. σ scale / null-procedure comparability

You explicitly warn that σ from different nulls are not directly comparable, and I did not find any place where you simply add or subtract them. The template-fit section correctly converts to p and then to σ. No ESSENTIAL issues here.

---

### 8. Length and focus

#### P4-MAJOR-6 — Paper is overlong relative to core cosmological result  
- **Assessment:** ~50+ pages for a single claim: “no detectable ℓ=1 chirality dipole under our pipeline; canonical-mask residual likely systematic.” A lot of space is spent on internal audit trail, artifact remarks, and null variants that could be summarized much more concisely.  
- **Concrete recommendation:**  
  - Aim to compress to **≤ 35 pages** of main text for PRD by:  
    - Moving almost all MC-run, pod, seed, and build-flag details to an online supplement.  
    - Collapsing the four-page canonical-mask discussion into one clear section with: description, main σ, key nulls, and the bottom-line interpretation.  
    - Shortening the bias-hardening text to the essentials plus a pointer to code.  

---

## Summary recommendation

**MAJOR REVISIONS**

The core cosmological methodology and the care with nulls look solid, and I did not find any catastrophic citation falsifications. The main issues are: one mischaracterized Shamir 2022 citation, too much internal revision/history and artifact-log language in the body, some over-strong abstract phrasing relative to what is actually demonstrated, and overall bloat that obscures the main result. With corrections to the Shamir 2022 description, removal of version-history chatter, tightening of claims about sensitivity/falsification, and significant condensation of implementation details into supplementary material, the paper would be suitable for PRD.