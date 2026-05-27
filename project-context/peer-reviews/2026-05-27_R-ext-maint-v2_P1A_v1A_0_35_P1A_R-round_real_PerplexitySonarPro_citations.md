# P1A R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-27_R-ext-maint-v2_P1A_v1A_0_35
**Wall time**: 28.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30063, completion=1910, total=31973

---

## PAPER-PER-B1 — Mis-cited Freidel et al. paper

**Location:** Sec. “Einstein-Cartan-Holst Action”, first paragraph around “Freidel, Minic & Takeuchi [Freidel2005]”.  

**Issue:** The text attributes the physical observability of the Barbero–Immirzi parameter via fermionic couplings to “Freidel, Minic & Takeuchi” with a 2005 reference tag, but the arXiv record gr-qc/0506067 is “A group field theory for 3d quantum gravity coupled to a scalar field” by Freidel, Oriti & Ryan and has nothing to do with Holst/Immirzi–fermion couplings.[2] The cited metadata (authors, topic) are fused from a different Freidel–Minic–Takeuchi paper.  

**Fix:** Replace the Freidel-2005 citation with the correct paper that actually treats Holst + fermions and Immirzi observability (e.g. the Freidel–Minic–Takeuchi Holst/fermion work, with correct arXiv ID, title, authors, and journal), and ensure the bibitem matches that record exactly.

---

## PAPER-PER-M1 — Mislabeling Ashtekar–Singh 2011 critical-density range

**Location:** Sec. “Loop Quantum Cosmology and the Holst Action”, eq. (mod. Friedmann) discussion and in Barrier 12 description; text states “Ashtekar–Singh … \(\rhocrit \simeq 0.27\text{–}0.41\,\rho_{\rm Pl}\)” and later calls this “the Ashtekar–Singh effective-LQC status report [1108.0893]”.  

**Issue:** The cited LQC status report arXiv:1108.0893 (Ashtekar & Singh, Class. Quant. Grav. 28 (2011) 213001) does give a critical density of order \(0.41 \rho_{\rm Pl}\) in the standard scheme, but the specific two-point range “0.27–0.41” and its split into “ABCK” vs “DLM” values for \(\gamma\) and \(\rho_c\) is not quoted as such in that review.[1] You are importing 0.27 from LQG entropy-counting literature and presenting the pair as a direct Ashtekar–Singh interval.  

**Fix:** Keep using Ashtekar–Singh for the standard \(\rho_c \approx 0.41\rho_{\rm Pl}\), but either (a) explicitly cite separate LQG entropy-counting papers for the \(\gamma\)-dependent variation giving \(\sim 0.27\), or (b) rephrase to say “\(\rho_c \sim 0.4\rho_{\rm Pl}\)” with a single value directly supported by Ashtekar–Singh, rather than a 0.27–0.41 “window” attributed to that paper.

---

## PAPER-PER-M2 — Incomplete metadata and arXiv info for Cai et al. (matter bounce)

**Location:** Abstract and throughout (e.g. Table I caption) when citing “Cai:2009fn” for the matter-bounce prediction \(\fnl=-35/8\).  

**Issue:** The source is arXiv:0903.0631, “Non-Gaussianity in a Matter Bounce” by Cai, Chen, Brandenberger & Zhang, submitted 2009-03-03.[0] In the current manuscript the arXiv ID is only given as “Cai:2009fn” in the BibTeX-style key, with no explicit arXiv number, author list, or journal metadata anywhere in the body; for a forensic cosmology paper claiming careful amplitude-level closure, the missing explicit arXiv and authorship makes cross-checking harder and risks confusion with other Cai 2009 non-Gaussianity papers.  

**Fix:** When you first invoke the \(\fnl = -35/8\) result, explicitly identify the paper as “Cai et al., ‘Non-Gaussianity in a Matter Bounce’, arXiv:0903.0631 (astro-ph.CO)” and ensure the bibliography entry includes the correct title, full author list, arXiv ID, and any journal reference.

---

## PAPER-PER-m1 — Ambiguous “Hehl–Datta NJL” citation

**Location:** Route 1 discussion, Sec. “Route 1 (NJL four-fermion contact)” around “Hehl–Datta NJL contact term … Hehl–DattaNJL1971”.  

**Issue:** The canonical source for the torsion-induced four-fermion term is usually cited as Hehl et al. 1976 (Rev. Mod. Phys. 48, 393) or earlier Einstein–Cartan papers; there is no obvious 1971 “Hehl–Datta NJL” article with that exact label in standard databases, and the closest standard long review is Hehl et al., Phys. Rept. 258:1–171 (1995), arXiv:gr-qc/9402012.[3] The combined “HehlDattaNJL1971” key looks like fused metadata rather than a real publication.  

**Fix:** Replace the “Hehl–DattaNJL1971” citation with concrete, existing references: e.g. Hehl, von der Heyde, Kerlick & Nester, Rev. Mod. Phys. 48 (1976) 393 and/or Hehl et al., Phys. Rept. 258 (1995) 1–171, with correct arXiv IDs (gr-qc/9402012) and journal details, and adjust prose to refer to “Hehl et al.” rather than “Hehl–Datta NJL” if no standalone Datta paper is being used.

---

## PAPER-PER-m2 — Vague reference to “Freidel–Minic–Takeuchi Holst–fermion construction”

**Location:** Sec. “Derivation of the Parity-Odd Term”, Step 3, referencing “the Holst+non-minimal-fermion construction of Mercuri [Mercuri2009]”, and earlier tying the physical visibility of \(\gamma\) to Freidel, Minic & Takeuchi.  

**Issue:** The arXiv record gr-qc/0506067 is not by Freidel, Minic & Takeuchi and does not discuss Barbero–Immirzi–fermion couplings; it is a Freidel–Oriti–Ryan GFT paper.[2] You appear to be combining Mercuri’s Holst+fermion work with an incorrectly remembered Freidel collaboration, producing a pseudo-lineage (Freidel–Minic–Takeuchi → Mercuri) that is not actually reflected in the arXiv literature.  

**Fix:** Strip “Freidel, Minic & Takeuchi” from the Holst–fermion narrative unless you can supply a correct arXiv ID and title showing that specific trio treating Immirzi–fermion couplings; otherwise, credit the Holst+non-minimal-fermion construction solely to Mercuri with the correct 2006/2009 references and remove the spurious Freidel–Minic–Takeuchi node from the citation chain.

---

## PAPER-PER-n1 — Companion “Golden2026P2/P3/P4/P1b” placeholders lack discoverable IDs

**Location:** Throughout: references to “Golden2026P2” (Paper II), “Golden2026P3” (Paper III), “Golden2026P4” (Paper IV), and “Golden2026P1b” (companion MCMC paper).  

**Issue:** These are treated as arXiv-style keys but no actual arXiv IDs, DOIs, or journal references are given; a search on arXiv for “Golden 2026 Einstein-Cartan Holst bounce”, “Golden bounce non-Gaussianity” etc. returns no such records as of now, so an external reader cannot verify any of the claims delegated to these “P2/P3/P4/P1b” works.[1][0] As written, they function as opaque internal documents rather than citable literature.  

**Fix:** Before journal submission, either (a) update each Golden2026Px citation with its real arXiv identifier and title once those preprints exist, or (b) clearly mark them as “in preparation, private communication” and avoid using them as the sole source for any quantitative claim that is central to the present paper’s no-go arguments.
