# P1B R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-03_R-upgraded-round9
**Wall time**: 9.9s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=33806, completion=1040, total=34846, search_context_size=low, cost={'input_tokens_cost': 0.10142, 'output_tokens_cost': 0.0156, 'request_cost': 0.006, 'total_cost': 0.12302}

---

## PAPER-PER-B1 — **BLOCKER** — lines 204–210 / §3, footnote `fn:eskilt_pr3_pr4`

**Issue:** The paper says the published Eskilt & Komatsu 2022 PRD paper analyzes **Planck PR3 + WMAP9**, while the same footnote and surrounding prose claim the repo version “was subsequently updated to use **Planck PR4 / NPIPE**” and then treat those labels as the basis for the executed pipeline. That is a fused attribution: published paper vs code-repo dataset are being collapsed into one citation label.

**Fix:** Split the attribution cleanly: cite the *published paper* for the PR3+WMAP9 result and separately cite the *code repository / README* for the later PR4/NPIPE implementation. Do not describe the published Eskilt result as PR4/NPIPE unless the cited source is the repository artifact, not the paper.

## PAPER-PER-B2 — **MAJOR** — lines 208–210, 633–635, 709–711, 830–835

**Issue:** The paper repeatedly labels the birefringence result as the “published joint WMAP+Planck value” and elsewhere as “Planck PR4/NPIPE + WMAP9.” The cited paper is internally treated as both PR3 and PR4 depending on context, which is exactly the kind of citation-chain regression that will confuse readers and looks like metadata fusion.

**Fix:** Use one canonical label for the published paper’s result and one separate label for the code-repo reproduction dataset. If the PR4/NPIPE numbers come from the repo, state that explicitly and stop attaching them to the paper citation key alone.

## PAPER-PER-B3 — **MAJOR** — lines 569–573 / §4, citation `\cite{ECTorsionDESI2025}`

**Issue:** The paper cites a specific “Liu et al.” EC torsion / DESI DR2 result and claims agreement at \(0.5\sigma\) in \(H_0\) and \(0.4\sigma\) in \(\sigma_8\). This citation chain is high-risk because the paper text itself contains multiple prior reflags about a confabulated cite-key title (“ECTorsionDESI2025”) versus the actual author list and arXiv entry.

**Fix:** Inline the exact bibliographic identity in the body once: full author list, journal, year, and arXiv ID. If the cite key is shorthand, add a parenthetical with the real metadata so the reader can verify the claim without relying on the key name.

## PAPER-PER-B4 — **MAJOR** — lines 752–776 / §6, `fn:theta_backreaction` and ALP prior block

**Issue:** The spectator-ALP discussion mixes three different claims: “natural-misalignment prior” \(\theta_i\in[0.5,2]\), a “spectator-consistent” sliver \(\theta_i\sim0.1\), and a dark-energy-ALP regime “excluded from the spectator-consistency claim.” That is internally coherent as a model scan, but it is not cleanly attributed to any cited paper and reads like new model-building layered onto the literature citation.

**Fix:** Mark the fine-tuning/spectator-consistency discussion as the paper’s own inference, not literature content. Keep the cited literature limited to the published birefringence measurement and ALP model class; separate the paper’s parameter-choice interpretation into an uncited analysis paragraph.

## PAPER-PER-B5 — **minor** — lines 239–246 / Table `tab:verification`, footnote `fn:sample_stratification`

**Issue:** The sample-count arithmetic is overexplained and internally unstable across the document: 309,189 raw samples, 216,432 post-burnin, 123,368 for one subset, 123,129 in a prior draft, and a separate 119,617 “getdist-thinned” figure. This is not a citation failure, but it is a forensics smell because the paper keeps revising the same provenance chain in prose.

**Fix:** Reduce this to one authoritative count table with one provenance sentence. Keep the burn-in and thinning derivation in a reproducibility appendix only, and delete the narrative archaeology from the main text.

## PAPER-PER-B6 — **nit** — lines 883–885 / §6 and lines 1032–1037 / appendix-like ALP text

**Issue:** The paper cites LiteBIRD’s \(\sigma(\beta)\approx 0.03^\circ\) forecast as if it were a settled quoted standard, but the text does not identify the exact paper or forecast configuration. This is a metadata-completeness problem, not a substantive science error.

**Fix:** Add the exact LiteBIRD forecast citation metadata in the sentence where the number first appears, including the forecast paper title/year.
