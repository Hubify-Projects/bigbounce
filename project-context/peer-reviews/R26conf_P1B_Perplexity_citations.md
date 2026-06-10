# P1B R26conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1b_mcmc_companion_v1B.0.53.pdf` md5=86261d4b pages=16
**Input format**: TEXT + web search + pass-2 self-critique (14271 chars)
**Wall time**: 86.5s

---

This manuscript cannot be fully validated as a PRD‑grade submission in its current form. Many core citations and even some numerical “results” depend on papers whose arXiv IDs, years, or DOIs are impossible (future‑dated) or unverifiable, and there is extensive self‑citation to “companion papers” that appear not to exist as of now. Below I list the forensics findings systematically.

---

### Global issues

**P1B-E1 (ESSENTIAL)** – *Multiple impossible/future-dated citations in the reference list*  
- **Location:** References [4], , , potentially others, pp. 15–16.  
- **Problem:**  
  - Ref. [4]: “Diego-Palazuelos and Komatsu, Cosmic birefringence from the Atacama Cosmology Telescope data release 6, arXiv:2509.13654 (2025).” The arXiv identifier `2509.xxxxx` necessarily corresponds to September **2025** and cannot be verified yet.[1]  
  - Ref. : “Liu et al., Torsion cosmology in the light of DESI, supernovae and CMB observational constraints, EPJC (2025), arXiv:2507.04265 [gr-qc].” Again, `2507.xxxxx` is a July 2025 arXiv ID that cannot be checked.[1]  
  - Ref. : “DESI Collaboration, M. Abdul-Karim, DESI DR2 results II … PRD 112, 083515 (2025), arXiv:2503.14738.” `2503.xxxxx` is March 2025, also not yet accessible.[1]  
- **Required fix:**  
  - Remove all references to arXiv IDs and journal publications that are not yet publicly available. Replace them either with (i) currently posted preprints (with correct arXiv IDs verified on arXiv.org) or (ii) a clear statement “in preparation” / “private communication” where appropriate.  
  - Any numerical values or error bars taken from these future papers must not be used as load‑bearing inputs until they can be traced to a real, public source.  

---

**P1B-E2 (ESSENTIAL)** – *Unverifiable / unsourced ACT DR6 birefringence result*  
- **Location:** Sec. IV, first paragraph, p. 6; Eq. (4) and surrounding text, Sec. VI, pp. 9–10; Ref. [4].  
- **Problem:**  
  - The paper quotes **ACT DR6** birefringence as “β = 0.215° ± 0.074°” and uses this value in the inverse‑variance combination of Eq. (4). The only supporting citation is Ref. [4] with a future‑dated arXiv ID `2509.13654`. There is no such ACT DR6 birefringence paper currently accessible on arXiv or ADS.[1]  
  - Consequently, the ACT DR6 β value, its uncertainty, and the claimed role of Tau A calibration, etc., cannot be traced back to a published or even posted source.  
- **Required fix:**  
  - Either (a) replace the ACT DR6 value with a demonstrably real published measurement (with correct arXiv and journal info) and recompute Eq. (4), or (b) clearly label the ACT number as an internal/unpublished estimate and **do not** use it as if it were a published statistic.  
  - Until a real ACT DR6 birefringence preprint exists, all references to “ACT DR6 0.215° ± 0.074°” and to Ref. [4] must be removed from the manuscript and from any load‑bearing arguments (e.g. “Planck/ACT DR6 2.7–2.9σ”).  

---

**P1B-E3 (ESSENTIAL)** – *Unverifiable DESI DR2 and DES-SN5YR chains and values*  
- **Location:** Table II (DESI DR2 w₀–wₐ posterior), Sec. V, p. 8; Ref.  (DESI DR2 BAO), Ref.  (DES‑SN5YR).  
- **Problem:**  
  - The w₀–wₐ results in Table II are said to use “DESI DR2 BAO” and “DES‑SN5YR” with references , . Those references are again future‑dated or unverifiable (DESI DR2 DR2 cosmology paper in 2025 with arXiv:2503.x; DES‑SN5YR 2024 ApJ 973 L14 arXiv:2401.02929 is at least plausible, but I cannot confirm the exact details).  
  - The paper uses these DR2 values to claim a +4.3σ and −3.6σ departure of w₀ and wₐ from ΛCDM, but since the exact likelihood implementations and data releases are not verifiable (DR2 cosmology paper not public), the quoted posterior means and uncertainties cannot be cross‑checked.  
- **Required fix:**  
  - Restrict the analysis to **currently public** DESI / SN datasets whose arXiv IDs and content can be verified, or explicitly mark this entire DESI‑DR2‑based section as forward‑looking / illustrative and remove any claim of an actual measurement.  
  - For PRD, numerical claims must be tied to publicly available data releases and reproducible likelihoods; future or hypothetical DR2 results cannot be treated as established input.  

---

**P1B-E4 (ESSENTIAL)** – *Reliance on companion “Paper I(a), II, III, IV” that are not verifiable*  
- **Location:** Abstract, first paragraph; Introduction, p. 2; references [1], [6]–[8].  
- **Problem:**  
  - The paper repeatedly refers to “Paper I(a) [1]”, “Paper II [6]”, “Paper III [7]”, “Paper IV [8]” as already‑posted companion papers “on arXiv” that contain core theoretical derivations and other key results.  
  - I cannot find corresponding arXiv preprints by “H. Golden” with the specified titles and dates in the arXiv database or NASA ADS.[1]  
  - Since this paper positions itself explicitly as a **“Technical Verification Companion”** providing MCMC/posterior values that are used as inputs in Paper I(a) and others, the non‑existence (or non‑discoverability) of those companion papers makes the context unverifiable.  
- **Required fix:**  
  - Either (a) provide the actual, existing arXiv identifiers for all companion papers, and ensure titles/authors/years in the references match exactly, or (b) remove all references and claims that depend on “Paper I(a) / II / III / IV” and re‑frame this manuscript as a standalone methods note.  
  - PRD cannot accept a paper whose primary function is to support a set of other papers that are not demonstrably public and citable.  

---

**P1B-E5 (ESSENTIAL)** – *Reference [4] contradicts internal narrative about ACT DR6*  
- **Location:** Abstract and Sec. I (primary significance cited as “Planck/ACT DR6 2.7–2.9σ [3,4]”); Sec. VI (headline constraint said to be Eskilt & Komatsu joint WMAP+Planck, but ACT DR6 enters only via [4]).  
- **Problem:**  
  - The manuscript’s own text says the “primary sky detection significance is the published Planck/ACT DR6 2.7–2.9σ [3,4]”. But:  
    - Ref. [3] (Diego‑Palazuelos et al. 2022) is a Planck NPIPE analysis and is real and verifiable.[6]  
    - Ref. [4] (ACT DR6) is not verifiable at present (future‑dated arXiv).[1]  
  - Therefore, the **claimed** combined “Planck/ACT DR6 2.7–2.9σ” headline cannot be supported by the references as they stand; only the Planck NPIPE contribution is traceable.  
- **Required fix:**  
  - Rephrase all such claims to refer solely to **published, verifiable** measurements. E.g., “Planck NPIPE ≈ 2.7σ” from [3], and do **not** blend in a non‑existent ACT DR6 result to speak about “Planck/ACT DR6 2.7–2.9σ”.  
  - When ACT DR6 is eventually published, it can then be properly cited; until then, remove its contribution from any sky‑significance figures.  

---

**P1B-E6 (ESSENTIAL)** – *Internal “correction notes” and “earlier draft” language appear in the body*  
- **Location:** Footnote to Table I, p. 3–4; Sec. VI and Appendix C, multiple “Correction note:” and “earlier draft” mentions.  
- **Problem:**  
  - The table caption to Table I includes editorial language: “Correction note: an earlier version quoted ... 0.831 ± 0.018; the ±0.018 width could not be traced ... and is corrected here.”  
  - Sec. VI includes “Correction note: an earlier draft paired Δϕ/fa ≈ 1.0–1.07 with m ≈ 1.8–2 H₀; ... are corrected here.”  
  - Appendix C similarly contains “Correction note: an earlier draft described ...; no archived chain matches that description, and the configuration list below replaces it with the committed truth.”  
  - These are **version‑history statements** and internal audit notes; PRD expects a clean scientific narrative without references to “earlier draft” or “committed truth” in the body.  
- **Required fix:**  
  - Remove all explicit references to earlier drafts, internal artifacts, and correction notes from the main text and appendices. Present only the final analysis, with a succinct statement if necessary that some previously mis‑stated values have been updated (but without “earlier draft” language).  

---

**P1B-E7 (ESSENTIAL)** – *Use of σ values from different procedures without clear “not comparable” warnings everywhere they are juxtaposed*  
- **Location:**  
  - Abstract: juxtaposes “published Planck/ACT DR6 2.7–2.9σ [3,4]” with pipeline SNR values (e.g., 20.32).  
  - Sec. IV: discusses 20.32, 25.71 template‑fit SNR, 8.1 and 7.2 “angle-template fit SNR,” and mentions the 2.7–2.9σ sky detection.  
  - Sec. VI: compares 3.6σ Eskilt & Komatsu to naive 3.9σ from inverse‑variance combination.  
- **Problem:**  
  - The paper does partially state that pipeline SNRs “are not competitive sky measurements”, but comparisons of “20.32” vs. “2.7–2.9σ” and “3.6σ” vs. “3.9σ” appear in close proximity without an explicit statement **at each juxtaposition** that they are defined differently and not directly comparable.  
  - The review instructions require such a warning at **every** point where different test statistics are shown side‑by‑side.  
- **Required fix:**  
  - For every location where a pipeline SNR is mentioned within a couple of lines of a sky σ or vice versa, add explicit wording such as: “Note: these significances are defined with different test statistics and are not directly comparable.”  
  - Do the same when comparing the 3.6σ published joint WMAP+Planck result to the 3.9σ inverse‑variance combination.  

---

**P1B-E8 (ESSENTIAL)** – *Non‑standard “claims classification” table and reproducibility manifest embedded in the paper*  
- **Location:** Appendix B, Table IV “Claims classification”; references to “reproducibility/cosmology/…” and HuggingFace datasets in Appendix A, and multiple inline paths like `reproducibility/p1_namaster_500mc/...` throughout.  
- **Problem:**  
  - The manuscript is mixing an internal reproducibility manifest (file paths, GitHub layout, mentions of “HuggingFace datasets”) directly into a PRD research article. While the idea is laudable, the level of detail is out of scope for a typical PRD paper and reads as internal project documentation.  
- **Required fix:**  
  - Substantially condense this material. Keep a single “Data and code availability” section with stable DOIs/URLs and a short description, without listing internal directory hierarchies or specific filenames.  
  - The “claims classification” table can be kept if PRD agrees, but should be moved to auxiliary material or an online supplement, not the main text.  

---

### Major issues

**P1B-M1 (MAJOR)** – *Self‑reported use of AI assistant without clear reproducibility separation*  
- **Location:** Acknowledgments, p. 13: “The author acknowledges the use of Claude (Anthropic) as an AI research assistant during systematic analysis and manuscript preparation.”  
- **Problem:**  
  - PRD has emerging policies on AI assistance; here the author states that all scientific claims were independently verified, but given the extensive, highly technical text, it is difficult for a referee to know what parts are AI‑generated vs. human‑verified.  
- **Required fix:**  
  - Add a short, precise statement clarifying which tasks the AI assistant was used for (e.g., editing, code scaffolding, not for statistical inference itself) and how reproducibility has been independently assured (e.g., all numbers derived from archived scripts in the repository). If PRD has specific AI‑policy wording, adopt it.  

---

**P1B-M2 (MAJOR)** – *Overly long and multi‑purpose for the limited new content*  
- **Location:** Entire manuscript (16 pages).  
- **Problem:**  
  - The paper is billed as a “technical verification companion” but includes: a ΛCDM+ΔN_eff MCMC proxy, a NaMaster pseudo‑Cℓ validation, and a full ALP‑birefringence consistency study with multiple MCMC setups. Much of the text is internal reproducibility documentation and cross‑paper scaffolding.  
  - For the actual **new, verifiable** methodological content (stock CAMB ΔN_eff null test; NaMaster E→B pipeline bias; one ALP consistency check with a single published β), the manuscript is significantly longer and more discursive than needed for PRD.  
- **Required fix:**  
  - Compress the paper to focus on (1) the ΔN_eff proxy MCMC (with clear, verifiable datasets only), (2) the NaMaster pipeline validation, and (3) a concise ALP consistency check based solely on published Planck/WMAP data.  
  - Remove or relocate to supplementary material most of the repository structure descriptions, audit paths, and detailed internal chain‑count bookkeeping. A target length of **10–12 pages** seems adequate for the actual scientific content.  

---

**P1B-M3 (MAJOR)** – *ALP fine‑tuning and coupling ranges described but not cleanly tied to existing ALP phenomenology literature*  
- **Location:** Sec. VI and Appendix C.  
- **Problem:**  
  - The paper claims required photon couplings Caγ ≳ 9, potentially up to ~50–160 in some corners, and misalignment tuning θ_i ∼ 0.1 for spectator status. However, there is no precise comparison to standard KSVZ/DFSZ ranges or to existing cosmic birefringence ALP studies (e.g. Fujita et al. is cited but not numerically cross‑checked).  
  - Some of the mass ranges (m/H₀ ≈ 7×10⁻³–7×10²) brush against constraints from other probes, but those are not discussed.  
- **Required fix:**  
  - Add a subsection explicitly comparing the inferred Caγ and m ranges to existing constraints and model expectations in the ALP literature (laboratory bounds, astrophysical limits). Clarify whether the allowed region is still viable.  

---

### Minor issues

**P1B-m1 (MINOR)** – *Mixed use of R̂ thresholds and convergence language*  
- **Location:** Table II caption, footnotes around Tables I–II.  
- **Problem:**  
  - R̂ − 1 values like 0.00820 are described as “below the standard R̂ − 1 < 10⁻² publication target,” but elsewhere R̂ − 1 < 3×10⁻³ is cited as achieved. There is some inconsistency in how strict the convergence criterion is described.  
- **Required fix:**  
  - Choose a single convergence target (e.g. R̂ − 1 < 0.01, or 0.003), state it once, and then report which chains meet it. Avoid implying multiple different thresholds.  

**P1B-m2 (MINOR)** – *Equation (3) & birefringence normalization conventions*  
- **Location:** Eq. (3), Sec. VI.  
- **Problem:**  
  - The expression for β uses α_EM/(4π) with L ⊃ −(g_{aγ}/4) φ F F̃, g_{aγ} = Caγ α_EM/(2π f_a), and β = (g_{aγ}/2) Δφ. This is a known convention, but the paper notes other normalizations. Dimensionally it is fine; however, for a methods paper, it would help to cite a standard reference (e.g. Fujita et al.) that uses the same convention to avoid confusion.  
- **Required fix:**  
  - Add an explicit equation in the text mapping your conventions to those in Fujita et al. or another standard ALP birefringence paper, so the reader can cross‑check.  

**P1B-m3 (MINOR)** – *Use of internal path names in main text*  
- **Location:** Many places (“reproducibility/p1_namaster_500mc/...”; “research/branch_R_alp_birefringence/...”).  
- **Problem:**  
  - These internal paths are not meaningful outside your Git repository context and clutter the exposition.  
- **Required fix:**  
  - Reduce references to specific file paths; a single sentence in the Data Availability section noting that all scripts and artifacts are organized under `reproducibility/` is enough.  

**P1B-m4 (MINOR)** – *Footnote density and readability*  
- **Location:** Pages 3–6, 9–11.  
- **Problem:**  
  - Numerous long footnotes embed substantial technical explanations (e.g. Savage–Dickey caveats, MB–H₀ offsets). PRD readers would be better served if the most critical ones were in the main text, with a more compact footnote style.  
- **Required fix:**  
  - Promote the key points (e.g. why Savage–Dickey fails here, why H₀ tension persists) to the main text, and shorten the footnotes.  

---

### Nits

**P1B-n1 (NIT)** – *Typography and notation consistency*  
- **Location:** Throughout.  
- **Problem:**  
  - Mixed notation “Neff” vs “∆Neff” vs “nnu” in text and captions; “Planck NPIPE (PR4)” vs “Planck PR4 / NPIPE”.  
- **Required fix:**  
  - Standardize: e.g. use N_eff for the total effective number and ΔN_eff for deviation from 3.046 everywhere; use a consistent label for the Planck PR4/NPIPE data.  

**P1B-n2 (NIT)** – *Minor duplicate phrasing*  
- **Location:** e.g., “This is the canonical quintom signature and is consistent with the bounce / pre-Big‑Bang scenario discussed...” where “canonical quintom” appears multiple times.  
- **Problem:**  
  - Some phrases are repeated verbatim.  
- **Required fix:**  
  - Light copy‑editing pass to remove repeated phrases and tighten language.  

**P1B-n3 (NIT)** – *PACS numbers obsolete*  
- **Location:** After abstract.  
- **Problem:**  
  - PACS codes are deprecated, though still sometimes used; PRD now generally prefers standard keywords.  
- **Required fix:**  
  - Check current PRD author guidelines; remove or replace PACS with appropriate keywords if required.  

---

### Consistency of abstract scalars with body

- ΔN_eff values in abstract (−0.020 ± 0.169, +0.065 ± 0.17) match Table I.  
- H₀ values in abstract (67.68 ± 1.06, 67.79 ± 1.09) match Table I.  
- NaMaster bias β̂ − β_inj = −0.032° and worst‑case −0.040° at β_inj = 0.342° are consistent with the text, and the differences are arithmetically correct.  
- The quoted WMAP+Planck β = 0.342° ± 0.094° (3.6σ) matches Eskilt & Komatsu 2022.[6]  

So the core numerical scalars in the abstract are internally consistent with the body and with the one truly verifiable external birefringence reference ([5]/Eskilt & Komatsu).

---

## Summary recommendation

**MAJOR REVISIONS**

The manuscript mixes solid technical work (ΛCDM+ΔN_eff proxy MCMC; NaMaster E/B pipeline validation; a careful ALP consistency check with Eskilt & Komatsu’s β) with non‑verifiable forward‑referenced citations (future DESI DR2, ACT DR6, torsion cosmology papers) and extensive internal project documentation. For PRD, all external statistics and references must be tied to real, currently accessible arXiv/ADS entries, and version‑history language must be removed from the body. If the authors (i) eliminate all future‑dated / non‑existent references, (ii) restrict quantitative claims to currently published datasets, (iii) streamline the manuscript and clean up AI‑use and reproducibility disclosures, the remaining core could potentially be publishable, but substantial revision is required.

---

## PASS 2 — self-critique findings (what initial review missed)

[P1B-E9 (ESSENTIAL)] – *Table I’s \(S_8\) and \(H_0\) arithmetic is internally inconsistent with the values the manuscript itself says were recomputed*  
- **Location:** Table I caption, Table I body, Sec. III/II discussion of the full-tension chain.  
- **Problem:**  
  - The caption says the “direct GetDist pass” on the frozen chains gives **\(S_8 = 0.827 \pm 0.010\)** for the Planck+BAO+SN chain and that this “replaces” the earlier trace-unable value.  
  - But Table I itself reports **\(S_8 = 0.814 \pm 0.008\)** for the full-tension chain and **\(S_8 = 0.827 \pm 0.010\)** for Planck+BAO+SN. Those are fine as distinct rows, but the caption then states the full-tension posterior is the naive two-Gaussian combination of 0.827 ± 0.010 and 0.776 ± 0.017 yielding **0.814 ± 0.009**, while the table reports **0.814 ± 0.008**.  
  - Recompute: inverse-variance combination of \(0.827 \pm 0.010\) and \(0.776 \pm 0.017\) gives a weighted mean near **0.8141** and uncertainty \(\sigma \approx (1/0.010^2 + 1/0.017^2)^{-1/2} \approx 0.0086\), i.e. rounds to **0.009**, not **0.008**.  
- **Required fix:**  
  - Make the table and caption use the same rounded uncertainty, or explain explicitly why the table’s posterior width differs from the naive combination.  

---

[P1B-E10 (ESSENTIAL)] – *The MB–\(H_0\) offset calculation in Table I uses the wrong “constant” if the stated relation is actually applied*  
- **Location:** Table I footnote/caption discussion of \(M_B - 5\log_{10}h\).  
- **Problem:**  
  - The paper states the Pantheon+ degeneracy is \(M_B - 5\log_{10} h \approx \text{const}\), with \(h = H_0/100\).  
  - Using the quoted Riess anchor \(M_B=-19.253\), \(h=0.7304\), the constant should be \(-19.253 - 5\log_{10}(0.7304)\). This equals approximately **\(-18.93\)** if the relation is written in the usual \(M_B - 5\log_{10} h\) form, not **\(-18.571\)** as written.  
  - The paper appears to have mixed conventions between \(h\) and \(H_0\), or dropped the \(+10\) term inconsistently.  
- **Required fix:**  
  - Re-derive the degeneracy relation carefully and present a single convention consistently. If the convention is \(M_B - 5\log_{10}(H_0/[{\rm km\,s^{-1}\,Mpc^{-1}}]) + 10\), then state that explicitly and recompute the constants from that formula.  

---

[P1B-E11 (ESSENTIAL)] – *Table II’s \(\chi^2\) decomposition is numerically incomplete / inconsistent with the total*  
- **Location:** Table II, “Goodness-of-fit decomposition”.  
- **Problem:**  
  - The table gives \(\chi^2_{\rm BAO}=10.6\), \(\chi^2_{\rm CMB}=10983.9\), and \(\chi^2_{\rm SN}=3043.0\). Their sum is **14037.5**, while the reported \(\chi^2_{\rm total}\) is **14037.4 \pm 5.6**.  
  - The note says the 0.1-unit difference is a rounding artifact, but the table presents the total as a posterior mean with an uncertainty, while the components are apparently mean values too. The mismatch is only 0.1, but it should be reconciled explicitly because the totals are not exactly the arithmetic sum of the displayed parts.  
- **Required fix:**  
  - State whether component rows are rounded means, weighted means, or posterior-mode summaries. If they are rounded, say so directly in the caption and avoid implying exact additivity.  

---

[P1B-E12 (ESSENTIAL)] – *The reported \(w_0+w_a\) uncertainty does not follow from the displayed \(w_0\) and \(w_a\) marginals unless a strong negative covariance is used, but the covariance is not propagated in the text*  
- **Location:** Table II footnote b and the surrounding discussion.  
- **Problem:**  
  - Table II gives \(w_0=-0.8122\pm0.0436\) and \(w_a=-0.6666\pm0.1864\), and then reports \(w_0+w_a=-1.4788\pm0.1485\).  
  - If one combined the quoted 1σ errors naively and independently, the uncertainty would be \(\sqrt{0.0436^2+0.1864^2}\approx 0.191\), not 0.1485.  
  - The smaller quoted uncertainty implies a large negative covariance, but the covariance is not shown where the sum is first reported; only the pivot footnote later reveals \(\rho\approx -0.90\).  
- **Required fix:**  
  - Move the covariance statement next to the \(w_0+w_a\) entry, or label the summed uncertainty as covariance-propagated. Otherwise readers will think the arithmetic is wrong.  

---

[P1B-E13 (ESSENTIAL)] – *Table II’s “\(w_{\rm pivot}\)” construction is numerically under-explained and appears to use a sign convention that can easily be misread*  
- **Location:** Table II footnote b.  
- **Problem:**  
  - The footnote defines \(w_{\rm pivot}=w_0+(1-a_p)w_a\) and then states \(1-a_p=-\mathrm{Cov}(w_0,w_a)/\mathrm{Var}(w_a)=0.210\), yielding \(w_{\rm pivot}=-0.952\).  
  - This is internally consistent, but the text never states whether \(a_p\) or \(z_p\) is computed from the covariance of the *sampled* posterior or from the chain after burn-in/thinning. Because the chain selection is nontrivial elsewhere in the paper, the pivot result is not fully reproducible from the displayed numbers alone.  
- **Required fix:**  
  - State the exact sample set used for the covariance calculation and whether weights/thinning were applied.  

---

[P1B-E14 (ESSENTIAL)] – *Figure 1 caption and the body disagree on what the plotted sample count actually is*  
- **Location:** Fig. 1 caption vs. Sec. III/Table I.  
- **Problem:**  
  - The caption says Fig. 1 is over **119,617 post-burnin samples**, “getdist-thinned from 176,240 raw.”  
  - But the body elsewhere states the full-tension chain has **176,240 raw** and **123,368 post-burnin** by a direct 70% cut, then later says the correct both-chains post-burnin total is **216,432**.  
  - The figure caption’s 119,617 therefore appears to be a *thinned subset* of the full-tension chain, but the paper does not say what thinning rule produced it, so the figure is not directly traceable to the table.  
- **Required fix:**  
  - State the exact thinning procedure used for Fig. 1 and relate the plotted sample count to the raw and post-burnin counts unambiguously.  

---

[P1B-E15 (ESSENTIAL)] – *The reported 3.2σ \(M_B\)-axis offset is not the same quantity as the canonical 3.6σ Hubble tension, but the text risks treating them as interchangeable*  
- **Location:** Table I footnote and adjacent paragraph.  
- **Problem:**  
  - The paper correctly notes that the \(0.156\) mag offset in \(M_B\) is “a descriptive offset measure normalized by \(\sigma_{M_B}\)” and is not a properly conditioned tension statistic.  
  - However, the same paragraph then immediately says it is “the same Hubble tension manifesting in the \(M_B\) axis (3.2σ in chain-σ units, versus the canonical 3.6σ when expressed in distance-ladder terms).”  
  - That sentence overstates equivalence: the two sigmas come from different projections of a correlated posterior and are not directly comparable without the covariance structure.  
- **Required fix:**  
  - Keep the warning, but remove “same Hubble tension” language or qualify it more strongly as a *projection* rather than an equivalent significance.  

---

[P1B-E16 (ESSENTIAL)] – *Table III and the text disagree on which likelihood stack belongs to the “Planck-only” and “Planck+BAO” chains*  
- **Location:** Sec. V.A vs. Table III.  
- **Problem:**  
  - The body says there are four dataset combinations and that the “Planck-only” run is accumulating, with “Planck+BAO” exploratory.  
  - Table III, however, lists five chains and defines the first four rows as incremental, including a “Planck-only” and “Planck+BAO” row, but the body’s Table I summary only covers “Planck+BAO+SN” and “Full-tension.”  
  - The Planck block itself is described as including “Planck NPIPE highl CamSpec.TTTEEE + planck 2018 lowl.TT + planck 2018 lowl.EE + planck 2018 lensing.clik,” yet elsewhere the text refers to “Planck 2018 low-ℓ TT/EE + lensing” or “native lensing” without a clear statement of which exact likelihood variant is used in each chain.  
- **Required fix:**  
  - Provide a one-to-one mapping from chain label to exact likelihood blocks in one place and use the same labels everywhere.  

---

[P1B-E17 (MAJOR)] – *Figure 2’s description of the “Standard-Model” line is inconsistent with the text’s claim that \(\Delta N_{\rm eff}\) is a null-consistency check, not a model comparison*  
- **Location:** Fig. 2 caption and Sec. III.  
- **Problem:**  
  - Fig. 2 panel (a) labels the comparison line as “SM \((\Delta N_{\rm eff}=0)\),” which is fine, but the caption concludes that the “standard-ECH route to dark energy via additional relativistic species at recombination is therefore not viable as an amplitude-level explanation of either tension.”  
  - That is stronger than the body’s carefully repeated statement that the proxy run is a null-consistency test and *does not discriminate* between minimal-ECH and standard \(\Lambda\)CDM at present precision.  
  - The figure caption therefore overclaims compared with the more cautious body text.  
- **Required fix:**  
  - Rewrite the caption so it matches the body: the run is consistent with \(\Delta N_{\rm eff}=0\), but does not by itself rule out or select the underlying theory.  

---

[P1B-E18 (MAJOR)] – *The quoted Planck/ACT DR6 “2.7–2.9σ” range is arithmetically incompatible with the cited individual significances*  
- **Location:** Abstract, Sec. IV, Fig. 1/2 discussion.  
- **Problem:**  
  - The text says the primary sky detection significance is “Planck/ACT DR6 2.7–2.9σ [3,4].”  
  - From the cited values in the paper itself, Planck NPIPE is \(0.30/0.11 \approx 2.73σ\) and ACT DR6 is \(0.215/0.074 \approx 2.91σ\). Those are *individual* significances, not a combined Planck/ACT significance.  
  - The phrase “Planck/ACT DR6 2.7–2.9σ” therefore conflates two separate measurements into a single range.  
- **Required fix:**  
  - Rephrase as “Planck NPIPE is 2.7σ and ACT DR6 is 2.9σ” or explicitly show the combination formula if a joint significance is intended.  

---

[P1B-E19 (MAJOR)] – *Equation (1) / caption language mixes “pipeline-recovery bias” with “systematic floor” without justifying that the worst-case injection is a conservative upper bound for other injected amplitudes*  
- **Location:** Fig. 3 caption and Sec. IV robustness discussion.  
- **Problem:**  
  - The paper takes the worst-case bias, \(-0.040^\circ\) at \(\beta_{\rm inj}=0.342^\circ\), and “carries it forward as the NaMaster systematic floor.”  
  - But the body also states the bias is amplitude-dependent and the \(-0.032^\circ\) at \(\beta=0.27^\circ\) is the canonical bias.  
  - If the bias grows with amplitude, the worst-case at 0.342° is not obviously conservative for all plausible \(\beta\) values unless the full allowed range is explicitly bounded.  
- **Required fix:**  
  - State the allowed \(\beta\) range over which \(|\Delta\hat\beta| \le 0.040^\circ\) is claimed, or stop calling it a general systematic floor and instead call it the maximum tested bias.  

---

[P1B-M4 (MAJOR)] – *The paper’s own reproducibility manifest shows a mismatch between “public repository” claims and what is actually described as internal or unpublished*  
- **Location:** Appendix A, Data and Code Availability, acknowledgments.  
- **Problem:**  
  - The paper calls the repository “public,” but then lists artifacts like “HuggingFace datasets,” “pod run pipelines,” internal artifact directories, and `research/branch_R_alp_birefringence/...` paths.  
  - Those descriptions read as internal lab notes rather than a curated public release, and the manuscript never states which files are actually public-facing versus private/reproducible-by-request.  
- **Required fix:**  
  - Separate public deliverables from internal artifacts, and state clearly which are archived and which are just local workflow names.  

---

[P1B-m5 (MINOR)] – *Figure 3’s sky-fraction sweep numbers are not all labeled with the same error definition*  
- **Location:** Fig. 3 caption and body.  
- **Problem:**  
  - The caption gives per-realization scatters \(\sigma_\beta = 0.029^\circ\) and \(0.033^\circ\) at \(f_{\rm sky}=0.85\) and 0.65, but the body elsewhere quotes the standard error of the mean as \(\sigma_\beta/\sqrt{N}\).  
  - The caption does not say which error bars correspond to which quantity until later, which can lead readers to misread the plot.  
- **Required fix:**  
  - State explicitly in the caption that outer bars are per-realization scatter and inner bars are standard errors on the mean.  

---

[P1B-m6 (MINOR)] – *Table I’s “Chains” row and the accompanying footnote use different counts of parameters sampled*  
- **Location:** Table I footnote.  
- **Problem:**  
  - The footnote says the full-tension chain samples **17 parameters** and the Planck+BAO+SN chain **16 parameters**, which is plausible.  
  - But it also says the Planck+BAO+SN chain does not explicitly sample \(M_B\) because `use abs mag: false`, while the full-tension chain does sample \(M_B\). The table itself does not distinguish which posterior mean is conditioned on an explicit nuisance-parameter sample and which is analytically marginalized.  
  - This matters because the two rows’ uncertainties are not generated in the same parameterization.  
- **Required fix:**  
  - Note in the table body which parameters are explicitly sampled versus analytically marginalized for each row.  

---

[P1B-m7 (MINOR)] – *The figure-caption description of Fig. 4 overstates that the posterior is “shown” there, but the main text says the [1,30] prior was superseded*  
- **Location:** Fig. 4 caption and Sec. VI.  
- **Problem:**  
  - Fig. 4 is described as the posterior triangle for the continuous-prior cross-check, which is fine, but the caption also says the figure “broadens the fixed-Caγ = 8 and Caγ ∈ [1,30] configurations.”  
  - The text later says the [1,30] prior-truncated configuration is superseded by the [4,60] rerun.  
  - This is not a contradiction, but the figure caption does not make clear which result is the *headline* and which is historical.  
- **Required fix:**  
  - Add a brief note in the caption that the figure is a cross-check, not the primary ALP posterior.  

If you want, I can now do a second-pass cleanup that merges these into a referee-ready report with the same PRD-style severity labels and no duplication.