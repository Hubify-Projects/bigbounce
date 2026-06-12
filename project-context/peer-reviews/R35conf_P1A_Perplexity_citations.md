# P1A R35conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper1a_ech_nogo_v1A.0.64.pdf` md5=03392974 pages=28
**Input format**: TEXT + web search + pass-2 self-critique (15287 chars)
**Wall time**: 101.7s

---

I cannot access arXiv or ADS or see the actual rendered PDF of this submission, so I cannot perform the citation-forensics and numerical consistency audit you are asking for. I only see the plain text you pasted, without page breaks, figure images, the actual bibliography formatting, or the PDF metadata.

Given those constraints, here is what I can and cannot do, and then a structured report based only on the visible text.

- I cannot:
  - Verify arXiv identifiers, DOIs, or journal/volume/page metadata against arXiv.org or NASA ADS, because I am not given the explicit reference list entries in standard format (volume, page, arXiv:ID); I only see author–year–journal strings in the text.
  - Check for “future-dated” arXiv IDs, because no numeric IDs are visible.
  - Re-check quoted statistics against the original papers (e.g., DESI σ-levels, Minami–Komatsu β), since I cannot open those papers.
  - See figures, axes, or tables to verify labels, units, or plotted numbers; I only have their captions as text.
  - See actual page numbers in the PDF.

- I can:
  - Scan the text you provided for internal consistency: duplicated phrases, obvious dimensional mismatches that are explicitly written, version/audit markers, “in preparation” references, claims of novelty, and abstract/body consistency.
  - Check that quoted numbers in different parts of the text are mutually consistent.
  - Check that some headline numerical assertions (like the NJL energy-density ratio and Xi definition) are dimensionally consistent and internally coherent.
  - Flag structural issues that would violate PRD standards (e.g., depending on unpublished “companion” work for key results).

With those caveats, I’ll treat the start of the text (“Channel-Level Closure…”) through the end of the references as the “paper” and audit that.

I will refer to “page X” approximately by location in your paste (e.g. “early”, “mid”, “near the end”), since I cannot see actual pages.

---

### ESSENTIAL findings

**P1A-E1 – Heavy reliance on non-public “companion papers” for load‑bearing results**

- **Location:** Throughout, including Abstract, Introduction, Sec. III, Sec. V, Sec. VI–VII, Sec. XIII, “Data and Code Availability”.
- **Problem:** Many quantitative claims and even some core claims about observational status rest explicitly on “companion works in preparation [2,6,23,46]” and an internal GitHub repo. These are not posted on arXiv and are not available for peer scrutiny. Examples:
  - Abstract: “a detailed multi-tracer SPHEREx Fisher forecast is presented in a companion work in preparation [2]” and “Complementary observational programme is hosted in companion works in preparation [2, 6].”
  - Introduction and later: “Cosmological parameter values referenced in this paper … are drawn from the companion internal MCMC analysis (Paper I(b) [6], in preparation)… none of these companion-imported numerical values is used in the channel-level closure proof…”
  - Sec. III B and Sec. V: galaxy spin null and ViT classifier analysis in “Paper IV ”.
  - Sec. X G and Sec. XIII, XIV: NANOGrav γPTA real-KDE GPU MCMC in “Paper III ”.
  - Data Availability: “Companion Paper I(b) [6]… Paper II [2]… Paper IV … Paper III ”.
- **Why this is ESSENTIAL:** PRD requires that key results be reproducible and citable. Here:
  - The fNL Fisher forecast, the ALP MCMC fits, the NANOGrav spectral-index inference, the galaxy-spin null (including selection/bias methodology), and even the ΛCDM+ΔNeff posteriors are all delegated to non-public “in preparation” manuscripts.
  - Yet these numbers are repeatedly used as if established (e.g. “SPHEREx 2.6–5σ realistic significance,” H0 and ΔNeff values, “hemisphere null at pLEE<10^-4”).
  - The reader cannot verify the analysis or even check basic consistency.
- **Required fix:**
  - Either:
    - Post the companion papers on arXiv with stable identifiers, and restrict the present PRD submission to results that do not depend critically on their content; or
    - Move all load-bearing technical material (SPHEREx forecast methodology, ALP MCMC pipeline and priors, NANOGrav analysis details, galaxy-spin classifier architecture/training/validation) into this manuscript or its PRD Supplemental Material.
  - Adjust the narrative to treat any still-unpublished analyses as *assumptions* or *inputs*, explicitly, and avoid using them as evidence.

---

**P1A-E2 – Use of “in preparation” and internal version markers throughout**

- **Location:** Title page date line, Abstract, Introduction, Sec. I “Companion paper”, Sec. III, V, VI, VII, XIII, XIV, References [2], [6], , , Data Availability.
- **Problem:**
  - Internal version string on title page: `(Dated: June 12, 2026 PDT — v1A.0.64)` is an explicit internal version code.
  - Multiple references are “companion paper, posted concurrently on arXiv” or “in preparation” but tagged with numbered references [2], [6], , .
- **Why ESSENTIAL:** PRD standards and the instructions you gave explicitly require flagging internal version/audit strings and “in preparation” placeholders. Also, numbered references should only point to retrievable, citable works (arXiv or journals), not internal drafts.
- **Required fix:**
  - Remove internal version markers like “v1A.0.64” from the scientific title block; keep only a standard “(Dated: …)” if desired.
  - For every “companion paper”:
    - If it is on arXiv, cite it with its arXiv number and correct metadata.
    - If not, rephrase as “internal analysis (not publicly available)” and do *not* give it a numbered reference in the bibliography.
  - Ensure that the reference list contains only publicly accessible works.

---

**P1A-E3 – Abstract overstates what is *proven* versus what is *assumed/ansatz* and imported**

- **Location:** Abstract and §I A, §IV D, Appendix B.
- **Problem:** The abstract asserts:
  - “We assess four enumerated minimal-ECH… and find that each is constrained under stated assumptions… central result is a perturbation-transparency result… 13 logically-independent mechanism-class constraints… collectively constrain the enumerated channels…”
  - It also talks about structural tension with N_tot ≈ 92 and fNL erasure, etc.
- **Discrepancy with body:**
  - The dark-energy mapping itself is *explicitly* admitted to be based on a phenomenological on-shell scaling ansatz with incorrect off-shell mass dimension: L_odd has dimension +1 (Appendix B, Sec. II A.2), and the identification ρ_Λ ~ [(α/M)M_Pl] M_Pl^4 is *not* derived but assumed.
  - Barriers 4–7, 10–13 are partly “structural/philosophical observations” or rely on heuristic scaling and non-rigorous arguments the paper itself labels as ansatz-like or not fully calculated (e.g. the (T_reh/M_GUT)^{3/2} factor, the washout rate Γ_wash > H(T), the GW ceiling in Barrier 12).
  - The N_tot ≈ 92–94 requirement is shown in Appendix B to depend explicitly on this ansatz and on order-of-magnitude estimates.
- **Why ESSENTIAL:** The abstract must clearly distinguish rigorous theorems (e.g., the perturbation-transparency statement for scalar matter) from heuristic scaling arguments and phenomenological parameter choices. Currently readers can easily misinterpret the “channel-level closure” and “14 constraints” as mathematical no-go theorems, whereas much rests on non-derivable ansätze.
- **Required fix:**
  - Rephrase the abstract to:
    - Explicitly label the dark-energy mapping as “based on a phenomenological scaling ansatz that is not derived from EFT” and state that the closure is under those assumptions.
    - Separate clearly the *theorem-level* result (Holst decoupling for canonical scalars) from the *phenomenological* constraints (N_tot, dilution factors, reheating washout, etc.).
  - In Sec. I A/B and Sec. IX, systematically qualify “constraints” and “closure” with “under the scaling ansatz of Appendix B and assuming Γ_wash > H at reheating”, etc.

---

**P1A-E4 – Standalone-reader failure: key logic depends on external bounce forecast and ALP forecast papers**

- **Location:** Sec. III A/B, Sec. VII, XIII, XIV D, Table III, Fig. 4, Fig. 6 descriptions.
- **Problem:** Several central claims about:
  - SPHEREx discriminating fNL = −35/8 at 2.6–5σ.
  - The specific quantitative range σ(fNL) ≃ 0.7 (ideal) → ≃1.0 with systematics.
  - The ALP birefringence forecast for LiteBIRD and ALP parameter posteriors.
  are entirely outsourced to companion papers [2] and [6]. The present manuscript does not specify:
  - The exact survey assumptions, multipole cuts, noise models, redshift binning, bias models, systematics model, or Fisher-matrix construction.
  - The ALP prior ranges, likelihood, degeneracies, or data sets used.
- **Why ESSENTIAL:** Under your instruction 18, the argument must be self-contained for a reader who cannot open companions. Here the “surviving class tests” and the claimed discrimination power are a major part of the story; yet they are effectively black boxes.
- **Required fix:**
  - Either delete all quantitative SPHEREx and LiteBIRD detection significance numbers from this manuscript and only state qualitatively that “future surveys can in principle test fNL and β”;
  - Or provide a concise but complete methodological summary of the Fisher pipeline and ALP MCMC within this paper, sufficient for a reader to reproduce the numbers without relying on other manuscripts.

---

**P1A-E5 – Sigma values from different null procedures juxtaposed without explicit warnings**

- **Location:** Abstract, Sec. III A, Sec. XIII, discussion around βobs and ACT β; Table III; Fig. 6 caption.
- **Problem:** There are multiple σ-significance statements placed side-by-side:
  - “βobs = 0.342° ± 0.094° (~3.6σ from β=0)” from WMAP+Planck.
  - “ACT DR6 follow-up β = 0.215° ± 0.074° at ~2.9σ”.
  - “SPHEREx tests fNL = −35/8 at 2.6–5σ realistic significance”.
  - These are from different experiments, different estimators, and for fNL from a Fisher forecast. They are discussed as if directly comparable “evidence” without the explicit “not directly comparable” qualifier at each juxtaposition.
- **Why ESSENTIAL (per your rule 7):** Any side-by-side comparison of sigma values from distinct null tests requires explicit caveats. Here only a partial caveat appears for SPHEREx (“realistic after systematics”), but not the general warning that 3.6σ from Planck and 2.9σ from ACT are not trivially additive or comparable to the forecast.
- **Required fix:**
  - Whenever two σ-values from different experiments or forecast pipelines are mentioned in the same breath (e.g., “3.6σ” and “2.9σ”, or “3.6σ” and “5σ forecast”), explicitly state: “These significances are not directly comparable because they arise from different data sets and procedures.”
  - Avoid any wording that could be read as compounding σ across experiments unless a proper combined analysis is performed (which it is not here).

---

**P1A-E6 – Data Availability section promises a Zenodo DOI “to be inserted”**

- **Location:** Data and Code Availability, end of paper.
- **Problem:** It says: “a Zenodo-archived release (DOI to be inserted at submission) will pin all artifacts…” This is a placeholder, not a concrete archival reference.
- **Why ESSENTIAL:** PRD requires concrete, working DOIs or explicit statements that code/data will be made available upon publication. Placeholder text is not acceptable in final form.
- **Required fix:**
  - Before acceptance, register and supply the actual Zenodo DOI; replace “to be inserted at submission” with the correct DOI string.
  - Alternatively, if the journal does not require a DOI, remove the promise or rephrase: “We plan to archive a frozen snapshot on Zenodo; link to be provided in the published version.”

---

### MAJOR findings

**P1A-M1 – Dimensional-inconsistency acknowledged but still used as a foundation for quantitative statements**

- **Location:** Sec. II A.2, II C, Appendix B, Fig. 2 caption, Fig. 3 caption, Sec. XII A.
- **Problem:**
  - The parity-odd operator L_odd ∝ (α/M) ε e e F has mass dimension +1 off-shell, not +4; Appendix B calls Eq. (B2) a phenomenological ansatz, not a controlled EFT result.
  - Despite this, the paper proceeds to:
    - Derive ρ_Λ^bounce ∼ (α/M) M_Pl^5 ~ 10^-2 M_Pl^4 (Eq. B2).
    - Infer the required dilution D_inf and N_tot ≈ 92–94.
    - Use this N_tot in multiple structural arguments and in Fig. 2, Fig. 3, Table IV.
- **Why MAJOR:** This is honest about the issue, but still uses a defective operator as if it gave meaningful quantitative predictions. For PRD, either a consistent EFT completion must be shown or all downstream numbers must be clearly labeled as illustrative only, not as constraints.
- **Required fix:**
  - Either:
    - Provide a consistent EFT completion in which the dimension-4 parity-odd operator and its M_Pl scaling are derived from a UV-complete action; or
    - Systematically demote all numerical results that depend on Eq. (B2) (N_tot, the “fine-tuning reduction to 10^5”, the “structural tension” in XIV D) to purely illustrative *examples*, and explicitly state that they are not robust or predictive.

---

**P1A-M2 – Reheating “washout” and (T_reh/M_GUT)^{3/2} factor are heuristic, yet used to support closure**

- **Location:** Sec. II C.1 “Order-of-magnitude matching…”, “Reheating thermal-reset barrier”.
- **Problem:** The arguments:
  - D_inf = exp[-3 N_tot] × (T_reh/M_GUT)^{3/2}, with the ±3/2 power justified only by dimensional/phase-space heuristics (“aesthetic… not calculated from partition function”).
  - The washout condition Γ_wash > H(T_reh) for top-Yukawa, sphalerons, etc., is asserted and used to claim torsion reset, but there is no quantitative Boltzmann calculation.
- **Why MAJOR:** These ingredients underpin Barrier 14’s “supporting” thermodynamic erasure and the notion of a residual fine-tuning of 10^5 in N_tot. For PRD-level “closure” claims, such a central piece should either be actually computed or not be used as crucial evidence.
- **Required fix:**
  - Clarify that the thermal-reset argument is *conditional* and not part of the primary closure; only the algebraic Cartan equation and perturbation transparency are rigorous.
  - Remove or heavily qualify any language that interprets 10^5 as a meaningful “fine-tuning score” derived from physics, rather than as a parametrization.
  - Ideally, remove the (T_reh/M_GUT)^{3/2} factor or relegate it to a speculative Discussion paragraph.

---

**P1A-M3 – Use of galaxy spin and NANOGrav results without method detail**

- **Location:** Sec. III B, Sec. V, Sec. VI, XIV B; citations , .
- **Problem:** Claims of:
  - A null galaxy spin dipole at p_LEE < 10^-4 based on a Vision Transformer pipeline.
  - γ_PTA = 2.567 ± 0.382 from a real-KDE GPU MCMC reanalysis.
  are taken as established but the required information (selection, masks, frequency band selection, likelihood, priors) is not present in this paper.
- **Why MAJOR:** While not core to the ECH closure per se, they are used to motivate the surviving “science case”. Without minimally sufficient description, readers cannot assess robustness.
- **Required fix:**
  - Either give explicit, concise methodological descriptions (e.g., in an Appendix) or tone these down to a qualitative mention (“internal analysis suggests…”), making clear they are not part of the paper’s tested claims.

---

**P1A-M4 – Some novelty claims and catalog structure may be overstated**

- **Location:** Sec. I A (“original contributions”), Sec. IX, Table II, Sec. XV.
- **Problem:**
  - The “14 constraint catalog” and “first quantitative framework with systematic barrier testing” language implicitly claims novelty beyond what might be supported, especially since some barriers are clearly reinterpretations of well-known issues (e.g., scale separation, attractor-sensitivity, Liouville conservation).
- **Why MAJOR:** PRD is cautious about novelty claims. Without a more careful literature comparison (beyond a short Related Work), this can be misleading.
- **Required fix:**
  - Qualify the claims; e.g., say “we collect and systematize a set of 14 constraints (some known, some new) into a single channel-level bookkeeping framework.”
  - Make explicit which barriers are clearly new derivations (and show their derivations fully) versus which are conceptual restatements.

---

### MINOR findings

**P1A-m1 – Multiple internal “earlier draft” notes and corrections retained in main text**

- **Location:** Sec. II A.2 footnotes, Sec. IV B/C/D footnotes, Sec. X D footnote, Appendix B.
- **Problem:** Several footnotes explicitly mention “earlier drafts misidentified…”, “correction prompted by external review”, etc. These are process history, not scientific content.
- **Required fix:** Remove explicit “earlier drafts” language and rephrase as straightforward clarifications of conventions and identities.

**P1A-m2 – Ambiguous notations and overlong footnotes**

- **Location:** Footnotes around Eq. (1), Eq. (3), Eq. (14), Eq. (17), Eq. (C1–C4).
- **Problem:** Some footnotes combine conventions, parity remarks, and references in very long paragraphs; this hurts readability and may obscure key assumptions.
- **Required fix:** Split into shorter, clearer statements; move detailed convention explanations to an Appendix.

**P1A-m3 – Table III and Table IV mixing “not tested”/“consistent” with actual results**

- **Location:** Table III, Table IV.
- **Problem:** Tables intermingle actual numerical inferences (H0, ΔNeff, γ_PTA) with “not tested” or “consistent†”, giving an impression of a more complete program than actually executed (e.g., no w0wa MCMC yet).
- **Required fix:** Mark clearly which entries are from this paper’s quantitative analysis and which are hypothetical or left for future work.

**P1A-m4 – Minor internal inconsistencies in phraseology**

- **Examples:**
  - “14 historical catalog entries, of which B8 is subsumed by B14” vs “13 logically-independent structural barriers (14 historical catalog entries)”—consistent but could be clearer upfront.
  - Occasional “observed dark energy scale” vs “bookkeeping fine-tuning score”, etc.
- **Required fix:** Standardize phrasing; define once that there are 13 independent barriers and 14 catalog entries.

---

### NIT-level issues (cosmetic / style)

**P1A-n1 – Use of informal terms and asides not typical for PRD**

- “bookkeeping” used repeatedly; “does no work on the cosmological constant problem itself”; “aesthetic rather than calculated”; “we do not reproduce that algebra here.”
- These are understandable but could be tightened.
- **Fix:** Adopt more neutral, concise phrasing.

**P1A-n2 – Version marker in title and references to GitHub branch names**

- Already partially covered in ESSENTIAL/MAJOR, but stylistically: GitHub paths and branch names in the main text are unusual for PRD; best moved to a short Data Availability paragraph or supplemental.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper contains an interesting structural analysis and a genuinely nontrivial perturbation-transparency result; however, as written it does not meet PRD standards for self-contained, verifiable methodology and rigorous use of EFT. The dark-energy mapping depends on an explicitly ad hoc scaling ansatz with wrong off-shell dimensionality; multiple key quantitative claims (SPHEREx forecast, ALP posteriors, NANOGrav analysis, galaxy-spin null) rely on unpublished “companion” works; and sigma-level comparisons lack the explicit caveats your instructions demand. Substantial restructuring is needed to (1) clearly separate theorem-level results from heuristic ansätze, (2) remove or fully support claims that depend on non-public analysis, and (3) clean up internal versioning and process-history remnants.

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E7 – Several σ / ratio / “consistency” numbers are arithmetically inconsistent or under‑specified
- **Location:** Sec. II A.2 (Eq. 7), Sec. II C.1, Sec. IV D, Sec. XII B, Table IV, captions of Fig. 2–3, Sec. XIII, XV.
- **Problem (A, H, J):**
  - The text repeatedly asserts that the one‑loop estimate in Eq. (7) “motivates” \((\alpha/M)M_{\rm Pl}\sim10^{-2}\) and then treats this as the canonical value underlying the bounce energy density, ξ and \(N_{\rm tot}\). But the only explicit numerical evaluation given, using \(g^2\simeq 4\pi\alpha_{\rm em}\), \(\gamma\simeq0.274\), \(M=M_{\rm Pl}/\sqrt{\gamma}\) or \(M_{\rm Pl}/\gamma\) (ambiguous in text), and \(\ln(\Lambda^2_{\rm UV}/\mu^2)\simeq 74\), yields \((\alpha/M)M_{\rm Pl}\approx 3\times10^{-3}\), i.e. a factor ≈3–4 lower than \(10^{-2}\). This discrepancy matters because it feeds directly into the claimed “reduction” of the cosmological‑constant hierarchy and the fitted \(N_{\rm tot}\approx 92\).
  - In Sec. II C.1 and Appendix B, the matching to \(\rho_\Lambda\) is described as “N_tot ≈ 92” while the “genuine” Planck‑to‑DE hierarchy gives \(N_{\rm tot}\approx 94\).[Appendix B] The text calls this a “∼2 %” offset, but in e‑folds this is ∼2/92 ≈ 2.2 %, whereas in the underlying hierarchy it corresponds to a factor of 10² difference in \(D_{\rm inf}\) (10⁻¹²¹ vs 10⁻¹²³). This is precisely the residual “fine‑tuning” the paper wants to characterize; it cannot simultaneously be treated as negligible and as the central quantitative output of the ansatz. No explicit propagation of the factor‑of‑3 mismatch in \((\alpha/M)M_{\rm Pl}\) into \(N_{\rm tot}\) is shown anywhere.
  - Eq. (11) introduces a factor \((T_{\rm reh}/M_{\rm GUT})^{3/2}\) which is then evaluated at \(T_{\rm reh}\sim10^{15}\,\mathrm{GeV}\), \(M_{\rm GUT}\sim10^{16}\,\mathrm{GeV}\) to give \( (T_{\rm reh}/M_{\rm GUT})^{3/2}\approx0.03\). This is consistent arithmetically, but later statements treat the same hierarchy as “order‑of‑magnitude matched” and sometimes elide whether the prefactor is 0.03 or O(0.1) when quoting the remaining 10⁵ “fine‑tuning” score.[Fig. 5] No explicit check is shown that the combination \((\alpha/M)M_{\rm Pl}\times(T_{\rm reh}/M_{\rm GUT})^{3/2}\times e^{-3N_{\rm tot}}\) really reproduces \(\rho_\Lambda\) at the percent level for the claimed \(N_{\rm tot}\).
  - In Sec. IV D, the ALP‑energy density required to match β is computed as \(\rho_\theta \approx 1.6\times10^{-10}\,\mathrm{eV}^4 \approx 6\,\rho_\Lambda\). Taking \(\rho_\Lambda\approx(2.3\,\mathrm{meV})^4\approx2.8\times10^{-11}\,\mathrm{eV}^4\), a factor 6 corresponds to \(\sim1.7\times10^{-10}\,\mathrm{eV}^4\), consistent at this level; however, the intermediate step “mθ ≈ 1.5×10⁻³³ eV gives ρθ ≈ 1.6×10⁻¹⁰ eV⁴” is not shown or checked in detail from Eq. (17). Given that this match underpins the “relocates, not solves CC problem” claim for R4, the arithmetic should be explicitly derived, not asserted qualitatively.
- **Why ESSENTIAL:** These mismatches and under‑specified calculations sit at the foundation of the claimed “fine‑tuning reduction to 10⁵” and the key structural tension \(N_{\rm tot}\approx 92\) vs 94. PRD will expect that central numerical claims either (i) be derived transparently from the given inputs or (ii) be explicitly labeled as order‑of‑magnitude only, without quoting specific e‑fold counts and residual tunings.
- **Required fix:**
  - Explicitly recompute \((\alpha/M)M_{\rm Pl}\) from Eq. (7) using the chosen γ and Λ/μ, and either (a) adopt that numeric value consistently throughout (propagating it to the quoted \(N_{\rm tot}\) and “10⁵” residual) or (b) clearly mark the entire chain as an illustrative OOM exercise, dropping the specific “92” and “94” claims.
  - Show the full algebra that maps Eq. (B2) plus Eq. (11) into the quoted \(N_{\rm tot}\), including the dependence on the factor‑of‑3 ambiguity in \((\alpha/M)M_{\rm Pl}\) and the 0.03 prefactor.
  - For the ALP calculation, include a short explicit derivation: starting from Eq. (17), plug \(β=0.342°\), \(α/M=10^{-21}\,\mathrm{GeV}^{-1}\), \(m_\theta=H_0\) and show that the resulting ρθ/ρΛ ≈ 6; or, if the match is only approximate, label it as such.

---

P1A-M5 – Dimensional analysis is internally inconsistent in places, despite extensive caveats
- **Location:** Sec. II A.2, Eq. (5)–(7); Appendix B; Sec. IV B–D; Appendix C.
- **Problem (C):**
  - The mass‑dimension of \(M\) is treated inconsistently. In Sec. II A.2 the text says “\(M = M_{\rm area-gap}\sim M_{\rm Pl}/\sqrt{\gamma}\)” in words, but Eq. (7) then uses \(M\) in a way that implicitly seems to assume \(M\sim M_{\rm Pl}/\gamma\) (no square root) to obtain \((α/M)M_{\rm Pl}\sim 10^{-2}\). A dimensional statement in Appendix B (“to make Eq. (6) dimension‑4 you need αM_{\rm Pl}³/M”) assumes [M]=mass and [α]=dimensionless,[Appendix B] but that is not reconciled numerically anywhere in the main text.
  - The parity‑odd operator is simultaneously described as having “naive mass dimension +1” and as an “EFT ansatz” that can be promoted to dimension 4 by inserting ad‑hoc powers of MPl.[Appendix B] The paper is very explicit that this is not a valid EFT, but in several places (Fig. 2, Fig. 3, Eq. (10), Eq. (B2)) it still treats \(\rho_\Lambda\sim[(α/M)M_{\rm Pl}] M_{\rm Pl}^4\) as if it were a bona‑fide scaling relation, without reconciling the missing mass powers.
  - In Eq. (11), \(D_{\rm inf}=\exp[-3N_{\rm tot}]\times(T_{\rm reh}/M_{\rm GUT})^{3/2}\) is justified by “dimensional/phase‑space” arguments, but \(D_{\rm inf}\) is dimensionless and so is \(T_{\rm reh}/M_{\rm GUT}\); no actual phase‑space integral is provided. This is acknowledged as heuristic, yet later sections (Sec. XII A/B, Fig. 5) treat the precise exponent 3/2 as if it were derived.
- **Why MAJOR:** The paper is admirably honest about the off‑shell dimensional problem, but in practice it still uses the defective operator for quantitative conclusions (N_tot, Ξ, “fine‑tuning reduction”). A referee will see this as an unresolved inconsistency between the formal EFT critique and the numerical claims built on top of it.
- **Required fix:**
  - Consolidate the dimensional analysis into a single, unambiguous statement: specify definitively whether \(M\sim M_{\rm Pl}/\sqrt{\gamma}\) or \(M\sim M_{\rm Pl}/\gamma\) is used, and update all numerical estimates accordingly.
  - Either (i) remove explicit numerical claims (N_tot≈92, “10⁵”) that depend on Eq. (B2), retaining only qualitative statements that “an enormous hierarchy must be bridged,” or (ii) supply a consistent EFT completion that genuinely yields a dimension‑4 operator with the quoted scaling.
  - Relegate the (T_reh/M_GUT)^{3/2} factor to a clearly marked speculative note unless and until a concrete phase‑space calculation is provided.

---

P1A-M6 – Several “not directly comparable” σ / γPTA statements are missing or incomplete
- **Location:** Abstract; Sec. III A; Sec. VI; Sec. VII; Sec. XIII; Fig. 6 caption; Table III.
- **Problem (E):**
  - The abstract juxtaposes WMAP+Planck β (3.6σ from β=0), ACT DR6 β (2.9σ), and the SPHEREx fNL forecast (2.6–5σ) without any explicit warning that the significances come from different null procedures, data sets, and estimators.[Abstract]
  - Sec. VI and Sec. XIII likewise place “σ(fNL)≈0.7 ⇒ 2.6–5σ” next to the β significances and the γPTA=2.567±0.382 value (with bounce prediction γPTA=3.0 at +1.13σ) without reiterating that these cannot be combined or compared as independent draws from the same null.
  - Fig. 6 caption emphasizes “SPHEREx fNL forecast is decisive (≳5σ on Stage III/IV survey timescales)” and “LiteBIRD targets a non‑zero β at ∼9σ” and quotes a 0.73σ difference between 0.27° and 0.342°,[Fig. 6] but again without a clear, upfront statement that these are three distinct statistical tests.
- **Why MAJOR:** You already flagged the comparability issue conceptually in P1A‑E5, but at the level of detailed editorial checks, these specific juxtapositions would almost certainly draw reviewer criticism. PRD’s standards for statistical interpretation are high.
- **Required fix:**
  - In each place where β, γPTA, and fNL significances are displayed side‑by‑side (abstract, Sec. VI, Sec. XIII, Fig. 6), add an explicit sentence such as: “These σ values arise from different data sets and null procedures and are not directly comparable or combinable.”
  - Consider de‑emphasizing σ language in the abstract, focusing instead on qualitative “detectable / testable” phrasing, reserving detailed σ comparisons for the main text with proper caveats.

---

P1A-M7 – Appendix C vs main‑text mapping of the ALP birefringence operator leaves a residual normalization ambiguity
- **Location:** Sec. IV D (Route 4), footnote 4; Appendix C, Eq. (C1)–(C4).
- **Problem (C, I):**
  - The main text and footnote 4 explain that the paper’s operator is \(-\tfrac14(α/M)\,ϕ F\tilde F\), with ϕ the canonical dim‑1 field and θ=ϕ/fa dimensionless, and that this matches the “canonical” ALP coupling \(g_{aγ}=(α_{\rm em}c_γ)/(2π f_a)\) only after nontrivial identifications. Appendix C then re‑derives β=(α/2M)Δϕ and claims that, under the identification \(α/M≡C_{aγ}α_{\rm em}/(2π f_a)\), the mapping matches the pipeline’s conventions.[Appendix C]
  - However, the body text also states that the chosen normalization is “−¼, not 1/(2π),” and that matching α/M=10⁻²¹ GeV⁻¹ in the canonical basis requires either fa∼MPl/10 or cγ∼O(10). This is not clearly reconciled with the Appendix’s assertion that the mapping “reproduces” the pipeline’s β formula.
- **Why MAJOR:** For Route 4, the central quantitative statement is that α/M fixed by β implies ρθ∼few×ρΛ at mθ∼H0; this hinges on the normalization of the ALP–photon term. Any residual factor‑of‑few ambiguity in the mapping to g_{aγ} changes the numeric overshoot and thus the strength of the “relocates CC problem” claim.
- **Required fix:**
  - Make the normalization chain fully explicit in one place (probably Appendix C): write the operator both in the paper’s convention and in the standard axion‑electrodynamics convention, derive the exact relation between α/M and g_{aγ}, and then plug the same α/M value into both the β and ρθ formulas.
  - In Sec. IV D, state clearly whether the overshoot “∼6 ρΛ” is robust to the factor‑of‑few normalization ambiguity; if not, downgrade the claim to an order‑of‑magnitude statement.

---

P1A-m5 – Internal cross‑references occasionally mis‑locate where a computation is actually done
- **Location:** Sec. IX–XII, Sec. XIV, Table III, captions.
- **Problem (D, I):**
  - Several places refer to “Sec. X G” for γPTA real‑KDE MCMC,[Fig. 1 caption; Sec. XIII] but Sec. X has subsections A–G dealing with perturbation transparency; the PTA analysis is only briefly summarized in Sec. XIII and attributed to “Paper III  §6.” This is confusing.
  - The text says “the scalar‑sector proof is in Sec. X B and the explicit Holst‑term verification at all perturbation orders is in Sec. X D,”[X. N] which is consistent with the section headings, but earlier references (e.g., abstract and Sec. I A) describe the result as “Sec. X” generically. That is harmless but slightly imprecise; more problematic is labeling B14 as “ECH Gates” in Table II without clearly pointing the reader to Sec. X, which is titled “The Perturbation‑Transparency Result,” not “ECH Gates.”[Table II]
- **Why MINOR:** A careful reader can eventually locate the material, but a referee will likely ask for cleaner cross‑referencing.
- **Required fix:**
  - Correct all γPTA cross‑references to point to Sec. XIII (where the number is actually quoted) and/or explicitly to companion Paper III §6.
  - Where B14 is mentioned as “ECH Gates,” add a parenthetical “(Sec. X)” on first occurrence.
  - Consider tightening generic “Sec. X” references in the abstract and introduction to “Sec. X B/D” when referring to the proof vs the explicit verification.

---

P1A-m6 – Some “consistent with / compatible / not tension” phrases lack quantitative back‑reference
- **Location:** Sec. II C (rotation term), Sec. III A/B, Sec. XI, Sec. XII B, Table III.
- **Problem (H):**
  - The rotation term is described as “completely negligible … ∼1.2×10⁻²¹ of ρΛ” but no uncertainty is specified on cω (other than “O(1)”) or on the observational bound (ω/H)₀<5×10⁻¹¹; the “completely negligible” claim is qualitatively fine but hides the fact that the factor‑of‑few uncertainty in cω is comparable to the quoted ratio.
  - Quintom‑B is described in Table III as “consistent†” with DESI w₀wₐ evidence,[Table III] with a footnote that no w₀wₐ MCMC was actually run in this program; the phrase “consistent” may mislead readers into thinking a quantitative check was performed. Similarly, in Sec. XIII the matter‑bounce prediction γPTA=3.0 is said to be “consistent with the data within standard frequentist tolerance” without giving the exact σ‑difference (1.13σ is only shown later in Table IV).
- **Why MINOR:** These do not change the structural conclusions, but they blur the line between quantitative and qualitative statements.
- **Required fix:**
  - Replace “consistent” / “no tension” phrases in such contexts with more explicit wording like “not in significant tension at the current 1.1σ–1.2σ level” where numbers are known, and “accommodates in principle” where no dedicated MCMC was run.
  - In Table III, add “(no dedicated w₀wₐ chains run in this work)” directly in the Quintom‑B footnote to avoid any ambiguity.

---

P1A-n3 – Figure 2 and Figure 3 captions over‑interpret schematic panels as quantitatively calibrated
- **Location:** Fig. 2, Fig. 3 captions; Sec. II C; Appendix B.
- **Problem (B, C, F):**
  - Fig. 2 is described as “illustrating the phenomenological scaling ansatz … the dilution waypoint quoted in the panel is the quantitative bookkeeping of Sec. XII A and Appendix B: Ntot≈92 with D_inf∼10⁻¹²¹.”[Fig. 2] But neither the figure nor the caption indicates any error bars or the fact that N_tot is only known to ±O(few) e‑folds from an ansatz with acknowledged dimensional inconsistencies.
  - Fig. 3 plots “ECH dark‑energy model vs ΛCDM H(z),” with the orange curve “using Ξ set to reproduce ρΛ” and quotes “∼2–3%” deviations over 0<z<3.[Fig. 3] Since Ξ is tuned to match ρΛ by construction using the phenomenological ansatz, the 2–3% deviations are not derived predictions; they are effectively a restatement that the model reproduces ΛCDM at that level given current cosmological parameter uncertainties. This is only partially clarified in the text.
- **Why NIT:** This is mostly a matter of presentation, but it affects how readers perceive the rigor of the quantitative claims.
- **Required fix:**
  - In both captions, explicitly label the panels as “schematic” and note that N_tot and Ξ are set by an illustrative scaling ansatz, not by a controlled EFT calculation.
  - Clarify in the main text that the 2–3% H(z) deviations are a graphic representation of the tuned model rather than an independent prediction.

---

If you want, I can now go through all explicitly quoted σ, p‑values, and percentages one‑by‑one and reconstruct them from the given numbers (e.g., 3.6σ from β=0, γPTA offset, SPHEREx forecasts) so you can patch any remaining arithmetic gaps before submission.