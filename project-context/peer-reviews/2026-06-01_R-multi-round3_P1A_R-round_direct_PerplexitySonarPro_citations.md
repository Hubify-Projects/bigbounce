# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round3
**Wall time**: 21.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33125, completion=2277, total=35402, search_context_size=low, cost={'input_tokens_cost': 0.09938, 'output_tokens_cost': 0.03415, 'request_cost': 0.006, 'total_cost': 0.13953}

---

## PAPER-PER-B1 – Mis-cited Shapiro & Teixeira paper

**Severity:** MAJOR  

**Location:** Sec. 2.1.3, Step 4: Parity-Odd Coefficient, around Eq. (12) “Following Freidel et al. [Freidel2005] and Shapiro & Teixeira [ShapiroTeixeira2014] …”  

**Issue:** I cannot find any paper by “Shapiro & Teixeira” matching the year, context, or claimed content (a one‑loop estimate giving \(\alpha_{\rm em}/(4\pi)\)-type coefficient in an ECH/Nieh–Yan setting). Searches on arXiv/ADS and publisher databases show Shapiro coauthors on torsion/anomaly work (e.g., with Sokolov, Mielke, etc.), but not with any “Teixeira” on a paper whose results align with the described one‑loop parity‑odd coefficient.[ ] The `ShapiroTeixeira2014` citation appears to be either fictional or metadata‑fused (author combination and/or year not corresponding to a real paper with that result.  

**Fix:** Replace `ShapiroTeixeira2014` with the correct existing torsion/anomaly reference that actually contains the one‑loop result you are summarizing (or drop it and state clearly that the coefficient is a generic one‑loop \(\alpha_{\rm em}/4\pi\) estimate without a specific source). Update the bibliography entry accordingly.

---

## PAPER-PER-M1 – Misleading attribution of Route‑2 one‑loop structure to Mercuri / Mercuri–Capozziello

**Severity:** MAJOR  

**Location:** Sec. 4.2, paragraph introducing Eq. (36) (Route 2 parity‑odd operator)  

**Issue:** The text states that the one‑loop operator  
\[
\Gamma_{\rm one\text{-}loop}^{\rm parity\text{-}odd}
= -\frac{1}{16\pi^2}\frac{\beta(\gamma)}{M_{\rm Pl}}
\int d^4x\sqrt{-g}\,\partial_\mu\theta\,J^{5\mu}
\]
is “motivated by (but not literally derived in) the Holst+non‑minimal‑fermion construction of Mercuri and Mercuri & Capozziello,” and that those works “establish … not this exact one‑loop operator.” That’s already partially caveated, but the paragraph still strongly suggests there is a concrete one‑loop structure in those papers that bounds the coefficient. In reality, Mercuri (2006, 2009) and Mercuri & Capozziello (2008) discuss Holst/Nieh–Yan structure, non‑minimal fermion couplings, and anomaly/coefficient issues, but do not contain an explicit EFT operator of the form \(\partial_\mu\theta\,J^{5\mu}/M_{\rm Pl}\) with the stated prefactor.[ ] The current wording is right on the edge of over‑attribution.  

**Fix:** Tighten the attribution to something like: “Guided by the Holst+Nieh–Yan and non‑minimal fermion analyses of Mercuri and Mercuri & Capozziello, which clarify how chiral anomalies and \(\gamma\) enter but do not present this specific EFT operator, we introduce as an explicit phenomenological ansatz the parity‑odd term in Eq. (36) and use it only as an upper‑bound template for Route 2.” Make clear that no existing paper provides this exact operator or its coefficient.

---

## PAPER-PER-M2 – Overstated “one-loop estimate” language for \(\alpha/M\)

**Severity:** MAJOR  

**Location:** Sec. 2.1.3, Step 4 “Parity‑Odd Coefficient,” Eq. (13) and surrounding text  

**Issue:** The paragraph says “the one‑loop estimate is  
\[
\frac{\alpha}{M} \sim \frac{g^2}{32\pi^2}\frac{\gamma}{M}\ln\Big(\frac{\Lambda_{\rm UV}^2}{\mu^2}\Big)+\delta_{\rm NY},
\]
motivating the order of magnitude \([(\alpha/M)M_{\rm Pl}]\sim10^{-2}\).” I cannot locate a published calculation with this specific structure and interpretation (especially the explicit \(\gamma/M\) factor and “\(\delta_{\rm NY}\)” piece) in the Holst/Nieh–Yan literature you cite (Freidel–Minic–Takeuchi; Mercuri; related anomaly papers).[ ] The equation appears to be an internally constructed schematic, not a literal “one‑loop estimate” from the literature. Calling it “the” one‑loop estimate reads as if it’s directly sourced from existing work.  

**Fix:** Rephrase to emphasize this is a schematic EFT scaling ansatz inspired by generic one‑loop behavior, not a published calculation: e.g., “At the level of dimensional and loop‑factor power counting, a generic one‑loop chiral correction would give a coefficient of order \(g^2/16\pi^2\) times appropriate mass scales; we therefore adopt the schematic form (13) as a phenomenological parametrization and treat \(\alpha/M\) as a free parameter, not as a derived one‑loop prediction.”

---

## PAPER-PER-M3 – Ambiguous dependence on companion papers labeled “in preparation”

**Severity:** minor  

**Location:** Abstract and multiple places citing Golden2026P1b / P2 / P3 / P4 as `[Golden2026P1b]`, `[Golden2026P2]`, etc.  

**Issue:** The text treats several “Paper I(b), II, III, IV” items as if they were standard references—complete with arXiv‑style keys—but they are described explicitly as “in preparation” and have no arXiv identifiers or published DOIs yet. There is no external way for a referee or reader to verify claims like “detailed multi‑tracer Fisher forecast in Paper II” or “real‑KDE GPU‑MCMC reanalysis in Paper III” against actual documents. That’s fine for internal documentation but inconsistent with normal arXiv/journal referencing practice, and the arXiv‑style labels risk being interpreted as existing submissions.  

**Fix:** Clearly tag all such entries in the text and in the `.bbl` as “internal companion, in preparation (not yet publicly available)” and avoid phrasing like “Ref. [Golden2026P2]” without that qualifier. If possible, replace some of these with brief in‑paper summaries of the specific quantitative facts you need, so that key claims do not rest solely on inaccessible documents.

---

## PAPER-PER-m1 – CMB birefringence measurement chain not fully traceable

**Severity:** minor  

**Location:** Sec. 3.1 and Sec. 4.4, references to “Planck/ACT DR6 3.6σ signal” and \(\beta_{\rm obs}=0.342^\circ\pm0.094^\circ\) citing `[Minami2020, Eskilt2022b, DiegoPalazuelos2025]`  

**Issue:** Minami & Komatsu (2020) and Eskilt (2022) indeed report non‑zero isotropic birefringence detections with \(\beta\) in the 0.3° range and significances \(\sim 2.4\)–\(3\sigma\), but I do not find any current, public “Planck/ACT DR6 joint 3.6σ” paper with exactly \(\beta=0.342^\circ\pm0.094^\circ\).[ ] The third reference, “DiegoPalazuelos2025,” appears not to correspond to a currently existing arXiv preprint or journal article (no such author combination and year on birefringence shows up), so the exact numerical combination and “DR6 joint” description are not externally checkable.  

**Fix:** Anchor the quoted \(\beta\) and significance to specific, extant birefringence analyses with verifiable numbers (e.g. Minami & Komatsu 2020; subsequent ACT‑only or Planck‑only updates), and either remove or clearly flag any not‑yet‑public “DiegoPalazuelos2025”/“Planck+ACT DR6 joint” combination as internal work in preparation rather than as a standard citation.

---

## PAPER-PER-m2 – Over‑specific wording about “canonical LQC value” for \(\rho_{\rm crit}\)

**Severity:** minor  

**Location:** Sec. 2.2, Eq. (11) and the paragraph on \(\rho_{\rm crit}\simeq0.27\)–\(0.41\,\rho_{\rm Pl}\) attributed to Ashtekar & Singh (2011)  

**Issue:** Ashtekar & Singh’s LQC review indeed gives \(\rho_{\rm crit}\approx0.41\rho_{\rm Pl}\) for the standard choice \(\gamma\simeq0.2375\); they do not present a scheme‑dependent “0.27–0.41” window as a published range, nor a value at \(\gamma=0.274\).[ ] You already note that \(\rho_{\rm crit}\simeq0.27\rho_{\rm Pl}\) is an internal extrapolation using a different \(\gamma\), but the phrase “Ashtekar & Singh quote the canonical LQC value 0.41…” followed immediately by “Substituting instead the SU(2) black‑hole‑entropy value \(\gamma_{\rm SU(2)}\approx0.274\)… gives 0.27” is easy to misread as both endpoints being “quoted” results.  

**Fix:** Slightly sharpen the wording so that only \(0.41\,\rho_{\rm Pl}\) is described as the “quoted” Ashtekar–Singh value, and the 0.27 value is explicitly labeled as your own extrapolation (e.g. “Using their formula but substituting \(\gamma=0.274\) yields an internally‑computed value \(\rho_{\rm crit}\approx0.27\rho_{\rm Pl}\), which is not quoted in Ref. [Ashtekar2011] and should be regarded as a scheme‑variation illustration rather than a published LQC result.”).
