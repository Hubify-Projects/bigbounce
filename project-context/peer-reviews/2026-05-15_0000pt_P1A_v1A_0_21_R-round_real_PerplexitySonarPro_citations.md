# P1A_v1A_0_21 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_0000pt
**Wall time**: 28.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=24774, completion=1733, total=26507

---

## PAPER-PER-B1 — Mis-cited Freidel–Minic–Takeuchi paper (BLOCKER)

**Location:** Sec. 2.1 “Einstein-Cartan-Holst Action”, around “Freidel, Minic & Takeuchi” and throughout where that citation is used.

**Issue:** The Holst/Barbero–Immirzi–fermion physics being referenced is the well-known paper “Holst action with the Immirzi parameter and fermions” (Freidel, Minic, Takeuchi, arXiv:hep-th/0507253), not “A group field theory for 3d quantum gravity coupled to a scalar field” (Freidel, Oriti, Ryan, arXiv:gr‑qc/0506067). The current arXiv identifier in the .bib (implicitly gr‑qc/0506067) points to the wrong paper with different authors, title, and subject.

**Fix (1–2 sentences):** Replace the Freidel–Minic–Takeuchi citation with the correct arXiv ID hep-th/0507253 and update title, journal/venue, and author list in the bibliography to match the actual Holst–Immirzi‑with‑fermions paper. Ensure all in‑text attributions of “Freidel, Minic & Takeuchi” consistently point to hep-th/0507253, not gr‑qc/0506067.

---

## PAPER-PER-M1 — Incomplete Cai et al. “Non-Gaussianity in a Matter Bounce” metadata (MAJOR)

**Location:** Abstract and Table I, references to “Cai:2009fn”.

**Issue:** The key citation for the matter-bounce prediction \(f_{\rm NL}=-35/8\) is clearly intended to be Yi‑Fu Cai et al., “Non‑Gaussianity in a Matter Bounce” (astro‑ph.CO/0903.0631), but the arXiv page header only lists Robert Brandenberger in the snippet and the paper title string in the LaTeX is truncated to “Non-Gaussianity in a Matter Bounce” without author list or journal metadata.[1] This is not fatal scientifically, but the bib entry should carry the correct author list and arXiv ID explicitly, since that result underpins multiple headline claims.

**Fix (1–2 sentences):** Verify the full author list and journal/publisher info for arXiv:0903.0631 on arXiv/ADS and update the .bib entry so that “Cai:2009fn” has correct authors, title, arXiv ID, and (if applicable) published journal citation. Leave the use of \(f_{\rm NL}=-35/8\) as-is, but ensure the reference is fully specified wherever it anchors mechanism-independence statements.[1]

---

## PAPER-PER-m2 — Mis-framed Freidel citation scope (minor)

**Location:** Sec. 2.1 after Eq. (2.1): “This construction builds on Freidel, Minic & Takeuchi… who established that the Barbero-Immirzi parameter becomes physically observable through its coupling to fermionic matter.”

**Issue:** Even with the correct hep‑th/0507253 paper, Freidel–Minic–Takeuchi show that \(\gamma\) affects the four‑fermion sector and can become observable in the presence of fermions, but they do not by themselves “fix” \(\gamma\) or fully settle the physical observability question in all settings. The current sentence slightly overstates what that single reference “established.”

**Fix (1–2 sentences):** Soften the phrasing to something like “Freidel, Minic & Takeuchi showed that, in the presence of fermions, the Holst term leads to \(\gamma\)-dependent four‑fermion interactions, rendering \(\gamma\) potentially observable,” and keep all stronger interpretive claims tied to your own analysis rather than attributed to that paper alone.

---

## PAPER-PER-m3 — Ambiguous “HehlDattaNJL1971” citation key vs actual article (minor)

**Location:** Sec. 4.1 Route 1, sentence “Following the standard Hehl–Datta derivation…” and citation “\cite{Hehl1976,HehlDattaNJL1971}”.

**Issue:** The key “HehlDattaNJL1971” suggests a specific 1971 paper, but the canonical torsion‑induced four‑fermion derivation is spread across Hehl et al.’s 1976 review and earlier work by Hehl and Datta; without a concrete arXiv ID, journal, or full title, this looks like an internal placeholder rather than a verifiable bib item. From the reader’s perspective this is currently non‑auditable.

**Fix (1–2 sentences):** Replace “HehlDattaNJL1971” with a concrete bibliographic entry (journal, volume, pages, year) or an arXiv identifier corresponding to the original Hehl–Datta torsion‑NJL derivation, and ensure the .bib file includes the correct metadata. If that specific early paper is hard to locate, drop the placeholder key and cite only the 1976 Hehl et al. review with an explicit statement that it contains the standard derivation you use.

---

## PAPER-PER-m4 — Over-precise numbers tied to companion papers without full external identifiers (minor)

**Location:** Multiple spots, e.g. Sec. 1 abstract (SPHEREx 3–5σ claim referencing “Golden2026P2”), Sec. 3.2 (“Paper IV \cite{Golden2026P4}”), and throughout where Paper I(b)/II/III/IV are invoked.

**Issue:** The internal “Golden2026P2/P3/P4” references point to companion works that, as of now, have no arXiv IDs or journal metadata visible, yet they are used to support very specific quantitative claims (e.g. \(\sigma(f_{\rm NL})\), NANOGrav \(\gamma\), chirality classifier performance). Without stable external identifiers, these are not verifiable in the same way as arXiv/journal references.

**Fix (1–2 sentences):** Either (a) register preprints for the companion papers and update the bib entries with their arXiv IDs and titles, or (b) clearly label these as “internal companion manuscripts, in preparation” and downgrade claims that depend critically on them to qualitative status until externally citable versions exist. In the main text, indicate explicitly whenever a numerical claim is only supported by internal work.[]

---

## PAPER-PER-n1 — Missing explicit arXiv IDs for some named classic references (nit)

**Location:** Several places in the introduction and framework, e.g. “Ashtekar2011”, “Holst1996”, “Mercuri2009”, “MercuriCapozziello2008”, “DateKaulSengupta2009”, “LueWangKamionkowski1999”, etc., which are referenced only by author–year keys.

**Issue:** For many of these well-known works there are canonical arXiv versions (e.g., Holst 1996 as gr‑qc/9506022, Lue–Wang–Kamionkowski 1999 as astro‑ph/9812088, Mercuri 2009 as arXiv:0903.2279), but the LaTeX does not make clear that the bib entries actually map to those specific IDs. This is not wrong, but it adds friction for forensic checking of who‑said‑what.

**Fix (1–2 sentences):** In the .bib file, ensure that each of these heavily used theory references carries its corresponding arXiv identifier in an `eprint`/`archivePrefix` field, and, where appropriate, include the journal reference as well. No wording change is needed in the main text; this is a metadata‑level clean‑up to make citation forensics straightforward.[]
