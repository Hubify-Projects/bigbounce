# EXT16 P3 ChatGPT — Referee Report

- Round: EXT16
- Paper: P3
- Provider: ChatGPT Pro Extended (Big Bounce Book project)
- URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc617-2480-83e8-bf48-cc78a7bce891
- Harvested: 2026-06-13 PST

## Verdict: MINOR REVISIONS

## Report Text

EXT16 focused delta review, Paper 3 v3.1.110
Summary

The EXT15 closure improves Table IX substantially. The fiducial Savage–Dickey calculation is now explicit and reproducible from the printed numbers: at γ
∗
	​

=3.0, the Gaussian KDE posterior density is given as 0.461 and the flat-prior density under γ∈[0,7] is 1/7=0.1429, giving B
MB/free
	​

=3.23; at γ
∗
	​

=4.33, the posterior density is 6.46×10
−5
, giving B
SMBHB/free
	​

=4.52×10
−4
; hence B
MB/SMBHB
	​

=7.14×10
3
. That resolves my previous concern about whether the headline value was a tail fraction or a genuine density ratio. 

paper3_anomaly_catalog_v3.1.110

However, the prior-sensitivity rows in Table IX still need a local definition/caption correction. This is not a request for new catalogue analysis and does not affect the main anomaly-catalog result. I therefore do not recommend major revisions. I would accept after this one local statistical-table correction.

Required minor revision
1. Table IX: clarify or correct the non-fiducial prior-sensitivity rows

Location: Appendix E, Table IX.

Issue: The fiducial [0,7] row is now clear. The remaining rows are still not fully consistent with the table’s stated definition. The caption says the flat prior is over the stated range, and the tablenote defines B=p(γ
∗
	​

∣data)/p(γ
∗
	​

∣prior). But the explanatory note then uses p(γ
∗
	​

∣prior)=1/7, i.e. the fiducial prior density, while the table also reports [0,5], [1,6], and [2,5] rows. 

paper3_anomaly_catalog_v3.1.110

Under the standard Savage–Dickey convention, if the prior range is changed to [0,5], the flat prior density at γ
∗
	​

 is 1/5, not 1/7; for [2,5], it is 1/3. If the posterior density at γ=3.0 is nearly unchanged, B
MB/free
	​

 should scale with the prior width rather than remain fixed at ≃3.23. Conversely, for the fixed-model ratio B
MB/SMBHB
	​

, the common prior-density factor should largely cancel when both fixed γ values are inside the tested prior range. The printed explanation instead says B
MB/free
	​

 is prior-stable while B
MB/SMBHB
	​

 inherits strong prior-width sensitivity, which is not the standard Savage–Dickey behavior without an additional estimator convention. 

paper3_anomaly_catalog_v3.1.110

Proposed fix: Either:

keep only the [0,7] fiducial Savage–Dickey row and move the other rows to a clearly labelled “posterior-tail / KDE-truncation sensitivity diagnostic”; or

recompute each row with the row-specific prior density 1/(γ
max
	​

−γ
min
	​

) and print the corresponding posterior KDE density used for that row; or

define the special reweighting/truncation estimator that produces the present non-fiducial rows and avoid describing those rows as standard Savage–Dickey Bayes factors.

This is a narrow local correction. It does not require rerunning the MCMC if the table is relabelled or if the row-specific densities are already available.

Items closed since EXT14/EXT15

DESI validation-gate wording is closed.
The abstract now correctly states that DESI robustness rests on 5-fold cross-validation Jaccard and native-retrain OOD Jaccard, not on a DESI injection-recovery test. It also separately reports the six injection-recovery gates, with SDSS, Planck, and NEOWISE passing and LAMOST, Gaia, and eROSITA failing diagnostically. 

paper3_anomaly_catalog_v3.1.110

DESI headline threshold wording is closed.
The manuscript now describes the DESI count as an S>5 fixed-threshold selection, 195,829 anomalies, corresponding to 0.87% of the 22.5M-spectrum stream, and it preserves the important like-for-like science-target comparison against the Liang et al. benchmark. 

paper3_anomaly_catalog_v3.1.110

Catalogue arithmetic remains correct.
The Path-C per-survey native counts sum to 388,493; the 7-way 5″ deduplication collapses 10,213 duplicate detections, giving 378,280 unique entries. The table also continues to distinguish 378,080 point-source detections from the 200 Planck CMB map-patch regions. 

paper3_anomaly_catalog_v3.1.110

Fiducial NANOGrav Bayes factor is now explicit.
The [0,7] row gives a transparent Savage–Dickey density-ratio computation using the printed KDE densities and prior density. My remaining concern is only about the non-fiducial prior-sensitivity rows, not the fiducial headline calculation. 

paper3_anomaly_catalog_v3.1.110

Production condition

The data availability section still uses future-tense release language: the HuggingFace dataset is staged, will be made public with arXiv posting, and a Zenodo DOI will be minted at submission. This remains a publication-production condition rather than a scientific revision. The live DOI and frozen release manifest should be inserted before journal publication. 

paper3_anomaly_catalog_v3.1.110

New issues introduced by EXT15 closure

No new scientific issue was introduced. The added KDE-density footnote is useful; it simply exposes that the fiducial row is now clear while the non-fiducial prior-sensitivity rows still need a precise definitio
