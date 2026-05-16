# P4_v1091 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-15_2330pt_P4_v1091_R10_R-round_real
**Wall time**: 10.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=81668, completion=976, total=82644

---

# Review

## PAPER-PER-B1 — Major
**Section:** Bib entry `\bibitem{Ivezic:2019}`  
**Issue:** The bibliography fuses the LSST Science Book arXiv preprint with the later ApJ reference-design paper. arXiv `0805.2366` is titled *LSST: from Science Drivers to Reference Design and Anticipated Data Products*, and the arXiv record itself points to a related DOI for the 2019 ApJ article, so the current entry is metadata-mixed rather than a clean citation.   
**Fix:** Split the citation into either the arXiv preprint entry or the ApJ article entry, but do not present them as a single identical paper unless you explicitly note the relationship.

## PAPER-PER-B2 — Major
**Section:** Abstract, Introduction, and Sections `\ref{sec:ceresnet}` / `\ref{sec:stats}`  
**Issue:** The paper repeatedly cites Jia et al. as `ApJ 943, 32` with DOI `10.3847/1538-4357/aca8aa`, which is correct for arXiv `2210.04168`; however, the manuscript’s own internal claims about sample size and “1.95 million galaxies” must be kept aligned with that specific CE-ResNet paper, which is the Z-wise vs S-wise spirals classifier paper. The reference itself is fine, but the manuscript’s phrasing around “all classified as CW or CCW since CE-ResNet lacks a not-spiral class” is a factual extrapolation beyond the paper’s bibliographic scope.   
**Fix:** Keep the citation, but rephrase claims about CE-ResNet’s catalog and class structure as what the cited paper explicitly reports, not as an inferred property of the present manuscript’s downstream use.

## PAPER-PER-B3 — Minor
**Section:** Bib entry `\bibitem{Dosovitskiy:2020}`  
**Issue:** The bibliography lists the ViT paper as an ICLR 2021 camera-ready version with arXiv `2010.11929`, which is fine; however, the in-text model description makes it sound like the paper itself is the source of the exact `vit_small_patch16_224` checkpoint and fine-tuning regime, which it is not. The paper is a general ViT reference, not evidence for the specific model variant or training recipe.   
**Fix:** Keep the citation for the Vision Transformer architecture only, and cite your own training artifacts or code for the exact checkpoint and head design.

## PAPER-PER-B4 — Minor
**Section:** Bib entry `\bibitem{Shamir:2022DESI}`  
**Issue:** The citation metadata is internally consistent with arXiv `2208.13866` and DOI `10.1093/mnras/stac2372`, but the manuscript uses it interchangeably as both a “DESI Legacy spin-directions paper” and a spiral-sample-size comparator. The arXiv abstract says “nearly 1.3 million galaxies” and does not itself support the manuscript’s repeated “~200,000 spirals” phrasing.   
**Fix:** If you use `~200,000 spirals`, source that number from the paper text or a secondary analysis, not from the arXiv abstract. Otherwise stick to the abstract’s stated nearly 1.3 million galaxies.

## PAPER-PER-B5 — Nit
**Section:** `\bibitem{DESI:2016}`  
**Issue:** This entry is incomplete: it has only `arXiv:1611.00036 (2016)` and no title, authors, journal venue, or arXiv title. That is acceptable only if you intend it as a placeholder, but it is not a properly auditable citation.  
**Fix:** Replace with a complete bibliographic entry or remove it if it is not needed.

## PAPER-PER-B6 — Major
**Section:** Conclusion, first numbered item  
**Issue:** The paper claims the `0.2%` statistical floor and `0.75%` empirical threshold are both definitive sensitivity bounds, but the manuscript itself states these are different conventions and different nulls. That means the conclusion currently compresses two non-equivalent metrics into one headline without enough separation, which is a citation-forensics problem because the paper’s own supporting sections do not establish a single unified threshold.  
**Fix:** Restate the conclusion to distinguish the Fisher/statistical floor from the empirical recovery threshold, and avoid wording that implies one number subsumes the other.
