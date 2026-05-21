# paper1a R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-21_R23_P1A_v1A_0_33
**Wall time**: 24.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=29028, completion=1576, total=30604

---

## PAPER-PER-B1 – Mis-cited cosmic birefringence “Eskilt 0.342°±0.094°”  

The paper attributes the birefringence measurement \(\beta = 0.342^\circ \pm 0.094^\circ\) to “Eskilt” and “Planck/ACT DR6 3.6σ” but gives no explicit citation key, and the value matches Minami & Komatsu’s Planck-only analysis, not an ACT DR6 paper by Eskilt. The arXiv ID and exact reference for the supposed “Eskilt” paper are not provided, and public records do not list an ACT DR6 birefringence result with those exact numbers, so as written this is at best ambiguous and at worst a fused attribution (Planck value + different author/survey tag). [1]  

**Fix (1–2 sentences):** Replace the vague “Eskilt 0.342°±0.094° observed / Planck/ACT DR6 3.6σ” language with an explicit, correct citation (e.g. Minami & Komatsu 2020 with its arXiv ID and Planck-only nature), and if an Eskilt ACT DR6 result exists with different central value or uncertainty, quote its actual numbers and cite its arXiv ID separately, making clear which dataset each number comes from.  

---

## PAPER-PER-M1 – Ambiguous use of Minami/Komatsu value as generic “Planck/ACT DR6”  

Throughout the discussion of ALP birefringence, the paper treats \(\beta \simeq 0.27^\circ\) as “consistent with published Planck/ACT DR6 3.6σ signal” and later equates \(\beta_{\rm obs} = 0.342^\circ \pm 0.094^\circ\) with that combined dataset, but the only well-known 0.342°±0.094° result is from a Planck analysis by Minami & Komatsu, not a Planck+ACT-DR6 joint measurement. [1] This renders the survey/author labeling internally inconsistent and potentially misleading about which experiment actually measured which value. [1]  

**Fix (1–2 sentences):** Clarify that 0.342°±0.094° comes from a specific Planck birefringence analysis (naming authors and arXiv ID), and, if you also want to reference ACT DR6, either (a) quote and cite its own published \(\beta\) value and significance, or (b) explicitly state that a true Planck+ACT DR6 joint analysis is not yet available and that you are only using the Planck number.  

---

## PAPER-PER-m1 – Over-precise LiteBIRD discrimination claim vs current \(\beta\)  

The conclusions section claims LiteBIRD’s \(\sigma(\beta)\approx 0.03^\circ\) would, by itself, support or refute a spectator-ALP value of \(\beta\approx 0.27^\circ\) relative to the current central value \(0.342^\circ\pm 0.094^\circ\) at a “naive 2.4σ” level, then walks this back to ~0.7σ when prior uncertainty is correctly included. This is an internal inconsistency in the quantitative interpretation of the same numbers, and the “2.4σ” sentence invites misreading even though it is later qualified. [1]  

**Fix (1–2 sentences):** Remove the “naive 2.4σ” comparison entirely and state only the statistically correct \(\sim 0.7σ\) discrepancy when combining LiteBIRD and current uncertainty, emphasizing that LiteBIRD’s main role is detecting a nonzero \(\beta\) relative to \(\beta=0\), not finely discriminating between 0.27° and 0.342°.  

---

## PAPER-PER-m2 – Missing explicit NaMaster / HEALPix citations in §VI methods paragraph  

The abstract and introduction state that NaMaster pseudo-\(C_\ell\) pipeline validation and related CMB analysis are done in a companion paper, but the new §VI methods text mentions “NaMaster pseudo-\(C_\ell\) pipeline validation” and “NaMaster methods paragraph added at §VI L427” without actually citing the NaMaster code paper or HEALPix for the underlying pixelization. The standard NaMaster reference (Alonso et al. 2019) and HEALPix reference should be present in any section that describes these tools as part of the methodology.  

**Fix (1–2 sentences):** In §VI where NaMaster and the pseudo-\(C_\ell\) pipeline are first described, add explicit citations to the NaMaster code paper (Alonso et al. with its arXiv ID) and to HEALPix, ensuring that the bibliography contains the correct titles, authors, and arXiv IDs for both.  

---

## PAPER-PER-n1 – “14-barrier” vs “13 logically-independent” wording drift  

The paper alternates between describing the constraint set as “14 barriers,” “13 logically-independent structural barriers (14 historical catalog entries),” and “the prior count of 14 retained Barrier 8 as the observational consequence of … Barrier 14; merged here under the perturbation-transparency umbrella.” These formulations are not strictly contradictory, but they are confusing and make it hard for a referee to know whether the main theorem uses 14 or 13 independent constraints.  

**Fix (1–2 sentences):** Choose one canonical phrasing early (e.g. “14 catalogued barriers, of which 13 are logically independent because B8 is the observational corollary of B14”) and then use that exact wording consistently whenever you refer to the barrier count, including in the abstract, introduction, Sec. 9, and conclusions.  

---

## PAPER-PER-n2 – Mixed “Planck-scale hierarchy” numbers in Appendix B  

Appendix B correctly notes the true cosmological-constant hierarchy \(\sim 10^{122}\) between \(\rho_{\rm Pl}\) and \(\rho_\Lambda\), but it also references earlier drafts that spoke of “\(\sim 35\)” orders and tries to reconcile this via a bounce-scale density \(\rho_\Lambda^{\rm bounce}\sim 10^{-2}M_{\rm Pl}^4\). The present text is long and self-referential in describing this correction and still leaves the exact numerical story (94 vs 92 e-folds, 120 vs 122 orders) somewhat muddy to a new reader.  

**Fix (1–2 sentences):** Collapse Appendix B’s discussion into a clean, forward-looking statement that (a) the physical hierarchy is \(\sim 10^{122}\), (b) this implies \(N_{\rm tot}\sim 90\text{–}95\) e-folds irrespective of \(\mathcal{O}(1)\) ansatz choices, and (c) previous misstatements about “\(\sim 35\) orders” were errors now superseded, without reproducing their details.  

---

If you want, I can next scan your BibTeX for specific arXiv IDs / titles that look most at risk of being fused or fabricated so you can harden those entries.
