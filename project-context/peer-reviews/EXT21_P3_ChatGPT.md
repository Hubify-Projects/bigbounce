# EXT21 P3 ChatGPT — chat: https://chatgpt.com/c/6a3e4ecc-e154-83e8-9843-bd2b2001a801

Referee report — Paper P3, "Multi-survey anomaly catalog"

1. Recommendation: ACCEPT

The manuscript is suitable for publication without requiring further scientific rework. The paper is unusually transparent about validation failures, cross-transfer artifacts, score-axis provenance, catalog-tier caveats, and cosmological forecast limitations. The main catalogue claim is supported at the level expected for a large anomaly-detection data release, provided readers follow the paper's own tier flags and avoid treating every component as equally validated.

I find no blocker and no major issue requiring reanalysis. The remaining points are clarity and presentation improvements that would reduce the risk of misquotation.

2. BLOCKERS
None.

3. MAJORS
None.

4. MINORS

Abstract / Sec. VII — "catalog-grade" terminology could still confuse readers.
The manuscript says the recommended catalog-grade tier is 269,317 unique entries, but that 6-way subset includes eROSITA and Gaia, both of which are also described as exploratory or failing injection-recovery gates.
Fix: Replace "catalog-grade" with a more precise phrase such as "recommended non-LAMOST release subset with per-survey validation flags," or explicitly state that "catalog-grade" here means "deduplicated release tier, not uniformly validation-PASS across all surveys."

Sec. VI.B — SDSS discussion still reads partly like the cross-transfer catalogue is the operative SDSS result.
The section says the transfer-learning approach used for SDSS deliberately exploits model dependence and that the SDSS catalogue is not comparable to DESI. Elsewhere the paper clearly says Path-C native retraining supersedes the cross-transfer scan, with the 77,905-object native continuity slice, top-1% score-knee set, and strict S > 5 set separated.
Fix: Recast Sec. VI.B as explicitly describing the historical cross-transfer baseline and clarify that the released SDSS tier is native-rescored.

Sec. IV.B — Cramér's V numerical expression is visually easy to misread.
The text gives the correct value, approximately 0.0064, but the rendered equation/string places the square-rooted definition next to an unsquare-rooted numeric fraction.
Fix: Write the numeric expression explicitly as V = sqrt(376713 / (378280 * 24047)) = 0.0064.

Table I — the table is scientifically useful but overloaded.
The table footnotes contain essential information on threshold families, LAMOST exploratory status, eROSITA membership-only status, Planck map-patch bookkeeping, and SDSS threshold variants. This is accurate but difficult to parse.
Fix: Add a short "catalog tier summary" table with rows: survey, released count, validation status, score-axis status, recommended downstream use.

Sec. III.E / Data availability — eROSITA membership-only framing should be mirrored in every release-facing sentence.
The text correctly explains that the eROSITA score axis is irreproducible and the reproducible product is the membership list. However, the Data Availability section still lists per-object scores generally before giving exceptions.
Fix: Put the exception first or include a compact schema sentence: "eROSITA has membership/rank only; no reproducible score column is released."

Sec. V / Appendix C — keep the two Fisher normalizations clearly separated.
The manuscript already warns that Appendix C's σ(fNL)=16.85 normalization differs from the Sec. V σ(fNL)=8.98 baseline. Because this is easy to misquote, the warning should also appear near any abstract/conclusion mention of the fixed-α reference.
Fix: Add one parenthetical in the Conclusions: "Appendix C uses a separate internal normalization; only relative changes are comparable."

Fig. 8 caption — display scores versus catalogue scores.
The caption does a good job disclosing that some burned-in values are display values, not catalogue-pipeline scores. This point is important enough that it should also be in the figure panel labels or abbreviated in the main text when the three DESI×SDSS matches are introduced.
Fix: Rename the labels to "display score" directly in the figure where possible.

Sec. IV.A — novelty fraction scope should be repeated in the Conclusions.
The manuscript properly states that 17.8% is a DESI top-1,000 score-stratum estimate, not a full-catalog rate. The Conclusions mention this, but the wording could be made even harder to misuse.
Fix: Add: "No full-catalog novelty fraction is claimed."

5. Strengths

- Strong transparency and provenance discipline. The manuscript repeatedly distinguishes native-retrained Path-C results from cross-transfer baselines, labels ACT as quarantined, treats eROSITA as membership-only, and separates Planck map patches from point-source objects.

- Scientifically responsible treatment of failure modes. The LAMOST blue-excess artifact, Gaia/eROSITA injection-recovery failures, NEOWISE mask geometry pass-by-construction, and SDSS cross-transfer inflation are not hidden; they are used as methodological lessons.

- Good validation architecture for the main DESI tier. The DESI 5-fold Jaccard stability, production-vs-control OOD Jaccard, top-200 visual inspection, science-class recount, and explicit non-primary-target dominance disclosure materially improve the credibility of the headline DESI component.

- Useful catalog stratification. The paper gives downstream users enough information to choose the 378,080 point-source tier, the 269,117 recommended point-source subset, or stricter survey-specific tiers depending on use case.

- Careful handling of cosmological applications. The fNL and NANOGrav sections are appropriately framed as illustrative or conditional. The paper avoids claiming a current multi-tracer detection and explicitly notes the SMBHB environmental caveat.

- Figures and tables are informative. The UMAP embeddings, DESI spatial map, SDSS cross-transfer cluster figure, DESI×SDSS spectral pairs, injection-recovery plot, and taxonomy image gallery all add useful diagnostic context rather than merely decorating the paper.

Overall assessment

This is a strong, publishable data-release and methodology paper. Its main contribution is not just the anomaly catalogue size, but the explicit demonstration that native retraining, tier flags, and provenance audits are mandatory for multi-survey anomaly detection at scale. The remaining issues are primarily wording safeguards against overinterpretation. I recommend ACCEPT.
