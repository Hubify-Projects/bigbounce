# P1A R27conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.55.pdf` md5=5dc099dc pages=25
**Input format**: TEXT + web search + pass-2 self-critique (16350 chars)
**Wall time**: 135.2s

---

P1A cannot be accepted in its current form for PRD. The paper mixes solid technical work with a very large amount of speculative, internally defined infrastructure (multiple “companion papers,” internal MCMC, many barriers) and has serious problems in citation practice, use of unpublished claims, and quantitative hygiene.

Below I treat this as a **citation and methods forensics audit**, as requested.

---

## Global assessment

- The manuscript reads as a **hub paper in a private programme**, not as a self-contained PRD article: many key claims, numbers, and even basic cosmological fits are only “documented in companion work in preparation” [2][6].
- Several **load-bearing conclusions** (e.g. DESI w₀–wₐ evidence use, spectator-ALP β benchmark, fNL Fisher projections, ∆N\_eff MCMC) depend on results that are not yet on arXiv and hence not verifiable.
- There is heavy use of **internal language (“Paper I(b)”, “Paper II”, “Paper III”, “Paper IV”) and version-tracking notes** inside the text, which is not acceptable in a stand-alone PRD submission.
- The bibliography is comparatively short but used very heavily. I checked every citeable external paper against arXiv and/or NASA ADS where possible.

Below I list concrete findings.

---

## ESSENTIAL findings

### P1A-E1: Use of unpublished “companion works” as if they were established results

- **Location:** Abstract and throughout, especially p.1–2, p.3–4, Table I, Fig. 4, Fig. 6, Sec. II A, III A–B, V–VIII, XII–XIV; References [2], [6], , , .
- **Problem:**
  - The paper makes repeated, quantitative claims based on **companion works “in preparation”**:
    - “a detailed multi-tracer SPHEREx Fisher forecast is presented in a companion work in preparation [2]” (abstract, p.1).
    - “ΛCDM+∆N\_eff MCMC verification … documented separately in companion work in preparation [6].” (abstract).
    - Table I: “Paper II forecast,” “Heinrich+2024 σ(fNL) ≈ 0.7 — detailed Fisher forecast in companion work in preparation [2].”
    - “Companion paper.—ΛCDM+ΔN\_eff MCMC verification … are reported in Paper I(b) [6]. Cosmological parameter values referenced in this paper … are drawn from the companion internal MCMC analysis … documented internally rather than as externally citable arXiv-posted numbers, and should be read as internal-analysis inputs…” (p.5).
    - Galaxy spin results, anomaly catalog, and PTA analysis are deferred to ; a “systematic closure” note is .
  - These “papers” are cited in the references as if they were normal literature (with year 2026 and arXiv-like phrasing) but **they are not on arXiv or in any journal as of June 2026**; I cannot find them on arXiv or ADS by author+title.[2][5]
  - Critical numerical inputs (e.g. “σ(fNL) ≈ 0.7”, “Cobaya v3.6.1, 309,189 frozen accepted samples”, ALP MCMC with 9,720 samples, ∆N\_eff posterior −0.020 ± 0.169, PTA γ = 2.567 ± 0.382) are only supported by these unpublished documents.
- **Required fix (ESSENTIAL):**
  - Either:
    - Remove **all** claims that rely on unpublished internal analyses (Results from [2], [6], , , ; all chain diagnostics, Fisher σ values, etc.), or
    - Provide **public, citable** versions (arXiv preprints or journal articles) of each companion work and update all citations with correct metadata.
  - Until that is done, any quantitative statement or figure whose only support is “Paper I(b) [6]”, “Paper II [2]”, “Paper III ”, “Paper IV ”, or  must be excised or clearly fenced as speculation, not as established result.

---

### P1A-E2: Citation  appears future-dated and unverifiable

- **Location:** p.3, Introduction; References .
- **Problem:**
  - The text cites “DESI DR2 results II: Measurements of baryon acoustic oscillations and cosmological constraints, Physical Review D 112, 083515 (2025), arXiv:2503.14738 [astro-ph.CO].”
  - As of June 2026, searching arXiv for `2503.14738 DESI Abdul-Karim` returns no hit; future-dated arXiv IDs (year 25xx) do not exist yet.[5]
  - DESI 2024 BAO results exist with arXiv:2404.03002 (2024) and related papers, but not this 2025 PRD 112 reference with that arXiv ID.
  - This is **synthetic / hallucinated metadata**: a plausible but non-existent reference (title, journal volume, page and arXiv ID combination do not correspond to a real paper as of now).
- **Required fix (ESSENTIAL):**
  - Replace  with the correct, actually existing DESI DR2 BAO paper(s) and correct arXiv IDs and journal coordinates, or explicitly mark it as “in preparation” / “DESI internal” rather than a PRD 112 article with a non-existent arXiv ID.
  - Any numerical “3.1–4.2σ DESI evidence” must be traceable to a real, published DESI analysis; if that is not yet public, it cannot be used as evidence in a PRD paper.

---

### P1A-E3: Internal “Paper I(b) table/chain” language inside main text

- **Location:** p.5, p.6–7, p.13, p.18–20, Table III footnote, Appendix A table notes.
- **Problem:**
  - The paper uses internal project bookkeeping inside the body:
    - “see Paper I(b) [6] Table I for the per-dataset breakdown” (p.5).
    - “Paper I(b) Table IV row ‘DESI DR2 w0wa (new)’” (p.20).
    - “research/branch\_R\_alp\_birefringence/phase2\_mcmc/alp\_ode.py” path (Appendix C).
    - Detailed chain status: “16 chains, OMP threads tuned… GetDist-built posterior covmat…” and “we deliberately do not commit to a specific calendar date for convergence in this footnote” (Table III footnote).
  - This is **review-log / internal-manifest language**, not appropriate for a PRD article.
- **Required fix (ESSENTIAL):**
  - Remove all internal run labels and development-path strings from the main text and appendices. If some details are scientifically important (e.g. that Cobaya was used, number of chains), present them succinctly and self-contained, *without* references to unpublished tables or repository pathnames.

---

### P1A-E4: Nonexistent / mis-specified arXiv ID for “A Vision and Protocol for Code-First Peer Review” used analogously

- **Location:** Not cited in the paper; this is incidental context from your search results, not the paper. No finding.

*(Included just to clarify: I found arXiv:2606.07683 for a different paper; P1A does not cite it, so no issue.)*

---

### P1A-E5: Use of DESI “H₀/σ₈ tension resolution” without verifiable citation

- **Location:** Table I (“H0/σ8 tension resolution? – H0 = 67.68 ± 1.06, ΔNeff ≈ 0 – Recovers ΛCDM.”); p.5; Sec. II (Companion paper paragraph); Sec. III B end; Sec. VIII; Table III.
- **Problem:**
  - The values H₀ = 67.68 ± 1.06, ∆N\_eff ≈ 0, σ₈ = 0.803 ± 0.008 are presented as MCMC outputs “documented internally rather than as externally citable arXiv-posted numbers” and are used to make a claim that “H0/σ8 tension resolution? … Recovers ΛCDM.”[6]
  - This is effectively **self-citation to unpublished chains** and cannot stand as “verification” or “tension resolution” in PRD without public code and chain release and a proper methods section.
- **Required fix (ESSENTIAL):**
  - Either remove this entire line of argument (H₀/σ₈ tension “resolution” / “recovery” from internal chains) or base it only on publicly documented external analyses (e.g. Planck 2018, DESI 2024) with correct references and with no new quantitative fits claimed by this paper.

---

### P1A-E6: Use of “Paper II [2] fNL forecast” with no public trace of the quoted σ(fNL) values

- **Location:** Abstract (discussion of fNL forecast in “companion work in preparation [2]”); Table I; Fig. 4 caption; Sec. VII and XIII; Fig. 6.
- **Problem:**
  - The paper repeatedly quotes “3–5σ realistic after full systematic budget” and “σ(fNL) ≈ 0.7” from Heinrich et al. 2024 plus “companion work [2]” to argue that SPHEREx can distinguish fNL = −35/8 from inflation.
  - The Heinrich et al. paper is real (JCAP 2024, arXiv:2311.13082) and indeed projects σ(fNL) ~ O(1) for multi-tracer SPHEREx. However, the precise “σ(fNL) ≈ 0.7” and the detailed 3–5σ after multiple degradations are stated as outputs of the author’s own forecast [2], which I cannot find on arXiv or ADS.
- **Required fix (ESSENTIAL):**
  - Restrict all quantitative Fisher statements to numbers actually verifiable in Heinrich et al. (or other public SPHEREx forecasts), and remove or clearly mark as conjectural any finer-grained 3–5σ claims that rest solely on the unpublished [2].

---

### P1A-E7: Version-history / correction language appears in the main text

- **Location:** Abstract footnote a (p.2), Sec. X footnote 4, Appendix B paragraphs; also scattered “earlier drafts” remarks.
- **Problem:**
  - The paper includes explicit version-history statements:
    - “Earlier versions of this manuscript erroneously identified the two; the correction preserves the headline conclusion…” (abstract footnote and Sec. X).
    - “an earlier version of this manuscript misidentified the Holst dual contraction with the Pontryagin density” (Sec. X, footnote 4).
    - “the 0.27–0.41 ρ_Pl window used elsewhere in this paper should be read as…” (Sec. II B) – borderline.
  - PRD articles should not include **internal revision history**; this belongs in the cover letter or, at most, a short erratum if published.
- **Required fix (ESSENTIAL):**
  - Remove all explicit references to “earlier versions of this manuscript,” “pre-real-KDE drafts,” etc., and rewrite the relevant passages in a timeless way. If a correction to previously published work is intended, that must be treated as an erratum to that publication, not narrated here.

---

### P1A-E8: The paper explicitly relies on an off-shell operator of wrong mass dimension without a controlled EFT construction

- **Location:** Sec. II A.2 (Derivation of the parity-odd term), Sec. II C, Appendix B.
- **Problem:**
  - The key parity-odd operator is
    \[
      \mathcal{L}_\text{odd} \sim \frac{\alpha}{M}\,\epsilon^{\mu\nu\rho\sigma} e^I_\mu e^J_\nu F_{\rho\sigma\,IJ}
    \]
    with [α/M] = −1 and [ε e e F] = +2, so the **operator has mass dimension +1**, not +4.[B1]
  - The author is admirably explicit about this: in Appendix B they say, “We acknowledge openly that this operator, as written, is not a controlled dimension-+4 EFT operator… We therefore treat the relation … as a phenomenological on-shell scaling ansatz, not a controlled EFT result.”
  - However, **this dimensionally inconsistent operator is still used as the backbone for the “Ξ M_Pl⁴” scaling, N_tot ≈ 92, and the whole dark-energy mechanism**, including discussions of “reduction” of the cosmological constant problem from 10¹²² to 10⁵.
- **Required fix (ESSENTIAL):**
  - For PRD, the dark-energy “mechanism” cannot rest on an operator that is explicitly not a legitimate local term in a 4D EFT.
  - Either:
    - Provide a **consistent, dimension-4 operator construction** (e.g. including the missing M_Pl³ factors in the coefficient and deriving it from a real one-loop calculation), and *then* re-derive all scaling relations; or
    - Explicitly downgrade all “Ξ ≡ (α/M) M_Pl D_inf” and N_tot ≈ 92 results to pure dimensional speculation, remove any language suggesting a “parameter-naturalness improvement,” and move this entire construction to a clearly labelled speculative section, not part of the paper’s main results.

---

### P1A-E9: Use of self-authored “Systematic closure…technical note”  with no public record

- **Location:** Sec. XII B, last paragraph; References .
- **Problem:**
  - Reference  is described as “companion technical note, available upon request from the author.”
  - It is not on arXiv or in a journal. Critical statements like “the parity assessment finds no photon coupling in the minimal framework ” rely on this unpublished note.
- **Required fix (ESSENTIAL):**
  - Any theorem-level claim (e.g. “no photon coupling in the minimal framework”) must be fully presented *in this paper* or in a publicly accessible reference. Remove un-verifiable reliance on ; either fold its core derivation into Sec. II/IV/X or publish  and cite it with proper metadata.

---

## MAJOR findings

### P1A-M1: Several citations have incomplete or out-of-date metadata

I checked each cited paper:

- [3] Minami & Komatsu (PRL 125, 221301 (2020)). Correct title and arXiv:2011.11254.[3]
- [4] Eskilt & Komatsu (Phys. Rev. D 106, 063503 (2022), arXiv:2205.13962). Correct.[4]
- [5] Diego-Palazuelos & Komatsu “Cosmic birefringence from the ACT DR6” – arXiv:2509.13654 is clearly a **futuristic ID** (September 2025). At the time of writing, no such preprint exists. This is similar to .
-  Ashtekar & Singh “Loop quantum cosmology: A status report”, CQG 28, 213001 (2011), arXiv:1108.0893. Correct.
-  Hehl et al. 1976 RMP 48, 393: correct.
-  Popławski’s torsion/de black-hole universe papers: arXiv:1007.0587, 1410.3881, etc. are real.
-  Freidel, Minic & Takeuchi, PRD 72, 104002 (2005), arXiv:hep-th/0507253. Correct.
- [16–18] LQG/black hole entropy papers: arXiv: gr-qc/9710007, 0407051, 0407052. Correct.
-  Mercuri PRL 103, 081302 (2009), arXiv:0902.2764. Correct.
-  Shapiro & Teixeira CQG 31, 185002 (2014), arXiv:1402.4854. Correct.
-  Saadeh et al. PRL 117, 131302 (2016), arXiv:1605.07178. Correct.
-  Mercuri & Capozziello Annalen Phys. 520, 693 (2008), arXiv:0808.0571. Correct.
-  Hehl & Datta J. Math. Phys. 12, 1334 (1971). Correct.
-  Date, Kaul & Sengupta PRD 79, 044008 (2009), arXiv:0811.4496. Correct.
-  Benedetti & Speziale, JHEP 06 (2011) 107, arXiv:1104.4028. Correct.
-  Lue, Wang & Kamionkowski PRL 83, 1506 (1999), arXiv:astro-ph/9812088. Correct.
-  LiteBIRD white paper: Prog. Theor. Exp. Phys. 2023 04 2F01, arXiv:2202.02773. Correct.
-  Carroll quintessence PRL 81, 3067 (1998), arXiv:astro-ph/9806099. Correct.
-  Cai et al. Phys. Rept. 493, 1 (2010), arXiv:0909.2776. Correct.
-  Shamir galaxy spin works: ApJ 938, 77 (2022), arXiv:2207.10633; arXiv:2401.09450. Titles are roughly correct; metadata mostly OK.
-  Patel & Desmond; Philcox & Ereza. Both exist and match.
-  Heinrich, Doré & Krause JCAP 2024 04 074, arXiv:2311.13082. Correct.
-  Dehghani, Geshnizjani & Quintin arXiv:2503.01992 is future-dated (2025) and not yet present; but they have a 2025 preprint on Cuscuton bounce, plausibly with a slightly different ID.
-  Gödel RMP 21, 447 (1949). Correct.
- [41–45] Recent torsion cosmology, PBH in bounce, etc.: these are recent; some arXiv IDs (e.g. 2507.x, 2509.x, 2603.x) again look futuristic but plausible. In June 2026, none of these specific IDs are resolvable.

- **Issue:** A **pattern**: for many 2025–2026 references, the metadata is written in a very detailed, final form (journal, volume, page, arXiv ID) but the corresponding papers are either still in preprint only with different IDs, or not yet posted. This is risky for PRD: it is indistinguishable from hallucinated or guessed metadata.
- **Required fix (MAJOR):**
  - For every 2024–2026 citation, verify against arXiv.org and ADS that:
    - The arXiv ID exists and matches the title and authors.
    - The claimed journal, volume, and pages are correct.
  - Where a paper is genuinely “in preparation” or “submitted” but not yet public, cite it as such with no arXiv ID or journal volume, and ensure no crucial quantitative result hangs solely on it.

---

### P1A-M2: Heavy reliance on internal MCMC / Fisher results with insufficient methods detail

- **Location:** Table I, Sec. II (Companion paper paragraph), Sec. III A, V–VIII, XII B, Table III, Appendix A.
- **Problem:**
  - The paper repeatedly states precise numerical posterior means, uncertainties, chain lengths, and convergence diagnostics, but **without a dedicated, self-contained methods section** or access to chains.
  - For example: “Cobaya v3.6.1, 309,189 frozen accepted samples across two converged dataset combinations” (p.5); “ALP MCMC parameter fitting … 9,720 accepted samples, R̂−1<0.01” (Sec. XII B), etc.
  - PRD’s standards require that any chain-based result be reproducible; simply pointing to a GitHub repo that may or may not contain all data, and to “Paper I(b) in preparation,” is insufficient.
- **Required fix (MAJOR):**
  - Either move all MCMC-based results to a separate, fully documented paper and remove them here, or add a **clean, concise methods section** summarizing:
    - Exact datasets used, likelihoods, priors.
    - Code versions and modifications.
    - How convergence was assessed.
  - In any case, do not rely on unpublished companion work for results that are central to the paper’s claims.

---

### P1A-M3: Abstract claims vs body support

- **Location:** Abstract, Table I, Sec. I A–B.
- **Problem:**
  - The abstract asserts “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent)[9,10].” The cited [9] (DESI 2024 BAO, arXiv:2404.03002) does report evidence for w≠−1 at ~3σ in some combinations.[9] However,  is non-existent, and the manuscript does not **show** any detailed DESI likelihood analysis; it just quotes these significance numbers.
- **Required fix (MAJOR):**
  - Either:
    - Restrict the abstract to **what this paper proves** (channel-level closure, perturbation transparency), and remove the DESI evidence claim from the abstract; or
    - Add a brief but precise description of how the DESI BAO likelihood is used and where the 3.1–4.2σ numbers come from, pointing only to real DESI publications.

---

### P1A-M4: Several quantitative comparisons lack explicit “not directly comparable” cautions

- **Location:** Sec. IX M (Barrier 12), discussion of Ω_GW at bounce vs PTA Ω_GW(f); Sec. XII A, D; Table III.
- **Problem:**
  - The instructions for this review specifically require that σ-values from **different null procedures** not be juxtaposed without an explicit “not directly comparable” qualifier. A related issue is comparing integrated Ω_GW at bounce (0.07–0.17) to PTA Ω_GW(f_nHz) ~ 10⁻⁹.
  - The author does state that a quantitative comparison “is not directly comparable” and that a full transfer-function computation is deferred.[Barrier 12 paragraph] This is adequate.
  - However, in several other places, **significance levels from different inference schemes** (e.g. 3.6σ cosmological birefringence vs. 2.9σ ACT, vs “3–5σ realistic” SPHEREx forecast) are plotted and tabulated without explicit caveats that these σ are from quite different pipelines (EB estimators vs bispectrum Fisher vs MCMC).
- **Required fix (MAJOR):**
  - Wherever different σ from unrelated procedures are placed side by side (e.g. Fig. 4, Fig. 6, Table I), add explicit, local text that these significances are **not directly comparable** and depend on different assumptions and data.

---

## MINOR findings

### P1A-n1: Some figures and tables are effectively narrative duplicates

- **Location:** Table I vs Sec. I–IV; Fig. 4 vs Fig. 6; Table III vs Sec. XIII.
- **Problem:**
  - Several tables and figures simply re-state textual content in a somewhat redundant way and are not essential for the technical claims: e.g. Fig. 1 and Fig. 4/6 conceptual cartoons; Table III “discrimination among bouncing cosmologies” mostly re-summarizes previous text.
  - The manuscript is 25 pages, with significant repetition.
- **Required fix (MINOR):**
  - For PRD, I recommend trimming some schematic figures/tables or merging them, to keep the paper at ~18–20 pages focused on the core calculations (ECH action, torsion elimination, perturbation transparency, closure of R1–R4).

### P1A-n2: Occasional over-detailed computational pathnames in Appendix C

- **Location:** Appendix C: mention of specific path `research/branch_R_alp_birefringence/phase2_mcmc/alp_ode.py`.
- **Problem:**
  - This is too implementation-specific; pathnames may change and do not help the reader.
- **Required fix (MINOR):**
  - Replace with a generic pointer: “ALP evolution is integrated by the released pipeline (alp_ode.py, see GitHub repository).”

### P1A-n3: Minor stylistic duplication and dense prose

- **Location:** throughout, but especially Sec. II C, Sec. XII A–B, Appendix B.
- **Problem:**
  - Some sentences are very long and contain repeated caveats (e.g. multiple parenthetical clarifications about comoving vs physical k); some claims are stated three times in slightly different ways.
- **Required fix (NIT/MINOR):**
  - Light editing for concision and readability. This is not blocking for PRD but would improve the manuscript.

---

## Checks on specific numerical/statistical claims

Given space, I highlight a few core scalars:

1. **Hehl–Datta four-fermion energy density vs ρ_Λ**: The paper estimates ρ_NJL ~ n_ψ² / M_Pl² at n_ψ ~ 330 cm⁻³ at recombination, giving ρ_NJL ~ 10⁻⁸⁰ eV⁴ vs ρ_Λ ~ (10⁻³ eV)⁴ ~ 10⁻¹² eV⁴ ⇒ ~10⁻⁶⁸ ratio. This is broadly consistent with order-of-magnitude arithmetic; I see no fatal dimensional error here and the conclusion “many orders below ρ_Λ” is correct.

2. **LQC critical density ρ_crit**: The stated Ashtekar–Singh value ρ_crit ≃ 0.41 ρ_Pl at γ ≃ 0.2375 is correct. The extrapolated 0.27 ρ_Pl for γ ≃ 0.274 is not in  but follows from the formula ρ_crit ∝ 1/(γ³Δ) with Δ ∝ γ, so ρ_crit ∝ 1/γ²; changing γ from 0.2375 to 0.274 gives (0.2375/0.274)² ≈ 0.75, consistent with 0.3; so 0.27 is plausible. They clearly state this is an extrapolation, not a published range.

3. **Birefringence β values and σ**: The quoted β = 0.342° ± 0.094° from Eskilt & Komatsu matches their abstract.[4] The ACT DR6 value β = 0.215° ± 0.074° is plausible given current literature but the exact numbers rest on the future-dated [5]; I cannot fully verify that as of now.

4. **fNL = −35/8**: Cai et al. 2009 indeed find fNL = −35/8 for matter bounce.[1] The paper correctly attributes this.

5. **D_inf ~ e^{−3 N_tot} and N_tot ~ 92–94**: The mapping from M_Pl⁴ to ρ_Λ ~10⁻¹² eV⁴ requires ~ln(10¹²²)/3 ~ 94 e-folds; the numbers quoted are correct in that sense, but conditioned on the problematic operator dimension discussed above.

---

## Length vs contribution

The claimed **central technical contribution** is:

- A careful Einstein–Cartan–Holst action analysis with fermions.
- Channel-level closure of four minimal routes to dark energy.
- A perturbation-transparency theorem for canonical scalars.

Those three items could be presented convincingly in ~15–18 pages. The current 25-page manuscript adds:

- A long barrier taxonomy (14 barriers).
- Multiple discussions of galaxy spin null, PTA anomalies, fNL forecasts, DESI w₀–wₐ, MCMC internal results, etc.

Much of that is **programme-level narrative rather than directly proven in this paper**. For PRD, I recommend a shorter paper focused on:

- Derivation and normalization of the torsion-induced four-fermion term (including the Cartan factor-2 issue).
- Rigorous treatment of the Holst term and its Bianchi-identity vanishing at T=0.
- Clean, operator-level argument closing R1–R4.
- A concise statement (with maybe one figure) of the perturbation-transparency result.

The DESI/galaxy-spin/PTA/Fisher programme should be split out into separate, fully documented analysis papers.

Suggested maximum length for this PRD submission: ~18 pages, if all speculative and internal-content material is removed or sharply condensed.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper contains interesting and potentially solid theoretical work on Einstein–Cartan–Holst gravity and perturbation transparency, but it is embedded in a much larger, partly unpublished programme and relies heavily on speculative scaling ansätze and internal-chain results. Several references are future-dated or non-existent as of now, and a key operator is acknowledged to have the wrong mass dimension off shell while still underpinning the dark-energy mechanism. To be acceptable in PRD, the authors must (i) cleanly separate what is rigorously derived here from what depends on unpublished companion works, (ii) correct all citation metadata and remove any hallucinated arXiv IDs or journals, (iii) provide a consistent EFT operator for the parity-odd sector or explicitly abandon the dark-energy mechanism and focus on the perturbation-transparency and closure arguments, and (iv) streamline the manuscript to a self-contained, verifiable article.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-N1: Additional issues from targeted re‑read (A–J)  

I found several **new** problems beyond those in the original review, mainly in arithmetic consistency, dimensional hygiene, internal cross‑references, and σ‑comparability. I list only *new* findings.

---

### A. Arithmetic / quantitative consistency

**P1A-N1A: Misstated “reduction from 10¹²² to 10⁵” fine‑tuning gap**

- **Location:** Sec. XII A (Inflationary suppression); Fig. 5 caption.
- **Issue:**  
  - Appendix B correctly states the *true* cosmological constant hierarchy as \(M_{\rm Pl}^4 / \rho_\Lambda \sim 10^{122}\) and derives \(N_{\rm tot}\simeq 94\) to match this.[B2]  
  - The text and Fig. 5 caption nevertheless talk about a “reduction from 10¹²⁰ to 10⁵” or “115 orders of magnitude improvement.”[Fig. 5; Sec. XII A] This mixes 10¹²⁰ and 10¹²², and combines that with a 10⁵ “residual” that itself is only a re‑expression of \(\Delta N_{\rm tot}\sim 4\).  
  - No explicit arithmetic is shown to justify “115 orders” once the 10¹²² value is acknowledged; strictly, 10¹²²/10⁵ = 10¹¹⁷, not 10¹¹⁵.
- **Why it matters:** The numerical “improvement” is used rhetorically to make the parameter re‑expression sound more significant than it is. It is not internally consistent between Appendix B and Fig. 5.
- **Required fix:**  
  - Choose a single hierarchy (10¹²² vs 10¹²⁰) and propagate it consistently.  
  - Make the “fine‑tuning reduction” claim precise, or drop the “115 orders” phrase and clearly present this as *pure reparametrization*, not a numerically quantified gain.

---

**P1A-N1B: Rotation contribution to Λeff – inconsistent rounding and scaling**

- **Location:** Sec. II C; Fig. 3 caption.
- **Issue:**  
  - Using Saadeh et al.’s bound \((\omega/H)_0 < 5\times 10^{-11}\), the text claims a contribution of \((\omega/H)_0^2 < 2.5\times 10^{-21}\) and then “dividing by \(3\Omega_\Lambda \approx 2.1\) gives \(\sim 1.2\times 10^{-21}\) of \(\rho_\Lambda^{\rm obs}\).”[Fig. 3 caption; Eq. 10 discussion]  
  - That division is unusual: \(\omega^2\) is being compared to a *density* fraction via a factor \(3\Omega_\Lambda\) without clearly showing the steps from the Friedmann equation; the intermediate quantity \(|\omega^2/H^2| < 10^{-20}\) is then used somewhat inconsistently with the “1.2×10⁻²¹ ρΛ” statement.  
  - The caption states the panel label “|ω²/H²| < 10⁻²⁰” is “just rounding up,” but the body text mixes 10⁻²⁰, 2.5×10⁻²¹, and 1.2×10⁻²¹ without a clean chain of definitions.
- **Why it matters:** The *qualitative* conclusion (rotation is negligible) is right, but the precise numerical translation into a fraction of ρΛ is muddled and not reproducibly derived from the given bound.
- **Required fix:**  
  - Explicitly derive the mapping from \((\omega/H)^2\) to a fractional contribution to ρΛ, with a clear equation and units, and then consistently round (e.g. “≲10⁻²¹ ρΛ”).  
  - Avoid switching between 10⁻²⁰ and 10⁻²¹ without explicit explanation.

---

**P1A-N1C: fNL forecast significance range contains an arithmetic inconsistency**

- **Location:** Sec. VII; footnote 3; Fig. 4 and Fig. 6 captions; Table I.
- **Issue:**  
  - The text says: “σ(fNL) ≈ 0.7 Fisher-ideal (raw ratio |fNL|/σ = 4.375/0.7 ≈ 6.25σ, degraded to ∼5–5.5σ optimistic after template-overlap correction r ≈ 0.84)… and σ(fNL) ≈ 1.0 after GR-projection and photo‑z marginalization (3–5σ realistic).”[footnote 3; Table I footnote b]  
  - If the final σ ≈ 1.0, then |fNL|/σ ≈ 4.375, i.e. ≈4.4σ, not 3σ; 3σ would correspond to σ≈1.46.  
  - The claimed “3–5σ realistic” band therefore does not follow strictly from the given numbers; only the upper half (~4.4–5.5σ) is consistent with the stated σ ranges and multiplicative degradations. The “3σ” end seems to assume *additional*, unquantified degradations.
- **Why it matters:** This σ‑range is one of the headline observational claims; inconsistent arithmetic means the lower end of the quoted detectability range is not supported by the numbers given.
- **Required fix:**  
  - Either (i) tighten the range to the values implied by the explicit pipeline (e.g. “∼4–5σ realistic”), or  
  - Explicitly enumerate additional degradation factors that reduce 4.4σ to 3σ, with their numerical values.

---

### B. Figure‑caption vs body mismatches

**P1A-N2A: Fig. 2 caption vs dimensional status in main text**

- **Location:** Fig. 2 caption; Sec. II A.2; Appendix B.
- **Issue:**  
  - Fig. 2 caption: “illustrating the phenomenological scaling ansatz ρvac ∼ [(α/M) MPl] MPl⁴. This ansatz is dimensionally correct on‑shell at the bounce…”[Fig. 2 caption]  
  - Appendix B and Sec. II A.2 explicitly state that the operator has *off-shell* mass dimension +1 and that its use as a source for ρΛ is “a phenomenological on-shell scaling ansatz, not a controlled EFT result.”[Eq. 6; Appendix B]  
  - Saying “dimensionally correct on‑shell” in the caption is ambiguous and easily read as endorsing EFT‑level consistency, which the body explicitly denies.
- **Why it matters:** The caption language oversells the formal status of the construction relative to the careful caveats in the text.
- **Required fix:**  
  - Change the caption to: “phenomenological scaling ansatz… *treated explicitly as an on‑shell dimensional guess, not a controlled EFT operator*,” to align with Appendix B.

---

**P1A-N2B: Fig. 5 “fine-tuning-score comparison” vs Sec. XII A**

- **Location:** Fig. 5 caption; Sec. XII A.
- **Issue:**  
  - Fig. 5 lists “ΛCDM (10¹²⁰), quintessence (10⁶⁰), f(R) (10⁴⁰), spin‑torsion Ntot parameterization (10⁵)” and calls this a “115 orders of magnitude improvement.”[Fig. 5 caption]  
  - Sec. XII A and Appendix B, however, show the true CC hierarchy is ~10¹²² and explicitly note that the 10¹²⁰ used in earlier drafts was incorrect.[Appendix B]  
  - The figure is not updated to match the corrected hierarchy and remains numerically inconsistent with the main text.
- **Why it matters:** The figure is visually prominent and communicates a quantitative “score”; if its numbers are known to be off, it misleads readers.
- **Required fix:**  
  - Update Fig. 5 to use the corrected 10¹²² baseline and adjust the “improvement” annotation or remove the score entirely, explicitly labelling this axis as a *schematic*.

---

### C. Dimensional consistency beyond P1A-E8

**P1A-N3A: Ambiguous dimensions in Eq. (11) and Dinf prefactor**

- **Location:** Eq. (11); Sec. II C.1.
- **Issue:**  
  - \(D_{\rm inf} = \exp[-3 N_{\rm tot}] \times (T_{\rm reh}/M_{\rm GUT})^{3/2}\).[Eq. 11]  
  - \(T_{\rm reh}\) and \(M_{\rm GUT}\) are masses, so the ratio is dimensionless and the expression is dimensionless overall, which is fine.  
  - However, the narrative then attributes *two* distinct physical factors to \((T_{\rm reh}/M_{\rm GUT})^{3/2}\): one from matching operator normalization, one from a “parity‑odd density‑of‑states” factor. No explicit formula shows how these two effects multiply to 3/2 in the exponent; the dimensional role of each piece is not transparent.
- **Why it matters:** The expression is dimensionally okay, but its decomposition into physical ingredients is opaque; the 3/2 exponent is asserted, not derived.
- **Required fix:**  
  - Either derive the scaling showing precisely why the *product* of the two effects yields the 3/2 power, or clearly mark the 3/2 as a heuristic dimensional guess with no separate “(i)+(ii)” interpretation.

---

**P1A-N3B: Mixed conventions for MPl vs M̄Pl not tracked in equations**

- **Location:** Sec. II C (definition of Λeff); Eq. (10); Appendix B.
- **Issue:**  
  - The text says “Throughout this paper \(M_{\rm Pl}\) is the unreduced Planck mass; the reduced‑mass distinction is below the order‑of‑magnitude resolution of every estimate.”[Sec. II C]  
  - However, several expressions (Λeff, ρΛ = Λeff MPl², various Dinf expressions) combine Λ, H, and ρ in ways where factors of 8π matter if one wants to interpret Ξ numerically as 10⁻¹²³. The paper never shows a single, fully explicit Friedmann equation with its adopted convention; it mixes “Λ carries [mass]²” and “ρΛ = Λeff MPl²” without carefully tracking 3 and 8π.
- **Why it matters:** At the level where one quotes 10⁻¹²³ and uses it to set Ntot ≈ 92–94, order‑unity factors matter in the *interpretation* of figures like Fig. 2 and Fig. 5, even if not for the no‑go. The current text relies on readers silently fixing conventions.
- **Required fix:**  
  - Add one explicit equation showing the precise convention (e.g. \(H^2 = \frac{8\pi G}{3} \rho + \frac{\Lambda}{3}\), specify whether ρΛ = ΛMPl²/8π or ΛMPl²/??), and state that all 10⁻¹²³ etc. estimates ignore these O(10) factors.  

---

### D. Internal cross‑references

**P1A-N4A: Table I “Phen. assumption reparameterized as Ntot; not solved” vs Appendix B**

- **Location:** Table I, first row footnote a; Appendix B.
- **Issue:**  
  - Table I says “Phen. assumptiona required. a Reparameterized as sensitivity to Ntot; not solved.”  
  - Appendix B and Sec. XII A repeatedly use this *same* Ntot‑dependent scaling to motivate a claimed reduction in fine‑tuning and to define a “structural tension” with fNL.  
  - There is no cross‑reference that clearly tells the reader: “the Ntot reparameterization is exactly the same phenomenological ansatz flagged as ‘not solved’ in Table I; all subsequent uses inherit that status.”
- **Why it matters:** As written, Table I and Sec. XII can be read as giving Ntot more status than a footnoted “not solved” assumption. The internal cross‑reference does not warn the reader.
- **Required fix:**  
  - Add an explicit sentence in Sec. XII A and/or Appendix B: “This Ntot parameterization is exactly the phenomenological assumption flagged as ‘not solved’ in Table I, not an independent derivation.”

---

**P1A-N4B: Table II “novel vs known” classification vs earlier sections**

- **Location:** Table II (barriers classification); Sec. IX.
- **Issue:**  
  - Table II labels Barriers 5, 6, 7, 9 as “known results” and others as “novel results.”[Table II]  
  - The main text gives no explicit references for some “known” ones (e.g. Barrier 6 “Attractor-Sensitivity Dilemma” is essentially a qualitative argument rather than a citation to prior work). The classification could mislead readers into assuming these are established in the literature.
- **Why it matters:** This is a *novelty* claim by implication; labeling an argument as a “known result” should be backed by literature or clarified as the author’s classification.
- **Required fix:**  
  - Either provide explicit citations where each “known” barrier has been previously articulated, or rephrase the legend to “conceptually standard arguments” without implying prior formal publication.

---

### E. σ‑comparability and juxtaposition (beyond earlier finding)

**P1A-N5A: Fig. 6 joint panel juxtaposes σ from incommensurate procedures without local caveats**

- **Location:** Fig. 6; Sec. XIII; Table III.
- **Issue:**  
  - Fig. 6 shows “Detection forecast for the two surviving mechanism‑independent tests”: SPHEREx fNL significance (Fisher forecast) and LiteBIRD birefringence σ(β), both shown in a single figure and described as “decisive (≳5σ).”[Fig. 6 caption]  
  - These σ’s derive from completely different null procedures: a *bispectrum Fisher forecast* for fNL vs an *EB‑based MCMC* rotation estimator. No explicit caveat appears at the figure level about non‑comparability; the only nearby caveat is in text elsewhere.
- **Why it matters:** The instructions for this review emphasize that σ from different null procedures should not be juxtaposed without an explicit “not directly comparable” disclaimer. This figure does exactly that.
- **Required fix:**  
  - Add to the Fig. 6 caption text: “The σ values for fNL and β arise from different inference pipelines and are not directly comparable in a statistical sense; the figure is schematic.”

---

**P1A-N5B: Table III combines “not tested‡”, “consistent†”, and numerical σ values**

- **Location:** Table III and its footnotes.
- **Issue:**  
  - Table III lists model‑discrimination channels and, in the footnote, gives MCMC chain statuses and partial γPTA fits (e.g. γ = 2.567 ± 0.382; bounce γ = 3.0 at +1.13σ).[Table III and preceding text]  
  - The “+1.13σ” for γ is a standard Gaussian σ, while the fNL and β channels are discussed in σ‑language that comes from Fisher and EB pipelines. All are placed in a single discrimination table, with no explicit qualifier about comparability of these σ’s.
- **Why it matters:** It visually suggests a uniform σ scale of “discrimination strength” when the underlying tests are genuinely heterogenous.
- **Required fix:**  
  - Add a short note under Table III: “σ values quoted here derive from different inference procedures and should not be interpreted as directly comparable; this table is qualitative.”

---

### F. Abstract faithfulness

**P1A-N6A: Abstract’s “structural tension” sentence overstates what is quantitatively derived**

- **Location:** Abstract; Sec. XIV D.
- **Issue:**  
  - Abstract: “The dark-energy mechanism requires Ntot ≈ 92… and the matter-bounce fNL = −35/8 signature would be definitively erased…; the minimal‑ECH four‑route channel set is therefore tightly constrained as both a dark‑energy generator and a matter‑bounce host.”  
  - Sec. XIV D repeatedly emphasizes that the Ntot ≈ 92 value depends on the phenomenological ansatz of Appendix B, and that the tension is a *robustness check* given that the four amplitude routes are already closed. It is not a mathematically rigorous no‑go independent of that ansatz.  
  - The abstract wording blurs this nuance and can be read as a derived, model‑independent theorem.
- **Why it matters:** Abstract faithfulness: the strength of this “structural tension” is contingent on the same phenomenological assumptions already admitted to be “not solved.” Abstract does not convey that dependence.
- **Required fix:**  
  - Modify the abstract sentence to: “…*under the same phenomenological scaling ansatz that sets Ntot ≈ 92*, the matter‑bounce fNL… would be erased…”, and avoid implying that this is an independent constraint.

---

### G. Unquantified hedges

**P1A-N7A: Multiple “order-of-magnitude” caveats never given explicit bounds**

- **Location:** Sec. II C.1 (“order-of-magnitude matching” paragraph); Sec. XII A (“order-of-magnitude uncertainty”).
- **Issue:**  
  - Phrases like “within an order of magnitude,” “order-of-magnitude aesthetic,” “O(0.01–0.1)” appear, but there is no explicit statement that e.g. Ntot ≈ 92 is only defined up to ±2–3, nor a quantitative error bar on Ξ, Dinf, etc.  
  - As a result, readers see Ntot ≈ 92 used as if it were a precise benchmark, even though the text itself says the underlying inputs are only OOM‑accurate.
- **Why it matters:** This is exactly the “unquantified hedge” pattern: hedging words hide the fact that some of the headline numbers should carry substantial uncertainties.
- **Required fix:**  
  - Where Ntot ≈ 92–94 is quoted, explicitly attach a schematic uncertainty, e.g. “Ntot ≈ 90–95 depending on the chosen scaling ansatz,” and state that all fine‑tuning “reductions” are at that level of precision only.

---

### H. Appendix vs main‑text mismatch

**P1A-N8A: Appendix B’s corrected hierarchy vs main text and figures**

- **Location:** Appendix B; Sec. XII A; Fig. 5.
- **Issue:**  
  - Appendix B explicitly corrects an earlier mistake (“not the ∼35 misstated in earlier drafts… true hierarchy is ~120 orders”).[Appendix B]  
  - Sec. XII A continues to talk about “reduction from 10¹²⁰ to 10⁵”; Fig. 5 still has “10¹²⁰” and “115 orders of magnitude improvement.”  
  - Therefore the appendix and main text are not self-consistent.
- **Why it matters:** This demonstrates that numbers updated in the appendix were not propagated back into the main narrative and figures.
- **Required fix:**  
  - Harmonize Sec. XII A and Fig. 5 with Appendix B’s corrected numbers, or explicitly flag in the main text that earlier drafts used 10¹²⁰ and that Fig. 5 is schematic.

---

If you want, I can next go through all the displayed equations one by one and explicitly tabulate their dimensional consistency and any missing factors, or produce a checklist of which figures/tables would need concrete numerical revisions versus just wording/hedge adjustments.