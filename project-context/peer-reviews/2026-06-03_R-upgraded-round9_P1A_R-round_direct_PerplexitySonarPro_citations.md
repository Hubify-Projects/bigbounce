# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-03_R-upgraded-round9
**Wall time**: 23.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=36260, completion=2075, total=38335, search_context_size=low, cost={'input_tokens_cost': 0.10878, 'output_tokens_cost': 0.03112, 'request_cost': 0.006, 'total_cost': 0.14591}

---

## BLOCKER-PER-B1 — Many “Golden2026…” self-citations unverifiable / likely fictional

**Location:** Multiple places (e.g. abstract lines citing `\cite{Golden2026P2}`, `\cite{Golden2026P1b}`, `\cite{Golden2026P3}`, `\cite{Golden2026P4}`, and throughout text where “Paper I(b)/II/III/IV” are treated as external works).  

**Issue:** The bibliography is not provided here, but web search on arXiv/ADS/publisher sites finds no records for:  
- “Golden 2026 P2” SPHEREx / matter-bounce forecast paper.  
- “Golden 2026 P1b” ΛCDM+ΔNeff / NaMaster / ALP MCMC companion.  
- “Golden 2026 P3” PTA / NANOGrav real-KDE GPU MCMC reanalysis.  
- “Golden 2026 P4” galaxy-spin ViT chirality catalog.  

The manuscript explicitly calls these “companion works in preparation” and says they are not on arXiv yet, but then repeatedly phrases results as “from companion Paper I(b)/II/III/IV” and assigns formal citation keys as if they were citable literature. This is indistinguishable from non-existent references for an external reader, and key quantitative claims (MCMC chains, PTA γ, galaxy-spin nulls, SPHEREx forecast details) rest on them.  

**Fix:** In the bibliography, mark these as internal, unpublished documents (e.g. “H. Golden, in preparation” without arXiv IDs or journal venues) and adjust text everywhere to treat their numbers as *internal working results* rather than externally citable sources. If any are now on arXiv, add correct arXiv IDs, titles, and venues; otherwise, remove any language implying public availability or independent verifiability.


## MAJOR-PER-M1 — Shapiro & Teixeira 2014: citation chain slightly overstated

**Location:** §II.C.1 “Step 4: Parity-Odd Coefficient”, Eq. (oneloop), around “Following Freidel et al. and Shapiro & Teixeira… one-loop estimate is … motivating the order of magnitude…”.  

**Issue:** Shapiro & Teixeira, “Quantum Einstein–Cartan theory with the Holst term,” Class. Quantum Grav. 31 (2014) 185002, arXiv:1402.4854, *do* compute one-loop effects in Einstein–Cartan–Holst, but they do not explicitly present the simple schematic coefficient  
\(\frac{\alpha}{M}\sim \frac{g^2}{32\pi^2}\frac{\gamma}{M}\ln(\Lambda_{\rm UV}^2/\mu^2)+\delta_{\rm NY}\)  
as written here; that compact formula is an EFT-style parametrization, not a literal result of their paper.  

**Fix:** Keep using the formula as a phenomenological ansatz, but soften attribution: e.g. “Motivated by the structure of the one-loop corrections in Freidel–Minic–Takeuchi and in Shapiro & Teixeira’s Einstein–Cartan–Holst calculation, we *parametrize* the parity‑odd coefficient schematically as …; this specific normalization is not taken verbatim from any single reference but captures the expected loop and log structure.”


## MAJOR-PER-M2 — Date–Kaul–Sengupta 2009 and Benedetti–Speziale 2011: β‑function not actually given in form used

**Location:** Route 3 (§IV, “Route 3 (quantum running of the Immirzi parameter)” lines around Eq. `\gamma_running`).  

**Issue:**  
- Date, Kaul & Sengupta, “Topological interpretation of Barbero–Immirzi parameter,” Phys. Rev. D79 (2009) 044008, arXiv:0811.4496, discuss Nieh–Yan and the interpretation of γ, but do **not** derive the explicit RG equation \(d\gamma/d\ln\mu = \frac{1}{12\pi^2}(N_F^L-N_F^R)\gamma + \dots\) used here.  
- Benedetti & Speziale, “Perturbative quantum gravity with the Immirzi parameter,” JHEP 1106 (2011) 107, arXiv:1104.4028, *do* derive a nontrivial β-function for γ, but its structure is more complicated than this chiral-counting form.  

The text partly hedges (“schematically motivated”), but the combination of explicit equation and dual attribution can mislead readers into thinking this exact β-function comes from those papers.  

**Fix:** Make the status explicit: clearly mark Eq. (γ_running) as a *toy EFT ansatz* used only for order-of-magnitude estimates, not as a published β-function. Cite Date–Kaul–Sengupta for the topological γ–Nieh–Yan setup and Benedetti–Speziale for an actual perturbative computation, but state that neither supplies Eq. (γ_running) and that the running estimate is schematic.


## MAJOR-PER-M3 — Lue–Wang–Kamionkowski usage: normalization not from that paper

**Location:** Route 4 (§IV, “Route 4 (parity-odd CMB coupling…)” around introduction of \(\mathcal{L}_{\rm CS} \supset -\frac14(\alpha/M)\theta \tilde F F\) and the sentence “An early cosmological-birefringence treatment of this mechanism is Lue, Wang & Kamionkowski… they work with a generic ∂μφ Kμ … not with the specific −¼(α/M) normalization adopted here.”  

**Issue:** Lue, Wang & Kamionkowski (Phys. Rev. Lett. 83 (1999) 1506, arXiv:astro-ph/9812088) indeed use a Chern–Simons–type coupling \(\partial_\mu\phi K^\mu\), but the precise normalization \(-\tfrac14 (\alpha/M)\theta F\tilde F\) used here is from standard ALP conventions, not from LWK. The text mostly clarifies this, but the initial phrasing “The operator … is the conventional ALP–photon coupling; we adopt this normalization and use LWK as an early example” could still be read as a direct normalization source.  

**Fix:** Slightly tighten wording: emphasize that LWK provide an **early cosmological application of a pseudoscalar–photon Chern–Simons term**, while the \(-\tfrac14(\alpha/M)\) normalization follows later ALP literature and is *not* fixed by LWK. Keep the current caveat but move it immediately next to the operator’s definition.


## minor-PER-m1 — Ashtekar & Singh 2011: rhocrit values and γ-choice need sharper bibliographic separation

**Location:** §II.B (“Black Hole Interior and Quantum Bounce”), Eqs. `\rhocrit` and paragraph explaining 0.27–0.41 ρ_Pl window.  

**Issue:** Ashtekar & Singh, “Loop Quantum Cosmology: A Status Report,” Class. Quantum Grav. 28 (2011) 213001, arXiv:1108.0893, quote ρ_crit ≈ 0.41 ρ_Pl for γ ≈ 0.2375. The paper here correctly states that 0.27 ρ_Pl arises by inserting γ ≈ 0.274 into the same formula, but the prose might still be misread as if the whole 0.27–0.41 range were Ashtekar–Singh’s published LQC range.  

**Fix:** Add one explicit clarifying sentence: “Ashtekar & Singh explicitly give ρ_crit ≈ 0.41 ρ_Pl for γ = 0.2375; the lower value 0.27 ρ_Pl used here is *our own extrapolation* obtained by substituting the SU(2) black‑hole entropy γ into their formula, and is not a value quoted in Ref. [Ashtekar & Singh].”


## nit-PER-n1 — Hehl–Datta reference appears slightly mis-labeled

**Location:** Route 1 (§IV, “Route 1 (NJL four-fermion contact)”) citing “HehlDattaNJL1971” and Eq. `NJL_torsion`.  

**Issue:** The classic four-fermion torsion–NJL result comes from F. W. Hehl & B. K. Datta, “Nonlinear Spinor Equation and Asymmetric Connection in General Relativity,” J. Math. Phys. 12, 1334 (1971), which is often cited alongside Hehl et al. 1976. The in-text label “HehlDattaNJL1971” seems to correspond to that, but without seeing the `.bib` there is a small risk of inconsistent citation metadata (title/year/journal). Web search confirms the paper exists with that year and journal; only the “NJL” nickname is modern.  

**Fix:** Verify in `references.bib` that the entry for the Hehl–Datta paper has the correct title, year (1971), journal (J. Math. Phys. 12, 1334), and authors, and that the in-text key matches it. If “NJL” is included in the label, ensure it is only in the BibTeX key, not in the title field.
