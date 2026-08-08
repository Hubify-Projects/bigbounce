# INT API Review — P4 v1.0.242 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.242  model: gemini-3.1-pro-preview
provenance: commit=97b9cb7f  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=8c9df3dac29459f568619bcb53daa7b9acc54e0a80bb8cb776f1277aa35a76c4
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-14T11:54:05.032536Z  |  latency: 75.0s  |  attempt: 1
usage: {"promptTokenCount": 13838, "candidatesTokenCount": 1247, "totalTokenCount": 18701, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 318}, {"modality": "IMAGE", "tokenCount": 13520}], "thoughtsTokenCount": 3616, "serviceTier": "standard"}
PARSED VERDICT: ACCEPT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

This is an expert referee report for *Physical Review D* on the manuscript "An Observed-Label Chirality-Dipole Null in 949,584 High-Confidence DESI Spirals and a Public 8.5-Million-Galaxy Catalog" (v1.0.242).

### 1. VERDICT
**ACCEPT**

This manuscript is exceptionally rigorous, transparent, and methodologically sound. It represents a substantial step forward for the field of galaxy chirality analysis. The author goes to extraordinary lengths to ensure reproducibility, clearly documenting all code artifacts, null procedures, and explicit limitations (the "open gates"). The application of test-time augmentation (TTA) to enforce flip-equivariance is exactly what this subfield has needed to address raw classifier bias. 

### 2. NUMBERED ISSUES
There are no major defects. The paper is publication-ready. I provide only a few [MINOR] non-blocking observations for the author’s consideration prior to final typesetting:

1. **[MINOR] Presentation of Artifact Hashes:** The heavy inline use of raw repository JSON paths (e.g., `pipelines/p2_chirality/...`) is excellent for reproducibility but slightly disrupts the reading flow in a traditional two-column PRD layout. *Optional fix:* Consider moving some of the longest path strings into footnote references or a dedicated consolidated artifact table in the appendix, leaving only the short SHA prefixes or descriptive tags in the main text. 
2. **[MINOR] Table IV and Text Precision Match:** In Table IV and Section IV.B, the raw Tier A fraction is given as $0.507879(274)$ with an excess of $+0.788\%$, and the significance is cited as $+28.72\sigma$. A strict recomputation of the binomial variance $\sqrt{f(1-f)/N}$ for $N=3,321,795$ yields $\sigma \approx 0.0002742$. Dividing the absolute deviation $(0.507879 - 0.5 = 0.007879)$ by this $\sigma$ yields exactly $28.73\sigma$. The text quotes $28.72\sigma$. *Optional fix:* This is a trivial rounding/truncation artifact in the trailing decimal and does not affect the science, but the author may wish to synchronize the float truncation in the final script execution.
3. **[MINOR] Eq. 1 Architecture Typo Check:** In Eq. 1, the layer sequence is denoted as `LayerNorm -> 384->512 (GELU, d=0.3) -> 512->256...`. The ViT-Small standard embedding dimension is usually 384. This transition implies the ML head expands 384 to 512, then down to 256. *Optional fix:* No fix required assuming this accurately reflects the custom PyTorch classification head implemented, but it is worth a quick visual check to ensure the documented dimensions exactly match the `bamfai/galaxy-chirality-v2` checkpoint architecture. 

### 3. SUPPORT FOR THE NARROW CENTRAL CLAIM
**Fully Supported.** 
The central claim—that the observed classifier-label chirality dipole in the $N=949,584$ high-confidence sample is consistent with zero ($z = +0.41\sigma$, rank $p=0.31$)—is comprehensively backed by the evidence. 

I have independently recomputed and verified the load-bearing summary statistics derived from the text's integer counts:
* The Catalog C global CW fraction $f_{CW} = 1,592,107 / 3,201,160 = 0.497353$ and its strict binomial uncertainty ($0.0002795$) precisely match the reported $-9.47\sigma$ suppression.
* The Fisher ideal information limits ($\sigma(A) = 9.7 \times 10^{-4}$ for the full sample and $1.78 \times 10^{-3}$ for the HC sample) check out perfectly.
* The 3-class GZ1 accuracy ($58.71\%$) and the conditional spiral-only accuracy ($69.91\%$) are correctly derived from the confusion matrix in Table XIII.
* The asymmetric confusion transfer factors ($s_{CW} = 0.674, s_{CCW} = 0.724$) yield a dilution slope $g_{eff} = 0.398$, exactly tracking the symmetric $2a-1$ approximation for near-balanced fields.

Most importantly, the paper successfully demonstrates how an uncorrected classifier monopole (even at $\sim 0.79\%$) couples to the patchy masked sky to produce highly significant, entirely spurious dipoles (the $+6.48\sigma$ raw pre-MASTER artifact). By neutralizing this with $Z_2$ TTA and utilizing a monopole-only generative null, the author provides a masterclass in separating footprint-coupled systematics from primordial signals. 

### 4. FRESH VERIFIED MAJOR BLOCKERS
**None.** 
The author has meticulously fenced off the limits of the study. By explicitly declaring the absence of a spatially varying physical transfer function (DP4-15), matched-footprint independent estimators (DP4-16), joint covariance likelihoods (DP4-17), and preregistration (DP4-21), the paper guarantees it does not overclaim. There are no hidden physical-parity bounds masquerading as calibrated cosmological exclusions. The work perfectly achieves its stated goal: delivering a massive, bias-hardened, null-consistent observational catalog.