# INT API Review — P4 v1.0.252 — gemini (gemini-3.1-pro-preview)
paper: P4  version: v1.0.252  model: gemini-3.1-pro-preview
provenance: commit=40d99073618cb6ce5ae6f6c3410e52ef0a1685be  pdf=pipelines/p2_chirality/chirality_catalog_paper.pdf  sha256=a109f3d150ff02107bc10bc7dec576ad28b0157081b3e521da86e7c06ade3292
packet: key=eb7a7f0700e505805f0041e907f8e06c2e6b4159f35ad6b1df9e09025353adc0  profile=APJS-CATALOG-METHODS
modality: native-PDF (Files/media upload file_uri)
UTC: 2026-07-15T20:14:07.163432Z  |  latency: 43.3s  |  attempt: 1
provider_receipt: {"attempt": 1, "latency_seconds": 43.3, "modality": "native-PDF (Files/media upload file_uri)", "provider": "google", "provider_reported_cost": "unavailable", "request_id": "unavailable", "requested_model": "gemini-3.1-pro-preview", "resolved_model": "gemini-3.1-pro-preview", "response_id": "HepXat-dKN63qtsPr_LlEQ", "usage": {"candidatesTokenCount": 521, "promptTokenCount": 14671, "promptTokensDetails": [{"modality": "TEXT", "tokenCount": 111}, {"modality": "IMAGE", "tokenCount": 14560}], "serviceTier": "standard", "thoughtsTokenCount": 1813, "totalTokenCount": 17005}}
PARSED VERDICT: MINOR REVISIONS

======================================================================
RAW RESPONSE (verbatim):
======================================================================

**VERDICT:** MINOR REVISIONS

**ISSUES:**
1. **[MAJOR] Section 6.2 (Sensitivity and Dilution):** The classifier's binary CW/CCW agreement with human GZ1 labels is roughly 70%, which significantly dilutes any underlying physical dipole signal (the authors estimate a scalar dilution factor $g \approx 0.4$). Table 9 shows that an injected $A_p = 0.75\%$ dipole is only recovered at $\ge 3\sigma$ in 55% of the trials. While the authors appropriately acknowledge that the "spatially resolved physical confusion model remains open," the abstract's concluding sentence ("The parity-even morphology observable supports no primordial-parity bound") is slightly overstated. This should be revised in the abstract and conclusions to explicitly state that the capacity to rule out a physical dipole at the $\sim 1\%$ level is currently limited by the ViT classifier's accuracy and resulting signal dilution.
2. **[MINOR] Readability and Provenance Hashes:** The inclusion of raw SHA-256 hashes, exact byte counts, and long JSON artifact filenames directly within the narrative text (e.g., in Sections 2.2, 4.2, 4.4, and 6.2) severely disrupts the flow and readability of the manuscript. I recommend moving these strict provenance strings to the Data Availability section, footnotes, or a dedicated Appendix table, retaining only concise descriptive references in the main text.
3. **[MINOR] Section 3.4 (Test-Time Equivariant Averaging):** Equation 2 successfully and elegantly enforces perfect symmetry, removing the global machine-learned bias (as demonstrated by the drop from Catalog A to Catalog C in Table 4). However, enforcing output equivariance does not guarantee that the base model learned robust chirality features rather than relying on symmetric random noise for borderline, low-resolution cases. The text correctly notes that TTA suppresses raw argmax probabilities toward $\sim 0.5$ for borderline objects (Section 6, Table 13 T7 proxy); a brief addition explicitly clarifying that TTA trades directional classifier bias for symmetric prediction noise on indeterminate spirals would further strengthen the methodological discussion.

**Is the central claim supported?** 
The central claim that the observed galaxy chirality field exhibits no statistically significant real-space dipole after properly mitigating classifier bias via test-time equivariance is exceptionally well supported by the data and an exhaustive suite of diagnostic null tests.