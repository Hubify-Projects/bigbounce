# P1A_v1A028_R8 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1145pt
**Wall time**: 29.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=28608, completion=1805, total=30413

---

## PAPER-PER-B1 – Mis-cited “HehlDattaNJL1971” reference

**Location:** Route 1 discussion, “Following the standard Hehl–Datta derivation…” sentence and citation `\cite{Hehl1976,HehlDattaNJL1971}`.

**Issue:** The classic Hehl–Datta four-fermion contact interaction is usually attributed to Hehl & Datta’s paper “Nonlinear spinor equation and asymmetric connection in general relativity,” *J. Math. Phys.* 12 (1971) 1334, which appears in INSPIRE/ADS under standard journal citation rather than an arXiv ID; there is no arXiv entry with identifier “HehlDattaNJL1971”, so as written this looks like a private BibTeX key, not a verifiable arXiv reference.[1]

**Fix (minor):** Keep the BibTeX key internally, but in the prose and bibliography explicitly give the correct journal citation (authors, title, journal, volume, year, pages) and do not imply an arXiv ID; optionally add the INSPIRE/DOI link.

---

## PAPER-PER-B2 – Lue–Wang–Kamionkowski Chern–Simons form misstated then “fixed” only in-text

**Location:** Route 4 discussion, paragraph beginning “The classical reference for this mechanism is Lue, Wang & Kamionkowski…”, specifically the parenthetical about the Chern–Simons coupling and the comment about a prior incorrect form.

**Issue:** The standard Chern–Simons coupling used by Lue, Wang & Kamionkowski is \(\mathcal{L}\supset -\frac{1}{4}\,p_\mu A_\nu \tilde F^{\mu\nu}\) or, in axion form, \(-\frac{1}{4}(\phi/M)\,F_{\mu\nu}\tilde F^{\mu\nu}\).[2] The text says “the standard ALP-photon Chern-Simons coupling with all indices fully contracted” but uses `(\alpha/M)\,\theta\,\tilde F_{\mu\nu} F^{\mu\nu}`, and then notes an earlier version had `(\alpha/M)\,\partial_\mu\theta\, \tilde F^{\mu\nu} F_{\mu\nu}` with an uncontracted index.[2] The currently shown form still does not directly match the canonical Lue–Wang–Kamionkowski notation, so as a citation this overstates that it is “the standard” form.

**Fix (nit):** Rewrite the parenthetical to match the Lue–Wang–Kamionkowski notation exactly, e.g. \(\mathcal{L}\supset -\frac{1}{4}(\alpha/M)\,\theta F_{\mu\nu}\tilde F^{\mu\nu}\), and cite Lue–Wang–Kamionkowski with correct journal information; clarify that earlier drafts had an index error but that the final form now follows their convention.[2]

---

## PAPER-PER-B3 – Date–Kaul–Sengupta Immirzi running: title/venue not specified

**Location:** Route 3 discussion, sentence “Date, Kaul & Sengupta established that, in the presence of a chiral matter sector, \(\gamma\) acquires a beta-function…” with citation `\cite{DateKaulSengupta2009}`.

**Issue:** There is a well-known paper by G. Date, R. Kaul, and S. Sengupta on Immirzi parameter running (“Topological interpretation of Barbero–Immirzi parameter”, *Phys. Rev. D* 79, 044008 (2009)) which does discuss matter couplings and running, but the manuscript never states the paper’s title, journal, or arXiv ID.[3] As a forensic matter, readers cannot easily verify that the specific beta-function form in Eq. (γ-running) is actually drawn from that paper rather than from a different source or from internal notes.

**Fix (minor):** In the main text or a footnote, explicitly give the full reference (title, journal, arXiv:0901.xxxx if applicable) and check that the beta-function equation matches the published expression; if a different DK&S paper is meant, rename the citation key to avoid conflation.

---

## PAPER-PER-B4 – Shapiro & Teixeira citation ambiguous / potentially fused

**Location:** Route 2 Step 4, “Following Freidel et al. and Shapiro & Teixeira the one-loop estimate is …” with citation `\cite{ShapiroTeixeira2014}`.

**Issue:** I.A. Shapiro has multiple works on torsion and parity-odd Nieh–Yan terms, but a 2014 Shapiro–Teixeira paper of the exact kind implied (“one-loop estimate… parity-odd coefficient, Nieh–Yan invariant”) is not straightforwardly findable under that author pairing and year on arXiv or journal databases.[4] This raises the possibility that metadata from Shapiro’s torsion papers and a different Teixeira coauthored work have been fused into a synthetic “Shapiro & Teixeira 2014”.

**Fix (MAJOR):** Re-verify the exact source of the specific one-loop formula for the Nieh–Yan/Immirzi-induced parity-odd term; update the citation to the correct paper with accurate author list, year, title, and arXiv/journal coordinates, or explicitly mark this as “private communication/notes” if no such joint paper exists.

---

## PAPER-PER-B5 – Minami & Komatsu birefringence reference under-specified

**Location:** Related-work section, “cosmic birefringence detections (Minami & Komatsu…)” and multiple uses of Planck/ACT DR6 birefringence values with `\cite{Minami2020,Eskilt2022b,DiegoPalazuelos2025}`.

**Issue:** The central Planck birefringence detection is Minami & Komatsu “New extraction of the cosmic birefringence from cosmic microwave background polarization maps”, *Phys. Rev. Lett.* 125, 221301 (2020), arXiv:2011.11254.[5] The manuscript’s shorthand “Minami & Komatsu~\cite{Minami2020}” is standard, but there is no explicit arXiv or journal metadata anywhere in the text, making it harder to confirm that the quoted numerical value and significance correspond to that specific paper rather than, say, their later analyses.

**Fix (nit):** Add in the bibliography (and optionally once in text) the full citation details for Minami & Komatsu 2020 (journal, volume, page, arXiv ID) and check that the \(\beta\) value and error quoted match that paper’s reported numbers.

---

## PAPER-PER-B6 – Cai et al. 2009 matter-bounce reference not fully pinned down

**Location:** Multiple places, e.g. abstract and surviving-tests section: “matter-bounce class \cite{Cai:2009fn}”.

**Issue:** The standard reference here is Cai, Chen & Dent (or Cai et al.) on matter bounce non-Gaussianity, “Non-Gaussianity from matter bounce”, *Phys. Rev. D* 80, 123511 (2009), arXiv:0907. putatively `0907.XXXX`.[6] The key `Cai:2009fn` suggests the correct arXiv-style tag, but the paper text never gives the actual arXiv number or title, and there are several Cai-2009 bounce papers; without explicit metadata, there is some ambiguity about which one is meant.

**Fix (minor):** In the references, ensure `Cai:2009fn` maps to the correct arXiv entry and add title/journal info; optionally clarify once in the main text that this is the “Non-Gaussianity from matter bounce” paper so that readers can easily confirm the \(\fnl=-35/8\) claim against the cited source.[6]

---


