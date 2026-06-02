# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round5
**Wall time**: 20.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34312, completion=2027, total=36339, search_context_size=low, cost={'input_tokens_cost': 0.10294, 'output_tokens_cost': 0.03041, 'request_cost': 0.006, 'total_cost': 0.13934}

---

## PAPER-B1 – Mis-citation of Shapiro–Teixeira paper

**Issue (BLOCKER):**  
In the front-matter comment the author writes that “Shapiro & Teixeira, ‘Quantum Einstein-Cartan theory with the Holst term,’ CQG 31:185002 (2014)” exists at arXiv:1402.4854 and that this falsifies an earlier review claim. In reality, arXiv:1402.4854 is “Quantum Einstein–Cartan gravity with the Holst term” by *I. L. Shapiro and P. M. Teixeira*, published in **Class. Quant. Grav. 31 (2014) 185002**, but the title is “Quantum Einstein–Cartan gravity with the Holst term” (gravity, not theory). The paper also sometimes calls it “Quantum Einstein-Cartan gravity with the Holst term” in the text; mixing “theory” vs “gravity” and the exact title while using the correct arXiv ID and journal is sloppy and undermines the “FALSIFIED” claim about a prior reviewer.  
**Fix:** Standardize to the exact published title “Quantum Einstein–Cartan gravity with the Holst term” wherever this paper references Shapiro & Teixeira, and soften the “FALSIFIED” language about the earlier reviewer (they were checking a slightly different title string).


## PAPER-M1 – Domagała–Lewandowski–Meissner attribution / values

**Issue (MAJOR):**  
The text claims “the refined SU(2) full counting gives \(\gamma_{\rm SU(2)}\approx 0.274\)… and the further Domagała–Lewandowski–Meissner refinement gives \(\gamma_{\rm DLM}\approx 0.2375\). Domagała–Lewandowski and Meissner do not quote a ±0.020 statistical uncertainty.” Domagała & Lewandowski (Class. Quant. Grav. 21 (2004) 5233, arXiv:gr-qc/0407051) and Meissner (Class. Quant. Grav. 21 (2004) 5245, arXiv:gr-qc/0407052) indeed obtain \(\gamma \approx 0.274\) and \(\gamma \approx 0.2375\) as separate preferred values in different counting schemes; they do **not** introduce a “DLM” notation or a “scheme range ~0.020” as an effective error bar, and they are not a sequential “refinement” of the same scheme but distinct approaches. Treating the difference as a 0.020 “range” attributable to “further refinement” is interpretive, not what those papers say.  
**Fix:** Rephrase to: (i) clearly attribute \(\gamma\approx0.274\) and \(\gamma\approx0.2375\) to different counting prescriptions in Domagała–Lewandowski and Meissner, (ii) drop the coined label “\(\gamma_{\rm DLM}\)” and the language of a single “refinement,” and (iii) state explicitly that the \(\sim 0.02\) spread is an internal scheme-comparison used in this work, not an uncertainty quoted by those authors.


## PAPER-M2 – Date–Kaul–Sengupta “schematic” RG equation

**Issue (MAJOR):**  
Section \(\ref{sec:r3_immirzi}\) introduces an RG equation  
\[
\frac{d\gamma}{d\ln\mu} = \frac{1}{12\pi^2}(N_F^L-N_F^R)\gamma + \mathcal{O}(\gamma^2)
\]  
and says this is “schematically motivated by” Date, Kaul & Sengupta. The cited paper (S. Date, R. K. Kaul, S. Sengupta, Phys. Rev. D79 (2009) 044008, arXiv:0811.4496) analyzes Holst+Nieh–Yan with chiral matter, but does **not** derive this specific beta function or the 1/(12π²)(N_F^L−N_F^R) coefficient; using this precise form and attributing its structure to DKS, even with “schematically motivated,” is still too strong and can be read as a concrete derivation.  
**Fix:** Explicitly state that Eq. (γ-running) is an ad hoc EFT ansatz chosen for order-of-magnitude illustration, not derived in DKS, and adjust the text to say DKS only motivates the possibility of chiral-matter–induced running, not the form or size of the beta function.


## PAPER-M3 – Lue–Wang–Kamionkowski operator normalization

**Issue (MAJOR):**  
For Route 4, the paper states that “Lue, Wang & Kamionkowski… work with a generic pseudoscalar-photon Chern–Simons coupling \(\partial_\mu\phi K^\mu\)… The operator \(\mathcal{L}_{\rm CS}\supset -\tfrac14(\alpha/M)\theta \tilde F F\) is the conventional ALP–photon coupling; we adopt this normalization and use LWK as an early example.” The original LWK paper (C. Lue, L. Wang, M. Kamionkowski, Phys. Rev. Lett. 83 (1999) 1506, arXiv:astro-ph/9812088) uses a specific Chern–Simons form with its own normalization conventions, but **does not** introduce the \(-\tfrac14(\alpha/M)\theta F\tilde F\) form or the \(\alpha/M \sim 10^{-21}\,\mathrm{GeV}^{-1}\) estimate. The text blurs the line between “we follow conventional ALP notation” and “early treatment by LWK,” which can be misread as LWK supporting the chosen normalization and numerical bound.  
**Fix:** Sharpen the attribution: say explicitly that \(-\tfrac14(\alpha/M)\theta F\tilde F\) is standard ALP–photon notation taken from the axion literature in general (not from LWK), that LWK is cited only as an early discussion of cosmological birefringence from such terms, and that the numerical bound \(\alpha/M \sim 10^{-21}\,\mathrm{GeV}^{-1}\) is derived within the present paper’s conventions and current CMB data, not from LWK.


## PAPER-m1 – Ashtekar–Singh critical-density range

**Issue (minor):**  
The paper states Ashtekar & Singh “quote the canonical LQC value \(\rho_{\rm crit} \simeq 0.41\rho_{\rm Pl}\)” and then says “substituting instead \(\gamma_{\rm SU(2)}\approx0.274\)… gives \(\rho_{\rm crit}\simeq 0.27\rho_{\rm Pl}\); this lower value is an internal extrapolation… not a value quoted in Ref. [Ashtekar2011].” Ashtekar & Singh (Class. Quant. Grav. 28 (2011) 213001, arXiv:1108.0893) indeed give \(\rho_{\rm crit}\approx 0.41\rho_{\rm Pl}\) for a standard area gap; they do not give 0.27, and they also caution that precise dependence on \(\gamma\) involves the area-gap choice. The current explanation is mostly correct but still ambiguous about whether the 0.27 value reflects a legitimate re-evaluation in LQC or a rough scaling using a different \(\gamma\).  
**Fix:** Add one clarifying sentence that 0.27 is obtained by naively inserting \(\gamma=0.274\) into the same effective formula used by Ashtekar–Singh, without a full re-derivation in LQC, and that no LQC paper has actually quoted \(\rho_{\rm crit}=0.27\rho_{\rm Pl}\); this keeps the distinction between cited and internally inferred numbers explicit.


## PAPER-m2 – Cai et al. matter-bounce \(\boldsymbol{f_{\rm NL}=-35/8}\) citation

**Issue (minor):**  
The paper repeatedly attributes \(\fnl=-35/8\) to “Cai:2009fn” and describes it as a generic matter-bounce-class prediction. The arXiv:0906.3341 paper (“A Matter Bounce Cosmology”) by Yi-Fu Cai et al. does derive this value for a specific single-field matter bounce model and under particular assumptions, not as a universal statement for all “matter-bounce class” scenarios. The text does partly acknowledge assumptions (later referencing “Assumption (f) of Paper II”) but the initial description in the abstract and early sections is still too universal.  
**Fix:** In the early mentions (abstract, Table 1 caption, first introduction of \(\fnl=-35/8\)), add “in the single-field matter-bounce model of Cai et al. (2009)” or “for the specific scalar-only matter-bounce setup of Cai et al.” so the scope of the cited result matches the original paper.
