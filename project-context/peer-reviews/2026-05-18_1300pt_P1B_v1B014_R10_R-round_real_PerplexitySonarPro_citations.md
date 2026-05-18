# P1B_v1B014_R10 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1300pt
**Wall time**: 9.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=17756, completion=958, total=18714

---

## PAPER-VERIF-B1

**BLOCKER — fused / likely confabulated citation metadata in the birefringence section.**  
The paper cites `Eskilt2022b`, `DiegoPalazuelos2022`, and `DiegoPalazuelos2025` as if they are established published sources for the quoted birefringence numbers, but I could not verify these specific arXiv/title-author combinations from the supplied text, and the one arXiv lookup I did for a seemingly related ID was clearly an unrelated paper, which is a red flag for citation fusion. **Fix:** replace every birefringence citation with the exact bibliographic record from arXiv/publisher/ADS, including correct author list, title, journal, and arXiv ID, and ensure no citation key points to a different paper than the quoted result.

## PAPER-VERIF-B2

**MAJOR — the paper’s “published joint Planck+ACT 3.6σ” claim is not citation-audited.**  
The text asserts a specific published joint value, \(\beta = 0.342^\circ \pm 0.094^\circ\), and uses it as a load-bearing anchor, but the provenance is not demonstrated in the manuscript text itself beyond an in-text cite key, so the claim is not yet citation-forensically secure. **Fix:** add an explicit reference note or bibliography entry with the exact source and confirm that the quoted number, significance, and “joint Planck+ACT” wording match that source verbatim.

## PAPER-VERIF-B3

**MAJOR — internal arithmetic/consistency issue in the ALP coupling range.**  
The manuscript says \(C_{a\gamma}(\Delta\phi/f_a)\approx 10.3\) for \(\beta=0.342^\circ\), then states \(\Delta\phi/f_a\in[0.2,1.1]\) implies \(C_{a\gamma}\sim 9\) to \(\sim 51\); that range is numerically consistent only if the prefactor assumptions are exactly right, but the text mixes \(\theta_i\), \(\Delta\phi/f_a\), and \(C_{a\gamma}\) in a way that remains easy to misread as a dimensional or algebraic mismatch. **Fix:** rewrite the derivation as one compact equation chain with definitions for every symbol and a single consistent variable set, then state the numeric interval with the exact arithmetic steps.

## PAPER-VERIF-B4

**MAJOR — Table 1B convergence claim is overstated relative to the reported diagnostics.**  
The table says the iter2 chain is “CONVERGED” because \(\hat R-1 = 0.00820 < 10^{-2}\), but the same caption also reports \(N_{\rm effective}=89{,}871\) after 30% burn-in and a chain-length diagnostic \(\hat R_{\rm cl}=0.0705\), so the manuscript is mixing convergence of one criterion with a much weaker/ambiguous chain-length condition. **Fix:** separate “R-hat convergence” from “sufficient chain length” and state clearly which diagnostic is the acceptance criterion for publication readiness.

## PAPER-VERIF-B5

**minor — SH0ES paragraph is internally dense and risks misleading the reader about what is actually constrained.**  
The caveat (c) paragraph correctly says the full-tension chain includes the SH0ES likelihood and that \(H_0\) remains Planck-dominated, but the prose buries the key point under several nested clauses and may read as if the SH0ES prior directly “pulls” \(H_0\) when the text later says it mainly constrains \(M_B\). **Fix:** split the paragraph into two sentences: one for which likelihood is active, one for what parameter it actually constrains and what does not move.

## PAPER-VERIF-B6

**minor — scope tightening around \(f_{\rm NL}=-35/8\) is okay, but the manuscript should stop implying relevance outside the specific matter-bounce class.**  
The text already says this is “matter-bounce-specific,” but it then repeats the value in a broader structural-closure context, which can still be read as a general program prediction. **Fix:** keep the number only in the matter-bounce subsection and add a one-line “not applicable to the rest of the model class” note where it is first mentioned.
