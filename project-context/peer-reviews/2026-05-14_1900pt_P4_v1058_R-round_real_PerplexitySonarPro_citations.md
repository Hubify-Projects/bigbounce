# P4_v1058 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-14_1900pt
**Wall time**: 26.0s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=57330, completion=1627, total=58957

---

Based on my forensic audit of the paper's citations, here are my findings:

## PAPER-PER-B1

**Classification:** BLOCKER  
**Location:** Bibliography, Jia et al. (2023) entry; Abstract & Sec. 1 (multiple citations)  
**Issue:** arXiv ID mismatch. The paper cites `\cite{Jia:2023}` with arXiv:2211.03497, but that ID resolves to "Black holes in non-local gravity" (Buoninfante et al., gr-qc). The CE-ResNet chirality paper by Jia, Zhu, and Pen does not appear in the bibliography with a verified arXiv ID. The title "CE-ResNet: A chirality-equivariant ResNet for spiral-galaxy classification" and journal "Astrophys. J. 943, 154 (2023)" are stated but the arXiv preprint identifier is fused metadata (title from one paper + arXiv ID from another).  
**Fix:** Retrieve the correct arXiv ID for Jia et al. CE-ResNet paper from arXiv.org or ADS and update the bibliography entry. Verify the paper exists at the stated journal venue before publication.

## PAPER-PER-B2

**Classification:** BLOCKER  
**Location:** Bibliography, Shamir (2022) entry; Sec. 1, Sec. 7.1, Conclusions  
**Issue:** The Shamir (2022) bibliography entry explicitly notes in a footnote: "the prior arXiv ID 2207.11885 pointed to an unrelated optimization paper (Wang et al., 'Distributed Projection-free Algorithm for Constrained Aggregative Optimization'); removed pending arXiv verification." The paper cites Shamir (2022) multiple times (e.g., "Shamir~(2020, 2022)~\cite{Shamir:2020,Shamir:2022}") but provides **no verified arXiv ID** for the 2022 work—only a journal venue (PASJ 74, 1114 with DOI 10.1093/pasj/psac058). This violates the citation chain requirement: the arXiv ID is missing and the prior ID is known to be wrong.  
**Fix:** Locate and verify the correct arXiv preprint ID for Shamir (2022) on arXiv.org or confirm the paper exists only in the journal (PASJ) without a preprint. If no arXiv version exists, remove the arXiv citation format and cite journal only.

## PAPER-PER-M1

**Classification:** MAJOR  
**Location:** Sec. 1, Introduction; Sec. 7.1 (Shamir comparison)  
**Issue:** The paper claims Shamir (2012) reported "a $2\text{--}4\sigmaunit$ chirality dipole using $\sim\!10^4$ Sloan Digital Sky Survey (SDSS) galaxies" but the arXiv:2007.16116 abstract (Shamir 2020, not 2012) states the sample is "$\sim 6.4 \times 10^4$ SDSS spiral galaxies" and "$\sim 3.3 \times 10^4$ Pan-STARRS galaxies"—not $10^4$ total. The 2020 paper also reports ">5σ" and ">8σ" quadrupole fits, not dipole significance. The original Shamir (2012) reference (arXiv:1207.5464) is cited but not fetched here; verify the sample size and reported statistic match the claim.  
**Fix:** Clarify whether the $10^4$ figure refers to Shamir (2012) or conflates it with Shamir (2020). Quote the exact significance metric (dipole vs. quadrupole) from the original 2012 paper.

## PAPER-PER-M2

**Classification:** MAJOR  
**Location:** Sec. 1, Introduction; Sec. 7.1 (Shamir 2022 comparison)  
**Issue:** The paper states "Shamir~(2022) further claimed confirmation with DESI Legacy Survey data" but the bibliography entry for Shamir (2022) provides only a journal venue (PASJ 74, 1114) with no accessible preprint link or arXiv ID. The claim cannot be verified against the source document. Additionally, the paper later states (Sec. 7.1) "Shamir~(2022)'s spiral subset~\cite{Shamir:2022} (${\sim}200{,}000$ spirals from a ${\sim}1.3$-million total)" but this specific sample-size claim is not verifiable without access to the actual paper.  
**Fix:** Provide the correct arXiv ID or a direct journal link for Shamir (2022) so the DESI Legacy claim and sample sizes can be independently verified.

## PAPER-PER-m1

**Classification:** nit  
**Location:** Bibliography, Dosovitskiy (2020) entry  
**Issue:** The citation reads "A.~Dosovitskiy, L.~Beyer, A.~Kolesnikov \textit{et~al.}, in \textit{Proc.\ Int.\ Conf.\ Learning Representations (ICLR)} (2021) ." The year in the proceedings is listed as 2021, but the arXiv submission date is October 2020. Verify whether ICCR 2021 is the correct conference year or if this should be ICLR 2021 (which would be consistent with the 2020 preprint).  
**Fix:** Confirm the conference year matches the arXiv preprint timeline or clarify the publication history.

## PAPER-PER-m2

**Classification:** nit  
**Location:** Sec. 1, Introduction; Bibliography (Komatsu 2022)  
**Issue:** The paper cites "Komatsu:2022" for the statement "providing a window into physics beyond the Standard Model of cosmology" but the bibliography entry is "E.~Komatsu, 'New physics from the polarized light of the cosmic microwave background,' Nature Rev.\ Phys.\ \textbf{4}, 452 (2022), arXiv:2202.13919." The arXiv ID 2202.13919 is a February 2022 preprint. Verify this preprint matches the Nature Reviews Physics article (published 2022) to confirm no metadata fusion.  
**Fix:** Cross-check arXiv:2202.13919 against the Nature Reviews Physics publication to confirm they are the same work.

---

**Summary:** Two blockers (Jia arXiv ID mismatch; Shamir 2022 missing arXiv verification), two majors (Shamir sample-size/statistic ambiguity; Shamir 2022 unverifiable claims), two nits (Dosovitskiy year; Komatsu preprint–journal match). The Shamir (2022) entry is the most problematic: it is cited 5+ times in the paper but lacks a retrievable preprint identifier, making the core comparative claim unverifiable.
