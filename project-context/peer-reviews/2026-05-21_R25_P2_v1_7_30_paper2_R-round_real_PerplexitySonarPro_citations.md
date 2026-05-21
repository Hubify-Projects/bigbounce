# paper2 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R25_P2_v1_7_30
**Wall time**: 9.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=30925, completion=702, total=31627

---

## PAPER-PER-B1 — MAJOR

Section: abstract and §2. The citation `Heinrich et al. 2024 \cite{Heinrich:2023}` is internally fused and likely wrong: the paper cites a 2024 forecast but uses a 2023-style key, and the surrounding claims depend on a specific `Fig. 6 / Table 3` result that must match the real author list, title, and venue exactly. Fix: replace the placeholder key with the actual bibliographic record and verify the exact forecast numbers against the publisher/arXiv record before quoting `σ(f_NL)=0.7`.  

## PAPER-PER-B2 — MAJOR

Section: §1 and appendix convention audit. The manuscript leans on a Cai-vs-Li/Brandenberger normalization story, but the arXiv metadata workup already shows how easy it is to fuse unrelated records; this paper’s bibliography needs the same hard check for every cited cosmology source because several claims are built on “real title + wrong arXiv ID” style risk. Fix: audit all reference keys against arXiv/ADS one by one and remove any source whose title, author list, or year cannot be verified exactly.  

## PAPER-PER-B3 — MAJOR

Section: §1, §2, §5, appendix A. The paper repeatedly asserts that `Cai et al. 2009` and `Cai & Brandenberger 2014` support a factor-of-two convention split, but the manuscript does not provide a traceable publication chain for the claimed normalization pipeline, and the way it is written invites a fused-metadata error between title, arXiv ID, and journal reference. Fix: cite the exact paper where each convention is defined, then separate “single time-ordering” from “commutator doubling” with explicit source lines and journal/arXiv references.  

## PAPER-PER-B4 — MAJOR

Section: §3–§4. The SPHEREx and MegaMapper forecast citations are used as if they are interchangeable survey-forecast anchors, but the manuscript mixes forecast provenance, survey status, and parameter targets in a way that needs source-level verification. Fix: for each survey claim, verify the survey description, forecast method, and reported σ(f_NL) in the original paper; do not let a generic survey citation stand in for a specific bispectrum or scale-dependent-bias result.  

## PAPER-PER-B5 — minor

Section: throughout. Several in-text citations use bare author-year shorthand (`Heinrich et al. 2024`, `Zhu & Cai 2026 echoes`, `Jolicoeur 2025`) without enough bibliographic specificity to prove the paper exists, which is exactly where LLM-confabulated titles creep in. Fix: expand each entry to a full verifiable record in the bibliography and ensure the arXiv ID, title, venue, and author list all match.  

## PAPER-PER-B6 — nit

Section: appendix A. The appendix claims a “reproducibility notebook” and “source-to-source normalization audit,” but none of that is citation-forensic evidence unless it is tied to externally verifiable papers. Fix: separate internal computation claims from external citation claims, and label internal derivations as author analysis rather than literature support.
