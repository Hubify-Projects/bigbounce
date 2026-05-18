# P1B_v1B017_R13 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1430pt
**Wall time**: 24.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=18148, completion=1589, total=19737

---

## PAPER-CIT-1 — Mis-cited Eskilt joint Planck+ACT paper

The paper repeatedly cites “Eskilt 2022b” with a joint Planck+ACT value \(\beta = 0.342^\circ \pm 0.094^\circ\) at \(3.6\sigma\), but the arXiv ID and full bibliographic details are not given, and the only Eskilt paper explicitly findable in DR4 Planck context is Eskilt (2022) “Frequency-Dependent Constraints on Cosmic Birefringence from the LFI and HFI Planck Data Release 4” (arXiv:2201.13347, A&A 662 A10), which is Planck-only, not a Planck+ACT joint analysis.[1] The text attributes this 0.342° joint value and 3.6σ significance to an “Eskilt et al.” Planck+ACT paper, which does not match the author list or scope of arXiv:2201.13347 (Planck-only, single author J. R. Eskilt). The fix is to (i) provide the correct arXiv ID / journal reference for the actual Planck+ACT joint analysis that reports \(\beta = 0.342^\circ \pm 0.094^\circ\) and includes ACT data, and (ii) ensure that “Eskilt 2022b” is not pointing at the frequency‑dependence Planck‑only paper (2201.13347); if no such joint paper exists yet in the literature, then the “joint Planck+ACT value” must be rephrased as a combination derived in this work, not as a published external result.  

## PAPER-CIT-2 — Diego-Palazuelos Planck NPIPE value mis-matched to arXiv:2201.13347

Section “Data Methods: CMB E–B Analysis” cites \(\beta = 0.30^\circ \pm 0.11^\circ\) (Planck NPIPE) attributed to “DiegoPalazuelos 2022” and also uses \(\beta = 0.215^\circ \pm 0.074^\circ\) for ACT DR6 (“DiegoPalazuelos 2025”). The Planck DR4 cosmic birefringence number \(\beta = 0.33^\circ \pm 0.10^\circ\) without frequency dependence and the frequency‑dependent constraints are in Eskilt (arXiv:2201.13347, A&A 662 A10), not a “Diego-Palazuelos 2022” paper.[1] The fix: verify the exact Planck NPIPE birefringence reference (likely Eskilt 2022, not Diego-Palazuelos) and replace the “DiegoPalazuelos 2022” citation with the correct Eskilt paper for Planck NPIPE, while keeping the separate Diego‑Palazuelos citation only for the ACT DR6 analysis if that indeed exists with the quoted value.  

## PAPER-CIT-3 — ACT DR6 birefringence citation needs verification

The ACT DR6 birefringence value \(\beta = 0.215^\circ \pm 0.074^\circ\) is attributed to “DiegoPalazuelos 2025” and again in the combined \(\beta_{\rm combined}\) equation, but I cannot match this to any existing arXiv ID or 2025 journal article with that author string and ACT DR6 EB birefringence measurement; current public ACT polarization birefringence analyses are earlier and do not use that author name as first author.[1] The fix is to (i) provide the concrete reference (arXiv number, title, journal) for the ACT DR6 birefringence paper with that central value and uncertainty, and (ii) if the work is unpublished or internal, relabel it as “in preparation” or “private communication” and stop presenting it as a fully published reference.  

## PAPER-CIT-4 — “Eskilt 2022b” duplicate-year label probably inconsistent with bibliography

In Sec. 6 and elsewhere, the paper uses “Eskilt 2022b” as if there are at least two Eskilt 2022 papers (“2022a” and “2022b”), but the only explicitly identifiable 2022 cosmology paper by Eskilt in this context is the Planck DR4 frequency‑dependent birefringence analysis (arXiv:2201.13347, A&A 662 A10).[1] If no second 2022 cosmic‑birefringence paper by Eskilt exists (especially one that is joint Planck+ACT), then the “2022b” label is incorrect and will not match the BibTeX; the fix is either to (a) rename this citation simply “Eskilt 2022” pointing to arXiv:2201.13347 and not describe it as joint with ACT, or (b) if there really is a second 2022 Eskilt paper, add it correctly to the bibliography with accurate title, journal, and arXiv ID and ensure that 2022a/2022b labels match standard BibTeX ordering.  

## PAPER-CIT-5 — Potential fused metadata in ACT/Planck combination description

The text states that the “primary sky detection significance is the published Planck/ACT DR6 2.4–2.9σ” and also mentions a “joint Planck+ACT value \(\beta=0.342^\circ\pm0.094^\circ\)” attributed to “Eskilt et al.” yet refers separately to Diego‑Palazuelos for ACT DR6; this mixture of Eskilt/Diego‑Palazuelos authorship, ACT‑only vs joint Planck+ACT, and DR4/DR6 datasets suggests fused metadata from multiple different papers.[1] The fix is to decouple these: (i) one explicit citation (with correct authors, journal, arXiv) for the Planck‑only birefringence result, (ii) one for ACT‑only birefringence, and (iii) one for any truly joint Planck+ACT analysis; if (iii) does not exist, the “joint Planck+ACT” phrasing must be changed to “approximate inverse‑variance combination of Planck and ACT results” and clearly marked as an internal combination done in this work.  

## PAPER-CIT-6 — LiteBIRD birefringence forecast citation incomplete

The paper quotes a LiteBIRD forecast \(\sigma(\beta)\approx 0.03^\circ\) and cites “LiteBIRD 2023” but does not give a concrete arXiv ID or paper title; LiteBIRD forecasts appear in specific collaboration white papers and instrument design papers whose numbers differ and which might use slightly different forecast values.[1] The fix is to identify the exact LiteBIRD forecast paper that provides the \(\sigma(\beta)\) value used (e.g. a 2023 LiteBIRD science white paper) and cite it with its correct title, author list (LiteBIRD Collaboration), and arXiv ID; if the number is instead from internal notes or a conference proceeding, the text should say so explicitly rather than treating it as a refereed journal result.
