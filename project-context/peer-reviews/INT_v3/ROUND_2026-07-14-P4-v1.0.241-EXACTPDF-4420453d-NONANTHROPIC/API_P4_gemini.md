# INT API Review — P4 v1.0.241 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.241  model: gemini-3.1-pro-preview
provenance: commit=4420453d2ae3614bc08bd22eec9454df3b3546b5  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=d6eded1df29da5d2ccf6acb1e04277876289ae1547a1b8a3d2fda819ae7097f2
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-14T10:20:40.122788Z  |  latency: 73.7s  |  attempt: 1
usage: {"promptTokenCount": 18294, "candidatesTokenCount": 616, "totalTokenCount": 21198, "promptTokensDetails": [{"modality": "IMAGE", "tokenCount": 18200}, {"modality": "TEXT", "tokenCount": 94}], "thoughtsTokenCount": 2288, "serviceTier": "standard"}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: MINOR REVISIONS

ISSUES:
1. [MAJOR] Sections III/IV/Appendices (Formatting and Readability): The manuscript includes dozens of explicit, inline filepath references (e.g., `pipelines/p2_chirality/outputs/canonical_provenance/c12_r24conf_local_batch.json`). While the commitment to absolute computational reproducibility is highly commendable and sets a strong standard, placing these long strings directly in the main text violates standard *Physical Review D* formatting norms and severely disrupts the narrative flow. These must be moved to footnotes, references, or a dedicated "Reproducibility Artifacts" table in the appendix/Data Availability section, with the main text using concise identifiers (e.g., "Artifact c12" or reference brackets).
2. [MINOR] Section VI.A / Appendix D (Comparison with prior literature): The explanation contrasting the block-bootstrap WLS template fit ($z \approx -7.6$) with the physical amplitude bound ($1.36\sigma$ after the $g=0.398$ dilution factor) is logically sound but rhetorically dense. The author rightly clarifies this is an "amplitude-level tension" rather than a frequentist exclusion of Shamir's estimator. Please streamline the phrasing in the main text (and ensure the abstract reflects this nuance) so that casual readers do not accidentally misquote the observed-label $z \approx -7.6$ diagnostic as a definitive physical exclusion significance.
3. [MINOR] Section IV.C & IV.D (Harmonic vs. Real-Space estimators): The attribution of the $+7.28\sigma$ MASTER $\ell=1$ excess to monopole-mask leakage and patchy footprint systematics is rigorously proven. However, to prevent reader confusion, please add a brief, explicit sentence early in Section IV.C explaining exactly *why* the primary real-space dipole estimator is mathematically immune/protected from this specific geometric leakage that plagues the harmonic pseudo-$C_\ell$ estimator. 
4. [MINOR] Section II.B & VI.A (Pseudo-label independence): The author excellently bounds the CE-ResNet pseudo-label dependence using the independent Galaxy Zoo 1 (GZ1) human labels. However, because the GZ1-only null check has a much coarser sensitivity ceiling ($A_{50} \approx 3.4\%$) compared to the primary sample ($0.75\%$), the sub-percent limit intrinsically assumes the pseudo-labels do not harbor a hidden, sub-percent coherent dipole orthogonal to the tested survey templates. A single sentence explicitly restating this minor limitation in the main Conclusions (Section VII) would perfectly round out the otherwise stellar bias-hardening discussion.

The central claim of a null galaxy chirality dipole at sub-percent sensitivity is exceptionally well-supported by the rigorous implementation of equivariant test-time augmentation and an exhaustive, highly transparent suite of systematic controls.