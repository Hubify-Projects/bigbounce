# P2_v1729_R2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_0230pt
**Wall time**: 17.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=31086, completion=1298, total=32384

---

## PAPER-CIT-1 — CaiBrandenberger:2014 now corrected (no remaining fused-ID)

**Issue.** The manuscript states that Cai et al. (2009) is arXiv:0903.0631 (“Non-Gaussianity in a Matter Bounce”) and that a previous fused-ID problem with “CaiBrandenberger:2014” (wrongly pointing to arXiv:1404.6968) has been removed. The current text never again assigns the 2014 cosmology paper a wrong arXiv ID, and the only explicit Cai et al. reference with an ID is 0903.0631, which is correct. [2]

**Fix.** No change needed here; just ensure the bibliography entry for “CaiBrandenberger:2014” either omits an arXiv ID or uses the correct one (if present in the .bib) and that 1404.6968 never appears for this cosmology paper.

---

## PAPER-CIT-2 — Wands & Finelli citations (titles/IDs)

**Issue.** The introduction cites Wands (1998) and Finelli & Brandenberger (2001) for scale-invariant spectra in matter-dominated contraction. The canonical papers are G. Wands, “Duality invariance of cosmological perturbation spectra” (arXiv:gr-qc/9809062), and F. Finelli & R. Brandenberger, “On the generation of a scale-invariant spectrum of adiabatic fluctuations in cosmological models with a contracting phase” (arXiv:hep-th/0112249). The LaTeX uses keys Wands:1998yp and Finelli:2001sr, which match the common arXiv identifiers and topics, so there is no fused-ID or title/author mismatch. [2]

**Fix.** No correction required, but in the .bib make sure Wands:1998yp points to gr-qc/9809062 with the correct title and Finelli:2001sr to hep-th/0112249; do not mix these IDs with unrelated astro-ph entries like astro-ph/9812216. [1][2]

---

## PAPER-CIT-3 — Cai et al. (2009) metadata

**Issue.** The paper heavily leans on Cai et al. (2009) for the matter-bounce bispectrum and \(\fnl=-35/8\). The arXiv entry arXiv:0903.0631 is indeed “Non-Gaussianity in a Matter Bounce” by Yi-Fu Cai, Wei Xue, Robert Brandenberger, and Xinmin Zhang, exactly matching the topic and claims used (non-Gaussianity in a matter-dominated bounce, computation of the bispectrum). There is no sign of title/ID fusion. [2]

**Fix.** None needed; just ensure the .bib for Cai:2009fn uses arXiv:0903.0631 and the correct title “Non-Gaussianity in a Matter Bounce” or its journal version.

---

## PAPER-CIT-4 — Maldacena consistency relation

**Issue.** The text attributes the single-field consistency relation \(\fnl^{\rm local}\approx (5/12)(1-n_s)\) to Maldacena (2002). The standard reference is J. Maldacena, “Non-Gaussian features of primordial fluctuations in single field inflationary models,” arXiv:astro-ph/0210603, which does contain this result. The key Maldacena:2002vr is the usual arXiv tagging; no sign of an ID or title mismatch. [2]

**Fix.** No change required; confirm in the .bib that Maldacena:2002vr points to astro-ph/0210603 with the correct title and journal citation.

---

## PAPER-CIT-5 — Einstein–Cartan–Holst references (Mercuri, Freidel et al.)

**Issue.** The text cites Mercuri (2006) and Freidel et al. (2005) for the statement that the Holst term becomes topological and the Barbero–Immirzi parameter drops out for torsionless scalar matter. The actual arXiv papers (e.g., S. Mercuri, “Fermions in Ashtekar–Barbero connections formalism for arbitrary values of the Immirzi parameter,” gr-qc/0610026; L. Freidel, D. Minic, T. Takeuchi, “Quantum gravity, torsion, parity violation and all that,” hep-th/0507253) do discuss torsion, Holst, and fermions, consistent with how they are used here. There is no evidence of mismatched titles or IDs in these citations. [2]

**Fix.** Ensure the Mercuri2006 and Freidel2005 entries in the .bib point to the correct arXiv IDs above (or to their journal versions) and that no unrelated arXiv numbers are attached; otherwise no change.

---

## PAPER-CIT-6 — Suyama–Yamaguchi inequality reframing

**Issue.** The paper states that the matter bounce obeys the Suyama–Yamaguchi inequality \(\tau_{\rm NL}\ge (6\fnl/5)^2\) and reframes it as an inequality rather than exact saturation, which is the correct usage of Suyama & Yamaguchi, “Non-Gaussianity in the modulated reheating scenario,” arXiv:0709.2545, and related work. That paper indeed derives the inequality, and saturation requires a single-source local case, which the manuscript explicitly does not claim. No title/ID mismatch is apparent. [2]

**Fix.** No fix needed; just confirm the Suyama–Yamaguchi .bib entry uses the correct arXiv:0709.2545 and title, and keep the “inequality, not saturation” phrasing as is.
