# P1B_v1B09 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-17_1030pt_P1B_v1B09_R5_R-round_real
**Wall time**: 21.3s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=13266, completion=1865, total=15131

---

## Finding 1 — Eskilt joint Planck+ACT citation mismatch (BLOCKER)

Paper location: Sec. 3 (abstract, “primary sky detection”), Sec. 4 (Data Methods), Sec. 6 (Spectator-ALP check).

Issue: The manuscript cites “Eskilt et al. joint Planck+ACT value \(\beta=0.342^\circ \pm 0.094^\circ\) (3.6σ) [Eskilt2022b]” and describes this as a published joint Planck+ACT analysis, but there is no such Eskilt-led Planck+ACT joint cosmic-birefringence paper with that value in the current arXiv/ADS literature; cosmic-birefringence analyses for Planck NPIPE and ACT DR6 are instead led by Diego-Palazuelos et al., and the only joint Planck+ACT treatment currently in the literature is also not by Eskilt with those numbers.[1] This looks like fused metadata: author string from earlier Eskilt Planck-only work plus a “joint Planck+ACT” description and central value/σ that do not map cleanly onto any single published paper.

Fix (1–2 sentences): Re-audit the source of the \(\beta=0.342^\circ \pm 0.094^\circ\) value and replace “Eskilt et al. joint Planck+ACT [Eskilt2022b]” with the correct author list, title, and bibkey of the actual joint analysis or combined constraint, or else relabel this value as an internal combination (clearly marked as “this work”) rather than as a published joint result.[1] Update all occurrences (abstract, Sec. 4, Sec. 6, Appendix/Table) to match the corrected citation.

---

## Finding 2 — Planck NPIPE and ACT DR6 birefringence references incomplete/likely mis-attributed (MAJOR)

Paper location: Sec. 4, first paragraph: “\(\beta = 0.30^\circ\pm 0.11^\circ\) (Planck NPIPE [DiegoPalazuelos2022]) and \(\beta = 0.215^\circ\pm 0.074^\circ\) (ACT DR6 [DiegoPalazuelos2025]).”

Issue: The paper attributes both Planck NPIPE and ACT DR6 birefringence measurements to “DiegoPalazuelos20xx” bibkeys, but in the current arXiv/ADS record the Planck NPIPE isotropic cosmic-birefringence analysis and the ACT DR6 birefringence analysis each have specific titles and full author lists that must be reflected correctly; there is no guarantee that the exact bibkeys “DiegoPalazuelos2022” / “DiegoPalazuelos2025” exist in your .bib as real entries matching those titles, and your text never gives titles or arXiv IDs for these references, which is a red flag in the context of an otherwise very explicit reproducibility program.[1]

Fix (1–2 sentences): Replace the shorthand “DiegoPalazuelos2022/2025” with full, correctly formatted citations including titles, full author lists (or “et al.”), and arXiv identifiers corresponding to the actual Planck NPIPE and ACT DR6 cosmic-birefringence papers, verifying that the quoted \(\beta\) values and uncertainties match exactly what those papers report.[1] If your .bib currently uses placeholder keys that do not map to real arXiv entries, rename the keys and correct the metadata to match the published papers.

---

## Finding 3 — Fujita et al. spectator-ALP model reference underspecified (minor)

Paper location: Sec. 6, opening paragraph: “The model class was previously studied by Fujita et al. [Fujita2021].”

Issue: You cite “Fujita et al. 2021” as having previously studied this spectator-ALP birefringence model, but you do not give a title or arXiv ID, and several Fujita et al. papers around 2020–2021 discuss ALP-induced birefringence with different model details and parameterizations.[1] Without an explicit arXiv identifier or title, it is ambiguous which exact work you are claiming continuity with.

Fix (1–2 sentences): Replace “[Fujita2021]” with a fully specified citation (title, journal or arXiv ID) to the specific Fujita et al. paper whose ALP model and parameter ranges you are adopting, and confirm that your claims about “previously studied model class” and natural parameter ranges match that work’s actual assumptions.[1]

---

## Finding 4 — DESI DR2 / “DESI2025DR2” reference timing and metadata (minor)

Paper location: Sec. 3 (independent cross-validation), Sec. 5 (datasets and configuration), Sec. 7 (DESI DR2 \(w_0w_a\) chain, and cross-paper discussion).

Issue: The text repeatedly cites “DESI2025DR2” and describes “DESI DR2 + Planck NPIPE + Pantheon+ + DES-SN5YR” as if DR2 and a 2025 reference are already in the literature with a stable cosmological-parameter release; however, you do not give an arXiv identifier or title, and current public DESI cosmology releases around 2024–2025 have specific naming conventions (e.g., BAO-only DR1/DR2, not necessarily a full \(w_0w_a\) cosmology paper under the generic “DESI2025DR2” tag).[1] In a citation-forensics context, that looks like fused or anticipatory metadata rather than a pointer to a concrete paper.

Fix (1–2 sentences): Either (a) replace “DESI2025DR2” with the exact published DESI DR2 cosmology/BAO paper you actually use (correct title, arXiv ID, and year), or (b) explicitly label DESI DR2 as “forthcoming / private collaboration release” and remove any implication that “DESI2025DR2” is a public, citable paper until such a paper exists.[1] In both cases, make the data provenance (public vs internal) explicit in the datasets subsection.

---

## Finding 5 — LiteBIRD forecast citation too vague (nit)

Paper location: Sec. 6, “LiteBIRD forecast” paragraph: “LiteBIRD is projected to achieve \(\sigma(\beta) \approx 0.03^\circ\) [LiteBIRD2023].”

Issue: The forecast \(\sigma(\beta)\) is plausible, but “LiteBIRD2023” is not accompanied by a concrete title or arXiv ID, and multiple LiteBIRD collaboration white papers and systematics/forecast papers exist around 2019–2023 with different forecast numbers and assumptions.[1] From a citation-forensics standpoint, the current text does not let a reader verify which specific forecast you are quoting.

Fix (1–2 sentences): Replace the vague “[LiteBIRD2023]” with a precise citation to the LiteBIRD science or forecast paper that actually contains the \(\sigma(\beta)\approx 0.03^\circ\) result, including its arXiv number and full title, and double-check that the quoted value and context (e.g., sky coverage, frequency channels) match that source.[1]

---

## Finding 6 — Internal “Golden2026P1a–P4” cross-paper entries not marked as unpublished (nit)

Paper location: Introduction (“Paper I(a) [Golden2026P1a] ... Paper IV [Golden2026P4]”), Cross-paper status table (Table 3).

Issue: The manuscript cites “Golden2026P1a”, “Golden2026P2”, “Golden2026P3”, “Golden2026P4” as if these were standard literature references, but they are internal companion manuscripts (with readiness percentages in Table 3) and not yet arXiv-posted or journal-published items; that matters for readers trying to follow up citations through ADS/arXiv.[1] As written, the bibkeys could be mistaken for established, externally citable papers.

Fix (1–2 sentences): Mark all “Golden2026P1a–P4” references explicitly as “in preparation / companion manuscript, this program” in the bibliography, and avoid phrasing in the main text that suggests they are already published external literature.[1] Optionally add arXiv IDs once the papers are actually posted and update the bib entries accordingly.
