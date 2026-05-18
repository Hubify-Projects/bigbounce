# P3_v3148_R10 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1300pt
**Wall time**: 31.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=62878, completion=1385, total=64263

---

## PAPER-PER-B1 — GEM-B1 Fisher-positivity refit not propagated

Issue: In §5 the text still quotes the symmetric linear propagation \(\sigma(f_{\rm NL}) = 8.27 \pm 2.37\) with a 95% CI \([3.62,12.95]\) from the linear form \(\sigma^{-2} =\) const\(+\)linear in \(\alpha\), even though the comments in the preamble (R8 GEM‑B1, R9 GEM‑B1) state the positivity‑respecting form is \(1/\sigma^2 = F_0 + c\alpha^2\) with the correct 95% envelope \([2.4,8.98]\) for the full‑sample case and \([0.94,8.98]\) for the GS subset, and that the previous \([3.62,12.95]\) etc. were erroneous. This leaves mutually inconsistent “canonical” intervals coexisting in the current draft.

Fix: Replace every remaining linear‑extrapolated \([3.62,12.95]\) and the symmetric \(\pm 2.37\) error‑bar interpretation in §5 with intervals explicitly derived from the \(1/\sigma^2 = F_0 + c\alpha^2\) fit, and state once that the Fisher‑positivity envelope (not the linear Taylor form) is the canonical CI used thereafter. Clarify that the quoted \(\pm 2.37\) is a local approximation only, not the global 95% range.  

## PAPER-PER-B2 — Caveat (j) arithmetic not fully aligned

Issue: The version-history comment at the top says caveat (j) has been corrected to the positivity‑respecting remap with envelope \([0.94,8.98]\) centred at \(\sigma=1.95\), but §5 still presents the GS forecast as \(2.28 \pm 7.43\) with a symmetric Gaussian interpretation and only notes the remap in the caveat list, relegating the physically meaningful \([0.94,8.98]\) to a deferred replacement. This creates two different “primary” descriptions of the same forecast in the same version.

Fix: Promote the \([0.94,8.98]\) asymmetric Fisher‑positivity envelope to the main text in §5 as the authoritative GS confidence interval, explicitly deprecating the symmetric \(2.28 \pm 7.43\) view as a misleading linearization kept only for historical comparison, and adjust any downstream language that still refers to the negative lower error bar.  

## PAPER-PER-M1 — Abstract/§5 still quote unphysical linear Fisher bounds

Issue: The abstract currently describes the multi-tracer \(\sigma(f_{\rm NL})\) improvement in terms of the central value “\(\sigma(f_{\rm NL}) = 8.27 \pm 2.37\)” and discusses tails that exceed the single‑tracer baseline, but it does not reflect the corrected Fisher‑positivity envelope or the fact that the earlier linear 95% intervals were formally unphysical (and flagged in GEM‑M1/R8). This means a casual reader may take the linear \(\pm 2.37\) as a standard, physically consistent error bar.

Fix: Reword the abstract (and any §5 summary sentences) so that the quoted range is explicitly anchored to the positivity‑respecting form (e.g. “\(\sigma(f_{\rm NL})\) forecast \(8.27\) with allowed range \(\sim[2.4,8.98]\) from the Fisher‑positivity form”), and explicitly note in §5 that earlier linear extrapolations are retired in favour of that form.  

## PAPER-PER-M2 — Minor inconsistency on “canonical catalog size” vs union‑find discrepancy

Issue: §4 and §6 state the unique-object count \(378{,}280\) as “canonical” while §4 and §6.4 explain there is a known arithmetic incompatibility between this number, the 388,493 detections, and the 637 cross-survey coincidences, with a still‑unreconciled 9,576‑object shortfall (deferral (a)). Presenting \(378{,}280\) as final without a very explicit “provisionally adopted; union‑find recompute pending” flag risks readers treating it as exact.

Fix: In the abstract and early sections, qualify the catalog size as “current best count” and point explicitly to deferral (a), or soften language to e.g. “headline figure \( \approx 3.78\times10^5\); exact union‑find recomputation queued” until the R3–R10 union‑find issue is resolved.  

## PAPER-PER-m1 — UMAP/HDBSCAN stability narrative slightly oversells

Issue: The UMAP/HDBSCAN stability appendix notes that only trustworthiness passes its pre‑registered threshold, while kNN‑preservation and cross‑seed Spearman fail, but then calls trustworthiness the “load‑bearing” metric and treats the taxonomy as robust. That is a reasonable judgment call, but the language could be read as implying all three metrics passed.

Fix: Tweak wording to say explicitly that only trustworthiness passes the pre‑registered thresholds, that the other two fail, and that the taxonomy is therefore to be viewed as a useful heuristic organization rather than a rigorously stable clustering.  

## PAPER-PER-n1 — eROSITA dual-score axes need clearer separation

Issue: §3.4 and Table 2 juggle two different anomaly scores for eROSITA (\(S_{\rm BigAE}\) and IsolationForest raw score), and although the text now distinguishes them, the footnote still briefly describes the 298‑object catalog as “top‑298” relative to the 9,303‑object IF reference set with “high overlap”, which can easily be misread as a strict subset claim (the exact intersection is still deferred).

Fix: Add one sentence in the eROSITA text explicitly stating that the 298‑source canonical catalog is defined solely on the BigAE z‑score axis and is not guaranteed to be a subset of the IF top‑1% set, with the intersection count pending; that will prevent readers from conflating the two axes or assuming a proven subset relation.  


