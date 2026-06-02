# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-01_R-multi-round6
**Wall time**: 15.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34329, completion=1690, total=36019, search_context_size=low, cost={'input_tokens_cost': 0.10299, 'output_tokens_cost': 0.02535, 'request_cost': 0.006, 'total_cost': 0.13434}

---

## PAPER-PER-B1 — Shapiro & Teixeira reference formatting / attribution

**Issue (MAJOR):**  
In the comments around v1A.0.37–.39 the paper cites “Shapiro & Teixeira, *Quantum Einstein-Cartan theory with the Holst term*, CQG 31:185002 (2014), arXiv:1402.4854” as validation against a prior reviewer’s “fictional” claim. The actual paper at arXiv:1402.4854 is by **Ilya L. Shapiro and Paulo M. Teixeira**, titled *“Quantum Einstein–Cartan theory with the Holst term”*, published in **Class. Quant. Grav. 31 (2014) 185002**; the existence, title, authors and venue are all correct, but in the LaTeX body the only explicit Shapiro–Teixeira reference is `\cite{ShapiroTeixeira2014}` without the arXiv ID or journal details shown in-text, so the “bbl entry correct” claim can only be checked if the `.bbl` is available, which it is not here.  

**Fix:**  
Explicitly ensure the BibTeX entry for Shapiro–Teixeira uses `arXiv:1402.4854`, the exact title, and “Class.Quant.Grav. 31 (2014) 185002”, and consider adding “(CQG 31:185002 (2014), arXiv:1402.4854)” at the first in-text mention to make the previously disputed provenance auditable from the TeX alone.

---

## PAPER-PER-M1 — Eskilt & Komatsu 2022 and Diego-Palazuelos & Komatsu 2025 birefringence claims

**Issue (minor):**  
The abstract and several sections describe “Eskilt & Komatsu 2022” as the WMAP+Planck joint cosmological-birefringence detection with \(\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ\) at \(\sim3.6\sigma\), and “Diego‑Palazuelos & Komatsu 2025” as an independent ACT DR6 follow-up with \(\beta = 0.215^\circ \pm 0.074^\circ\) at \(\sim2.9\sigma\). These are consistent with the actual works (Eskilt & Komatsu 2022, arXiv:2207.XXX, Planck+WMAP birefringence; Diego‑Palazuelos & Komatsu 2025, ACT DR6 birefringence), but no arXiv IDs or journal venues are given, and the text leans heavily on the numerical values as if they were already in final journal form.  

**Fix:**  
Add arXiv identifiers and current publication status to the citations (e.g. “Eskilt & Komatsu (2022), arXiv:22xx.xxxx” and “Diego‑Palazuelos & Komatsu (2025), arXiv:25xx.xxxx, in preparation/submitted” as appropriate), and clarify that the quoted \(\beta\) values are taken from those specific analyses and may evolve with future reanalyses.

---

## PAPER-PER-M2 — Date–Kaul–Sengupta running of \(\gamma\) (Eq. \ref{eq:gamma_running})

**Issue (minor):**  
The text states that Date, Kaul & Sengupta “analyzed the Holst term coupled to fermions and the Nieh–Yan invariant … and do not present the explicit RG equation used below,” and then presents Eq. (γ running) as “schematically motivated” by them. This is a fair disclaimer, but the numerical coefficient \(1/(12\pi^2)\) and dependence on \((N_F^L - N_F^R)\) are not directly traceable to any standard published RG calculation for \(\gamma\); they look like a typical chiral one‑loop estimate rather than something Date–Kaul–Sengupta “schematically motivate.”  

**Fix:**  
Make the provenance cleaner: explicitly label Eq. \ref{eq:gamma_running} as a **toy EFT ansatz** inspired by generic chiral one‑loop RG structures, and cite Date–Kaul–Sengupta only for the *topological interpretation* of \(\gamma\), not as providing even a schematic form of this specific beta function.

---

## PAPER-PER-m1 — Lue–Wang–Kamionkowski birefringence normalization

**Issue (nit):**  
The text correctly notes that Lue, Wang & Kamionkowski work with a generic \(\partial_\mu\phi\,K^\mu\) (or \(\phi F\tilde F\)) coupling and **do not** use the specific \(-\tfrac14 (\alpha/M)\theta F\tilde F\) normalization adopted here, and it says “we adopt this normalization and use LWK as an early example.” This is accurate, but the phrase “an early cosmological-birefringence treatment of this mechanism” can be read as implying LWK considered the same parameterization, which they did not.  

**Fix:**  
Slightly tighten the wording to “an early cosmological-birefringence treatment of *pseudoscalar–photon Chern–Simons couplings*” and explicitly state that the \(-\tfrac14(\alpha/M)\) normalization is purely conventional and not taken from LWK.

---

## PAPER-PER-m2 — Ashtekar & Singh critical density \(\rho_{\rm crit}\) usage

**Issue (nit):**  
The paper now correctly states Ashtekar & Singh quote \(\rho_{\rm crit} \simeq 0.41\,\rho_{\rm Pl}\) at \(\gamma=0.2375\) and clarifies that \(\rho_{\rm crit} \simeq 0.27\,\rho_{\rm Pl}\) obtained by inserting \(\gamma_{\rm SU(2)}\approx0.274\) into the LQC formula is an *internal extrapolation* not a published value. That’s accurate, but the abstract and Table \ref{tab:barriers} still use the range “0.27–0.41 \(\rho_{\rm Pl}\)” without always repeating that only the upper end is directly from Ashtekar–Singh.  

**Fix:**  
Wherever the range “0.27–0.41 \(\rho_{\rm Pl}\)” appears outside the detailed discussion, add a brief parenthetical “(0.41 from Ashtekar & Singh’s canonical LQC value, 0.27 from our internal extrapolation using \(\gamma_{\rm SU(2)}\))” to prevent any misreading that both bounds are literature values.

---

## PAPER-PER-n1 — “Golden2026Px” companion papers marked “in preparation”

**Issue (minor):**  
The text repeatedly cites Golden2026P1b/P2/P3/P4 as “in preparation” companions, plus internal tables and chain inventories, but provides no arXiv IDs or journal venues. The current draft explicitly acknowledges that these are internal and not yet externally citable, which is honest, but it still leans on them for quantitative numbers (e.g., MCMC posterior values, real-KDE PTA spectral index, SPHEREx Fisher forecast).  

**Fix:**  
Maintain the current explicit caveats, and add a one‑sentence statement near the first occurrence of any Golden2026Px citation that all such references are to **unpublished internal notes**; recommend that external readers treat any numerical values sourced only from those notes as provisional until corresponding arXiv entries exist.
