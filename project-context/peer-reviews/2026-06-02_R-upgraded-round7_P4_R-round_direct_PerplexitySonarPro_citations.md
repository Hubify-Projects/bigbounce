# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round7
**Wall time**: 20.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=100567, completion=1683, total=102250, search_context_size=low, cost={'input_tokens_cost': 0.3017, 'output_tokens_cost': 0.02525, 'request_cost': 0.006, 'total_cost': 0.33295}

---

## PAPER-PER-B1 (BLOCKER) – Mis-cited Motloch et al. paper

**Location:** §7.3 “Motloch & Pen (2021)”, around  
> “Motloch et al.~\cite{Motloch:2021} report a marginal ($\sim\!2.7\sigmaunit$) correlation …”

**Issue:**  
Citation `\cite{Motloch:2021}` is described as “Motloch et al.” and a “$\sim\!2.7\sigma$ correlation”, but arXiv:2003.04800 / Nature Astronomy 5, 283 (2021) is authored by *Yu, Motloch, Pen & Xie* (“An observed correlation between galaxy spins and initial conditions”) and reports a higher significance (~4σ) signal, not a 2.7σ result. The bib entry in the paper also lists “P. Motloch, H.-R. Yu, U.-L. Pen, and Y. Xie”, but the prose calls it “Motloch et al.” and mischaracterises the result and its context.

**Fix:**  
Correct the description to match the actual paper and its authorship, e.g. “Yu et al. (2020/2021) / Motloch et al. (Nature Astronomy 5, 283)” with accurate significance and context, or if you intend a different 2.7σ result, update the arXiv ID and bib metadata to that work. Ensure title, authors, σ-value and arXiv ID are consistent with ADS/arXiv.

---

## PAPER-PER-M1 (MAJOR) – SpArcFiRe numbers and DR9 overlap not clearly sourced

**Location:** §7.3 “SpArcFiRe”, esp. paragraphs:

> “The SpArcFiRe algorithm~\cite{Davis:2014} … producing catalogs of $\sim\!140{,}000$ galaxies.”  
> “The published SpArcFiRe DR9-overlap catalog reports CW/CCW counts consistent with $50/50$ to within $\sim\!0.3\%$ at its $\sim\!1.4\!\times\!10^{5}$-galaxy footprint (…Table 3 plus the public Hayes-Davis DR9 update)…”

**Issue:**  
Davis & Hayes (2014, ApJ 790, 87) describe the algorithm and a DR7-scale sample; there is no refereed “DR9-overlap” paper with a 1.4×10⁵ sample and “0.3%” parity figure. That DR9 update appears to be an unpublished catalog / web release; in its current wording it reads like a refereed result. The exact “1.4×10⁵” and “0.3%” numbers are not clearly traceable to a citable paper.

**Fix:**  
Explicitly identify the DR9 catalog as an unpublished or online data release (with author/URL), and qualify the 1.4×10⁵ and 0.3% figures as coming from that catalog, not from Davis & Hayes 2014. Alternatively, remove the quantitative DR9 overlap claim or replace it with numbers that you can tie directly to a formal publication.

---

## PAPER-PER-M2 (MAJOR) – Conflicting / opaque use of Philcox–Hou–Cabass parity-violation references

**Location:** §7.3 “Motloch & Pen (2021)” and §7.4 “Motloch & Pen / parity‑odd sectors” and the bibliography entries:
- `\bibitem{Philcox:2023}`
- `\bibitem{Hou:2023}`
- `\bibitem{Cabass:2023}`

**Issue:**  
You attribute to Philcox (2023) a “$\sim\!2.9\sigma$ (blind)” parity-odd 4PCF detection and to Hou et al. “7.1σ (CMASS) / 3.1σ (LOWZ)”, and then state that Cabass–Ivanov–Philcox map this 4PCF amplitude to an EFT parameter \(g_*\). These numbers and attributions are easy to muddle because Philcox has multiple parity-odd 4PCF papers (BOSS, CMASS-only, blind/bias-corrected) and Cabass et al. have several EFT-of-LSS parity papers. Without explicit titles and arXiv IDs here, it’s not possible for a reader to confirm that the specific σ-values correspond to the specific papers you cite.

**Fix:**  
For each of Philcox, Hou and Cabass references, add precise titles and check that the σ-values you quote match the specific paper (BOSS DR12 vs CMASS-only vs LOWZ etc.). If any σ-value actually comes from a different paper (e.g. a follow-up by Philcox alone), either move it to the correct citation or drop it.

---

## PAPER-PER-m3 (minor) – “Motloch et al.” / “Yu et al.” naming inconsistency

**Location:** §7.3 “Motloch & Pen (2021)” and the corresponding bibliography entry for `\bibitem{Motloch:2021}`.

**Issue:**  
The bib entry is correctly “P. Motloch, H.-R. Yu, U.-L. Pen, and Y. Xie”, but in the prose you refer to “Motloch et al.” and elsewhere to “Yu, Motloch, Pen & Xie”. That’s stylistically inconsistent, and also potentially confusing given there is a separate Yu et al. 2020 PRL (arXiv:1904.01029) on the same topic.

**Fix:**  
Pick one consistent main-citation name for the Nature Astronomy paper (e.g. “Yu et al. (2021)” or “Yu, Motloch, Pen & Xie”) and use it everywhere; reserve “Motloch & Pen” for the 2.7σ correlation if that’s actually a different paper, with its own bib entry.

---

## PAPER-PER-m4 (minor) – Ambiguous pointer to “Hayes-Davis DR9 update”

**Location:** §7.3 “SpArcFiRe”, sentence:

> “…the public Hayes-Davis DR9 update…”

**Issue:**  
“Hayes-Davis DR9 update” isn’t a standard bibliographic object: no arXiv ID, journal, or year is given. For a forensic reader, this looks like fused metadata – author names from the 2014 ApJ paper combined with an unspecified later catalog.

**Fix:**  
Either (a) add a proper reference entry with year and a description (e.g. “Hayes & Davis, unpublished DR9 catalog, URL …”), or (b) remove the mention and only use numbers that can be tied to Davis & Hayes (2014) or another citable source.

---

## PAPER-PER-n1 (nit) – Slightly misleading “An anticipated Iye & Yagi forthcoming” wording

**Location:** §7.1 “Shamir (2012, 2020, 2022)”:

> “An anticipated Iye & Yagi forthcoming HSC-WIDE Survey spin-parity analysis (Iye & Yagi, in prep.) is expected to extend the same group’s spin-parity program…”

**Issue:**  
“Iye & Yagi, in prep.” has no arXiv ID or journal; using “anticipated” plus “is expected” reads speculative and may be interpreted as citing non-existent literature.

**Fix:**  
Either drop this sentence entirely, or rephrase to something like “Iye has indicated plans for an HSC-WIDE spin-parity analysis (private communication); we do not rely on any result from that work here.” and remove `(Iye & Yagi, in prep.)` from the bibliography.
