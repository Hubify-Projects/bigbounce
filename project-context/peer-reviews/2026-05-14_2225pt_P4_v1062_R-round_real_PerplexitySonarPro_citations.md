# P4_v1062 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_2225pt
**Wall time**: 10.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=59516, completion=688, total=60204

---

# Review

## PAPER-PER-B1
**BLOCKER**  
Section: `Conclusions` / bibliography `Shamir:2022`  
The paper’s note says the prior arXiv ID `2207.11885` belonged to Wang et al.’s *Distributed Projection-free Algorithm for Constrained Aggregative Optimization*, and the fetch confirms that is correct. The bibliography still claims the Shamir 2022 paper is canonically identified only by PASJ 74, 1114 and “arXiv search-pending,” so any residual arXiv linkage must stay removed until verified; do not silently restore the wrong identifier. [1]

## PAPER-PER-B2
**BLOCKER**  
Section: bibliography `Jia:2023`  
The paper previously attached arXiv `2211.03497` to Jia et al., but that identifier belongs to Buoninfante et al.’s *Black holes in non-local gravity*, not CE-ResNet. The current “DOI only, arXiv removed” state is the correct fix; keep it that way and do not cite or imply the wrong arXiv preprint anywhere in the manuscript. [2]

## PAPER-PER-M1
**MAJOR**  
Section: `Conclusions`, paragraph “Canonical-$N$ MASTER $\ell=1$ direct compute”  
The new closure paragraph changes the live result from the earlier analytic projection to a direct-MC artifact with a different numerical regime (`+1.85σ` vs `+0.26σ`) and a different mask fraction (`f_sky=0.494` vs `0.491`). That is a substantive methodological change; the paper must explicitly reconcile why the direct-MC number supersedes the analytic projection and why the “no primordial dipole” claim still follows from it.  

## PAPER-PER-M2
**MAJOR**  
Section: `Conclusions`, paragraph “Surviving real-cross-vendor deferrals”  
The update from “deferred” to “closed” is directionally correct, but the paragraph still reads like an audit log rather than a manuscript conclusion. Tighten it so the paper states one final canonical status for the $\ell=1$ MASTER result, instead of simultaneously narrating prior deferrals, supersession, and the leakage-floor interpretation.  

## PAPER-PER-m1
**minor**  
Section: `Conclusions`, estimator table  
The table mixes `f_sky=0.494` in the direct-MC row with `f_sky=0.4938` in the prose; that precision mismatch is unnecessary and makes the provenance look sloppy. Use one canonical value consistently, or explicitly say the table rounds `0.4938` to `0.494`.  

## PAPER-PER-n1
**nit**  
Section: bibliography `Ivezic:2019`  
The citation metadata looks fused: the title is correct for LSST reference design, but the arXiv ID `0805.2366` is old and likely not the publication record readers expect for a 2019 ApJ article. Recheck that the author/title/venue/arXiv combination is internally consistent and format it cleanly if you want to avoid another fused-metadata complaint.
