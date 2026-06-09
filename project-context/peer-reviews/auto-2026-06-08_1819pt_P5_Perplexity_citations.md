# P5 auto-2026-06-08_1819pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (13068 chars)
**Wall time**: 145.5s

---

P5-E1 (ESSENTIAL)  
Section: Throughout; Abstract, §II, §V.B, §VIII, references (no page numbers available; refer to occurrences by content)  
Problem: Heavy reliance on an unpublished, “in preparation” companion paper (Paper IV [3]) whose results are treated as quantitative, load‑bearing inputs, including the key catalog monopole \(\Delta f_{\rm CW} \approx -0.0026\), catalog‑level \(\sigma\), dipole null, imaging‑leg systematics characterization, and even the chirality labels themselves. The reference is listed as “in preparation; manuscript in preparation,” not an arXiv preprint or accepted paper. This is below PRD’s standard when the entire analysis hinges on that work.  
Required fix: Paper IV must be publicly available in a citable form (at minimum on arXiv with a stable version) and its key statistical numbers verified, or the present paper must be rewritten so that all quantitative uses of Paper IV (monopole value and uncertainty, dipole null, imaging‑leg systematics, per‑leg splits, classifier performance, etc.) are either reproduced within this paper (with full methodological detail) or removed. The claim that environment‑dependence is limited “beyond the catalog monopole” is not acceptable unless that monopole is itself transparently documented in a published or submitted reference.

P5-E2 (ESSENTIAL)  
Section: References [1], [2] (Appendix A, operator discussion)  
Problem: The paper states explicitly that the toy operator \(L_{\rm parity} \supset g_\phi (\nabla_i\phi)(\nabla_i\rho/\rho_{\rm bg})(\hat L\cdot \hat z)\) is “not contained” in Alexander & Yunes 2009 [1] or Lue et al. 1999 [2], and that these works “motivate the general class” only. This is acceptable as long as the actual content and metadata of [1] and [2] are correct. Checking:  
• [1] Alexander & Yunes, Phys. Rep. 480, 1 (2009), “Chern–Simons modified general relativity,” doi:10.1016/j.physrep.2009.07.002, arXiv:0907.2562 — matches arXiv and ADS.[1]  
• [2] Lue, Wang & Kamionkowski, Phys. Rev. Lett. 83, 1506 (1999), “Cosmological signature of new parity-violating interactions,” arXiv:astro-ph/9812088 — title, journal, year and arXiv ID are correct.[2]  
However, the language “inspired by but not derived from the cited parity‑violating‑gravity literature” risks reader confusion about whether these references actually support any quantitative bound.  
Required fix: Tighten the wording in Appendix A to make crystal clear that [1] and [2] are used only to motivate the existence of parity‑violating interactions in cosmology, not to justify this particular operator or the specific scaling of the bound. For example: “Following the general idea of parity‑violating interactions in [1,2], but not any specific operator therein, we introduce the following toy coupling …” The current language is close but should be sharpened to avoid misinterpretation.

P5-E3 (ESSENTIAL)  
Section: Abstract and §V.A (Equation (1)); use of “σ” across disparate nulls  
Problem: The manuscript uses \(\sigma\) language for several different test statistics and null procedures (simple Gaussianized binomial deviation “σfrom half”, a predicted “σpred” from the Paper IV monopole, permutation‑based max‑stat nulls, and Bonferroni thresholds) and then juxtaposes “σ” values from these different contexts side by side (e.g., “cluster −4.66σ”, “3.4σ bright‑vs‑dark sign‑flip”, “none reach 3σ after look‑elsewhere correction”) without always reiterating that these σ values are not directly comparable between procedures. The instructions explicitly require a clear statement whenever σ from different procedures are shown together.  
Required fix: At every location where σ from different null constructions are reported side‑by‑side (e.g., Abstract, §VI.A–E, §VII, §VIII.F, §IX.A, §XI), insert explicit wording indicating non‑comparability, such as: “These σ values are defined with different nulls and are not directly comparable.” In tables that contain both “σfrom half” and residuals relative to σpred, this must be spelled out in the caption or immediately in the text.

P5-E4 (ESSENTIAL)  
Section: Abstract and §VIII (DESIVAST usage)  
Problem: DESIVAST is cited as Rincón et al. 2025, ApJ 982, 38 , with an arXiv:2411.00148. Checking ADS/arXiv: the paper “DESI‑VAST: Catalogs of Low‑redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey” by H. Rincón et al. exists with ApJ 982, 38 (2025) and arXiv:2411.00148; metadata is correct. However, the text states explicitly that DESIVAST is “peer-reviewed DR1 BGS void catalog… standardized across the DESI collaboration”. This is fine; nonetheless, the claimed numbers (e.g. 1,461 interior voids for VoidFinder, 420 REVOLVER, 295 VIDE, 3,765 maximal voids, 101,863 holes) must be checked against the DESIVAST paper’s abstract/tables. Those specific counts do not appear in the abstract; they are catalog‑level details coming from the VAC, not summarized in the paper’s main text. PRD typically expects that numerical claims tied to a citation can be traced to that citation.  
Required fix: Either (i) explicitly state that those detailed counts (e.g. “101,863 interior holes”) are derived by the author directly from the released DESIVAST files and not from the Rincón et al. 2025 journal article, or (ii) remove the appearance that these precise counts are “from” . Make clear which numbers are from the publication vs from the author’s own analysis of the DESIVAST VAC.

P5-E5 (ESSENTIAL)  
Section: Abstract (“χ2 = 4932, 3 d.o.f., p < 10−1000”)  
Problem: The paper quotes an extremely small p‑value “p < 10−1000” for a 4×2 contingency table (3 d.o.f.) with χ² = 4932. This number is far beyond machine precision and is not traceable to any cited external reference; it is a new calculation. For referee purposes, one must check the numerical reasonableness: for 3 d.o.f., χ² = 4932 implies a tail probability vastly smaller than 10^{-1000}, but the exact “10−1000” floor is arbitrary. This is presented as a calculated statistic without explanation of numerical method.  
Required fix: Replace “p < 10−1000” with a more defensible and reproducible statement, e.g. “p ≪ 10^{-50}” or “p ≲ 10^{-300} (underflow to zero in double precision)”. Alternatively, explicitly state how this p‑value was computed (e.g., using log‑gamma approximations) and give a realistic bound. As written, “10−1000” looks like a rhetorical exaggeration, which is not acceptable in PRD.

P5-E6 (ESSENTIAL)  
Section: Bibliography and in‑text references [3], [4], , ,   
Problem: Need to verify all references and IDs:  
• [3] “H. Golden, A Survey-Scale Chirality Catalog … companion paper (Paper IV), in preparation.” No arXiv ID, not traceable. This is already covered by P5‑E1.  
• [4] “H. Golden, fNL = −35/8 Forecast: SPHEREx Discrimination … companion paper (Paper II), in preparation.” Also not on arXiv or ADS as far as search reveals.  
• [5] Hahn et al. 2007 — Mon. Not. R. Astron. Soc. 375, 489 (2007), “Properties of dark matter haloes in clusters, filaments, sheets and voids”; arXiv:astro-ph/0610280, correct.  
• [6] Hoffman et al. 2012 — MNRAS 425, 2049, “A kinematic classification of the cosmic web,” arXiv:1201.3367, correct.  
• [7] Cautun et al. 2014 — MNRAS 441, 2923, “Evolution of the cosmic web,” arXiv:1401.7866, correct.  
•  Planck 2018 results. VI. Cosmological parameters, A&A 641, A6 (2020), arXiv:1807.06209, correct.  
•  Shamir 2022 — MNRAS 516, 2281, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” arXiv:2208.13866, correct.  
•  Tempel et al. 2014 — A&A 566, A1, “Flux- and volume-limited groups/clusters for the SDSS galaxies: catalogues and mass estimation,” arXiv:1402.1350, correct.  
•  Ullah et al. 2026 — arXiv:2604.02463, “Cosmic-web quenching with DESI DR1: T-Web environments and mass-dependent red/blue classification,” preprint, not peer‑reviewed; metadata matches arXiv.  
•  Zapata‑Zuluaga et al. 2026 — arXiv:2604.01456, “The Cosmic Web in the DESI Early Data Release: A Probabilistic Environment Catalog,” preprint; metadata matches arXiv.  
•  Rincón et al. 2025 — ApJ 982, 38; arXiv:2411.00148, “DESI‑VAST: Catalogs of Low‑redshift Voids Using Data from the DESI Data Release 1 Bright Galaxy Survey,” correct.  
The fused metadata issue: references  and  are explicitly “preprint (2026)”; the main text at places speaks of them nearly as “published public DR1 product” or “published DESI environmental VAC,” which over‑states their status.  
Required fix: Clearly mark  and  as preprints in the main text wherever their catalogs are treated as “public products,” and avoid language that implies peer review or official DESI endorsement beyond what those preprints state. Maintain consistency: they are independent preprints, not yet refereed.

P5-E7 (ESSENTIAL)  
Section: Abstract and §III.B (“16,361,731 DR1 input rows”)  
Problem: The DR1 zall‑pix‑iron.fits row count and cuts are stated as “not published DR1 constants; the fetch + filter driver is derived in this work.” That is acceptable, but there is no explicit check against the DR1 documentation. DR1 public docs describe the spectroscopic catalog and target selection; however, the exact count 16,361,731 is not in the abstract of any cited DESI paper and is thus a new number. For PRD, such basic dataset counts should be either cross‑checked against official DR1 release notes or clearly labeled as “derived by the author from the files,” not implied as DR1 published metadata.  
Required fix: Add a short clarifying sentence in §III.B such as: “These row counts are computed directly from the public DR1 zall catalog by our own cuts and are not quoted from any DESI publication.” That removes any impression of mis‑citation.

P5-M1 (MAJOR)  
Section: Abstract; Table II; §VI.A  
Problem: The abstract states the per‑class CW fractions for the V‑Web canonical run and calls these “headline result”. However, the true primary analysis is later redefined to be the DESIVAST‑anchored void test; V‑Web is then declared “secondary.” This is internally inconsistent: the abstract reads as if the V‑Web result is the main claim. PRD expects the abstract to reflect the analysis hierarchy described in the body.  
Required fix: Revise the abstract so that the DESIVAST‑anchored void cross‑check (with n = 56,981 and \(\Delta f_{\rm CW} = 0.0007\)) is clearly identified as the primary test, and the V‑Web per‑class fractions presented as one of several supporting diagnostics. The current wording “primary path of this paper is the DESIVAST-anchored void cross-check; the V-Web classification is the supporting cross-check” appears, but the numerical emphasis is almost entirely on V‑Web. Rebalance the emphasis and make the hierarchy unambiguous.

P5-M2 (MAJOR)  
Section: Abstract; §VI.D; §VIII (bright vs dark tracer discussion)  
Problem: The paper claims that the catalog‑level −5σ monopole is “entirely driven by the BGS‑bright sample,” and that the LRG/ELG/QSO sample returns +1.25σ in the opposite sign, leading to a |z| ≈ 3.4σ bright‑vs‑dark difference. This is an important residual and is used to argue that environment trends are likely selection‑function driven. However, there is no check that the 3.4σ two‑sample z test is computed correctly from the stated numbers, and the underlying counts (nbright, ndark and fCW for each) are not given in a table; they appear only scattered in the text. This is fragile from a reader‑audit standpoint.  
Required fix: Add a small table with the actual nCW and nCCW for bright and dark subsamples in the relevant environment class (filament, and cluster if quoted). From those, explicitly define and compute the two‑sample z statistic in the text. This will allow readers to verify the 3.4σ claim. Also, whenever interpreting this as a “real residual structure,” emphasize the caveat that this is not corrected for multiple testing across all explored splits.

P5-M3 (MAJOR)  
Section: §VI.C, Table III and Figure 3 (density‑quintile test)  
Problem: The “Paper IV monopole prediction” is stated as \(\sigma_{\rm pred} = -2 \Delta f_{\rm CW} \sqrt{N}\) at \(\Delta f_{\rm CW} = -0.0026\). This follows automatically from the definition of σfrom half, so numerically it is fine. However, the table mixes |σobs − σpred| and Bonferroni thresholds, with all significance language resting on the correctness of \(\Delta f_{\rm CW}\) from Paper IV. Since Paper IV is not citable, this entire correction procedure is only as trustworthy as the missing paper.  
Required fix: If Paper IV becomes citable, this section should explicitly reference the specific equation and monopole values in Paper IV and, ideally, reproduce the derivation of \(\Delta f_{\rm CW}\) and its uncertainty so that readers can assess whether using a point estimate of −0.0026 without error bars is justified. If Paper IV remains unavailable, the density‑quintile section should be rewritten to present raw σfrom half and permutation p‑values only, without a “monopole‑corrected residual” interpretation.

P5-M4 (MAJOR)  
Section: §VII (Phase‑2 sensitivity sweep; Figure 5; Table VI)  
Problem: The sweep over Rs and λth is claimed to show that the maximum inter‑class range is 0.22 percentage points, always below “counting‑statistics floors”. This is important to the robustness claim, but the actual numbers for each class per (Rs, λth) cell are not shown, only the ranges. Without a table of per‑class fCW and n for each cell, these ranges are not verifiable by the reader.  
Required fix: Provide either in the main text or an appendix a table listing, for each of the 9 (Rs, λth) combinations: per‑class n and fCW. With that, one can recompute the ranges and the claimed 0.22 pp maximum, and check that they are indeed below the quoted binomial 1σ uncertainties.

P5-M5 (MAJOR)  
Section: §X (ASTRA EDR cross‑validation) and references ,   
Problem: The ASTRA catalog  and the concurrent T‑Web analysis  are preprints. The text sometimes calls ASTRA “published DESI environmental catalog” or similar and speaks of “public DR1 product” for DESIVAST, conflating the status of different datasets. Also, the ASTRA overlap is only 25,186 objects, and per‑galaxy labels differ substantially between ASTRA and V‑Web, yet the text occasionally treats their agreement in aggregate fCW as strong robustness. PRD standards require a clearer separation between solid, peer‑reviewed inputs and more tentative, small‑sample cross‑checks.  
Required fix: Tone down any language implying that ASTRA or Ullah et al. have the same status as DESIVAST or DR1 itself. Make explicit that ASTRA is EDR‑only and preprint‑level, and that the 25k‑object overlap is a small, non‑independent check that should be interpreted cautiously. Clarify that their per‑class fCW null is consistent with, but does not materially strengthen, the headline DESIVAST‑based conclusion.

P5-M6 (MAJOR)  
Section: Appendix A (toy EFT mapping)  
Problem: The effective operator mapping (toy EFT) is explicitly described as “not derived” from the cited literature, not gauge invariant, and only schematic. Nonetheless, it proceeds to write a numerical bound of order \(|g_\phi (\nabla\phi)/H_0| \lesssim 10^{-2}/\langle|\Delta\rho/\rho_{\rm bg}|\rangle\) and calls this an “order‑of‑magnitude bound.” This risks being misread as a real phenomenological constraint, even though the calculation is not actually carried out.  
Required fix: Either remove the numerical bound entirely, keeping only a qualitative statement that the current \(|\Delta f_{\rm CW}|\) limits place an upper bound on any such coupling, or add a much clearer disclaimer that no explicit transfer‑function calculation has been done and that the number is not to be interpreted as a quantitative constraint. PRD generally prefers not to include half‑finished EFT estimates unless they are carefully justified.

P5-M7 (MAJOR)  
Section: Overall length (20 pages) vs claimed contribution  
Problem: The paper is long relative to the core scientific claim, which is essentially a null test: “no environment dependence at DR1 sensitivity.” There is extensive, somewhat repetitive detail on multiple classifiers, null tests, and robustness checks that are secondary once the primary DESIVAST analysis is established. PRD expects concision commensurate with the novelty of the result.  
Required fix: Streamline the manuscript. A recommended target is ≈12–14 pages by moving some of the more routine null tests (e.g. some HEALPix scans, minor variants of the density and redshift stratifications, and secondary ASTRA cross‑checks) to an online supplement or data repository. The main text should focus on: data definition, primary DESIVAST analysis, V‑Web and Tempel cross‑checks, key systematic tests, and then a succinct discussion.

P5-M8 (MAJOR)  
Section: Claims of “largest” / “cleanest” measurements (e.g. §VIII.D)  
Problem: There are statements like “This is the cleanest single chirality-in-voids measurement in this paper at n ≳ 80,000” and “largest matched-sample environmental-dependence test … to date.” These qualitative superlatives are not supported by external citations. For the “to date” claim in particular, there is no systematic comparison to existing chirality–environment studies (beyond Shamir 2022 which is an all‑sky asymmetry, not environment‑conditioned).  
Required fix: Either provide appropriate citations showing that no larger environment‑conditioned chirality sample exists, or weaken the language (e.g. “to our knowledge within DESI DR1” or simply “in this work”). For PRD, unqualified “largest to date” claims should be avoided without a literature survey.

P5-N1 (MINOR)  
Section: Abstract (“p = 0.61/0.135/0.413”)  
Problem: The notation for multiple p‑values separated by slashes is non‑standard and can be confusing.  
Required fix: Replace with explicit notation, e.g. “p = 0.61, 0.135, and 0.413 for NSIDE = 16, 32, and 64, respectively.”

P5-N2 (MINOR)  
Section: Various (e.g. Table captions, text around Figures 3–5)  
Problem: Units are sometimes implicit (e.g. “25 Mpc/h Gaussian smoothing” is clear, but “6,634 Mpc/h at 256^3 → cell 25.9 Mpc/h” could be misread without stating comoving/h units in the figure caption).  
Required fix: Ensure that all key physical quantities appearing in figures and tables have units either in the axis label or the caption (e.g., “R_s in comoving h^{-1} Mpc”).

P5-N3 (MINOR)  
Section: Eq. (2) and (3) (Bonferroni and permutation pLEE)  
Problem: The symbols \(|\sigma|_{\rm Bonf}\) and \(|\sigma|_{\rm max}\) are introduced but not clearly defined in a stand‑alone way for a reader arriving at this section cold.  
Required fix: Add a brief sentence explicitly defining \(|\sigma|_{\rm Bonf\,\alpha,K}\) as the Bonferroni‑adjusted per‑family threshold and \(|\sigma|_{\rm max}\) as the maximum absolute deviation across bins.

P5-N4 (MINOR)  
Section: §III.C (cross‑match method)  
Problem: The parameter choices for the cross‑match (1″ primary radius, exploration out to 5″) are sensible, but there is no reference to any DESI or imaging‑catalog paper that justifies 1″ as consistent with fiber positioning. This is an implied but uncited claim.  
Required fix: Briefly justify the 1″ radius by referencing DESI fiber positioning precision or the underlying imaging astrometry, or clearly state that 1″ is chosen conservatively by the author and validated by the observed separation distribution (p50, p99), which is already given.

P5-N5 (MINOR)  
Section: §XIII (RSD discussion)  
Problem: The text uses quantities like “σ_rs d ∼ 5 Mpc/h” and “σ_v ≲ 400 km/s” without explicit references. These are standard order‑of‑magnitude values but should either be referenced (e.g. to a DESI clustering paper) or explicitly described as rough estimates.  
Required fix: Clarify that these are order‑of‑magnitude estimates and, if possible, add one standard reference on RSD scales in BOSS/DESI‑like surveys.

P5-N6 (NIT)  
Section: Several places (e.g. “null is at σ = 0.43, p = 0.30 for direct amplitude estimation and −0.12σ for the subsample-mask MASTER-deconvolved ℓ = 1 amplitude”)  
Problem: Mixed notation of \(\ell\) and “l” (ell vs L) is not consistently typeset in math mode in the snippet provided.  
Required fix: Ensure consistent use of \(\ell\) for multipole indices in math mode throughout.

P5-N7 (NIT)  
Section: Reproducibility checklist  
Problem: “Deterministic seed: 20260515” is fine, but PRD will not archive code or configs; this is more appropriate for a data‑repository README than for the main paper.  
Required fix: Move the detailed bullet‑point reproducibility checklist (seed value, config file existence) to an online supplement or data‑repository documentation, and keep only a concise “Data and code availability” paragraph in the paper.

P5-N8 (NIT)  
Section: Throughout  
Problem: A few minor typographical/formatting issues: line breaks split words (“spec- tro sample”, “stat-istics”), likely due to PDF extraction; these must be checked in the actual TeX. Also occasional hyphenation like “classifier- monopole”.  
Required fix: Proof‑read the final TeX to remove awkward hyphenation and ensure words are not split across lines in the published version.

P5-N9 (NIT)  
Section: §VIII.A (“0/6 V-Web ‘void’ spirals inside any of the 101,863 DESIVAST VoidFinder holes”)  
Problem: The phrase “0/6” for a cross‑match sample is acceptable, but it might be clearer to give a binomial 95% upper limit on the misclassification fraction, in keeping with the otherwise statistical tone.  
Required fix: Optionally add “(95% CL upper limit ≈ 45%)” or similar, or note explicitly that this is too small a sample for a meaningful quantitative constraint and is presented only illustratively.

## Summary recommendation

REJECT

The conceptual idea—testing environment‑dependence of spiral chirality in DESI DR1—is solid and potentially interesting, but the present manuscript is not yet suitable for PRD. The analysis depends critically on an unpublished companion (Paper IV) for the chirality catalog, classifier bias (monopole) characterization, and key systematics, and numerous significance statements and “monopole‑corrected” interpretations cannot be independently verified without that paper. Several robustness arguments are therefore on shaky footing. In addition, the paper is overly long for a null result, and some methodological and citation practices (e.g., extremely tiny quoted p‑values, partially developed EFT mapping) do not meet PRD’s standards for rigor and clarity. I recommend resubmission only after Paper IV is publicly available and the present work is substantially tightened, with a clearer separation between solid, self‑contained results and speculative or dependent components.

---

## PASS 2 — self-critique findings (what initial review missed)

P5-E8 (ESSENTIAL)  
Section: §VI.D (“Within-class density-stratified cluster + filament follow-up”; Table IV – cluster quartiles)  
Problem: The cluster quartile σ values in Table IV are internally inconsistent with the given definition \(\sigma_{\rm from\ half} \equiv (n_{\rm CW}-0.5N)/(0.5\sqrt{N})\). For example, for cluster Q1 (n = 99,398, \(\sigma = -3.07\)) this implies \(n_{\rm CW}\approx 48{,}310\) (\(f_{\rm CW}\approx 0.4859\)), while cluster Q2 (same n, \(\sigma=-3.42\)) implies \(n_{\rm CW}\approx 47{,}897\) (\(f_{\rm CW}\approx 0.4818\)). Averaging these with Q3 and Q4 to recover the catalog cluster mean \(f_{\rm CW}=0.4963\) (Table II) is impossible: the implied mean over quartiles would be \(\lesssim 0.49\), not 0.4963. In other words, either the σ’s or the mapping between quartiles and counts has changed without updating the table, or the quartiles are not equal-population as claimed, but the n’s are still listed as exactly equal (99,3xx), which suggests stale or inconsistent numbers.  
Required fix: Recompute and explicitly tabulate, for each cluster and filament quartile: \((n, n_{\rm CW}, f_{\rm CW}, \sigma_{\rm from\ half})\), and verify that the four quartiles sum back to the class totals in Table II. Correct Table IV and the surrounding text so that the σ values, fractions, and the global class numbers are mutually consistent.

P5-E9 (ESSENTIAL)  
Section: §VI.D (“Redshift-stratified cross-check” in the cluster class)  
Problem: The redshift-quartile σ values for the cluster class (Z1–Z4) are not reconcilable with the overall cluster mean \(f_{\rm CW}=0.4963\) (Table II). At n = 99,376–99,377 and σ values −2.33, −1.73, −3.14, −2.12, the implied four quartile fractions are all ≈ 0.49 or below; their average cannot yield 0.4963 (which is closer to 0.5 than any individual quartile). This again points to σ (and/or n) values that were modified at some point without updating either the quartile decomposition or the class-level numbers.  
Required fix: As above, provide explicit \((n, n_{\rm CW}, f_{\rm CW}, \sigma_{\rm from\ half})\) for each redshift quartile and ensure that: (i) the four quartiles sum to the total cluster counts in Table II, and (ii) the σ values match the stated formula. Correct either the quartile σ’s or the class totals so they are arithmetically consistent.

P5-E10 (ESSENTIAL)  
Section: §VII (“Phase 2 sensitivity sweep”; largest σ and monopole prediction)  
Problem: The text states that “The largest single-cell \(|\sigma_{\rm from\ half}|\) across the entire sweep is 11.32 (filament at \(R_s = 10\), \(\lambda_{\rm th} = 0\), \(n = 3{,}696{,}152\)). This is … predicted, not measured: \(\sigma_{\rm pred} \approx -0.0026 \cdot 2 \sqrt{N} \approx -10\) matches the observed −11.3 within order unity.” This mixes two different approximations: with the paper’s own definition \(\sigma_{\rm pred} = 2\Delta f_{\rm CW}\sqrt{N}\) and \(\Delta f_{\rm CW}=-0.0026\), the prediction is \(\approx -12.54\) for \(N=3{,}696{,}152\), not −10. Using the simplified \(-0.0026\cdot 2\sqrt{N}\) as written actually gives ≈ −12.54, not −10. The numerical check in the text is therefore incorrect and undermines the claim that the extreme σ is “predicted, not measured.”  
Required fix: Recompute \(\sigma_{\rm pred}\) for the quoted cell using the stated formula and either (i) update the text to give the correct numerical value and its comparison to −11.32, or (ii) remove the specific “≈ −10” claim and simply state that the observed value is consistent with the monopole prediction within 1σ. Ensure all other uses of Eq. (1) in the sweep use consistent arithmetic.

P5-M9 (MAJOR)  
Section: §VI.D (“b. Tracer-program stratification”; bright/dark σ and 3.4σ z-test)  
Problem: The paper quotes program-level σ’s (bright: −5.25, dark: +1.25) and a filament two-sample \(|z| \approx 3.4σ\) bright–dark difference, but never gives the underlying counts \(n_{\rm CW}, n_{\rm CCW}\) for bright and dark in each environment class. Some of the σ’s can be approximately checked using the provided n’s and f’s elsewhere (e.g., filament dark n = 21,203, σ = +2.85), but without a compact table it is not possible for a reader to verify that the quoted 3.4σ comes from a correctly computed two-sample proportion test rather than an approximate or stale number. This is especially important because this bright–dark residual is highlighted as the “strongest single residual structure in the paper.”  
Required fix: Add a small table that gives, at minimum for the filament (and optionally cluster) class: \(n_{\rm CW}^{\rm bright}, n_{\rm CCW}^{\rm bright}, f_{\rm CW}^{\rm bright}\) and \(n_{\rm CW}^{\rm dark}, n_{\rm CCW}^{\rm dark}, f_{\rm CW}^{\rm dark}\). Next to that, explicitly write the two-sample z-statistic used and show it evaluates to ≈ 3.4 with these numbers. Correct any numerical values if necessary. Make clear that this 3.4σ is not look-elsewhere corrected.

P5-M10 (MAJOR)  
Section: §VII; Table VI and Fig. 5 (Phase 2 ranges vs. “counting-statistics floor”)  
Problem: The argument that the maximum inter-class range (0.22 pp) is “below the per-class counting-statistics floor” is only qualitatively supported. The counting floor is described in terms of per-class uncertainties (0.08 pp for filament/cluster, 0.6 pp for wall, 2.4 pp for void), but the 0.22 pp quantity is a range across four classes, not a simple per-class σ. Because ranges of four noisy estimates have a different sampling distribution, it is not mathematically obvious that a 0.22 pp range is always “sub-noise” based only on those per-class σ’s, and that claim is not backed by any Monte Carlo or analytic calculation in the text. This is more a conceptual than arithmetic gap, but it weakens a central robustness argument.  
Required fix: Either (i) add a brief Monte Carlo or analytic estimate of the expected distribution of the max inter-class range under the null for the quoted class n’s and show that 0.22 pp is within, e.g., the 68–95% range, or (ii) weaken the wording to say simply that 0.22 pp is “of the same order as” the per-class 1σ uncertainties and that no single class deviates from the monopole by more than ≈1σ in any cell. Avoid claiming that the range is definitively “below the counting-statistics floor” without such support.

P5-M11 (MAJOR)  
Section: §VIII.F; Table X (“σ vs monopole residuals”)  
Problem: Table X reports, e.g., for the filament class \(f_{\rm CW}-f_{\rm CW}^{\rm P5}=+0.0008\) and \(\sigma_{\rm vs\ monopole}=+0.99\). Using the paper’s σ definition and the quoted n = 408,187, a shift of 0.0008 corresponds to \(\sigma \approx 0.73\), not 0.99. To get ≈ 0.99 would require \(\Delta f\approx 0.0011\). Similar tension appears for other classes. This indicates either that the \(\Delta f\) entries are rounded too aggressively (masking the true value used to compute σ), or that σ has been recomputed after an update to f that is not reflected in the table. In either case, the reader cannot check the “all four classes within |σ|<1.15” statement with the given numbers.  
Required fix: Use consistent precision and ensure that the listed \(f_{\rm CW}-f_{\rm CW}^{\rm P5}\), n, and \(\sigma_{\rm vs\ monopole}\) are mathematically consistent to at least 2–3 significant digits. If necessary, increase the printed precision in Table X (e.g., 4 decimals on f differences) so that recomputing σ from the table values reproduces the quoted σ within roundoff.

P5-M12 (MAJOR)  
Section: §X (“ASTRA EDR per-object cross-validation”; Table XII)  
Problem: For the V-Web-on-overlap classifier in Table XII, “max |σ| vs 1/2 = 2.68” is quoted without any supporting per-class counts or fractions. Given the overlap sample size (25,186) and the statement that V-Web assigns 31.7% to filament and 68.3% to cluster, the corresponding class sizes are around 8,000 and 17,000. A 2.68σ deviation in one of these bins would imply a fractional offset \(|f_{\rm CW} - 0.5|\sim 0.7–0.8\) percentage points. Without a table of \(n_{\rm CW}, n_{\rm CCW}\) per class, it is not possible to verify these numbers, and any stale σ here directly affects one of the cross-check robustness claims.  
Required fix: Provide a compact table for the ASTRA EDR overlap giving, for each environment class and each classifier (V-Web, ASTRA argmax, ASTRA entropy-weighted): \((n, n_{\rm CW}, f_{\rm CW}, \sigma_{\rm from\ half})\). Ensure that the “max |σ| vs 1/2” values quoted in Table XII can be reproduced. Adjust the text or Table XII if discrepancies are found.

P5-N7 (MINOR)  
Section: §V (“Statistical methods”; Eq. (1) and its use)  
Problem: In multiple places, Eq. (1) is applied with slightly inconsistent algebra or notation. The equation is written as \(\sigma_{\rm pred} = \Delta f_{\rm CW}/\sqrt{0.5/N} = 2\,\Delta f_{\rm CW}\sqrt{N}\), but later the text phrases the prediction as “\(-0.0026\cdot 2\sqrt{N}\)” (Sec. VII) without explicitly restating the sign convention. While mathematically equivalent, the mix of forms and the incorrect “≈ −10” numerical evaluation (P5-E10) make it easy to misinterpret or misapply the formula.  
Required fix: Standardize the presentation: always write \(\sigma_{\rm pred} = 2\,\Delta f_{\rm CW}\sqrt{N}\) and, when plugging numbers, show one explicit worked example with correct arithmetic. Remove or correct any shorthand expressions that have already led to numerical mistakes.

P5-N8 (MINOR)  
Section: §VIII.A (“RSD treatment for DESIVAST”) vs §XIII (“Limitations; RSD discussion”)  
Problem: The DESIVAST section asserts fairly strongly that the DESIVAST primary path is “essentially RSD-immune at the level relevant to this work,” while §XIII emphasizes that a proper RSD treatment for V-Web requires reconstruction and that scalar σv/(aH) arguments are only indicative. Although the contexts differ (void membership vs tidal-tensor classification), the contrast in tone can be confusing. The DESIVAST argument rests on the statement that typical RSD displacements (5–8 Mpc/h) are “several times smaller” than void radii, but the text does not give a quantitative bound on how that maps into possible void/non-void misclassification for galaxies near void edges.  
Required fix: Clarify in §VIII.A that the RSD immunity claim for DESIVAST is an order-of-magnitude argument, not a strict proof, and tie it explicitly to the typical void effective radii and edge-fraction of galaxies. Alternatively, soften the language (“RSD effects are expected to be subdominant for the void/non-void split at current precision”) to match the more cautious tone in §XIII.

P5-N9 (MINOR)  
Section: Abstract; §V, §VI, §VII (σ comparability)  
Problem: In addition to the σ-comparability issues already flagged previously (P5-E3), there are a few further juxtapositions that still omit explicit non-comparability language, despite mixing σfrom half, σpred, permutation-based σ-equivalents, and Bonferroni thresholds. Examples include the Abstract sentence that quotes “|σ|max = 3.94” (density quintiles) followed by a “|σobs − σpred| = 1.87, below all Bonferroni thresholds” without an explicit reminder that σpred is not a separate null-sigma and the Bonferroni thresholds are for different statistics. Similarly, in §VII the phrase “no (Rs, λth) cell shows an inter-class chirality signal above the counting-statistics shot-noise null” is framed as if σvs monopole, σfrom half, and Bonferroni thresholds are all on a single common σ scale.  
Required fix: Add short qualifying phrases in these remaining locations, along the lines of: “Note that these σ values arise from different null constructions and are not directly comparable; they are each interpreted within their own test framework.” This can be done very compactly (one clause) but should be present wherever mixed σ’s are used to build a narrative.

P5-N10 (MINOR)  
Section: §VIII.B–D; claims of “cleanest single chirality-in-voids measurement” and “largest matched-sample environmental-dependence test … in this paper / in DESI DR1”  
Problem: Beyond the “largest to date” issue already flagged (P5-M8), there is an internal subtlety: the abstract and §VIII.D sometimes use “cleanest” in a way that conflates two different notions (smallest |σ|, largest n). For example, V2-REVOLVER GALZONE voids (n = 86,276, σ = −0.24) are called “the cleanest single chirality-in-voids measurement,” while the VoidFinder-based void/non-void split has larger nvoid = 56,981 but a slightly larger |σ|. These are both valid senses of “clean,” but the text does not specify which criterion is meant and may give the impression that there is a uniquely best statistic.  
Required fix: Make the criterion explicit when using qualitative labels: e.g., “cleanest (smallest |σ| at n ≳ 80,000)” or “largest-n void sample used in this work.” This will avoid confusion and keep the qualitative claims tightly aligned with the quantitative numbers already given.

If you want, I can next step through specific tables and equations one by one and provide explicit recomputations so you can systematically correct the manuscript.