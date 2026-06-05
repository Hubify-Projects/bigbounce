# P1B auto-2026-06-05_1517pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (13713 chars)
**Wall time**: 59.5s

---

I can audit the manuscript text you provided for internal consistency and citation problems, but I **cannot actually verify arXiv/ADS metadata against live web sources** from the search results available here because the returned search set is unrelated to the paper’s references. As a result, I can only give a **partial forensic review** based on the rendered text itself, not the full citation-by-citation external verification you requested.

- **P1B-E1 — Entire manuscript, especially pages 1–10** — **Essential**  
  **Problem:** The paper contains multiple **self-contradictory numerical statements** that are not reconciled clearly enough for PRD standards. For example, the abstract says the proxy run has “309,189 frozen samples across two converged dataset combinations,” but later footnote 1 says the same two chains have “176,240+132,949 raw accepted samples,” while the post-burn-in arithmetic is internally inconsistent in several places (e.g. “176,240 × 0.7 + 132,949 × 0.7 ≈ 216,432” and later “post-burnin count of the full-tension subset alone is 123,129 … the correct both-chains post-burnin total is 216,432”). The chain bookkeeping is not cleanly presented.  
  **Required fix:** Provide a single, unambiguous sample-accounting table with raw, burn-in, retained, thinned, and frozen counts for each chain and each dataset combination, and ensure every figure/table caption uses the same numbers.

- **P1B-E2 — Abstract, p. 1** — **Essential**  
  **Problem:** The abstract states the NaMaster validation “recovers β̂ = 0.238◦ (pipeline-recovery bias 0.032◦)” and calls this a validation of the pseudo-\(C_\ell\) deconvolution. But the body later says the same injection at \(\beta=0.342^\circ\) yields \(\hat\beta=0.302^\circ\), i.e. a bias of \(0.040^\circ\), and that the bias is *amplitude-dependent*. This is a materially different quantitative characterization than the abstract’s simpler “0.032°” framing.  
  **Required fix:** Make the abstract match the full set of results, including the amplitude dependence and the worst-case bias. If a single representative bias is quoted, explicitly say it is for the \(\beta=0.27^\circ\) injection only.

- **P1B-M1 — Abstract and Sec. VI, pp. 1, 6–7** — **Major**  
  **Problem:** The paper repeatedly mixes **published observational constraints** with **internal pipeline-recovery statistics** without always distinguishing the two strongly enough. The abstract says “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ,” but later the NaMaster analysis reports “pipeline-recovery SNR = 20.32” and “25.71.” Although you state that these are not sky significances, the repeated juxtaposition is risky and could mislead readers.  
  **Required fix:** In every place where these quantities appear side by side, add an explicit qualification that they are not directly comparable, and separate observational significance from injected-signal recovery significance in prose and captions.

- **P1B-M2 — Sec. III, p. 3** — **Major**  
  **Problem:** The manuscript asserts that the \(\Lambda\)CDM point is “at > 4σ in the joint marginal tails and is therefore unsampled by the Metropolis-Hastings chain,” and uses that to dismiss Savage–Dickey evidence estimates. This is plausible, but the paper does not show the underlying marginal posterior plots, density estimates, or a quantitative tail-distance calculation supporting the \(>4\sigma\) claim.  
  **Required fix:** Provide the actual posterior plot or numerical tail-distance computation, and state precisely how the \(4.3\sigma\) / \(>4\sigma\) claims were computed.

- **P1B-M3 — Table II, p. 4** — **Major**  
  **Problem:** Table II reports \(\chi^2_{\rm total}=14037.4 \pm 5.6\), while the listed channel means sum to \(10.6+10983.9+3043.0=14037.5\). You note this is a rounding artifact, but the table also gives an uncertainty of \(\pm 5.6\), which is large compared to the 0.1 difference, and the text does not explain whether the \(\chi^2\) values are means over weighted samples, best fits, or something else.  
  **Required fix:** State clearly whether each \(\chi^2\) entry is a posterior mean, best-fit value, or weighted-sample average, and either remove the redundant uncertainty notation or explain its origin.

- **P1B-M4 — Sec. II / Table I, pp. 2–3** — **Major**  
  **Problem:** The paper calls the \(\Lambda\)CDM+ \(\Delta N_{\rm eff}\) run a “null-consistency test” but then repeatedly uses it to discuss the Hubble tension and claims “the \(\Delta N_{\rm eff}\) extension alone does not resolve the Hubble tension.” That is fine, but the paper also says the extension is “a phenomenological proxy for the spin-torsion sector’s possible effective radiation contribution,” while earlier and elsewhere it says the Hehl–Datta–Mercuri contact term cannot produce \(\Delta N_{\rm eff}\). These two framing statements are in tension and need sharper separation.  
  **Required fix:** Explicitly distinguish between a **proxy parameterization** and a **theory prediction**, and remove any language that could suggest the proxy is expected to map directly onto a torsion-induced radiation component.

- **P1B-M5 — Sec. II, p. 2** — **Major**  
  **Problem:** The manuscript states “the high-precision Planck NPIPE CamSpec TTTEEE+lowl+lensing likelihoods carry sufficient inverse-variance weight that the posterior H0 … is pulled to 67.68 ± 1.06 rather than to the simple Gaussian-combination value ∼ 70.” This is an inference from the fit, not a directly demonstrated weighted average, and the paper does not show the arithmetic.  
  **Required fix:** Either present the explicit weighting calculation or rephrase as a qualitative interpretation of the posterior behavior.

- **P1B-M6 — Sec. III, Table I, p. 3** — **Major**  
  **Problem:** The table says “Worst R̂−1 = 0.001” and “Min ESS 4,744 / 4,692,” while footnote text says a third Planck-only chain is “at sub-convergence sample count” and has \(R̂−1\sim 0.05\). The manuscript is therefore mixing converged and unconverged chains in a way that is not cleanly partitioned.  
  **Required fix:** Separate converged frozen chains from the still-running Planck-only chain in all summaries and state explicitly which diagnostics apply to which chain.

- **P1B-M7 — Sec. III, p. 3** — **Major**  
  **Problem:** The paper says “the canonical quintom signature” is implied by \(w_0=-0.8122\pm0.0436\), \(w_a=-0.6666\pm0.1864\), and \(w_0+w_a=-1.4788\pm0.1485\). But the quoted significance values are based on marginal-tail extrapolation, not a likelihood-ratio or posterior-odds test, and the manuscript sometimes writes as if they were exclusion significances.  
  **Required fix:** Remove any language implying a frequentist exclusion or Bayesian evidence unless you provide a valid evidence calculation.

- **P1B-M8 — Sec. IV, p. 5** — **Major**  
  **Problem:** The pseudo-\(C_\ell\) pipeline description is incomplete enough to prevent reproducibility at PRD level. The text mentions beam smoothing, pixel windows, mask apodization, \(\Delta \ell=20\), and \(N_{\rm side}=512\), but does not give the exact mask file identity, transfer-function handling, bandpower window normalization, or whether \(E/B\) purification changes the effective degrees of freedom.  
  **Required fix:** Provide the precise analysis configuration and the exact map/mask inputs used, plus the transfer-function and purification conventions.

- **P1B-M9 — Sec. VI, p. 6** — **Major**  
  **Problem:** Equation (2) claims \(\Delta\phi/f_a \approx 0.65\) for \(m=H_0,\theta_i=1\), and then Eq. (3) gives \(\beta\approx (\alpha_{\rm EM} 8 /4\pi)\times 1.07 \approx 0.29^\circ\). The link between \(\Delta\phi/f_a\), \(C_{a\gamma}\), and the observed angle is presented as if numerically derived, but the text later admits the ranges are based on a “joint-trajectory scan” and not independent extrema.  
  **Required fix:** Show the actual numerical mapping from the ALP evolution to \(\beta\) and clarify exactly which quantities were scanned versus held fixed.

- **P1B-M10 — Sec. VI, p. 6** — **Major**  
  **Problem:** The paper quotes a “\(\sim 25\times\) misalignment tuning” requirement, but the numerical basis is inconsistent. It says the spectator-consistent corner is \(\theta_i\sim 0.1\), while the scan prior midpoint is \(\theta_i\sim 0.5\), which is a factor of 5, not 25. The factor of 25 appears to come from energy-density scaling \(\Omega_a\propto \theta_i^2\), but this is not stated cleanly at the point where the tuning claim is made.  
  **Required fix:** State explicitly whether the tuning claim refers to \(\theta_i\), \(\Omega_a\), or both, and show the scaling law used.

- **P1B-M11 — Sec. VI, p. 7** — **Major**  
  **Problem:** The manuscript reports three ALP fits: \(\beta_{\rm ALP}=0.336^\circ\pm0.107^\circ\), \(\beta_{\rm free}=0.344^\circ\pm0.096^\circ\), and a combined \(\beta=0.241^\circ\pm0.061^\circ\). These are not obviously mutually consistent with the stated published headline \(\beta=0.342^\circ\pm0.094^\circ\), yet the paper treats all of them as aligned.  
  **Required fix:** Explain the data sets, priors, and likelihood stacks for each fit more explicitly and clarify why the model-dependent fit shifts downward relative to the published headline.

- **P1B-M12 — Table III, p. 10** — **Major**  
  **Problem:** The claims-classification table labels multiple statements as “Verified,” but several of those are not actually verified in the manuscript to PRD standards. In particular, the “Model-comparison \(\Delta AIC/BIC/\ln B\)” row is marked “Omitted,” yet the prose still uses model-comparison language elsewhere to interpret posterior structure.  
  **Required fix:** Reconcile the classification table with the main text and remove any claim of verification that is not actually supported by a demonstrated computation.

- **P1B-M13 — References [1], [3], , , , p. 9** — **Essential**  
  **Problem:** Several bibliography entries are **internally suspect** or appear fused with commentary. Examples:  
  - Ref. [1] is listed as “(in preparation) (2026), hUBIFY-2026-001A; companion paper, this volume,” which is not a normal physical reference format and may be an internal placeholder rather than a citable publication.  
  - Ref. [3] is attributed to “P. Diego-Palazuelos and E. Komatsu” with a PRD 2025 arXiv preprint and commentary embedded in the entry.  
  - Ref.  is a 2025 EPJ C torsion paper; the manuscript claims it uses DESI, supernovae and CMB constraints, but the entry format is incomplete and the title should be verified.  
  - Ref.  includes prose after the title and page data, not a clean reference entry.  
  - Ref.  calls DESI 2024 VI “arXiv preprint (2024)” with a 2025 PRD style citation elsewhere in the manuscript’s prose; this needs consistency.  
  **Required fix:** Rebuild the bibliography in standard PRD format and verify every reference against arXiv/ADS. Remove embedded commentary from the reference list.

- **P1B-M14 — References , p. 9** — **Major**  
  **Problem:** Ref.  contains embedded explanatory prose after the bibliographic information: “canonical quintom-cosmology review (two-field DE with w crossing -1). Used in P1A Sec. VI to point readers to the bounce-class alternative DE mechanism that survives the 14 ECH-specific structural barriers.” That is not a citation entry; it is editorial commentary.  
  **Required fix:** Strip commentary from the bibliography and keep only bibliographic metadata.

- **P1B-M15 — Appendix A and footnotes 4–5, pp. 8–9** — **Major**  
  **Problem:** The manuscript places important physical caveats in footnotes, including the claim that the “spectator-consistent regime” is only \(\theta_i\sim0.1\), while the sampled prior is \([0.5,2]\), and that the latter corresponds to a “dark-energy-ALP regime.” This is central physical content, not a side note.  
  **Required fix:** Move these caveats into the main text of Sec. VI and Appendix C, where they can be clearly seen and assessed.

- **P1B-N1 — Abstract, p. 1** — **NIT**  
  **Problem:** The paper says “ΛCDM+∆Neff” and elsewhere uses “\(\Lambda\)CDM+\(\Delta N_{\rm eff}\)” and “LCDM.”  
  **Required fix:** Standardize typography and notation.

- **P1B-N2 — Throughout** — **NIT**  
  **Problem:** Some section headings are overloaded with parenthetical disclaimers, for example “Generic Radiation-Proxy Test (Not a Spin-Torsion Theory Module).”  
  **Required fix:** Shorten headings for readability.

- **P1B-N3 — p. 5** — **NIT**  
  **Problem:** The figure caption and the body use different notations for the same measured angle: “\(\beta\)” vs “\(\beta_{\rm NaMaster}\)” vs “\(\hat\beta\).”  
  **Required fix:** Use one notation consistently and define the others only if needed.

- **P1B-N4 — p. 8** — **NIT**  
  **Problem:** The data/code availability section repeats repository information already given in Appendix A.  
  **Required fix:** Condense repeated repository descriptions.

- **P1B-E3 — References [1], [4], [5], [6], pp. 9–10** — **Essential**  
  **Problem:** Several entries are explicitly listed as “(in preparation)” while being used in the body as if they were established, citable results. For a PRD submission, this is not acceptable for load-bearing claims unless the manuscript clearly states they are unpublished internal manuscripts and the claims are not used as evidence for the present paper’s conclusions.  
  **Required fix:** Remove dependence on unpublished companion papers for any claim that is essential to the present manuscript, or provide public preprints with stable identifiers.

- **P1B-M16 — Abstract, p. 1 and Sec. VI, p. 6** — **Major**  
  **Problem:** The abstract says the ALP result is “consistent with the published joint WMAP+Planck value \(\beta=0.342^\circ\pm0.094^\circ\) (3.6σ)” and then says the spectator-status caveat makes the model “not a distinctive ECH prediction.” This is conceptually coherent, but the manuscript still frames the ALP result as a verification item in the paper’s title and abstract, which overstates its relevance to the ECH program.  
  **Required fix:** Recast the ALP section as an external consistency check and make the title/abstract less programmatic if the result is not truly derived from ECH.

## Summary recommendation
**REJECT**

The paper has several serious problems that prevent acceptance at PRD level: unresolved internal bookkeeping inconsistencies, overuse of unpublished/in-preparation references, commentary embedded inside the bibliography, and insufficiently separated inference versus measurement in multiple load-bearing claims. Most importantly, the manuscript does not yet present its numerical and citation record with the rigor required for a technical verification companion in a high-bar journal.

---

## PASS 2 — self-critique findings (what initial review missed)

P1B-E4 — Table I, Fig. 1, footnote 1 sample counts — Essential  
**Problem (arithmetic / stale numbers):** The manuscript tries to reconcile chain lengths but still contains mutually inconsistent “frozen/post‑burn‑in” counts. Footnote 1 states the full‑tension chain has 176,240 raw samples and 119,617 post‑burn‑in samples “reflecting … thinning of this subset only,” i.e. a thinning factor of ≈176,240/119,617 ≈ 1.47. Yet the same footnote also says “the correct both‑chains post‑burn‑in total is 216,432,” which for two chains of sizes 176,240 and 132,949 with 30% burn‑in implies **no additional thinning at all** beyond the 0.7 factor (176,240×0.7 + 132,949×0.7 = 216,433). The text is therefore simultaneously claiming (a) getdist‑thinned post‑burn‑in samples for the full‑tension chain (119,617) and (b) an unthinned, purely post‑burn‑in count for both chains (216,432), using that latter as the “correct” number. These are different objects and must not be mixed under the same “post‑burn‑in” label.  
**Required fix:** Clearly separate: (i) raw accepted samples, (ii) post‑burn‑in unthinned counts, and (iii) any additional getdist thinning, for each chain and dataset combination. Do not present a single “correct” post‑burn‑in total that silently mixes thinned and unthinned definitions.

---

P1B-M17 — Abstract vs. Sec. III, description of ∆Neff proxy — Major  
**Problem (abstract faithfulness / scope):** The abstract frames analysis (1) as “Stock‑CAMB ΛCDM+∆Neff MCMC proxy … reported as a null‑consistency test … not as evidence for or against the ECH spin‑torsion framework,” while Sec. III more strongly says “The MCMC therefore tests whether the data prefer an extra radiation‑like degree of freedom, treated as a generic phenomenological proxy for the spin‑torsion sector’s possible effective radiation contribution” and explicitly notes that the Hehl–Datta–Mercuri term “does not produce a ∆Neff at recombination.” This makes the **“proxy for the spin‑torsion sector” language in the abstract somewhat misleading**, because the body concedes the torsion term does not in fact map to ∆Neff in the way “radiation‑proxy” normally implies.  
**Required fix:** In the abstract, explicitly align the wording with Sec. III: stress that ∆Neff is *only* a phenomenological null‑consistency check and that the minimal ECH contact term is not expected to generate a recombination‑era ∆Neff, so the run is not a test of any concrete torsion prediction.

---

P1B-M18 — Sec. II, “spin-torsion framework alone does not resolve cosmological tensions” — Major  
**Problem (unquantified hedge / support):** Sec. II ends with “The spin‑torsion framework alone does not resolve cosmological tensions at the present data precision,” but the only quantitative evidence shown in this paper is for **stock ΛCDM+∆Neff with no torsion sector implemented**. There is no explicit model where torsion parameters are turned on and tested against data in this manuscript. Calling this “the spin‑torsion framework” therefore over‑generalizes from a stock‑CAMB proxy.  
**Required fix:** Rephrase to something like “This ΛCDM+∆Neff proxy, used here as a crude bounce‑class/radiation proxy, does not resolve the tensions” and move any stronger claims about “the spin‑torsion framework” back into Paper I(a) where the structural arguments actually live.

---

P1B-M19 — Sec. III, “Key finding” statement on ∆Neff and H0 — Major  
**Problem (null‑procedure comparability / hedge):** The “Key finding” paragraph claims that both frozen datasets find ∆Neff consistent with zero and H0 consistent with Planck ΛCDM at 0.3σ, “confirming that the ∆Neff extension alone does not resolve the Hubble tension.” This is qualitatively true, but the **0.3σ “consistency with Planck” figure is never explicitly demonstrated** (no baseline Planck‑only value with error bar is shown for direct comparison), and the “does not resolve the Hubble tension” statement is not accompanied by a clear quantitative tension metric (e.g. explicit ΔH0/σ combined). There is hand‑waving back to the canonical 3.6σ tension but no explicit re‑evaluation with the proxy model.  
**Required fix:** Explicitly compute and quote the H0 shifts and combined-tension significance under the ΛCDM+∆Neff model relative to SH0ES and to Planck baseline ΛCDM. This will make the “does not resolve” statement quantitatively grounded.

---

P1B-M20 — Sec. IV vs. Abstract: NaMaster SNR vs published sky significance — Major  
**Problem (null procedure comparability, juxtaposition):** The abstract says “The primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ; the pipeline SNR figures refer to recovery of injected MC signals and are not competitive sky measurements.” Sec. IV reiterates that “The high pipeline‑recovery SNR figures (e.g., 20.32, 25.71) must not be conflated with the published Planck/ACT DR6 2.4–2.9σ sky detection.” While this is stated, the **same paragraph still repeats numerical SNRs alongside the published 2.4–2.9σ**, which risks exactly the casual comparison PRD is sensitive to, particularly since both are labeled in “σ” units. The null procedures differ (Monte‑Carlo noise vs. sky‑measurement null), but that is not spelled out explicitly.  
**Required fix:** Wherever the 20.32σ / 25.71σ values appear near 2.4–2.9σ sky significances, add an explicit sentence that the σ units reflect *different null procedures* (MC noise vs. sky null) and are therefore not directly comparable, and avoid describing both using “detection significance” without this clarification.

---

P1B-M21 — Sec. IV, amplitude‑dependent bias characterization — Major  
**Problem (arithmetic / stale text):** Sec. IV notes that the pipeline bias is 0.032° at β=0.27° (0.238° recovered) and 0.040° at β=0.342° (0.302° recovered), and that “the bias was initially characterized as strictly ‘stable across all three injections’ at 0.032°, but the 0.342° injection actually gives 0.040°, a relative ∼12% amplitude‑dependent component.” However, the **abstract still quotes only the 0.032° figure and omits both the 0.040° worst‑case bias and the fact that the bias is amplitude‑dependent**, which materially changes the characterization of the validation accuracy.  
**Required fix:** Update the abstract’s NaMaster sentence to mention the amplitude dependence and the worst‑case 0.040° bias, or else clearly state that “0.032°” refers only to the β=0.27° injection and is not the maximum bias found.

---

P1B-M22 — Sec. VI, Eq. (2) and surrounding text — Major  
**Problem (dimensional / normalization clarity):** Eq. (2) gives “∆ϕ/fa ≈ 0.65 (m = H0, θi = 1)” and then states that across m/H0 ∈ [1,3], θi ∈ [0.5,2] one finds ∆ϕ/fa ∈ [0.2,1.1]. The text later uses a *different* set of representative parameters (“For Caγ = 8, θi = 1, m ≈ 2H0”) to motivate β ≈ 0.29° in Eq. (3), and then says “The fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8H0 , ∆ϕ/fa ≈ 1.0.” None of these intermediate ∆ϕ/fa values (0.65, 1.0, 0.2–1.1) are shown in a table or figure, and the mapping from (m/H0, θi) to ∆ϕ/fa is opaque—particularly since θi appears linearly in the energy density scaling but not explicitly in Eq. (2). Dimensional consistency is fine (∆ϕ/fa is dimensionless), but **the normalization and parameter dependence of Eq. (2) are under‑documented relative to how heavily they are used later.**  
**Required fix:** Provide either (a) a small table or figure of ∆ϕ/fa versus m/H0 and θi or (b) an explicit fitting formula showing how the 0.65, 1.0, and 0.2–1.1 values are obtained from numerics. This is necessary to support the later β and Caγ inferences that depend critically on these numbers.

---

P1B-M23 — Sec. VI, Eq. (3) numerical consistency and β‑range — Major  
**Problem (arithmetic / range construction):** Eq. (3) says “β ≈ (αEM × 8 / 4π) × 1.07 ≈ 0.29°” for Caγ=8, and the text says “The fiducial value β ≈ 0.27° corresponds to the midpoint m ≈ 1.8H0 , ∆ϕ/fa ≈ 1.0.” Later it states “The prediction spans β ≈ 0.17–0.43° over Caγ ∈ [4, 12], m/H0 ∈ [1, 3], θi ∈ [0.5, 2]…” and then clarifies that this 0.17–0.43° range is from a “joint‑trajectory scan … not from an independent‑extremes product (which would give the wider naive envelope [0.027, 0.44]°).” However:  
- The manuscript never explicitly shows the calculation that leads from the (Caγ, m/H0, θi) priors and ∆ϕ/fa range [0.2,1.1] to the quoted [0.17,0.43]° interval.  
- The “naive” [0.027,0.44]° envelope is also not shown numerically; it is just asserted.  
Given that later claims about misalignment tuning and Caγ enhancement rely on this compressed 0.17–0.43° band, this constitutes an **under‑justified numerical summary**.  
**Required fix:** Add a short derivation or table: e.g., list the minimum and maximum β found in the joint scan, along with the corresponding (Caγ, m/H0, θi), and separately show the “independent extremes” product that yields [0.027,0.44]°. This will make the β‑range construction transparent and reproducible.

---

P1B-M24 — Sec. VI, Caγ Δϕ/fa ≈ 10.3 and “∼25× misalignment tuning” — Major  
**Problem (arithmetic / clarity of what is tuned):** Sec. VI now states that the coupling‑displacement product is Caγ (∆ϕ/fa) ≈ 10.3 for β=0.342°, and that the ∆ϕ/fa range [0.2,1.1] implies Caγ ∈ [9,51], all lying above “minimal KSVZ/DFSZ” expectations. It then states that the spectator‑consistent corner θi∼0.1 requires a “∼25× fine‑tuning” relative to θi∼0.5, referencing the Ωa ∝ θi² scaling in footnote 4. However, the **text still mixes three different sense of “25×”: a factor 5 in θi, a factor 25 in Ωa, and a qualitative statement about “misalignment tuning”** without clearly separating them. For a reader, it is ambiguous whether the “25× tuning” refers to the field angle, the energy density, or some combined measure.  
**Required fix:** At the point where “∼25× misalignment tuning” is claimed in Sec. VI, explicitly spell out: (i) the numerical factor in θi (0.1 vs 0.5), (ii) the implied factor in Ωa via θi², and (iii) how this translates to the required Caγ to keep Caγ ∆ϕ/fa ≈ 10.3 fixed. This will remove lingering ambiguity that your previous footnotes did not fully resolve.

---

P1B-M25 — Sec. VI, comparison of βALP, βfree, βobs, βcombined — Major  
**Problem (figure‑vs‑body / comparability):** The ALP section now reports four different amplitudes: βALP = 0.336°±0.107°, βfree = 0.344°±0.096°, βobs = 0.342°±0.094° (Eskilt & Komatsu joint), and βcombined = 0.241°±0.061° (Planck‑NPIPE+ACT inverse‑variance combination). The text says “All three within 1σ,” but this appears to be referring only to βALP, βfree, and βobs; βcombined is clearly >1σ lower than βobs and βfree (difference ≈0.10° compared to ≈0.09–0.10° errors). The manuscript calls βcombined “auxiliary” and not headline, which is good, but **it never explicitly discusses this internal tension between βcombined and the other three numbers**, even though βcombined is used to argue for consistency with ALP predictions in the 0.17–0.43° band.  
**Required fix:** Explicitly note that βcombined is lower than βobs/βfree at roughly the 1.5–2σ level (you can compute this precisely) and clarify how that affects the ALP “consistency” narrative. Either down‑weight βcombined in the argument or discuss whether it might hint at systematics or different sky coverage, rather than silently treating all four as equally “within 1σ.”

---

P1B-N5 — Sec. IV vs. Sec. VI notation for birefringence angle — NIT  
**Problem (notation consistency beyond previous nit):** Even after your earlier cleanup, Sec. IV uses **β̂NaMaster**, Sec. VI uses **β, βALP, βfree, βobs, βcombined**, and the abstract uses **β** and **β̂**. There is still no single, explicit one‑line “notation dictionary” explaining that βobs is the published sky value, β̂NaMaster is the recovered MC value, βALP is the ALP‑model prediction, etc. This can confuse readers trying to track which β is coming from which pipeline or likelihood.  
**Required fix:** Add a short notation paragraph (either at the start of Sec. IV or Sec. VI) listing the different β‑symbols and their meanings, and then stick strictly to that notation in captions and body text.

---

P1B-M26 — Appendix C vs. Sec. VI: prior ranges and “naturalness” — Major  
**Problem (appendix vs. main text mismatch / hedging):** Appendix C states that the ALP prior takes θi ∈ [0.5,2] as the “natural‑misalignment range” and explicitly notes that this is *not* the spectator‑consistent sub‑range (θi ∼ 0.1), describing θi ∼ 0.1 as a “sub‑natural sliver” requiring ∼25× tuning. Sec. VI, however, still describes the ALP model as “natural parameters (taken at scan‑prior midpoint values; the ∼25× misalignment tuning required for the headline result is disclosed below and in fn. 4)” in a way that **blurs the difference between what is actually sampled in the MCMC (θi≥0.5) and what is required for true spectator status (θi≈0.1)**. A reader could easily miss that almost all sampled θi values correspond to the dark‑energy‑ALP regime that is explicitly “excluded” from the companion‑paper’s remit.  
**Required fix:** In Sec. VI, directly reference Appendix C’s statement that the prior range [0.5,2] is *not* spectator‑consistent, and explicitly say that the ALP‑MCMC explores the DE‑ALP regime as well, while the spectator‑consistent θi~0.1 realization is not actually drawn from the stated prior but is effectively a hand‑picked tuning point. This is a conceptual, not merely notational, clarification.

---

If you want, I can now go equation‑by‑equation and build the explicit arithmetic table (σ‑recomputations, β ranges, Caγ ranges, and exact σ‑level comparisons) you would need to systematically fix the points above.