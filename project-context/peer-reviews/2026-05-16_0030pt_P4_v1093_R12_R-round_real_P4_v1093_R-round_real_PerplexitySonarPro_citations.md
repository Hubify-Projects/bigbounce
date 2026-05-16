# P4_v1093 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-16_0030pt_P4_v1093_R12_R-round_real
**Wall time**: 17.4s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=82031, completion=1059, total=83090

---

## PAPER-PER-B1 – Shamir 2022 DESI DOI

**Section/lines:** Bibliography entry `Shamir:2022DESI` and all in-text references to its DOI.  

**Issue:** The paper now cites Shamir’s DESI-spirals paper correctly as MNRAS 516, 2281, DOI `10.1093/mnras/stac2372`, arXiv:2208.13866, which matches ADS and arXiv metadata (title, author, journal, year). No fused metadata or wrong ID remain here.[1]  

**Fix:** No change required; keep the current citation block for Shamir (2022) DESI as-is.  

---

## PAPER-PER-B2 – CE-ResNet (Jia et al. 2023) metadata

**Section/lines:** Bibliography entry `Jia:2023`, multiple mentions in text (CE-ResNet sections).  

**Issue:** The CE-ResNet paper is cited as ApJ 943, 32, DOI `10.3847/1538-4357/aca8aa`, arXiv:2210.04168, with authors He Jia, Hong‑Ming Zhu, Ue‑Li Pen; this matches arXiv and publisher metadata exactly (title, authors, abstract, DOI).[0]  

**Fix:** No change required; this citation is internally consistent and non‑fused.  

---

## PAPER-PER-B3 – DESI Legacy Imaging Surveys (Dey et al. 2019)

**Section/lines:** Data section, and bibliography entry `Dey:2019`.  

**Issue:** The reference “Overview of the DESI Legacy Imaging Surveys” is given as AJ 157, 168 (2019), DOI `10.3847/1538-3881/ab089d`, arXiv:1804.08657, authors led by Arjun Dey; these match ADS and arXiv records.[1]  

**Fix:** No change required; metadata and claims about survey scope and bands are consistent with the cited paper.[1]  

---

## PAPER-PER-M1 – Tadaki et al. 2020 scope and result

**Section/lines:** Introduction, discussion of prior nulls: Tadaki et al. HSC-SSP sample and null result.  

**Issue:** The paper describes Tadaki et al. (2020) as “Spin parity of spiral galaxies II… HSC‑SSP imaging… smaller sample… null results,” which matches the actual MNRAS paper: ~80k spirals from HSC, no significant S vs Z excess.[2]  

**Fix:** No change required; title, survey, and qualitative result (“no significant difference between S- and Z‑spirals”) correctly reflect the cited work.[2]  

---

## PAPER-PER-M2 – Iye et al. 2021 reading-direction bias and duplication critique

**Section/lines:** Introduction (Iye et al. as prior null and critique of Shamir).  

**Issue:** The paper claims Iye et al. (2021) find no significant signal after correcting reading-direction bias and note duplicated photometric objects in earlier Shamir catalogs; this matches the stated aims and conclusions of “Spin parity of spiral galaxies III… SDSS spirals… 3D random walk simulations,” which documents both reading-direction bias and issues with duplicated substructures in Shamir’s samples.[3]  

**Fix:** No change required; the scope and qualitative claims about Iye et al. 2021 are faithful to the paper.  

---

## PAPER-PER-OV1 – Overall citation-chain status

**Section/lines:** All cosmology/method citations checked in this round: Jia 2023, Dey 2019, Shamir 2012/2020/2022 DESI, Iye 2021, Tadaki 2020.  

**Issue:** For this adversarial pass, every checked citation has correct arXiv ID, journal, authors, and title; where the manuscript summarizes their results (CE‑ResNet parity, DESI Legacy description, Shamir’s claimed amplitudes, Iye and Tadaki nulls), the summaries are qualitatively consistent with the source abstracts and stated conclusions.[0][1][2][3] There are no remaining clear cases of fused metadata (title from one paper + arXiv ID/DOI from another) among these key cosmology references.  

**Fix:** No correction needed at citation-forensics level for the checked papers; if you want to be maximally bulletproof before external review, the next targets to spot-check in a future round are Walmsley (Galaxy Zoo DESI), Motloch & Pen, Cahn/Slepian/Hou parity‑odd trispectrum papers, and the LSST Ivezic et al. reference.  


