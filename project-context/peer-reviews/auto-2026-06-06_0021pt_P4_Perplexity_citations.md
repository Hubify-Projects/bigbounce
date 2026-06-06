# P4 auto-2026-06-06_0021pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (19818 chars)
**Wall time**: 84.7s

---

Below is a forensic audit of the bibliography and all load‑bearing external claims in the supplied manuscript text. I focus on: correctness and consistency of citation metadata (title/author/venue/year/arXiv/DOI), detectability of quoted statistics in the cited works, and any obvious anomalies (fabricated IDs, fused entries, “in prep” ghosts, etc.). Where needed I have checked arXiv and NASA ADS.

Because the PDF is short and mostly self‑contained, there are no equations/figures I can recompute numerically here, so this report focuses on citation forensics and consistency of quoted results.

---

## 1. Bibliography and citation metadata

### P4‑E1 — Inconsistent use of “Shamir (2020, 2022)” vs numbered refs [1]–[4]  
**Type:** ESSENTIAL  
**Location:** Sec. I (Introduction, p.2), Sec. V A (p.5), References [1]–[4].

**Problem**

The text repeatedly refers to “Shamir (2012, 2020, 2022)” and associates those with specific claimed amplitudes and dipole significances:

- “Shamir (2012) [4] reported a 2–4σ dipole…”  
- “Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼ 2–4% asymmetries…”  

The bibliography lists:

- [1] “Patterns of galaxy spin directions in SDSS and Pan‑STARRS show parity violation and multipoles,” *Astrophys. Space Sci.* 365, 136 (2020), arXiv:2007.16116.  
- [2] “Analysis of the alignment of non‑random patterns of spin directions in populations of spiral galaxies,” *Publ. Astron. Soc. Japan* 74, 1114 (2022), DOI:10.1093/pasj/psac058.  
- [3] “Analysis of spin directions of galaxies in the DESI Legacy Survey,” *MNRAS* 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.  
- [4] “Handedness asymmetry of spiral galaxies with z < 0.3 shows cosmic parity violation and a dipole axis,” *Phys. Lett. B* 715, 25 (2012), arXiv:1207.5464.  

All four of these are real, correctly titled, and have correct years and venues.[1][2][3][4] However:

- The text lumps “Shamir (2022)” together, but there are two 2022 papers ([2] PASJ and [3] MNRAS).  
- In Sec. V A only [1], [3], [4] are named explicitly; [2] is never referenced in the text despite being in the bibliography.

This is inconsistent and confusing for a PRD‑level paper.

**Required fix**

- Disambiguate which 2022 paper is meant in each place by author+year+suffix, e.g. “Shamir (2022a, PASJ)” vs “Shamir (2022b, MNRAS)”, and align citation numbers accordingly.  
- Either explicitly cite [2] in the body where its results are used, or remove [2] from the reference list if it is not actually used.  
- Ensure the “Shamir (2020, 2022)” phrasing explicitly maps to [1] and [2]/[3] rather than ambiguously to “some 2022 paper”.

---

### P4‑E2 — Missing citation and justification for “Shamir’s claimed ∼3% signal”  
**Type:** ESSENTIAL  
**Location:** Abstract (p.1: “Shamir’s claimed ∼ 3% signal”), Sec. IV C (p.4), Sec. VI A (p.6), Sec. VII (p.7).

**Problem**

The manuscript asserts that “Shamir’s claimed ∼ 3% signal” is disfavored by factors of 6–12 in amplitude and is “inconsistent in amplitude” with the present null. Multiple such statements appear, but:

- None of the Shamir papers are explicitly quoted for a “∼3%” full‑sky or dipole amplitude.  
- In Shamir 2020 (*Astrophys. Space Sci.* 365, 136) and Shamir 2012 (*Phys. Lett. B* 715, 25), the abstract and main text quote per‑region or per‑azimuthal‑bin asymmetries in the range several percent to tens of percent, and various dipole fits.[1][4]  
- The current paper does not point to a specific table, figure, or equation in [1]–[4] where a “3%” dipole amplitude is defined in the same way as the present “A” parameter; the 3% looks like a rounded summary of a set of heterogeneous asymmetries.

Without a precise definition and explicit pointer (e.g. “Shamir 2012, Fig. X, N hemisphere vs S hemisphere asymmetry of 3.1%”), the “∼3%” comparator is effectively unsupported.

**Required fix**

- Identify the exact Shamir statistic being referenced (dipole amplitude, hemispheric asymmetry, or similar), give its definition, and cite the exact reference and location (section and figure/table) where it is documented.  
- Check that the 3% number is computed with the same normalization as your “A” so that ratio factors (6–12) are meaningful. If not identical, explicitly state how they differ.  
- If no well‑defined 3% quantity exists, remove the numerical factor‑of‑6–12 comparison and revert to a qualitative statement like “well above our 0.75% sensitivity threshold” with a clear, traceable value from Shamir’s paper.

---

### P4‑E3 — CE‑ResNet cw/ccw = 0.998 claim lacks precise pointer and definition  
**Type:** ESSENTIAL  
**Location:** Sec. I (p.2), Sec. V B (p.5); Reference [7].

**Problem**

The paper states:

- “Jia et al. [7] introduced CE‑ResNet … yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies.”  
- Sec. V B: “CE‑ResNet [7] achieves cw/ccw = 0.998 with architectural equivariance on 1.95 million galaxies.”

In Jia et al. 2023, *ApJ* 943, 32 (“Galaxy Spin Classification I: Z‑wise vs S‑wise Spirals With Chirality Equivariant Residual Network”), the abstract and text report:

- A chirality‑equivariant residual network applied to a Galaxy Zoo–based sample, with high accuracy.  
- However, the specific metric “cw/ccw = 0.998” is not *obviously* an accuracy; it looks like a ratio of total counts of CW to CCW galaxies, or possibly a classification balance metric. In Jia et al., the central quoted metric is classification accuracy (e.g. ~98–99%), not a cw/ccw ratio of 0.998 by itself.[7]

Thus it is ambiguous what “cw/ccw = 0.998” means, and it is not directly traceable from the abstract; the manuscript uses it as if it were an accuracy number, but the notation strongly suggests a *ratio of counts* (almost perfect 1:1 CW/CCW).

**Required fix**

- Clarify in the text what “cw/ccw = 0.998” means (ratio of counts? fraction CW? classification accuracy?).  
- Point to the precise place in Jia et al. (section or figure/table) where that statistic is defined. If Jia et al. do not explicitly use this notation, you must either:
  - derive it explicitly from their published numbers (e.g. “from Table N, the ratio of CW to CCW galaxies is 0.998”), or  
  - drop the 0.998 claim and simply quote their published performance metrics (accuracy, AUC, etc.), with correct values.

---

### P4‑M1 — Reference [2] year/venue consistent but not linked to narrative  
**Type:** MAJOR  
**Location:** Reference [2] (p.9).

**Problem**

Ref. [2] is:

- L. Shamir, “Analysis of the alignment of non‑random patterns of spin directions in populations of spiral galaxies,” *Publ. Astron. Soc. Japan* 74, 1114 (2022), DOI:10.1093/pasj/psac058.

This is a real paper with that title, journal, year, and DOI; metadata are correct.[2] However, the main text never refers to this paper explicitly—there is no “[2]” in the body, only “[1]”, “[3]”, “[4]” in the Shamir discussion.

As written, [2] is either unused (dead reference) or implicitly bundled into “Shamir (2020, 2022)” without clear mapping. That is disfavored in PRD.

**Required fix**

- Either: explicitly cite [2] where its results are actually used (e.g. in the discussion of Shamir’s later catalog work), or  
- Remove [2] from the bibliography.

---

### P4‑M2 — Cahn, Slepian, Hou parity‑odd 4PCF citation partially mis‑summarized  
**Type:** MAJOR  
**Location:** Reference ; implied earlier when situating parity‑odd galaxy statistics (though not fully visible in the excerpt).

**Problem**

Ref.  in the bibliography:

- “J. Hou, Z. Slepian, and R. N. Cahn, ‘Measurement of parity‑odd modes in the large‑scale 4‑point correlation function of SDSS BOSS DR12 CMASS and LOWZ galaxies,’ *MNRAS* 522, 5701 (2023), arXiv:2206.03625.”[4]

This metadata is correct: the title, journal, volume, page, year, and arXiv ID all match the actual paper.[1][4]

However, in conjunction with  and  (Philcox’s PRD 106, 063501) the paper is used to motivate parity‑odd large‑scale structure statistics. The Hou et al. paper finds:

- 3.1σ evidence for a non‑zero parity‑odd 4PCF in LOWZ and 7.1σ in CMASS.[1][4]

You do not quote these numbers, so there is no direct numerical mis‑statement, but the text refers generically to “measurement of parity‑odd modes” without clearly flagging that these detections may be contaminated by systematics and do not yet imply confirmed cosmological parity violation; Hou et al. themselves are cautious.[1] Given how carefully you distinguish parity‑even vs parity‑odd channels in your own work, the parity‑odd references should be equally precise.

**Required fix**

- Where you cite //, explicitly state that those works measure parity‑odd *correlation functions* with evidence at ~3–7σ, and that the interpretation (cosmology vs systematics) is still under investigation.  
- Ensure no implied claim that these are *confirmed* cosmological parity violations unless you quote the cautious language from the originals.

---

### P4‑M3 — Komatsu birefringence and Cosmoglobe citations correct but under‑specified  
**Type:** MAJOR  
**Location:** Refs. , , .

**Problem**

The references for CMB cosmic birefringence and parity‑violating physics:

-  Lue, Wang, Kamionkowski, PRL 83, 1506 (1999) — correct.  
-  Eskilt & Komatsu, PRD 106, 063503 (2022) — correct.  
-  Cosmoglobe DR1 II, A&A 679, A144 (2023) — correct.  
-  Komatsu, Nat. Rev. Phys. 4, 452 (2022) — correct.

Metadata are all fine. However, in your discussion of parity‑violating sectors (Sec. VI B) you mention constraining late‑universe morphology channels and refer to these works as exemplars of primordial parity‑violating observables. You do *not* claim any numerical bounds, so there is no numerical misquotation. But for PRD‑level clarity, readers should be pointed to which observable is used in each cited work (CMB birefringence, 4PCF, etc.) when you compare channels.

**Required fix**

- Add brief clarifying phrases like “CMB birefringence angle constraints of order 0.3°” or “parity‑odd 4PCF detection at 3–7σ” with proper references.  
- Make clear that your morphological dipole is a **parity‑even** observable and cannot be directly compared to those parity‑odd constraints without a model‑dependent transfer function (which you already state, but the link to citations should be explicit).

---

### P4‑M4 — CE‑ResNet sample size “∼1.95 million galaxies” needs explicit support  
**Type:** MAJOR  
**Location:** Sec. I (p.2), Sec. V B (p.5); Ref. [7].

**Problem**

The text says:

- “… yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies.”  
- “… our catalog … 1.6× CE‑ResNet’s scale…”

Jia et al.’s paper indeed uses a very large sample constructed from SDSS/Galaxy Zoo; the arXiv and journal versions mention a sample of order a few million galaxies.[7] But the specific figure “1.95 million” and the “1.6×” factor are not justified in the text:

- I do not see “1.95 million” stated verbatim in Jia et al.’s abstract; it is derived from text and data section and could be slightly different depending on cuts.  
- Your 1.6× factor hinges on taking your 3.2M spirals divided by “1.95M” CE‑ResNet galaxies; this needs a transparent mapping to their definition of “galaxies used for spin classification.”

**Required fix**

- Explicitly state how you computed “1.95 million” from Jia et al. (e.g., “Table N, N = 1.95×10^6 spiral galaxies passing their quality cuts”).  
- If that number is not stable across different cuts in their paper, either quote their own stated headline sample size verbatim (even if 2.0M or 1.9M) or round more conservatively (e.g. “∼2 million”).  
- Recompute the “1.6×” factor with a clearly documented denominator.

---

### P4‑N1 — Tadaki et al. catalog size “∼80,000 face‑on spirals”  
**Type:** NIT  
**Location:** Sec. I (p.2); Ref. [6].

**Problem**

The text says: “Tadaki et al. [6] … ‘a catalogue of ∼ 80,000 face‑on spirals.’”

Tadaki et al. 2020, *MNRAS* 496, 4276 (“Spin parity of spiral galaxies. II. A catalogue of ∼ 80,000 face‑on spirals”) genuinely has that title and sample size scale.[6] The quoted “∼80,000” is literally in the title and abstract, so this is correct and properly supported.

Only minor issue: your quotation marks include the tilde and number but omit “face‑on spirals” in some places; that’s stylistic, not forensic.

**Required fix**

- None mandatory. For precision, make clear you are paraphrasing the title (e.g. no full‑sentence quoting without quoting marks), but the number is correct.

---

### P4‑N2 — Galaxy Zoo and SpArcFiRe references  
**Type:** NIT  
**Location:** Refs. , , , .

**Problem**

All of these are real and correctly cited:

- Galaxy Zoo SDSS morphologies (Lintott et al. 2008, MNRAS 389, 1179).  
- SpArcFiRe (Davis & Hayes 2014, ApJ 790, 87, arXiv:1402.1910).  
- Galaxy Zoo morphology vs environment and redshift bias papers.

No numerical claims from these appear in the excerpt beyond qualitative descriptions.

**Required fix**

- None. Just ensure any numerical Galaxy Zoo bias factors you use (e.g. Hayes 2017 reports spurious winding bias) are properly referenced if you move beyond qualitative statements elsewhere in the full paper.

---

## 2. Internal numerical consistency and σ / p‑value usage

Within the excerpt, σ values and p‑values are defined as estimator‑relative, and the abstract explicitly warns that σ from different nulls are not directly comparable. This satisfies instruction (7) in your guidelines.

Where numbers can be checked for internal consistency in the excerpt, they are consistent:

- Binomial σ for CW fraction: with \(N_{\rm spiral} = 3{,}201{,}160\) and \(p \approx 0.5\), \(\sigma \approx \sqrt{p(1-p)/N} \approx 0.00028\), matching the reported ±0.000279.  
- The “9.5σ” monopole deviation for 0.4974 vs 0.5 corresponds to difference 0.0026 / 0.000279 ≈ 9.3–9.5.  
- Table II and text match on the CW fractions and σ‑values.  

Given the lack of full numerical tables and raw numbers in this excerpt, I cannot fully recompute every σ quoted (e.g. +3.64σ from a 500‑MC null), but the ones that rely only on N and p agree.

No fabricated arXiv IDs or future‑dated references are present; all arXiv numbers (2007.16116, 2208.13866, 2210.04168, 2206.03625, etc.) correspond to real papers with consistent titles and venues.[1][2][3][4][7]

---

## 3. Unsupported novelty claims

### P4‑M5 — “largest galaxy chirality catalog to date” needs explicit comparative justification  
**Type:** MAJOR  
**Location:** Sec. VII (p.7), Conclusions; implied in Abstract.

**Problem**

The paper claims:

- “We have constructed and analyzed the largest galaxy chirality catalog to date: 8,474,531 galaxies… 3,201,160 spirals.”

Prior works include:

- Shamir 2020/2022 with claims of ~1.3×10^6 spirals (per their abstracts).[1][3]  
- CE‑ResNet with “∼1.95 million galaxies” (your reading of Jia et al.).[7]  
- Tadaki et al. with ∼80,000 face‑on spirals.[6]

So a 3.2M‑spiral chirality catalog is indeed larger than these. However, the novelty claim “largest to date” should be backed explicitly by comparing to these numbers; otherwise, if any other group published a larger catalog (or a new release appears between submission and publication), the statement becomes fragile.

**Required fix**

- Add a short sentence cross‑referencing the catalog sizes from Shamir, Tadaki, and CE‑ResNet and stating explicitly that 3.2M > 1.95M > 1.3M, with references.  
- Qualify with “to our knowledge” unless you have systematically surveyed the literature. PRD often expects such novelty claims to be carefully hedged.

---

## 4. Miscellaneous citation hygiene

### P4‑N3 — Software and data references –  
**Type:** NIT  
**Location:** Acknowledgments, Software list; Refs. –.

**Problem**

All these are standard, real packages and correctly cited (Astropy, HEALPix/healpy, NumPy, pandas, PyTorch, timm, NaMaster/pymaster). No forensics issues.

**Required fix**

- None.

---

## 5. “In preparation”, versioning, and internal tags

I see no “in preparation”, “submitted”, “earlier draft”, “superseded”, or internal review‑log tags in the provided excerpt. The references are all to published or arXiv‑posted work. No future‑dated arXiv IDs or DOIs are used.

---

## 6. Duplicate / stale entries

No duplicate references are present in the visible bibliography; each numbered entry corresponds to a distinct paper. All journal names (AJ, MNRAS, PASJ, Phys. Lett. B, Phys. Rev. D, etc.) and volumes match the years, so there are no obvious stale or fused entries.

---

## Summary recommendation

**MAJOR REVISIONS**

The bibliography metadata are generally accurate and correspond to real papers with correct titles, venues, years, and arXiv/DOI identifiers. However, several core comparative claims—especially those relying on “Shamir’s claimed ∼3% signal” and “CE‑ResNet cw/ccw = 0.998 on ∼1.95 million galaxies”—are not traceable to precisely defined statistics in the cited works as currently written. There is also ambiguity in how multiple 2022 Shamir papers are referenced and at least one unused reference. For PRD’s standards, these issues must be corrected: every numerical comparison to prior work needs a clear definition and pointer to the exact table/figure/section in the cited paper, and ambiguous references (e.g. “Shamir 2022”) must be disambiguated. Once those essential and major issues are addressed, the citation layer should meet PRD rigor.

---

## PASS 2 — self-critique findings (what initial review missed)

P4‑E4 — Inconsistent / incorrect significance values and z‑scores  
**Type:** ESSENTIAL  
**Class:** A (arithmetic), E (null comparability), J (stale numbers)  
**Locations:** Sec. IV A, IV B, IV C, VI A, VII a–d, Appendix A, Appendix B, Appendix C, Appendix D, Table II, text around Tables III–IV.

**Problem**

Multiple σ and “z” values are numerically inconsistent with the adjacent numbers or with earlier definitions, and some appear to have been copied from earlier drafts and not updated:

- **Global CW fraction “Dev. (σ)” vs numbers.**  
  Table II gives for Catalog C:  
  - \(f_{\rm CW}=0.4974\), \(N_{\rm spiral}=3{,}201{,}160\), with binomial \(\sigma = 0.000279\).  
  - The deviation reported is “9.5σ”.  
  But \((0.4974-0.5)/0.000279 \approx -0.0026/0.000279 \approx -9.3\), and the sign is negative (CW deficit), not a positive 9.5σ.[Table II]  
  The text then calls this “The Catalog C residual (9.5σ from 0.5000, Table II) is spatially uniform…” without sign information, obscuring that the monopole is a **deficit** of CW, not an excess.[Sec. IV B]

- **Raw Catalog A percentages and σ.**  
  Table II:  
  - Tier A: \(0.5079 \pm 0.000279\) and “Excess = +0.79%” (correct: \(0.5079-0.5=0.0079=0.79\%\)).  
  - “Dev. = 28.8σ” implies \((0.5079-0.5)/0.000279 \approx 0.0079/0.000279 \approx 28.3\), not 28.8. The difference is small but indicates these σ values are not recomputed from the listed N and p, suggesting lingering stale numbers.[Table II]

- **“3.86× asymmetry‑suppression factor from raw +2.05% to equivariant −0.53%” is numerically inconsistent.**  
  Sec. IV B states a suppression factor of 3.86× from “raw +2.05%” to “equivariant −0.53%.”[Sec. IV B]  
  However:
  - The raw Catalog A excess is +0.79% (Table II), not +2.05%.  
  - The Catalog C monopole is −0.26% (0.4974 vs 0.5), not −0.53%.  
  - No other place reports “2.05%” or “0.53%” as the current catalog‑tier monopoles.  
  This looks like a left‑over pair of values from an earlier model or earlier catalog size: the stated ratio 2.05/0.53 ≈ 3.87 matches the quoted 3.86×, but neither 2.05% nor −0.53% match the current Table II numbers. This is a **stale, inconsistent** calculation.

- **Monopole subtraction effect description vs numbers.**  
  Appendix A(c) says:  
  - “Monopole subtraction reduces decoupled \(C_1\) at ℓ=1 from \(2.30\times10^{-5}\) to \(1.51\times10^{-5}\) (∼34%) and increases σ from +1.85 to +3.64 (the canonical‑mask number).”[App. A(c)]  
  However, Table III lists for the canonical‑N MASTER recompute (bandpowers, not the single‑mode headline): \(C_\ell\) and σ for ℓ_eff=4,…,24; there is no explicit 1.85σ there.[Table III]  
  Earlier in the main text, the canonical‑mask post‑MASTER residual is reported as +3.64σ as a **post‑monopole‑subtracted** quantity.[Sec. IV D, Table I]  
  The +1.85σ value appears only in Appendix A and is never clearly defined (pre‑ or post‑subtraction), but the text describes subtraction as simultaneously reducing \(C_1\) and *increasing* significance from 1.85σ to 3.64σ, which is counter‑intuitive and not re‑derived in the main text. This is likely a stale or mislabeled σ from an earlier configuration (different mask or bin definition).

- **Inconsistent semantics of “σ” vs “z” and Gaussian equivalents.**  
  - For the canonical‑mask residual, you state “+3.64σ (z = ∆/σ_null; empirical rank \(p_{\rm MC} = 0.030\), i.e. ≈1.9σ Gaussian‑equivalent).”[Abstract; Sec. IV D]  
  A Gaussian 1.9σ corresponds to \(p ≈ 0.057\) (two‑sided) or 0.029 (one‑sided). You appear to be using a one‑sided mapping for the Monte‑Carlo rank but a two‑sided “σ” for ∆/σ_null. This mixing of conventions is never spelled out and is confusing: 3.64σ (two‑sided) corresponds to \(p \sim 2.7 \times10^{-4}\), not 0.03.  
  - Appendix D further uses “zboot ≈ −18.1” with block‑bootstrap inflation “by 14.7×” starting from z = −264.5.[App. D(f)] The “−264.5σ” and “−18.1σ” cannot be literally interpreted as Gaussian σ‑equivalents; they are extreme χ² or WLS residuals on an over‑constrained template fit. Presenting them as σ without qualification is misleading, and they are not connected to the earlier σ definitions in Sec. IV.  

- **Joint χ²/dof value suspiciously large without cross‑check.**  
  Table III reports “Joint χ²/dof (38 bandpowers) = 161.2/38 = 4.24,” interpreted as “Dominated by mask‑coupled monopole.”[Table III]  
  A reduced χ² of 4.24 implies extreme tension under the stated null. However, this χ² is not recomputed anywhere from the listed per‑band σ values, nor is it reconciled with the statement that the monopole‑only null reproduces 99.3% of the pre‑MASTER ℓ=1 power.[Table IV] The combination of 99.3% agreement at ℓ=1 and χ²/dof ~4 over 38 low‑ℓ bandpowers suggests either:  
  - the χ² is computed under a different null than the one described in Table IV, or  
  - at least some tabulated σ’s are not consistent with that χ² (or vice versa).  
  As written, these statistics are not internally cross‑checked.

**Required fix**

- Recompute all binomial σ’s and “Dev.” values in Table II from the listed N and f; correct the Catalog C significance, including **sign**, and ensure the 9.5σ quoted in the text matches the corrected value.  
- Remove or update the “3.86× suppression from +2.05% to −0.53%” line so that it uses the current Catalog A and C monopoles (0.79% and −0.26% if those remain) and recompute the factor. Avoid mixing sign and magnitude in the “suppression factor” description.  
- Clarify in Appendix A(c) exactly which configuration yields σ=1.85 and σ=3.64, and check that the “reduces C1 but increases σ” statement is correct under your null; if not, correct the values or label them as outdated.  
- Standardize “σ” usage:  
  - use σ only for the “∆/σ_null” significance from a clearly defined null,  
  - use separate notation for Monte‑Carlo rank Gaussian equivalents and specify one‑vs‑two‑sided, and  
  - avoid quoting extreme template‑fit residuals (e.g. 264.5) as “σ” unless they are genuine Gaussian standard‑deviation units.  
- Recompute the joint χ²/dof in Table III from the actual bandpower residuals and their covariance; explicitly state the covariance model. If the χ² is evaluated against a different null than the monopole‑only null of Table IV, say so; otherwise ensure consistency.

---

P4‑E5 — Equations and probability definitions: dimensional / logical consistency gaps  
**Type:** ESSENTIAL  
**Class:** C (equations), D (cross‑ref), J (stale definitions)  
**Locations:** Eq. (2), Eq. (3), Appendix A(a,c), Appendix B(b), discussion of mask‑mean subtraction.

**Problem**

Several key equations are **almost** correct but not fully self‑consistent with the surrounding text or with usual probabilistic conventions:

- **Equivariant probabilities Eq. (2) use inconsistent symbols and missing normalization commentary.**  
  Eq. (2) defines  
  \[
  P^{\rm eq}_{\rm CW} = \tfrac12P^{\rm orig}_{\rm CW} + P^{\rm flip}_{\rm CCW},\quad
  P^{\rm eq}_{\rm CCW} = \tfrac12P^{\rm orig}_{\rm CCW} + P^{\rm flip}_{\rm CW},\quad
  P^{\rm eq}_{\rm NS} = \tfrac12P^{\rm orig}_{\rm NS} + P^{\rm flip}_{\rm NS}.
  \]
  written with mismatched ½ factors and a stray  symbol, but more importantly, the CW/CCW lines as printed lack explicit ½ before the second term (the layout suggests “½ P_orig + P_flip” instead of “½(P_orig + P_flip)”).[Eq. (2)]  
  From context, you clearly intend  
  \[
  P^{\rm eq}_{\rm CW} = \tfrac12\big(P^{\rm orig}_{\rm CW} + P^{\rm flip}_{\rm CCW}\big),
  \]
  etc., so that total probability remains normalized. As typeset, the equations are ambiguous and dimensionally inconsistent (one term halved, the other not).  

- **Asymmetry map definition vs mask‑mean subtraction and NaMaster field.**  
  - In Sec. IV C, you define \(A_p = (N_{\rm CW}^{(p)} - N_{\rm CCW}^{(p)})/(N_{\rm CW}^{(p)} + N_{\rm CCW}^{(p)})\).[Eq. (3)]  
  - In Appendix A(a), you state: “The asymmetry field is \(A_p = (N_{\rm CW}^{(p)} - N_{\rm CCW}^{(p)})/(N_{\rm CW}^{(p)}+N_{\rm CCW}^{(p)})\) (spirals only). The quantity \(N_{\rm map,weighted} = \sum_p W_p\) …” and then “The depth weighting does not introduce a monopole–dipole coupling because the galaxy‑weighted mask‑mean \(\langle A\rangle_{\rm mask,gw}\) is subtracted before field construction.”[App. A(a)]  
  But the formula for \(A_p\) in Appendix A(c) immediately after is written as  
  \[
  A_p = (N_{\rm CW}^{(p)}-N_{\rm CCW}^{(p)})/N_{\rm total}^{(p)},
  \]
  i.e. dividing by all galaxies (spiral + NS) rather than CW+CCW only.[App. A(c)]  
  These are **different normalizations**. One uses spirals as the denominator (as in dipole analysis; Eq. 3); the other uses all classified galaxies as the denominator (as in mask weighting). The text asserts that “The field is scalar (spin‑0) asymmetry map \(A_p=\dots\) with galaxy‑weighted mask‑mean subtraction,” but never clearly reconciles the CW+CCW denominator with the use of \(N_{\rm all}\) in the weight map and in the later definition. This creates ambiguity:  
  - Are your reported \(C_\ell\) and dipole amplitude A defined for spirals only, or diluted by NS counts?  
  - The detection threshold “A=0.75%” should be tied to one specific definition (spiral‑only); mixing in NS in the field definition changes the effective amplitude.  

- **Monopole subtraction and “ℓ=0 removed before MASTER” vs generative null.**  
  Appendix A(a) says the monopole is subtracted at field construction, so ℓ=0 is absent from the MASTER matrix and cannot leak into ℓ=1.[App. A(a)]  
  But Sec. IV D’s generative monopole‑only null intentionally uses a field **without** monopole subtraction to demonstrate leakage.[Sec. IV D] This is correct conceptually, but the document never explicitly states that all headline MASTER numbers (Table I and the −0.122σ) come from the monopole‑subtracted pipeline, whereas the 99.3% reproduction in Table IV comes from the non‑subtracted pipeline.  
  As written, it is possible to misread Appendix A as implying that all analyses use monopole subtraction; in that case, a “monopole‑only” generative field would trivially have zero signal at ℓ≥1, contradicting Table IV. This is more a documentation inconsistency than a physics error, but it affects reproducibility.

**Required fix**

- Rewrite Eq. (2) with unambiguous parentheses and identical ½ factors on both terms for each class; verify that all three probabilities still sum to 1 and state this explicitly.  
- Unify the field definition for \(A_p\): pick either \(A_p = (N_{\rm CW}-N_{\rm CCW})/(N_{\rm CW}+N_{\rm CCW})\) (spirals only) or the all‑galaxies denominator, and propagate that choice consistently through Sec. IV C, Appendix A, Table III, and the injection‑recovery description. If the denominator differs between the cosmological estimator and the NaMaster field, state this clearly and justify why it does not bias the null.  
- Make explicit in Appendix A(a) that the **headline MASTER results** use the monopole‑subtracted field (ℓ=0 removed), whereas the monopole+mask generative null in Sec. IV D uses a separate, non‑subtracted field to expose leakage. Cross‑reference the two pipelines to avoid confusion.

---

P4‑M6 — Null‑procedure comparability still violated in several juxtaposed σ claims  
**Type:** MAJOR  
**Class:** E (null procedure comparability)  
**Locations:** Abstract; Sec. III A; Sec. IV C–D; Sec. VI; Sec. VII(a,b); Appendix C; Table I; text describing “disfavors by factor ∼6–12.”

**Problem**

You correctly state in the abstract and Sec. IV that “σ values … are defined relative to their respective null procedures and are not directly comparable.”[Abstract; Sec. IV] However, several later passages **compare σ’s across distinct nulls without reiterating this qualifier** and sometimes implicitly use them as if they were commensurate:

- Sec. III A lists a hierarchy: real‑space dipole (+0.43σ, isotropic bootstrap), MASTER ℓ=1 (−0.122σ, pixel‑shuffle null), canonical MASTER (+3.64σ, pixel‑shuffle null), hemisphere LEE (max‑stat MC), monopole‑mask null (+1.68σ), and injection floor at A=0.75%.[Sec. III A; Table I] These are presented in a single summary table and bullet list without reminders that each σ is under a different null.  
- Sec. VI states “The raw Catalog A dipole (2.31σ real‑space; +6.48σ pre‑MASTER) demonstrates that a classifier bias of only 0.79%… produces highly significant but entirely spurious dipole signals.”[Sec. VI] The 2.31σ comes from the real‑space bootstrap null; 6.48σ comes from a pre‑MASTER pseudo‑Cℓ null (not fully described). They are juxtaposed as if they were jointly characterizing one effect, without noting that their σ scales are different.  
- In VII(a–d) you narrate: “+3.64σ… The present null disfavors the Shamir ∼2–4% detection class at the amplitude level,” and also “The raw (Catalog A) analysis produces a 2.31σ real‑space dipole and a +6.48σ pre‑MASTER pseudo‑Cℓ… Equivariant post‑processing collapses … to 0.43σ; MASTER… to −0.122σ.”[Sec. VII(a–d)] The chain “2.31σ → 0.43σ” and “6.48σ → −0.122σ” implicitly treats these σ’s as comparable scales.  
- In Appendix C, the hemisphere look‑elsewhere test gives “maximum asymmetry 3.05σ” (over many directions), “p_LEE ≤ 10−4,” and that Bonferroni/BH reduces significance to “<1σ.”[App. C(c)] None of these σ’s tie back to the null types in Table I, and they are casually compared to the canonical 3.64σ in the main text.

**Required fix**

- In key narrative comparisons (Sec. VI and VII), avoid statements like “2.31σ → 0.43σ” or “6.48σ → −0.122σ” without explicitly re‑stating the nulls; instead describe changes in **amplitudes** (e.g. change in fitted dipole A) and only then mention the separate σ’s under their own nulls.  
- In Table I, add a short column or footnote explicitly reminding that σ columns are not directly comparable and refer to the specific null type (bootstrap, pixel‑shuffle, generative, max‑stat MC).  
- In Appendix C and D, when a σ is introduced, explicitly tie it back to “moment‑ratio under per‑pixel label‑shuffle null” or “max‑stat MC null” and avoid using those σ’s side‑by‑side with the headline −0.122σ unless you stress the different nulls again.

---

P4‑M7 — Abstract and conclusion contain claims not fully supported by body with precise quantitative mapping  
**Type:** MAJOR  
**Class:** F (abstract faithfulness), H (unquantified hedges)  
**Locations:** Abstract; Sec. VI B; Sec. VII(a,d).

**Problem**

A few abstract/conclusion statements are broader than what is strictly demonstrated in the body, or they use qualitative hedges without giving the supporting numbers:

- **“Sub‑percent sensitivity… empirical 50%-recovery‑at‑3σ threshold at |A_dipole|≥0.75%”** is stated early.[Abstract; Sec. III A; Sec. VI A]  
  Sec. VI A gives the injection‑recovery result on the **HC‑spiral subsample** (471k galaxies), not the full 3.2M spirals.[Sec. VI A] The extrapolation to “the present null disfavors any model predicting late‑universe morphology‑channel dipole ≥0.75% on the DESI footprint” implicitly applies the HC‑sample sensitivity to the full catalog. This is reasonable, but the abstract does not clearly state that the injection‑recovery is validated only on a smaller, higher‑purity subset; the sensitivity on the full, noisier population may differ.  

- **“Disfavors Shamir ∼2–4% detection class by a factor ∼6–12”** appears multiple times.[Abstract; Sec. VI B; Sec. VII(a)]  
  You now quantify detection **threshold** (0.75%) and mention Shamir’s amplitudes qualitatively, but the text still lacks one explicit worked example: e.g., “Shamir’s hemispheric asymmetry ~3% (as defined in [ref] with denominator X) corresponds to A=Y in our normalization; our 3σ threshold is 0.75%, thus the ratio is…”. As a result, “factor of ∼6–12” is still not concretely tied to a specific Shamir statistic or to your A definition, and remains a somewhat hand‑waving amplitude comparison.

- **Parity‑violating sector mapping remains qualitative.**  
  Sec. VI B and the abstract carefully state that the ℓ=1 chirality dipole is parity‑even and “not a direct parity‑violation test,” which is good.[Abstract; Sec. VI B] However, the conclusion lines “disfavors any model predicting a late‑universe morphology‑channel dipole ≥0.75%… including the Shamir ∼3% amplitude class” could be misread as competitive with CMB birefringence or parity‑odd 4PCF constraints. The body does not supply any explicit mapping or numerical comparison to those other channels (e.g. constraints on parity‑odd 4PCF amplitudes at 3–7σ).[Refs. 17–21]  

**Required fix**

- In the abstract and Sec. VI A, explicitly state that the injection‑recovery sensitivity of A≈0.75% is measured on the **HC‑spiral subsample** and that extension to the full catalog relies on the assumption that classification noise scales as estimated in Sec. VI A and Appendix E.  
- For the “factor ∼6–12” claim, either:  
  - provide one explicit Shamir statistic (with a citation to a figure/table/section) and show the conversion to your A, then compute the ratio numerically, or  
  - soften the language to “well above our 0.75% sensitivity floor” without quoting a numerical factor.  
- In the conclusion paragraphs that mention parity‑violating sectors, add one clarifying sentence that your bound is on a **parity‑even morphology dipole only**, and cannot be directly translated into constraints on parity‑odd 4PCF or CMB birefringence without an explicit model.

---

P4‑m8 — Minor internal cross‑reference and wording inconsistencies  
**Type:** MINOR  
**Class:** D (cross‑refs), J (stale wording)  
**Locations:** Sec. II B; Sec. IV A; Sec. V A/B; Appendix E; Data‑availability section.

**Problem**

A few references and phrasings appear inconsistent with the current numbers or pipeline:

- Sec. II B: “Note: 67.6% of training labels derive from CE‑ResNet predictions” and “26,636 images (80/20 split).”[Sec. II B] Later, Appendix B reports three‑class accuracy 93.7% (with augmentation) and 94.9% (post‑hoc) and binary CW/CCW 93.2%.[App. B(a)] None of these are explicitly used to recompute the “GZ1 accuracy floor 69.91%” or the “g ≈ 0.398” dilution factor in Sec. VI A; the reader must infer that 69.91% comes only from the GZ1 cross‑match, not from the full training set. Explicit cross‑reference (“as in Sec. II B, 69.91% is from the disjoint GZ1 test, not the CE‑ResNet‑based training set”) would avoid confusion.  
- Sec. V B: “Our Catalog C achieves 1.6× the spiral coverage with cw/(cw+ccw)=0.4974±0.0003…”[Sec. V B] This 1.6× factor uses the 1.95M CE‑ResNet figure that is not explicitly demonstrated from Jia et al.; you already flagged this as P4‑M4 in your first review. With the updated catalog size 3.201M spirals, the ratio is precisely 3.201/1.95 ≈ 1.64; if the sample size in Jia et al. is revised or rounded (~2.0M), this ratio changes and should be recomputed.  
- Data‑availability and Acknowledgments sections repeat “69.91% agreement, κ=0.40” without explicitly cross‑referencing Sec. II B, which might lead a reader to wonder whether this is an *evaluation* on the production catalog or only on the disjoint GZ1 subset.  

**Required fix**

- Add explicit cross‑references: when citing the 69.91% accuracy floor, always point back to Sec. II B / Appendix E where the GZ1 cross‑match is defined.  
- Reconfirm the CE‑ResNet sample size from Jia et al. and either (i) show how 1.95M is obtained, or (ii) adjust both the denominator and the 1.6× factor consistently.  
- Where catalog‑wide performance is discussed in the conclusions or data‑availability section, clarify that the 69.91% is the GZ1 cross‑match accuracy, not a full‑catalog self‑evaluation.

---

If you need, I can next go systematically through one table at a time (Tables I–IV) and explicitly recompute every σ and ratio with suggested corrected numbers.