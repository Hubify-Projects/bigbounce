# P3 auto-2026-06-08_1354pt — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input format**: TEXT + web search + pass-2 self-critique (20838 chars)
**Wall time**: 124.2s

---

The manuscript’s references are overall plausible and largely consistent with real literature, but there are multiple serious citation‑forensics and internal‑consistency problems. Several key references are mis‑dated or partially mis‑specified; one citation appears to be a genuine fusion of two different papers; and there are quantitative claims and ratios in the abstract and body that are numerically inconsistent or not properly traceable to the cited work. In addition, there are process/archival issues (GitHub/HuggingFace links, “pending arXiv acceptance” language, internal-round labels in figures) that are not acceptable for PRD.

Below I list findings by severity. Page numbers are approximate, based on the ordering of the text you provided.

---

### ESSENTIAL FINDINGS

**P3‑E1 — Abstract, p.1 — “141×” and “73×” improvement factors do not match quoted prior numbers**

- **Offending text (abstract):**  
  “The point-source tier is ∼ 141× the size of the largest prior single-survey anomaly catalog ; the DESI-only axis (195,829 anomalies) is a ∼ 73× like-for-like increase.”

- **Problem:**  
  In the Introduction the paper quotes Liang et al.  as “∼ 250,000 DESI EDR spectra, finding 2,685 anomalies (1.07%).” If 2,685 is the “largest prior single-survey anomaly catalog,” then 378,080/2,685 ≈ 141 is consistent for the total number of anomalies, but 195,829/2,685 ≈ 72.9, not 73 “like‑for‑like” in the same sense (DESI vs DESI). However, the text in several places shifts between “point‑source tier,” “canonical catalog,” “Path‑C per‑survey counts,” and “largest prior single‑survey catalog” without consistently defining what the 141× baseline is (2,685 anomalies vs. survey size). The abstract lumps these ratios together as if they are straightforward, but the internal logic is inconsistent:
  - If the 141× factor uses 378,080 vs. 2,685, that is **not** a single‑survey like‑for‑like comparison; it is multi‑survey vs. single‑survey.
  - If “like‑for‑like” means DESI‑only anomalies vs. Liang’s DESI‑EDR anomalies, 195,829/2,685 ≈ 72.9 ≈ 73 is fine, but then the 141× statement should explicitly say “multi‑survey catalog vs. largest prior single‑survey catalog,” which it does not.
  - Nowhere is the denominator of the 141× clearly stated, and the same reference  is used for both.

- **Required fix:**  
  Explicitly state what the 141× and 73× ratios are relative to:
  - Clarify in the abstract and in §VII that 141× = 378,080 / 2,685 and that this compares the **total multi‑survey anomaly count** to Liang et al.’s single‑survey DESI EDR anomaly count.
  - Clarify that 73× = 195,829 / 2,685 is the DESI‑only like‑for‑like increase.
  - If the authors intend “largest prior single‑survey anomaly *catalog*” to mean a DESI‑specific catalog, say so. Otherwise, remove or re‑phrase the 141× claim to avoid conflating multi‑survey and single‑survey comparisons.
  - Make sure the same denominators are referenced consistently wherever these factors appear.

---

**P3‑E2 — Cosmology references , ,  — Mis‑attribution of matter‑bounce fNL and double‑counting Wands**

- **Offending text (body, multiple places; §I, §V, §V A, Appendix E):**  
  - “...the quasi‑matter bounce model predicts fNL = −35/8 = −4.375 [13, 14, 35]…”  
  - References list:  
    -  D. Wands, “Local non-Gaussianity from inflation,” Class. Quant. Grav. 27, 124002 (2010).  
    -  Y.-F. Cai, W. Xue, R. Brandenberger, and X. Zhang, “Non-Gaussianity in a matter bounce,” J. Cosmol. Astropart. Phys. 0905, 011 (2009).  
    -  E. Wilson-Ewing, “The Matter Bounce Scenario in Loop Quantum Cosmology,” JCAP 1303, 026 (2013).

- **Problem:**  
  - The specific prediction \(f_{\rm NL} = -35/8\) for matter bounce is derived in Cai et al. 2009 (JCAP 0905:011) and related follow‑up work, not in Wands 2010, which is a review of local non‑Gaussianity in *inflationary* models, and not in Wilson‑Ewing 2013, which focuses on loop quantum cosmology and does not, as standardly cited, quote that particular numerical value as a headline prediction.  
  - Using all three references [13,14,35] for the value −35/8 is therefore misleading:  is correct,  is a broad review of local fNL signatures (not bounce‑specific), and  is about LQC matter bounce but does not directly introduce this exact number as a *prediction*. You are effectively triple‑citing a single numerical result.
  - This violates PRD’s standard for precise attribution: when quoting a single quantitative prediction, the reference must clearly be the paper that actually derives or prominently uses that value.

- **Required fix:**  
  - Restrict the attribution of \(f_{\rm NL} = -35/8\) to Cai et al. (2009) and closely related work that genuinely derive this number in the matter‑bounce scenario. For example, use  as the primary citation.  
  - If Wilson‑Ewing 2013 is to be cited, clarify what role it plays (e.g. “implements the matter-bounce scenario in loop quantum cosmology” or “discusses related observables”), and do not bundle it into the same bracket as the numerical fNL value unless you can show that the number is explicitly quoted there.  
  - Remove Wands 2010  from the fNL‑prediction bracket. It is a general review, not a source of the specific -35/8 figure.
  - Check the entire manuscript for similar bundled citations where specific numerical predictions are attributed to multiple papers but really originate in one.

---

**P3‑E3 — Reference  SPHEREx mis‑dated**

- **Offending text (ref. ):**  
  “O. Doré et al. (SPHEREx Collaboration), ‘Cosmology with the SPHEREx All-Sky Spectral Survey,’ arXiv:1412.4872 (2014).”

- **Problem:**  
  The canonical SPHEREx cosmology white paper is arXiv:1412.4872, but it was posted in **December 2014** and is generally cited as “2015, JCAP 04 (2016) 045” or similar, depending on the version. Listing “(2014)” as a publication year is misleading: 2014 is the arXiv posting year, not a journal year, and PRD expects either a journal reference with its year, or an arXiv e‑print with appropriate “(2014), arXiv:1412.4872” wording. But the same paper is now journal‑published, which should be preferred.

- **Required fix:**  
  - Update  to the correct journal citation, with year and volume/page, e.g. “JCAP 04 (2016) 045” with the 2016 publication year, and keep arXiv:1412.4872 as a preprint reference if desired.  
  - Ensure consistency in year conventions across references: if you always use journal years when a journal exists, do so here as well.

---

**P3‑E4 — Reference  “Planck and the local universe” incorrectly titled/attributed**

- **Offending text (ref. ):**  
  “L. Verde, P. Protopapas, and R. Jimenez, ‘Planck and the local universe: Quantifying the tension,’ Phys. Dark Univ. 2, 166 (2013), arXiv:1306.6766.”

- **Problem:**  
  - The standard paper is “Planck and the local Universe: Quantifying the tension,” by Verde, Protopapas, & Jimenez, Phys. Dark Univ. **2 (2013) 166‑175**, arXiv:1306.6766. The current entry shortens the title but still retains its recognizable form; this is acceptable, but the way it’s cited (“Phys. Dark Univ. 2, 166 (2013)”) omits the page range and appears informal compared to the rest of the bibliography.  
  - More importantly: the paper is not obviously used anywhere in the text. If the authors are invoking “tension” in cosmological parameters to contextualize non‑Gaussianity or PTA results, that should be made explicit and the numeric tension level quoted. Otherwise this is an unused, “ornamental” citation.

- **Required fix:**  
  - Either: use this reference in the text, explicitly tying it to an actual numeric statement about Planck vs local H0 or σ8 tensions, with correct values traceable to the paper; or  
  - Remove  if it is not actually needed.  
  - If retained, give a standard full citation with page range.

---

**P3‑E5 — Internal versioning / round tags inside the main text and figure captions**

- **Offending text examples (Appendix C figure caption and context):**  
  - “Multi-tracer Fisher: shot-noise sensitivity for sparse anomaly tracers (fNL) realistic  
    … P3 anomaly\_gold n=8.5e-06  
    P3 anomaly\_silver n=4.5e-05  
    P3 anomaly\_silver…”  
  - Elsewhere: “P2 §IV penalty (15–30%)”, “P3 anomaly\_gold n=…”.

- **Problem:**  
  These “P2” / “P3 anomaly\_gold/anomaly\_silver” labels clearly look like internal project bookkeeping or round labels (“P3” matches the paper tag in the [REVIEWER METADATA]). PRD does not accept internal round codes or private pipeline labels in the published figures unless they are fully defined and meaningful to readers. Here, they are unexplained and look like internal audit tags rather than scientific labels.

- **Required fix:**  
  - Remove all “P2”, “P3 anomaly\_…”, “P3” style pipeline tags from figure labels, axis labels, and captions. Replace them with reader‑understandable, self‑contained labels (e.g., “Gold anomaly subsample,” “Silver anomaly subsample” without “P3”).  
  - Search the entire manuscript (including appendices) for similar internal version markers (e.g., “R7”, “R8”, “round”, “Path‑B”, etc.) and remove or explain them in scientific terms.

---

**P3‑E6 — External links and “pending arXiv acceptance” language in Data availability**

- **Offending text (end of paper, “Data availability”):**  
  - Mentions of “HuggingFace at https://huggingface.co/datasets/bamfai/bigbounce-anomaly-catalog (private pending arXiv acceptance; public upon acceptance)” and “https://github.com/Hubify-Projects/bigbounce.”

- **Problem:**  
  - PRD expects stable, citable data releases, not conditional statements like “private pending arXiv acceptance; public upon acceptance.”  
  - Using GitHub and HuggingFace URLs is acceptable as supplemental material, but they must be stable and not tied to the paper’s acceptance status. In its current wording, this is effectively a promise about future availability that may not be verifiable by readers; it also introduces non‑standard formatting (“https://…”) and a quasi‑marketing tone.  
  - Also, arXiv “acceptance” is not a meaningful status (arXiv is a preprint server, not a journal); this phrasing is confusing.

- **Required fix:**  
  - Remove conditional language (“private pending arXiv acceptance; public upon acceptance”). Commit either to “will be made public upon publication in PRD” or, preferably, ensure the datasets are public at submission and simply state their location.  
  - Format the data‑availability statement in line with PRD norms (no raw URL text in the body; provide repository names and DOIs or persistent identifiers if possible).  
  - Make sure the catalog, scripts, and weights are actually accessible in a stable form at the time of publication.

---

### MAJOR FINDINGS

**P3‑M1 — Reference  Nicolaou et al. mis‑specified as “2026, in press”**

- **Offending text (ref. ):**  
  “C. Nicolaou et al., ‘Anomaly Detection in DESI Early Data Release Spectra with Astronomaly,’ Mon. Not. Roy. Astron. Soc. (2026, in press).”

- **Problem:**  
  - At the time implied by the paper (dated “June 2026”), giving a future‑dated “2026, in press” for an MNRAS article is hazardous unless the paper is genuinely accepted and in press. The citation as written lacks a DOI, volume, and page numbers, and looks like an aspirational or pre‑acceptance reference.  
  - PRD will not accept references to “in preparation” or “in press” work unless the paper is actually accepted; even then, a DOI or accepted‑manuscript arXiv link should be given.

- **Required fix:**  
  - Confirm whether the Nicolaou et al. article is accepted by MNRAS.  
  - If yes, update the citation with the correct year, journal volume, and page/DOI, and remove “in press.”  
  - If not yet accepted, then either:
    - Cite it purely as an arXiv preprint with its arXiv ID and posting year, or  
    - Remove it from the reference list and refer to it in the text as “work in preparation” without assigning it a numbered reference.

---

**P3‑M2 — Reference  Liang et al. year and details must be checked precisely**

- **Offending text (ref. ):**  
  “Y. Liang et al., ‘Outlier detection in the DESI Bright Galaxy Survey,’ Mon. Not. Roy. Astron. Soc. 525, 1078 (2023), arXiv:2307.07664.”

- **Problem:**  
  - The paper’s arXiv:2307.07664 is real and titled “Outlier detection in the DESI Bright Galaxy Survey.” It did appear in MNRAS; however, the journal details given (“525, 1078 (2023)”) need to be exact. MNRAS volumes and pages are easy to mis‑transcribe.  
  - The manuscript uses this paper as the basis for the 2,685 anomalies / 1.07% rate; it is essential that this number is traceable to the actual MNRAS/arXiv tables. The present manuscript does not show a direct citation to a specific table or figure in  where 2,685 comes from. Without checking the original, there is a risk of mis‑quoting.

- **Required fix:**  
  - Confirm via MNRAS or arXiv that the cited volume and page (525, 1078) and year are correct. If not, correct them.  
  - Explicitly indicate in the text where 2,685 and 1.07% come from (e.g., “Liang et al. , Table N, report 2,685 anomalies among 250,000 BGS spectra, a 1.07% fraction”).  
  - If the exact numbers differ (e.g., slightly different sample size), update your quoted numbers and the derived 141× and 73× ratios accordingly.

---

**P3‑M3 — Reference –, ,  cosmology chain must be numerically cross‑checked**

- **Offending text (several sections):**  
  - Use of Heinrich et al.  for σ(fNL) ≈ 0.7;  
  - Use of Hamaus et al. , Seljak , and Heinrich et al.  to motivate the Fisher forecast and the “6.1%” or “7.9%” improvements.

- **Problem:**  
  - The manuscript takes specific sigma forecasts (e.g. σ(fNL)std = 8.98, improvements ∼6–8%) and attributes the methodology to Heinrich et al. , but without a clear mapping from the symbol conventions (bias parameters, shot noise, kmax, etc.) used in Heinrich et al. to those used here.  
  - Claims like “Heinrich et al. §IV report a 15–30% degradation of Fisher information …” must be traceable to specific equations or figures. Without explicit citations, these appear as paraphrased numbers that may or may not match the original paper’s conditions (SPHEREx configuration, redshift binning, kmax etc.).  
  - For PRD, you need to show that your use of those numbers is not just heuristic but consistent with the actual forecasting setup of .

- **Required fix:**  
  - Add explicit cross‑references in §V and Appendix C to the precise equations/figures in Heinrich et al. (and any other forecasting/GR‑correction references ,–) from which your quoted numbers and penalties are taken.  
  - Briefly state which of Heinrich’s forecast configurations you adopt (k‑range, redshift bins, tracer populations) and what approximations you make when transferring those results to your anomaly‑selected tracers.  
  - Without this, the fNL forecasting section is under‑documented and not sufficiently backed by the cited literature.

---

**P3‑M4 — Use of NANOGrav 15 yr  KDE free–spectrum product: need explicit mapping to your likelihood**

- **Offending text (Section V A, Appendix E):**  
  - “Dataset: NANOGrav 15-yr HD-correlated KDE free-spectrum product (30f fs{hd} ceffyl), Zenodo 10.5281/zenodo.8060824 . Model: matter-bounce power-law GWB template … emcee 32 walkers × 10,000…”  
  - Then Bayes factors BMB/free, BSMBHB/free are quoted.

- **Problem:**  
  - Agazie et al. (NANOGrav) provide a KDE‑based free‑spectrum likelihood; using it to derive Bayes factors for a specific model (bounce vs SMBHB) is nontrivial. One must correctly propagate the HD correlation information, the prior volume, and the transformation from the free‑spectrum amplitude parameters to a power‑law amplitude and spectral index.  
  - The manuscript gives a formula for log10 ρi in Appendix E, but it is not obvious that this is exactly the same quantity used in the NANOGrav KDE representation; nor is it obvious that the priors on (γ, log10 A) are consistent with those in . Quoted Bayes factors as large as 7.1×10^3 must be firmly traceable to the NANOGrav methodology to pass PRD scrutiny.

- **Required fix:**  
  - Directly reference the relevant sections/appendices of Agazie et al. (e.g., their Eq./Appendix for the KDE likelihood) and explain in a few sentences how your model maps to their parameter vector.  
  - State explicitly whether you use flat priors in the native KDE parameterization or in (γ, log10 A), and how that compares to the priors used in NANOGrav’s own model comparisons.  
  - If your prior or parameterization is materially different, emphasize that your Bayes factors are *your own* re‑analysis under specific priors, rather than the NANOGrav collaboration’s headline results.  
  - This is necessary to avoid misattributing strong model preferences to NANOGrav when they are in fact from your re‑interpretation.

---

**P3‑M5 — Non‑Gaussianity references , – are present but not tightly linked to explicit quantitative corrections**

- **Offending text:**  
  - Several references on GR corrections and number counts ( Yoo et al.,  Bonvin & Durrer,  Challinor & Lewis,  Di Dio et al.) are cited in the bibliography but not clearly tied to any explicit equation in the main text.

- **Problem:**  
  - The paper claims that GR projection effects induce |Δσ/σ|<0.02% at kmax=0.2 h/Mpc, citing a “plane‑parallel monopole; sub‑% of b.” Without explicit reference to how this was computed (e.g., using CLASSgal  with certain settings), the claim is not auditable.  
  - Given that these references are sophisticated treatments of number‑count observables, you must either show you actually implemented their prescription or clearly state that you are quoting a known result from them.

- **Required fix:**  
  - In §V or Appendix C, add one concise paragraph explaining how GR corrections were computed or bounded: e.g., “We estimated the magnitude of GR light‑cone effects using CLASSgal  for the DESI QSO redshift range with fiducial cosmology; including lensing magnification and Doppler terms yields Δb/b ≤ X%, translating to |Δσ/σ|<0.Y% under our Fisher setup.”  
  - Cite the specific reference(s) used for this computation (e.g., ) right at the relevant sentence.  
  - Otherwise, remove quantitative claims about the size of these corrections.

---

### MINOR FINDINGS

**P3‑N1 — Duplicate phrase in Section II D**

- **Offending text (Section II D):**  
  “...reproducibility scripts shipped with the data release (reproducibility scripts shipped with the companion data repository).”

- **Problem:**  
  Exact duplicate phrase “reproducibility scripts shipped …” within one sentence.

- **Required fix:**  
  Remove the repetition and keep one clear clause.

---

**P3‑N2 — Slightly inconsistent survey naming for Gaia and Planck**

- **Offending text:**  
  - “Gaia DR3” consistently used; ref. [5] is “Gaia Data Release 3, Astron. Astrophys. 674, A1 (2023)” which is fine.  
  - Planck: references  and  are both “Planck 2018 results” but the text sometimes just says “Planck” and sometimes “Planck CMB.”

- **Problem:**  
  Minor terminology inconsistency; not strictly wrong, but can confuse which exact data product (SMICA vs other) is used.

- **Required fix:**  
  When referring to the CMB map used for anomalies, explicitly write “Planck 2018 SMICA CMB map” once in the main text and ensure references , are clearly tied to that product.

---

**P3‑N3 — SIMBAD and NED references**

- **Offending text:**  
  - SIMBAD:  Wenger et al. 2000 A&AS 143, 9 is correct; NED is only described in the acknowledgments.

- **Problem:**  
  The text uses NED extensively (multi‑catalog cross‑match), but references NED only in the acknowledgments instead of a formal reference.

- **Required fix:**  
  Add a short NED bibliographic entry (following their recommended citation) to the reference list, and cite it in the body where NED is used.

---

**P3‑N4 — “Largest multi-archive anomaly search” novelty claim**

- **Offending text (Table I caption, Conclusions):**  
  “The total represents the largest multi-archive anomaly search reported to date.” and “We have presented the largest multi-archive anomaly detection campaign to date…”

- **Problem:**  
  This is plausible but not rigorously substantiated. There are many outlier‑detection and anomaly‑detection works across multiple surveys; it is unlikely any have the same exact combination of surveys and scale, but “largest” is a strong claim. PRD prefers such claims to be either very carefully qualified or avoided unless clearly documented.

- **Required fix:**  
  Rephrase to something like “To our knowledge, this is among the largest multi‑archive anomaly detection campaigns reported to date” or “largest at DESI‑like spectroscopic scale,” or else provide a brief justification (e.g., citing [10–12] as the largest prior works and noting their object counts).

---

### NITS / TYPOGRAPHIC

**P3‑T1 — Minor inconsistencies in hyphenation and capitalization**

- “multi-tracer” vs “multi tracer”; “multi-survey” vs “multi survey” appear slightly inconsistently.
- “quasi-matter bounce” vs “matter-bounce” also vary.

**Required fix:**  
Choose one consistent hyphenation convention and apply across the paper.

---

**P3‑T2 — Unclear symbol and gate labeling in Fig. 7 caption**

- The caption uses “FAIL*” with a footnote style explanation; formatting is somewhat confusing.

**Required fix:**  
Make the gate logic clearer, e.g. separate sentences for PASS surveys and FAIL‑with‑diagnostic surveys, and avoid cryptic in‑figure legend text.

---

## Length and focus of the paper

The paper is long (20 pages + extensive appendices) and mixes three rather separate contributions: (i) large‑scale multi‑survey anomaly catalog construction; (ii) methodological lessons (training bias, Path‑C gates); and (iii) cosmological applications (fNL forecasts and NANOGrav spectral‑index analysis). For PRD, which focuses on fundamental physics and cosmology, the anomaly‑catalog engineering and survey‑specific method details might be more condensed, with emphasis placed on rigor and clarity of the cosmological inference.

A focused PRD paper could reasonably be ~14–16 pages if the catalog‑engineering content were streamlined and the cosmology sections made more tightly connected and better justified with citations.

---

## Summary recommendation

**MAJOR REVISIONS**

The paper is ambitious and uses real, plausibly cited cosmology and survey references, but it does not yet meet PRD standards for citation rigor and internal numerical consistency. The attribution of key cosmological predictions (matter‑bounce fNL, GR corrections, NANOGrav Bayes factors) is not precise enough, some references are mis‑dated or loosely specified, internal process tags appear in the scientific text, and some headline quantitative comparisons (141×, 73×, “largest” claims) are not sufficiently clarified. All essential and major issues above must be addressed before the manuscript can be considered for publication in a high‑precision cosmology journal.

---

## PASS 2 — self-critique findings (what initial review missed)

P3-E7 — Table I arithmetic and consistency errors (rates, totals, and “largest” claim)

- **Offending text (Table I main block and caption; Conclusions §VII):**  
  - DESI DR1 row: “22,504,897 … 195,829 … 0.87%”  
  - SDSS DR18 row: “2,304,830 … 77,905 … 3.38%”  
  - LAMOST DR10 row: “11,418,594 … 44,075 … 0.39%”  
  - Total row: “Total (cross-transfer, ACT-incl.) 37,292,042 … 319,443 … 0.86%”  
  - “This is ∼ 141× the largest prior single-survey catalog …”

- **Problems (A, J, G, F):**  
  1. **Rates in Table I are internally inconsistent with the text and with the described Path‑C numbers.**  
     - DESI: 195,829 / 22,504,897 ≈ 0.870% (0.87% is fine).  
     - SDSS row is explicitly labeled as a cross‑transfer count (“77,905”) in the caption and footnotes, but the body states that the **Path‑C native retrain** has 77,905 anomalies at S ≥ 0.1060 and *only 12* at S > 5.[…] The table mixes these logically distinct counts in one column without labeling which regime each rate refers to (cross‑transfer vs native), while the text later treats 77,905 as the native count. This is not arithmetically wrong but is **internally inconsistent labeling**: the same number is simultaneously described as cross‑transfer and native, and the reported 3.38% rate is with respect to Ntotal, not to the subset actually re‑scored (1.93M).  
     - LAMOST: 44,075 / 11,418,594 ≈ 0.386% (0.39%) is again the *cross‑transfer* rate, but the Path‑C native tier is 113,342 anomalies; the corresponding rate (~1.0%) is nowhere shown.  
     - The caption insists that “Path‑C native‑retrained counts are the canonical results; cross‑transfer counts are preserved as baseline,” yet the numeric column is still the cross‑transfer column. This is a **systematic consistency failure** between caption and numbers, not just narrative wording.

  2. **Total counts and rates are stale relative to Path‑C.**  
     - The “Total (cross‑transfer, ACT‑incl.)” row uses 37,292,042 and 319,443, but the Path‑C per‑survey native counts are 388,493 anomalies and 37,272,042 inputs.[…]  
     - The headline abstract and conclusions use “378,280 unique anomalies” and “37.3 million sources and CMB patches,” while the table’s “Total” row still reflects the pre‑rebuild cross‑transfer baseline and ACT inclusion. The text correctly notes that the total row is a baseline, but the structure strongly invites misreading as the main result. This is a **stale‑number / presentation** issue: the only “Total” visible in the table is the non‑canonical one.  
     - The 0.86% rate in that row is for the old 319,443/37,292,042, yet the canonical Path‑C catalog has 378,280/37,272,042 ≈ 1.01% (given in a footnote), which conflicts with the rate impression a reader would take from the table’s main body.

  3. **“Largest multi‑archive anomaly search” and “141× the largest prior single‑survey catalog” are not simultaneously supported.**  
     - The Liang et al. prior has ~2,685 anomalies in one DESI EDR survey. The claim “largest prior single‑survey anomaly catalog” is plausible relative to DESI‑specific work, but the table also cites Baron & Poznanski’s SDSS anomaly work and does not check whether their multi‑million‑object SDSS campaign has a comparable or larger catalog.  
     - No quantitative comparison is made to earlier multi‑survey or multi‑archive anomaly studies; thus “largest multi‑archive anomaly search reported to date” remains an **unsupported novelty claim** (G).  
     - The same 141× factor is used in the abstract and conclusions without a clearly stated denominator, and the table’s mixture of cross‑transfer and native counts makes it harder to verify this back from the displayed numbers alone (F, G).

- **Required fix:**  
  - Replace the Table I Nanom and Rate columns with **two clearly separated sets of numbers**: cross‑transfer and Path‑C native, or move cross‑transfer to a separate table/appendix. Use the native numbers (e.g., SDSS 77,905 / 1,925,279, LAMOST 113,342 / 11,418,594) wherever “headline” or “canonical” language appears.  
  - Add a “Total (Path‑C native, ACT‑excluded)” row with 37,272,042 and 388,493 plus the correct 1.04% rate, and explicitly separate it from the cross‑transfer total.  
  - In the text and conclusions, explicitly define the denominator for 141× and 73× (Liang’s 2,685 DESI‑EDR anomalies) and restrict “largest prior single‑survey anomaly catalog” to DESI‑based work unless you have checked Baron & Poznanski and other SDSS‑scale searches. If you wish to retain “largest multi‑archive anomaly search,” add a brief quantitative comparison or downgrade to “among the largest.”

---

P3-E8 — Figure 2 caption vs body: inconsistent S‑scale explanation and unit usage

- **Offending text:**  
  - Body (Section II B): “Throughout this paper, ‘S’ refers … to the per‑survey standardized (‘z‑scored’) reconstruction residual … S(x) ≡ (MSE(x) − μval)/σval.”  
  - Figure 2 caption: “The score S is the per-spectrum reconstruction MSE rescaled to validation z‑units: S = (MSE − μval)/σval … cross‑transfer for SDSS, native for DESI/LAMOST.”  
  - Figure 2 right panel axis: “Anomaly score S” with ticks labeled up to “1.9 × 10¹¹”.

- **Problems (A, B, H, E):**  
  1. **Dimensional consistency/equation semantics (C):**  
     - If S is literally a z‑score, it should be of order a few to a few tens in any reasonable distribution. A plotted value of S = 1.9×10¹¹ implies either that S is *not* actually (MSE−μ)/σ for SDSS in that plot, or that μ and σ are being taken from a different population (e.g., DESI training) while the axis is still labeled as if it were a canonical z‑score. That breaks the “one definition for the whole paper” promise.

  2. **Caption vs body mismatch (B, E):**  
     - The caption says “cross‑transfer for SDSS, native for DESI/LAMOST,” but later sections insist that SDSS native retrain is the canonical result (§III C). The figure plots the cross‑transfer SDSS distribution with extreme S values, but the main text elsewhere describes the native SDSS as having S < 14 for the same objects. The figure’s axis and caption therefore describe S as if it were the same canonical quantity, while the body later warns that these S values are cross‑transfer artifacts; this is **not cleanly flagged on the figure**.

  3. **Implicit comparability of different σ procedures (E):**  
     - S for DESI, SDSS cross‑transfer, and LAMOST are constructed from validation sets of different size and provenance (DESI training set vs SDSS data). Yet the figure overlays their S‑distributions and the body loosely compares rates without an explicit statement that these S values arise from **different null procedures** and are not directly comparable across surveys.

- **Required fix:**  
  - For Figure 2 and any figure using cross‑transfer SDSS S values, relabel the plotted score explicitly as “S (cross‑transfer z‑score on DESI‑trained scale)” and state in the caption that these are *not* directly comparable to the native S used elsewhere.  
  - Add a short sentence in §III C making clear that S in Fig. 2 (SDSS) is defined using DESI’s μval, σval (if true), and is a diagnostic only, not the canonical SDSS anomaly score; if μval and σval are SDSS‑specific for that plot, then explain how S can reach 10¹¹ and reconcile this with the definition of a z‑score.  
  - In §II B, clarify that **two different S scales exist in the paper**: canonical per‑survey native S, and a diagnostic cross‑transfer S, and that they should not be mixed in rate comparisons or cross‑survey thresholds.

---

P3-E9 — σ(fNL) forecasting: incorrect baseline mapping and inconsistent envelopes

- **Offending text (Abstract; §V; Appendix C; Table VII; Table IV):**  
  - Abstract: “σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement …; σ(fNL)std = 8.98 single‑tracer baseline).”  
  - §V: “Under the Fisher‑positivity‑respecting asymptotic form 1/σ(fNL)² = F0 + c α² with F0 = 1/8.982 and c = 0.0747, inserting αjk = 0.19 gives a central forecast σ(fNL) = 8.14 with 1σ envelope σ(fNL) ∈ [3.92, 8.98]. The single‑tracer DESI QSO baseline is σ(fNL)std = 8.98.”  
  - Appendix C/Table VII: tabulates σ(fNL) vs α assuming linear scaling from a fiducial “full 7‑bin Fisher result at α = 0.15,” showing σ(fNL)std = 8.98 and σ(fNL)(α=0.15) = 8.43 (6.1% improvement).

- **Problems (A, C, D, E, F, J):**  
  1. **Arithmetic / internal consistency:**  
     - If F0 = 1/8.982 ≈ 0.1113, then in the absence of any α‑dependent c term, σ(fNL) = 8.982, matching the stated single‑tracer baseline. That is consistent.  
     - However, the Appendix C linear scaling table uses a completely different scheme: σ(fNL)(α) is obtained by linearly scaling from σstd = 8.98 with a fixed 6.1% improvement at α = 0.15. That implies a relative change proportional to α, whereas the main text now insists on a quadratic α² dependence via F0 + c α². These two constructions are not mathematically compatible except at α = 0.15, and a “5‑α refit” alone does not reconcile them.  
     - The 1σ envelope [3.92, 8.98] corresponds to applying the extreme ±1σ error on α (0.19 ± 0.65) *directly* through the Fisher mapping; but α enters as α², so α < 0 and α > 0 map to the same α², and α = 0 (null) is a stationary point. The text admits that “the local‑linear propagation σ(fNL) ≈ 8.98 − 3.66α fails inside the 1σ interval,” yet then still quotes [3.92, 8.98] as “1σ envelope.” This is **not a valid 1σ propagation** given the symmetry and non‑linearity of α².

  2. **Equation/units and null‑procedure comparability (C, E):**  
     - The baseline σ(fNL)std = 8.98 is described in different places alternately as: “single‑tracer DESI QSO baseline,” “canonical 5‑tracer” baseline, and as the F0 component of a 7‑bin Fisher. It is not clear which underlying forecast (Heinrich configuration, survey area, kmax, etc.) corresponds to 8.98. The forecast that yields 11.71 and 12.72 in Fig. 8 is not clearly tied to the 8.98 baseline.  
     - Different σ values (11.71, 12.72, 16.85, 8.98, 8.43, 8.14, 1.95) are juxtaposed across sections and appendices without clear indication of **which null procedure** each uses (with/without shot noise, with/without nuisance parameters, dense limit vs shot‑noise‑degraded). This makes comparisons like “7.9% improvement” and “consistent with 6.1% within the Heinrich penalty range” formally unsupported.

  3. **Abstract faithfulness and hedging (F, H):**  
     - The abstract presents σ(fNL) = 8.14 and the [3.92, 8.98] interval as if they were a standard 1σ forecast and then claims a “7.9% improvement consistent with no improvement at < 1σ,” but the body shows that this interval comes from a somewhat ad‑hoc mapping of α uncertainty through a non‑linear α² Fisher formula, and that the “improvement” is essentially a central‑value artifact.

- **Required fix:**  
  - Choose a **single, documented baseline σ(fNL)std** (with explicit reference to Heinrich et al. or your own full Fisher calculation), and derive all quoted improvements from that one configuration.  
  - Replace the Appendix‑C linear scaling table with the α²‑based Fisher‑positivity expression you now favor, or clearly segregate it as “obsolete linearized toy model” not used for headline numbers.  
  - Recompute the “1σ envelope” by properly marginalizing over α with α² entering the Fisher, rather than linearly mapping ±1σ(α). If this is too complex, downgrade the quoted [3.92, 8.98] to a **scenario range** rather than a 1σ interval, and remove the “1σ envelope” wording from abstract and body.  
  - Add a brief paragraph in §V explaining which σ values (11.71, 12.72, 16.85, 8.98) come from which Fisher configurations, and explicitly flag that they are not all directly comparable (different shot‑noise assumptions, tracer sets, and nuisance parameters).

---

P3-M6 — NANOGrav spectral-index Bayes factors: prior volume and model definition not fully specified

- **Offending text (§V A, Appendix E, Table IV):**  
  - “flat priors γ ∈ [0, 7], log10 A ∈ [−18, −11]. … Proper Savage–Dickey Bayes factors against the γ‑uniform prior yield BMB/free = 3.23 and BSMBHB/free = 4.52 × 10−4, giving BMB/SMBHB = 7.14×10³ (log10 B = +3.85, ‘decisive’).”  
  - Table IV: “Savage–Dickey BMB/SMBHB = 7.14×10³ (log10 B = +3.85, decisive) — Ceffyl KDE chain; §V A.”

- **Problems (A, D, E, H):**  
  1. **Model/prior mismatch vs NANOGrav (E, H):**  
     - You use the NANOGrav KDE free‑spectrum likelihood, but adopt your own flat priors in (γ, log10 A) over [0,7]×[−18,−11]. NANOGrav’s published Bayes factors use different parameterizations and prior choices. Without an explicit, equation‑level mapping to NANOGrav’s priors and a check that the KDE likelihood is being interrogated in the same space, the quoted BMB/free and BMB/SMBHB *cannot* be directly compared to NANOGrav collaboration results.  
     - Yet Table IV labels BMB/SMBHB as “decisive” on Jeffreys’ scale without emphasizing that this is **your own re‑analysis under different priors**, not NANOGrav’s official model comparison. The caveat “Neither constitutes a detection; both are reported as illustrative” (in §V A) helps but does not appear where the Bayes factors are first presented or summarized.

  2. **Savage–Dickey applicability (D):**  
     - Savage–Dickey requires that the nested model’s parameter value (e.g., γ = 3.0 for bounce, γ = 4.33 for SMBHB) lies within the support of the prior for the larger model and that the prior on the “extra” parameter factorizes. You do not show that the KDE implementation and your priors satisfy these conditions; given the KDE is in free‑spectrum amplitudes, the mapping to (γ, log10 A) is non‑trivial.  
     - It is therefore not clear that the Bayes factors have been computed in a way that strictly satisfies Savage–Dickey’s assumptions.

- **Required fix:**  
  - In §V A and Table IV, explicitly state that BMB/SMBHB is **your re‑analysis under flat priors γ ∈ [0,7], log10 A ∈ [−18,−11]**, and that NANOGrav’s own Bayes factors are different because of different models/priors.  
  - Either provide a short derivation or clear reference showing that the Savage–Dickey formula is valid for this KDE‑based likelihood and your parameterization, or switch to a straightforward numerical evidence ratio (e.g., via thermodynamic integration or nested sampling) to avoid reliance on conditions that are not demonstrated.  
  - Tone down “decisive” language: present the 7.1×10³ figure as an **illustrative Bayes factor under specific priors**, not as a robust model‑selection statement.

---

P3-M7 — Cross‑survey deduplication: radius choice and unique‑count robustness overstated

- **Offending text (§IV C, Table I footnote ∥, Appendix F):**  
  - “The uniform 5″ matching radius is a conservative compromise… the 637 multi‑survey coincidence count should be read as a lower bound … Because all reported headline numbers … are computed at the canonical 5″ radius, alternate radii would shift the multi‑survey/intra‑survey split slightly but cannot change the unique‑object count by more than the 637 + 9,576 = 10,213 total compression observed at 5″.”  
  - “The Planck patches contribute zero positional overlaps with the point‑source surveys at the 5″ matching radius … so the stratification is exact.”

- **Problems (B, C, D, H):**  
  1. **Over‑strong claim of robustness (H):**  
     - The statement that alternate radii “cannot change the unique‑object count by more than 10,213” is not strictly justified: moving from 5″ to 7″ can identify cross‑survey associations that are *not* present at 5″ and thus increase compression beyond the 5″ value; similarly, moving to 3″ can *reduce* compression if some current 5″ matches are spurious. The 10,213 number is the compression at one radius, not a rigorous upper bound on possible compression.  
     - The Budavári–Szalay probabilistic‑matching approach is mentioned as “deferred,” yet you still assert ≤0.1% sensitivity of the unique count to more sophisticated matching; that is speculative.

  2. **Unit/geometry assumptions (C):**  
     - The claim that Planck patches “contribute zero positional overlaps … analogous to the ACT zero‑overlap result” and hence that the stratification of 378,080 point sources + 200 patches is “exact” assumes that a 64×64 pixel patch at Planck/ACT resolution can never be associated with any catalogued object within 5″ of its center. This is not a dimensional impossibility; 5″ is a tiny fraction of a patch, but associations are about sky coordinates, not pixel indexing. The “exact” language therefore overstates what has been shown (which is only that *in the present run* no such overlaps were found).

- **Required fix:**  
  - Replace “cannot change … by more than 10,213” with a more cautious statement: e.g., “alternate radii would change the unique‑object count at most at the few‑percent level given the current 2.6% compression at 5″; we have not yet explored a full probabilistic matching.”  
  - For the Planck/ACT stratification, rephrase to “In the current 5″ matching scheme, no Planck patches overlap point‑source anomalies; thus the 378,080 and 200 tiers are disjoint under our matching criterion,” avoiding “exact” language that suggests a geometric impossibility.  
  - Flag clearly that more advanced cross‑matching (Budavári–Szalay, variable radius, proper‑motion propagation) could in principle modify the unique‑object count modestly.

---

P3-N5 — Abstract vs body: “three DESI×SDSS cross‑matches” vs 637 multi‑survey coincidences

- **Offending text:**  
  - Abstract: “Three DESI×SDSS cross‑matches include a time‑variable source … and an uncataloged BAL QSO at z ≈ 0.86.”  
  - Body (§IV C): “The 7‑way positional deduplication at 5″ identifies 637 multi‑survey coincidences … The three highest‑confidence cross‑survey detections are from the DESI×SDSS pairwise channel (Fig. 6): …”

- **Problem (F):**  
  - The abstract mentions “three DESI×SDSS cross‑matches” and lists them as if they were the only cross‑survey matches of note, without any allusion to the much larger set of 637 multi‑survey coincidences documented later. A hurried reader could interpret this as “only three cross‑survey matches were found,” which understates the multi‑survey coincidence structure.

- **Required fix:**  
  - In the abstract, add a clause to indicate scale, e.g., “Among 637 multi‑survey coincidences, three DESI×SDSS cross‑matches include…” so that the abstract faithfully reflects the broader cross‑survey statistics presented in §IV C.

---

P3-N6 — Minor text/notation inconsistencies affecting clarity

- **Offending text (scattered):**  
  - Use of “0.87% anomaly rate” and later “0.87% anomaly rate; applying [the threshold] to a random uncured SPARCL sweep flags >50% of spectra” (Section II B).  
  - Use of “val loss ≤ 0.30” as a universal gate for surveys whose typical val loss is ~0.03 (spectroscopic) vs 0.44 (CMB).

- **Problems (H, C):**  
  - The SPARCL comparison mixes a curated DESI sample and a “random uncured” external sample but still uses S > 5 anchored to DESI’s μval, σval, without reiterating that this is not a like‑for‑like comparison of anomaly *rates*; you do state this in prose, but the numerical juxtaposition (0.87% vs >50%) invites over‑interpretation.  
  - The val‑loss gate of 0.30 is more than an order of magnitude above the typical spectroscopic convergence values (≈0.03) and below the Planck val loss (0.44) that you still accept by invoking injection‑recovery. The numerical choice of 0.30 thus appears arbitrary rather than optimized, but this is nowhere quantified.

- **Required fix:**  
  - When quoting 0.87% vs >50%, add a brief parenthetical “(non‑comparable samples; see §VI D)” directly in the sentence to prevent misuse.  
  - In §II D, briefly justify the numeric value 0.30 for the val‑loss gate (e.g., by relating it to median per‑pixel variance or to the range of convergence values seen in spectroscopic vs CMB cases), or acknowledge that it is heuristic and that injection‑recovery is the decisive gate for CMB.

---

Overall, you did well on citation forensics and some high‑level consistency in the first pass, but this “fresh eyes” review finds that:

- The **σ(fNL)** forecasting story is still under‑rigorously documented and internally inconsistent between linear and quadratic α treatments.  
- The **NANOGrav Bayes factors** are presented more strongly than the derivation justifies.  
- Table I and associated “largest” claims blend cross‑transfer and Path‑C quantities in ways that obscure what is actually canonical.  
- Several **abstract and caption statements** either omit crucial qualifiers or suggest comparability where the underlying null procedures differ.

These are all fixable with careful editing and, in a couple of places, recomputation, but they matter at PRD’s standard of rigor.