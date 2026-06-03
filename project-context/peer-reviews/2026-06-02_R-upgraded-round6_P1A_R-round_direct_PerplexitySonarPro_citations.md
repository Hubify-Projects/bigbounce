# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round6
**Wall time**: 18.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=35543, completion=1738, total=37281, search_context_size=low, cost={'input_tokens_cost': 0.10663, 'output_tokens_cost': 0.02607, 'request_cost': 0.006, 'total_cost': 0.1387}

---

## PAPER-PER-B1 (BLOCKER) – Shapiro & Teixeira 2014 mis-cited

**Location:** Route 2, Step 4: Parity-odd coefficient, Eq. (oneloop), around `\label{eq:oneloop}`.  

**Issue:** The text attributes the one-loop estimate and formula
\(\alpha/M \sim \frac{g^2}{32\pi^2}\frac{\gamma}{M}\ln(\Lambda_{\rm UV}^2/\mu^2)+\delta_{\rm NY}\)
to “Freidel et al. and Shapiro & Teixeira 2014.” Shapiro & Teixeira’s paper *“Quantum Einstein-Cartan theory with the Holst term”* (Class. Quant. Grav. 31 (2014) 185002, arXiv:1402.4854) develops the quantum EC–Holst theory but does **not** contain this specific operator or numerical estimate; the formula is a phenomenological ansatz assembled by the author, not literally present in that paper.[ ]  

**Fix:** Rephrase the attribution to: “Motivated by the structures discussed in Freidel et al. and in Shapiro & Teixeira’s quantum EC–Holst analysis, we adopt the following phenomenological one‑loop estimate…” and explicitly state that this exact coefficient and logarithm are not derived in those references.


## PAPER-PER-M1 (MAJOR) – Mercuri / Mercuri–Capozziello operator attribution

**Location:** Sec. “Derivation of the Parity-Odd Term,” Step 3 and Step 4; also Route 2 discussion of Mercuri & Mercuri–Capozziello.  

**Issue:** The text now correctly says the operator is “motivated by but not literally derived in” Mercuri and Mercuri–Capozziello, but still repeatedly blurs the line between (i) their classical Holst+Nieh–Yan+fermion constructions and (ii) the specific EFT operator and one‑loop coefficient used here. The actual Mercuri (2009) and Mercuri–Capozziello (Phys. Rev. D 78, 021301 (2008), arXiv:0805.4238) papers do not present this exact \((\alpha/M)\,e\wedge e\wedge\mathcal F\) operator or the numeric \(\alpha_{\rm em}/(4\pi)\) normalization adopted later.[ ]  

**Fix:** Add one explicit sentence in both locations: “Neither Mercuri (2009) nor Mercuri & Capozziello (2008) derive the specific operator in Eqs. (…); we construct it as the simplest EFT structure consistent with their classical Holst–Nieh–Yan setup, and we treat all coefficients as phenomenological.”


## PAPER-PER-M2 (MAJOR) – Lue–Wang–Kamionkowski normalization

**Location:** Route 4, first paragraph of Sec. `\ref{sec:r4_birefringence}`.  

**Issue:** The text says Lue, Wang & Kamionkowski “work with a generic pseudoscalar-photon Chern–Simons coupling \(\partial_\mu\phi K^\mu\) (equivalently \(\phi F\tilde F\) up to a total divergence), not with the specific \(-\tfrac14 (\alpha/M)\theta \tilde F F\) normalization adopted here,” but earlier versions framed LWK as the source of that normalization. LWK (Phys. Rev. Lett. 83, 1506 (1999), arXiv:astro-ph/9812088) indeed use a generic \(\phi F\tilde F\) term without this particular \(\alpha/M\) identification.[ ] The body text is mostly corrected, but the remaining phrasing “operator … is the conventional ALP-photon coupling used throughout the literature” still implicitly suggests a literature-standard value for \(\alpha/M\) that does not exist.  

**Fix:** Clarify: “The normalization \(-\tfrac14(\alpha/M)\theta F\tilde F\) is a conventional EFT parametrization we adopt; neither Lue–Wang–Kamionkowski nor any specific reference fixes the numerical value of \(\alpha/M\), which we treat as a free phenomenological parameter constrained by data.”


## PAPER-PER-m1 (minor) – Ashtekar & Singh 2011 critical density window

**Location:** Sec. `\ref{sec:bounce}`, Eq. `\ref{eq:rhocrit}` and the paragraph immediately following.  

**Issue:** Ashtekar & Singh (Class. Quant. Grav. 28 (2011) 213001, arXiv:1108.0893) review LQC and quote the standard critical density \(\rho_c \approx 0.41\,\rho_{\rm Pl}\) for the usual choice \(\gamma\simeq0.2375\); they do **not** present a “0.27–0.41” window.[ ] The text states this correctly in the second half of the paragraph (0.27 is an internal extrapolation) but earlier in the paper and Table 2 it sometimes reads like a published “LQC window.”  

**Fix:** Everywhere this appears, standardize the wording to “we use a scheme‑dependent internal range \(\rho_c \in [0.27,0.41]\,\rho_{\rm Pl}\), where 0.41 is the canonical LQC value quoted in Ashtekar & Singh and 0.27 is our own extrapolation obtained by inserting \(\gamma_{\rm SU(2)}=0.274\) into the same formula; the 0.27–0.41 interval is not a published LQC range.”


## PAPER-PER-m2 (minor) – Cai et al. 2009 matter-bounce \(\boldsymbol{f_{\rm NL}=-35/8}\) statement

**Location:** Abstract and Secs. `\ref{sec:intro}`, `\ref{sec:surviving}`, and Table~\ref{tab:bounce_disc}.  

**Issue:** The paper repeatedly attributes \(\fnl=-35/8\) as the “matter-bounce class” prediction citing Cai et al. 2009 (e.g. JCAP 10 (2009) 003, arXiv:0904.0822). That work indeed derives \(\fnl=-35/8\) for a specific single-field matter bounce with \(w=0\) and particular matching; it is not a universal prediction of *all* “matter-bounce class” models (e.g. ekpyrotic, non-scalar, or multi-field bounces give different shapes and amplitudes).[ ]  

**Fix:** Soften the phrasing to: “\(\fnl = -35/8\) is the prediction for the simplest scalar-only \(w=0\) matter-bounce model of Cai et al. (2009); we use it as a benchmark for that subclass of bounces, not as a universal value for all ‘matter-bounce’ scenarios.”


## PAPER-PER-n1 (nit) – Golden2026 companion papers labeled as “in preparation”

**Location:** Multiple: abstract, intro “Companion paper” paragraph, Route 4 discussion, falsification section, appendices.  

**Issue:** All references `Golden2026P1b`, `Golden2026P2`, `Golden2026P3`, `Golden2026P4` are cited as “in preparation,” but they are not discoverable via arXiv/ADS or journal databases at present. There is no fabrication implied, but readers cannot verify any numerical or methodological claims that depend on them.  

**Fix:** Keep the citations but add one explicit sentence early in the paper clarifying that these are internal manuscripts not yet available on public repositories, and that any key quantitative results depending on them (e.g. MCMC posteriors, Fisher matrices) should be regarded as non‑reproducible until those companions are posted.
