# P4 auto-2026-06-05_1617pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (14565 chars)
**Wall time**: 93.5s

---

P4-E1 (ESSENTIAL)  
Section: Title and throughout; Reference list, page 9–10  
Problem: The manuscript repeatedly refers to “σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I for the mapping of each result to its null.” Yet several sections juxtapose significances from different null procedures without restating this caveat locally, in particular:  
- Abstract: “The MASTER-deconvolved single-mode pseudo-C1 … yields −0.122σ … The real-space post-TTA Catalog C dipole is +0.43σ (p = 0.30, isotropic-null bootstrap, NMC = 10,000).”  
- Sec. III.A (Declared Analysis Hierarchy, p.3): “(i) … σdipole = 0.43 … (ii) … −0.122σ. (iii) … +3.64σ; and (iv) hemisphere maximum-asymmetry (3.05σ local maximum; Appendix C).”  
- Sec. IV.D, IV.E, VI.A, VII: multiple places place +3.64σ, +6.48σ, 0.43σ, −0.122σ side by side.  
This violates the explicit instruction in the review brief that sigma values from different null procedures must be explicitly labelled “not directly comparable” at every juxtaposition.  
Required fix: At every location where two or more σ significances from different null procedures are placed side by side (abstract, Sec. III.A, IV.C–E, VI, VII, table captions), add an explicit local statement that these σ values are defined with different null procedures and must not be directly compared, or re-express comparisons in terms of p-values or effect sizes with clear explanation of the differing nulls.

---

P4-E2 (ESSENTIAL)  
Section: Abstract, first paragraph, page 1; Sec. IV.A/Table II, p.3–4  
Problem: The abstract states “We report … 3,201,160 DESI Legacy spiral galaxies (8.47 M sources, 471 049 high-confidence per-spiral after peqCW > 0.9).” In the body, the only explicit high-confidence subsample size is “HC-spiral subsample (N = 471,049, NMC,null = 1000, NMC,inj = 100 per amplitude)” in Sec. VI.A. There is no definition of “peqCW > 0.9” in the main text; elsewhere “HC-broad-0.6 (peq > 0.6, N = 949,584)” and “HC-strict (peq > 0.8, N = 624,660)” are used, but no 0.9 cut is defined. This is an internal inconsistency in the key scalar in the abstract.  
Required fix: Explicitly define the 471,049 high-confidence subset in the Methods/Results (including the exact probability threshold and whether it is peq, pCW, or something else), and make sure the threshold used in the abstract matches this definition. If the 471,049 subsample actually uses peq > 0.8 or some other cut, correct the abstract accordingly.

---

P4-E3 (ESSENTIAL)  
Section: References [1]–[4], page 9–10  
Problem: The citations for Shamir’s works are incorrect and in some cases conflated:

- [1] Currently: “L. Shamir, ‘Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles,’ Astrophys. Space Sci. 365, 136 (2020), arXiv:2007.16116.”  
  On arXiv:2007.16116, the title is “Patterns of galaxy spin directions in SDSS and Pan-STARRS show parity violation and multipoles” and it is published in Ap&SS 365, 136 (2020). This entry is correct.

- [2] Currently: “L. Shamir, ‘Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies,’ Publ. Astron. Soc. Jpn. 74, 1114 (2022), DOI:10.1093/pasj/psac058.”  
  Searching PASJ shows “Analysis of the alignment of non-random patterns of spin directions in populations of spiral galaxies” by Shamir in PASJ 74, 1114 (2022) with DOI 10.1093/pasj/psac058.[1] This is correct, but note it is a different work from [1] and [3]; the text sometimes treats [2] as “Shamir (2020)” or “Shamir (2022)” without clarity.

- [3] Currently: “L. Shamir, ‘Analysis of spin directions of galaxies in the DESI Legacy Survey,’ Mon. Not. R. Astron. Soc. 516, 2281 (2022), arXiv:2208.13866, DOI:10.1093/mnras/stac2372.” On MNRAS and arXiv:2208.13866, the title and bibliographic info match this entry.[2]

- [4] Currently: “L. Shamir, ‘Handedness asymmetry of spiral galaxies with z < 0.3 shows cosmic parity violation and a dipole axis,’ Phys. Lett. B 715, 25 (2012), arXiv:1207.5464.”  
  On arXiv:1207.5464 and Phys. Lett. B 715, 25 (2012), the title and details are correct.[3][4]

However, in the Introduction (p.2) the text says: “Shamir (2012) [4] reported a 2–4σ dipole with per-bin asymmetry amplitudes of ∼ 5–20% using ∼1.27×105 SDSS galaxies. Shamir (2020) [1] and Shamir (2022) [3] reported results with ∼2–4% asymmetries...” Then later, Sec. V.A is titled “Shamir (2012, 2020, 2022)”. Reference [2] (PASJ 74, 1114) is another Shamir 2022 paper but is never cited in the running text; and the phrase “Shamir (2022) [3]” ambiguously overlaps with “Shamir (2022) [2]”. This is confusing but also bibliographically misleading.  
Required fix:  
- Ensure each “Shamir (year)” in the text clearly maps to a unique reference ID; e.g. “Shamir (2020a, Ap&SS 365) [1]; Shamir (2020b/2022, PASJ 74) [2]; Shamir (2022, MNRAS 516) [3]”.  
- If [2] is not actually used in the analysis/argument, remove it from the reference list to avoid phantom citations, or add explicit citations where it is discussed.  
- Check that numerical claims taken from “Shamir (2012, 2020, 2022)” (e.g. “∼2–4% asymmetries”, “∼3% signal”) are actually traceable to the correct paper: the ∼2–4% global asymmetry and “cosmic parity violation and multipoles” language comes from arXiv:2007.16116/Ap&SS 365, 136 (2020)[5][6], whereas the DESI Legacy analysis corresponds to MNRAS 516, 2281 (2022)[2]. Cite the specific paper for each statistic.

---

P4-E4 (ESSENTIAL)  
Section: Sec. V.A (Comparison with Shamir), p.5–6; Abstract, p.1  
Problem: The manuscript claims that Shamir’s signal amplitude is “∼ 3%” and that the present null “is inconsistent in amplitude with Shamir’s claimed ∼ 3% signal by a factor of ∼ 6–12 under the present pipeline.” Yet no explicit quantitative mapping from Shamir’s raw asymmetry statistic (e.g. per-hemisphere or per-region asymmetries in his SDSS / Pan-STARRS / DESI analyses) to the present dipole amplitude A is given, nor is a reference to the exact table/figure in Shamir’s papers from which the ∼3% figure is taken. For instance, Shamir (2020) Ap&SS 365, 136 reports per-bin asymmetries around a few percent in SDSS and Pan-STARRS[5][6], but translating these into a single-sky dipole amplitude requires a specified estimator, sky weighting, and mask. The text nonetheless presents the “∼ 6–12” factor as a quantitative inconsistency.  
Required fix: Either:  
- Provide an explicit, reproducible definition of how Shamir’s quoted “∼3%” is converted into a dipole amplitude comparable to the A ≈ 0.75% sensitivity, including a citation to the exact table/figure in the Shamir papers, or  
- Downgrade the statement to a qualitative comparison (e.g. “our 0.75% detection floor is at least a factor of a few below several-percent asymmetries reported in Shamir (2020, 2022),” with careful wording that avoids any implication of a formal statistical exclusion), and remove the “by a factor of ∼ 6–12” since it is not rigorously demonstrated from the cited works.

---

P4-E5 (ESSENTIAL)  
Section: Data Availability (Appendix, p.9)  
Problem: The paper gives specific URLs for datasets, model weights, and code (HuggingFace and GitHub). I cannot directly verify that the concrete URLs, repository names, and tags correspond to existing public releases (e.g. “Smith42/galaxies”, “bamfai/galaxy-chirality-catalog”, “Hubify-Projects/bigbounce”). Given PRD standards and the central role of reproducibility here, these must be real, accessible resources at the time of publication.  
Required fix:  
- Ensure that the stated repositories actually exist and are publicly accessible, with contents matching what the text claims (catalog tiers A/B/C, model, scripts).  
- Update names/URLs/tags in the manuscript to match the final released assets exactly (removing any placeholders or private-internal names).  
- Include a version tag or DOI (e.g. Zenodo) tied to the exact version used to produce the results, to guard against later repository changes.

---

P4-E6 (ESSENTIAL)  
Section: Sec. II.B (Training Labels), p.2–3; Appendix B, p.7–8  
Problem: The text states “The independent GZ1 cross-match on 234,282 disjoint matches yields spiral-chirality accuracy 69.91% (Cohen’s κ = 0.40). We treat 69.91% as the conservative accuracy floor and propagate it to all downstream isotropy bounds via the sub-percent systematic floor in Sec. IV C.” However, in Sec. VI.A the GZ1-based dilution factor is given as g = 2a − 1 with a = 0.6991, leading to a true underlying threshold ∼1.88%. This implies that the 0.75% “headline empirical 50%-recovery-3σ threshold” is already scaled, but the mapping between the measured accuracy and the sensitivity floor is only sketched, not fully documented (e.g. assumptions about confusion symmetry between CW and CCW, independence of label noise from sky position). For PRD, this propagation must be transparent.  
Required fix:  
- Add an explicit derivation (perhaps in an appendix) of how the measured GZ1 accuracy a = 0.6991 leads to the effective sensitivity floor and the 0.75%/1.88% relation, including a clear statement of assumptions (symmetric misclassification, no spatially varying bias, etc.).  
- Clarify in Sec. VI.A whether the 0.75% value is the observed catalog-space amplitude or the underlying true sky amplitude after de-biasing; use consistent terminology across abstract, Sec. VI.A, and conclusions.

---

P4-M1 (MAJOR)  
Section: Reference [7], page 9–10; Sec. V.B, p.5  
Problem: The CE-ResNet citation is given as “H. Jia, H.-M. Zhu, and U.-L. Pen, ‘Galaxy Spin Classification I: Z-wise vs S-wise Spirals With Chirality Equivariant Residual Network,’ Astrophys. J. 943, 32 (2023), arXiv:2210.04168, DOI:10.3847/1538-4357/aca8aa.” Checking arXiv:2210.04168 and ApJ 943, 32 confirms the title and bibliographic data.[7] However, the sentence “Jia et al. [7] introduced CE-ResNet … yielding cw/ccw = 0.998 on ∼ 1.95 million galaxies.” is vague and potentially misleading. CE-ResNet reports an overall CW/CCW balance very close to 1 for their classified sample; but it is not clear from their abstract that “cw/ccw = 0.998” is the exact figure and that the sample size is “∼ 1.95 million galaxies” (rather than, say, 1.96M or a different subset).[7]  
Required fix:  
- Check CE-ResNet’s actual numbers (total number of classified galaxies and the reported CW/CCW ratio). Replace “cw/ccw = 0.998 on ∼ 1.95 million galaxies” with the exact values quoted in the paper, or provide a precise reference (table/figure) if you wish to retain the numerical claim.  
- If the 0.998 ratio is derived from their catalog rather than explicitly stated in the paper, note that explicitly (“computed from the released CE-ResNet catalog”) and provide enough detail for reproducibility.

---

P4-M2 (MAJOR)  
Section: References –, p.9–10  
Problem: Several parity-violation and galaxy-statistics references are cited, e.g., Cahn et al. “A test for cosmological parity violation using the 3D distribution of galaxies,” Phys. Rev. Lett. 130, 201002 (2023)[1]; Komatsu (2022) Nature Rev. Phys.[8]; Eskilt & Komatsu (2022) Phys. Rev. D 106, 063503; and Hou, Slepian & Cahn (2023) MNRAS 522, 5701[1][3]. Spot checks against arXiv and journals show that the titles, years, volumes, and arXiv IDs are correct. However, the connections made in the narrative (Sec. VI.B, p.6) between the present morphology-channel dipole and these fundamentally different probes (4PCF parity-odd modes, CMB birefringence, etc.) are essentially qualitative and border on overclaiming: “The present null disfavors at the amplitude level any model predicting a late-universe morphology-channel dipole ≥ 0.75% … including the Shamir ∼ 3% amplitude class by a factor of ∼ 6–12.” No explicit link is given to actual inflationary/chiral tensor models in Cabass et al. or Philcox that would map onto a morphology dipole.  
Required fix:  
- Tone down these statements and clearly state that the present work does not provide a quantitative constraint on the specific parity-violating models discussed in –, only on the empirical morphology-channel dipole.  
- If you wish to connect to specific models (e.g., Lue et al. 1999; Cabass et al. 2023), include at least an order-of-magnitude estimate of the mapping required (e.g., how a primordial chiral tensor amplitude might translate into a late-time chirality dipole), or else explicitly frame it as an open theoretical question rather than a “disfavoring” of those models.

---

P4-M3 (MAJOR)  
Section: Equations (2), (3), (B1); Sec. III.C, IV.C, Appendix A, p.3–4,7–8  
Problem: Dimensional and probabilistic consistency:

- Eq. (2) defines equivariant probabilities as simple averages of original and flipped outputs. That is dimensionally fine, but the text claims that this “enforces flip-equivariance of the output protocol (flip-swap correlation = 1.000).” In fact, a simple arithmetic averaging of probabilities guarantees that the *ensemble-mean* output is equivariant under flip-swap, but it does not guarantee that the *per-instance* classification is equivariant; Appendix B later notes that 21.4% of argmax labels flips under D4. The wording in Sec. III.C is too strong for PRD standards.  

- Eq. (3) defines \(A_p\) as \((N^{(p)}_{\rm CW} - N^{(p)}_{\rm CCW}) / (N^{(p)}_{\rm CW} + N^{(p)}_{\rm CCW})\). However, in Appendix A there is also a definition using \(A_p = (N^{(p)}_{\rm CW} - N^{(p)}_{\rm CCW}) / N^{(p)}_{\rm total}\). The equivalence holds only if \(N_{\rm NS}\) is negligible; here the NS fraction is large (~62%). They state both forms in different places; this is inconsistent and affects the interpretation of dipole amplitude A and the Fisher-floor calculation.  

- Eq. (B1) defines a loss with a “flip-equivariance consistency term.” This implicitly assumes that the distribution of flipped images is equivalent to the original, but no explicit justification is given (e.g., training augmentation symmetry, no RA/Dec encoding).  

Required fix:  
- Clarify the precise definition of the asymmetry field \(A_p\) used in each analysis (real-space dipole vs NaMaster). Use a single consistent definition throughout the paper, or explicitly explain why two different definitions lead to negligible differences in the reported results.  
- Rephrase “enforces flip-equivariance of the output protocol (flip-swap correlation = 1.000)” to something like “enforces flip-equivariance in expectation; empirically we find r≈1.000 at the catalog level, though per-instance argmax labels can differ (Appendix B).”  
- Add a brief comment on the validity of the flip-consistency loss assumption: e.g. that no absolute orientation metadata is provided to the network and that augmentation ensures the flipped inputs are drawn from the same underlying distribution.

---

P4-M4 (MAJOR)  
Section: Sec. VI.A (Sensitivity Floor), p.6; Appendix A, p.7  
Problem: The Fisher Poisson floor is quoted as “∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).” Recomputing: for a binomial distribution with fraction f = 0.5 and N ≈ 3.2×10^6, σ(f) = sqrt(0.25/N) ≈ sqrt(0.25 / 3.2e6) ≈ 2.8×10^-4 = 0.028%. The stated 0.048% is larger by ~70%. This suggests either a miscalculation, an implicit fsky factor incorrectly applied, or an error in translating per-hemisphere to full-sky amplitude. Similarly, the “3σ” full amplitude 0.29% is about 10× the single-pixel σ(f); the numbers could be right for a particular dipole estimator, but this is not shown.  
Required fix:  
- Show explicitly how σ(A/2) ≈ 0.048% is computed from Nspiral and fsky, including all numerical steps (weighting, effective N, etc.).  
- Recalculate 3σ amplitude using a standard Fisher formalism for a dipole estimator on a partial sky, and ensure that the 0.29% value is correct or adjust it.  
- Align the numbers in Sec. VI.A and Appendix A with the recomputed values, or explicitly state if you are using a conservative inflation factor (e.g., from systematics) beyond the pure Poisson floor.

---

P4-M5 (MAJOR)  
Section: Sec. IV.C (Dipole Analysis), Table III, p.4–5  
Problem: Table III reports bandpower significances (“Significance (σ)”) such as +6.097, +2.232 etc., which are interpreted as “Mask-coupled monopole leakage” or “Residual mask coupling.” However, earlier text emphasizes that “significance … values from distinct null procedures are not directly comparable” and stresses mask-leakage interpretation; yet here the significance is presented as if derived from a simple Gaussian null with a standard deviation “σnull,” without any explicit link to the underlying MC procedure (how many realizations, whether the fields include the inferred monopole only, etc.). This is not strictly a citation error but a methodological opacity that directly affects interpretation of prior claims (Shamir, Iye et al.).  
Required fix:  
- In the caption or immediately adjacent text to Table III, restate the null definition (e.g. label-shuffle null with N=500, mask and weighting identical to the data) and clearly state that these σ values are relative to that specific null.  
- Where Table III is used to interpret previous literature, emphasize that these high-σ values are not cosmological but are generated under a controlled monopole-only generative null, to avoid any misreading that the paper is “detecting” a physical signal at >6σ.

---

P4-M6 (MAJOR)  
Section: Scope and length  
Problem: The paper is 10 pages plus multiple appendices, significantly longer than needed for the core methodological contribution (a null ℓ=1 dipole with a clearly identified mask-leakage channel). Many sections (especially Appendix C and D) describe a large number of diagnostic tests, some with overlapping conclusions, and the prose in the main text often rehearses these in detail. For PRD, where the bar is both rigor and concision, this reads more as a technical note plus an extended methods supplement than a tightly focused article.  
Required fix:  
- Consider shortening the main text to at most ~8 pages by:  
  - Moving most of the “signal-hunt diagnostics” (RA quadrants, multiple confidence ladders, several cross-spectra variants) completely to appendices, referenced briefly in the main text.  
  - Condensing the description of the bias-hardening suite and sensitivity floor to the most essential pieces needed to justify the 0.75% threshold.  
- Ensure that all essential technical details needed for reproducibility remain, but avoid repetition between the main text and appendices.

---

P4-N1 (NIT)  
Section: Title, first page  
Problem: Title uses nonstandard phrasing like “A −0.122σ Subsample-Mask ℓ = 1 Null” and “Canonical-Mask Residual” which may be confusing on first read. PRD usually prefers more conventional titles.  
Required fix: Consider simplifying the title to plain language highlighting the main result and method, e.g. “Survey-scale galaxy chirality constraints with an equivariant classifier: a null ℓ=1 dipole and mask-induced monopole leakage in DESI Legacy imaging.” Avoid jargon like “subsample-mask ℓ = 1 null” in the title.

---

P4-N2 (NIT)  
Section: All sections; formatting  
Problem: Occasional hyphenation/spacing artifacts in the transcription (e.g. “D4 -TTA”, “galaxy- chirality- catalog”, “NaMaster/pymaster”, “ce-ResNet catalog of Jia et al. (2023)” with inconsistent capitalization). While minor, PRD expects polished style.  
Required fix: Standardize naming and spacing (D4-TTA or D4 test-time augmentation; “galaxy-chirality-catalog” as a single hyphenated token; “NaMaster / pymaster” if you wish to emphasize the Python implementation; consistent capitalization of CE-ResNet).

---

P4-N3 (NIT)  
Section: Footnote in abstract: “Note: σ values throughout this paper are defined relative to their respective null procedures and are not directly comparable across estimators; see Table I for the mapping of each result to its null.”  
Problem: This is important but buried; several crucial results (headlines about −0.122σ, +0.43σ, +3.64σ) appear far from this note. As per PRD readability standards, key caveats should be reiterated near each complex comparison.  
Required fix: In addition to the ESSENTIAL fix P4-E1, consider moving part of this note into the beginning of Sec. IV (“Results”) or adding a short subsection “Significance conventions” (you already have one starting Sec. IV) that readers cannot easily skip. Make sure the note is also clearly visible in the abstract or introduction.

---

## Summary recommendation

REJECT

The paper is ambitious and carefully executed in many respects, but from a citation and methods-forensics standpoint it does not yet meet PRD standards. There are multiple essential issues: inconsistent and partially undocumented use of σ from different nulls; ambiguous or untraceable numerical comparisons to prior work (especially the “∼3%” Shamir signals and “factor of 6–12” claims); an unclear mapping between the GZ1-based accuracy floor and the advertised 0.75% sensitivity; and some inconsistent definitions of the core asymmetry field. The reference handling around Shamir’s multiple 2020–2022 papers is confusing, and some key numbers taken from CE-ResNet are not cleanly traceable to the published record. These are fixable, but they require substantial reworking and tightening of both the analysis exposition and the literature comparison, not just minor corrections.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-E7 (ESSENTIAL)  
Section: Table II; Sec. IV.B, VI.A, VII.d; Appendix B, Table V; multiple places where “σ” is used for binomial deviations  
Problem (Arithmetic / propagation): Several quoted “σ” deviations and derived percentages are numerically inconsistent with the stated binomial errors or their own definitions.

- In Table II, the binomial uncertainty is explicitly given as σ = √[p(1−p)/N] with Nspiral = 3,201,160. Using the tier C value p = 0.4974 and N = 3,201,160 yields σ ≈ 0.00028 (0.028%), which matches the quoted ±0.000279. The deviation from 0.5 is Δ = 0.4974 − 0.5 = −0.0026. In units of σ this is |Δ|/σ ≈ 0.0026 / 0.000279 ≈ 9.3, consistent with the “Dev. (σ) = 9.5” entry if one allows rounding. However, the text elsewhere calls this a “−0.53%” residual (Sec. IV.B: “from raw +2.05% to equivariant −0.53%”) while Table II’s “Excess (%)” entry is −0.26%. These two quoted percentages disagree by a factor ≈ 2, and only −0.26% is consistent with the tabulated numbers. Similar inconsistency appears for the “3.86× asymmetry-suppression factor” claimed between “raw +2.05%” and “equivariant −0.53%”: 2.05 / 0.53 ≈ 3.87, but 2.05 / 0.26 ≈ 7.9. The current manuscript mixes the two inconsistent amplitudes.  

- In Sec. VI.A the Fisher Poisson floor is quoted as “σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46” leading to “∼ 0.29% full-amplitude” at 3σ. Using a binomial model at f = 0.5 and N = Nspiral gives σ(f) ≈ √[0.25/N] ≈ 0.028%, not 0.048%. Even if an effective N were reduced by fsky, N_eff ≈ fsky·N ≈ 0.46·3.20×10^6 ≈ 1.47×10^6, the binomial σ would be ≈ 0.041%, still significantly below 0.048%. The text also conflates σ(A/2) and “full amplitude” A without explicitly stating the geometrical conversion (dipole fit vs single-pixel fraction). This makes the 0.29% 3σ floor non-reproducible and inconsistent with the stated inputs.  

- In Appendix B, Test T8 “CW/CCW balance (50%±10%). Result 49.7%.” This is consistent numerically. However, in Sec. IV.B and Appendix E the same CW fraction is variously described as “−0.26% residual” and “0.26% (9.5σ)”, whereas earlier in the Introduction and elsewhere the raw (Catalog A) monopole excess is “0.79%” and sometimes “2.05%”. There is no single, clearly defined mapping between “% excess” and σ across these sections; some numbers are evidently stale from earlier catalog versions.  

Required fix:  
- Audit all occurrences of percentages for the CW–CCW imbalance (e.g., “+2.05% raw”, “−0.53% equivariant”, “0.79% classifier bias”, “−0.26% residual”) and recompute them directly from the stated cw/(cw+ccw) values in Tables II and the catalog description. Replace all inconsistent percentages with a single coherent set, and correct any derived suppression factors accordingly.  

- In Sec. VI.A and VII.d, explicitly derive σ(A/2) from Nspiral and fsky, showing whether you use Nspiral, an effective N_eff, or a dipole-fit Fisher expression. Recompute the 0.048% and 0.29% numbers or adjust them to match the explicit calculation. Make sure “full amplitude” and “A/2” are clearly distinguished and used consistently.  

- Ensure that whenever you quote a “σ” deviation from 0.5 for the global monopole, it is numerically consistent with the binomial σ in Table II and that all percentages (Excess (%)) match those σ values.

---

P4-E8 (ESSENTIAL)  
Section: Eq. (3) vs Appendix A (“Field: Ap = (NCW−NCCW)/Ntotal”)  
Problem (Equation consistency / units): Eq. (3) defines the per-pixel asymmetry as \(A_p = (N^{(p)}_{\rm CW} - N^{(p)}_{\rm CCW}) / (N^{(p)}_{\rm CW} + N^{(p)}_{\rm CCW})\), i.e. normalized by spirals only. Appendix A, however, states that the NaMaster field uses \(A_p = (N^{(p)}_{\rm CW} - N^{(p)}_{\rm CCW}) / N^{(p)}_{\rm total}\), where \(N^{(p)}_{\rm total} = N^{(p)}_{\rm CW} + N^{(p)}_{\rm CCW} + N^{(p)}_{\rm NS}\). Since the NS fraction is large (~62% of the catalog), these two normalizations differ at the tens-of-percent level in amplitude. The manuscript currently presents both forms as if they were interchangeable, and some derived amplitudes (e.g., mapping to A ≈ 1.7% in Sec. IV.D and VI.A) implicitly assume one or the other without stating which. This is not just stylistic—using different Ap definitions changes the dipole amplitude and hence the sensitivity and comparison to Shamir.  

Required fix:  
- Choose one definition of \(A_p\) as the primary asymmetry field and use it consistently in all equations, NaMaster configuration text, and dipole-fit descriptions. If you need both (spiral-only and total-normalized), explicitly denote them with different symbols (e.g., \(A_p^{\rm spiral}\) and \(A_p^{\rm tot}\)) and state where each is used.  

- Recompute any quoted amplitudes (e.g., 1.7% interpretation (i) dipole, 0.75% threshold, Fisher floor) using the chosen definition, and update the text so that all numbers and equations are internally consistent and dimensionally matched.

---

P4-M7 (MAJOR)  
Section: Abstract; Sec. III.A; Table I; Sec. IV.C; Appendix A and D (σ / p-value comparability)  
Problem (Null procedure comparability beyond previous P4-E1): While P4-E1 already flagged some juxtapositions, there remain additional places where σ values from heterogeneous null procedures are effectively compared or read as comparable without a local warning:

- Abstract’s “Falsification criterion”: “A future survey detecting a chirality dipole at σ > 5 with full amplitude ≳ 0.75% … would falsify the present null.” Here σ>5 is implicitly under some future survey’s own null (likely different from any of your six current nulls), while 0.75% is tied to your per-pixel shuffle null and HC sample. Presenting a σ-threshold from arbitrary future analyses alongside your amplitude threshold suggests direct comparability of those σ’s, without restating that σ depends on the null and estimator.  

- Sec. III.A (Declared Analysis Hierarchy) lists “σdipole = 0.43,” “−0.122σ,” “+3.64σ,” and “3.05σ local maximum” in one bullet-point hierarchy without any local caveat about distinct nulls. Table I is referenced for mapping, but the hierarchy reads as if the σ values are on a common scale.  

- Sec. VI.A: “P(σ>3) = 0.55 at A = 0.75% and P(σ>3) = 0.15 at A = 0.5% (a non-detection point).” These σ are tied to the injection-recovery null on the HC subsample, but a few lines later the text compares this to “Fisher Poisson floor at 3σ ∼ 0.29%” (a different statistical model) without re-emphasizing that “3σ” here is computed under a different analytic null and estimator than the injection-based σ.  

Required fix:  
- In the “Falsification criterion” sentence in the abstract and in VII.d, explicitly state that the “σ > 5” refers to significance under that future survey’s own specified null and is not directly comparable to the σ values reported here, and that the crucial comparable quantity is amplitude relative to your 0.75% sensitivity floor.  

- In Sec. III.A’s bullet list, add a short parenthetical after the σ’s indicating their nulls (e.g., “+3.64σ (canonical per-pixel shuffle null; not comparable to (i)/(ii) σ)”) or otherwise restate non-comparability in situ.  

- In Sec. VI.A, when juxtaposing “P(σ>3)” from the injection tests with the analytic 3σ Fisher floor, add clarifying language that these “3σ” thresholds are defined under different assumptions and nulls and cannot be strictly equated; the key message is relative amplitude (0.75% vs ≈0.29%), not the numerical σ label.

---

P4-M8 (MAJOR)  
Section: Abstract; Sec. II.B; Appendix B; Sec. VI.A; Appendix E (GZ1 accuracy and dilution factor mapping)  
Problem (Noise model / dilution propagation): The manuscript states that the independent GZ1 cross-match yields an accuracy of a = 0.6991, and in Sec. VI.A uses a “GZ1-dilution factor g = 2a − 1 ≈ 0.398” to infer a “true-underlying threshold ∼ 1.88%” from the observed 0.75% 50%-rec-3σ amplitude. This assumes (i) symmetric misclassification between CW and CCW, (ii) no sky-position dependence of errors, and (iii) that NS contamination and GZ1’s own biases can be collapsed into a single scalar g. At several points the text asserts that 69.91% is “propagated … via the sub-percent systematic floor,” but the concrete propagation is only partially sketched; for example, Appendix E’s discussion of edge-on contamination is not explicitly folded into the same dilution model, and Appendix B’s eight-test bias suite does not quantify how asymmetric misclassification would alter g.  

Required fix:  
- Provide a self-contained derivation (equation-level) of the dilution relation used: explicitly show that, under your stated assumptions, an underlying sky dipole of amplitude A_true is observed as A_obs = g · A_true, with g = 2a − 1, and demonstrate how this leads from A_obs,thr ≈ 0.75% to A_true,thr ≈ 1.88%.  

- Explicitly justify or at least clearly state the assumptions (symmetric CW/CCW confusion, spatial independence, treatment of NS) and discuss in 1–2 sentences how violating these assumptions (e.g., if misclassification is skewed or RA/Dec-dependent) would change g and thus the claimed sensitivity.  

- Ensure that all mentions of the 69.91% accuracy floor, 0.75% threshold, and 1.88% underlying threshold reference this derivation so that readers can reproduce the mapping and see its limitations.

---

P4-M9 (MAJOR)  
Section: Abstract; Sec. VI.B; VII.a–d  
Problem (Abstract faithfulness / overconstraint of parity-violating models): The Discussion and Conclusions now partially acknowledge that mapping to primordial parity-violating models is not done (“that transfer function is not derived in this paper”), but the abstract and VII.a still use language that implies constraint on “any model predicting a late-universe morphology-channel dipole ≥ 0.75% … including the Shamir ∼ 3% amplitude class by a factor of ∼ 6–12.” The latter phrasing is especially strong: “by a factor of ∼ 6–12” reads as a quantitative exclusion, even though Shamir’s ∼3% is not rigorously re-expressed in your A-normalization and the systematic/noise floor has multiple components (GZ1 dilution, edge-on contamination, mask geometry). This remains a stronger claim than is justified by the analysis as written.  

Required fix:  
- In the abstract and VII.a, soften wording from “disfavors… by a factor of ∼ 6–12” to a qualitative amplitude comparison that does not imply a formal statistical exclusion; for example, “our empirical 0.75% sensitivity is well below the several-percent asymmetries reported by Shamir (2012, 2020, 2022), indicating that if such a large, clean morphology-channel dipole existed on the DESI footprint, it would likely have been detected under our pipeline.”  

- Remove or justify the specific “factor of ∼ 6–12” unless you supply an explicit calculation showing how Shamir’s particular estimator, masks, and sky weights map to your A parameter and null, with clear references to the exact tables/figures used. If that calculation is not provided, the ratio should not be quoted as a numerical fact.

---

P4-M10 (MAJOR)  
Section: Abstract; Sec. II.B, III.C, Appendix E (flip-equivariance statements)  
Problem (Per-instance vs ensemble equivariance): The abstract and Sec. III.C state that the test-time averaging “enforces flip-equivariance of the output protocol (flip-swap correlation = 1.000).” Appendix B and E later clarify that argmax labels flip for ~21.4% of borderline galaxies under D4, and Appendix E relies on “ensemble-mean flip symmetry” to argue that edge-on galaxies mainly dilute rather than bias the signal. The current phrasing “enforces flip-equivariance” is too strong: the averaging enforces equivariance only in expectation at the probability level; the deployed catalog, based on discrete class labels and thresholds, is not strictly equivariant per instance, and that subtlety matters for systematics like edge-on contamination.  

Required fix:  
- In the abstract and Sec. III.C, rephrase to “enforces flip-equivariance in expectation at the probability level (catalog-level flip–swap correlation ≈ 1.000), though per-instance argmax labels can differ for borderline cases (see Appendix B).”  

- In Appendix E, when using this to argue that edge-on galaxies only dilute sensitivity, explicitly reference the same probabilistic-equivariance assumption and note that any residual per-instance asymmetry in edge-on classifications is treated as part of the noise floor, not as guaranteed zero bias.

---

P4-N4 (NIT)  
Section: Data Availability; main text references to repositories  
Problem (Versioning / reproducibility detail): The Data Availability section now lists concrete HuggingFace and GitHub URLs and a tag “v2026.04” for the dataset, but the model and code entries do not include explicit version tags or commit hashes. It is also not stated which exact dataset tag and model checkpoint were used for the results in the paper (e.g., whether the catalog labeled “v2026.04” corresponds one-to-one with the Catalog C used in all plots, and whether the PyTorch checkpoint is uniquely identified).  

Required fix:  
- Add explicit version identifiers (tag or commit SHA) for the model repository and GitHub code used to generate the results, and explicitly state that the catalog used in this manuscript corresponds to tag v2026.04 (or correct tag) and to a specific model checkpoint. This will make the computational environment fully reproducible and avoid ambiguity if repositories evolve post-publication.

---

P4-N5 (NIT)  
Section: Sec. II.B; Appendix B; References  
Problem (Internal cross-reference clarity): The manuscript repeatedly refers to an “independent GZ1 cross-match on 234,282 disjoint matches” in Sec. II.B and Data Availability, but the exact procedure (matching radius, which Galaxy Zoo catalog version, how “disjoint” is enforced) is only vaguely described. The references , ,  are present but not tied to the specifics of this cross-match. For PRD-level reproducibility, this is acceptable scientifically but could be clearer.  

Required fix:  
- Add a brief sentence giving the matching criterion (e.g., maximum angular separation and which GZ1 catalog version) or point to a specific script in the released code that implements it (e.g., “see script match_gz1.py in the repository for exact cross-match criteria”). This will improve the traceability of the 69.91% accuracy figure.

If you’d like, I can now walk through the key arithmetic recalculations (e.g., the correct Fisher floor and CW-excess percentages) step by step so you have concrete numbers to drop into the revised manuscript.