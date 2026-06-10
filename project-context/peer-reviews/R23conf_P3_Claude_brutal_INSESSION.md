# P3 R23conf — Claude brutal-referee
**Reviewer**: `Claude_brutal`
**Model**: `claude (in-session, subscription)`
**Input PDF**: `site/public/papers/paper3_anomaly_catalog_v3.1.80.pdf` md5=03f05e26 pages=23
**Input format**: NATIVE PDF (in-session Read) + pass-2 self-critique
---

Referee stance: brutal PRD/astro-ph.IM. All 23 pages read natively in three chunks; every figure and table visually inspected; all headline arithmetic recomputed by hand.

## Findings

### P3-E1 — "7.9% improvement" is arithmetically inconsistent with its own σ values (abstract headline)
- **Location**: Abstract; §V A b (p.12); §VI C limitation (4) (p.15); Conclusions item 5 (p.16).
- **Problem**: The paper states σ(f_NL) = 8.14 against the single-tracer baseline σ(f_NL)^std = 8.98 and calls this a "7.9% improvement." (8.98 − 8.14)/8.98 = **9.4%**, not 7.9%. The paper's own definition is fixed by the fixed-α reference: 8.98 → 8.43 is reported as 6.1%, and (8.98 − 8.43)/8.98 = 6.12% ✓ — so the same definition applied to 8.14 must give 9.4%. The σ = 8.14 central value itself is correct (1/σ² = 1/8.98² + 0.0747·0.19² → 8.139 ✓), as is the envelope [3.92, 8.98]. The stray "7.9%" appears to be contamination from the **unrelated** Appendix C dense-tracer-limit figure "+7.93%" ((12.72 − 11.71)/12.72 = 7.94%), which lives on a different internal normalization (16.85/11.71 axis, explicitly disclosed as not comparable to the §V axis). Table VII linear scaling at α = 0.19 would give ~7.7%, also not 7.9%, and §V uses the quadratic form (8.14), not the linear table.
- **Required fix**: Change "7.9%" to "9.4%" (or "~9%") at all four sites, OR explicitly define the improvement metric used if 7.9% is intended under some other convention. Verify no collision wording remains with the Appendix C +7.93% dense-limit number — having 7.9% and 7.93% mean two different things in the same paper is a referee trap even after the fix.

### P3-M1 — Fig. 2 caption contradicts its own burned-in title and legend on ACT inclusion
- **Location**: Fig. 2 (p.5), burned-in title "Spatial distribution of all 319,443 anomalies across 8 archives"; legend includes ACT DR6 (brown); caption sentence "ACT DR6 is quarantined and excluded."
- **Problem**: 319,443 is the ACT-inclusive cross-transfer total (Table I: "Total (cross-transfer, ACT-incl.)"), the title says "8 archives," and ACT DR6 appears in the legend with plotted markers — yet the caption asserts ACT is "excluded." Either the map plots ACT points (caption wrong) or it doesn't (title/count/legend wrong). As printed, the figure is internally contradictory.
- **Required fix**: Reword caption to "ACT DR6 points are shown for completeness but are formally quarantined (App. F) and contribute zero objects to the Path-C headline," or regenerate the figure without ACT and retitle with the 7-archive count.

### P3-M2 — Fig. 4 sample size (77,905) contradicts body text (top-50,000)
- **Location**: §III C (p.6): "UMAP/HDBSCAN clustering of the top-50,000 cross-transfer anomalies yields 14 HDBSCAN clusters (99.4% of objects clustered)" vs. Fig. 4 (p.7) burned-in title and caption: "the 77,905 SDSS DR18 anomalies … 14 clusters, 99.4% clustered."
- **Problem**: The same 14-cluster/99.4% result is attributed to two different input sets (50,000 vs 77,905). One of the two numbers is stale.
- **Required fix**: State the actual UMAP/HDBSCAN input set once, consistently, in both body and caption; if the embedding was run on 50k and the figure overlays all 77,905, say so explicitly.

### P3-M3 — Fig. 8 panels (a,b): scores 3.2 / 2.8 are below every disclosed catalog threshold
- **Location**: Fig. 8 (p.13), Match 1 "Known QSO at z ≈ 1.55", burned-in Score = 3.2 (DESI), Score = 2.8 (SDSS); §IV C lists this object as one of the three DESI×SDSS cross-survey *anomaly* matches.
- **Problem**: Cross-survey matches are by construction intersections of the two anomaly catalogs. DESI membership requires S > 5.0 (canonical cut) and SDSS cross-transfer membership requires S > 5 (or native S ≥ 0.1060). A DESI score of 3.2 is below the DESI catalog threshold on the only DESI axis defined in the paper, so this object cannot be a member of the 195,829 DESI anomaly set as displayed. The caption carefully discloses the score axis for the TIC 374313355 panel (49.5 = cross-transfer axis) but is silent on which axis panels (a,b) use and how sub-threshold scores are compatible with catalog membership.
- **Required fix**: State the score axis for every panel and reconcile membership (e.g., if Match 1 entered via a different selection or the burned-in scores are per-arm/native values, say so); otherwise this is a counterexample to the catalog's own selection rule sitting in a headline figure.

### P3-M4 — "Gold-tier" / "Gold+Silver" populations are used with three different counts and no in-paper definition
- **Location**: Fig. 1 caption (p.2): "83 gold-tier anomalies (cyan stars)"; §V A b (p.12): "1,122-object Gold+Silver subset"; Appendix C.1 (p.17): gold n̄ = 8.5×10⁻⁶, silver 4.5×10⁻⁵ (Mpc/h)⁻³.
- **Problem**: The gold/silver tiers carry a key cosmology result (α_GS = +1.83 ± 2.03 → σ(f_NL)^GS = 1.95 central) yet are never defined in the paper: no selection criterion, no score cut, no count reconciliation between the 83 (Fig. 1), the 1,122 (§V), and the Appendix C number densities. A referee cannot check the Gold+Silver forecast without the tier definition.
- **Required fix**: Add a short definition (selection criteria + counts for gold and silver separately) at first use, and reconcile 83 vs 1,122 explicitly (e.g., 83 = gold only, DESI 500k-sample subset shown in Fig. 1 vs 1,122 = gold+silver full catalog — whatever the truth is, print it).

### P3-m1 — Fig. 3 caption: "twelve orders of magnitude" is ~10.6
- **Location**: Fig. 3 caption (p.6).
- **Problem**: From S = 5 to 1.9×10¹¹ is a factor 3.8×10¹⁰ ≈ 10.6 dex, not 12.
- **Required fix**: "more than ten orders of magnitude" (or count from the distribution minimum if 12 is intended, and say so).

### P3-m2 — §III A contains a near-verbatim duplicated paragraph
- **Location**: p.4, end of col. 1 vs col. 2: the ~20× galaxy/QSO rate (0.75% vs 0.037%), anomaly z ~ 0.75 vs 0.93, and the three top scores 25.2/24.6/24.5 are stated twice within the same subsection.
- **Required fix**: Delete one copy.

### P3-m3 — Broken/odd internal cross-reference "Sections II–II D"
- **Location**: p.2, col. 1 ("Sections II–II D describe the method").
- **Required fix**: Should read "Sections II A–II D" (or just "Section II").

### P3-m4 — Limitation (6) "no upper/lower-bound status" contradicts the quoted Wilson interval
- **Location**: §VI C (6) (p.15) vs §IV A (p.10): "Wilson 68% binomial interval 17.8 ± 1.2%."
- **Problem**: The paper does give a sampling interval on the 17.8% top-1,000 estimate. What it lacks is an extrapolation bound to the full catalog. The limitation's wording overstates.
- **Required fix**: Reword to "binomial sampling interval only (±1.2%); no bound on the full-catalog extrapolation, which is empirically untested."

### P3-m5 — Planck patch bookkeeping: 20,000 catalog patches vs 2×10⁵ training patches vs "200K-patch full re-score"
- **Location**: §III F (p.7) "Input: 20,000 SMICA CMB map patches"; §II D step 2 / Table V footnote † (p.18): trained on 2×10⁵ masked patches; "The 200K-patch full re-score took 25.3 s … source of the ~8,000 patches/s throughput entry."
- **Problem**: The training pool (200K) is 10× the scored catalog input (20K) and the throughput entry is derived from re-scoring the 200K pool, not the catalog. Nowhere is the relationship (overlapping tiles? augmentation? subsetting?) explained, and Table I N_total = 20,000.
- **Required fix**: One sentence reconciling the 200K training/re-score pool with the 20,000-patch catalog tier.

### P3-m6 — Fig. 12 panel label "[Cool Dwarf]" vs caption "Cool/unusual star"
- **Location**: Fig. 12 (p.20), row 2 panel 4.
- **Required fix**: Align label and caption taxonomy names. (Otherwise Fig. 12 caption-panel match is clean: 10 panels = 10 caption families in order; no undefined burned-in scores; the raw-score omission is explicitly disclosed — good.)

### P3-m7 — Figure/layout polish
- **Location**: Fig. 3 left panel (p.6): the three top-score labels overprint as "2425.2…" smudge; p.20 is ~2/3 whitespace around Fig. 12 and p.21 carries a single orphan paragraph on an otherwise blank page.
- **Required fix**: Nudge Fig. 3 annotation offsets; let Fig. 12 float earlier or resize to recover p.21.

### P3-N1 — Fig. 9 (right): total AI-tracer count never stated
- **Location**: Fig. 9 right panel (p.14): per-bin counts (174, 61, 2,645, 11,653, ~14.7k, 9,328, 1,350) sum to ~40k.
- **Note**: The text defines the 5,384 QSO-candidate bias sample and the 195,829 DESI catalog, but never the ~40k multi-tracer set whose per-bin counts drive the reference Fisher. State the selection and total in the caption or §V.

### P3-N2 — Fig. 10 caption NEOWISE mask latitudes {85°, 82°, 80.5°} vs §III H's 80° mask
- **Note**: Presumably injection latitudes for the 1000/1000 recovery, not the catalog mask cut (|b_ecl| < 80°). One clarifying clause would remove the apparent mismatch.

## Explicit all-clear (areas scrutinized and verified clean)

- **Count consistency**: 195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493 ✓; − 10,213 dedup (637 clusters + 9,576 intra-survey ✓) = 378,280 ✓; 378,080 + 200 stratification ✓; ~265k = 378,280 − 113,342 = 264,938 ✓; ACT arithmetic 388,693→388,493 and 378,480→378,280 ✓; Table I rates (0.87/3.38/0.39/1.01%) all recompute ✓; Table II sums to exactly 77,905 with correct fractions ✓.
- **4.05% continuity-slice relabel**: consistent at every site — Table I footnote ♥, §II B b, §III C (77,905/1,925,279 = 4.046%; S ≥ 0.1060; "sized to equal the cross-transfer count"); top-1% proper = 19,253 at S ≥ 0.2051 = 1.0% ✓; "only 12 sources at S > 5" consistent in both locations ✓.
- **Dedup radius sweep**: 378,604/378,280/378,145 at 3″/5″/7″; max deviation from canonical 324/378,280 = 0.0857% ✓ matches "0.086%"; compressions 2.55/2.63/2.66% all recompute ✓.
- **NANOGrav arithmetic**: (3.0−2.567)/0.382 = 1.134σ ✓; (4.33−2.567)/0.382 = 4.615σ ✓; B_MB/SMBHB = 3.23/4.52×10⁻⁴ = 7.15×10³ ✓; log₁₀B = 3.85 ✓; quantile CI 2.591+0.291/−0.287 → [2.304, 2.882] ✓; ESS 320,000/τ≈58 ≈ 5,500 ✓; Eq. (E1) is the correct free-spectrum power-law log-form ✓; Savage–Dickey usage (posterior/uniform-prior density at nested point) is legitimate; non-detection framing explicit ✓.
- **Fisher/Landy–Szalay arithmetic** (apart from E1's % label): σ(0.19) = 8.14 ✓; envelope [3.92, 8.98] from α ∈ [−0.46, +0.84] with max at α = 0 ✓; 0.29σ, 0.06σ, 95% CI [−1.08, +1.46] ✓; GS subset σ = 1.95 and [0.94, 8.98] ✓; Table VII row arithmetic ✓.
- **Scale-claim baselines**: 378,080/2,685 = 140.8 ≈ 141× and 195,829/2,685 = 72.9 ≈ 73×, both against Liang et al. [11] (2,685 anomalies, 1.07% of ~250k ✓), with the like-for-like caveat properly attached ✓; 37.3M ✓; ~90× sample-size ratio ✓.
- **eROSITA reframe**: 284/298 = 95.3% now consistently presented as descriptive shared-latent overlap (§III E, Table I footnote §, Table IV (f)) — no residual enrichment language found anywhere ✓.
- **LAMOST lesson framing, release-status ("public with the arXiv posting"), ACT quarantine**: implemented as calibrated; internally consistent across abstract, §III D, §VI A, Table I ♠, Data availability, App. F ✓.
- **SIMBAD/novelty scoping**: 235/400 = 58.8% ✓; 17.8% (178/1,000, Wilson ±1.2% ✓) consistently quoted as the discovery-rate figure with top-1,000 stratum scoping in abstract, §IV A, Fig. 6 caption, Conclusions ✓ (m4 wording nit aside).
- **References**: spot-checked [11], [18], [33], [35], [37] — plausible and correctly deployed.

## Summary recommendation

**Major revision — but a short one.** The catalog bookkeeping, dedup sweep, NANOGrav arithmetic, and the eROSITA/LAMOST/release-status reframes are in genuinely good shape; the count web (378,280/378,080/388,493/~265k/4.05%) survives full recomputation, which is rare at this scale. What blocks acceptance is one wrong headline percentage in the abstract (E1: 7.9% should be 9.4% by the paper's own definition) and four figure-level internal contradictions (M1–M4) of exactly the kind PRD referees seize on: a caption that denies what its own legend shows, two different sample sizes for one clustering result, sub-threshold scores in a cross-match gallery, and an undefined "gold tier" carrying a cosmology forecast. All are fixable in a single editing pass with no new computation except verifying the M3 score axes. Fix E1 + M1–M4, sweep the m-list, and this is acceptable.

*Pass-2 self-critique applied: verified the 6.1% definition anchor before asserting E1; confirmed Fig. 11's internal normalization disclosure exonerates the 7.93%/12.72/11.71 numbers themselves; confirmed the burned-in Fig. 4 "score > 5.0" and Fig. 8 TIC axis disclosures are already calibrated and not double-flagged; dropped a contemplated flag on Table V's withdrawn 10.6 s entry (transparent and self-correcting as written).*
