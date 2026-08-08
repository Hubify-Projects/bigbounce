# INT API Review — P1B v1B.0.108 — gemini (gemini-3.1-pro-preview)
paper: P1B  version: v1B.0.108  model: gemini-3.1-pro-preview
provenance: commit=bbdc79db20500e6aa64f2d6f246120a01c53d2bb  pdf=arxiv/paper1b_mcmc_companion.pdf  sha256=a85f43f93ed7bb53e73304cd21fb0fe68ed0d6627103ccbcf970036d31d9a9fb
packet: key=8e2c24906ae75eba3ce6c9a1abb9edcb500999dfeee244a7e7f7aa08f96c0879  profile=JCAP-COMPUTATIONAL
modality: native-PDF (inline_data base64)
UTC: 2026-07-15T08:57:37.181513Z  |  latency: 30.0s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 30.0, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "gktXasmPCNSkmtkP-ZHesQc", "usage": {"candidatesTokenCount": 495, "promptTokenCount": 9995, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 115}, {"modality": "IMAGE", "tokenCount": 9880}], "serviceTier": "standard", "thoughtsTokenCount": 1940, "totalTokenCount": 12430}}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

(1) VERDICT: REJECT

(2) ISSUES:
1. [MAJOR] Standalone Scientific Significance and Scope (Sec. I): The manuscript explicitly states it does not derive or test any distinctive physical observable, does not implement new theoretical modules, and does not conduct a competitive sky detection. These analyses constitute routine pipeline cross-checks that belong as a supplementary appendix or repository attachment to the companion theoretical manuscript ("Paper I(a)"), rather than as an independent peer-reviewed JCAP research article.
2. [MAJOR] Lack of Methodological Novelty (Secs. III, IV, VI): To qualify as a standalone computational methods paper, a manuscript must introduce a novel algorithm, code, or statistical technique. Running stock CAMB/Cobaya to sample a standard $\Delta N_{\rm eff}$ extension, confirming that NaMaster mathematically inverts its own window function, and integrating a standard scalar field ODE using SciPy-equivalent tools are routine data-analysis tasks that do not represent publishable methodological advances.
3. [MAJOR] Triviality of the NaMaster Pipeline Check (Sec. IV): The pseudo-$C_\ell$ recovery check is performed on foreground-free, noise-only synthetic skies generated with standard `healpy` tools. Confirming that standard public software (NaMaster) recovers an injected signal with near-zero bias under ideal, synthetic conditions is effectively a software unit test. Without realistic foregrounds, anisotropic noise, or instrumental systematics, this section carries no scientific weight for evaluating real-sky cosmic birefringence pipelines.
4. [MAJOR] Over-simplified Summary Likelihood in ALP MCMC (Sec. VI): The spectator ALP consistency check relies on a single 1D Gaussian summary likelihood ($\beta = 0.342^\circ \pm 0.094^\circ$) rather than evaluating the actual $C_\ell^{EB}$ power spectra. Because this summary statistic strips away all scale-dependent spectral shape information, the resulting parameter estimation merely maps the geometric degeneracy of variables that can reproduce a single rotation amplitude, severely limiting its utility as a physical constraint on the ALP parameter space. 

(3) The central claim—that these numerical pipelines are reproducible and yield results consistent with standard $\Lambda$CDM or existing summary bounds—is technically supported by the computational artifacts, but the manuscript entirely lacks the original scientific findings or methodological novelty required for a standalone JCAP publication.