# P4 v1.0.66 — Houston external 4-vendor adversarial review (CONSOLIDATED) — 2026-05-15

**Source**: Houston ran this round himself on ChatGPT/GPT-5, Gemini Deep Research, Grok (xAI), and Gemini, using the public PDF + public artifacts. Unanimous verdict across all 4 vendors: **NO-GO for arXiv release, NO-GO for journal submission.** Houston: "got blasted as totally no-go unpublishable by everyone."

## Verdict summary (cross-vendor)

| Vendor | Verdict | arXiv? | Journal? |
|---|---|---|---|
| ChatGPT/GPT-5 | REJECT-AND-RESUBMIT INTERNALLY | NO | NO |
| Gemini Deep Research | REJECT-AND-RESUBMIT INTERNALLY | NO | NO |
| Gemini | MAJOR REVISION | NO | NO |
| Grok | ACCEPT AS PREPRINT after 5 must-fix + MINOR REVISION for journal | NO (yet) | NO (yet) |

## 4-vendor CONVERGENT BLOCKERs (must close in v1.0.67 single bundled wave)

### B1 — LLM/agent text artifacts in manuscript (4-vendor convergent: Gemini-B1, Gemini-DR-G2, Grok-B6-implied via I-1, Grok-I-1, ChatGPT-B-6 + H-1 + I-4)

Section VII Conclusions and various footnotes contain raw text like:
- "Real cross-vendor adversarial-review (v1.0.53)"
- "The DeepSeek-B1 / DeepSeek-M3 deferral..."
- "A multi-vendor adversarial round on v1.0.51 (GPT-5.5, Gemini-2.5-Pro, Grok-4-fast...)"
- "v1.0.62 closure", "v1.0.55 analytic projection"

Gemini calls this "instant desk-reject at any serious journal." Gemini DR: "creates the impression that the manuscript is an unedited auto-generated log file." This is the single highest-rejection-risk item.

**Fix**: Scrub ENTIRELY from manuscript. Move to repository provenance only.

### B2 — Missing GitHub release tag `paper4-v1.0` (ChatGPT-G-1, Gemini-DR-G-1)

Paper cites `https://github.com/Hubify-Projects/bigbounce/releases/tag/paper4-v1.0` as permanent reproducibility anchor. Returns 404. Releases page shows no releases.

**Fix**: Create the tag AND release before submission, OR revise the claim. Add Zenodo DOI + commit SHA.

### B3 — Cited dipole summary artifact does NOT support headline (ChatGPT-B-4 + G-2)

Abstract: "canonical results file `pipelines/p2_chirality/outputs/dipole/summary.json`" — but that public JSON is the PRE-TTA 2.31σ run, not the headline 0.43σ post-TTA result. The headline number has no on-disk anchor.

**Fix**: Produce + commit a new canonical `catalog_c_post_tta_dipole_summary.json` with the 0.43σ run, exact input catalog hash, seed, mask, N, p-value. Update the paper path.

### B4 — HF dataset card contradicts paper architecture (ChatGPT-C-4, Gemini-DR-G2 implied)

Paper says ViT-Small + 2-fold horizontal-flip TTA. HF dataset card (https://huggingface.co/datasets/bamfai/galaxy-chirality-catalog) says ResNet-based + GalaxyMNIST training + D4 8-transform TTA.

**Fix**: Rewrite HF dataset card to match paper exactly. ViT-Small, GZ1+CE-ResNet+synthetic labels, 2-fold flip TTA.

### B5 — HF dataset viewer CastError (ChatGPT-G-3)

HF dataset viewer fails with schema CastError because actual columns (`p_cw_raw_x`, `class_raw_x`) don't match declared features (`p_cw_raw`, `class_raw`).

**Fix**: Either fix the HF dataset schema or upload a clean Parquet with column names matching the dataset card.

### B6 — Shamir 2022 comparison wrong (ChatGPT-A-1 + F-1, Gemini-DR-F-1, Gemini-F-1 minor)

Paper claims "~16× larger than Shamir 2022 spiral subset" implying ~200,000 Shamir spirals. But Shamir 2022 DESI Legacy (arXiv:2208.13866) abstract explicitly says "nearly 1.3×10⁶ spiral galaxies". The correct ratio is ~3.2M/1.3M ≈ 2.5×, not 16×.

**Fix**: Correct Shamir citation and replace 16× with verified 2.5×. Build a neutral comparison table covering Shamir 2012/2020/2022, Iye, Tadaki, Jia CE-ResNet, SpArcFiRe, this work.

### B7 — Independent GZ1 accuracy 69.91% buried under 93.7% internal (ChatGPT-C-1, Gemini-A-1, Gemini-DR-C-1, Grok-C-1)

Paper headlines 93.7% internal validation accuracy. Independent GZ1 cross-match agreement is only 69.91% (Cohen's κ=0.40). 67.6% of training is CE-ResNet pseudo-labels, so 93.7% is mostly distillation consistency, not external chirality accuracy.

**Fix**: Lead abstract/intro with 69.91% independent GZ1 agreement as primary external-validation metric. Demote 93.7% to "internal training/validation consistency".

### B8 — Hemisphere pLEE≤10⁻⁴ buried as "artifact" without formal monopole-leakage null (ChatGPT-B-1, Gemini-DR-B-2, Gemini-D-1, Grok-D-1)

Hemisphere asymmetry rejects random-label null at p_LEE≤10⁻⁴ (≥3.7σ under that null) but is dismissed as "systematic-floor artifact" without an explicit monopole+mask leakage null model. Multiple reviewers call this statistical circularity.

**Fix**: Run a controlled MC injecting only the observed 0.4974 monopole into the canonical mask (no dipole). Show that this generative null reproduces the observed +1.85σ canonical-mask ℓ=1 AND the 3.05σ hemisphere max-statistic. Establish pre-result estimator hierarchy: primary cosmological estimator → systematic diagnostic → artifact null.

### B9 — Estimator multiplicity / "headline" selection (ChatGPT-D-1, Gemini-DR-B-3, Grok-B-1)

Paper presents −0.122σ (subsample mask), +1.85σ (canonical mask), 0.43σ (real-space), 3.05σ (hemisphere), pLEE≤10⁻⁴ as different estimators on the same data and picks the most null one as "headline". Looks post-hoc.

**Fix**: Define one primary estimator + mask BEFORE results in a Methods pre-registration. Elevate the +1.85σ canonical-mask result to abstract alongside −0.122σ.

### B10 — Per-imaging-leg systematics deferred (ChatGPT-A-2 + E-1, Gemini-DR-A-2, Grok-E-1)

BASS+MzLS / DECaLS / DES have different cameras, PSFs, scan strategies. Paper checks RA/Dec slabs only. Per-leg analysis "deferred to a future revision". For a sub-percent chirality claim, this is unacceptable.

**Fix**: Add per-imaging-leg CW fraction + dipole table. Add PSF FWHM / ellipticity / depth / extinction / seeing quartile breakdowns.

### B11 — "Reject at any amplitude probed" overclaim (ChatGPT-B-2)

Abstract: "independently reject a primordial ℓ=1 dipole at any amplitude probed". Injection grid shows P(σ>2)=0.18 at A=0.5% (NOT a rejection). The phrase is not statistically justified.

**Fix**: Replace with: "No injected amplitude up to 0.5% met our pre-specified recovery criterion; therefore the empirical 50%-recovery threshold lies above 0.5%, and the measured catalog dipole remains below our operational detection threshold."

### B12 — Title overclaims given monopole + non-null diagnostics (Gemini-DR-B-1, Grok-H-1, ChatGPT-I-2)

Title: "No Evidence for Large-Scale Parity Violation". But paper contains 9.5σ global monopole + 3.05σ hemisphere + +1.85σ canonical ℓ=1 + low-ℓ bandpower excesses.

**Fix**: Soften title. Recommended: "A Survey-Scale Chirality Catalog of 8.47 Million Galaxies (3.2 Million Spirals): No Evidence for Large-Scale Parity-Violating **Dipoles** at Sub-Percent Sensitivity". Lead abstract with: catalog release + bias-audit + dipole null + acknowledged monopole.

## MAJOR convergent findings

### M1 — Abstract too long, version archaeology, looks like rebuttal log (3-vendor convergent)
Rewrite to ≤350 words. Drop file paths, version numbers, internal review log references.

### M2 — Training arithmetic 26,626 vs 26,636 (ChatGPT-C-2, Gemini-DR — note: components actually 6,637+17,999+2,000=26,636)
Correct the manifest count to 26,636 throughout OR explain the 10-image discrepancy.

### M3 — Table V stale snapshot 3,321,795 vs canonical 3,201,160 (4-vendor convergent: ChatGPT-A-7 + I-5, Gemini-I-1, Gemini-DR-I-1, Grok-I-1)
Recompute Table V at canonical 3,201,160 denominator. Delete the snapshot row.

### M4 — Fig 8 plots OLD 2.75σ data with caption admitting deprecation (Gemini-DR-D-4 + I-3)
Re-render Fig 8 using the corrected 6.48σ / 3,201,160 normalization. Never ship a paper where a main figure has a caption explaining why it's wrong.

### M5 — "All higher multipoles consistent with noise" contradicts Table IV +6.097σ ℓ=4 (ChatGPT-D-4, Gemini-DR-D-4)
Rewrite Fig 8 caption: "Several low-ℓ bandpowers are high under the random-label null and are attributed to monopole-mask leakage; they are not interpreted as parity dipoles."

### M6 — "Consistent with exact parity" Fig 5 caption contradicts 9.5σ monopole (ChatGPT-B-5, Gemini-DR-B-5)
Rewrite to: "close to 50/50 in absolute fraction but formally inconsistent with a 50/50 monopole under naive binomial errors; this monopole is not interpreted cosmologically."

### M7 — PSF ellipticity correlation r=0.042 explicitly fails strict bar (ChatGPT-E-2, Gemini-DR-E-1, Grok-E-1, Gemini-E-1)
Add 2D scatter/calibration plot of f_CW vs PSF e_1/e_2. Quantify dipole leakage in % amplitude.

### M8 — Edge-on 59.4% spiral classification too high (Gemini-DR-A-1, ChatGPT-A-5)
Add face-on clean primary sample (b/a > 0.5 or > 0.6) and rerun all headline statistics. Report full sample as secondary.

### M9 — Cross-paper bounce framing inflated for null result (ChatGPT-I-7, Gemini-DR-B-4, Grok-H-1)
Minimize cosmology framing. The result is a catalog + dipole null + bias-audit. Move bounce/parity-violation cosmology to one short caveated Discussion paragraph.

### M10 — Training GZ1 not excluded from independent GZ1 (ChatGPT-C-3)
Recompute external GZ1 metrics excluding training IDs + nearby positional matches.

### M11 — DR8 vs DR8/DR9 inconsistency between paper and explorer (ChatGPT-E-5)
Standardize to DR8 everywhere.

### M12 — Public Hubify SSOT links 404 (Gemini-DR-G-1 implied, internal known)
The "Hubify SSOT" links in paper Data Availability are 404; only the GitHub bigbounce repo and HF datasets resolve.

## Convergent strengths to preserve

1. 3.86× equivariance suppression of raw dipole (4-vendor agreement).
2. Honest reporting of 9.5σ monopole rather than hiding it.
3. Catalog scale (3.2M spirals, 8.47M total) is genuinely the largest.
4. The empirical >0.5% recovery threshold is honest (does not falsely claim rejection).
5. NaMaster MASTER mode-coupling deconvolution is a real methodological advance.
6. Including NOT_SPIRAL class prevents elliptical contamination.

## Priority closure order for v1.0.67

1. **B1 LLM scrub** (fastest, highest impact)
2. **B12 title softening** (fast)
3. **B11 "reject at any amplitude" reword** (fast)
4. **B7 lead with 69.91%** (fast)
5. **M1 abstract rewrite** (medium)
6. **M3 Table V recompute or delete snapshot** (medium)
7. **M2 training arithmetic fix** (fast)
8. **M5/M6 figure caption rewrites** (fast)
9. **B3 add canonical post-TTA dipole JSON** (medium — local script)
10. **B6 Shamir comparison fix** (fast text fix)
11. **B4 + B5 HF dataset card + schema** (Houston needs to push to HF; out of git scope)
12. **B2 GitHub release tag** (local but needs git tag push)
13. **B10 per-imaging-leg table** (requires data work)
14. **M7 PSF calibration plot** (figure work)
15. **B8 monopole+mask leakage null simulation** (compute-bound, may defer to v1.0.68)
16. **B9 estimator hierarchy pre-registration** (paper structure)

Tick-47-followup v1.0.67 should target: B1, B6, B7, B11, B12, M1, M2, M3, M5, M6, M9, M11 — all text-level fixes closable locally. B3 + B2 require artifact creation + git tag. B4 + B5 require HF push. B8 + B10 + M7 are compute-bound and may defer to v1.0.68.

Houston's standing memory: `feedback_take_critiques_seriously` (FULL HARD FIX), `feedback_default_hardest_path`, `feedback_no_questions_full_hard_fix`. Translate: close everything closable locally THIS WAVE. Defer only the genuinely-compute-bound items, on-record, with explicit reasoning.
