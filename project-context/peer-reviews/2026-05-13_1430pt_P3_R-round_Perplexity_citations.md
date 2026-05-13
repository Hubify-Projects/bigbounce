# P3 R-round — Perplexity-style citation-chain adversarial review

**Reviewer persona:** Perplexity AI (literature/citation hawk; cross-validates every bibitem against arXiv / ADS / journal records).
**Target:** `pipelines/p3_anomaly_engine/paper3_draft.tex` (embedded `thebibliography` at L976–L1132).
**Version reviewed:** P3 v3.1.37 (30 `\bibitem` entries embedded in .tex; the on-disk `paper3_draftNotes.bib` is a stub — bibliography is .tex-embedded per status.md "bibliography (28 \bibitem) embedded in .tex ✓" line at L72 of SSOT/paper-3/status.md, now actually 30 with `Foreman-Mackey2013` + `Lentati2013` + `WilsonEwing2012` added in Wave 13-B and R41).
**Scope:** Spot-check 11 high-stakes bibitems from the citation-focus list (NANOGrav 15-yr, EPTA DR2, Hellings-Downs, Heinrich+2024, Baron+Poznanski 2017, eROSITA DR1, Gaia DR3, DESI DR1, LAMOST DR10, SDSS DR18, recent 2024–2026 PTA/anomaly-detection lit) plus a hygiene sweep across the remainder. SSOT context: status.md records Heinrich+2024 prose harmonization at "SSSSS" (year=2024) and a Foreman-Mackey emcee bibitem added at Wave 13-B (2026-05-01).
**Method:** WebSearch against arxiv.org / ui.adsabs.harvard.edu / aanda.org / IOPscience landing pages. Spot-check, not exhaustive; the most consequential bibitems were fully traced.
**Date:** 2026-05-13 14:30 PT.

---

## TL;DR

- **Total findings: 7** — **1 BLOCKER, 3 MAJOR, 2 MINOR, 1 NIT.**
- **Most concerning citation error (one sentence):** The `Heinrich2023` bibitem at L1107–1110 reads "`JCAP \textbf{2024}, 074 (2024), arXiv:2311.13082`" but arXiv:2311.13082 (Heinrich, Doré, Krause, "Measuring $f_{\rm NL}$ with the SPHEREx Multi-tracer Redshift Space Bispectrum") was published in **Phys. Rev. D 109, 123511 (2024)** — *not* JCAP — so the prior R-round SSSSS "year=2024" harmonization fixed the year but left the venue wrong, and a reviewer who clicks through to verify the σ(f_NL)=0.7 forecast (the load-bearing primary-source anchor the paper now leans on after the R41 cross-paper-cite removal) will land on a journal/volume mismatch.
- The NANOGrav 15-yr bibitem verifies clean (Agazie et al. 2023, ApJL 951, L8, arXiv:2306.16213). SDSS DR18 (Almeida et al. 2023, ApJS 267, 44), Gaia DR3 (Gaia Collab. / Vallenari et al. 2023, A&A 674, A1), eROSITA DR1 (Merloni et al. 2024, A&A 682, A34), Wilson-Ewing 2012/2013 (JCAP 1303:026, arXiv:1211.6269), Cai et al. 2009 (JCAP 0905:011, arXiv:0903.0631), and Wenger et al. 2000 (SIMBAD A&AS 143, 9) all match arXiv/journal records. DESI DR1 (`DESI2025DR1`) is cited via a documentation URL with no formal paper — recommend upgrading to the published DESI Collab. 2025 arXiv:2503.14745 (see m1).
- **Coverage gap (MAJOR, see M3):** The citation-focus list explicitly asked Perplexity to verify EPTA DR2 and Hellings–Downs 1983. *Neither is cited anywhere in paper3_draft.tex*. §V.A invokes "HD-correlated KDE free-spectrum" (NANOGrav 15-yr) without ever citing the Hellings–Downs 1983 paper that defines HD correlation, and §V (Combined PTA GPU MCMC) discusses "combined PTA" but never cites EPTA DR2 (Antoniadis et al. 2023). For a paper whose §V.A headline result is "γ = 2.567 ± 0.382 from real HD-correlated KDE recovery", these are required references, not optional ones.

---

## BLOCKERs

### B1. `Heinrich2023` bibitem cites the wrong journal — published in PRD, not JCAP

- **Location:** `paper3_draft.tex` L1107–1110.
- **Claimed in bibitem:**
  ```
  \bibitem{Heinrich2023}
  C.\ Heinrich, O.\ Dor\'e, and E.\ Krause,
  ``Measuring $f_{\rm NL}$ with the SPHEREx Multi-tracer Redshift Space Bispectrum,''
  JCAP \textbf{2024}, 074 (2024), arXiv:2311.13082.
  ```
- **Verified reality (sources: arXiv:2311.13082 abstract page; APS journal record https://doi.org/10.1103/PhysRevD.109.123511):**
  - **arXiv:2311.13082** = Heinrich, Doré, Krause, "Measuring $f_{\rm NL}$ with the SPHEREx Multi-tracer Redshift Space Bispectrum", submitted 2023-11-22.
  - **Published as:** **Phys. Rev. D 109, 123511** (5 June 2024), DOI 10.1103/PhysRevD.109.123511.
  - **NOT a JCAP paper.** No JCAP 2024:074 publication of this work exists. The fiducial result $\sigma(f_{\rm NL})=0.7$ that this paper's §V leans on is in the PRD published version §IV.
- **What's wrong:**
  1. Journal venue is wrong (`JCAP \textbf{2024}, 074` instead of `Phys.\ Rev.\ D \textbf{109}, 123511`).
  2. The prior R-round (SSSSS) closed only the *year* (2023 → 2024) and prose harmonization ("Heinrich \etal~2024") — it left the venue line untouched. SSOT/paper-3/status.md confirms the prose-year harmonization but does not record a venue fix.
  3. This is the citation that backs the σ(f_NL) Fisher forecast and the Wave 14-O α-calibration / Wave 14-R zero-systematic caveat — i.e., the single most-cited primary source in the paper after the survey-DR papers. The R41 closure (line 50 of status.md) explicitly removed the cross-paper `\cite{Golden:2026framework/forecast/chirality}` references "and replaced with primary-source citations (Heinrich2023 for SPHEREx forecast methodology…)". That replacement put weight on Heinrich2023 — and the venue is wrong.
- **Manuscript-level consequence:** §V (L547+) prose reads "Heinrich \etal~2024 §IV 15–30% shot-noise sensitivity range" (Wave 14-O contextualization, line 41–42 of status.md). A reviewer who clicks through to JCAP looking for vol. 2024 article 074 will not find this paper and will mark the manuscript down for citation hygiene. The Path-B zero-systematic caveat in §V also references the Heinrich+2023 systematic floor — the same wrong journal venue.
- **Fix:** Replace L1110 with:
  ```
  Phys.\ Rev.\ D \textbf{109}, 123511 (2024), arXiv:2311.13082.
  ```
  Year stays 2024 (already correct after SSSSS). Bibitem key `Heinrich2023` can stay (it tracks the arXiv submission year, which is fine for the key even when the publication year is 2024). No prose changes needed — the L547 / L720–738 / abstract references to "Heinrich \etal~2024" all remain accurate; only the bibitem journal line changes.
- **Priority:** BLOCKER. The cite is to the most-leaned-on primary source in the paper, and the venue is verifiably wrong. The prior closure recorded in SSOT was incomplete.

---

## MAJORs

### M1. `DESI2025DR1` bibitem cites a documentation URL, not the published DESI Collab. 2025 DR1 paper

- **Location:** `paper3_draft.tex` L978–981.
- **Claimed in bibitem:**
  ```
  \bibitem{DESI2025DR1}
  DESI Collaboration,
  ``The DESI Data Release 1,''
  2025, \href{https://data.desi.lbl.gov/doc/releases/dr1/}{DESI DR1 documentation}.
  ```
- **Verified reality (source: arXiv:2503.14745 abstract; ADS 2025arXiv250314745D):**
  - The formal DESI DR1 reference paper is **DESI Collaboration et al., "Data Release 1 of the Dark Energy Spectroscopic Instrument", arXiv:2503.14745 (2025)**. This is the canonical citable reference for DR1 (analogous to Almeida+2023 for SDSS DR18 and Merloni+2024 for eROSITA DR1, both of which the bib does cite properly).
  - DR1 was publicly released 19 March 2025 and the companion paper appeared on the same date. There IS a formal paper to cite.
- **What's wrong:**
  1. Citing a documentation URL instead of the corresponding arXiv/journal paper is below the standard set by the other six survey-DR bibitems in this paper (each of which gives author + title + journal + volume + page + year). For revtex4-2 publication readiness, a paper URL is not a substitute for a citation.
  2. The 18.7M-redshift / 13.1M-galaxy / 1.6M-quasar / 4M-star DR1 sample sizes the paper invokes throughout §I/§III come from arXiv:2503.14745, not from the documentation URL.
- **Fix:** Replace L979–981 with:
  ```
  DESI Collaboration,
  ``Data Release 1 of the Dark Energy Spectroscopic Instrument,''
  arXiv:2503.14745 (2025), \href{https://data.desi.lbl.gov/doc/releases/dr1/}{DR1 documentation portal}.
  ```
  This keeps the documentation-URL link for reproducibility but anchors the citation to the formal paper.
- **Priority:** MAJOR. Not a falsehood (the URL points to real DR1 docs), but it's the headline survey of the paper and the only survey-DR bibitem without a formal paper anchor — a hygiene gap a careful referee will flag.

### M2. `Liang2023` bibitem journal venue and volume do not match the actual paper

- **Location:** `paper3_draft.tex` L1028–1031.
- **Claimed in bibitem:**
  ```
  \bibitem{Liang2023}
  Z.\ Liang \etal,
  ``Searching for Anomalies in the DESI Early Data Release Spectra,''
  Astrophys.\ J.\ Lett.\ \textbf{961}, L5 (2023).
  ```
- **Verified reality (source: arXiv:2307.07664 abstract page; ADS):**
  - The DESI EDR anomaly paper from this group is **Liang, Y. et al., "Outlier Detection in the DESI Bright Galaxy Survey", arXiv:2307.07664 (2023)** — submitted 14 July 2023. The methodology matches the bibitem description (autoencoder compresses spectra into a redshift-invariant latent space; normalizing flow scores outliers; BGS sample from DESI EDR), so this is unambiguously the paper meant.
  - **Title is wrong:** Actual title is "Outlier Detection in the DESI Bright Galaxy Survey", *not* "Searching for Anomalies in the DESI Early Data Release Spectra".
  - **Journal venue is wrong:** The Liang et al. 2023 paper is in **MNRAS** (Monthly Notices, not ApJL). The bib's "Astrophys.\ J.\ Lett.\ \textbf{961}, L5 (2023)" cannot be verified — ApJL 961 L5 (Jan 2024) is a different paper (in a search I could not locate any anomaly-detection paper at that ApJL volume/page).
  - **First author affiliation:** Y. Liang, not Z. Liang. (Initial in bib is incorrect.)
- **What's wrong:**
  1. Title mis-stated (manufactured-sounding "Searching for Anomalies in DESI EDR Spectra" instead of the literal "Outlier Detection in the DESI Bright Galaxy Survey").
  2. Journal mis-stated (ApJL 961 L5 instead of MNRAS).
  3. First-initial mis-stated (Z. instead of Y.).
- **Manuscript-level consequence:** The bibitem is cited in §II (Methods / Related work, anomaly-detection literature review) as a comparison point for the BigAE framework. A referee who pulls ApJL 961 L5 will not find this paper, and a reader trying to compare BigAE against Liang's normalizing-flow approach will not be able to retrieve the paper via the cited record.
- **Fix:** Replace L1029–1031 with:
  ```
  Y.\ Liang \etal,
  ``Outlier Detection in the DESI Bright Galaxy Survey,''
  Mon.\ Not.\ Roy.\ Astron.\ Soc.\ (2023), arXiv:2307.07664.
  ```
  (Insert MNRAS volume/page when known; the arXiv anchor is the load-bearing piece for verification.)
- **Priority:** MAJOR. Three independent factual errors in one bibitem (author initial, title, journal) — this is the most internally-inconsistent bibitem in the entire bibliography. It looks confabulated.

### M3. EPTA DR2 and Hellings-Downs 1983 are NOT cited — required for §V.A integrity

- **Location:** Throughout §V (Combined PTA GPU MCMC) and §V.A (Wave 13-B real-KDE recovery).
- **Verified reality:**
  - §V.A is built on "the real NANOGrav 15-yr HD-correlated KDE free-spectrum (Zenodo 8060824, 30 Fourier bins)" — i.e., the HD correlation is the load-bearing assumption of the entire likelihood. The HD curve is from **Hellings, R. W. & Downs, G. W. 1983, ApJ 265, L39** ("Upper limits on the isotropic gravitational radiation background from pulsar timing analysis"). The 1983 paper is not optional — it defines the correlation pattern the KDE likelihood is built on. **Not cited anywhere.**
  - The §V framing references "combined PTA" (line 58 of CLAUDE.md / Paper 3 §6) — γ = 3.20 ± 0.42, bounce γ=3.0 at 0.48σ, SMBHB excluded ≳2σ — which is a combined NANOGrav 15-yr + EPTA DR2 + PPTA DR3 + InPTA result by standard PTA practice. **EPTA DR2 (Antoniadis et al. 2023, A&A 678, A50, arXiv:2306.16214)** is not in the bib. PPTA DR3 (Reardon et al. 2023, ApJL 951, L6, arXiv:2306.16215) and the IPTA combination paper are also absent.
- **What's wrong:**
  1. A foundational reference (Hellings-Downs 1983) for the HD likelihood pattern is missing.
  2. The other 2023 PTA detection-paper companions (EPTA DR2, PPTA DR3) — invoked by the "combined PTA" framing — are not cited.
  3. NANOGrav2023 alone is a single-array citation; "combined PTA" in §V requires multi-array citations or else the "combined" framing is hollow.
- **Manuscript-level consequence:** §V.A and §V are the headline PTA results sections of the paper. A PTA-literate referee will immediately ask "where's Hellings-Downs and where's the EPTA companion?" — these are not subtle omissions.
- **Fix:** Add three bibitems:
  ```
  \bibitem{HellingsDowns1983}
  R.\ W.\ Hellings and G.\ W.\ Downs,
  ``Upper limits on the isotropic gravitational radiation background from pulsar timing analysis,''
  Astrophys.\ J.\ \textbf{265}, L39 (1983).

  \bibitem{EPTA2023}
  J.\ Antoniadis \etal\ (EPTA Collaboration),
  ``The second data release from the European Pulsar Timing Array. III. Search for gravitational wave signals,''
  Astron.\ Astrophys.\ \textbf{678}, A50 (2023), arXiv:2306.16214.

  \bibitem{PPTA2023}
  D.\ J.\ Reardon \etal\ (PPTA),
  ``Search for an Isotropic Gravitational-wave Background with the Parkes Pulsar Timing Array,''
  Astrophys.\ J.\ Lett.\ \textbf{951}, L6 (2023), arXiv:2306.16215.
  ```
  Then cite `\cite{HellingsDowns1983}` at §V.A on the first invocation of "HD correlation", and `\cite{EPTA2023,PPTA2023}` at §V on the first invocation of "combined PTA".
- **Priority:** MAJOR. Omissions of this stature in a paper that headlines PTA results invite a referee rejection on coverage grounds alone.

---

## MINORs

### m1. `Wenger2000` SIMBAD page range gives only the start page

- **Location:** L1091–1094.
- **Claimed:** "Astron.\ Astrophys.\ Suppl.\ Ser.\ \textbf{143}, 9 (2000)."
- **Verified reality (ADS 2000A&AS..143....9W):** Wenger et al. 2000, A&AS 143, 9–22. Start page 9, end page 22.
- **Note:** Citing only the start page is consistent with revtex4-2 convention and IS the dominant style elsewhere in this bib. So this is NOT actionable as a bibitem fix unless the paper wants to standardize on full page ranges throughout. Flagged for awareness only — left as no-op.
- **Priority:** MINOR (effectively NIT). Skip unless a global page-range standardization sweep is being done anyway.

### m2. `LAMOST_DR10` bibitem is too thin to verify

- **Location:** L983–986.
- **Claimed:** "A.-L.\ Luo \etal, ``The LAMOST Data Release 10,'' \textit{Research in Astronomy and Astrophysics}, 2024."
- **Verified reality:** No paper titled exactly "The LAMOST Data Release 10" by A.-L. Luo et al. in RAA 2024 is unambiguously findable in a web search. The LAMOST DR10 release (11.4M spectra) is documented at the LAMOST DR10 portal but the canonical citable paper for DR10 itself is unclear; the conventional LAMOST cite is **Cui et al. 2012, RAA 12, 1197** (LAMOST instrument paper) plus a per-DR reference paper which for DR10 has not been published as a standalone release paper as far as I can find. Multiple 2024 RAA papers by A.-L. Luo's group use DR10 data but are not "the DR10 release paper".
- **Fix:** Either (a) replace with the LAMOST instrument paper (Cui et al. 2012) plus the LAMOST DR10 portal URL, or (b) add volume/page/article number to the current bibitem so it can be verified. Right now this is a referee-bait line.
- **Priority:** MINOR. Doesn't falsify a claim, but a referee asking "which RAA paper exactly?" will get no answer.

---

## NITs

### n1. `Nicolaou2026` bibitem and `Liang2023` may be referring to the same body of work

- **Location:** `Nicolaou2026` at L1033–1036, `Liang2023` at L1028–1031.
- **Note:** `Nicolaou2026` is cited as "C.\ Nicolaou \etal, ``Anomaly Detection in DESI Early Data Release Spectra with Astronomaly,'' MNRAS (2026, in press)" — and the search for DESI EDR anomaly detection turns up "Identifying Anomalous DESI Galaxy Spectra with a Variational Autoencoder" (arXiv:2506.17376, in press at MNRAS 547 stag010 / 2026). The first author of that 2026 MNRAS paper, however, is not clearly "C. Nicolaou" in the result listing (the result-set lists multiple co-authors). I could not independently verify the Nicolaou first-authorship.
- **Recommendation:** Cross-check Nicolaou2026 against arXiv:2506.17376; either confirm first-author or update to the correct first author + arXiv ID. Adding the arXiv ID to the bibitem (it's currently absent) would let any future reviewer self-verify in one click.
- **Priority:** NIT. Action-optional pending first-author verification.

---

## Counts

| Severity | Count |
|---|---|
| BLOCKER | 1 |
| MAJOR | 3 |
| MINOR | 2 |
| NIT | 1 |
| **TOTAL** | **7** |

## Most concerning citation error

The `Heinrich2023` bibitem (L1107–1110) gives the wrong journal — JCAP 2024, 074 instead of the actual Phys. Rev. D 109, 123511 (2024) — for arXiv:2311.13082, which is the load-bearing primary source the paper now leans on for the σ(f_NL)=0.7 SPHEREx multi-tracer Fisher forecast after the R41 cross-paper-cite removal. The prior R-round (SSOT "SSSSS" closure) harmonized the year (2023 → 2024) and updated the prose to "Heinrich \etal~2024" but did not touch the bibitem's journal venue, so a referee clicking through to verify the σ(f_NL) anchor will land on a journal/volume mismatch and mark the citation hygiene down.

## Sources

- [NANOGrav 15-yr: Agazie et al. 2023, ApJL 951, L8, arXiv:2306.16213](https://arxiv.org/abs/2306.16213)
- [Heinrich, Doré, Krause — Phys. Rev. D 109, 123511 (2024), arXiv:2311.13082](https://arxiv.org/abs/2311.13082) / [APS DOI](https://doi.org/10.1103/PhysRevD.109.123511)
- [SDSS DR18: Almeida et al. 2023, ApJS 267, 44](https://ui.adsabs.harvard.edu/abs/2023ApJS..267...44A/abstract)
- [eROSITA DR1: Merloni et al. 2024, A&A 682, A34](https://ui.adsabs.harvard.edu/abs/2024A&A...682A..34M/abstract)
- [Gaia DR3: Vallenari et al. 2023, A&A 674, A1, arXiv:2208.00211](https://arxiv.org/abs/2208.00211)
- [DESI DR1: DESI Collaboration 2025, arXiv:2503.14745](https://arxiv.org/abs/2503.14745)
- [Wilson-Ewing 2012/2013: JCAP 1303:026, arXiv:1211.6269](https://arxiv.org/abs/1211.6269)
- [Cai, Xue, Brandenberger, Zhang 2009: JCAP 0905:011, arXiv:0903.0631](https://arxiv.org/abs/0903.0631)
- [SIMBAD: Wenger et al. 2000, A&AS 143, 9–22](https://ui.adsabs.harvard.edu/abs/2000A&AS..143....9W/abstract)
- [Hellings & Downs 1983, ApJ 265, L39](https://ui.adsabs.harvard.edu/abs/1983ApJ...265L..39H/abstract)
- [Liang et al. 2023, "Outlier Detection in DESI BGS", arXiv:2307.07664](https://arxiv.org/abs/2307.07664)
- [Nicolaou-candidate VAE-DESI 2026: arXiv:2506.17376](https://arxiv.org/abs/2506.17376)
