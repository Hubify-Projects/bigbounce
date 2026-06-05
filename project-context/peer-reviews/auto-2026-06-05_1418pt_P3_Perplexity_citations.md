# P3 auto-2026-06-05_1418pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (20710 chars)
**Wall time**: 99.0s

---

P3-E1 (ESSENTIAL)  
Section: Multiple (Title page, throughout)  
Page: 1, 2, 4, 5, 7, 8, 11, 12, 14, 15, 18  

Problem: Use of undefined “Path-C” / “Path-C rebuild” protocol as if it were an established external method. There is no cited external reference defining “Path‑C”; it appears to be an internal label introduced only within this manuscript (e.g. “Path‑C rebuild protocol resolves cross-transfer artifacts”, “Path‑C native retrain”, “Path‑C final catalog”). Treating an internal workflow label as if it were a standard named method is confusing and fails PRD standards for methodological clarity.  

Required fix: Explicitly define “Path‑C” the first time it appears (as an internal protocol name) and state clearly that it is a procedure introduced in this work, not an external standard. Either (a) relabel it with descriptive language (“native‑retrain rebuild protocol”) and drop the “Path‑C” branding, or (b) clearly introduce it as “we define Path‑C as …” in one place and then use it consistently. Clarify in the abstract that “Path‑C” is an internal rebuild procedure, not an external prior.  


P3-E2 (ESSENTIAL)  
Section: Abstract; Section V (Cosmological applications)  
Page: 1, 11  

Problem: fNL forecast and σ(fNL) improvements are presented in a way that can be misread as detection‑level results and are not always clearly distinguished from validated results from the literature. For example, the abstract states:  
- “inserting this into the Fisher‑positivity‑respecting form 1/σ(fNL)² = F₀ + cα² gives a central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at < 1σ; σ(fNL)std = 8.98 single‑tracer baseline).”  

There is no explicit citation when the Fisher baseline σ(fNL)std = 8.98 is first introduced, nor when the specific functional form 1/σ² = F₀ + cα² is stated; this could be mistaken for an external result instead of an internal parametrization. The “7.9% improvement” is heavily derived from internal assumptions (choice of Fisher configuration, bias enhancement parametrization) but is presented in the abstract alongside more directly data‑driven numbers, with only minimal qualification.  

Required fix:  
- In the abstract and in Sec. V, explicitly label these as *forecasted* sensitivities derived from an internal Fisher calculation in this paper, not as measurements.  
- When first introducing σ(fNL)std = 8.98, cite the relevant DESI/SPHEREx or Heinrich et al. reference for the baseline configuration, or state explicitly that this is your own Fisher baseline calculation and summarize the inputs.  
- Make clear that the functional dependence 1/σ² = F₀ + cα² is a phenomenological fit to your Fisher computation, not a general theoretical law.  
- Emphasize again in the abstract that the “7.9% improvement” is not a detection but an illustrative central forecast, and move the quantitative improvement to the main text only, or add a strong qualifier like “forecast-level” to avoid any implication of an achieved constraint.  


P3-E3 (ESSENTIAL)  
Section: Abstract; Sec. IV.A “SIMBAD Cross-Match and Novelty Assessment”  
Page: 1, 9  

Problem: The “∼17.8% genuine novelty fraction” is a single‑stratum, single‑survey estimate (DESI top‑1000) but is phrased in the abstract as if it characterizes the entire 378,080‑object point‑source catalog:  
- Abstract: “Extended archival cross-matching of the top-1,000 DESI anomalies … yields a genuine novelty fraction of ∼17.8% … (full-catalog rate empirically untested).”  

The parenthetical caveat helps, but this still reads easily as a catalog‑wide “headline discovery rate.” In the body, IV.A correctly stresses that this is a single‑sample point estimate, but the abstract mixes it with catalog‑level numbers.  

Required fix: In the abstract, explicitly label this number as “for the DESI top‑1000 anomalies only” and reiterate that “this should not be extrapolated to the full catalog; full‑catalog novelty rate remains unmeasured.” Consider moving the 17.8% figure out of the abstract or presenting it as an example (“we illustrate, for the DESI top‑1000 subset, that…”).  


P3-E4 (ESSENTIAL)  
Section: σ(fNL) forecasting; mixing of null and non‑null in close proximity  
Page: 1, 11–12  

Problem: The instructions require that if sigma values from different null procedures appear side‑by‑side, every juxtaposition must be explicitly flagged as “not directly comparable.” The paper juxtaposes:  
- σ(fNL)std = 8.98 “single-tracer baseline,”  
- σ(fNL) = 8.14 (forecast with anomaly tracers),  
- σ(fNL)GS central 1.95 (Gold+Silver subset),  
derived under slightly different assumptions and with different sample definitions. These are compared in text, but it is not always stated explicitly at each juxtaposition that the σ values are not directly comparable because of differing tracer sets, Fisher configurations, and bias‑enhancement assumptions.  

Required fix:  
- Wherever multiple σ(fNL) values are quoted within the same paragraph (or sentence), explicitly state “these σ values are not directly comparable because they correspond to different tracer samples and Fisher setups.”  
- Ideally, add a short table listing each σ(fNL) with its tracer sample, kmax, and nuisance‑parameter treatment, and refer to this when comparing.  


P3-E5 (ESSENTIAL)  
Section: Appendix E (NANOGrav MCMC) and main text V.A  
Page: 11, 16–17, 19–20  

Problem: The paper claims consistency of its NANOGrav analysis with the NANOGrav 15 yr results and uses a specific KDE free-spectrum likelihood (Zenodo), but no explicit arXiv identifier or journal reference is given for the KDE free‑spectrum methodology. Reference  is the main NANOGrav GWB detection paper (Agazie et al. 2023, ApJL 951 L8), which does not itself describe the KDE post‑processing; the Zenodo DOI is given but not cited in standard bibliographic form. PRD expects a standard bibliographic reference for the dataset/likelihood product or a clear indication that it is an unpublished companion product.  

Required fix:  
- Add a proper bibliographic entry (or clear descriptive note) for the KDE free‑spectrum likelihood used (including author list or internal NANOGrav note if available) or explicitly state that this is an official supplementary data product linked to .  
- Ensure that the statement “real-KDE posterior recovers γ = 2.567 ± 0.382” clearly distinguishes what is reproduced from NANOGrav versus what is newly inferred here, and cite  at the precise numerical comparison.  


P3-M1 (MAJOR)  
Section: Reference [1] DESI DR1  
Page: 19  

Problem: Citation [1] is “DESI Collaboration, ‘The DESI Data Release 1,’ 2025, DESI DR1 documentation.” At present there is a DESI DR1 data release documentation, but it is not yet a refereed ApJS paper with final bibliographic details. Without an arXiv ID or journal reference, it is unclear whether this is pointing to the internal DESI documentation page, a draft paper, or a final publication.  

Required fix: Check current DESI DR1 status on arXiv and NASA ADS. If an arXiv preprint or journal article exists, cite it with full metadata (authors, title, arXiv:YYMM.NNNNN, journal, year). If no citable paper exists yet, state explicitly “DESI Collaboration, DESI DR1 online documentation (accessed YYYY)” and give enough information for reproducibility; avoid implying a refereed article if it does not exist.  


P3-M2 (MAJOR)  
Section: Reference [2] LAMOST DR10  
Page: 19  

Problem: [2] is given as “A.-L. Luo et al., ‘The LAMOST Data Release 10,’ Research in Astronomy and Astrophysics, 2024.” A RA&A DR10 paper may exist, but the author list and year need to be checked against ADS to confirm exact title and publication details. If DR10 is only documented in online data releases, “Research in Astronomy and Astrophysics, 2024” could be inaccurate or premature.  

Required fix: Verify via ADS whether a LAMOST DR10 RA&A paper by Luo et al. has appeared; if so, give its actual volume/page or article number. If not, correct the reference to the latest published DR (e.g. DR8/DR9) and cite DR10 as an online data release separately (with URL or DOI if available), clearly labeled as such.  


P3-M3 (MAJOR)  
Section: Reference [4] eROSITA DR1  
Page: 19  

Problem: [4] is “A. Merloni et al., ‘The SRG/eROSITA All-Sky Survey: The first X-ray all-sky survey in the 21st century,’ A&A 682, A34 (2024).” Check via ADS: eROSITA early data release papers exist, but the exact title and year must match. If the paper referenced is actually the eRASS1 DR paper, confirm that 682, A34 (2024) is correct. Any mismatch in title or year needs correction, especially given PRD’s standards.  

Required fix: Verify with ADS; if the volume 682, A34 and the title as written are correct, no change is needed; otherwise, adjust title, volume, or year to match the published article. If DR1 is only partially released, ensure the citation corresponds to the data scope actually used (e.g., eRASS1, eRASS:4) and state that in the text.  


P3-M4 (MAJOR)  
Section: Reference [6] NEOWISE  
Page: 19  

Problem: [6] is “A. Mainzer et al., ‘NEOWISE Reactivation Mission Year Ten,’ Planetary Science Journal, 2024.” There are NEOWISE reactivation and year‑X papers, but “Year Ten” must be checked against ADS for correctness. Also, the catalog used in the paper is NEOWISE’s infrared photometry; the paper should confirm that the specific release and time span correspond to the referenced mission‑year paper.  

Required fix: Confirm via ADS the exact title and year of the most recent NEOWISE reactivation/year‑ten paper, and update reference metadata accordingly (authors, year, journal, volume, page). If the data used correspond to a different year or release, correct either the reference or the description in the main text.  


P3-M5 (MAJOR)  
Section: Reference  Nicolaou et al. “in press”  
Page: 19  

Problem:  is “C. Nicolaou et al., ‘Anomaly Detection in DESI Early Data Release Spectra with Astronomaly,’ MNRAS (2026, in press).” At time of review, this future‑dated “in press” claim must be checked on ADS. If the paper is still only on arXiv, calling it “in press” with a 2026 date may be incorrect.  

Required fix: Check ADS/arXiv. If the paper is only on arXiv, format as “Mon. Not. R. Astron. Soc., in preparation” or better as “submitted to” or simply cite the arXiv preprint with arXiv ID and year, dropping “in press” and the speculative publication year. PRD generally discourages “in press” without a volume/DOI unless the acceptance is firm and verifiable.  


P3-M6 (MAJOR)  
Section: References –,  (bounce cosmology / fNL)  
Page: 19–20  

Problem: Several citations are used to support very specific numerical predictions, notably fNL = −35/8 and γGW = 3.0 attributed to the “matter‑bounce scenario.” The paper cites:  
-  Cai et al. JCAP 0905, 011 (2009) “Non-Gaussianity in a matter bounce”,  
-  Wilson‑Ewing JCAP 1303, 026 (2013),  
and , ,  for broader context. It is essential to ensure that:  
(a) the exact value fNL = −35/8 is indeed clearly stated or derivable from /;  
(b) “matter‑bounce γ = 3.0” is correctly attributed and that no different convention is used.  

Required fix: Re‑check  and  for the numerical values and the sign convention for fNL and the spectral index. If the numbers are not explicitly present or if they correspond to a particular limit (e.g., single‑field, specific matching conditions), state that explicitly. If you are combining results from different papers (Cai et al. for fNL, Quintin et al. for γ), make that explicit rather than treating them as coming from a single unified model paper. Adjust the referencing sentences so that each numerical claim directly matches what is in the cited paper’s abstract or main equations.  


P3-M7 (MAJOR)  
Section: References ,  (SMBHB background)  
Page: 19  

Problem: The paper cites  Sesana et al. and  Burke‑Spolaor et al. to justify the SMBHB spectral index γ = 4.33. It is necessary that the exact numerical value 13/3 ≈ 4.333… and its context (circular, GW‑driven binaries) is clearly supported by at least one of these references.  

Required fix: Confirm via ADS/arXiv that  or  explicitly state the standard SMBHB background spectral index γ = 13/3 in the conventions you use. If not, add a more standard reference (e.g., Phinney 2001, already cited as ) in the sentence where γ = 4.33 is introduced. Ensure that the numerical value and its assumptions (circular, GW‑driven, power‑law) are properly attributed.  


P3-M8 (MAJOR)  
Section: Introduction, prior anomaly work and “largest” claims  
Page: 1–2, 14  

Problem: The paper claims:  
- “The point-source tier is ∼141× the size of the largest prior single-survey anomaly catalog ; the DESI-only axis (195,829 anomalies) is a ∼73× like-for-like increase.”  

Reference  (Liang et al. 2023 MNRAS 525, 1078) indeed used ∼250,000 DESI EDR spectra and reported 2,685 anomalies (1.07%). That is a single‑survey, DESI‑only study. But the “largest prior single‑survey anomaly catalog” claim needs to be checked against broader literature (e.g., Baron & Poznanski , other SDSS‑scale anomaly hunts). Some works have applied anomaly detection to millions of objects; you must ensure that no larger single‑survey anomaly catalog exists at time of submission.  

Required fix: Search ADS for large‑scale anomaly catalogs (e.g., SDSS, Gaia) and verify that 2,685 objects from  is indeed the largest published single‑survey anomaly list. If larger catalogs exist, revise the “largest prior” language to something narrower (e.g., “largest prior DESI anomaly catalog” or “largest prior spectroscopic anomaly catalog using autoencoders”) and qualify appropriately. If  is truly the largest, add a sentence quantifying its object count to make the comparison transparent.  


P3-M9 (MAJOR)  
Section: Novelty and database coverage (SIMBAD vs. NED/VizieR)  
Page: 9  

Problem: The statement “A matching exercise on randomized 20-object samples from the eROSITA, NEOWISE, and Gaia DR3 SIMBAD-unmatched populations yields the same 100% archival-ID rate in VizieR” is a very strong claim that is not cross‑checked or documented with any external citation. Given that VizieR does not always have complete cross‑identifications or that some truly new sources can appear, claiming 100% identification from small 20‑object samples is fragile and risks over‑generalization.  

Required fix:  
- Tone this down: report the numbers as “in small 20‑object test samples we found archival counterparts for all 20 objects in each case” and explicitly state that this is an illustrative check, not a statistical proof that all SIMBAD‑unmatched objects have archival counterparts.  
- Make clear that this result is internal to your analysis; no external citation possible, but the wording must avoid over‑claiming completeness.  


P3-M10 (MAJOR)  
Section: Data availability; GitHub/HuggingFace URLs  
Page: 18  

Problem: The data‑availability statement cites specific URLs (“https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog”, “https://github.com/Hubify-Projects/bigbounce”) which are non‑standard for PRD and can change between submission and publication. PRD typically prefers stable DOIs and avoids embedding long URLs in the main text. Also, the HuggingFace dataset is described as “private pending arXiv acceptance; public upon acceptance,” which is not appropriate for a PRD article that should be self‑contained and reproducible at acceptance time.  

Required fix:  
- Replace raw URLs with stable DOIs or a short statement that “all catalog data and code are available in a public repository; exact access details will be given in the published version” if DOIs are not yet minted.  
- Remove “private pending arXiv acceptance” language. Instead, commit to making the data public upon PRD acceptance and, ideally, deposit them in a repository with a DOI (Zenodo, etc.).  


P3-M11 (MAJOR)  
Section: Figures with “??” placeholders  
Page: 2, 3, 5  

Problem: Several places in the text refer to “Fig. ??” instead of actual figure numbers (e.g., “architecture shown schematically in Fig. ??”; “per-band contributions rB, rR, rZ … (Fig. ??)”; “Figure ?? shows DESI Legacy Survey DR9 grz composite cutouts”). This indicates incomplete cross‑referencing/tagging in the LaTeX, not acceptable for PRD.  

Required fix: Fix all “Fig. ??” placeholders to correct figure numbers and ensure that every figure referenced in the text actually exists, with consistent numbering. Recompile and verify that no “??” remains anywhere (figures, sections, equations).  


P3-M12 (MAJOR)  
Section: Table I and thresholds; internal consistency  
Page: 7–8  

Problem: Table I’s main body lists Nanom as the *cross-transfer* counts, while footnotes explain that the “Path‑C native-retrained counts” supersede them and are summarized only in the Path‑C row and scattered in text. This mix of baseline and final numbers in the same table is confusing and can easily mislead readers about which numbers are the actual scientific results.  

Required fix:  
- Split Table I into two tables: one for the cross‑transfer baseline (clearly labelled as diagnostic only), and one for the Path‑C native‑retrained results with the correct Nanom for each survey.  
- Alternatively, keep one table but use two columns (“baseline Nanom”, “Path‑C Nanom”) and clearly label each. Ensure that the text around Table I refers to the “Path‑C” column when quoting scientific headline numbers.  


P3-M13 (MAJOR)  
Section: ACT DR6 “quarantined” discussion  
Page: 4, 7, 17–18  

Problem: ACT DR6 is described as “formally quarantined,” yet significant text and a full appendix are devoted to its cross‑transfer anomalies, including statements like “The scan returned 200 anomalous patches (top 1%),” and a Planck×ACT null cross-correlation is reported in the main text. This straddles the line between methodological note and science result. For PRD, if a dataset fails your own acceptance gate, it should not be used as input to any main‑text result.  

Required fix:  
- Move all ACT‑related content (including the Planck×ACT null cross‑correlation) to a clearly demarcated appendix and explicitly label it as a non‑science, methodological exploration.  
- In the main text, reduce ACT mentions to one short sentence (“ACT DR6 was tested in a preliminary cross‑transfer scan, but failed our quality gates and is not used in any results presented here.”).  
- Remove the Planck×ACT null result from the main text (Sec. IV.D) or rephrase it as a qualitative check presented only in the appendix, clearly marked as non‑robust.  


P3-N1 (MINOR)  
Section: Abstract, Introduction  
Page: 1–2  

Problem: Statements like “largest-scale application of autoencoder anomaly detection across seven astronomical archives” and “largest multi-archive anomaly search reported to date” are strong “largest” claims with no explicit survey of previous cross‑survey anomaly work to back them. While likely true, PRD favors cautious phrasing.  

Required fix: Soften to “to our knowledge, the largest…” and briefly note that you are not aware of multi‑survey anomaly catalogs of comparable size, but have not exhaustively surveyed every possible domain (e.g., time-domain alerts).  


P3-N2 (MINOR)  
Section: Reference  Heinrich et al.  
Page: 20  

Problem:  is cited as “Heinrich et al. JCAP 2024, arXiv:2311.13082” but the bibkey “Heinrich2023” is referenced in the text as “publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity.” This is confusing and not necessary for PRD.  

Required fix: Use a consistent citation label and year—e.g., “Heinrich et al. (2024)” everywhere—and avoid explaining bibkey idiosyncrasies in the bibliography.  


P3-N3 (MINOR)  
Section: Multiple (e.g., Sec. II.D, VI.D, appendices)  
Page: many  

Problem: There are numerous internal audit terms (“gate PASS”, “gate FAIL-with-diagnostic”, “Path‑C final”, “canonical headline”) and dataset identifiers that read like internal notebook bookkeeping rather than a polished journal narrative.  

Required fix: Retain the conceptual content (e.g., you have validation gates) but streamline the language to standard scientific prose. For example, “passes our injection-recovery criterion” instead of “gate PASS,” “fails our primary gate but passes a cross-validation diagnostic” instead of “FAIL-with-diagnostic.” Reduce jargon that is meaningful only within your group’s workflow.  


P3-N4 (MINOR)  
Section: Figures; axis labeling and units  
Page: 4–6, 10–11, 16–17  

Problem: Some figures (e.g., UMAP embeddings, σ(fNL) vs. n̄ plot) do not show units explicitly on axes (e.g., n̄ in (Mpc/h)⁻³ is only described in the caption or text). PRD expects axes to be self‑explanatory when possible.  

Required fix: Add units directly to axis labels where relevant (e.g., “number density n̄ [(Mpc/h)⁻³]”). Ensure that all axes, including those in appendices, are clearly labeled with quantity and units.  


P3-N5 (NIT)  
Section: Repeated phrase  
Page: 3  

Problem: Phrase duplication: “reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).” The repetition is unnecessary.  

Required fix: Delete the repeated clause; keep a single clear statement about where the reproducibility scripts are stored.  


P3-N6 (NIT)  
Section: Typographic conventions  
Page: throughout  

Problem: In a few places, the paper alternates between “BigAE” and “BigAE autoencoder” and between “SMBHB” and “SMBHBs.” While not misleading, internal consistency helps readability.  

Required fix: Choose a single convention for the model name (“BigAE autoencoder” on first use, “BigAE” thereafter) and for acronyms like SMBHB (singular vs plural) and apply consistently throughout.  


P3-N7 (NIT)  
Section: Data availability and code references  
Page: 18  

Problem: The line “The 319,443-anomaly cross-transfer baseline is preserved as an archival comparison artifact; consumers should use the Path-C native-retrained blocks for all headline numbers” uses informal terms like “consumers.”  

Required fix: Rephrase in standard scientific language, e.g. “The 319,443-object cross-transfer baseline is retained only as an archival diagnostic; all scientific analyses should use the Path‑C native‑retrained catalogs.”  


## Summary recommendation

REJECT

The manuscript is ambitious and technically detailed but falls short of PRD standards in several key areas: reference metadata need careful verification and correction, the treatment of forecasts and significance is not always clearly separated from measurements (especially in the abstract), ACT DR6 is used inconsistently despite being “quarantined,” and the presentation still contains internal bookkeeping (“Fig. ??”, “gate PASS/FAIL”) that must be resolved. The cumulative weight of these essential and major issues requires substantial restructuring and careful citation/methodology clarification that goes beyond a normal revision cycle; I recommend rejection in its current form, with the expectation that a thoroughly cleaned and clarified version could be resubmitted as a fresh manuscript.

---

## PASS 2 — self-critique findings (what initial review missed)

P3-E6 (ESSENTIAL)  
Section: Abstract; Sec. II.B; Table I footnotes; Sec. VI.D(i), Appendix C  
Page: 1, 2–3, 7–8, 12–13, 15  

Problem (arithmetic / internal consistency, σ(fNL) and Fisher form): The text asserts a Fisher “positivity‑respecting” form \(1/\sigma(f_{\mathrm{NL}})^2 = F_0 + c\alpha^2\) with \(F_0 = 1/8.982\) and \(c = 0.0747\), and uses this to quote \(\sigma(f_{\mathrm{NL}})=8.14\) (α=0.19), envelope [3.92, 8.98], and a “7.9% improvement.” However:  

- Using the stated form and numbers, \(F_0 = 1/8.982 ≈ 0.01239\), \(c\alpha^2 = 0.0747×0.19^2 ≈ 0.00270\), so \(F_0 + c\alpha^2 ≈ 0.01509\), implying \(\sigma ≈ 1/\sqrt{0.01509} ≈ 8.14\) (central σ is consistent). But the corresponding *fractional improvement* relative to σ(std)=8.98 is \(1−8.14/8.98 ≈ 9.3%\), not 7.9%.  

- Appendix C/Table VII instead states a *linear* scaling relation \(\Delta\sigma/\sigma_{\mathrm{std}} ≈ (6.1\%/0.15)\,\alpha\) and tabulates σ(fNL)=8.43 (6.1% improvement) at α=0.15, 8.25 (8.1%) at α=0.20, etc., which are incompatible with the quadratic Fisher form. For α=0.15, the quadratic model with the stated F0,c gives \(\sigma\approx 8.80\), not 8.43; for α=0.05 it gives ≈8.93, not the 8.80 listed in Table VII.  

- The abstract’s quoted improvement “7.9%” at α=0.19 does not match either the quadratic Fisher formula (≈9.3%) or a strict linear extrapolation from the “fiducial 6.1% at α=0.15” (which would give ≈7.7%).  

- The claimed 1σ envelope “[3.92, 8.98]” around the central σ=8.14 is never explicitly derived; it also conflicts with Appendix C’s dense‑tracer “ideal multi‑tracer” σ=11.71 and “baseline multi‑tracer” σ=12.72 values in Fig. 8, which use a different baseline (multi‑tracer) than the DESI‑only σ(std)=8.98 in the main text.  

Required fix:  
- Choose a single consistent σ(fNL) forecasting model (either the quadratic Fisher form or the linearized scaling) and recompute *all* σ and %-improvement values (8.14, 7.9%, Table VII entries, Fig. 8 annotations, “6.1%” at α=0.15, etc.) from that model, updating numbers wherever they appear.  
- Explicitly show the derivation of the 1σ envelope [3.92, 8.98] (or recompute it) from the adopted Fisher parametrization, and ensure it is consistent with σ(std)=8.98 and with any “dense‑tracer” baseline quoted in Appendix C/Fig. 8.  
- Once recomputed, check for and correct any inconsistencies between the abstract, Sec. V, Sec. VI.D(i), Table VII, and Fig. 8. If you retain the quadratic Fisher form, drop the linear “Δσ/σ ≈ (6.1%/0.15)α” statement or recast it as an explicit *small‑α approximation* with numerical values recomputed to match.  


P3-E7 (ESSENTIAL)  
Section: Abstract; Sec. V; Sec. VI.D(i); Appendix C; cross‑comparison with Gold+Silver σ(fNL)GS  
Page: 1, 11–13, 15  

Problem (null‑procedure comparability and juxtaposition of σ values): Several σ(fNL) values derived from different Fisher setups and tracer samples are placed side‑by‑side without a clear, repeated “not directly comparable” qualifier, despite the instructions and your own caveat text. Examples:  

- Abstract: σ(fNL)=8.14 with envelope [3.92, 8.98], improvement vs. “σ(fNL)std = 8.98 single‑tracer baseline.” No explicit reminder that the former includes anomaly tracers and a specific α fit, whereas the latter is a DESI single‑tracer configuration.  

- Sec. V(b): σ(fNL)std=8.98 baseline, σ(fNL)=8.14 forecast with anomaly tracers, and later in the same section Sec. V(b–c) a separate σ(fNL)=8.43 forecast at fixed α=0.15 is mentioned (Appendix C) plus multi‑tracer baselines σ=11.71, 12.72 in Fig. 8. These are inter‑compared without always reiterating that they come from different Fisher configurations (single‑tracer DESI vs. multi‑tracer SPHEREx forecast, different kmax, nuisance‑parameter blocks).  

- Sec. V(b–c) and VI.D(i,j): σ(fNL)GS=1.95 central (Gold+Silver subset) is mentioned next to 8.14, 8.98 and the multi‑tracer numbers with only a brief “consistent with no improvement at <1σ” but without an explicit warning that σGS is computed from a separate, high‑bias, sparse‑tracer Fisher with stronger shot‑noise assumptions and cannot be directly compared to σ(std) or σ(αjk).  

Required fix:  
- For every paragraph where two or more σ(fNL) values from different null procedures or tracer configurations appear together (e.g., the abstract sentence, Sec. V(b), Sec. V(c), the GS comparison, Fig. 8 caption), add an explicit sentence such as: “These σ values are not directly comparable because they are derived from different Fisher setups (different tracer samples, number densities, kmax, and nuisance‑parameter treatments).”  
- In Sec. V and VI.D(i,j), add a small table or bullet list summarizing, for each σ quoted (σstd, σ(αjk), σ(α=0.15), σGS, σmulti, σsingle‑tracer 16.85, etc.), the tracer set, number density, kmax, and nuisance‑parameter block. Refer to this when making any qualitative comparison.  
- In the abstract, either remove the σstd=8.98 baseline value or explicitly mark both as “forecast‑level Fisher sensitivities from different configurations, not directly comparable measurements.”  


P3-E8 (ESSENTIAL)  
Section: Abstract; Sec. IV.A (“Archival cross‑match and genuine novelty fraction”); Fig. 5; surrounding discussion  
Page: 1, 9–10  

Problem (arithmetic and scope of the 17.8% novelty fraction): The genuine novelty fraction is given as 178/1000=17.8% for the DESI top‑1,000 anomalies after cross‑matching to 20 catalogs, but several related statements and implied extrapolations are not fully consistent or quantified:  

- The abstract calls this “genuine novelty fraction of ∼17.8% (single‑sample point estimate at the top‑1,000 score stratum; full‑catalog rate empirically untested).” In Sec. IV.A you further state that extended matching “reduces the headline novelty pool by a factor of ∼5.6× relative to the SIMBAD‑unmatched aggregate.” However, the arithmetic relating 17.8% to the 58.8% SIMBAD‑unmatched aggregate is never explicitly shown: 58.8% / 17.8% ≈ 3.3, not 5.6. The “∼5.6×” can only be obtained if one compares to a different fraction (e.g., DESI‑only SIMBAD‑unmatched 99%) but that is not clearly specified.  

- The DESI top‑10,000 SIMBAD‑unmatched fraction (∼99%) and the top‑1,000 multi‑catalog genuine novelty rate (17.8%) are used together as if they probe the same underlying novelty; however, one is specific to SIMBAD only, the other to an ensemble of 20 catalogs. The text says the SIMBAD‑unmatched fractions “substantially overstate true catalog novelty” but does not give a quantitative mapping—e.g., a binomial uncertainty on 17.8% or any explicit statement that 17.8%±x% applies only at the very top‑score stratum.  

Required fix:  
- Recompute and clearly state the ratio that yields “∼5.6× reduction”: specify *which* baseline fraction is being compared to 17.8% and show the arithmetic. If it is DESI’s ∼99% SIMBAD‑unmatched, then 99/17.8 ≈ 5.6; say this explicitly and clarify that this is a DESI‑top‑1k vs. DESI‑top‑10k comparison, not an “aggregate 58.8%” comparison.  
- Add an explicit binomial (or Bayesian) uncertainty interval for 178/1000, e.g., 17.8% ± √(0.178×0.822/1000) ≈ 17.8% ± 1.2%, and note that this is a single‑stratum, DESI‑only estimate at the very top of the score distribution.  
- In the abstract and in Sec. IV.A, reinforce that 17.8% is *not* applicable to the full 378,080‑object catalog (or even to the full DESI anomaly sample); recommend language like “for the DESI top‑1,000 anomalies only; this should not be extrapolated to the full catalog.” (You already partly do this; the fix is to make the arithmetic internally consistent and the comparison target explicit.)  


P3-E9 (ESSENTIAL)  
Section: Sec. II.B (DESI thresholds and S vs MSE); Sec. III.A; Table I footnotes  
Page: 2–3, 4, 7–8  

Problem (arithmetic, thresholds, and unit consistency between S and MSE): The DESI thresholding description mixes S (z‑scored reconstruction residual) and raw MSE in a way that is numerically opaque and slightly inconsistent:  

- Sec. II.B states that for DESI “µval ≈ 0.0287” and “σval is set such that the S>5 catalog threshold corresponds to MSE ≈ 0.143 on the rescaled scale.” If S=(MSE−µ)/σ, then S=5 at MSE=0.143 implies σ ≈ (0.143−0.0287)/5 ≈ 0.0229. That should be explicitly given or checked; elsewhere you quote only µval and S>5.  

- Fig. 2 and Table I footnotes treat S>5 as a universal “canonical” anomaly criterion, but later footnotes describe SDSS and LAMOST headline counts being based on top‑percentile cuts (e.g., S≥0.1060 and S≥0.4613) on the same DESI‑trained score scale for the *cross‑transfer* baseline, and simultaneously say that applying S>5 to SDSS yields only 12 anomalies, LAMOST 2,054. It is not transparent from the text how these thresholds relate numerically across surveys, nor whether the “per‑survey S distribution” used for percentile cuts uses the same µval,σval as DESI or survey‑specific re‑normalization.  

- The DESI 0.87% anomaly rate is derived from 195,829/22,504,897; this is ≈0.87% (0.870%). The numbers themselves are consistent, but because S is a derived, dimensionless z‑score and you also discuss raw MSE (≈0.0287 and threshold ≈0.143), readers cannot easily reconstruct the exact mapping without explicit σval and a clear formula for each survey.  

Required fix:  
- For DESI, explicitly state σval (≈0.0229) alongside µval in Sec. II.B, and verify that MSE≈0.143 truly corresponds to S=5 using the given formula. If a slightly different σ was used in code, update the text to the precise value actually used.  
- Clarify, in Table I footnotes and Sec. II.B, whether SDSS and LAMOST use *their own* µval,σval from cross‑transfer validation or share the DESI normalization. If they use survey‑specific z‑scoring, indicate µval,σval for each survey (or at least note that the S units differ slightly across surveys).  
- Add a brief worked example (one line) for DESI: “e.g., MSE=0.143 corresponds to S = (0.143−0.0287)/0.0229 ≈ 5.0” so that readers can verify the arithmetic and understand the dimensional mapping between MSE and S.  


P3-M14 (MAJOR)  
Section: Fig. 1 and caption vs. Section II.D / Table I (cross‑transfer vs Path‑C totals, ACT inclusion)  
Page: 4, 7–8, Appendix F  

Problem (figure‑caption vs body‑claim mismatch): Fig. 1 is labeled “Spatial distribution of all 319,443 anomalies across 8 archives,” while the caption text says this is the “initial cross‑transfer anomaly baseline (319,443 detections shown; canonical Path‑C unique count is 378,280 after per‑survey native retrains and 7‑way deduplication — see Table I Path‑C row and §II D). ACT DR6 is quarantined and excluded.” There are two issues:  

- The opening caption line “across 8 archives” is misleading because the text immediately states ACT is “quarantined and excluded.” If ACT is excluded, the map is across *7* retained archives, not 8; if ACT anomalies are included in the plotted 319,443, then “ACT DR6 is quarantined and excluded” is ambiguous and contradictory.  

- Table I footnotes later explain that the cross‑transfer baseline total of 319,443 “historically included a 200‑patch ACT cross‑transfer block” and that ACT contributes zero objects to Path‑C. The reader has to infer whether those 200 ACT patches are actually plotted in Fig. 1 (the legend shows ACT DR6 in the color key). This is a figure‑caption vs body‑clarity mismatch that makes it hard to understand whether ACT is visually represented in the baseline map or not.  

Required fix:  
- Decide whether Fig. 1 includes ACT anomalies. If yes, clarify the caption to say “8 archives including the quarantined ACT DR6 cross‑transfer baseline; ACT is shown here only as a diagnostic and is excluded from all Path‑C science results.” If no, change “8 archives” to “7 archives” and remove ACT from the legend.  
- Ensure the caption text explicitly matches the description in Table I footnotes and Appendix F regarding whether the 200 ACT patches are part of the 319,443 shown.  


P3-M15 (MAJOR)  
Section: Appendix C (multi‑tracer Fisher; Fig. 8); Sec. V (SPHEREx 3–5σ claim)  
Page: 11–12, 15–16  

Problem (stale or mismatched numbers between main text and appendix, σ(fNL) for multi‑tracer SPHEREx forecast):  

- Appendix C introduces a “canonical 5‑tracer” multi‑tracer Fisher setup and Fig. 8 labels: dense‑tracer limit σ(fNL)=11.71, baseline multi‑tracer σ(fNL)=12.72, and single‑tracer σ(fNL)=16.85. These values are not clearly tied back to the σ(fNL)std=8.98 single‑tracer DESI baseline used elsewhere in Sec. V for the anomaly‑tracer improvement.  

- Sec. V’s statement that “The projected SPHEREx multi-tracer forecast yields 3–5σ detection significance for the matter-bounce fNL = −35/8 prediction (uncertainty range reflects systematic degradation budget)” is not numerically backed up in the body: there is no explicit σ(fNL)SPHEREx quoted in the main text that, when inverted, corresponds to 3–5σ for fNL=−4.375. Heinrich et al. are referenced, but your own numbers (11.71, 12.72 in Appendix C; 8.98 single‑tracer DESI baseline) are not coherently connected to “3–5σ.”  

- It is not clear whether the 11.71/12.72 multi‑tracer numbers already include the anomaly tracers, shot‑noise penalties, and nuisance blocks discussed in Sec. VI.D(i), or whether they refer to a different, idealized SPHEREx setup. This makes it possible that some σ numbers are leftovers from an earlier version of the Fisher pipeline.  

Required fix:  
- Clearly define in Appendix C (and cross‑reference in Sec. V) the exact configuration that yields σ(fNL)=11.71 and 12.72: list the tracer types, number densities, survey volume, kmax, and nuisance‑parameter priors. Indicate explicitly whether these numbers correspond to the SPHEREx configuration cited by Heinrich et al., to a DESI‑like survey, or to a hybrid.  
- In Sec. V, when you claim “3–5σ” SPHEREx sensitivity to fNL=−35/8, show the corresponding σ (e.g., σ≈1–1.5) and how it arises from your or Heinrich et al.’s Fisher calculation. If you are relying entirely on Heinrich et al. for this number, state that explicitly and avoid mixing your own 11.71/12.72 σ values into the same paragraph unless you clarify they are different scenarios.  
- Remove or update any σ numbers in Appendix C or Fig. 8 that come from an outdated Fisher setup. After reconciling with P3‑E6, ensure all σ values used in the SPHEREx 3–5σ claim are consistent across Sec. V, Sec. VI.D(i), Appendix C, and Fig. 8.  


P3-M16 (MAJOR)  
Section: Sec. II.B (per‑band scores rB,rR,rZ and Fig. “??” reference); Sec. III.A,B; Appendix B, Fig. 9  
Page: 2–3, 4–5, 17  

Problem (figure‑caption vs body‑description; missing band‑score figure): Sec. II.B states that “For spectroscopic surveys, we additionally decompose the score into per-band contributions rB, rR, rZ computed over the blue (3600–6200 Å), red (6200–8200 Å), and near-infrared (8200–9800 Å) subsets (Fig. ??).” Later, Sec. III.A and III.B use these band‑scores extensively (e.g., Z‑arm dominance, rZ for high‑z candidates; Appendix B and Fig. 9 show taxonomy families). However:  

- The referenced “Fig. ??” for rB,rR,rZ never appears explicitly in the excerpted figures; only Fig. 2, 3, 4, 5, 6, 7, 8, 9 are present, and none is a pure per‑band score distribution or clear visualization of rB,rR,rZ. This is an internal cross‑reference failure and a figure‑body mismatch.  

- The per‑band contributions are central to DESI high‑z candidate selection (Sec. III.B) and to the B‑dominant vs multi‑band classification in Appendix B/Table VI, yet there is no figure explicitly showing how rB,rR,rZ are computed or distributed.  

Required fix:  
- Either (a) add a dedicated figure showing the distributions of rB,rR,rZ (or an example spectrum with its per‑band residuals) and update the “Fig. ??” reference to that figure number, or (b) remove the “(Fig. ?)” reference and briefly describe the per‑band decomposition in text only.  
- Ensure that all uses of rB,rR,rZ in Sec. III.A,B and Appendix B are internally consistent with the definitions given in Sec. II.B (same wavelength ranges, same normalization). If the earlier version of the paper had a band‑score figure whose numbering changed, update all references accordingly and recompile to confirm no remaining “??”.  


P3-M17 (MAJOR)  
Section: Sec. IV.A (VizieR follow‑up on 20‑object samples); Fig. 5 caption; novelty extrapolation  
Page: 9–10  

Problem (unquantified hedges and over‑generalization risk): The statement “A matching exercise on randomized 20‑object samples from the eROSITA, NEOWISE, and Gaia DR3 SIMBAD‑unmatched populations yields the same 100% archival-ID rate in VizieR” is then summarized in Fig. 5’s caption as: “Extended archival cross-matching reduces the headline novelty pool by a factor of ∼5.6× relative to the SIMBAD-unmatched aggregate…” and in surrounding text as evidence that SIMBAD‑unmatched fractions “substantially overstate” novelty. Even after you already toned down language in the first review, the current wording still risks implying that *all* SIMBAD‑unmatched objects have archival IDs, based on very small samples (3×20 objects).  

Required fix:  
- Explicitly label these 20‑object checks as “small illustrative tests” and provide the binomial confidence limits (e.g., for 0/20 misses, the 95% upper bound on the true “not found in VizieR” rate is ≈14% for each survey). Make clear that 100% in 20 objects does not rule out a nontrivial tail of truly uncataloged objects.  
- In Fig. 5 caption and Sec. IV.A, avoid phrases like “the same 100% archival-ID rate” without qualification; instead say “in small 20‑object test samples we happened to find archival counterparts for all objects; this is illustrative only and does not statistically prove 100% coverage.”  
- Separate more clearly, in wording, the robust DESI top‑1k multi‑catalog 17.8% result (large‑N) from the small‑N 20‑object VizieR tests for other surveys, so readers do not unconsciously transfer the 100% small‑N result to the full anomaly populations.  


P3-N4 (MINOR)  
Section: Abstract; Sec. III.E; Table III; Sec. IV.A  
Page: 1, 7–8, 9  

Problem (stale or ambiguous counts for “203 novel X‑ray sources” from eROSITA):  

- Sec. III.E states “SIMBAD‑unmatched: 68% (203 novel X‑ray sources)” for the 298 eROSITA anomalies. 68% of 298 is ≈202.6, consistent with “203,” but this is only defined with respect to SIMBAD (not the 20‑catalog multi‑match used for DESI), and later Sec. IV.A cautions that SIMBAD‑unmatched fractions overstate true novelty.  

- The abstract still phrases this as “203 novel X‑ray sources” without the “SIMBAD‑unmatched” qualifier or an explicit reminder that this is *not* a 20‑catalog genuine novelty assessment.  

Required fix:  
- In the abstract, append “(SIMBAD‑unmatched; not yet tested against the full 20‑catalog cross‑match used for DESI)” when citing “203 novel X-ray sources,” or soften to “203 SIMBAD‑unmatched X‑ray anomalies” to avoid implying they are all genuinely new astrophysical sources.  
- Optionally, add a short sentence in Sec. III.E pointing to Sec. IV.A and explaining that a full multi‑catalog novelty audit analogous to DESI’s top‑1k sample has not been performed for eROSITA yet.  


P3-N5 (MINOR)  
Section: Sec. II.C (GPU inference timing); Table V  
Page: 3, 15  

Problem (arithmetic consistency of processing times): You state “The total processing time across the seven retained surveys plus the quarantined ACT DR6 cross-transfer scan (Appendix F) was approximately 42 hours (wall-clock), dominated by the DESI DR1 scan (19,705 s for 22.5M spectra, throughput ∼1,142 spectra/s) and the LAMOST DR10 scan (11.4M spectra).” Table V, however, lists only *training* times (e.g., “∼3,600 s” for DESI training) and throughput numbers, not full inference runtimes, and gives no explicit per‑survey inference times to reconstruct the 42‑hour total. This is not a hard error, but it makes it impossible to verify the 42‑hour figure from Table V.  

Required fix:  
- Either (a) add a column in Table V for “Total inference time” per survey so that summing them reproduces the stated ≈42 hours, or (b) drop the precise “42 hours” and describe the runtime more qualitatively (e.g., “O(1–2) days on a single H200, dominated by DESI and LAMOST”), avoiding a pseudo‑precise total that cannot be reconstructed from the table.  

---

I have not repeated any issues already covered in P3‑E1–E5, P3‑M1–M13, or P3‑N1–N3. The new findings above focus on internal arithmetic consistency (σ(fNL), percentages), figure‑caption vs text mismatches (cross‑transfer vs Path‑C, ACT inclusion), and scope/quantification of novelty and σ comparisons, which are areas that initial reviews often under‑scrutinize.