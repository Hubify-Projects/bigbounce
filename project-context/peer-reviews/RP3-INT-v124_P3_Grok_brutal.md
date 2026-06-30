# P3 RP3-INT-v124 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=6ac11a96 pages=32
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 62.2s

---

**Referee Report**

**P3-E1 (ESSENTIAL, p. 6, Table I caption and footnote ¶)**  
Text: “revised in v3.1.122 so the body no longer displays superseded cross-transfer baselines”.  
Internal version-control language remains in the published manuscript. Required fix: remove every occurrence of version strings, “superseded”, “revised in”, and internal reconciliation footnotes.

**P3-E2 (ESSENTIAL, p. 1 abstract paragraph + p. 6 Table I)**  
Abstract states “269,317 Recommended-Tier (378,280 Total)”. Body shows the 269,317 figure mixes a validated core with 798 explicitly flagged exploratory objects whose per-object validity flags are required for any science use. The abstract therefore overstates the science-ready sample size. Required fix: state the validated subset (268,519) as the headline number and move the larger total to a clearly caveated secondary figure.

**P3-E3 (ESSENTIAL, p. 1 and p. 22)**  
Abstract and §V claim “no statistically significant improvement on \(f_{NL}\) bounds”. The quoted central value shifts from 8.98 to 8.14 (9.4 %). The paper never supplies the effect-size or practical-significance statement required by PRD policy for any \(\sigma\) or \(\chi^2\) headline. Required fix: add Cramér’s \(V\) or fractional amplitude for every such claim.

**P3-E4 (ESSENTIAL, p. 2 and p. 22)**  
Fisher forecast uses the empirically measured \(\alpha_{jk}=0.19\pm0.65\) (0.29\(\sigma\) from null) yet labels the 9.4 % shift a “central forecast”. The two statements are contradictory; the abstract claim is stronger than the body’s final calibrated statement. Required fix: replace the abstract sentence with the body’s exact wording.

**P3-M1 (MAJOR, throughout §§II–III)**  
Every survey-specific \(S\) threshold is defined on its own validation pool; absolute \(S\) values are therefore incommensurable. The paper repeatedly juxtaposes raw \(S>5\) counts without the mandatory “not directly comparable” qualifier at each comparison. Required fix: insert the qualifier at every cross-survey numerical comparison.

**P3-M2 (MAJOR, p. 3 Fig. 1 and p. 13 Fig. 4)**  
UMAP panels are presented as evidence that high-score anomalies occupy distinct islands. No quantitative cluster-validity metric (silhouette, Davies–Bouldin, etc.) is supplied; visual impression alone is used. Required fix: add at least one numeric validation statistic.

**P3-M3 (MAJOR, p. 32 length)**  
32-page manuscript whose primary deliverable is a catalog rather than a new methodological result. PRD methods papers of this type are routinely required to be \(\leq20\) pages. Required fix: condense to \(\leq20\) pages or justify the length.

**P3-M4 (MAJOR, p. 6 and p. 9)**  
Injection-recovery results are reported only for the final native-retrained models. The cross-transfer baseline that motivated the entire Path-C protocol is never re-tested with the same 5\(\sigma\) protocol. The central methodological claim therefore lacks its own control.

**P3-N1 (MINOR, p. 1)**  
“\(\geq268{,}519\)” and “269,317” appear in the same sentence without an explicit statement that the difference is the 798 exploratory objects. Minor clarification required.

**P3-N2 (MINOR, multiple tables)**  
Several footnotes contain parenthetical arithmetic (“\(275{,}151\to269{,}317\)”) that is never shown in the main text. Move to main text or delete.

**P3-NIT1–NIT4**  
Minor typographic inconsistencies (duplicate “canonical canonical-mask” phrasing on p. 6, inconsistent use of en-dash vs. hyphen in coordinate lists, axis-label font size in Fig. 7, missing units on one color-bar in Fig. 5).

**Summary recommendation**  
**REJECT**

The manuscript contains multiple instances of unretracted internal versioning language, headline numbers in the abstract that are not supported by the body’s final calibrated statements, and missing effect-size qualifiers on every \(\sigma\) claim. These are not cosmetic issues; they violate PRD’s standards for reproducibility and quantitative honesty. Until the internal-audit text is excised, the abstract–body mismatch is corrected, and every cross-survey numerical comparison carries an explicit incomparability warning, the paper cannot be considered for publication.