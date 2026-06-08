# P1B auto-2026-06-08_1632pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (11302 chars)
**Wall time**: 37.5s

---

I cannot complete the requested **citation-forensics audit** to PRD standard from the materials provided.

The prompt includes the paper text, but **it does not include the actual web-search evidence needed to verify arXiv IDs, ADS records, DOI/venue metadata, or bibliography claims**, and the “search results” attached are unrelated to this cosmology paper. Because of that, I cannot responsibly certify whether references [1]– are correct or whether cited statistics trace back to the underlying papers.

What I *can* say from the rendered paper text alone is that there are several **internal consistency and citation-policy problems** visible without web lookup:

- The bibliography contains multiple **“in preparation”** entries for the author’s own companion papers ([1], [4], [5], ) that are not verifiable as published literature in the paper itself. If these are being used as substantive support for claims, they need proper manuscript-status handling and full disclosure.
- Reference [3] is cited as **“arXiv preprint (2025), arXiv:2509.13654”** even though the paper is dated **2026-06-08**; that arXiv identifier looks **future-dated** relative to the manuscript date and must be checked.
- The paper repeatedly states that several results are **“deferred”** or **“not reported”** (Bayes factors, AIC/BIC, ln B), yet it still makes strong model-comparison language in the prose. That is not a citation issue per se, but it is a load-bearing methodological gap.
- The text contains many internal self-referential correction notes such as “earlier count erroneously quoted…”, “reconciliation,” “verified by direct .input.yaml inspection,” and detailed bookkeeping about sample counts. Those are not necessarily fatal, but they are exactly the kind of claims that require source-level audit.
- The paper also includes multiple numerical statements that are trivially checkable from the displayed values and are mostly arithmetically consistent, e.g. the inverse-variance weighted \( \beta \) combination and the quoted \(w_0+ w_a\). But I have not been asked to just sanity-check arithmetic; you explicitly requested full forensic verification against arXiv/ADS.

Because I cannot verify the references or the literature-claimed statistics with the provided evidence, I cannot produce the required line-by-line referee report in good faith.

## Summary recommendation
**MAJOR REVISIONS**

The paper may be internally coherent in places, but on the record available here it is **not audit-ready for PRD** because the bibliography and external citations have not been verifiably checked against authoritative sources, and at least one cited arXiv identifier appears potentially future-dated relative to the manuscript. The authors must provide a fully verified reference list, provenance for every external numerical claim, and an explicit correction of any manuscript-status or arXiv-metadata inconsistencies before this can be considered acceptable.

---

## PASS 2 — self-critique findings (what initial review missed)

[P1B-E1] **Arithmetic – inconsistent σ and SNR for NaMaster bias**

- In Sec. IV, the NaMaster recovery for injected β = 0.27° is quoted as  
  “β̂NaMaster = 0.238° (pipeline-recovery SNR = 20.32)” with bias 0.032°.[IV]  
  Taken at face value, SNR ≈ (recovered amplitude / 1σ) or ≈ (injected amplitude / 1σ) implies 1σ ≈ 0.011–0.013°.  
  But later the *systematic* bias is described as 0.032–0.040°, treated as a “systematic floor.”[IV, VI]  
  A systematic floor larger than the implied statistical 1σ by a factor ≳3 is not explicitly acknowledged or propagated anywhere (e.g., into the βALP comparisons), and the paper never shows the actual MC scatter that would justify SNR=20.32 with that level of bias. This arithmetic inconsistency between stated SNR and stated systematic floor should be flagged; either the SNR, the floor, or their interpretation is off.

[P1B-E2] **Arithmetic – inconsistent “stable bias” vs quoted values 0.032° and 0.040°**

- The text first calls the NaMaster bias “stable across all three injections” at 0.032°, but later admits the β = 0.342° injection gives 0.040°.[IV] A 25% change in the systematic bias (0.032→0.040) is *not* “stable at 0.032°.” The paper corrects this in prose but never corrects the earlier claim or updates any downstream usage to 0.040° as the worst-case floor. This is an internal numerical inconsistency.

[P1B-E3] **Arithmetic – inconsistent characterization of β scan envelope**

- Sec. VI states that a joint scan over (Caγ, m/H0, θi) gives β ≈ 0.17–0.43° across Caγ ∈ [4,12], m/H0 ∈ [1,3], θi ∈ [0.5,2], and says the wider naive envelope [0.027,0.44]° from independent extremes is *not* used.[VI]  
  However, earlier in the same section, simple substitution using the provided fiducial numbers (Caγ=8, ∆ϕ/fa ≈1.07) gives β ≈ 0.29°, and the “fiducial value” β ≈ 0.27° is associated with ∆ϕ/fa ≈1.0 at m≈1.8 H0.[VI] These are internally consistent, but the lower bound 0.17° at Caγ=4 and ∆ϕ/fa≈0.2 is difficult to reconcile with the stated ∆ϕ/fa envelope [0.2,1.1] and the same prefactor αEM/(4π). A strict recomputation with these ranges tends to push the low end closer to ≈0.07–0.08° rather than 0.17°, unless some additional constraint couples Caγ and ∆ϕ/fa. That coupling is not made explicit, so the quoted 0.17° lower bound is numerically under-justified.

[P1B-E4] **Arithmetic – implied Caγ range does not match earlier envelope**

- Using βobs = 0.342° and αEM/(4π) = 5.8×10⁻⁴, the paper correctly infers Caγ∆ϕ/fa ≈10.3.[VI]  
  Given the previously stated ∆ϕ/fa ∈ [0.2,1.1], this implies Caγ ∈[~9,~51], which the paper states.[VI]  
  However, earlier it presented Caγ ∈[4,12] as a “natural” scan range.[VI] These two ranges are only barely overlapping at the *upper* edge; for most of the stated “natural” scan, β is far too small. The paper partly acknowledges this as “non-minimal” but still treats Caγ∈[4,12] and “natural parameter values (taken at scan-prior midpoint values)” as if they genuinely bracket the observed β; in fact, only the very upper edge of that Caγ range can match βobs without moving ∆ϕ/fa outside the [0.2,1.1] envelope. This is a hidden arithmetic tension between the advertised scan box and the derived Caγ requirement.

[P1B-E5] **Arithmetic – 25× misalignment tuning is not consistently quantified**

- Footnotes 4 and 5 state that going from θi=0.5 (prior midpoint) to θi≈0.1 (spectator-consistent) corresponds to a “∼25× fine-tuning” in misalignment.[VI, App. C]  
  But the actual scaling is Ωa ∝ θi², so Ωa(0.1)/Ωa(0.5) = (0.1/0.5)² = 1/25 for the energy density, while the *angle* tuning is 5×. The manuscript mixes “25× fine-tuning” (in energy) with an implicitly angular prior midpoint θi≈0.5, without ever clearly stating which quantity (energy vs angle) is meant in each place. When read alongside the β scaling Caγ∆ϕ/fa≈const, a 5× reduction in θi really implies ≈5× change in Caγ, not 25×, so the repeated “25× misalignment tuning” in β-context sentences is numerically misleading.

[P1B-E6] **Arithmetic – wpivot error propagation has an unshown intermediate**

- The paper claims σ²(wpivot) = σ²(w0) + (1−ap)²σ²(wa) = (0.0436)² + (0.3320)²(0.1864)² = (0.0301)², reproducing the quoted ±0.0301.[Table II]  
  Doing this explicitly: (0.0436)² ≈ 0.00190, (0.1864)² ≈ 0.0348, (0.3320)²≈0.1102, so the second term is ≈0.00384; their sum ≈0.00574, whose square root is ≈0.0757, not 0.0301. The only way to get 0.0301 is *not* to square 0.3320; one needs σ²(wpivot)=σ²(w0)+(1−ap)σ²(wa), which is not the usual error propagation formula. Since the paper does not show the arithmetic step, this is a hidden error: the wpivot uncertainty as written is not consistent with the standard propagation given the quoted numbers.

[m1] **Figure/body mismatch – NaMaster SNR not clearly tied to any panel or variance**

- Sec. IV reports SNR values (20.32, 25.71) for the pipeline without any explicit figure, panel, or variance plot; later sections treat these as “consistent with the ACT-noise floor.”[IV] Since no figure is provided, there is no way for the reader to map those SNR numbers to visual error bars or dispersion in a corner plot or histogram. This is not a numerical error per se, but it is a figure–body mismatch: the claimed SNR cannot be checked against any displayed variance or figure in the manuscript.

[M2] **Dimensional consistency – β units vs αEM/(4π) prefactor**

- In Eq. (3) and surrounding text, β is treated in degrees (0.29°, 0.27°, etc.) while the prefactor αEM/(4π) is a dimensionless number that naturally produces β in radians.[VI] The paper never explicitly states that the computation is done in radians and then converted to degrees, though it clearly *must* be. This is a minor, but the omission makes the equation dimensionally opaque: a reader could mistakenly plug degrees directly into the formula and get inconsistent results.

[M3] **Cross-reference – inconsistent Section labels for ∆Neff results**

- The introduction promises that “When this companion reports MCMC values (H0, σ8, etc.) that are referenced in the main paper, those values come from Secs. III and V here.”[Intro]  
  In practice, the *only* quantitative ∆Neff results are in Table I (Sec. III) and the conclusion; Sec. V explicitly *defers* model-comparison statistics and does not give additional ∆Neff posteriors for the w0–wa run. This makes the claim “Secs. III and V” misleading for ∆Neff: Sec. V does not actually carry any ∆Neff numbers and so cannot be the provenance for ∆Neff-based statements in Paper I(a).

[m4] **Null-procedure comparability – mixed σ levels from distinct likelihood stacks**

- The paper juxtaposes:
  - σ(β) ≈ 0.094° from the joint WMAP+Planck analysis (βobs).[VI]  
  - σ(β) ≈ 0.061° from an inverse-variance combination of Planck NPIPE and ACT DR6.[VI]  
  - σ(βfree) ≈ 0.096° from an internal model-independent MCMC using Planck PR4+ACT EB spectra.[VI]  
- These σ’s come from three *different* likelihood stacks with different systematics and shared-calibration treatments, but they are routinely compared and averaged in prose without strong, repeated warnings that they are not strictly comparable null procedures. A short caveat is given once (for the 3.9σ auxiliary combination), but later sentences still talk about “all three within 1σ” as if they were the same measurement. That is a comparability issue under class E.

[M5] **Abstract faithfulness – spectator ALP described as “consistent” without foreground/systematics caveats**

- The abstract claims “a field with fa ∼ MPl, m ∼ H0 is consistent with the published joint WMAP+Planck value β = 0.342° ± 0.094° (3.6σ).”[Abstract]  
  In the body, however, we learn:
  - The NaMaster test uses a foreground-cleaned Commander map that “removes the very component that breaks the β–α degeneracy.”[Abstract footnote, Sec. IV]  
  - The required Caγ range (∼9–51) pushes well beyond standard KSVZ/DFSZ benchmarks and requires non-minimal model building.[VI]  
  - The spectator regime requires a 5× angular (25× energy) tuning of θi to keep Ωa≪1.[VI, fn. 4, fn. 5]  
- The abstract never mentions any of these substantial caveats. The headline “consistent” therefore overstates how straightforward this agreement is, relative to the more conditional story given in Sec. VI.

[M6] **Unquantified hedges – “consistent with” without Δ/σ for several parameters**

- There are multiple uses of “consistent with” that are only partly quantified:
  - “Both frozen dataset combinations find ∆Neff consistent with zero … and H0 consistent with standard ΛCDM.”[Abstract] For H0 this is later quantified as ≈0.3σ; for ∆Neff the difference from zero is indeed small but never explicitly turned into a Δ/σ number in the text.
  - “Our MCMC agrees at 0.5σ in H0 and 0.4σ in σ8” with Liu et al.[III] Those specific σ offsets are quoted but the underlying means and σ’s are not tabulated anywhere in this paper, so readers cannot verify the arithmetic.  
- These are weaker than the β case but still fall under unquantified/under-documented “consistent with” uses.

[M7] **Appendix vs main-text mismatch – ALP priors vs “natural” spectator description**

- The main text repeatedly frames the ALP parameters as “natural” (fa ∼ MPl, m ∼ H0, θi in [0.5,2]) and then discusses spectator consistency only at θi ∼0.1 with “∼25× tuning,” but it does not explicitly state that *none* of the sampled θi values in the ALP-MCMC runs actually live in the true spectator regime.[VI]  
- Appendix C confirms the sampled θi prior is [0.5,2] and that θi≈0.1 lies *outside* the prior box and would require a separate run.[App. C] The main text nevertheless treats the ALP-MCMC results as bearing on “spectator ALP consistency.” This is a conceptual mismatch: the appendix makes clear the sampling is done in a DE-ALP regime for much of the prior, whereas the main text’s “spectator” framing suggests those samples are directly applicable.

[N1] **Stale numbers – wpivot explanation looks like a leftover from a different covariance**

- The wpivot discussion claims that with ap=0.6680, the decorrelation condition yields σ(wpivot)=0.0301 using the given σ(w0) and σ(wa).[Table II] As noted in [P1B-E6], plugging the table values into the stated formula does not reproduce 0.0301. This strongly suggests the 0.0301 value and/or the supporting formula are from an earlier iteration of the chain or a different covariance, and were not updated when w0, wa, or ap changed.

[N2] **Stale characterization – NaMaster bias originally claimed perfectly stable**

- The sentence “the bias was initially characterized as strictly ‘stable across all three injections’ at 0.032°” followed by “but the 0.342° injection actually gives 0.040°”[IV] is an explicit admission that a previous characterization (0.032° for all injections) was wrong. The text corrects the explanation but does *not* update any of the other places where 0.032° is implicitly treated as the definitive bias. That earlier “strictly stable” description is a stale claim that has not been globally corrected.

If you want, I can next go through the tables line-by-line and recompute every quoted mean±σ, tension level in σ units, and internal consistency relations (MB–H0, χ² decomposition, etc.) to see if there are further hidden arithmetic or cross-reference issues.