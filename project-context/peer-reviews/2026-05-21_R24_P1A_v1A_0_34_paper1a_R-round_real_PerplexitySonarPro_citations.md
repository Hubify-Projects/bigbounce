# paper1a R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R24_P1A_v1A_0_34
**Wall time**: 8.7s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30324, completion=651, total=30975

---

# Review

## PAPER-PER-B1
**BLOCKER | sec. \ref{sec:dilution} / sec. \ref{sec:gdp} / Appendix B**  
The draft still treats \((T_{\rm reh}/M_{\rm GUT})^{3/2}\) as a “phenomenological phase-space ansatz,” but the text then uses it to propagate a precise \(N_{\rm tot}\approx 92\) inference; that is not a closed derivation and the paper admits the dependence. The fix is to downgrade every downstream quantitative claim that depends on Eq. \(\ref{eq:Dinf}\) to order-of-magnitude only, or replace the ansatz with an actual derivation.  

## PAPER-PER-B2
**MAJOR | sec. \ref{sec:r2_oneloop}**  
Route 2 cites Mercuri/Capozziello for a one-loop parity-odd coefficient, but the paper’s own formula and wording are internally inconsistent about the dimensional reduction and even note a second “distinct” ratio of order \(10^{-33}\). The fix is to choose one consistent observable, state the exact dimensional chain once, and remove the alternate ratio unless it is fully derived.  

## PAPER-PER-B3
**MAJOR | sec. \ref{sec:r4_birefringence}**  
The Chern-Simons 4-current is finally defined inline, but the route still conflates three different things: a spectator-ALP fit, an ECH-internal parity-odd operator, and a dark-energy source. The fix is to separate “fitted ALP consistency check” from “ECH no-go” and explicitly state that the birefringence match is not derived from ECH.  

## PAPER-PER-B4
**MAJOR | sec. \ref{sec:fourroute} / sec. \ref{sec:related}**  
The bibliography chain is still vulnerable to fused or mismatched metadata: the manuscript repeatedly points to route-closure citations while also admitting that several operators are not enumerated and that companion-paper content is external. The fix is to audit every cited source against the exact claim being made, especially where a title, arXiv ID, and author set are bundled into a single “support” sentence.  

## PAPER-PER-B5
**minor | Appendix B**  
Appendix B is doing double duty as both a dimensional-status note and a retrofit defense of the main-text \(N_{\rm tot}\) value, which makes the paper’s logical dependency graph harder to trust. The fix is to keep Appendix B purely diagnostic and move any sensitivity analysis of \(N_{\rm tot}\) into a separate, explicitly non-binding note.  

## PAPER-PER-B6
**nit | throughout**  
The manuscript repeatedly says “closed,” “no-go,” and “structural closure,” while also leaving several results explicitly phenomenological or deferred. The fix is editorial: reserve “closed” for fully derived claims and use “effectively ruled out at the channel level” for the rest.
