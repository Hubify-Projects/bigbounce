# P1A_v1A028_R9 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1230pt
**Wall time**: 9.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=28658, completion=744, total=29402

---

## PAPER-PER-B1

**BLOCKER — fused bibliography metadata in Route 1.** The text cites `HehlDattaNJL1971` as if it were the standard torsion-induced NJL/Hehl–Datta source, but the metadata in the manuscript is not anchored to a real arXiv/publisher record here and the route description should be pinned to an actual paper entry. Fix by replacing the placeholder-style key with the exact journal/arXiv citation used for the Hehl–Datta derivation and verifying the authors, year, and title against the source record. 

## PAPER-PER-B2

**MAJOR — Route 2 citation trail is internally unsafe.** The manuscript attributes the one-loop parity-odd Holst correction to `Mercuri2009` and `MercuriCapozziello2008`, but the claimed dimensional/birefringence chain is not cleanly tied to a single real publication in the text, so the reader cannot audit which result is actually being used. Fix by splitting the claim into separately cited statements: one for the Holst/Nieh–Yan one-loop structure and one for any photon-birefringence matching, with exact titles and venues. 

## PAPER-PER-B3

**MAJOR — Route 4 overstates what the cited birefringence paper supports.** The text treats the Planck/ACT birefringence signal as if it directly licenses the full ALP-to-dark-energy inversion, but the cited observational papers only constrain a rotation angle; they do not establish the cosmological-density relation used later in the no-go. Fix by narrowing the claim to “the measurement constrains \(\beta\)” and separating that from the model-building step that relates \(\beta\) to \(\rho_\theta\). 

## PAPER-PER-B4

**BLOCKER — Appendix B has an explicit mass-dimension admission that undercuts the main result.** The appendix says the parity-odd operator is off-shell dimension \(+1\), not a controlled dimension-\(+4\) EFT operator, and then rescues the main formula only by on-shell scaling ansatz with extra \(M_{\rm Pl}\) insertions. Fix by either deriving a genuine dimension-\(+4\) operator basis or removing all claims that the dark-energy density follows from the operator itself. 

## PAPER-PER-B5

**MAJOR — the paper mixes two incompatible treatments of \(M_{\rm Pl}^5\) vs \(M_{\rm Pl}^4\).** In the main text it alternates between \(\rho_\Lambda^{\rm bounce}\sim (\alpha/M)M_{\rm Pl}^5\) and \([\!(\alpha/M)M_{\rm Pl}\!]M_{\rm Pl}^4\), while Appendix B says these are only phenomenological on-shell scalings, not derivations. Fix by choosing one scaling convention, stating its dimensional status once, and ensuring every downstream \(N_{\rm tot}\) estimate uses the same power counting. 

## PAPER-PER-B6

**minor — some arXiv-style references look non-auditable from the manuscript alone.** Several citations are given only as author-year keys without titles or venues, which makes it easy to fuse metadata from different papers. Fix by expanding the bibliography entries for the load-bearing citations in Routes 1–4 and the observational claims so each source can be checked against arXiv or publisher records. 
