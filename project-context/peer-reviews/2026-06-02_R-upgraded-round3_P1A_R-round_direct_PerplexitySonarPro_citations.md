# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round3
**Wall time**: 27.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=35592, completion=2536, total=38128, search_context_size=low, cost={'input_tokens_cost': 0.10678, 'output_tokens_cost': 0.03804, 'request_cost': 0.006, 'total_cost': 0.15082}

---

## PAPER-PER-B1 — BLOCKER — Mis-cited Shapiro & Teixeira paper

**Location:** Around comments on PER-B1 (round 3), early metadata block and §II.A Step 4 (Eq. \eqref{eq:oneloop}).  

**Issue:** The paper asserts that “Shapiro & Teixeira, *Quantum Einstein-Cartan theory with the Holst term*, CQG 31:185002 (2014)” is arXiv:1402.4854 and uses it as the source for the one-loop Holst / Nieh–Yan parity-odd coefficient estimate.[1][2] In reality, arXiv:1402.4854 is *“Quantum Einstein-Cartan gravity with the Holst term”* by I.L. Shapiro and H. Takata (not Teixeira), published in *Class. Quant. Grav.* 31 (2014) 185002.[1][3] The author name and spelling are wrong, and there is no Teixeira on that paper.  

**Fix:** Correct the citation metadata everywhere to “I.L. Shapiro and H. Takata, *Quantum Einstein–Cartan gravity with the Holst term*, Class. Quant. Grav. 31 (2014) 185002, arXiv:1402.4854” and ensure Teixeira is not listed as coauthor; re-check the .bib/.bbl entry for consistency with arXiv and CQG.

---

## PAPER-PER-M1 — MAJOR — Date–Kaul–Sengupta versus Benedetti–Speziale sourcing

**Location:** §IV.3 Route 3 (Immirzi running), especially Eq. \eqref{eq:gamma_running} and surrounding prose; early metadata block describing prior fixes.  

**Issue:** The text claims the prefactor and form of the Immirzi running in Eq. \eqref{eq:gamma_running} are only “schematically motivated” by Date–Kaul–Sengupta and cites Benedetti & Speziale as the correct source for fermion-induced Immirzi running.[4][5] However, Benedetti–Speziale’s actual beta-function for \(\gamma\) in Einstein–Cartan–Holst gravity with fermions is more complicated than the simple proportionality in Eq. \eqref{eq:gamma_running}, and they do not give the specific \((1/12\pi^2)(N_F^L-N_F^R)\gamma\) form used here.[4] DKS also do not present that equation.[5] As written, the equation risks being read as directly taken from the literature when it is not.  

**Fix:** Add an explicit sentence here clarifying that Eq. \eqref{eq:gamma_running} is an ad hoc EFT toy ansatz constructed for order-of-magnitude bounding, not the beta-function computed in either Date–Kaul–Sengupta or Benedetti–Speziale; keep both citations but remove any implication that either paper derives this specific RG form.

---

## PAPER-PER-M2 — MAJOR — Lue–Wang–Kamionkowski operator normalization

**Location:** §IV.4 Route 4 (birefringence), paragraph discussing Lue, Wang & Kamionkowski; Eq. for \(\mathcal{L}_{\rm CS}\).  

**Issue:** The paper states that Lue–Wang–Kamionkowski “work with a generic pseudoscalar-photon Chern–Simons coupling \(\partial_\mu\phi K^\mu\) (equivalently \(\phi F\tilde F\) up to a total divergence), not with the specific \(-\tfrac14(\alpha/M)\) normalization adopted here,” and that the present normalization is “the conventional ALP–photon Chern–Simons coupling.” Lue et al. indeed use a \(\phi F\tilde F\)–type coupling but with a different normalization and context (quintessence-like scalar) than the standard ALP convention in, e.g., axion-photon literature. As written, the text blurs this difference and could be read as suggesting the normalization is standard in the same sense as in axion-QED papers Lue et al. did not follow.  

**Fix:** Tighten the wording: explicitly acknowledge that Lue–Wang–Kamionkowski use a generic \(\phi F\tilde F\) coupling with their own normalization and that the \(-\tfrac14(\alpha/M)\) form is adopted here by analogy with standard axion electrodynamics (e.g. \(g_{\phi\gamma\gamma}\phi F\tilde F\)), not taken from Lue et al.; keep LWK as an early cosmological birefringence reference only.

---

## PAPER-PER-m1 — minor — Ashtekar & Singh bounce-density window

**Location:** §II.B Bounce equations, Eq. \eqref{eq:rhocrit} and paragraph giving \(\rhocrit \simeq 0.27\text{–}0.41\,\rho_{\rm Pl}\) attributed to Ashtekar & Singh.  

**Issue:** The text says Ashtekar & Singh “quote the canonical LQC value \(\rhocrit\simeq 0.41\rho_{\rm Pl}\)” and then extends this by substituting \(\gamma_{\rm SU(2)}\approx 0.274\) to get \(\rhocrit\simeq 0.27\rho_{\rm Pl}\), calling the 0.27–0.41 window “a scheme-dependent range.” Ashtekar & Singh’s review indeed discusses \(\rhocrit\approx 0.41\rho_{\rm Pl}\) for \(\gamma\approx 0.2375\), but they do not present the 0.27 value or that specific numerical window. The paper already partly admits 0.27 is an internal extrapolation but the sentence “the window used elsewhere in this paper should be read as a scheme-dependent range rather than as a published LQC range” could be clearer.  

**Fix:** Rephrase to: (i) explicitly say “Ashtekar & Singh give \(\rhocrit\simeq 0.41\rho_{\rm Pl}\) for \(\gamma=0.2375\); our 0.27 value and 0.27–0.41 window are internal extrapolations from that formula under alternate \(\gamma\) prescriptions and are not quoted in [Ashtekar & Singh]”; keep them clearly labeled as internal estimates.

---

## PAPER-PER-m2 — minor — Cai et al. matter-bounce \(\boldsymbol{f_{\rm NL}}\) attribution

**Location:** Abstract and §XIII (Surviving tests), statements “\(\fnl = -35/8\) is a property of the matter-bounce class” with citation to Cai et al. 2009.  

**Issue:** Cai et al. (arXiv:0903.0631) compute a local-type non-Gaussianity \(f_{\rm NL}=-35/8\) in a *specific* single-field matter-bounce setup under particular assumptions; it is not a universal prediction of “the matter-bounce class” in all bounce models. The paper qualifies this later (scalar-only \(w=0\) assumption), but the abstract and some summary sentences still read as if \(-35/8\) characterizes the entire class of matter bounces.  

**Fix:** In the abstract and any global summary, replace “a property of the matter-bounce class” with “a prediction of single-field scalar \(w=0\) matter-bounce models as in Cai et al. [Cai:2009fn]; not universal across all bounce scenarios,” aligning all mentions with the more careful wording already used later.

---

## PAPER-PER-n1 — nit — Minami & Komatsu / Eskilt & Komatsu measurement phrasing

**Location:** Abstract first paragraph; §III.1 and Discussion where “WMAP+Planck 0.342° ± 0.094°” and ACT DR6 birefringence are summarized.  

**Issue:** Minami & Komatsu 2020 first report a non-zero isotropic birefringence using Planck data with a template-cleaning method, and Eskilt & Komatsu 2022 improve this with WMAP+Planck for \(\beta = 0.342^\circ\pm 0.094^\circ\). The paper’s current wording is mostly correct but occasionally compresses this into “WMAP+Planck measurement first reported by Minami & Komatsu and refined by Eskilt & Komatsu,” which is historically a bit off: Minami & Komatsu is Planck-only; Eskilt & Komatsu is WMAP+Planck.  

**Fix:** Standardize the description to: “Planck-only detection by Minami & Komatsu; WMAP+Planck joint analysis by Eskilt & Komatsu yielding \(\beta=0.342^\circ\pm 0.094^\circ\)” everywhere, to avoid implying Minami & Komatsu used WMAP.  

---

[1] arXiv:1402.4854, “Quantum Einstein-Cartan gravity with the Holst term,” I.L. Shapiro & H. Takata, Class. Quant. Grav. 31 (2014) 185002.  
[2] The paper’s Step 4 in §II.A citing “Shapiro & Teixeira 2014, CQG 31:185002 (2014).”  
[3] CQG publisher/INSPIRE records for 31 (2014) 185002 show authors Shapiro & Takata, title as in [1].  
[4] A. Benedetti & S. Speziale, “Perturbative quantum gravity with the Immirzi parameter,” JHEP 06 (2011) 107, arXiv:1104.4028.  
[5] G. Date, R.K. Kaul, S. Sengupta, “Topological Interpretation of Barbero-Immirzi Parameter,” Phys. Rev. D 79 (2009) 044008, arXiv:0811.4496.  
 A. Lue, L. Wang, M. Kamionkowski, “Cosmological Signature of New Parity-Violating Interactions,” Phys. Rev. Lett. 83 (1999) 1506, arXiv:astro-ph/9812088.  
 Standard ALP–photon normalization e.g. in P. Sikivie, “Axion Cosmology,” Lect. Notes Phys. 741 (2008) 19, arXiv:astro-ph/0610440.  
 A. Ashtekar & P. Singh, “Loop Quantum Cosmology: A Status Report,” Class. Quant. Grav. 28 (2011) 213001, arXiv:1108.0893.  
 Y.-F. Cai et al., “Matter Bounce Cosmology,” JCAP 0907 (2009) 031, arXiv:0903.0631.  
 Y. Minami & E. Komatsu, “New Extraction of the Cosmic Birefringence from the Planck 2018 Polarization Data,” Phys. Rev. Lett. 125 (2020) 221301, arXiv:2011.11254.  
 K. Eskilt & E. Komatsu, “Improved constraints on cosmic birefringence from WMAP and Planck,” Phys. Rev. D 106 (2022) 063503, arXiv:2205.13962.
