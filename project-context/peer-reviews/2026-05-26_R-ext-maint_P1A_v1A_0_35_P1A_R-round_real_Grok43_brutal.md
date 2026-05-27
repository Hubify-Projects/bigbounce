# P1A R-round — REAL cross-vendor — Grok-4.3 brutal-honesty reviewer

**Model**: `x-ai/grok-4.3` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-26_R-ext-maint_P1A_v1A_0_35
**Wall time**: 11.7s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=26797, completion=1537, reasoning=873, total=28334

---

**PAPER-GRO-B1**  
**BLOCKER** — Title + abstract (lines 1–3, abstract ¶1)  
Title and abstract advertise a “No-Go Theorem” and “structural closure” of minimal-ECH dark energy. The text immediately qualifies that the four routes are not claimed to be a complete operator basis and that Jackiw–Pi CS and the parity-odd four-fermion partner are omitted.  

Fix: Retitle to “Channel-Level Amplitude Constraints on Four Enumerated Minimal-ECH Dark-Energy Routes” and remove “No-Go Theorem” from the title and abstract.

**PAPER-GRO-B2**  
**BLOCKER** — Sec. 9 (Table 2 + Barriers 1–14)  
Fourteen “logically independent mechanism-class constraints” are listed, yet the text states that B8 is the observational consequence of B14 and is retained only for “historical completeness.” This directly contradicts the independence claim used to reach the headline number 13/14.  

Fix: Either drop the independence language or remove B8 from the count and table.

**PAPER-GRO-M1**  
**MAJOR** — Sec. 4 (four-route closure) + Appendix B  
The dimensional ansatz \(\rho_\Lambda^{\rm bounce} \sim (\alpha/M) M_{\rm Pl}^5\) is repeatedly labeled a “phenomenological scaling ansatz, not a controlled EFT result,” yet \(N_{\rm tot} \approx 92\) and the entire structural-tension argument are derived from it. The central amplitude no-go therefore rests on an admitted non-derivation.  

Fix: State explicitly that the amplitude closures of R1–R4 are independent of the ansatz, or move the \(N_{\rm tot}\) tension argument to a separate “phenomenological consistency check” section.

**PAPER-GRO-M2**  
**MAJOR** — Abstract + Sec. 13  
The two “surviving” predictions (\(f_{\rm NL} = -35/8\) and \(\beta \approx 0.27^\circ\)) are explicitly stated to be properties of the matter-bounce class and of generic GR+ALP setups, respectively, with “no ECH input.” Presenting them as outputs of the present work is therefore inaccurate.  

Fix: Remove both from the abstract and from the “surviving tests” section; keep only the statement that ECH does not forbid them.

**PAPER-GRO-m1**  
**minor** — Throughout (especially comments and version history)  
The LaTeX source contains extensive internal review logs, Gemini error audits, and “R23 closure” notes. These have no place in a submission draft.  

Fix: Delete all review-history blocks before any external submission.

**PAPER-GRO-n1**  
**nit** — Sec. 10 (perturbation transparency)  
The result that torsion vanishes for canonical scalars and the Holst term becomes topological is a direct consequence of the algebraic Cartan equation plus the Bianchi identity; it is not a new theorem.  

Fix: Cite the standard EC literature and label the section “Restatement of known decoupling for scalar matter” rather than “The Perturbation-Transparency Result.”
