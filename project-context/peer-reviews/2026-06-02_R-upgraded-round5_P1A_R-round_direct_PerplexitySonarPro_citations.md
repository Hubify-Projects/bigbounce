# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round5
**Wall time**: 19.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=35532, completion=2195, total=37727, search_context_size=low, cost={'input_tokens_cost': 0.1066, 'output_tokens_cost': 0.03293, 'request_cost': 0.006, 'total_cost': 0.14552}

---

## PAPER-PER-B1 — BLOCKER — Shapiro & Teixeira 2014 mis-cited and misused

**Location:** Around v1A.0.39 changelog and Sec. II.B.3, Eq. (11) / text around Eq. \eqref{eq:oneloop}

**Issue:** The paper claims “Shapiro & Teixeira 2014, ‘Quantum Einstein-Cartan theory with the Holst term,’ CQG 31:185002 (2014)” with arXiv:1402.4854 and uses them as a source for a fermion‑induced parity‑odd one‑loop operator and “one‑loop estimate” of \(\alpha/M\).[ ] However, arXiv:1402.4854 is **“Quantum Einstein-Cartan theory”** (no Holst term in the title) by I. L. Shapiro & P. M. Teixeira, CQG 31 (2014) 185002, and it does not give the explicit \((\alpha/M)\) chiral Chern–Simons–type operator or the numerical estimate claimed.[ ] The bibliographic metadata is partly fabricated (“with the Holst term”), and the text implies a much more concrete result than the paper actually contains.

**Fix:** Correct the citation metadata to the actual title and clearly separate what Shapiro–Teixeira actually compute (renormalization / effective action structure in Einstein–Cartan) from the **phenomenological** form and size of Eq. \eqref{eq:oneloop}, which should be explicitly labeled as an EFT ansatz not derived in that work. Remove the phrase “with the Holst term” and the “one-loop estimate” language unless backed by a precise equation from the cited paper.


## PAPER-PER-M1 — MAJOR — Benedetti & Speziale attribution still off

**Location:** Sec. IV.C, Eq. \eqref{eq:gamma_running} and surrounding text (“Benedetti & Speziale… find a β-function whose sign depends on |γ|…”)

**Issue:** The paper cites Benedetti & Speziale 2011 for a fermion‑induced running of the Immirzi parameter with sign depending on \(|\gamma|\) and then introduces a schematic RG equation \(d\gamma/d\ln\mu = (1/12\pi^2)(N_F^L-N_F^R)\gamma + \mathcal{O}(\gamma^2)\) as “schematically motivated” by Date–Kaul–Sengupta, while using Benedetti–Speziale as the actual computation.[ ] In reality, Benedetti & Speziale (arXiv:1104.4028, “Perturbative quantum gravity with the Immirzi parameter”) compute a β‑function for \(\gamma\) in a Euclidean, parity‑even gravity plus fermions setting and do **not** give the chiral‑asymmetry‑driven SM‑like form of Eq. \eqref{eq:gamma_running}, nor do they frame it as proportional to \(N_F^L-N_F^R\).[ ] The current wording still reads as if the functional dependence and magnitude are grounded in that paper.

**Fix:** Reword this section to: (i) state precisely what Benedetti & Speziale actually show (existence and qualitative behavior of the \(\gamma\) β‑function in a specific truncation), (ii) make clear that Eq. \eqref{eq:gamma_running} is a **toy EFT parametrization** not found in either Benedetti–Speziale or Date–Kaul–Sengupta, and (iii) remove any suggestion that the \(1/(12\pi^2)(N_F^L-N_F^R)\gamma\) structure or its numerical size is reported by those references.


## PAPER-PER-M2 — MAJOR — Freidel–Minic–Takeuchi and Mercuri/Capozziello over-claimed on specific operators

**Location:** Sec. II.A, Eq. \eqref{eq:ECH}; Sec. II.B.3, discussion of Eq. \eqref{eq:Seff}–\eqref{eq:Seff_comp} and Eq. \eqref{eq:oneloop_parity_odd}

**Issue:** The text attributes a concrete parity‑odd effective action \(S_{\rm eff} = (\alpha/M)\int e\wedge e\wedge\mathcal{F}\) and a one‑loop \(\alpha/M\sim (g^2/32\pi^2)(\gamma/M)\ln(\Lambda_{\rm UV}^2/\mu^2)+\delta_{\rm NY}\) to “Freidel, Minic & Takeuchi” and “Mercuri / Mercuri & Capozziello” as if these works give that operator and coefficient in this form.[ ] In fact, Freidel–Minic–Takeuchi (arXiv:0507253) show that the Immirzi parameter becomes physical in the presence of non‑minimal fermions and discuss induced four‑fermion interactions, but they do **not** derive the ALP‑like \((\alpha/M)\,\theta F\tilde F\) operator or a numerical \(\alpha/M\) for photons.[ ] Mercuri (e.g. arXiv:0903.2270) and Mercuri–Capozziello (Phys. Rev. D78, 024016) analyze the Holst/Nieh–Yan structure and chiral anomalies, but again do not present the exact Eq. \eqref{eq:oneloop_parity_odd} form with that specific coefficient and “\(\sim 10^{-2}\)” estimate.[ ]

**Fix:** Tighten the attribution: explicitly say that these papers motivate *the presence* of parity‑odd Nieh–Yan–type structures and show that \(\gamma\) can enter fermionic couplings, but that the concrete form and numerical value of Eqs. \eqref{eq:Seff}, \eqref{eq:Seff_comp}, and \eqref{eq:oneloop_parity_odd} are introduced here as a **phenomenological EFT ansatz**. Remove or soften any phrasing that reads as “following [X], the one-loop estimate is …” unless you can point to a specific equation in the cited work.


## PAPER-PER-M3 — MAJOR — Lue–Wang–Kamionkowski normalization still overstated

**Location:** Sec. IV.D, Route 4, around “An early cosmological birefringence treatment is Lue, Wang & Kamionkowski…”

**Issue:** The paper has improved the wording, but it still implicitly suggests that Lue–Wang–Kamionkowski (Phys. Rev. Lett. 83, 1506 (1999), arXiv:astro-ph/9812088) support the **same normalization** as used here for the ALP–photon operator \(-\tfrac14(\alpha/M)\theta F\tilde F\).[ ] In reality, LWK work with a generic \(\partial_\mu\phi\,K^\mu\) Chern–Simons–like term and derive rotation formulas qualitatively similar to Eq. \eqref{eq:beta_bound}, but they do not define or constrain “\(\alpha/M\sim 10^{-21}\,\mathrm{GeV}^{-1}\)” nor fix the specific numerical normalization used in the paper.[ ]

**Fix:** Further separate the roles: say explicitly that LWK are cited only as an *early example of the cosmological consequences* of a generic \(\partial\phi\,K^\mu\) coupling, and that the coefficient normalization and numerical bound \(\alpha/M\sim 10^{-21}\,\mathrm{GeV}^{-1}\) are obtained by **this work’s own mapping** to WMAP+Planck \(\beta\), not from LWK. Avoid any language that could be read as “we take their normalization.”


## PAPER-PER-m1 — minor — Mistitled Shapiro–Teixeira reference in changelog

**Location:** Comment block in header, “PER-B1 (round 3, Shapiro-Teixeira ‘fictional’)… ‘Quantum Einstein-Cartan theory with the Holst term,’ CQG 31:185002 (2014).”

**Issue:** As in BLOCKER B1, the internal log entry uses a non‑existent title “Quantum Einstein-Cartan theory with the Holst term” for arXiv:1402.4854, whose actual title is just “Quantum Einstein-Cartan theory.”[ ] While this is in a comment rather than the main text, it documents a fictitious title and could confuse future readers or referees checking the history.

**Fix:** Update the log text to the correct title, or at least note explicitly that the phrase “with the Holst term” is *not* in the original title and was an internal shorthand.


## PAPER-PER-n1 — nit — Slightly misleading description of Date–Kaul–Sengupta

**Location:** Sec. IV.C, paragraph introducing Date–Kaul–Sengupta and Eq. \eqref{eq:gamma_running}

**Issue:** The text say DKS “analyzed the Holst term coupled to fermions and the Nieh–Yan invariant in the chiral-matter setting” in a way that suggests a **direct quantitative** basis for the running used, but Date–Kaul–Sengupta (Phys. Rev. D79, 044008 (2009), arXiv:0811.4496) focus on the topological interpretation of \(\gamma\) and do not compute an RG flow or chiral‑asymmetry proportional β‑function of the form used.[ ]

**Fix:** Add one clarifying sentence that DKS are used only to motivate the *possibility* of \(\gamma\) running in chiral settings and the Nieh–Yan topological structure, and explicitly state that they do **not** provide the β‑function of Eq. \eqref{eq:gamma_running}.
