# P4 v1.0.138/139 — Houston External Review (2026-06-01)

**Source:** Houston ran the P4 external-review prompt against three real frontier-model UIs (Grok heavy, Gemini 2.5 thinking, ChatGPT extended-thinking). This file is the verbatim copy of what Houston pasted back.

**Critical caveat discovered during ingestion:** ChatGPT explicitly says the reviewed PDF is **v1.0.138** dated May 26, 2026, NOT v1.0.139 dated May 28, 2026. Verified: the **live https://bigbounce.hubify.app/papers/chirality_catalog_paper.pdf is v1.0.138** (etag a3f11d16, May 26 stamp). The local repo (and Convex paper_versions table) tracks v1.0.139 (md5 65c652f4, May 28 stamp). The two cached deploy artifacts diverged. **Houston downloaded the LIVE stale-PDF, gave it to all 3 reviewers, so a substantial fraction of "BLOCKERs" in ChatGPT's review are STALE — they're complaints that v1.0.139 features (block-bootstrap, NSIDE=8 super-pixel, ∼18σ exclusion) aren't in the PDF. They ARE in v1.0.139; ChatGPT was just looking at v1.0.138.**

Verdicts at a glance:

| Reviewer | Verdict | Headline BLOCKERs |
|---|---|---|
| Grok-heavy | MINOR REVISIONS | 0 blockers, 1 minor (release-tag inconsistency) |
| Gemini-thinking | MAJOR REVISIONS | 3 blockers (covariance, rank-deficiency, dev-log prose) |
| ChatGPT-extended | REJECT | 9 blockers (mostly downstream of "PDF reviewed is v1.0.138 not v1.0.139") |

**Real new findings unique to this external review** (not stale from older R-rounds):

- Release-tag string `paper4-v1.0.134` still appears 5+ times in v1.0.139 .tex (abstract footer, footnotes 3 + Table II footnotes b/c, §IX, bibliography URL). Prior "release-tag scrub" was a literal no-op (replaced v1.0.134 with v1.0.134). **Grok-m1 / Gemini m1 — VERIFIED, needs real fix in v1.0.140.**
- Rank-deficiency in 9-template design (3 leg fractions + constant collinear). Paper notes "dipole vectors are orthogonal to the null subspace" but doesn't drop a baseline column or apply SVD projection. **Gemini-B2 — VERIFIED, needs real fix.**
- Dev-log / AI-review version-history prose still in main body (not just comment block). **Gemini-B3 / ChatGPT-B9 — VERIFIED, needs scrub.**
- Body Shamir citations: [2] vs [3] mix-up; PASJ methodology vs DESI Legacy MNRAS conflated. **ChatGPT-B8 — VERIFIED, real text fix.**
- 24-template interaction amplitudes (z=26.5 on DECaLS×[0.6,0.8)) need physical-driver discussion. **Gemini-M1 — VERIFIED, prose addition.**
- Hard-label dilution `1 + p_flip = 1.21` factor needs derivation. **Gemini-M2 — VERIFIED, ~2 lines of statistical proof.**
- Typo: "Catalog C row entry 3.4974 ± 0.0003" should be "0.4974 ± 0.0003". **Gemini-m2 — VERIFIED, typo.**
- Hemisphere null clarification (random-label vs systematics-preserving). **ChatGPT-M7 — VERIFIED.**
- Parity language "parity-violating chirality dipole" risk reintroducing confusion (abstract is OK, body still slips). **ChatGPT-M8 — partial.**
- Density-stratified-null wording (+3.80σ leaves residual not absorbed by density-only). **ChatGPT-M5 — language tune.**
- Imaging-leg proxy (25% of ℓ=1 amplitude) presented as evidence, ChatGPT says only as motivation. **ChatGPT-M6 — VERIFIED.**

**Findings that are STALE because reviewer read v1.0.138 not v1.0.139:**

- ChatGPT-B1 (PDF says v1.0.138, block-bootstrap absent) — STALE; v1.0.139 includes block-bootstrap; PDF mirror was stale on the site.
- ChatGPT-B2 (covariance correction needed) — STALE in v1.0.139.
- Gemini-B1 (same covariance critique) — STALE in v1.0.139.

**Findings of genuine residual difficulty (deferred or hard):**

- ChatGPT-B3 + B6: full morphology/PSF/depth template basis (b/a, fracdev, PSF FWHM, depth, shape r_eff). Requires DR8 sweep per-galaxy fields. **Pod-bound**; honest "deferred to v2 / follow-up" item, not closeable in this fire.
- ChatGPT-B4: mask-family inference / formal preregistration of hierarchy. Methodologically deep; needs a §10-§11 rewrite.
- ChatGPT-B5: null-model standardization. Same.
- ChatGPT-B7: classifier-uncertainty propagation into cosmological covariance. Needs soft-probability re-derivation throughout. **Multi-day work.**
- ChatGPT-M3: independent low-ℓ estimator (direct a_lm pseudo-deconvolution). New compute.

---

## Verbatim review text follows.

(See git log for the unedited paste from Houston.)
