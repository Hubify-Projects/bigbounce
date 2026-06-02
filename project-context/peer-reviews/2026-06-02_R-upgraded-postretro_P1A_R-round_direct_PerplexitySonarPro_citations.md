# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-postretro
**Wall time**: 20.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=35376, completion=1341, total=36717, search_context_size=low, cost={'input_tokens_cost': 0.10613, 'output_tokens_cost': 0.02012, 'request_cost': 0.006, 'total_cost': 0.13224}

---

## PAPER-B1 — Mis-citation of Shapiro & Teixeira paper

**Section:** Version-history comments (around “PER-B1 (round 3, Shapiro-Teixeira ‘fictional’)”)  

**Issue:** The text states that “Shapiro & Teixeira, ‘Quantum Einstein-Cartan theory with the Holst term,’ CQG 31:185002 (2014)” exists at **arXiv:1402.4854**. arXiv:1402.4854 is actually *“Conformal transformations and Nordström’s scalar theory of gravity”* by Faria (and coauthors), not a Shapiro–Teixeira EC–Holst paper. The title, authors, journal, and arXiv ID are fused from different works.  

**Fix:** Correct the metadata to the actual Shapiro–Teixeira Holst/Einstein–Cartan paper (true arXiv ID, title, journal) and state explicitly that the earlier claim “arXiv:1402.4854, Shapiro & Teixeira” was an internal error now fixed.


## PAPER-M1 — Date–Kaul–Sengupta running of Immirzi parameter

**Section:** Route 3 (quantum running of Immirzi), Eq. (γ running) and surrounding text  

**Issue:** The RG ansatz  
\(\frac{d\gamma}{d\ln\mu} = \frac{1}{12\pi^2}(N_F^L-N_F^R)\gamma + \mathcal{O}(\gamma^2)\)  
is described as “schematically motivated by” Date–Kaul–Sengupta, but that paper does not present this specific β–function or this chiral-counting form. The current wording risks over‑attributing a concrete formula to them.  

**Fix:** Rephrase to attribute the explicit RG equation only to the present work (e.g. “we adopt the following EFT-motivated ansatz”) and cite Date–Kaul–Sengupta solely for the qualitative topological/chiral context, not as the source of Eq. (γ running).


## PAPER-M2 — Lue–Wang–Kamionkowski operator normalization

**Section:** Route 4 (parity-odd CMB coupling), first paragraph  

**Issue:** Lue, Wang & Kamionkowski indeed study a pseudoscalar–photon Chern–Simons term of \(\phi F\tilde F\) / \(\partial_\mu\phi K^\mu\) type, but they do **not** use the specific \(-\tfrac14(\alpha/M)\theta F\tilde F\) normalization adopted here. The text mostly says this, but at points still blurs “early cosmological-birefringence treatment” with “source of our exact coefficient”.  

**Fix:** Make the separation explicit wherever LWK is cited: state that LWK provide the cosmological-birefringence *framework* for a generic pseudoscalar–photon term, while the precise \(-\tfrac14(\alpha/M)\) normalization is chosen by the present work and not taken from LWK.


## PAPER-m1 — Eskilt & Komatsu vs Minami & Komatsu birefringence source

**Section:** Abstract and Secs. discussing \(\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ\)  

**Issue:** The WMAP+Planck birefringence detection at \(\beta \approx 0.34^\circ\) is originally from **Minami & Komatsu 2020**; Eskilt (2022) reanalyses Planck and related data with improved systematics. The phrase “Eskilt & Komatsu” as the sole source of the 0.342° ± 0.094° number is historically incomplete and may mislead about which paper first reported that specific measurement.  

**Fix:** Attribute the 0.342° ± 0.094° value jointly and precisely (e.g. “as measured by Minami & Komatsu and refined by Eskilt”) with separate citations, and specify which dataset/analysis each paper corresponds to (Planck-only vs WMAP+Planck, etc.) if those distinctions matter for later arguments.


## PAPER-m2 — Ashtekar & Singh critical density value

**Section:** LQC bounce density discussion (Eq. for \(\rho_{\rm crit}\) and 0.27–0.41 range)  

**Issue:** Ashtekar & Singh explicitly quote \(\rho_{\rm crit} \simeq 0.41\,\rho_{\rm Pl}\) for \(\gamma=0.2375\); the alternative 0.27 value derived by inserting \(\gamma=0.274\) is not in their paper. The text notes this, but in a way that still reads close to “Ashtekar & Singh quote 0.27–0.41”.  

**Fix:** Tighten the wording so that Ashtekar & Singh are cited only for the 0.41 value and the formula, and the 0.27 value is clearly labeled as an internal extrapolation using their formula with a different \(\gamma\), not as part of their published numerical range.


## PAPER-n1 — “Quantum Einstein–Cartan theory with the Holst term” title traceability

**Section:** Version-history comments and any reference list entry that uses this exact title  

**Issue:** A paper titled exactly “Quantum Einstein-Cartan theory with the Holst term” in CQG 31:185002 (2014) by Shapiro & Teixeira does not appear in arXiv/ADS; given the wrong arXiv ID already identified, the combination of this precise title, journal, year, pages, and authors is not currently verifiable as a single real article and likely fuses metadata from multiple sources.  

**Fix:** Re-verify the existence of the CQG article via publisher/ADS; if the exact title/volume/page combination cannot be confirmed, correct the reference to the real Shapiro–Teixeira EC–Holst paper (or remove it), and note in the changelog that the earlier CQG 31:185002 metadata was an internal placeholder that has been corrected.
