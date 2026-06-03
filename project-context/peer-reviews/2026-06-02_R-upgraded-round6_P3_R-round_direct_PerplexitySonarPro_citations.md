# P3 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round6
**Wall time**: 18.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=79630, completion=1540, total=81170, search_context_size=low, cost={'input_tokens_cost': 0.23889, 'output_tokens_cost': 0.0231, 'request_cost': 0.006, 'total_cost': 0.26799}

---

## PAPER-PER-B1 — Mis-cited Heinrich et al. paper (major)

**Location:** Introduction, paragraph 2; Section 5; multiple references to “Heinrich et al. 2023 / Heinrich+2024” and “JCAP 2024 arXiv:2311.13082”

**Issue:**  
The paper repeatedly treats *Heinrich et al. (SPHEREx multi-tracer bispectrum)* as an already-published JCAP 2024 article with arXiv:2311.13082, and uses it as the “Heinrich+2024 anchor σ₍fNL₎ ≈ 0.7”. In reality, arXiv:2311.13082 (“Measuring fNL with the SPHEREx Multi-tracer Redshift Space Bispectrum”) is **a 2023 preprint not yet published in JCAP 2024**, and there is no JCAP 2024 volume/page metadata to match the claimed citation at the time of writing.[ ]  

**Fix:**  
Change all instances of “JCAP 2024” / “Heinrich+2024” to the correct arXiv preprint reference (“Heinrich et al. 2023, arXiv:2311.13082”) and remove or soften language that implies an already-published JCAP 2024 article, unless up‑to‑date bibliographic details can be verified and inserted.


## PAPER-PER-M1 — Ambiguous / fused referencing of Munchmeyer et al. forecast (minor)

**Location:** Introduction, last sentence of second paragraph on cosmology; Section 5 Fisher discussion.

**Issue:**  
The text cites “Münchmeyer et al. [Munchmeyer2019] consensus σ₍fNL₎ ≈ 0.4–0.9 for SPHEREx‑class surveys” while Munchmeyer et al. (Phys. Rev. D 100, 083508, 2019, arXiv:1810.13424) actually discusses *kSZ tomography / multi‑tracer LSS forecasts*, not specifically a consensus SPHEREx σ₍fNL₎ range.[ ] This “consensus σ₍fNL₎ ≈ 0.4–0.9 for SPHEREx‑class” looks like an inference or synthesis across multiple works but is attributed to a single paper, risking a fused metadata / over‑attribution.

**Fix:**  
Either (a) explicitly say this 0.4–0.9 range is a *derived comparison across several forecasts* and cite additional appropriate SPHEREx‑forecast papers, or (b) narrow the claim so that Munchmeyer et al. is only cited for what it actually contains (kSZ / LSS Fisher methodology) and re‑phrase the “consensus” language accordingly.


## PAPER-PER-m2 — Slightly misleading phrasing for Sesana/Burke-Spolaor SMBHB prior (minor)

**Location:** NANOGrav / PTA discussion, Section 5.2; references to “Sesana2016, Burke-Spolaor2019” as defining γ=13/3 SMBHB prior and log10A prior.

**Issue:**  
Sesana (2016, MNRAS 463, L6) and Burke‑Spolaor et al. (A&ARv 27, 5, 2019) are correctly cited as standard SMBHB‑background references, but the text implies a very specific combination of γ=13/3 with a log10A ~ N(−15, 0.7) prior is *directly* taken from them. In practice, the amplitude prior is a synthesis / conventional PTA choice (codified in later NANOGrav/EPTA works), not explicitly given in either of those review papers.

**Fix:**  
Clarify that γ=13/3 is the standard SMBHB spectral index motivated by Sesana (2016) and Burke‑Spolaor (2019), while the log10A ~ N(−15,0.7) prior is adopted from PTA‑analysis conventions (e.g., NANOGrav/EPTA methodology papers), and add/correct citations accordingly if you want to keep the amplitude‑prior statement.


## PAPER-PER-n1 — Inconsistent naming of “Heinrich+2024” vs reference year (nit)

**Location:** Throughout Section 5 and conclusions, e.g. “Heinrich+2024 anchor σ₍fNL₎ ≈ 0.7” vs bibliography entry “Heinrich2023”.

**Issue:**  
Text alternates between “Heinrich et al. 2023” and “Heinrich+2024” for the same arXiv:2311.13082 preprint. This is confusing and suggests two different publications when there is currently only one preprint.

**Fix:**  
Standardize all in‑text mentions to a single year matching the actual publication state (e.g., “Heinrich et al. 2023, arXiv:2311.13082”) unless and until a formal 2024 journal publication exists, in which case update the bib entry and all mentions consistently.


## PAPER-PER-n2 — Over‑specific venue metadata for Nicolaou et al. 2026 (nit)

**Location:** Introduction, survey‑history paragraph; bibliography entry Nicolaou2026.

**Issue:**  
Nicolaou et al. is cited as “Mon. Not. Roy. Astron. Soc. (2026, in press)” but as of now there is **no visible MNRAS 2026 paper matching that exact EDR/Astronomaly description** and year.[ ] This may well be a genuine “accepted / in press” manuscript, but without DOIs or at least an accepted‑manuscript arXiv version, the very specific venue+year risks aging badly.

**Fix:**  
Either (a) cite only the arXiv preprint if it exists, or (b) soften to “Nicolaou et al., submitted to MNRAS” / “in press (MNRAS), arXiv:XXXX.YYYYY” once that ID exists. Avoid hard‑coding “2026, in press” without a stable public record.


## PAPER-PER-n3 — Slightly fused language around “SPHEREx multi-tracer bispectrum” title (nit)

**Location:** Prior‑work and cosmology paragraphs describing “the SPHEREx multi-tracer bispectrum of Heinrich et al., JCAP 2024”.

**Issue:**  
The phrasing “SPHEREx multi-tracer bispectrum” is close but not exactly the arXiv title “Measuring fNL with the SPHEREx Multi-tracer Redshift Space Bispectrum” (arXiv:2311.13082). As long as this is clearly paraphrased it’s fine, but combined with calling it “JCAP 2024” it reads like a hybrid of a guessed journal title and the preprint title.

**Fix:**  
Quote the exact arXiv title at first mention, then use a shorter paraphrase (“SPHEREx multi‑tracer bispectrum forecast of Heinrich et al.”) without attaching a speculative JCAP 2024 volume.
