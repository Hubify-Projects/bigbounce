# INT API Review — P1U v1U.0.13 — gemini (gemini-3.1-pro-preview)
paper: P1U  version: v1U.0.13  model: gemini-3.1-pro-preview
modality: native-PDF (inline_data base64)
UTC: 2026-07-11T15:03:01.406721Z  |  latency: 53.7s  |  attempt: 1
usage: {"promptTokenCount": 31294, "candidatesTokenCount": 673, "totalTokenCount": 33646, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 94}, {"modality": "IMAGE", "tokenCount": 31200}], "thoughtsTokenCount": 1679, "serviceTier": "standard"}
PARSED VERDICT: MAJOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MAJOR REVISIONS

**ISSUES:**
1. [MAJOR] **Presentation and Tone:** The manuscript is excessively verbose, repetitive, and defensively written. The extensive disclaimers, "evidentiary status" classifications (e.g., Tables I, III, XI), and legalistic scoping paragraphs (e.g., the boxed "What this paper does and does not establish" on page 4) severely detract from the physics. The author must heavily condense the text, remove the meta-commentary, and adopt a standard scientific tone appropriate for *Physical Review D*. 
2. [MAJOR] **Originality and Context:** The core physical observation—that minimal Einstein-Cartan torsion sourced by Standard Model fermions is Planck-suppressed and therefore too weak to drive late-time dark energy—is a well-established consequence of the algebraic Cartan constraint (e.g., Hehl et al. 1976). The author must substantially streamline the discussion of Route 1 to reflect its status as established background. The genuine novelty lies primarily in linking the Holst/Nieh-Yan loop running (Routes 2 and 3) to the cosmic birefringence observational budget (Route 4), and the paper should be restructured to focus tightly on this synthesis rather than presenting a sprawling 14-point catalog.
3. [MAJOR] **Triviality of the "Perturbation Transparency" Theorem:** The central result of Section X boils down to two well-known facts: (1) canonical scalars carry no spin, hence source zero torsion ($S=0 \implies T=0$), and (2) the Holst term vanishes identically on a torsion-free Levi-Civita connection due to the first algebraic Bianchi identity. Expanding this into a multi-page "theorem" with term-by-term perturbation checks is entirely unnecessary. This should be reduced to a single short paragraph stating the exact geometric identity.
4. [MINOR] **Over-reliance on Artifacts and Companions:** While the commitment to open science and reproducibility is commendable, a PRD manuscript must be physically self-contained. The exhaustive documentation of MCMC chain convergence statistics, GitHub repository structures, and NaMaster pseudo-$C_\ell$ pipeline validation (Appendices E, F, and H) reads like a software validation report rather than a theoretical physics paper. These sections should be drastically truncated, citing the repository for purely technical details.
5. [MINOR] **Nomenclature of the "14 Constraints":** Grouping 14 disparate arguments—ranging from exact algebraic identities (the Bianchi identity) to heuristic naturalness bounds (the cosmological constant problem) and simple scaling limits (naive dimensional analysis)—into a co-equal "mechanism-class" catalog is confusing and overstates the rigidity of the no-go arguments. The author should abandon this "catalog" framing and simply present the arguments sequentially as EFT scaling bounds, geometric identities, and naturalness limitations.

**ONE-SENTENCE SUMMARY:**
The central claim that minimal Einstein-Cartan-Holst theory cannot naturally source late-time dark energy is technically supported by standard effective field theory and geometric arguments, but the manuscript requires a massive structural rewrite to strip away defensive meta-commentary and meet the presentation and originality standards of the journal.