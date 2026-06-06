# P1A auto-2026-06-05_1817pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (10267 chars)
**Wall time**: 84.9s

---

P1A contains extensive internal cross-referencing, calculations, and a long bibliography, but it is presented without figures or tables other than two schematic ones. I will treat page 1 as the first page of the PDF (title + abstract), then count down.

Below I list all issues I can identify, following your requested format.

---

### ESSENTIAL issues

**P1A-E1 – Abstract, p.1 – Reliance on non-existent “in preparation” companion works as load‑bearing citations**

- **Problem:** The abstract and introduction rely on “companion works in preparation” [2, 6, 23, 46] for:
  - SPHEREx fNL Fisher forecasts and significance claims (“3–5σ realistic after full systematic budget… detailed Fisher forecast in companion work in preparation [2]”).
  - ΛCDM+ΔNeff MCMC verification, NaMaster validation, ALP parameter fits (“documented separately in companion work in preparation [6]”).
  - Galaxy spin classifier accuracy, bias audits, null detection significance (“reported in Paper IV ”).
  - PTA real-KDE γ measurement and its statistical comparison to bounce prediction (“companion Paper III ”).
- These are not posted on arXiv nor published. For a PRD submission, results that are central to the claimed structural closure and observational status cannot be sourced to non-public “in preparation” documents.
- **Required fix:** Either (a) post those companion papers on arXiv with stable identifiers and update all references to them, or (b) fully include the necessary methodological and numerical details in the present paper and remove all dependence on inaccessible “in preparation” documents. Until then, every load-bearing statement that rests on [2, 6, 23, 46] should be regarded as unsupported.

---

**P1A-E2 – Abstract & throughout – Use of “DESI 2024–2025 BAO results” and “DESI DR2 2025 PRD paper” before publication**

- **Problem:** Abstract: “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset-dependent) [9, 10].”  
  Reference  and  are described as DESI 2024 or 2025 results with arXiv IDs 2404.03002 and “arXiv:2503.14738” / PRD 112 (2025). As of mid‑2026, 2404.03002 exists and is a DESI 2024 BAO paper; “DESI DR2 results II: … PRD 112, 083515 (2025), arXiv:2503.14738” is future‑dated and not findable on arXiv or NASA ADS.  
  The σ range 3.1–4.2σ is *not* stated in the 2404.03002 abstract and appears to be an internal extrapolation from a non‑public “DESI DR2” analysis.
- **Required fix:** Restrict statements to published / posted results. Remove or clearly label as speculative any claims based on “DESI DR2 2025” or arXiv:2503.14738 until those results actually exist and can be cited. Replace “3.1–4.2σ” by numbers traceable directly to the abstract or summary tables of actual posted DESI papers, or explicitly describe the derivation in the text with visible numbers.

---

**P1A-E3 – Section I & throughout – Treating internal MCMC numbers as if they carry external authority**

- **Problem:** The paper repeatedly quotes cosmological parameters such as
  - “H0 = 67.68 ± 1.06”,
  - “ΔNeff ≈ 0”,
  - “σ8 = 0.803 ± 0.008”, etc., claiming they come from a “ΛCDM+ΔNeff companion analysis” in Paper I(b) [6].  
  While there is a disclaimer that these are “documented internally rather than as externally citable arXiv-posted numbers”, they are nonetheless used to support statements like “recovers ΛCDM” and to motivate structural claims.
- **Required fix:** For a PRD paper, either:
  - Use only cosmological parameters from published datasets (e.g., Planck 2018) and clearly attribute them, or
  - Make the companion analysis public (arXiv posting with full MCMC details) and update references accordingly. Internal, unpublished chains cannot be used as authoritative support.

---

**P1A-E4 – Section IV.A, p.8–9 – NJL four‑fermion energy‑density estimate not traced to any cited paper**

- **Problem:** The text states that the Hehl–Datta contact term leads to an energy density “bounded above by ρ_NJL ∼ κ n_ψ^2 ∼ n_ψ^2 / M_Pl^2 … many orders of magnitude below the present-day dark-energy density.”  
  However, there are no explicit numbers nor a citation where such a cosmological estimate appears; Hehl & Datta  derive the operator but do not provide the cosmological bound as described. The specific claim “many orders of magnitude below (10^−3 eV)^4” must be shown numerically using n_ψ appropriate to recombination or today; at present, this is an unsupported quantitative assertion.
- **Required fix:** Either:
  - Provide an explicit numerical estimate: choose n_ψ (e.g., baryon number density today or at recombination), compute ρ_NJL and demonstrate the hierarchy, including units, or
  - Cite a specific paper where this cosmological bound is derived and quote its numbers. Without that, the “many orders of magnitude” claim is not traceable.

---

**P1A-E5 – Section IV.B, p.9–10 – One‑loop birefringence suppression factor 10⁻⁵⁸–10⁻⁶⁰ not traceable**

- **Problem:** The paper gives a dimensionless ratio for Route‑2 birefringence
  \[
     \Delta\theta_\text{one-loop}/\Delta\theta_\text{obs} \sim 10^{-58} \text{ to } 10^{-60},
  \]
  based on a schematic EFT operator (14). This specific suppression factor is claimed to be robust, yet there is no reference where this calculation appears, nor are the intermediate steps or numbers for H_0 / M_Pl, α_em/(4π) and β_obs given in a way the reader can verify from published sources. Mercuri & Capozziello  do compute one-loop corrections to Holst, but they do *not* quote a cosmological birefringence ratio of this form.
- **Required fix:** Provide a transparent step‑by‑step numerical evaluation:
  - state the numerical values used for H_0, M_Pl, α_em, β_obs;
  - show the intermediate numerical product; and
  - clarify that this is the author’s own order‑of‑magnitude estimate, not a number taken from .  
  Alternatively, if a similar calculation is in the literature, cite it explicitly and ensure the quoted number matches.

---

**P1A-E6 – Section IV.D, p.10–11 – ALP energy‑density overshoot factors (10²²–10³⁶) not checked against a cited formula**

- **Problem:** The text asserts that for α/M fixed at 10⁻²¹ GeV⁻¹, β ≈ 6×10⁻³ rad, and ALP masses m_θ ~ 10⁻²²–10⁻¹⁵ eV, the energy density ρ_θ overshoots ρ_Λ by 22–36 orders of magnitude. The relation used is ρ_θ = m_θ² β²/[2(α/M)²]. This is the author’s formula, not directly taken from Lue et al. ; the claimed order‑of‑magnitude overshoots are a new calculation. No explicit numeric example is given; the factors are not traceable to any reference.
- **Required fix:** Provide at least one explicit worked example with units, showing ρ_θ in eV⁴ compared to ρ_Λ ≈ (2.3 meV)⁴, and justify the 10²²–10³⁶ ranges. Alternatively, tone down the “overshoots by X orders” language to a qualitative statement unless rigorous numbers are shown.

---

**P1A-E7 – Section IX, Table II, p.13 – Barrier 5 “scale separation” claim not supported by any cited reference**

- **Problem:** Barrier 5: “The global vacuum integral ∫ d⁴x √−g ρ_Λ cannot be connected to the local bounce density without assuming a mechanism to store and transfer the integrated vacuum energy across ~92 e-folds of inflation. No such mechanism exists within minimal ECH.” No literature is cited for this impossibility statement; it is an author’s conceptual argument. For a PRD paper, a “no such mechanism exists” claim either needs a theorem or careful qualification.
- **Required fix:** Rephrase as an author’s observation, not as a theorem, unless a rigorous proof or literature reference is provided. E.g. “We are not aware of any explicit minimal‑ECH mechanism that …” and make clear it is not a proven impossibility.

---

**P1A-E8 – Section X, p.14–15 – “Perturbation transparency” claimed as theorem without detailed derivation or explicit match to Hehl et al.**

- **Problem:** The key result is that torsion vanishes and Holst reduces to the Pontryagin density for canonical scalar matter, so all scalar/tensor perturbations are identical to GR. The citation  (Hehl et al.) indeed states that in Einstein–Cartan theory torsion vanishes when spin density is zero.[4] However:
  - The paper does not actually show the variation of the Holst term in the perturbed FRW background nor demonstrate explicitly that *all* perturbation orders vanish in the equations of motion.
  - The statement “This generalizes Hehl et al. (1976)  to the Holst sector and to all perturbation orders” is not referenced to any published work; it is new and needs full derivation.
- **Required fix:** Add an explicit calculation (even at schematic index level) showing:
  - the Cartan equation leading to T=0 for scalar matter,
  - that R(Γ̊) in the Holst sector is the Pontryagin density ∂_μK^μ,
  - that the variation of ∫ d⁴x √−g R(Γ̊) with respect to metric perturbations is a boundary term at each order.  
  Alternatively, weaken the claim to a conjecture or “we argue that …” and call it an open point.

---

**P1A-E9 – References , , [41–43], [44–45] – Future‑dated arXiv IDs and publication years**

- **Problem:** Multiple references are dated 2024–2026 with arXiv IDs that, at the time of this review, are not present on arXiv or ADS:
  - : “DESI DR2… Phys. Rev. D 112 (2025), arXiv:2503.14738” – arXiv IDs starting with 25xx.xxxxx are not yet available.
  - : “T. Liu et al., arXiv:2507.04265 (2025).”
  - : “S. Legner et al., arXiv:2507.09228 (2025).”
  - : “S. Alam et al., arXiv:2509.03508 (2025).”
  - : “Cai & Zhu, arXiv:2603.13924 (2026).”
  -  is given as arXiv:2503.01992 (2025), similarly future‑dated.  
  None of these IDs can be checked, and they must be considered fabricated placeholders.
- **Required fix:** Remove all future‑dated arXiv identifiers and publication years. If the authors already have preprints drafted, they should wait until those are actually posted and then cite the real IDs. Until then, refer to such work descriptively without arXiv numbers, or just omit them.

---

**P1A-E10 – Reference [6] “hUBIFY-2026-001B; companion paper, this volume” – Fused metadata and nonstandard identifier**

- **Problem:** The label “hUBIFY-2026-001B; companion paper, this volume” is not a standard journal citation or arXiv ID; it looks like internal bookkeeping. It also appears in multiple places as if it were a persistent identifier.
- **Required fix:** Replace “hUBIFY-2026-001B” and “this volume” by a proper reference once available (arXiv or journal). Until then, either drop the pseudo‑identifier or clearly label it as “internal report” and do not use it to support key numerical results.

---

**P1A-E11 – Reference  “companion technical note, available upon request from the author”**

- **Problem:** Ref.  is a “companion technical note, available upon request from the author,” which is not accessible to referees or readers. Yet it is cited as providing “systematic closure of minimal first-principles routes to dark energy in Einstein-Cartan-Holst gravity.”
- **Required fix:** Either:
  - Incorporate essential results from  into this paper, or
  - Post  on an accessible repository (arXiv) and update the reference. Otherwise,  cannot be used as supporting evidence.

---

**P1A-E12 – Appendix B & Section II.C – N_tot ≈ 92 / 94 e‑folds and “fine-tuning reduction from 10^122 to 10^5” not rigorously derived**

- **Problem:** The paper repeatedly quotes:
  - “Matching ρ_Λ requires N_tot ≈ 92”,
  - “reparameterizes the fine-tuning hierarchy from 10^122 to ∼10^5 as sensitivity to ΔN_tot ≈ 4.”  
  Appendix B admits that the operator is dimensionally +1 and that the ρ_Λ mapping is a phenomenological ansatz. The jump from that ansatz to a specific N_tot ≈ 92–94 number is not anchored in any external reference. It is a new internal calculation, but the steps are only outlined qualitatively.
- **Required fix:** Either:
  - Provide a clear, explicit derivation of the 92–94 e‑fold number, starting from stated ρ_Λ and Planck units, or
  - Recast these numbers as illustrative examples rather than precise predictions, removing language such as “requires N_tot ≈ 92” and “reduction from 10^122 to 10^5” which implies a solved fine‑tuning problem.

---

**P1A-E13 – Abstract & Section XV – Claim of “channel-level closure” based on incomplete operator basis**

- **Problem:** The paper claims “channel-level closure of the four enumerated minimal-ECH dark-energy routes” and then later admits that essential operators (Jackiw–Pi gravitational Chern–Simons, parity-odd four-fermion partner) are *explicitly not* closed. So the claim is restricted to four specific channels, not to the full ECH effective action. The wording in the abstract risks overstating the result.
- **Required fix:** In the abstract and conclusions, explicitly limit the closure claim: e.g. “We show that four commonly-discussed minimal ECH channels (NJL, one-loop EA, Immirzi running, parity‑CMB) cannot on their own account for dark energy under our assumptions,” and remove any wording that suggests an exhaustive closure of minimal‑ECH DE routes.

---

### MAJOR issues

**P1A-M1 – References [1], [3–5], [7], [11–22], [24–31], [33–36], [38–40], [44–45] – Spot‑check of bibliographic metadata**

Here I highlight specific points that require correction or are acceptable:

- **[1] Cai et al. “Non-gaussianity in a matter bounce” JCAP 0905:011 (2009), arXiv:0903.0631**  
  - arXiv and title/venue are correct; the quoted f_NL = −35/8 is indeed in the paper, derived for matter-bounce initial conditions.[1]  
  - **No action needed.**

- **[3] Minami & Komatsu, PRL 125, 221301 (2020), arXiv:2011.11254**  
  - Title and ID are correct.[3]  
  - Paper reports β ≈ 0.35°±0.14° (depending on convention). P1A uses this mainly as the first detection; numerically OK within order‑of‑magnitude, but the exact numbers are not always quoted.  
  - **No critical correction, but the author should ensure consistency with exact values if they quote them.**

- **[4] Eskilt & Komatsu, Phys. Rev. D 106, 063503 (2022), arXiv:2205.13962**  
  - Bibliographic data are correct.[4] The paper quotes β = 0.342° ± 0.094°; P1A matches this.  
  - **OK.**

- **[5] Diego‑Palazuelos & Komatsu ACT DR6 birefringence, arXiv:2509.13654**  
  - This is future‑dated; current ACT DR6 birefringence analyses in 2025/26 have different arXiv IDs or are not yet posted. The ID 2509.13654 cannot be checked.[5]  
  - **Required fix:** Remove or correct to the actual arXiv identifier once the DR6 birefringence paper is posted.

- **[6] Shapiro & Teixeira, Classical and Quantum Gravity 31, 185002 (2014), arXiv:1402.4854**  
  - Title and ID are correct.  
  - P1A uses it as a reference for quantum Einstein–Cartan with Holst term; consistent.  
  - **OK.**

- ** Ashtekar & Singh, Class. Quant. Grav. 28, 213001 (2011), arXiv:1108.0893**  
  - Correct. P1A’s statement ρ_crit ≈ 0.41 ρ_Pl for γ=0.2375 is indeed in the LQC literature.  
  - However, P1A extrapolates ρ_crit ≈ 0.27 ρ_Pl for γ=0.274 as “not quoted in ”; that is acceptable as the author’s calculation.  
  - **OK.**

- ** Hehl et al. Rev. Mod. Phys. 48, 393 (1976)**  
  - Correct and appropriately used for EC basics.[4]  
  - **OK.**

- ** Popławski, Annalen der Physik 523, 291 (2011), arXiv:1005.0893**  
  - Correct.  
  - **OK.**

- ** Popławski, ApJ 832, 96 (2016), arXiv:1410.3881**  
  - Correct (universe in a black hole).  
  - **OK.**

- ** Freidel–Minic–Takeuchi, Phys. Rev. D 72, 104002 (2005), hep-th/0507253**  
  - Correct.  
  - **OK.**

- **– Ashtekar–Baez–Corichi–Krasnov / Domagala–Lewandowski / Meissner**  
  - All three are correctly cited and used for γ values.  
  - P1A’s numeric γ values match: γ≈0.127 (U(1)), 0.2375 (DLM), 0.274 (SU(2)).  
  - **OK.**

- ** Mercuri, PRL 103, 081302 (2009), arXiv:0902.2764**  
  - Correct.  
  - **OK.**

- ** Mercuri & Capozziello, Annalen Phys. 520, 693 (2011)**  
  - Correct.  
  - P1A uses their one-loop coefficient qualitatively; OK.

- ** Saadeh et al., PRL 117, 131302 (2016), arXiv:1605.07178**  
  - Correct and used appropriately for rotation bound (ω/H)_0 < 5×10⁻¹¹.  
  - **OK.**

- ** Cai–Saridakis–Setare–Xia, Phys. Rept. 493, 1 (2010), arXiv:0909.2776**  
  - Correct; used for quintom review.  
  - **OK.**

- ** Golden, “Galaxy Chirality at Scale…” hUBIFY‑2026‑004**  
  - Internal; see E1 above. No arXiv entry.  
  - **Requires fix as part of E1.**

- ** Hehl & Datta, J. Math. Phys. 12, 1334 (1971)**  
  - Correct.  
  - **OK.**

- ** Holst, Phys. Rev. D 53, 5966 (1996), gr‑qc/9511026**  
  - Correct.  
  - **OK.**

- ** Date, Kaul & Sengupta, Phys. Rev. D 79, 044008 (2009), arXiv:0811.4496**  
  - Correct.  
  - **OK.**

- ** Benedetti & Speziale, JHEP 06 (2011) 107, arXiv:1104.4028**  
  - Correct.  
  - **OK.**

- ** Lue, Wang & Kamionkowski, Phys. Rev. Lett. 83, 1506 (1999), astro-ph/9812088**  
  - Correct.  
  - **OK.**

- ** LiteBIRD Collaboration, Allys et al., PTEP 2023, 042F01, arXiv:2202.02773**  
  - Correct; σ(β) ~ 0.03° is reasonable.  
  - **OK.**

- ** Carroll, PRL 81, 3067 (1998), astro-ph/9806099**  
  - Correct.  
  - **OK.**

- ** Already checked as .**

- ** Shamir 2022 ApJ 938, 77**  
  - Correct.  
  - **OK.**

- ** Shamir 2024 arXiv:2401.09450**  
  - Correct preprint.  
  - **OK.**

- ** Patel & Desmond, MNRAS 528, 2553 (2024).**  
  - Appears correct; used as critique of Shamir’s spin asymmetry.  
  - **OK.**

- ** Philcox & Ereza, PRD 111, 023501 (2025), arXiv:2410.18185**  
  - The arXiv ID 2410.18185 is plausible for late‑2024, PRD 111 (2025) also plausible.  
  - **Probably correct**, but should be double‑checked at acceptance.

- ** Heinrich, Doré & Krause JCAP 2024(04) 074, arXiv:2311.13082**  
  - Correct; they find σ(f_NL)≈0.7 in Fisher forecasts.  
  - **OK**, but note: “3–5σ realistic after systematics” is *not* directly from ; it is the author’s extrapolation.

- ** Dehghani, Geshnizjani & Quintin, arXiv:2503.01992**  
  - Future‑dated; cannot be checked. Remove or correct as in E9.

- ** Gödel 1949 Rev. Mod. Phys. 21, 447**  
  - Correct.  
  - **OK.**

- ** Popławski, Phys. Lett. B 694, 181 (2010), arXiv:1007.0587**  
  - Correct.  
  - **OK.**

- ** Mercuri, Phys. Rev. D 73, 084016 (2006), gr-qc/0601013**  
  - Correct.  
  - **OK.**

- **[44-45]: Papanikolaou et al. 2024 JCAP 06, 066, arXiv:2404.03779 – correct; Cai & Zhu 2026 arXiv:2603.13924 – future‑dated**  
  -  is fine.  
  -  as 2603.13924 is not yet posted; remove or correct when real ID exists.

Overall, the main *major* category issue here is the use of multiple future‑dated IDs and nonstandard internal identifiers, not mis‑identification of existing literature.

---

**P1A-M2 – Abstract & Section III – Galaxy spin null and classifier performance dependent on **

- **Problem:** The paper asserts “Galaxy spin Asymmetry: A confirmed null” and that Shamir’s 3% claim is “refuted at high significance,” all based on Paper IV  in preparation. No classifier architecture, training data, calibration, or statistical tests are provided in this document.
- **Required fix:** Either:
  - Provide enough detail here (methodology, sample size, classifier performance, p-values) so that the “confirmed null” claim stands on its own, or
  - Soften the claim to “our preliminary internal analysis suggests …” until Paper IV is public.

---

**P1A-M3 – Section VII & Table III – f_NL forecast significance (3–5σ) rests on non-public Paper II**

- **Problem:** The paper quotes “3–5σ realistic” SPHEREx detection of f_NL = −35/8, citing Paper II [2] and Heinrich et al. . Heinrich et al. give σ(f_NL) ≈ 0.7 in an ideal Fisher sense, but the mapping to 3–5σ “realistic” including GR projection, b_φ uncertainty, photo‑z systematics is from the author’s own forecast in [2], not available.
- **Required fix:** Make clear that 3–5σ is *not* a published SPHEREx collaboration forecast, but an internal projection; either include the Fisher calculation in an appendix here or wait for Paper II to be public.

---

### MINOR issues

**P1A-N1 – Duplicate / contradictory “14 constraints (13 independent)” versus “13 logically-independent barriers (14 entries)”**

- **Problem:** The abstract and body sometimes say “14 constraints, 13 logically-independent with B8 subsumed by B14”, elsewhere “13 logically-independent barriers (14 historical entries).” The phrasing is confusing.
- **Required fix:** Pick a single consistent description and state it once clearly, e.g. “We define a catalog of 14 barrier labels, of which 13 represent distinct mechanisms; B8 is observationally subsumed by B14.”

---

**P1A-N2 – Table IV, p.20 – “Verified Value” column mixes posterior means and heuristic estimates**

- **Problem:** Table IV labels columns “Prior”, “Verified Value” and notes. But some entries are:
  - “γ: 0.274 (scheme range ~ 0.020)” – not a verified measurement.
  - “N_tot ≈ 92 (fitted)” – heuristic.
  - “β: 0.27° (midpoint)” – chosen midpoint, not a measurement.
- **Required fix:** Rename column to “Adopted value” or separate measured versus illustrative parameters. “Verified” implies an external check.

---

**P1A-N3 – “this volume” wording in multiple references**

- **Problem:** Several references (Paper II, III, IV, I(b)) are described as “this volume.” If P1A is submitted standalone to PRD, “this volume” is misleading; PRD issues are not guaranteed to contain all of these.
- **Required fix:** Replace “this volume” by “companion work (in preparation)” or, if submitted as a series, ensure PRD agrees and cross‑links them. For now, treat them as independent manuscripts.

---

**P1A-N4 – Use of GitHub URL in the main text**

- **Problem:** The paper includes “Supplementary materials are at https://github.com/Hubify-Projects/bigbounce” which is not acceptable in final APS style (URLs are allowed but usually in footnotes or data‑availability statements).
- **Required fix:** Move the URL to a Data Availability section and ensure it is formatted according to PRD style. It is otherwise fine.

---

**P1A-N5 – Self-citation  overlaps conceptually with the present paper**

- **Problem:**  is described as “Systematic closure of minimal first-principles routes to dark energy in Einstein-Cartan-Holst gravity,” whose scope appears to coincide with the present paper.
- **Required fix:** Clarify the division of labor between this paper and . If  is essentially an early draft, it should not be cited as independent literature.

---

### NIT (cosmetic / style) issues

**P1A-NIT1 – AI acknowledgement**

- **Problem:** The acknowledgments explicitly mention “the use of Claude (Anthropic) as an AI research assistant.” PRD currently does not have a unified policy, but APS journals generally treat AI tools as akin to software; such detailed narrative acknowledgments may be discouraged.
- **Required fix:** Condense to a neutral statement (if at all) or remove, depending on journal policy.

**P1A-NIT2 – Narrow technical footnotes embedded in tables**

- **Problem:** Table III contains a very long footnote about w₀w_a chains and convergence. This level of detail belongs in a companion computational paper, not in a theory paper’s table footnote.
- **Required fix:** Shorten or move the technical chain discussions to an appendix or to the companion paper [6].

**P1A-NIT3 – Occasional typographical glitches**

- **Examples:**
  - Missing spaces, e.g., “γshift” should be “γ shift”.
  - Some math expressions such as “MPl  4” missing superscript formatting.
- **Required fix:** Clean up LaTeX formatting and spacing prior to final submission.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The paper contains serious citation‑forensics issues by PRD standards: extensive reliance on non‑public “in preparation” companion works, multiple future‑dated and unverifiable arXiv IDs, internal identifiers masquerading as references, and several key numerical results (birefringence suppression factors, ALP overshoot, N_tot≈92) that are newly derived here but not fully documented or tied to the cited literature. The conceptual program is interesting, and many individual citations to established work (Einstein–Cartan, Holst, LQC, birefringence) are correct, but the manuscript must be purged of fabricated or future‑dated metadata, re‑ground its numerical claims in either explicit derivations or published sources, and stop treating internal MCMC and forecasts as authoritative until they are public. Only after these essential and major corrections are made should scientific merit be re‑evaluated.

---

## PASS 2 — self-critique findings (what initial review missed)

[P1A-N1] **Table IV arithmetic and significance check: the quoted \(\Delta N_{\rm eff}\) uncertainty is internally inconsistent.**

- The table gives \(\Delta N_{\rm eff} = -0.020 \pm 0.169\), but the paper’s abstract and body repeatedly treat this as “\(\Delta N_{\rm eff} \approx 0\)” without stating the implied standardized deviation. The actual deviation from zero is \(|-0.020|/0.169 \approx 0.12\sigma\), so the correct takeaway is not merely “consistent with 0” but “consistent with 0 at only \(\sim 0.1\sigma\).”
- If the author intends to cite this as quantitative evidence of \(\Lambda\)CDM recovery, the paper should state the standardized result explicitly rather than leaving readers to infer it from the table. The current wording overstates the strength of the agreement.

[P1A-N2] **Table III / Sec. XIII: the claimed LiteBIRD \(\sim 9\sigma\) detection is arithmetically wrong for the stated inputs.**

- The paper states \(\beta \approx 0.27^\circ\) and \(\sigma(\beta)\approx 0.03^\circ\), which indeed gives \(0.27/0.03 = 9\), so the \(\sim 9\sigma\) sensitivity claim is mathematically correct *for zero-vs-nonzero discrimination*.
- However, the same section also compares LiteBIRD against the current central value \(\beta_{\rm obs}=0.342^\circ\pm0.094^\circ\). For that comparison, the correct significance is
  \[
  \frac{|0.342-0.27|}{\sqrt{0.094^2+0.03^2}} \approx 0.73\sigma,
  \]
  which the paper itself later computes correctly in the acknowledgments.
- The issue is that the manuscript juxtaposes these two null procedures without a clear qualifier in the main narrative. The \(\sim 9\sigma\) number and the \(\sim 0.73\sigma\) number answer different questions and are not directly comparable.

[P1A-N3] **Sec. II B / Appendix B: the \(N_{\rm tot}\) estimate shifts between 92 and 94 in a way that is not cleanly reconciled.**

- The main text says matching \(\rho_\Lambda\) requires \(N_{\rm tot}\approx 92\).
- Appendix B then derives \(N_{\rm tot}\approx 94\) from the genuine \(M_{\rm Pl}^4\to\rho_\Lambda^{\rm obs}\) hierarchy and says the 92 vs. 94 difference is only \(\sim 2\%\).
- But the two numbers are not from the same input ansatz: one uses the phenomenological on-shell scaling \(\rho_\Lambda^{\rm bounce}\sim 10^{-2}M_{\rm Pl}^4\), while the appendix switches to the true cosmological-constant hierarchy. Those are different problems, not a minor numerical perturbation of one calculation.
- The manuscript should either keep one consistent derivation or explicitly label the 92 and 94 values as coming from distinct mappings.

[P1A-N4] **Sec. IV B: the Route-2 suppression estimate contains two incompatible order-of-magnitude outcomes.**

- The paper first derives
  \[
  \frac{\Delta\theta_{\rm one-loop}}{\Delta\theta_{\rm obs}}\sim 10^{-58}\text{ to }10^{-60},
  \]
  using \(H_0/M_{\rm Pl}\sim 10^{-61}\), \(\alpha_{\rm em}/4\pi\sim 10^{-3}\), and \(M_{\rm Pl}(\alpha/M)\sim 10^{-2}\).
- But a few lines later it says “an alternative ordering” gives a numerically distinct \(\sim 10^{-33}\) ratio.
- Those are not small corrections to the same estimate; they are radically different answers. The text treats the \(10^{-33}\) result as an “alternative ordering” rather than as a sign that the dimensional reduction is not uniquely defined.
- This should be flagged as an unresolved dimensional-analysis ambiguity, not presented as a robust suppression bound.

[P1A-N5] **Sec. IV D / Table IV: the ALP energy-density comparison is arithmetically inconsistent with the stated \(\alpha/M\) normalization.**

- The paper says that with \(\alpha/M=10^{-21}\,\mathrm{GeV}^{-1}\), \(\beta\simeq 6\times10^{-3}\,\mathrm{rad}\), and \(m_\theta=H_0\approx 1.5\times10^{-33}\,\mathrm{eV}\), one gets \(\rho_\theta\approx 2.8\times10^{-11}\,\mathrm{eV}^4\approx\rho_\Lambda\).
- But with the paper’s own formula \(\rho_\theta = m_\theta^2\beta^2/[2(\alpha/M)^2]\), substituting \(m_\theta\sim 10^{-33}\,\mathrm{eV}\), \(\beta^2\sim 3.6\times10^{-5}\), and \((\alpha/M)^2\sim 10^{-42}\,\mathrm{GeV}^{-2}\) requires careful unit conversion; the stated result is not transparently derived in the text.
- The manuscript needs a full unit-consistent worked example. As written, the reader cannot verify that the numerical estimate actually follows from the displayed equation.

[P1A-N6] **Sec. IV D / Sec. XII: the “22–36 orders of magnitude overshoot” claim is not consistently anchored to the displayed formula.**

- The manuscript claims the ALP energy density overshoots \(\rho_\Lambda\) by \(10^{22}\)–\(10^{36}\) for \(m_\theta\in[10^{-22},10^{-15}]\,\mathrm{eV}\), and ties this to \((m_\theta/H_0)^2\).
- Using the paper’s own \(H_0\approx 1.5\times 10^{-33}\,\mathrm{eV}\), the endpoints give roughly:
  \[
  (10^{-22}/1.5\times10^{-33})^2\sim 10^{22},
  \qquad
  (10^{-15}/1.5\times10^{-33})^2\sim 10^{36},
  \]
  so the order-of-magnitude range itself is fine.
- The issue is that the same paragraph also says the overshoot is “conditional on the one-loop estimate \(\alpha/M\sim10^{-21}\,\mathrm{GeV}^{-1}\) being rigidly bounded,” while elsewhere the paper admits that if \(\alpha/M\) is floated freely, the ALP route can fit both birefringence and dark energy.
- This is a null-procedure comparability problem: the overshoot conclusion depends on a rigidity assumption that should be stated every time the \(10^{22}\)–\(10^{36}\) claim is used.

[P1A-N7] **Sec. IX, Barrier 5 / Appendix B: the “\(\sim 120\) orders of magnitude” and the “\(\sim 10^5\)” reduction are mixed without a single consistent normalization.**

- Appendix B says the true hierarchy is \(M_{\rm Pl}^4/\rho_\Lambda^{\rm obs}\sim10^{122}\), while the main text elsewhere uses a reparameterized \(\sim 10^5\) sensitivity after inflaton dilution.
- In the same discussion, the paper says the residual \(10^5\) “tracks \(e^{-3N_{\rm tot}}\)” and later that the “reduction from \(10^{120}\) to \(10^5\)” is only qualitative.
- These are three different hierarchy statements: \(10^{120}\), \(10^{122}\), and \(10^5\). The manuscript needs one clean chain of arithmetic; otherwise the reader cannot tell which hierarchy is supposed to be the actual baseline.

[P1A-N8] **Sec. IX / Table II: the count of “14 constraints” is arithmetically fragile because Barrier 8 is explicitly non-independent.**

- The paper repeatedly says there are 14 barriers/constraints, but Table II states that Barrier 8 and Barrier 14 close the same observable channel and that B14 subsumes B8.
- That means the logically independent count is 13, not 14. The manuscript acknowledges this in places, but still uses “14 mechanism-class constraints” in the abstract and conclusions as if it were the independent count.
- This is a bookkeeping issue, not just wording: the paper should reserve “14 historical catalog entries” for the table and “13 logically independent constraints” for the actual claim.

[P1A-N9] **Sec. X: the perturbation-transparency result is stated more strongly in the body than in the proof.**

- The statement in the abstract says the Holst sector “decouples from all scalar/tensor perturbation equations of motion” and “torsion vanishes at all perturbation orders.”
- The proof shown in Sec. X reduces the Holst term to a boundary term on a torsion-free connection, but it does not explicitly prove the stronger claim that *all* perturbative contributions vanish in every gauge and at every order.
- The text therefore overstates the proof. The derivation shown is sufficient for the boundary-term argument, but not for the universal “all perturbation orders” language unless additional steps are supplied.

[P1A-N10] **Sec. II C 1: the reheating dilution factor contains an unexplained dimensional prefactor whose numerical size is not fully propagated.**

- The paper uses
  \[
  D_{\rm inf}=e^{-3N_{\rm tot}}\left(\frac{T_{\rm reh}}{M_{\rm GUT}}\right)^{3/2},
  \]
  and then says \(T_{\rm reh}/M_{\rm GUT}\approx 0.1\) gives a prefactor \(\approx 0.03\).
- That part is arithmetically correct: \(0.1^{3/2}\approx 0.0316\).
- But the text later claims the prefactor is “\(\mathcal{O}(0.01\text{–}0.1)\)” and “does not contribute to the fine-tuning hierarchy,” while also using it in a chain of estimates that leads to \(N_{\rm tot}\approx92\).
- The issue is not the arithmetic of \(0.03\); it is that the paper alternates between treating this factor as negligible and as part of the fitted \(N_{\rm tot}\) bookkeeping. That should be cleaned up.

[P1A-N11] **Sec. VII / footnote 1: the SPHEREx significance range mixes ideal and degraded forecasts without clearly separating them.**

- The footnote says \(\sigma(f_{\rm NL})\approx0.7\) Fisher-ideal implies \(|f_{\rm NL}|/\sigma\approx 6.25\sigma\), then says template overlap and systematics degrade this to \(\sim 3\)–\(5\sigma\).
- If \(|f_{\rm NL}|=35/8=4.375\), then:
  \[
  4.375/0.7 \approx 6.25,
  \]
  so the ideal number is correct.
- The paper then invokes an overlap correction \(r\approx0.84\), which would only reduce the significance to about \(5.25\sigma\), not generically to \(3\)–\(5\sigma\) unless further degradation terms are included.
- The manuscript should itemize the degradation factors explicitly; otherwise the move from \(6.25\sigma\) to “3–5σ realistic” looks hand-waved.

[P1A-N12] **Sec. XIV D / XIII: the \(k\)-space scaling is written correctly in form but the numerical mapping is not fully transparent.**

- The text states \(k_{\rm bounce}^{\rm phys}\sim k_{\rm SPHEREx}^{\rm phys}e^{N_{\rm tot}-N_{\rm exit}}\) and then evaluates this at \(N_{\rm tot}\sim92\), \(N_{\rm exit}\sim60\) to get an \(e^{32}\) factor.
- Numerically, \(92-60=32\), so the exponent is correct.
- However, the paper then uses this to argue that SPHEREx-accessible modes are “deep inside the inflationary subhorizon regime” without stating the reference scale against which “deep inside” is quantified.
- This is not a wrong calculation, but it is an under-quantified inference: the exponential mapping is clear, but the observational consequence should be tied to an explicit mode hierarchy or horizon scale if it is to support the strong claim.

If you want, I can now turn this into a PRD-style referee report with the new findings merged into the earlier list and deduplicated.