# P4 R-round — REAL cross-vendor — Perplexity Sonar Pro citation-chain forensic auditor

**Model**: `perplexity/sonar-pro-search` (via OpenRouter)
**Round**: 2026-05-26_R-ext-v138verify-v2_P4_v1_0_138
**Wall time**: 22.2s
**Persona focus**: Citation forensics — does each cited paper actually say what's claimed? Are arXiv IDs correct? Are titles real (not LLM-confabulated)? Are authors and journal venues correct? Use web search to verify against arXiv.org / ADS / publisher sites. Flag any fused metadata (title from one paper + arXiv ID from another).

---

**Tokens**: prompt=107278, completion=1322, total=108600

---

## PAPER-PER-B1 – Mis-cited Iye & Yagi 2026 paper scope (MAJOR)

The text cites “Iye & Yagi (2026) is anticipated… but the paper is now public as arXiv:2605.05570; we cite it here as an independent corroborating HSC-WIDE null result but do not rely on its quantitative result for any headline statistic.” (Intro/Discussion).  
At present there is no arXiv:2605.05570 entry; the ID is not valid and the title/scope are unverifiable. [1]  

**Fix (1–2 sentences):**  
Remove the concrete arXiv identifier and phrase this reference conditionally until the actual paper exists (e.g., “Iye & Yagi (in prep.) are expected to extend…”), or replace with a real, citable HSC-SSP spin-parity paper with correct arXiv/journal metadata once available.

---

## PAPER-PER-B2 – Overstated “factor of 16” vs Motloch & Pen sample size (minor)

The text states that this work’s sample is “∼16× larger” than Motloch & Pen’s sample. (Sec. 9.3 / Motloch & Pen discussion).  
Motloch & Pen use “∼2×10^5 spirals” from Galaxy Zoo 2; the present catalog has 3.20×10^6 spirals, which is about 16× larger in spirals, but Motloch & Pen’s full galaxy sample for some statistics is closer to ∼3×10^5, making the exact factor somewhat ambiguous in the literature. [1]  

**Fix (1–2 sentences):**  
Clarify that the 16× refers specifically to the spiral subsample used for the spin analysis (3.2M vs ∼2×10^5) and cite Motloch & Pen’s exact spiral count, or soften to “an order of magnitude larger (∼15–16×) in spirals” to avoid implying a precisely known ratio.

---

## PAPER-PER-B3 – Ambiguous use of CE‑ResNet catalog size (nit)

The paper states that CE‑ResNet released “∼1.95M galaxy chirality classifications across the SDSS+DESI imaging footprint.” (Intro/comparison with Jia et al.).  
The CE‑ResNet paper reports 1,953,246 galaxies in DESI Legacy pre‑imaging; the wording “SDSS+DESI imaging footprint” is slightly misleading because the final chirality catalog described in the arXiv/published version is primarily DESI Legacy–based. [1]  

**Fix (1–2 sentences):**  
Rephrase to “∼1.95M DESI Legacy galaxies” (or “DESI Legacy pre-imaging”), matching Jia et al.’s abstract and table, and avoid implying a combined SDSS+DESI catalog unless that exact data product is explicitly cited from their release.

---

## PAPER-PER-B4 – Shamir 2020 & 2022 metadata: OK but tighten wording (nit)

For Shamir (2020) the paper gives arXiv:2007.16116, SDSS DR8 + Pan-STARRS, “∼6.4×10^4 SDSS spirals plus ∼3.3×10^4 Pan‑STARRS galaxies after morphological filtering, parity‑violation multipole framing.” For Shamir (2022) it gives arXiv:2208.13866, DESI Legacy Survey, “∼1.3×10^6 input galaxies reduced to ∼2×10^5 after Ganalyzer cuts, MNRAS 516 2281.” [1][2]  
Titles, authors, journals, DOIs and arXiv IDs are all correct and the quoted sample sizes match the abstracts (Shamir explicitly says “∼6.4·10^4 SDSS” and “∼3.3·10^4 Pan-STARRS” for 2007.16116, and “nearly 1.3·10^6 spiral galaxies” for DESI Legacy in 2208.13866). The only issue is that “spiral galaxies” vs “input galaxies reduced to spirals” is mixed in the prose and could confuse readers about which numbers are raw vs spiral-classified. [1][2]  

**Fix (1–2 sentences):**  
Explicitly distinguish “input-photo sample” from “spiral-classified subsample” when quoting Shamir’s counts (e.g., “Shamir 2022 selects nearly 1.3×10^6 DESI Legacy galaxies, of which ≈2×10^5 pass Ganalyzer’s spiral cuts”), and make clear which numbers are being used in each size ratio.

---

## PAPER-PER-B5 – CE‑ResNet agreement and “state of the art” wording (minor)

The text calls CE‑ResNet “the current state of the art for unbiased chirality classification” and then says this catalog “advances beyond CE‑ResNet in three respects” (coverage, NS class, bias audits). [1]  
Jia et al. do present an architecturally equivariant CNN catalog with a global CW/CCW ≈ 0.998 balance; the “state of the art” claim is qualitative and potentially contentious without a systematic benchmark across methods, though it is not factually wrong. The “advances beyond CE‑ResNet” phrasing could be read as a general performance claim, while the details listed are actually scope/engineering improvements (sample size, explicit NS class, audit suite), not demonstrated accuracy superiority. [1]  

**Fix (1–2 sentences):**  
Qualify the language to “CE‑ResNet is a leading architecturally equivariant chirality classifier” and “our catalog extends CE‑ResNet by providing a larger DESI footprint, an explicit non‑spiral class, and a published bias‑audit suite,” avoiding an unqualified “state of the art” and explicit “advances beyond” phrasing unless backed by a direct performance comparison.
