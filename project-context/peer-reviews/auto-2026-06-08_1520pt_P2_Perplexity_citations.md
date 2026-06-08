# P2 auto-2026-06-08_1520pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (9238 chars)
**Wall time**: 83.3s

---

P2-E1 (ESSENTIAL) – Abstract & body (multiple pages) – misuse of existing constraint paper and fused citation  
Problem: The manuscript repeatedly treats “Eskilt et al. joint Planck + ACT analysis” as an already‑published, specific numerical result βobs = 0.342 ± 0.094° and a 3.6σ signal, but no such paper exists in the current literature with that title, authorship, or that exact number. The only closely related work is Eskilt & Komatsu, Phys. Rev. D 106, 063503 (2022), which analyzes **Planck/WMAP** birefringence and reports β ≃ 0.342 ± 0.094° using Planck NPIPE + WMAP, *without* ACT.[1][2] The abstract of that paper gives β = 0.342 ± 0.094° (3.6σ) from Planck NPIPE + WMAP; there is no “joint Planck + ACT” paper or arXiv entry with Eskilt as first author and Komatsu as coauthor producing the same number. The manuscript’s phrase “Eskilt et al. joint Planck + ACT analysis” is therefore a fused, incorrect description of the existing NPIPE+WMAP analysis, and the statement “3.6σ isotropic birefringence signal … from the Eskilt et al. joint Planck + ACT analysis” is factually inaccurate.  
Required fix:  
- Correct all occurrences of “Eskilt et al. joint Planck + ACT analysis” to the actual published work: “Eskilt & Komatsu (2022) Planck + WMAP NPIPE analysis,” and clarify explicitly that the 3.6σ signal and the βobs = 0.342 ± 0.094° number come from Planck+WMAP, not ACT.  
- Remove any implication that ACT data were used in that particular analysis unless you can point to a real, citable paper (with arXiv ID/DOI) that indeed combines Planck and ACT and gives that number.  
- In the abstract and conclusion, rewrite the description of the 3.6σ signal to be factually accurate (“Planck + WMAP NPIPE” rather than “Planck + ACT”), and ensure the phrasing does not claim a dataset combination that does not exist in the cited work.

---

P2-E2 (ESSENTIAL) – Pg. 1 Abstract / Pg. 3 §3.1 – incorrect attribution of quoted 3.6σ significance  
Problem: The abstract states: “βobs = 0.342 ± 0.094° from the Eskilt et al. joint Planck + ACT analysis” and calls this a 3.6σ signal. The quoted numbers 0.342 ± 0.094° and 3.6σ originate from Eskilt & Komatsu 2022 (Planck/WMAP NPIPE), not from any ACT analysis.[1][2] There is currently no published ACT birefringence paper quoting exactly β = 0.342 ± 0.094°. The paper later cites Diego‑Palazuelos & Komatsu as “Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025” with no arXiv ID.[3] After searching NASA ADS and arXiv, no paper with that exact title, author list, and year is found, and no ACT cosmic birefringence paper currently reports β = 0.342 ± 0.094°. The 3.6σ value is therefore mis‑attributed.  
Required fix:  
- Attribute the 0.342 ± 0.094° and 3.6σ numbers solely to Eskilt & Komatsu (Planck/WMAP) and explicitly state the dataset used (Planck NPIPE + WMAP).  
- Remove “+ ACT” from the description of this measurement unless a real ACT‑inclusive paper is found, in which case provide the correct arXiv ID, title, and numbers and update the text to match that paper’s abstract or tables.  
- If there is unpublished internal ACT work, it must not be cited as though it were a peer‑reviewed, public result.

---

P2-E3 (ESSENTIAL) – Pg. 3 §3.1 and References – non‑existent / uncitable ACT DR6 birefringence paper  
Problem: The manuscript cites “P. Diego-Palazuelos and E. Komatsu. Cosmic birefringence from the Atacama Cosmology Telescope. arXiv preprint, 2025.” and uses it quantitatively (“ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074° (2.9σ)”). A search of arXiv and ADS shows no such 2025 arXiv preprint with that title/author list.[3] The closest current results concern ACT DR6 lensing and polarization but do not carry that exact title or numbers. There is no verifiable source for β = 0.215 ± 0.074° as an official ACT DR6 birefringence measurement.  
Required fix:  
- Either (a) provide a valid arXiv identifier and confirm that the ACT paper exists and indeed reports β = 0.215 ± 0.074°, or (b) remove this citation and associated numbers entirely, or clearly label them as *private communication/unpublished* and do not treat them as public, citable constraints.  
- PRD standards require that quantitative constraints used in your analysis be traceable to publicly available, citable sources; otherwise, they cannot serve as a primary input to your summary likelihood.

---

P2-E4 (ESSENTIAL) – Pg. 3 §3.2 Eq. (3) and Eq. (4) – inconsistent use of data and unverified combined constraint  
Problem: The combined constraint βcombined = 0.242 ± 0.061° (3.9σ) is said to result from combining “Planck NPIPE [Eskilt and Komatsu, 2022]: β = 0.30 ± 0.11° (2.7σ)” and “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]: β = 0.215 ± 0.074° (2.9σ)” via a Gaussian likelihood. However:  
- As above, the ACT DR6 number is not traceable to any published source.  
- The Planck NPIPE value 0.30 ± 0.11° is not quoted in the abstract of Eskilt & Komatsu; they quote 0.342 ± 0.094° (and other values for different data/priors) rather than 0.30 ± 0.11°.[1][2] If 0.30 ± 0.11° is drawn from a particular subset or alternative analysis within that paper, the specific table or figure is not identified and cannot be verified from the abstract alone.  
- Recomputing the inverse‑variance weighted combination of 0.30 ± 0.11° and 0.215 ± 0.074° indeed yields approximately 0.242 ± 0.061°, but because one input value is uncited/missing and the other is not clearly documented, the combined constraint is not reproducible from the literature.  
Required fix:  
- Provide explicit citations (table/figure numbers) in Eskilt & Komatsu (2022) from which β = 0.30 ± 0.11° is obtained, or correct this value to one that is actually published in that paper.  
- Do not combine in Eq. (3) any measurements that are not fully traceable to public sources. If you wish to provide an illustrative combination, clearly state that it is for illustration only and based in part on preliminary/assumed ACT numbers, and it must not be used for formal inference or Bayes factor calculations presented as robust results.  
- Alternatively, restrict Eq. (3–5) to Planck/WMAP measurements only, with all inputs directly sourced from Eskilt & Komatsu, and recompute βcombined and fphoton × C0 accordingly.

---

P2-E5 (ESSENTIAL) – Pg. 3 Eq. (5) – missing definition and unsupported numerical inference for “fphoton × C0”  
Problem: Eq. (5) states “fphoton × C0 = 1.73 ± 0.44” without defining fphoton anywhere in the text, without units, and without showing the derivation from βcombined. The only related quantity defined earlier is the photon coupling gaγ = C0/fa. In standard notation, one expects either gaγ or fa/C0; the combination “fphoton × C0 = 1.73” is dimensionally ambiguous. No prior paper in the bibliography is cited as the source of a similar combination, and this scalar cannot be traced to the literature.  
Required fix:  
- Define fphoton precisely, including units, and relate it clearly to gaγ and fa. For example, if fphoton is 1/(gaγ MPl) or a rescaled coupling, state this explicitly.  
- Show the explicit formula connecting βcombined, Δϕ/fa, and fphoton × C0. Provide enough algebra that a reader can recompute 1.73 ± 0.44 directly from the quoted βcombined. If there is any dependence on assumed order‑unity factors (e.g., θi, J0 integrals), specify them.  
- If you cannot provide a clear definition and derivation, remove the numerical value 1.73 ± 0.44 as a “constraint” and instead leave the result in terms of gaγ or fa directly.

---

P2-E6 (ESSENTIAL) – Pg. 3 §3.3 Table 1 – inconsistent notation for coupling parameter  
Problem: Table 1 states “Model: ALP (C = 8 fixed)” and “Priors: … Caγ flat on [1, 30] (Run 2 only).” Later in §3.3 and the caption of Fig. 1, the coupling is written as “Caγ” and in the text also as “C0” and gaγ = C0/fa. There is no consistent definition of C, C0, Caγ or how they relate; “C=8” appears nowhere else, and there is no reference that uses exactly “Caγ” with this range. This makes the MCMC configuration unreproducible and the mapping to physical gaγ ambiguous.  
Required fix:  
- Introduce a clear, unique symbol for the anomaly coefficient (e.g., C0) and stick with it throughout. Explicitly define Caγ if it differs (e.g., a rescaled coupling g aγ MPl).  
- Update Table 1 and the priors paragraph to use the same symbol and explain “C = 8 fixed” in terms of the previously defined quantities.  
- Ensure that when you compare to Fujita et al. (2021) or Namikawa et al. constraints, the same coupling normalization is used or a conversion is given.

---

P2-E7 (ESSENTIAL) – Pg. 2 Eq. (2) and surrounding text – dimensional inconsistency and unjustified numerical estimate  
Problem: Eq. (2) is written as  
β = gaγ Δϕ / 2 = C0 Δϕ / (2fa) ≈ C′0 θi / 2 × O(1)  
and then the text claims “For C0 ∼ 1, θi ∼ 1: the cosmological field evolution gives Δϕ/fa ∼ 10−2 … yielding β ≈ C0 θi × 5 × 10−3 rad ≈ 0.27°.” There are several issues:  
- Δϕ/fa ∼ O(1) is inferred from Eq. (1) (Δϕ ≈ fa θi × O(1)), which contradicts the statement that Δϕ/fa ∼ 10−2 “from the ratio of field displacement to decay constant over the Hubble time.” No derivation is given for the factor 10−2, and it is incompatible with Eq. (1) if θi ∼ O(1).  
- The expression “5 × 10−3 rad ≈ 0.27°” is numerically incorrect: 0.27° ≈ 4.7 × 10−3 rad, so 5 × 10−3 rad corresponds to ≈ 0.286°. While close, the mismatch signals sloppiness in the central, model‑defining relation.  
- No connection is made to actual cosmological parameters or the integration of the field equation; the “10−2” factor appears as an unsupported back‑of‑the‑envelope claim rather than a result grounded in Fujita et al. (2021) or any other prior work.[6]  
Required fix:  
- Make the field dynamics consistent: either derive Δϕ/fa from a proper solution of the ALP equation of motion in ΛCDM and show where the effective 10−2 comes from, or remove it and keep only the qualitative statement Δϕ ≈ fa θi × O(1).  
- If you keep the numerical prediction β ≈ 0.27°, show explicitly how it follows from chosen parameters m, fa and initial conditions, preferably referencing Fujita et al. (2021) or other literature that performs the integral.  
- Correct the rad–degree conversion and avoid mixing “≈” with a level of precision that suggests more accuracy than is justified by the model.  
- Ensure that Eq. (2) and the subsequent text are dimensionally consistent, explicitly stating that gaγ has dimension (energy)−1 in natural units and that β is dimensionless.

---

P2-E8 (ESSENTIAL) – Pg. 3 §3.3 quoted Eskilt & Komatsu number vs. literature  
Problem: The paper uses βobs = 0.342 ± 0.094° as “Eskilt et al. joint analysis” and then claims that the ALP and βfree posteriors (0.336 ± 0.107°, 0.344 ± 0.096°) match this value “with no tension.” In Eskilt & Komatsu (2022), the central Planck+WMAP NPIPE result is indeed 0.342 ± 0.094° (3.6σ), but there are also other values depending on frequency cuts and foreground treatments.[1][2] The manuscript does not cite which exact configuration it is matching nor show that its priors on θi, m, and Caγ align with those used in that paper when comparing constraints on ALP masses.[6] Without clarifying which measurement is being matched, the claim of “no tension” is not verifiable.  
Required fix:  
- Explicitly state which equations or tables in Eskilt & Komatsu (2022) correspond to β = 0.342 ± 0.094°.  
- Clarify in the text that you are matching this specific configuration (e.g., Planck NPIPE + WMAP full EB spectrum), not a combined Planck+ACT analysis.  
- When asserting “no tension,” quantify it properly (e.g., Δβ/σcombined) and note that different data selections in Eskilt & Komatsu may yield slightly different central values.

---

P2-E9 (ESSENTIAL) – Bibliography: Namikawa et al. (2025) entry “in preparation”  
Problem: The reference “Toshiya Namikawa, Kai Murai, and Sho Naokawa. Constraints on axion-like particles from cosmic birefringence. arXiv e-prints, 2025. In preparation; cited for comparison of ALP mass constraints.” appears to refer to an in‑preparation or anticipated paper. A search of arXiv for “Namikawa Murai Naokawa constraints on axion-like particles from cosmic birefringence” does not return any entry corresponding to this description.[4][5] Citing non‑existent or in‑preparation work as if it were an arXiv e‑print is not acceptable for PRD, especially when used to claim “superior ALP mass constraints using the full Planck EB spectrum.”  
Required fix:  
- Remove this reference unless the paper has in fact appeared on arXiv; if so, provide the correct arXiv identifier and year and ensure that all claims match the abstract or tables of that paper.  
- Do not rely on “in preparation” results to support statements about “superior constraints.” If these are private communications, label them explicitly as such and do not base key comparison statements on them.

---

P2-M1 (MAJOR) – Abstract & §3.4 – Bayes factor ln B = 5.17 not reproducibly derived  
Problem: The paper quotes ln B = 5.17 as the Bayes factor between the ALP model (β ≠ 0) and the null, using a Savage–Dickey ratio with a flat prior β ∈ [0°, 1°], and then gives values 4.48 and 5.86 for other priors. However:  
- The quoted chain lengths (2,160–6,840 accepted samples) and Neff ~ 1,000 are marginal for robust Savage–Dickey estimation at β = 0, especially when tail behavior is important.  
- No explicit posterior density at β = 0 is shown, nor is any kernel density method or binning described, so the numerical value 5.17 cannot be independently checked.  
- The Bayes factor depends sensitively on whether the prior is uniform in β or β^2, and on whether systematic uncertainties are included; none of this is discussed.  
Required fix:  
- Provide explicit details on the computation of the Savage–Dickey ratio: how the density at β = 0 was estimated, the bin width, and a convergence test for ln B.  
- At minimum, add an explicit caveat in the body where ln B is quoted that, given the limited sample size, the Bayes factor is only an order‑of‑magnitude indication and should not be over‑interpreted.  
- Better, rerun the chains to achieve at least O(50,000) effective samples for β and recompute ln B, reporting an uncertainty on ln B or performing a cross‑check via thermodynamic integration or nested sampling.

---

P2-M2 (MAJOR) – §3.3 MCMC details insufficient for reproducibility  
Problem: The paper provides only very coarse MCMC details: total accepted samples per run, R̂ − 1, and some priors. There is no description of sampler type (e.g. Metropolis, HMC), proposal distributions, burn‑in length, thinning, or the exact likelihood used (beyond Eq. 3). This is below PRD standards for reproducibility in cosmology.  
Required fix:  
- Specify the sampler algorithm, number of chains, burn‑in fraction, and whether convergence diagnostics were applied per‑parameter or globally.  
- Provide the explicit likelihood used in the ALP parameter space (e.g., was β treated as a derived parameter with Gaussian likelihood centered on βobs = 0.342 ± 0.094°?).  
- Ideally, include in a supplemental material a corner plot and 1D posterior for β from each run, and a brief statement of autocorrelation times.

---

P2-M3 (MAJOR) – §4 LiteBIRD forecast: over‑simplified significance and neglect of systematics  
Problem: The LiteBIRD forecast uses σ(β) ≈ 0.03° from “LiteBIRD Collaboration (2023)” and then calculates a naïve significance 0.27 / 0.03 = 9σ. However, the cited LiteBIRD forecast paper’s σ(β) depends on assumptions about self‑calibration, foregrounds, and systematics.[4][5] The paper itself later acknowledges systematic challenges in §6 but does not carry any of these caveats into Eq. (10) or the explicit 9σ claim. This over‑states the forecast precision and treats a best‑case statistical error as a robust detection significance.  
Required fix:  
- In §4, explicitly state that the 9σ figure is a *statistical*, idealized forecast that neglects systematics, and that the actual detection significance will depend on LiteBIRD’s calibration, foreground modeling, and possible frequency‑dependent birefringence.  
- Consider quoting the range of σ(β) values provided by the LiteBIRD paper or at least one “optimistic” and one “pessimistic” scenario and propagate this into a range of possible significances.  

---

P2-M4 (MAJOR) – Abstract & §6 – novelty claim vs. Fujita et al. (2021) and later work  
Problem: The paper states that its contribution is “the specific parameter identification (fa ∼ MPl, m ∼ H0) that produces a natural prediction matching the observed signal” and that “Fujita et al. (2021) already demonstrated that a Planck-scale ALP naturally produces β ~ 0.3°… Our contribution is not the model itself, but rather the specific parameter identification…” Fujita et al. (2021) explicitly study isotropic birefringence from an oscillating ALP and show parameter regions where Planck‑scale couplings yield β of order 0.3°.[6] Recent Planck‑based ALP papers (e.g. 2506.20824, Planck Constraints on Axion-Like Particles through Isotropic Cosmic Birefringence) similarly explore m ~ H0 and fa ~ MPl configurations.[1][4] The incremental novelty of merely highlighting fa ~ MPl and m ~ H0 is therefore modest, and the paper does not clearly delineate what is genuinely new versus re‑interpretation of existing results.  
Required fix:  
- Add a subsection in the introduction explicitly comparing your parameter choices and predictions to Fujita et al. (2021) and later Planck ALP constraint papers.  
- Tone down novelty language and clarify that the primary contribution is a simple phenomenological summary and forecast, not a fundamentally new ALP mechanism.  
- Make sure all claims about “first” or “naturalness” are explicitly linked to and contrasted with existing work.

---

P2-M5 (MAJOR) – §5 bounce cosmology link and references to companion papers  
Problem: The paper references “the companion paper [Golden, 2026a] for the full ECH framework and 14-barrier catalog” and “Golden, 2026b” for matter-bounce fNL. Neither has arXiv IDs, DOIs, or confirmed existence. They are described as “submitted simultaneously,” which PRD does not treat as guaranteeing availability. Furthermore, the birefringence analysis in this paper does not, in fact, depend on the ECH framework.  
Required fix:  
- Either provide arXiv identifiers for Golden (2026a, 2026b) or remove these references as load‑bearing citations.  
- Restrict discussion of ECH and matter-bounce fNL to brief qualitative remarks and do not rely on unpublished “14‑barrier catalogs” to motivate physics claims here.  
- Ensure that the cosmology/bounce connection is explicitly optional for the ALP prediction, as you partly state already.

---

P2-M6 (MAJOR) – Abstract & Conclusion – mismatch between claimed 3.6σ “Planck + ACT” signal and body  
Problem: The abstract and conclusion repeatedly describe “the 3.6σ Eskilt et al. joint Planck + ACT signal,” but the body only provides Planck NPIPE and an asserted ACT DR6 number; it never demonstrates that a *joint* Planck+ACT analysis exists with 3.6σ, nor is such a combination computed in the paper. Internal consistency demands that the load‑bearing scalar in the abstract (3.6σ) be either derived in the paper or properly attributed to a specific external work.  
Required fix:  
- Either (a) remove the “Planck + ACT” phrasing and clearly attribute 3.6σ to Eskilt & Komatsu Planck+WMAP NPIPE, or (b) perform and present an explicit Planck+ACT joint analysis with clearly documented data and methods.  
- Ensure that the headline number in the abstract matches a real analysis either in this paper or in a precisely cited external reference.

---

P2-M7 (MAJOR) – Equation (1) Bessel function heuristic without reference or derivation  
Problem: Eq. (1) writes Δϕ ≈ fa θi (1 − J0(m/H0)/J0(0)) with J0 a Bessel function and then asserts that “for m/H0 ~ 1, 1 − J0(1) ≈ 0.24; the precise value depends on the cosmological integration through the matter and dark-energy eras.” No derivation is given, and no literature reference is provided that uses this J0 form for an ALP rolling at late times. Standard ALP analyses typically integrate the Klein–Gordon equation numerically; a J0 expression suggests a simplified de Sitter or matter‑dominated approximation. Without showing origin, this looks like an ad‑hoc formula.  
Required fix:  
- Either provide a short derivation of Eq. (1) in an appendix (or at least sketch it in the text, citing the background expansion used), or cite a prior paper that derived this approximate form.  
- Clarify the assumptions under which Eq. (1) holds (e.g., constant H, small‑angle approximation).  
- If such a derivation cannot be provided, remove the J0 expression and instead rely on a more standard approximate or numerical solution.

---

P2-M8 (MAJOR) – §6 “fNL = −35/8” from companion paper  
Problem: The discussion section states: “The matter-bounce non-Gaussianity fNL = −35/8 provides a complementary and independent test [Golden, 2026b].” This specific numerical prediction is attributed only to an unpublished companion paper for which no arXiv ID is given. There is no way to verify that −35/8 is truly derived in that work or not contradicted by existing non‑Gaussianity literature.  
Required fix:  
- Either provide a citable source (with arXiv ID or DOI) for the fNL = −35/8 prediction, or remove this sentence from the current paper.  
- Given that non‑Gaussianity is not central to the ALP birefringence analysis, it is safer to omit this unverified numerical claim.

---

P2-m1 (MINOR) – Abstract and §3.2 – statistical significance wording  
Problem: The abstract says “σ(β) ≈ 0.03° will test this prediction at 9σ significance” and in §4 “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.” This implicitly treats the posterior on β as Gaussian and ignores uncertainty in the theoretical prediction (e.g., θi, C0 distributions). A 9σ statement suggests extremely high precision that is not fully justified by the model uncertainties.  
Required fix:  
- Qualify the 9σ statements to indicate that they are under the assumption of a fixed predicted β = 0.27° and Gaussian statistical errors only.  
- Consider replacing “9σ” with “O(10σ)” or providing a short sentence acknowledging that theory uncertainties will slightly degrade the effective significance.

---

P2-m2 (MINOR) – §6 “naturalness” claims without quantitative measure  
Problem: The text repeatedly states “no fine-tuning,” “natural prediction,” and “all inputs are O(1),” but never quantifies these in terms of, e.g., width of viable parameter ranges or any Bayesian prior volume argument.  
Required fix:  
- Add a brief paragraph quantifying the range of θi, m, and fa consistent with the observed β at, say, 1σ and 2σ, to substantiate the naturalness claim.  
- Alternatively, soften the language and present these as qualitative observations.

---

P2-m3 (MINOR) – References formatting and completeness  
Problems:  
- Fujita et al. (2021) reference lacks any arXiv ID, though the published PRD paper has one (2103.03436).  
- Minami & Komatsu (2020) and Eskilt & Komatsu (2022) are missing arXiv IDs as well.  
Required fix:  
- Add arXiv identifiers to all references that have them, per common PRD practice, and check that journal, volume, and page numbers match the actual publications.  
- For “LiteBIRD Collaboration. LiteBIRD science goals and forecasts: a full-sky CMB polarization survey. Prog. Theor. Exp. Phys., 2023:042F01, 2023,” verify that title, volume, and article number match the official PTEP entry and add the arXiv ID.

---

P2-n1 (NIT) – Minor numerical consistency  
Problem: “5 × 10−3 rad ≈ 0.27°” is numerically slightly off. 0.27° ≈ 4.71 × 10−3 rad.  
Required fix:  
- Either adjust to “4.7 × 10−3 rad ≈ 0.27°” or keep “5 × 10−3 rad ≈ 0.29°,” but do not mix cross‑rounded numbers.

---

P2-n2 (NIT) – Language and style  
Problem: Occasional informal phrases like “consumer hardware” and explicit mention of “AI research assistants” in the Acknowledgments are not typical of PRD style and may distract from the scientific content.  
Required fix:  
- Consider simplifying these to a more standard form (e.g., “Computations were performed in Python using NumPy and SciPy.”) and omit mention of AI unless required by journal policy.

---

## Length and scope

The scientific content is modest: a simple ALP birefringence back‑of‑the‑envelope, a summary‑likelihood combination, and a naïve LiteBIRD forecast. For this, 6 pages is on the long side, especially given the absence of detailed derivations or a full likelihood pipeline. A more appropriate length would be 4–5 pages, focusing on (i) a clean, correctly referenced summary of existing constraints, (ii) a properly derived parameter‑space mapping for fa ∼ MPl, m ∼ H0, and (iii) a carefully caveated LiteBIRD forecast.

## Summary recommendation

REJECT

The paper has multiple essential issues in citation accuracy (mis‑attribution of key results, non‑existent or in‑preparation references presented as established), and several of its headline numerical claims—especially the “Planck + ACT 3.6σ” signal, the ACT DR6 constraint, and the Bayes factor—are not traceable to published sources or are insufficiently derived. Combined with conceptual and reproducibility shortcomings in the theory estimate and MCMC methodology, the manuscript does not currently meet PRD’s standards for rigor and verifiability. Substantial re‑writing, re‑derivation, and re‑anchoring in the actual literature would be required; such changes go beyond “major revisions” and effectively constitute a new submission.

---

## PASS 2 — self-critique findings (what initial review missed)

P2-E10 (ESSENTIAL) – Abstract / §2.2 – internal inconsistency between Eq. (1), Eq. (2), and the claimed “Δϕ/fa ∼ 10⁻²”  
Problem: Eq. (1) gives \(\Delta\phi \approx f_a \theta_i[1 - J_0(m/H_0)/J_0(0)] \approx f_a \theta_i \times O(1)\), and the text explicitly states that for \(m/H_0 \sim 1\), \(1 - J_0(1) \approx 0.24\), i.e. \(\Delta\phi/f_a \sim 0.24\,\theta_i\), an \(\mathcal{O}(1)\) fraction.[p.1–2] Eq. (2) then writes \(\beta \approx C_0\,\theta_i/2 \times O(1)\), consistent with \(\Delta\phi/f_a\sim O(1)\).[p.2] Immediately after, however, the text asserts “the cosmological field evolution gives \(\Delta\phi/f_a \sim 10^{-2}\)” and uses this to obtain \(\beta \approx C_0 \theta_i \times 5 \times 10^{-3}\,\text{rad} \approx 0.27^\circ\).[p.2] There is no derivation or change of assumptions that would reduce the \(\mathcal{O}(0.24)\) factor in Eq. (1) down to \(10^{-2}\); the two statements are mathematically incompatible for the same \(m\sim H_0, \theta_i \sim 1\).  
Required fix:  
- Either derive a proper cosmological solution that genuinely gives \(\Delta\phi/f_a \sim 10^{-2}\) for the stated parameter choices, or remove/replace that number and keep the scaling implied by Eq. (1).  
- Make the chain \(\Delta\phi/f_a \Rightarrow \beta\) fully consistent: if you change the effective “O(1)” factor from 0.24 to \(10^{-2}\) you must show explicitly what physics (e.g., different mass, initial conditions, or integration interval) justifies it.  
- Rewrite the paragraph so that Eq. (1), Eq. (2), and the quoted 0.27° prediction all follow from a single, coherent set of assumptions.

---

P2-E11 (ESSENTIAL) – §6 “matches the combined Planck + ACT measurement at 1σ” – unquantified and not reproducible  
Problem: In §6 the text claims “The ALP birefringence prediction β ≈ 0.27° … matches the combined Planck + ACT measurement at 1σ.”[p.4–5] However:  
- The “combined Planck + ACT” measurement is not clearly defined as a single number; the paper quotes \(β_\text{combined} = 0.242 \pm 0.061^\circ\) from a summary likelihood,[Eq.(4)] and \(β_\text{obs} = 0.342 \pm 0.094^\circ\) from the “Eskilt et al. joint analysis.”[p.1,3]  
- If the 1σ‑matching refers to βcombined, then \(|0.27 - 0.242| / 0.061 ≈ 0.46σ\), which is within 1σ but not shown or stated; if it refers to βobs, \(|0.27 - 0.342| / 0.094 ≈ 0.77σ\).  
- No actual Δβ/σcombined is computed in the text, and the phrase “at 1σ” is left as a qualitative assertion.  
Required fix:  
- State explicitly which measurement you are comparing to (βcombined or βobs) and compute \(\Deltaβ / σ\) numerically to justify “1σ.”  
- Clarify that this is a simple Gaussian consistency check based on central values and uncertainties, not a dedicated likelihood comparison between a fixed‑β prediction and the data.

---

P2-M8 (MAJOR) – Abstract & §6 – “Combined, the evidence exceeds 3.5σ” without defined combination method  
Problem: The Introduction states that “The Planck HFI analysis [Minami and Komatsu, 2020] reported β = 0.35 ± 0.14° (2.5σ), and the ACT DR6 analysis confirmed the signal at comparable significance. Combined, the evidence exceeds 3.5σ.”[p.1] There is no description anywhere in the paper of how this “combined” σ is computed—no explicit weighted average, no reference to a joint likelihood, and no quoted ACT number to allow reproduction. The only explicit combination performed is later in Eq. (4), where Planck NPIPE and an asserted ACT DR6 value are combined to yield 3.9σ, but this uses different inputs than Minami & Komatsu plus an unspecified ACT analysis.  
Required fix:  
- Either remove or qualify the “Combined, the evidence exceeds 3.5σ” statement, or show explicitly how this significance is obtained (e.g., inverse‑variance combination of two specified Gaussian constraints with quoted numbers).  
- If the intent was simply to paraphrase the qualitative literature consensus, make that attribution clear and do not present 3.5σ as your own quantitatively derived result.

---

P2-M9 (MAJOR) – §3.3 & Fig. 2 – unquantified “no tension” and “all three are consistent” claims  
Problem: §3.3 states “The ALP model reproduces the observed birefringence with no tension.”[p.3] Figure 2’s caption says “All three are consistent with each other and with the observed value βobs = 0.342 ± 0.094°.”[p.4] However:  
- No quantitative comparison is given: the paper does not compute, for example, \(|β_\text{ALP} - β_\text{obs}| / \sqrt{\sigma_\text{ALP}^2 + \sigma_\text{obs}^2}\) or similar.  
- Different β determinations (βALP, βfree, βobs, βcombined) stem from different likelihoods and possibly different datasets, but are treated as directly comparable without stating that the underlying null procedures and priors differ.  
Required fix:  
- Add a brief quantitative check (e.g., Δβ/σcombined) for at least βALP vs βobs and βfree vs βobs, and state the numerical level of agreement (e.g., “differences are < 0.3σ”).  
- Acknowledge explicitly that the ALP‑derived β and the βfree fit are based on the same βobs likelihood and are therefore not independent confirmations, just internal consistency checks.

---

P2-M10 (MAJOR) – Abstract & §3.2 – use of “order-unity, no fine-tuning” for fphoton × C0 without definition or context  
Problem: The abstract calls \(f_\text{photon} \times C_0 = 1.73 \pm 0.44\) “order‑unity, no fine‑tuning,”[Abstract] and §3.2 repeats that this is “consistent with the ALP prediction without fine‑tuning.”[p.2] However:  
- fphoton is never defined anywhere in the paper (units, relation to gaγ, and to fa are all unspecified), making it impossible to judge whether 1.73 is “order‑unity” in a physically meaningful sense.  
- There is no discussion of what range of fphoton × C0 would be considered tuned versus natural, or how this compares to typical anomaly coefficients or couplings in the literature.  
Required fix:  
- After properly defining fphoton (see P2‑E5), either justify quantitatively why values in the 1–3 range correspond to “no fine‑tuning” (e.g., by comparison to known anomaly coefficients) or soften this language (e.g., “numerically of order one, within the a priori assumed prior range”).  
- Avoid using “no fine‑tuning” as a strong claim unless a concrete criterion for tuning is provided.

---

P2-m1 (MINOR) – §3.3 Table 1 – ambiguous use of “Samples” and “Neff ~ 1,000”  
Problem: Table 1 lists “Samples” for each run (e.g., 2,160; 6,840; 720) and the text then states “the small effective sample sizes (Neff ∼ 1,000) limit the precision of tail estimates.”[p.3] It is not clear whether the numbers in the table refer to post‑burn‑in draws per chain, total draws summed over chains, or effective samples after thinning; nor is it clear how “Neff ∼ 1,000” is derived from these values.  
Required fix:  
- Clarify in the text (or a footnote to Table 1) whether “Samples” means raw posterior draws per run or effective samples, and specify how Neff was computed (e.g., via autocorrelation times).  
- Ensure the description is internally consistent (e.g., avoid implying Neff ~ 1,000 for a run that lists only 720 samples unless that 720 is per chain and multiple chains are combined).

---

P2-m2 (MINOR) – §4 LiteBIRD forecast – “excluded at 9σ” phrasing without symmetric treatment of uncertainties  
Problem: §4 states “If LiteBIRD measures β = 0 ± 0.03°, the ALP explanation is excluded at 9σ.”[p.3] This assumes that the only uncertainty is the LiteBIRD measurement error and treats the theoretical prediction β = 0.27° as exact. In reality, the model prediction depends on order‑unity parameters C0 and θi, for which the paper itself later allows a range (e.g., Caγ × θi = 3.4 ± 1.1).[Eq.(8)]  
Required fix:  
- Add a brief sentence noting that this 9σ exclusion assumes the central prediction β = 0.27° with negligible theoretical uncertainty; in practice, uncertainties in C0, θi and the cosmological integration would broaden the prediction and slightly weaken the formal “σ” interpretation.  
- Alternatively, present the forecast significance as a range based on plausible variation in the predicted β.

---

P2-m3 (MINOR) – §6 bullet point 2 – “matches … at 1σ” refers to “combined Planck + ACT measurement” whereas the body uses “Planck NPIPE + ACT DR6”  
Problem: Bullet point 2 in §6 calls the relevant observable “the combined Planck + ACT measurement,”[p.4–5] while §3.2 explicitly defines the combined constraint using “Planck NPIPE [Eskilt and Komatsu, 2022]” and “ACT DR6 [Diego-Palazuelos and Komatsu, 2025]”.[p.2–3] The change in wording could be read as implying a more general Planck‑wide + ACT combination than the specific NPIPE + DR6 summary likelihood actually used.  
Required fix:  
- Harmonize the terminology: specify in §6 that the “combined Planck + ACT measurement” refers to the particular NPIPE+DR6 combination defined in §3.2 and Eq. (4).  
- This makes it clear that the 1σ statement is about that specific summary likelihood, not an exhaustive Planck+ACT joint analysis.

If you would like, I can now do a targeted pass on the equations alone (for dimensions and hidden assumptions) or on the figure/appendix consistency, but that would require access to the full compiled figures/appendices beyond the text you provided.