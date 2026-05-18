# P1A_v1A031_R14 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1500pt
**Wall time**: 26.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=28739, completion=1685, total=30424

---

## PAPER-CIT-B1 — ABCK1998 citation mismatch (Immirzi value)

**Issue (MAJOR, load-bearing but not math):**  
The text cites “ABCK1998” as giving \(\gamma_{\rm ABCK} \approx 0.274\), and lumps this with “DLM full SU(2) counting” giving \(\gamma_{\rm DLM}\approx 0.2375\).[1] In the actual LQG literature, the original ABCK (Ashtekar–Baez–Corichi–Krasnov) SU(2) black-hole entropy calculation gives \(\gamma \sim 0.2375\), while the later Domagala–Lewandowski/Meissner refinements adjust the value slightly but do not swap the two; there is no standard source with ABCK at 0.274 and DLM at 0.2375 as distinct benchmark values.[2] The current mapping looks like a fused attribution of numbers and labels.

**Fix (1–2 sentences):**  
Re-check the primary ABCK and Domagala–Lewandowski/Meissner papers and correct the assignment so that the numerical values and acronyms match the actual results (or collapse to a single “\(\gamma\sim 0.24\)” reference if you do not want to track detailed scheme differences). Add explicit arXiv IDs and journal references for ABCK and DLM to make the provenance of the quoted \(\gamma\) values auditable.

---

## PAPER-CIT-B2 — MercuriCapozziello2008 one-loop coefficient over-interpretation

**Issue (minor, conceptual tightness):**  
The narrative links the parity-odd suppression factor and the \(\alpha_{\rm em}/(4\pi)\) estimate directly to “Mercuri & Capozziello 2008 one-loop coefficient” in several places, treating that paper as a clean quantitative source for the specific size of the parity-odd Holst/Nieh–Yan coefficient used later (e.g. in \(\alpha/M \sim 10^{-21}\,\mathrm{GeV}^{-1}\)).[3] Mercuri & Capozziello (Class. Quantum Grav. 27 (2010) 215015) discuss parity-violating terms in torsion gravity and the role of regularization choices, but they do not provide a universal, model-independent numerical matching of \(\alpha_{\rm em}/(4\pi)\) to the IR \(\alpha/M\) used here; the text overstates how tightly that paper fixes the prefactor.[3]

**Fix (1–2 sentences):**  
Rephrase these citations to say that Mercuri & Capozziello motivate the *existence* and generic loop suppression of parity-odd torsion terms, but that the specific \(\alpha/M\) magnitude adopted here is a phenomenological choice rather than a number directly computed there. Make explicit that different regularization schemes or UV completions could change the finite part of the coefficient.

---

## PAPER-CIT-B3 — Lue–Wang–Kamionkowski operator form and provenance

**Issue (nit, already partially corrected but still loose):**  
The text notes that an earlier draft used \((\alpha/M)\,\partial_\mu\theta\,\tilde F^{\mu\nu}F_{\mu\nu}\) with an uncontracted index and that this was corrected to the integrated-by-parts equivalent of the standard Chern–Simons coupling from Lue, Wang & Kamionkowski.[4] However, the current wording still suggests that Lue et al. *derive* exactly the ALP–photon operator normalization used later (\(\alpha/M\sim 10^{-21}\,\mathrm{GeV}^{-1}\)), whereas in their 1999 paper they work with a generic pseudo-scalar coupling and discuss CMB rotation qualitatively, without fixing \(\alpha/M\) to the specific phenomenological value employed here.[4]

**Fix (1–2 sentences):**  
Clarify that Lue–Wang–Kamionkowski provide the *formalism* connecting a generic Chern–Simons coupling to CMB polarization rotation, but not the particular \(\alpha/M\) value; emphasize that \(\alpha/M\sim 10^{-21}\,\mathrm{GeV}^{-1}\) is chosen by matching to current birefringence data, not taken from that paper.

---

## PAPER-CIT-B4 — Cai:2009fn matter-bounce \(\fnl\) ownership

**Issue (nit, attribution nuance):**  
The paper repeatedly treats \(\fnl=-35/8\) as “the matter-bounce class” prediction citing Cai et al. 2009.[5] In the actual Cai et al. work, that value arises in a specific single-field, matter-dominated contracting model with defined assumptions about initial conditions and interactions; they do not claim it as a universal prediction for “any matter-bounce host,” and later literature explores variants with different \(\fnl\).[5]

**Fix (1–2 sentences):**  
Tighten the language wherever \(\fnl=-35/8\) is called a “class-level” prediction: explicitly say it is the prediction of the Cai et al. single-field matter-bounce model (under the assumptions spelled out there), and that other bounce implementations can give different non-Gaussianity signatures.

---

## PAPER-CIT-B5 — Shamir galaxy spin results and refutations

**Issue (minor, external-paper claims):**  
The manuscript asserts that Shamir reported “\(\sim1\)–\(3\%\) CW excesses” and that these have been refuted at high significance by Patel & Desmond and Philcox.[6] Shamir’s arXiv papers indeed quote a few-percent-level asymmetry, but the exact magnitude and sky dependence vary between their 2022 and 2024 analyses; similarly, Patel & Desmond (and Philcox) critique methods and do not phrase their conclusions as a single definitive “refutation of 3%” number.[6] Wording here compresses multiple results into a single precise-sounding statement that no single cited paper actually makes.

**Fix (1–2 sentences):**  
Rephrase to: “Shamir reports order‑percent CW/CCW asymmetries in several analyses, while Patel & Desmond and Philcox find results consistent with no dipole when re-analyzing comparable imaging data; our ViT-Small classifier likewise finds no significant dipole.” This keeps the citation accurate without over-quoting a specific 3% figure or overstating the refuters’ language.

---

## PAPER-CIT-B6 — LiteBIRD sensitivity and \(\sigma(\beta)\) claim

**Issue (minor, forecast provenance):**  
The text quotes LiteBIRD as achieving “\(\sigma(\beta)\approx 0.03^\circ\)” in the early 2030s, treating this as a concrete forecast used in several places.[7] LiteBIRD’s official design papers and white papers indeed discuss cosmic birefringence sensitivity, but the exact \(\sigma(\beta)\) depends on assumptions about foregrounds, systematics, and analysis methods; current public documents typically give ranges or scenario-dependent numbers rather than a single, unconditional 0.03° forecast.[7]

**Fix (1–2 sentences):**  
Qualify this as an indicative forecast and cite an explicit LiteBIRD design/forecast paper, e.g. “Representative LiteBIRD forecasts suggest \(\sigma(\beta)\) of order \(0.03^\circ\) under optimistic assumptions about foregrounds and systematics,” and include the precise arXiv reference supporting that order-of-magnitude estimate.
