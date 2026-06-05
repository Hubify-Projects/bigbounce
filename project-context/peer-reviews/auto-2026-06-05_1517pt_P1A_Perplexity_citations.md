# P1A auto-2026-06-05_1517pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (14606 chars)
**Wall time**: 98.8s

---

P1A-E1 (ESSENTIAL) – Global: Companion papers [2], [6], , ,   
Problem: A large fraction of the paper’s quantitative claims and even some central narrative elements rely on “companion works in preparation” that do not exist as citable, peer‑reviewed documents. Examples include:  
- “[2] H. Golden, fNL = −35/8 Forecast: SPHEREx Discrimination of Bounce vs. Inflation, (in preparation) (2026), hUBIFY-2026-002; companion paper, this volume.”  
- “[6] H. Golden, Cobaya MCMC + NaMaster Birefringence + ALP Companion: Computational Verification for ECH Structural Closure, (in preparation) (2026), hUBIFY-2026-001B; companion paper, this volume.”  
- “ H. Golden, Galaxy Chirality at Scale: 8.47M Galaxies Classified, Hemisphere Null at pLEE < 10−4 , (in preparation) (2026), hUBIFY-2026-004; companion paper, this volume.”  
- “ H. Golden, Spectrally Unusual Sources at Scale: … (in preparation) (2026), hUBIFY-2026-003; companion paper, this volume.”  
- “ H. Golden, Systematic closure of minimal first-principles routes to dark energy in Einstein-Cartan-Holst gravity (2026), companion technical note, available upon request from the author.”  

None of these have arXiv IDs, DOIs, or journal information; they are not verifiable. Yet the paper uses them for:  
- The stated MCMC cosmological parameters (H₀, ΔN_eff, σ₈, etc.).  
- The claimed SPHEREx f_NL forecast significance.  
- The galaxy spin null result.  
- PTA γ re‑analysis.  
- Further theoretical support for the ECH “closure.”  

Required fix: Either (a) publicly post these works with stable identifiers (arXiv or equivalent) and adjust the manuscript to reference only results that actually appear in those posted texts; or (b) remove all results that depend on them and re‑derive any essential statements fully within this paper or from existing, published literature. As long as central quantitative statements rely on inaccessible “internal” documents, this is not acceptable for PRD.

---

P1A-E2 (ESSENTIAL) – Abstract & throughout: Misuse of “this volume” and internal labels  
Problem: Multiple references use “this volume” and internal labels, implying a proceedings or special‑issue context that does not exist, and which is not meaningful to a stand‑alone PRD article:  
- “[2] … companion paper, this volume.”  
- “[6] … companion paper, this volume.”  
- “ … companion paper, this volume.”  
- “ … companion paper, this volume.”  

Similarly, labels such as “hUBIFY-2026-001B” are internal (self‑assigned) report numbers, not standard bibliographic identifiers.

Required fix: Replace “this volume” and internal report codes with proper bibliographic references (journal, arXiv ID) if available; otherwise remove them. Any companion work not yet publicly available must be described as “in preparation” without implying co‑publication, and crucial results must not depend on them (see P1A‑E1).

---

P1A-E3 (ESSENTIAL) – Abstract & Sec. X: “Theorem” claim vs. literature  
Problem: The paper states a “perturbation‑transparency theorem” that torsion vanishes at all perturbation orders and the Holst sector decouples for canonical scalars (abstract; Sec. X). The core fact that torsion vanishes when there is no spin current is standard Einstein–Cartan theory (e.g., Hehl et al. 1976[3]). The extension “at all perturbation orders” with Holst is asserted but not justified by a detailed perturbative calculation in the paper, and no external reference is cited that demonstrably proves the claimed “all orders” result in an FRW + perturbations setting.

Required fix: Provide a fully explicit derivation (including the perturbative expansion to at least cubic order in scalar and tensor modes) or a precise, verifiable citation that has already done this in the Holst+scalar setting. Alternatively, weaken the claim from a “theorem” / “at all orders” statement to a carefully qualified statement clearly labeled as an extension of known EC results, with the limitations and assumptions spelled out.

---

P1A-E4 (ESSENTIAL) – Global: Internal “status” / version‑history language  
Problem: The manuscript contains multiple instances of internal workflow / version‑history language explicitly forbidden in the review instructions:  
- “This figure supersedes the earlier synthetic‑Gaussian-likelihood value γ = 3.20 ± 0.42 used in pre-real-KDE drafts; the migration is documented in Paper III § 6.”  
- “not the value quoted in Ref. ” vs. “earlier drafts” in Appendix B.  
- Numerous “earlier drafts” / “pre‑real‑KDE drafts” / “synthetic‑likelihood value” style comments.  

Required fix: Remove all language referring to earlier drafts, internal audit history, or previous versions of the work. Present only the final derivations and numbers with clear references.

---

P1A-E5 (ESSENTIAL) – Eq. (15) and Route‑2 amplitude estimate: Dimensional consistency and traceability  
Problem: Eq. (15) gives a dimensionless ratio for Δθ_one-loop / Δθ_obs and claims an enormous suppression (10⁻⁵⁸–10⁻⁶⁰). The construction mixes α_em, H₀/M_Pl, α/M, and β_obs, but the normalization of the one‑loop operator (14) is explicitly acknowledged not to be taken from a standard published derivation; it is called an “EFT ansatz,” and the mapping to β is not demonstrated via a concrete calculation or citation to Mercuri & Capozziello or Shapiro & Teixeira that actually compute cosmic birefringence from the given operator. Therefore the claimed 30+ orders of magnitude gap is not traceably supported by cited literature, but rather by a bespoke, implicitly dimension‑dependent normalization.

Required fix:  
- Either provide a literature‑traceable derivation of the one‑loop birefringence amplitude from the Holst/Nieh–Yan operator, with the exact normalization used, or clearly mark the entire Δθ_one-loop estimate as a rough, order‑of‑magnitude scaling assumption, not a quantitative exclusion.  
- In either case, ensure that the units are tracked systematically. A reader must be able to reproduce the ratio numerically from the displayed equations without hidden conversion factors.

---

P1A-E6 (ESSENTIAL) – Appendix B & Sec. II C: Cosmological constant hierarchy numerics and consistency  
Problem: Appendix B asserts that earlier drafts “misstated” the hierarchy as ∼35 orders of magnitude and now state correctly that M_Pl⁴/ρ_Λ ∼ 10¹²². Yet the main text still uses a specific value N_tot ≈ 92 and occasionally ∼94 e‑folds to connect bounce‑scale densities to ρ_Λ via Eq. (B2). This mapping depends on:  
- The ad hoc scaling ansatz ρ_Λ^bounce ∼ (α/M) M_Pl⁵ (B2), which is not derived from the ECH action or any cited EFT construction.  
- A phenomenological dilution D_inf ∼ e⁻³N_tot (T_reh/M_GUT)³/², itself only partially justified, and explicitly labeled as “dimensional‑analysis aesthetic” rather than computed.  

Yet the paper uses N_tot ≈ 92 as a “structural tension” headline number (abstract, Sec. I, Sec. XIV D).

Required fix:  
- Make absolutely explicit, in the abstract and main text, that N_tot ≈ 92 and the “105 sensitivity to ΔN_tot ≈ 4” are not derived predictions but artifacts of stacking multiple phenomenological ansätze.  
- Remove any implication that ECH “reduces the CC hierarchy” from 10¹²² to 10⁵. It does not; it merely re‑labels fine‑tuning in terms of N_tot.  
- Provide a clear numerical derivation of N_tot from Eq. (B2) and Eq. (11) with all intermediate steps and parameters specified (M, α/M, T_reh, M_GUT, etc.), so the reader can verify the numbers.

---

P1A-E7 (ESSENTIAL) – Use of DESI “3.1–4.2σ“ claim for evolving dark energy [9,10]  
Problem: The introduction states: “DESI 2024–2025 BAO results suggest dynamical dark energy at 3.1–4.2σ (dataset‑dependent) [9, 10].” Checking Adame et al. 2024 BAO and Abdul-Karim et al. 2025 DESI DR2 constraints shows that while tensions relative to w = −1 are discussed, the exact range “3.1–4.2σ” with that specific wording does not appear in the abstracts; the numbers depend strongly on combined datasets and priors. The paper does not show how those particular σ‑values are obtained from the cited works.

Required fix:  
- Either (a) quote directly and precisely the significance as reported in the cited DESI papers, with the corresponding dataset combination explicitly named, or (b) if this is the author’s own re‑analysis, move the claim into a separate, fully documented subsection with equations, likelihoods, and explicit methodology, or remove it.  
- The current formulation reads as an untraceable, inflated headline number.

---

P1A-E8 (ESSENTIAL) – Reliance on private PTA re‑analysis  for γ_PTA  
Problem: The paper uses “γ = 2.567 ± 0.382 from real-KDE re‑analysis of the 15-yr free-spectrum data (GPU MCMC, companion Paper III )” as an input to Table III and Sec. XIII. This value and method are not present in any published NANOGrav (or EPTA, PPTA, IPTA) paper and are not described in this manuscript.

Required fix: Remove γ_PTA and any claims based on this private re‑analysis, unless a fully reproducible, self‑contained analysis is added here (or a public arXiv paper is cited), including: data description, likelihood, KDE construction, priors, and convergence checks. PRD cannot accept as evidence a parameter value published only in a non‑archived “companion” document.

---

P1A-E9 (ESSENTIAL) – Multiple “in preparation” claims used as load‑bearing evidence  
Problem: The abstract and several sections treat results from “works in preparation” as if they were established facts, e.g.:  
- “a detailed multi-tracer SPHEREx Fisher forecast is presented in a companion work in preparation [2]” yet the main text uses “3–5σ realistic” as if already vetted.  
- “ΛCDM+ΔN_eff MCMC verification, NaMaster pipeline validation, and ALP parameter fitting are documented separately in companion work in preparation [6]” but numerous quantitative numbers (H₀, ΔN_eff) are imported.  

Required fix: All such usage must be downgraded to “anticipated” or removed, with the main claims of this paper reformulated so that they depend only on results that are either fully derived here or traceably published.

---

P1A-E10 (ESSENTIAL) – Unsupported claim of uniqueness / novelty  
Problem: Sec. VIII claims: “No prior work assembles these into a single quantitative framework with systematic barrier testing.” The references [11–15,19–22, etc.] indeed do not present this specific “barrier catalog,” but the statement is broad enough to imply a general claim of uniqueness which is not substantiated by a comprehensive survey.

Required fix: Soften and qualify the novelty claim, e.g., “To our knowledge, explicit cataloguing of these 14 mechanisms within minimal ECH, in this particular organizational form, has not been presented before.” Remove implications that no one has ever systematically analyzed dark‑energy routes in EC/Holst frameworks unless backed by a review of the literature.

---

P1A-M1 (MAJOR) – References with incomplete or non‑standard metadata  
Problem: Several references do not give full/standard journal and year information although those are available:  
-  Lue, Wang & Kamionkowski: Phys. Rev. Lett. 83, 1506 (1999). Only “Phys. Rev. Lett. 83, 1506” is implicit in the text; year is omitted in the reference list.  
- A number of recent works [41–45] are cited as arXiv e‑prints with projected years 2025–2026, which are plausible but must match the actual arXiv records. The manuscript does not give arXiv IDs for them, only “(2025)” or “(2026)”.  

Required fix: For every reference that is not “in preparation,” supply complete metadata: author list, full journal name, volume, page, year, and arXiv ID if applicable. For arXiv‑only references, provide arXiv:YYMM.NNNNN with subject class. Remove any guesswork “(2025)” / “(2026)” year tags that do not match the actual submission date once checked.

---

P1A-M2 (MAJOR) – Self‑citations with internal prefixes and no external identifier  
Problem: References [2], [6], , ,  use custom report labels like “hUBIFY‑2026-002” but no arXiv IDs or DOIs. This is not standard for PRD and hinders bibliographic indexing.

Required fix: Replace internal report numbers by standard bibliographic identifiers once the works are public. If they will not be made public, remove them from the reference list and from the text (or clearly label them as “private communication” and ensure that no essential result depends on them).

---

P1A-M3 (MAJOR) – Use of Planck/LQG parameters without consistent citation  
Problem: The text cites specific values for the Barbero–Immirzi parameter and LQC critical density:  
- γ_U(1) ≈ 0.127, γ_SU(2) ≈ 0.274, γ_DLM ≈ 0.2375, claiming origin in [16–18].  
- ρ_crit ≃ 0.27–0.41 ρ_Pl, attributing part of this to “internal extrapolation across counting schemes (not a value quoted in Ref. ).”  

In [16–18], Ashtekar et al. and Domagala–Lewandowski–Meissner indeed give certain numerical γ values, but the ranges and error‑like “±0.020” interpretation are subjective. The manuscript states “Domagala–Lewandowski and Meissner do not quote a ±0.020 statistical uncertainty… retained as an effective range only” but still uses it in a parameter table.

Required fix:  
- For γ and ρ_crit, quote directly the values as given in the original papers, clearly distinguishing between published numbers and any extrapolated or “effective range” the author introduces.  
- Remove any pseudo‑error bar notation that could be mistaken for a quoted uncertainty.  

---

P1A-M4 (MAJOR) – Claims about DESI H₀ / σ₈ “tension resolution”  
Problem: Table I states “H₀/σ₈ tension resolution? – H₀ = 67.68 ± 1.06, ΔN_eff ≈ 0 – Recovers ΛCDM.” This is not a DESI result; it is explicitly based on the author’s private MCMC [6]. Presenting it in the executive summary alongside “DESI” items risks conflating outcomes.

Required fix: Move all statements that depend on private MCMC into a clearly marked subsection, and explicitly state that they are internal analyses, not DESI or Planck results. The executive summary table should not mix external experiment status with private “verification” numbers.

---

P1A-M5 (MAJOR) – Use of SPHEREx f_NL forecast without in‑paper derivation  
Problem: The text states “σ(fNL) ≈ 0.7 — detailed Fisher forecast in companion work in preparation [2]” and uses “3–5σ realistic” in the main claims. Heinrich et al. 2024 indeed find σ(fNL) ≈ 0.7 for certain configurations, but the mapping from their setup to the specific matter‑bounce forecast, including GR projection and bias priors, is not shown here and is relegated to [2].

Required fix:  
- Either provide a brief but complete SPHEREx Fisher derivation (equations, survey specs, shapes, and the impact of systematics) in an appendix, or else cite Heinrich et al. alone and refrain from quoting a customized “3–5σ realistic” range that depends on unseen assumptions.  
- Clearly state that the −35/8 value is from Cai et al. 2009[1] and that this paper does not recompute it.

---

P1A-M6 (MAJOR) – Ambiguous statement on “confirmed null” galaxy spin result  
Problem: The paper says: “An independent ViT-Small chirality classifier … confirms the null at the dipole level… reported in Paper IV . Galaxy spin asymmetry is not a prediction of the theory.” Later: “The galaxy spin channel is a confirmed null … full quantitative chirality results in Paper IV .” Since  is not public, this “confirmed null” is a private claim.

Required fix: Either publish the galaxy spin analysis (arXiv) and provide at least an abridged methodology and key statistics in this paper, or rephrase to “our internal analysis indicates no significant dipole, but this result will be presented elsewhere; we therefore treat spin asymmetry as unconstraining here.” Do not present it as a confirmed observational fact without a citable analysis.

---

P1A-M7 (MAJOR) – “Reheating thermal‑reset barrier” – no supporting citation  
Problem: The “reheating thermal‑reset barrier” section asserts detailed statements about axial current damping and the thermal erasure of torsion memory, but provides only generic references to EC theory and no finite‑temperature calculation or literature reference that explicitly demonstrates such a reset in EC/Holst cosmology.

Required fix: Either supply a calculation (even schematic) that shows how ⟨J_5^μ⟩ → 0 in the EC context and how this translates into the claimed erasure of bounce torsion, or add a clear statement that this is a qualitative, heuristic argument, not a derived theorem. Remove its use in any quantitative “barrier” that purports to be rigorous.

---

P1A-M8 (MAJOR) – Claims about birefringence significance vs β = 0  
Problem: The manuscript quotes “β_obs = 0.342° ± 0.094° (~3.6σ from β=0)” and “ACT DR6 β = 0.215° ± 0.074° at ~2.9σ.” Checking Eskilt & Komatsu 2022[4] and Diego‑Palazuelos & Komatsu 2025[5], the central values and errors are plausible, but the combined significances and the combined interpretation are not derived here; moreover, recent literature continues to debate these results. Presenting them as uncontested “detections” is misleading.

Required fix:  
- Stick to the precise statements in [4] and [5]; quote their stated significance and caveats.  
- Explicitly acknowledge that cosmic birefringence is under active investigation and that systematics remain an issue; avoid using it as an unequivocal “3.6σ detection” without qualification.

---

P1A-M9 (MAJOR) – Table II barrier labels vs. actual derivations  
Problem: Several “barriers” (e.g., Barrier 5 “Scale separation,” Barrier 6 “Attractor‑sensitivity dilemma,” Barrier 9 “Liouville conservation”) are presented as crisp mechanism‑blocking statements but are not formally derived; they are qualitative arguments without equations or explicit references that tie them to established results.

Required fix:  
For each barrier in Table II, either:  
- Provide a concise, explicit derivation or a clear citation where the core statement is rigorously shown; or  
- Reclassify them as “heuristic structural observations” and separate them from those constraints that are genuinely quantitative and derived in this paper. The paper should not implicitly elevate all 14 “barriers” to the same level of rigor if that is not the case.

---

P1A-M10 (MAJOR) – Use of speculative future experiments and dates  
Problem: The text repeatedly commits to specific future experiment timelines and capabilities, e.g., “SPHEREx (2028)”, “LiteBIRD (early 2030s) with σ(β) ≈ 0.03°”. While such projections exist in official mission papers, the manuscript often uses them as if guaranteed, and uses future dates as anchors in the argument.

Required fix: Phrase all future experimental projections as conditional and cite the mission white papers explicitly. Avoid assigning concrete calendar years unless they correspond to official, current plans in the cited documents.

---

P1A-M11 (MAJOR) – Overly long and repetitive for the actual technical content  
Problem: The manuscript is 21 pages with extensive narrative, cross‑references to non‑existent companions, and repeated explanations of the same points (e.g., that the parity‑odd operator has wrong mass dimension, that α/M is phenomenological, that ECH does not solve the CC problem). Given that no new, fully explicit calculation is presented for the core “no‑go” beyond qualitative dimensional arguments, the length is disproportionate to the actual, verifiable technical contribution.

Required fix: Condense to ~12–14 pages focused on:  
- Clear definition of the four channels.  
- A compact, explicit demonstration of why each fails, with minimal reliance on speculative ansätze.  
- A brief discussion of perturbation transparency with either a solid derivation or precise citations.  
Remove narrative digressions and internal program roadmapping (Paper I(b), II, III, IV, etc.), which belong in a project overview, not a PRD research article.

---

P1A-N1 (NIT) – Duplicate and awkward phrases  
Problem: There are a number of minor stylistic issues:  
- Repeated phrases like “channel‑level amplitude closure” and “amplitude‑budget granularity” throughout.  
- Occasional awkward duplication, e.g., “canonical LQC value ρ_crit ≃ 0.41 ρ_Pl … gives ρ_crit ≃ 0.27 ρ_Pl; this lower value is an internal extrapolation…” where two different “canonical” values are referenced closely.  

Required fix: Edit for conciseness and clarity. Avoid repeated jargon; define it once and then use simple terminology.

---

P1A-N2 (NIT) – GitHub link and AI acknowledgement in a PRD article  
Problem: The data/code section gives a GitHub URL and a “tree/main/reproducibility” path. PRD typically allows code‑availability statements but URLs can change; also, the “Acknowledgments” section explicitly thanks a commercial AI system (Claude) used as a “research assistant,” which is unconventional for a theoretical physics paper and may not pass APS policy scrutiny without clarification.

Required fix:  
- Retain a generic “code available upon request / on a public repository” statement, but ensure that any essential data are archived in a stable form (e.g., Zenodo with a DOI).  
- Check APS policy on AI acknowledgments; if allowed, clarify that AI tools were used only for drafting assistance, not for generating scientific content or numerical results. Otherwise, remove or neutralize this sentence.

---

## Summary recommendation

REJECT

The manuscript attempts an ambitious “channel‑level” no‑go analysis for Einstein–Cartan–Holst dark‑energy routes but relies heavily on non‑public “companion” works for core numerical inputs, uses phenomenological ansätze in place of controlled derivations while presenting the results as rigorous “barriers,” and contains multiple citation and metadata issues that do not meet PRD’s standards of traceability and rigor. To be publishable, the work would need substantial restructuring, elimination of dependence on unpublished analyses, and replacement of heuristic arguments by explicit calculations or precise literature‑based theorems; this goes well beyond “major revisions.”

---

## PASS 2 — self-critique findings (what initial review missed)

P1A-E11 (ESSENTIAL) – EB formula and “β ≈ 0.27°” benchmark: internal inconsistency and unsupported central value  
Problem: The EB–rotation relation is written as  
\(C_\ell^{EB} \approx 2\beta C_\ell^{EE} - C_\ell^{BB}\) (Eq. 12), but the standard small‑angle result is \(C_\ell^{EB} \simeq 2\beta C_\ell^{EE}\) with *no* minus‑\(C_\ell^{BB}\) term for a uniform rotation; the extra \(-C_\ell^{BB}\) is dimensionally allowed but not derived or justified and will numerically alter forecasts and parameter fits. The paper then uses a benchmark “β ≈ 0.27°” as if it were a meaningful central prediction (midpoint between 0 and 0.342°) but never defines how that number is obtained or propagated; it is not a posterior mean, not quoted in [3–5], and not derived from any likelihood in this manuscript.  

Required fix:  
- Correct Eq. (12) to the standard uniform-rotation expression or explicitly derive and justify the \(-C_\ell^{BB}\) term, including how it enters Fisher forecasts and parameter estimation.  
- Either remove “β ≈ 0.27°” as a benchmark, or clearly define it as an arbitrary illustrative midpoint, not a prediction or fit; do not assign it the same status as β_obs values taken from published analyses.  

---

P1A-E12 (ESSENTIAL) – Mis‑handled cosmic‑birefringence significance and LiteBIRD “9σ” forecast  
Problem: The manuscript repeatedly states β_obs = 0.342° ± 0.094° is “∼ 3.6σ from β = 0” and β_ACT = 0.215° ± 0.074° is “∼ 2.9σ,” then claims LiteBIRD with σ(β) ≈ 0.03° will detect non‑zero β at “∼ 9σ.” However:  
- 0.342°/0.094° ≈ 3.64 is arithmetically correct, but the paper treats this as an uncontested “3.6σ detection” throughout (abstract; Sec. III A; Sec. XII B; XV), without reproducing or even sketching the null‑test methodology, lensing/systematics marginalization, or alternative analyses that reduce the significance, contrary to [4,5].  
- The “∼9σ” LiteBIRD claim is computed as 0.27°/0.03° = 9 but then used as if it were the discovery significance relative to the current β_obs, even though the consistent comparison is to β = 0 (new experiment alone) or to the joint posterior combining Planck+LiteBIRD, which is not derived. The later text partially corrects this (Sec. XIII, XV) by pointing out that the differential test against β_obs is only ≈0.7σ, contradicting the earlier “9σ” emphasis that appears in the conclusions.  

Required fix:  
- Limit all “σ” statements to those explicitly reported in the original birefringence papers and quote their caveats; where you recompute significances, show the inputs and clarify the null hypothesis (β = 0 vs. difference between experiments).  
- Remove or carefully rephrase the “∼9σ” LiteBIRD statement from the abstract, Sec. VII, Sec. XV unless you explicitly separate “internal detection relative to β = 0” from “differential test relative to current β_obs,” and make clear that LiteBIRD cannot distinguish 0.27° from 0.34° at high significance.  

---

P1A-E13 (ESSENTIAL) – Inconsistent use of Λ hierarchy numbers and N_tot mapping (Appendix B vs. main text)  
Problem: Appendix B derives N_tot ≈ 94 from the true Planck‑to‑Λ hierarchy \(M_{\rm Pl}^4/ρ_\Lambda \sim 10^{122}\) using \(D_{\rm inf} \sim e^{-3N_{\rm tot}} \sim 10^{-122}\), then states this is “consistent at the ∼2% level with the structural‑tension N_tot ≈ 92 quoted in Sec. XIV D,” attributing the difference to ansatz choices in Eq. (B2). However:  
- The main text (abstract; Sec. II C 1; Sec. XII A; Sec. XIV D) continues to foreground N_tot ≈ 92 and a “10^5 sensitivity to ΔN_tot ≈ 4” without ever explicitly walking the reader through the numerical steps from the *on‑shell* ansatz (B2) to N_tot ≈ 92 and then reconciling that with the “true” 10^122 hierarchy.  
- The abstract still says “structural tension…requires N_tot ≈ 92 post‑bounce e‑folds” despite Appendix B explicitly acknowledging that 92 versus 94 is ansatz‑dependent and order‑of‑magnitude only.  

Required fix:  
- In the abstract and every place N_tot ≈ 92 is mentioned, explicitly qualify it as an order‑of‑magnitude value derived from the phenomenological scaling ansatz (B2), and cross‑reference the Appendix B discussion that the true Planck‑to‑Λ hierarchy corresponds to ≈94 e‑folds.  
- Provide a transparent, step‑by‑step numerical derivation of N_tot ≈ 92 from Eq. (B2) and Eq. (11) *in the main text* (not just in Appendix B) so that readers can reproduce it, and clearly distinguish that bookkeeping from the physical 10^122 hierarchy.  

---

P1A-E14 (ESSENTIAL) – Misleading presentation of “Ω_GW^ECH ≤ 0.07–0.17” ceiling vs PTA measurements  
Problem: Barrier 12 defines an upper bound  
\(\Omega_{\rm GW}^{\rm ECH}|_{\rm bounce} \lesssim (ρ_{\rm crit}/ρ_{\rm Pl})^2 ≃ 0.07–0.17\) (Eq. 20) and then states this is “not directly comparable to the present‑day PTA spectral‑density measurement Ω_GW(f_nHz) ∼ 10⁻⁹” and hence used only as a “global energy‑density‑fraction ceiling.” However:  
- The square \((ρ_{\rm crit}/ρ_{\rm Pl})^2\) is dimensionally odd: both ρ’s have units of energy density, so their ratio is dimensionless; squaring it produces an \(O(10^{-1})\) number that is physically *much* larger than unity, unlike standard constraints on the *total* energy density in primordial GWs near the Planck era, and the paper provides no derivation (just “we have used the window ρ_crit/ρ_Pl ≃ 0.27–0.41”).  
- Presenting 0.07–0.17 next to ∼10⁻⁹, even with a verbal caveat, invites misinterpretation; it also conflicts with basic BBN/CMB bounds that limit integrated GW energy at early times to well below order unity.  

Required fix:  
- Either remove Eq. (20) entirely or derive it carefully: define the quantity whose upper bound you are quoting (instantaneous GW fraction at the bounce? integrated over frequency? relative to total radiation?) and ensure that the factor of \((ρ_{\rm crit}/ρ_{\rm Pl})^2\) is dimensionally and physically meaningful.  
- If you cannot present a controlled calculation consistent with BBN/CMB bounds, restrict Barrier 12 to a qualitative statement about “vacuum amplification ceilings” and explicitly state that any quantitative comparison to PTA Ω_GW is deferred.  

---

P1A-E15 (ESSENTIAL) – “All orders” perturbation‑transparency theorem remains under‑derived  
Problem: Sec. X still states a theorem‑like result: “torsion vanishes at all perturbation orders…Holst term therefore decouples from all scalar/tensor perturbation equations of motion,” yet the “proof” is just the standard chain: (i) scalar has no spin; (ii) torsion is algebraic in spin; (iii) Holst term reduces to Pontryagin density for torsion‑free connection, which is a total derivative (Eq. 23). This correctly reproduces the *background* EC result but:  
- It does not show an explicit perturbative expansion of the action (e.g., to cubic order in scalar/tensor modes) demonstrating that no Holst‑dependent vertices contribute; the bispectrum statement “receives zero contribution” is asserted without a displayed cubic action or any variation.  
- It does not address subtleties like boundary terms on finite patches, possible contributions from nontrivial topology, or whether field redefinitions used in the background carry through order by order in perturbation theory.  

Required fix:  
- Either provide a concrete perturbative calculation (explicit quadratic and cubic actions in ζ and h_ij, showing the absence of γ‑dependent terms), or rephrase the result as a carefully qualified extension of the standard EC torsion‑vanishing fact, not as an “all orders” theorem. The bispectrum and “all perturbation orders” claims in the abstract and Sec. X should be softened unless backed by an explicit computation or an external reference that has already done this in the Holst+scalar setting.  

---

P1A-M12 (MAJOR) – Arithmetic and unit issues in the Route‑2 birefringence suppression estimate  
Problem: The Route‑2 suppression factor (Eq. 15) is presented as  
\(\Delta θ_{\rm one-loop}/\Delta θ_{\rm obs} ∼ α_{\rm em}(H₀/M_{\rm Pl})·M / [4π M_{\rm Pl} · α · β_{\rm obs}] ∼ 10^{-58} – 10^{-60}\). The text acknowledges a previous missing factor of 1/M_Pl and a “factor‑of‑∼100 ambiguity,” but:  
- The derivation is not transparent: H₀/M_Pl ≈ 10⁻⁶¹ is asserted; α/M ≈ 10⁻²¹ GeV⁻¹ is quoted; M_Pl ≈ 10¹⁹ GeV; β_obs ≈ 6 × 10⁻³; yet the intermediate step “M_Pl·(α/M) ∼ 10⁻²” is just dropped in, with no consistent choice of units. Plainly multiplying the stated numbers gives ~10⁻⁵⁷–10⁻⁵⁸, but this mixes eV and GeV and uses H₀ “in eV” without ever specifying the conversion; the reader cannot reproduce 10⁻⁵⁸–10⁻⁶⁰ cleanly.  
- The paragraph explicitly admits that a different ordering of factors gives 10⁻³³ instead of 10⁻⁵⁸, and then says the closure is “robust to this choice,” which undercuts the claim of a 30‑orders‑of‑magnitude gap.  

Required fix:  
- Rewrite the Route‑2 estimate with a consistent unit system (e.g. natural units with M_Pl = 2.4×10¹⁸ GeV and H₀ in GeV), show each numerical step, and state clearly which conventional definitions you use (reduced vs. unreduced M_Pl).  
- Then classify the result as an *order‑of‑magnitude bound*, not a precise “10⁻⁵⁸–10⁻⁶⁰” exclusion. Make explicit that depending on normalization conventions one obtains ∼10⁻³³ to 10⁻⁵⁹, and that the only robust statement is that Route‑2 is utterly negligible, not that it lies a specific number of decades below the observed signal.  

---

P1A-M13 (MAJOR) – EB / TB “tensor chirality” barriers vs. perturbation transparency: mixing different null procedures  
Problem: Barrier 8 (parity‑even interaction) and Barrier 14 (perturbation transparency) both speak about “tensor chirality” and “no TB/EB from ECH,” while the observational section uses EB from isotropic *rotation* (β) driven by an ALP, not from primordial GW chirality. These are different null procedures:  
- EB from uniform β probes a parity‑violating *photon‑sector* coupling (rotation of linear polarization).  
- EB/TB from tensor chirality probe opposite‑helicity GW power sourcing from the primordial tensor sector.  

The text sometimes conflates them in language (“CMB birefringence channel provides the surviving parity‑violation evidence” immediately followed by “parity‑even interaction…cannot generate tensor chirality”), and Table II lists both as closing the “same observable channel,” when in fact a nonzero β is perfectly compatible with zero tensor chirality.  

Required fix:  
- Explicitly separate “birefringence (β)” from “tensor chirality” in the barrier taxonomy and in Secs. III, IX, and X: they probe different operators and use different null procedures, and their σ‑levels are not directly comparable.  
- In Table II, clarify that B8/B14 refer to *tensor chirality* (GW‑induced TB/EB) and do not constrain ALP‑induced β, and ensure the narrative does not treat the existing β_obs as a constraint or confirmation of those barriers.  

---

P1A-M14 (MAJOR) – SPHEREx f_NL “3–5σ realistic” significance inconsistently presented and arithmetically shaky  
Problem: The SPHEREx forecast is described multiple times as “σ(f_NL) ≈ 0.7 — 3–5σ realistic,” with more detail in footnote 1: start from |f_NL|/σ = 4.375/0.7 ≈ 6.25σ Fisher‑ideal, apply a “template‑overlap” factor r ≈ 0.84 (to ~5.25σ), then additional GR‑projection and photo‑z degradation to σ(f_NL) ≈ 1.0 giving “3–5σ realistic.” However:  
- There is no quantitative propagation from the 0.84 overlap to the 3–5σ final range; the reader is asked to take on faith that GR projection and photo‑z increase σ from 0.7 to ~1.0 and that this maps to 3–5σ, but no explicit numbers (e.g. correlation matrices, marginalizations) are shown.  
- The abstract and executive summary Table I still present “3–5σ realistic” as if it were a robust prediction of this paper, despite being entirely imported from a non‑public companion [2].  

Required fix:  
- Either (a) bring into this paper a concise but explicit Fisher calculation using Heinrich et al. 2024’s σ(f_NL) ≈ 0.7, showing how each degradation (shape overlap, GR projection, bias priors, photo‑z) modifies σ quantitatively; or (b) soften to “of order few‑σ” and clearly attribute any specific 3–5σ range to forthcoming work, not to calculations performed here.  
- In the abstract and Table I, avoid precise σ ranges unless they are independently reproducible from the equations and numbers in this manuscript.  

---

P1A-M15 (MAJOR) – Abstract and body still over‑state novelty after softening attempt  
Problem: Sec. VIII has been partly softened (“No prior work assembles these into a single quantitative framework with systematic barrier testing”), but the abstract still frames the work as establishing a “central result” perturbation‑transparency theorem and “channel‑level closure…at amplitude‑budget granularity,” implying a level of systematic, quantitative completeness across all four routes that is not supported, given:  
- Several barriers (5, 6, 7, 9, 10, 13) are explicitly qualitative, heuristic, or philosophical (“no mechanism…within ECH” without a formal no‑go theorem).  
- Key numerical inputs (γ_PTA, σ(f_NL), β ≈ 0.27°, N_tot ≈ 92) still depend on unpublished companions or phenomenological ansätze.  

Required fix:  
- Further soften the novelty claims in the abstract and Sec. I A: describe this as a “framework organizing known constraints into a channel‑level audit” rather than as a comprehensive “closure,” and distinguish clearly between rigorous amplitude bounds (Routes 1–3, parts of Route 4) and more heuristic structural/principle‑based barriers.  
- Add an explicit sentence early on (e.g. end of abstract or Sec. I A) stating that many barriers are qualitative consistency arguments rather than derived theorems, and that a full operator‑basis closure remains open.  

---

P1A-m2 (MINOR) – Confusing use of “verified value” and pseudo‑errors in Table IV  
Problem: Table IV lists γ = 0.274 with “scheme range ∼ 0.020” and calls it “Verified Value,” and ρ_crit/ρ_Pl ≃ 0.27–0.41 is later interpreted via a “∼0.020” spread as an “effective range.” These are not statistical errors but differences between counting schemes, yet the table’s layout (single number plus “range”) makes them look like uncertainties of a fitted parameter.  

Required fix:  
- In Table IV and the surrounding text, clearly separate “fixed theoretical inputs with scheme variation” from “fitted parameters with uncertainties.” For γ and ρ_crit, drop the “∼0.020” range from the “Verified Value” column and instead explain in a note that different schemes give discrete values 0.2375, 0.274, etc., without a statistical error bar.