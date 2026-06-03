# P4 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round3
**Wall time**: 18.6s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=100558, completion=1140, total=101698, search_context_size=low, cost={'input_tokens_cost': 0.30167, 'output_tokens_cost': 0.0171, 'request_cost': 0.006, 'total_cost': 0.32477}

---

## PAPER-PER-B1 — Mis-cited Motloch & Pen (spin–tidal-field paper)

**Issue (MAJOR)**  
Section `\subsection{Motloch \& Pen (2021)}`: the cited paper is described as “Motloch \& Pen 2021, Nature Astronomy 5, 283, arXiv:2003.04325” which matches *“An observed correlation between galaxy spins and initial conditions”*, not “SDSS spirals with spin-direction estimates from SDSS imaging and large-scale tidal-field reconstructions (BOSS/2MRS)” as written. The description fuses elements of different spin–LSS works and is not an accurate summary of the cited paper.

**Fix**  
Change the description to match the actual Nature Astronomy paper (spin–initial-condition correlation inferred via tidal reconstruction) and remove or rephrase the BOSS/2MRS / “large-scale tidal-field reconstructions” wording unless you explicitly cite the correct companion / follow‑up paper for that methodology.

---

## PAPER-PER-B2 — Mischaracterization of CE-ResNet training labels

**Issue (MAJOR)**  
In `\subsection{CE-ResNet (Jia et al.\ 2023)}`, the table row “Training labels” says for CE‑ResNet: “GZ1 + bot‑validated”. Jia et al. (2023) describe training on Galaxy Zoo / GZ2‑like human labels and automated pipeline selections, but “bot‑validated” is not a term they use and over‑specifies their label provenance in a way that is not supported by the cited paper.

**Fix**  
Replace “GZ1 + bot‑validated” with a neutral, paper‑accurate phrase such as “Galaxy Zoo–derived labels with automated selection cuts (per Jia et al. 2023)” and, if needed, add a sentence in the text explaining exactly what label sources Jia et al. report.

---

## PAPER-PER-b3 — Overstated description of Walmsley+ 2022 / 2023 scope

**Issue (minor)**  
Sec. `\subsection{Spiral Fraction Variation Across the Sky}`: “Galaxy Zoo DESI detailed-morphology measurements of ~8.67×10^6 galaxies … report a featured-galaxy fraction ... in agreement with the present 38% spiral fraction” is broadly correct but treats “featured” as strictly equivalent to your spiral definition. Walmsley et al. (2023) are explicit that “featured” includes non‑spiral structure; the cited match is suggestive, not one‑to‑one.

**Fix**  
Qualify the comparison: e.g., “their ‘featured’ fraction (which includes but is not limited to spirals) lies at 35–40% and is broadly consistent in scale with our 38% spiral fraction, though the definitions are not identical.”

---

## PAPER-PER-b4 — Ambiguous citation of Motloch & Pen result significance

**Issue (minor)**  
Sec. `\subsection{Motloch \& Pen (2021)}` calls their signal “$\sim2\sigma$ correlation,” but the Nature Astronomy paper reports multiple statistics and the main quoted detection is closer to 3σ in some choices. The arXiv version emphasizes “marginal” rather than fixing a single σ. Your text sounds more precise than the citation supports.

**Fix**  
Rephrase to “a marginal (order‑few‑σ) correlation” or similar, or quote the exact σ interval they themselves emphasize, making clear it depends on estimator choice.

---

## PAPER-PER-n1 — Redundant / confusing dual citation years for the same Shamir 2022 DESI paper

**Issue (nit)**  
You have both `\bibitem{Shamir:2022}` and `\bibitem{Shamir:2022DESI}` for the same MNRAS 516, 2281 DESI Legacy paper, and in the main text sometimes refer to “Shamir (2022)” plus “Shamir (2022) DESI Legacy” separately. This can be read as if they are distinct works.

**Fix**  
Keep one bib entry for the DESI Legacy paper (with a single key, e.g. `Shamir:2022DESI`) and make all in‑text references to that work use the same citation key and clear descriptor (“Shamir 2022 DESI Legacy Survey paper”).

---

## PAPER-PER-n2 — Slightly misleading “independent GZ1 agreement” phrasing for CE‑ResNet

**Issue (nit)**  
Table~\ref{tab:ceresnet_compare}: the “Independent GZ1 agreement” row lists a number only for “This work” and “Not separately reported” for CE‑ResNet. As written, “independent GZ1 agreement” could be misread as you having a quantified *independent* agreement metric for CE‑ResNet and choosing not to show it, whereas Jia et al. simply did not publish that test in the paper you cite.

**Fix**  
Change the CE‑ResNet entry to something like “Not reported in Jia et al. (2023)” and, if desired, add a footnote clarifying that this metric would require running CE‑ResNet on GZ1 yourself, which is outside the scope of the cited paper.
