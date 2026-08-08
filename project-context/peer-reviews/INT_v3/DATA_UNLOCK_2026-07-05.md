# DATA-UNLOCK — closing the pod/data-gated computes (2026-07-06)

Mission: close ALL remaining "pod/data-gated" computes across the bigbounce
papers with **real computation on real data only** — no fabrication. Houston
authorized any compute (local CPU, HuggingFace, RunPod).

Machine: local (Darwin, 244 GB free). No RunPod needed — every gated dataset
turned out to be reachable locally or from public/HF sources.

Summary board:

| Item | Paper | Status | Result |
|---|---|---|---|
| 1. DESI score-vs-z QSO enrichment | P3 | **CLOSED — data unlocked, honest MIXED result** | 100% TARGETID join; composition transfers, score-vs-z control does NOT replicate |
| 2. Edge-on-ISOLATED tie-break coherence | P4 | **CLOSED** | isotropic; family-wise joint p=0.49 |
| 3. Per-galaxy DR8 ℓ=1 residual attribution | P4 | **ALREADY CLOSED** (committed 2026-07-02) | +morphology 52.4%→53.0%, 47% remainder |
| 4. Heinrich 2023 SPHEREx Cov_B | P2 | **GENUINELY-UNAVAILABLE** | not published; only unvalidated WIP code |

---

## Item 1 — P3 DESI score-vs-z QSO high-z enrichment — CLOSED

**Gap (from `P3_realscience_2026-07-05.md`):** run the *identical* score-vs-z /
spectype-join test that was done for SDSS, but on the DESI stream — the exact
object of the recurring ChatGPT [MAJOR] §III A/§III B + Grok [MINOR] §IV A.
Named blocker: `desi_zall.parquet` (~28.4 M rows) "pod/HF-bound."

**Data resolution.** `desi_zall.parquet` is on **no** HF dataset (checked
`bamfai/bigbounce-anomaly-catalog`, `bamfai/galaxy-chirality-catalog`,
`bamfai/astra-desi-edr-mirror`, and the full `bamfai` org). But its provenance
file names the **public** DESI DR1 source:
`https://data.desi.lbl.gov/public/dr1/spectro/redux/iron/zcatalog/v1/zall-pix-iron.fits`
(22.37 GB, 28,425,963 rows). Downloaded it directly (public, no auth). The
committed `desi_dr1_anomalies.parquet` (195,829 rows) carries `tid` = the DESI
`TARGETID`, so the join is a **direct hash join on TARGETID** — no positional
match needed.

**Script:** `pipelines/p3_anomaly_engine/scripts/desi_qso_hiz_enrichment.py`
**Output:** `pipelines/p3_anomaly_engine/outputs/desi_qso_hiz_enrichment.json`
(FITS read via fitsio, columns TARGETID/SPECTYPE/Z/ZWARN/DELTACHI2/ZCAT_PRIMARY;
primary-coadd dedup on 28.4 M → 27.5 M unique targets.)

**Result (real, no fabrication) — the test ran; the outcome is honestly MIXED:**

*Join & composition (transfers cleanly to DESI):*
- **100% of the 195,790 anomalies join** to the DESI DR1 primary zcatalog on
  TARGETID (match_fraction = 1.000).
- SPECTYPE composition: **GALAXY 193,452 (98.8%), QSO 2,102 (1.07%), STAR 236
  (0.12%)** — the DESI anomaly-selected population is overwhelmingly real
  Redrock-classified spectroscopic objects (galaxies + a high-z QSO tail), **not
  sky/fiber/calibration artifacts**. This directly answers ChatGPT §III A's
  "are these scientifically meaningful objects?" on the DESI stream itself.
- QSO redshift structure (2,102 QSOs): median z = **3.81**; z>2: 1,504; z>4:
  769; z>6: **327**. The QSO tail is strongly high-z — approximate parent
  enrichment ~40× at z>4 (binomial p≈0), direction robust.

*Internal control (does NOT replicate the SDSS result — reported honestly):*
- The decisive SDSS statistic was "anomaly score is significantly HIGHER for
  z>4 QSOs" (SDSS: Mann-Whitney p=1e-103, Spearman +0.036). On DESI this
  **does NOT hold**: over the 2,102 QSOs, **Spearman(score, z) = −0.059
  (p=0.006)** — a slight *negative* trend — and Mann-Whitney finds the score is
  **not** higher for z>4 (median 5.39 vs 5.51; one-sided p=0.999). The
  secure-redshift subset (ZWARN==0, N=34 QSOs) is positive but statistically
  underpowered (Spearman +0.265, p=0.13; MW p=0.17).
- Caveat driving the difference: **only 0.1% (201/195,790) of DESI
  anomaly-matched spectra have ZWARN==0** — anomaly-selected spectra are
  outliers that Redrock fits poorly *by construction*, so the all-primaries QSO
  redshifts are largely ZWARN≠0 (less reliable), and the DESI anomaly `score`
  metric (range 5–25) is a different quantity from the SDSS `anomaly_score`
  (0–1). The score-vs-z monotonicity appears to be an SDSS-specific property of
  that detector/metric, not a universal one.

**Honest conclusion for the paper.** The DESI-stream test is now *runnable and
run* (data unlocked). Its transferable DESI result is the **composition/redshift
rebuttal** — the anomaly clusters are real Redrock objects (98.8% galaxies plus
327 z>6 QSO candidates), not artifacts. The **score-vs-z ranking claim should be
scoped to SDSS**; on the DESI anomaly score it does not replicate. Per the
research directive this narrows rather than closes: the DESI "real objects"
evidence stands independent of the score-monotonicity, which is the honest,
non-overclaimed statement.

---

## Item 2 — P4 edge-on-ISOLATED argmax tie-break spatial coherence — CLOSED

**Gap (Gemini v1.0.215 App E MAJOR, per `P4_residual_bound_edgeon_2026-07-05.md`):**
"a direct quantification of the spatial coherence of the argmax tie-break on
**edge-on** systems is required." The committed leg-resolved statistic
(`per_leg_confidence_familywise_maxstat.json`) covers the whole borderline band
(all axis ratios); the edge-on-**isolated** variant was flagged pod/data-gated
because it needs `class_eq + RA/Dec + b/a` jointly.

**Data resolution — NO pod needed.** `catalog_production.parquet` (HF cache,
`bamfai/galaxy-chirality-catalog`) has `class_eq/p_eq/ra/dec` but no b/a; the
committed `spiral_morphology_dr8.parquet` (3.20 M spirals, real DR8-sweep
ellipticities) supplies b/a. They join cleanly on
`dr8_id == f"{BRICKID}_{OBJID}"`. b/a computed as `(1-|e|)/(1+|e|)`,
`|e|=sqrt(e1²+e2²)` (deV shape if TYPE∈{DEV,COMP,SER} or FRACDEV≥0.5 else EXP),
identical to the committed `systematic_l1_forward_model_dr8morph.py`.

**Method:** identical dipole statistic + isotropic label-shuffle null as
`per_leg_confidence_familywise_maxstat.py`, restricted to edge-on (b/a<0.30)
borderline (p_eq∈[0.5,0.6]) galaxies — the systems where the CW/CCW argmax is
genuinely ambiguous. NSIDE=64, 2000 MC per cell, family-wise joint max|z| null.

**Script:** `pipelines/p2_chirality/scripts/edgeon_isolated_tiebreak_coherence.py`
**Output:** `pipelines/p2_chirality/outputs/canonical_provenance/edgeon_isolated_tiebreak_coherence.json`

**Result (real):** edge-on tie-break population N=295,170 (of 505,889 edge-on
spirals). Per-leg ℓ=1 dipole significance:

| Leg | N | A_obs | z vs isotropic null |
|---|---|---|---|
| BASS+MzLS | 80,258 | 0.02468 | **−0.23** |
| DECaLS | 154,793 | 0.01269 | **+0.71** |
| DES | 60,119 | 0.07275 | **+1.17** |
| ALL edge-on | 295,170 | 0.00920 | +1.32 (p_emp=0.096) |

**Family-wise joint p = 0.487** (obs max|z|=1.17 @ DES; null p99 max|z|=3.54).
**Verdict: EDGEON_TIEBREAK_ISOTROPIC.**

**Interpretation.** The edge-on-isolated argmax tie-break shows **no**
spatially-coherent ℓ=1 dipole in any leg — fully consistent with the isotropic
null. Notably, the leg-selective coherence seen in the *full* borderline band
(committed DECaLS z=+4.72) is **not** driven by edge-on systems: isolating to
edge-on (b/a<0.30) removes it (DECaLS z=+0.71). This is the strongest possible
answer to Gemini's App E concern — the argmax step on the ambiguous edge-on
population introduces no directional bias that could fake a dipole. Combined
with the whole band flowing into the σ=0.41 real-space Catalog-C dipole null,
the tie-break cannot reintroduce a cosmological dipole.

---

## Item 3 — P4 per-galaxy DR8 ℓ=1 residual attribution — ALREADY CLOSED (committed)

**Gap:** extend the imaging-only ℓ=1 forward model with per-galaxy DR8
morphology (b/a, fracdev, shape_r) and report the new explained fraction.

**Finding:** this was **already computed and committed** on 2026-07-02
(commits `903b2e9c`, `96b78b1d`):
`pipelines/p2_chirality/scripts/systematic_l1_forward_model_dr8morph.py` →
`pipelines/p2_chirality/outputs/systematic_l1_forward_model_dr8morph.json`.
It pulled REAL DR8-sweep morphology for all 3,201,160 spirals (100% matched),
built orthogonalized b/a / fracdev / shape_r pixel templates, and re-fit the
canonical-mask ℓ=1 residual.

**Result (committed, verified real — spiral_morphology_dr8.parquet is genuine
DR8 data: 3.20 M rows, b/a median 0.577, 15.8% edge-on):**
- imaging-only forward-modelled ℓ=1 fraction: **52.4%** (cos +0.835)
- imaging **+ DR8 morphology**: **53.0%** (cos +0.842), Δ = **+0.7 pts**
- un-modelled remainder: **47.0%** — a genuine open item
- verdict: `NO_MEANINGFUL_IMPROVEMENT` — per-galaxy morphology orthogonalized
  against imaging adds essentially nothing to the ℓ=1 projection.

No new compute needed; the data (`spiral_morphology_dr8.parquet`) was never
truly pod-gated. The honest 47% remainder is bounded cosmologically by Item-2's
sibling result (Target 1 of `P4_residual_bound_edgeon_2026-07-05.md`): its
coherent-cosmological content is < A_95 (1.0–1.5%) and nulled at σ=0.41.

---

## Item 4 — P2 Heinrich et al. 2023 SPHEREx bispectrum Cov_B — GENUINELY-UNAVAILABLE

**Gap (from `P2_joint_covariance_full_2026-07-05.md`):** to replace the proxy
ρ=−0.868 with the channel-native marginalized σ(f_NL), need the SPHEREx
multi-tracer galaxy-bispectrum noise covariance Cov_B(k₁,k₂,k₃) on the triangle
set from Heinrich, Doré & Krause 2023 (arXiv:2311.13082). The repo imports only
the scalar σ(f_NL^local)=0.7. The ∂B/∂A_GR shape derivative is already computed
locally and committed (`c12_gr_projection_dBdAgr_probe.py`).

**Availability hunt (evidence-backed).** Checked: arXiv abstract + full PDF
(incl. acknowledgments/footnotes), arXiv ancillary listing
(`/src/2311.13082/anc` → HTTP 404), the PRD published record, web search for
GitHub/GitLab/Zenodo/data-availability, the SPHEREx public-products repo, and
Chen Heinrich's full GitHub.

**Verdict: NOT PUBLICLY AVAILABLE as a downloadable data product.**
- The paper has **no** data-availability or code-availability statement, **no**
  arXiv ancillary files, **no** Zenodo DOI, **no** "available on request" note.
- Its only public-data footnote points to survey *inputs* (linear biases +
  number densities): `SPHEREx/Public-products/galaxy_density_v28_base_cbe.txt`
  — sensitivity/density text files, **zero** covariance/Fisher content.
- The generating **code** exists but is unusable as-is:
  `github.com/chenheinrich/SphereLikes` (branch `develop`) has
  `covariance/*_covariance.py`, `fisher/fisher_*.py`, `generate_covariance.py`
  — but last pushed **2021-08-26** (2+ yr before the paper), README labels the
  covariance/Fisher modules **"[Not validated; under construction]"**, no
  paper-matching tagged release, and the only precomputed `.npy` files are tiny
  unit-test *signal* fixtures (b3d at f_NL=0/1), **not** the per-triangle Cov_B
  on the paper's triangle set and **not** the σ=0.7 Fisher matrix.

**Confirmed citation:** Chen Heinrich, Olivier Doré, Elisabeth Krause,
"Measuring f_NL with the SPHEREx multitracer redshift-space bispectrum,"
Phys. Rev. D **109**, 123511 (2024); DOI 10.1103/PhysRevD.109.123511;
arXiv:2311.13082.

**Consequence for P2 (honest closure):** the channel-native marginalized
σ(f_NL) genuinely **cannot** be computed — it is gated on external data that
was never released. This is legitimate external-data-gating, not a deferral of
in-repo work. The existing honest closure stands: (a) ∂B/∂A_GR shape computed +
committed; (b) in-repo shape overlap confirms strong degeneracy |ρ|≈0.95,
bracketing the marginalized floor at ≈0.8–1.3σ; (c) the ρ=−0.868 c8 proxy
remains the best-available source-cited bound. "Cov_B not publicly available"
is now the *definitive* final answer for the paper.

---

## Proposed .tex edits (NOT applied)

### P3 — `pipelines/p3_anomaly_engine/paper3_draft.tex`, §sec:desi + §IV limitations
Replace the "pod-bound `desi_zall.parquet`" deferral with the honest DESI-stream
result. Suggested wording (numbers from `desi_qso_hiz_enrichment.json`):

> Joining the $195{,}790$ DESI DR1 anomalies to the public DESI DR1 primary
> redshift catalog on \texttt{TARGETID} ($100\%$ match) confirms the
> anomaly-selected population is astrophysically real rather than
> artifact-dominated: $98.8\%$ are Redrock-classified \textsc{galaxy},
> $1.07\%$ (\,$2{,}102$) \textsc{qso} and $0.12\%$ \textsc{star}, with the QSO
> tail strongly high-redshift (median $z=3.81$; $327$ at $z>6$). We note,
> however, that unlike the SDSS Path-C slice the DESI anomaly \emph{score} does
> not rise with QSO redshift (Spearman $\rho(S,z)=-0.06$, $p=6\times10^{-3}$
> over the $2{,}102$ QSOs); the score--redshift monotonicity is therefore an
> SDSS-specific property and we do not claim it for the DESI stream. The
> composition/redshift evidence (real objects, not sky/fiber) is the DESI
> result that transfers
> (\artifact{pipelines/p3\_anomaly\_engine/outputs/desi\_qso\_hiz\_enrichment.json}).

This scopes the score--z claim to SDSS (honest) while adding the DESI
composition rebuttal ChatGPT §III A asked for. Do NOT state a DESI score--z
enrichment; the real computation contradicts it.

### P4 — `pipelines/p2_chirality/chirality_catalog_paper.tex`, Appendix E
Extend Edit B of `P4_residual_bound_edgeon_2026-07-05.md`: append that the
**edge-on-isolated** (b/a<0.30) tie-break is directly measured and is
**spatially isotropic** (family-wise joint p=0.49; per-leg |z|<1.4, BASS+MzLS
−0.23 / DECaLS +0.71 / DES +1.17), so the leg-selective coherence in the full
borderline band is *not* driven by edge-on systems and the argmax step
introduces no directional bias.
Artifact: `\artifact{pipelines/p2_chirality/outputs/canonical_provenance/edgeon_isolated_tiebreak_coherence.json}`.
This removes the last pod-gated caveat in that appendix.

### P2 — `research/focused_paper_source_integration/...` (P2 systematics §)
Update the joint-covariance deferral to state definitively that the SPHEREx
multi-tracer bispectrum Cov_B of Heinrich et al. 2023 is **not publicly
available** (no ancillary/Zenodo/repo; generating code unvalidated & predates
the paper), so the channel-native σ_marg(f_NL) is external-data-gated; the
ρ=−0.868 proxy bound (σ_marg≈0.8–1.3σ band) stands as best-available.

---

**Integrity:** every number above is computed from real committed/public data
(DESI DR1 public zcatalog, HF-cached catalog_production, committed
spiral_morphology_dr8). No value invented. Item 4 is a documented
data-non-availability, evidenced by the exact places checked.
