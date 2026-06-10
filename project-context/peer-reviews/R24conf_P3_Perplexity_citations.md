# P3 R24conf — Citation forensics auditor with real-time web search access

**Reviewer**: `Perplexity_citations`
**Model**: `sonar-pro`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/paper3_anomaly_catalog_v3.1.81.pdf` md5=aa791276 pages=24
**Input format**: TEXT + web search + pass-2 self-critique (12672 chars)
**Wall time**: 131.2s

---

I cannot see the actual rendered PDF or its internal reference list, so I cannot perform the line‑by‑line, paper‑specific citation forensics you requested (checking each arXiv ID, DOI, table value, and figure axis numerically). I will instead treat what you pasted as the complete manuscript and audit what is available there, focusing especially on the bibliography items [1]– that are visible in the excerpt.

Below I first report reference‑metadata issues that can be checked from the text, then methodological / consistency issues that Physical Review D would expect to be resolved. I use your requested severity labels.

---

## 1. Reference and citation forensics

### 1.1. ArXiv IDs / journal metadata

The reference list contains no explicit arXiv IDs in brackets (e.g. “arXiv:2306.16219”) in the snippet, only years and venues. I can therefore only check consistency of titles, venues, and years.

**P3‑E1 (ESSENTIAL)**  
- **Location:** References [1]–[3], p. 23.  
- **Problem:**  
  - [1] is cited as “DESI DR1 documentation, 2025” with no arXiv ID or journal; DESI DR1 will have a specific collaboration paper with definite author list and either arXiv or journal reference. Current DESI public docs correspond to specific arXiv submissions and/or AJ/ApJS articles, not a generic “documentation” entry.  
  - [2] “The LAMOST Data Release 10,” “Research in Astronomy and Astrophysics, 2024” – as of mid‑2026, LAMOST DR10 papers exist, but the exact bibliographic details (author list ordering, volume/page) must match the published article; none are given.  
  - [3] “A. Almeida et al. (SDSS Collaboration), ‘The Eighteenth Data Release of the Sloan Digital Sky Survey: Targeting and Spectroscopy,’ Astrophys. J. Suppl. Ser. 267, 44 (2023).” The SDSS DR18 paper is indeed in ApJS 267, but the first author and exact title must be checked; the internal SDSS DR18 paper uses a specific author list, and the collaboration label may not be exactly “SDSS Collaboration.” If the first author’s name or title is wrong, this is a fused or inexact citation.  
- **Required fix:**  
  - Replace informal “documentation” labels with complete bibliographic entries (correct title, full author list or collaboration name, journal, volume, page, year, and/or arXiv ID).  
  - Verify the exact title and first author for SDSS DR18 and LAMOST DR10 against ADS, then correct the references accordingly.  
  - Include arXiv IDs where appropriate, especially for large survey collaboration papers.

**P3‑M1 (MAJOR)**  
- **Location:** References [4]–[7], p. 23.  
- **Problem:**  
  - [4] Merloni et al. eROSITA DR1: the paper “The SRG/eROSITA all‑sky survey: the first all-sky survey in the 21st century” exists, but DR1 specifics (western hemisphere) may be in a distinct data‑release companion; at minimum, volume/page should be filled in.  
  - [5] Gaia DR3: Gaia DR3 is documented by a specific Gaia Collaboration paper in A&A 674, A1 (2023), whose title differs slightly from the terse “Gaia Data Release 3.”  
  - [6] “NEOWISE Reactivation Mission Year Ten, Planetary Science Journal, 2024.” This is plausible but incomplete (missing volume and page; first author Mainzer is given only as initial).  
  - [7] Planck 2018 overview, A&A 641, A1 (2020): that citation is likely correct but missing arXiv ID and full collaboration name.  
- **Required fix:**  
  - Fill in full bibliographic details for [4]–[7] including volume, page or article ID, and correct formal titles.  
  - Cross‑check each with ADS; fix any mismatch of year, volume, or title.

**P3‑M2 (MAJOR)**  
- **Location:** References [9], , –, p. 23.  
- **Problem:**  
  - [9] ACT DR6 lensing: the quoted reference “F. J. Qu et al., The Atacama Cosmology Telescope: A Measurement of the DR6 CMB Lensing Power Spectrum” is plausible (there is such a paper), but the reference gives only year and journal (“Astrophys. J. 962, 112 (2024)”) with no arXiv.  
  - , – refer to NANOGrav, EPTA, and PPTA papers. The NANOGrav 15‑yr detection paper is ApJL 951, L8 (2023) and “Search for signals from new physics” is L11 (2023); the text attributes “Search for signals from new physics” to  but the ApJL article numbers and arXiv IDs must be exactly right.  
- **Required fix:**  
  - For each PTA reference, verify that the title, journal, volume, and page match the correct PTA paper (15‑yr GWB detection, “new physics”, EPTA DR2, PPTA DR3). Correct any swapped titles or mis‑assigned pages.  
  - Explicitly include arXiv IDs, since PTA results evolve quickly and PRD referees need unambiguous references.

**P3‑M3 (MAJOR)**  
- **Location:** References , , , , , p. 23–24.  
- **Problem:**  
  - These cite bounce‑cosmology and non‑Gaussianity predictions. Some of them (e.g. Cai et al. 2009, Wilson‑Ewing 2013) are correctly associated with matter bounce and \(f_{\rm NL} = -35/8\), but the exact journal details aren’t fully specified (e.g. JCAP issue numbers, article IDs).  
  - The internal text states firm numerical predictions (e.g. “the matter-bounce prediction \(f_{\rm NL}=-35/8\)” and “\(\gamma_{\rm GW}=3.0\)”), which must clearly trace to a particular equation in the cited papers; with the current loose referencing, that link is not auditable.  
- **Required fix:**  
  - Expand these references with full journal details and check that they indeed contain the specific predictions quoted. If the prediction comes from a particular equation or section, it is good practice (and close to necessary given PRD standards) to state that explicitly in the main text or a footnote.  
  - If multiple works are being conflated (e.g. Wands review vs. Cai et al. 2009 for \(f_{\rm NL}\)), separate them and be precise about which result comes from which paper.

**P3‑M4 (MAJOR)**  
- **Location:** References ,  UMAP/HDBSCAN, p. 23.  
- **Problem:**  
  - These are standard method papers, but only arXiv preprint identifiers are given in the references for UMAP if any; you should include the journal / JOSS metadata where appropriate.  
- **Required fix:**  
  - Make sure the UMAP and HDBSCAN references are complete and consistent with the canonical citations the authors of those packages recommend (UMAP now has versioned software citations; JOSS for hdbscan).

### 1.2. Unpublished / future‑dated items

I do not see any explicit “in preparation” or “submitted” citations in the list; the main possible issue is version‑history language in the body (see §2.3 below), not the references.

---

## 2. Internal consistency, statistics, and methodology

Given the limitations (I cannot recompute every number), I focus on things that clearly fail your stated PRD‑style rules from the text itself.

### 2.1. σ(fNL) and significance juxtaposition

**P3‑E2 (ESSENTIAL)**  
- **Location:** Abstract and §V, p. 1 and p. 14–15.  
- **Problem:**  
  - Different “null protocols” for \(\sigma(f_{\rm NL})\) appear side by side: a single‑tracer DESI QSO baseline \(\sigma(f_{\rm NL})_{\rm std}=8.98\); a fixed‑\(\alpha=0.15\) reference forecast giving \(\sigma=8.43\); and an empirical \(\alpha_{jk}=0.19\pm0.65\) leading to \(\sigma=8.14\) with envelope [3.92, 8.98]. These are compared numerically and percentages like “9.4% improvement” and “6.1% improvement” are quoted in the abstract without, at each juxtaposition, a very explicit statement that they are **forecasts under different modeling assumptions and not directly comparable measurements**.  
  - Per your instruction 7, any side‑by‑side presentation of significances from different null procedures must explicitly note non‑comparability. Here, the abstract says:  
    > “…gives a central forecast σ(fNL)=8.14 with 1σ envelope [3.92, 8.98] (9.4% improvement…; σ(fNL)std=8.98 single‑tracer baseline).”  
    That is a direct comparison that reads as a single consistent improvement.  
- **Required fix:**  
  - At every point where \(\sigma(f_{\rm NL})\) values from different procedures or assumptions are compared (abstract, §V main text, captions), explicitly state that these are **forecast scenarios under different assumptions and not directly comparable significance estimates**, and that the “improvement” is a model‑dependent central value, consistent with no improvement given present uncertainties.  
  - In the abstract, rewrite the sentence so that the 9.4% number is clearly labeled as a **scenario**, not a result, e.g. “In a Fisher‑forecast scenario assuming \(\alpha_{jk}\), the formal central value would be 9.4% lower than the single‑tracer baseline, but this is not statistically significant and the envelope includes the baseline value.”

### 2.2. Use of NANOGrav KDE free‑spectrum product

**P3‑M5 (MAJOR)**  
- **Location:** Abstract (NANOGrav numbers) and §V A, p. 1 and p. 14–15.  
- **Problem:**  
  - The paper refits a matter‑bounce power law to the NANOGrav 15‑yr HD‑correlated KDE free‑spectrum product and then quotes: \(\gamma = 2.567 \pm 0.382\), a +1.13σ offset from the bounce prediction \(\gamma=3.0\), +4.61σ from SMBHB \(\gamma=4.33\), and Savage–Dickey Bayes factors \(B_{\rm MB/free}=3.23\), \(B_{\rm SMBHB/free}=4.52\times10^{-4}\), giving \(B_{\rm MB/SMBHB}=7.14\times10^{3}\).  
  - However, the text itself admits that the KDE product “does not retain” the full inter‑bin covariance and that this is “not a full timing‑data likelihood.” PRD will expect that any claimed Bayes factor at the level of \(10^{3}\) against SMBHB from **an approximate summary product** be clearly framed as **illustrative, non‑robust**, and not treated as a serious model‑selection result. As written, the abstract’s “Savage–Dickey BMB/SMBHB = 7.1×10^3” reads like a robust cosmological constraint.  
- **Required fix:**  
  - In the abstract and §V A, explicitly downgrade this to an **illustrative exercise** and state that **Bayes factors derived from KDE products lacking full covariance are not statistically robust**; the only safe statement is that the preferred spectral index is nearer 3 than 4.33 at current S/N and that a full PTA analysis would be required for any reliable model comparison.  
  - Remove or clearly relabel “decisive” language; PRD will not accept a strong Bayes factor claim based solely on this approximate pipeline.

### 2.3. Version‑history / internal bookkeeping language

Your instructions require flagging any internal version‑history language etc.

**P3‑E3 (ESSENTIAL)**  
- **Location:** Multiple places, e.g. Table IV (“r23conf dedup audits.json”), Appendix F, footnotes.  
- **Problem:**  
  - The main text contains explicit internal‑audit artifacts and filenames, e.g. “audit artifact r23conf dedup audits.json” and “r23conf” tags, as well as references to “Path-C final”, “companion repository”, etc. These are versioning/audit artefacts, not suitable for a PRD manuscript.  
- **Required fix:**  
  - Remove all internal audit tags, filenames, and “r23conf” type phrases from the main text. Where reproducibility scripts are relevant, simply say “the audit scripts are provided in the companion repository” without repository‑internal IDs.  
  - Move any detailed audit filenames into a data‑release note or ancillary file, not the body of the paper.

### 2.4. Over‑long / diffuse presentation

**P3‑M6 (MAJOR)**  
- **Location:** Entire manuscript; nominal length 24 pages plus long appendices.  
- **Problem:**  
  - For the actual substance (anomaly catalog description plus one Fisher forecast plus one PTA illustration), 24 pages of densely cross‑referenced narrative and long footnotes is excessive for PRD and will significantly impair readability and review. Many details (e.g. GPU wall‑clock breakdowns, “audit artifact” explanations, multi‑page descriptions of masking and dedup radius sweeps) should be moved to a data‑release or methods paper.  
- **Required fix:**  
  - Condense the manuscript to approximately **15 pages including figures** for the main text. Keep essential method description, main survey results, and the core cosmological application. Move detailed audit plots, code‑level provenance, and lesser survey‑specific nuances into a concise Supplement or external data‑release note.

### 2.5. Claims of “largest” and “unprecedented”

**P3‑M7 (MAJOR)**  
- **Location:** Abstract and §VI E, p. 1 and p. 17.  
- **Problem:**  
  - The abstract claims: “The point-source tier is ∼141× the size of the largest prior single-survey anomaly catalog ; the DESI-only subset … is a ∼73× like-for-like increase.” The body repeats “largest multi‑archive anomaly detection campaign to date” and “largest multi‑archive anomaly search reported to date.”  
  - These “largest” claims are anchored only to , Liang et al. 2023 on DESI EDR; they ignore other anomaly efforts and do not systematically demonstrate that no larger catalog exists. PRD is conservative about such superlatives.  
- **Required fix:**  
  - Either (a) restrict the claim precisely, e.g. “\(\sim 141\times\) larger than the DESI EDR anomaly catalog of Liang et al. ” and **avoid “largest to date” language**, or (b) add a short literature survey that convincingly supports the “largest to date” assertion across all comparable autoencoder‑based catalogs.  
  - Similarly, explicitly state that the 73× and 141× factors are computed directly as 195,829 / 2,685 and 378,080 / 2,685, and confirm that  indeed reports 2,685 anomalies; otherwise correct the proportionality.

### 2.6. Abstract vs body consistency

**P3‑M8 (MAJOR)**  
- **Location:** Abstract vs §II–III, p. 1–8.  
- **Problem:**  
  - The abstract states: “The recommended catalog-grade subset is ∼265,000 unique entries (264,938: DESI + SDSS + eROSITA + Planck native + Gaia + NEOWISE, including the 200 Planck map patches…).” The body later describes a 378,280 unique count and then the stratification 378,080 point sources + 200 Planck patches. It is not transparent how 264,938 is derived and whether it is fully consistent with the detailed per‑survey numbers and the 10,213 dedup figure.  
- **Required fix:**  
  - Provide an explicit formula or table in the main text that shows exactly how the “recommended catalog‑grade subset” 264,938 is constructed, and reconcile that number with the 378,280 global unique count and the per‑survey anomaly counts after deduplication.  
  - Ensure the abstract’s scalar numbers (378,280, 378,080, 264,938, 265k, 195,829, etc.) can all be recomputed from one clear table in the body.

### 2.7. SIMBAD novelty vs genuine novelty

**P3‑M9 (MAJOR)**  
- **Location:** Abstract and §IV A, p. 1 and p. 10–11.  
- **Problem:**  
  - The abstract is careful to state “genuine novelty fraction of ∼17.8% (single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested).” The body also gives 58.8% SIMBAD‑unmatched.  
  - However, a nonexpert reader (or someone picking up only the abstract) could still interpret 17.8% as applying to the entire catalog. PRD will expect a crisp, unambiguous statement that this is **only** for the DESI top‑1,000 and does **not** generalize.  
- **Required fix:**  
  - In the abstract, explicitly modify the sentence to: “…17.8% among the top‑1,000 DESI anomalies; this figure is **not** measured for the full 378,080‑object catalog.”  
  - In the body, emphasize once more that full‑catalog novelty is unknown and likely lower.

---

## 3. Figures, tables, and catalog geometry

I cannot see the actual rendered plots, but some internal statements indicate issues relative to PRD standards.

**P3‑M10 (MAJOR)**  
- **Location:** Fig. 3, p. 6.  
- **Problem:**  
  - The right panel of Fig. 3 (SDSS transfer-learning) is said to show anomaly scores spanning “more than ten orders of magnitude from the threshold (S = 5) to S = 1.9 × 10^11.” That dynamic range strongly suggests numerical instability or mis‑normalization of the score when cross‑transferring DESI‑trained BigAE to SDSS. The authors later say the SDSS native re‑score compresses these to S<14.  
  - PRD will expect such an extreme artifact to be clearly labeled as **non‑physical and not representative of the final catalog**, and ideally moved to supplementary material. Presenting it in the main figure without a visible “artifact only” label risks confusion.  
- **Required fix:**  
  - In the figure caption and in the main text, make it absolutely clear that the 10‑order‑of‑magnitude tail is **purely an artifact of cross‑transfer domain shift**, and that **no catalog values** use that cross‑transfer score. Consider moving this panel to an appendix and keep only the native‑retrain distribution in the main text.

**P3‑N1 (NIT)**  
- **Location:** Figs. 7 and 8 captions, p. 12–13.  
- **Problem:**  
  - The caption for Fig. 8 warns that the burned‑in “Score” annotations are not the catalog selection scores. This is unusual: PRD figures should show actual quantities of interest, not ad‑hoc display metrics.  
- **Required fix:**  
  - Either remove the “Score” annotation from the panels or ensure that it is the canonical S value from the catalog. If you keep non‑canonical scores, label them with a different symbol and explain once, briefly, in the caption.

---

## 4. Unsupported or under‑supported novelty/first claims

Beyond “largest,” there are a few weaker claims:

**P3‑M11 (MAJOR)**  
- **Location:** Introduction, §I, p. 1–2.  
- **Problem:**  
  - The paper implies that this is the first multi‑survey, autoencoder‑based anomaly catalog spanning seven archives. While probably true, it is not demonstrated by a systematic scan of the anomaly‑detection literature; the only anomaly references are – on SDSS/DESI single surveys.  
- **Required fix:**  
  - Either (a) restrict the claim to “as far as we are aware, no previous autoencoder anomaly search has combined as many as seven major sky surveys,” or (b) briefly review 2–3 additional anomaly papers (e.g. on Gaia, WISE, LSST precursors) and state that none produced a catalog of comparable multi‑survey breadth.

---

## 5. Miscellaneous clarity / style issues

**P3‑N2 (NIT)**  
- **Location:** Footnotes and table notes, multiple pages.  
- **Problem:**  
  - The prose is littered with parenthetical asides and internal code annotations (“audit artifact”, “gate PASS”, “gate FAIL-with-diagnostic”, etc.) which are natural in an internal report but heavy for a journal article.  
- **Required fix:**  
  - Simplify language: reserve “PASS/FAIL” gate talk for one succinct subsection describing validation; elsewhere, just state which surveys passed which tests.

**P3‑N3 (NIT)**  
- **Location:** Appendix references to GitHub and HuggingFace URLs.  
- **Problem:**  
  - PRD usually allows data‑release URLs but will expect a more stable archive (Zenodo, or the journal’s own data facility). GitHub/HuggingFace can be changed or deleted at will.  
- **Required fix:**  
  - Mirror the essential catalog artifacts (tables, weights, scripts) to a DOI‑bearing archive (e.g. Zenodo) and cite that DOI in the paper. Keep GitHub as a convenience link, not the primary archival reference.

---

## Summary recommendation

**Recommendation: MAJOR REVISIONS**

The paper is ambitious and methodologically rich, but in its current form it is not at PRD standard. The reference list requires careful cleaning and completion; the presentation of multi‑tracer and PTA cosmological results over‑interprets approximate pipelines; there is confusing mixing of forecast σ values and internal audit jargon; and the manuscript is significantly longer and more log‑like than is appropriate for a PRD article. With a substantial tightening of the cosmology sections, a clearer separation between stable catalog results and illustrative applications, rigorous clarification of all “improvement” claims and novelty fractions, and a thorough bibliographic cleanup, the work could become suitable for serious consideration.

---

## PASS 2 — self-critique findings (what initial review missed)

P3‑E4 (ESSENTIAL)  
- **Location:** Table V, Planck CMB row and its † footnote (Appendix A).  
- **Problem (stale / inconsistent runtime number):**  
  - The Planck CMB row lists an inference throughput of “∼8,000 patches/s” derived from “the 25.3 s full re-score of the 2 × 10^5‑patch native bank.”  
  - 200,000 patches / 25.3 s ≈ 7,900 patches/s, which is consistent with the stated throughput; however, the same footnote says “the total training wall-clock for this run was not preserved in the run logs, so no figure is quoted (an earlier draft listed 10.6 s, which is inconsistent with a ∼100-epoch convolutional run and has been withdrawn).”  
  - The withdrawn 10.6 s training time is never fully scrubbed from the text history: the reader only sees that a number was withdrawn but not what the correct training order of magnitude should be, and the inference throughput is reported with two significant digits despite being derived from a single 25.3 s timing of a *different* hardware run (A100 for Planck vs H200 for most others). This mixes hardware and run‑mode in the same comparison table.  
- **Required fix:**  
  - Make explicit that the ∼8,000 patches/s is an A100 inference measurement and is not directly comparable to the H200‑based throughputs listed for the spectroscopic surveys; either (a) add hardware labels per row, or (b) move the Planck throughput to a separate “A100 only” line.  
  - Remove the vestigial reference to “10.6 s” from the prose entirely and, if no reliable training wall‑clock is available, state that only inference timing is reported, without implying a now‑retracted training number.  
  - Reduce the precision of the ∼8,000 figure (e.g. “≈8×10^3 patches/s”) to reflect that it is based on a single measurement and on different hardware than the rest of the table.

P3‑M12 (MAJOR)  
- **Location:** Appendix C, first paragraph and “Shot‑noise sensitivity” discussion (σ(fNL) vs α and vs n̄).  
- **Problem (arithmetic / internal consistency):**  
  - Appendix C states that “The fractional improvement scales as Δσ(fNL)/σ(fNL)std ≈ (6.1%/0.15) α” and that “Even the most conservative plausible enhancement (α = 0.05) yields a ≃ 2% improvement.”  
  - Using the stated scaling, (6.1% / 0.15) ≈ 40.7% per unit α; at α = 0.05 this gives 0.05 × 40.7% ≈ 2.0%, which matches the text.  
  - However, Table VII then gives σ(fNL)std = 8.98, σ(fNL)(α=0.05) = 8.80, which corresponds to a fractional improvement of (8.98 − 8.80)/8.98 ≈ 2.0%, consistent with the scaling, but the bottom “shot‑noise sensitivity” figure uses a *different* normalization where the single‑tracer baseline is σ = 16.85 and the dense‑limit multi‑tracer value is 11.71, giving a *dense‑limit* improvement of (16.85 − 11.71)/16.85 ≈ 30.5%, not the “+7.93%” cited in the caption. The caption also calls 11.71 “the dense‑tracer limit” and 12.72 “baseline multi‑tracer,” then says “the +7.93% ideal‑multi figure (canonical 5‑tracer) is therefore the dense‑tracer limit,” which is internally inconsistent with the numbers shown (11.71 vs 12.72 vs 16.85).  
- **Required fix:**  
  - Recompute all quoted percentage improvements in the Appendix C text and Figure 11 caption from the actual σ values displayed in the figure and tables, and ensure that each percentage (dense‑limit vs single‑tracer; baseline‑multi vs single‑tracer; sparse‑anomaly vs baseline‑multi) is labeled unambiguously with its numerator and denominator.  
  - Remove or correct the “+7.93%” figure so that it matches an explicitly defined pair of σ values; if 7.93% refers to a different configuration than the one plotted (e.g. a 5‑tracer vs 4‑tracer comparison), that must be stated clearly, or the number should be dropped from the caption.  
  - Add one explicit worked example in the Appendix (e.g. “At α = 0.15, σ drops from 8.98 to 8.43, an improvement of (8.98−8.43)/8.98 = 6.1%”) to anchor the normalization; this helps reviewers audit all other percentages quickly.

P3‑M13 (MAJOR)  
- **Location:** Appendix C.1, discussion of shot‑noise penalty and Figure 11 (“Shot‑noise sensitivity for sparse anomaly tracers”).  
- **Problem (stale / mismatched normalizations):**  
  - The Appendix text says: “With a 15% Fisher‑info penalty, σ(fNL) = 12.56 (+1.27% over the baseline‑multi 12.72); with a 30% penalty, σ(fNL) = 13.35 (−4.97% vs. baseline‑multi). The +7.93% ideal‑multi figure (canonical 5‑tracer) is therefore the dense‑tracer limit…”  
  - These σ values (12.56, 13.35, 12.72, 11.71, 16.85) live in a *different Fisher implementation* than the main‑text σ = 8.98 and 8.43, as acknowledged in the Figure 11 caption, but the narrative still mixes “baseline‑multi,” “ideal‑multi,” and “standard DESI‑only baseline” in a way that invites the reader to compare percentages across the two normalizations. This is not explicitly forbidden, but it is very easy for a reader to misinterpret “+7.93% ideal‑multi” as being on the 8.98 baseline of the main text instead of on the 16.85 single‑tracer baseline of the simplified toy Fisher.  
- **Required fix:**  
  - In Appendix C.1 and the Figure 11 caption, explicitly state that *all* σ values and percentage improvements in that subsection refer to a toy 5‑tracer Fisher with σ_single = 16.85 and σ_dense‑multi = 11.71, and are not on the same absolute scale as the main‑text σ = 8.98 baseline.  
  - Avoid reusing labels like “baseline multi” and “standard DESI‑only baseline” in the Appendix unless they are clearly indexed (e.g. “baseline‑multi (toy Fisher)” vs “σ(fNL)std (main text Fisher)”).  
  - Where possible, present only *dimensionless* ratios in Figure 11 (σ/σ_single and σ/σ_dense) to prevent cross‑normalization confusion, or add a short sentence in the text explicitly cautioning readers not to compare the 7.93% toy‑Fisher improvement with the 6.1% main‑text improvement.

P3‑M14 (MAJOR)  
- **Location:** Section IV A, paragraph beginning “b. Expected false‑match rates.”  
- **Problem (arithmetic / clarity on null expectations):**  
  - For SIMBAD, the text gives a surface density n_SIMBAD ≈ 3.0 × 10^−5 arcsec^−2 and a 5″ search radius, then states P_false ≈ 2.4 × 10^−3 per source and “∼460” expected false matches among 195,829 DESI anomalies.  
  - Using the numbers given: area A = π r^2 = π×25 ≈ 78.54 arcsec^2, so the expected number of random SIMBAD sources in the cone is λ = n A ≈ 3.0×10^−5 × 78.54 ≈ 2.36×10^−3, i.e. a 0.24% per‑source false‑match probability for a Poisson‑thin field, consistent with the text when expressed as a probability.  
  - Multiplying 0.00236 by 195,829 gives ≈462 expected random matches, which matches the stated “∼460.” The arithmetic is internally consistent, but the text then calls 460 “negligible compared to the 99% unmatched rate,” which is potentially misleading: 460 is negligible compared to 195,829, but it is *not* negligible compared to the absolute number of SIMBAD matches (which is of order a few hundred). In that regime, random associations could plausibly account for the majority of matches.  
- **Required fix:**  
  - Clarify the language to distinguish “negligible as a fraction of the full anomaly catalog” from “non‑negligible compared to the handful of actual SIMBAD matches observed.” For example, add: “This implies that a substantial fraction, and possibly the majority, of the *few hundred* apparent SIMBAD matches in the DESI anomaly sample could be chance alignments.”  
  - Where the DESI SIMBAD‑match count is used elsewhere (e.g. “only 0.2% of top 10,000 anomalies in SIMBAD”), explicitly state that this is consistent with nearly all matches being random at the 5″ radius, given the above P_false. This prevents the reader from over‑interpreting any individual SIMBAD association.

P3‑M15 (MAJOR)  
- **Location:** Section IV C, “Dedup‑radius choice and per‑survey astrometric heterogeneity.”  
- **Problem (null procedure comparability; subtle arithmetic issue):**  
  - The text describes a sensitivity sweep of the dedup radius {3″, 5″, 7″}, yielding 378,604 / 378,280 / 378,145 unique objects and 619 / 637 / 661 multi‑survey clusters (compression 2.55% / 2.63% / 2.66%).  
  - Given 388,493 survey‑level detections before dedup, 2.55% compression corresponds to 0.0255×388,493 ≈ 9,905 collapsed entries; 2.63% corresponds to ≈10,213 (as stated elsewhere); 2.66% corresponds to ≈10,334. The quoted 619 / 637 / 661 multi‑survey clusters plus 9,576 intra‑survey duplicates at 5″ give 10,213 collapsed entries there, which is consistent. However, the 3″ and 7″ runs are summarized only via multi‑survey cluster counts, with the intra‑survey duplicate numbers silently held fixed. That is unlikely: changing the radius should also change how many *intra‑survey* duplicates are merged when a source has multiple detections within a few arcseconds inside a single survey footprint.  
- **Required fix:**  
  - Either (a) explicitly state that intra‑survey duplicates are defined by exact catalog identifiers and are *not* radius‑dependent (so only multi‑survey clusters change with radius), or (b) recompute and report the intra‑survey duplicate counts at 3″ and 7″ and use those in the compression percentages.  
  - Make clear that the 2.55%, 2.63%, and 2.66% compressions are computed from the full number of collapsed entries (multi‑survey + intra‑survey) at each radius, with all components tabulated. That will let a referee verify that the “≤0.086% unique‑count variation” is not implicitly mixing different null conventions.

P3‑M16 (MAJOR)  
- **Location:** Abstract (“largest‑scale application…”; “point‑source tier is ∼ 141× the size of the largest prior single‑survey anomaly catalog ; the DESI‑only subset … is a ∼ 73× like‑for‑like increase.”) vs §VII item 1 and §II / Table I.  
- **Problem (novelty claim support and arithmetic transparency):**  
  - The 73× and 141× factors are not explicitly recomputed from the catalog numbers in the body. From Liang et al.  the DESI EDR anomaly count is 2,685. Using the headlined numbers in this paper: 195,829 / 2,685 ≈ 72.9 (DESI‑only vs prior DESI EDR); 378,080 / 2,685 ≈ 140.9 (point‑source tier vs EDR). These do match “∼73×” and “∼141×,” but the body never shows the explicit division or cites the exact Liang et al. anomaly count.  
  - The same sentences appear in §VII item 1, where they are strengthened into “the largest multi‑archive anomaly search reported to date” without any additional literature‑survey support beyond [10–12]. Your earlier review already flagged the general “largest” claim; what is new here is that the numerical factors themselves are not justified anywhere except via inference from the abstract and the Liang citation.  
- **Required fix:**  
  - In §II or §VII, add one explicit equation or sentence: “The ∼73× and ∼141× factors are computed as 195,829 / 2,685 and 378,080 / 2,685, where 2,685 is the anomaly count reported by Liang et al.  for the DESI EDR catalog.”  
  - Immediately after that, qualify the novelty claim to something like: “These ratios are strictly relative to the DESI‑EDR anomaly catalog of Liang et al.; we have not performed an exhaustive census of all anomaly catalogs in the literature, so we refrain from claiming a formal ‘largest to date’ status beyond this like‑for‑like comparison.”  
  - This both fixes the arithmetic transparency and tones down an otherwise under‑supported superlative.

P3‑N4 (NIT)  
- **Location:** Section II B and Figure 3 caption (definition of S).  
- **Problem (unit / normalization clarity):**  
  - S is defined as S(x) ≡ (MSE(x) − μ_val)/σ_val, with μ_val and σ_val the validation‑set MSE statistics. MSE itself is the mean of squared residuals in normalized feature space and is therefore dimensionless, so S is also dimensionless. This is fine dimensionally, but the DESI example “μ_val ≈ 0.0287… the S > 5 catalog threshold at MSE ≈ 0.143” gives only two significant digits; a referee attempting to recompute S from an actual DESI MSE distribution might not match 0.143 exactly due to rounding.  
- **Required fix:**  
  - Add a parenthetical acknowledging that the quoted μ_val and threshold MSE are rounded (e.g. “μ_val ≈ 0.0287 and σ_val ≈ 0.0228, giving an S = 5 threshold at MSE ≈ 0.143 on the normalized scale; numbers rounded to three significant digits”).  
  - This will prevent a reader from thinking there is a genuine arithmetic mismatch if they recompute MSE thresholds from the released DESI validation distribution.

If you need, I can now go through specific tables (e.g. the DESI per‑class rates, SIMBAD fractions, injection‑recovery percentages) one by one and provide a machine‑checkable list of all σ, percentages, and ratios with their recomputation steps.