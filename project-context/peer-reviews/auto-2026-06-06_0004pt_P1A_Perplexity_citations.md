# P1A auto-2026-06-06_0004pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (12814 chars)
**Wall time**: 93.6s

---

The manuscript as provided is internally self-contained, but many of its citations, numerical claims, and cross‑references do not yet meet Physical Review D standards for traceability, rigor, or verifiability.

Below I list all issues I can identify, following your requested format. Page numbers refer to the PDF text you supplied (counting the title page as p.1).

---

### ESSENTIAL findings

**P1A-E1 – Abstract (p.1): Unverifiable “companion works in preparation” used as load‑bearing references**

- **Problem:** The abstract repeatedly appeals to companion works “[2, 6]” and “Paper I(b)” for:
  - SPHEREx Fisher forecast details for \(f_{\mathrm{NL}}=-35/8\).
  - ΛCDM+\(\Delta N_{\rm eff}\) MCMC verification.
  - NaMaster pipeline validation.
  - ALP parameter fitting.
- These are all listed as “in preparation” and not on arXiv. Yet they are used to support specific numerical claims (e.g., forecasted σ’s, chain lengths, convergence, parameter values).
- **Required fix:** Either (i) post these companion works on arXiv and cite them with concrete identifiers, or (ii) remove / drastically soften any claims that rely on them, and restate only what can be justified from published literature or from fully described methods in this paper. For PRD, “companion in preparation” cannot be used as the primary support for quantitative claims.

---

**P1A-E2 – Abstract (p.1): Use of unpublished “Paper II” for SPHEREx \(f_{\rm NL}\) forecast**

- **Problem:** The abstract states: “a detailed multi-tracer SPHEREx Fisher forecast is presented in a companion work in preparation [2]” and uses this to advertise a 3–5σ detection claim in Table I and Sec. XIII. No arXiv ID is given; [2] is “in preparation” with an internal tag.
- **Required fix:** Either (a) include the full Fisher forecast in this paper with enough detail for reproduction, or (b) restrict discussion to qualitative expectations (e.g. cite Heinrich et al. 2024 JCAP 04, 074) and remove all specific σ(fNL) numbers that depend on the unpublished internal work.

---

**P1A-E3 – Abstract & throughout (multiple pages): Heavy reliance on internal MCMC analysis [6] for quoted cosmological parameters**

- **Problem:** H0, \(\Delta N_{\rm eff}\), σ8, Ωm and the statement that “H0 = 67.68 ± 1.06, ∆Neff ≈ 0 recovers ΛCDM” and many later claims (Table I, Sec. I, Sec. V–VII) are explicitly based on Paper I(b) [6], “in preparation.” The paper repeatedly insists these are “internal inputs, not peer‑reviewable values” yet still uses them to support its conclusions.
- **Required fix:** For PRD, key cosmological numbers must either:
  - Be taken from published sources (e.g., Planck 2018[7]) with explicit citations and consistent values, or
  - Be fully documented in this paper’s methods and results sections (chains, priors, likelihoods, convergence, etc.).
  The current solution (“internal MCMC inputs”) is not acceptable for a standalone PRD article.

---

**P1A-E4 – Sec. II B (p.6) & Sec. IX M / Eq. (20), Table II: Misattribution of LQC critical density values to Ashtekar & Singh (2011)**

- **Problem:** The paper claims “Ashtekar & Singh  quote … ρcrit ≃ 0.41 ρPl at γ=0.2375; substituting γ≈0.274 gives ρcrit ≃ 0.27 ρPl” and then uses a “0.27–0.41 ρPl window” throughout (e.g. Eq.(20), Table II).  
  Ashtekar & Singh (Class. Quantum Grav. 28, 213001 (2011)) indeed discuss \(\rho_{\rm crit}\approx 0.41 \rho_{\rm Pl}\) for the standard area gap, but they do not quote an alternative 0.27 value arising from γ=0.274. The 0.27 number is an internal extrapolation.
- **Required fix:** Correct the attribution:
  - Explicitly state that ρcrit ≃ 0.41 ρPl is what Ashtekar & Singh actually provide.
  - Label the 0.27 value as an internal extrapolation across counting schemes, not as a published value.
  - Wherever the “0.27–0.41” window and Eq.(20) are used, make clear which part is sourced from the literature and which is authors’ own scaling.

---

**P1A-E5 – Sec. II C / Eq. (10) (p.6): Cosmological-constant mapping built on an explicitly non‑EFT, dimensionally inconsistent ansatz**

- **Problem:** The parity-odd operator in Eq.(6) has off‑shell mass dimension +1 (confirmed in Appendix B, Eq.(B1)), yet it is treated as sourcing a vacuum energy density via the ansatz \( \rho_\Lambda = \Xi M_{\rm Pl}^4\) with \(\Xi\sim[(\alpha/M)M_{\rm Pl}] D_{\rm inf}\). This mapping is acknowledged to be an “on‑shell scaling ansatz” and not a controlled EFT calculation, and the author admits missing mass powers (Appendix B).
- **Required fix:** For PRD, any quantitative claim that this operator can source dark energy must be either:
  - Derived from a well‑defined renormalizable or effective Lagrangian of dimension 4 with all mass scales explicit, or
  - Clearly demoted to a speculative toy ansatz, not used to derive precise numerical requirements like “Ntot ≈ 92” or “fine‑tuning reduced to 10^5.”
  The text must be restructured so that no key conclusions depend on a manifestly dimensionally inconsistent operator identification.

---

**P1A-E6 – Sec. II C 1 & Appendix B (pp.6–7, 19): The Ntot ≈ 92 “structural tension” is numerically fitted to the same uncontrolled ansatz**

- **Problem:** The claimed structural tension between dark-energy suppression and matter‑bounce \(f_{\rm NL}\) hinges on \(D_{\rm inf}\sim e^{-3N_{\rm tot}}\) producing Ξ ≈10⁻¹²³. But the numerical mapping from the parity‑odd operator to ρΛ has no controlled derivation, and the paper itself notes that the factor \((T_{\rm reh}/M_{\rm GUT})^{3/2}\) is only a dimensional “aesthetic” estimate, not computed from a partition function.
- **Required fix:** Either:
  - Provide a rigorous derivation from a specified microphysical model (including a legitimate dimension‑4 operator and explicit computation of \(D_{\rm inf}\)), or
  - Present the Ntot ≈ 92 figure as merely illustrative and remove it as a structural quantitative result. The “tension” cannot be treated as a robust prediction under the current level of control.

---

**P1A-E7 – Sec. IV B (pp.8–9): Route‑2 one-loop birefringence amplitude involves a constructed operator not clearly derived from the cited literature**

- **Problem:**
  - Equation (14) introduces a parity‑odd operator 
    \[
    \Gamma_{\text{one-loop}} = -\frac{1}{16\pi^2 M_{\rm Pl}}\int d^4x \sqrt{-g}\,\beta(\gamma)\,\partial_\mu\theta J_5^\mu
    \]
    and asserts that it is “motivated by” Mercuri & Capozziello, but it is not actually derived there. Mercuri & Capozziello compute one-loop corrections to the Holst term and Nieh–Yan invariant within Einstein–Cartan theory, but they do not present this exact effective operator with the given 1/(16π² MPl) normalization.
  - The paper admits this is an “upper-bound EFT ansatz,” yet it is used to obtain a numerical suppression factor (~10⁻⁵⁸–10⁻⁶⁰) and a quantitative “closure” of Route 2.
- **Required fix:** Either derive this operator explicitly (showing how Mercuri–Capozziello and/or other literature yield the coefficient and structure used) or clearly separate this as an author‑defined phenomenological toy. Then, weaken the Route‑2 no‑go from a quantitative amplitude exclusion to a qualitative statement (e.g., “any plausible one-loop Holst-induced birefringence is vastly below current data”) that does not depend on an ad hoc operator.

---

**P1A-E8 – Sec. IV C (p.9): Ad hoc RG equation for Immirzi running not matched to the literature**

- **Problem:**
  - Eq.(16) postulates \( d\gamma/d\ln\mu = \frac{1}{12\pi^2}(N_{FL}-N_{FR})\gamma + O(\gamma^2)\). It is labeled an “EFT bound” “motivated” by Date, Kaul & Sengupta, but that paper interprets γ as a topological angle; it does not present this RG equation.
  - The actual perturbative running of γ with fermions in Einstein-Cartan–Holst gravity is computed in Benedetti & Speziale, JHEP 06 (2011) 107, with a more complicated β-function depending on four-fermion interactions and gauge choice.
- **Required fix:** Replace Eq.(16) and subsequent estimates with either:
  - A faithful use of Benedetti & Speziale’s β-function, including its parameter dependence, and redo the amplitude estimate, or
  - A clearly marked qualitative statement (“even for order‑unity β-functions, the induced IR effect is \(\sim H/M_{\rm Pl} \ll 1\)”).
  Presenting a new RG equation as if literature‑based when it is not is unacceptable for PRD.

---

**P1A-E9 – Sec. IV D (pp.10–11): Spectator‑ALP Route‑4 “naturalness objection” rests on internal numbers and implicit formulae not traced to **

- **Problem:**
  - Eq.(17) for the birefringence angle β uses \(\beta \sim (\alpha/M)\sqrt{2\rho_\theta}/m_\theta\) without explicitly deriving it from the Lue, Wang & Kamionkowski Chern–Simons coupling analysis.
  - The numerical bounds on overshoot factors (e.g. 22–36 orders of magnitude for “natural” ALP mass range) are based on an internal choice α/M ~ 10⁻²¹ GeV⁻¹ that is traced back to WMAP+Planck β_obs but not transparently derived in this paper.
- **Required fix:** Provide a clear, stepwise derivation of Eq.(17) from the standard φFF̃ Lagrangian and show explicitly how α/M is fixed by the cited WMAP+Planck measurement[3][4]. Alternatively, downgrade the detailed numerical “22–36 orders of magnitude” statements to qualitative remarks and focus on the general naturalness issue.

---

**P1A-E10 – Sec. X (“Perturbation transparency”, pp.14–15): Overstated generality vs. existing Einstein–Cartan results**

- **Problem:**
  - The paper states as “central result” that “torsion vanishes at all perturbation orders; Holst term is dynamically inert” for canonical scalars and claims novelty by calling this a “perturbation‑transparency theorem,” only referencing Hehl et al. 1976 in passing.
  - Hehl et al. already show that in Einstein–Cartan theory, torsion vanishes when spin density vanishes, leading to standard GR dynamics (this is not limited to background, although the detailed perturbation-level analysis is not spelled out there). This paper does not provide an explicit perturbation-level tensor or scalar action derivation, nor a comparison with existing EC+Holst perturbation analyses such as Freidel, Minic & Takeuchi or Mercuri.
- **Required fix:** Either:
  - Provide a full derivation of the scalar and tensor perturbation actions (to at least cubic order) showing step-by-step how the Holst term reduces to a boundary term and verifying no hidden γ‑dependence, and explicitly delineate what is new relative to; or
  - Reduce the claim to a “rephrasing/extension of known Einstein–Cartan results to the Holst term,” not a new theorem.

---

**P1A-E11 – Use of DESI DR2 / DESI 2024–2025 evidence for dynamical dark energy (Abstract, Sec. I, Sec. XIV D)**

- **Problem:** The paper cites DESI Collaboration results as showing “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ”. Those preprints exist, but the quoted significances are dataset‑dependent and sensitive to modeling assumptions (DESI 2024 arXiv:2404.03002; DESI DR2 arXiv:2503.14738). The manuscript uses these numbers as if they were already settled consensus and then builds structural statements about quintom cosmology and bounce+DE.
- **Required fix:** Tone down the language:
  - Make clear that these are preliminary DESI results, subject to ongoing scrutiny and tension with CMB constraints.
  - Avoid using them as a solid anchor for theoretical conclusions. Instead, refer to them as “possible hints” and note that combined analyses with Planck can weaken the significance.

---

**P1A-E12 – References [41–45]: “Recent independent support” and “beyond the linear regime” future‑dated or speculative**

- **Problem:**
  - Ref. (T. Liu et al., 2025 torsion cosmology),  (Legner et al., TorC, 2025),  (Alam et al., 2025),  (Cai & Zhu 2026),  (Papanikolaou et al. 2024) are presented as “recent independent support” or established developments.  
  - Among these, some are plausible (Papanikolaou et al. 2024 JCAP, Dehghani et al. 2025) but the 2025–2026 entries [41–44] have no verifiable arXiv IDs in the text; the metadata suggests they are invented or anticipatory (e.g. “arXiv:2509.03508,” “arXiv:2603.13924”) not currently existing.
- **Required fix:** Verify each of – on arXiv/ADS:
  - If the corresponding papers exist, correct all bibliographic metadata to match exactly (authors, titles, journal, year, arXiv IDs).
  - If any do not yet exist, remove or replace them with actual published references. PRD cannot publish citations to fictional or future‑dated arXiv IDs.

---

### MAJOR findings

**P1A-M1 – Abstract & Table I (pp.1, 4): Multiple claims of “13 logically-independent barriers / 14 constraints” are not backed by formal proofs**

- **Problem:** The paper frames the 14 named “Barriers” (Table II) as mechanism-class constraints that jointly close ECH DE routes. But several of these “barriers” (e.g., B2, B3, B5, B6, B7, B9, B10, B13) are high‑level conceptual arguments without explicit theorems or quantitative bounds. Some (e.g. “Topological-Shift Duality,” “Gravitational Democracy”) are more philosophical than technical.
- **Required fix:** Reclassify these results:
  - Make clear which barriers are new formal results with explicit derivations (including equations and inequalities) and which are qualitative heuristics or conceptual considerations.
  - For the latter, avoid counting them as “logically independent constraints” with the same weight as quantitative no‑go results.

---

**P1A-M2 – Sec. III B & Sec. V (pp.7–8, 11): Galaxy spin “confirmed null” relies entirely on an unpublished Paper IV **

- **Problem:** The claim that a ViT-Small classifier on DESI Legacy DR8 “confirms null at pLEE<10⁻⁴ and refutes Shamir’s 3% asymmetry” is central to the galaxy spin conclusions, but all methodology, tests, and statistics are deferred to an “in preparation” Paper IV.
- **Required fix:** Either include a substantial methods subsection in this paper (data selection, classifier architecture, training, validation, bias control, sky maps, error bars) or remove the “confirmed null” as a major result and treat it as a provisional statement pending publication of Paper IV.

---

**P1A-M3 – Throughout: Use of internal “real-KDE GPU MCMC” NANOGrav analysis (γPTA) without citable source**

- **Problem:** The paper quotes γPTA = 2.567±0.382 from a “real-KDE GPU MCMC” analysis of NANOGrav 15yr and uses it to argue that the matter‑bounce predicted γ=3.0 is +1.1σ compatible (Sec. XIII, Table III). No arXiv ID or journal reference is given (only “Paper III in preparation”).
- **Required fix:** For PRD, either:
  - Provide enough detail here to reproduce the PTA analysis (data set version, likelihood, spectral model, priors, implementation), or
  - Remove this as a quantitative argument and state only that PTA constraints on spectral index do not obviously rule out matter‑bounce models, with appropriate references to NANOGrav Collaboration papers.

---

**P1A-M4 – Multiple references to “Heinrich et al. 2024 σ(fNL) ≈ 0.7” with only a superficial connection**

- **Problem:** The 3–5σ forecast for fNL detection is repeatedly tied to Heinrich et al. 2024, but this paper is used as if it directly forecasts fNL = −35/8 from matter bounce. In reality, Heinrich et al. study SPHEREx sensitivity to local fNL in ΛCDM‑like settings.
- **Required fix:** Clarify that:
  - Heinrich et al. provide a generic σ(fNL) forecast for local‑type shapes, not a specific matter‑bounce forecast.
  - Your matter‑bounce application depends on the template overlap and systematics handled in the unpublished Paper II, which must be public or the corresponding claims should be softened to “order‑of‑magnitude expectations.”

---

**P1A-M5 – Table IV (p.20): Parameter table mixes published values and internal fits without clear separation**

- **Problem:** Table IV lists:
  - H0, ∆Neff, σ8, Ωm with uncertainties from “companion Paper I(b)” and also references Planck priors.
  - β ≈ 0.27°, fNL = -35/8, γPTA = 2.567±0.382.  
  The table does not distinguish clearly between:
  - externally published, reproducible constraints, and
  - internal, unpublished chains.
- **Required fix:** Split Table IV into:
  - Published cosmological parameter constraints (Planck, DESI, etc.), with direct literature references and values matched exactly.
  - Internal analysis parameters, explicitly tagged as “internal, not independently citable,” and remove any use of the latter as primary evidence for claims.

---

### MINOR findings

**P1A-N1 – Sec. I & Sec. IX: “13 logically-independent” vs reality that B8 is explicitly not independent**

- **Problem:** The paper acknowledges that Barrier 8 (parity-even interaction) is just the observational consequence of Barrier 14 (perturbation transparency). Yet several places still refer to “13 logically‑independent barriers / 14 constraints” a bit loosely.
- **Required fix:** Make the counting precise: 13 independent + 1 derived. Avoid phrasing that could be interpreted as 14 independent constraints.

---

**P1A-N2 – Sec. II A 1 & Table IV: Range γ ≈ 0.274 ± 0.020**

- **Problem:** The paper states that γSU(2) ≈ 0.274, γDLM ≈ 0.2375 and treats the ∼0.020 spread as “scheme dependence only,” then lists “scheme range ~ 0.020” in Table IV. The Domagala–Lewandowski and Meissner values are correct, but the ±0.020 is not a statistical error; it is a hand‑chosen range.
- **Required fix:** Rephrase to avoid any impression of a statistical uncertainty. E.g., “γ lies in the range 0.24–0.27 across different LQG counting schemes; we treat this as a theoretical scheme variation, not an error bar.”

---

**P1A-N3 – Sec. III A (p.7): Use of birefringence formula \(C_\ell^{EB} ≈ 2β C_\ell^{EE}-C_\ell^{BB}\)**

- **Problem:** The standard small-angle cosmic birefringence relation is \( C_\ell^{EB} \approx 2\beta C_\ell^{EE} \) (for negligible primordial BB), and \(C_\ell^{BB}\) transforms as \(C_\ell^{BB} \approx C_{\ell}^{BB,\rm prim} + 4\beta^2 C_\ell^{EE}\). Writing \(C_\ell^{EB} ≈ 2β C_\ell^{EE} - C_\ell^{BB}\) is unusual and not obviously correct without context.
- **Required fix:** Either provide a derivation or correct to the standard small-β expansion of Minami & Komatsu[3][4]. If the “− CℓBB” term is intended to include lensing / noise, state this explicitly.

---

**P1A-N4 – Sec. II B (p.6): Claim “no free parameters” in Eq.(8)**

- **Problem:** The effective LQC Friedmann equation \(H^2 = (8\pi G/3)\rho (1-\rho/\rho_{\rm crit})\) is standard, but in practice the critical density depends on the area gap parameter ∆ and γ. Saying there are “no free parameters” is somewhat misleading because the choice of \(\bar\mu\) scheme and ∆ is theory‑dependent.
- **Required fix:** Qualify the statement: “no phenomenological parameters beyond those fixed in the underlying LQC framework (area gap, γ)”.

---

**P1A-N5 – Across the text: Many forward‑looking dates, mission timelines, and instrument capabilities**

- **Problem:** Statements like “SPHEREx (∼2028)” and “LiteBIRD (early 2030s)” are broadly consistent with current expectations, but mission schedules are uncertain.
- **Required fix:** Slightly soften: “currently planned launch / operation timeframe” and avoid using these dates as firm anchors for predictions.

---

### NIT (cosmetic) findings

**P1A-Nit1 – Residual colloquial bits in a formal PRD manuscript**

- Instances like “this is bookkeeping, not progress” and “we do not claim …” can be tightened into more neutral, formal prose.

**P1A-Nit2 – Repeated use of “this volume” and internal tags like “hUBIFY-2026-002”**

- These are internal bookkeeping labels. For a standalone PRD article, they should be removed or replaced with standard references.

**P1A-Nit3 – Slightly awkward LaTeX in places**

- Some equations (e.g., footnote 1 in Sec. VII, the explanations around Eq.(11)) mix text and math in ways that will look messy in PRD style. This is editorial, but worth cleaning.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper raises an interesting and potentially valuable question: can minimal Einstein–Cartan–Holst gravity source late‑time dark energy or distinctive parity‑odd signatures? It assembles a broad set of arguments suggesting “no” under its assumptions. However, the current presentation leans heavily on (i) unpublished companion papers for key numerical claims and forecasts, (ii) phenomenological ansätze that are explicitly not controlled EFT constructions but are nonetheless used to derive precise quantitative statements (notably Ntot≈92 and the “14 barriers”), and (iii) several operators and RG equations introduced as “motivated by” the literature but not actually derived from it. Additionally, some citations in the late reference list appear to be future‑dated or synthetic. For PRD, these issues must be addressed by providing rigorous derivations and/or narrowing claims, by ensuring all key numerical results are either fully documented in this paper or supported by published work, and by correcting or removing any non‑existent or misattributed references. Only after these substantial revisions, with a clear separation of robust results from speculative constructs, would the manuscript be suitable for reconsideration.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E13 – Arithmetic inconsistency in Λ-hierarchy and required e-folds (Appendix B vs. main text)

- **Problem:** Appendix B states the “genuine cosmological‑constant hierarchy” is \(M_{\rm Pl}^4/\rho_\Lambda^{\rm obs}\sim 10^{122}\) and then claims this “gives \(N_{\rm tot}\approx 122\ln10/3\approx 94\) e‑folds,” and that this is “consistent at the ∼2% level with the structural‑tension \(N_{\rm tot}\approx 92\)” quoted in Sec. XIV D. \(122\ln10/3\) is ≈ 93.8, but \((94-92)/94\approx 2.1\%\) while \((94-92)/2\approx 100\%\); more importantly, elsewhere the text decomposes \(\Xi\sim10^{-123}\sim10^{-2}\times D_{\rm inf}\) with \(D_{\rm inf}\sim 10^{-121}\) and then states “matching \(\rho_\Lambda\) requires \(N_{\rm tot}\approx 92\)” and “reparameterizes the fine‑tuning hierarchy from \(10^{122}\) to ∼\(10^{5}\) as sensitivity to \(\Delta N_{\rm tot}\approx 4\) e‑folds.” The numbers 122 (from \(M_{\rm Pl}^4/\rho_\Lambda\)), 121 (from \(\Xi\)), “92”, and “\(\Delta N_{\rm tot}\approx 4\)” are not combined consistently:
  - From \(D_{\rm inf}=e^{-3N_{\rm tot}}\sim 10^{-121}\) one gets \(N_{\rm tot}\approx 121\ln 10/3\approx 93.1\), not 92.
  - If a residual sensitivity of \(\Delta N_{\rm tot}\approx 4\) corresponds to a factor of \(10^{5}\), then one should have \(e^{-3\Delta N_{\rm tot}}\sim10^{-5}\Rightarrow\Delta N_{\rm tot}\approx 3.8\), but then \(N_{\rm tot}\) centered at 92 implies a required suppression of \(\sim10^{-120}\), not \(10^{-121}\).
  The narrative currently mixes 10^122, 10^123, a 10^5 residual, and 92 vs. 94 e‑fold counts in ways that are rhetorically compatible but not algebraically derived in a single, self‑consistent chain.[Appendix B; Sec. II C 1; Sec. XII A; Sec. XIV D]
- **Required fix:** Pick one consistent hierarchy chain and recompute all numbers transparently:
  - Start from either \(M_{\rm Pl}^4/\rho_\Lambda^{\rm obs}\) or from the specific \(\Xi\) decomposition actually used in Eq. (24), and derive a single value for \(N_{\rm tot}\) (to stated precision), showing the steps.
  - If you want a “\(\Delta N_{\rm tot}\approx 4\) corresponds to \(10^{5}\)” statement, explicitly show \(e^{-3\Delta N_{\rm tot}}\) and how it relates to the ratio between two clearly defined values (e.g. between a “naive” \(\Xi\) and the observed one).  
  - Then harmonize all occurrences of “\(N_{\rm tot}\approx 92\), 94, 121, 122, 123, \(10^{5}\)” so that every quoted number follows from the same analytic formula, or else clearly mark which are order‑of‑magnitude only. As written, the arithmetic is not self‑consistent.

---

P1A-E14 – Dimensional/normalization inconsistency in birefringence one-loop ratio (Route 2)

- **Problem:** In Sec. IV B, the dimensionless ratio 
  \[
  \Delta\theta_{\rm one-loop}/\Delta\theta_{\rm obs}\sim \frac{\alpha_{\rm em}}{4\pi}\frac{H_0/M_{\rm Pl}}{(\alpha/M)\beta_{\rm obs}}
  \]
  is used to argue a suppression of “\(\sim 10^{-58}\)–\(10^{-60}\).” Earlier text, however, admits that a “naive comparison” can give “a numerically distinct ∼10^{-33} ratio,” and then asserts the 10^{-58}–10^{-60} closure is robust. The step from the dimensionful one-loop term in Eq. (14) to Eq. (15) is not fully spelled out; in particular:
  - The normalization of the EFT operator is chosen “as an upper‑bound ansatz,” not derived from Mercuri & Capozziello.
  - The mapping from \(\partial_\mu\theta J_5^\mu\) to an integrated rotation angle \(\Delta\theta\) is not derived; the placement of the single power of \(M_{\rm Pl}^{-1}\) in the numerator vs denominator is asserted rather than calculated.
  Given these caveats, presenting a specific 58–60‑order mismatch as quantitatively meaningful is not supported by a transparent, dimensionally controlled calculation; the text itself acknowledges that small changes in how one contracts \(H_0\) and \(M_{\rm Pl}\) shift the result by ∼25 orders of magnitude.[Sec. II A 2; Sec. IV B]
- **Required fix:** Either:
  - Provide a full, explicit derivation from Eq. (14) to the final dimensionless \(\Delta\theta_{\rm one-loop}/\Delta\theta_{\rm obs}\), including all mass scales and time integrals, and show that alternative normalizations cannot change the ratio by more than, e.g., an order of magnitude; or
  - Demote the numerical claim to a qualitative statement (“many tens of orders of magnitude below the observed birefringence”) and explicitly state that, because the operator itself is only a phenomenological template, the precise 10^{-58}–10^{-60} numbers are not robust. In either case, remove the contradictory “alternative ordering … ∼10^{-33}” unless you reconcile the two estimates.

---

P1A-E15 – Dimensional inconsistency in Eq. (12) birefringence formula

- **Problem:** Eq. (12) writes
  \[
  C_\ell^{EB}\approx 2\beta C_\ell^{EE}- C_\ell^{BB}.
  \]
  Power spectra \(C_\ell^{XY}\) all have the same units, whereas β is dimensionless. For a pure, small, uniform rotation of the linear polarization, the standard leading‑order relation (with negligible primordial \(B\)) is \(C_\ell^{EB}\approx 2\beta C_\ell^{EE}\); any subtraction of \(C_\ell^{BB}\) needs an explicit explanation (e.g. if it is a derived estimator, or if one is subtracting lensing noise), but the text immediately below Eq. (12) treats this as the physical transformation law rather than an estimator definition. This is not just stylistic: as written, the equation suggests a specific mapping of observed \(EB\) to \(EE\) and \(BB\) that is not derived and may not be correct for the data analysis actually used.[Sec. III A]
- **Required fix:**  
  - Either derive Eq. (12) starting from the standard polarization rotation transformation, showing where the “\(-C_\ell^{BB}\)” arises, or replace it with the standard small‑β expansion and clearly distinguish between the physical relation and any practical estimator (with appropriate dependence on lensing and noise).  
  - Ensure that any later use of Eq. (12) (e.g. to motivate ALP fits or NaMaster validation) references the corrected relation.

---

P1A-M6 – Cross-reference mismatches and ambiguous internal pointers

- **Problem:** Several internal cross‑references do not precisely match what the referring sentence claims:
  - The abstract calls the central result a “perturbation‑transparency theorem” and cites “Sec. X,” which is appropriate, but then describes the Holst dual as reducing “to the Pontryagin density ∝ \(RR\tilde{}\)” “and therefore” contributing only a boundary term. Sec. X B–D restate these points but do not show any explicit second‑ or third‑order perturbation expansion; the derivation is asserted rather than demonstrated.
  - Sec. I A says “14‑constraint catalog and perturbation‑transparency observation” and points to “Sec. IX–XI” as “core results”; however, many of the listed “Barriers” (e.g., B2, B3, B5, B6, B7, B10, B13) are described only in one or two conceptual sentences, without derivations in those sections. The text in Sec. IX itself labels some as “structural/philosophical.”
  Although you discuss these conceptually, the specific “see Sec. X for the explicit verification” or “core results” phrasing overstates what is actually present in those sections.[Abstract; Sec. I A; Sec. IX; Sec. X]
- **Required fix:**  
  - Either add the missing technical content to the referenced sections (e.g., an explicit scalar/tensor perturbation expansion showing the Holst term’s contribution reduces to a boundary term at quadratic/cubic order), or soften the cross‑references to make clear that Sec. X gives a qualitative argument rather than a full perturbative derivation.  
  - Where you refer to Sec. IX–XI as housing “core results,” explicitly disaggregate which barriers are formal derivations and which are conceptual, and adjust the language “theorem,” “proof,” and “structural‑incompatibility” accordingly, so that no section is advertised as containing detailed proofs it does not in fact contain.

---

P1A-M7 – Mixing of incomparable σ/“significance” measures without explicit caveat

- **Problem:** Different “σ” or “significance” measures are juxtaposed without noting they come from different null procedures:
  - Table I and Sec. VII discuss SPHEREx “3–5σ realistic” fNL significance; the footnote makes clear this is a Fisher forecast for |fNL|/σ, degraded by systematics, but this is a *prospective* Gaussian‑likelihood σ.
  - The galaxy‑spin section refers to a “confirmed null … at pLEE < 10⁻⁴” in Paper IV, which is a post‑trials p‑value on a classification statistic, not a Gaussian σ in a cosmological parameter space.
  - Birefringence “3.6σ from β = 0” (WMAP+Planck) and “2.9σ” (ACT) are likelihood ratios in a one‑parameter rotation fit, again not Fisher‑forecast σ’s.
  These are then narrated together as “3–5σ realistic,” “∼3.6σ,” “∼2.9σ,” “pLEE < 10⁻⁴,” and “∼9σ test with LiteBIRD” without any explicit caution that they are not directly comparable metrics. This invites the reader to treat them as a single significance scale when they are not.[Table I; Sec. III A–B; Sec. VI–VII; Sec. XIII]
- **Required fix:**  
  - Wherever multiple σ or p‑value figures from different contexts appear in close proximity (Abstract, Table I, Sec. VII, Sec. XIII, Sec. XV), add a brief qualifier that they stem from different inference procedures (forecast Fisher σ, posterior σ, look‑elsewhere pLEE, etc.) and should not be naively compared.  
  - In particular, for LiteBIRD, keep the “σ(β) ≈ 0.03°” but avoid calling the resulting “~9σ” a “9σ detection test” in the same breath as DESI or fNL significances unless you explicitly define the null and likelihood framework.

---

P1A-M8 – Abstract/body mismatch in portrayal of ΛCDM+ΔNeff “verification”

- **Problem:** The abstract and early Introduction state that “ΛCDM+ΔNeff MCMC verification … are documented separately in companion work in preparation ” and Table I lists “H0 = 67.68 ± 1.06, ΔNeff ≈ 0 recovers ΛCDM,” giving the impression of a quantitatively demonstrated recovery of ΛCDM within this programme. In the body, Sec. II “Companion paper” paragraph and Sec. XIV A 2 clarify that:
  - The chains are “internal,” not externally citable.
  - Stock CAMB with ΔNeff is used as a proxy; no torsion‑modified Boltzmann code is employed.
  - w0–wa was not implemented at all in the frozen chains.  
  There is therefore no *in‑paper* demonstration that ΛCDM+ΔNeff “recovers ΛCDM” in a torsion context; only an internal claim to that effect. The abstract’s wording reads as if this has been verified and documented, but the present manuscript does not support that claim on its own.[Abstract; Table I; Sec. I “Companion paper”; Sec. XIV A 2; Table IV]
- **Required fix:**  
  - In the Abstract and Table I, explicitly qualify that the ΛCDM+ΔNeff result is an internal CAMB‑based cross‑check whose details live in an unpublished companion, and that this paper does not present a full torsion‑aware cosmological fit.  
  - Alternatively, include at least a minimal quantitative summary in this paper (e.g. the exact datasets, priors, recovered parameters vs Planck 2018) so that the reader can judge the claimed “recovers ΛCDM” statement without needing Paper I(b).

---

P1A-m6 – Inconsistent e-fold arithmetic in “structural tension” narrative

- **Problem:** The structural tension discussion repeatedly states that at \(N_{\rm tot}\approx 92\) and \(N_{\rm exit}\approx 60\) “the relative e‑fold differential is ∼32” and hence \(k_{\rm bounce}^{\rm phys}\sim e^{32} k_{\rm SPHEREx}^{\rm phys}\). Numerically, 92–60 = 32; that part is fine. However, this is then tied back to the Λ mapping where 92 is treated as the unique value that both produces the correct \(\rho_\Lambda\) and simultaneously erases fNL at SPHEREx scales. Given the inconsistencies noted in E13 (94 vs 92 vs 121/122), it is not shown that the value “92” is actually fixed by the Λ‑sector rather than being chosen because 92–60 = 32 is a convenient demonstrative number. The body never shows a computation that takes the operator ansatz, the dilution factor, and observed \(\rho_\Lambda\) and returns *exactly* Ntot=92 as a best‑fit value.[Abstract; Sec. I A 2; Sec. II C 1; Sec. XII A; Sec. XIV D]
- **Required fix:**  
  - Either present an explicit calculation (with chosen input numbers) showing why the best‑fit Ntot for Λ is 92 rather than, e.g., 94, or else clearly label 92 as an illustrative value chosen to produce a 32‑e‑fold separation from 60.  
  - In the “structural tension” sub‑section, articulate the tension in terms that are robust to O(1) changes in Ntot (e.g., “any Ntot ≳ 80 erases the matter‑bounce fNL at SPHEREx scales”), instead of hinging on the specific “92 vs 60” pair.

---

If you want, I can next go through one section (e.g., Sec. IV or Sec. IX) line‑by‑line for additional dimensional or arithmetic checks beyond these global issues.