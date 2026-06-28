# EXTDB2 P4 ChatGPT — chat: https://chatgpt.com/c/6a40ecf1-fd44-83e8-afda-98afbe430794

Provider: ChatGPT (Instant tier)
PDF md5: 342597924827541af63ee00bff1aa1af
Harvested: 2026-06-28

---

Recommendation: MINOR REVISIONS

The paper is scientifically valuable and largely publication-ready: it releases a major 8.47M-galaxy chirality catalog, correctly downgrades the headline real-space dipole to a null result, and is unusually transparent about systematics. I do not see a blocker requiring rejection or major rework, but several presentation and methodology issues should be fixed before publication.

BLOCKERS
None.

MAJORS

M1. The abstract is overloaded and risks confusing the primary result. The abstract mixes the primary +0.41σ real-space null, label-shuffle checks, MASTER residuals, 500-MC vs 10⁴-MC distinctions, harmonic completeness, monopole leakage, and falsification thresholds in one dense paragraph. Authors should restructure: catalog, primary estimator/result, systematics finding, sensitivity/falsification, data release.

M2. The "largest chirality-labeled catalog to date" claim needs a careful qualifier. Only 3.20M objects are spiral-labeled CW/CCW, and the training set is substantially CE-ResNet-derived. Should explicitly say "largest catalog with this three-class ViT/TTA labeling and 3.2M spiral labels," or justify the broader "largest" claim against all previous public chirality catalogs.

M3. The training-label dependence on CE-ResNet weakens independence more than the text's first-pass framing suggests. 66.5% of training labels derive from CE-ResNet and validation partly measures agreement with it. Should more prominently separate "new independent information" from "relabeling/extension using a CE-ResNet-influenced teacher." Not fatal, but must be explicit in Introduction and Comparison sections.

M4. The confidence threshold peq > 0.6 needs cleaner pre-registration/provenance language. The primary result depends on suppressing the low-confidence tail where the unthresholded dipole is ~4.2–4.4σ. Should provide a short, auditable provenance statement explaining when/why peq > 0.6 was fixed before seeing the final dipole result.

M5. The MASTER residual discussion remains too intricate for the main text. The paper repeatedly says the harmonic channel is diagnostic, not cosmological, but then gives many large σ values: +3.64σ, +7.28σ, +7.93σ, +7.13σ. Should add one compact "estimator map" figure/table showing which result is primary, which is diagnostic, what field/mask/null each uses, and which conclusions are allowed from each.

MINORS

m1. External-truth accuracy (GZ1 chirality accuracy only 69.91% with κ=0.40) should be stated earlier and more plainly near the catalog headline.

m2. "Sub-percent sensitivity" phrasing needs consistent qualification: observed-space A50≈0.75% is sub-percent, but true-amplitude correction using g=2a−1 gives ~1.88%. Specify "observed-space estimator amplitude" whenever "sub-percent" is used.

m3. Abstract's statement about disfavoring clean cosmological dipole should add "within the adopted nuisance-template and block-bootstrap model" as qualifier.

m4. The raw vs equivariant comparison (Figure 7) should directly state: raw classifier bias plus footprint modulation creates a false dipole; TTA removes the real-space dipole; remaining harmonic residual is systematics-diagnostic.

m5. Data-availability section says Zenodo DOI not yet minted. Should be replaced with a persistent DOI or explicitly state that DOI minting will occur before acceptance.

m6. Edge-on contamination treatment is incomplete. The 65.7% edge-on CW/CCW assignment is potentially important. Authors should either include the promised axis-ratio cross-match or label the 10–15% Neff reduction as an estimate requiring confirmation.

m7. Paper alternates between fCW deviations and Ap units. Tables/figures should visibly label "Ap units" or "fCW units" every time.

Strengths

1. The catalog scale is genuinely impressive: 8,474,531 galaxies and 3,201,160 spiral labels.
2. The paper is unusually transparent about systematics, including the monopole-mask leakage channel and low-confidence-tail behavior.
3. The primary scientific conclusion is appropriately conservative: the real-space chirality dipole is null at +0.41σ.
4. Equivariant TTA is a strong methodological improvement and the raw-vs-equivariant comparison clearly demonstrates why it matters.
5. The release of catalog, model, code, and provenance artifacts makes the work valuable as a community resource.
