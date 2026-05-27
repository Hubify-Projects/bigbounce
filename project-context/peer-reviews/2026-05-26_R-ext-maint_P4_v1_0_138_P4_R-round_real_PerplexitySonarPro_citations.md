# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-maint_P4_v1_0_138
**Wall time**: 25.5s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=107276, completion=1363, total=108639

---

## PAPER-PER-B1 — Shamir 2022 DESI sample size / selection

The paper claims “Shamir (2022)… DESI Legacy Survey, ∼1.3×10^6 input galaxies reduced to ∼2×10^5 after Ganalyzer cuts, MNRAS 516 2281” and later restates “Shamir 2022 DESI Legacy… nearly 1.3×10^6 spiral galaxies.” These specific numbers and description are plausible but I was not able to directly verify them because the exact Shamir 2022 DESI paper (MNRAS 516, 2281) is not available in the retrieved tool content, and the MNRAS DOI/ADS metadata (title, abstract, and sample description) were not cross-checked here line‑by‑line against the values quoted in this manuscript.[1]  
**Severity:** MAJOR  
**Fix:** Explicitly re‑cross‑check Shamir (2022) on ADS/MNRAS for: (a) the exact sample size(s) at each stage (input vs post–Ganalyzer cuts), (b) whether “spiral” is used for the final sample or just “input galaxies”, and (c) the exact wording of the abstract’s “nearly 1.3×10^6” claim; then either (i) quote the numbers exactly as given in Shamir (2022) with clear labels (“input pool” vs “spiral subsample”), or (ii) mark any inferred numbers as approximate and remove “spiral” if that term is not used in the original.

---

## PAPER-PER-B2 — CE‑ResNet citation metadata

The CE‑ResNet reference is given as “Jia et al. (2023) … ApJ 943, 32, DOI 10.3847/1538-4357/aca8aa,” with arXiv:2210.04168 and authors He Jia, Hong‑Ming Zhu, Ue‑Li Pen.[1] This matches the arXiv entry and the linked journal DOI (title, authors, venue, year, and DOI all consistent). There is no fused or incorrect metadata here.  
**Severity:** nit  
**Fix:** None required for correctness. For clarity, you could standardize the citation the first time to “ApJ 943, 32 (2023), arXiv:2210.04168, DOI 10.3847/1538‑4357/aca8aa” and then use a short form later.

---

## PAPER-PER-B3 — Shamir 2012 / 2020 arXiv + journal mapping

The manuscript cites Shamir (2012) as Phys. Lett. B 715, 25 (2012), arXiv:1207.5464, and Shamir (2020) as Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.[1] Those arXiv IDs, titles, and venues match the ADS/arXiv records, and there is no evidence of title/ID fusion or wrong DOI in the tool output.  
**Severity:** nit  
**Fix:** No change needed. If you want to tighten, you can ensure the bibliography uses a consistent style for both (journal volume, page, and arXiv ID).

---

## PAPER-PER-B4 — CE‑ResNet sample size and balance claim

You state that CE‑ResNet “released ∼1.95 million galaxy chirality classifications” and “CE‑ResNet’s catalog of 1.95 million galaxies from DESI Legacy pre‑imaging yields CW/CCW=0.998.”[1] The arXiv abstract for 2210.04168 confirms a classifier trained on SDSS with application to DESI imaging and reports a reduction of an observed 7σ human‑bias discrepancy to <1.8σ, but the exact “1.95M” DESI count and the specific 0.998 CW/CCW ratio are not spelled out in the snippet retrieved and thus not fully cross‑checked here sentence‑by‑sentence.[1]  
**Severity:** minor  
**Fix:** Verify directly from the CE‑ResNet paper or its released catalog the exact DESI sample size and the CW/CCW ratio; if the catalog is 1.953M galaxies and they quote CW/CCW=0.998, keep the numbers and add an explicit “as reported by Jia et al.”; if the numbers differ, adjust your text to match their published figures or mark them as approximate.

---

## PAPER-PER-B5 — Motloch & Pen description

You summarize Motloch & Pen (2021) as using Galaxy Zoo 2 spins and reporting a ∼2σ spin–tidal correlation.[1] The specific paper details (sample size, survey, exact significance) are not shown in the retrieved content, so I cannot independently confirm that GZ2 and “∼2σ” are exactly how the authors describe their result, though the overall characterization is qualitatively consistent with the literature.[1]  
**Severity:** minor  
**Fix:** Re‑check Motloch & Pen 2021 (ADS) for: (a) which Galaxy Zoo catalog they actually use (GZ1 vs GZ2) and (b) their quoted significance; then tighten your wording to mirror their abstract (e.g., “they report a marginal (≈2σ) correlation between galaxy spins and the tidal field using [exact dataset wording]”).

---

## PAPER-PER-B6 — LSST reference / arXiv linkage note

For LSST you cite Ivezić et al. (2019) as ApJ 873, 111, DOI 10.3847/1538‑4357/ab042c, and discuss that arXiv:0805.2366 (LSST Science Book) is not the preprint of that specific article and was removed to avoid fused metadata.[1] This is a correct and useful clarification; it matches the ADS/arXiv situation and avoids the common error of treating the science book preprint as the ApJ article preprint.  
**Severity:** nit  
**Fix:** None. The explicit “no arXiv ID here to avoid confusion” explanation is appropriate and avoids a typical title/ID fusion problem.
