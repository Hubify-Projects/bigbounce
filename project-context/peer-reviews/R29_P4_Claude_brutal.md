# P4 R29 — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7 (in-session)`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/site/public/papers/chirality_catalog_paper_v172.pdf` md5=f6c1f145 pages=22
**Input format**: NATIVE PDF (document block) + extended thinking 16K
**Wall time**: in-session (API leg 413 fallback)

---

## Brutal-honesty PRD referee report — Paper 4 v1.0.172 (post-EXT1 closure)

PRD referee, full read, no cap. Sweeps 1–14 plus upgraded sweeps 15 (abstract-last drift), 16 (provenance), 17 (uncomputed claims), 18 (standalone-reader), 19 (effect sizes). Findings labeled with P4-E1-style IDs, ESSENTIAL/MAJOR/MINOR/NIT severity, reference line/section, exact quote, and concrete fix.

---

## Verifications completed (in-session, no API)

- `git log -1 --format=%h pipelines/p2_chirality/chirality_catalog_paper.tex` → `0ce3d47c` (HEAD touch). Cited stamp `7c03bb64` is a valid ancestor and IS the v1.0.172 EXT1 stamp commit. ✓
- `python3 tools/artifact_crosscheck.py pipelines/p2_chirality/chirality_catalog_paper.tex` → PASS 0 problems, 12/12 artifact paths resolve, single WARN on commit-vs-HEAD drift (see E03 below).
- Training-count arithmetic (sweep 17): `21,293 + 5,323 = 26,616` ✓ matches the stated post-augmentation pool. Source manifest = 25,790 (6,637 + 17,153 + 2,000), augmented pool = 26,616, difference = 826, matches "the 826-image difference between the source manifest and the training pool" exactly. **Internally consistent.**
- Grep for stale `f_sky_canonical` → 0 hits. Renamed artifact field `mask_restricted_normalization_factor` not stale.
- Three significance conventions (Sec. III.A): real-space moment-$z$/rank-$p$ pair (used Sec. IV.A); MASTER $\ell\!=\!1$ moment-$z$ (used Sec. IV.B, Table III); block-bootstrap $z$ (used Sec. IV.E, Table V). All three are used downstream consistently with the declaration. ✓
- Post-MASTER monopole-only null paragraph ($\sigma\!=\!+4.84$, ~12% reproduction) is in §IV.D at line 417, cited from Table IV caption "This is a pre-MASTER diagnostic only". ✓
- NS gallery (`fig_gallery_notspi.png`): symlink present on disk, **never embedded in tex** — see ESSENTIAL E02.

---

## ESSENTIAL

### P4-R29-E01 — Brittle single-block-scale headline exclusion (z≈−18.1)

**Section**: §IV.E / Appendix D (Joint nuisance-marginalized WLS fit, lines 640–664, footnote at lines 640–641).
**Severity**: ESSENTIAL.
**Quote**: "The NSIDE$\,=\,$8 choice is therefore the natural block scale for this systematic family. **No sensitivity test at alternative NSIDE values has been computed**; a block-scale sensitivity check at NSIDE$\,\in\!\{4,8,16\}$ is a recommended follow-up validation."
**Brutal verdict**: The headline harmonic-channel exclusion ($z\!\approx\!-18.1$) and the abstract's "block-bootstrap WLS template fit disfavors a clean cosmological dipole at the 1.7% reference amplitude at $z\approx-18$" both rest on a *single* block scale (NSIDE=8, ~7° super-pixels). The footnote concedes alternative scales were not tried. The analytic argument that NSIDE=8 sits between the PSF coherence length (~3°) and the leg-boundary scale (~5–10°) is plausible but textual, not numerical — and the inflation factor moves $\sigma$ by 14.7× already at this single scale. A naive doubling of the block radius could plausibly push $\sigma_{\rm boot}$ to $\sim\!3\times10^{-3}$, halving the headline exclusion to $z\!\sim\!-10$ — still strong, but the *quoted* value $-18$ is not robustness-tested. For a PRD-level headline statistic this is an open methodological gap.
**Fix**: Compute the block-bootstrap covariance at NSIDE $\in\{4,8,16\}$ (or, given the NSIDE=4 super-pixel deficiency, at NSIDE=8 plus two intermediate radii via spherical-cap blocks). Report the inflation factor and headline $z$ at each scale. If the headline survives ($|z|\!\geq\!10$ across all scales), the result hardens; if it collapses at NSIDE=4-equivalent scale, the abstract claim must be re-quoted with an interval or with the most conservative value. Pattern-016 (single-knob headline) applies.

### P4-R29-E02 — NS gallery figure referenced in EXT1 closure brief but not embedded in paper

**Section**: §II.A figure block (lines 105–126); files `fig_gallery_cw.png`, `fig_gallery_ccw.png` embedded, `fig_gallery_notspi.png` present on disk (symlink to `figs/fig_gallery_notspi.png`) but never `\includegraphics`'d.
**Severity**: ESSENTIAL (closure-claim consistency).
**Quote (from R29 brief)**: "NS gallery caption now 'edge-on'".
**Quote (paper, Fig.1 caption)**: "Representative high-confidence galaxies from the classified spiral sub-catalog … Left: clockwise (CW); right: counter-clockwise (CCW)." — no NS panel exists.
**Brutal verdict**: The closure brief implies an EXT1 action item was to (re-)caption the NS gallery as "edge-on" to disambiguate the NS class from a pure non-spiral class. Either (a) the figure was supposed to be added in v1.0.172 and was not, leaving a closure gap, or (b) the figure was deliberately omitted because the journal-condensation cut it (cf. CLAUDE.md header line 3: "CONDENSED VERSION v1.0.155 — cut from 54pp to ≤25pp"), in which case the closure log is wrong. Either way the closure ledger and the paper do not match. The NS-class composition (62.23% of the catalog, "NS/edge-on / morphologically indeterminate", line 249) is load-bearing for the catalog claim and a reader cannot inspect what an NS exemplar looks like.
**Fix**: Either (i) add a 3rd panel to Fig.1 with `\includegraphics{fig_gallery_notspi.png}` and caption "non-spiral / edge-on / morphologically indeterminate", or (ii) annotate the closure ledger that the figure is intentionally deferred to the catalog data release page. Choose one; the current state is internally inconsistent.

### P4-R29-E03 — Data Availability hash artifact_crosscheck WARN: stale at HEAD

**Section**: §Data Availability (line 690).
**Severity**: ESSENTIAL (provenance gate, sweep 16).
**Quote**: "Repository state for this version: commit \texttt{7c03bb64} (v1.0.172, June 2026); headline sample is HC-broad $N=949{,}584$ ($p_{\rm eq}>0.6$) spirals at this snapshot."
**Brutal verdict**: `python3 tools/artifact_crosscheck.py pipelines/p2_chirality/chirality_catalog_paper.tex` reports `WARN-OLD-COMMIT 7c03bb64: valid ancestor but not HEAD (377316d9) — update at restamp`. The verdict is *correct* in principle — the cited commit `7c03bb64` IS the v1.0.172 stamp commit (verified: `git log -1 --format=%H 7c03bb64 → feat(P4 v1.0.172): EXT1 closure wave`), and the subsequent `0ce3d47c` commit's own message ("fix(P4): pin Data Availability hash to v1.0.172 stamp commit") deliberately pinned the hash to the *stamp* commit, not to itself or to HEAD. So the cite is provenance-correct, but the cross-check tool flags it because HEAD has moved (now `377316d9`, the EXT1 6-paper BUMP_BUNDLE). Per the R29 brief, the provenance gate REQUIRES the hash to equal the v1.0.172 stamp commit — it does. **Pass on substance, but the WARN must not be ignored at next restamp**: if any P4 edit between `7c03bb64` and HEAD touched paper-bearing files or reproducibility code, the cited hash is stale even though it matches the stamp. `git log 7c03bb64..HEAD -- pipelines/p2_chirality/ research/` is the gate query.
**Fix**: Either (a) accept the warning as expected (the pin policy holds the cite at the stamp commit and HEAD will always drift forward — document this in the closure ledger so the WARN is a known false positive), or (b) re-pin at every restamp to the current stamp commit, in which case the cite would advance to the next stamp on the next bump.

### P4-R29-E04 — Two distinct meanings of "$+3.64\sigmaunit$" still coexist; reader trip-hazard

**Section**: Abstract (line 77), §IV.B (line 351), §IV.D (line 417), §VI Conclusions (line 494), Table I row (iii) (line 172), Table III caption (line 354).
**Severity**: ESSENTIAL (post-EXT1 verification).
**Quote (abstract, new EXT1 parenthetical)**: "(The $+3.64\sigmaunit$ value is from a 500-MC direct run on the canonical unapodized mask; the $10^4$-permutation canonical unapodized row in Table~III gives $+7.93\sigmaunit$; both are systematics-attributed diagnostics from different null-run sizes, not two independent detection claims.)"
**Brutal verdict**: The EXT1 closure correctly disambiguated 500-MC ($z\!=\!+3.64$, $p_{\rm MC}\!=\!0.030$, Gaussian-equiv ${\approx}1.9\sigmaunit$) from $10^4$-MC ($z\!=\!+7.93$, $p\!=\!3\!\times\!10^{-4}$) for the *same physical estimator and footprint*. The pair is mathematically reconcilable: the 500-MC null underestimates the upper tail because $1/500\!=\!2\!\times\!10^{-3}$ is the floor, and the heavy-tailed permutation null pulls the moment-$z$ upward at higher $N_{\rm MC}$. But the manuscript still propagates "$+3.64\sigmaunit$" as the canonical-mask headline in four prominent places (abstract, conclusions §VI Headline finding, conclusions §VI Canonical-N direct compute, Table I row iii) while Table III's $10^4$ run gives $+7.93\sigmaunit$. A casual reader will conclude the canonical-mask channel residual has dropped from 7.93σ to 3.64σ between two reductions on the same data. The mismatch is not a defect, but the resolution is buried in a single abstract parenthetical and a Table III caption sentence. The Conclusions paragraph "Canonical-$N$ MASTER $\ell=1$ direct compute" still quotes only $+3.64\sigmaunit$ without the $+7.93\sigmaunit$ cross-reference.
**Fix**: Either (a) demote $+3.64$ to "(500-MC direct run; see Table III for the $10^4$-permutation recompute at $z=+7.93$)" in §VI Conclusions and in Table I row (iii) caption, or (b) promote $+7.93$ to the headline canonical-mask value and relegate $+3.64$ to the leakage-comparison context where the Gaussian-equivalent matters. Currently the two coexist without a single in-text identity statement (they describe the same field/mask, just different $N_{\rm MC}$).

---

## MAJOR

### P4-R29-M01 — Falsification criterion conflates two different injection conventions

**Section**: Abstract (line 77), §VI Conclusions §"Sensitivity convention" (lines 502–503), §V.A Empirical injection-recovery (line 459).
**Severity**: MAJOR.
**Quote (abstract)**: "Falsification criterion: a future $\ge\!5\sigmaunit$ detection at amplitude $A \gtrsim A_{95}$, where injection–recovery brackets $A_{95}$ between $1.0\%$ and $1.5\%$ ($A_{50}\approx0.75\%$), would be in tension with the present null. **These thresholds are estimator-specific to the real-space dipole**; the harmonic-channel completeness ($P(\geq\!3\sigmaunit)\!\geq\!0.999$ at $A_p\!=\!0.75\%$) is a separate diagnostic property…"
**Brutal verdict**: The EXT1 closure explicitly added the "estimator-specific" disclaimer — good. But the falsification *amplitude scale itself* is still ambiguous: the injection-recovery sweep in §V.A defines $A$ via $p_{\rm CW}(\hat n) = p_{\rm CW}^{\rm global} + (A/2)\cos\theta$, i.e., $A$ is the *full-amplitude* dipole. The Shamir comparison uses $\sim\!3\%$ asymmetry (likely the same convention). But the WLS template fit (Appendix D) uses $A_{\rm ref}\!=\!0.034$ in $A_p$ units (line 640), which the paper notes "$0.23\%$ in $f_{\rm CW}$ units" — i.e., the $1.7\%$ in $f_{\rm CW}$ units is 1.7% in $f_{\rm CW}$-deviation units = $A_p\!=\!0.034$ in $A_p$ units. So the WLS reference amplitude is $A\!=\!3.4\%$ in the *full-amplitude* convention. **The falsification threshold $A_{95}\in(1.0\%,1.5\%]$ and the WLS reference $1.7\%$ are in different conventions** by a factor of 2 — $1.7\%$ in $f_{\rm CW}$ units = $3.4\%$ in full-amplitude units. The abstract and §VI both quote "$1.7\%$" without specifying which.
**Fix**: Add the unit clarifier explicitly: "block-bootstrap WLS template fit disfavors a clean cosmological dipole at the $1.7\%$ ($f_{\rm CW}$-deviation; equivalently $A_p\!=\!3.4\%$ in the full-amplitude convention of the injection-recovery sweep) reference amplitude". The current text relies on the reader having internalized Eq.~\ref{eq:ap_def} and the $A_p\!=\!2(f_{\rm CW}-\tfrac12)$ identity, which is documented but easy to miss.

### P4-R29-M02 — Table III canonical unapodized $+7.93\sigmaunit$ vs §IV.B $+7.31$ vs single-mode $+7.28$ — three distinct values within one section

**Section**: Table III rows (apod. $\ell=1$: $+7.31$, canonical unapod. $\ell=1$: $+7.93$); §IV.B narrative (line 351, $+7.28$).
**Severity**: MAJOR.
**Quote (§IV.B)**: "$C_1^{\rm meas}=2.348\!\times\!10^{-5}$ against a 500-MC per-galaxy label-shuffle null with mean $1.71\!\times\!10^{-6}$ and $\sigma_{\rm null}=2.99\!\times\!10^{-6}$, i.e.\ $+7.28\sigmaunit$ for $W_p\!=\!N_{\rm all}$ … the $10^4$-permutation recompute (Table~\ref{tab:multipole}) confirms this channel at $z=+7.31$"
**Quote (Table III, canonical unapodized $\ell=1$ row)**: "$z=+7.93$"
**Brutal verdict**: Three distinct numerical values ($+7.28$, $+7.31$, $+7.93$) coexist for ostensibly nearby quantities. The paper *does* explain this: $+7.28$ is the 500-MC single-mode apodized result; $+7.31$ is the $10^4$-permutation apodized result (Table III row 1); $+7.93$ is the $10^4$-permutation *canonical unapodized* result (Table III row 7). The 500-MC vs $10^4$ shift from $+7.28$ to $+7.31$ is plausible. The apod-vs-unapod shift from $+7.31$ to $+7.93$ is consistent with the apodization smoothing the high-$\ell$ edge response. But these three values are scattered across the section and a careful reader needs to triangulate fields, footprints, weights, and $N_{\rm MC}$ to keep them straight. The Table III caption tries to help ("single-multipole bin, … not a bandpower over a range") but does not explicitly map $+7.28 \to +7.31 \to +7.93$ as a sequence of well-controlled methodological shifts.
**Fix**: Add a short transition sentence in §IV.B right after the $+7.28/+7.31$ pair: "The corresponding canonical *unapodized* binary-weight result is Table III row 7, $z\!=\!+7.93$; the apod-vs-unapod gap of $\Delta z\!\approx\!0.6$ is attributable to the apodization's reduced effective sky fraction ($f_{\rm sky}^{\rm eff}\!=\!0.452$ vs.\ $0.49005$, Table II)." This collapses three pages of cross-referencing into one sentence.

### P4-R29-M03 — Standalone-reader sweep: paper is publishable but reader cannot reconstruct withdrawn-result audit from the paper alone

**Section**: Abstract (line 77), Appendix A §"Provenance note: withdrawn subsample-mask null" (lines 540–541).
**Severity**: MAJOR (sweep 18).
**Quote (Appendix A)**: "An earlier version of this paper reported a $-0.122\sigmaunit$ MASTER $\ell=1$ null on a putative 'strict-superset subsample mask' ($n=5{,}547{,}858$, $f_{\rm sky}=0.659$). A subsequent provenance audit found that this number was produced by a script that was not part of the version-controlled analysis pipeline, operating on a *synthetic* catalog…"
**Brutal verdict**: The disclosure is admirable and at PRD level it is the right call — most journals would have buried this. But a referee asks: was the synthetic catalog ever publicly released? If yes, anyone with the old draft can re-derive a $-0.122\sigmaunit$ result that no longer matches the production catalog. The audit log is referenced ("dated audit log") but not given as a citable artifact ("catalogued in the repository README" — informal). The withdrawn result is itself a teaching moment about catalog provenance and would benefit from at least the audit-log filename or a Zenodo DOI. **The paper currently relies on "trust the README"** for the most fragile part of its provenance story.
**Fix**: Add an explicit artifact link in the Provenance note paragraph: `\artifact{<path-to-audit-log>}` for the dated audit log, and a one-line statement of what *exactly* triggered the audit (Houston-noticed discrepancy? automated CI catch? external reviewer query?). The current "subsequent provenance audit found" is passive-voice and uninformative.

### P4-R29-M04 — Table II $f_{\rm sky}$ rounding: 0.494 quoted in three places but 0.488 (apodized footprint binary $C^2 2^\circ$) is the actual NaMaster-active value

**Section**: Table II (lines 524–537), Fig. 5 caption (line 264), §V "MASTER decoupling" config.
**Severity**: MAJOR.
**Quote (Table II)**: "Footprint ($N_{\rm all}\!\ge\!1$) | binary, none | $0.494$" and "Footprint | binary, $C^2$ $2^\circ$ | $0.488$" and "Footprint | $W_p\!=\!N_{\rm all}$, $C^2$ $2^\circ$ | $0.452$".
**Quote (§IV.B, line 351)**: "the real analysis footprint ($N_{\rm all}\!\geq\!1$; $24{,}297$ pixels, $f_{\rm sky}=0.494$, $C^2$ $2^\circ$ apodization, depth weight $W_p$)"
**Brutal verdict**: §IV.B asserts $f_{\rm sky}\!=\!0.494$ for a configuration that also has $C^2$ $2^\circ$ apodization and $W_p\!=\!N_{\rm all}$ depth weight. Per Table II, the *correct* $f_{\rm sky}^{\rm eff}$ for that *exact* configuration is $0.452$, not $0.494$. The $0.494$ value is the binary-footprint geometric pixel fraction; the $0.488$ value is binary + apodized; the $0.452$ value is the apodized + depth-weighted-eff. Same issue in Fig. 5 caption: "$N_{\rm all}\!\geq\!1$ analysis footprint ($f_{\rm sky}\!=\!0.494$) is used for the apodized MASTER diagnostic" — but the apodized MASTER diagnostic uses the $W_p\!=\!N_{\rm all}$ weight, which has $f_{\rm sky}^{\rm eff}\!=\!0.452$. The paper *does* footnote Table I row (iv) with the $f_{\rm sky}^{\rm eff}\!=\!0.452$ correction, so the authors know about it — but two of the three textual recapitulations still use the geometric $0.494$.
**Fix**: In §IV.B and Fig. 5, write either "$f_{\rm sky}\!=\!0.494$ (binary; $f_{\rm sky}^{\rm eff}\!=\!0.452$ under the $W_p\!=\!N_{\rm all}$, $C^2$ $2^\circ$ configuration; Table II)" or just quote the effective value directly. Currently the geometric and effective values are used interchangeably depending on which paragraph you read.

### P4-R29-M05 — Effect-size honesty: abstract presents $z\!\approx\!-18$ as a headline exclusion, but the cosmological reader cannot tell from the abstract that the *block-bootstrap covariance* is what's load-bearing

**Section**: Abstract (line 77).
**Severity**: MAJOR (sweep 19).
**Quote**: "a block-bootstrap WLS template fit disfavors a clean cosmological dipole at the $1.7\%$ reference amplitude at $z\approx-18$ (Appendix~D)."
**Brutal verdict**: $z\!=\!-18$ is the *block-bootstrap* value. The *naive WLS* value is $z\!=\!-264$ (Table V footnote). The 14.7× covariance inflation is the entire methodological story — without spatial-coherence correction the paper would have an arguably-impossible $-264\sigmaunit$ exclusion. The abstract elides this and quotes $-18$ as if it were a directly-measured Gaussian-tail number. **PRD referees will ask: "$-18$ in what null distribution?"** The block-bootstrap null is heavy-tailed, and the paper's own text explicitly disclaims directly mapping the moment-$z$ to a Gaussian tail probability for other estimators (Sec. III.A, "they do not follow the Gaussian $z\!\to\!p$ mapping"). The same caveat should apply here.
**Fix**: Add a parenthetical to the abstract: "(block-bootstrap moment-$z$, not a Gaussian tail probability; naive WLS gives $z\!\approx\!-264$, which is superseded by the spatial-coherence-corrected bootstrap covariance — Appendix~D, Table V)". Or, more honestly: drop the $z\!\approx\!-18$ headline number from the abstract entirely and use a qualitative "strongly disfavored under spatial-coherence-corrected covariance" — the precise number is hard to defend in a Gaussian frame.

---

## MINOR

### P4-R29-N01 — T7 bias-test threshold in Table VIII does not match the implemented criterion in the §B.3 narrative

**Section**: Table VIII (lines 562–578), Appendix B narrative (line 560).
**Severity**: MINOR.
**Quote (Table VIII row T7)**: "T7: Calibration proxy | $>30\%$ at $\max p\!>\!0.9$ | $73.6\%$"
**Quote (§B.3 narrative)**: "The implemented T7 criterion is: $>\!30\%$ of predictions at $\max p\!>\!0.9$ (a confidence-mass sanity check), **together with the requirement that the flip-swap error of high-confidence ($\max p\!>\!0.9$) predictions be lower than that of low-confidence ($\max p\!<\!0.7$) predictions**".
**Brutal verdict**: Two-part criterion in text, single part in table. The table is incomplete. A subsequent reader auditing Table VIII against the bias-hardening suite will not know about the flip-swap-error monotonicity sub-condition. Worse, the narrative immediately notes that "restricted to equivariant-class spirals only the mean ordering inverts" — meaning T7 passes on the *full* sample but fails on the *spiral subsample*. This nuance is invisible in Table VIII.
**Fix**: Add a Table VIII footnote: "T7 is a two-part criterion: (a) $>\!30\%$ HC mass (passes at $73.6\%$); (b) HC mean flip-swap error $<$ LC mean flip-swap error (passes on all-class evaluation; spiral-subsample-only evaluation inverts, see Appendix B narrative)."

### P4-R29-N02 — Bibliography ordering: bibitems are bibstyle-sorted, not "by first citation" as the comment claims

**Section**: Bibliography (line 715 onward).
**Severity**: MINOR.
**Quote (bib comment, line 715)**: "% Bibliography sorted by order of first citation."
**Brutal verdict**: The bib opens with `Shamir:2020` then `Shamir:2022` then `Shamir:2012` then `Shamir:2022DESI`. The text first-citation order is `Shamir:2012` → `Shamir:2020` → `Shamir:2022` → `Shamir:2022DESI` (Sec. I, line 92). The bib is therefore NOT in first-citation order — it's alphabetical-by-year-within-author or some hybrid. The comment is wrong.
**Fix**: Either (a) reorder the bib to match the comment (rearrange so `Shamir:2012` is first), or (b) delete the misleading comment. revtex4-2's default `\bibitem`-explicit bibliography requires manual ordering; the comment as written is an assertion that doesn't hold.

### P4-R29-N03 — `\bibitem{Zonca:2019}` is missing the article title

**Section**: Bibliography line 891–893.
**Severity**: MINOR (sweep 18).
**Quote**: "\bibitem{Zonca:2019}\\ A.~Zonca, L.~Singer, D.~Lenz \textit{et~al.},\\ J.\ Open Source Softw.\ \textbf{4}, 1298 (2019)."
**Brutal verdict**: No paper title given. Other bibitems all carry titles. Inconsistent, and a reviewer cross-checking citations will flag this.
**Fix**: Add the title: "``healpy: equal area pixelization and spherical harmonics transforms for data on the sphere in Python.''"

### P4-R29-N04 — `\bibitem{Paszke:2019}` and `\bibitem{McKinney:2010}` also drop titles; same fix

**Section**: Bibliography lines 899–907.
**Severity**: MINOR.
**Brutal verdict**: Same pattern as N03 — these conference/proceedings citations omit titles whereas all other bibitems include them. Inconsistent.
**Fix**: Add titles for both: "Data Structures for Statistical Computing in Python" (McKinney), "PyTorch: An Imperative Style, High-Performance Deep Learning Library" (Paszke).

### P4-R29-N05 — `\bibitem{Harris:2020}` drops the title and uses a bare `Nature` cite

**Section**: Bibliography line 895–897.
**Severity**: MINOR.
**Fix**: "Array programming with NumPy".

### P4-R29-N06 — Notation §III.A "moment-$z$" definition uses verbal mean/width but never gives the symbolic formula in the same place

**Section**: §III.A (line 144).
**Severity**: MINOR.
**Quote**: "All significance values $z$ are moment-ratios $(x - \langle x\rangle_{\rm null})/\sigma_{\rm null}$ against the null distribution specified per result."
**Brutal verdict**: The formula IS given here — re-reading, this is actually fine. WITHDRAWN. (Internal cross-check satisfied.)

### P4-R29-N07 — §IV.A correction-note text inside body is long; should be a footnote

**Section**: §IV.A (line 326).
**Severity**: MINOR.
**Quote**: "[Correction note: an earlier version printed $0.43\sigmaunit$ ($p=0.30$) from a $10^3$-realization run whose committed generator was later found to carry a selection-filter defect (it selected only CW-confident galaxies); the generator was repaired and the anchor regenerated from the released catalog at $10^4$ realizations…]"
**Brutal verdict**: This is a 75-word parenthetical inside the headline-result paragraph. It's important provenance but breaks the reading flow of the headline. A footnote would work better and is conventional in PRD.
**Fix**: Convert the bracketed correction note to `\footnote{…}`.

### P4-R29-N08 — Sec. III.B (Declared Analysis Hierarchy) primary estimator (ii) says "$z\!\approx\!-18$" but does not specify the convention; sec. III.A had just defined a "block-bootstrap $z$" convention

**Section**: §III.B (line 156).
**Severity**: MINOR.
**Brutal verdict**: Pre-EXT1 closure this would have been ambiguous; post-EXT1 the "Notation and Significance Conventions" subsection (III.A) explicitly lists "Block-bootstrap $z$: $(A_{\rm dipole}^{\rm best} - A_{\rm ref})/\sigma_{\rm boot}$ with spatial-coherence-corrected $\sigma_{\rm boot}$; the $z\!\approx\!-18.1$ headline exclusion uses this convention only." So the convention IS declared. Good. But §III.B's primary-estimator (ii) bullet does not back-reference §III.A's convention enumeration. A reader skimming §III.B will see "$z\!\approx\!-18$" without context.
**Fix**: Add inline back-ref "(block-bootstrap $z$ convention, §III.A)" to the §III.B (ii) bullet.

### P4-R29-N09 — Sec. IV.A "$N=949{,}584$" appears 5+ times; would benefit from a shared symbol

**Section**: Sec. I, III.B, IV.A, IV.E, V.A.
**Severity**: MINOR/NIT.
**Brutal verdict**: The HC-broad sample size $N=949{,}584$ at $p_{\rm eq}\!>\!0.6$ is the headline-sample number. It is repeated five+ times throughout the paper. A defined shortcut (e.g., `\newcommand{\NHC}{949{,}584}` or `$N_{\rm HC}$`) would (a) prevent drift if the number ever needs a recompute, (b) shorten future revision diffs.
**Fix**: Optional. PRD does not require it, but it's a maintenance hygiene win.

### P4-R29-N10 — §V.A's $A_{50}$ binomial SE quote is right but doesn't propagate to the $A_{95}$ bracket

**Section**: §V.A (line 459), Table VII (line 461).
**Severity**: MINOR.
**Quote (Table VII caption)**: "With $N_{\rm MC,inj}\!=\!100$ per amplitude, each tabulated $P$ carries a binomial standard error $\sqrt{P(1-P)/100}\!\leq\!0.05$ (e.g.\ $0.55\pm0.05$ at $A\!=\!0.75\%$)."
**Brutal verdict**: Excellent for $A_{50}$. But the abstract and §VI both quote "$A_{95}\in(1.0\%,1.5\%]$" as if the bracket itself were precise. With $\pm0.05$ binomial SE on $P=0.91$ at $A=1.0\%$, the 95% threshold could be at $A=1.0\%$ or just barely above; the bracket is itself uncertain. The paper acknowledges "$A_{95}$ is bracketed, not measured" — good — but doesn't quantify the bracket-edge uncertainty.
**Fix**: Add to §V.A: "The $P\!=\!0.91$ at $A\!=\!1.0\%$ carries $\sigma_P\!=\!0.029$, so the lower bracket edge is itself uncertain at the $\sim\!0.1\%$-amplitude level; a finer-grid recovery curve is in computation." This is already partially stated ("a finer-grid, higher-$N_{\rm inj}$ recovery curve is in computation"); the SE quantification would tighten it.

---

## NIT

- **P4-R29-T01** (Title, lines 63–68): 5-line title; PRD norm ≤2–3 lines. Suggest condensing to "A Null Real-Space Chirality Dipole and a Quantifiable Monopole-Mask Leakage Channel on 8.47M DESI Legacy Galaxies".
- **P4-R29-T02** (Abstract): single paragraph ~410 words after EXT1 disambiguation adds. Suggest breaking into two paragraphs without dropping disclaimers.
- **P4-R29-T03** ("to our knowledge" appears in abstract line 77 and §VI Conclusions line 488): one instance suffices.
- **P4-R29-T04** (`\artifact{}` underscore-break macro, lines 33–43): defensive coding present; run `/latex-audit` on v172 PDF before arXiv (standing protocol per CLAUDE.md).
- **P4-R29-T05** (`\paperRoundNote` defined line 59 but never used): dead `\newcommand`; either display under title or delete.
- **P4-R29-T06** (`\tableofcontents` line 83 on 22-page PRD): journals typically strip; consider removing for arXiv tarball.
- **P4-R29-T07** (Acknowledgments line 703 names "RunPod"): naming a commercial GPU vendor is unconventional in cosmology; stylistic only.

---

## Sweep coverage matrix

| Sweep | Coverage | Findings |
|-------|----------|----------|
| 1–14 (standard PRD sweeps) | Done | E01, E04, M01–M05, N01–N10, T01–T07 |
| 15 (abstract-last drift; new 500-MC/$10^4$ parenthetical + estimator-specific falsification) | Done | E04, M01, T02 — abstract is now content-correct but stylistically over-loaded |
| 16 (provenance; hash = stamp commit; artifact_crosscheck; no stale `f_sky_canonical`) | Done | E03 — hash is correct on substance, artifact_crosscheck WARN noted, no stale field-name hits |
| 17 (uncomputed claims; NSIDE=8 block-bootstrap justification footnote) | Done | E01 — single-scale brittleness is the dominant concern |
| 18 (standalone-reader) | Done | M03 (provenance audit log not citably referenced), N03–N05 (missing bib titles), T01 (long title), T02 (long abstract) |
| 19 (effect sizes) | Done | M05 (block-bootstrap $z\!=\!-18$ vs naive $z\!=\!-264$) — readers cannot distinguish the conventions from the abstract |

Additional EXT1 closure verifications (per R29 brief):
- Post-MASTER monopole-only null paragraph ($\sigma\!=\!+4.84$, ~12%) cited in §IV.D ✓ (line 417)
- Table IV caption "pre-MASTER diagnostic only" ✓ (line 406)
- NS gallery caption "edge-on": **FIGURE NOT EMBEDDED** — see ESSENTIAL E02
- Notation & Significance Conventions subsection: §III.A, three conventions all map consistently to their downstream uses ✓
- Training-count reconciliation: 25,790 source + flip augmentation → 26,616 augmented pool; 80/20 split = $n_{\rm train}\!=\!21,293$ + $n_{\rm val}\!=\!5,323$ = 26,616 ✓ arithmetic verified, narrative coherent. 826 augmented duplicates between source manifest (25,790) and augmented pool (26,616) ✓.
- SAMPLE+ESTIMATOR+NULL rule: HC-broad $N=949,584$ is the headline real-space-dipole sample throughout ✓

---

## Summary recommendation

**Verdict: MAJOR REVISIONS (close-but-not-yet).** The paper is publication-grade in scientific content and the EXT1 closure wave materially improved disambiguation. The headline real-space null ($+0.41\sigmaunit$) and the leakage-channel diagnostic are solid and well-supported. However:

1. **E01 (single-block-scale headline exclusion)** is a load-bearing methodological gap. The abstract's $z\!\approx\!-18$ comes from one block scale (NSIDE=8) with no sensitivity test at adjacent scales. The footnote concedes this. A 1–2 hour compute run at NSIDE∈{4,8,16} or equivalent spherical-cap scales would close it cleanly.

2. **E02 (NS gallery)** is a closure-ledger / paper-state mismatch. Either the figure goes into Fig.1 as a third panel or the closure ledger is updated to note the deferral.

3. **E03 (Data Availability hash)** is a provenance-tool false-positive but the closure ledger should document it so future restamps don't re-flag.

4. **E04 (twin meanings of $+3.64\sigmaunit$)** persists even after the abstract parenthetical. The Conclusions paragraph "Canonical-$N$ MASTER $\ell\!=\!1$ direct compute" still propagates the 500-MC value without explicit cross-ref to the $10^4$ recompute.

5. The five MAJOR findings (M01–M05) are all surface-textual and fixable in a single editorial pass; none requires recomputation.

6. The MINOR + NIT findings are predominantly stylistic.

**Effort**: 4–8h edits + 1–2h NSIDE-block sensitivity compute = single day. After E01–E04 + M01–M05 close, publishable PRD.

**Brutal coda**: substantively done on science. Editorial discipline at abstract+conclusions remains. EXT1 was effective but added abstract drift to consolidate. Do not arXiv with NSIDE=8 single-scale brittleness — any informed referee will ask E01.

**Counts**: ESSENTIAL 4 · MAJOR 5 · MINOR 10 · NIT 7 · TOTAL 26.










