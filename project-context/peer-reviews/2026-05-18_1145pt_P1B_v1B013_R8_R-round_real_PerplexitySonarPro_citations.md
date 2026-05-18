# P1B_v1B013_R8 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-18_1145pt
**Wall time**: 24.8s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=17274, completion=1650, total=18924

---

## PAPER-PER-B1 — BLOCKER — Mis-cited cosmic birefringence headline result

Location: Sec. 6 “Spectator-ALP consistency check”, “Headline observational constraint” paragraph, citation `\cite{Eskilt2022b}`.

Issue: The paper attributes the joint Planck+ACT cosmic birefringence result \(\beta = 0.342^\circ \pm 0.094^\circ\) (3.6σ) to “Eskilt et al. 2022b”, but this arXiv entry and its journal metadata could not be located under that identifier or year; the title, year, and “joint Planck+ACT” description appear to be fused from multiple real works (separate Planck-only and ACT-only analyses) rather than an actual published joint analysis with those exact numbers. [1] This makes the main observational anchor for the ALP consistency test non-verifiable as cited.

Fix: Replace `Eskilt2022b` with the correct arXiv ID, year, title, and journal reference for the real joint Planck+ACT birefringence analysis that reports the quoted \(\beta = 0.342^\circ \pm 0.094^\circ\); if no such joint paper exists yet, explicitly state that the 0.342° value is an internal or re-analysis result (not a published Eskilt et al. paper), change the wording from “published” to “internal combination,” and cite only the actual Planck and ACT publications that can be verified.

---

## PAPER-PER-B2 — MAJOR — Ambiguous “quintom-B” framework citation

Location: Physics-interpretation paragraph after Table 1B (iter2 posterior), sentence: “This is the canonical quintom signature … (phantom / quintom-B).”

Issue: The paper describes the iter2 \((w_0,w_a)\) result as “the canonical quintom signature” and uses “quintom-B” language but does not give any explicit citation to foundational quintom/quintom-B dark energy papers at the point where this interpretation is made. The only nearby citation in that discussion is to DESI DR2 for data, not to theory; readers cannot easily verify that “quintom-B” is a standard framework label or that the claimed phantom-crossing interpretation matches the cited theory literature. [1]

Fix: Add explicit quintom/quintom-B theory citations (e.g., original phantom–quintom crossing papers defining this class and its \(w_0\)–\(w_a\) behavior) directly in the physics-interpretation paragraph after “canonical quintom signature” and after “quintom-B,” and check that the cited papers actually (i) define the relevant model class and (ii) associate phantom crossing \(w_0+w_a<-1\) with that class.

---

## PAPER-PER-B3 — MAJOR — Incomplete NaMaster / pseudo-\(C_\ell\) method citation

Location: Sec. 4 “Data Methods: CMB E–B Analysis”, “Pipeline configuration” paragraph, `\cite{Alonso2019}`.

Issue: The NaMaster framework is correctly named, but only a single generic reference is given and the text attributes specific implementation features (spin-2 purification, mode-coupling machinery, binning scheme) to NaMaster without precise verification that Alonso et al. 2019 is the paper that documents all these exact options and flags in the way stated. Preliminary checking shows that NaMaster has multiple related papers and documentation sources; attributing detailed implementation behavior to one reference risks over-claiming what that paper actually spells out. [1]

Fix: Verify on arXiv/publisher that Alonso et al. 2019 indeed describes the specific NaMaster options used here (spin-2 purification, `purify_b`, `purify_e` behavior, mask apodization, bandpower binning); if not, either (a) add the correct companion methods/codes paper(s) or software documentation as additional citations, or (b) narrow the claim so that `\cite{Alonso2019}` only supports what that paper demonstrably covers.

---

## PAPER-PER-B4 — MAJOR — Vague DESI torsion-paper citation

Location: “Independent cross-validation” paragraph in the cosmology section, “Liu et al. 2025” as `\cite{ECTorsionDESI2025}`.

Issue: The manuscript claims that “Liu et al. (2025) constrained an EC torsion model using DESI DR2 + Pantheon+ + DES-SN5YR + Planck 2018, finding torsion preferred by AIC (ΔAIC = −5.7 to −6.6)”, but no clearly matching arXiv ID or journal article could be located under that author/year/topic combination; the description looks like a plausible but unverified fusion of an Einstein–Cartan or torsion paper with DESI DR2 cosmology results. [1] Without a verifiable citation, the claimed external cross-validation and specific ΔAIC numbers are not auditable.

Fix: Identify the exact arXiv entry or journal article that actually carries an EC torsion analysis with the stated data combination and AIC preference; update the BibTeX entry to correct authors, title, year, and venue, and confirm the ΔAIC numbers match the cited work. If no such paper exists, remove the claim of external AIC preference and either (i) drop the paragraph or (ii) rephrase it as a projection/analogy clearly labeled as speculative, without numerical ΔAIC values or a fictitious citation.

---

## PAPER-PER-B5 — minor — Ambiguous Planck NPIPE / CamSpec reference

Location: Multiple places, e.g. Sec. 2 and Sec. 3, citing Planck 2018 parameters as `\cite{Planck2018params}` while talking about “Planck NPIPE CamSpec TTTEEE+lowl+lensing”.

Issue: The text refers to “Planck NPIPE CamSpec TTTEEE+lowl+lensing likelihoods” but uses a single `Planck2018params` citation, which typically corresponds to the 2018 base-parameters paper; the NPIPE and CamSpec likelihoods are usually documented in distinct Planck collaboration or companion papers. [1] This conflates standard PR3/PR4 parameter summaries with a specific likelihood configuration and makes it hard to verify that the exact combination used is described in the cited paper.

Fix: Add the correct dedicated NPIPE and CamSpec likelihood references alongside `\cite{Planck2018params}` wherever “Planck NPIPE CamSpec TTTEEE+lowl+lensing” is mentioned, and ensure that `Planck2018params` is only used for global parameter summaries while NPIPE/CamSpec configuration details explicitly cite their own methods papers.

---

## PAPER-PER-B6 — nit — “Planck Commander map” citation missing for birefringence context

Location: Sec. 4 “Data Methods: CMB E–B Analysis”, description of “Planck Commander CMB polarization map”.

Issue: The text uses the “Planck Commander CMB polarization map” as a key input to the NaMaster pipeline but does not attach an explicit reference where it first appears; readers must infer the Commander map citation from context or from other sections. [1] This is a small documentation gap, but it weakens citation traceability in a section that is otherwise meant to be reproducibility-focused.

Fix: Add the standard Commander-component-separation paper as an explicit citation at the first mention of “Planck Commander CMB polarization map” in Sec. 4 and any other place where Commander-specific properties (e.g., foreground cleaning) are central to the argument.
