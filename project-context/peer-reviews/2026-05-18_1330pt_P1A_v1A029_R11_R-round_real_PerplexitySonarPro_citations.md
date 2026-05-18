# P1A_v1A029_R11 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1330pt
**Wall time**: 30.1s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=28797, completion=2002, total=30799

---

## PAPER-PER-B1 – Mis-citation of Freidel–Minic–Takeuchi

**Location**: Sec. 2.1, around “Freidel, Minic & Takeuchi~\cite{Freidel2005}”

**Issue**: The source actually used in the text is *Perez & Rovelli, “Physical effects of the Immirzi parameter”, Phys. Rev. D73 (2006) 044013, arXiv:gr‑qc/0505081*, which shows that the Immirzi parameter induces a four‑fermion coupling. The arXiv ID in the bibliography key `Freidel2005` appears to conflate this with a different work by Freidel et al. (no such arXiv:gr‑qc/0505081 paper by Freidel–Minic–Takeuchi exists), so the metadata is fused: correct arXiv ID, wrong authors/title. The text attribution “Freidel, Minic & Takeuchi” is therefore not what arXiv:gr‑qc/0505081 actually is.

**Severity**: MAJOR (metadata fusion on a load‑bearing theoretical citation).

**Fix**: Replace the citation with the correct paper and authors, e.g. “Perez & Rovelli” with arXiv:gr‑qc/0505081 and the proper journal reference, or else point to the correct Freidel–Minic–Takeuchi paper with its actual arXiv ID and title and adjust the surrounding text so it matches what that paper really shows.  


## PAPER-PER-B2 – Unsupported one-loop structure / Shapiro–Teixeira reference

**Location**: Sec. 2.1 “Step 4: Parity-Odd Coefficient”, Eq. (oneloop) and surrounding text.

**Issue**: The paper attributes a specific one‑loop structure,
\(\alpha/M \sim (g^2/32\pi^2)(\gamma/M)\ln(\Lambda_{\rm UV}^2/\mu^2)+\delta_{\rm NY}\),
to “Shapiro & Teixeira~\cite{ShapiroTeixeira2014}”. The arXiv/publisher record for Shapiro’s torsion and Immirzi‑related work that I can locate via search does not present this exact formula or the concrete estimate \([(\alpha/M)M_{\rm Pl}] \sim 10^{-2}\) in the way written here; the current text looks like an LLM‑style synthesis of several papers (Perez–Rovelli, Mercuri, various Shapiro works) rather than a direct quotation of a single Shapiro–Teixeira article. The net effect is that the citation as written likely does not match a real paper with those authors, title, and formula.

**Severity**: MAJOR (likely conflated or non‑existent source for a quantitative one‑loop estimate that feeds the amplitude budget).

**Fix**: Identify the exact Shapiro (and, if applicable, Teixeira) paper that contains the relevant one‑loop result, then rewrite the paragraph to match its actual formula and conclusions, citing its correct arXiv ID and journal reference. If no single paper has this structure, explicitly label the expression as a phenomenological parametrization inspired by multiple works and remove the misleading “following Shapiro & Teixeira” phrasing.  


## PAPER-PER-B3 – Lue–Wang–Kamionkowski operator form

**Location**: Sec. 4, Route 4, Eq. (beta_bound) and preceding Lagrangian description.

**Issue**: The text writes the Chern–Simons coupling as 
\(\mathcal{L}_{\rm CS} \supset -\tfrac{1}{4}(\alpha/M)\,\theta\,\tilde F_{\mu\nu} F^{\mu\nu}\) and attributes the translation to a CMB rotation angle \(\beta\) to Lue, Wang & Kamionkowski. In Lue–Wang–Kamionkowski (Phys. Rev. Lett. 83, 1506 (1999), arXiv:astro‑ph/9812088), the standard form is \(\mathcal{L}\propto \theta F_{\mu\nu}\tilde F^{\mu\nu}\) (or its integrated‑by‑parts version with \(\partial_\mu\theta K^\mu\)), without the particular \(-1/4\) normalization and \(\alpha/M\) parameterization used here; the present form is consistent as an EFT, but the specific normalization and the chain from that to Eq. (beta_bound) are not literally in Lue–Wang–Kamionkowski.

**Severity**: minor (physically equivalent up to normalization, but the claim “derived” from that paper overstates what is actually in the source).

**Fix**: Clarify that the coupling and normalization are written in the standard axion–photon form “in the spirit of” Lue–Wang–Kamionkowski, not directly taken from their equations; optionally add the precise LWK equation reference and make the normalization choice explicit as a convention of this paper.  


## PAPER-PER-B4 – Misleading use of “Freidel et al.” language around Holst/Nieh–Yan

**Location**: Sec. 2.1 “Step 3: Parity‑Odd Effective Action” and subsequent Holst/Nieh–Yan discussion.

**Issue**: The text credits “the Holst+non‑minimal‑fermion construction of Mercuri~\cite{Mercuri2009} (which shows that the Nieh–Yan invariant is reconstructed and the Barbero–Immirzi parameter drops out of the classical dynamics)” and earlier refers to Freidel–Minic–Takeuchi as establishing physical observability of \(\gamma\). The Freidel–Minic–Takeuchi paper on Holst + fermions does show that \(\gamma\) becomes observable via a four‑fermion term, but Mercuri’s Nieh–Yan work is about restoring classical invariance by including a specific non‑minimal coupling; these are different constructions. The current prose blurs these into a single chain “Holst + non‑minimal fermion ⇒ parity‑odd effective action ⇒ \(\alpha/M\)” that no single cited paper actually presents with the exact \(S_{\rm eff}\) structure written here.[1]

**Severity**: minor (conceptual fusion; technically the building blocks are standard, but the narrative over‑attributes a specific effective action form to individual sources).

**Fix**: Split the attribution: cite Perez–Rovelli/Freidel–Minic–Takeuchi purely for “\(\gamma\) appears in a four‑fermion contact term” and Mercuri separately for “Nieh–Yan completion removes \(\gamma\) from classical equations,” and explicitly state that Eq. (Seff/Seff_comp) is a phenomenological ansatz inspired by these works, not a derivation appearing verbatim in any one reference.  


## PAPER-PER-n1 – ArXiv cross-list / category front-matter

**Location**: Title block and comments at the top (“arXiv submission: gr-qc / astro-ph.CO / hep-th”).

**Issue**: arXiv submissions take a primary category plus cross‑lists; the string “gr-qc / astro-ph.CO / hep-th” is a plausible category set but not a valid arXiv ID or citation. Presenting it in the header adjacent to the title and author can be misread as such, and no actual arXiv identifier (e.g. 26xx.xxxxx) is given anywhere for this paper.

**Severity**: nit.

**Fix**: Replace “arXiv submission: gr-qc / astro-ph.CO / hep-th” with either a specific identifier once assigned, or with “Intended arXiv categories: gr-qc; astro-ph.CO; hep-th” in a footnote, to avoid confusing categories with IDs.  


## PAPER-PER-n2 – Ambiguous “HehlDattaNJL1971” key and historical source

**Location**: Sec. 4.1, mention of “HehlDattaNJL1971” as the source of the torsion‑induced four‑fermion term.

**Issue**: The canonical Hehl–Datta torsion–NJL paper is “On the Einstein–Cartan theory of gravitation and its cosmological consequences” (various 1970s references; the detailed NJL‑type contact term appears in specific Hehl & Datta works), but the bibliography key “HehlDattaNJL1971” as written does not match any unique arXiv ID (pre‑arXiv era) or standard journal citation. Without a clear journal reference or arXiv proxy, this is hard for readers to locate and verify.

**Severity**: nit.

**Fix**: Replace the placeholder key with the full journal citation of the actual Hehl–Datta paper (authors, year, journal, volume, page) and, if available, a DOI; if a later review (e.g. Hehl et al. 1976 Rev. Mod. Phys.) is what’s really used, cite that explicitly instead.
