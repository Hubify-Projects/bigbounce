# P1A R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round7
**Wall time**: 9.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=35658, completion=1087, total=36745, search_context_size=low, cost={'input_tokens_cost': 0.10697, 'output_tokens_cost': 0.01631, 'request_cost': 0.006, 'total_cost': 0.12928}

---

## PAPER-PER-B1 — **BLOCKER**
**Line/section:** `\section{Theoretical Framework}` → `\subsubsection{Derivation of the Parity-Odd Term}` / `\subsection{Route 2}`

**Issue:** The paper cites `\cite{ShapiroTeixeira2014}` and treats it as support for a one-loop Holst/Nieh–Yan parity-odd coefficient, but the bibliography key and claim need verification against the actual paper metadata. The source likely exists as *Quantum Einstein-Cartan theory with the Holst term* (Shapiro & Teixeira, CQG 31:185002, 2014), but the manuscript repeatedly uses it for more than it actually derives, sliding from “motivated by” to effective coefficient support.  

**Fix:** Make the citation strictly descriptive: say the paper motivates Holst/Nieh–Yan structure, not the exact one-loop operator or coefficient. Verify the bib entry against arXiv/publisher metadata and remove any wording implying the exact coefficient is published there.

## PAPER-PER-M2 — **MAJOR**
**Line/section:** `\subsubsection{Route 4}`

**Issue:** The text attributes the standard ALP birefringence normalization to `LueWangKamionkowski1999` but then mixes it with a specific `-\tfrac14(\alpha/M)\theta \tilde F F` normalization and claims the paper is the source for the cosmological birefringence operator. That is a citation-metadata/claim fusion: Lue–Wang–Kamionkowski is an early birefringence paper, not the provenance of the exact normalization used here.  

**Fix:** Split the claim: cite Lue–Wang–Kamionkowski only for early birefringence phenomenology, and cite a modern axion-electrodynamics reference for the exact normalization. Keep the paper’s normalization as a convention, not as something derived from that source.

## PAPER-PER-M3 — **MAJOR**
**Line/section:** Abstract; `Companion paper` paragraph; `Section 3`; `Section 15`; Appendix A

**Issue:** The manuscript repeatedly cites `Golden2026P1b`, `Golden2026P2`, `Golden2026P3`, and `Golden2026P4` as if they are published companion works, while the text elsewhere labels them “in preparation.” That is acceptable internally, but citation-forensics-wise it is still a live metadata risk: these are not arXiv-verifiable works in the current paper and should not be presented as external evidence for numbers, MCMC results, NaMaster validation, or galaxy-spin claims.  

**Fix:** Keep them explicitly as in-preparation internal companions everywhere, and remove any phrasing that treats their numerical outputs as externally citable literature. If the paper is to be reviewed as a standalone manuscript, segregate those claims into clearly marked unpublished internal inputs.

## PAPER-PER-M4 — **minor**
**Line/section:** `\subsection{Route 3 (quantum running of the Immirzi parameter)}`

**Issue:** The paper cites `Benedetti2011` and `DateKaulSengupta2009` for Immirzi running, but the text overstates what those works establish. The manuscript itself partially corrects this by saying Date–Kaul–Sengupta do not present the explicit RG equation, yet the surrounding prose still reads as if the running law is sourced from them.  

**Fix:** Explicitly label Eq. (gamma_running) as the authors’ phenomenological ansatz, not a published equation. Restrict the citations to “motivation” language and verify the exact bibliographic details of the cited papers.

## PAPER-PER-N1 — **minor**
**Line/section:** `Abstract`; `Sec. 1`; `Sec. 4`; `Sec. 9`; Appendix B

**Issue:** The manuscript repeatedly claims a “first Bianchi identity” derivation for vanishing Holst dual contraction, but the proof text later says the torsion-free Holst term becomes a Pontryagin density that is generically nonzero pointwise and only a boundary term. These are not equivalent statements, and the prose conflates them.  

**Fix:** Rephrase consistently: torsion-free Holst/Nieh–Yan terms reduce to a topological boundary term, not identically zero pointwise. Keep the Bianchi-identity claim only where it is mathematically justified.

## PAPER-PER-N2 — **nit**
**Line/section:** `\subsection{Route 1}`; `Section 9 Barrier 8`

**Issue:** The paper alternates between calling the Hehl–Datta contact term parity-even and using it as part of a “parity-odd / dark-energy route” taxonomy. That taxonomy is internally confusing and risks misleading the reader about what is actually being excluded.  

**Fix:** State explicitly that Route 1 is excluded on amplitude grounds and is parity-even, while the paper’s “parity-odd” framing applies only to the broader route catalog, not the NJL operator itself.
