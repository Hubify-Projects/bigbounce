# INT API Review — P1B v1B.0.112 — gemini (gemini-3.1-pro-preview)
paper: P1B  version: v1B.0.112  model: gemini-3.1-pro-preview
provenance: commit=72812cf63cc124ec0c203fc43f5dfde0f509953f  pdf=arxiv/paper1b_mcmc_companion.pdf  sha256=d420a7f5be48f1fa5f9fc1b2cf57206708881ffe29c782ea6cdf4d65eb20331c
packet: key=520b39108427fceb5c2918f551296a77b9be759c6531305d9fc32378760bd823  profile=JCAP-COMPUTATIONAL
modality: native-PDF (inline_data base64)
UTC: 2026-07-16T13:57:08.402401Z  |  latency: 28.9s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 28.9, "modality": "native-PDF (inline_data base64)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "NeNYauX5LL2dz7IPtYLzwQw", "usage": {"candidatesTokenCount": 455, "promptTokenCount": 10515, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 115}, {"modality": "IMAGE", "tokenCount": 10400}], "serviceTier": "standard", "thoughtsTokenCount": 1817, "totalTokenCount": 12787}}
PARSED VERDICT: REJECT

======================================================================
RAW RESPONSE (verbatim):
======================================================================

VERDICT: REJECT

ISSUES:
1. [MAJOR] Lack of Novel Scientific or Computational Contribution (Sections III, IV, VI). The manuscript presents a collection of standard analyses: a routine $\Lambda$CDM+$\Delta N_{\rm eff}$ MCMC parameter estimation using existing public codes (stock CAMB, Cobaya) on standard datasets, a basic synthetic pseudo-$C_\ell$ recovery test, and a generic ODE fit for a spectator ALP. These do not constitute a new computational method, a novel code release, or a new physical insight required for a standalone publication in JCAP.
2. [MAJOR] Unjustified Fragmentation of Research (Section I). The manuscript is explicitly framed as a repository of "reproducibility artifacts" and "pipeline checks" for a concurrent companion paper (Paper I(a)). Routine numerical cross-checks, MCMC validation runs, and software unit tests belong in the appendices or supplementary material of the primary science paper, not as a disjointed standalone article. 
3. [MAJOR] Triviality of the NaMaster Validation (Section IV). The synthetic CMB $E-B$ recovery test explicitly excludes realistic astrophysical and instrumental complications, such as galactic foregrounds, instrumental beams, calibration degeneracies, and anisotropic noise. Recovering an injected signal in this idealized, foreground-free synthetic setup is a basic software unit test of the NaMaster package, not a competitive or publishable methodological result.
4. [MAJOR] Disconnect Between Theoretical Motivation and Execution (Sections I, III, VI). The manuscript extensively discusses Einstein-Cartan-Holst (ECH) gravity and spin-torsion, yet explicitly admits that the $\Delta N_{\rm eff}$ proxy run "does not verify the spin-torsion theory module itself" (lacking a torsion-modified Boltzmann solver) and that the ALP model "has no ECH-specific content." The computational exercises are entirely generic and fail to actually test or constrain the theoretical framework used to motivate them.

The central claim that these three computational exercises are technically reproducible is supported, but the analyses themselves are routine, lack novel methodological or scientific value, and represent an unjustified fragmentation of work that should be integrated into the companion paper.