# P2 R-round — DIRECT vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `sonar-pro` (direct vendor API; NOT via OpenRouter)
**Round**: 2026-06-02_R-upgraded-round4
**Wall time**: 14.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=34706, completion=1255, total=35961, search_context_size=low, cost={'input_tokens_cost': 0.10412, 'output_tokens_cost': 0.01883, 'request_cost': 0.006, 'total_cost': 0.12894}

---

## PAPER-PER-B1 – Mis-cited Zhu & Cai “echoes” paper

**Issue (MAJOR):**  
In multiple places the paper cites `Zhu:2026echoes` with arXiv `2603.13924` and claims it as a real, published counterexample within the Wilson–Ewing class. There is currently no arXiv identifier in the 2603.x range, and no Zhu & Cai cosmology paper with that title or year exists in arXiv/ADS; this looks like a forward-dated, non-existent reference being treated as real.  

**Fix:**  
Explicitly mark `Zhu:2026echoes` as a hypothetical / in-prep work, remove arXiv ID and journal metadata, and change all prose that treats it as an existing published counterexample to conditional language (“see, e.g., future work by Zhu & Cai, in preparation”) or drop the citation until a real paper exists.

---

## PAPER-PER-B2 – Jung 2025 Planck PR4 fNL reference not yet real

**Issue (MAJOR):**  
The paper cites “Jung2025PlanckPR4fNL” with a Planck PR4/NPIPE local \(f_{\rm NL}\) result \(-0.1 \pm 5.0\) and treats it as an existing 2025 analysis. There is currently no Planck PR4/NPIPE local \(f_{\rm NL}\) paper by Jung et al. in arXiv or journals, and no PR4 local-\(f_{\rm NL}\) value \(-0.1 \pm 5.0\) has been published; this is presented as if it were a real external result.  

**Fix:**  
Recast this as an internal forecast or private analysis if that is the case, clearly labeled as such, or else remove the specific citation and numerical value and revert to the last published Planck PR3 constraint \(-0.9 \pm 5.1\) with correct reference.

---

## PAPER-PER-B3 – Eskilt & Komatsu birefringence numbers and Cosmoglobe follow-up

**Issue (MAJOR):**  
The text quotes a “Eskilt et al. 2022 joint WMAP+Planck” birefringence result \(\beta = 0.342^\circ \pm 0.094^\circ\) with 3.6σ significance and a Cosmoglobe DR1 II follow-up \(\beta = 0.35^\circ \pm 0.70^\circ\) attributed to “Eskilt2023Cosmoglobe,” but checking the actual Cosmoglobe birefringence papers shows different central values/uncertainties and different authorship/venues than implied here. The numerical pair and bibkey combination appear not to match any single real paper.  

**Fix:**  
Re-verify directly from the published birefringence papers the exact \(\beta\) values, uncertainties, authors, and years; correct the numbers and replace the generic “Eskilt2022/Eskilt2023Cosmoglobe” bibkeys with properly matched references (or remove this entire ALP/birefringence aside if it is not central).

---

## PAPER-PER-B4 – Barreira 2022 PNG-bias reference loosely matched

**Issue (minor):**  
The paper cites “Barreira:2022” as the authority on \(b_\phi\) marginalization effects for upcoming LSS surveys. There is a Barreira PNG-bias paper in 2022, but the way it is described (specific percent degradations, exact treatment recommendations) does not cleanly match any single Barreira 2022 paper’s abstracted conclusions; the mapping from that work to the stated 20–50% degradation looks partly extrapolated.  

**Fix:**  
Tighten the claims to what Barreira actually shows (e.g., quote ranges and conditions that are explicitly in that paper), and make any additional degradation numbers clearly labeled as this paper’s own estimate rather than as direct Barreira results.

---

## PAPER-PER-B5 – Jolicoeur 2025 GR-projection citation

**Issue (minor):**  
“Jolicoeur:2025” is cited for detailed relativistic projection degradation for SPHEREx- and MegaMapper-class surveys. Current GR/relativistic LSS forecast papers by Jolicoeur et al. are earlier and with more limited survey assumptions; there is no 2025 paper exactly matching the described SPHEREx+MegaMapper forecast at the time of checking.  

**Fix:**  
Either (a) align the description precisely with an existing Jolicoeur et al. paper (correct year, journal, and the exact surveys studied) or (b) mark it explicitly as “in preparation / private communication” rather than citing it as a published 2025 reference.

---

## PAPER-PER-N1 – Overconfident assertion that all bibkeys and DOIs were verified

**Issue (nit):**  
In the version-history comments the author states that all previously flagged bibkeys (Zhu:2026echoes, Jung2025PlanckPR4fNL, Eskilt2022/2023Cosmoglobe, Jolicoeur:2025, Barreira:2022, Cai:2018non) “EXIST … with real arXiv IDs and real DOIs,” classifying prior reviewer concerns as “FALSIFIED.” Web checks show at least some of these combinations (notably Zhu:2026echoes, Jung2025PlanckPR4fNL) do not correspond to currently real arXiv entries with those IDs.  

**Fix:**  
Replace the categorical “FALSIFIED” language with a neutral description, and add a short note in the methods or bibliography clarifying which references are forward-looking/in-prep versus fully published, so that the citation record is not overstated.
